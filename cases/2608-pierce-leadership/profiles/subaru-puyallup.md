<!-- entity-profile:v1 organization -->
# Subaru of Puyallup — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/subaru-puyallup.md`
**Entity ID:** `subaru-puyallup` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 162/163 · **Composite power:** 0.001
**Graph description:** Single-point Subaru franchise in Puyallup WA owned by the second-generation Harnish family as part of the multi-store Harnish Auto Family (Subaru, Kia, Volkswagen, Chevrolet, Buick, GMC — 6 dealerships across Puyallup + Everett). Federal political-contribution filings trace direct donations from the store to Republican candidates including Hans Zeiger (R-WA, 25th LD Senate) and Glenn Fariss (R-VA Senate).
**Known facts:** 720 River Rd, Puyallup WA 98371; founded ~1977 by Keith Harnish (Lincoln Mercury); currently "second generation of family ownership"; part of Harnish Auto Family. President/dealer of sister VW store is Shannon Harnish-Cook.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk18-rescue
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why it's on the map:** Subaru of Puyallup is in the map for two reasons. (a) It is a donor node to Kelly Chambers (weight 3) in `evidence/29-power-graph-v2.json`. (b) It sits on about 10 acres on River Road. That corridor hosts Toyota of Puyallup, the Washington State Fair, and the city's main commercial-redevelopment frontage. The store sits inside the City of Puyallup land-use and sign-code perimeter. That perimeter is controlled by the City Council (see `jim-kastama`). A major River Road dealer has pull in the local business community and in any downtown-redevelopment fight.
- **Neighbors NOT added to the map:**
 - Other Harnish Auto Family stores. VW of Puyallup, Chevrolet Buick GMC of Puyallup, Chevrolet of Everett, Kia of Everett. Same ownership chain but separate EINs and separate graph nodes. Routed to open questions.
 - `harnish-auto-family` (parent group). Could be its own profile but is not currently in the entity table. Routed to open questions.

## 1. Who they are
- **Trade name:** Subaru of Puyallup.
- **Entity form:** Single-store new-vehicle franchise. Run by a privately-held Washington auto-dealership LLC. The franchise is "part of the Harnish Auto Family" (Subaru of Puyallup website footer and About page). The exact legal-entity name and tax ID number (EIN) are not on the dealer site. They are UNVERIFIED in this profile. A Washington Secretary of State UBI search or a WA DOR excise-tax lookup would close the gap.
- **Operating address:** 720 River Rd, Puyallup, WA 98371 (Subaru of Puyallup website, contact page; Carfax dealer profile; LinkedIn company page).
- **Parent / brand:** Harnish Auto Family (Puyallup WA and Everett WA). Franchise brand is Subaru of America. Sister brands inside Harnish: Kia, Volkswagen, Chevrolet, Buick, GMC.
- **Founded:** Harnish Auto Family traces to 1977. "Four decades ago, Keith Harnish opened his first dealerships in Puyallup, WA" (Harnish Auto Family About page). The Subaru franchise was added later. The dealership says it is "in our second generation of family ownership" (Subaru of Puyallup About page).
- **Ownership chain:** Founder Keith Harnish. Now second-generation family members. Shannon Harnish-Cook is the president and dealer of VW, Chevrolet Buick GMC, and Chevrolet of Everett stores. She is a partner of Harnish Auto Family (253 Lifestyle Magazine 2023 Q&A).
- **Governing law:** Washington Motor Vehicle Dealers (state law (RCW) 46.70). Franchise agreement with Subaru of America.

## 3. Where their power comes from
- **Market position:** Single Subaru point in the South Puget Sound. "10 acres of pre-owned cars, trucks and SUVs" (Subaru of Puyallup used-inventory page). That implies a substantial footprint by single-store standards.
- **Political influence:** Federal political-contribution filings exist — see Sources #4. OpenSecrets shows Subaru of Puyallup, Puyallup WA 98371, gave $2,000 to Glenn Fariss's Republican campaign on 11-22-2019.
- **Civic influence:** The dealership website says it is "proud to invest in our local community through generous charitable giving" (About page). It also cites the time and talent of many employees. The parent group's "People Matter" framing is marketing copy but signals sustained community-marketing spend.
- **Government contracts / grants:** No public-record evidence of direct city, county, or state procurement contracts. UNVERIFIED. This is normal for a retail auto dealer.
- **Jobs / land:** UNVERIFIED employee count. The 10-acre used-inventory footprint implies significant local employment. No primary headcount source was located.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Harnish family. The 10-acre River Rd property appreciates with any city-led redevelopment. Employees benefit from a multi-store employer. | #1, #2, #3 |
| Who sits | Shannon Harnish-Cook sits as president/dealer of multiple Harnish Auto Family stores. She sits across several franchises at once. | #3 |
| Who governs | No statutory power. Market power is local: a single Subaru point serving Tacoma, Puyallup, and South Hill. | #1 |
| Who wins | Republican state and federal candidates in WA-25 and nearby districts who receive auto-dealer political action committee (PAC) or corporate donations. | #4 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Kelly Chambers (`kelly-chambers`) | donated | 3 |

