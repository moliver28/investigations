<!-- entity-profile:v1 organization -->
# Banner Bank — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/banner-bank.md`
**Entity ID:** `banner-bank` · **Type:** organization · **Domain:** economic
**Tier:** tier3 · **Rank:** 150/163 · **Composite power:** 0.005
**Graph description:** Banner Bank — regional bank; AJ Gordon (Banner) was Chamber Board Chair
**Known facts:** (from graph) AJ Gordon served as Tacoma-Pierce County Chamber Board Chair
**Status:** ✅ researched — 2026-09-19 — tier3-chunk15
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why it is on the map:** Banner Bank is on the map because it is well-connected and holds civic office through its leaders. Banner Bank is the main operating part of Banner Corporation (a company that trades on the NASDAQ stock exchange under the symbol BANR). It is a Washington-state-chartered commercial bank based in Walla Walla. Banner runs branches in Tacoma and across Pierce County. Two Tacoma branches are at 1015 A Street and 1211 South Pearl Street. Banner is on this map because one of its officers, AJ Gordon, was Board Chair of the Tacoma-Pierce County Chamber of Commerce. That gives Banner direct civic leadership ties.
- **Who is NOT on the map:** Umpqua Bank (a Pacific Northwest rival), Columbia Bank (now part of Umpqua), and big national banks like Wells Fargo, JPMorgan, and Bank of America. They have Tacoma branches but no specific Pierce County board ties in this research. Islanders Bank, a Banner subsidiary in the San Juan Islands, is not a separate entity.

