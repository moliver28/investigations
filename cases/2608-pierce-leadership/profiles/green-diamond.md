<!-- entity-profile:v1 organization -->
# Green Diamond — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/green-diamond.md`
**Entity ID:** `green-diamond` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 157/163 · **Composite power:** 0.004
**Graph description:** Timber (formerly Simpson)
**Known facts:** (from graph) — 5th-largest private US landowner; 1.37M acres; Douglas Reed leads
**Status:** ✅ researched — 2026-09-19 — tier3-chunk17
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why it is on the map:** Green Diamond Resource Company is included because of the office it holds and its network. It is the sixth-generation, family-owned successor to Simpson Logging Company. It is one of the largest private timberland owners in the U.S. Its land in Pierce and Thurston Counties (corporate HQ in Seattle, WA office in Shelton) puts it inside the Pierce County economic map. The graph shows a direct edge from Green Diamond to Dale Sowell (former CFO), which gives it network weight. The company's $58.6M in net assets and about 300+ workers make it a real economic player.
- **Adjacent but not on the map:** Weyerhaeuser (the largest private timberland owner — profiled separately, near Pierce County). Port Blakely Tree Farms (also a Pacific NW family timber company). Sierra Pacific Industries (based in California). All are nearby economic-power nodes but separate entities.

## 1. Who they are
- **Legal name:** Green Diamond Resource Company (renamed from Simpson Resource Company in 2004).
- **Entity type:** Privately held, family-owned forest products company. Sixth generation of Simpson/Reed family ownership.
- **Tax ID (EIN) and corporate registration:** Privately held, not publicly traded. SEC EDGAR registrations do not apply. The company is incorporated in Washington (exact state of incorporation not confirmed — filings were not pulled; main office is in Washington).
- **Headquarters:** 1301 Fifth Avenue, Suite 2700, Seattle, WA 98101-2613; phone (206) 224-5800 (per the official company contact page).
- **Washington operations office:** 215 North Third, Shelton, WA 98584 (Mason County, next to Pierce County).
- **Subsidiaries:** Green Diamond Management Company (runs timberlands in AL, FL, GA, MS, SC, WA); Green Diamond Washington; Green Diamond California (Korbel, CA); Green Diamond Montana (Kalispell); Green Diamond Oregon (Klamath Falls).
- **Governing law:** Washington State corporate law. Must also meet HCP (Habitat Conservation Plan) rules under the federal Endangered Species Act and Washington Department of Natural Resources rules.

