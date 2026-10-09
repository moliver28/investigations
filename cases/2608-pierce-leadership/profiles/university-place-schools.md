<!-- entity-profile:v1 organization -->
# University Place Schools — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/university-place-schools.md`
**Entity ID:** `university-place-schools` · **Type:** organization · **Domain:** institutional
**Tier:** tier3 · **Rank:** 82/163 · **Composite power:** 0.026
**Graph description:** — 
**Known facts:** — (none recorded)
**Status:** ✅ researched — 2026-09-19 — tier3-chunk2 · **Last updated:** 2026-09-19
**Sources:** 3/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why it is on the map.** University Place School District (UPSD) is in the map because of two reasons. First, State Sen. T'wina Nobles (D-28) sits on its 5-member Board of Directors. That gives the district a direct line to two state Senate committees: Higher Education & Workforce Development, and Early Learning & K-12. Second, UPSD puts levy and bond measures on the ballot. In February 2026, it placed a $320 million bond on the ballot. That makes it an active player in Pierce County Council levy decisions.
- **Who is left out.** Tacoma Public Schools, Clover Park, Bethel, and Peninsula are separate districts. Each is on its own page or in open questions.

## 1. Who they are
- **Legal name:** University Place School District No. 83 (Washington). It does business as University Place School District (UPSD).
- **Type:** A Washington public school district. It is a junior taxing district (a local government body with limited tax power) under state law RCW 28A (common schools) and Title 84 RCW (property tax levies). It has no EIN (federal tax ID). It is a tax-exempt government body.
- **Governing law:** RCW 28A.315 (school director elections); RCW 28A.500-525 (levies and bonds); RCW 84.52.053 (levy lids — the legal cap on how much a school district can raise through local property taxes).
- **Superintendent (current):** Jeff Chamberlin (per UPSD83.org).
- **Current board (5 members):** Marisa Peloquin (2017–2029); Ethelda Burke (2015–2029); Rick Maloney (2019–2027); **T'wina Nobles (2015–2027)**; Mary Lu Dickinson (1995–2027). Source: Ballotpedia 2024 election page. Nobles was first sworn in in 2015.
- **Schools:** 8 (2023–24).
- **Students:** 5,606 (2023–24, OSPI — the Office of Superintendent of Public Instruction).
- **FY24 total spending:** $98,082,000 ($17,474 per student).

## 3. Where their power comes from
- **Local decision-making:** The 5-member Board sets policy for about 5,600 students and a $98 million budget. It approves bond and levy measures that go before Pierce County voters. The February 2026 special-election ballot includes two replacement levies and a $320 million bond. That gives the Board direct control of the building pipeline.
- **Bridge to the state Legislature:** Sen. Nobles wears two hats. She is a UPSD board director and a state senator on the Higher Education & Workforce Development and Early Learning & K-12 committees. That gives UPSD a direct line into K-12 funding formulas (the rules that decide how much state money each district gets) and any McCleary-fix changes (court-ordered updates to K-12 funding). Most mid-sized districts do not have that kind of access.
- **Community power:** UPSD is the main K-12 institution for the City of University Place and nearby unincorporated areas. It shapes school boundaries, land use, and where new schools get built across about 3 square miles of incorporated UP.
- **Why it scores this way:** The score comes from the Nobles board overlap (graph weight 4) and the levy ties to Pierce County Council (graph weight 3).

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | UPSD students and parents get steady levy support and a senator on key committees. Local building contractors get work from the bond pipeline. School board members benefit from incumbency and ballot design. | #1, #2 |
| Who sits | Sen. T'wina Nobles (state senator D-28 and UPSD board director Position 3 since 2015). Mary Lu Dickinson (director since 1995). Four other elected directors. | #1, #3 |
| Who governs | A 5-member elected Board of Directors governs. Superintendent Jeff Chamberlin runs daily work. OSPI provides state oversight. Voters approve levies and bonds. | #1, #2 |
| Who wins | Nobles wins a clear channel of influence. The district wins legislative access. The former county council chair (Ryan Mello, prior) had a District 4 seat covering downtown Tacoma, Hilltop, and University Place — an overlapping base of voters. | INFERENCE from #1, #2 |

