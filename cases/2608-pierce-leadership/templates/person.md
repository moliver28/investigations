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