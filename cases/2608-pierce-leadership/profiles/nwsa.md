<!-- entity-profile:v1 organization -->
# Northwest Seaport Alliance — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/nwsa.md`
**Entity ID:** `nwsa` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 131/163 · **Composite power:** 0.010
**Graph description:** Marine cargo operating partnership of the Ports of Seattle and Tacoma; manages container, breakbulk, auto and some bulk terminals.
**Known facts:** Formed Aug 4, 2015 under RCW 53.57; FMC-approved port development authority; CEO John Wolfe (also Port of Tacoma CEO); HQ Tacoma; co-chaired by home port commission presidents.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk12-rescue
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Inclusion rule:** decision-making + economic. The Northwest Seaport Alliance (NWSA) is the only bi-county port-operating joint authority in the U.S. It runs the marine cargo terminals that drive Pierce County's biggest private-sector employer cluster (logistics, longshore, drayage). It is also a Federal Maritime Commission–regulated body. Its actions affect every trade-dependent employer in the South Sound.
- **Adjacent but EXCLUDED candidates:** Port of Seattle (parent). Port of Tacoma (parent, kept as a separate node `port-tacoma`). SSA Marine and Northwest Container Services, which lease terminals from NWSA. Individual shipping lines (Maersk, MSC, ONE, etc.).

## 1. Who they are
- **Exact legal name:** The Northwest Seaport Alliance (NWSA).
- **Entity type:** Port development authority under state law (RCW) 53.57 (Wash. Rev. Code, "Joint Port Authorities"). Federal Maritime Commission–approved operating agreement (FMC Agreement No. 201228).
- **Formation date:** August 4, 2015, via an Interlocal Agreement between the Port of Seattle and the Port of Tacoma.
- **Governing law:** Washington RCW 53.57; FMC oversight. Interlocal agreement effective 8/4/2015. Current Alliance Agreement effective 9/18/2023.
- **HQ:** P.O. Box 2985, Tacoma, WA 98401-2985. Office space is also in Tacoma.
- **Parents:** Jointly owned by Port of Seattle and Port of Tacoma as equal members. Each port keeps ownership of its own real estate and assets.
- **CEO:** John Wolfe. He is also Port of Tacoma CEO. He was the first CEO when NWSA formed.
- **Charter/Bylaws:** Third Amended PDA Charter (effective 9/18/2023). Sixth Amended Bylaws (signed 1/7/2025).
- **Governance body:** "Managing Members" = the two 5-member port commissions acting together. The president of each home-port commission serves as co-chair of the NWSA Managing Members. They meet monthly, in public, on the first Tuesday. Meetings are streamed live.

## 3. Where their power comes from
- **Statutory authority:** RCW 53.57 lets two ports form a port development authority. NWSA has joint operating power over marine cargo terminals. It can bind both ports on terminal leases, capital projects, and labor rules.
- **Market position:** The combined gateway is the 6th-busiest U.S. container port by volume. It handles about $68 billion of waterborne trade with 175 trading partners (NWSA 2025 stats). 2024 international container volume: 3,340,733 TEUs (up 12.3% YoY). 2025: down 5.5% to 3.2M TEUs.
- **Economic leverage:** NWSA operations support about 52,000 jobs statewide and about $14 billion in business output (2025 Community Attributes study).
- **Federal nexus:** Subject to Federal Maritime Commission oversight (FMC Agreement No. 201228). It competes for federal INFRA and MEGA grants (e.g., Puget Sound Gateway Program Executive Committee — Marzano sits there).
- **Veto power:** Each port commission (5 elected members) can block alliance actions through the Managing Members structure. It acts like a two-house check.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Trade-dependent employers. International Longshore and Warehouse Union (ILWU) labor (longshore jurisdiction). Pierce County property-tax base via Port of Tacoma lease revenue. | 1, 4 |
| Who sits | Managing Members = 10 elected port commissioners (5 Seattle / 5 Tacoma). Pierce Co. reps in 2026: Marzano, McCarthy, Keller, Wilcox, Ang. | 1, 2 |
| Who governs | Tacoma-side commissioners co-chair with Seattle-side. Pierce Co. effectively holds 50% of Managing Members votes, even though Port of Tacoma carries a smaller cargo share in some segments. | 1, 2 |
| Who wins | Cargo volumes, lease rent to ports, ILWU hours, Pierce Co. property-tax base from Port of Tacoma industrial district. Trade-offs: noise and environmental hits concentrated near Tacoma Tideflats. | 1, 3 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Port of Tacoma (`port-tacoma`) | operates | 5 |

