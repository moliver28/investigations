# Plan: Deep Entity Profiles — Ultra-worked Exhaustive Deepening + Default Templates (INV-2026-002)

**Saved:** 2026-09-19 20:21 PDT · **Plan file:** `.hermes/plans/2026-09-19_202149-deep-entity-profiles.md`
**Repo:** `/Users/moliver/Documents/Investigations/2608-pierce-leadership` (branch `main`, clean at `600f6ba`)

---

## Goal

Deepen the Pierce County Leadership Investigation into a complete, source-verified profile for every one of the 163 entities in the power graph, driven by a reusable, tiered, entity-type-specific template system that also becomes the default template kit for all future investigations.

## Current context / assumptions

- The investigation intent is documented in `2608-pierce-leadership.md` (Key Questions 1–6, Power Domains table): who holds power, its *basis*, what they *do* with it, cross-domain actors, mechanisms connecting domains, and self-dealing/capture patterns. The ultimate goal (per standing project direction) is revealing structural/systemic truths — "how the world works" — not just naming actors.
- Entity inventory (verified just now, read from `evidence/29-power-graph-v2.json`):
  - **163 nodes** — 72 persons, 91 organizations; domains: government 53, economic 32, institutional 47, political 17, legal 6, media 8.
  - **272 edges**; every node has `desc`; 119 have `facts`; **no node carries a `power` key** — composite power is computed at build time in `scripts/build_power_network.py` lines 36–114 (35% weighted degree + 25% betweenness + 20% eigenvector + 20% PageRank, then VETO_BONUS + caps).
  - `/tmp/pierce_graph_v2.json` was pruned — the committed copy at `evidence/29-power-graph-v2.json` is canonical, but `build_power_network.py` line 19 still defaults to `/tmp/pierce_graph_v2.json`. Must fix.
- Evidence files use a standard header block (Case / File / Summary / Key actors / Pull when) and a Sources line with Reliability 0.0–1.0. Profiles must match these conventions.
- Existing verification machinery: hypercritical audit (`audit-pierce-graph.md`), red-team (`red-team-report.md`), skeptic reviews (`skeptic-ranking.md`, `skeptic-omissions.md`, `skeptic-money.md`), HCD/UDL check (`hcd-udl-verification.md`). The graph is post-correction: top-5 = Ryan Mello, Chamber of Commerce, Pierce County Council, Puyallup Tribe, JBLM.
- Subagent fan-out ceiling: 10 parallel children. Python: `/Users/moliver/.hermes/hermes-agent/venv/bin/python3` (has networkx + numpy; **no scipy** — PageRank stays on numpy power iteration).
- Naming/slug conventions (standing): no emotionally loaded slugs; `profiles/<entity-id>.md` uses the graph's existing hyphenated ids.

## Architecture / proposed approach

One shared scoring module (`scripts/compute_power.py`) becomes the single source of truth for power/tier computation — imported by both the HTML build script (refactored, no behavior change) and a new profile generator. The generator renders per-entity profile stubs from two base templates (`templates/person.md`, `templates/organization.md`) whose sections are machine-annotated with ids and tier markers, so depth varies automatically (Tier 1 = top 25, exhaustive; Tier 2 = ranks 26–75, standard; Tier 3 = ranks 76–163, baseline). Research subagents then fill each stub in parallel batches against primary sources with a source-registry (quote + URL + reliability score); a sync script parses a strict "NEW EDGES" block from completed profiles and merges discovered relationships back into the graph, and the HTML is rebuilt only at the end so ranking stays stable.

---

## Step-by-step tasks

### Task 0 — Intent review + README (2 min)

Create `profiles/README.md` documenting: the investigation intent (quote Key Questions 1–6 from `2608-pierce-leadership.md`), the entity inventory (163 nodes / 272 edges, domain+type counts above), tier definitions (below), the workflow (generate → research → sync edges → rebuild → verify), and the templates table (person vs organization × tier).

