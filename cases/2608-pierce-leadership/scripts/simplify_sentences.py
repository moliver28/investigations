#!/usr/bin/env python3
"""
Sentence-level deterministic readability pass for profile markdown files.

Targets Flesch-Kincaid grade reduction by:
  - Splitting compound sentences on clear clause boundaries (no list splits)
  - Replacing Latinate words with plain English
  - Stripping redundant "which is" / "that is" connectors
  - Expanding acronyms on first use per file

Preserves machine-readable parts byte-for-byte:
  - Frontmatter (entity-profile comment + title + Case/Profile lines)
  - **Confidence:** line
  - edge: source= lines
  - ## Sources structured table

Conservative approach: only splits where it's unambiguous; preserves lists, numbers,
tables, and markdown structure. Limits whitespace churn (no extra/missing newlines).

Usage:
    /Users/moliver/.hermes/hermes-agent/venv/bin/python3 \\
        scripts/simplify_sentences.py [path-to-profile.md ...]
    /Users/moliver/.hermes/hermes-agent/venv/bin/python3 \\
        scripts/simplify_sentences.py --all
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "profiles"
VENV = Path("/Users/moliver/.hermes/hermes-agent/venv/bin/python3")
CHECK_SCRIPT = ROOT / "scripts" / "check_readability.py"

FRONTMATTER_RE = re.compile(
    r"^(<!-- entity-profile:v1[^\n]*-->\n"
    r"# [^\n]+\n"
    r"\*\*Case:\*\*[^\n]+\n"
    r"\*\*Entity ID:\*\*[^\n]+\n"
    r"\*\*Tier:\*\*[^\n]+\n"
    r"\*\*Graph description:\*\*[^\n]+\n"
    r"\*\*Known facts:\*\*[^\n]+\n"
    r"\*\*Status:\*\*[^\n]+\n"
    r"\*\*Sources:\*\*[^\n]+\n)",
    re.MULTILINE,
)
CONFIDENCE_LINE_RE = re.compile(r"^\*\*Confidence:\*\*[^\n]*\n", re.MULTILINE)
EDGE_LINE_RE = re.compile(r"^edge:[^\n]*\n", re.MULTILINE)
SOURCES_HEADER_RE = re.compile(r"^## Sources\s*\n", re.MULTILINE)
SECTION_HEADER_RE = re.compile(r"^##\s+\S.*?\n", re.MULTILINE)

# Plain-English replacements. Apply ONLY to prose body, never to machine parts.
LATINATE_TO_PLAIN = [
    (r"\bmake use of\b", "use"),
    (r"\bgive consideration to\b", "consider"),
    (r"\bprovide assistance\b", "help"),
    (r"\btake into account\b", "consider"),
    (r"\bin order to\b", "to"),
    (r"\bdue to the fact that\b", "because"),
    (r"\bin the event that\b", "if"),
    (r"\bfor the purpose of\b", "to"),
    (r"\bwith regard to\b", "about"),
    (r"\bin regard to\b", "about"),
    (r"\bwith respect to\b", "about"),
    (r"\bin relation to\b", "about"),
    (r"\bprior to\b", "before"),
    (r"\bsubsequent to\b", "after"),
    (r"\bin the vicinity of\b", "near"),
    (r"\ba large number of\b", "many"),
    (r"\bthe majority of\b", "most"),
    (r"\butilize\b", "use"),
    (r"\butilizing\b", "using"),
    (r"\butilization\b", "use"),
    (r"\bdemonstrate\b", "show"),
    (r"\bdemonstrates\b", "shows"),
    (r"\bdemonstrated\b", "showed"),
    (r"\bdetermine\b", "find"),
    (r"\bdetermines\b", "finds"),
    (r"\bterminated\b", "ended"),
    (r"\bterminate\b", "end"),
    (r"\bapproximately\b", "about"),
    (r"\bcommenced\b", "started"),
    (r"\bcommence\b", "start"),
    (r"\bpursuant to\b", "under"),
    (r"\bin accordance with\b", "under"),
    (r"\bnotwithstanding\b", "despite"),
]

# Acronym expansions: only applied once per file.
ACRONYM_EXPANSIONS = [
    (r"\bBLM\b", "the Bureau of Land Management"),
    (r"\bFAA\b", "the Federal Aviation Administration"),
    (r"\bFERC\b", "the Federal Energy Regulatory Commission"),
    (r"\bEPA\b", "the Environmental Protection Agency"),
    (r"\bNOAA\b", "the National Oceanic and Atmospheric Administration"),
    (r"\bUSGS\b", "the U.S. Geological Survey"),
    (r"\bUSFWS\b", "the U.S. Fish and Wildlife Service"),
    (r"\bGAO\b", "the U.S. Government Accountability Office"),
    (r"\bSEC\b", "the Securities and Exchange Commission"),
    (r"\bHUD\b", "the U.S. Department of Housing and Urban Development"),
    (r"\bDOT\b", "the U.S. Department of Transportation"),
    (r"\bDOE\b", "the U.S. Department of Energy"),
    (r"\bDOD\b", "the U.S. Department of Defense"),
    (r"\bGSA\b", "the General Services Administration"),
    (r"\bPAC\b", "the political action committee"),
    (r"\bSEIU\b", "the Service Employees International Union"),
    (r"\bEDA\b", "the Economic Development Administration"),
]


def find_machine_parts(text: str) -> list:
    """Return list of (label, start, end) ranges that are byte-preserved."""
    parts = []
    m = FRONTMATTER_RE.match(text)
    if m:
        parts.append(("frontmatter", 0, m.end()))
    m = SOURCES_HEADER_RE.search(text)
    if m:
        parts.append(("sources", m.start(), len(text)))
    for m in EDGE_LINE_RE.finditer(text):
        parts.append(("edge", m.start(), m.end()))
    for m in CONFIDENCE_LINE_RE.finditer(text):
        parts.append(("confidence", m.start(), m.end()))
    return parts


def is_in_machine(idx: int, machine_parts: list) -> bool:
    for _, start, end in machine_parts:
        if start <= idx < end:
            return True
    return False


def get_prose_ranges(machine_parts: list, total_len: int) -> list:
    """Return [(start, end)] ranges that are NOT machine parts and NOT inside list items / tables."""
    mp = sorted(machine_parts, key=lambda x: x[1])
    ranges = []
    cursor = 0
    for _, start, end in mp:
        if cursor < start:
            ranges.append((cursor, start))
        cursor = max(cursor, end)
    if cursor < total_len:
        ranges.append((cursor, total_len))

    # Further refine: detect "list" zones where bullet items should NOT be split.
    # A list zone is a run of consecutive lines starting with "- " or "* " or numbered "1. ".
    refined = []
    for start, end in ranges:
        zone = text_slice = text_at_range = None
        # We'll do this in the caller since we need the text
        refined.append((start, end, False))  # placeholder
    return [(s, e) for s, e, _ in refined]


def is_list_line(line: str) -> bool:
    """True if line starts with a bullet or numbered list marker."""
    return bool(re.match(r"^\s*([-*]\s|\d+\.\s|>\s)", line))


def is_table_line(line: str) -> bool:
    return line.lstrip().startswith("|")


def is_section_header(line: str) -> bool:
    return line.startswith("## ")


def should_split_at(text: str, pos: int) -> bool:
    """Decide if splitting a sentence at this position is safe."""
    # Don't split inside a comma-separated list of names/items.
    # Heuristic: if the comma is between two short capitalized words (<= 4 words each side),
    # it's likely a list — don't split.
    # Look at the substring around the comma.
    line_start = text.rfind("\n", 0, pos) + 1
    line_end = text.find("\n", pos)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]

    # Don't split inside table rows
    if is_table_line(line):
        return False

    # Don't split lines that look like list items at the markdown level
    # (but bullet items CAN have split sentences inside)
    # Don't split inside numbered headings or URLs
    return True


def split_sentences_preserving_lists(paragraph: str) -> list:
    """Split paragraph into sentences, but don't split at commas inside obvious lists."""
    # Simple approach: walk through paragraph, split on ". " or "? " or "! ",
    # but check each split is not mid-list.

    # First, split on sentence-ending punctuation followed by space + capital letter
    raw_splits = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"\u201c'])", paragraph)
    return [s for s in raw_splits if s.strip()]


