#!/usr/bin/env python3
"""Merge NEW-EDGE submissions and researched profile metadata into the graph JSON.

Three deterministic jobs, run in this order:
1. backfill  — copy "Known facts" + "Graph description" header lines from each
               ✅-researched profile into the matching node (facts/desc). Only
               fills EMPTY node fields, so it never clobbers hand-authored graph data.
2. edges     — parse strict `- edge: source=<id>, target=<id>, relationship=<REL>`
               lines from profiles and add them (rejecting unknown ids, non-whitelisted
               rels, duplicates, self-loops).
3. dedupe    — drop self-loops and exact (source,target,rel) duplicates that may have
               accumulated across prior runs.

This keeps evidence/29-power-graph-v2.json in sync with the researched profiles,
which are the canonical source of truth for entity facts.

Usage:
  python3 scripts/sync_profiles_to_graph.py --dry-run
  python3 scripts/sync_profiles_to_graph.py    # writes evidence/29-power-graph-v2.json
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import DEFAULT_GRAPH

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PROFILES = os.path.join(REPO, "profiles")

REL_WHITELIST = {
    "member", "board", "board_chair", "chair", "ceo", "president", "commissioner",
    "owner", "owned_by", "parent", "donated", "ie", "lobbying", "lobbies", "endorses",
    "trains_candidates", "federal_funding", "state_funding", "federal_appropriations",
    "transit_funding", "appropriates", "property_tax_levy", "levy", "levy_funding",
    "taxing", "municipal", "tax_exempt_status", "tax_exemption", "sovereignty",
    "federal_land_grant", "school_bond", "ballot_measure", "wellfound_jv", "jv",
    "operates", "land_use", "contract", "family", "mentor", "staffer",
    "appointed", "grant", "education", "colleague", "social",
}

# ── Normalization layer (deterministic, added after the tier-3 consistency audit) ──
# Subagents used freeform relationship labels and near-miss node slugs that the strict
# whitelist silently dropped. These maps normalize the HIGH-CONFIDENCE cases so real
# discovered edges are not lost; anything still unmatched is reported (never silent).

# Freeform relationship label → canonical label. Only mechanically-unambiguous synonyms
# (identical meaning) are mapped; semantically novel labels are left for manual review.
REL_ALIAS = {
    "board_interlock": "board",
    "board_member": "board",
    "board_president": "board_chair",
    "committee_member": "member",
    "caucus_affiliate": "member",
    "party_colleague": "colleague",
    "senate_colleague": "colleague",
    "legislative_colleague": "colleague",
    "co_legislator": "colleague",
    "caucus_colleague": "colleague",
    "wa_delegation_colleague": "colleague",
    "cross_endorsement": "endorses",
    "coverage": "covers",
    "regent": "board",
    "commissioner_position_4": "commissioner",
    "former_board_member": "former_board",
    "former_member": "former",
}

# Near-miss node slug → canonical node id (typos, case, abbreviation/full-name expansion).
NODE_ALIAS = {
    "Columbia-Bank": "columbia-bank",
    "drew-strokesbary": "drew-stokesbary",
    "sumner-bonney-lake-sd": "sumner-bonney-lake",
    "pierce-county-council": "county-council",
    "tacoma-pierce-county-health-department": "tpchd",
    "tacoma-pierce-county-health-dept": "tpchd",
    "greater-tacoma-community-foundation": "gtcf",
    "united-way-pierce-county": "united-way",
    "tacoma-chamber": "chamber",
    "pierce-county-executive": "ryan-mello",
    "pierce-county-exec": "ryan-mello",
    "governor-ferguson": "bob-ferguson",
    "sheila-edwards-lange": "sheila-lange",
    "deborah-krishnadasan": "deb-krishnadasan",
}

EDGE_RE = re.compile(
    r'-\s*edge:\s*source=([\w-]+),\s*target=([\w-]+),\s*relationship=([\w-]+)'
    r'(?:,\s*weight=(\d+(?:\.\d+)?))?(?:,\s*note="([^"]*)")?')

# Money flows donor→recipient (evidence/28 + skill pitfall). If a submission names a
# PAC/organization as the SOURCE of a 'donated' edge to a person, that direction is
# correct; the reverse (person → PAC) is the common reversal bug. We can't auto-detect
# all of them safely, but these are the confirmed reversals found by red-team review.
REVERSED_DONATED = {
    # (source, target): the wrong-direction edge to DROP. Realtors PAC → Conway is the
    # correct money direction; the profile also submitted Conway → PAC (reversed).
    ("steve-conway", "wa-realtors-pac"),
}

def parse_submissions():
    subs = []
    for fname in sorted(os.listdir(PROFILES)):
        if not fname.endswith(".md"):
            continue
        for line in open(os.path.join(PROFILES, fname)):
            m = EDGE_RE.search(line)
            if m:
                src = NODE_ALIAS.get(m.group(1), m.group(1))
                tgt = NODE_ALIAS.get(m.group(2), m.group(2))
                rel = REL_ALIAS.get(m.group(3), m.group(3))
                subs.append({
                    "source": src, "target": tgt, "relationship": rel,
                    "weight": float(m.group(4)) if m.group(4) else 1.0,
                    "note": m.group(5) or "",
                })
    return subs

# Role relationships where the PERSON holds a seat/office at the ORGANIZATION.
# Canonical direction is person → organization. Subagents sometimes wrote org → person.
PERSON_TO_ORG_RELS = {
    "board", "board_chair", "chair", "ceo", "president", "commissioner",
    "regent", "member", "former_board", "former", "staffer", "superintendent",
    "exec", "exec_director", "ed", "director", "chairman", "councillor", "mayor",
    "judge", "lobbyist", "advisor", "mentor", "board_president",
}

def _correct_direction(s, node_types):
    """Return (src, tgt) with direction fixed for person↔org role edges."""
    src, tgt, rel = s["source"], s["target"], s["relationship"]
    if rel not in PERSON_TO_ORG_RELS:
        return src, tgt
    st = node_types.get(src)
    tt = node_types.get(tgt)
    # org → person is backwards; flip so person is the source.
    if st == "organization" and tt == "person":
        return tgt, src
    return src, tgt

def backfill_node_metadata(data):
    """Copy researched profile header facts/desc into nodes with EMPTY fields."""
    filled_facts, filled_desc = 0, 0
    for n in data["nodes"]:
        pid = n["id"]
        path = os.path.join(PROFILES, f"{pid}.md")
        if not os.path.exists(path):
            continue
        txt = open(path).read()
        # only backfill from profiles that are actually researched
        if "✅ researched" not in txt:
            continue
        mf = re.search(r"\*\*Known facts:\*\*\s*(.+)", txt)
        md = re.search(r"\*\*Graph description:\*\*\s*(.+)", txt)
        if not n.get("facts") and mf:
            raw = mf.group(1).strip()
            if raw and raw not in ("(none yet)", "None"):
                facts = [f.strip() for f in re.split(r"[;•]", raw) if f.strip()]
                if facts:
                    n["facts"] = facts
                    filled_facts += 1
        if not n.get("desc", "").strip() and md:
            raw = md.group(1).strip()
            if raw and raw not in ("(none yet)", "None"):
                n["desc"] = raw
                filled_desc += 1
    print(f"backfill: +{filled_facts} facts lists, +{filled_desc} descs (only empty fields filled)")
    return data

def main():
    dry = "--dry-run" in sys.argv
    data = json.load(open(DEFAULT_GRAPH))

    # ── 1. backfill facts/desc from researched profiles ──
    data = backfill_node_metadata(data)

    # ── 2. edge submissions ──
    nids = {n["id"] for n in data["nodes"]}
    node_types = {n["id"]: n["type"] for n in data["nodes"]}
    existing = {(e["source"], e["target"], e["relationship"]) for e in data["edges"]}
    added, rejected = [], []
    added_keys = set()
    for s in parse_submissions():
        s["source"], s["target"] = _correct_direction(s, node_types)
        key = (s["source"], s["target"], s["relationship"])
        if (s["source"], s["target"]) in REVERSED_DONATED and s["relationship"] == "donated":
            rejected.append((s, "reversed money edge (donor/recipient flipped)"))
        elif s["relationship"] not in REL_WHITELIST:
            rejected.append((s, "rel not whitelisted"))
        elif s["source"] not in nids or s["target"] not in nids:
            rejected.append((s, "unknown node id"))
        elif key in existing or (s["target"], s["source"], s["relationship"]) in existing or key in added_keys:
            rejected.append((s, "duplicate edge"))
        elif s["source"] == s["target"]:
            rejected.append((s, "self-loop"))
        else:
            added.append(s)
            added_keys.add(key)
    print(f"edge submissions: {len(added) + len(rejected)} | add {len(added)}, reject {len(rejected)}")
    for s, why in rejected:
        print(f"  REJECT ({why}): {s['source']} --{s['relationship']}--> {s['target']}")
    for s in added:
        print(f"  ADD   {s['source']} --{s['relationship']}--> {s['target']} (w={s['weight']})")

    # ── 3. drop reversed + self-loop + exact-duplicate edges that already exist in JSON ──
    before = len(data["edges"])
    dropped = []
    keep = []
    seen = set()
    for e in data["edges"]:
        key = (e["source"], e["target"], e["relationship"])
        if e["source"] == e["target"]:
            dropped.append(("self-loop", e)); continue
        if (e["source"], e["target"]) in REVERSED_DONATED and e["relationship"] == "donated":
            dropped.append(("reversed", e)); continue
        if key in seen:
            dropped.append(("dup", e)); continue
        seen.add(key)
        keep.append(e)
    data["edges"] = keep
    if dropped:
        print(f"cleanup: dropped {len(dropped)} stale edges")
        for why, e in dropped:
            print(f"  DROP ({why}): {e['source']} --{e['relationship']}--> {e['target']}")

    if dry:
        print(f"DRY-RUN: no write. would be {len(data['nodes'])} nodes / {len(data['edges'])} edges")
        return

    if added or dropped:
        data["edges"].extend({
            "source": s["source"], "target": s["target"],
            "relationship": s["relationship"], "weight": s["weight"],
        } for s in added)
        json.dump(data, open(DEFAULT_GRAPH, "w"), indent=1)
        print(f"wrote {DEFAULT_GRAPH} ({len(data['nodes'])} nodes, {len(data['edges'])} edges)")
    else:
        print("no changes to write")

if __name__ == "__main__":
    main()
