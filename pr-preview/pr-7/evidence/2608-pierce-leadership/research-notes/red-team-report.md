# RED-TEAM REPORT — INV-2026-002 (Pierce County Leadership)

**Red-team operating assumption:** EVERYTHING in this investigation is wrong. Every claim was attacked against primary sources (.gov, Ballotpedia, Wikipedia, WA PDC, IRS 990s via ProPublica, Fitch, org websites, court/AG records). Only claims that survived are kept.
**Verification date:** 2026-09-09
**Method:** Independent web_search/web_extract against primary sources. Evidence files were treated as hostile/untrusted.

---

## VERDICT SUMMARY

**The investigation survives its attack substantially intact — roughly 80% of the core factual claims are CONFIRMED against primary sources.** The formal power structure (Mello, Council 4D-3R, Swank, Robnett), the major dollar figures (JBLM $12.1B, MultiCare $7.2B, County $3.5B, Weyerhaeuser 10.4M acres, Port cargo, Chamber $3M, Pierce Transit $345M), the campaign-finance numbers, the entity roster, and the audit's 12 edge corrections all check out.

**What is WRONG or WEAK:**
1. **The composite power score is a network-centrality measure, not a power measure.** It systematically over-ranks hubs (Council, party nodes, courts) and under-ranks veto/structural actors (Tribe, JBLM, Sheriff, Chamber). The audit itself concedes this. The ranking in evidence/12 is a defensible *qualitative* ranking; the graph's computed composite is not.
2. **The structural-capture thesis overreaches.** The underlying facts (federal appropriations, tax exemption, sovereignty, land grant, public levy) are all real and verified. But the conclusion that "the private sector is a government-created rentier class" is editorializing, not evidence. The "growth machine" is a recognized academic lens (Logan & Molotch) but the evidence shows overlapping interests, not a proven coordinated machine.
3. **Several dollar figures are mischaracterized** (Puyallup "$162M assets" is actually the 1990 settlement; JBLM "$12.1B" is a combined Pierce+Thurston multiplier figure; "Tacoma Schools $1B+ levy" is not supported).
4. **Domain assignments are contestable** (Port should be government, not economic; Tribe/Chamber/MultiCare are borderline).
5. **The graph has real bugs** the audit caught: duplicate/contradictory Sterud edges, reversed `appropriates` edges, wrong `elected` edges, and the Puyallup chairman rotates annually (Sterud ↔ Bean).

---

## CONFIRMED CLAIMS (survived attack — each with primary source)

