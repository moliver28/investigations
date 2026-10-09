<!-- entity-profile:v1 organization -->
# PCCLC — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/pclc.md`
**Entity ID:** `pclc` · **Type:** organization · **Domain:** political
**Tier:** tier2 · **Rank:** 28/163 · **Composite power:** 0.068
**Graph description:** Pierce County Central Labor Council, AFL-CIO — organized labor's political and coordinating body for Pierce County; 114 affiliated unions, 44,000+ members.
**Known facts:** Founded 1890 as Tacoma Trades Council. 114 affiliated unions representing 44,000+ working people. President Alice Phillips (IBEW Local 483). Secretary-Treasurer Nathe Lawver (Building Trades).
**Status:** ✅ researched — 2026-09-19 — tier2-chunk1
**Sources:** 7/5 (minimum for tier2)

---

## 0. Why this person or group is on the map
- The PCCLC is the Pierce County Central Labor Council, AFL-CIO. It is the main political body for organized labor in Pierce County. It represents 114 affiliated unions and more than 44,000 workers.
- PCCLC is on the map for three reasons. (1) It exercises political power through endorsements and PAC (political action committee) spending. (2) Its officers sit on other boards: Nathe Lawver on the Greater Tacoma Community Foundation (GTCF) board, Alice Phillips on the Clover Park Board of Trustees. (3) Its endorsement process is driven by delegates, so it can pull labor votes behind a single candidate.
- Not on the map separately: the Washington State Labor Council (state parent body), Pierce County Labor Community Services Agency (the nonprofit arm), and each individual member union.

## 1. Who they are
- **Full name:** Pierce County Central Labor Council, AFL-CIO (PCCLC).
- **Type:** A 501(c)(5) labor organization. It is a chartered local labor council of the AFL-CIO.
- **Parent:** The AFL-CIO (national federation) and the Washington State Labor Council (state body).
- **Founded:** 1890 as the Tacoma Trades Council. The AFL chartered it as the Tacoma Central Labor Council. It later became the Pierce County Central Labor Council.
- **Address:** 3049 South 36th St., Suite 201, Tacoma, WA 98409.
- **Governing law:** The National Labor Relations Act (NLRA) and the AFL-CIO constitution.

## 3. Where their power comes from
- **Endorsement power:** PCCLC endorsements come from "union delegates representing more than 44,000 working people across Pierce County after a democratic process." Endorsements bring volunteer capacity, get-out-the-vote (GOTV) work, and PAC support. In 2025, PCCLC endorsed candidates for State Senate District 26 (Deborah Krishnadasan), Tacoma Mayor (Anders Ibsen), Tacoma City Council (Latasha Palmer, Silong Chhun, Joe Bushnell), Puyallup City Council, and multiple school board races.
- **PAC spending:** PCCLC has a political action committee that files with the state PDC (Public Disclosure Commission). Older records show $24,650 in 2014, $45,550 in 2016, and $32,150 in 2018. Current cycle spending is not confirmed.
- **Candidate training:** PCCLC recruits and trains labor-aligned candidates for local office. Its endorsement pipeline feeds into the Pierce County Democratic Party.
- **Solidarity work:** PCCLC calls itself "a democratic hub where unions come together to organize, advocate, educate, and build solidarity across industries and communities."

## 4. Power in numbers
|| Indicator | Finding | Source # |
||-----------|---------|----------|
|| Who benefits | Endorsed candidates get volunteers, GOTV, and PAC support. The 44,000+ union members get labor movement coordination. Member unions get political leverage through collective action. | #1, #3, #5 |
|| Who sits | President Alice Phillips (IBEW Local 483). Secretary-Treasurer Nathe Lawver (Building Trades). Vice President Christina Hall. Ten or more Executive Board members and Trustees. | #1, #2 |
|| Who governs | Delegate-driven governance. Monthly delegate meetings at 7 to 9 PM. Endorsements and resolutions are voted on by delegates. The executive board runs things between meetings. | #1, #5 |
|| Who wins | Endorsed candidates gain labor vote share. PCCLC backed the Pierce Transit ballot measure to expand transit. It named May 2026 Hispanic Heritage Month by resolution. | #3, #5 |

## 5. How they touch government
- **Campaign finance and PAC:** PCCLC files political expenditure reports with the state PDC. Older totals were $24,650 (2014), $45,550 (2016), and $32,150 (2018). Current cycle totals are not yet confirmed.
- **Endorsements:** PCCLC endorses candidates for local, county, and state races. 2025 endorsements include State Senate District 26, Tacoma Mayor, Tacoma City Council, Puyallup City Council, Gig Harbor City Council, Steilacoom Mayor, and several school board races.
- **Ballot measures:** PCCLC endorsed the Pierce Transit ballot measure to expand transit service.
- **Lobbying:** As a 501(c)(5), PCCLC can do political activity and lobbying beyond what a 501(c)(3) can do. Specific lobbying registrations are not confirmed.
- **Government contracts:** None identified. Not confirmed.

