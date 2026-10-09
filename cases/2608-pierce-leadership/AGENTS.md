# 2608-pierce-leadership — Power Network UI v3 Task Instructions

**Task:** Rebuild the power-network UI as an entity-first interface. Active plan: `.hermes/plans/2026-10-04_115252-power-network-ui-v3.md`. **Read the plan before starting any build step.**

## Context you cannot discover from files
- The deliverable is an **entity-first HTML bundle** at `evidence/network/` — split view (map + sortable directory), full entity pages with ego-networks, 8 canonical relationship classes, tier bands for power. The map is ONE lens, not the product.
- v2 (`evidence/11-power-network.html`) is archived as `11-power-network-v2-archive.html` and stays shippable until v3 passes its gates.
- **Measured v2 failures this rebuild must fix:** drawer covers 100% of the canvas (map unseeable while reading); median click target 16px (WCAG 2.5.5 floor is 24px) because viewBox 2560×1440 scales 0.40×; zero search inputs for 163 entities; exactly 1 media query; 6,784px of profile in a 463px viewport with no section nav.
- Locked decisions: split view · full entity page · folder bundle · normalize relationships in graph data · tier bands headline the score · guided missions kept as the LOWEST-priority integrated layer (content order = mission arc; adds no new surface).
- **Governing priority:** simplest possible nav/architecture and a clean, easy-to-read UI outranks everything else. Nav budget: exactly 3 primary states (split view → entity page → back) + 1 modal; 0 tabs, 0 nested menus, 0 onboarding overlays.

## Rules that change behavior here
1. **Verify, never trust a subagent's completion claim.** Check the file on disk (`ls`, parse it, run the gate) before reporting success or advancing a phase.
2. **Every gate is a command with expected output.** Run it; paste the actual output. If a gate fails, fix the cause — never skip or soften the gate.
3. **Preserve machine-readable profile lines byte-for-byte.** Lines 1–9 of every `profiles/*.md` (including the long `Graph description` and `Known facts` lines, which look like prose but are consumed by scripts) plus `**Confidence:**`, `edge:`, the `## Sources` table, and `(submit)` markers. Verify with `git show HEAD:profiles/X.md | head -9`.
4. **Power scores are network-centrality composites, not settled truth.** Present them as tier bands with the score on demand, always one click from the method note (35% weighted degree + 25% betweenness + 20% eigenvector + 20% PageRank + veto bonus, hub/party caps).
5. **Every entity page must stand alone for a zero-context reader:** tier band visible, acronyms expanded on first use on that page, no "as seen above", no machine syntax (`edge: source=`, `[x]`) in prose.
6. **No CDN, no framework, no network requests.** The bundle must open offline from `file://`.
7. **Run scripts from** `/Users/moliver/.hermes/hermes-agent/venv/bin/python3` **; run them from the repo root** (`~/Documents/Investigations/2608-pierce-leadership`).
8. **8-pt spacing grid, ≥16px body text, 1.6 line-height, 72ch prose measure, WCAG 2.2 AA** (4.5:1 at actual rendered opacity), min 24px node diameter at every supported viewport.

## Success criteria
- `scripts/verify_ui.py` → **12/12 PASS**, output committed.
- Independent adversarial reviewer verdict `pass` or `pass_with_fixes` with every critical/high finding fixed and re-verified.
- A zero-context subagent answers all three comprehension questions (top power + why · the government↔private money relationship · three dual-side entities) from the UI alone.
- `evidence/network/index.html` opens by double-click, offline.

## When blocked
Report the exact command, its actual output, and the smallest reproducer. Do not guess or fabricate output.
