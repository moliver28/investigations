<!-- entity-profile:v1 organization -->
# Russell Investments — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/russell-invest.md`
**Entity ID:** `russell-invest` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 85/163 · **Composite power:** 0.025
**Graph description:** — 
**Known facts:** — (none recorded)
**Status:** ✅ researched — 2026-09-19 — tier3-chunk2 · **Last updated:** 2026-09-19
**Sources:** 3/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- Inclusion rule: **well-connected + reputational**. Russell Investments is on the map for three reasons: (a) it is the direct creation of the Russell family (Frank Russell, then George F. Russell Jr.), and the Russell Family Foundation is already a graph node (`russell-family`); (b) Jason Thompson, Russell's Americas Institutional director, also sits on the MultiCare Health board — a key cross-influence node (MultiCare is a tier-2 entity); (c) the firm was founded and long run out of Tacoma and still runs institutional money tied to Pierce County civic philanthropy.
- Adjacent but excluded: Frank Russell Company (the pre-1999 operating company, now absorbed); separate Russell Indexes licensing business (now part of London Stock Exchange Group per Russell 3000/2000 index sales — exact date UNVERIFIED here, see open questions).

## 1. Who they are
- Exact legal name: **Russell Investments Group, LLC** (current parent holding).
- Entity type: **Private investment-management firm** — Delaware LLC operating worldwide. Subsidiaries include Russell Investment Management Company (RIMCo, 909 A Street Tacoma WA — old HQ address), Russell Fund Services Company, Russell Financial Services Inc., and Russell Insurance Agency Inc.
- Founded: **1936** in Tacoma WA by **Frank Russell**. Reorganized under Northwestern Mutual Life, which bought Frank Russell Co. in 1999 in a $1.2B-scale deal. The firm rebranded as Russell Investment Group. It is now mostly owned by **TA Associates Management, L.P.**, with minority stakes held by **Reverence Capital Partners, L.P.** and certain employees plus Hamilton Lane Advisors LLC minority stakes.
- Leadership (current): **Zach Buchwald** — Chairman and CEO (joined February 2023 from BlackRock, where he ran the $2T Institutional Business). **Kate El-Hillow** — President and CIO (since 2022).
- HQ: **Russell Investments Center, Seattle WA** (current HQ; old Tacoma 909 A Street address kept by some subsidiaries).
- Assets: **~$418 billion** (August 2026) under management. **$2.6 trillion** under advisement across 32 countries. Russell is the 4th-largest adviser in the world. Employees: about 1,350 (2019).

## 3. Where their power comes from
- **Market and financial power**: Russell is a top-5 global investment-outsourcing firm. It created the Russell 2000 and Russell 3000 indexes (now under FTSE Russell / LSEG — UNVERIFIED transition date here). Russell controls how trillions of dollars are benchmarked and how hundreds of billions are actively managed. Major clients have included AT&T, Boeing, and Union Pacific Railroad.
- **Civic bridge power**: The Russell family (Jane and George Russell Jr.) founded The Russell Family Foundation in Gig Harbor WA in 1999 with part of the Northwestern Mutual sale proceeds. The foundation funded the Museum of Glass (opened 2002 in downtown Tacoma), environmental sustainability, and Pacific NW impact-aligned investments. George Russell was honored after his death by Tacoma Mayor Victoria Woodards.
- **Institutional bridge power**: **Jason Thompson** joined Russell in 1994. He serves as director of the firm's Americas Institutional business. He joined the MultiCare Board of Directors in January 2025 — creating a direct Russell to MultiCare pipeline. MultiCare CEO Bill Robertson's firm could have a $418B-AUM advisory relationship with Russell.
- Basis for scoring overlap: Russell Family Foundation (founded_by graph weight 5). Jason Thompson director link (graph weight 4) — the latter is the most concrete Pierce County tie.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|---|---------|---------------------|
| Who benefits | TA Associates (private-equity majority owner); Reverence Capital; Hamilton Lane; institutional clients (AT&T, Boeing, Union Pacific, etc.); Pacific NW nonprofits funded by Russell Family Foundation; MultiCare (via Jason Thompson board cross-membership). | #1, #2, #3 |
| Who sits | Zach Buchwald (Chairman/CEO); Kate El-Hillow (President/CIO); Jason Thompson (Director, Americas Institutional). Jason Thompson also sits on MultiCare board since January 2025. | #1, #2 |
| Who governs | The Securities and Exchange Commission (SEC) regulates registered investment advisers (RIMCo is registered). The Russell Investments Group LLC board is the fiduciary authority. TA Associates and Reverence Capital exercise private-equity control. CFTC and FINRA regulate subsidiaries where applicable. | #1, #2 |
| Who wins | The 1999 sale to Northwestern Mutual produced the endowment that created the Russell Family Foundation — a durable Pacific NW civic-philanthropy win. The Russell 2000/3000 indexes (now under LSEG/FTSE Russell) generate ongoing index-licensing fees. George Russell's legacy is a Tacoma-to-Seattle-to-global pipeline of investment-management reach. | INFERENCE from #1, #3 |

