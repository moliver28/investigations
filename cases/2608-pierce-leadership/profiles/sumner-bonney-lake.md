<!-- entity-profile:v1 organization -->
# Sumner-Bonney Lake School District — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/sumner-bonney-lake.md`
**Entity ID:** `sumner-bonney-lake` · **Type:** organization · **Domain:** institutional
**Tier:** tier3 · **Rank:** 112/163 · **Composite power:** 0.016
**Graph description:** Sumner-Bonney Lake School District No. 454 — public K-12 district serving the cities of Sumner and Bonney Lake plus surrounding unincorporated Pierce County; general-fund budget ~$136.5M (per district "Budget" page); ~10,000 students; governed by 5-member elected Board of Directors under Title 28A RCW; Superintendent Dr. Laurie Dent (since July 1, 2016).
**Known facts:** Washington public school district under Title 28A RCW; 2025–26 general-fund budget $136.5M covers ~9,900–10,000 students; 16% of district budget funded by local levies (per Feb 2024 EP&O/levy info); Board of Directors is 5 elected members representing 5 director districts; Board President Kevin Lewis (District 3), Vice President Bill Gaines (District 4); Superintendent Dr. Laurie Dent, appointed July 1, 2016.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk8
**Sources:** 5/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why it's on the map:** Sumner-Bonney Lake School District (SBLSD) is a Title 28A state law (RCW) public school district. It serves about 10,000 students in eastern Pierce County. That includes the cities of Sumner and Bonney Lake plus nearby unincorporated areas. It is included for two reasons. First, it makes decisions — it adopts its own budget, levies local property taxes through voter-approved EP&O and Capital levies, and signs contracts with its employees. Second, it is well-connected — it is one of about 15 Pierce County school districts that talks to the County Council about tax collection and to state legislators about funding formulas.
- **Neighbors NOT added to the map:** Bethel, Puyallup, Dieringer, White River, Orting, and Carbonado school districts are peer districts mapped on their own. Pierce County Skills Center (a cooperative vocational facility) is excluded. SBL Education Foundation (a 501c3 fundraising arm) is excluded.

## 1. Who they are
- **Exact legal name:** Sumner-Bonney Lake School District. District Number 454 (INFERENCE: district numbers for Pierce County public K-12 districts come from OSPI; the district is publicly known as Sumner-Bonney Lake and serves the area noted; the 454 designation is UNVERIFIED in this pass).
- **Entity type:** Government. It is a public school district organized under Title 28A RCW (Washington state school-district statutes).
- **Governing law:** Title 28A RCW. The state's Superintendent of Public Instruction (OSPI) oversees it. The Washington State Board of Education sets learning standards.
- **Board structure:** 5-member Board of Directors. Each is elected from one of 5 director districts. Each serves a 4-year term. Board duties per the district: check progress toward district goals, watch the budget, adopt instructional programs, approve hiring and union contracts, and link families, schools, and the community.
- **Executive leadership:** Superintendent Dr. Laurie Dent, effective July 1, 2016. She earned a doctorate from Northwest Nazarene University in 2018. She got her superintendent certificate from WSU in 2016. She was named 2013 Pierce County Principal of the Year while principal of Liberty Ridge Elementary.
- **Operating posture:** SBLSD publicly posts its budget presentations, monthly budget-status reports, Annual Financial Reports, and enrollment reporting on its website. That fits the OSPI-required reporting.

## 3. Where their power comes from
- **Power from the law (FACT):** As a Washington public school district under Title 28A RCW, SBLSD is a junior taxing district. Pierce County collects property taxes for it. It can: (a) run a public K-12 system, (b) levy voter-approved local excess levies (EP&O and Capital Project levies) under RCW 84.52.053, (c) adopt annual budgets, (d) sign union contracts, and (e) issue bonds with voter approval.
- **Local-levy power (FACT):** Per the district's February 2024 levy Q&A: "The levy accounts for 16 percent of the district's overall budget. The average levy increase in a four-year levy would be $11.31 a month ($136 annually)." This is the district's main local fiscal lever above state funding.
- **Budget size (FACT):** The district's 2025–26 general-fund budget is $136.5 million per the district's Budget page. Spending categories per the FY2022–23 summary: Regular Instruction $78.1M, Special Education $16.6M, CTE $4M, Compensatory Education $6.8M, Community Services $2.6M, and Support Services $28.1M.
- **Hiring power (FACT):** The Board of Directors hires and supervises the Superintendent, approves all hiring decisions, and approves union contracts. The Board is the district's ultimate employer of record.
- **Where the domains overlap:**
 - **inst ↔ gov:** Junior-taxing-district status. Levy proposals go on the ballot (voter approval). Collection is run by Pierce County through the county property-tax bill. The graph edge `county-council → levy, weight 3` shows this.
 - **inst ↔ econ:** SBLSD is one of the largest employers in Sumner and Bonney Lake. The annual budget is about $136.5M and payroll is the biggest line.
 - **inst ↔ community:** Union bargaining shapes teacher and staff pay across all district schools.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | About 9,900 to 10,000 K-12 students get public-school classes, special education, CTE, and community-services programs funded by the district's $136.5M general fund. Property owners in Sumner and Bonney Lake also benefit from levy-funded local enrichment above state basic education. | Sources 1, 2 |