Tier definitions (deterministic, recomputed from composite power):
- **tier1** = top 25 by composite power, **plus** every evidence/12 power-matrix top-tier actor that falls below rank 25 (elevation set `ELEVATE_TIER1` in the generator — power-matrix rank outranks centrality rank; see Stress Test finding #1) → exhaustive profile (all sections), ≥10 sources, confidence level + VERIFIED stamp
- **tier2** = ranks 26–75 (not elevated) → 8 sections (boundary, identity, power-basis, power-indicators, government-interfaces, interlocks, network-position, sources, assessment), ≥5 sources
- **tier3** = ranks 76–163 (not elevated) → 6 sections (boundary, identity, power-basis, power-indicators, network-position, sources, assessment), ≥3 sources

```bash
mkdir -p profiles
```
Verify: `ls profiles/README.md` exists.

### Task 1 — Extract scoring to `scripts/compute_power.py` (10 min)

Create `/Users/moliver/Documents/Investigations/2608-pierce-leadership/scripts/compute_power.py` with the exact scoring logic currently in `build_power_network.py` lines 36–114 (composite + VETO_BONUS + Kelly Chambers cap + Council cap + party cap), plus a `--selftest`.

Complete file contents:

```python
#!/usr/bin/env python3
"""Composite power scoring shared by the HTML build and the profile generator.

Single source of truth for the academically grounded composite
(evidence/26-power-methodology.md): 35% weighted degree + 25% betweenness
+ 20% eigenvector + 20% PageRank, plus the veto/structural bonus and the
hub/party caps added after the skeptic ranking audit (skeptic-ranking.md).
No scipy — PageRank via numpy power iteration.

Usage: python3 compute_power.py --selftest
"""
import json, os, sys
import networkx as nx
import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DEFAULT_GRAPH = os.path.join(REPO, "evidence", "29-power-graph-v2.json")

VETO_BONUS = {
    "ryan-mello":     0.30,   # County Executive, veto + $3.5B budget (evidence/12 #1)
    "puyallup-tribe": 0.30,   # sovereignty/veto (evidence/12 ranks #3)
    "jblm":           0.28,   # federal veto, largest employer (#5)
    "chamber":        0.20,   # agenda/narrative power (CRITICAL in /13)
    "keith-swank":    0.16,   # legal autonomy (#7)
    "mary-robnett":   0.14,   # prosecutorial discretion (#8)
    "multicare":      0.10,   # largest private employer (#4)
    "anders-ibsen":   0.10,   # Tacoma Mayor, county's largest city (#16)
    "nathe-lawver":   0.10,   # labor-civic interlock (evidence/27)
    "john-wiborg":    0.08,   # interlock economy (#11)
    "dona-ponepinto": 0.08,   # 7+ board interlock (evidence/27)
    "tom-pierson":    0.10,   # revolving door (Chamber CEO + County Econ Dev)
    "john-mccarthy":  0.06,   # (#12)
    "news-tribune":   0.05,   # narrative control (#15)
    "ltg-mcfarlane":  0.05,   # (#22)
    "bill-sterud":    0.05,   # (#23)
}

def build_graph(data):
    G = nx.Graph()
    for n in data["nodes"]:
        G.add_node(n["id"], label=n["label"], type=n["type"], domain=n["domain"])
    for e in data["edges"]:
        if e["source"] in G and e["target"] in G:
            G.add_edge(e["source"], e["target"],
                       relationship=e.get("relationship", ""), weight=e.get("weight", 1))
    return G

def compute_power(G):
    wdeg = dict(G.degree(weight="weight"))
    btw = nx.betweenness_centrality(G, weight="weight")
    eig = nx.eigenvector_centrality(G, max_iter=1000, weight="weight")
    nodes = list(G.nodes()); idx = {n: i for i, n in enumerate(nodes)}; N = len(nodes)
    A = np.zeros((N, N))
    for u, v, d in G.edges(data=True):
        w = d.get("weight", 1); A[idx[u], idx[v]] = w; A[idx[v], idx[u]] = w
    d = A.sum(axis=1); d[d == 0] = 1; M = A / d[:, None]; beta = 0.85
    pr = np.ones(N) / N
    for _ in range(200):
        pr_new = (1 - beta) / N + beta * M.T @ pr
        if np.abs(pr_new - pr).sum() < 1e-9:
            break
        pr = pr_new
    pagerank = {nodes[i]: pr[i] for i in range(N)}

    def normalize(dd):
        vals = list(dd.values()); mn, mx = min(vals), max(vals)
        if mx == mn:
            return {k: 0.5 for k in dd}
        return {k: (v - mn) / (mx - mn) for k, v in dd.items()}

    n_wdeg, n_btw, n_eig, n_pr = normalize(wdeg), normalize(btw), normalize(eig), normalize(pagerank)
    composite = {n: 0.35*n_wdeg[n] + 0.25*n_btw[n] + 0.20*n_eig[n] + 0.20*n_pr[n] for n in G.nodes()}
    for nid, bonus in VETO_BONUS.items():
        if nid in composite:
            composite[nid] = min(1.0, composite[nid] + bonus)
    # Kelly Chambers: holds no office (left WA House Jan 2025, lost 2024 Exec race) — cap below top-25.
    if "kelly-chambers" in composite:
        composite["kelly-chambers"] = min(composite["kelly-chambers"], 0.06)
    # Council hub discount: cap below the Executive so ranking follows evidence/12.
    if "county-council" in composite and "ryan-mello" in composite:
        composite["county-council"] = min(composite["county-council"], composite["ryan-mello"] - 0.02)
    # Party-node artifact: caps well below elected officials.
    for nid in ["pierce-dem", "pierce-gop"]:
        if nid in composite:
            composite[nid] = min(composite[nid], 0.12)
    return composite

def load_default_graph():
    with open(DEFAULT_GRAPH) as f:
        return json.load(f)

def selftest():
    data = load_default_graph()
    G = build_graph(data)
    power = compute_power(G)
    ranked = sorted(G.nodes(), key=lambda n: -power[n])
    top5 = [G.nodes[n]["label"] for n in ranked[:5]]
    print("top5:", top5)
    assert top5 == ["Ryan Mello", "Chamber of Commerce", "Pierce County Council",
                    "Puyallup Tribe", "JBLM"], f"ranking drift: {top5}"
    assert all(power[n] > 0 for n in G.nodes()), "zero-power node found"
    print("selftest PASS")

if __name__ == "__main__":
    selftest()
```

Verify:
```bash
cd ~/Documents/Investigations/2608-pierce-leadership && /Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/compute_power.py --selftest
```
Expected output: `top5: ['Ryan Mello', 'Chamber of Commerce', 'Pierce County Council', 'Puyallup Tribe', 'JBLM']` then `selftest PASS`.

### Task 2 — Refactor `build_power_network.py` to use the shared module (10 min)

Three edits to `scripts/build_power_network.py` (exact patches):

**Edit 2a** — default graph path (line 19): replace
```python
GRAPH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/pierce_graph_v2.json"
```
with
```python
GRAPH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "29-power-graph-v2.json")
```

**Edit 2b** — replace G construction (lines 28–34, from `G = nx.Graph()` through the edge loop) with:
```python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import build_graph, compute_power
G = build_graph(graph_data)
```

**Edit 2c** — delete lines 36–114 (the inline composite computation, VETO_BONUS dict, and all three cap blocks — everything between `# ── Composite power score` and the `max_comp = max(composite.values())` line, exclusive of the latter) and insert:
```python
composite = compute_power(G)
```
Keep `max_comp = max(composite.values())` and everything after it untouched.

Verify (regression — must be bit-identical powers):
```bash
cd ~/Documents/Investigations/2608-pierce-leadership
git show HEAD:evidence/11-power-network.html > /tmp/pre-refactor.html
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/build_power_network.py evidence/29-power-graph-v2.json /tmp/refactor.html
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/compute_power.py --selftest
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 - <<'EOF'
import re, json
def powers(html):
    m = re.search(r'const NODE_DATA\s*=\s*(\{.*?\});', html, re.DOTALL)
    return {k: v.get('power', 0) for k, v in json.loads(m.group(1)).items()}
old = powers(open('/tmp/pre-refactor.html').read())
new = powers(open('/tmp/refactor.html').read())
diffs = {k: abs(old[k] - new[k]) for k in old if abs(old[k] - new[k]) > 1e-9}
print("nodes:", len(old), len(new), "| power diffs:", len(diffs))
assert not diffs, list(diffs.items())[:5]
print("refactor regression PASS")
EOF
```
Expected: `nodes: 163 163 | power diffs: 0` + `refactor regression PASS`; build prints `Labels placed: 33 | remaining overlaps: 0`.

Commit: `git add -A && git commit -m "Extract compute_power.py shared scoring module; build script regression-identical" && git push origin main`.

### Task 3 — Write the two base templates (15 min)

Create `/Users/moliver/Documents/Investigations/2608-pierce-leadership/templates/person.md` — exact contents:

```markdown
<!-- entity-profile:v1 person -->
# {{label}} — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/{{id}}.md`
**Entity ID:** `{{id}}` · **Type:** {{type}} · **Domain:** {{domain}}
**Tier:** {{tier}} · **Rank:** {{rank}}/163 · **Composite power:** {{power}}
**Graph description:** {{desc}}
**Known facts:** {{facts}}
**Status:** ⬜ pending — not yet researched · **Last updated:** {{date}}
**Sources:** 0/{{min_sources}} (minimum for {{tier}})

---

## 0. Boundary & inclusion
<!-- id:boundary -->
- [ ] Inclusion rule — why is this entity inside the map boundary? (positional / reputational / decisional / relational — Laumann, Marsden & Prensky 1983)
- [ ] Adjacent but EXCLUDED candidates? (route to Open questions & leads)

## 1. Identity
<!-- id:identity tier:1 -->
- Legal name, aliases, DOB/birthplace, current residence, family/spouse, education.
- [ ] Fill from primary sources (voter registration where public, Ballotpedia, official bios).

## 2. Career & offices timeline
<!-- id:career tier:1 -->
- [ ] Offices held, employers, dates — chronological; note appointment vs election.

## 3. Power basis & domains
<!-- id:power-basis -->
- [ ] What power does this person hold? (elected/appointed office, wealth, institutional role, inherited position.)
- [ ] Basis for each power-domain overlap (from the scoring framework).
- [ ] Domain focus questions: {{domain_questions}}

## 3a. Power indicators (Domhoff)
<!-- id:power-indicators -->
- [ ] Score each indicator with evidence or UNVERIFIED (Who benefits / Who sits / Who governs / Who wins — Domhoff, whorulesamerica.ucsc.edu):
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | | |
| Who sits | | |
| Who governs | | |
| Who wins | | |

## 4. Financial footprint
<!-- id:financial tier:1 -->
- [ ] Compensation/salary, assets, business interests, property holdings (county assessor records).
- [ ] PDC C1/C3/C4 activity; donor/donee totals.

## 5. Government interfaces
<!-- id:government-interfaces -->
- [ ] Campaign donations given/received (WA PDC), lobbying, contracts, grants, land-use actions.

## 6. Interlocks
<!-- id:interlocks -->
- [ ] Board seats, memberships, employment ties that span domains (cross-reference the graph connections below).

## 7. Controversies
<!-- id:controversies tier:1 -->
- [ ] Ethics complaints, litigation, audits, disciplinary actions. Anticipate the defense counter-argument.

## 8. Media & narrative
<!-- id:media tier:1 -->
- [ ] Coverage pattern, owned outlets, social reach, editorial stance toward this person.

## 9. Network position
<!-- id:network-position -->
- Graph connections (from `evidence/29-power-graph-v2.json`):

{{connections}}

## 10. Sources
<!-- id:sources -->
- [ ] Every claim in sections above needs a primary-source entry with quote + URL + reliability (0.0–1.0). Verify the source as well as the information (provenance + corroboration — Verification Handbook, Silverman/EJC).
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | TODO | | | | |

## 11. Open questions & leads
<!-- id:leads tier:1 -->
- [ ] Follow-ups for deeper investigation.

## 12. Assessment
<!-- id:assessment -->
- [ ] Verdict: what does this person actually control, and how did they get it?
- [ ] Conflicts-of-interest flags (defense-attorney counter-argument anticipated).
- [ ] Analysis of alternatives (ICD 203): what is the opposing reading of the evidence?
- [ ] **Confidence:** ⬜ pending — replace with High / Medium / Low + one-line basis (tier1 mandatory, gate-enforced).
- [ ] VERIFIED stamp (tier1 only): date + reviewer.

## New relationships discovered (submit)
<!-- Each line must match exactly:
     - edge: source=<id>, target=<id>, relationship=<REL>, weight=<n>, note="..."
     REL whitelist: member, board, board_chair, chair, ceo, president, commissioner,
     owner, owned_by, parent, donated, ie, lobbying, lobbies, endorses,
     trains_candidates, federal_funding, state_funding, federal_appropriations,
     transit_funding, appropriates, property_tax_levy, levy, levy_funding, taxing,
     municipal, tax_exempt_status, tax_exemption, sovereignty, federal_land_grant,
     school_bond, ballot_measure, wellfound_jv, jv, operates, land_use, contract,
     family, mentor, staffer, appointed, grant, education, colleague, social -->
- (none yet)
```

Create `templates/organization.md` — identical header/status block, same sections 0 (Boundary & inclusion), 3 (with 3a Power indicators), 5, 6, 9–12 (including the provenance-columns Sources table and the Confidence/Analysis-of-alternatives Assessment) and NEW-EDGES block, but with org-specific sections 1, 2, 4:

```markdown
## 0. Boundary & inclusion
<!-- id:boundary -->
- [ ] Inclusion rule — why is this entity inside the map boundary? (positional / reputational / decisional / relational — Laumann, Marsden & Prensky 1983)
- [ ] Adjacent but EXCLUDED candidates? (route to Open questions & leads)

## 1. Legal identity
<!-- id:identity tier:1 -->
- Exact legal name, entity type (501c3/c6, LLC, government, tribal, religious), EIN/registration, parent/subsidiaries, ownership chain, governing law (e.g. RCW 53 for ports).

## 2. Leadership & board
<!-- id:career tier:1 -->
- Executives (CEO/ED/chair), full board roster — flag every interlock (name appears elsewhere in this graph?).

## 3a. Power indicators (Domhoff)
<!-- id:power-indicators -->
- [ ] Score each indicator with evidence or UNVERIFIED (Who benefits / Who sits / Who governs / Who wins — Domhoff, whorulesamerica.ucsc.edu):
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | | |
| Who sits | | |
| Who governs | | |
| Who wins | | |

## 4. Money
<!-- id:financial tier:1 -->
- Revenue/budget, funding sources (government grants/contracts/appropriations share), tax status, property holdings, levy/bond history.
```

(Tier filters reference ids `identity, power-basis, government-interfaces, interlocks, network-position, sources, assessment` as always-kept; `career, financial, controversies, media, leads` are tier1-only.)

Verify: `ls templates/ && grep -c 'id:' templates/person.md templates/organization.md` (expect 14 markers for person, 13 for organization — person has sections 0,1,2,3,3a,4–12; org has 0,1,2,3,3a,4,5,6,9–12).

### Task 4 — Write `scripts/gen_profile_templates.py` (15 min)

Complete file contents:

```python
#!/usr/bin/env python3
"""Generate deep-profile stubs for every entity in the graph, tiered by power.

Tiers (deterministic, recomputed from the composite power score):
  tier1 = top 25    -> exhaustive profile (all 12 sections, >=10 sources, VERIFIED pass)
  tier2 = rank 26-75 -> standard profile (7 sections, >=5 sources)
  tier3 = rank 76+   -> baseline profile (5 sections, >=3 sources)

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
    # split into [preamble, section, section, ...]
    parts = SECTION_RE.split(raw)
    preamble = parts[0]
    kept = [preamble]
    keep = TIER_SECTIONS[tier]
    for i in range(1, len(parts), 2):
        heading, body = parts[i], parts[i + 1]
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
```

Verify:
```bash
cd ~/Documents/Investigations/2608-pierce-leadership
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/gen_profile_templates.py --dry-run
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/gen_profile_templates.py
ls profiles | wc -l   # expect 163 + README.md = 164 lines
grep -c 'Tier: tier1' profiles/*.md | grep -c ':1$'   # expect 25
```
Expected dry-run line: `profiles: 163 would be generated, 0 existing skipped; tier counts: {'tier1': 25, 'tier2': 50, 'tier3': 88}`.

Spot-check one stub: `read_file profiles/ryan-mello.md` → Tier tier1, rank 1, all 12 sections present, connections table populated.

Commit: `git add -A && git commit -m "Add tiered entity-profile templates + generator (163 stubs: 25/50/88)" && git push origin main`.

### Task 5 — Write `scripts/sync_profiles_to_graph.py` (10 min)

Complete file contents:

```python
#!/usr/bin/env python3
"""Merge NEW-EDGE submissions from completed profiles into the graph JSON.

Only strict `- edge: source=<id>, target=<id>, relationship=<REL>[, weight=<n>][, note="..."]`
lines are parsed. Rejects unknown ids, non-whitelisted rels, and duplicates.

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
}

