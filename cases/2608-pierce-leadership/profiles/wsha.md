<!-- entity-profile:v1 organization -->
# WSHA — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/wsha.md`
**Entity ID:** `wsha` · **Type:** organization · **Domain:** political
**Tier:** tier2 · **Rank:** 67/163 · **Composite power:** 0.031
**Graph description:** Washington State Hospital Association — 501(c)(6) trade association representing 100+ WA hospitals; operates HHFPAC political action committee.
**Known facts:** Founded 1961; EIN 91-0584257; HQ Seattle, WA; 2024 revenue $17.1M; represents 100+ hospitals; runs Hospitals for a Healthy Future PAC.
**Status:** ✅ researched — 2026-09-19 — tier2-chunk9 · **Last updated:** 2026-09-19
**Sources:** 8/5 (minimum for tier2)

---

## 0. Why this person or group is on the map
- **Why it is on the map — from holding office + decision-making:** WSHA is the main trade group for Washington State hospitals. That includes major Pierce County health systems (MultiCare, Virginia Mason Franciscan Health). Its lobbying, political action committee (PAC) spending, and regulatory advocacy directly affect health care policy and funding in Pierce County. (Sources 1, 3)
- **Adjacent but EXCLUDED candidates:** Washington State Medical Association (WSMA) — a separate group for doctors. American Hospital Association (AHA) — the national counterpart. Both are adjacent but not the subject here.

## 1. Who they are
- **Exact legal name:** Washington State Hospital Association
- **Type of entity:** A 501(c)(6) business league / trade association (Source 4)
- **tax ID number (EIN):** 91-0584257 (Source 4)
- **Founded:** 1961 (Source 5)
- **HQ:** 1201 3rd Avenue, Suite 1601, Seattle, WA 98101 (Source 1)
- **Parent/subsidiaries:** Washington Hospital Services (WHS) is the services arm of WSHA. It offers group purchasing and business solutions. (Source 6)
- **Governing law:** IRC 501(c)(6); Washington State nonprofit corporation law.
- **2024 finances:** Total revenue $17,096,686. Total expenses $19.8M. Total assets $33.5M. Net assets $26.6M. (Sources 4, 5)

## 3. Where their power comes from
- **Statutory/regulatory power:** WSHA has no direct statutory authority. But it has strong influence through lobbying the state legislature and Congress, advocating with regulatory agencies (WA State Health Care Authority, CMS), and building coalitions. It represents 100+ hospitals. That includes nonprofit, investor-owned, county, state, and military hospitals. (Sources 1, 3)
- **Market power:** WSHA is the unified voice of WA hospitals. It has outsized influence on health care policy. Its member hospitals control billions in annual revenue and employ tens of thousands in WA. (Source 3)
- **Political power:** WSHA runs the Hospitals for a Healthy Future PAC (HHFPAC). The PAC raised more than $236,000 in 2024. The 2025 goal is $275,000. Washington Hospital Services (a WSHA subsidiary) gave $200,000 and $143,190 to HHFPAC in 2022. (Sources 7, 8)
- **Domain overlaps:** Political (PAC, lobbying) + Health care (member hospitals) + Government (regulatory advocacy, Medicaid policy).

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Member hospitals benefit from WSHA's advocacy on Medicaid funding, regulatory relief, and payment rates | 3, 7 |
| Who sits | Board chaired by Florence Chang (President, MultiCare Health System, Tacoma) — a direct Pierce County link | 3 |
| Who governs | WSHA sets legislative priorities and PAC spending strategy. It lobbies the state legislature and Congress | 1, 3, 7 |
| Who wins | HHFPAC helps elect "health care champions." WSHA pushed successfully on Medicaid directed payment programs | 2, 7 |

## 5. How they touch government
- **Lobbying:** Registered federal lobbyists (LDA filings) — multiple lobbyists including Matthew Levin, Elizabeth Fortunato, and Nina Flink. (Source 2)
- **PAC spending:** Hospitals for a Healthy Future PAC (HHFPAC) — raised more than $208,000 in 2022, more than $236,000 in 2024. The 2025 goal is $275,000. Washington Hospital Services gave $343,190 to HHFPAC in 2022. (Sources 7, 8)
- **Federal advocacy:** WSHA leaders and members went to Capitol Hill (May 2025) to push on Medicaid funding and directed payment programs (Safety Net Assessment Program). (Source 3)
- **State lobbying:** Active in the WA State Legislature on hospital funding, workforce, and regulatory issues. Publishes annual legislative summaries. (Source 7)

