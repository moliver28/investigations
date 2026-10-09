<!-- entity-profile:v1 organization -->
# Pierce Dems — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/pierce-dem.md`
**Entity ID:** `pierce-dem` · **Type:** organization · **Domain:** political
**Tier:** tier1 · **Rank:** 15/163 · **Composite power:** 0.120 (capped at 0.12 — party nodes are centrality artifacts)
**Graph description:** Pierce County Democratic Party (PCDCC) — county-wide umbrella organization; endorses candidates, trains campaigns, controls PCO network
**Known facts:** Controls 4 council seats + Exec; 3 state Senate seats; Union coalition (HDCC, WEA, UFCW, IBEW); 17 graph edges; campaign finance violation settlement $38,520 (2017)
**Status:** ✅ researched — 2026-09-19 — tier1-chunk3
**Sources:** 11/10 (minimum for tier1)

---

## 0. Why this person or group is on the map
- **Inclusion rule — power and decision-making.** The Pierce County Democratic Central Committee (PCDCC) is on this map as the county Democratic Party. It backs candidates with endorsements, trains campaigns, fills empty elected offices, and runs the Precinct Committee Officer (PCO) network.
- The PCDCC is a statutory party organization under Washington law. It has formal powers to endorse candidates and to fill vacancies in partisan offices.
- **Important caveat:** Party nodes are an artifact of how the graph works. They collect all the "member" edges from legislators who share that party label. That makes them look more connected than they really are. The PCDCC's 17 graph edges mostly come from Democratic officials — that is party affiliation, not a chain of command. The composite score is capped at 0.12 to correct for this.
- **Adjacent but excluded:** The Washington State Democratic Central Committee (WSDCC) is the parent. King County Democrats is a peer. Pierce County Republicans is the counterpart. LD-level Democratic groups (2nd, 25th, 26th, 27th, 28th, 29th, 31st) are sub-units, not separate map nodes.

## 1. Who they are
- **Legal name:** Pierce County Democratic Central Committee (PCDCC).
- **Common name:** Pierce County Democrats / Pierce Dems.
- **Entity type:** Political committee registered with the Washington State Public Disclosure Commission (PDC). Not a 501(c)(3) or 501(c)(6). Governed by state law (RCW 42.17A) and the WSDCC charter.
- **EIN or PDC registration:** Not verified. Political committees usually file with the PDC, not the IRS.
- **Parent and sub-units:** Under the Washington State Democratic Central Committee. Legislative District (LD) Democratic groups (2nd, 25th, 26th, 27th, 28th, 29th, 31st) work under the PCDCC.
- **Ownership chain:** Democratic National Committee → Washington State Democratic Central Committee → Pierce County Democratic Central Committee → LD Democratic organizations.
- **Governing law:** RCW 42.17A (Public Disclosure Commission); WSDCC charter; PCDCC bylaws.
- **Address:** PO Box (per the official site). Office: 3049 S 36th St, Tacoma, WA 98409 — same building as PCCLC.

## 2. Their career and offices
- **2025–2026 Officers (from the official website):**

| Position | Name |
|---|---|
| Chair | Marianna Hyke |
| Vice Chair | Jared Richardson |
| 2nd Vice Chair | Justin Camarata |
| Vice Chair of Outreach | Megan Capes |
| Vice Chair of PCO Development | Carlos Lugo |
| Vice Chair of Communications | Jenn Marie Strickling-Severns |
| Membership Chair | Wendy Wright |
| Sgt at Arms | Jared Denton |
| Treasurer | Jake Hunter |
| Assistant Treasurer | Steven Ketelsen |
| Secretary | Derek Martinez |
| State Committee Member | Drena Sellers |
| State Committee Member | Cameron Severns |

- **Previous Chair:** Kathy Orlando. The move from Orlando to Hyke is not verified in detail.
- **Board overlaps:** Jenn Marie Strickling-Severns serves as both PCDCC Vice Chair of Communications and Chair of the 25th LD Democrats. That is a confirmed overlap inside the party. No other officer shows up as a separate map entity.
- **Full central committee:** Includes all elected and appointed PCOs plus dues-paying members. PCO lists live in Google Sheets on the website. The exact PCO count is not verified.

