# Skeptic's Money-Channel & Thesis Gap Report — INV-2026-002

**Reviewer stance:** Assume every dollar figure is wrong until proven against a primary source.
**Method:** Cross-checked the HTML node graph (`11-power-network.html`) money/influence edges against the evidence files and primary sources via web search.
**Date:** 2026-09-09
**Verdict scale:** CONFIRMED / WRONG / UNVERIFIED / MISSING

---

## A. THE 6 STRUCTURAL-CAPTURE ANCHORS

### A1. JBLM — "$12.1B economic impact, 100% federal appropriations"
**Suspected problem:** The $12.1B figure is a *combined Pierce+Thurston total economic impact* (direct + indirect + induced multiplier), not a Pierce-only or direct figure. The graph states it flatly as "$12.1B economic impact" with no scope qualifier.
**Verdict:** CONFIRMED (figure exists) but **MISCHARACTERIZED** (what it measures).
**Evidence:**
- SSMCP REIA 2023 (ssmcp.org/wp-content/uploads/2023/10/REIA-2023-Pierce-Thurston-as-of-09272023.pdf): "total employment impact attributable to the existence of JBLM is more than 57,640 total jobs in Pierce. JBLM contributes $3.6 billion in new and sustained labor income and **$3.9 billion in economic output in Pierce**." The $12.1B is the *combined* Pierce+Thurston total impact.
- City of Lakewood (cityoflakewood.us/jblm-economic-impact): "JBLM contributes more than $12.1 billion to the region's economy" — region = Pierce+Thurston.
- South Sound Biz (southsoundbiz.com/news/jblm-study-thurston-pierce-county): $8B direct impact = payroll $3.24B + BAH $1.3B + retiree $1.27B + disability $1.48B + healthcare $113M + school aid $12.31M + contracts $581.1M.
**Action:** **CORRECT FIGURE / ADD QUALIFIER.** The graph's "$12.1B" must be labeled "Pierce+Thurston combined total economic impact (direct+indirect+induced)." Pierce-only direct output is $3.9B; Pierce-only total output is $3.9B. The "100% federal appropriations" characterization is sound — every component is federal money.

### A2. MultiCare — "$7.2B revenue, 501(c)(3) + Medicare/Medicaid"
**Suspected problem:** Is $7.2B the right revenue figure, and is the tax-exempt characterization correct?
**Verdict:** CONFIRMED.
**Evidence:**
- Fitch Ratings (fitchratings.com/research/us-public-finance/fitch-affirms-multicare-healthcare-system-wa-at-a-outlook-stable-11-06-2026): "MultiCare's revenues were approximately **$7.2 billion in fiscal 2025** (Dec. 31; audited)."
- Chief Healthcare Executive (chiefhealthcareexecutive.com/view/multicare-ceo-to-retire-at-end-of-2026-successor-is-named): "about $7.2 billion in revenue in the 2025 fiscal year."
- ProPublica EIN 911352172 confirms 501(c)(3).
**Action:** **NO CHANGE.** Figure and tax status confirmed. Note: $7.2B is *system-wide* (WA/ID/OR), not Pierce-only — the graph's "largest private employer" framing is Pierce-specific but the revenue is not; flag as a scope caveat, not an error.

### A3. Puyallup Tribe — "1990 settlement $162M + 900 acres"
**Suspected problem:** Verify the settlement figure and land.
**Verdict:** CONFIRMED.
**Evidence:**
- HistoryLink File 20157 (historylink.org/file/20157): "a settlement package of approximately **$162 million** in land, fisheries, economic and social development... The Tribe also received roughly **900 acres** of land."
- LA Times (latimes.com/archives/la-xpm-1990-03-24-mn-680-story.html): "$162 million in cash, real estate and economic development programs... 900 acres of land."
- HistoryLink File 7969: second-largest land claims settlement in U.S. history.
**Action:** **NO CHANGE.** Note the graph's `sovereignty` edge (county-council→puyallup-tribe) is directionally defensible as a government-granted privilege, but "sovereignty" is a legal status, not a money flow — see G.