| Claim | Primary source |
|---|---|
| Ryan Mello is County Executive, elected 2024, general margin 51.28%–48.58% | https://en.wikipedia.org/wiki/2024_Pierce_County_Executive_election ; https://ballotpedia.org/Ryan_Mello_(Pierce_County_Executive,_Washington,_candidate_2024) |
| Mello took office Jan 2025; first openly-gay WA county exec | https://www.piercecountywa.gov/8703/Biography |
| Pierce County Council is 7 members, 4D-3R; members Morell(R-1), Herrera(R-2), Cruver(R-3), Ayala(D-4), Yambe(D-5), Hitchen(D-6), Denson(D-7) | https://www.piercecountywa.gov/99/Pierce-County-Council ; https://en.wikipedia.org/wiki/Pierce_County_Council |
| Keith Swank is Sheriff (since 2025); Mary Robnett is Prosecuting Attorney (since 2019) | https://www.piercecountywa.gov/126/Meet-Your-Sheriff ; https://www.piercecountywa.gov/3560/About-Mary-Robnett |
| JBLM economic impact ~$12.1B (UW Tacoma study, Pierce+Thurston combined) | https://cityoflakewood.us/jblm-economic-impact |
| MultiCare revenue ~$7.2B FY2025 (Fitch) | https://www.fitchratings.com/research/us-public-finance/fitch-affirms-multicare-healthcare-system-wa-at-a-outlook-stable-11-06-2026 |
| Puyallup Tribe 1990 settlement = $162M cash/real estate/programs + 900 acres | https://www.latimes.com/archives/la-xpm-1990-03-24-mn-680-story.html ; https://www.historylink.org/File/7969 |
| Weyerhaeuser owns/controls ~10.4M acres U.S. timberlands (still accurate, largest private owner) | https://investor.weyerhaeuser.com/2025-10-30-Weyerhaeuser-Provides-Update-on-Timberlands-Portfolio-Optimization-Actions |
| Weyerhaeuser 1900 purchase: 900,000 acres from Northern Pacific for $6/acre ($5.4M) | https://www.historylink.org/file/5241 ; https://foresthistory.org/wp-content/uploads/2016/12/stillgrowing-after-100-years.pdf |
| NWSA handled nearly $76B waterborne trade in 2024 (note: ~$68B in 2025) | https://www.nwseaportalliance.com/about-us/cargo-statistics |
| Pierce County 2026-27 biennial budget = $3.5B, adopted Nov 25, 2025 | https://www.piercecountywa.gov/8875/2026-2027-Biennial-Budget-Development |
| Sheriff budget $406M (LE $242.2M + Corrections $164.3M = 42% of GF); ~76-77% of GF to law/justice | https://www.piercecountywa.gov/CivicSend/ViewMessage/message/277287 ; https://www.govtech.com/em/safety/pierce-county-wash-earmarks-77-of-budget-for-public-safety |
| Mello raised ~$510K, Chambers ~$550K, Swank ~$121K (PDC) | https://www.pdc.wa.gov/political-disclosure-reporting-data/browse-search-data/candidates/93053 (Mello); PDC candidate pages for Chambers/Swank |
| Chamber revenue $3.08M FY2024 (501(c)(6)) | https://projects.propublica.org/nonprofits/organizations/910434830 |
| Pierce Transit 2026 adopted budget ~$345M | https://piercetransit.org/wp-content/uploads/2025/2026-Adopted-Budget.pdf |
| Port of Tacoma is an independent municipal corporation under RCW Title 53, 5 county-wide elected commissioners | https://www.portoftacoma.com/commission ; https://app.leg.wa.gov/rcw/default.aspx?Cite=53 |
| VMFH is owned by/affiliated with CommonSpirit Health (Chicago) | https://www.vmfh.org/about-vmfh ; https://en.wikipedia.org/wiki/Virginia_Mason_Medical_Center |
| Jim Kastama is on Puyallup City Council (D1), NOT Pierce County Council | https://www.puyallupwa.gov/634/District-1---Jim-Kastama |
| T'wina Nobles is on University Place School Board (and 28th LD Senator) | https://senatedemocrats.wa.gov/nobles/biography |
| Nathe Lawver is the GTCF–United Way interlock (UWPC Board Chair + GTCF board + Building Trades exec sec) | https://www.uwpc.org/board-directors ; https://www.gtcf.org/blog/profile/nathe-lawver |
| Steve Conway (D-29) announced Jan 21, 2026 he will NOT seek re-election | https://senatedemocrats.wa.gov/conway/2026/01/21/sen-conway-announces-he-will-not-seek-re-election ; https://ballotpedia.org/Steve_Conway |
| Deb Krishnadasan is 26th LD Senator (appointed Dec 2024) | https://ballotpedia.org/Deborah_Krishnadasan |
| Jake Fey is 27th LD Rep, House Transportation Chair | https://jakefey.com ; https://housedemocrats.wa.gov/fey/news |
| Adam Smith WA-09, Kim Schrier WA-08, Emily Randall WA-06, Marilyn Strickland WA-10 | https://www.narfe.org/wa/resources/links/congress-contact |
| Chris Gildon (R-25), Phil Fortunato (R-31), Yasmin Trudeau (D-27), Laurie Jinkins (Speaker), Drew Stokesbary (Minority Leader), Melanie Morgan (D-29) | https://leg.wa.gov/legislators ; https://leg.wa.gov/media/0pvgo5ic/2025-26-committee-assignment-telephone-directory.pdf |
| Tom Pierson (Chamber CEO) appointed Acting Director of Economic Development for Pierce County (revolving door) | https://www.linkedin.com/in/tom-pierson-a2808912 |
| Bill Sterud on Puyallup Tribal Council since 1978 (chairman rotates annually) | https://www.puyalluptribe-nsn.gov/council_member/bill-sterud |