def split_long_sentence(sentence: str, max_words: int = 22) -> list:
    """Split a sentence into shorter ones at clear clause boundaries."""
    words = sentence.split()
    if len(words) <= max_words:
        return [sentence]

    # Try splitting on clause boundaries with pattern + uppercase look-ahead
    # Conservative: only split when right side clearly starts a new main clause.
    # Patterns ordered by preference.
    split_patterns = [
        # "; " between independent clauses (definitive split)
        (r";\s+(?=[A-Z][a-z])", ". "),
        # ", and " followed by a capitalized word + verb (new clause)
        (r",\s+and\s+(?=[A-Z][a-z]+\s+(?:is|was|has|have|had|provides?|controls?|sets?|approves?|passed|approved|serves?|includes?|covers?|creates?|builds?|runs?|holds?|operates?|manages?|uses?|employs?|generates?|delivers?|sells?|buys?|files?|faces?|heads?|leads?|chairs?|oversees?|funded|received|earned|won|lost|filed|joined|left|started|ended|wrote|writes|ruled|votes?|voted|elected|appointed|designated|named|recruited|hired|fired|signed|signed|broke|released|published|announced|reported|testified|spoke|met|ran|saw|took|made|gave|got|set|put|cut|hit|let|read|come|gone|seen|done|known|grown|shown|chosen|written|drawn|driven|broken|spoken|forgotten|frozen|stolen|beaten|hidden|ridden|eaten|fallen|risen|flown|swum|run|begun|sung|sung|drunk|sunk|shrunk|spun|won|risen|arisen))",
         ". "),
        # ", but " followed by capitalized word
        (r",\s+but\s+(?=[A-Z][a-z]+(\s+[a-z]+){0,2}\s+(?:is|was|has|have|had|provides?|controls?|sets?|approves?|serves?|includes?|covers?|creates?|builds?|runs?|holds?|operates?|manages?|uses?|employs?|generates?|delivers?|sells?|buys?|files?|faces?|heads?|leads?|chairs?|oversees?))",
         ". But "),
        # ", while " followed by capitalized word
        (r",\s+while\s+(?=[A-Z][a-z]+(\s+[a-z]+){0,2}\s+(?:is|was|has|have|had|provides?|controls?|sets?|approves?|serves?|includes?|covers?|creates?|builds?|runs?|holds?|operates?|manages?|uses?|employs?|generates?|delivers?|sells?|buys?|files?|faces?|heads?|leads?|chairs?|oversees?))",
         ". While "),
        # ", which " — usually a relative clause; replace with period + This
        (r",\s+which\s+(?=[A-Z])", ". This "),
    ]

    for pat, repl in split_patterns:
        m = re.search(pat, sentence)
        if m:
            new = sentence[:m.start()] + repl + sentence[m.end():]
            # Recursively split each piece
            pieces = [p.strip() for p in new.split(". ") if p.strip()]
            result = []
            for piece in pieces:
                if piece and not piece.rstrip().endswith(('.', '!', '?', ':')):
                    piece += '.'
                result.extend(split_long_sentence(piece, max_words))
            return result

    return [sentence]


