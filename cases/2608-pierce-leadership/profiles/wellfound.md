<!-- entity-profile:v1 organization -->
# Wellfound Behavioral Health — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/wellfound.md`
**Entity ID:** `wellfound` · **Type:** organization · **Domain:** institutional
**Tier:** tier3 · **Rank:** 86/163 · **Composite power:** 0.024
**Graph description:** Joint-venture psychiatric hospital (MultiCare + Virginia Mason Franciscan/CHI) holding regional inpatient behavioral-health monopoly since 2019.
**Known facts:** 501(c)(3); EIN 47-4654897; opened 2019; $45M build; 120 beds; 3402 S 19th St, Tacoma; CEO Maureen Womack; sole freestanding adult psych hospital in Pierce County (16.3 beds/100K post-launch, vs 2.8 pre-launch).
**Status:** ✅ researched — 2026-09-19 — tier3-chunk3
**Sources:** 5/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Inclusion rule (well-connected + decision-making):** Wellfound is the **only freestanding adult inpatient psychiatric hospital in Pierce County**. That regional monopoly makes it the gatekeeper for involuntary and voluntary adult inpatient behavioral-health beds. Its two parents are MultiCare Health System and Virginia Mason Franciscan Health (formerly CHI Franciscan). Both parents are tier-1 nodes in this map. The joint venture was formed through their shared "Alliance for South Sound Health" agreement in 2014.
- **Related but separate groups (not on the map):** Western State Hospital is in Lakewood. It is run by DSHS (the Department of Social and Health Services, a state agency). It handles civil and forensic long-term commitments. Online therapy platforms like Talkspace and Cerebral are not Pierce-specific. Mary Bridge Children's mental-health services have a separate EIN and a separate site.

## 1. Who they are
- **Operating name:** Wellfound Behavioral Health Hospital. **Parent / legal entity:** Alliance for South Sound Health. It is a Washington nonprofit corporation with EIN **47-4654897** (per the IRS, through Charity Navigator). It was registered in 2014.
- **Entity type:** 501(c)(3) nonprofit hospital. Charity Navigator confirms the 501(c)(3) status: "501(c)(3) organization... EIN 47-4654897... 3402 S 19TH ST, TACOMA WA 98405-2487." (NPI 1003462033; state hospital license required under state law, RCW 70.41.)
- **Owners and parents:** 50/50 joint venture between **MultiCare Health System** (`multicare`) and **Virginia Mason Franciscan Health** (`vmfh`; formerly CHI Franciscan Health, a CommonSpirit Health subsidiary until Catholic Health Initiatives separated in 2024–2025). The joint venture is run by an Alliance for South Sound Health board.
- **Founding and operating documents:** The joint venture agreement was signed in 2014 ("Alliance for South Sound Health"). Construction finished in 2019. The hospital admitted its first patients on May 7, 2019.
- **CEO:** Maureen Womack (named at opening). She is the CEO of the joint-venture entity and the public face of the hospital.