## 6. Other seats they hold
- **Board of Directors:** Chaired by Florence Chang (President, MultiCare Health System, Tacoma) — a direct board overlap with MultiCare. Chair-Elect: Eric Moll (CEO, Mason Health). Secretary-Treasurer: Joel Gilbertson (Chief Executive, Providence Central Division). Cassie Sauer is President/CEO of WSHA. (Source 3)
- **Virginia Mason Franciscan Health (VMFH)/CHI link:** Ketul Patel, CEO of Virginia Mason Franciscan Health, became WSHA board chair in October 2024. (Source 3)
- **AWPHD:** Non-voting representative from the Association of Washington Public Hospital Districts. (Source 3)
- **WSMA:** Non-voting representative from Washington State Medical Association (John Scott, UW Medicine). (Source 3)
- **AHA:** Jon Hersen serves as AHA RPB Delegate. (Source 3)

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| MultiCare Health (`multicare`) | member | 4 |
| VMFH/CHI (`vmfh`) | member | 4 |
| HHFPAC (`hhfpac`) | runs | 5 |

- 
`wsha`, target=`providence`, relationship=member, weight=4, note="https://www.wsha.org/about-us/board-of-directors".
`wsha`, target=`multicare`, relationship=board_chair, weight=5, note="https://www.wsha.org/about-us/board-of-directors".
`wsha`, target=`vmfh`, relationship=board_chair, weight=4, note="https://www.wsha.org/press-room".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Organization description, HQ address, membership scope | WSHA About Us page | https://www.wsha.org/about-us | primary | 1.0 |
| 2 | Federal lobbyist registrations (LDA filings) | LegiStorm | https://www.legistorm.com/lobbying/lobbyists_by_org/id/7234/name/Washington_State_Hospital_Association/per_page/50/sort/end_year/type/asc.html | primary | 0.95 |
| 3 | Board of Directors roster, VMFH board chair, Capitol Hill advocacy | WSHA Board of Directors page | https://www.wsha.org/about-us/board-of-directors | primary | 1.0 |
| 4 | EIN 91-0584257, 501(c)(6) status, 2024 revenue $17.1M, assets $33.5M | Candid/ProPublica Nonprofit Explorer | https://app.candid.org/profile/8311300/washington-state-hospital-association-91-0584257 | primary | 0.95 |
| 5 | Founded 1961, FY2021 financials, Form 990 data | ProPublica Nonprofit Explorer | https://projects.propublica.org/nonprofits/organizations/910584257 | primary | 0.95 |
| 6 | Washington Hospital Services as WSHA services arm, board roster | WHS About page | https://www.wahospitalservices.com/about | primary | 1.0 |
| 7 | HHFPAC fundraising ($208K in 2022, $236K in 2024, $275K goal 2025) | WSHA 2023 & 2025 Legislative Summary PDFs | https://www.wsha.org/wp-content/uploads/WSHA_2023_LegislativeSummary_FNL.pdf | primary | 1.0 |
| 8 | Washington Hospital Services contributions to HHFPAC ($200K + $143K in 2022) | TransparencyUSA | https://www.transparencyusa.org/wa/contributor/washington-hospital-services/contributions?cycle=2022-election-cycle | primary | 0.90 |

## 1. Who they are
- **The bottom line:** WSHA has strong political influence. It speaks for 100+ WA hospitals. It runs a PAC (HHFPAC) and lobbies at the state and federal level. Its board is chaired by MultiCare's Florence Chang. That is a direct power link from Pierce County's largest health system to statewide health policy. WSHA's power comes from its members' collective economic weight and its ability to coordinate advocacy.
- **Conflicts-of-interest flags:** WSHA plays two roles: industry advocate and patient-safety promoter. That creates a built-in tension. HHFPAC contributions to lawmakers who then vote on hospital funding create a feedback loop. The board chair leading both MultiCare and WSHA concentrates power.
- **Analysis of alternatives:** An opposing reading: WSHA's power is derivative. It represents hospitals but does not control them. Individual health systems (MultiCare, Providence) have their own lobbying and political operations. WSHA's PAC spending ($236K) is modest compared to major statewide PACs.
- **Confidence:** High — extensive primary sources including the federal tax agency (IRS) filings, WSHA's own website, the state campaign-finance agency (PDC) contribution data, and federal lobbyist registrations.