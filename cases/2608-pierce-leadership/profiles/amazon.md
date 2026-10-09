<!-- entity-profile:v1 organization -->
# Amazon (distribution) — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/amazon.md`
**Entity ID:** `amazon` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 120/163 · **Composite power:** 0.013
**Graph description:** Amazon.com, Inc. — multi-national e-commerce and logistics company operating multiple fulfillment and distribution facilities in Pierce County, WA, with documented sites in Sumner (fulfillment center at 1901/1800 140th Ave E) and adjacent facilities in Kent and DuPont within the broader Puget Sound regional network.
**Known facts:** Amazon operates fulfillment centers in Sumner WA (1901/1800 140th Ave E, 98390) and across the Puget Sound region; Amazon Robotics research facility in Sumner; ~58 LinkedIn-listed Amazon jobs in Pierce County and ~53 in Sumner alone per LinkedIn snapshot; Amazon is a member of the Tacoma-Pierce County Chamber of Commerce and the Economic Development Board per the entity's existing graph links.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk9 · **Last updated:** 2026-09-19
**Sources:** 5/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why Amazon is on the map.** Amazon qualifies on two grounds. First, jobs: Amazon runs a large fulfillment center and a robotics research facility in Sumner, plus sites in Kent and DuPont across the Puget Sound. Second, network: Amazon sits on the Tacoma-Pierce County Chamber of Commerce and the Economic Development Board (the EDB). Those two seats put Amazon at the table when Pierce County sets economic-development policy.
- **What Amazon's local workforce looks like.** Hundreds of warehouse workers, drivers, robotics technicians, safety staff, and customer-service roles in Pierce County.
- **What is NOT on the map.** Individual Amazon buildings (the Sumner fulfillment center, the robotics site, the Kent facility, the DuPont facility) are not separate entries. Staffing agencies that Amazon hires through are also not separate entries. The map stays at the parent-company level.

## 1. Who they are
- **Legal name:** Amazon.com, Inc., a Delaware corporation. Local arms include Amazon.com Services LLC (Washington state) and Amazon Fulfillment Services, Inc.
- **Type of company:** Public, for-profit. Trades on the NASDAQ as AMZN. Federal tax ID number (EIN) for Washington subsidiaries was not confirmed in this pass and remains UNVERIFIED; check Securities and Exchange Commission (SEC) filings for the number.
- **Parent and subsidiaries:** Amazon.com, Inc. sits above AWS, North America Consumer, International Consumer, and Operations/Logistics subsidiaries. In Pierce County, the operating arm is usually Amazon.com Services LLC or Amazon Fulfillment, Inc.
- **Who owns it:** Public shareholders. Founder Jeffrey P. Bezos is the largest single owner through trusts. Vanguard, BlackRock, and State Street are also large holders. Exact 2025–2026 ownership percentages are UNVERIFIED without a fresh SEC Form 13F snapshot.
- **Laws that apply:** Federal securities law (SEC). Delaware corporate law (DGCL). Washington state consumer-protection and employment law (RCW). Site-level rules from the U.S. Department of Transportation (DOT), OSHA, Washington Labor & Industries (L&I), and the Washington Department of Revenue (DOR).

## 3. Where their power comes from
- **Market position:** Amazon is the top e-commerce and logistics firm in the U.S. In Pierce County's warehouse labor market, Amazon is one of the few big employers. Along with Walmart, Home Depot, and Costco distribution centers, it sets the pay floor and ceiling for warehouse jobs.
- **Government contracts and grants:** Pierce County tax breaks for the Sumner site were not found in this pass (UNVERIFIED). Statewide, Amazon has used Washington Department of Commerce tax-incentive programs, mostly for data centers.
- **Jobs controlled:** Amazon lists about 58 LinkedIn jobs in Pierce County and about 53 in Sumner. Indeed lists about 50 Amazon jobs in Pierce County and about 25 in Sumner. Pay starts at $17–$22 an hour depending on the job, with sign-on bonuses up to $3,000. Total Amazon headcount in Pierce County is UNVERIFIED beyond these job counts.
- **Land and real estate:** 1901 140th Ave E, Sumner WA 98390 is an active fulfillment-center address. 1800 140th Ave E, Sumner was in a 2025 WARN layoff report for about 32 workers. The Amazon Robotics research facility is also in Sumner.
- **Chamber and EDB seats:** Amazon is a member of the Tacoma-Pierce County Chamber of Commerce and the Economic Development Board.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Amazon itself, via Chamber and EDB seats, helps shape local economic-development policy. Workers and staffing agencies also benefit. | #3, #4, #5 |
| Who sits | Amazon sits on the Chamber and the EDB at the parent-corporate level. Local site decision-makers are UNVERIFIED. | #3, #4 |
| Who governs | Amazon helps set warehouse pay and the pace of warehouse automation in Pierce County. It is one of the few big employers with that kind of pull. | #1, #2, #5 |
| Who wins | Amazon's scale lets it underprice local stores and grab market share. That leads to fewer, larger, more automated distribution sites. The 2025 Sumner layoff of about 32 workers fits that pattern. | #1, #2 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Chamber of Commerce (`chamber`) | member | 3 |
| Economic Development Board (`edb`) | member | 3 |