- **Note on graph convention:** The graph stores the parent→subsidiary direction (`port-tacoma → nwsa` as `operates`). The stub had `nwsa → port-tacoma operates`. That is the inverse of the real parent/child relationship. NWSA is *operated* by the two ports together. See "New relationships discovered" below.

## 1. Who they are
- Every claim above is grounded in primary documents (NWSA official site, FMC filings, Port of Tacoma news releases, Wikipedia for general reference, News Tribune for revenue context).

| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | NWSA is an FMC-approved port development authority under RCW 53.57, governed by Ports of Seattle & Tacoma acting through their 5-member commissions; HQ Tacoma; formed 8/4/2015 | NWSA official governance page | https://www.nwseaportalliance.com/about-us/governance | primary | 0.95 |
| 2 | Port of Tacoma commissioners for 2025: McCarthy (president), Marzano (vice president), Don Meyer (secretary), Keller (1st asst.), Ang (2nd asst.); McCarthy as commission president also serves as co-chair of the NWSA | Port of Tacoma news release, 12/17/2024 | https://www.portoftacoma.com/news/port-tacoma-designates-commission-officer-positions-2025 | primary | 0.95 |
| 3 | 2024 international container volume 3,340,733 TEUs (up 12.3% YoY); 2025 down 5.5% to 3.2M TEUs; supports about 52,000 jobs; about $68B waterborne trade with 175 partners (2025) | NWSA cargo statistics page & Port of Seattle maritime cargo post | https://www.nwseaportalliance.com/about-us/cargo-statistics ; https://www.portseattle.org/blog/2025-maritime-cargo-comings-and-goings | primary | 0.90 |
| 4 | Wikipedia summary (good-article rated): CEO John Wolfe (also Port of Tacoma CEO); parent organizations Port of Seattle and Port of Tacoma; revenue $195M (2017); formed 8/4/2015 | Wikipedia: Northwest Seaport Alliance | https://en.wikipedia.org/wiki/Northwest_Seaport_Alliance | secondary | 0.80 |

## 1. Who they are
- **Verdict:** The NWSA is a new kind of legal tool. It is the first North American inter-port operating authority. It pulls cargo-terminal decisions for two big U.S. ports into one 10-member Board. For Pierce County the effect is clear. 5 of 10 votes on every lease, capital project, and labor rule sit with Pierce County voters through their port commissioners. That makes the Port of Tacoma commission — especially its president, who co-chairs the NWSA — a structural lever on regional trade policy.
- **Conflicts-of-interest flags:** Commissioner Dick Marzano (Port of Tacoma, Position #2) served six years as ILWU Local 23 president before his 1995 election. He sits on the Tacoma-Pierce County Economic Development Board and the WSDOT Puget Sound Gateway Program Executive Committee. Those overlap with NWSA interests.
- **Analysis of alternatives:** The defense reading: NWSA is a transparent public body with audited financials and a two-house check. The critical reading: Pierce County holds 50% of votes on a body that drives billions in trade-dependent activity. The environmental and labor costs land in Tacoma Tideflats neighborhoods.
- **Confidence:** High. Primary-source governance docs, NWSA newsroom, Port of Tacoma newsroom, and FMC filings all agree on formation, structure, and 2025 leadership.
 (submit)<!-- Each line must match exactly:
<id>, target=<id>, relationship=<REL>, weight=<n>, note="..."
 REL whitelist: member, board, board_chair, chair, ceo, president, commissioner,
 owner, owned_by, parent, donated, ie, lobbying, lobbies, endorses,
 trains_candidates, federal_funding, state_funding, federal_appropriations,
 transit_funding, appropriates, property_tax_levy, levy, levy_funding, taxing,
 municipal, tax_exempt_status, tax_exemption, sovereignty, federal_land_grant,
 school_bond, ballot_measure, wellfound_jv, jv, operates, land_use, contract,
 family, mentor, staffer, appointed, grant, education, colleague, social -->
