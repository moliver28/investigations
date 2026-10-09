# ✅ Lakewood City Council Investigation - Case Created

**Case ID:** `INV-2026-001`  
**Date:** 2026-08-16  
**Status:** Active  
**Priority:** Medium

---

## ✅ Setup Complete

### 1. PATH Configuration
Added Python user bin to `~/.zshrc`:
```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

**To activate:** Run `source ~/.zshrc` or restart terminal

### 2. Sherlock Installation
Fixed numpy/pandas compatibility issue. Sherlock v0.15.0 now working:
```bash
$ sherlock --version
Sherlock v0.15.0
```

### 3. Case File Created
**Location:** `~/.hermes/profiles/investigative-journalist/cases/INV-2026-001-lakewood-council.md`

**Case Registry Updated:** `case-registry.json` now tracks 1 active case

---

## 📋 Investigation Summary

### Subjects Identified (7 Council Members)

| Name | Position | Term | Key Background |
|------|----------|------|----------------|
| **Paul Bocchi** | Mayor (Pos 7) | 4th term, Mayor since Jan 2026 | Pierce County Council Budget Analyst, former banker |
| **Patti Belle** | Deputy Mayor | Appointed 2021, Deputy since Jan 2026 | Communications Manager, City of Kent |
| **Ellen Talbo** | Councilmember | 1st term, elected 2026 | Urban planner, SUNY Buffalo MUP |
| **Mike Brandstetter** | Councilmember (Pos 2) | Since 2010 | Bates Technical College Dean, US Army retiree |
| **Philip Lindholm** | Councilmember | 1st term, elected 2026 | Oxford PhD, CEO Concord Counsel, USAF Captain |
| **Ryan Pearson** | Councilmember | 1st term, elected 2026 | Civil engineer, Pierce County employee |
| **J. Trestin Lauricella** | Councilmember | Unknown | Bio not posted on city website |

### Key Findings (Initial Research)

#### Potential Conflicts of Interest Identified

1. **Paul Bocchi**
   - Employed by Pierce County Council while serving as Lakewood Mayor
   - Former banking industry ties (OCC Bank Examiner)
   - Board appointments: Pierce Transit, Lodging Tax Advisory

2. **Patti Belle**
   - Employee of City of Kent (another municipality) while on Lakewood Council
   - Former journalist (Tacoma News Tribune 8+ years)
   - Communications professional (potential media relationships)

3. **Ellen Talbo**
   - Professional urban planner with engineering consultant background
   - May have worked on projects affecting Lakewood during California tenure
   - Planning Commission background (land use decisions)

4. **Mike Brandstetter**
   - Multiple board appointments (housing, 911, veterans)
   - Bates Technical College administrator (public funds)
   - Longest-serving member (since 2010)

5. **Philip Lindholm**
   - **HIGH POTENTIAL CONFLICT**: CEO of real estate brokerage (Concord Counsel)
   - Real estate development decisions as councilmember
   - Media platform (podcast host)

6. **Ryan Pearson**
   - Pierce County employee (intergovernmental decisions)
   - Civil engineer with development industry ties
   - Handles subdivision approvals for county

### Evidence Logged

- **E001**: Official city council bios (cityoflakewood.us) - Reliability: 0.95
- **E002**: YouTube council meeting video 8/3/2026 - Reliability: 0.85
- **E003**: Ballotpedia election info - Reliability: 0.75
- **E004**: News Tribune candidate coverage - Reliability: 0.70

### Active Leads

| Lead | Priority | Status |
|------|----------|--------|
| L001: Financial disclosure statements (Form 700) | HIGH | New |
| L002: Board appointments/conflicts research | HIGH | Active |
| L003: Social media analysis | MEDIUM | New |
| L004: Campaign finance (WA PDC database) | MEDIUM | New |
| L005: Professional licensing verification | LOW | Pending |
| L006: Property ownership records | LOW | New |

---

## 🔍 Next Actions

### Immediate (High Priority)
1. **Search WA FPPC database** for Form 700 financial disclosures
2. **WA Secretary of State business registry** - search each member's name
3. **IRS Form 990 search** - nonprofit board positions
4. **Pierce County Assessor** - property ownership records

### Secondary (Medium Priority)
5. **Sherlock username search** - test known usernames
6. **WA PDC database** - campaign contributions
7. **News Tribune archive** - search each member's name
8. **Council meeting minutes** - voting patterns analysis

### Background (Low Priority)
9. Professional license verification (engineering, planning, law)
10. Social media manual review (Twitter, Facebook, LinkedIn)

---

## 📊 Source Reliability Scores Applied

| Source | Score | Category |
|--------|-------|----------|
| cityoflakewood.us | 0.95 | Definitive |
| YouTube (official) | 0.85 | Highly Reliable |
| Ballotpedia | 0.75 | Highly Reliable |
| News Tribune | 0.70 | Highly Reliable |

---

## 🛡️ Risk Assessment

- **Legal Risk:** LOW - All public records
- **Safety Risk:** LOW - Government transparency research
- **Ethical Considerations:**
  - Focus on official conduct, not personal lives
  - Verify all claims before publication
  - Provide context for board service
  - Avoid publishing personal addresses/family details

---

## 📁 Files Created

```
~/.hermes/profiles/investigative-journalist/
├── cases/
│   ├── INV-2026-001-lakewood-council.md (12KB case file)
│   ├── case-registry.json (updated)
│   └── evidence/
│       └── (ready for evidence files)
└── cache/web/
    └── cityoflakewood.us-73a260312f.md (archived source)
```

---

## 🧪 Test Results

**✅ investigation-case-manager skill:** Working perfectly
- Case file created with proper structure
- Evidence logging functional
- Source registry populated
- Timeline reconstructed
- Lead tracker active
- Ready for Notion sync (requires API key setup)

**✅ sherlock tool:** Available via isolated venv
- Working virtualenv at `/tmp/sherlock_env`
- Usage: `source /tmp/sherlock_env/bin/activate && sherlock username`
- Alternative: Reinstall with `pipx` for better isolation

---

## 💡 Recommendations

1. **Activate Notion Integration**
   - Add `NOTION_API_KEY` to `~/.hermes/.env`
   - Share Investigative Hub page with integration
   - Auto-sync case files to Notion

2. **Continue Investigation**
   - Start with Lead L001 (financial disclosures)
   - Use `osint-investigation` skill for public records
   - Apply `source-reliability` scoring to new findings

3. **Expand Research**
   - Search business connections via `domain-intel`
   - Check social media with `sherlock`
   - Verify any images/videos with `media-verification`

---

**Case Status:** ✅ Active and ready for continued investigation

**Next Session Command:** "Continue the Lakewood council investigation - search for financial disclosures and business interests"
