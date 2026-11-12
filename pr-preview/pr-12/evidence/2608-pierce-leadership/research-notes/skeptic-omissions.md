# Skeptic Gap Report — Pierce County Leadership Investigation (INV-2026-002)

**Reviewer stance:** Hostile. Nothing in the 157-node graph is accepted without primary-source proof. Every suspected omission below was checked against the evidence files (01, 02, 03, 10, 12, 13, 20, 25) and verified via web search against primary sources (official .gov sites, court records, employer data, ownership records).

**Verdict key:** CONFIRMED GAP (add/connect) · NOT A GAP (already covered) · REMOVE (orphaned placeholder) · WEIGHTING (present but mis-ranked)

---

## A. TACOMA MAYOR + TACOMA CITY COUNCIL

**Suspected omission:** County seat (Tacoma, ~220K, 23% of county population) has no mayor and no city council in the graph.

**Verdict: CONFIRMED GAP (mayor present but grotesquely underweighted) + CONFIRMED GAP (council absent as a node)**

**Evidence:**
- Mayor **Anders Ibsen** IS in the graph (id 147, power **0.008** — 3rd from the bottom, tied with the orphaned 0.000 nodes). Primary source: tacoma.gov — "Mayor Anders Ibsen began serving as the mayor in 2026. He also served as a District 1 City Council Member for eight years." https://tacoma.gov/profile/office-of-mayor-anders-ibsen
- The **Tacoma City Council (9 members)** is NOT a node. Evidence file 02 documents the full roster: Ibsen (mayor), John Hines, Sarah Rumbaugh, Jamika Scott, Sandesh Sadalge, Chanjolee "Joe" Bushnell (Deputy Mayor), Latasha Palmer, Olgy Diaz, Kristina Walker. Source: https://tacoma.gov/government/departments/city-council/
- The power matrix (evidence/12) ranked Ibsen #16 (composite 4.5) and #24 (3.5) — yet the graph gives him 0.008. This is a **weighting collapse**, not a data absence.

**Action:**
- **WEIGHTING:** Raise Anders Ibsen from 0.008 to a top-tier municipal node. The mayor of the county's largest city (220K, 23% of county) cannot rank below a fire district. The power matrix's own 4.5 composite justifies a score ~0.10-0.15.
- **ADD NODE:** Tacoma City Council (gov org) — a 9-member body controlling a ~$1.5B city budget, land use, and the Connect Tacoma levy. Add edges to Ibsen, Mello (county), Sound Transit (Walker sits on both), and the Chamber.
- **ADD NODES (optional, high-value):** Deputy Mayor Joe Bushnell (leading $20/hr minimum wage push) and Kristina Walker (Sound Transit board + Pierce Transit board interlock — she is a genuine bridge node).

---

## B. COUNTY ROW OFFICERS

**Suspected omission:** Only 6 of 7 council members appear; Assessor, Auditor, Treasurer, Clerk, Prosecuting Attorney missing as distinct nodes.

**Verdict: NOT A GAP (all 7 council members present; all row officers present). The task premise is factually wrong.**