EDGE_RE = re.compile(
    r'-\s*edge:\s*source=([\w-]+),\s*target=([\w-]+),\s*relationship=([\w-]+)'
    r'(?:,\s*weight=(\d+(?:\.\d+)?))?(?:,\s*note="([^"]*)")?')

def parse_submissions():
    subs = []
    for fname in sorted(os.listdir(PROFILES)):
        if not fname.endswith(".md"):
            continue
        for line in open(os.path.join(PROFILES, fname)):
            m = EDGE_RE.search(line)
            if m:
                subs.append({
                    "source": m.group(1), "target": m.group(2),
                    "relationship": m.group(3),
                    "weight": float(m.group(4)) if m.group(4) else 1.0,
                    "note": m.group(5) or "",
                })
    return subs

def main():
    dry = "--dry-run" in sys.argv
    data = json.load(open(DEFAULT_GRAPH))
    nids = {n["id"] for n in data["nodes"]}
    existing = {(e["source"], e["target"], e["relationship"]) for e in data["edges"]}
    added, rejected = [], []
    for s in parse_submissions():
        if s["relationship"] not in REL_WHITELIST:
            rejected.append((s, "rel not whitelisted"))
        elif s["source"] not in nids or s["target"] not in nids:
            rejected.append((s, "unknown node id"))
        elif (s["source"], s["target"], s["relationship"]) in existing or \
             (s["target"], s["source"], s["relationship"]) in existing:
            rejected.append((s, "duplicate edge"))
        elif s["source"] == s["target"]:
            rejected.append((s, "self-loop"))
        else:
            added.append(s)
    print(f"submissions: {len(added) + len(rejected)} | add {len(added)}, reject {len(rejected)}")
    for s, why in rejected:
        print(f"  REJECT ({why}): {s['source']} --{s['relationship']}--> {s['target']}")
    for s in added:
        print(f"  ADD   {s['source']} --{s['relationship']}--> {s['target']} (w={s['weight']})")
    if not dry and added:
        data["edges"].extend({
            "source": s["source"], "target": s["target"],
            "relationship": s["relationship"], "weight": s["weight"],
        } for s in added)
        json.dump(data, open(DEFAULT_GRAPH, "w"), indent=1)
        print(f"wrote {DEFAULT_GRAPH} ({len(data['nodes'])} nodes, {len(data['edges'])} edges)")