### A4. Weyerhaeuser — "10.4M acres from 1864 federal land grant"
**Suspected problem:** The 10.4M acres is *current company-wide U.S. timberland*, not land from the 1864 grant. The 1864 grant produced the 900,000 acres purchased in 1900. The graph node's own facts say "400K+ acres in WA" — internally inconsistent with the 10.4M anchor claim.
**Verdict:** CONFIRMED (both figures exist) but **MISCHARACTERIZED** (conflates 1900 purchase with current holdings).
**Evidence:**
- Weyerhaeuser investor release (investor.weyerhaeuser.com/2025-05-22...): "owns or controls approximately **10.4 million acres** of timberlands in the U.S." — *current* holdings, not grant-derived.
- HistoryLink File 5241 (historylink.org/file/5241): Jan 3, 1900, Hill sells 900,000 acres to Weyerhaeuser for $5.4M ($6/acre); land originally granted to Northern Pacific by the federal government in the 1870s-80s.
- Forest History (foresthistory.org): "purchase of 900,000 acres... from the Northern Pacific Railway for $6 an acre."
**Action:** **CORRECT FIGURE / CLARIFY.** The graph must distinguish: (a) the 1864/1870s federal land grant → Northern Pacific → 900,000 acres sold to Weyerhaeuser in 1900 for $5.4M; (b) Weyerhaeuser's *current* 10.4M acres (U.S., company-wide, includes Plum Creek merger). The graph node's "400K+ acres in WA" is a third, unverified figure — reconcile or remove. The `federal_land_grant` edge is historically sound.

### A5. Port of Tacoma — "$76B cargo, $25.3M property tax levy"
**Suspected problem:** Verify the levy and cargo figures.
**Verdict:** CONFIRMED.
**Evidence:**
- Port of Tacoma 2023 Budget (s3.us-west-2.amazonaws.com/portoftacoma.com.../Combined%20Final%202023%20Budget%20Document.pdf): "annual tax levy receipts will grow from **$25.3 million in 2023** to $28.5 million in 2027"; levy increases from $24,567,849 to **$25,304,884**.
- $76B cargo is the *NWSA* (Northwest Seaport Alliance, Tacoma+Seattle combined) figure, not Port-of-Tacoma-only. The graph's `nwsa` node and `operates` edge correctly attribute it.
**Action:** **NO CHANGE** on the levy. **ADD QUALIFIER** on "$76B cargo" — it is NWSA combined, not Port-of-Tacoma alone. The graph already models this via the NWSA node, so the qualifier is a labeling fix.

### A6. Chamber — "$3M budget, 501(c)(6)"
**Suspected problem:** The graph node states "$4.5M budget" — this is the *aspirational 2021/22* figure from a US Chamber job posting, NOT actual revenue. Actual FY2024 revenue is $3,083,509.
**Verdict:** **WRONG** (graph figure).
**Evidence:**
- ProPublica EIN 910434830 / CauseIQ: FY2024 total revenue **$3,083,509**, expenses $3,392,757.
- US Chamber job posting (uschamber.com/assets/documents/TPCC-President-and-CEO.pdf): "$4.5M budget for the 2021/2022 fiscal year" — aspirational/pass-through, contradicted by actual 990s (FY2022 actual $3.95M, FY2023 $3.24M, FY2024 $3.08M).
**Action:** **CORRECT FIGURE.** Change graph fact from "$4.5M budget" to "$3.08M revenue (FY2024, IRS 990)." The 501(c)(6) status is confirmed.

---

## B. MISSING MONEY FLOWS (biggest flows not in the graph)

