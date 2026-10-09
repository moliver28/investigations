#!/usr/bin/env python3
"""
Deterministic prose-rewriting pass for 8-10th grade readability.
Does the mechanical work that doesn't need judgment:
  1. Strip [x] / [ ] checkbox markers
  2. Rename section headers to plain English (matching exemplar)
  3. Expand acronyms on first use per page
  4. Replace jargon with plain-English equivalents
  5. Strip academic citations from prose
  6. Strip edge-machine lines left in prose sections
  7. Remove "§N" style headers, normalize to "## N."

This is NOT a full rewrite — it handles the mechanical transformations
so subagents can focus on sentence-level rewriting.

Usage:
  python3 scripts/rewrite_prose.py [file.md ...]   # process specific files
  python3 scripts/rewrite_prose.py --all             # process all profiles
  python3 scripts/rewrite_prose.py --dry-run [files] # show changes without writing
"""

import os
import re
import sys

PROFILES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "profiles")

# ── Acronym expansion (first use per page) ──────────────────────────
# Map: acronym → (full name, domains where it's common)
ACRONYM_MAP = {
    "JBLM": "Joint Base Lewis-McChord",
    "GTCF": "Greater Tacoma Community Foundation",
    "PDC": "the state campaign-finance agency (PDC)",
    "RCW": "state law (RCW)",
    "EIN": "tax ID number (EIN)",
    "IRS": "the federal tax agency (IRS)",
    "PAC": "political action committee (PAC)",
    "EDB": "Economic Development Board (EDB)",
    "TPU": "Tacoma Public Utilities (TPU)",
    "NWSA": "Northwest Seaport Alliance (NWSA)",
    "SSMCP": "South Sound Military and Communities Partnership (SSMCP)",
    "PSE": "Puget Sound Energy (PSE)",
    "PLU": "Pacific Lutheran University (PLU)",
    "TCC": "Tacoma Community College (TCC)",
    "UWT": "University of Washington Tacoma (UWT)",
    "ILWU": "International Longshore and Warehouse Union (ILWU)",
    "VMFH": "Virginia Mason Franciscan Health (VMFH)",
    "WEA": "Washington Education Association (WEA)",
    "FPD": "Fire Protection District (FPD)",
    "GF": "General Fund (GF)",
    "ICD": "investigative control document (ICD)",
}

# ── Jargon → plain English ──────────────────────────────────────────
JARGON_SWAPS = [
    # (pattern, replacement) — word-boundary aware
    (r'\bpositional power\b', 'power from holding an office'),
    (r'\bpositional\b', 'from holding office'),
    (r'\bdecisional power\b', 'power to make decisions'),
    (r'\bdecisional\b', 'decision-making'),
    (r'\brelational power\b', 'power from connections'),
    (r'\brelational\b', 'well-connected'),
    (r'\bstructural capture\b', 'a cycle where public money becomes private power'),
    (r'\binstitutional authority\b', 'power from running a big organization'),
    (r'\bagenda-setting power\b', 'the power to set the agenda'),
    (r'\binfluence network\b', 'network of connections'),
    (r'\bboard\s+interlocks\b', 'board overlaps'),
    (r'\binterlocks\b', 'board overlaps'),
    (r'\bboard\s+interlock\b', 'board overlap'),
    (r'\binterlock\b', 'board overlap'),
    (r'\bgrowth machine\b', 'development coalition'),
    (r'\bgrowth machine actors\b', 'developers and business leaders who push for growth'),
    (r'\bdomain focus questions\b', 'key facts'),
    (r'\bdomain focus\b', 'key facts'),
    (r'\bboundary & inclusion\b', 'why this entity is on the map'),
    (r'\bboundary and inclusion\b', 'why this entity is on the map'),
    (r'\blegal identity\b', 'who they are legally'),
    (r'\bleadership & board\b', 'leadership and board'),
    (r'\bpower basis & domains\b', 'where their power comes from'),
    (r'\bpower basis and domains\b', 'where their power comes from'),
    (r'\bpower indicators\b', 'what they influence'),
    (r'\bgovernment interfaces\b', 'how they touch government'),
    (r'\bnetwork position\b', 'who they are connected to'),
    (r'\bcontroversies and questions\b', 'controversies and open questions'),
    (r'\bsources and evidence\b', 'sources and evidence'),
    (r'\bopen questions\b', 'open questions'),
    (r'\bwhat it all means\b', 'what it all means'),
]