if __name__ == "__main__":
    main()
```

Verify: `python3 scripts/sync_profiles_to_graph.py --dry-run` → `submissions: 0 | add 0, reject 0` (no submissions yet — proves the parser runs clean).

Commit: `git add -A && git commit -m "Add profile-to-graph edge sync with whitelist validation" && git push origin main`.

### Task 6 — Write `scripts/check_profiles.py` (10 min)

Completeness gate the parent runs after every research batch. Complete file contents:

```python
#!/usr/bin/env python3
"""Profile completeness gate. Exit 1 if any profile is below its tier minimums.

Checks per profile: tier parsed from header, sources table rows >= tier minimum,
no 'TODO' left in the tier's required sections, status flipped to researched.
Usage: python3 scripts/check_profiles.py
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import REPO  # noqa: F401  (REPO == investigation root)

PROFILES = os.path.join(REPO, "profiles")
MIN_SOURCES = {"tier1": 10, "tier2": 5, "tier3": 3}

def check(path):
    txt = open(path).read()
    m = re.search(r"\*\*Tier:\*\* (tier\d)", txt)
    tier = m.group(1) if m else None
    src_rows = len(re.findall(r"^\| \d+ \|", txt, re.MULTILINE))
    todos = len(re.findall(r"\[ \]|TODO", txt))
    status = "researched" if re.search(r"\*\*Status:\*\* ✅", txt) else "pending"
    ok = bool(tier) and src_rows >= MIN_SOURCES.get(tier, 999) and todos == 0 and status == "researched"
    # tier1 additionally requires an explicit confidence level (Stress Test finding #7, ICD 203)
    if tier == "tier1" and not re.search(r"\*\*Confidence:\*\* (High|Medium|Low)", txt):
        ok = False
    return tier, src_rows, todos, status, ok

def main():
    bad = []
    for fname in sorted(os.listdir(PROFILES)):
        if not fname.endswith(".md"):
            continue
        tier, src, todos, status, ok = check(os.path.join(PROFILES, fname))
        if not ok:
            bad.append(f"{fname}: tier={tier} src={src}/{MIN_SOURCES.get(tier,'?')} todos={todos} status={status}")
    print(f"profiles failing gate: {len(bad)}")
    for b in bad:
        print("  FAIL", b)
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
```

Verify: `python3 scripts/check_profiles.py; echo "exit=$?"` → expect `profiles failing gate: 163` and `exit=1` (nothing researched yet — proves detection works, including the tier1-confidence requirement).

Commit: `git add -A && git commit -m "Add profile completeness gate (check_profiles.py)" && git push origin main`.

### Task 7 — Research fan-out: Tier 1 (top 25) — delegate 5 subagents × 5 entities (parallel)

Get the exact tier-1 id list from the generator (deterministic): `grep -l 'Tier: tier1' profiles/*.md | xargs -n1 basename | sed 's/\.md//'` and partition into 5 chunks of 5 (chunk 1 = ranks 1–5, chunk 2 = ranks 6–10, etc.).

Subagent context template (fill `<ids>` per chunk):

```
You are an expert investigative researcher filling entity deep-profiles for the Pierce County
Leadership Investigation (INV-2026-002, case type: corruption, legally-defensible evidence
standard). Working dir: /Users/moliver/Documents/Investigations/2608-pierce-leadership

YOUR ASSIGNMENT — exactly these 5 profile files (tier1, exhaustive):
  profiles/<id1>.md
  profiles/<id2>.md
  ... (5 files)

RULES:
1. Fill EVERY section in each file. Every factual claim must trace to a PRIMARY source
   (.gov, Ballotpedia, WA PDC, IRS 990 via ProPublica, SEC, court records, org bios).
2. Sources table: minimum 10 rows per profile. Each row: claim | source name | URL | Type (primary/secondary) | reliability 0.0-1.0.
   Score reliability with the source-reliability skill rubric (weighted 0.0-1.0), not an ad-hoc guess.
   Verify the source as well as the information — provenance + corroboration (Verification Handbook).
3. Anticipate the defense counter-argument in section 12 (Assessment).
4. Distinguish FACT from INFERENCE explicitly. If a figure is unverifiable, write UNVERIFIED.
5. If you discover relationships not in the graph, add lines to the
   "New relationships discovered" block in EXACTLY this format:
   - edge: source=<id>, target=<id>, relationship=<REL>, weight=1, note="<primary source URL>"
   (REL must be from the whitelist; both ids must already exist in evidence/29-power-graph-v2.json;
   put the evidence URL in note — every edge needs provenance, not just every node)
6. When done, flip the header: **Status:** ✅ researched — <date> — <your name>.
7. Verify with web_search for every contested figure. Save each file in place.

Budget: ~8-10 minutes per profile. Output: the 5 completed profile files.
```

Dispatch via `delegate_task` with 5 parallel tasks (one per chunk). After they complete, the parent verifies (subagent self-reports are not trusted):

```bash
cd ~/Documents/Investigations/2608-pierce-leadership
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/check_profiles.py && echo GATE-PASS
grep -c 'Tier: tier1' profiles/*.md | grep -c ':1$'   # still 25
```
Expected: `profiles failing gate: 163 → 138` (25 researched pass, 138 pending still fail) and `exit=1` until all tiers are done; treat "tier1 profiles absent from FAIL list" as the tier-1 gate.

Spot-check (parent, anti-hallucination): `read_file` one profile's Sources table; `web_extract` 2 random URLs to confirm they exist and support the claim.

Commit: `git add -A && git commit -m "Tier-1 deep profiles researched (25 entities, primary-sourced)" && git push origin main`.

### Task 8 — Research fan-out: Tier 2 (ranks 26–75) — delegate 10 subagents × 5 entities (parallel)

Same context template, but: tier2 → 7 sections already filtered by the generator, minimum 5 sources, "✅ researched" flip, NEW-EDGES block same format. 10 parallel tasks × 5 entities.

Verify after completion:
```bash
cd ~/Documents/Investigations/2608-pierce-leadership
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/check_profiles.py; echo "exit=$?"
```
Expected: only tier3 files remain in the FAIL list (88 of them).

Commit: `git add -A && git commit -m "Tier-2 standard profiles researched (50 entities)" && git push origin main`.

### Task 9 — Research fan-out: Tier 3 (ranks 76–163) — 2 waves of 10/9 subagents × 4-5 entities

Same template, tier3 → 5 sections, minimum 3 sources. Wave 1: 10 subagents × 5; wave 2: 9 subagents × ~4.2 (split the 88 ids into 18 chunks: ten 5s + eight 4s+leftovers; adjust chunk sizes so every id is covered exactly once).

Verify:
```bash
cd ~/Documents/Investigations/2608-pierce-leadership
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/check_profiles.py && echo GATE-PASS
```
Expected final: `profiles failing gate: 0` + `GATE-PASS` + `exit=0`.

Commit: `git add -A && git commit -m "Tier-3 baseline profiles researched (88 entities) — all 163 profiles complete" && git push origin main`.

### Task 10 — Sync discovered edges into the graph + rebuild HTML (10 min)

```bash
cd ~/Documents/Investigations/2608-pierce-leadership
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/sync_profiles_to_graph.py --dry-run
```
Review the ADD/REJECT output (rejects should be empty or explained). Then:
```bash
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/sync_profiles_to_graph.py
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/compute_power.py --selftest
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 scripts/build_power_network.py
```
Expected: sync prints the new node/edge counts; selftest prints `selftest PASS` (top-5 unchanged — the veto/cap guards hold); build prints `Labels placed: N | remaining overlaps: 0`.

If selftest FAILS (ranking drifted from new edges), do NOT accept it silently: re-run the skeptic-style review on the changed top-25, adjust caps in `compute_power.py` with an evidence note, and re-run until PASS — then record the decision in the case file.

Commit: `git add -A && git commit -m "Merge profile-discovered edges into graph; rebuild HTML (N nodes / M edges)" && git push origin main`.

### Task 11 — HCD/UDL re-verification + housekeeping (10 min)

Re-run the HCD/UDL quick checks against the rebuilt HTML (fast, no subagent needed for a regression check):
```bash
cd ~/Documents/Investigations/2608-pierce-leadership
grep -c 'prefers-reduced-motion' evidence/11-power-network.html        # ≥1
grep -c 'aria-hidden="true"' evidence/11-power-network.html            # == number of label divs (build output)
grep -c 'tax_exempt_status' evidence/11-power-network.html            # 0 in MONEY_RELS context
```
Then update:
- `evidence/INDEX.md` — add rows: `profiles/` (163 entity deep-profiles), `templates/` (person/org tiered templates), `scripts/{compute_power,gen_profile_templates,sync_profiles_to_graph,check_profiles}.py`, and bump graph counts if edges changed.
- `2608-pierce-leadership.md` — append evidence-log row `E013 | 2026-09-19 | Deep profiles | 163 entity profiles generated from tiered templates and researched to primary sources; new edges synced; HTML rebuilt | profiles/ + evidence/29-power-graph-v2.json | Complete` and update `last_updated`.
- Add `profiles/README.md` workflow diagram update if tier counts changed.

Commit: `git add -A && git commit -m "E013: deep-profile completion + index updates" && git push origin main`.

### Task 12 — Persist the template system into skills (10 min)

1. `skill_view(name='investigation-case-manager')`, then patch a new section "## Deep Entity Profiles (default for every case)" pointing to the workflow: generate (`gen_profile_templates.py`) → tiered research fan-out → `sync_profiles_to_graph.py` → rebuild → `check_profiles.py` gate; and state the tier rules (top-25/next-50/rest; 10/5/3 source minimums; NEW-EDGES strict format + whitelist).
2. Save the template files into the skill via `skill_manage` `write_file` ops as `references/profile-template-person.md` and `references/profile-template-organization.md` (copy of `templates/*.md`), so future investigations inherit them.
3. Copy the 4 scripts into the skill as `scripts/` assets via `skill_manage` `write_file` (or note in the skill that they live in each case repo under `scripts/` and are copied from `references/`).

Verify: `skill_view` shows the new section + `linked_files` lists the two template references.

---

## Tests / validation (summary of gates, in order)

| Gate | Command | Expected |
|---|---|---|
| Scoring selftest | `python3 scripts/compute_power.py --selftest` | top-5 = Mello, Chamber, Council, Tribe, JBLM; `selftest PASS` |
| Refactor regression | Task 2 heredoc script | `nodes: 163 163 \| power diffs: 0`; `refactor regression PASS` |
| Generator | `python3 scripts/gen_profile_templates.py --dry-run` then real run | `163 would be generated`; tier counts `{'tier1': 25, 'tier2': 50, 'tier3': 88}` |
| Edge sync parser | `--dry-run` before research | `submissions: 0 \| add 0, reject 0` |
| Gate detection | `check_profiles.py` before research | 163 FAIL, exit 1 |
| Tier gates | `check_profiles.py` after Tasks 7 / 8 / 9 | FAIL list shrinks 163→138→88→0; final `GATE-PASS`, exit 0 |
| Rebuild | `build_power_network.py` + selftest | `remaining overlaps: 0`; top-5 unchanged |
| HCD regression | Task 11 greps | reduced-motion ≥1; aria-hidden == label count; no gold tax-exempt-status |

## Risks, tradeoffs, open questions

- **Hallucination risk in 163 researched profiles.** Mitigation: mandatory primary-source rows with URL + Type + reliability per claim (weighted rubric, not ad-hoc); parent spot-checks random URLs with `web_extract`; provenance-and-corroboration rule (Verification Handbook); the "TODO/checkbox" + source-count + tier1-confidence gates force real work before a profile passes.
- **Ranking drift after edge sync.** New edges change centrality; the veto/cap guards keep the top-5 stable, but mid-list movement is possible and acceptable — the selftest only pins top-5. If a cap needs adjustment, document it in the case file (evidence decision, not silent tweak).
- **Centrality ≠ power (Stress Test finding #1).** Network centrality systematically under-ranks Domhoff "Who benefits/Who wins" actors (pure donors, beneficiaries, veto actors with few edges). Mitigated by the `ELEVATE_TIER1` power-matrix override, the Domhoff-indicator section (3a) scoring all four indicators, and the veto bonus already in the composite. Residual: the four indicators cannot be fully quantified from public records (reputation/business-council positions) — sections will carry UNVERIFIED rather than fabricated scores.
- **Boundary specification (Stress Test finding #2, Laumann/Marsden/Prensky 1983).** A positional/reputational boundary (who holds office) is the least biased basis; our boundary is relational/positional. Section 0 forces each profile to state its inclusion rule and name excluded candidates; exclusions roll up to the master case file so the boundary stays auditable.
- **Edge provenance (Stress Test finding #5).** NEW-EDGES now requires a source URL in `note=`; the sync script preserves it. Nodes have source tables; edges get at least one URL each — ICIJ-style auditability.
- **Cost/latency: 163 entities ≈ 24+ subagent tasks.** Tiering (10/5/3 source minimums) bounds it; Tier 3 baselines are deliberately light. If wall-clock is a concern, Tier 3 can be deferred — explicitly an open question for the user, defaulting to "research all."
- **Dual-domain organizations** (Puyallup Tribe, Chamber, MultiCare are listed single-domain in the graph): the org template uses the single `domain` field; if the user wants dual-domain profiles, the generator must accept a domain list — small extension, deferred (YAGNI).
- **Template placement:** templates live in the case repo and are mirrored into the skill at Task 12 — one copy per new case, sourced from the skill, to avoid skill bloat (consistent with the recently-slimmed skill).
- **Edge directionality:** graph is undirected (nx.Graph); `donated`/`lobbying` semantics live in `source→target` ordering of the JSON. The sync script preserves ordering as submitted — subagents must get donor→recipient direction right; rejected duplicates are the safety net.
- **Open question — profiles vs. existing evidence files:** evidence/01–28 remain the thematic research files; profiles are per-entity consolidations that cite them. No dedup planned; profiles link to evidence files where relevant.

---

## Stress test against academic & professional frameworks

Conducted 2026-09-19. Frameworks verified against primary literature via web search (Domhoff `whorulesamerica.ucsc.edu`, ODNI ICD 203/206 PDF, Laumann–Marsden–Prensky 1983, Verification Handbook/EJC, LittleSis/Map-the-Power toolkit; Hunter 1953, Dahl 1961, Mills 1956 already cited in case files).

### #1 — FAIL → FIXED: Tiering by centrality contradicts Domhoff's power indicators

Domhoff's operational framework (Who Rules America) measures power by FOUR indicators — **Who benefits? Who sits? Who governs? Who wins?** — because a network trait can only be indexed imperfectly by multiple indicators. The plan tiered by composite centrality, which measures connectedness; the case's own skeptic review (E010) already proved centrality over-ranks hubs and under-ranks veto/beneficiary actors. Tiering on centrality alone would have given Weyerhaeuser-class "Who benefits" actors shallow profiles.
**Fix applied:** `ELEVATE_TIER1` override (evidence/12 power-matrix rank outranks centrality rank); new section 3a scoring all four Domhoff indicators with evidence-or-UNVERIFIED; veto bonus retained in scoring.

### #2 — PASS: Boundary specification problem (Laumann, Marsden & Prensky 1983)

The canonical network-analysis trap is the *boundary specification problem* — the boundary choice determines which actors appear "powerful." The plan's approach: the graph boundary is audited (skeptic-omissions.md already forced the Tacoma City Council, TPCHD, Boeing et al. inside), and **section 0 (Boundary & inclusion)** now forces every profile to state its inclusion rule and name adjacent-but-excluded candidates, with exclusions rolling up to the case file. This makes the boundary auditable and revisable — exactly what Laumann/Marsden/Prensky demand.

### #3 — PASS: Positional approach (Mills 1956; Hunter 1953)

Hunter's community-power tradition (reputational/positional method) supports the "map the holders of formal position first" foundation the investigation already uses (evidence/01 formal-power-structure). The plan deepens each holder into a complete profile rather than re-deriving the roster — consistent with Mills's positional reading of the power elite.

### #4 — PASS with caution: Verification standard (Verification Handbook; source-reliability rubric)

Silverman/EJC: verify the *source* as well as the information; provenance + corroboration. The plan now enforces primary-source rows with a **Type (primary/secondary)** column and weighted reliability via the `source-reliability` skill — matching the user's legally-defensible standard. **Caution (residual):** subagent self-reports remain a risk; mitigation is the parent's random URL spot-checks with `web_extract` (already in Tasks 7–9) and the provenance rule now added to the subagent instructions.

### #5 — PARTIAL → FIXED: Entity-centric data model (LittleSis / Map-the-Power / ICIJ)

LittleSis's production system is entity-centric with relationship types, sources-per-relationship, and interlocks — the plan's per-entity profiles + `relationship` + `note` fields mirror it. **Gap found:** LittleSis attaches a source to EVERY relationship; the plan's NEW-EDGES block had no provenance field. **Fix:** `note="<primary source URL>"` is now mandatory in the submission format and preserved by the sync script.

### #6 — PASS: Analytic tradecraft (ICD 203 / ICD 206)

ODNI ICD 203's standards: describe source quality/credibility, express uncertainty, distinguish underlying information from analyst judgments, incorporate analysis of alternatives, use clear logical argumentation. The template now encodes: source Type+reliability columns (206-style), FACT/INFERENCE separation (already in rules), **Analysis of alternatives** + explicit **Confidence level** in section 12 (gate-enforced for tier1), and the defense-counter-argument requirement. The plan's skeptic/red-team/HCD verification passes already operationalize ICD-203-style challenge.

### #7 — FAIL → FIXED: Confidence levels were absent from the gate

The plan's assessment section asked for a verdict but not an explicit confidence statement; ICD 203 mandates uncertainty characterization. **Fix:** Confidence line added to section 12 (High/Medium/Low + one-line basis); `check_profiles.py` now fails any tier1 profile without it.

### #8 — PASS (already in plan): Reproducibility (DRY extraction of compute_power.py)

Matches the reproducible-research norm (single scoring source of truth; bit-identical refactor regression test) and the standing "zero-shot reproducible build" requirement of this project.

### #9 — Residual risk (accepted, documented): Domhoff indicators under-quantified

"Who benefits/wins" for many actors cannot be quantified from public records (business councils, reputation). Profiles will record UNVERIFIED rather than fabricated scores — consistent with the user's standard ("UNVERIFIED is better than wrong"). If the user wants quantified indicator scores later, that is a separate data-collection project (interviews, business-council minutes, decision-outcome coding à la Dahl 1961).

### Verdict

The original plan survived 5 of 9 framework checks unscathed; 4 failures/partials were found and all are now fixed in-plan: power-matrix tier elevation (Domhoff), edge provenance (LittleSis/ICIJ), confidence levels + alternatives (ICD 203), and boundary/inclusion documentation (Laumann et al. 1983). One residual risk (#9) is accepted and documented.