---

## WRONG CLAIMS (proven false — correct fact + source)

| Investigation claim | Correct fact | Source |
|---|---|---|
| **"Puyallup Tribe $162M+ assets"** (task framing) | $162M is the **1990 land-claims settlement**, not current assets. Current tribal assets are not publicly stated at $162M. | https://www.latimes.com/archives/la-xpm-1990-03-24-mn-680-story.html |
| **"Tacoma Schools $1B+ levy"** (task framing) | Tacoma's Feb 2026 EP&O levy funds ~$120M/yr (4-yr avg); the $650M figure was the **2024 bond**, not a $1B levy. No $1B+ Tacoma levy exists. | https://www.tacomaschools.org/about/bond/february-10-2026-election ; https://www.thenewstribune.com/news/local/education/article284320308.html |
| **JBLM "$12.1B economic impact"** presented as Pierce County | The $12.1B is a **combined Pierce + Thurston counties** multiplier figure (UW Tacoma study). Pierce-only direct impact is ~$3.9B output / $3.6B labor income. | https://www.ssmcp.org/wp-content/uploads/2023/10/REIA-2023-Pierce-Thurston-as-of-09272023.pdf ; https://www.southsoundbiz.com/news/jblm-study-thurston-pierce-county/article_7adfd7de-2688-11ee-abc5-1b8e8d3f57a2.html |
| **Graph edge `jim-kastama → county-council (member)`** | Kastama is on Puyallup City Council, not Pierce County Council. | https://www.puyallupwa.gov/634/District-1---Jim-Kastama |
| **Graph edge `anders-ibsen → county-council (mayor)`** | Ibsen is Tacoma Mayor, not a Pierce County Council member. | https://tacoma.gov/government/departments/mayor |
| **Graph edge `twina-nobles → puyallup-schools (board_member)`** | Nobles is on University Place School Board, not Puyallup. | https://senatedemocrats.wa.gov/nobles/biography |
| **Graph edge `catholic-archdiocese → vmfh (owns)`** | VMFH is owned by CommonSpirit Health (Chicago); Archdiocese relationship is religious sponsorship, not ownership. | https://www.vmfh.org/about-vmfh |
| **Graph edge `weyerhaeuser → green-diamond (timber)`** | Separate, competing timber companies; no ownership relationship. | https://investor.weyerhaeuser.com/2025-10-30-Weyerhaeuser-Provides-Update-on-Timberlands-Portfolio-Optimization-Actions |
| **Graph edge `gtcf → dona-ponepinto (board)`** | Ponepinto is NOT on GTCF board; the GTCF–United Way interlock is Nathe Lawver. | https://www.uwpc.org/board-directors ; https://www.gtcf.org/blog/profile/nathe-lawver |
| **Graph edges `keith-swank/mary-robnett/superior-court/district-court → county-council (appropriates)`** | Direction reversed — the Council appropriates the budget TO the Sheriff/PA/courts. | https://www.piercecountywa.gov/8875/2026-2027-Biennial-Budget-Development |
| **Graph edges `linda-farmer/marty-campbell → county-council (elected)`** | Both are elected by county voters, not by the Council. | https://www.piercecountywa.gov/8103/About-Auditor-Linda-Farmer |
| **Graph duplicate `puyallup-tribe → bill-sterud` AND `bill-sterud → puyallup-tribe`** | Contradictory duplicate pair; Sterud leads the tribe (person→org direction correct). | https://www.puyalluptribe-nsn.gov/council_member/bill-sterud |
| **Graph lists Sterud as "Puyallup Tribal Chairman" (static)** | Chairman rotates annually; David Z. Bean has served as chairman (Sterud vice chairman) in recent years. | https://www.puyalluptribe-nsn.gov/news/david-z-bean-elected-chairman-of-tribal-council-bill-sterud-elected-vice-chairman |

---

## UNVERIFIABLE / WEAK CLAIMS