### B1. County's top vendors / procurement contractors
**Suspected problem:** The $3.5B biennial budget is in the graph (via `appropriates` edges to sheriff/PA/courts), but the *largest private contractors receiving county money* are absent. The evidence file 05 explicitly flags "Who are the top 10 county vendors?" as an open question.
**Verdict:** MISSING.
**Evidence:** Evidence file 05-budget-contracts.md (OpenGov procurement portal, Small Works Roster, sole-source awards to Tacoma Parks Foundation and Dave Purchase Project). No vendor nodes exist in the graph.
**Action:** **ADD EDGE/NODES** once the top-vendor list is pulled from OpenGov. This is the single biggest gap in the "government creates wealth → private actors" half of the loop for the county itself.

### B2. Tacoma Public Schools $650M bond (2024)
**Suspected problem:** The graph has a `tacoma-schools` node but no bond/levy money edge. The $650M 2024 bond is one of the largest single capital flows in the county.
**Verdict:** MISSING.
**Evidence:** KING 5 / News Tribune (thenewstribune.com/news/local/education/article284320308.html): "$650 million bond" passed Feb 2024, 69% approval; Tacoma Schools Prop 1 "Neighborhood School Improvements & Safety Upgrades."
**Action:** **ADD EDGE** — `tacoma-schools → county-council : bond/levy` (or a `school-bond` money edge). Also missing: Puyallup $175M capital levy (failed 2024), Sumner-Bonney Lake $114M bond (graph has the node but no levy edge), University Place $355M construction (node present, no edge).

### B3. Pierce Transit $345M budget + Nov 2026 sales-tax ballot measure
**Suspected problem:** The graph has a `pierce-transit` node and a `transit_funding` edge from Jake Fey, but the *Nov 2026 ballot measure* (0.6%→0.9% sales tax, the first transit tax increase since 2002) is a major prospective money flow not modeled.
**Verdict:** MISSING.
**Evidence:** Evidence file 22-pierce-transit.md; Pierce Transit Resolution 2026-006 (July 13, 2026); $345M 2026 budget; sales tax = $117M (73.1% of operating revenue).
**Action:** **ADD EDGE** — `pierce-transit → county-council : sales_tax_ballot` (or a `ballot_measure` money edge). The graph models the agency but not the revenue mechanism that funds it.

### B4. Port $25.3M levy
**Verdict:** PRESENT (confirmed in A5). **NO CHANGE.**

### B5. Fire district levies
**Suspected problem:** Graph has `east-pierce-fire` and `gig-harbor-fire` with `taxing` edges, and `west-pierce-fire`/`central-pierce-fire` nodes. But the *dollar* levies are absent (East Pierce $80M bond, West Pierce $75.5M budget, Central Pierce $180M budget).
**Verdict:** PARTIALLY PRESENT / MISSING (dollar values).
**Action:** **ADD DOLLAR VALUES** to the existing `taxing` edges. The edges exist; the amounts don't.

### B6. Federal grants beyond JBLM (HUD, transportation, health)
**Suspected problem:** The graph has generic `federal_funding` edges from congress members (Cantwell, Murray, Randall, Strickland, Smith, Schrier) to county-council, but no *specific* federal grant programs (HUD CDBG, transportation, health) and no dollar amounts.
**Verdict:** MISSING (specificity).
**Action:** **ADD EDGE/AMOUNTS** — the federal_funding edges are placeholders without program or dollar specificity. The county's own budget flags "federal revenue uncertainty" (evidence 05), so this is material.

### B7. State funding to the county
**Suspected problem:** `state_funding` edges exist from state legislators, but no dollar amounts and no specific programs (transportation, human services, opioid settlement funds).
**Verdict:** PARTIALLY PRESENT / MISSING (amounts).
**Action:** **ADD DOLLAR VALUES.** The edges exist; the amounts don't.

---

## C. THE MONEY→PEOPLE→SYSTEMS LOOP — is it actually visible?

**Suspected problem:** The thesis claims a *closed* loop (gov→private→gov). Does the graph show BOTH the money edge (gov→private) AND the influence edge (private→gov) for each anchor?

