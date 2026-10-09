<!-- entity-profile:v1 organization -->
# Bethel School District — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/bethel-schools.md`
**Entity ID:** `bethel-schools` · **Type:** organization · **Domain:** institutional
**Tier:** tier2 · **Rank:** 68/163 · **Composite power:** 0.031
**Graph description:** Bethel School District No. 403 — public K-12 district in unincorporated Pierce County (Spanaway, Graham, Roy); ~21,500 students, 39 schools, $164.2M budget.
**Known facts:** District No. 403, Pierce County; serves 200 sq mi unincorporated area; 21,539 students (2023-24); 39 schools; Supt. Brian Lowney since July 2024.
**Status:** ✅ researched — 2026-09-19 — tier2-chunk9 · **Last updated:** 2026-09-19
**Sources:** 8/5 (minimum for tier2)

---

## 0. Why this person or group is on the map
- **Inclusion rule:** from holding office + decision-making — Bethel SD is one of the largest school districts in Pierce County, governing education for ~21,500 students across 200 sq mi of unincorporated Pierce County. Controls $164.2M annual budget, levies, and facilities decisions affecting tens of thousands of residents. Elected school board exercises direct governance over a major public institution. (Sources 1, 3, 5)
- **Adjacent but EXCLUDED candidates:** Puyallup School District (neighbor, boundary tension noted in graph); Franklin Pierce School District; Sumner-Bonney Lake School District — all adjacent Pierce County districts but not the subject here.

## 1. Who they are
- **Exact legal name:** Bethel School District No. 403, Pierce County, Washington
- **Entity type:** Public school district (government entity, non-profit public corporation under WA law)
- **Governing law:** state law (RCW) 28A (Washington school district law); chapter 28A.505 RCW (budget process); chapter 392-123 WAC (budget regulations); OSPI oversight. (Source 4)
- **NCES District ID:** 5300480 (Source 7)
- **Location:** 516 176th St. E., Spanaway, WA 98387; serves Spanaway, Graham, Kapowsin, Roy, and Frederickson. (Sources 2, 4)
- **Service area:** ~200 square miles (520 km²) of unincorporated Pierce County. (Source 2)
- **Parent/subsidiaries:** None; Pierce College operates satellite campuses at two Bethel high schools via partnership. (Source 5)

## 3. Where their power comes from
- **Budget authority:** 2025-26 adopted budget: $164.2 million (reduction of $6.4M from prior year). Five governmental funds. Budget governed by RCW 28A.505 and OSPI F-195 reporting. (Sources 1, 4)
- **Enrollment:** 21,539 students (2023-24); 39 schools; 2,340.87 FTE staff (2025-26). Enrollment grew from 17,651 (2009-10) to 21,539 (2023-24). (Sources 3, 7)
- **Levy authority:** Operates local enrichment and capital levies subject to voter approval. Replacement levy (Resolution No. 8, 25-26) on ballot. State K-12 funding share dropped from 51.6% (2019-21) to 43.2% (2025-27), increasing reliance on local levies. (Sources 4, 8)
- **Elected governance:** 5-member Board of Directors, 4-year terms. Board adopts budget, sets policy, hires superintendent. (Sources 3, 5)
- **Domain overlaps:** Institutional (K-12 education) + Government (public entity, levy authority) + Political (school board elections, levy campaigns).

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | ~21,500 students and families receive education services; 2,340 staff employed | 3, 7 |
| Who sits | 5-member elected board (Marcus Young Sr. Pres., John Manning, Dr. Roseanna Camacho, Terrance Mayers Sr. VP, Teresa Cosio) | 5 |
| Who governs | Board adopts budget, sets policy; Superintendent Brian Lowney executes | 1, 5, 6 |
| Who wins | Pierce County Council committed $245M in planned community investments in Bethel area over 6 years | 9 |

## 5. How they touch government
- **Levy elections:** Operates enrichment and capital levies subject to voter approval. Running replacement levy (Resolution No. 8, 25-26). (Source 4)
- **Pierce County Council:** Joint meeting with County Council; Council reported $245M in planned community investments in Bethel area over 6 years. (Source 9)
- **OSPI:** State oversight via F-195 budget reporting; state funding based on enrollment formula. (Source 4)
- **State funding:** Enrollment decline (lost ~100 students = $1.2M less state funding). K-12 share of state budget dropped from 51.6% to 43.2%. Insurance costs up 32% year-over-year. (Sources 1, 8)
- **Federal funding:** Loss of COVID-era federal grants contributing to budget pressure. Impact Aid program (military-impacted district). (Sources 1, 8)

