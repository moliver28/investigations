"""Stage 1: validate graph data + site config. Emits structured errors; exits non-zero on ERROR+.

Validations (loud, structured, fix-hinted):
  GRAPH.SCHEMA        — graph fails JSON Schema (jsonschema Draft7).
  GRAPH.DUP_NODE      — duplicate node id.
  GRAPH.DUP_EDGE      — duplicate (source,target,relationship) edge.
  GRAPH.ORPHAN        — edge references a node id absent from the graph.
  GRAPH.SELF_LOOP     — source == target.
  GRAPH.BAD_WEIGHT    — weight <= 0 or non-numeric.
  GRAPH.ZERO_POWER    — (optional) node scores 0.000 (broken/placeholder).
  REL.UNCLASSIFIED    — relationship not in any site relationship class (WARN).
  SITE.SCHEMA         — site config fails JSON Schema.
  SITE.ORPHAN_REF     — config references a node id absent from the graph (money node,
                        veto bonus, hub cap, mission target).
  SITE.BAD_DOMAIN     — domain in graph missing from site config `domains`.

Usage:
  python3 -m pipeline.validate GRAPH_JSON SITE_JSON [--strict]
"""
from __future__ import annotations

import json
import sys

import jsonschema

from .errors import ErrorCollector

GRAPH_SCHEMA = "schema/graph.schema.json"
SITE_SCHEMA = "schema/site.schema.json"


def _schema_path(name: str) -> str:
    import os
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), name)


def _load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _validate_schema(data: dict, schema_name: str, code: str, errs: ErrorCollector) -> None:
    schema = _load_json(_schema_path(schema_name))
    validator = jsonschema.Draft7Validator(schema)
    for e in validator.iter_errors(data):
        path = "/".join(str(p) for p in e.absolute_path) or "(root)"
        errs.error(code, e.message, path=f"/{path}",
                   fix="Correct the field to satisfy the schema.", data={"path": path})


def validate_graph(data: dict, errs: ErrorCollector, check_power: bool = False,
                   power: dict | None = None) -> None:
    _validate_schema(data, GRAPH_SCHEMA, "GRAPH.SCHEMA", errs)

    seen_nodes: set[str] = set()
    for i, n in enumerate(data.get("nodes", [])):
        nid = n.get("id", "")
        if nid in seen_nodes:
            errs.error("GRAPH.DUP_NODE", f"duplicate node id '{nid}'",
                       path=f"/nodes/{i}", fix="Deduplicate the node.", data={"id": nid})
        seen_nodes.add(nid)

    seen_edges: set = set()
    for i, e in enumerate(data.get("edges", [])):
        src, tgt, rel = e.get("source"), e.get("target"), e.get("relationship")
        key = (src, tgt, rel)
        if key in seen_edges:
            errs.error("GRAPH.DUP_EDGE", f"duplicate edge {src} --{rel}--> {tgt}",
                       path=f"/edges/{i}", fix="Drop the duplicate.", data={"source": src, "target": tgt, "relationship": rel})
        seen_edges.add(key)
        if src == tgt:
            errs.error("GRAPH.SELF_LOOP", f"self-loop on '{src}'",
                       path=f"/edges/{i}", fix="Remove or rewire the edge.", data={"id": src})
        w = e.get("weight", 1)
        if not isinstance(w, (int, float)) or w <= 0:
            errs.error("GRAPH.BAD_WEIGHT", f"bad weight {w!r} on {src}--{rel}-->",
                       path=f"/edges/{i}", fix="Set weight to a positive number.", data={"weight": w})

    node_ids = {n.get("id") for n in data.get("nodes", [])}
    for i, e in enumerate(data.get("edges", [])):
        for side in ("source", "target"):
            ref = e.get(side)
            if ref and ref not in node_ids:
                errs.error("GRAPH.ORPHAN", f"edge {side} '{ref}' not in nodes",
                           path=f"/edges/{i}/{side}",
                           fix="Add the node or fix the reference.", data={"ref": ref})

    if check_power and power is not None:
        for nid, p in power.items():
            if p <= 0.0:
                errs.error("GRAPH.ZERO_POWER", f"node '{nid}' has zero power",
                           path=f"/nodes/{nid}", fix="Connect it, or remove it.",
                           data={"id": nid})

    return None


