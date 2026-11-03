# HYPERCRITICAL AUDIT — Pierce County Power Network Graph (112 nodes / 149 edges)

**Case:** INV-2026-002 · **Graph audited:** `/tmp/pierce_graph.json` · **Evidence base:** `evidence/01–28`
**Auditor:** Hypercritical review subagent · **Date:** 2026-09-09
**Verdict:** The graph is a **solid skeleton but not a power map.** It captures the formal government layer and the major institutions, but it systematically **over-ranks network hubs, under-ranks veto/structural power, contains several factually wrong edges, and omits the entire growth-machine coalition and the money→people→systems loop** that is the investigation's stated thesis (evidence/28). It will mislead the HTML rebuild if used as-is.

---

## 1. ENTITY AUDIT

Verdicts: **OK** = real, correctly named/typed/domained. **WRONG** = factual error. **MISSING** = evidence names it, graph omits it. **BORDERLINE** = defensible but contestable domain/type.

### 1.1 Nodes present in graph

| Node | Type | Domain | Verdict | Correction / Note |
|------|------|--------|---------|-------------------|
| ryan-mello | person | government | **OK** | Exec since 2025, 51.28% (evidence/01, /04). |
| county-council | org | government | **OK** | 7 members 4D-3R (evidence/01). |
| keith-swank | person | government | **OK** | Sheriff since 2025 (evidence/01). |
| mary-robnett | person | government | **OK** | PA since 2019 (evidence/01). |
| jani-hitchen | person | government | **OK** | Council Chair D-6 (evidence/01). |
| dave-morell | person | government | **OK** | Vice Chair R-1 (evidence/01). |
| paul-herrera | person | government | **OK** | R-2 (evidence/01). |
| amy-cruver | person | government | **OK** | R-3 (evidence/01). |
| rosie-ayala | person | government | **OK** | D-4, GTCF board (evidence/01, /18). |
| bryan-yambe | person | government | **OK** | D-5 (evidence/01). |
| robyn-denson | person | government | **OK** | D-7 Exec Pro Tem (evidence/01). |
| anders-ibsen | person | government | **OK** | Tacoma Mayor since 2026 (evidence/01, /02). |
| kristina-walker | person | government | **OK** | Tacoma Council Pos 8, Pierce Transit Chair (evidence/02, /22). |
| jim-kastama | person | government | **OK** | Puyallup Council D1 (evidence/02). |
| bruce-dammeier | person | government | **OK** | Former Exec 2017-24 (evidence/01). |
| metro-parks | org | government | **OK** | Independent park district (evidence/25). |
| pierce-transit | org | government | **OK** | Regional transit (evidence/22). |
| sound-transit | org | government | **OK** | Regional transit (evidence/20). |
| west-pierce-fire | org | government | **OK** | Dist 3 (evidence/21). |
| central-pierce-fire | org | government | **OK** | Dist 6, 2025 merger (evidence/21). |
| matt-mauer | person | government | **OK** | Metro Parks Board President (evidence/25). |
| mike-griffus | person | government | **OK** | Pierce Transit CEO (evidence/22). |
| john-clancy | person | government | **OK** | West Pierce Fire Board Chair (evidence/21). |
| port-tacoma | org | economic | **BORDERLINE** | Evidence/28 calls it a **public** municipal corp funded by property tax. Domain could be government. |
| john-mccarthy | person | economic | **OK** | Port Commissioner, 4 terms (evidence/01). |
| jt-wilcox | person | economic | **OK** | Port Commissioner, ex-State House GOP Leader (evidence/01). |
| eric-johnson | person | economic | **OK** | Port Exec Director (evidence/01). |
| chamber | org | economic | **BORDERLINE** | Evidence/14 calls it a "shadow political party." 501(c)(6). Economic defensible, but its power is political. |
| tom-pierson | person | economic | **OK** | Chamber Interim CEO (evidence/14). |
| chyna-willman | person | economic | **OK** | Chamber Board Chair (evidence/14). |
| john-wiborg | person | economic | **OK** | MultiCare Board Chair / Stellar CEO (evidence/08). |
| nash-cascadia | org | economic | **OK** | NASH Cascadia Verde LLC, donor (evidence/04). |
| master-builders | org | economic | **OK** | Construction PAC (evidence/04). |
| foss-family | org | economic | **OK** | Maritime dynasty (evidence/19). |
| columbia-bank | org | economic | **OK** | Tacoma-HQ bank (evidence/19). |
| russell-invest | org | economic | **OK** | Russell Investments (evidence/19). |
| weyerhaeuser | org | economic | **OK** | Timber (evidence/19). |
| green-diamond | org | economic | **OK** | Timber, Simpson/Reed (evidence/19). |
| chatham-am | org | economic | **BORDERLINE** | Hedge fund owning McClatchy. Its power is **media** (evidence/06). Domain should arguably be media. |
| puyallup-tribe | org | institutional | **BORDERLINE** | Evidence/12 scores Economic 9, Institutional 9. Gaming is its biggest lever; economic is defensible. |
| bill-sterud | person | institutional | **OK** | Tribal Chairman, 46 yrs (evidence/03). |
| tim-reynon | person | institutional | **OK** | Tribal Council, ex-Gov Office of Indian Affairs (evidence/03). |
| multicare | org | institutional | **BORDERLINE** | Evidence/12 scores Economic 9, Institutional 8. Largest private employer; economic defensible. |
| bill-robertson | person | institutional | **OK** | MultiCare CEO retiring Dec 2026 (evidence/08). |
| florence-chang | person | institutional | **OK** | President → CEO Jan 2027 (evidence/08). |
| vmfh | org | institutional | **OK** | VMFH/CHI (evidence/24). |
| uli-chi | person | institutional | **OK** | VMFH Board Chair (evidence/24). |
| julie-manas | person | institutional | **OK** | VMFH NW Region President (evidence/24). |
| diann-puls | person | institutional | **OK** | VMFH board, ex-Weyerhaeuser (evidence/24). |
| jblm | org | institutional | **OK** | Joint Base (evidence/09). |
| ltg-mcfarlane | person | institutional | **OK** | I Corps CG (evidence/09). |
| dona-ponepinto | person | institutional | **OK** | United Way CEO / TCC Board Chair (evidence/18, /23). |
| gtcf | org | institutional | **OK** | GTCF (evidence/18). |
| kathi-littmann | person | institutional | **OK** | GTCF CEO (evidence/18). |
| united-way | org | institutional | **OK** | United Way of Pierce County (evidence/18). |
| russell-family | org | institutional | **OK** | Russell Family Fdn (evidence/18). |
| erika-tucci | person | institutional | **OK but ISOLATED** | Cheney Foundation ED (evidence/18). **Zero edges** — orphaned. |
| uw-tacoma | org | institutional | **OK** | UW Tacoma (evidence/23). |
| sheila-lange | person | institutional | **OK** | UW Tacoma Chancellor (evidence/23). |
| plu | org | institutional | **OK** | PLU (evidence/23). |
| allan-belton | person | institutional | **OK** | PLU President (evidence/23). |
| tcc | org | institutional | **OK** | TCC (evidence/23). |
| ivan-harrell | person | institutional | **OK** | TCC President (evidence/23). |
| lin-zhou | person | institutional | **OK but ISOLATED** | Bates President (evidence/23). **Zero edges** — orphaned. |
| pierce-gop | org | political | **OK** | (evidence/04). |
| pierce-dem | org | political | **OK** | (evidence/04). |
| kelly-chambers | person | political | **OK** | State Rep R-25, lost 2024 Exec (evidence/04). |
| hdcc | org | political | **OK** | HDCC (evidence/04). |
| wea-pac | org | political | **OK** | WEA PAC (evidence/04). |
| together-pierce | org | political | **OK** | Together for Pierce (evidence/04). |
| michael-shaw | person | political | **OK** | County lobbyist (evidence/07). |
| gth-gov | org | political | **OK** | GTH Gov Relations (evidence/07). |
| pclc | org | political | **OK** | PCCLC (evidence/16). |
| alice-phillips | person | political | **OK** | PCCLC President (evidence/16). |
| ilwu23 | org | political | **OK** | ILWU Local 23 (evidence/16). |
| tacoma-pd-union | org | political | **OK** | Tacoma Police Union Local 6 (evidence/16). |
| news-tribune | org | media | **OK** | (evidence/06). |
| mcclatchy | org | media | **OK** | (evidence/06). |
| stephanie-pedersen | person | media | **OK** | News Tribune Editor (evidence/06). |
| south-sound-biz | org | media | **OK** | (evidence/06). |
| premier-media | org | media | **OK** | (evidence/06). |
| knkx | org | media | **OK** | (evidence/06). |
| iheart | org | media | **OK** | (evidence/06). |
| audacy | org | media | **OK** | (evidence/06). |
| lotus | org | media | **OK** | (evidence/06). |
| superior-court | org | legal | **OK** | 23 judges (evidence/01). |
| district-court | org | legal | **OK** | 8 judges — **UNVERIFIED** count (evidence/01 doesn't specify). |
| court-appeals | org | legal | **OK** | Div 2 Tacoma (evidence/01). |
| stanley-rumbaugh | person | legal | **OK** | Superior Court judge (evidence/01). |
| linda-farmer | person | government | **OK** | Auditor (evidence/01). |
| marty-campbell | person | government | **OK** | Assessor-Treasurer (evidence/01). |
| chris-gildon | person | government | **OK** | State Sen R-25 (evidence/01). |
| phil-fortunato | person | government | **OK** | State Sen R-31 (evidence/01). |
| yasmin-trudeau | person | government | **OK** | State Sen D-27 (evidence/01). |
| twina-nobles | person | government | **OK** | State Sen D-28 (evidence/01). |
| steve-conway | person | government | **WRONG** | Evidence/01: Conway **did not seek re-election in 2026**; 29th LD seat contested. Graph lists him as current. |
| laurie-jinkins | person | government | **OK** | State Rep D-27, House Speaker (evidence/13). |
| drew-stokesbary | person | government | **OK** | State Rep R-31, House GOP leader (evidence/13). |
| melanie-morgan | person | government | **OK** | State Rep D-29 (evidence/13). |
| maria-cantwell | person | government | **OK** | US Sen (evidence/13). |
| patty-murray | person | government | **OK** | US Sen (evidence/13). |
| emily-randall | person | government | **OK** | US Rep WA-06 (evidence/13). |
| marilyn-strickland | person | government | **OK** | US Rep WA-10 (evidence/13). |
| tacoma-schools | org | institutional | **OK** | (evidence/17). |
| puyallup-schools | org | institutional | **OK** | (evidence/17). |
| bethel-schools | org | institutional | **OK** | (evidence/17). |
| clover-park-schools | org | institutional | **OK** | (evidence/17). |
| josh-garcia | person | institutional | **OK** | Tacoma Schools Supt (evidence/17). |
| korey-strozier | person | institutional | **OK** | Tacoma School Board President (evidence/17). |
| catholic-archdiocese | org | institutional | **OK** | Archdiocese of Seattle (evidence/13). |
| life-center | org | institutional | **OK** | Megachurch (evidence/13). |
| healthy-bay | org | institutional | **OK** | Communities for a Healthy Bay (evidence/20). |

### 1.2 Nodes MISSING from the graph (evidence names them)

| Missing node | Evidence | Why critical |
|---|---|---|
| **Nathe Lawver** | /18, /27 | The **single most important labor-civic interlock** — GTCF board + United Way board chair + Building Trades exec secretary. Explicitly flagged in /27 as a key interlock. |
| **Andrew Strobel** | /23 | TCC board + senior advisor to Exec Mello + former Puyallup Tribe planning director — a direct county/tribe/TCC line. |
| **Lois Bernstein** | /23 | MultiCare Chief Community Executive on TCC board — MultiCare–TCC interlock. |
| **Jason Thompson** | /08 | MultiCare board + Russell Investments director — healthcare/finance interlock. |
| **Dale Sowell** | /08 | MultiCare board + Green Diamond (retired CFO) — healthcare/timber interlock. |
| **Dick Marzano, Deanna Keller, Kristin Ang** | /01 | Other 3 Port commissioners (Marzano is 2026 Commission President). |
| **Adam Smith** | /13 | US Rep WA-09, **Ranking Member Armed Services** — JBLM's champion in Congress. |
| **Kim Schrier** | /13 | US Rep WA-08, Energy & Commerce. |
| **Deb Krishnadasan** | /01 | 26th LD State Senator (appointed 2024). |
| **Jake Fey** | /13, /22 | State Rep D-27, **House Transportation chair** — transit funding gatekeeper. |
| **Bob Ferguson** | /13 | Governor — appoints judges, board members, agency heads. |
| **CommonSpirit Health** | /24 | VMFH's **actual owner** (Chicago). |
| **Wellfound Behavioral Health** | /24 | MultiCare–VMFH **competitor-collaboration JV**. |
| **WSHA / HHFPAC** | /08, /24 | The healthcare lobbying channel both systems use. |
| **Cheney Foundation** | /18 | Orphaned Erika Tucci's employer. |
| **Bates Technical College** | /23 | Orphaned Lin Zhou's employer. |
| **Tacoma Art Museum** | /18 | Ponepinto chairs it — cultural/symbolic capital. |
| **Museum of Glass** | /13 | Cultural power, Russell family legacy. |
| **Developers (Rush, Miles Sand & Gravel, Southport, Tucci, Lincoln Park, Nall)** | /13, /19 | The **growth-machine core**. |
| **Tacoma Housing Authority** | /13 | Hilltop redevelopment vehicle. |
| **Saltchuk** | /19 | Foss/Saltchuk parent. |
| **Teamsters** | /16 | Major labor power. |
| **SSMCP** | /09 | JBLM's key county-coordination vehicle. |
| **Northwest Seaport Alliance** | /01, /19 | Port's operating authority. |
| **Pierce County Library** | /25 | $56M independent taxing district. |
| **Flood Control Zone District** | /25 | County-wide flood taxing body. |
| **Tacoma Public Utilities** | /20 | Municipal utility, water power. |
| **Economic Development Board** | /14 | Chamber partner. |
| **Pierce Military & Business Alliance** | /09 | JBLM community nonprofit. |
| **Tacoma Weekly / Washington Observer** | /06 | Independent media (counter to Chatham). |

---

## 2. RELATIONSHIP AUDIT

Verdicts: **OK** = justified by evidence. **WRONG** = factually incorrect. **MISSING** = evidence supports but graph omits. **FILLER** = generic/padding edge with no documented relationship.

### 2.1 WRONG edges (factual errors — must fix)

| Edge | Problem | Evidence |
|---|---|---|
| `jim-kastama → county-council (member)` | Kastama is on **Puyallup City Council**, NOT Pierce County Council. | /02 |
| `anders-ibsen → county-council (mayor)` | Ibsen is **Tacoma Mayor**, not a Pierce County Council member. | /02 |
| `twina-nobles → puyallup-schools (board_member)` | Nobles is on **University Place** School District board, not Puyallup. | /17 |
| `catholic-archdiocese → vmfh (owns)` | VMFH is owned by **CommonSpirit Health (Chicago)**, not the Archdiocese. The Archdiocese relationship is religious sponsorship (Franciscan sisters), not ownership. | /24 |
| `weyerhaeuser → green-diamond (timber)` | **Separate, competing timber companies.** No ownership/relationship. | /19 |
| `gtcf → dona-ponepinto (board)` | Ponepinto is **NOT** on the GTCF board. The GTCF–United Way interlock is **Nathe Lawver**, not Ponepinto. | /18 |
| `keith-swank → county-council (appropriates)` | **Direction reversed.** The Council appropriates the budget TO the Sheriff, not vice versa. | /05 |
| `mary-robnett → county-council (appropriates)` | **Direction reversed.** Council appropriates to the PA's office. | /05 |
| `superior-court → county-council (appropriates)` | **Direction reversed.** Council appropriates to the court. | /05 |
| `district-court → county-council (appropriates)` | **Direction reversed.** Council appropriates to the court. | /05 |
| `linda-farmer → county-council (elected)` | Farmer is elected **by county voters**, not by the Council. Relationship mislabeled. | /01 |
| `marty-campbell → county-council (elected)` | Same — elected by voters, not the Council. | /01 |
| `bill-sterud` edge direction | `puyallup-tribe → bill-sterud (chairman)` — Sterud **leads** the tribe; direction should be person→org. | /03 |

### 2.2 FILLER / misleading edges (inflate centrality, no documented relationship)

| Edge | Problem | Evidence |
|---|---|---|
| `iheart → county-council (media)` | No documented relationship between iHeart and the Council. Padding that inflates Council degree. | /06 |
| `audacy → county-council (media)` | Same. | /06 |
| `lotus → county-council (media)` | Same. | /06 |
| `knkx → county-council (media)` | Same. | /06 |
| `columbia-bank → county-council (banking)` | Generic; no specific documented relationship. | /19 |
| `central-pierce-fire → county-council (consolidation)` | The fire merger is internal to fire districts, not a Council relationship. | /21 |
| `life-center → pierce-gop (aligned)` | No documented GOP alignment for Life Center. **UNVERIFIED.** | /13 |
| `life-center → county-council (influence)` | No documented direct influence. **UNVERIFIED.** | /13 |
| `catholic-archdiocese → county-council (influence)` | Weak; only indirect via VMFH lobbying. **UNVERIFIED.** | /13 |
| `healthy-bay → weyerhaeuser (holds_accountable)` | CHB monitors Superfund cleanup; Weyerhaeuser is a historical polluter, but the specific CHB–Weyerhaeuser relationship is not directly cited. **UNVERIFIED.** | /20 |
| `state_funding` edges (8 legislators → county-council) | Direction questionable — legislators appropriate state funds that flow to the county, but the relationship is generic. | /13 |
| `levy_funding` edges (4 school districts → county-council) | School districts levy their **own** taxes; the county collects but doesn't fund them. Misleading. | /17 |
| `federal_funding` edges (4 federal → county-council) | Generic; the real relationship is via appropriations committees, not the Council. | /13 |

### 2.3 MISSING edges (evidence supports, graph omits)

| Missing edge | Evidence |
|---|---|
| `master-builders → paul-herrera (donated)` | /04 — $2,400 to Herrera. |
| `john-wiborg → gtcf (former_board)` | /08 — Wiborg was a GTCF board member. |
| `john-wiborg → uw-tacoma` | /08 — UW Tacoma Milgard Business Leader of the Year. |
| `dona-ponepinto → tacoma-art-museum (president)` | /18 — she chairs TAM. |
| `nathe-lawver → gtcf (board)` + `nathe-lawver → united-way (chair)` | /18 — the critical labor-civic interlock. |
| `andrew-strobel → tcc (board)` + `andrew-strobel → ryan-mello (advisor)` + `andrew-strobel → puyallup-tribe (former)` | /23. |
| `lois-bernstein → tcc (board)` + `lois-bernstein → multicare (exec)` | /23. |
| `jason-thompson → multicare (board)` + `jason-thompson → russell-invest` | /08. |
| `dale-sowell → multicare (board)` + `dale-sowell → green-diamond` | /08. |
| `diann-puls → weyerhaeuser (former)` | /24 — Puls is the actual Weyerhaeuser tie, not an org-to-org edge. |
| `multicare → wellfound (jv)` + `vmfh → wellfound (jv)` | /24 — the competitor-collaboration. |
| `vmfh → commonspirit (owned_by)` | /24 — the real ownership. |
| `multicare → wsha (member)` + `vmfh → wsha (member)` | /08, /24. |
| `puyallup-tribe → ryan-mello (donated)` | /04 — $2,400 to Mello (already present, OK). |
| `puyallup-tribe → amy-cruver` / `→ jani-hitchen` / `→ rosie-ayala` | /04 — Tribe donated to all three council races. |
| `ilwu23 → jani-hitchen (donated)` | /04 — ILWU Local 23 State PAC $2,400 to Hitchen. |
| `tom-pierson → pierce-county-econ-dev (acting_director)` | /14, /27 — the revolving-door edge. |
| `ryan-mello → gtcf (former_board)` | /18 — Mello moved GTCF→Exec. |
| `rosie-ayala → gtcf (board)` | /18 — already present, OK. |
| `jt-wilcox → pierce-gop (former)` | /01 — ex-State House GOP Leader. |
| `jblm → ssmcp` + `county-council → ssmcp` | /09 — the coordination vehicle. |
| `port-tacoma → nwsa` | /01, /19. |
| `foss-family → saltchuk` | /19. |
| `chamber → candidate-academy` (pipeline to candidates) | /14 — the shadow-party mechanism. |

---

## 3. POWER-RANKING AUDIT (computed composite vs evidence/12 power matrix)

The composite (35% wdeg + 25% btw + 20% eig + 20% PageRank) was recomputed from the graph. **The ranking diverges sharply from the evidence-based power matrix in /12.**

| Computed rank | Node | /12 matrix rank | Verdict |
|---|---|---|---|
| 1 | County Council (1.000) | 2 | **OVER-RANKED.** Council's 184 weighted degree is inflated by the FILLER edges (media, state_funding, appropriates). /12 ranks Mello #1. |
| 2 | Ryan Mello (0.441) | 1 | **UNDER-RANKED.** The actual executive. /12 puts him #1. |
| 3 | Pierce Dems (0.426) | 14 | **GROSSLY OVER-RANKED.** The party node collects all legislator `member` edges — a structural artifact, not real power. /12 ranks Dems #14. |
| 4 | MultiCare (0.366) | 4 | OK. |
| 5 | Port of Tacoma (0.358) | 6 | OK. |
| 6 | Chamber (0.333) | — (scored CRITICAL in /13) | **UNDER-RANKED.** /13 and /27 both say the Chamber is the most powerful unelected actor; its power is agenda/narrative, not centrality. |
| 7 | Pierce GOP (0.330) | 13 | **OVER-RANKED.** Same party-node artifact as Dems. |
| 8 | Superior Court (0.306) | — | **OVER-RANKED.** Inflated by reversed `appropriates` edges. |
| 9 | Rosie Ayala (0.299) | — | Reasonable (GTCF + Transit + Council). |
| 10 | Tacoma Public Schools (0.295) | — | Reasonable. |
| 11 | Puyallup Tribe (0.293) | 3 | **GROSSLY UNDER-RANKED.** /12 ranks the Tribe #3 (most powerful non-gov actor). Its power is **sovereignty/veto**, not centrality. /27 explicitly warns the composite underweights this. |
| 12 | Keith Swank (0.289) | 7 | **UNDER-RANKED.** /12 ranks him #7. His power is legal autonomy, not centrality. |
| 14 | JBLM (0.276) | 5 | **GROSSLY UNDER-RANKED.** /12 ranks JBLM #5. Only 3 edges. Veto/structural power. |
| 19 | Mary Robnett (0.260) | 8 | **UNDER-RANKED.** /12 ranks her #8. |
| 20 | Communities for a Healthy Bay (0.259) | — | **GROSSLY OVER-RANKED.** A counter-power environmental org at #20? Inflated by 3 edges. |
| 24 | Catholic Archdiocese (0.250) | — | **OVER-RANKED.** Weak evidence. |
| 25 | Dona Ponepinto (0.249) | — | **UNDER-RANKED.** /27 flags her as a key interlock. |
| 41 | Kelly Chambers (0.242) | 10 | **UNDER-RANKED.** /12 ranks her #10. |
| 58 | John Wiborg (0.229) | 11 | **UNDER-RANKED.** /12 ranks him #11. The interlock economy is underweighted. |
| 67 | John McCarthy (0.224) | 12 | **UNDER-RANKED.** /12 ranks him #12. |
| 70 | LTG McFarlane (0.222) | 22 | **UNDER-RANKED.** |
| 71 | Bill Sterud (0.221) | 23 | **UNDER-RANKED.** |
| 74 | News Tribune (0.217) | 15 | **UNDER-RANKED.** /12 ranks it #15. |
| 111 | Erika Tucci (0.000) | — | **STRUCTURAL FLAW.** Isolated node, zero score. |
| 112 | Lin Zhou (0.000) | — | **STRUCTURAL FLAW.** Isolated node, zero score. |

**Bottom line:** The composite is a **network-centrality measure, not a power measure.** It systematically over-ranks hubs (Council, party nodes, courts) and under-ranks veto/structural actors (Tribe, JBLM, Sheriff, Chamber, interlock nodes). This is exactly the limitation /27 predicted. **Do not use the raw composite as the final ranking.**

---

## 4. CRITICAL GAPS (ranked by severity)

### #1 — The growth-machine coalition is entirely unmapped (CRITICAL)
The investigation's core thesis (evidence/28) is that Pierce County is a **growth machine** — developers + realtors + banks + media + Chamber converting public land/tax revenue into private wealth. The graph has NASH Cascadia and Master Builders but **no individual developers, no realtors PAC, no Southport, no Rush, no Miles Sand & Gravel, no Tucci, no Lincoln Park, no Nall** — all named in /13 and /19 as the growth-machine core.
**Add:** nodes for Rush Development, Miles Sand & Gravel, Southport Real Estate, Tucci & Sons, Lincoln Park Partners, Nall Capital, WA Realtors PAC; edges `developer → chamber (member)`, `developer → candidate (donated)` using /04 donor data.

### #2 — The money→people→systems loop is not visible (CRITICAL)
Evidence/28's structural-capture loop (government-created wealth → private power → policy → more wealth) is **absent from the graph.** There are no edges encoding the SOURCE of economic power.
**Add:** `jblm ← federal-appropriations`, `multicare ← tax-exemption/medicare`, `puyallup-tribe ← sovereignty/gaming-compact`, `weyerhaeuser ← federal-land-grant`, `port-tacoma ← property-tax-levy`, `chamber ← tax-exempt-status`. These are the edges that make the thesis visible.

### #3 — Nathe Lawver, the labor-civic interlock, is missing (CRITICAL)
Evidence/18 and /27 both name Lawver as the single most important bridge between organized labor and philanthropic power (GTCF board + United Way board chair + Building Trades exec secretary). He is not in the graph.
**Add:** node `nathe-lawver`; edges `nathe-lawver → gtcf (board)`, `nathe-lawver → united-way (chair)`, `nathe-lawver → pclc (exec)`.

### #4 — The revolving door is not mapped (CRITICAL)
Evidence/27 documents the revolving door as "the real pipeline": Pierson (Chamber CEO + Acting County Economic Development Director), Mello (GTCF→Exec), Ayala (GTCF→Council), Wilcox (State House→Port), Ponepinto (7+ boards). The graph captures none of these as edges.
**Add:** `tom-pierson → pierce-county-econ-dev (acting_director)`, `ryan-mello → gtcf (former_board)`, `jt-wilcox → pierce-gop (former)`.

### #5 — Veto power is not scored (HIGH)
Evidence/27 explicitly says the composite underweights veto power. The Tribe (#11), JBLM (#14), MultiCare, and the Sheriff are all under-ranked because their power is the ability to block, not centrality.
**Add:** a veto-power dimension to the score, or at minimum flag these nodes as veto actors in the HTML.

### #6 — Missing federal delegation members (HIGH)
Evidence/13 names **Adam Smith** (Ranking Member Armed Services — JBLM's champion) and **Kim Schrier** (Energy & Commerce) as key external actors. The graph has Cantwell, Murray, Randall, Strickland but not Smith or Schrier.
**Add:** `adam-smith`, `kim-schrier`; edge `adam-smith → jblm (armed-services-champion)`.

### #7 — Missing state delegation (HIGH)
Evidence/13 and /22 name **Jake Fey** (House Transportation chair — transit funding gatekeeper) and **Deb Krishnadasan** (26th LD senator). The graph omits both, and lists **Steve Conway** who did not seek re-election (evidence/01).
**Add:** `jake-fey`, `deb-krishnadasan`; remove or flag Conway.

### #8 — Missing Governor Ferguson (HIGH)
Evidence/13: the Governor appoints judges, board members, agency heads, and appointed Doris Walkins to Superior Court. Not in graph.
**Add:** `bob-ferguson`; edges to judicial appointments, TCC/Bates trustees.

### #9 — Missing CommonSpirit and Wellfound (HIGH)
Evidence/24: VMFH is owned by **CommonSpirit** (Chicago), and MultiCare + VMFH jointly own **Wellfound Behavioral Health**. The graph has the wrong `catholic-archdiocese → vmfh (owns)` edge and no Wellfound.
**Add:** `commonspirit`, `wellfound`; fix the ownership edge; add `multicare → wellfound (jv)` + `vmfh → wellfound (jv)`.

### #10 — Missing WSHA / HHFPAC (HIGH)
Evidence/08 and /24: both hospital systems lobby through WSHA's HHFPAC. The graph has no healthcare lobbying channel.
**Add:** `wsha`, `hhfpac`; edges `multicare → wsha`, `vmfh → wsha`.

### #11 — Orphaned nodes (HIGH)
Erika Tucci and Lin Zhou are in the graph with **zero edges** and score 0.000. Their employers (Cheney Foundation, Bates Tech) are missing.
**Add:** `cheney-foundation`, `bates-tech`; edges `erika-tucci → cheney-foundation (ed)`, `lin-zhou → bates-tech (president)`.

### #12 — Missing cultural/symbolic capital (MEDIUM)
Evidence/18 and /13: Tacoma Art Museum (Ponepinto chairs it), Museum of Glass (Russell legacy). These are the Bourdieu "symbolic capital" machines that convert economic power into legitimacy.
**Add:** `tacoma-art-museum`, `museum-of-glass`; edges to Ponepinto, Russell family.

### #13 — Missing special districts (MEDIUM)
Evidence/25: Pierce County Library ($56M), Flood Control Zone District, water districts. All independent taxing bodies.
**Add:** `pierce-county-library`, `flood-control-zone-district`.

### #14 — Missing school districts (MEDIUM)
Evidence/17 maps 14 districts; the graph has only 4. Missing Sumner-Bonney Lake (Laurie Dent, $114M bond), University Place ($355M construction), Franklin Pierce, Peninsula.
**Add:** at minimum `sumner-bonney-lake-schools`, `university-place-schools`.

### #15 — Missing fire districts (MEDIUM)
Evidence/21 maps 20+ fire districts; the graph has only West and Central. Missing East Pierce ($80M bond), Gig Harbor, South Pierce.
**Add:** `east-pierce-fire`, `gig-harbor-fire`.

---

## 5. STRUCTURAL-INSIGHT GAPS (what's missing to make the loop visible)

The investigation's thesis (evidence/28) is a **four-step feedback loop**:
1. **Government creates wealth** — land grants, appropriations, tax exemptions, sovereignty, public levies.
2. **Private actors convert it to power** — timber fortunes, hospital empires, tribal gaming, business coalitions.
3. **That power influences government** — lobbying, campaign donations, Chamber Candidate Academy, board interlocks, revolving door.
4. **Government returns the favor** — more tax breaks, contracts, favorable regulation, land-into-trust, deference.

**The graph captures steps 2 and 3 partially, but steps 1 and 4 are invisible.** Specifically:

- **Step 1 (government→wealth) is absent.** No edges show JBLM's federal appropriations, MultiCare's tax exemption, the Tribe's gaming compact, Weyerhaeuser's land grant, the Port's property levy, or the Chamber's tax-exempt status. Without these, the "private" actors look like independent capital — which is exactly the false impression /28 warns against.
- **Step 4 (policy→wealth) is absent.** No edges show contracts, land-use approvals, tax breaks, or land-into-trust flowing back to the elite. The Tideflats subarea plan, the PLU-MultiCare medical center land-use amendment, the school construction bonds — none are edges.
- **The Chamber's Candidate Academy is not an edge.** Evidence/14 calls it the shadow-party mechanism that trains and vets candidates. This is the clearest private→political pipeline in the county and it's not in the graph.
- **The revolving door is not an edge.** Evidence/27 calls it "the real pipeline." Pierson's dual role (Chamber CEO + Acting County Economic Development Director) is the single most damning fact in the evidence and it's not represented.
- **The interlock economy is underweighted.** Wiborg, Ponepinto, Lawver, Thompson, Sowell, Bernstein, Strobel — the people who sit on both government-facing and private-facing boards — are the "most powerful actors" per /28, yet they rank in the bottom half of the composite.

**To make the loop visible, the HTML rebuild must add:**
1. A **"source of wealth" edge type** (government grant → private actor) for the six entities in /28.
2. A **"revolving door" edge type** (person holds positions in ≥2 of government/business/philanthropy/labor).
3. A **"growth machine" cluster** (developers + realtors + banks + media + Chamber).
4. A **"policy return" edge type** (contracts, land use, tax breaks flowing back).
5. A **veto-power dimension** so the Tribe, JBLM, MultiCare, and the Sheriff rank where the evidence puts them.

---

## 6. SUMMARY OF REQUIRED FIXES

| Category | Count | Detail |
|---|---|---|
| **Wrong edges to fix** | 12 | Kastama, Ibsen, Nobles, Archdiocese-owns-VMFH, Weyerhaeuser-GreenDiamond, GTCF-Ponepinto, 4 reversed `appropriates`, 2 mislabeled `elected`, Sterud direction. |
| **Filler edges to remove/relabel** | 12 | 4 media→council, Columbia Bank→council, Central Pierce→council, Life Center×2, Archdiocese→council, CHB→Weyerhaeuser, state/federal/levy funding generic edges. |
| **Missing nodes to add** | 30+ | Lawver, Strobel, Bernstein, Thompson, Sowell, 3 Port commissioners, Smith, Schrier, Krishnadasan, Fey, Ferguson, CommonSpirit, Wellfound, WSHA, HHFPAC, Cheney Fdn, Bates, TAM, MOG, developers, THA, Saltchuk, Teamsters, SSMCP, NWSA, library, flood control, TPU, EDB, PMBA, independent media. |
| **Missing edges to add** | 25+ | Master Builders→Herrera, Wiborg interlocks, Ponepinto→TAM, Lawver interlocks, Strobel/Bernstein/Thompson/Sowell, Wellfound JV, CommonSpirit ownership, WSHA membership, Tribe→council races, ILWU→Hitchen, Pierson revolving door, Mello→GTCF, Wilcox→GOP, SSMCP, NWSA, Saltchuk, Candidate Academy. |
| **Ranking corrections** | 15+ | Tribe #3, JBLM #5, Chamber, Swank #7, Robnett #8, Chambers #10, Wiborg #11, McCarthy #12, News Tribune #15 — all under-ranked by the composite. Council, Dems, GOP, Superior Court, CHB over-ranked. |

**Bottom line:** The graph is a defensible **formal-structure skeleton** but it is not yet a **power map**. It will mislead the HTML rebuild unless the wrong edges are fixed, the filler edges removed, the growth-machine coalition and revolving door added, and the ranking corrected to weight veto/structural power. The evidence to do all of this is already in files /01–/28.