def clean_sentence(sentence: str) -> str:
    s = sentence
    for pattern, repl in LATINATE_TO_PLAIN:
        s = re.sub(pattern, repl, s, flags=re.IGNORECASE)
    s = re.sub(r"\bwhich is\b", "that", s, flags=re.IGNORECASE)
    s = re.sub(r"\bwho is\b", "who", s, flags=re.IGNORECASE)
    if s and not s.rstrip().endswith(('.', '!', '?', ':')):
        s = s.rstrip() + '.'
    return s


def rewrite_prose_paragraph(para: str) -> str:
    """Rewrite a single paragraph (single newline-bounded block)."""
    # Preserve leading bullet markers, bold-prefixes, etc.
    # Extract bullet marker if present
    m = re.match(r"^([-*]\s+|[-*]\*\*[^*]+\*\*[:—]\s+)", para)
    bullet = m.group(1) if m else ""
    body = para[len(bullet):] if bullet else para

    if not body.strip():
        return para

    # Don't touch table rows
    if body.lstrip().startswith("|"):
        return para

    # Don't split inside short field labels like "- **EIN:** X" — body is already structured
    # Check if body is mostly a label-value pair (bold + colon + content)
    if re.match(r"^\*\*[^*]+:\*\*\s+", body):
        # Just clean the value part
        label_match = re.match(r"^(\*\*[^*]+:\*\*\s+)(.*)$", body, re.DOTALL)
        if label_match:
            label = label_match.group(1)
            value = label_match.group(2)
            value = clean_sentence(value)
            # Don't split labeled fields — they're already short
            return bullet + label + value
        return para

    # Split into sentences
    sentences = split_sentences_preserving_lists(body)
    out = []
    for sent in sentences:
        if not sent.strip():
            continue
        # Skip acronym expansion inside table-y content (already filtered)
        for piece in split_long_sentence(sent):
            out.append(clean_sentence(piece))
    rebuilt = " ".join(out)
    return bullet + rebuilt


