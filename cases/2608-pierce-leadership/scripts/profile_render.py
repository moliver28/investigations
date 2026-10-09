#!/usr/bin/env python3
"""Profile-rendering transforms for the Pierce County power network (UI v3).

Owns: SECTION_TITLES, ACRONYMS, the readability transforms, and
render_profile_html(). Imported by scripts/build_entity_bundle.py (the v3 bundle
builder) and build_power_network.py (v2, retired).

Render-layer readability pass (2026-10-04):
- No whole-block cut at machine headings any more. The previous re.split at any
  "New relationships …" heading silently deleted everything AFTER it — the
  10-sources table on 21 pages and the §12 assessment on 10 more. Machine
  syntax is now stripped line-by-line so content that follows it survives.
- Content-signature section renumbering: duplicated template headings get their
  canonical numbers back (sources table → 10, four-question grid → 3a, open
  questions → 11, assessment/verdict → 12), so every TOC label is unique. The
  research record (profiles/*.md) is untouched — machine-readable lines stay
  byte-for-byte in the canonical files.
- De-jargoning: internal build-path citations and node-id parentheticals are
  removed from reader-facing prose; rescue-family headings (§7 connections,
  §2 power basis) normalize to canonical numbers.
"""
import os, re
import markdown

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_DIR = os.path.join(REPO_DIR, "..", "profiles")

# ── Full-profile rendering: embed each entity's researched deep-profile (sections 0–12)
#    as HTML in the node data, so the drawer shows the NEARLY-FULL profile by default
#    with the sources table / relationships collapsible. Deterministic: reads the
#    canonical profiles/*.md (the researched source of truth), not the graph desc/facts. ──

# Plain-English section titles that map onto the template's numbered section markers.
# The number is kept (traceability to templates); the words tell the reader what the
# section ANSWERS, so a zero-context reader always understands the page.
SECTION_TITLES = {
    "0":  "Why this person or group is on the map",
    "1":  "Who they are",
    "2":  "Their career and offices",
    "3":  "Where their power comes from",
    "3a": "What they actually influence",
    "4":  "Their money",
    "5":  "How they touch government",
    "6":  "Other seats they hold",
    "7":  "Controversies and questions",
    "8":  "How the press covers them",
    "9":  "Who they are connected to",
    "10": "Sources and evidence",
    "11": "Open questions",
    "12": "What it all means",
}

# Acronyms to expand on first use. Each key is expanded once per profile, in place,
# so every page is self-contained for a reader with zero context.
ACRONYMS = [
    ("JBLM", "Joint Base Lewis-McChord"),
    ("GTCF", "Greater Tacoma Community Foundation"),
    ("PLU", "Pacific Lutheran University"),
    ("TCC", "Tacoma Community College"),
    ("VMFH", "Virginia Mason Franciscan Health"),
    ("UW", "University of Washington"),
    ("TPS", "Tacoma Public Schools"),
    ("TPU", "Tacoma Public Utilities"),
    ("PDC", "Washington Public Disclosure Commission (the state campaign-finance agency)"),
    ("PSRC", "Puget Sound Regional Council"),
    ("SSMCP", "South Sound Military and Communities Partnership"),
    ("RCW", "Revised Code of Washington (state law)"),
    ("EIN", "Employer Identification Number (a tax ID)"),
    ("IRS", "Internal Revenue Service (the federal tax agency)"),
    ("PAC", "political action committee (a group that raises money for candidates)"),
    ("LUCP", "Land Use Consultation Process"),
    ("FMSIB", "Freight Mobility Strategic Investment Board"),
    ("EDB", "Economic Development Board"),
    ("TPCHD", "Tacoma-Pierce County Health Department"),
    ("NWSA", "Northwest Seaport Alliance"),
    ("PSE", "Puget Sound Energy"),
    ("WSHA", "Washington State Hospital Association"),
    ("HHFPAC", "Hospital Health Facilities Political Action Committee"),
    ("CHI", "Catholic Health Initiatives"),
    ("WEA", "Washington Education Association"),
    ("PCCLC", "Pierce County Central Labor Council"),
    ("ILWU", "International Longshore and Warehouse Union"),
    ("UPS", "University of Puget Sound"),
    ("GOIA", "Government Operations and Indian Affairs (tribal affairs office)"),
    ("HCD", "Human-Centered Design"),
    ("UDL", "Universal Design for Learning"),
    ("AUM", "assets under management"),
    ("FY", "fiscal year"),
    ("BoC", "Board of Commissioners"),
    ("CEO", "chief executive officer"),
    ("CFO", "chief financial officer"),
    ("COO", "chief operating officer"),
    ("ED", "executive director"),
    ("JD", "Juris Doctor (a law degree)"),
    ("PhD", "doctor of philosophy (a doctorate degree)"),
    ("BA", "bachelor of arts degree"),
    ("BS", "bachelor of science degree"),
    ("MA", "master of arts degree"),
    ("MPA", "master of public administration degree"),
    ("501(c)(3)", "a tax-exempt charity"),
    ("501(c)(6)", "a tax-exempt business or trade group"),
    # Exec titles + federal codes the audit found unexpanded on multicare / port-tacoma pages
    ("SVP", "senior vice president"),
    ("CIO", "chief information officer"),
    ("CAO", "chief administrative officer"),
    ("EVP", "executive vice president"),
    ("NTEE", "National Taxonomy of Exempt Entities (IRS category code)"),
    ("NAICS", "North American Industry Classification System (federal industry code)"),
    ("CESO", "chief external strategy officer"),
    ("CHRO", "chief human resources officer"),
]


