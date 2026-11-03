# Procedural Knowledge from INV-2026-001 Session

## Evidentiary Standard: "Legally Defensible"
This case operated under the standard that every claim should be evaluated as if a prosecutor would need to prove it in court. Key adjustments this required:
- **Peer comparison** — cannot claim "systemic failure" without establishing a baseline. Required analysis of 8 comparable cities.
- **Threshold awareness** — Lindholm's F-1 omission looks damning but the PDC threshold is $2,400. The claim must be: "his F-1 lists zero income from his CEO role" — not "he violated RCW 42.17."
- **Entity separateness** — Pierce Transit ≠ Pierce County. Bocchi's conflict is attenuated. Must be framed precisely.
- **Correlation vs. causation** — 2 donor-guest overlaps is suggestive. 6 (with 4 clustering on one date) is a pattern. The difference matters legally.

## Exhaust Every Tool Before Declaring Blocked
When a search appears blocked, don't stop at the first tool failure. This session demonstrated:
- `web_extract` blocked on Angular SPA → try `browser_exec` → if that needs Chrome consent, try `curl` API probes → check 3rd-party aggregators
- CCFS portal block resolved by user's manual search (confirmed: Concord Counsel not registered = sole proprietorship)
- The "couldn't find anything" result WAS the finding

## Right-of-Reply Framework
20 questions across 7 council members. Saved to `~/voice-michael-oliver/right-of-reply-framework.md` for user review. See `references/right-of-reply-practice.md` in the case-manager skill for general practice rules.

## Key Sources Discovered
- Lakewood Municipal Code Ch. 1.32 (Code of Ethics) — exists but never enforced
- Lakewood Council Rules of Procedure, Section 7.3 (Conflict of Interest), Section 10.1 (Abstention)
- Federal Way Municipal Code Ch. 2.90 (Ethics Board with subpoena power) — proves code city CAN enforce ethics
- PDC F-1 instructions confirm $2,400 threshold for business entity income
- MRSC guidance: abstention IS the legally required remedy for conflicts in WA

## NER Pipeline Runs This Session
8 runs across: campaign finance, new evidence (Phase 4), narrative gaps, property records, hypercritical review, new-evidence supplement, peer comparison, how-the-world-works, master citation index, podcast-donor cross-ref