# ── Section header mapping (number → plain English title) ────────────
SECTION_HEADERS = {
    "0": "Why this person or group is on the map",
    "1": "Who they are",
    "2": "Their career and offices",
    "3": "Where their power comes from",
    "3a": "What they actually influence",
    "4": "Their money",
    "5": "How they touch government",
    "6": "Other seats they hold",
    "7": "Controversies and open questions",
    "8": "How the press covers them",
    "9": "Who they are connected to",
    "10": "Sources and evidence",
    "11": "Open questions",
    "12": "What it all means",
}

# ── Academic citation patterns to strip ──────────────────────────────
ACADEMIC_CITE_PATTERNS = [
    r'\(Laumann[^)]*\)',
    r'\(Marsden[^)]*\)',
    r'\(Prensky[^)]*\)',
    r'\(Domhoff[^)]*\)',
    r'\(Hunter[^)]*\)',
    r'\(Mills[^)]*\)',
    r'\(Wasserman[^)]*\)',
    r'\(Faust[^)]*\)',
    r'\(Freeman[^)]*\)',
    r'\(Bonacich[^)]*\)',
    r'\(Brin[^)]*\)',
    r'\(Page[^)]*\)',
    r'ICD\s+\d{3}',
    r'\bper\s+(?:the\s+)?(?:Laumann|Marsden|Prensky|Domhoff|Hunter|Mills|Wasserman|Faust|Freeman|Bonacich)\b',
    r'\bper\s+graph\b',
    r'\bper\s+source\s+#?\d+\b',
    r'\bgraph:\s*`[^`]+`\s*',
]

# ── Edge-machine lines to strip ──────────────────────────────────────
EDGE_MACHINE_PATTERNS = [
    r'^\s*-\s*edge:\s+source=',
    r'^\s*##\s*(?:New\s+)?[Rr]elationships?\s+(?:discovered|to\s+record|found)',
    r'^\s*#\s+(?:New\s+)?[Rr]elationships?\s+(?:discovered|to\s+record|found)',
    r'\*\*New\s+edges?\s+discovered:\*\*',
    r'\(graph:\s*`[^`]+`\s*\)',       # (graph: `entity-id`)
    r'\(graph:\s*[^)]+\)',             # (graph: text without backticks)
]

# Also clean up empty parentheticals and dangling punctuation after cite removal
POST_CLEANUP_PATTERNS = [
    (r'\(\s*\)', ''),                   # empty parens ()
    (r'\(\s*,\s*\)', ''),               # empty parens with comma (,)
    (r',\s*\)', ')'),                   # trailing comma before closing paren
    (r'\(\s*\)', ''),                   # again for nested
]


def expand_acronyms(text: str) -> str:
    """Expand acronyms on first use. Each acronym gets expanded once."""
    used = set()
    lines = text.split('\n')
    result = []
    for line in lines:
        for acro, full in ACRONYM_MAP.items():
            if acro in used:
                continue
            # Match acronym as a whole word, but NOT inside a markdown link or URL
            # and NOT already expanded (i.e., "Full Name (ACRO)" pattern)
            already_expanded = re.search(
                re.escape(full.split('(')[0].strip()) + r'\s*\(' + re.escape(acro) + r'\)',
                line
            )
            if already_expanded:
                used.add(acro)
                continue
            # Replace standalone acronym (word boundary)
            pattern = r'\b' + re.escape(acro) + r'\b(?!\s*[)})\]])'
            new_line = re.sub(pattern, full, line, count=1)
            if new_line != line:
                used.add(acro)
                line = new_line
        result.append(line)
    return '\n'.join(result)


