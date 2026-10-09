<!-- entity-profile:v1 organization -->
# U.S. District Court, Western District of Washington — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/federal-district-court.md`
**Entity ID:** `federal-district-court` · **Type:** organization · **Domain:** legal
**Tier:** tier3 · **Rank:** 99/163 · **Composite power:** 0.020
**Graph description:** U.S. District Court for the Western District of Washington (WDWA). Article III federal trial court. 7 active district judgeships + 6 magistrate judges. Courthouses in Seattle and Tacoma (Union Station, 1717 Pacific Avenue, Room 3100).
**Known facts:** Established 1905; 7 active judgeships (all filled as of 2026); Chief Judge David G. Estudillo (appointed Biden 2021); U.S. Attorney Neil Floyd (interim); Tacoma courthouse at Union Station serves Pierce County federal caseload.
**Status:** ✅ researched — 2026-09-19 — tier3-chunk5 · **Last updated:** 2026-09-19
**Sources:** 5/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- **Why included:** Holds office + makes decisions — The U.S. District Court for the Western District of Washington is the only federal trial court with jurisdiction over Pierce County. Federal criminal cases, federal civil rights actions, habeas petitions (prisoners asking a federal court to review their state conviction), RICO and FCA cases, and federal-question diversity cases all go through WDWA. The Tacoma courthouse sits in Union Station. It handles criminal and civil cases from the southern district (Pierce, Lewis, Mason, Thurston, Clark, Skamania, Cowlitz, Wahkiakum, and Pacific counties). (Sources 1, 2, 4)
- **Adjacent but NOT included:** U.S. Bankruptcy Court for WDWA (separate court, related but different job). Washington State Superior Court (state court — handles most criminal and civil matters in Pierce County). U.S. Court of Appeals for the Ninth Circuit (hears appeals from WDWA — separate court). U.S. District Court for the Eastern District of Washington (covers eastern WA). U.S. Attorney's Office WDWA (this is the prosecutor, not the court).

## 1. Who they are
- **Legal name:** United States District Court for the Western District of Washington. (Sources 1, 2, 4)
- **Type:** Federal Article III trial court. Established under Article III of the U.S. Constitution and 28 U.S.C. § 81 (the law that creates federal district courts). 28 U.S.C. § 132 reorganized WDWA into 7 seats. (Sources 1, 2)
- **When it was set up:** First set up March 2, 1905. Reorganized over time — 1938 (3 seats), 1961 (5 seats), 1978 (6 seats), 1984 (7 seats, 1 temporary), 1990 (7 permanent). (Source 1)
- **Where it reaches:** Western Washington — 19 counties west of the Cascades. Main courthouse is Seattle. There are also courthouses in Tacoma (Union Station) and Mount Vernon. (Sources 1, 2)
- **Tacoma courthouse:** U.S. District Court, Clerk's Office, 1717 Pacific Avenue, Room 3100, Tacoma, WA 98402-3200. Phone (253) 882-3800. The public lobby is open weekdays 7 AM–5 PM. Closed on federal holidays. You do NOT need a REAL ID to enter. (Source 2)
- **Chief Judge (2026):** David G. Estudillo. Appointed by President Biden in 2021. Took office October 7, 2021. Has been Chief Judge since 2022. Born 1973. He was previously a Pierce County Superior Court judge and U.S. Attorney WDWA. (Sources 1, 3, 4)
- **Clerk of Court / District Court Executive:** Joshua C. Lewis. (Source 2)
- **U.S. Attorney WDWA:** Neil Floyd (interim). (Source 1)
- **Judgeships allowed:** 7. All are filled, with no vacancies as of 2026. (Source 1)
- **Who appointed them:** The active judges are mostly Biden appointees. The senior judges were appointed during the Reagan, Clinton, and G.W. Bush presidencies.

## 3. Where their power comes from
- **Federal judicial power (legal side):** It is the only federal trial court for Pierce County. It has original (first-hearing) power over federal criminal matters (FBI, DEA, and ATF prosecutions; federal civil rights; RICO; drug trafficking; public corruption). It also handles federal civil cases (civil rights, antitrust, environmental enforcement, FCA qui tam (whistleblower lawsuits under the False Claims Act), immigration habeas, federal tort claims), and diversity cases (cases between citizens of different states) where the amount in dispute is over $75,000. (Source 4)
- **Constitutional rulings:** The court issues binding rulings on constitutional questions. For example, recent WDWA rulings have addressed First Amendment rights tied to Pierce County Sheriff Keith Swank. (Source 5)
- **Appeals:** Cases from WDWA go to the U.S. Court of Appeals for the Ninth Circuit, based in San Francisco. The Ninth Circuit hears oral arguments at the Pioneer Federal Courthouse in Portland, Oregon. (Source 1)
- **Where power crosses domains:** Legal (Article III trial court) + government (Pierce County federal caseload) + institutional (review of federal agency actions within Pierce County).
- **Caseload stats (general federal):** National U.S. District Courts civil cases filed in FY2025: 271,802 (down 21.9% from the year before). Criminal defendants filed: 73,644 (up 11.5%). WDWA-specific 2024 case numbers were not found in tabular form. (Source 6)

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | Pierce County residents who need federal help (civil rights, habeas, FCA, civil antitrust). Federal defendants facing prosecution. Civil parties in diversity cases. | 1, 4 |
| Who sits | 7 active district judges (most active judges were appointed by Biden). Plus 11 senior judges. Plus 6 full-time magistrate judges. Plus 1 recalled and 1 part-time. Clerk of Court Joshua C. Lewis. | 1, 2, 3 |
| Who governs | Active judges rotate through criminal and civil calendars. Senior judges handle smaller caseloads. Magistrate judges handle pretrial matters, petty offenses, and civil consent cases under 28 U.S.C. § 636(c). | 2, 4 |
| Who wins | The federal government and federal civil rights plaintiffs (when they file in WDWA). The Tacoma legal community has a busy federal practice anchored at Union Station. | 1, 2 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Keith Swank (`keith-swank`) | federal_cases | 3 |
| Prosecuting Attorney's Office (`pa-office`) | federal_cases | 3 |
| Superior Court (`superior-court`) | federal_oversight | 3 |

