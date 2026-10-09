# 2608-lakewood-council (INV-2026-001)

**Title:** `2026-08-16: Lakewood City Council Investigation`  
**Case ID:** INV-2026-001  
**Status:** Active — Phase 3 (Evidence → Conflict Analysis → Social Audit)

---

Public-records investigation into potential conflicts of interest among all
seven Lakewood City Council members.

## Repo Layout

```
/
├── README.md
├── .gitignore
├── 2608-lakewood-council.md                    ← Master case file (canonical)
├── 2608-lakewood-council-update.md             ← Detailed findings report
├── 2608-lakewood-council-social.md             ← Social-media footprint analysis
├── lakewood-council-citation-verification.md   ← Citation audit
├── lakewood-council-ethics-code-review.md      ← Ethics framework review
├── lakewood-council-phase2-summary.md          ← Executive summary
└── evidence/
    └── cityoflakewood.us-73a260312f.md         ← Raw web cache
```

## Git Workflow

| Layer | Path |
|-------|------|
| **Bare repo (canonical)** | `~/.investigations/repos/2608-lakewood-council.git` |
| **Worktree (edit here)** | `~/Documents/Investigations/2608-lakewood-council/` |
| **Hermes symlink** | `~/.hermes/profiles/investigative-journalist/cases/` |

### After every session

```bash
cd ~/Documents/Investigations/2608-lakewood-council
git add -A && git commit -m "<summary>" && git push origin main
```

## Findings

- 4 of 7 council members have significant conflicts of interest
- Ethics code lacks explicit recusal requirements
- Dual-employment and real-estate conflicts persist unchecked