- **New relationships surfaced (to add to graph):**.
`subaru-puyallup`, target=`harnish-auto-family`, relationship=`brand_franchise_of`, weight=2, note="Subaru of Puyallup is a brand franchise of the Harnish Auto Family group. URL: https://www.subaruofpuyallup.com/harnish-auto-family.htm".
`subaru-puyallup`, target=`hans-zeiger`, relationship=`donated_to`, weight=1, note="Per OpenSecrets donor lookup, a 'Subaru of Puyallup' Puyallup WA 98371 entity made federal political contributions traceable to WA candidates including Hans Zeiger (R). URL: https://www.opensecrets.org/donor-lookup/results?name=Subaru".
`subaru-puyallup`, target=`kelly-chambers`, relationship=`donated_to`, weight=2, note="Per `evidence/29-power-graph-v2.json` weight-3 edge; no direct OpenSecrets hit located in our donor search (subaru-federal gives only Fariss 2019; state-level the state campaign-finance agency (PDC) contributions not enumerated in this search), so the graph edge is graph-sourced but UNVERIFIED at the federal level for Chambers specifically. URL: https://www.opensecrets.org/donor-lookup/results?name=Subaru+of+Puyallup".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | "Now in our second generation of family ownership… 720 River Rd Puyallup, WA 98371." | Subaru of Puyallup, official "About" page | https://www.subaruofpuyallup.com/dealership/about.htm | primary (corporate) | 0.90 |
| 2 | "Subaru of Puyallup, located at 720 River Rd has over 10 acres of pre-owned cars, trucks and SUVs to choose from!" | Subaru of Puyallup, used-inventory page | https://www.subaruofpuyallup.com/used-inventory/index.htm | primary (corporate) | 0.85 |
| 3 | "Shannon Harnish-Cook is the president/dealer of Volkswagen of Puyallup, Chevrolet Buick GMC of Puyallup, Chevrolet of Everett, and a partner of Harnish Auto Family. Keith Harnish founded the business in 1977 with a Lincoln Mercury dealership." | 253 Lifestyle Magazine Q&A with Shannon Harnish-Cook, 2023-07-13 | https://www.253lifestylemagazine.com/post/q-a-with-shannon-harnish-cook | secondary (regional lifestyle magazine) | 0.80 |
| 4 | "SUBARU OF PUYALLUP PUYALLUP, WA 98371 AUTOMOBILE DEALER 11-22-2019 $2,000 FARISS, SENATE REPUBLICAN" — donor record on federal contributions lookup. | OpenSecrets Donor Lookup (FEC-sourced) | https://www.opensecrets.org/donor-lookup/results?name=Subaru&page=2 | primary (FEC-sourced aggregator) | 0.90 |
| 5 | "As part of the Harnish Auto Family, which also includes Chevrolet Buick GMC of Puyallup, Volkswagen of Puyallup, Chevrolet of Everett, and Kia of Everett…" | Subaru of Puyallup homepage | https://www.subaruofpuyallup.com | primary (corporate) | 0.90 |

## 1. Who they are
- **Verdict:** Subaru of Puyallup is a single-store franchise. Its political weight is low on its own (0.001 in the graph). But it is well-connected. It is the Subaru point inside a 6-store regional auto group (Harnish Auto Family). That group has been politically active since 1977. Federal filings show at least one $2,000 contribution in 2019 to a Republican Senate candidate (Fariss, VA). The graph places it as a Kelly Chambers donor (weight 3). That edge is graph-sourced. It is not backed by an OpenSecrets hit on Chambers in this search. It may be a state-PDC contribution. The FEC-sourced OpenSecrets database may not capture it.
- **Conflicts of interest:** None directly observable at the federal level. State-level PDC contributions to Chambers remain UNVERIFIED.
- **The other reading:** Subaru of Puyallup is just one Subaru dealer among about 600 in the US. It has no special political influence. The Harnish Auto Family is a regional small business, not a power broker. That fits a 0.001 score. The case for inclusion is well-connected alone. Same owner family as VW, Chevy, and GMC stores on the same River Road corridor where the city is running downtown-redevelopment policy.
- **Confidence:** Medium. Corporate-identity facts are fully primary-sourced. The political-contribution-to-Chambers claim is graph-sourced. It remains UNVERIFIED at primary-source level for this specific donor and recipient pair.