| Anchor | Money edge (gov→private) | Influence edge (private→gov) | Loop complete? |
|--------|--------------------------|------------------------------|----------------|
| JBLM | `federal_appropriations` ✓ | `armed_services_champion` (Adam Smith), `ssmcp` ✓ | **NO — thesis break.** JBLM is *government*, not a private actor. The "private actor converts wealth to power" step does not apply. The loop as drawn is gov→gov. |
| MultiCare | `tax_exemption` ✓ | `donated`→pierce-dem, `lobbies` via HHFPAC, `member`→WSHA ✓ | **YES** — loop visible. |
| Puyallup Tribe | `sovereignty` ✓ | `donated`→6 candidates, lobbying ✓ | **YES** — loop visible. |
| Weyerhaeuser | `federal_land_grant` ✓ | **NONE** — no donated, no lobbying, no board edge | **NO — loop BROKEN.** The graph shows money INTO Weyerhaeuser but zero influence edges back to government. This is the weakest anchor in the graph. |
| Port of Tacoma | `property_tax_levy` ✓ | `gth-gov` lobbying, `chamber` board ✓ | **NO — thesis break.** Port is *public* (RCW 53), not private. Same problem as JBLM. |
| Chamber | `tax_exempt` ✓ | `influence`, `candidate-academy`, `wa-realtors-pac` ✓ | **YES** — loop visible. |

**Verdict:** The loop is **only fully visible for 3 of 6 anchors** (MultiCare, Tribe, Chamber). Two anchors (JBLM, Port) are *government entities* — the thesis's "private actors convert it to power" step is structurally inapplicable, which is a **thesis error**, not just a graph gap. One anchor (Weyerhaeuser) has **no influence edge at all** — the loop is broken.
**Action:**
- **ADD EDGE** — Weyerhaeuser needs influence edges (campaign donations — William Weyerhaeuser gave $2,400 to Rohrer and $2,000 to Robnett per evidence 04; lobbying; Chamber membership). Without these, Weyerhaeuser cannot support the capture thesis.
- **REFRAME THESIS** — JBLM and Port are public actors; the "structural capture" claim must either (a) drop them from the "private actors" framing and recast them as *public wealth concentrations that private actors seek to influence* (which the evidence file 28 itself acknowledges for the Port), or (b) explicitly label them as the "government creates wealth" side, not the "private converts to power" side.

---

## D. CAMPAIGN FINANCE CHANNEL

