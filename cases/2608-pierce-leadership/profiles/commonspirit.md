<!-- entity-profile:v1 organization -->
# CommonSpirit Health — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/commonspirit.md`
**Entity ID:** `commonspirit` · **Type:** organization · **Domain:** institutional
**Tier:** tier3 · **Rank:** 107/163 · **Composite power:** 0.016
**Graph description:** Chicago-based nonprofit, Catholic-affiliated national health system formed Feb 2019 by merger of Catholic Health Initiatives (CHI) and Dignity Health. Parent company of Virginia Mason Franciscan Health (VMFH) — the principal CommonSpirit subsidiary operating in Pierce County (St. Joseph Medical Center, Tacoma; St. Clare Hospital, Lakewood; St. Anthony Hospital, Gig Harbor; St. Elizabeth Hospital, Enumclaw; St. Francis Hospital, Federal Way; plus CHI Franciscan medical clinics).
**Known facts:** Created February 2019 by CHI/Dignity merger; ~150,000 employees, ~25,000 physicians/advanced-practice clinicians; operates 137 hospitals across 21 states; FY2019 revenue ~$29B; CHI Franciscan represented ~$2.45B revenue pre-2021 merger; Virginia Mason combined with CHI Franciscan to form VMFH effective January 5, 2021.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk7
**Sources:** 5/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Inclusion rule:** From holding office + decision-making. CommonSpirit Health is included as the parent company that controls Virginia Mason Franciscan Health (VMFH). VMFH runs many hospitals and clinics in Pierce County. These include St. Joseph in Tacoma, St. Clare in Lakewood, and St. Anthony in Gig Harbor.
- CommonSpirit is a 501(c)(3) nonprofit health system. It is Catholic-affiliated. As a large health system, it shapes hospital pricing, charity-care policy, capital decisions, and labor relations across the Puget Sound region. The graph records it as the parent of VMFH (weight 6) and as affiliated with the Catholic Archdiocese (weight 2).
- **Excluded but related:** MultiCare Health System is the main Pierce County rival. It is profiled separately as `multicare`. PeaceHealth, Swedish Health (Providence), and UW Medicine are nearby regional systems. They have a small Pierce County presence. The Catholic Archdiocese of Seattle is profiled separately. It connects to CommonSpirit through VMFH's Catholic affiliation and the Ethical and Religious Directives for Catholic Health Care Services (ERDs).

## 1. Who they are
- **Exact legal name:** CommonSpirit Health.
- **Entity type:** 501(c)(3) nonprofit, Catholic-affiliated health system. National office in Chicago, IL.
- **How it was formed:** Created in February 2019. It was a merger of Catholic Health Initiatives (CHI, headquartered in Englewood, CO) and Dignity Health (headquartered in San Francisco, CA). Both were large Catholic-affiliated systems before the merger.
- **Scale:** About 150,000 employees. About 25,000 physicians and advanced practice clinicians. It runs 137 hospitals and more than 1,000 care sites across 21 states. Fiscal Year 2019 revenue was about $29 billion.
- **Pierce County subsidiary:** Virginia Mason Franciscan Health (VMFH). VMFH was formed January 5, 2021. It merged CHI Franciscan (Tacoma) with Virginia Mason (Seattle). Ketul J. Patel was the CEO of VMFH. He was also president of the Pacific Northwest Division of CommonSpirit Health.
- **Governing law:** Washington State nonprofit corporation statutes (state law (RCW) 24.03A). Catholic-affiliated governance through board oversight and the Ethical and Religious Directives (ERDs). The ERDs are issued by the U.S. Conference of Catholic Bishops.

## 3. Where their power comes from
- **Market position in Pierce County:** Through VMFH and CHI Franciscan, CommonSpirit runs several hospitals in or near Pierce County. These include St. Joseph Medical Center (Tacoma), St. Clare Hospital (Lakewood), St. Anthony Hospital (Gig Harbor), St. Elizabeth Hospital (Enumclaw), and St. Francis Hospital (Federal Way). The system also runs Franciscan Medical Group clinics and CHI Franciscan urgent-care sites. Tacoma-Pierce County Health Department and Chamber listings show CHI Franciscan and VMFH sites as major regional providers.
- **Tax status:** 501(c)(3) nonprofit, Catholic-affiliated. Tax-exempt status gives an indirect subsidy. CommonSpirit pays no federal income tax. It pays no state B&O tax on most activities. It also has property-tax exemptions on many sites. This is a structural edge over for-profit hospital operators.
- **Decision-making authority:** Capital projects, mergers, EHR systems, staffing, charity care, and reproductive-health rules are all set at the CommonSpirit corporate level. They are not set at the VMFH local-board level. Ketul Patel was VMFH and Pacific Northwest Division President until 2024. He led Pacific Northwest ops for CommonSpirit.
- **Domain overlap:**
 - **inst ↔ gov:** Hospital licensing, certificate-of-need (CON) for capital projects, Medicare and Medicaid — heavy work with the WA Department of Health and CMS.
 - **inst ↔ econ:** One of the largest private employers in the region. Big purchasing power. Big real-estate holdings.
 - **inst ↔ social:** Charity-care and community-benefit duties tied to tax-exempt status. Reproductive health and end-of-life rules under the ERDs.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Patients with insurance coverage accepted by CHI Franciscan/VMFH (commercial, Medicare, Medicaid — though Medicaid acceptance varies by site and physician); Catholic patients seeking care at a faith-aligned provider; the broader community from charity-care investments required to maintain tax-exempt status. | Sources 1, 2, 3 |