def _strip_checkboxes(body):
    # Remove '[x] ' / '[ ] ' / '[] ' checkbox markers that leak into rendered prose.
    return re.sub(r"^\s*[-*]\s*\[[ xX]?\]\s*", "- ", body, flags=re.MULTILINE)


def _resolve_cross_references(body):
    """Resolve dangling 'See above' cross-references inline (render layer only).

    Two profiles end a key-facts block with 'See above' (puyallup-tribe, pmba);
    on a standalone entity page the phrase dangles, and AGENTS.md rule 5 bans
    'as seen above' in rendered prose. Replace with a factual inline restatement;
    the canonical profiles/*.md stay byte-for-byte (research record preserved).
    """
    pairs = [
        ("See above. Sterud (46 years), Reynon (Governor connection).",
         "Sterud (46 years on the council); Reynon (direct line to the Governor's Office of Indian Affairs)."),
        ("See above (President + VP + Secretary + Treasurer + 22 directors, FY2020 roster).",
         "President, vice president, secretary, treasurer, two directors emeritus, and a 22-director roster (FY2020)."),
    ]
    for old, new in pairs:
        body = body.replace(old, new)
    return body


def _classify_tail_block(block):
    """Classify a section body for the render-layer renumbering pass.

    Returns one of: sources_table | four_question_grid | assessment |
    open_questions | other. Signatures are content-based (position-independent),
    because the duplicate template headings occur at different occurrence
    numbers across the 149 affected profiles.
    """
    body = [l for l in block if l.strip()]
    text = "\n".join(body[:14])
    if re.search(r"\|\s*#\s*\|\s*Claim\s*\|", text):
        return "sources_table"
    if re.search(r"\|\s*(?:Question\s*\|\s*Answer|Indicator\s*\|\s*(?:Finding|Evidence|Source))", text) or (
            "Who benefits" in text and "Who wins" in text):
        return "four_question_grid"
    if re.search(r"(?i)\*{0,2}(?:the bottom line|verdict)", text) and re.search(
            r"(?i)counter-argument|counter-view|defense counter-argument|confidence|alternative reading", text):
        return "assessment"
    qlines = [l for l in body if l.lstrip().startswith(("-", "*", "1.", "2.")) and "?" in l]
    if body and len(qlines) >= max(1, len(body) // 2) and not text.startswith("|"):
        return "open_questions"
    return "other"


def _normalize_headers(body):
    """§-style headers → 'N. Title', then content-signature renumbering.

    The duplicated template headings get canonical numbers back so the TOC has
    no duplicate labels: sources table → 10, four-question grid → 3a, leads
    → 11, assessment/verdict → 12. Empty duplicate blocks are dropped.
    """
    body = re.sub(r"^##\s*§(\d+[a-z]?)\s*(.*)$", r"## \1. \2", body, flags=re.MULTILINE)

    lines = body.split("\n")
    heads = []
    for i, l in enumerate(lines):
        m = re.match(r"^##\s+(.*?)\s*$", l)
        if m:
            heads.append((i, m.group(1)))
    if not heads:
        return body

    occ = {}
    repl = {}
    drop = set()
    assigned = set()
    for k, (i, raw) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        m = re.match(r"(\d+[a-z]?)\s*[.:]?\s*(.*)$", raw, re.I)
        num = m.group(1).lower() if m else None
        tail = m.group(2) if m else raw
        occ[num] = occ.get(num, 0) + 1
        isdup = occ[num] > 1
        block = lines[i + 1:end]
        cls = _classify_tail_block(block)
        new = None
        if cls == "sources_table":
            new = ("10", SECTION_TITLES["10"])
        elif cls == "four_question_grid":
            new = ("3a", SECTION_TITLES["3a"])
        elif isdup and cls == "assessment":
            new = ("12", SECTION_TITLES["12"])
        elif isdup and cls == "open_questions":
            new = ("11", SECTION_TITLES["11"])
        elif isdup and not any(x.strip() for x in block):
            drop.add(i)   # empty duplicate heading (e.g. saltchuk's second §12)
            continue
        elif isdup and cls == "other":
            new = ("11", SECTION_TITLES["11"])
        elif num == "7" and re.search(r"connected", tail, re.I):
            # Rescue-family '§7 who they are connected to' → canonical §9.
            new = ("9", SECTION_TITLES["9"])
        elif num == "2" and re.search(r"(?i)power basis|governance", tail):
            # Rescue-family '§2 Power basis / Governance' → canonical §3.
            new = ("3", SECTION_TITLES["3"])
        elif num is None and re.fullmatch(r"(?i)\s*sources\s*", tail):
            new = ("10", SECTION_TITLES["10"])
        elif num is None and re.search(r"(?i)open questions", tail):
            new = ("11", SECTION_TITLES["11"])
        elif num in SECTION_TITLES and occ[num] == 1:
            new = (num, SECTION_TITLES[num])
        if new is None:
            continue
        if new[0] in assigned and new[0] == "11":
            drop.add(i)   # a second leads block merges into the first §11
            continue
        if new[0] in assigned and new[0] in ("10", "12", "3a") and not isdup:
            pass  # keep first assignment; later same-number sections are rare
        assigned.add(new[0])
        repl[i] = f"## {new[0]}. {new[1]}"

    out = []
    for i, l in enumerate(lines):
        if i in drop:
            continue
        out.append(repl.get(i, l))
    return "\n".join(out)


def _expand_acronyms(body):
    # Expand each acronym once per profile, at first use. Word-boundary match so we
    # don't corrupt URLs, ids, or partial words.
    for acr, full in ACRONYMS:
        pattern = re.compile(rf"\b{re.escape(acr)}\b")
        if pattern.search(body):
            body = pattern.sub(f"{acr} ({full})", body, count=1)
    return body


def _strip_academic_cites(body):
    # Remove academic-author citations and framework jargon from the reader-facing prose
    # so it reads like plain language, not a sociology paper. The Sources table keeps the
    # verifiable primary URLs; the methodology (evidence/26-power-methodology.md) keeps the
    # academic grounding. This strips the NAME-DROP scaffolding, not the underlying facts.

    # 1. Parenthetical citations naming an author or the positional/decisional framework.
    body = re.sub(
        r"\s*\([^()]*(?:Laumann|Marsden|Prensky|Domhoff|Mills|Hunter|Dahl|Stone|Logan|"
        r"Molotch|Bourdieu|Foucault|Lukes|Galbraith|Freeman|Bonacich|Brin|Page|Wasserman|"
        r"Faust|whorulesamerica|ICD 20[0-9]|Verification Handbook|Silverman|EJC)[^()]*\)",
        "", body)

    # 2. Bare author-name citations (slash or ampersand forms) with optional year and
    #    trailing "criterion/criteria/framework" scaffolding.
    body = re.sub(
        r"\b(?:Laumann/Marsden/Prensky|Laumann, Marsden & Prensky|Laumann|Marsden|Prensky)"
        r"(?:\s*[0-9]{4})?\s*(?:positional|decisional|reputational|relational)?\s*"
        r"(?:criterion|criteria|framework|inclusion)?\s*:?",
        "", body)

    # 3. Domhoff references and the "Who benefits / Who governs" scaffolding.
    body = re.sub(r"\bDomhoff\s*(?:'s)?\s*(?:framework)?\s*", "", body)
    body = re.sub(r"[\u201c\"](?:Who benefits / Who governs|Who benefits|Who governs)[\u201d\"]\s*", "", body)

    # 4. ICD analytic-tradecraft codes.
    body = re.sub(r"\bICD\s*20[0-9]\b", "", body)

    # 5. Verification Handbook / Silverman / EJC / whorulesamerica references.
    body = re.sub(r"\b(?:whorulesamerica\.ucsc\.edu|Verification Handbook|Silverman/EJC|Silverman|EJC)\b", "", body)

    # collapse any double spaces left by removals
    body = re.sub(r" {2,}", " ", body)
    return body


def _strip_edge_machine_lines(body):
    # Remove machine-facing graph-sync syntax from reader-facing prose.
    #
    # Replaces the old whole-block cut (re.split at any "New relationships …"
    # heading), which swallowed everything AFTER the heading — including the
    # sources table on 21 pages and the §12 assessment on 10 rescue pages.
    # Now: HTML comments are dropped wholesale (they are invisible by design),
    # then individual machine lines are removed and nothing after them is lost.

    # 0. Drop HTML comments entirely (hint blocks, id markers — never rendered).
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

    label_re = re.compile(
        r"^[-*]?\s*\*{0,2}New (?:edges|relationships)\b[^*]*\*{0,2}[:.]*\s*$", re.I)

    out = []
    for line in body.split("\n"):
        s = line.strip()
        # machine section headings (#, ##, ### variants)
        if re.match(r"^#{1,3}\s*[^\n]*(?:New relationships|relationships to record)", line, re.I):
            continue
        # old bullet label forms: "- edge: source=..."
        if re.match(r"^[-*]\s*edge:\s*source=", s, re.I):
            continue
        # standalone / bold label lines ("**New edges to add:**." etc.)
        if label_re.match(s):
            continue
        # graph-sync edge lines (bare, backticked, or bulleted)
        if (", target=" in s) and ("relationship=" in s or "weight=" in s):
            continue
        if re.search(r"\bweight=\d+\b", s) and "note=" in s:
            continue
        # comment-scaffolding leftovers that escaped comment removal
        if re.search(r"\bREL whitelist\b|Each line must match exactly", s):
            continue
        # (submit) markers
        if "(submit)" in line:
            line = line.replace("(submit)", "")
            st = line.strip()
            if not st or set(st) <= set("| "):
                continue
        out.append(line)
    body = "\n".join(out)

    # Strip prose that points at the (now-removed) machine section.
    body = re.sub(r'\s*See [\u201c"]New relationships discovered[\u201d"][^.\n]*\.', "", body)

    # Parentheticals that only reference the machine graph.
    body = re.sub(r"\s*\(\s*(?:the\s+)?(?:power-)?graph edge[^)]*\)", "", body, flags=re.I)

    # Inline graph-edge tokens mid-sentence → readable gloss, keeping the sentence
    # grammatical. e.g. "The power-graph edge `hdcc → ryan-mello, donated, weight=6`
    # shows …" → "The graph edge shows …". Tokens may be bare or backticked.
    tok = r"(?:`?)"
    body = re.sub(
        r"(?i)\bthe\s+(?:power-)?graph(?:'s)?\s+`?[a-z0-9-]+\s*→\s*[a-z0-9-]+"
        r"(?:\s*,\s*[a-z_/]+)?(?:\s*,\s*weight=\d+)?`?\s+edge",
        "The graph edge", body)
    body = re.sub(
        r"(?i)\bthe\s+(?:power-)?graph\s+edge[:\s]+`?[a-z0-9-]+\s*→\s*[a-z0-9-]+"
        r"(?:\s*,\s*[a-z_/]+)?(?:\s*,\s*weight=\d+)?`?",
        "The graph edge", body)
    body = re.sub(
        r"(?i)\bgraph\s+edge[:\s]+`?[a-z0-9-]+\s*→\s*[a-z0-9-]+"
        r"(?:\s*,\s*[a-z_/]+)?(?:\s*,\s*weight=\d+)?`?",
        "The graph edge", body)

    # De-jargon: internal build-path citations and node-id parentheticals.
    body = re.sub(r"\bGraph connections\s*(?:\([^)]*\))?\s*:", "Connections:", body)
    body = re.sub(r"`evidence/\d[^`]*`", "the case evidence file", body)
    body = re.sub(r"\bevidence/\d[0-9a-z._-]+\.(?:json|md)\b", "the case evidence file", body)
    body = re.sub(r"\s*\(\s*path:\s*[^)]*\)", "", body, flags=re.I)
    body = re.sub(r"\s*\(not yet in graph\)", "", body, flags=re.I)
    body = re.sub(r"\s*\(`[a-z0-9][a-z0-9-]*`\)", "", body)

    # Workflow/provenance metadata that leaked into body prose (it belongs to the
    # research process, not the reader). The frontmatter already carries it; the
    # body duplicate is dropped. The verification record is preserved as a clean
    # line — with the internal chunk reference removed — because the automated-
    # research disclosure is material to the evidence standard.
    body = re.sub(r"^\s*(?:-\s*)?\*{0,2}Status:?\*{0,2}\s*(?:\u2705\s*)?researched\b[^\n]*\n?", "", body, flags=re.M)
    body = re.sub(
        r"^\s*(?:-\s*)?\*{0,2}VERIFIED stamp:\*{0,2}\s*N/A[^\n]*\n?", "", body, flags=re.M)
    body = re.sub(
        r"^\s*(?:-\s*)?\*{0,2}VERIFIED stamp:\*{0,2}\s*(\d{4}-\d{2}-\d{2})\s*[\u2014-]\s*"
        r"tier\d+-chunk\d+[a-z-]*(?:\s+\w+)?\s*(?:\(([^)]*)\))?[.\s]*\n?",
        lambda m: f"**Verification:** research pass {m.group(1)}"
                  f"{' (' + m.group(2) + ')' if m.group(2) else ''}.\n",
        body, flags=re.M)
    body = re.sub(r"^\s*(?:-\s*)?\*{0,2}Verification:\*{0,2}.*$", lambda m: m.group(0), body, flags=re.M)  # keep ours
    body = re.sub(r"^-\s*\(none yet\)\s*$\n?", "", body, flags=re.M)
    body = re.sub(r"\*{0,2}Analysis of alternatives:\*{0,2}\s*None warranted\.?\s*", "", body)
    body = re.sub(r"\bThe stub file\b", "An earlier record", body)
    body = re.sub(r"\bthe original stub file\b", "an earlier record", body)
    body = re.sub(r"\bThe stub records\b", "An earlier record lists", body)
    body = re.sub(r"\bThe stub had\b", "An earlier record had", body)
    body = re.sub(r"\bThe stub\b", "An earlier record", body)
    body = re.sub(r"\bthe stub\b", "an earlier record", body)
    body = re.sub(r"\btier3 stub\b", "basic reference profile", body)
    body = re.sub(r"\bstub title\b", "earlier file's title", body)
    body = re.sub(r"\bstub file title\b", "earlier file's title", body)
    body = re.sub(r"That is flagged in the Graph description above\.", "That is flagged in the entity summary.", body)

    return body


def autolink_html(html: str) -> str:
    """Wrap bare http(s) URLs in <a> anchors (inside text nodes only).

    python-markdown does not autolink, so bare URLs ship as dead text. This
    pass runs AFTER markdown rendering and skips anything inside existing
    tags/attributes (split on tags, transform text segments only).
    """
    parts = re.split(r"(<[^>]+>)", html)
    url_re = re.compile(r"""https?://[^\s<>"')\]]+""")
    for i, seg in enumerate(parts):
        if seg.startswith("<"):
            continue
        parts[i] = url_re.sub(lambda m: f'<a href="{m.group(0)}" target="_blank" rel="noopener">{m.group(0)}</a>', seg)
    return "".join(parts)


def _render_source_url_cells(html: str) -> str:
    """Inside the sources table, link the URL column and shorten visible text.

    Sources tables carry long bare URLs in the URL column; autolink fixes the
    dead-text problem but a 90-char URL still bloats the cell, so visible text
    becomes a compact label: domain + /…/tail.
    """
    tag_re = re.compile(r"(<td>[^<]*)(https?://[^\s<>\"]+)([^\s<>\"]*)(</td>)")

    def _shorten(m: re.Match) -> str:
        url = m.group(2) + m.group(3)
        shown = url if len(url) <= 48 else url[:46] + "…"
        return f'{m.group(1)}<a href="{url}" target="_blank" rel="noopener">{shown}</a>{m.group(4)}'

    return tag_re.sub(_shorten, html)


def _render_prose_links(html: str) -> str:
    """Trim visible text of mid-prose autolinks to host + short path.

    In running sentences the full URL is noise: https://en.wikipedia.org/wiki/Ryan_Mello
    reads better as wikipedia.org/wiki/Ryan_Mello, still one click from the full address.
    """
    def _trim(m: re.Match) -> str:
        url, shown = m.group(1), m.group(2)
        if shown != url:
            return m.group(0)   # hand-written anchor text — keep as authored
        if len(shown) > 60:
            host = re.sub(r"^https?://", "", shown)
            parts = [p for p in host.split("/") if p]
            shown = "/".join(parts) if len(shown) <= 80 else (host if len(host) <= 40 else "/".join(parts[:2]) + "/…")
        return f'<a href="{url}" target="_blank" rel="noopener">{shown}</a>'

    return re.sub(r'<a href="(https?://[^"]+)"[^>]*>([^<]+)</a>', _trim, html)


def render_profile_html(pid):
    """Render profiles/<pid>.md → HTML fragment: strip metadata + machine blocks, then
    apply the plain-English readability transform (checkbox strip, header normalization,
    acronym expansion, academic-citation removal). Returns '' if unresearched."""
    path = os.path.join(PROFILES_DIR, f"{pid}.md")
    if not os.path.exists(path):
        return ""
    txt = open(path, encoding="utf-8").read()
    if "✅ researched" not in txt:
        return ""
    # 1. drop the frontmatter metadata header (everything through the first '---' line)
    parts = txt.split("\n---\n", 1)
    body = parts[1] if len(parts) == 2 else txt
    # 2. readability transform (deterministic). Note: no whole-block cut here —
    #    machine syntax is stripped line-by-line in _strip_edge_machine_lines so
    #    content that FOLLOWS a machine heading (sources tables, assessments) is
    #    preserved. The canonical profiles/*.md remain untouched.
    body = _strip_checkboxes(body)
    body = _strip_edge_machine_lines(body)
    body = _resolve_cross_references(body)
    body = _normalize_headers(body)
    body = _expand_acronyms(body)
    body = _strip_academic_cites(body)
    # 3. render markdown → html (tables for sources, fenced code, sane lists)
    html = markdown.markdown(body, extensions=["tables", "fenced_code", "sane_lists"])
    # 4. link integrity (audit finding): sources-table URLs and bare prose URLs
    #    become real anchors so no citation ships as dead text. ORDER MATTERS:
    #    autolink first would re-wrap URLs that _render_source_url_cells already
    #    anchored (nested-<a> is invalid HTML) — so compact cells, autolink the
    #    remaining text nodes, then compact mid-prose link text.
    html = autolink_html(html)
    html = _render_source_url_cells(html)
    html = _render_prose_links(html)
    return html