## 6. Other seats they hold
- **Alice Phillips** — President. IBEW Local 483 member (retired Business Manager, longest-serving, 30 years). Sits on the Clover Park Board of Trustees. 40 years of labor movement experience. First woman in several IBEW Local 483 leadership roles.
- **Nathe Lawver** — Secretary-Treasurer. Also Executive Secretary of the Pierce County Building and Construction Trades Council AFL-CIO. Sits on the GTCF board At-Large. Connects PCCLC to philanthropy and the building trades.
- **Christina Hall** — Vice President.
- **Executive Board:** Rick Hertzog, Jade Monroe, Brenda Wiest, Brent Wagar, Amber Roulst, Jared Ross, Cindy Richardson, Floyd David Dugan, Patti Dailey-Shives.
- **Patti Dailey-Shives** — Executive Board member. Also sits on the Pierce County Labor Community Services Agency board.
- **Member unions:** ILWU Local 23, Teamsters, plus 112 other affiliated unions.
- **Pierce County Democrats:** Aligned. PCCLC endorsements usually match Democratic Party candidates.
- **Ryan Mello:** Endorsed. Now the Pierce County Executive.

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Pierce Dems (`pierce-dem`) | aligned | 4 |
| Ryan Mello (`ryan-mello`) | endorsed | 4 |
| Nathe Lawver (`nathe-lawver`) | exec | 5 |
| ILWU Local 23 (`ilwu23`) | member | 4 |
| Teamsters (`teamsters`) | member | 4 |
| Alice Phillips (`alice-phillips`) | president | 5 |

- **New edges identified:**.
pclc, target=gtcf, relationship=board_interlock, weight=3, note="https://www.gtcf.org/about/gtcf-team" (Nathe Lawver on both PCCLC and GTCF boards).
pclc, target=alice-phillips, relationship=president, weight=5, note="https://unionhall.aflcio.org/pcclc/about-us/alice-phillips" (confirms existing edge).
pclc, target=clover-park, relationship=board_interlock, weight=2, note="https://unionhall.aflcio.org/pcclc/about-us/alice-phillips" (Alice Phillips on Clover Park Board of Trustees).
pclc, target=wslc, relationship=affiliated, weight=3, note="https://unionhall.aflcio.org/pcclc/content/14706" (one of nearly 500 state/local labor councils chartered by AFL-CIO).

## Sources
| # | Claim | Source | URL | Type | Reliability |
|---|-------|--------|-----|------|-------------|
| 1 | PCCLC was founded in 1890 as the Tacoma Trades Council. It has 114 affiliated unions and more than 44,000 members. Address: 3049 S 36th St Suite 201 Tacoma WA 98409. Officers: Nathe Lawver, Alice Phillips, Christina Hall. Ten or more executive board members. | PCCLC AFL-CIO website | https://unionhall.aflcio.org/pcclc/content/14706 | primary | 0.97 |
| 2 | Alice Phillips is PCCLC President. She is an IBEW Local 483 member. She retired from the City of Tacoma. She has 40 years of labor experience and was the longest-serving Business Manager of IBEW Local 483 (30 years). She sits on the Clover Park Board of Trustees. | PCCLC website bio | https://unionhall.aflcio.org/pcclc/about-us/alice-phillips | primary | 0.97 |
| 3 | PCCLC 2025 endorsements: Deborah Krishnadasan (State Senate D26), Anders Ibsen (Tacoma Mayor), Latasha Palmer, Silong Chhun, Joe Bushnell (Tacoma Council), and other local races. | Blue Voter Guide | https://bluevoterguide.org/endorser-org/Pierce_County_(WA)_Labor_Council,_AFL-CIO/WA/4490 | secondary | 0.85 |
| 4 | The Tacoma Trades Council started in 1890. The AFL chartered it as the Tacoma Central Labor Council. It later became the Pierce County Central Labor Council. | Archives West | https://archiveswest.orbiscascade.org/ark:80444/xv00503 | primary | 0.90 |
| 5 | Endorsements come from delegates representing more than 44,000 workers. PCCLC endorsed the Pierce Transit ballot measure to expand transit service. | PCCLC website news | https://unionhall.aflcio.org/pcclc/content/14709 | primary | 0.95 |
| 6 | PCCLC political expenditures per PDC records: $24,650 (2014), $45,550 (2016), $32,150 (2018). | Freedom Foundation | https://www.freedomfoundation.com/washington/freedom-foundation-sues-pdc-again-for-ignoring-union-violations-of-campaign-finance-laws | secondary | 0.70 |
| 7 | Patti Dailey-Shives sits on the PCCLC Executive Board and on the Pierce County Labor Community Services Agency Board. | Pierce County Labor Community Services Agency | https://www.pclaborcares.org/aboutus | primary | 0.90 |

## 12. Bottom line
- **The bottom line.** PCCLC is the central voice of organized labor in Pierce County. It has 114 affiliated unions and more than 44,000 members. It can move labor votes through endorsements and PAC spending.
- **Why it matters.** Endorsements bring volunteers and money. The PCCLC pipeline feeds into the Pierce County Democratic Party. It endorsed Ryan Mello, who is now County Executive. Its leaders also sit on the GTCF board and the Clover Park school board.
- **The counter-view.** Union density has dropped nationally. The PAC totals of $24,000 to $46,000 (2014 to 2018) are small compared to independent-expenditure campaigns. The 44,000-member number may overstate how many members are politically active.
- **Why PCCLC still matters.** The delegate-driven endorsement process and the dense board overlaps give PCCLC real structural influence. Its leaders connect labor, philanthropy (GTCF), and education (Clover Park).
- **Confidence:** Medium. The AFL-CIO website provides strong primary sourcing for the council's structure and leaders. PAC totals come from a secondary source (the Freedom Foundation). Current-cycle PDC data was not pulled.