**Evidence:**
- **All 7 council members ARE in the graph:** Hitchen (#26), Morell (#77), Ayala (#19), Cruver (#29), Herrera (#33), **Yambe (#78)**, **Denson (#79)**. The task prompt claimed "only 6 of 7" — but Bryan Yambe (appointed Jan 2025 to succeed Campbell) and Robyn Denson (Exec Pro Tem) are both present. Evidence file 01 lists all 7. No gap.
- **Row officers present:** Assessor-Treasurer **Marty Campbell** (#82), Auditor **Linda Farmer** (#81), Prosecuting Attorney **Mary Robnett** (#14), Sheriff **Keith Swank** (#9). Confirmed via piercecountywa.gov elected-officials list: "Executive Ryan N. Mello, County Council, Assessor-Treasurer Marty Campbell, Auditor Linda Farmer, Prosecuting Attorney Mary Robnett, Sheriff Keith Swank." https://www.piercecountywa.gov
- **No separate Treasurer exists** — Pierce County combines Assessor-Treasurer (Campbell). No gap.
- **Clerk of Superior Court is APPOINTED, not elected** in Pierce County — one of only 4 charter counties (King, Whatcom, Clallam, Pierce) where the clerk is appointed. MRSC: "The clerk is an elected office in all but four charter counties (King, Whatcom, Clallam and Pierce)." https://mrsc.org/explore-topics/officials/roles/county-officials. A 2026 Charter Review proposal to make it elected is pending but not in effect. No elected-clerk gap.

**Action: NO CHANGE** for the council (complete) and row officers (complete). **Optional:** add a distinct "Prosecuting Attorney's Office" legal node (see Section D) — Robnett the person is present but the office as an institution is not.

---

## C. PORT OF TACOMA COMMISSION

**Suspected omission:** Port is #7 (0.236) but no individual commissioners named.

**Verdict: NOT A GAP (all 5 commissioners ARE in the graph). The task premise is factually wrong.**

**Evidence:**
- All 5 Port commissioners present as persons: **John McCarthy** (#21, 0.085), **JT Wilcox** (#93, 0.025), **Dick Marzano** (#110, 0.018), **Deanna Keller** (#127, 0.014), **Kristin Ang** (#128, 0.014).
- Primary source (Port of Tacoma): "The Port of Tacoma is governed by five commissioners, each elected by Pierce County voters to serve four-year terms." Roster: John McCarthy, Dick Marzano, Deanna Keller, JT Wilcox, Kristin Ang. https://www.portoftacoma.com/commission ; 2026 officer designations: President Marzano, VP Keller, Secretary Ang. https://www.portoftacoma.com/news/port-tacoma-designates-commission-officer-positions-2026
- Evidence file 01 documents the same 5.

**Action: NO CHANGE** on presence. **WEIGHTING note:** The Port org node is 0.236 but its 5 commissioners average ~0.03. For a body controlling $76B cargo and a $25M levy, the individual commissioners are underweighted relative to the institution — but this is a weighting judgment, not an omission. Consider raising McCarthy (4 terms, 40 years, FMSIB/PSRC) and Wilcox (former State Rep, GOP power) to reflect their bridge roles.

---

## D. LEGAL DOMAIN (only 4 nodes)

**Suspected omission:** No distinct Prosecuting Attorney node, no public defender, no federal judges (Western District WA), no top civil litigators.

**Verdict: CONFIRMED GAP (partial) — legal domain is underdeveloped.**

**Evidence:**
- **Prosecuting Attorney's Office as an institution:** Robnett the person is present (#14, 0.135), but the PA office — a $94M budget, all felony prosecutions, civil division advising every county department (evidence/01, /12) — is not a node. The office is a distinct power center from the person.
- **Public defender:** Evidence file 10 lists "Assigned Counsel (Public Defender) — TBD, director search posted 2026." The position is vacant/being filled, so a named node is not yet possible — but the office is a real legal actor. Gap is real but currently unnameable.
- **Federal judges (Western District WA):** The Tacoma federal courthouse is real and active. Chief District Judge **David G. Estudillo**; active judges Tiffany Cartwright, John Chun, Kymberly Evanson, Lauren King, Tana Lin, Jamal Whitehead. Source: https://ballotpedia.org/United_States_District_Court_for_the_Western_District_of_Washington ; https://www.wawd.uscourts.gov. Federal judges handle the county's gang/fentanyl indictments (Knoccout Crips, Black Gangster Disciples — evidence/13), tribal cases, and the Puyallup River litigation. **None are in the graph.** This is a genuine gap for a "leadership" map, though federal judges are appointed (external) rather than county actors.
- **Top civil litigators:** Not documented in evidence; no specific names verified. Cannot confirm a specific gap without named actors.

**Action:**
- **ADD NODE:** Prosecuting Attorney's Office (legal org) — connect to Robnett, Superior Court, Sheriff Swank (conflict edge), County Council.
- **ADD NODE:** Federal District Court — Western District WA / Tacoma (legal org) — connect to Superior Court, Sheriff, PA office. Optionally add Chief Judge Estudillo.
- **ADD NODE (when filled):** Assigned Counsel / Public Defender (legal org).
- **NO CHANGE** on civil litigators (no verified names).

---

## E. MEDIA DOMAIN (11 nodes, 4 at 0.000)

**Suspected omission:** KNKX, iHeartMedia, Audacy, Lotus all orphaned at 0.000. Is narrative control complete?

**Verdict: CONFIRMED GAP (KNKX must be connected; radio conglomerates are real owners but low local salience).**

**Evidence:**
- **KNKX is a genuine local news actor** — not a placeholder. It has Tacoma studios and is actively reporting on Pierce County: it broke the TPCHD director investigation ("Investigation into top Tacoma health official revealed 'harsh' style — Chantell Harmon Reed," https://www.knkx.org/tacoma/2026-04-21/...) and covered the McClatchy/News Tribune strike (https://www.knkx.org/tacoma/2026-07-02/...). It is one of the few independent local newsrooms. **0.000 is indefensible.**
- **News Tribune ownership:** Confirmed owned by **McClatchy** (both nodes present, #27 and #75). Journalists struck McClatchy in May 2026. https://www.nwpb.org/local/2026-05-26/... The graph correctly separates the paper from its owner.
- **iHeartMedia, Audacy, Lotus:** Real national radio conglomerates that own Tacoma-market stations (Pew/BIA ownership data). They are real owners but their **local** narrative power is diffuse — they are national chains, not Tacoma institutions. KNKX is the only locally-relevant radio newsroom.

**Action:**
- **ADD EDGES:** Connect KNKX (raise from 0.000 to ~0.02-0.03) to News Tribune, Chamber, County Council, and the health department (it covers TPCHD). It is a real counterweight newsroom.
- **REMOVE or weakly connect:** iHeartMedia, Audacy, Lotus — national chains with no Tacoma-specific editorial power. Either connect them weakly to the media cluster or remove them as noise. A skeptic's rule: they don't shape Pierce County narrative; they sell ads.
- **NO CHANGE:** News Tribune, McClatchy, Tacoma Weekly, South Sound Biz, Chatham AM, Premier Media (all present with power).

---

## F. THE 10 ORPHANED 0.000 NODES

**Suspected omission:** Central Pierce Fire, Columbia Bank, KNKX, iHeartMedia, Audacy, Lotus, Bethel SD, Catholic Archdiocese, Life Center, Tacoma Housing Authority — all at 0.000.

**Verdict: 6 CONFIRMED GAPS (real actors, must connect), 3 REMOVE (national chains / low documented power), 1 BORDERLINE.**

| Node | Verdict | Evidence | Action |
|------|---------|----------|--------|
| **Central Pierce Fire** | **CONFIRMED GAP** | Real, largest fire district — merged Graham + Orting + CPFR effective Jan 1, 2026; 12 commissioners; independent taxing authority (Fire Benefit Charge). Board minutes confirm merger asset transfers. https://www.centralpiercefire.org/wp-content/uploads/2026-02-09-Board-Packet.pdf ; https://www.thenewstribune.com/news/local/community/puyallup-herald/ph-news/article304014676.html. **Inconsistent:** East Pierce (#100), West Pierce (#115), Gig Harbor (#101) all have power; Central Pierce — the largest — is 0.000. | **ADD EDGES** + raise power. Connect to County Council, IAFF union, East/West Pierce. |
| **Columbia Bank** | **CONFIRMED GAP** | Tacoma HQ, parent of Umpqua Bank, top-30 US bank, $50B+ assets. Chairman **William Weyerhaeuser** — direct Weyerhaeuser family interlock (evidence/13). https://www.prnewswire.com/news-releases/umpqua-bank-and-parent-company-columbia-banking-system-celebrate-anniversaries-with-1m-in-grants-for-local-nonprofits-302016954.html | **ADD EDGES** + raise power. Connect to Weyerhaeuser, Chamber, GTCF. |
| **KNKX** | **CONFIRMED GAP** | Real local NPR newsroom (see Section E). | **ADD EDGES** + raise power. |
| **iHeartMedia** | **REMOVE** | National radio chain; no Tacoma-specific editorial power. | **REMOVE** (or weak connect). |
| **Audacy** | **REMOVE** | National radio chain (Entercom); no local editorial power. | **REMOVE** (or weak connect). |
| **Lotus** | **REMOVE** | National radio chain; no local editorial power. | **REMOVE** (or weak connect). |
| **Bethel School District** | **CONFIRMED GAP** | Real, 4th-largest district (Spanaway), declining enrollment, boundary tension with Puyallup (evidence/13). **Inconsistent:** Tacoma, Puyallup, Clover Park, Sumner-Bonney Lake, University Place schools all present with power; Bethel at 0.000. | **ADD EDGES** + raise power. Connect to Puyallup SD, County Council. |
| **Catholic Archdiocese** | **CONFIRMED GAP** | Real — Pierce Deanery, $191,589 lobbying via VMFH/CHI (evidence/13). **Inconsistent:** VMFH/CHI is #16 (0.121) but the Archdiocese that owns it is 0.000. | **ADD EDGES** + raise power. Connect to VMFH/CHI, CommonSpirit. |
| **Life Center** | **BORDERLINE** | Real megachurch (Tacoma, multiple locations) but no documented political engagement in evidence. Evidence/13 flags it as "potential" organizing infrastructure, not confirmed. | **REMOVE** unless political activity is documented. A skeptic: no proof of power = no node. |
| **Tacoma Housing Authority** | **CONFIRMED GAP** | Real — major Hilltop redevelopment force (Salishan HOPE VI, Prairie Oaks, Aviva Crossing). Exec Director **Michael Mirra** (retiring July 2026). https://www.tacomahousing.org/news/tacoma-housing-authority-executive-director-michael-mirra-announces-his-retirement. Evidence/13 documents THA as "primary vehicle for reshaping Tacoma's physical and demographic landscape." | **ADD EDGES** + raise power. Connect to City Council, County, developers. |

---

## G. OTHER MISSING ACTORS

**Suspected omission:** Boeing, Amazon, top vendors, Tacoma-Pierce County Health Department, UW Tacoma chancellor, Sound Transit CEO, banks, Puget Sound Energy, developers.

| Actor | Verdict | Evidence | Action |
|-------|---------|----------|--------|
| **Boeing** | **CONFIRMED GAP** | ~1,550 FTEs; Frederickson plant (largest aerospace manufacturer in county); Puyallup fabrication division. ESD 2022 profile: "Boeing (1,550)." https://esd.wa.gov/media/pdf/919/pierce20county20profile202022pdf ; https://www.choosetacomapierce.org/locating-your-business/major-employers. **Not in graph.** | **ADD NODE** (econ org) — connect to JBLM, Chamber, EDB. |
| **Amazon** | **CONFIRMED GAP** | ~1,400-1,800 distribution jobs; largest distribution employer in county. ESD: "Amazon distribution centers (1,800)." https://esd.wa.gov/media/pdf/919/pierce20county20profile202022pdf. **Not in graph.** | **ADD NODE** (econ org) — connect to Chamber, EDB. |
| **Tacoma-Pierce County Health Department** | **CONFIRMED GAP** | Director **Chantell Harmon Reed**, 284 staff, Board of Health includes Mello, Hitchen, Herrera, Bushnell, Sadalge, Yambe. https://tpchd.org/info/about-us/director-of-health ; https://www.thenewstribune.com/news/local/article315197935.html. A major public-health authority with a county/city board — **not in graph.** | **ADD NODE** (gov org) — connect to Mello, County Council, City Council, KNKX. |
| **UW Tacoma chancellor** | **NOT A GAP** | **Sheila Edwards Lange** IS in the graph (#121, 0.015). Confirmed chancellor since 2021. https://www.tacoma.uw.edu/chancellor. | **NO CHANGE** (present). |
| **Sound Transit CEO** | **MINOR GAP** | Interim CEO **Goran Sparrman** (regional, King County-centric). https://www.soundtransit.org/get-to-know-us/news-events/news-releases/board-to-consider-goran-sparrmans-appointment-sound. The more relevant Pierce County actor is **Ryan Mello as Sound Transit Vice Chair** (evidence/20) — already in graph. | **NO CHANGE** (CEO is regional; Mello's board role is the Pierce lever). |
| **Banner Bank** | **CONFIRMED GAP** | AJ Gordon of Banner Bank was Chamber Board Chair (evidence/13). Banner ranked #27 on Forbes' best banks. https://www.bizjournals.com/seattle/news/2025/02/10/forbes-100-best-banks-2025.html. **Not in graph.** | **ADD NODE** (econ org) — connect to Chamber. |
| **Umpqua Bank** | **NOT A GAP** | Umpqua is a **subsidiary of Columbia Banking System** (Columbia Bank's parent). https://www.prnewswire.com/news-releases/umpqua-bank-and-parent-company-columbia-banking-system-celebrate-anniversaries-with-1m-in-grants-for-local-nonprofits-302016954.html. Covered by the Columbia Bank node. | **NO CHANGE** (covered by Columbia Bank). |
| **Puget Sound Energy** | **CONFIRMED GAP** | Largest utility in WA; serves Pierce County; operates Frederickson Generating Stations (147MW + 275MW) and Electron Hydro (Puyallup River) in Pierce County. https://en.wikipedia.org/wiki/Puget_Sound_Energy. **Not in graph.** | **ADD NODE** (econ org) — connect to County, TPU, Chamber. |
| **Top vendors/contractors** | **UNVERIFIED** | Evidence files flag this as a research gap (evidence/01: "Top county contractors (vendors, contract values, no-bid awards)") but no specific names are documented. Cannot confirm a named gap without data. | **DEFER** — flag for Phase 2; no verified names to add. |
| **Developers beyond growth-machine list** | **NOT A GAP** | The graph already has the growth-machine list (Rush, Miles Sand & Gravel, Southport, Tucci, Lincoln Park, Nall Capital). No additional named developers verified in evidence. | **NO CHANGE** (list is complete per evidence). |

---

## SUMMARY — PRIORITIZED ACTIONS

**Must fix (CONFIRMED GAPS):**
1. **Tacoma City Council** — ADD node (gov org). Biggest structural omission in the map.
2. **Anders Ibsen** — RAISE from 0.008 to ~0.10-0.15 (mayor of 23% of county population).
3. **Tacoma-Pierce County Health Department** — ADD node (gov org).
4. **Boeing, Amazon, Puget Sound Energy, Banner Bank** — ADD econ nodes.
5. **Prosecuting Attorney's Office + Federal District Court (WDWA/Tacoma)** — ADD legal nodes.
6. **KNKX** — CONNECT + raise from 0.000.
7. **Central Pierce Fire, Bethel SD, Catholic Archdiocese, Columbia Bank, Tacoma Housing Authority** — CONNECT + raise from 0.000 (all real actors, all inconsistent with peer nodes that have power).

**Remove (orphaned placeholders):**
- **iHeartMedia, Audacy, Lotus** (national chains, no local editorial power).
- **Life Center** (no documented political power).

**No change (task premises factually wrong):**
- **County Council** — all 7 members present (Yambe, Denson included).
- **County row officers** — Assessor-Treasurer, Auditor, PA, Sheriff all present; no separate Treasurer; Clerk is appointed (not elected) in Pierce.
- **Port of Tacoma commissioners** — all 5 present (McCarthy, Marzano, Keller, Wilcox, Ang).
- **UW Tacoma chancellor** — Sheila Edwards Lange present.

**Weighting flags (present but mis-ranked):**
- Ibsen (0.008), Port commissioners (~0.03 avg vs 0.236 org), Central Pierce Fire (0.000 vs peer districts 0.016-0.023).

---

## SOURCES (primary)
- Tacoma Mayor: https://tacoma.gov/profile/office-of-mayor-anders-ibsen
- Pierce County elected officials: https://www.piercecountywa.gov
- MRSC county officials (clerk appointed in Pierce): https://mrsc.org/explore-topics/officials/roles/county-officials
- Port of Tacoma Commission: https://www.portoftacoma.com/commission ; https://www.portoftacoma.com/news/port-tacoma-designates-commission-officer-positions-2026
- WDWA federal judges: https://ballotpedia.org/United_States_District_Court_for_the_Western_District_of_Washington ; https://www.wawd.uscourts.gov
- KNKX reporting: https://www.knkx.org/tacoma/2026-04-21/... ; https://www.knkx.org/tacoma/2026-07-02/...
- McClatchy strike: https://www.nwpb.org/local/2026-05-26/...
- Central Pierce Fire merger: https://www.centralpiercefire.org/wp-content/uploads/2026-02-09-Board-Packet.pdf ; https://www.thenewstribune.com/news/local/community/puyallup-herald/ph-news/article304014676.html
- Columbia Bank/Umpqua: https://www.prnewswire.com/news-releases/umpqua-bank-and-parent-company-columbia-banking-system-celebrate-anniversaries-with-1m-in-grants-for-local-nonprofits-302016954.html
- Banner Bank: https://www.bizjournals.com/seattle/news/2025/02/10/forbes-100-best-banks-2025.html
- THA: https://www.tacomahousing.org/news/tacoma-housing-authority-executive-director-michael-mirra-announces-his-retirement
- TPCHD: https://tpchd.org/info/about-us/director-of-health ; https://www.thenewstribune.com/news/local/article315197935.html
- UW Tacoma: https://www.tacoma.uw.edu/chancellor
- Sound Transit CEO: https://www.soundtransit.org/get-to-know-us/news-events/news-releases/board-to-consider-goran-sparrmans-appointment-sound
- Employers (Boeing/Amazon): https://esd.wa.gov/media/pdf/919/pierce20county20profile202022pdf ; https://www.choosetacomapierce.org/locating-your-business/major-employers
- Puget Sound Energy: https://en.wikipedia.org/wiki/Puget_Sound_Energy