**Suspected problem:** Is the campaign-finance channel complete? Are the biggest donors in the graph?
**Verdict:** PARTIALLY COMPLETE — **MISSING** several of the largest donor flows.
**Evidence (evidence file 04, PDC API):**
- **Present in graph:** Pierce GOP ($175,500 to Chambers — the single largest donor flow), Together for Pierce County ($293,755 IE), HDCC ($28,500), WEA PAC, WA Realtors PAC, NASH Cascadia, Master Builders, Puyallup Tribe, ILWU 23, Tacoma PD Union.
- **MISSING from graph (all confirmed donors in evidence 04):**
  - **Miles Sand & Gravel** — donated to Chambers, Herrera ($1,800), Cruver ($1,200), Rohrer ($2,400). A top developer donor, absent.
  - **Weyerhaeuser (William)** — $2,400 to Rohrer, $2,000 to Robnett. Absent (and relevant to C's broken Weyerhaeuser loop).
  - **Master Builders** — present, but only edges to Cruver/Herrera; missing Rohrer ($2,400).
  - **WA Realtors PAC** — present but only a generic `county-council` edge; missing Rohrer ($2,400).
  - **Auto dealers** (Subaru of Puyallup, Kia of Everett, Toyota of Puyallup) — absent.
  - **Rush Development, Southport, Tucci & Sons, Lincoln Park, Nall Capital** — present as Chamber members/land_use but have **no `donated` edges** despite being confirmed donors (Rush $2,400 to Chambers, etc.).
- **Directional error:** The graph's `donated` edges for candidates (e.g., `ryan-mello → pierce-dem : donated (in)`) are drawn with the *candidate* as source and the *donor* as target. Money flows donor→candidate; the graph reverses this for several edges (e.g., `pierce-dem → ryan-mello : donated (out)` is correct, but `ryan-mello → pierce-dem : donated (in)` is inverted). **Inconsistent directionality** across donated edges.
**Action:** **ADD EDGES** for Miles Sand & Gravel, Weyerhaeuser, auto dealers, and the developer donors (Rush, Southport, Tucci, Lincoln Park, Nall). **FIX DIRECTION** on inverted `donated` edges so money always flows donor→candidate.

---

## E. LOBBYING CHANNEL

**Suspected problem:** The graph has only 2 `lobbying` edges (GTH→county-council, GTH→port-tacoma) and lobbyist nodes GTH, Michael Shaw, WSHA, HHFPAC. Is this complete?
**Verdict:** **MISSING** — the biggest lobbyists are absent.
**Evidence (evidence file 07, PDC L-5 data):**
- **Puyallup Tribe** — the *largest* lobbying spender in the county ($1,434,500 in 2024; $1,910,333 combined 2024-25). The graph has the Tribe node but **no lobbying edge** for it.
- **MultiCare** — $103,400 (2024) / $107,556 (2025) via Ingrid Mungia (PDC lobbyist 17588). The graph has MultiCare→WSHA→HHFPAC but **no direct MultiCare lobbying edge**.
- **Virginia Mason Franciscan Health** — $191,589 (2024). Node exists (`vmfh`), **no lobbying edge**.
- **LeadingAge WA** ($166K), **WA Independent Physicians** ($164K), **City of Tacoma** ($92K), **Waste Connections** ($103K), **Southport Real Estate** ($116K) — all absent.
- **Michael Shaw** — present ($110K/yr, confirmed in evidence 07).
- **GTH Gov Affairs** — present, but the evidence file notes GTH's Pierce County-area clients include City of Tacoma and Port of Tacoma; the graph only models GTH→county-council and GTH→port-tacoma, missing GTH→city-of-tacoma.
**Action:** **ADD EDGES** — Puyallup Tribe lobbying (the single largest), MultiCare, VMFH, City of Tacoma, and the top-10 list from evidence 07. The lobbying channel as drawn captures only the county's own lobbyist and one firm, missing the entire private-actor lobbying side that the thesis depends on.

---

## F. THE $357K HHFPAC FIGURE + "TRIBE = LARGEST COUNTY LOBBYIST"

**Suspected problem:** Red-team flagged these as unverifiable without a WA PDC C4 pull.
**Verdict:** **UNVERIFIED** (both).
**Evidence:**
- **HHFPAC $357K:** The evidence file 08 cites "In 2022, HHFPAC spent ~$357,000 against Democratic candidates including Sen. Marko Liias and Rep. Melanie Morgan (per Olympian reporting)." Web search of the Olympian's 2022 top-PAC article (theolympian.com/news/politics-government/election/article269217882.html) lists the top 5 IE spenders (New Direction, WA Realtors, Concerned Taxpayers, etc.) and **does not mention HHFPAC or a $357K figure**. The specific $357K figure could not be confirmed from any primary source. The graph's `hhfpac` node and `lobbies` edge rest on this unverified figure.
- **Tribe = largest county lobbyist:** The evidence file 07 claims $1,434,500 (2024) from PDC L-5 data. OpenSecrets shows the Tribe's *federal* lobbying at only $270K (2024) — a different, much smaller number. The state-level $1.4M figure is **self-reported in the evidence file but not independently confirmed** via a PDC C4/L-5 pull in this review. The claim that the Tribe is the *largest* county lobbyist is plausible but **unverified**.
**Action:** **FLAG UNVERIFIED** on both the HHFPAC $357K figure and the "Tribe = largest county lobbyist" claim. Do not present either as established fact in the graph until a WA PDC C4/L-5 pull confirms them. The HHFPAC `lobbies` edge and the Tribe's lobbying dominance should carry an "UNVERIFIED" marker.

---

## G. TAX EXEMPTIONS

**Suspected problem:** The graph claims `tax_exemption`/`tax_exempt` edges for MultiCare, Chamber, and others. Tax-exempt status is not a dollar figure — is it quantified?
**Verdict:** **UNQUANTIFIED** (edges exist, no dollar value).
**Evidence:**
- MultiCare: 501(c)(3) confirmed (ProPublica EIN 911352172). The evidence file 28 cites a *national* figure — "$37.4 billion tax benefit in 2021" for all nonprofit hospitals (PMC11428023, CRS IF13192) — but **no MultiCare-specific dollar value** for its tax exemption.
- Chamber: 501(c)(6) confirmed (ProPublica EIN 910434830). No dollar value for the exemption.
- The skeptic's objection is valid: "tax-exempt status is not the same as a dollar figure." The graph's `tax_exemption` edges assert a *money flow* (they render as gold money edges) without quantifying it.
**Action:** **FLAG UNQUANTIFIED / ADD VALUE.** Either (a) quantify the exemption (e.g., MultiCare's foregone property/income tax, which would require a county assessor or 990-derived estimate), or (b) relabel the edges as `tax_exempt_status` (a legal status, not a money flow) so they don't render as gold money edges. As drawn, the graph implies a dollar flow that has not been measured. The `sovereignty` edge (Tribe) has the same problem — it's a legal status rendered as a money edge.

---

## SUMMARY OF REQUIRED ACTIONS

| # | Item | Verdict | Action |
|---|------|---------|--------|
| A1 | JBLM $12.1B | CONFIRMED, mischaracterized | ADD QUALIFIER (Pierce+Thurston combined total impact; Pierce-only $3.9B) |
| A2 | MultiCare $7.2B | CONFIRMED | NO CHANGE (add system-wide scope caveat) |
| A3 | Tribe $162M/900ac | CONFIRMED | NO CHANGE |
| A4 | Weyerhaeuser 10.4M ac | CONFIRMED, mischaracterized | CORRECT FIGURE (distinguish 1900 grant purchase vs current holdings; reconcile "400K+ acres in WA") |
| A5 | Port $25.3M levy | CONFIRMED | NO CHANGE (qualify $76B as NWSA combined) |
| A6 | Chamber "$4.5M budget" | **WRONG** | CORRECT FIGURE → $3.08M (FY2024 990) |
| B1 | County top vendors | MISSING | ADD EDGES (OpenGov top-10 vendor pull) |
| B2 | Tacoma Schools $650M bond | MISSING | ADD EDGE |
| B3 | Pierce Transit ballot measure | MISSING | ADD EDGE |
| B5 | Fire district levy dollars | MISSING | ADD DOLLAR VALUES |
| B6/B7 | Federal/state grant amounts | MISSING | ADD DOLLAR VALUES |
| C | Loop completeness | 3/6 anchors complete | ADD Weyerhaeuser influence edges; REFRAME JBLM/Port (public, not private) |
| D | Campaign finance | PARTIAL | ADD Miles Sand & Gravel, Weyerhaeuser, auto dealers, developer donors; FIX inverted `donated` direction |
| E | Lobbying | MISSING | ADD Tribe, MultiCare, VMFH, City of Tacoma lobbying edges |
| F | HHFPAC $357K + Tribe largest lobbyist | **UNVERIFIED** | FLAG UNVERIFIED (needs PDC C4/L-5 pull) |
| G | Tax exemptions | UNQUANTIFIED | QUANTIFY or RELABEL as status, not money flow |

**Bottom line:** The thesis's *money* half is largely sound (5 of 6 anchor figures confirmed; Chamber budget is the one outright error). But the *loop* half is the weak point: Weyerhaeuser has no influence edges, JBLM and Port are public actors that don't fit the "private converts to power" step, the lobbying channel omits the county's largest lobbyists, and the two most aggressive claims (HHFPAC $357K, Tribe = largest lobbyist) are unverified. The graph overstates the completeness of the capture loop.
