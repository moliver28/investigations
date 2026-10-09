# SKEPTIC RANKING REPORT — Pierce County Leadership Investigation (INV-2026-002)

**Reviewer:** Skeptical investigative reviewer (assumes every rank is wrong until proven otherwise)
**Date:** 2026-09-09
**Object of attack:** The composite power score ranking in `evidence/11-power-network.html` (157 nodes)
**Method:** Cross-checked the graph's embedded node data (extracted from the HTML) against the documented methodology (`26-power-methodology.md`), the power matrix (`12-power-matrix.md`), the audit (`audit-pierce-graph.md`), the build script (`scripts/build_power_network.py`), and primary sources via web search.

---

## EXECUTIVE SUMMARY

**The graph's ranking is a network-centrality measure, not a power measure, and it is NOT the ranking the investigation's own evidence supports.** The investigation's own audit (`audit-pierce-graph.md`) and red-team report (`red-team-report.md`) both conclude this explicitly: *"Do not use the raw composite as the final ranking."* The graph was rebuilt with a veto bonus and party cap (in `build_power_network.py`), but **those corrections were insufficient** — the Council still scores a perfect 1.000, the party nodes still outrank the Sheriff, and the Tacoma Mayor is buried at #147.

**The single most damning finding:** The graph's own guided-mission text (line 670 of the build script) says *"The most powerful actor is Ryan Mello, the Pierce County Executive (power score 9.2). The County Council is second (8.7)."* — but the graph's actual ranking puts **Council #1 (1.000) and Mello #6 (0.250)**. The graph contradicts its own narrative. This is a confirmed measurement error.

---

## A. COUNCIL AT #1 WITH PERFECT 1.0 — CONFIRMED ERROR

**Suspected problem:** A 7-member legislative body scoring a perfect 1.0 while the County Executive (who has the veto, the $3.5B budget, and countywide mandate) scores 0.250.

**Verdict: CONFIRMED ERROR.** Council #1 is a centrality-over-ranks-hubs artifact, exactly as the audit warned.

**Evidence:**
- The graph's Council node has **61 connections** — by far the most in the network (Mello has 13, MultiCare 15, Chamber 16). Its weighted degree dominates the 35% weight.
- The audit (`audit-pierce-graph.md`, §3) recomputed the composite and found Council's degree is **inflated by filler edges** (media→council, state_funding, federal_funding, levy_funding, reversed `appropriates` edges) that the audit flagged as "padding that inflates Council degree."
- The audit's own verdict: Council is **"OVER-RANKED"** — /12 ranks Mello #1, Council #2.
- The build script's veto bonus does NOT touch the Council (it's not in the `VETO_BONUS` dict), so Council's raw centrality stands at 1.000.
- The power matrix (`12-power-matrix.md`) scores Mello 9.2 vs Council 8.7 — Mello #1, Council #2.
- Primary source: Pierce County's own charter (piercecountywa.gov) confirms the Council "has all powers of the County not otherwise reserved to the people, the Executive, or general law" — i.e., the Executive holds the veto and budget authority; the Council is a check, not the apex.