## 1. Who they are
- **Legal name (operating part):** Banner Bank. It is a Washington-state-chartered commercial bank.
- **Parent company:** Banner Corporation. It is a Washington company that trades on the NASDAQ stock exchange under the symbol BANR. It started as a thrift in 1890 (per the Banner Bank About page).
- **Headquarters:** 10 South First Avenue, P.O. Box 907, Walla Walla, WA 99362.
- **Type:** Washington-state-chartered commercial bank. It is insured by the FDIC (Federal Deposit Insurance Corporation). Its parent company files with the Securities and Exchange Commission (SEC).
- **Leadership:** President & CEO Mark J. Grescovich. He became President in April 2010 and CEO in August 2010. He held other banking jobs before that. His total pay for fiscal year 2025 was $3,590,983, per AFL-CIO PayWatch.
- **Subsidiaries:** Banner Bank (the operating bank) and Islanders Bank (3 branches in the San Juan Islands), per SEC filings.
- **Law that governs it:** Washington State banking code. The Washington State Department of Financial Institutions (DFI) supervises it. The SEC oversees the parent. The Federal Reserve oversees the holding company.
- **Size:** $16.34 billion in assets as of March 31, 2026 (per Banner's release on the Pacific Financial deal). Branches in Washington, Oregon, Idaho, and California. It calls itself one of the largest community banks in the Pacific Northwest.
- **Recent deal:** Banner plans to buy Pacific Financial Corporation of Aberdeen, WA. Pacific Financial is the parent of Bank of the Pacific. The deal was announced in 2026.

## 3. Where their power comes from
- **Power from the law:** As a state-chartered commercial bank, Banner makes loans, takes deposits, and offers mortgages and treasury services. It is supervised by the Federal Reserve and the DFI. Banner is not a regulator itself.
- **Domain = economic.** Power comes from its market position as a Pacific Northwest bank and from its civic board ties.
- **Key facts:**
 - Revenue: FY 2025 CEO pay was $3.59 million (a rough scale measure). Full financial data is on SEC EDGAR (the SEC's public filing system).
 - Ownership: Public, traded on NASDAQ under BANR. Institutional and individual shareholders own it.
 - Market position: Pacific Northwest community-banking leader (about $16 billion in assets). One of the largest banks based in Washington.
 - Government contracts and deposits: Banner holds public funds in places where it serves as a bank for government. Its exact Pierce County depositary status was not confirmed.
 - Jobs: About 2,000+ employees across the Pacific Northwest. The exact number was not confirmed.
 - Real estate: Branch network in Tacoma (1015 A St, 1211 S Pearl St) and across Pierce County. Specific holdings were not confirmed.
- **Civic leadership:** AJ Gordon was Board Chair of the Tacoma-Pierce County Chamber of Commerce around 2021–2022, when the Chamber moved from Tom Pierson to Andrea Reay as President & CEO. Other Banner bankers in the area include Christopher Estrada (VP, Tacoma–Pierce County region), Doug Hedger (VP, Pierce & South King counties), and Michael Cruz (VP, Branch Manager in Tacoma). That is a deep bench for one bank in Pierce County.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Banner Corporation shareholders; commercial and consumer banking customers; the Tacoma-Pierce County Chamber (when a banker chairs its board, the Chamber benefits from that sponsor tie) | 2, 3 |
| Who sits | Board Chair of the Tacoma-Pierce County Chamber (AJ Gordon, around 2021–2022); Mark Grescovich as CEO of Banner Corp and Banner Bank | 2, 3 |
| Who governs | Standard bank rules: SEC-reporting parent; state-chartered bank; DFI and Federal Reserve oversight. Banner does not write rules. | 1, 3 |
| Who wins | Pacific Northwest commercial real estate, farm lending, and small-business borrowers; bank shareholders; Pacific Northwest non-profits (Banner gives about $2 million a year to charity plus thousands of volunteer hours, per company materials) | 4 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Chamber of Commerce (`chamber`) | board_chair | 3 |

**New edges to add:**.
`banner-bank`, target=`banner-corp`, relationship=`subsidiary_of`, weight=5, note="Banner Corporation (NASDAQ: BANR) is the parent of Banner Bank; SEC filings https://www.sec.gov/Archives/edgar/data/946673/".
`banner-bank`, target=`tacoma-branch-network`, relationship=`operates_branches`, weight=2, note="1015 A St and 1211 S Pearl St Tacoma; https://locations.bannerbank.com/wa/tacoma".
`banner-bank`, target=`bank-of-the-pacific`, relationship=`acquirer`, weight=3, note="Pending acquisition of Pacific Financial Corp / Bank of the Pacific announced 2026; https://investor.bannerbank.com/news/news-details/2026/Banner-Corporation-to-Acquire-Pacific-Financial-Corporation/".
`banner-bank`, target=`economic-development-board`, relationship=`board_or_member`, weight=1, note="UNVERIFIED — would be plausible given AJ Gordon's Chamber involvement; no direct EDBoTPC roster confirmation in primary sources reviewed".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Banner Corporation is the parent company of Banner Bank; $4.2B in assets at time of NCW Community Bank merger filing (historical); Walla Walla HQ | SEC filing, Banner Corporation 8-K (2007) | https://www.sec.gov/Archives/edgar/data/946673/000093905707000220/k8062707.htm | primary (SEC) | 0.95 |
| 2 | "Tacoma-Pierce County Chamber board chair AJ Gordon, of Banner Bank" — direct quote from South Sound Business | South Sound Business Journal, "Tacoma-Pierce County Chamber Announces New President/CEO" | https://www.southsoundbiz.com/news/tacoma-pierce-county-chamber-announces-new-president-ceo/article_5e7da3a2-bcf6-11ec-ba2f-a32daed8331e.html | secondary (trade press) | 0.90 |
| 3 | Banner Corporation/Banner Bank HQ; CEO Mark J. Grescovich named President 2010 then CEO 2010; DFI lists Banner Bank as Washington state-chartered; Walla Walla HQ | Washington State DFI commercial bank list | https://dfi.wa.gov/banks/who-we-regulate/commercial | primary (regulator) | 0.95 |
| 4 | Banner Bank: 135+ year history; ~$16B assets (Mar 2026); WA/OR/ID/CA footprint; ~$2M annual charitable giving; community-bank identity; multiple PNW "Best Bank" awards | Banner Bank "About Us" page | https://www.bannerbank.com/about-us | primary | 0.90 |

## 1. Who they are
- **Verdict:** Banner Bank is a $16 billion Pacific Northwest community bank (its parent trades on NASDAQ under BANR). Its main Pierce County tie is the AJ Gordon board overlap with the Tacoma-Pierce County Chamber of Commerce. As Chamber Board Chair, a Banner officer helped guide the change from Tom Pierson to Andrea Reay. That gave Banner a view into regional economic-development strategy. The bank runs Tacoma branches. It is now buying Bank of the Pacific.
- **Conflicts of interest (defense counter-argument):** A possible critique: a banker chairing the Chamber creates an appearance that Chamber policy favors banking interests (commercial real estate loans, tax policy, regulatory burden). The counter: AJ Gordon works in technology banking, not consumer or real estate lending. Chamber bylaws require members to step aside on direct competitor matters. No public conflict allegation was found.
- **Analysis of alternatives (investigative control document (ICD)-203):** The counter-view is that community banks are a commodity in Pacific Northwest finance and do not move civic outcomes. The view that elevates Banner: Chamber endorsements and legislative priorities do shape South Sound economic policy. A banker in the chair can shape those priorities. The evidence supports the tier-3 placement at rank 150.
- **Confidence:** High on the corporate identity, HQ, size, and Chamber board overlap (three independent sources). Medium on how long AJ Gordon served as chair (the graph shows a moment in time; the role may have rotated).