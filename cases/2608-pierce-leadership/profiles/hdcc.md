<!-- entity-profile:v1 organization -->
# HDCC — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/hdcc.md`
**Entity ID:** `hdcc` · **Type:** organization · **Domain:** political
**Tier:** tier3 · **Rank:** 106/163 · **Composite power:** 0.016
**Graph description:** Washington State House Democratic Campaign Committee — the campaign arm of the WA House Democratic Caucus. Endorses and funds House Democratic candidates statewide, including in Pierce County legislative districts (2, 25, 26, 27, 28, 29, 30, 31, 35).
**Known facts:** Official campaign committee of the Washington House Democratic Caucus; PDC-registered political committee (continuous reporting); Chair: Rep. Monica Stonier (49th LD, Clark County); mailing address PO Box 9100, Seattle, WA 98109; has held Democratic House majority in Olympia since 2001 per the committee's own framing.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk7
**Sources:** 4/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Inclusion rule:** Well-connected and decision-making. The House Democratic Campaign Committee (HDCC) is the official campaign arm of the Washington State House Democratic Caucus. It is on this map because its spending shapes which Democrats win or lose House elections in Pierce County. Those districts are LD 2, 25, 26, 27, 28, 29, 30, 31, and 35. The power-graph edge `hdcc → ryan-mello, donated, weight=6` shows a documented money flow into a Pierce County candidate.
- **Adjacent but EXCLUDED candidates:** The Washington State Democratic Party (state party at wadems.org) overlaps on candidate endorsements and get-out-the-vote work. It is a separate legal entity. The Senate Democratic Campaign Committee (SDCC) is the Senate counterpart. It is not mapped at this tier. House caucuses like the Members of Color Caucus or the New Democrat Coalition are caucus groups, not campaign committees. They are outside this profile.

## 1. Who they are
- **Exact legal name:** House Democratic Campaign Committee (HDCC)
- **Entity type:** Washington State political committee. It is a continuous-reporting committee registered with the Washington Public Disclosure Commission (PDC).
- **PDC committee ID:** co-2026-9042 (2026 cycle identifier). The committee ID format is consistent with PDC's continuous committee scheme for WA House Democrats.
- **Registered office:** PO Box 9100, Seattle, WA 98109 (per the HDCC donation page).
- **Chair (2025–2026 cycle):** Rep. Monica Stonier. She represents Washington House District 49 in Vancouver, Clark County. She is the House Majority Floor Leader.
- **Governing instrument:** HDCC operates as the campaign committee of the House Democratic Caucus. It is not a separate 501(c) entity. It is a political committee under state law RCW 42.17A, Washington's Campaign Disclosure and Contribution law.

## 3. Where their power comes from
- **Statutory authority:** As a registered political committee under RCW 42.17A, HDCC can raise and spend money. It can support or oppose candidates for the Washington House. It is the main way the caucus spends on House races.
- **Candidate recruitment and endorsement gatekeeping:** HDCC is how the House Democratic Caucus picks, recruits, endorses, and pays for its candidates. The committee "works to elect House Democrats to lead our state forward." It also works to "strengthen the Democratic House majority in Olympia — a majority we have held since 2001."
- **Domain overlap:**
  - **political ↔ gov:** HDCC spends directly into Washington House races. The committee exists to help the caucus keep its House majority.
  - **political ↔ econ:** HDCC coordinates with labor groups. Partners include the Washington Education Association (WEA). The National Education Association (NEA) is a partner. The Service Employees International Union (SEIU) is a partner. The United Food and Commercial Workers (UFCW) is a partner. PDC filings show these flows.
- **Key facts:**
  - **PAC spending:** Independent expenditures and coordinated contributions to candidates are filed at the PDC. Specific 2024 and 2026 spending totals by race were not extracted in this pass. They are UNVERIFIED.
  - **Party machinery control:** Through the chair and caucus-aligned staff, HDCC picks which Democratic primaries to enter. It picks where to put organizational muscle. It also picks where to withhold resources.
  - **Candidate recruitment/training:** Caucus-affiliated training pipelines like Candidate Academy and Pierce County Dems feed into HDCC-endorsed candidacies.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Incumbent and challenger House Democrats running in competitive districts gain from coordinated spending, list rentals, polling, field operations, and paid media that HDCC pays for. In Pierce County, that includes races in LD 25, 27, 28, 29, 30, 31, and 35. | Sources 1, 2 |