| Who sits | CommonSpirit Health national board (governance of the parent system); VMFH regional board (oversight of Pacific Northwest operations). Ketul J. Patel served as VMFH CEO and Pacific Northwest Division President of CommonSpirit. The Catholic Health Ministries (CHI side) and Dignity Health Community Ministerial Alliance (Dignity side) constitute the canonical sponsors. | Sources 3, 4 |
| Who governs | Decisions on M&A, capital allocation, charity-care policy, and ERD-restricted services are made at the CommonSpirit national level. The Catholic Health Ministries (public juridic persons) maintain canonical authority over Catholic-identity issues. | Sources 3, 4 |
| Who wins | CommonSpent shareholders (there are none — it is nonprofit), executives, and large creditors/investors (via outstanding bonds) win from system expansion. Tacoma and Lakewood communities "win" from having an acute-care hospital operator committed to those markets, though they lose the ability to access ERD-restricted services (e.g., elective abortion, physician-assisted death) at CommonSpirit facilities. | Sources 1, 2 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| VMFH (`vmfh`) | owned_by | 6 |
| Catholic Archdiocese (`catholic-archdiocese`) | religious_affiliation | 2 |

- 
commonspirit, target=catholic-archdiocese, relationship=canonical_authority, weight=3, note="https://www.commonspirit.org/who-we-are/our-heritage".
commonspirit, target=multicare, relationship=market_competitor, weight=2, note="https://www.piercecountywa.gov/6834/Health-Services".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Pierce County hospital list including St. Joseph (CHI Franciscan), St. Clare (CHI Franciscan), St. Anthony (CHI Franciscan), St. Elizabeth, St. Francis, plus MultiCare Tacoma General, Allenmore, Good Samaritan | Pierce County WA official website — Health Services | https://www.piercecountywa.gov/6834/Health-Services | primary | 0.95 |
| 2 | VMFH hospital listings — St. Joseph Tacoma, St. Clare Lakewood, St. Anthony Gig Harbor, St. Elizabeth Enumclaw, St. Francis Federal Way | Tacoma-Pierce County Chamber — Hospitals Category | https://business.tacomachamber.org/list/category/hospitals-19 | primary | 0.85 |
| 3 | CommonSpirit Health is a nonprofit, Catholic health system created Feb 2019 by CHI/Dignity merger; ~150,000 employees; 25,000 physicians/APCs; 137 hospitals; 21 states; FY2019 revenue ~$29B; CHI Franciscan ~$2.45B revenue (10 hospitals) | CommonSpirit/CHI Franciscan merger announcement (PR Newswire) | https://www.prnewswire.com/news-releases/chi-franciscan-and-virginia-mason-finalize-agreement-to-form-virginia-mason-franciscan-health-301201379.html | primary | 0.95 |
| 4 | CHI Franciscan (Tacoma) and Virginia Mason (Seattle) merged January 5, 2021 into VMFH, a subsidiary of CommonSpirit Health; Ketul J. Patel named CEO of VMFH and Pacific Northwest Division President of CommonSpirit | Fierce Healthcare | https://www.fiercehealthcare.com/hospitals/chi-franciscan-virginia-mason-finalize-acquisition-deal-and-roll-out-new-name | secondary | 0.85 |
| 5 | VMFH operates as the joint operating company of CHI Franciscan and Virginia Mason; CommonSpirit Health is the parent; ~300 care sites in Pacific Northwest; Ketul Patel comments on continued patient experience and expansion plans | Tacoma News Tribune | https://www.thenewstribune.com/news/business/article248261560.html | secondary | 0.85 |

## 1. Who they are
- **Verdict:** CommonSpirit Health controls a large share of acute-care hospital capacity in Pierce County through its VMFH subsidiary. St. Joseph in Tacoma is one of two adult acute-care hospitals in central Tacoma. St. Clare in Lakewood is the only hospital in that city. St. Anthony anchors Gig Harbor. The corporate parent sets the strategy. VMFH and CHI Franciscan leaders carry it out locally. The system is bound by Catholic ERDs and by Washington's rules. Even so, it is one of the two top hospital operators in the county, alongside MultiCare.
- **Conflicts-of-interest flags:** As a Catholic-affiliated system, VMFH and CommonSpirit are bound by the Ethical and Religious Directives. The ERDs ban direct abortion services (with narrow exceptions) and physician-assisted death. This limits the reproductive-health options of patients in Pierce County — especially in Lakewood and Gig Harbor, where CommonSpirit hospitals are the only option. The 501(c)(3) tax-exempt status gives a structural subsidy. That subsidy is not linked to a fixed community-benefit standard. ERD enforcement is set at the sponsor and corporate level, not the local level. It is not clear if VMFH local boards have any real opt-out power (UNVERIFIED).
- **Analysis of alternatives :** An opposing reading: CommonSpirit is one national system among many. In Pierce County, MultiCare is the bigger rival. MultiCare runs Tacoma General, Allenmore, Good Samaritan in Puyallup, and Mary Bridge Children's Hospital. CommonSpirit/VMFH has lost market share in some lines (e.g., the Yakima hospital broke off from Virginia Mason at the start of 2021, before the merger). Catholic governance is a feature, not a bug, for faith-aligned patients. ERD restrictions push some procedures out to secular providers like MultiCare. That keeps pluralistic access in the broader market.
- **Confidence:** Medium-High — formation history, scale figures, and VMFH merger are corroborated by primary press release (CommonSpirit/CHI Franciscan) and multiple secondary outlets (Fierce Healthcare, Tacoma News Tribune). Specific 2024–2026 Pierce County market share figures, ERD-enforcement incidents at VMFH, and CommonSpirit national bond debt are not extracted in this pass — UNVERIFIED.
 (submit)