**What the top 5 SHOULD be** (per the investigation's own evidence/12 matrix + audit):
1. **Ryan Mello** (County Executive) — 9.2
2. **Pierce County Council** — 8.7
3. **Puyallup Tribe** — 8.1 (sovereignty/veto)
4. **MultiCare** — 7.6
5. **JBLM** — 7.4

The graph's #1 (Council) and #6 (Mello) are **swapped**. The Chamber at #2 is defensible as a top-5 actor (the audit and /13 score it CRITICAL) but should not outrank the Tribe, JBLM, or MultiCare on raw power.

**Action: RE-RANK.** Council must be demoted to #2 (or lower, given the filler-edge inflation), Mello promoted to #1. The perfect 1.0 is indefensible.

---

## B. MYSTERY LOW-POWER INDIVIDUALS — MOSTLY DEFENSIBLE, A FEW INFLATED

I verified each person's identity and role against primary sources. **All 14 are real people with the roles the graph assigns.** The question is whether their rank is justified.

| Person | Rank | Graph role | Verified role (primary source) | Verdict |
|--------|------|-----------|-------------------------------|---------|
| **John McCarthy** | #21 (0.085) | Port Commissioner | Port Commissioner 4 terms/40 yrs, FMSIB board, NWSA co-chair (portoftacoma.com, fmsib.wa.gov) | **DEFENSIBLE** — but UNDER-ranked. /12 ranks him #12. His power is institutional longevity, not centrality. |
| **Paul Herrera** | #33 (0.054) | Council D-2 (R) | Councilmember D-2, won 2024 (evidence/01, /04) | **DEFENSIBLE** — a council member with 3 edges. Rank is reasonable. |
| **Michael Shaw** | #58 (0.039) | County lobbyist | Pierce County's contracted state lobbyist, $110K/yr (evidence/07, PDC L-5) | **DEFENSIBLE** — a hired lobbyist is not a power center. Rank is fine. |
| **Eric Johnson** | #106 (0.018) | Port Exec Director | Port of Tacoma Executive Director since 2019 (portoftacoma.com) | **DEFENSIBLE** — but note: he's also on the Chamber board and EDB exec committee (portoftacoma.com). The graph gives him only 1 edge (port-tacoma), **missing his Chamber/EDB interlocks** — he's UNDER-connected in the graph. |
| **Dick Marzano** | #110 (0.018) | Port Commissioner | Port Commissioner, 2026 Commission President (portoftacoma.com, NWSA minutes) | **DEFENSIBLE** — but as 2026 Commission President he's arguably the most powerful Port commissioner this year; the graph ranks him below McCarthy. Borderline. |
| **Deanna Keller** | #127 (0.014) | Port Commissioner | Port Commissioner since 2019 (portoftacoma.com) | **DEFENSIBLE** — one of 5 equal commissioners. |
| **Kristin Ang** | #128 (0.014) | Port Commissioner | Port Commissioner, first person of color elected, Puyallup Tribe endorsement (portoftacoma.com) | **DEFENSIBLE** — but her Puyallup Tribe endorsement is a notable edge the graph omits. |
| **Alice Phillips** | #132 (0.013) | PCCLC President | PCCLC President, IBEW 483 (unionhall.aflcio.org) | **DEFENSIBLE** — but she's the head of the county's labor federation (114 unions/44K workers per /16). The graph gives her 1 edge (pclc). **UNDER-connected** — she should link to the unions she leads. |
| **Kathi Littmann** | #137 (0.012) | GTCF CEO | GTCF President/CEO since 2015, transitioning by 2027 (gtcf.org) | **DEFENSIBLE** — but she's stepping down; her rank is fine. |
| **Ivan Harrell** | #138 (0.012) | TCC President | TCC 11th President since 2018 (tacomacc.edu) | **DEFENSIBLE** — TCC president, 1 edge. Fine. |
| **Josh Garcia** | #135 (0.013) | Tacoma Schools Supt | Tacoma Public Schools Superintendent (tacomaschools.org) | **DEFENSIBLE** — but he runs a $665M district (per graph facts). The graph gives him 1 edge. **UNDER-connected** — should link to the school board, city, and construction contractors. |
| **Korey Strozier** | #143 (0.011) | Tacoma School Board President | TPS Board President (tacomaschools.org) | **DEFENSIBLE** — school board president, 1 edge. Fine. |
| **Tim Reynon** | #108 (0.018) | Puyallup Tribal Council | Tribal Council member, ex-Gov Office of Indian Affairs Director (governor.wa.gov, puyalluptribe-nsn.gov) | **DEFENSIBLE** — but he's a direct line to Gov. Ferguson. The graph gives him 1 edge (puyallup-tribe). **UNDER-connected** — his Governor's-office link is a real power edge that's missing. |
| **Diann Puls** | #105 (0.019) | VMFH Board | VMFH board, ex-Weyerhaeuser pension/risk director (vmfh.org) | **DEFENSIBLE** — 2 edges (vmfh, weyerhaeuser). Correctly captures her interlock. |

**Overall verdict on B:** No individual is **inflated** — all ranks are defensible or under-ranked. The pattern is the opposite of the suspicion: these people are **under-connected** in the graph, not over-ranked. The graph gives most of them a single edge to their employer, missing their real interlocks (Johnson→Chamber/EDB, Phillips→unions, Reynon→Governor, Garcia→city/contractors).

**Action: NO CHANGE to ranks (they're defensible), but ADD missing edges** for Johnson, Phillips, Reynon, Garcia to reflect their real interlocks.

---

## C. PARTY NODES — CONFIRMED ERROR (cap not working)

**Suspected problem:** Pierce Dems (#8, 0.217) and Pierce GOP (#15, 0.123) rank above the Sheriff (#9, 0.166) and nearly above the County Executive.

**Verdict: CONFIRMED ERROR.** The party cap exists in the build script but **does not bind**, so the party-node artifact persists.

**Evidence:**
- The build script (`build_power_network.py`, lines 86-88) caps party nodes at 0.30: `composite[nid] = min(composite[nid], 0.30)`. But Dems (0.217) and GOP (0.123) are **already below 0.30**, so the cap does nothing.
- Pierce Dems has **16 connections**, including 9 legislator `member` edges (Trudeau, Nobles, Conway, Jinkins, Morgan, Cantwell, Murray, Randall, Strickland). This is the exact "collects all legislator member edges" artifact the audit warned about.
- The audit (`audit-pierce-graph.md`, §3) called Dems **"GROSSLY OVER-RANKED"** — /12 ranks Dems #14, GOP #13. The graph has Dems #8, GOP #15.
- The power matrix scores Dems 4.8 and GOP 5.0 — both in the bottom half of the top-25, NOT top-10.

**What's wrong:** A party committee's power is the sum of its members' power, but it should NOT outrank the individual elected officials who actually hold office. Dems at 0.217 outranking the Sheriff (0.166) and nearly matching the Executive (0.250) is a structural artifact.

**Action: RE-RANK.** Party nodes should be capped well below the elected officials they serve — at most ~0.10-0.12 (below the Sheriff and Prosecutor). Dems should drop from #8 to ~#15-18; GOP from #15 to ~#20-22. The cap needs to be lowered from 0.30 to ~0.12.

---

## D. KELLY CHAMBERS (#18, 0.101) — CONFIRMED ERROR (over-ranked)

**Suspected problem:** A state senator ranked above the County Executive's council members and the Sheriff.

**Verdict: CONFIRMED ERROR.** Kelly Chambers is **not a state senator** — she is a **former** State Representative (R-25) who **left office January 13, 2025** and **lost the 2024 County Executive race** to Mello (48.58% to 51.28%).

**Evidence:**
- Ballotpedia: "She left office on January 13, 2025. Chambers did not run for re-election to Washington House of Representatives District 25-Position 1 in 2024."
- BillTrack50: "Out of Office" — WA House District 25, 01/14/2019 to 01/14/2025.
- The graph's own data labels her "political" and gives her **only 2 connections** (pierce-gop, tacoma-pd-union). Her 0.101 score comes almost entirely from the **veto bonus (+0.06)** in the build script plus her party edge — not from any current office or network position.
- The power matrix ranks her #10 (5.9) based on her 2024 campaign fundraising ($550K, $175K from GOP) — but that was a **losing** campaign. She holds no office in 2026.

**Why she's over-ranked:** The graph gives her a veto bonus (+0.06) and ranks her #18, above the Sheriff's own council members and above the Prosecutor's office. A former candidate who lost and holds no office should not outrank sitting elected officials.

**Action: RE-RANK.** Chambers should drop out of the top 25 (to roughly #30-40). She is a party donor-network figure, not a current power holder. The veto bonus for her should be removed.

---

## E. THE 0.000 NODES — CONFIRMED ERROR (disconnected placeholders)

**Suspected problem:** 10 nodes at 0.000 power.

**Verdict: CONFIRMED ERROR — they are disconnected placeholders, and several should NOT be at 0.000.**

**Evidence (from the graph's own embedded data):** All 10 zero nodes have **zero connections**:
- Central Pierce Fire, Columbia Bank, KNKX, iHeartMedia, Audacy, Lotus, Bethel SD, Catholic Archdiocese, Life Center, Tacoma Housing Authority — **all 0 connections**.

**The skeptic is right on both counts:**
1. **They're disconnected placeholders** — the audit (`audit-pierce-graph.md`, §2.2) flagged the media→council and Columbia Bank→council edges as **FILLER** ("no documented relationship... padding that inflates Council degree"). The rebuild removed those filler edges, which correctly zeroed the media/bank nodes — but left them in the graph as dead weight.
2. **Several should NOT be 0.000** — they have real, documented power that the graph fails to connect:
   - **Columbia Bank** — the largest bank headquartered in the Northwest (Tacoma HQ, per columbiabankingsystem.com). It's a growth-machine actor (evidence/19, /27). It should connect to the Chamber, developers, and county. 0.000 is wrong.
   - **Catholic Archdiocese** — the audit flagged the `catholic-archdiocese → vmfh (owns)` edge as WRONG (VMFH is owned by CommonSpirit, not the Archdiocese), but the Archdiocese still has real institutional presence (evidence/13). It should connect to VMFH via religious sponsorship, not 0.000.
   - **Tacoma Housing Authority** — the audit calls it "the primary vehicle for reshaping Tacoma's physical and demographic landscape" (evidence/13). It should connect to the city, county, and developers. 0.000 is wrong.
   - **Bethel SD** — a major south-county school district (evidence/17). It should connect to the county and its board. 0.000 is wrong.

**Action:**
- **REMOVE** the pure media placeholders (KNKX, iHeartMedia, Audacy, Lotus) — they have no documented power relationship and are dead weight. (Or connect them to the county via advertising/coverage if evidence supports it.)
- **CONNECT** Columbia Bank, Catholic Archdiocese, Tacoma Housing Authority, Bethel SD, Central Pierce Fire, Life Center to their real counterparts so they score >0.
- **DO NOT** leave any node at 0.000 — a node in the map at 0.000 is either a lazy placeholder or a broken measurement.

---

## F. MISSING HIGH-POWER ACTORS — CONFIRMED ERROR (several missing/under-ranked)

**Suspected problem:** Actors who should be in the top 25 are missing or under-ranked.

**Verdict: CONFIRMED ERROR.** The most glaring case is the **Tacoma Mayor at #147 (0.008)**.

**Evidence:**

1. **Tacoma Mayor Anders Ibsen — #147 (0.008) — GROSSLY UNDER-RANKED.** He is the mayor of Tacoma, a city of ~220,000 (the county's largest city, ~1/3 of county population). He was sworn in Jan 2026 (tacoma.gov). The graph gives him **1 connection** (metro-parks, "mayor"). The power matrix ranks him #16 (4.5) and #24 (3.5). A mayor of the county's dominant city at #147, below the Tacoma School Board President, is indefensible. **He should be in the top 25.**

2. **The Prosecuting Attorney as an institution** — Mary Robnett is #14 (0.135), which is defensible, but the graph treats her as a person only. The PA's office controls all felony prosecutions and civil advice to the county (evidence/01). Her rank is OK but the office's institutional power is underweighted.

3. **Federal judges** — The Western District of Washington has a Tacoma courthouse with multiple district judges (Estudillo, Bryan, Cartwright, Evanson, Settle, Christel, Fricke, Leupold — wawd.uscourts.gov). The graph has only Superior Court, District Court, Court of Appeals, and one Superior Court judge (Rumbaugh). **No federal judge node exists.** Federal judges have enormous power over county matters (habeas, civil rights, federal cases). **MISSING.**

4. **Boeing (Frederickson)** — Boeing's Frederickson fabrication site employs ~1,600 and is a top-10 private employer (evidence/19, EDB). It's on the Chamber board (Rich White, evidence/14). **The graph has no Boeing node** — only "Rich White" is absent too. **MISSING.**

5. **The county's biggest private employers** — Per ESD/EDB data: MultiCare, CHI Franciscan (VMFH), State Farm, Boeing, DaVita, Milgard, Kaiser Permanente. The graph has MultiCare and VMFH but **no State Farm, DaVita, Milgard, or Kaiser**. Several are major employers with political presence. **MISSING (at least Milgard, Kaiser).**

6. **Sound Transit CEO** — Sound Transit is a node (#73, 0.034) but the CEO (Goran Sparrman, interim) is not. Sound Transit is building light rail through Pierce County. The CEO is a regional power. **MISSING** (minor).

7. **UW Tacoma Chancellor** — Sheila Edwards Lange is a node (#121, 0.015) and UW Tacoma is #32 (0.060). Both are present but **under-ranked** — UW Tacoma is driving the "Tacoma Revival" narrative and a $115M expansion (evidence/23). Chancellor Lange at #121 is too low.

8. **The county's biggest banks** — Columbia Bank is at 0.000 (see E). KeyBank (Jimmy Ng on Chamber board, evidence/14) is **MISSING entirely**. Banks are growth-machine actors (evidence/27).

9. **The county's top vendors** — The audit notes the county's top contractors (Kiewit, BnBuilders, Skanska, Absher, Korsmo) are unmapped. **MISSING.**

**Action: ADD NODE** for the Tacoma Mayor (re-rank into top 25), federal judges, Boeing, Milgard/Kaiser, KeyBank, and top vendors. **RE-RANK** UW Tacoma and Chancellor Lange upward.

---

## G. THE COMPOSITE SCORE ITSELF — CONFIRMED ERROR (measures connectedness, not power)

**Suspected problem:** The 35/25/20/20 centrality blend measures connectedness, not power.

**Verdict: CONFIRMED ERROR — and the investigation's own documents admit it.**

**Evidence:**
- The methodology (`26-power-methodology.md`, §Limitations) concedes: *"The composite score measures structural/network power — it reflects position in the mapped network, not necessarily real-world impact... This is a measurement aid, not a verdict."*
- The audit (`audit-pierce-graph.md`, §3) is blunt: *"The composite is a network-centrality measure, not a power measure. It systematically over-ranks hubs (Council, party nodes, courts) and under-ranks veto/structural actors (Tribe, JBLM, Sheriff, Chamber, interlock nodes)."*
- The red-team report (`red-team-report.md`) repeats: *"Do NOT use the raw composite as the final ranking."*
- The power theory review (`27-power-theory-review.md`, §2.1) states the core problem: *"Our composite score underweights veto power because it's network-based (centrality), not veto-based."*

**The veto bonus is too small and mis-targeted:**
- The build script's `VETO_BONUS` adds: Tribe +0.18, JBLM +0.16, Chamber +0.14, Swank +0.10, Robnett +0.08, MultiCare +0.06, Lawver +0.10, Wiborg +0.08, Ponepinto +0.08, Pierson +0.10, Chambers +0.06, McCarthy +0.06, News Tribune +0.05, McFarlane +0.05, Sterud +0.05.
- **Result:** Tribe = 0.356 (#4), JBLM = 0.297 (#5), Chamber = 0.403 (#2). These are better than the raw composite, but **still below the Council's 1.000** and **below where the evidence puts them** (Tribe #3, JBLM #5 per /12).
- **The veto bonus is additive to a 0-1 scale but the Council's raw centrality is 1.000** — so no additive bonus can ever lift the Tribe/JBLM/Chamber above the Council. The bonus is structurally incapable of fixing the over-ranking.
- **The Sheriff is still under-ranked** at #9 (0.166) despite a +0.10 veto bonus. /12 ranks him #7. His power is legal autonomy (he cannot be fired, controls $406M), which centrality can't capture.
- **The Chamber at #2 is defensible** (the audit and /13 score it CRITICAL), but it should not outrank the Tribe (#3) and JBLM (#5) on raw power.

**The deeper problem:** A centrality score rewards **how many connections** an actor has, not **how much power they can exercise**. The Council has 61 connections because it's the hub of every government relationship — but a 7-member body that must vote, can be overridden by the Executive's veto, and is checked by the courts is not the most powerful actor in the county. The Tribe can opt out of county jurisdiction entirely (sovereignty); JBLM can leave; the Sheriff can't be fired. None of that shows up as centrality.

**Action: RE-RANK using the evidence/12 qualitative matrix as the primary ranking, with the composite as a secondary network measure.** Add a real veto-power dimension (not an additive bonus) that can lift veto actors above hubs. The current composite should be labeled "network centrality," not "power."

---

## CORRECTED TOP 25 (proposed, per evidence/12 + audit + primary sources)

| New Rank | Actor | Old Rank | Change |
|----------|-------|----------|--------|
| 1 | Ryan Mello (Exec) | 6 | ▲ |
| 2 | Pierce County Council | 1 | ▼ |
| 3 | Puyallup Tribe | 4 | ▲ |
| 4 | MultiCare | 3 | ▼ |
| 5 | JBLM | 5 | — |
| 6 | Chamber of Commerce | 2 | ▼ |
| 7 | Port of Tacoma | 7 | — |
| 8 | Keith Swank (Sheriff) | 9 | ▲ |
| 9 | Mary Robnett (Prosecutor) | 14 | ▲ |
| 10 | Jani Hitchen (Council Chair) | 26 | ▲ |
| 11 | John Wiborg | 10 | ▼ |
| 12 | John McCarthy | 21 | ▲ |
| 13 | Pierce GOP | 15 | ▼ |
| 14 | Pierce Dems | 8 | ▼ |
| 15 | News Tribune | 27 | ▲ |
| 16 | Anders Ibsen (Tacoma Mayor) | 147 | ▲▲▲ |
| 17 | Bruce Dammeier | 55 | ▲ |
| 18 | Amy Cruver | 29 | ▲ |
| 19 | Drew Stokesbary | 61 | ▲ |
| 20 | Tim Reynon | 108 | ▲ |
| 21 | LTG McFarlane | 28 | ▲ |
| 22 | Bill Sterud | 24 | ▲ |
| 23 | Dona Ponepinto | 12 | ▼ |
| 24 | Nathe Lawver | 13 | ▼ |
| 25 | Gordon Thomas Honeywell | 53 | ▲ |

**Removed from top 25:** Kelly Chambers (#18 → out, holds no office), Rosie Ayala (#19 → ~#30, council member), PCCLC (#20 → ~#25), Pierce Transit (#22 → ~#28), GTCF (#23 → ~#30), Weyerhaeuser (#25 → ~#35, historical power, weak current political giving per /27).

---

## SUMMARY OF ACTIONS

| Section | Verdict | Action |
|---------|---------|--------|
| A. Council #1 (1.000) | CONFIRMED ERROR | RE-RANK: Mello #1, Council #2 |
| B. Mystery individuals | DEFENSIBLE (all real) | NO CHANGE to ranks; ADD missing interlock edges |
| C. Party nodes | CONFIRMED ERROR | RE-RANK: cap party nodes at ~0.12, below elected officials |
| D. Kelly Chambers | CONFIRMED ERROR | RE-RANK: out of top 25 (holds no office, lost 2024) |
| E. 0.000 nodes | CONFIRMED ERROR | REMOVE media placeholders; CONNECT Columbia Bank, Archdiocese, THA, Bethel SD |
| F. Missing actors | CONFIRMED ERROR | ADD: Tacoma Mayor (→top 25), federal judges, Boeing, Milgard/Kaiser, KeyBank, vendors |
| G. Composite score | CONFIRMED ERROR | RE-RANK using evidence/12 matrix; add real veto-power dimension |

**Bottom line:** The graph's ranking is a network-centrality measure that the investigation's own audit, red-team report, and power-theory review all explicitly reject as a power ranking. The rebuild's veto bonus and party cap were insufficient to fix the over-ranking of hubs (Council, party nodes) and under-ranking of veto actors (Tribe, JBLM, Sheriff) and the Tacoma Mayor. **The graph contradicts its own guided-mission text**, which says Mello is #1 and Council #2. The ranking must be corrected before it is used as the investigation's bottom line.