## 9. Who they are connected to
Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Jason Thompson (`jason-thompson`) | director | 4 |
| Russell Family Fdn (`russell-family`) | founded_by | 5 |

### New relationships to record.
`russell-invest`, target=`multicare`, relationship=`board_cross_membership`, weight=4, note="Jason Thompson joined MultiCare Board Jan 2025 per multicare.org/about/leadership/board-directors".
`russell-invest`, target=`museum-of-glass`, relationship=`funded_by_family`, weight=3, note="Russell Family Foundation funded Museum of Glass opening 2002 per Seattle Times obit".
`russell-invest`, target=`ta-associates`, relationship=`majority_owner`, weight=5, note="TA Associates Management LP holds majority stake".
`russell-invest`, target=`zach-buchwald`, relationship=`ceo`, weight=4, note="Chairman & CEO since Feb 2023".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Russell Investments Group LLC is a private American investment firm, founded 1936 in Tacoma WA by Frank Russell, now headquartered at Russell Investments Center, Seattle WA; led by Chairman & CEO Zach Buchwald (since Feb-2023, ex-BlackRock $2T Institutional Business) and President & CIO Kate El-Hillow (since 2022); ~$418B AUM as of Aug-2026 plus $2.6T under advisement; ownership: TA Associates majority, Reverence Capital + employees + Hamilton Lane minority stakes. | Wikipedia, "Russell Investments" | https://en.wikipedia.org/wiki/Russell_Investments | secondary (encyclopedic) | 0.85 |
| 2 | Jason Thompson joined Russell Investments in 1994 and serves as director of the firm's Americas Institutional business; he joined the MultiCare Board of Directors in January 2025 and was previously chair of the Board of Directors for Overlake Medical Center & Clinics. | MultiCare, "Board of Directors - Leadership" | https://www.multicare.org/about/leadership/board-directors | primary (institutional board roster) | 0.95 |
| 3 | George F. Russell Jr. (founder's son, longtime chairman) co-founded The Russell Family Foundation in 1999 with wife Jane using proceeds from sale to Northwestern Mutual; foundation based in Gig Harbor WA; family funded Museum of Glass (opened 2002 in downtown Tacoma); Russell died in 2023 at age 93, honored by Tacoma Mayor Victoria Woodards. | Seattle Times, "George F. Russell Jr., 93, turned family firm into investing giant, dies" (Megan Ulu-Lani Boyanton) | https://www.seattletimes.com/business/local-business/george-f-russell-jr-93-turned-family-firm-into-investing-giant-dies | primary (obituary, contemporary news) | 0.90 |

## 1. Who they are
- Verdict: Russell Investments is a tier-3 economic node. Its current direct Pierce County power is modest (operations are now Seattle-based), but its family-mediated reach is real. The Russell Family Foundation's Pacific NW grant-making (Gig Harbor-based, environmental focus, Museum of Glass legacy), plus Jason Thompson's January-2025 MultiCare board seat, make Russell a meaningful pipeline into the region's healthcare-power network. George Russell's 2023 death marked the end of the founder era. Ownership now rests with private-equity sponsors TA Associates and Reverence Capital, who are return-on-capital actors rather than civic figures.
- Conflicts-of-interest flags: (a) Jason Thompson's two roles — Russell's Americas Institutional director and MultiCare board director — open a channel for investment-management business between the two firms. MultiCare's investment policy and Russell's institutional business could touch. (b) The 1999 sale to Northwestern Mutual raises ongoing questions about the family's retained influence despite the Russell Family Foundation's formal independence.
- Analysis of alternatives (investigative control document (ICD)-203 opposing view): A skeptic would call Russell Investments a Seattle-based PE-owned investment firm with a Tacoma-origin story but no current Pierce County operations. The civic reach runs through the Russell Family Foundation (a separate 501(c)(3)) rather than Russell Investments itself. The graph weight here likely overstates Russell Investments' direct Pierce County reach and understates the foundation's separate role.
- **Confidence:** **Medium** — Founding facts, ownership, and Jason Thompson's MultiCare board seat are well-documented. The exact current Russell-MultiCare business relationship and the precise transfer of the Russell Indexes business to FTSE/LSEG are UNVERIFIED in this pass.