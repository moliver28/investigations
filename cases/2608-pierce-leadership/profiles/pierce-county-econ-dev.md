<!-- entity-profile:v1 organization -->
# Pierce County Econ Dev — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/pierce-county-econ-dev.md`
**Entity ID:** `pierce-county-econ-dev` · **Type:** organization · **Domain:** government
**Tier:** tier3 · **Rank:** 137/163 · **Composite power:** 0.008
**Graph description:** Pierce County (WA) Economic Development Department — a division of Pierce County government under the County Executive. Housed at 950 Pacific Ave., Suite 720, Tacoma. Oversees business development, loan programs, tourism, Lodging Tax Advisory Committee, Tourism Promotion Area Commission, Arts Commission, and the 1 Percent for the Arts program.
**Known facts:** Long-serving Director Betty Nokes Capestany (now Betty Baublits) led 2018–2026; she moved to EDB Director of Investor Relations April 2026. Tom Pierson (Tacoma-Pierce County Chamber President & CEO) was appointed Acting Director while a permanent replacement is recruited.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk13-rescue · **Last updated:** 2026-09-19
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Inclusion rule (decision-making + well-connected):** This department sits inside Pierce County government's executive branch. The County Executive oversees it (per the 2026 job posting). It runs loan funds, tourism money, and the 1% for-Art program. It staffs three advisory bodies: the Lodging Tax Advisory Committee, the Tourism Promotion Area Commission, and the Arts Commission. It is a boundary-spanning unit. It is governmental in budget and reporting line. But it works like a quasi-quango with the EDB and the Tacoma-Pierce County Chamber.
- **Excluded but related:**
 - EDB (Economic Development Board for Tacoma-Pierce County) is a separate nonprofit. Now led by Bruce Kendall (transitioning to Meredith Neal). It is adjacent.
 - Tacoma-Pierce County Chamber is a separate 501(c)(6). Its President and CEO Tom Pierson is also Acting Director of this department in 2026. That is a network overlap, not a duplicate.
 - City of Tacoma Community & Economic Development is a separate municipal department.
 - Port of Tacoma is a separate special-purpose district. It is not part of this department.

## 1. Who they are
- **Exact legal name:** Pierce County Economic Development Department (also "Economic Development Department, Pierce County" in board rosters).
- **Entity type:** Government department / executive-branch agency (Pierce County, Washington).
- **Governing law:** Pierce County Charter and state law (RCW) 36 (counties). The 1% for-Art program follows RCW 36.32.235 et seq. as applied county-wide.
- **Tax ID number (EIN) / registration:** N/A. It operates under the Pierce County government EIN.
- **Parent / subsidiaries:** Sub-unit of the Pierce County Executive's office. It works with the Economic Development Corporation of Pierce County. Its board has reps from Tacoma, Port of Tacoma, MBDA, Pierce County Central Labor, Lakewood, Puyallup, and private industry.
- **Address:** 950 Pacific Ave., Suite 720, Tacoma, WA 98402. Phone (253) 798-6150.
- **Director classification (per official spec):** "Director of Economic Development." Salary band is $140,105 to $189,216 a year (GovernmentJobs posting 26-00251, opened 3/13/2026, closing 4/17/2026).

## 3. Where their power comes from
- **Statutory authority:** County-government department. It has no independent taxing power. It spends money from the County General Fund and pass-through lodging-tax receipts.
- **Decision-making authority:** Oversees business-development programs. Runs loan funds. Manages tourism funding and the Lodging Tax Advisory Committee. Manages the Tourism Promotion Area Commission and the Arts Commission (including 1% for-Art grants).
- **Power-domain overlap basis (scoring framework):**
 - Government — 0.5 weight: executive-branch department.
 - Economic (Workforce + Capital) — 0.4 weight: loan programs and tourism money.
 - Cultural/Arts — 0.2 weight: Arts Commission and 1% for-Art grants.
 - Tourism/Lodging — 0.2 weight: Tourism Promotion Area Commission staff.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Pierce County businesses receiving loan/grant funding; arts grantees under 1% for-Art; tourism-promotion-area contractors. | #1, #3 |