| Claim | What's needed to verify |
|---|---|
| **MultiCare "$357K via HHFPAC against Democratic candidates in 2022"** | The $357K figure is attributed to HHFPAC (WSHA PAC) spending, not MultiCare directly. MultiCare has no standalone PAC; its giving flows through WSHA/HHFPAC. Needs a PDC C4 report pull to confirm the exact $357K and the "against Democrats" characterization. |
| **Puyallup Tribe "largest lobbying spender in Pierce County"** | Federal lobbying is verifiable ($270K in 2024 per OpenSecrets), but "largest in Pierce County" needs a county-wide PDC lobbying comparison. | 
| **"Chamber = shadow political party"** | The Chamber officially states it does not endorse candidates. The Candidate Academy, Voters Guide, and Candidates Forum are real, but "shadow party" is an analytical characterization, not a fact. |
| **"Growth machine" as a coordinated coalition** | Developers, realtors, banks, and Chamber share overlapping interests (documented via PDC donors), but no evidence proves a coordinated, self-aware "machine." |
| **Bruce Dammeier "still embedded in Republican donor network"** | Analytical assessment; not directly sourceable. |
| **Swank's birth location (Silver Spring, MD) / high school** | Not on campaign or official sites. |
| **Exact current committee chairs for county council committees** | Not verified for current session. |
| **MultiCare "largest private employer in Pierce County"** | Plausible and widely stated, but no single authoritative headcount for Pierce County specifically (30,000 is system-wide across 3 states). |

---

## ENTITY CORRECTIONS

| Node | Issue | Fix |
|---|---|---|
| **port-tacoma** | Domained `economic`; it is a **public municipal corporation** (RCW Title 53) funded partly by property tax levy, with elected commissioners. | Re-domain to **government** (or dual-tag government/economic). Evidence/28 itself calls it public. |
| **puyallup-tribe** | Domained `institutional`; evidence/12 scores Economic 9, Institutional 9. Gaming is its biggest lever. | Defensible either way; recommend **economic** (or dual-tag) given Emerald Queen Casino is the primary revenue engine. |
| **chamber** | Domained `economic`; it's a 501(c)(6) whose power is political (Candidate Academy, Voters Guide). | Defensible as economic, but its influence is political — recommend dual-tag or note in desc. |
| **multicare** | Domained `institutional`; evidence/12 scores Economic 9, Institutional 8. | Defensible; largest private employer. Keep institutional but note economic weight. |
| **chatham-am** | Domained `economic`; its power is **media** (owns McClatchy/News Tribune). | Re-domain to **media**. |
| **bill-sterud** | Labeled "Puyallup Tribal Chairman" (static); chairman rotates annually. | Update desc to note rotating chairmanship (Sterud ↔ Bean). |
| **steve-conway** | Listed as current D-29 Senator; he announced Jan 2026 he will not seek re-election (term ends Jan 2027). | Flag as "retiring — not seeking re-election 2026." |
| **jt-wilcox** | Listed as Port Commissioner (correct) but evidence/01 notes his State House term ended Jan 2025. | Confirm he's on Port Commission (verified), not a current state legislator. |
| **New nodes (Lawver, Strobel, Bernstein, Thompson, Sowell, Marzano, Keller, Ang, Smith, Schrier, Krishnadasan, Fey, Ferguson, CommonSpirit, Wellfound, WSHA, HHFPAC, Cheney Fdn, Bates, TAM, MOG, developers, Saltchuk, NWSA, SSMCP, PMBA, Tacoma Weekly)** | All are real entities/people. | Keep — verified real. |

---

## EDGE CORRECTIONS

