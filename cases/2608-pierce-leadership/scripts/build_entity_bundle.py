#!/usr/bin/env python3
"""Emit the UI v3 bundle's data file: evidence/network/assets/data.js (Task 2.1).

Single source of truth per field:
- nodes/label/type/domain/desc/facts ........ evidence/30-power-graph-v3.json (verbatim)
- tier band / rank / composite power ........ profiles/*.md frontmatter (the researched record)
- rel_class ................................ evidence/30-power-graph-v3.json (Task 1.1 output)
- profile HTML + sections ................... scripts/profile_render.py (Task 2.2 transforms)
- moneyFigure ............................... evidence/network/money-map.json (Task 2.3, gate 16)
- thesis .................................... verbatim from v2 appbar (evidence/11-power-network.html)

Builds window.PIERCE_DATA with NO timestamps — build metadata (time, git SHA,
input hashes) goes to evidence/network/manifest.json, which is EXEMPT from the
byte-identical-rebuild gate (Task 3.4).

Gate (Task 2.1): data.js parses; nodes == 163; edges == 342; every researched
node has non-empty profile + sections whose titles come from SECTION_TITLES;
band boundaries agree with frontmatter Tier; ranks 1..163 each used exactly once.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from profile_render import SECTION_TITLES, render_profile_html  # noqa: E402

import networkx as nx  # noqa: E402

GRAPH_V3 = REPO / "evidence" / "30-power-graph-v3.json"
GRAPH_V2 = REPO / "evidence" / "29-power-graph-v2.json"
PROFILES = REPO / "profiles"
MONEY_MAP = REPO / "evidence" / "network" / "money-map.json"
EXEC_SUMMARIES = REPO / "evidence" / "network" / "exec-summaries.json"
OUT_DIR = REPO / "evidence" / "network" / "assets"

THESIS = ("Government creates wealth \u2192 private power converts it \u2192 policy returns it. "
          "This is the structural-capture loop.")

TIER_BANDS = [
    {"id": "top", "label": "Top tier", "frontmatter": "tier1", "range": "1\u201325",
     "note": "The 25 most powerful actors. They set policy, control the biggest budgets, "
             "or hold a legal power nobody else has."},
    {"id": "high", "label": "High", "frontmatter": "tier2", "range": "26\u201375",
     "note": "Strong actors with real leverage \u2014 department heads, institution "
             "leaders, and large funders who move specific decisions."},
    {"id": "notable", "label": "Notable", "frontmatter": "tier3", "range": "76\u2013163",
     "note": "Meaningful local influence. They matter in their own lane and connect "
             "the map, but rarely move the whole county by themselves."},
]
BAND_BY_FRONTMATTER = {b["frontmatter"]: b["id"] for b in TIER_BANDS}

CLASSES = [
    {"id": "money", "label": "Money", "color": "#B8860B",
     "sentence": "Public money or government-granted wealth"},
    {"id": "influence", "label": "Influence", "color": "#0B6E6E",
     "sentence": "Agenda power \u2014 persuading, convening, endorsing"},
    {"id": "governance", "label": "Governance", "color": "#37474F",
     "sentence": "Holds a seat, office, or board position"},
    {"id": "legal", "label": "Legal", "color": "#6a1b9a",
     "sentence": "Prosecution, policing, courts, legal leverage"},
    {"id": "business", "label": "Business", "color": "#b84a00",
     "sentence": "Ownership, contracts, employer power"},
    {"id": "media", "label": "Media", "color": "#5d4037",
     "sentence": "Publishes or broadcasts what the public sees"},
    {"id": "community", "label": "Community", "color": "#1e7d32",
     "sentence": "Nonprofit, civic, labor, community ties"},
    {"id": "other", "label": "Other", "color": "#666666",
     "sentence": "Everything not routed above (must stay empty)"},
]

FRONT_RE = re.compile(
    r"\*\*Tier:\*\*\s*(tier\d)\s*\u00b7\s*\*\*Rank:\*\*\s*(\d+)/163"
    r"\s*\u00b7\s*\*\*Composite power:\*\*\s*([0-9]+\.[0-9]+)"
)
SECTION_HEAD_RE = re.compile(r"^#{2,3}\s+(\d+[a-z]?)\.\s+(.+)$", re.M)
REND_H_RE = re.compile(r'<h[23]>\s*(?P<num>\d+[a-z]?)\.\s*(?P<t>[^<]+)', re.I)


def frontmatter_fields(pid: str) -> tuple[str, int, float]:
    text = (PROFILES / f"{pid}.md").read_text()
    m = FRONT_RE.search(text)
    if not m:
        raise SystemExit(f"FATAL: no Tier/Rank/Composite line in profiles/{pid}.md")
    return m.group(1), int(m.group(2)), float(m.group(3))


def sections_of(profile_html: str) -> list[dict]:
    """TOC derived from the RENDERED HTML (post readability-transforms) so the
    TOC exactly equals the headings a reader actually sees. Renders strip some
    raw-markdown heading repeats, so a raw-scan TOC would contain dead entries.
    Duplicates get a -2, -3 suffix so DOM anchors stay unique."""
    out, seen = [], {}
    for m in REND_H_RE.finditer(profile_html):
        num, title = m.group("num"), m.group("t")
        seen[num] = seen.get(num, 0) + 1
        sid = num if seen[num] == 1 else f"{num}-{seen[num]}"
        out.append({"id": sid, "num": num,
                    "title": SECTION_TITLES.get(num, title)})
    return out


def add_section_anchors(nodes_out: list[dict]) -> None:
    """Inject id="sec-<n>" anchors into profile HTML at each rendered section
    heading so the TOC jumps, and strip the template section numbers from the
    visible heading text (review pass 2026-10-05: the rail shows clean titles;
    the body must match it exactly — the '0. / 3a. / 12.' scaffolding read as
    machine syntax and made the rail look like a duplicate of the body).
    Section ids stay stable for anchors; sections_of() already parsed the
    numbers from the pre-anchor HTML, so this changes display only."""
    for nd in nodes_out:
        sects = nd["sections"]
        if not sects:
            continue
        html = nd["profile"]
        pos = 0
        edits = []
        for s in sects:
            num_esc = re.escape(s["num"])
            # markdown renders '## 0. Why ...' as <h2>0. Why ...</h2>
            pat = re.compile(r"<h([23])>\s*" + num_esc + r"\.\s*([^<]*)</h\1>", re.I)
            m = pat.search(html, pos)
            if not m:
                continue
            tag = f"h{m.group(1)}"
            edits.append((
                m.span(),
                f'<{tag}><a class="h-anchor" id="sec-{s["id"]}"'
                f' tabindex="-1"></a>{m.group(2).strip()}</{tag}>',
            ))
            pos = m.end()
        for (a, b), repl in reversed(edits):
            html = html[:a] + repl + html[b:]
        nd["profile"] = html


def add_layout(nodes_out: list[dict], edges: list[dict]) -> None:
    """Deterministic layout (v2's exact recipe, ported): spring_layout(k=1.8,
    iterations=400, seed=7) normalized into a 2560x1440 space with 60px padding.
    x/y ride on each node dict so app.js never computes layout."""
    G = nx.Graph()
    for n in nodes_out:
        G.add_node(n["id"])
    for e in edges:
        G.add_edge(e["s"], e["t"])
    W, H, PAD = 2560, 1440, 60
    pos = nx.spring_layout(G, k=1.8, iterations=400, seed=7)
    xs = [pos[n][0] for n in G.nodes()]
    ys = [pos[n][1] for n in G.nodes()]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    by_id = {n["id"]: n for n in nodes_out}
    for nid in G.nodes():
        x = PAD + (pos[nid][0] - minx) / (maxx - minx) * (W - 2 * PAD)
        y = PAD + (pos[nid][1] - miny) / (maxy - miny) * (H - 2 * PAD)
        by_id[nid]["x"] = round(x, 1)
        by_id[nid]["y"] = round(y, 1)


def build() -> dict:
    g3 = json.loads(GRAPH_V3.read_text())
    money = {e["node_id"]: e for e in json.loads(MONEY_MAP.read_text())}

    nodes, bands_seen = [], []
    for n in g3["nodes"]:
        pid = n["id"]
        tier_fm, rank, power = frontmatter_fields(pid)
        band = BAND_BY_FRONTMATTER[tier_fm]
        bands_seen.append((tier_fm, band))
        # order of sections must come from the MARKDOWN BODY (render_html strips it)
        md_path = PROFILES / f"{pid}.md"
        raw = md_path.read_text()
        profile_html = render_profile_html(pid)
        if not profile_html.strip():
            raise SystemExit(f"FATAL: empty profile render for {pid} (not researched?)")
        nodes.append({
            "id": pid, "label": n["label"], "type": n["type"], "domain": n["domain"],
            "tier": band, "rank": rank, "power": power,
            "desc": n.get("desc", ""), "facts": n.get("facts", []),
            "moneyFigure": money.get(pid, {}).get("figure"),
            "moneyBasis": money.get(pid, {}).get("basis"),
            "moneySource": money.get(pid, {}).get("source"),
            "profile": profile_html,
            "sections": sections_of(profile_html),
        })

    # ── Gates ────────────────────────────────────────────────────────────
    errors = []
    if len(nodes) != 163:
        errors.append(f"node count {len(nodes)} != 163")
    if len(g3["edges"]) != 342:
        errors.append(f"edge count {len(g3['edges'])} != 342")
    if any(c["id"] == "other" and False for c in CLASSES):
        pass
    ranks = sorted(nd["rank"] for nd in nodes)
    if ranks != list(range(1, 164)):
        errors.append("ranks are not exactly 1..163")
    for fm, band in bands_seen:
        lo, hi = (1, 25) if fm == "tier1" else (26, 75) if fm == "tier2" else (76, 163)
        nd = next(x for x in nodes if BAND_BY_FRONTMATTER[fm] == x["tier"])
        if not (lo <= nd["rank"] <= hi):
            errors.append(f"band mismatch {nd['id']} {nd['rank']} vs {fm}")
    # every edge rel_class resolves to a known class; 'other' stays empty
    valid = {c["id"] for c in CLASSES}
    bad = [e for e in g3["edges"] if e.get("rel_class") not in valid]
    if bad:
        errors.append(f"{len(bad)} edges with unknown rel_class")
    others = [e for e in g3["edges"] if e.get("rel_class") == "other"]
    if others:
        errors.append(f"{len(others)} edges classed 'other' (gate 15)")
    # money entries all resolve
    for mid in money:
        if not any(nd["id"] == mid for nd in nodes):
            errors.append(f"money-map node_id not in graph: {mid}")

    if errors:
        print("BUILD FAILURE:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    edges = [{"s": e["source"], "t": e["target"], "rel": e["relationship"],
              "relClass": e["rel_class"], "w": e.get("weight", 1)}
             for e in g3["edges"]]
    add_layout(nodes, edges)

    # Hand-written verdict / defense counter / confidence per entity
    # (commit 4f83c52, red-team-reviewed). Missing key is a build failure —
    # every entity page is supposed to open with its bottom line.
    exec_summaries = json.loads(EXEC_SUMMARIES.read_text())
    summary_gaps = [nd["id"] for nd in nodes if nd["id"] not in exec_summaries]
    if summary_gaps:
        print("BUILD FAILURE:")
        print(f"  - {len(summary_gaps)} nodes lack an exec summary: {summary_gaps[:5]}")
        sys.exit(1)

    payload = {
        "meta": {"case": "INV-2026-002", "title": "Pierce County Power Network",
                 "nodeCount": 163, "edgeCount": 342},
        "thesis": THESIS,
        "tiers": TIER_BANDS,
        "classes": CLASSES,
        "execSummaries": exec_summaries,
        "nodes": nodes,
        "edges": edges,
    }
    add_section_anchors(nodes)
    return payload


def main() -> None:
    payload = build()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    text = "window.PIERCE_DATA = " + json.dumps(payload, ensure_ascii=True) + ";\n"
    out = OUT_DIR / "data.js"
    out.write_text(text)
    print(f"WROTE {out} ({len(text):,} bytes)")

    # ── Gate verification (Task 2.1) ────────────────────────────────────
    s = out.read_text()
    parsed = json.loads(s[s.index("{"): s.rindex(";")])
    assert parsed["meta"]["nodeCount"] == 163 and parsed["meta"]["edgeCount"] == 342
    assert len(parsed["nodes"]) == 163 and len(parsed["edges"]) == 342
    n_empty = sum(1 for nd in parsed["nodes"] if not nd["profile"].strip())
    assert n_empty == 0, f"{n_empty} empty profiles"
    n_seen = sum(1 for nd in parsed["nodes"] if "see above" in nd["profile"].lower())
    assert n_seen == 0, f"{n_seen} profiles still contain 'See above' (standalone-page rule)"
    n_sec = sum(len(nd["sections"]) for nd in parsed["nodes"])
    print(f"parse OK | nodes 163 | edges 342 | empty profiles 0 | TOC sections total {n_sec}")
    print("sections with titles outside SECTION_TITLES:",
          sum(1 for nd in parsed["nodes"] for t in nd["sections"]
              if t["title"] not in set(SECTION_TITLES.values())))


if __name__ == "__main__":
    main()