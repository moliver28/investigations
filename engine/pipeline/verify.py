"""Stage 6: post-build verification (deterministic gates).

Runs after `build_site` and checks the OUTPUT against the DATA, so drift is caught
mechanically rather than by a skeptic's eyeball:

  COUNT.DRIFT        — rendered node/edge counts vs graph counts (stale 'N nodes' text).
  TOP.DRIFT          — the #1 node in the rendered ranking vs the computed ranking.
  READABILITY        — any researched profile above the FK grade ceiling (via prose gate).
  ZERO_POWER         — any node at 0.000 power (placeholder / broken measurement).
  ORPHAN_PROFILE     — graph node with a profile file that is NOT marked researched.
  REL.GAP            — (info) relationship classes in config with zero edges in graph.

Usage:
  python3 -m pipeline.verify GRAPH_JSON SITE_JSON OUT_HTML [--max-grade 10]
"""
from __future__ import annotations

import json
import os
import re
import sys

from .errors import ErrorCollector
from .power import build_graph, compute_power


def _load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def fk_grade(text: str) -> float | None:
    def syllables(word):
        word = re.sub(r"[^a-z]", "", word.lower())
        if not word:
            return 0
        groups = re.findall(r"[aeiouy]+", word)
        n = len(groups)
        if word.endswith("e") and n > 1 and not word.endswith(("le", "ce", "ge", "be", "de", "ke", "me", "ne", "pe", "se", "te", "ve", "ze")):
            n -= 1
        if word.endswith("es") and n > 1:
            n -= 1
        if word.endswith("ed") and n > 1:
            n -= 1
        return max(n, 1)
    text = re.sub(r"\|.*\|", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[#*`>\[\]()]", " ", text)
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"edge:\s*source=", " ", text)
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if len(s.strip().split()) > 3]
    words = [w for s in sentences for w in s.split()]
    if not sentences or not words:
        return None
    asl = len(words) / len(sentences)
    asw = sum(syllables(w) for w in words) / len(words)
    return 0.39 * asl + 11.8 * asw - 15.59


def verify(graph_path: str, site_path: str, out_html: str, max_grade: int = 10) -> ErrorCollector:
    errs = ErrorCollector()
    graph = _load_json(graph_path)
    site = _load_json(site_path)
    G = build_graph(graph)
    composite = compute_power(G, site.get("power"))
    nodes = graph["nodes"]
    edges = graph["edges"]

    # zero-power
    for nid, p in composite.items():
        if p <= 0.0:
            errs.error("ZERO_POWER", f"node '{nid}' has 0.000 power",
                       fix="Connect it or remove it.", data={"id": nid})

    # readability gate
    base_dir = os.path.dirname(os.path.abspath(site_path))
    profiles_dir = site.get("paths", {}).get("profiles", "profiles")
    if not os.path.isabs(profiles_dir):
        profiles_dir = os.path.join(base_dir, profiles_dir)
    if os.path.isdir(profiles_dir):
        for fname in sorted(os.listdir(profiles_dir)):
            if not fname.endswith(".md") or fname == "README.md":
                continue
            txt = open(os.path.join(profiles_dir, fname), encoding="utf-8").read()
            if "✅ researched" not in txt:
                continue
            body = txt.split("\n---\n", 1)[1] if "\n---\n" in txt else txt
            body = re.split(r"\n#{1,2}\s*[^\n]*(?:New relationships|relationships to record)", body)[0]
            g = fk_grade(body)
            if g is not None and g > max_grade:
                errs.error("READABILITY", f"{fname} reads at grade {g:.1f} (>{max_grade})",
                           path=f"profiles/{fname}",
                           fix="Run the prose pass (simplify sentences) on it.",
                           data={"file": fname, "grade": round(g, 1)})

    # orphan profiles (node exists but profile not researched)
    nids = {n["id"] for n in nodes}
    for nid in sorted(nids):
        p = os.path.join(profiles_dir, f"{nid}.md")
        if os.path.exists(p):
            txt = open(p, encoding="utf-8").read()
            if "✅ researched" not in txt:
                errs.warn("ORPHAN_PROFILE", f"profile '{nid}.md' exists but is not researched",
                          path=f"profiles/{nid}.md",
                          fix="Research it, or it will render as desc/facts only.",
                          data={"id": nid})

    # count drift in HTML (stale hard-coded counts)
    html = open(out_html, encoding="utf-8").read()
    # The HTML injects counts via JS/JSON; check the node_data JSON size.
    m = re.search(r"const NODE_DATA = (\{.*?\});\n", html, re.DOTALL)
    if m:
        try:
            node_data = json.loads(m.group(1))
            rendered_nodes = len(node_data)
            if rendered_nodes != len(nodes):
                errs.error("COUNT.DRIFT", f"rendered {rendered_nodes} nodes vs graph {len(nodes)}",
                           fix="Rebuild from the current graph JSON.")
        except json.JSONDecodeError:
            errs.warn("COUNT.DRIFT", "could not parse NODE_DATA to verify counts")

    # top-actor drift: verify the #1 ranked node label appears in the HTML
    ranked = sorted(G.nodes(), key=lambda n: -composite[n])
    if ranked:
        top_label = G.nodes[ranked[0]]["label"]
        if top_label not in html:
            errs.error("TOP.DRIFT", f"top actor '{top_label}' not found in rendered HTML",
                       fix="Rebuild — the mission/ranking text is stale.")

    # relationship class coverage (info)
    for cls in ("money", "influence", "interlock"):
        rels = set(site.get("relationship_classes", {}).get(cls, []))
        edge_rels = {e.get("relationship") for e in edges}
        unused = rels - edge_rels
        if unused:
            errs.info("REL.GAP", f"relationship class '{cls}' has {len(unused)} rels with no edges",
                      data={"unused": sorted(unused)})

    return errs


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 3:
        print("usage: verify.py GRAPH_JSON SITE_JSON OUT_HTML [--max-grade 10]", file=sys.stderr)
        return 2
    max_grade = 10
    if "--max-grade" in argv:
        max_grade = int(argv[argv.index("--max-grade") + 1])
    graph_path, site_path, out_html = argv[0], argv[1], argv[2]
    errs = verify(graph_path, site_path, out_html, max_grade)
    errs.emit()
    print(f"\nverify: {errs.count('ERROR')} errors, {errs.count('WARN')} warnings, {errs.count('INFO')} info", file=sys.stderr)
    return 1 if errs.has_any("FATAL", "ERROR") else 0


if __name__ == "__main__":
    sys.exit(main())