## 3. Where their power comes from
- **Power held.** The PCDCC has statutory party power under Washington law. It endorses candidates, fills vacancies in partisan Democratic offices, organizes the PCO network, and coordinates campaigns across Pierce County.
- Its real power is mediated and limited. The PCDCC does not tell elected Democrats how to vote. It can endorse, train, and organize volunteers. The graph's cap of 0.12 composite reflects this: 17 edges inflate the count, but actual decision-making power is weaker than that suggests.
- **Political domain:** The main power levers are candidate endorsements and PCO organizing. Endorsements matter in primary elections — they signal support and direct volunteer and donor energy.
- **Government domain overlap.** The PCDCC's endorsed Democrats hold many offices: Ryan Mello (Pierce County Executive), Laurie Jinkins (Speaker of the WA House, 27th LD), Melanie Morgan (29th LD), Yasmin Trudeau (27th LD Senate), T'wina Nobles (28th LD Senate), Steve Conway (29th LD Senate), Emily Randall (6th LD Senate, now in Congress), Marilyn Strickland (10th CD), Maria Cantwell (US Senate), Patty Murray (US Senate). The graph's 10 "member" edges are party affiliation, not a command structure.
- **Labor domain overlap.** The Pierce County Central Labor Council (PCCLC) is "aligned" with the PCDCC, weight 4. PCCLC's 2026 endorsements overlap with PCDCC picks. The Washington Education Association (WEA) PAC is also "aligned," weight 3. The union coalition — House Democratic Campaign Committee (HDCC), WEA, United Food and Commercial Workers (UFCW), and International Brotherhood of Electrical Workers (IBEW) — provides volunteers and money.
- **Economic domain overlap.** MultiCare Health donated to the PCDCC, weight 3. The Puyallup Tribe donated, weight 3. Those are institutional donors in the economic space.
- **Key facts:**
  - **Who is endorsed?** The PCDCC backed Amanda Cuthbert and Davida Haygood for Puyallup School Board in 2023. The 2026 endorsement process is on the website.
  - **PAC spending?** Not verified. The PCDCC files C3 (contributions) and C4 (expenditures) reports with the PDC. A 2017 complaint showed $63,643 in unreported contributions and $90,357 in unreported spending over three years.
  - **Party machinery.** The PCDCC controls the PCO network, runs the PCO handbook, and coordinates with LD organizations.
  - **Candidate training?** The website links to candidate resources. The Chamber's Candidate Academy trains candidates across party lines — adjacent to PCDCC, but not PCDCC-run.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Endorsed Democratic candidates gain name recognition, volunteers, and party support. The union coalition (PCCLC, WEA PAC) benefits from aligning with a major party. Pierce County Democratic voters get organized party infrastructure. | #3, #9 |
| Who sits | 13 officers plus all PCOs make up the governing body. State Committee Members (Drena Sellers, Cameron Severns) represent Pierce County at the WSDCC. No officer is a separate map entity. | #1 |
| Who governs | The PCDCC runs endorsements, PCO appointments, vacancy fills, and bylaws. Chair Marianna Hyke directs operations. Treasurer Jake Hunter handles finances. | #1 |
| Who wins | Endorsed candidates who won: Laurie Jinkins (Speaker of the House), Ryan Mello (County Executive), Rosie Ayala (Council D4), Jani Hitchen (Council D2). PCDCC-backed Democrats hold 4 County Council seats plus the Executive. | graph + #8 |

## 4. Their money
- **Budget:** Not verified for the current year. The 2017 complaint showed about $30K to $45K per year in contributions and spending for 2015–2017. Current numbers require pulling PDC C3/C4 reports.
- **Funding sources:** Membership dues ($27 regular, $15 hardship); ActBlue donations; institutional donations (MultiCare, Puyallup Tribe); possible labor coalition contributions.
- **Government funding:** None. Political parties do not get government money.
- **Tax status:** Political committee. Not tax-exempt under 501(c)(3) or (c)(6). Donations are not tax-deductible.
- **Property:** None identified. The PCDCC operates from a PO Box and shares an office address with PCCLC at 3049 S 36th St, Tacoma.
- **Levy or bond history:** Not applicable.