def strip_checkbox(text: str) -> str:
    """Remove [x] and [ ] checkbox markers from line starts."""
    return re.sub(r'^(\s*)-\s*\[[ x]\]\s*', r'\1- ', text, flags=re.MULTILINE)


def rename_sections(text: str) -> str:
    """Rename section headers to plain English."""
    for num, title in SECTION_HEADERS.items():
        # Match ## 3a. or ## 3a or §3a or § 3a patterns
        # Pattern: ## <number>[<dot><space>][<old title>]
        escaped = re.escape(num)
        pattern = r'^(##)\s+' + escaped + r'[\.\s]*.*$'
        replacement = f'\\1 {num}. {title}'
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
        # Also handle § style
        pattern = r'^(§)\s*' + escaped + r'[\.\s]*.*$'
        text = re.sub(pattern, f'## {num}. {title}', text, flags=re.MULTILINE)
    return text


def swap_jargon(text: str) -> str:
    """Replace jargon with plain-English equivalents."""
    for pattern, replacement in JARGON_SWAPS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def strip_academic_cites(text: str) -> str:
    """Remove academic citation parentheticals from prose."""
    for pattern in ACADEMIC_CITE_PATTERNS:
        text = re.sub(pattern, '', text)
    # Clean up double spaces left by removals
    text = re.sub(r'  +', ' ', text)
    # Clean up " ." → "."
    text = re.sub(r' \.', '.', text)
    # Clean up " , " → ", "
    text = re.sub(r'\s+,', ',', text)
    return text


def strip_edge_machine(text: str) -> str:
    """Remove edge-machine lines that leaked into prose sections."""
    for pattern in EDGE_MACHINE_PATTERNS:
        text = re.sub(pattern, '', text, flags=re.MULTILINE)
    # Clean up blank lines left behind
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def clean_prose(text: str) -> str:
    """Run all mechanical cleaning passes."""
    text = strip_checkbox(text)
    text = rename_sections(text)
    text = swap_jargon(text)
    text = strip_academic_cites(text)
    text = strip_edge_machine(text)
    text = expand_acronyms(text)
    # Post-cleanup: remove empty parens and dangling punctuation
    for pattern, replacement in POST_CLEANUP_PATTERNS:
        text = re.sub(pattern, replacement, text)
    # Final whitespace cleanup
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r'\s+,', ',', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def process_file(filepath: str, dry_run: bool = False) -> tuple:
    """Process a single profile file. Returns (filepath, changed, diff_summary)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    # Split into frontmatter (before ---) and body
    parts = original.split('\n---\n', 1)
    if len(parts) == 2:
        header, body = parts[0], parts[1]
    else:
        # No --- found, process everything
        header, body = '', original

    # Only process the body
    cleaned_body = clean_prose(body)

    # Reassemble
    if len(parts) == 2:
        result = header + '\n---\n' + cleaned_body
    else:
        result = cleaned_body

    changed = result != original
    if changed and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)

    # Count changes
    orig_lines = original.count('\n')
    new_lines = result.count('\n')
    diff_summary = f"{orig_lines}→{new_lines} lines" if changed else "no change"

    return (filepath, changed, diff_summary)


def main():
    dry_run = '--dry-run' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')]

    if not files or '--all' in sys.argv:
        files = sorted(
            os.path.join(PROFILES_DIR, f)
            for f in os.listdir(PROFILES_DIR)
            if f.endswith('.md') and f != 'README.md'
        )

    changed_count = 0
    for fpath in files:
        try:
            _, changed, summary = process_file(fpath, dry_run=dry_run)
            status = "CHANGED" if changed else "OK"
            if changed:
                changed_count += 1
            print(f"  {status}: {os.path.basename(fpath)} ({summary})")
        except Exception as e:
            print(f"  ERROR: {os.path.basename(fpath)}: {e}")

    total = len(files)
    print(f"\nDone: {changed_count}/{total} files changed" + (" (dry run)" if dry_run else ""))


if __name__ == '__main__':
    main()