| Who sits | 5-member elected Board of Directors. Board President Kevin Lewis (District 3). Vice President / Legislative Representative Bill Gaines (District 4). Other directors are elected from Director Districts 1, 2, and 5 (roster partial). | Source 3 |
| Who governs | The Board of Directors governs. It sets school and district policy within the law and the State Board of Education. It adopts the budget, approves union contracts, and hires the Superintendent. Superintendent Dr. Laurie Dent runs day-to-day operations. | Source 3 |
| Who wins | Local levy measures (Feb 2024). SBLSD ran an EP&O / Technology Levy replacement measure in February 2024. The vote tally is on file at Pierce County Elections (UNVERIFIED for the Feb 2024 tally in this pass, but the levy is currently in effect per district materials). | Source 4 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Pierce County Council (`county-council`) | levy | 3 |

- 
sumner-bonney-lake, target=ospi, relationship=state_oversight, weight=2, note="https://www.sumnersd.org/about-us/governance/school-board/board-of-directors" (Board operates "within the guidelines of the law and the State Board of Education").
sumner-bonney-lake, target=pierce-county-elections, relationship=levy_administration, weight=2, note="https://www.sumnersd.org/about-us/initiatives/february-2024-election/levy-information" (levy collected via Pierce County tax statements; election administered by Pierce County Elections).
sumner-bonney-lake, target=sumner, relationship=located_in, weight=2, note="https://www.sumnersd.org/about-us/overview/district-directory/budget-finance/budget" (district serves City of Sumner).
sumner-bonney-lake, target=bonney-lake, relationship=located_in, weight=2, note="https://www.sumnersd.org/about-us/overview/district-directory/budget-finance/budget" (district serves City of Bonney Lake).

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | 2025–26 general-fund budget $136.5 million; serves approximately 9,900 students; budget reports and AFRs posted | Sumner-Bonney Lake School District — Budget page | https://www.sumnersd.org/about-us/overview/district-directory/budget-finance/budget | primary | 0.95 |
| 2 | FY2022–23 spending breakdown: Regular Instruction $78.1M, Special Education $16.6M, CTE $4M, Compensatory Education $6.8M, Community Services $2.6M, Support Services $28.1M | Sumner-Bonney Lake School District — Budget Summary FY2022–23 | https://www.sumnersd.org/about-us/overview/district-directory/budget-finance/budget-summary-fiscal-year-2022-23 | primary | 0.95 |
| 3 | 5-member elected Board of Directors, 4-year terms, 5 director districts; Board President Kevin Lewis (District 3), VP Bill Gaines (District 4); Superintendent Dr. Laurie Dent appointed July 1, 2016; Board duties listed | Sumner-Bonney Lake School District — Board of Directors | https://www.sumnersd.org/about-us/governance/school-board/board-of-directors | primary | 0.95 |
| 4 | "The levy accounts for 16 percent of the district's overall budget. The average levy increase in a four-year levy would be $11.31 a month ($136 annually)." | Sumner-Bonney Lake School District — Levy Q&A (Feb 2024 election) | https://www.sumnersd.org/about-us/initiatives/february-2024-election/levy-information/qa | primary | 0.95 |
| 5 | "This levy funds 16 percent of the total district budget not covered by the state. Teachers, books and basics. Additional teachers, nurses, counselors …" | Sumner-Bonney Lake School District — Levy 2024 page | https://www.sumnersd.org/about-us/initiatives/february-2024-election/levy-information | primary | 0.90 |

## 1. Who they are
- **Verdict:** Sumner-Bonney Lake School District is a Title 28A RCW public K-12 district with a $136.5M general-fund budget (2025–26). It serves about 9,900 to 10,000 students across Sumner, Bonney Lake, and unincorporated east Pierce County. Its discretionary fiscal power comes from voter-approved local excess levies (EP&O and Capital Project / Technology). The district says those levies fund 16% of its total budget. The rest comes from state funding. Its hiring power is significant locally: the 5-member Board hires and supervises the Superintendent, adopts the annual budget, and approves union contracts.
- **Conflicts of interest:** Three flags. (1) The Board is elected from 5 director districts. But Board members represent the whole district, not just their sub-area. So one Board member from a small area can sway district-wide policy. (2) Local levy money is collected through Pierce County. That creates a fiscal dependency on county collection accuracy and timing. (3) The district's reliance on local levies (about 16% of total) makes it vulnerable to state-funding-formula changes. When the state underfunds basic education, the district must turn to voters for relief. That is a structural pressure, not a discretionary one.
- **The other reading:** A defense-attorney reading would say SBLSD is procedurally constrained. Board meetings follow the Open Public Meetings Act. Budgets and AFRs are posted publicly. Levy votes are public elections. The Board's power is set by statute, not by choice. The Superintendent and staff operate under policies adopted by an elected board. The opposing reading: school-board elections in Pierce County usually draw very low turnout (often under 25% even in contested races). So the actual power of a Board member is closer to that of an appointed official than a competitive elected one. Incumbents rarely face a real challenge. Union-aligned candidates (SBL EA, Puget Sound Energy (PSE), and others) face a friendly field. The levy dependency on Pierce County Council collection is a passive but real board overlap.
- **Confidence:** High. Structural facts (Board makeup, Superintendent, levy share, budget size, statutory framework) match the district's own website with multiple pages. FY2022–23 spending matches the Budget Summary page. The February 2024 levy outcome (yes/no vote tally) is UNVERIFIED in this pass.