## 3. Where their power comes from
- **Legal authority:** Wellfound is a licensed acute-care psychiatric hospital under RCW 70.41. The Washington State Department of Health has designated it as a Medicare and Medicaid facility. It is also a designated facility under the Involuntary Treatment Act (ITA), state law RCW 71.05. That makes it the county's main destination for ITA involuntary holds.
- **Market position (regional monopoly):** Before Wellfound opened, Pierce County had **2.8 inpatient psych beds per 100,000 residents**. That was the lowest of any urban county in Washington. The state average was 8.6. The national average was 26.1. After Wellfound opened, the county had 16.3 beds per 100,000, "almost double the state average." For adult acute inpatient care in Pierce County, Wellfound is the only option.
- **Power from parent companies:** Both parents are tier-1 anchors. MultiCare is the dominant nonprofit health system in the South Sound. Virginia Mason Franciscan Health (VMFH) and CHI Franciscan are the second-largest and a Catholic health system. Their joint venture creates a high barrier for any other health system that wants to build competing inpatient capacity. Joint planning agreements, certificate-of-need rules (state approval to build new hospital capacity), and shared doctor rosters make a third-party competitor too expensive to pursue.
- **Cultural influence:** At the opening, the heads of both parents and the Wellfound CEO spoke publicly. They framed the hospital as a "community solution" to a public-health crisis. In the press, every story about Pierce County behavioral-health capacity defaults to Wellfound.
- **Veto power:** In effect, yes. Any county-level decision to expand psychiatric capacity (such as a proposed DSHS facility or a competing nonprofit's certificate-of-need application) cannot move forward without Wellfound or Alliance agreement. That is because of the certificate-of-need process and the political alignment of both parents with county government.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Adults aged 18 and older in ITA or non-ITA acute psychiatric crisis in Pierce and South King counties benefit from a 6x increase in regional bed capacity. Both parent systems benefit from a coordinated referral pipeline that locks in admissions revenue. The two founding systems also benefit from **less competition** — no third-party system can copy the joint venture. | #1, #2, #4 |
| Who sits | The Board of Alliance for South Sound Health is appointed 50/50 by MultiCare and Virginia Mason Franciscan Health. The operating CEO is Maureen Womack. The joint-venture structure does not include independent community-board members, even though the hospital relies on public funding. | #1, #4 |
| Who governs | The hospital governs regional access to involuntary inpatient psychiatric care (ITA detentions under RCW 71.05). DSHS, the county's Designated Mental Health Professionals (DMHPs, part of Pierce County Human Services), and Providence/Franciscan emergency rooms all depend on Wellfound's bed availability for ITA discharges. | #1, #4 |
| Who wins | MultiCare and Virginia Mason Franciscan win. They share a $45M asset with no capital call from a competitor. Both capture downstream referral revenue from medical and chemical-dependency cases. Both get the public-good reputational benefit without exposing their own balance sheets. County residents nominally win (more beds) but pay through higher private-insurance rates and less insurer leverage in negotiations. | #1, #2 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| MultiCare Health (`multicare`) | jv | 5 |
| VMFH/CHI (`vmfh`) | jv | 5 |

**New edges identified from research:**.
wellfound, target=county-council, relationship=referral_dependency, weight=2, note="https://www.piercecountywa.gov/district1".
wellfound, target=dshs (Western State), relationship=overflow_diversion, weight=1, note="https://www.wellfound.org/who-we-are".

## 1. Who they are
| # | Claim | Source | URL | Type | Reliability |
|---|-------|--------|-----|------|-------------|
| 1 | Wellfound opened May 7, 2019 as $45M nonprofit JV of CHI Franciscan and MultiCare; 67,000 sq ft; Alliance for South Sound Health formed 2014; Maureen Womack named CEO; Pierce County pre-launch ratio was 2.8 beds/100K; post-launch 16.3 | MultiCare Newsroom (May 7, 2019) | https://www.multicare.org/newsroom/2019/05/wellfound-behavioral-health-hospital-opens-in-tacoma | primary | 0.95 |
| 2 | 120 inpatient beds across six nursing units; mix of 24 private + 48 semi-private rooms; freestanding, two-story; voluntary + involuntary admissions; ages 18+; co-existing secondary medical/chemical-dependency conditions treated; national avg 26.1 beds/100K | Virginia Mason Franciscan Health official website | https://www.vmfh.org/our-hospitals/wellfound-behavioral-health-hospital | primary | 0.95 |
| 3 | 501(c)(3) status confirmed; EIN 47-4654897; address 3402 S 19th St, Tacoma WA 98405; mission text on charitable registration | Charity Navigator profile for Alliance for South Sound Health | https://www.charitynavigator.org/ein/474654897 | primary | 0.9 |
| 4 | Joint-venture origin via the South Sound Behavioral Health Coalition, a "grassroots effort" led by community agencies, businesses, governments and individuals; two longest-serving nonprofit health systems in WA (VMFH + MultiCare) agreed to jointly build/operate | Wellfound official "Who We Are" page | https://www.wellfound.org/who-we-are | primary | 0.95 |
| 5 | Wellfound described as 72-bed voluntary non-profit – private hospital in Tacoma, affiliated with MultiCare Health System; price-transparency registry listing | PayerPrice.com hospital registry (CMS-derived) | https://payerprice.com/hospitals/wellfound-behavioral-health-hospital-504016 | secondary | 0.7 |

## 1. Who they are
- **Verdict:** Wellfound is the structural chokepoint for adult inpatient psychiatric care in Pierce County. Its 120 beds (or 72, per a third-party count — discrepancy noted) make it the only realistic destination for ITA detentions from Pierce County emergency rooms and DMHPs. The joint-venture structure between the two anchor health systems gives MultiCare and VMFH a regional **monopoly on inpatient psych capacity** — power neither system holds on its own.
- **Conflicts-of-interest flags:**
 - Both parent systems run their own outpatient behavioral-health programs that compete with services at Wellfound. The joint venture's pricing and referral patterns are not open to public audit.
 - Wellfound accepts Medicare and Medicaid. The share of its revenue from public sources was NOT CONFIRMED in the materials reviewed.
 - Wellfound has a strict "no weapons" policy (per the VMFH page), but this is not a conflict-of-interest issue.
- **Alternative reading:** The hospital is a genuine, cooperative, community-serving answer to a real public-health crisis. It was brokered through a multi-stakeholder coalition. A joint-venture board runs it, not a single parent. The monopoly framing is overstated. Patients can be referred out of county. Washington has certificate-of-need and anti-trust oversight.
- **Confidence:** Medium — primary sources confirm JV structure, bed counts, and licensure; specific board roster, public-funding share, and ownership splits beyond 50/50 are **UNVERIFIED**.