# Writing Style Guide — Entity Profiles (8–10th Grade)

**Case:** INV-2026-002 · **File:** evidence/30-writing-style-guide.md
**Summary:** The plain-English standard every entity profile must meet, plus the rewrite rules for writer subagents.
**Key actors:** all 163 mapped entities
**Pull when:** writing or rewriting ANY entity profile, or reviewing prose for reading level.

---

## The standard (what "8–10th grade" means here)

Measured by Flesch-Kincaid grade level, computed by `scripts/check_readability.py`. Target is **grade 8–10**. The current corpus averages grade 13.4 — that is the gap this guide closes.

Concretely, grade 8–10 means:

1. **Short sentences.** Average sentence length 12–16 words, never a 25-word run-on.
2. **Active voice.** "He runs the county" not "The county is run by him."
3. **One idea per sentence.** Don't stack three clauses with "while," "which," and "as well as."
4. **Common words.** "Money," "power," "job," "office" — not "fiscal allocation," "institutional authority," "positional decisional capacity."
5. **No jargon.** If a word needs a dictionary or a sociology degree, replace it or explain it.

## What "every page stands alone" means

The reader sees ONE entity at a time in a drawer. They may never see any other page. So every page must explain itself:

- **Expand every acronym on first use ON that page** — even if another page already did. A reader who opens only the MultiCare page must see "MultiCare, a hospital system" spelled out there.
- **Name the context.** Don't say "the Council." Say "the Pierce County Council." Don't say "PDC." Say "the state's campaign-finance agency (PDC)."
- **Assume nothing about the map.** If a reader doesn't know what "Pierce County" or "Joint Base Lewis-McChord" is, the page should still make sense.

## The story structure (per page, for impact)

Each page is an argument about ONE entity: why it has power, where that power comes from, and what it does with it. Lead with the punchline, then prove it.

Order the sections so the reader gets the most important thing first:

1. **Who they are + why they matter** (one strong lead sentence, not a name-and-birthdate list).
2. **Where their power comes from** (the money, the office, the law that gives them authority).
3. **What they do with it** (the decisions, the money they move, the people they influence).
4. **Who they're connected to** (the network — clickable chips).
5. **The receipts** (sources and evidence, kept as a table).

The plain-English section labels already do this: "Why this person or group is on the map," "Where their power comes from," "What they actually influence," "Who they are connected to," "What it all means."

## The rewrite rules (what to change, and what NOT to touch)

**Change (prose only — sections 0 through 12 body text):**
- Shorten sentences; split run-ons.
- Replace jargon with plain words: "positional power" → "power from holding an office"; "decisional" → "makes decisions"; "relational" → "well-connected"; "structural capture" → "a cycle where public money becomes private power."
- Write in active voice.
- Explain acronyms on first use.

**Do NOT touch (machine-read or evidence-critical):**
- The frontmatter header (everything before the first `---` line): `**Known facts:**`, `**Graph description:**`, `**Status:** ✅ researched`, `**Tier:**`, `**Composite power:**`.
- The `**Confidence:**` line in section 12 (the gate checks it — keep `High`/`Medium`/`Low` + one-line basis).
- The `edge: source=...` lines in the "New relationships" section (the sync script reads them).
- The Sources table rows (they are the verifiable evidence; you may trim a redundant column note but keep the URL and reliability score).
- Any dollar figure, date, percentage, vote count, or proper name. If you don't have a source for it, do NOT change it — flag it instead.

## Anti-AI-writing rules (from the humanizer skill)

- No "serves as," "stands as," "a pivotal/crucial/key role," "underscores," "highlights," "showcases."
- No "-ing" decoration tacked onto a sentence to sound deep.
- No rule-of-three padding.
- No em dashes, no emojis, no bold-face section headers in prose.
- No "Not only X but Y," no "It's not just about X."
- No "Let's dive in," no "here's what you need to know."
- No vague authority ("experts say," "observers note") — cite a real source or cut it.
- No "the real question is," "at its core," "fundamentally."
- Use "is," "are," "has," "does" — not "serves as," "functions as," "represents."

## A worked example (before → after)

**Before (grade ~13, jargon-heavy):**
> Ryan Mello's inclusion is warranted on positional and decisional grounds, as the County Executive exercises veto authority over the seven-member legislative Council and operational control over all executive departments, positioning him at the apex of county government per the Laumann, Marsden & Prensky (1983) boundary-specification framework.

**After (grade ~8, plain):**
> Ryan Mello is on this map because he is the Pierce County Executive. That means he runs the county's departments and can veto almost anything the seven-member County Council passes. He is the most powerful elected official in the county.

The facts are identical. The second version a 13-year-old can read.

## How a writer subagent applies this

1. Read the profile once, in full.
2. Rewrite sections 0 through 12 in plain English, using the section labels and rules above.
3. Run `python3 scripts/check_readability.py --max-grade 10` and keep editing until the profile passes.
4. Confirm the header, `**Confidence:**` line, Sources table, and `edge:` lines are untouched.
5. Report the before/after grade level.