## 5. How they touch government
- **Campaign donations.** The PCDCC gives to endorsed candidates. The graph shows donations to Ryan Mello (weight 5), Rosie Ayala (weight 4), and Jani Hitchen (weight 4). These are PDC C3 filings. Exact amounts need PDC lookup.
- **Campaign finance violations.** In August 2017, the Washington State Attorney General filed a complaint against the PCDCC. The PCDCC settled for $38,520 ($31,780 fine with $15,890 suspended for four years). Violations included $63,643 in late-reported contributions (92 reports, up to 179 days late), $90,357 in late-reported spending (16 reports, up to 171 days late), and $34,791 in unreported debts. The PCDCC did not file any 2017 reports until after the AGO opened its investigation. This is a confirmed, legally documented controversy.
- **Lobbying.** Political parties do not register as lobbyists. The PCDCC's advocacy is electoral, not legislative lobbying.
- **Contracts or grants.** None. Political parties do not receive government contracts.
- **Regulation.** The PCDCC is regulated by the Washington Public Disclosure Commission (PDC) and RCW 42.17A. The 2017 AGO action is the main documented regulatory interaction.
- **Vacancy fills.** Under Washington law, the PCDCC can fill vacancies in partisan Democratic offices. When a Democratic officeholder resigns, the PCDCC's PCOs pick a replacement. That is a real governmental power. Specific recent fills are not verified.