## 6. Other seats they hold
- **Pierce College:** Partnership operating satellite campuses at two Bethel high schools. (Source 5)
- **Pierce County Council:** Formal joint meetings; $245M planned investment in Bethel area. (Source 9)
- **Superintendent:** Brian Lowney, Ph.D. — 30th year in public education; previously Assistant Superintendent of Secondary Schools in Bethel. Salary ~$268,529 (2025). (Sources 6, 10)
- **Deputy Superintendent:** David Hammond, Ed.D. (Source 8)

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Puyallup School District (`puyallup-schools`) | boundary_tension | 2 |
| Pierce County Council (`county-council`) | levy | 3 |

- 
`bethel-schools`, target=`county-council`, relationship=joint_investment, weight=4, note="https://www.facebook.com/execmello/posts/795110799305114".
`bethel-schools`, target=`pierce-college`, relationship=partnership, weight=3, note="https://superintendentsearch.com/wp-content/uploads/2024/04/Bethel-Final-Brochure-PDF-1.pdf".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | 2025-26 budget $164.2M, $6.4M reduction, 12 staff cuts, Clear Lake Elementary closure | Lookout Eugene-Springfield (reporting on Bethel SD board meeting) | https://lookouteugene-springfield.com/story/education/2025/06/27/bethel-school-board-passes-budget-cuts-spending-by-6-4-million | secondary | 0.80 |
| 2 | District description, 200 sq mi service area, superintendent, NCES ID | Wikipedia (Bethel School District WA) | https://en.wikipedia.org/wiki/Bethel_School_District_(Washington) | secondary | 0.85 |
| 3 | Enrollment 21,539 (2023-24), 39 schools, 5 board members, enrollment trends | Ballotpedia | https://ballotpedia.org/Bethel_School_District,_Washington | secondary | 0.90 |
| 4 | Budget process (RCW 28A.505, WAC 392-123), F-195 report, levy information | Bethel SD official website | https://www.bethelsd.org/programs-departments/business-office/business-office | primary | 1.0 |
| 5 | Board of Directors roster, superintendent search brochure | Bethel SD / Northwest Leadership Associates | https://www.bethelsd.org/about-our-district/board-of-directors | primary | 1.0 |
| 6 | Superintendent Brian Lowney bio, appointment July 2024 | Bethel SD official + Tacoma News Tribune | https://www.bethelsd.org/about-our-district/about-the-superintendent | primary | 1.0 |
| 7 | NCES District ID 5300480, staff count 2,340.87 FTE (2025-26) | NCES (U.S. Dept of Education) | https://nces.ed.gov/ccd/districtsearch/district_detail.asp?ID2=5300480 | primary | 1.0 |
| 8 | Levy info, Resolution No. 8 (25-26), state K-12 funding decline, insurance costs | Bethel SD levy page + Pierce County doc + TNT | https://www.bethelsd.org/resources/levy | primary | 1.0 |
| 9 | Pierce County Council $245M planned investment in Bethel area | Pierce County Council (Facebook post by Exec Mello) | https://www.facebook.com/execmello/posts/795110799305114 | primary | 0.75 |
| 10 | Superintendent salary $268,529 (2025) | OpenPayrolls (public records) | https://openpayrolls.com/rank/highest-paid-employees/washington-bethel | primary | 0.85 |

## 1. Who they are
- **Verdict:** Bethel SD controls a $164.2M annual budget and education services for ~21,500 students across 200 sq mi of unincorporated Pierce County. Its power is institutional — exercised through elected board governance, levy authority, and partnership with Pierce County ($245M in area investments). The district is under financial pressure from declining enrollment, rising insurance costs, and shrinking state K-12 funding share.
- **Conflicts-of-interest flags:** School board members are elected in nonpartisan races but may have political alignments. Clear Lake Elementary closure (saving $1.6M) creates community tension. Budget cuts and staff reductions through attrition may affect educational quality.
- **Analysis of alternatives :** An opposing reading would note that Bethel SD's power is declining — enrollment trends, budget cuts, and school closures suggest an institution under stress rather than one wielding significant power. Its levy authority is constrained by voter approval and state caps. The $245M county investment is County Council spending, not Bethel SD's own budget.
- **Confidence:** High — primary sources from district website, OSPI/NCES data, and budget resolution; financial figures corroborated by multiple sources.