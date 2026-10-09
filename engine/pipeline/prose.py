"""Deterministic readability transforms for profile prose (config-driven).

Ports the four render-time transforms that were hard-coded inside
build_power_network.py, sourcing the section titles and acronyms from site config
so they stop drifting. Pure functions: markdown text in, cleaned markdown out.

Transforms:
  1. strip checkbox markers ([x] / [ ]) that leak into prose
  2. normalize section headers  `## 0` / `## §3a` → plain-English titled headers
  3. expand acronyms on first use per profile (config `acronyms`)
  4. strip academic name-drops (Laumann/Marsden/Domhoff/etc.) from prose
  5. strip machine-facing edge lines + "New relationships" blocks
"""
from __future__ import annotations

import re

# Academic scaffolding stripped from reader prose; the Sources table + methodology
# keep the real citations. (Stable, not config — these are analytic-tradecraft noise.)
_ACADEMIC_AUTHORS = (
    r"Laumann|Marsden|Prensky|Domhoff|Mills|Hunter|Dahl|Stone|Logan|Molotch|"
    r"Bourdieu|Foucault|Lukes|Galbraith|Freeman|Bonacich|Brin|Page|Wasserman|Faust"
)


def strip_checkboxes(body: str) -> str:
    return re.sub(r"^\s*[-*]\s*\[[ xX]\]\s*", "- ", body, flags=re.MULTILINE)


def normalize_headers(body: str, sections: dict[str, str]) -> str:
    # '§N Title' → 'N. Title'
    body = re.sub(r"^##\s*§(\d+[a-z]?)\s*(.*)$", r"## \1. \2", body, flags=re.MULTILINE)

    def repl(m: re.Match) -> str:
        num = m.group(1).lower()
        title = sections.get(num)
        if title:
            return f"## {m.group(1)}. {title}"
        return m.group(0)

    return re.sub(r"^##\s*(\d+[a-z]?)\s*[.:]?\s*(.*)$", repl, body, flags=re.MULTILINE)


def expand_acronyms(body: str, acronyms: list[list[str]]) -> str:
    for acr, full in acronyms:
        pattern = re.compile(rf"\b{re.escape(acr)}\b")
        if pattern.search(body):
            body = pattern.sub(f"{acr} ({full})", body, count=1)
    return body


def strip_academic_cites(body: str) -> str:
    body = re.sub(
        rf"\s*\([^()]*(?:{_ACADEMIC_AUTHORS}|whorulesamerica|ICD 20[0-9]|"
        rf"Verification Handbook|Silverman|EJC)[^()]*\)", "", body)
    body = re.sub(
        rf"\b(?:Laumann/Marsden/Prensky|Laumann, Marsden & Prensky|Laumann|Marsden|Prensky)"
        rf"(?:\s*[0-9]{{4}})?\s*(?:positional|decisional|reputational|relational)?\s*"
        rf"(?:criterion|criteria|framework|inclusion)?\s*:?", "", body)
    body = re.sub(r"\bDomhoff\s*(?:'s)?\s*(?:framework)?\s*", "", body)
    body = re.sub(r"[\u201c\"](?:Who benefits / Who governs|Who benefits|Who governs)[\u201d\"]\s*", "", body)
    body = re.sub(r"\bICD\s*20[0-9]\b", "", body)
    body = re.sub(r"\b(?:whorulesamerica\.ucsc\.edu|Verification Handbook|Silverman/EJC|Silverman|EJC)\b", "", body)
    return re.sub(r" {2,}", " ", body)


def strip_edge_machine_lines(body: str) -> str:
    out = []
    for line in body.split("\n"):
        s = line.strip()
        if re.match(r"^[-*]\s*edge:\s*source=", s):
            continue
        if re.match(r"^[-*]\s*\*\*(?:New edges|New relationships)[^*]*\*\*", s):
            continue
        if re.match(r"^[-*]\s*(?:New edges|New relationships)[^:]*:", s):
            continue
        if re.match(r"^\*\*(?:New edges|New relationships)[^*]*\*\*[:\s]*$", s):
            continue
        out.append(line)
    body = "\n".join(out)
    body = re.sub(r'\s*See [\u201c"](?:New relationships discovered)[\u201d"][^.\n]*\.', "", body)
    return body


def clean_prose(body: str, sections: dict[str, str], acronyms: list[list[str]]) -> str:
    """Full deterministic pass. Order matters (strip edges before header normalize)."""
    body = strip_checkboxes(body)
    body = strip_edge_machine_lines(body)
    body = normalize_headers(body, sections)
    body = expand_acronyms(body, acronyms)
    body = strip_academic_cites(body)
    return body
