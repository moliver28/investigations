#!/usr/bin/env python3
"""Normalize verbatim relationship types into 8 canonical classes (UI v3, Task 1.1).

- Adds `rel_class` to every edge; the verbatim `relationship` string is
  preserved byte-for-byte (gate 2).
- Exits NON-ZERO on any unclassified type (gate 1) or any edge classed
  `other` (gate 15) - an unrouted type is a build failure, not a warning.

Usage:
  normalize_relationships.py --dry-run                 # histogram only, no write
  normalize_relationships.py                            # write evidence/30-power-graph-v3.json
  normalize_relationships.py --check-plan-table <plan>  # embedded table vs plan table
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GRAPH_IN = REPO / "evidence" / "29-power-graph-v2.json"
GRAPH_OUT = REPO / "evidence" / "30-power-graph-v3.json"
PLAN_DEFAULT = REPO / ".hermes" / "plans" / "2026-10-04_115252-power-network-ui-v3.md"

CLASS_ORDER = ["money", "influence", "governance", "legal", "business", "media", "community", "other"]

ROUTE: dict[str, str] = {
    # money
        "appropriates": "money",
        "ballot_measure": "money",
        "donated": "money",
        "federal_appropriations": "money",
        "federal_funding": "money",
        "federal_land_grant": "money",
        "ie": "money",
        "levy": "money",
        "municipal": "money",
        "property_tax_levy": "money",
        "school_bond": "money",
        "sovereignty": "money",
        "state_funding": "money",
        "tax_exempt_status": "money",
        "tax_exemption": "money",
        "taxing": "money",
        "transit_funding": "money",
            # influence
        "aligned": "influence",
        "endorsed": "influence",
        "endorses": "influence",
        "influence": "influence",
        "lobbies": "influence",
        "lobbying": "influence",
        "lobbyist": "influence",
        "supports": "influence",
        "trains_candidates": "influence",
        "veto": "influence",
            # governance
        "acting_director": "governance",
        "appointed": "governance",
        "appoints": "governance",
        "appoints_judges": "governance",
        "board": "governance",
        "board_chair": "governance",
        "board_member": "governance",
        "board_of_health": "governance",
        "board_president": "governance",
        "board_tie": "governance",
        "ceo": "governance",
        "chair": "governance",
        "chairman": "governance",
        "chairman_tie": "governance",
        "chancellor": "governance",
        "city_council": "governance",
        "commands": "governance",
        "commissioner": "governance",
        "commissioner_position": "governance",
        "council": "governance",
        "director": "governance",
        "ed": "governance",
        "elected_by_voters": "governance",
        "employer": "governance",
        "exec": "governance",
        "exec_director": "governance",
        "former_board": "governance",
        "former_commissioner": "governance",
        "holds_accountable": "governance",
        "judge": "governance",
        "led_by": "governance",
        "mayor": "governance",
        "member": "governance",
        "oversees": "governance",
        "oversight": "governance",
        "president": "governance",
        "serves": "governance",
        "sheriff": "governance",
        "superintendent": "governance",
        "vice_chair": "governance",
            # legal
        "conflict": "legal",
        "enforces": "legal",
        "federal_cases": "legal",
        "federal_oversight": "legal",
        "hears_appeals": "legal",
        "prosecutes": "legal",
            # business
        "aerospace_partner": "business",
        "contract": "business",
        "county_partnership": "business",
        "developer_partner": "business",
        "founded_by": "business",
        "jv": "business",
        "land_use": "business",
        "maritime": "business",
        "operates": "business",
        "owned_by": "business",
        "parent": "business",
        "partner": "business",
        "partnership": "business",
        "peer_utility": "business",
        "redevelopment": "business",
        "utility": "business",
        "wellfound_jv": "business",
            # media
        "covered_by": "media",
        "covers": "media",
        "editor": "media",
        "peer_newsroom": "media",
            # community
        "advisor": "community",
        "armed_services_champion": "community",
        "boundary_tension": "community",
        "colleague": "community",
        "coordinates": "community",
        "former": "community",
        "former_cfo": "community",
        "former_exec": "community",
        "former_planning": "community",
        "honored": "community",
        "legacy": "community",
        "overlap": "community",
        "peer_district": "community",
        "religious_affiliation": "community",
        "religious_sponsor": "community",
        "runs": "community",
        "social": "community",
        "ssmcp": "community",
            }


def check_plan_table(plan_path=None):
    plan_path = plan_path or PLAN_DEFAULT
    text = Path(plan_path).read_text()
    lo = text.index("**The 8 classes**")
    hi = text.index("**Step 1: Write the classifier**")
    plan_route = {}
    for line in text[lo:hi].split("\n"):
        m = re.match(r"\|\s*`([a-z_]+)`\s*\|[^|]+\|(.+)\|\s*$", line)
        if m and m.group(1) in CLASS_ORDER:
            plan_route[m.group(1)] = re.findall(r"`([a-z][a-z0-9_]*)`", m.group(2))
    ok = True
    embedded_ok = True
    for c in CLASS_ORDER:
        embedded = sorted(t for t in ROUTE if ROUTE[t] == c)
        listed = sorted(plan_route.get(c, []))
        listed_valid = [t for t in listed if t in ROUTE]
        if sorted(embedded_ok and embedded) != sorted(listed_valid):
            print(f"PLAN DRIFT [{c}]:")
            print(f"  embedded: {embedded}")
            print(f"  plan:     {listed_valid}")
            ok = False
    return ok

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="check only, write nothing")
    ap.add_argument("--check-plan-table", nargs="?", const=PLAN_DEFAULT, default=None,
                    help="verify embedded ROUTE matches the plan table (uses default plan path)")
    args = ap.parse_args()

    if args.check_plan_table:
        sys.exit(0 if check_plan_table(args.check_plan_table) else 1)

    g = json.loads(GRAPH_IN.read_text())
    nodes, edges = g["nodes"], g["edges"]
    if any("rel_class" in e for e in edges):
        print("FATAL: rel_class already present - refusing to double-normalize")
        sys.exit(2)

    hist = Counter()
    unclassified, other_classed = [], []
    for e in edges:
        rt = e.get("relationship")
        if rt is None:
            print("FATAL: edge missing relationship:", e)
            sys.exit(2)
        if rt not in ROUTE:
            unclassified.append(rt)
            continue
        if ROUTE[rt] == "other":
            other_classed.append(rt)
            continue
        hist[ROUTE[rt]] += 1

    print(f"Nodes: {len(nodes)}  Edges: {len(edges)}")
    for c in CLASS_ORDER:
        print(f"  {c:12s} {hist.get(c, 0)}")
    print(f"Unclassified: {len(unclassified)}  {sorted(set(unclassified)) or ''}")
    print(f"'other'-classed: {len(other_classed)}  {sorted(set(other_classed)) or ''}")
    if unclassified or other_classed:
        print("BUILD FAILURE - gates 1 & 15: every verb must be explicitly routed")
        sys.exit(1)
    if sum(hist.values()) != len(edges):
        print("BUILD FAILURE - histogram does not sum to edge count")
        sys.exit(1)

    if args.dry_run:
        print("Dry-run PASS (gates 1 & 15).")
        sys.exit(0)

    for e in edges:
        e["rel_class"] = ROUTE[e["relationship"]]
    out = json.dumps(g, indent=1, ensure_ascii=True)   # NO trailing newline (byte-fidelity)
    GRAPH_OUT.write_text(out)
    print(f"WROTE {GRAPH_OUT} ({len(out):,} bytes)")

if __name__ == "__main__":
    main()
