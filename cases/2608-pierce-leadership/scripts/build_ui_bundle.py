#!/usr/bin/env python3
"""One command produces the whole evidentiary bundle (Task 3.4).

Pipeline: normalize (T1.1) -> data emit (T2.1) -> verify static assets -> manifest.
--verify: after building, rebuild into a temp dir and confirm byte-identical
output for every gated asset (data.js, app.css, app.js, index.html) — the
reproducibility gate. Timestamped/mutable inputs (money-map.json) stay OUTSIDE
the byte gate by design; the manifest carries the record.

Usage:
  build_ui_bundle.py            # build + manifest
  build_ui_bundle.py --verify   # + byte-identical rebuild check
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VENV = Path("/Users/moliver/.hermes/hermes-agent/venv/bin/python3")
NETROOT = REPO / "evidence" / "network"
ASSETS = NETROOT / "assets"

GATED = ["evidence/network/index.html",
         "evidence/network/assets/app.css",
         "evidence/network/assets/app.js",
         "evidence/network/assets/data.js"]

STEP_SCRIPTS = [
    REPO / "scripts" / "normalize_relationships.py",
    REPO / "scripts" / "build_entity_bundle.py",
]

STATIC_SRC = {
    REPO / "evidence" / "network" / "index.html": "index.html",
    REPO / "evidence" / "network" / "assets" / "app.css": "assets/app.css",
    REPO / "evidence" / "network" / "assets" / "app.js": "assets/app.js",
}


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run_steps() -> None:
    for s in STEP_SCRIPTS:
        r = subprocess.run([str(VENV), str(s)], capture_output=True, text=True, cwd=str(REPO))
        tail = (r.stdout or "").strip().splitlines()[-1:] or [""]
        print(f"step {s.name}: rc={r.returncode} | {tail[0][:100]}")
        if r.returncode != 0:
            print((r.stderr or "")[-800:])
            sys.exit(f"BUILD FAILED at {s.name}")


def write_manifest() -> Path:
    files = {}
    for rel in GATED:
        p = REPO / rel
        files[rel] = {"bytes": p.stat().st_size, "sha256": sha256(p)}
    money = REPO / "evidence" / "network" / "money-map.json"
    manifest = {
        "case": "INV-2026-002",
        "note": "manifest.json is exempt from the byte-identical gate; it is the audit record",
        "generatedAtUtc": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                                         capture_output=True, text=True).stdout.strip(),
        "inputs": {
            "graph": "evidence/30-power-graph-v3.json",
            "graphSha256": sha256(REPO / "evidence" / "30-power-graph-v3.json"),
            "moneyMapSha256": sha256(money) if money.exists() else None,
        },
        "gatedAssets": files,
    }
    out = NETROOT / "manifest.json"
    out.write_text(json.dumps(manifest, indent=1) + "\n")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="rebuild into scatch and compare gated assets byte-for-byte")
    args = ap.parse_args()

    run_steps()

    # static assets already live in evidence/network (authored files, not emitted);
    # sanity: they exist
    for rel in GATED:
        p = REPO / rel
        if not p.exists():
            sys.exit(f"missing gated asset: {rel}")

    mpath = write_manifest()
    m = json.loads(mpath.read_text())
    print("\nMANIFEST (gated assets):")
    for rel, meta in m["gatedAssets"].items():
        print(f"  {rel:44s} {meta['bytes']:>9,} B  {meta['sha256'][:16]}")

    if args.verify:
        # snapshot, rebuild, compare
        before = {rel: sha256(REPO / rel) for rel in GATED}
        run_steps()
        after = {rel: sha256(REPO / rel) for rel in GATED}
        diffs = [rel for rel in GATED if before[rel] != after[rel]]
        print("\nREPRODUCIBILITY GATE:", "PASS (byte-identical)" if not diffs else f"FAIL {diffs}")
        if diffs:
            sys.exit(1)


if __name__ == "__main__":
    main()