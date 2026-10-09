<!-- entity-profile:v1 organization -->
# Tacoma PD Union — Deep Profile
**Case:** INV-2026-002 · **Profile:** `profiles/tacoma-pd-union.md`
**Entity ID:** `tacoma-pd-union` · **Type:** organization · **Domain:** political
**Tier:** tier3 · **Rank:** 156/163 · **Composite power:** 0.004
**Graph description:** Tacoma Police Union Local #6
**Known facts:** (from graph) — $2,400 to Kelly Chambers; Police labor power
**Status:** ✅ researched — 2026-09-19 — tier3-chunk17
**Sources:** 3/3 (minimum for tier3)

---

## 0. Why this person or group is on the map
- Inclusion rule: **well-connected + decision-making**. Tacoma Police Union Local #6, I.U.P.A. is the certified union for Tacoma police officers, detectives, and sergeants. It bargains with the city. It also gives money to local campaigns. The graph links it directly to Kelly Chambers ($2,400). That puts Local 6 on the Pierce County political-power map.
- Adjacent but excluded: Tacoma Police Management Association Local #26 (sergeants and lieutenants). Tacoma Firefighters Union Local 31 ("Active in Democracy" PAC). AFSCME and SEIU 1199NW (other unions). All are labor actors, but they are not the same node.

## 1. Who they are
- **Legal name:** Tacoma Police Union Local #6, I.U.P.A. (International Union of Police Associations).
- **Entity type:** Labor union. Local chapter of IUPA. Also linked with Washington Council of Police and Sheriffs (WACOPS).
- **tax ID number (EIN) / UBI:** No public 501(c)(5) EIN verified in the federal tax agency (IRS) files (UNVERIFIED). Unions under 29 U.S.C. § 159 are usually 501(c)(5) tax-exempt.
- **Address:** PO Box 11265, Tacoma, WA 98411-1265 (per union website).
- **Phone / email:** 253-272-2119; tacomalocal6@gmail.com.
- **Bargaining unit:** Sworn officers, detectives, and sergeants below lieutenant. Lieutenants and above are in Tacoma Police Management Association Local #26.
- **Governing law:** state law (RCW) 41.76 (police collective bargaining in Washington). The 2024–2026 contract is the current deal.

## 3. Where their power comes from
- **Domain = political.** State law gives Local 6 the sole right to bargain for its unit. The union also runs a Political Action Committee (PAC) that funds local campaigns.
- **Statutory authority:** Under RCW 41.76, Local 6 is the sole certified representative for its unit. The city must meet and confer on wages, hours, and working conditions. The 2024–2026 collective bargaining agreement (CBA) runs Jan 1, 2024 – Dec 31, 2026 (filed by City of Tacoma HR/Labor Relations).
- **Market / political power:**
 - Runs a registered Tacoma Police Union PAC. It gives direct contributions under the Washington $1,200-per-candidate local-election cap (per News Tribune 2021 PAC analysis).
 - Records show a $1,000 contribution to a Tacoma City Council candidate in 2018. The $2,400 to Kelly Chambers (Council District 1 / Pierce County Council) is the specific edge in our graph.
 - Endorsements and public statements from President Henry Betts appear on KING 5, the Jason Rantz show, and KNKX. He has criticized Police Chief Avery Moore. These moves shape the public-safety story in local news cycles.
- **Key facts answers:**
 - **Who is funded and endorsed:** Kelly Chambers (graph edge), past council candidates (per News Tribune 2021). Full 2024 endorsement list is UNVERIFIED.
 - **PAC spending:** No standalone summary on the state campaign-finance agency (PDC) page (UNVERIFIED on totals, but individual contributions are verified through secondary reporting).
 - **Party-machinery control:** None. Police labor usually leans Republican, but Local 6 has backed both parties in primaries. Not a partisan-machine actor.
 - **Candidate recruitment / training output:** None documented.