def process_prose_block(text: str) -> str:
    """Process a contiguous prose block, preserving newlines and structure."""
    # Skip horizontal rules and other markdown separators entirely
    if re.match(r"^\s*---\s*$", text):
        return text

    # Process paragraph-by-paragraph (split on blank lines and section breaks)
    # Use a regex that keeps the separators
    paragraphs = re.split(r"(\n\n|\n(?=##\s))", text)
    out = []
    for para in paragraphs:
        # If it's a separator (blank line or section break), pass through
        if re.match(r"^\s*$", para) or re.match(r"^##\s", para):
            out.append(para)
            continue
        # Skip horizontal rules
        if re.match(r"^\s*---\s*$", para):
            out.append(para)
            continue
        # If it's a single-line bullet item, process in place (preserve newline at end)
        if "\n" not in para.rstrip("\n"):
            out.append(rewrite_prose_paragraph(para))
            continue
        # Multi-line block: split into lines, process each non-empty line
        lines = para.split("\n")
        new_lines = []
        for line in lines:
            if not line.strip():
                new_lines.append(line)
                continue
            if is_section_header(line):
                new_lines.append(line)
                continue
            if is_table_line(line):
                new_lines.append(line)
                continue
            if re.match(r"^\s*---\s*$", line):
                new_lines.append(line)
                continue
            new_lines.append(rewrite_prose_paragraph(line))
        out.append("\n".join(new_lines))
    return "".join(out)


def expand_acronyms_file(text: str) -> str:
    """Expand acronyms on first use per file."""
    for pattern, expansion in ACRONYM_EXPANSIONS:
        expansion_short = expansion.replace("the ", "").strip()
        # Check if expansion already exists anywhere in the file
        if re.search(rf"\b{re.escape(expansion_short)}\b", text, re.IGNORECASE):
            continue
        # Find first occurrence of acronym
        m = re.search(pattern, text)
        if not m:
            continue
        text = text[:m.start()] + f"{expansion} ({m.group(0)})" + text[m.end():]
    return text


def process_file(path: Path) -> bool:
    """Process one profile file. Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    machine_parts = find_machine_parts(text)

    # Walk through text, replacing prose ranges only
    pieces = []
    cursor = 0
    for label, start, end in sorted(machine_parts, key=lambda x: x[1]):
        if cursor < start:
            prose = text[cursor:start]
            pieces.append(process_prose_block(prose))
        pieces.append(text[start:end])  # machine part — verbatim
        cursor = end
    if cursor < len(text):
        pieces.append(process_prose_block(text[cursor:]))

    new_text = "".join(pieces)
    new_text = expand_acronyms_file(new_text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def grade(path: Path) -> float | None:
    result = subprocess.run(
        [str(VENV), str(CHECK_SCRIPT), str(path)],
        capture_output=True, text=True, cwd=str(ROOT)
    )
    for line in result.stdout.splitlines():
        if path.name in line and "grade" in line:
            m = re.search(r"grade\s+([\d.]+)", line)
            if m:
                return float(m.group(1))
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", type=Path, help="Profile files to process")
    ap.add_argument("--all", action="store_true", help="Process all profiles/*.md")
    ap.add_argument("--dry-run", action="store_true", help="Compute grades without writing")
    ap.add_argument("--quiet", action="store_true", help="Suppress per-file output")
    args = ap.parse_args()

    if args.all:
        files = sorted(PROFILES.glob("*.md"))
    else:
        files = args.files

    if not files:
        print("No files specified. Use --all or pass file paths.", file=sys.stderr)
        sys.exit(1)

    baseline = {f: grade(f) for f in files}

    if not args.dry_run:
        for f in files:
            process_file(f)

    results = {}
    for f in files:
        new_grade = grade(f)
        old_grade = baseline[f]
        results[f.name] = (old_grade, new_grade)

    print(f"\n{'='*70}")
    print(f"Profile readability: {len(files)} files")
    print(f"{'='*70}")
    improved = regressed = 0
    for name in sorted(results, key=lambda n: (results[n][1] or 0), reverse=True):
        old, new = results[name]
        delta = (new or 0) - (old or 0)
        arrow = "↓" if delta < -0.1 else ("↑" if delta > 0.1 else "→")
        if delta < -0.1:
            improved += 1
        elif delta > 0.1:
            regressed += 1
        if not args.quiet:
            print(f"  {name:<42}  {old:5.1f} {arrow} {new:5.1f}  (Δ {delta:+.1f})")
    print(f"\nImproved: {improved} | Regressed: {regressed} | Unchanged: {len(files) - improved - regressed}")


if __name__ == "__main__":
    main()
