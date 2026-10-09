#!/usr/bin/env python3
"""case2hub.py — derive per-case site artifacts from canonical case files.

Single source of truth: `cases/<slug>/<slug>.md` frontmatter (+ Case Summary /
Key Questions sections). Everything else in the published site is DERIVED and
must byte-match a re-derivation (CI enforces this):

  cards/<slug>.html   dossier card for the case (approved cases only)
  site/index.html     master index (approved cases only)

Approved means frontmatter `publish.approved: true`. Unapproved cases never
appear in the site or the README — source is mirrored to the repo, rendered
pages are not (until approved).

Usage:
  case2hub.py build   <repo>            # repo = monorepo root (cases/, cards/, site/)
  case2hub.py selftest <repo>           # re-derive and byte-compare (same as CI)
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
KEY_RE = re.compile(r"^([a-z_]+):\s*(.*)$")


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no YAML frontmatter found")
    meta: dict = {}
    list_key = None
    for line in m.group(1).splitlines():
        if line.startswith(("  - ", "- ")):  # list item under previous key or inline tags
            item = line.strip()[2:].strip().strip('"')
            if list_key:
                meta[list_key].append(item)
            continue
        km = KEY_RE.match(line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        list_key = None
        if val.startswith("[") and val.endswith("]"):
            items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(",") if x.strip()]
            meta[key] = items
        elif val == "":
            meta[key] = []
            list_key = key
        else:
            meta[key] = val.strip('"').strip("'")
    # sub-dict: publish: (list_key style) with approved/published_at lines
    pub = meta.get("publish")
    if isinstance(pub, list):
        flags = {}
        for item in pub:
            if ":" in item:
                k, v = item.split(":", 1)
                flags[k.strip()] = v.strip()
        meta["publish"] = flags
    elif pub is None:
        meta["publish"] = {}
    return meta


def parse_publish_block(text: str) -> dict:
    """Read a `publish:` frontmatter sub-block written in expanded YAML form:
    publish:\n  approved: true\n  published_at: ...\n"""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    flags: dict = {}
    in_pub = False
    for line in m.group(1).splitlines():
        s = line.strip()
        if re.match(r"^publish:\s*$", s):
            in_pub = True
            continue
        if in_pub:
            if line.startswith(" ") or line.startswith("\t"):
                if ":" in s:
                    k, v = s.split(":", 1)
                    flags[k.strip()] = v.strip()
            else:
                in_pub = False
    return flags


def approved(text: str) -> bool:
    flags = parse_publish_block(text)
    if not flags:
        # fallback: inline publish: [approved: true, ...] handled by parse_frontmatter
        try:
            meta = parse_frontmatter(text)
            flags = meta.get("publish", {}) if isinstance(meta.get("publish"), dict) else {}
        except ValueError:
            flags = {}
    return str(flags.get("approved", "false")).strip().lower() in ("true", "yes", "1")


def extract_section(text: str, header_re: str) -> str:
    m = re.search(header_re, text)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"\n## ", text[start:])
    end = start + nxt.start() if nxt else len(text)
    return text[start:end].strip()


def inline_html(md: str) -> str:
    t = html.escape(md)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def discover_cases(repo: Path) -> list[Path]:
    """cases/<slug>/<slug>.md with frontmatter case_id — the canonical set."""
    out = []
    for d in sorted((repo / "cases").iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        canonical = d / f"{d.name}.md"
        if canonical.exists():
            out.append(canonical)
    return out


def build_card(case_md: Path) -> str:
    text = case_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    slug = meta.get("slug") or case_md.parent.name
    summary = extract_section(text, r"\n#+ Case Summary\s*\n")
    questions = extract_section(text, r"\n#+ Key Questions\s*\n")
    qlist = ""
    for q in [x for x in questions.splitlines() if re.match(r"^\d+\.", x.strip())]:
        clean = re.sub(r"^\d+\.\s*", "", q).strip()
        qlist += f"<li>{inline_html(clean)}</li>"
    summary_first = re.split(r"\n\n", summary)[0] if summary else ""
    summary_html = " ".join(inline_html(p) for p in summary_first.splitlines() if p.strip())
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tagchips = "".join(f'<span class="chip">{html.escape(str(t))}</span>' for t in tags)
    pub = parse_publish_block(text)
    published_at = pub.get("published_at", "")
    gh_src = f"https://github.com/moliver28/investigations/blob/main/cases/{slug}/{slug}.md"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(str(meta.get('title', slug)))}</title>
<link rel="stylesheet" href="../style.css"></head>
<body>
<main class="card">
<p class="backlink"><a href="../index.html">&larr; Investigation Index</a></p>
<p class="caseid">{html.escape(str(meta.get('case_id', '')))}</p>
<h1>{html.escape(str(meta.get('title', slug)))}</h1>
<p class="meta">Status: <strong>{html.escape(str(meta.get('status', 'unknown')))}</strong>
 &middot; Priority: {html.escape(str(meta.get('priority', '—')))}
 &middot; Type: {html.escape(str(meta.get('type', '—')))}
 &middot; Opened: {html.escape(str(meta.get('date_opened', '—')))}
 &middot; Updated: {html.escape(str(meta.get('last_updated', '—')))}</p>
<div class="tags">{tagchips}</div>
<section><h2>Summary</h2><p>{summary_html}</p></section>
{f'<section><h2>Key questions</h2><ol>{qlist}</ol></section>' if qlist else ''}
<section class="links">
<h2>Record</h2>
<ul>
<li><a href="{gh_src}">Case file source (GitHub)</a></li>
{f'<li><a href="../assets/network/{slug}/index.html">Interactive network map</a></li>' if (case_md.parent / 'evidence' / 'network' / 'index.html').exists() else ''}
{f'<li>Published: {html.escape(published_at)}</li>' if published_at else ''}
</ul>
</section>
</main>
</body></html>
"""