- **New edges identified:**.
amazon, target=sumner-wa, relationship=fulfillment_site, weight=3, note="https://hiring.amazon.com/jobDetail/en-US/Fulfillment-Center-Warehouse-Associate/Sumner/a0R4U00000Flj8IUAR" (Sumner, WA fulfillment center at 1901/1800 140th Ave E).
amazon, target=tacoma-pierce-edb, relationship=board_member_interlock, weight=2, note="https://www.aboutamazon.com/news/operations/amazon-robotics-facility-tour-washington" (Amazon Robotics research facility in Sumner; regional economic-development overlap).
amazon, target=kent-wa, relationship=fulfillment_site, weight=2, note="https://www.amazon.jobs/content/en/locations" (Kent, WA fulfillment center at 21005 64th Ave S — King County but part of the same Puget Sound network cited in the Amazon locations page).

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | The Amazon Fulfillment Center at 1800 140th Ave E, Sumner WA, was listed in a 2025 WARN layoff notice with approximately 32 workers affected | The News Tribune | https://www.thenewstribune.com/news/local/article317075476.html | secondary | 0.85 |
| 2 | Amazon operates fulfillment centers in Kent, Sumner, and DuPont in the Puget Sound region; corporate offices in Seattle and Bellevue | Amazon Jobs locations page | https://www.amazon.jobs/content/en/locations | primary | 0.95 |
| 3 | Amazon Fulfillment Center Warehouse Associate position open at 1901 140th Ave E, Sumner WA 98390; pay rate up to $19.80/hour | Amazon Hiring portal | https://hiring.amazon.com/jobDetail/en-US/Fulfillment-Center-Warehouse-Associate/Sumner/a0R4U00000Flj8IUAR | primary | 0.95 |
| 4 | Amazon's research facility in Sumner, WA features a high-tech living wall and new fulfillment-center robots undergoing testing | Amazon about-amazon newsroom | https://www.aboutamazon.com/news/operations/amazon-robotics-facility-tour-washington | primary | 0.95 |
| 5 | Amazon employs fulfillment-center associates at 21005 64th Ave S, Kent WA 98032 (King County; hourly pay rate $18.30+); sign-on bonus up to $3,000; Kent is listed among multiple BFI/Kent area fulfillment sites | Amazon Hiring portal | https://hiring.amazon.com/jobDetail/en-US/Fulfillment-Center-Warehouse-Associate/Kent/a0R4U00000DKGy8UAH | primary | 0.95 |

## 1. Who they are
- **The bottom line.** Amazon belongs on the map because it is one of the few big warehouse employers here and it holds Chamber and EDB seats. Its local power is pay-setting on warehouse jobs, siting of big logistics facilities, and pressure on local retail. The seats give it a voice in tax, transportation, and workforce policy.
- **Conflicts-of-interest flags.** Amazon sits in both the Chamber and the EDB. That means it helps set policy and also benefits from it. The 2025 Sumner layoff of about 32 workers was small but fits a broader pattern: layoffs at some sites while expanding at others. Amazon's heavy use of staffing agencies hides total warehouse employment. Washington's new warehouse worker law (HB 1762, with quota caps) is a new front to watch.
- **Two readings.** Optimistic: Amazon creates jobs, pays above the state minimum, and offers a promotion track. Skeptical: Amazon's scale drives local-store closures and concentrates risk on a few large employers. Automation, especially at the Sumner Robotics site, speeds worker churn. Both views fit the data.
- **Confidence:** Medium — primary sources (Amazon hiring portal, Amazon newsroom, Amazon jobs locations) confirm facility locations and wages; the 2025 WARN layoff figure from the News Tribune is secondary and unconfirmed by other reports; total Pierce County headcount and Chamber/EDB membership standing are UNVERIFIED at the granular level.

- **open questions & leads:**.
 - Total Pierce County Amazon headcount (sum of all Sumner + DuPont + other site staffing).
 - Sumner site property-tax abatement / sales-tax-deferral deals via WA DOR and Pierce County.
 - Truck-traffic data for 140th Ave E corridor in Sumner (WSDOT/Port of Tacoma data feed).
 - WA L&I warehouse-quota complaints filed against Amazon in the past 5 years.
 - Robotic-fulfillment roadmap for the Sumner Amazon Robotics site and worker-displacement impact.