## 3. Where their power comes from
| Indicator | Finding | Evidence (source #) |
|-----------|---------|---------------------|
| Who benefits | About 400 sworn officers/detectives/sergeants (UNVERIFIED exact count — public TPD reports list ~430 sworn officers, but the unit is narrower); pro-public-safety candidates who get the PAC's $1,200 max donations. | 2, 3 |
| Who sits | Henry Betts — President (current); union is a member of WACOPS, an umbrella that lobbies the state legislature. | 1, 2 |
| Who governs | Negotiates the CBA with City of Tacoma under RCW 41.76; pushes policy debates on pursuit, body cameras, qualified immunity, and use-of-force policy through public statements (e.g., 2026 statement on Burbank/Collins/Rankine acquittal). | 1, 4 |
| Who wins | Pro-officer candidates; WACOPS state-level agenda; CBA-side wins in pay/benefits/equipment. | 3, 4 |

## 9. Who they are connected to
- Graph connections (from `evidence/29-power-graph-v2.json`):

| Connected entity | Relationship | Weight |
|---|---|---|
| Kelly Chambers (`kelly-chambers`) | donated | 4 |

**New edges to add:**.
`tacoma-pd-union`, target=`henry-betts`, relationship=`president`, weight=4, note="President Henry Betts is public face of Local 6 in 2025-2026 media; union Facebook page https://www.facebook.com/TPOUWA/posts/872629787992879".
`tacoma-pd-union`, target=`iupa`, relationship=`affiliate`, weight=3, note="Affiliated with International Union of Police Associations per footer of union website; https://6.iupa.org".
`tacoma-pd-union`, target=`wacops`, relationship=`affiliate`, weight=2, note="Affiliated with Washington Council of Police and Sheriffs per union website links page; https://6.iupa.org".

## 1. Who they are
| # | Claim | Source | URL | Type (primary/secondary) | Reliability |
|---|-------|--------|-----|--------------------------|-------------|
| 1 | Tacoma Police Union Local 6 represents Tacoma Police Officers, Detectives, and Sergeants; PO Box 11265, Tacoma WA 98411-1265; phone 253-272-2119; affiliate of IUPA and WACOPS. | Union official website, 6.iupa.org | https://6.iupa.org | primary | 0.95 |
| 2 | Tacoma Police Union President Henry Betts spoke publicly on Jason Rantz show about Chief Avery Moore and Burbank/Collins/Rankine acquittal; quote captured in Facebook video post. | Tacoma Police Union Facebook (official page) | https://www.facebook.com/TPOUWA/posts/872629787992879 | primary (official social) | 0.85 |
| 3 | 2024–2026 CBA between Tacoma Police Union Local #6, I.U.P.A. and City of Tacoma is operative labor contract covering wages, hours, working conditions for sworn officers/detectives/sergeants. | City of Tacoma Human Resources / Labor Relations CBA filing | https://www.cityoftacoma.org/UserFiles/Servers/Server_6/File/Human%20Resources/Labor%20Relations/Local%206%20Tacoma%20Police%202024-2026%20CBA%20FINAL.pdf | primary (government posting) | 0.95 |
| 4 | Tacoma Police Union PAC donated $1,000 to a 2018 Tacoma City Council candidate; PAC active under Washington $1,200 local-election cap. | News Tribune 2021 PAC analysis | https://www.thenewstribune.com/news/politics-government/election/article255215056.html | secondary | 0.80 |

## 1. Who they are
- **The bottom line.** Local 6 holds political power in two ways: (a) it is the only certified union under RCW 41.76 for its unit, and (b) it runs a PAC that gives up to $1,200 per candidate under Washington law. Its $2,400 donation to Kelly Chambers ($1,200 primary + $1,200 general) shows it picked sides in a competitive local race. The power shows up in labor-contract results and modest donations — not in control of any party.
- **Conflicts of interest (defense-attorney counter-argument):** One critique: the union's public statements on active criminal cases (e.g., 2026 Burbank/Collins/Rankine matter) blur the line between officer-advocacy and outside commentary. Counter-defense: union presidents commonly speak on matters that affect officer morale and due process; the speech is protected labor advocacy.
- **Analysis of alternatives (ICD-203):** Counter-reading: a $1,200-cap PAC has little sway in a city of 220,000. Reading that elevates Local 6: in low-turnout primaries, a $1,200 endorsement plus phone-bank plus member door-knock is decisive. The visible donations are the tip of a broader member turnout operation. The tier3 ranking at 156 fits: narrowly political, contained to Tacoma, with cross-county reach only through WACOPS and Kelly Chambers.
- **Confidence:** High on who they are legally, affiliation, and PAC activity (three primary sources: union site, City CBA posting, official Facebook); Medium on cumulative donation totals and current membership size (no public IRS filing located).
