# Entity Deep Profiles — INV-2026-002.

## Investigation intent

Key Questions (from `2608-pierce-leadership.md`):
1. Who holds power in Pierce County?
2. What is the *basis* of their power?
3. What do they *do* with it?
4. Which actors cross domain boundaries?
5. What mechanisms connect domains?
6. What self-dealing / capture patterns exist?

The ultimate goal: reveal structural/systemic truths — "how the world works" — using facts.

## Entity inventory

- **163 nodes** — 72 persons, 91 organizations.
- **342 edges**.
- Domains: government 53, economic 32, institutional 47, political 17, legal 6, media 8.
- Source graph: `evidence/29-power-graph-v2.json`.

## Tier definitions (recomputed from composite power score)

| Tier | Rank range | Sections | Min sources | Notes |
|------|-----------|----------|-------------|-------|
| tier1 | top 25 (+ ELEVATE_TIER1 overrides) | all (~13) | 10 | Confidence level + VERIFIED stamp required |
| tier2 | 26–75 | 9 | 5 | Standard depth |
| tier3 | 76–163 | 7 | 3 | Baseline |

ELEVATE_TIER1: actors the evidence/12 power matrix ranks top-tier are elevated to tier1.
even if centrality ranks them below 25 (centrality under-ranks donors/beneficiaries/veto.
actors — Domhoff "Who benefits/Wins" indicators).

## Workflow

1. **Generate** — `scripts/gen_profile_templates.py` creates 163 stubs from graph + templates.
2. **Research** — subagent fan-out fills stubs against primary sources (tiered batches).
3. **Sync edges** — `scripts/sync_profiles_to_graph.py` merges NEW-EDGES into graph JSON.
4. **Rebuild** — `scripts/build_power_network.py` regenerates HTML with ranking guards.
5. **Verify** — `scripts/check_profiles.py` completeness gate (fails until all tier minimums met).

## Templates

| Template | Entity type | Sections |
|----------|------------|----------|
| `templates/person.md` | person | 0,1,2,3,3a,4–12 (14 markers) |
| `templates/organization.md` | organization | 0,1,2,3,3a,4,5,6,9–12 (13 markers) |

Tier filtering: generator keeps only sections whose `id:` marker is in the tier's.
keep-set (tier1 = all; tier2 = 9 sections; tier3 = 7 sections).