## 6. Other seats they hold
| Organization | Relationship | Domain | Cross-reference |
|---|---|---|---|
| PCCLC (`pclc`) | aligned (weight 4) | Labor / Political | Graph edge; confirmed by overlapping endorsements (#9) |
| WEA PAC (`wea-pac`) | aligned (weight 3) | Labor / Education / Political | Graph edge |
| Ryan Mello (`ryan-mello`) | donated (weight 5) | Government / Political | Graph edge; Mello is County Executive |
| Puyallup Tribe (`puyallup-tribe`) | donated (weight 3) | Economic / Political | Graph edge |
| MultiCare Health (`multicare`) | donated (weight 3) | Economic / Health / Political | Graph edge |
| Rosie Ayala (`rosie-ayala`) | donated (weight 4) | Government / Political | Graph edge; Council D4 |
| Jani Hitchen (`jani-hitchen`) | donated (weight 4) | Government / Political | Graph edge; Council D2 |
| 10 Democratic legislators | member (weight 3 each) | Government / Political | Graph edges; affiliation, not control |

- **PCCLC link.** PCCLC's 2026 endorsements overlap with PCDCC picks, confirming the "aligned" edge. PCCLC Secretary-Treasurer Nathe Lawver runs the labor endorsement process that tracks PCDCC choices.
- **Chamber Candidate Academy.** The Tacoma-Pierce County Chamber runs a Candidate Academy program that trains candidates across party lines. This creates an indirect PCDCC–Chamber overlap through shared training.

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| WEA PAC (`wea-pac`) | aligned | 3 |
| PCCLC (`pclc`) | aligned | 4 |
| Ryan Mello (`ryan-mello`) | donated | 5 |
| Puyallup Tribe (`puyallup-tribe`) | donated | 3 |
| MultiCare Health (`multicare`) | donated | 3 |
| Rosie Ayala (`rosie-ayala`) | donated | 4 |
| Jani Hitchen (`jani-hitchen`) | donated | 4 |
| Yasmin Trudeau (D-27) (`yasmin-trudeau`) | member | 3 |
| T'wina Nobles (D-28) (`twina-nobles`) | member | 3 |
| Steve Conway (D-29) (`steve-conway`) | member | 3 |
| Laurie Jinkins (D-27) (`laurie-jinkins`) | member | 3 |
| Melanie Morgan (D-29) (`melanie-morgan`) | member | 3 |
| Maria Cantwell (`maria-cantwell`) | member | 3 |
| Patty Murray (`patty-murray`) | member | 3 |
| Emily Randall (D-6) (`emily-randall`) | member | 3 |
| Marilyn Strickland (D-10) (`marilyn-strickland`) | member | 3 |

**Network analysis.** The PCDCC has 16 graph edges — the most in this chunk. But 10 of those are low-weight (3) "member" edges from Democratic officials. They show party affiliation, not directed control. Laurie Jinkins does not take orders from the PCDCC — she is the Speaker of the House. The graph's cap of 0.12 composite correctly accounts for this artifact. The meaningful edges are PCCLC aligned (4), Mello donated (5), Ayala donated (4), Hitchen donated (4). Those reflect the PCDCC's real power: the labor coalition and candidate donations. The PCDCC's rank of 15/163 is inflated by the member-edge artifact. It is a network hub, not the 15th most powerful entity in Pierce County.

## 1. Who they are
| # | Claim | Source | URL | Type | Reliability |
|---|-------|--------|-----|------|-------------|
| 1 | 2025–2026 PCDCC officers (Chair: Marianna Hyke, Vice Chair: Jared Richardson, etc.); 7 LD organizations listed; bylaws and platform pages | Pierce County Democrats — official website (homepage) | https://www.piercecountydems.com | primary | 0.8 |
| 2 | Membership dues ($27 regular, $15 hardship); ActBlue donation page; PCO role description; PCO election process; PCO handbook links; PCO lists in Google Sheets; "PCOs... help fill vacancies in elected office" | Pierce County Democrats — official website (Get Involved page) | https://www.piercecountydems.com/involved | primary | 0.8 |
| 3 | PCDCC endorsed Amanda Cuthbert (Puyallup SD Pos 3) and Davida Haygood (Puyallup SD Pos 5) in 2023 general election; 2 total endorsees tracked by Ballotpedia | Ballotpedia — Endorsements by Pierce County, Wash., Democratic Party | https://ballotpedia.org/Endorsements_by_Pierce_County,_Wash.,_Democratic_Party | secondary | 0.8 |
| 4 | Endorsements page exists with link to latest endorsed candidates from local Legislative Districts | Pierce County Democrats — official website (Endorsements page) | https://www.piercecountydems.com/copy-of-endorsements | primary | 0.8 |
| 5 | AGO filed campaign finance complaint against PCDCC (Aug 2017); $63,643 unreported contributions (92 reports, up to 179 days late); $90,357 unreported expenditures (16 reports, up to 171 days late); $34,791 unreported debts; failed to file 2017 reports until after investigation | Washington State Attorney General's Office — official press release | https://www.atg.wa.gov/news/news-releases/ago-files-campaign-finance-complaint-against-pierce-county-democrats | primary | 0.95 |
| 6 | PCDCC settled for $38,520 ($31,780 fine, $15,890 suspended 4 years); Thurston Superior Court #17-2-04616-34; detailed breakdown of violations | We the Governed (news blog with court documents) | https://www.wethegoverned.com/washington-state-democrats-find-hope-in-ags-38520-fine-against-the-pierce-county-democrats | secondary | 0.7 |
| 7 | Kathy Orlando identified as PCDCC Chair (April 2019 Facebook post) | Pierce County Democrats — Facebook page | https://www.facebook.com/piercecountydems/posts/greetings-from-kathy-orlando-pcdcc-chairapril-1-2019past-time-for-an-update-for-/2129954907052021 | primary (self-published) | 0.4 |
| 8 | PCDCC address: 3049 S 36th St, Tacoma, WA 98409 (same as PCCLC); "Pierce County Democratic Central Committee (PCDCC) is the county-wide umbrella organization" | Pierce County Democrats — Facebook page (About section) | https://www.facebook.com/piercecountydems | primary (self-published) | 0.4 |
| 9 | PCCLC 2026 primary endorsements: Laurie Jinkins (27th), Sharlett Mena (29th Sen), Linda Farmer (Auditor), Kelsey Barrans (D1), Bryan Yambe (D5), Brenda Lykins (D7) — overlap with PCDCC-aligned candidates | Pierce County Central Labor Council — official AFL-CIO website | https://unionhall.aflcio.org/pcclc/news/2026-pierce-county-primary-election-endorsements | primary | 0.9 |
| 10 | Chamber operates Candidate Academy program (trains candidates across party lines) | Tacoma-Pierce County Chamber — official website | https://www.tacomachamber.org/candidateacademy.html | primary | 0.8 |
| 11 | PCCLC office address: 3049 South 36th St., Suite 201, Tacoma, WA 98409 (same building as PCDCC) | PCCLC — official AFL-CIO website (Secretary-Treasurer's Statement) | https://unionhall.aflcio.org/pcclc/news/secretary-treasurers-statement-mcclatchy-layoffs | primary | 0.8 |

## 1. Who they are
1. **PDC C3/C4 reports:** Retrieve the PCDCC's current campaign finance reports from the WA PDC database. What is the current annual budget? How much does it donate to candidates? What are the exact contribution amounts from MultiCare, Puyallup Tribe, and other institutional donors?
2. **2017 AGO settlement compliance:** Has the PCDCC committed any additional violations since the 2017 settlement? The $15,890 suspended fine was contingent on no additional violations for four years (through ~2021). Check PDC enforcement actions post-2017.
3. **Endorsement process:** How does the PCDCC endorsement process work? Who votes? What threshold is required? Are there contested endorsements? Retrieve PCDCC bylaws from the website.
4. **Vacancy fills:** Has the PCDCC filled any elected office vacancies in recent years? When a Democratic officeholder resigns, the PCDCC PCOs nominate a replacement. This is a significant governmental power — trace specific instances.
5. **PCO count:** How many PCOs does the PCDCC currently have? Count from the Google Sheets linked on the website (source #2). This quantifies the PCDCC's grassroots organizing capacity.
6. **PCDCC–PCCLC relationship:** The PCDCC and PCCLC share an office address (3049 S 36th St, source #8, #11). Is this a formal partnership? Does the PCDCC rent from the PCCLC? This physical co-location suggests a deep organizational tie.
7. **Centrality artifact analysis:** The graph caps party nodes at 0.12 composite. Verify this cap by comparing the PCDCC's actual decision-making power (endorsement + vacancy fill + PCO organization) against its 16-edge who they are connected to. Should the cap be lower?

## 1. Who they are
- **Verdict:** The PCDCC controls the Democratic Party endorsement machinery in Pierce County — it endorses candidates, organizes PCOs, fills vacancies in partisan offices, and coordinates with aligned labor organizations (PCCLC, WEA PAC). However, its actual power is **weaker than its who they are connected to suggests**: the 10 'member' edges from Democratic elected officials represent party affiliation, not directed control. The PCDCC cannot tell Laurie Jinkins (Speaker of the House) or Maria Cantwell (US Senator) how to vote. The graph's cap at 0.12 composite correctly accounts for this centrality artifact. The PCDCC's real power levers are: (1) endorsement signals in primary elections, (2) PCO organization and volunteer capacity, (3) vacancy-fill authority, and (4) coordination with the labor coalition.
- **Conflicts-of-interest flags (defense counter-argument anticipated):** (1) The 2017 campaign finance violations ($63K unreported contributions, $90K unreported expenditures, source #5) demonstrate a history of financial opacity. (2) Institutional donations from MultiCare (a health system) and Puyallup Tribe (a sovereign economic entity) to a political party that endorses candidates who oversee health policy and tribal relations create potential conflict-of-interest concerns. (3) Sharing an office address with PCCLC (source #8, #11) suggests an organizational melding that may compromise the PCDCC's independence from labor. **Defense counter:** (1) The 2017 violations were settled and the PCDCC paid $38,520 in penalties; the suspended fine created a compliance incentive. (2) Institutional donations to political parties are legal and common; they are publicly reported through PDC filings. (3) Co-location with PCCLC is an efficiency measure, not evidence of improper control — many political organizations share office space with aligned groups.
- **Analysis of alternatives :** The opposing reading is that the PCDCC is a volunteer-run political organization with limited actual power — its endorsements are often rubber-stamps for incumbents, its PCO network is incomplete, and its financial resources are modest (~$30K–$45K annually based on 2015–2017 data, source #5). Under this reading, the PCDCC's rank 15/163 is entirely a centrality artifact and should be much lower. The counter to this: the PCDCC's vacancy-fill authority is a genuine governmental power (when a Democratic officeholder resigns, the PCDCC chooses the replacement), and its endorsement signal materially affects primary outcomes in a Democratic-leaning county.
- **Confidence:** Medium. Primary sources confirm the PCDCC's existence, officer roster, and endorsement activity (official website, reliability 0.8). The 2017 AGO complaint is confirmed by the Attorney General's own press release (reliability 0.95). However, current financial data (budget, donation amounts, expenditure totals) is UNVERIFIED — requires PDC C3/C4 retrieval. The 10 'member' edges are confirmed by public party affiliation records but overstate the PCDCC's actual power over those officials. The centrality-artifact caveat is well-supported by the graph structure.
- **VERIFIED stamp:** 2026-09-19 — tier1-chunk3 researcher
 (submit)<!-- Each line must match exactly:
<id>, target=<id>, relationship=<REL>, weight=<n>, note="..."
 REL whitelist: member, board, board_chair, chair, ceo, president, commissioner,
 owner, owned_by, parent, donated, ie, lobbying, lobbies, endorses,
 trains_candidates, federal_funding, state_funding, federal_appropriations,
 transit_funding, appropriates, property_tax_levy, levy, levy_funding, taxing,
 municipal, tax_exempt_status, tax_exemption, sovereignty, federal_land_grant,
 school_bond, ballot_measure, wellfound_jv, jv, operates, land_use, contract,
 family, mentor, staffer, appointed, grant, education, colleague, social -->
pierce-dem, target=pclc, relationship=colleague, weight=3, note="https://www.piercecountydems.com and https://unionhall.aflcio.org/pcclc/news/secretary-treasurers-statement-mcclatchy-layoffs — PCDCC and PCCLC share office address at 3049 S 36th St, Tacoma WA 98409; overlapping 2026 endorsements confirm aligned relationship"