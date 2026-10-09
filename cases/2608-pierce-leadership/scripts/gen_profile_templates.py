#!/usr/bin/env python3
"""Generate deep-profile stubs for every entity in the graph, tiered by power.

Tiers (deterministic, recomputed from the composite power score):
  tier1 = top 25    -> exhaustive profile (all sections, >=10 sources, VERIFIED pass)
  tier2 = rank 26-75 -> standard profile (9 sections, >=5 sources)
  tier3 = rank 76+   -> baseline profile (7 sections, >=3 sources)

Usage:
  python3 scripts/gen_profile_templates.py            # generate missing stubs
  python3 scripts/gen_profile_templates.py --dry-run  # show what would be created
  python3 scripts/gen_profile_templates.py --force    # regenerate ALL stubs (overwrite)
"""
import json, os, re, sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import build_graph, compute_power, load_default_graph

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TEMPLATES = os.path.join(REPO, "templates")
PROFILES = os.path.join(REPO, "profiles")

TIER_RANKS = {"tier1": (0, 25), "tier2": (25, 75), "tier3": (75, 10**9)}
# Elevation set (Stress Test finding #1): actors the evidence/12 power matrix ranks
# top-tier must be tier1 EVEN IF composite centrality ranks them below 25
# (centrality under-ranks donors/beneficiaries/veto actors — Domhoff "Who
# benefits/Wins" actors). Populate from evidence/12 during Task 4 verification.
ELEVATE_TIER1 = set()
TIER_SECTIONS = {
    "tier1": None,  # keep every section
    "tier2": {"boundary", "identity", "power-basis", "power-indicators",
              "government-interfaces", "interlocks", "network-position",
              "sources", "assessment"},
    "tier3": {"boundary", "identity", "power-basis", "power-indicators",
              "network-position", "sources", "assessment"},
}
TIER_MIN_SOURCES = {"tier1": 10, "tier2": 5, "tier3": 3}

DOMAIN_QUESTIONS = {
    "government": ("What offices/authority does this entity hold? What budget does it control? "
                   "Appointment/veto powers? Which jurisdictions does it govern?"),
    "economic": ("Revenue, ownership structure, market position? Government contracts/grants received? "
                 "Jobs controlled? Land/real-estate holdings?"),
    "institutional": ("Tax status (501c3/c6, tribal, federal, religious)? Board roster and interlocks? "
                      "Government funding share of revenue?"),
    "political": ("Who is funded and endorsed? PAC spending? Party machinery control? "
                  "Candidate recruitment/training output?"),
    "legal": ("Jurisdiction and discretion? Appointment path (elected/appointed)? "
              "Caseload and enforcement power?"),
    "media": ("Ownership chain (parent company)? Reach (circulation/listeners/pageviews)? "
              "Editorial stance and investigative record?"),
}

SECTION_RE = re.compile(r"^## ", re.MULTILINE)
MARKER_RE = re.compile(r"<!-- id:([\w-]+)(?:\s+tier:1)?\s*-->")

def render_connections(G, nid):
    rows = []
    for u, v, d in sorted(G.edges(nid, data=True), key=lambda t: str(t[2].get("relationship"))):
        other = v if u == nid else u
        rows.append(f"| {G.nodes[other]['label']} (`{other}`) | {d.get('relationship','')} | {d.get('weight',1)} |")
    if not rows:
        return "(no connections in graph — investigate and submit NEW EDGES)"
    return "| Connected entity | Relationship | Weight |\n|---|---|---|\n" + "\n".join(rows)

def render_template(tpl_path, G, nid, power, rank, tier):
    raw = open(tpl_path).read()
    # split into [preamble, section, section, ...] — each section starts with heading text
    parts = SECTION_RE.split(raw)
    preamble = parts[0]
    kept = [preamble]
    keep = TIER_SECTIONS[tier]
    for part in parts[1:]:
        first_nl = part.find('\n')
        heading = part[:first_nl] if first_nl != -1 else part
        body = part[first_nl+1:] if first_nl != -1 else ''
        m = MARKER_RE.search(body)
        sec_id = m.group(1) if m else None
        if keep is None or sec_id in keep:
            kept.append("## " + heading + MARKER_RE.sub("", body))
    out = "".join(kept)
    nd = G.nodes[nid]
    facts = "; ".join(nd.get("facts", [])) if nd.get("facts") else "— (none recorded)"
    repl = {
        "id": nid, "label": nd["label"], "type": nd["type"], "domain": nd["domain"],
        "tier": tier, "rank": rank, "power": f"{power[nid]:.3f}",
        "desc": nd.get("desc", "—"), "facts": facts,
        "connections": render_connections(G, nid),
        "domain_questions": DOMAIN_QUESTIONS.get(nd["domain"], "—"),
        "min_sources": TIER_MIN_SOURCES[tier],
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    for k, v in repl.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out

def main():
    dry = "--dry-run" in sys.argv
    force = "--force" in sys.argv
    data = load_default_graph()
    G = build_graph(data)
    power = compute_power(G)
    ranked = sorted(G.nodes(), key=lambda n: -power[n])
    rank = {n: i + 1 for i, n in enumerate(ranked)}
    tier_of = {}
    for tier, (lo, hi) in TIER_RANKS.items():
        for n in ranked[lo:hi]:
            tier_of[n] = tier
    for nid in ELEVATE_TIER1:
        if nid in tier_of:
            tier_of[nid] = "tier1"
    made, skipped = 0, 0
    os.makedirs(PROFILES, exist_ok=True)
    for nid in ranked:
        out_path = os.path.join(PROFILES, f"{nid}.md")
        if os.path.exists(out_path) and not force:
            skipped += 1
            continue
        tpl = "person.md" if G.nodes[nid]["type"] == "person" else "organization.md"
        body = render_template(os.path.join(TEMPLATES, tpl), G, nid, power, rank[nid], tier_of[nid])
        if not dry:
            with open(out_path, "w") as f:
                f.write(body)
        made += 1
    counts = {t: sum(1 for v in tier_of.values() if v == t) for t in TIER_RANKS}
    print(f"profiles: {made} {'would be ' if dry else ''}generated, {skipped} existing skipped; "
          f"tier counts: {counts}")

if __name__ == "__main__":
    main()