| Who sits | The director is appointed by and serves at the pleasure of the County Executive. Staff supports three advisory bodies (LTAC, TPAC, Arts Commission) and the Economic Development Corporation of Pierce County. | #3, #4 |
| Who governs | Indirectly: recommendations from LTAC, TPAC, and Arts Commission are forwarded to County Council for final adoption; department itself does not vote. | #3 |
| Who wins | Businesses that capture loan/grant dollars; arts organizations; tourism-marketing firms. | #1, #3 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Tom Pierson (`tom-pierson`) | acting_director | 6 |

**New edges discovered during research:**.
`pierce-county-econ-dev`, target=`pierce-county-executive`, relationship=reports_to, weight=5, note="https://www.governmentjobs.com/careers/piercecountywa/jobs/newprint/5271113".
`pierce-county-econ-dev`, target=`edb`, relationship=partner, weight=4, note="https://www.piercecountywa.gov/CivicSend/ViewMessage/message/106555".
`pierce-county-econ-dev`, target=`chamber`, relationship=partner, weight=4, note="https://www.piercecountywa.gov/CivicSend/ViewMessage/message/106555".
`pierce-county-econ-dev`, target=`economic-development-corp-pierce-county`, relationship=staffs, weight=3, note="https://www.piercecountywa.gov/8523/Economic-Development-Corporation-of-Pier".
`pierce-county-econ-dev`, target=`arts-commission-pierce-county`, relationship=staffs, weight=3, note="https://www.governmentjobs.com/careers/piercecountywa/jobs/newprint/5271113".

## 1. Who they are
| # | Claim | Source | URL | Type | Reliability |
|---|-------|--------|-----|------|-------------|
| 1 | "Pierce County Economic Development Department … supports a business environment that is diverse, equitable, and inclusive … advances entrepreneurship, job creation, workforce readiness, tourism and the arts." | Pierce County official site | https://www.piercecountywa.gov/103/Economic-Development | primary | 0.95 |
| 2 | "Pierce County Economic Development 950 Pacific Ave, Suite 720 Tacoma, WA 98402 … Betty Capestany, Director … (253) 798-6926" — staff directory. | Pierce County staff directory | https://www.piercecountywa.gov/Directory.aspx?did=15 | primary | 0.95 |
| 3 | "Director of Economic Development … $140,105.00 – $189,216.00 Annually … DEPARTMENT: County Executive … Tourism and Arts: Economic Development handles tourism funding, supports the Lodging Tax Advisory Committee and Tourism Promotion Area Commission, and oversees the County's arts programs, including the Arts Commission, grant funding, and the 1 Percent for the Arts program." | Pierce County GovernmentJobs posting 26-00251 | https://www.governmentjobs.com/careers/piercecountywa/jobs/newprint/5271113 | primary | 0.95 |
| 4 | "Economic Development Corporation of Pierce County … board roster includes Patricia Beard (City of Tacoma), Tyra Dieffenbach (Port of Tacoma), Becky Newton (City of Lakewood), Meredith Neal (City of Puyallup), Nathe Lawver (Pierce County Central Labor)" — confirms public-private structure. | Pierce County official site | https://www.piercecountywa.gov/8523/Economic-Development-Corporation-of-Pier | primary | 0.95 |

## 1. Who they are
- **Verdict:** The Pierce County Economic Development Department is a small executive-branch unit. It does not set tax rates. It does not hold electoral power. But it runs staff work behind county tourism, Arts Commission grants, 1% for-Art money, and business loans. The 2026 leadership change (Capestany → Pierson-as-acting) made it a bridge between the county executive, the Chamber, and the EDB.
- **Conflicts-of-interest flags:**
 - Tom Pierson's dual role is a clear COI. He is Chamber CEO and Acting Director of a county department that contracts with the Chamber. The County Executive's office flagged it when the dual role was set up.
 - Lodging-tax committee seats can be captured by the hotel industry. The 1% for-Art money can be steered toward development-friendly public art.
- **Analysis of alternatives :** A skeptical reading says the department is mostly a "marketing and ribbons-cutting" operation. Its loan fund is small compared with private capital. The opposing reading (favored) is that the *coordination* function is the real product. The department exists to staff and fund the convenings between the EDB, the Chamber, the City of Tacoma, and the Port.
- **Confidence:** Medium — director salary band, mission, address, programs, and staff roster confirmed by Pierce County primary sources; the Pierson acting-director appointment confirmed via LinkedIn and the 2026 GovernmentJobs posting; 2026 acting status is the current state.
 (submit)