## 9. Who they are connected to
Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| T'wina Nobles (D-28) (`twina-nobles`) | board_member | 4 |
| Pierce County Council (`county-council`) | levy | 3 |

### New relationships to record.
`university-place-schools`, target=`ospi`, relationship=`oversight`, weight=2, note="Washington Office of Superintendent of Public Instruction regulates UPSD as a common-school district".
`university-place-schools`, target=`jeff-chamberlin`, relationship=`employment`, weight=3, note="Jeff Chamberlin, UPSD superintendent (per UPSD83.org)".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | UPSD Board of Directors voted unanimously to place two replacement levies and a bond measure on a Feb. 10, 2026 special election ballot; current 5-member board includes T'wina Nobles (term 2015–2027), Marisa Peloquin (2017–2029), Ethelda Burke (2015–2029), Rick Maloney (2019–2027), Mary Lu Dickinson (1995–2027). | Ballotpedia, "University Place School District, Washington, elections" | https://ballotpedia.org/University_Place_School_District,_Washington,_elections | secondary (elections encyclopedia, multi-source) | 0.90 |
| 2 | T'wina Nobles has served on the University Place School Board since 2016 (per Senate bio; Ballotpedia lists term start 2015) and chairs the WA Senate Higher Education & Workforce Development Committee while vice-chairing Early Learning & K-12 Education. | Washington State Senate Democrats, "Biography - Sen. T'wina Nobles" | https://senatedemocrats.wa.gov/nobles/biography | primary (official bio) | 0.95 |
| 3 | UPSD enrolled 5,606 students across 8 schools in 2023–24 with $98.082M total expenditures ($17,474/student); per-pupil breakdowns: instructional $9,336 (53%), support $2,243 (13%), admin $1,717 (10%). | Ballotpedia UPSD page (citing OSPI / NCES data) | https://ballotpedia.org/University_Place_School_District,_Washington,_elections | secondary (cites official OSPI data) | 0.90 |

## 1. Who they are
- Verdict: UPSD is a tier-3 institutional node. Its influence does not come from size — only 5,606 students. It comes from Nobles wearing two hats: she is a school-board director and a state senator on the very committees that set K-12 funding. That makes UPSD a stronger policy pipeline than its mid-tier budget suggests.
- Conflicts-of-interest flags: (a) Sen. Nobles serving on a school board and as a state senator on K-12 funding committees at the same time is unusual. Any votes where she recused herself should be reviewed. (b) The February 2026 ballot has a $320 million construction bond. The campaign-finance filings for that measure should be checked for contractor contributions.
- Analysis of alternatives (ICD-203 opposing view): UPSD could also be read as a small suburban district with shrinking enrollment (down 3.5% over five years per Ballotpedia, from 5,816 in 2018–19 to 5,606 in 2023–24) and average academic results. It is not a power hub on its own. The power reading rests on the Nobles board overlap. Remove her and the graph weight collapses. UNVERIFIED: how often Nobles actually recuses.
- **Confidence:** **Medium** — Board roster and enrollment figures are well-sourced from Ballotpedia/NCES; the Feb-2026 bond amount and exact Nobles recusal record are partially UNVERIFIED at this depth of research.
 (submit)
<!-- Each line must match exactly:
<id>, target=<id>, relationship=<REL>, weight=<n>, note="..."
REL whitelist: member, board, board_chair, chair, ceo, president, commissioner,
owner, owned_by, parent, donated, ie, lobbying, lobbies, endorses,
trains_candidates, federal_funding, state_funding, federal_appropriations,
transit_funding, appropriates, property_tax_levy, levy, levy_funding, taxing,
municipal, tax_exempt_status, tax_exemption, sovereignty, federal_land_grant,
school_bond, ballot_measure, wellfound_jv, jv, operates, land_use, contract,
family, mentor, staffer, appointed, grant, education, colleague, social -->