**Wrong edges (fix):**
- `jim-kastama → county-council` → change to `jim-kastama → puyallup-city-council` (or remove; he's not a county council member).
- `anders-ibsen → county-council` → change to `anders-ibsen → tacoma-city` (mayor).
- `twina-nobles → puyallup-schools` → change to `twina-nobles → university-place-schools`.
- `catholic-archdiocese → vmfh (owns)` → replace with `vmfh → commonspirit (owned_by)`.
- `weyerhaeuser → green-diamond (timber)` → remove (separate companies).
- `gtcf → dona-ponepinto (board)` → replace with `nathe-lawver → gtcf (board)` + `nathe-lawver → united-way (chair)`.
- 4 reversed `appropriates` edges → reverse direction: `county-council → keith-swank/mary-robnett/superior-court/district-court (appropriates)`.
- 2 `elected` edges (Farmer, Campbell) → relabel as `elected_by_voters`, not `→ county-council`.
- Duplicate `puyallup-tribe → bill-sterud` + `bill-sterud → puyallup-tribe` → keep only `bill-sterud → puyallup-tribe (chairman)`.

**Filler/misleading edges (remove or relabel):**
- `iheart/audacy/lotus/knkx → county-council (media)` — no documented relationship.
- `columbia-bank → county-council (banking)` — generic.
- `central-pierce-fire → county-council (consolidation)` — internal to fire districts.
- `life-center → pierce-gop` and `life-center → county-council` — UNVERIFIED.
- `catholic-archdiocese → county-council (influence)` — weak.
- `healthy-bay → weyerhaeuser (holds_accountable)` — not directly cited.
- Generic `state_funding`/`federal_funding`/`levy_funding` edges to county-council — misleading; the real relationships are via appropriations committees and the districts' own levies.

**Missing edges (add — all evidence-supported):**
- `master-builders → paul-herrera (donated)` — $2,400 (PDC).
- `john-wiborg → gtcf (former_board)`, `john-wiborg → uw-tacoma`.
- `dona-ponepinto → tacoma-art-museum (president)`.
- `nathe-lawver → gtcf (board)` + `nathe-lawver → united-way (chair)` + `nathe-lawver → pclc (exec)`.
- `andrew-strobel → tcc/ryan-mello/puyallup-tribe`; `lois-bernstein → tcc/multicare`; `jason-thompson → multicare/russell-invest`; `dale-sowell → multicare/green-diamond`.
- `diann-puls → weyerhaeuser (former)` (the real Weyerhaeuser tie).
- `multicare → wellfound (jv)` + `vmfh → wellfound (jv)`; `vmfh → commonspirit (owned_by)`.
- `multicare → wsha (member)` + `vmfh → wsha (member)`; `wsha → hhfpac`.
- `puyallup-tribe → amy-cruver/jani-hitchen/rosie-ayala (donated)` — PDC.
- `ilwu23 → jani-hitchen (donated)` — PDC.
- `tom-pierson → pierce-county-econ-dev (acting_director)` — revolving door.
- `ryan-mello → gtcf (former_board)` — revolving door.
- `jt-wilcox → pierce-gop (former)`.
- `jblm → ssmcp` + `county-council → ssmcp`; `port-tacoma → nwsa`; `foss-family → saltchuk`.
- `chamber → candidate-academy` (pipeline).
- **Money-source edges (the thesis's step 1):** `jblm ← federal-appropriations`, `multicare ← tax-exemption/medicare`, `puyallup-tribe ← sovereignty/gaming-compact`, `weyerhaeuser ← federal-land-grant`, `port-tacoma ← property-tax-levy`, `chamber ← tax-exempt-status`. These make the structural-capture loop visible.

---

## RANKING CORRECTIONS

The evidence/12 qualitative ranking (Mello #1, Council #2, Tribe #3, MultiCare #4, JBLM #5, Port #6, Swank #7, Robnett #8) is **defensible and survives**. The graph's **computed composite** (35% wdeg + 25% btw + 20% eig + 20% PageRank) does NOT survive as a power ranking:

| Computed rank | Node | Problem | Fix |
|---|---|---|---|
| 1 | County Council | Over-ranked — inflated by filler edges (media, state_funding, appropriates). | Remove filler edges; Council should be #2. |
| 3 | Pierce Dems | Grossly over-ranked — party node collects all legislator `member` edges (structural artifact). | Cap party-node aggregation or remove legislator→party edges. |
| 7 | Pierce GOP | Same party-node artifact. | Same fix. |
| 8 | Superior Court | Over-ranked — inflated by reversed `appropriates` edges. | Fix edge direction. |
| 11 | Puyallup Tribe | Grossly under-ranked (#3 in evidence/12). Power is sovereignty/veto, not centrality. | Add veto-power dimension. |
| 14 | JBLM | Grossly under-ranked (#5). Only 3 edges. | Add veto/structural weight. |
| 7 | Swank | Under-ranked (#7 in evidence/12). Legal autonomy, not centrality. | Add veto/legal weight. |
| 8 | Robnett | Under-ranked (#8). | Add legal weight. |
| 6 | Chamber | Under-ranked (evidence/13 scores CRITICAL). Agenda/narrative power. | Add agenda/narrative dimension. |
| 41 | Kelly Chambers | Under-ranked (#10). | — |
| 58 | John Wiborg | Under-ranked (#11). Interlock economy underweighted. | Add interlock edges. |
| 67 | John McCarthy | Under-ranked (#12). | — |
| 111/112 | Erika Tucci / Lin Zhou | Zero score — isolated nodes (structural flaw). | Add employer edges (Cheney Fdn, Bates Tech). |

**Bottom line:** Do NOT use the raw composite as the final ranking. Use the evidence/12 qualitative matrix, and add a veto-power/structural dimension so the Tribe, JBLM, Sheriff, and Chamber rank where the evidence puts them.

---

## THESIS ASSESSMENT

**The structural-capture thesis survives in its factual core but overreaches in its conclusion.**

**What is CONFIRMED (all primary-sourced):**
- JBLM's economic impact is federal appropriations/payroll (SSMCP REIA).
- MultiCare is a 501(c)(3) nonprofit funded heavily by Medicare/Medicaid and tax-exempt (Fitch, ProPublica 990).
- The Puyallup Tribe's sovereignty and gaming rest on federal recognition + a state gaming compact (tribal site, WA Gambling Commission).
- Weyerhaeuser's fortune originated in a federal land grant to the Northern Pacific, sold to Weyerhaeuser in 1900 (HistoryLink).
- The Port is a public municipal corporation funded partly by property tax levy (RCW 53).
- The Chamber is a tax-exempt 501(c)(6) (ProPublica 990).

**What is OVERREACH (editorializing, not evidence):**
- "The private sector in Pierce County is largely a government-created rentier class" — this is a normative conclusion, not a finding. It ignores that MultiCare, Weyerhaeuser, and the Tribe also generate genuine private/economic value and employment.
- "The growth machine is a literal machine" — Logan & Molotch's growth-machine is a recognized academic lens, and the evidence (developers→Chamber→Council donor flows, Tideflats development, land-use approvals) is consistent with it. But the evidence shows **overlapping interests**, not a proven coordinated conspiracy. Frame it as "growth-coalition dynamics consistent with the growth-machine model," not a proven machine.
- "Structural capture" as a feedback loop is a **defensible analytical frame** (government-created wealth → private power → policy influence → more wealth), but it should be labeled as an interpretation, not a demonstrated causal chain.

**Defensible version:** "Pierce County's major economic institutions derive substantial power from government-granted privileges (appropriations, tax exemption, sovereignty, land grants, public levies), and these institutions in turn influence the government that grants those privileges. This creates a structural interdependence that warrants scrutiny." — This survives. The stronger "rentier class / literal machine" framing does not.

---

## RECOMMENDED UPDATES

**Graph (`/tmp/pierce_graph_corrected.json`):**
1. Fix the 12 wrong edges (Kastama, Ibsen, Nobles, Archdiocese-owns-VMFH, Weyerhaeuser-GreenDiamond, GTCF-Ponepinto, 4 reversed `appropriates`, 2 mislabeled `elected`, Sterud duplicate).
2. Remove the 12 filler/misleading edges (media→council ×4, Columbia Bank→council, Central Pierce→council, Life Center ×2, Archdiocese→council, CHB→Weyerhaeuser, generic funding edges).
3. Add the 30+ missing nodes and 25+ missing edges listed above (Lawver, Strobel, Bernstein, Thompson, Sowell, developers, Smith, Schrier, Krishnadasan, Fey, Ferguson, CommonSpirit, Wellfound, WSHA, HHFPAC, Cheney Fdn, Bates, TAM, MOG, Saltchuk, NWSA, SSMCP, PMBA, Tacoma Weekly).
4. Add the **money-source edges** (federal_appropriations, tax_exemption, sovereignty, land_grant, levy) so the structural-capture loop is visible.
5. Re-domain: port-tacoma → government; chatham-am → media; flag Tribe/Chamber/MultiCare as dual-domain.
6. Add a **veto-power dimension** to the composite so Tribe, JBLM, Sheriff, Chamber rank correctly.
7. Cap party-node aggregation (remove legislator→party `member` edges or weight them down).

**Evidence files:**
- `12-power-matrix.md`: Keep the qualitative ranking; add a note that the graph's computed composite is a centrality measure, not a power measure.
- `28-source-of-economic-power.md`: Soften the "rentier class / literal machine" language to "structural interdependence consistent with the growth-machine model." Correct the JBLM figure to note it's Pierce+Thurston combined.
- `01-formal-power-structure-VERIFIED.md`: Update Conway to "retiring 2026"; note Puyallup chairman rotates (Sterud ↔ Bean).
- `04-campaign-finance.md`: Verify the $357K HHFPAC figure against a PDC C4 report before citing it as MultiCare's spend.

**HTML (`11-power-network.html`):**
- Rebuild from the corrected graph.
- Use the evidence/12 qualitative ranking (with veto-power adjustment) for node sizing, not the raw composite.
- Add the "Follow the money" toggle to show the money-source edges (already planned).

---

## Sources (primary, key)
- Pierce County official: https://www.piercecountywa.gov/99/Pierce-County-Council ; /8875/2026-2027-Biennial-Budget-Development ; /8703/Biography ; /126/Meet-Your-Sheriff ; /3560/About-Mary-Robnett
- Wikipedia: https://en.wikipedia.org/wiki/2024_Pierce_County_Executive_election ; /Pierce_County_Council
- Ballotpedia: https://ballotpedia.org/Ryan_Mello_(Pierce_County_Executive,_Washington,_candidate_2024) ; /Steve_Conway ; /Deborah_Krishnadasan
- Fitch: https://www.fitchratings.com/research/us-public-finance/fitch-affirms-multicare-healthcare-system-wa-at-a-outlook-stable-11-06-2026
- SSMCP REIA: https://www.ssmcp.org/wp-content/uploads/2023/10/REIA-2023-Pierce-Thurston-as-of-09272023.pdf
- City of Lakewood: https://cityoflakewood.us/jblm-economic-impact
- NWSA: https://www.nwseaportalliance.com/about-us/cargo-statistics
- ProPublica 990s: https://projects.propublica.org/nonprofits/organizations/910434830 (Chamber) ; /911352172 (MultiCare)
- HistoryLink: https://www.historylink.org/file/5241 (Weyerhaeuser) ; /File/7969 (Puyallup settlement)
- Weyerhaeuser IR: https://investor.weyerhaeuser.com/2025-10-30-Weyerhaeuser-Provides-Update-on-Timberlands-Portfolio-Optimization-Actions
- Puyallup Tribe: https://www.puyalluptribe-nsn.gov/council_member/bill-sterud ; /news/david-z-bean-elected-chairman-of-tribal-council-bill-sterud-elected-vice-chairman
- WA Legislature: https://leg.wa.gov/legislators ; https://leg.wa.gov/media/0pvgo5ic/2025-26-committee-assignment-telephone-directory.pdf
- Port of Tacoma: https://www.portoftacoma.com/commission ; https://app.leg.wa.gov/rcw/default.aspx?Cite=53
- VMFH: https://www.vmfh.org/about-vmfh
- United Way/GTCF: https://www.uwpc.org/board-directors ; https://www.gtcf.org/blog/profile/nathe-lawver
- Tacoma Schools: https://www.tacomaschools.org/about/bond/february-10-2026-election
- Pierce Transit: https://piercetransit.org/wp-content/uploads/2025/2026-Adopted-Budget.pdf