## 3. Where their power comes from
- **Domain = economic.** Power basis: market share in Pacific NW timber, federal and state HCP permits that effectively license its operations, and family ownership across generations. That long ownership keeps the company out of the pressure of quarterly earnings reports.
- **Land and resource position:**
 - Owns or runs about 2.2 million acres (per a Mason EDC profile using Green Diamond's own number). That puts it among the top five U.S. private timberland owners. The PCL graph lists "1.37M acres," which may use a different count (Washington and Oregon only, or leaving out some HCP-managed acres).
 - Pacific NW Washington land traces back to Sol Simpson's 1890 founding. The company still owns 400,000+ acres of the original 1900 purchase (per case-graph context).
 - Federal ESA Section 10 permits: a 1992 HCP for the Northern Spotted Owl (the first private-timberland HCP, in Humboldt and Del Norte Counties, CA). A 2000 multi-species HCP covering 51 fish and wildlife species in WA. A 2007 HCP for six aquatic species in CA, including coho salmon.
- **Revenue and workers:**
 - Estimated revenue ranges from $35M (Growjo) to $76.7M or $100M–$500M (RocketReach, SignalHire). The wide range reflects different methods (private-company self-reporting vs. Growjo's algorithm). No single audited figure is confirmed. Private companies do not file public financials.
 - Employees: the range is 200–500 across self-reported sources (LinkedIn 201–500, SignalHire 200–500, Growjo 301). RocketReach counts about 144. LinkedIn puts the company at 253 associated members.
- **Carbon and sustainability revenue:** 628,000+ acres enrolled in carbon sequestration projects (per Mason EDC). That is a new revenue line in voluntary carbon markets.
- **Key facts:**
 - **Revenue and ownership structure:** Privately held, Simpson/Reed family (sixth generation). CEO and President is Douglas Reed (great-great-grandson of founder Sol Simpson). CFO was Dale Sowell (now retired — per MultiCare board bio: "retired in 2020 from his role as vice president and chief financial officer at Green Diamond Resource Company").
 - **Market position:** Top-5 private timberland owner in the U.S. Top-3 in the Pacific NW.
 - **Government contracts and grants:** None directly documented (not confirmed). HCP permits are operating permits, not subsidies.
 - **Jobs controlled:** About 300 workers in the region. Not a dominant employer in Pierce County itself.

## 3. Where their power comes from
| Question | Answer | Source |
|----------|--------|--------|
| Who benefits | The Simpson/Reed family (sixth-generation owners). About 300 workers. Pacific NW contractors and mill operators. Voluntary carbon-market buyers of Green Diamond offsets. | 1, 2 |
| Who sits | Douglas Reed — President (since 2014). Dale Sowell — VP and CFO (retired 2020). Colin Moseley — Chairman (since 1996, per WFPA anniversary page). The Reed family is also on The Nature Conservancy Washington Board of Trustees. | 1, 2, 4 |
| Who governs | Indirect influence through HCP permits, the Washington Forest Practices Board, and trade groups (member of the Washington Forest Protection Association, WFPA). Dale Sowell sits on the MultiCare Health System Board (Director since 2001; Chair of the Finance & Audit Committee). | 3, 4, 5 |
| Who wins | Family owners (no shareholder pressure). Long-tenured managers. Conservation NGOs partnered through TNC trusteeship. Downstream lumber customers. | 1, 4 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Dale Sowell (`dale-sowell`) | former_cfo | 4 |

**New edges to add:**.
`green-diamond`, target=`douglas-reed`, relationship=`president`, weight=5, note="Douglas Reed is President since 2014; Reed family/TNC trustee https://www.nature.org/en-us/about-us/where-we-work/united-states/washington/stories-in-washington/douglas-reed".
`green-diamond`, target=`multicare`, relationship=`board_interlock_via_sowell`, weight=3, note="Dale Sowell serves on MultiCare Board since 2001, retired from Green Diamond 2020; multicare.org/about/leadership/board-directors".
`green-diamond`, target=`wfpa`, relationship=`member`, weight=2, note="Member of Washington Forest Protection Association; anniversary.wfpa.org/founders".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Green Diamond Resource Company history: founded 1890 by Sol Simpson as Simpson Logging; spun out 2002 as Simpson Resource Company; renamed Green Diamond 2004; sixth-generation family ownership; HQ Seattle WA; manages ~2.2M acres in 9 states. | Green Diamond official About page | https://www.greendiamond.com/about | primary | 0.95 |
| 2 | Green Diamond HQ address 1301 Fifth Avenue Suite 2700, Seattle WA 98101-2613; phone (206) 224-5800; Shelton WA and Korbel CA operational offices. | Green Diamond official Contact page | https://www.greendiamond.com/contact-us | primary | 0.95 |
| 3 | Dale Sowell retired 2020 as VP/CFO of Green Diamond Resource Company; has served on MultiCare Health System Board of Directors since 2001; Chair, MultiCare Finance & Audit Committee. | MultiCare Health System Board of Directors page | https://www.multicare.org/about/leadership/board-directors | primary (host institution) | 0.95 |
| 4 | Douglas Reed is President of Green Diamond since 2014; great-great-grandson of founder Sol Simpson; TNC Washington Board Trustee; background in Simpson Door Company and California operations. | The Nature Conservancy Washington profile of Douglas Reed | https://www.nature.org/en-us/about-us/where-we-work/united-states/washington/stories-in-washington/douglas-reed | primary (host institution) | 0.90 |
| 5 | Green Diamond is a 5th-generation family timber company; Colin Moseley chairman since 1996; owns timberland in WA, OR, CA. | Washington Forest Protection Association 100th Anniversary founders page | https://anniversary.wfpa.org/founders/page_2.html | primary (trade association) | 0.90 |

## 1. Who they are
- **Verdict:** Green Diamond Resource Company is a top-five U.S. private timberland owner. It runs about 2.2 million acres across nine states. Estimated annual revenue is $35M to $500M (private company, no audited figure). It holds federal HCP permits that pre-clear its operations for 30+ years. Its power comes from the office it holds and its network, not overt politics. The company does not lobby visibly in Pierce County politics. But Dale Sowell's seat on the MultiCare board extends its network into Pierce County health care. Douglas Reed's TNC trusteeship gives it standing in the conservation world.
- **Possible conflicts of interest (defense expected):** One critique: the Reed family sits on both Green Diamond (commercial timber) and The Nature Conservancy (a conservation group) boards. That dual role could be read as either bridge-building or greenwashing. Defense: HCP compliance and third-party FSC and SFI certifications show real stewardship beyond words.
- **Other ways to read this (ICD-203):** Counter-reading: a private family timber company is just one of many Pacific NW operators, not a regional power center. Reading that elevates Green Diamond: about 2.2M acres of land controlled by one family for 130+ years makes it a structural economic power, even if it is not a Pierce County political actor. Its HCP permits set the de facto regional forestry standards. Tier-3 placement at rank 157 reflects that the Pierce County tie is indirect (Sowell → MultiCare; Shelton operations just outside the county line).
- **Confidence:** High on identity, history, acreage, and leadership (four primary sources: company About/Contact, MultiCare board bio, TNC profile, WFPA); Medium on revenue figure (private company, no audited financials); Medium on current employee count (range 144–500 across sources).