- 
`federal-district-court`, target=`keith-swank`, relationship=swank_attorney_first_amendment_ruling, weight=3, note="https://www.thenewstribune.com/news/local/article314068855.html".
`federal-district-court`, target=`ninth-circuit`, relationship=appellate_path, weight=4, note="https://ballotpedia.org/United_States_District_Court_for_the_Western_District_of_Washington".
`federal-district-court`, target=`pierce-county`, relationship=exclusive_federal_jurisdiction, weight=5, note="https://www.wawd.uscourts.gov/visitors/tacoma-courthouse".
`federal-district-court`, target=`us-attorney-wdwa`, relationship=prosecution_function, weight=4, note="https://en.wikipedia.org/wiki/United_States_District_Court_for_the_Western_District_of_Washington".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | WDWA: 7 active Article III judgeships (Biden-appointed bench); 11 senior judges; 6 full-time magistrate judges; established 1905; statutory reorganization through 1990; appeals to 9th Circuit (Portland) | Ballotpedia — U.S. District Court for WDWA | https://ballotpedia.org/United_States_District_Court_for_the_Western_District_of_Washington | secondary | 0.95 |
| 2 | Tacoma Courthouse: 1717 Pacific Avenue Room 3100 Tacoma WA 98402; phone (253) 882-3800; lobby hours; Chief Judge David G. Estudillo; Clerk of Court Joshua C. Lewis | U.S. District Court WDWA official (Tacoma Courthouse page) | https://www.wawd.uscourts.gov/visitors/tacoma-courthouse | primary | 1.0 |
| 3 | Court Directory listing 17 district judges + 8 magistrate judges' chambers with phone numbers; Tacoma chambers at (253) 882-XXXX | U.S. District Court WDWA official (Court Directory) | https://www.wawd.uscourts.gov/about/directory | primary | 1.0 |
| 4 | WDWA active judges list: Tiffany Cartwright, John Chun, David G. Estudillo, Kymberly Evanson, Lauren King, Tana Lin, Jamal Whitehead; senior: Bryan, Coughenour, Dimmick, Jones, Lasnik, Martinez, Pechman, Robart, Rothstein, Settle, Zilly | U.S. District Court WDWA official (Judges page) | https://www.wawd.uscourts.gov/judges | primary | 1.0 |
| 5 | Sheriff Keith Swank's would-be private attorney lost First Amendment ruling in U.S. District Court (likely WDWA Tacoma) Dec 31; Swank separately faces WA Assn of Sheriffs and Police Chiefs expulsion over legislative testimony Jan 2026 | The News Tribune | https://www.thenewstribune.com/news/local/article314068855.html | secondary | 0.90 |
| 6 | Federal judicial caseload stats FY2025: U.S. District Courts civil 271,802 filed (-21.9% YoY); criminal defendants 73,644 filed (+11.5% YoY); national aggregate | U.S. Courts — Federal Judicial Caseload Statistics 2025 | https://www.uscourts.gov/data-news/reports/statistical-reports/federal-judicial-caseload-statistics/judicial-caseload-indicators-federal-judicial-caseload-statistics-2025 | primary | 1.0 |

## 1. Who they are
- **Verdict:** The U.S. District Court for the Western District of Washington has exclusive federal judicial power over Pierce County. It works through its Tacoma courthouse at Union Station, 1717 Pacific Avenue. Seven active district judges (appointed by Biden), 11 senior judges, and 6 magistrate judges handle the federal caseload. The Tacoma courthouse processes criminal and civil cases from Pierce, Lewis, Mason, Thurston, Clark, and other southern district counties. Chief Judge David G. Estudillo — former Pierce County Superior Court judge and former U.S. Attorney WDWA — is a known figure in the Pierce County legal community.
- **Conflicts-of-interest flags:** The map edge labeled "federal_oversight" between WDWA and Superior Court is INACCURATE in the strict constitutional sense. WDWA does not exercise appellate "oversight" over Pierce County Superior Court. WDWA has habeas power to review state-court convictions under 28 U.S.C. § 2254, but Superior Court decisions are reviewed by the Washington State Court of Appeals, not WDWA. WDWA and Superior Court run side by side, not in a hierarchy. (FACT — 28 U.S.C. § 2254 limits federal habeas to constitutional issues, not state-court error correction.)
- **Analysis of alternatives:** A defense reading: WDWA is a neutral, life-tenured Article III court. It is bound by statute and binding appellate precedent (9th Circuit, U.S. Supreme Court). An opposing reading: WDWA's bench is overwhelmingly Biden-appointed (all 7 active judges). This affects Pierce County residents on civil rights, immigration, federal criminal sentencing, and federal regulatory challenges. Judge Estudillo's past roles (Pierce County Superior Court judge, U.S. Attorney WDWA) mean he has direct relationships with many Pierce County lawyers and law enforcement figures who now appear before him.
- **Confidence:** High — primary-source confirmation via WDWA official website (Judges, Directory, Tacoma Courthouse) and Ballotpedia roster; news coverage of recent Swank-related rulings. WDWA-specific Pierce County caseload statistics (cases filed/terminated per year from WDWA) require deeper search of uscourts.gov statistical tables and were not retrieved in this research pass.