def build_index(repo: Path, rows: list[dict]) -> str:
    hub_cfg = {}
    cfgp = repo / "engine" / "config" / "hub.json"
    if cfgp.exists():
        hub_cfg = json.loads(cfgp.read_text(encoding="utf-8"))
    title = hub_cfg.get("title", "Investigation Index")
    tagline = hub_cfg.get("tagline", "Published investigations — evidence-first, source-linked.")
    items = []
    for r in sorted(rows, key=lambda r: r.get("last_updated", ""), reverse=True):
        items.append(
            f'<li><span class="date">{html.escape(str(r.get("last_updated", ""))[:10])}</span> '
            f'<a href="cards/{r["slug"]}.html">{html.escape(str(r.get("title", r["slug"])))}</a> '
            f'<span class="cid">{html.escape(str(r.get("case_id", "")))}</span></li>'
        )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="style.css"></head>
<body>
<main>
<h1>{html.escape(title)}</h1>
<p class="tagline">{html.escape(tagline)}</p>
<ul class="index">
{chr(10).join(items)}
</ul>
<p class="foot">Generated from case files — every entry links to its source on GitHub.</p>
</main>
</body></html>
"""


def collect_rows(repo: Path) -> list[dict]:
    rows = []
    for case_md in discover_cases(repo):
        text = case_md.read_text(encoding="utf-8")
        if not approved(text):
            continue
        meta = parse_frontmatter(text)
        slug = case_md.parent.name
        if meta.get("slug") != slug:
            raise SystemExit(f"MECE: frontmatter slug {meta.get('slug')!r} != folder {slug!r}")
        rows.append({
            "case_id": meta.get("case_id", ""),
            "title": meta.get("title", ""),
            "slug": slug,
            "status": meta.get("status", ""),
            "last_updated": meta.get("last_updated", ""),
        })
    return rows


def write_site(repo: Path) -> dict:
    rows = collect_rows(repo)
    cards_dir = repo / "site" / "cards"
    cards_dir.mkdir(parents=True, exist_ok=True)
    approved_slugs = {r["slug"] for r in rows}
    # MECE cleanup: cards of cases no longer approved must not survive on disk
    for stale in cards_dir.glob("*.html"):
        if stale.stem not in approved_slugs:
            stale.unlink()
    written = []
    for case_md in discover_cases(repo):
        text = case_md.read_text(encoding="utf-8")
        if not approved(text):
            continue
        card = build_card(case_md)
        p = cards_dir / f"{case_md.parent.name}.html"
        p.write_text(card, encoding="utf-8")
        written.append(str(p.relative_to(repo)))
    (repo / "site" / "index.html").write_text(build_index(repo, rows), encoding="utf-8")
    # network bundle copies (approved engine-path cases only)
    assets = repo / "site" / "assets" / "network"
    assets.mkdir(parents=True, exist_ok=True)
    for case_md in discover_cases(repo):
        text = case_md.read_text(encoding="utf-8")
        if not approved(text):
            continue
        src = case_md.parent / "evidence" / "network"
        if src.exists():
            dst = assets / case_md.parent.name
            copytree_newer(src, dst)
    # registry.json (all registered cases — published or not, no secrets)
    reg = []
    for case_md in discover_cases(repo):
        meta = parse_frontmatter(case_md.read_text(encoding="utf-8"))
        reg.append({
            "case_id": meta.get("case_id", ""),
            "title": meta.get("title", ""),
            "slug": case_md.parent.name,
            "status": meta.get("status", ""),
            "priority": meta.get("priority", ""),
            "type": meta.get("type", ""),
            "date_opened": meta.get("date_opened", ""),
            "last_updated": meta.get("last_updated", ""),
            "tags": meta.get("tags", []),
            "notion_url": meta.get("notion_url", None),
            "approved": approved(case_md.read_text(encoding="utf-8")),
        })
    (repo / "site" / "registry.json").write_text(
        json.dumps({"cases": reg}, indent=2, sort_keys=False) + "\n", encoding="utf-8"
    )
    return {"rows": rows, "written": written, "registry": reg}


def copytree_newer(src: Path, dst: Path) -> None:
    import shutil
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))


def selftest(repo: Path) -> int:
    """Re-derive every derived artifact from case sources; byte-compare. CI parity."""
    rows = collect_rows(repo)
    problems = []
    for case_md in discover_cases(repo):
        text = case_md.read_text(encoding="utf-8")
        slug = case_md.parent.name
        if approved(text):
            p = repo / "site" / "cards" / f"{slug}.html"
            if not p.exists():
                problems.append(f"{slug}: approved but card missing")
            else:
                want = build_card(case_md)
                if p.read_text(encoding="utf-8") != want:
                    problems.append(f"{slug}: card.html drift (re-run publish.py build)")
        else:
            p = repo / "site" / "cards" / f"{slug}.html"
            if p.exists():
                problems.append(f"{slug}: MECE — unapproved case has a published card")
    want_index = build_index(repo, rows)
    got_index = repo / "site" / "index.html"
    if not got_index.exists():
        problems.append("site/index.html missing")
    elif got_index.read_text(encoding="utf-8") != want_index:
        problems.append("site/index.html drift vs re-derivation")
    # MECE on case_ids
    ids = [r["case_id"] for r in collect_rows(repo)]
    if len(ids) != len(set(ids)):
        problems.append("duplicate case_id among approved cases")
    # README parity is checked by publish.py selftest (README generated there)
    for pr in problems:
        print("FAIL", pr)
    if not problems:
        print("case2hub selftest: PASS", f"({len(rows)} published cases)")
    return 0 if not problems else 1


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, repo = argv[0], Path(argv[1]).resolve()
    if cmd == "build":
        out = write_site(repo)
        print(f"case2hub: built {len(out['written'])} cards + index ({len(out['rows'])} published)")
        return 0
    if cmd == "selftest":
        return selftest(repo)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))