def validate_site(site: dict, graph_data: dict, errs: ErrorCollector) -> None:
    _validate_schema(site, SITE_SCHEMA, "SITE.SCHEMA", errs)

    node_ids = {n.get("id") for n in graph_data.get("nodes", [])}
    edge_rels = {e.get("relationship") for e in graph_data.get("edges", [])}

    # relationship taxonomy completeness (ERROR: any rel in NO class would silently
    # render as 'structural' fallthrough — that must never happen silently).
    classified: set[str] = set()
    membership: dict[str, list[str]] = {}
    for cls in ("money", "influence", "interlock", "structural"):
        for rel in site.get("relationship_classes", {}).get(cls, []):
            classified.add(rel)
            membership.setdefault(rel, []).append(cls)
    for rel in sorted(edge_rels):
        if rel not in classified:
            errs.error("REL.UNCLASSIFIED",
                       f"relationship '{rel}' is in NO relationship class",
                       path="/relationship_classes",
                       fix="Add it to exactly one of money/influence/interlock/structural.",
                       data={"relationship": rel})
        elif len(membership[rel]) > 1:
            # intentional dual-class (money+influence) for campaign-finance verbs
            dual_ok = {"donated", "ie", "lobbying", "lobbies", "endorses", "trains_candidates"}
            if rel not in dual_ok:
                errs.warn("REL.AMBIGUOUS",
                          f"relationship '{rel}' is in multiple classes: {membership[rel]}",
                          path="/relationship_classes",
                          fix="Assign it to exactly one class.",
                          data={"relationship": rel, "classes": membership[rel]})

    # orphan references in config
    for nid in site.get("extra_money_nodes", []):
        if nid not in node_ids:
            errs.error("SITE.ORPHAN_REF", f"extra_money_nodes '{nid}' not in graph",
                       path="/extra_money_nodes", fix="Remove or rename it.", data={"id": nid})
    for nid in (site.get("power", {}).get("veto_bonus") or {}):
        if nid not in node_ids:
            errs.error("SITE.ORPHAN_REF", f"veto_bonus '{nid}' not in graph",
                       path="/power/veto_bonus", fix="Remove or rename it.", data={"id": nid})
    for spec in (site.get("power", {}).get("hub_caps") or []):
        nid = spec.get("id")
        if nid and nid not in node_ids:
            errs.error("SITE.ORPHAN_REF", f"hub_caps '{nid}' not in graph",
                       path="/power/hub_caps", fix="Remove or rename it.", data={"id": nid})
        below = spec.get("below")
        if below and below not in node_ids:
            errs.error("SITE.ORPHAN_REF", f"hub_caps.below '{below}' not in graph",
                       path="/power/hub_caps", fix="Fix the `below` reference.", data={"id": below})
    for m in site.get("missions", []):
        tgt = m.get("target")
        if tgt and tgt not in node_ids:
            errs.error("SITE.ORPHAN_REF", f"mission target '{tgt}' not in graph",
                       path="/missions", fix="Fix or remove the target.", data={"id": tgt})

    # domain coverage: every domain in the graph must have a color/shape/label
    domains_cfg = site.get("domains", {})
    graph_domains = {n.get("domain") for n in graph_data.get("nodes", []) if n.get("domain")}
    for dom in graph_domains:
        if dom not in domains_cfg:
            errs.error("SITE.BAD_DOMAIN", f"domain '{dom}' in graph has no site config",
                       path="/domains", fix="Add color/shape/label for it.", data={"domain": dom})

    return None


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 2:
        print("usage: validate.py GRAPH_JSON SITE_JSON [--strict]", file=sys.stderr)
        return 2
    graph_path, site_path = argv[0], argv[1]
    strict = "--strict" in argv

    errs = ErrorCollector()
    graph_data = _load_json(graph_path)
    site = _load_json(site_path)

    validate_site(site, graph_data, errs)
    validate_graph(graph_data, errs)

    errs.emit()
    print(f"\nvalidation: {errs.count('ERROR')} errors, {errs.count('WARN')} warnings", file=sys.stderr)
    if errs.has_any("FATAL", "ERROR") or (strict and errs.has_any("WARN")):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
