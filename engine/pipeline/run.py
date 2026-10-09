#!/usr/bin/env python3
"""Hermes Investigation Pipeline — orchestrator.

Runs the stages in dependency order. Each stage is a distinct, cacheable, idempotent
step. The publish path is `validate → build → verify`: nothing reaches the web page
that hasn't passed schema + cross-reference validation, and the output is re-checked
against the data after rendering so drift fails loudly.

Stages:
  validate  — schema + cross-reference validation (exits non-zero on ERROR+)
  build     — render HTML from (graph + profiles + site config)
  verify    — post-build gates (readability, zero-power, count drift, top drift)

Usage:
  python3 -m pipeline.run SITE_JSON [--strict] [--max-grade 10]

The site config's `paths` block names the graph + output locations, so the whole
publish step is one command with zero hard-coded paths in the caller.
"""
from __future__ import annotations

import json
import os
import sys

from . import validate as validate_mod
from . import verify as verify_mod
from . import build_site as build_mod


def _load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _resolve(base_dir: str, p: str) -> str:
    if os.path.isabs(p):
        return p
    return os.path.join(base_dir, p)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0].startswith("-"):
        print("usage: python3 -m pipeline.run SITE_JSON [--strict] [--max-grade 10]", file=sys.stderr)
        return 2

    site_path = argv[0]
    strict = "--strict" in argv
    max_grade = 10
    if "--max-grade" in argv:
        max_grade = int(argv[argv.index("--max-grade") + 1])

    site = _load_json(site_path)
    base_dir = os.path.dirname(os.path.abspath(site_path))
    paths = site.get("paths", {})
    graph_path = _resolve(base_dir, paths.get("graph", "evidence/graph.json"))
    out_path = _resolve(base_dir, paths.get("output", "evidence/network.html"))
    profiles_dir = _resolve(base_dir, paths.get("profiles", "profiles"))

    print(f"[1/3] validate {graph_path}")
    rc = validate_mod.main([graph_path, site_path] + (["--strict"] if strict else []))
    if rc != 0:
        print("validation failed — aborting before build", file=sys.stderr)
        return rc

    print(f"[2/3] build  → {out_path}")
    rc = build_mod.main([graph_path, site_path, out_path])
    if rc != 0:
        print("build failed", file=sys.stderr)
        return rc

    print(f"[3/3] verify  (max grade {max_grade})")
    rc = verify_mod.main([graph_path, site_path, out_path, "--max-grade", str(max_grade)])
    if rc != 0:
        print("verify failed — publish blocked", file=sys.stderr)
        return rc

    print(f"publish ready: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