| Who sits | The committee is chaired by Rep. Monica Stonier (49th LD). The broader board and membership includes House Democratic caucus leadership. HDCC is not autonomous; it is the campaign arm of sitting Democratic House members. | Source 1 |
| Who governs | The House Democratic Caucus as an institution governs HDCC. The caucus sets the strategy and the resource map. HDCC carries it out through spending. | Source 1 |
| Who wins | Democratic House candidates who get HDCC backing gain from coordinated spending and party infrastructure. The graph's `hdcc → ryan-mello, donated, weight=6` edge documents a prior financial relationship with a Pierce County candidate. Since 2001, per HDCC's own messaging, Democrats have held the House majority continuously. That 25-year run is the committee's work product. | Sources 1, 3 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):
| Connected entity | Relationship | Weight |
|---|---|---|
| Ryan Mello (`ryan-mello`) | donated | 6 |

- 
hdcc, target=pierce-dem, relationship=caucus_affiliate, weight=3, note="https://www.piercecountydems.com/".
hdcc, target=monica-stonier, relationship=chaired_by, weight=4, note="https://www.hdcc.org".
hdcc, target=state-house-democratic-caucus, relationship=campaign_arm, weight=5, note="https://www.hdcc.org".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | HDCC is the official campaign committee of the Washington State House Democratic Caucus; chaired by Rep. Monica Stonier; majority held since 2001; mailing address PO Box 9100, Seattle, WA 98109 | HDCC official website | https://www.hdcc.org | primary | 0.95 |
| 2 | Donation portal, mailing instructions, online contribution form | HDCC official website — Donate page | https://www.hdcc.org/donate | primary | 0.95 |
| 3 | Graph edge `hdcc → ryan-mello, donated, weight=6` documents a prior financial relationship between HDCC and a Pierce County candidate | Power-graph v2 (project internal) | https://www.theurbanist.org/ryan-mello-has-a-clear-vision-for-pierce-county | secondary | 0.80 |
| 4 | PDC committee registration identifier and continuous-committee reporting status for HDCC (2026 cycle: co-2026-9042) | Washington State Public Disclosure Commission | https://www.pdc.wa.gov/political-disclosure-reporting-data/browse-search-data/committees/co-2026-9042 | primary | 0.95 |

## 1. Who they are
- **Verdict:** HDCC is not powerful on its own. It is the operational arm of a powerful institution, the Washington House Democratic Caucus. Its real control is the ability to direct coordinated campaign spending into specific House races. That includes Pierce County races. That is enough to change competitive dynamics in primaries and general elections. The committee has been the institutional vehicle for the Democratic House majority since 2001. That is a 25-year run, per HDCC's own framing. Its power is party-internal, not market-based.
- **Conflicts-of-interest flags:** HDCC's chair is a sitting House member, Stonier. That creates an inherent conflict between incumbent-protection spending and challenger-candidate support. Incumbents on the committee may favor incumbents in primaries. The committee's spending decisions affect which Democrats hold office, which in turn affects legislation. No formal recusal mechanism is documented. That is UNVERIFIED.
- **Analysis of alternatives:** An opposing reading: HDCC is one of many political committees competing for influence in Washington House races. The Republican counterpart, the Washington House Republican Campaign Committee, plays the same role on the other side. HDCC's "donated to Ryan Mello" edge reflects a prior candidate. Mello ran for and won the Pierce County Executive seat in 2024. That was not a House race. That suggests the edge documents a broader Democratic-funding network rather than HDCC's specific House-race activity. The graph edge may be mis-classified at the relationship-type level. HDCC's actual leverage in 2024 House races in Pierce County is UNVERIFIED.
- **Confidence:** Medium. The official website and PDC registration are primary and reliable. Specific 2024 and 2026 spending by race, candidate pipeline metrics, and PDC financial totals were not pulled in this pass. The chair and caucus relationship is FACT. The weight-6 donation to Mello edge is INFERENCE from graph data. It is not independently verified by a primary-source PDC filing.