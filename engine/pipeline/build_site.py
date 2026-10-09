"""Stage 5: config-driven HTML renderer (pure function, zero hard-coded case data).

Replaces the monolithic build_power_network.py with a deterministic renderer that
reads (graph JSON + profiles/*.md + site config) and emits self-contained SVG+JS HTML.

Every presentation decision — domain colors/shapes/labels, relationship taxonomy,
section titles, acronyms, thesis copy, mission text, node/edge counts, top-actor
names, money nodes — is sourced from config or computed from the graph at build time.
Nothing about the *specific case* is a Python literal here. Node/edge counts and
ranking names are substituted from data, so they can never drift out of sync.

Usage:
  python3 -m pipeline.build_site GRAPH_JSON SITE_JSON OUT_HTML
"""
from __future__ import annotations

import json
import math
import os
import re
import sys

import networkx as nx
import markdown

from . import prose
from .power import build_graph, compute_power


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _fmt(x) -> str:
    """Render a number without trailing '.0' (12.5 stays 12.5; 22.0 becomes 22)."""
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


def _apply_theme(html: str, C: dict, rail_w, drawer_w) -> str:
    """Post-process the rendered HTML with config-driven theme tokens.

    Idempotent: the DEFAULT token values reproduce the prior hard-coded output
    byte-for-byte, so a site.json with no `theme` block renders identically to
    before this feature existed. Only non-default values change the output.
    This keeps the renderer a pure function while letting readability/color
    changes be made in config without touching Python.

    (Font sizes and spacing are injected directly into the CSS/JS f-strings;
    this pass handles only the hex-color literals and panel widths, which are
    scattered across SVG, inline styles, and JS strings.)
    """
    # Accent + highlight appear throughout the JS/SVG as hex literals.
    html = html.replace("#B8860B", C["accent"]).replace("#E8C547", C["highlight"])
    # Page background (SVG canvas + body both use #fafafa lowercase).
    html = html.replace("#fafafa", C["page_bg"])
    # Surface / ink / border / text / muted / money-chip / link colors.
    html = html.replace("#FAFAFA", C["surface"]).replace("#1B1B1B", C["ink"])
    html = html.replace("#E0E0E0", C["border"]).replace("#1a1a1a", C["text"])
    html = html.replace("#5D4037", C["muted"]).replace("#FFF8E1", C["money_chip_bg"])
    html = html.replace("#0B6E6E", C["link"])
    # Panel widths (rail 280 / drawer 340) — appear in the two panel style blocks.
    html = html.replace("width:280px", f"width:{_fmt(rail_w)}px")
    html = html.replace("width:340px", f"width:{_fmt(drawer_w)}px")
    return html


# ── Profile → HTML (deterministic, config-driven transforms) ──────────────────
def render_profile_html(pid: str, profiles_dir: str, sections: dict, acronyms: list) -> str:
    path = os.path.join(profiles_dir, f"{pid}.md")
    if not os.path.exists(path):
        return ""
    txt = open(path, encoding="utf-8").read()
    if "✅ researched" not in txt:
        return ""
    parts = txt.split("\n---\n", 1)
    body = parts[1] if len(parts) == 2 else txt
    body = re.split(r"\n#{1,2}\s*[^\n]*(?:New relationships|relationships to record)", body)[0]
    body = prose.clean_prose(body, sections, acronyms)
    return markdown.markdown(body, extensions=["tables", "fenced_code", "sane_lists"])


# ── Label layout (deterministic, overlap-free) ───────────────────────────────
def _text_width(txt: str, font: int) -> float:
    return 0.62 * font * len(txt)


def _rects_overlap(b1, b2, pad=6):
    return not (b1[0] + b1[2] + pad < b2[0] or b2[0] + b2[2] + pad < b1[0] or
                b1[1] + b1[3] + pad < b2[1] or b2[1] + b2[3] + pad < b1[1])


def place_labels(G, composite, svg_pos, radius_fn, W, H, threshold, font=40):
    label_nodes = {n for n in G.nodes() if composite[n] >= threshold}
    placed_rects, placements = [], {}
    for n in sorted(label_nodes, key=lambda x: -composite[x]):
        x, y = svg_pos[n]
        r = radius_fn(n)
        label = G.nodes[n]["label"]
        w, h = _text_width(label, font), font * 1.4
        placed = False
        for radius in range(0, 2000, 12):
            for ang in range(0, 360, 10):
                cx = x + radius * math.cos(math.radians(ang))
                cy = y + radius * math.sin(math.radians(ang))
                cx = max(w / 2 + 10, min(W - w / 2 - 10, cx))
                cy = max(h + 10, min(H - 10, cy))
                rect = (cx - w / 2, cy - h, w, h)
                if not any(_rects_overlap(rect, pr, pad=6) for pr in placed_rects):
                    placements[n] = (cx, cy)
                    placed_rects.append(rect)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            placements[n] = (x, y)
            placed_rects.append((x - w / 2, y - h, w, h))
    return placements


# ── Shape glyphs / SVG geometry ───────────────────────────────────────────────
SHAPE_GLYPH = {"square": "&#9632;", "circle": "&#9679;", "triangle": "&#9650;",
               "diamond": "&#9670;", "hexagon": "&#11022;", "pentagon": "&#11021;"}


def node_svg(nid, attrs, x, y, r, domain_cfg):
    dom = domain_cfg.get(attrs.get("domain", ""), {})
    color = dom.get("color", "#333")
    shape = dom.get("shape", "circle")
    label = attrs.get("label", nid)
    dlabel = nid
    domain = attrs.get("domain", "institutional")
    common = f'id="n-{dlabel}" class="node" data-id="{dlabel}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" '
    if shape == "square":
        s = r * 0.9
        return f'<rect {common}x="{x-s:.1f}" y="{y-s:.1f}" width="{2*s:.1f}" height="{2*s:.1f}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'
    if shape == "triangle":
        pts = f"{x:.1f},{y-r:.1f} {x+r*0.87:.1f},{y+r*0.5:.1f} {x-r*0.87:.1f},{y+r*0.5:.1f}"
        return f'<polygon {common}points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'
    if shape == "diamond":
        pts = f"{x:.1f},{y-r:.1f} {x+r:.1f},{y:.1f} {x:.1f},{y+r:.1f} {x-r:.1f},{y:.1f}"
        return f'<polygon {common}points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'
    if shape == "hexagon":
        pts = " ".join(f"{x+r*math.cos(math.radians(a)):.1f},{y+r*math.sin(math.radians(a)):.1f}" for a in range(0, 360, 60))
        return f'<polygon {common}points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'
    if shape == "pentagon":
        pts = " ".join(f"{x+r*math.cos(math.radians(a-90)):.1f},{y+r*math.sin(math.radians(a-90)):.1f}" for a in range(0, 360, 72))
        return f'<polygon {common}points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'
    return f'<circle {common}cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>'


def build(graph_data: dict, site: dict, profiles_dir: str) -> str:
    """Render the full self-contained HTML string."""
    G = build_graph(graph_data)
    composite = compute_power(G, site.get("power"))
    nodes = graph_data["nodes"]
    edges = graph_data["edges"]
    node_by_id = {n["id"]: n for n in nodes}

    case = site.get("case", {})
    domains = site.get("domains", {})
    rel_classes = site.get("relationship_classes", {})
    sections = site.get("sections", {})
    acronyms = site.get("acronyms", [])
    rcfg = site.get("render", {})
    missions = site.get("missions", [])

    # ── theme tokens (readability + visuals), resolved once with defaults ──
    # Defaults reproduce the current output byte-for-byte, so this is idempotent.
    _t = site.get("theme", {})
    _tc = _t.get("colors", {})
    C = {
        "accent": _tc.get("accent", "#B8860B"),
        "highlight": _tc.get("highlight", "#E8C547"),
        "page_bg": _tc.get("page_bg", "#fafafa"),
        "surface": _tc.get("surface", "#FAFAFA"),
        "ink": _tc.get("ink", "#1B1B1B"),
        "text": _tc.get("text", "#1a1a1a"),
        "border": _tc.get("border", "#E0E0E0"),
        "money_chip_bg": _tc.get("money_chip_bg", "#FFF8E1"),
        "muted": _tc.get("muted", "#5D4037"),
        "link": _tc.get("link", "#0B6E6E"),
        "edge": "#999", "dim": "#888", "halo": "#fff", "neutral_bg": "#eee",
        "neutral_fg": "#666", "guide_bg": "#fff",
    }
    _t_label = _t.get("label_font_px", 22)
    _t_prof_body = _t.get("profile_body_px", 12.5)
    _t_prof_table = _t.get("profile_table_px", 11.5)
    _t_prof_h2 = _t.get("profile_h2_px", 14)
    _t_prof_h3 = _t.get("profile_h3_px", 13)
    _t_line_height = _t.get("profile_line_height", 1.5)
    _t_chip = _t.get("chip_font_px", 12)
    _t_drawer_title = _t.get("drawer_title_px", 15)
    _t_rail = _t.get("rail_width", 280)
    _t_drawer = _t.get("drawer_width", 340)

    # detail view mode (entity focus) — config-driven
    _fullscreen = bool(rcfg.get("detail_fullscreen", False))
    _detail_max_w = rcfg.get("detail_max_width", 960)

    # ── computed, never hard-coded ──
    node_count = len(nodes)
    edge_count = len(edges)
    ranked = sorted(G.nodes(), key=lambda n: -composite[n])
    top_actor = G.nodes[ranked[0]]["label"] if ranked else "—"
    top_three = ", ".join(G.nodes[n]["label"] for n in ranked[1:4]) if len(ranked) >= 4 else top_actor

    money_rel = set(rel_classes.get("money", []))
    influence_rel = set(rel_classes.get("influence", []))
    interlock_rel = set(rel_classes.get("interlock", []))

    # money edges = edges whose relationship is money-class
    money_edges = set()
    for e in edges:
        if e.get("relationship", "") in money_rel:
            money_edges.add((e["source"], e["target"]))
            money_edges.add((e["target"], e["source"]))
    # money nodes = config extra list + endpoints of money edges
    money_nodes = set(site.get("extra_money_nodes", []))
    for a, b in money_edges:
        money_nodes.add(a)
        money_nodes.add(b)

    # ── layout ──
    W, H = rcfg.get("canvas_w", 2560), rcfg.get("canvas_h", 1440)
    PAD = rcfg.get("pad", 60)
    R_MIN, R_MAX = rcfg.get("r_min", 14.0), rcfg.get("r_max", 36.0)
    ORG_SCALE = rcfg.get("org_scale", 1.2)
    SEED = rcfg.get("layout_seed", 7)
    max_comp = max(composite.values()) if composite else 1.0

    def radius(nid):
        s = composite[nid] / max_comp
        r = R_MIN + (R_MAX - R_MIN) * (s ** 0.5)
        if G.nodes[nid].get("type") == "organization":
            r *= ORG_SCALE
        return r

    pos = nx.spring_layout(G, k=1.8, iterations=400, seed=SEED)
    xs = [pos[n][0] for n in G.nodes()]; ys = [pos[n][1] for n in G.nodes()]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)

    def to_svg(x, y):
        return (PAD + (x - minx) / (maxx - minx) * (W - 2 * PAD),
                PAD + (y - miny) / (maxy - miny) * (H - 2 * PAD))

    svg_pos = {n: to_svg(*pos[n]) for n in G.nodes()}

    threshold = rcfg.get("label_threshold", 0.06)
    label_placements = place_labels(G, composite, svg_pos, radius, W, H, threshold)
    top_persist = rcfg.get("top_labels_persistent", 5)
    top_labels = set(sorted(label_placements, key=lambda n: -composite[n])[:top_persist])

    # ── SVG ──
    svg_parts = [f'<svg id="net" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" style="background:#fafafa" role="img" aria-label="{case.get("appbar_label", "")}">',
                 f'<rect id="bg-clear" x="0" y="0" width="{W}" height="{H}" fill="transparent" style="cursor:default;"/>']
    for u, v, d in G.edges(data=True):
        x1, y1 = svg_pos[u]; x2, y2 = svg_pos[v]; w = d.get("weight", 1)
        op = min(0.12 + w / 22, 0.55); sw = 0.5 + w / 7
        is_money = "1" if (u, v) in money_edges else "0"
        svg_parts.append(f'<line id="e-{u}-{v}" class="edge" data-u="{u}" data-v="{v}" data-money="{is_money}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#999" stroke-width="{sw:.2f}" stroke-opacity="{op:.2f}"/>')
    for n in G.nodes():
        x, y = svg_pos[n]; r = radius(n)
        svg_parts.append(f'<circle id="ring-{n}" class="ring" cx="{x:.1f}" cy="{y:.1f}" r="{r+6:.1f}" fill="none" stroke="#ffd700" stroke-width="4" stroke-opacity="0" style="display:none;"/>')
        if n in money_nodes:
            svg_parts.append(f'<circle id="mring-{n}" class="mring" cx="{x:.1f}" cy="{y:.1f}" r="{r+11:.1f}" fill="none" stroke="#B8860B" stroke-width="3" stroke-dasharray="6,4" stroke-opacity="0" style="display:none;"/>')
        svg_parts.append(node_svg(n, G.nodes[n], x, y, r, domains))
        if n in label_placements:
            lx, ly = label_placements[n]
            svg_parts.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="#999" stroke-width="0.8" stroke-opacity="0.35" stroke-dasharray="2,2"/>')
    svg_parts.append('</svg>')

    # ── label overlays ──
    overlays = []
    for n in label_placements:
        lx, ly = label_placements[n]
        label = G.nodes[n]["label"]
        px, py = lx / W * 100, ly / H * 100
        persist = "1" if n in top_labels else "0"
        overlays.append(f'<div class="label" data-id="{n}" data-persist="{persist}" aria-hidden="true" style="left:{px:.2f}%;top:{py:.2f}%;transform:translate(-50%,-50%);{"display:none;" if persist=="0" else ""}">{label}</div>')
    label_html = "\n".join(overlays)

    # ── node data (for JS) ──
    node_data = {}
    for n in nodes:
        nid = n["id"]
        conns = {}
        for e in edges:
            if e["source"] == nid:
                conns.setdefault(e["target"], []).append({"rel": e.get("relationship", ""), "dir": "out"})
            if e["target"] == nid:
                conns.setdefault(e["source"], []).append({"rel": e.get("relationship", ""), "dir": "in"})
        node_data[nid] = {
            "label": n["label"], "type": n["type"], "domain": n["domain"],
            "desc": n.get("desc", ""), "facts": n.get("facts", []),
            "profile": render_profile_html(nid, profiles_dir, sections, acronyms),
            "power": round(composite[nid], 3),
            "conns": conns,
        }

    # ── legend ──
    legend_rows = []
    for dom in domains:
        c = domains[dom].get("color", "#333")
        g = SHAPE_GLYPH.get(domains[dom].get("shape", "circle"), "&#9679;")
        lbl = domains[dom].get("label", dom.capitalize())
        legend_rows.append(f'<div style="display:flex; align-items:center; gap:8px; font-size:13px; color:#1B1B1B; padding:2px 0;"><span style="color:{c}; width:16px; text-align:center;">{g}</span><span>{lbl}</span></div>')
    legend_html = "\n".join(legend_rows)

    # ── config → JS literals ──
    def js_list(s):
        return "[" + ",".join(json.dumps(x) for x in s) + "]"

    money_js = js_list(sorted(money_rel))
    influence_js = js_list(sorted(influence_rel))
    interlock_js = js_list(sorted(interlock_rel))
    domain_color_js = json.dumps({d: domains[d]["color"] for d in domains})
    domain_shape_js = json.dumps({d: domains[d]["shape"] for d in domains})

    thesis = case.get("thesis", "")
    thesis_emphasis = case.get("thesis_emphasis", "")
    thesis_span = f' <span style="color:#E8C547; font-weight:bold;">{thesis_emphasis}</span>' if thesis_emphasis else ""
    appbar_label = case.get("appbar_label", case.get("title", ""))
    about_body = case.get("about_body", "")
    about_body = about_body.replace("{node_count}", str(node_count)).replace("{edge_count}", str(edge_count))
    thesis_loop = case.get("thesis_loop", {"wealth": "Wealth", "power": "Power", "policy": "Policy"})
    loop_explain = case.get("loop_explain", "")

    # mission text placeholder substitution (MUST run before missions_js serialization)
    for m in missions:
        m["body"] = m["body"].replace("{node_count}", str(node_count)).replace("{edge_count}", str(edge_count))
        m["fact"] = m["fact"].replace("{top_actor}", top_actor).replace("{top_three}", top_three)
    missions_js = json.dumps(missions, ensure_ascii=False)

    # ── HTML shell ──
    appbar = f"""
<div id="appbar" style="position:absolute; top:0; left:0; right:0; height:56px; background:#1B1B1B; color:#FAFAFA; display:flex; align-items:center; padding:0 20px; box-shadow:0 2px 8px rgba(0,0,0,0.3); z-index:10; font-family:sans-serif;">
  <div style="font-size:16px; font-weight:bold; white-space:nowrap;">{appbar_label}</div>
  <div style="flex:1; margin-left:20px; font-size:13px; color:#ccc; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
    <span id="appbar-thesis">{thesis}{thesis_span}</span>
    <span id="appbar-mission" style="display:none; color:#E8C547; font-weight:bold;"></span>
  </div>
  <button id="money-toggle" role="switch" aria-checked="false" aria-label="Follow the money: show public money flows" style="display:flex; align-items:center; gap:8px; background:transparent; border:2px dashed #B8860B; border-radius:20px; padding:4px 12px; cursor:pointer; margin-right:12px; font-family:sans-serif;">
    <span id="money-switch" style="width:36px; height:20px; border-radius:10px; background:#555; position:relative; flex-shrink:0; transition:background 0.2s;"><span id="money-thumb" style="position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:50%; background:#fff; transition:left 0.2s; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:bold; color:#1B1B1B;">$</span></span>
    <span id="money-label" style="color:#E8C547; font-size:13px; font-weight:bold;">Follow the money</span>
  </button>
  <button id="begin-btn" style="background:#E8C547; border:none; color:#1B1B1B; border-radius:4px; padding:4px 12px; font-size:13px; font-weight:bold; cursor:pointer; margin-right:8px;" aria-label="Begin the guided investigation">Begin investigation</button>
  <button id="about-btn" style="background:transparent; border:1px solid #555; color:#FAFAFA; border-radius:4px; padding:4px 12px; font-size:13px; cursor:pointer;" aria-label="About this investigation">About</button>
</div>
"""

    rail = f"""
<div id="rail" style="position:absolute; top:56px; left:0; bottom:0; width:280px; background:#FAFAFA; border-right:1px solid #E0E0E0; padding:16px; box-sizing:border-box; overflow-y:auto; z-index:9; font-family:sans-serif;">
  <div id="guide-card" style="background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:12px; margin-bottom:16px; display:none;">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
      <span style="font-size:11px; font-weight:bold; color:#B8860B; text-transform:uppercase; letter-spacing:1px;">Mission <span id="guide-num">1</span> of {len(missions)}</span>
      <button id="guide-skip" style="background:none; border:none; color:#888; font-size:12px; cursor:pointer; text-decoration:underline;">Skip</button>
    </div>
    <div id="guide-title" style="font-size:15px; font-weight:bold; color:#1B1B1B; margin-bottom:4px;"></div>
    <div id="guide-body" style="font-size:13px; color:#333; line-height:1.5; margin-bottom:8px;"></div>
    <div id="guide-fact" style="background:#FFF8E1; border-left:4px solid #B8860B; padding:8px 10px; border-radius:4px; font-size:12px; color:#5D4037; display:none;"></div>
    <div id="guide-progress" style="display:flex; gap:4px; margin-top:10px;"></div>
  </div>
  <div id="loop-card" style="background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:12px; margin-bottom:16px; cursor:pointer;" role="button" tabindex="0" aria-label="The structural-capture loop: Wealth to Power to Policy">
    <div style="font-size:13px; font-weight:bold; color:#1B1B1B; margin-bottom:8px;">How power works here</div>
    <div style="display:flex; align-items:center; justify-content:space-between; font-size:13px; font-weight:bold;">
      <span style="color:#B8860B;">{thesis_loop.get("wealth","Wealth")}</span><span style="color:#888;">→</span>
      <span style="color:{domains.get("government",{}).get("color","#1f77b4")};">{thesis_loop.get("power","Power")}</span><span style="color:#888;">→</span>
      <span style="color:{domains.get("institutional",{}).get("color","#1e7d32")};">{thesis_loop.get("policy","Policy")}</span>
    </div>
    <div style="font-size:11px; color:#666; margin-top:6px; line-height:1.4;">{loop_explain}</div>
  </div>
  <div id="legend-card" style="margin-bottom:16px;">
    <div style="font-size:13px; font-weight:bold; color:#1B1B1B; margin-bottom:6px;">Domains</div>
    <div>{legend_html}</div>
  </div>
  <button id="top10-btn" style="display:none; width:100%; background:#1B1B1B; color:#FAFAFA; border:none; border-radius:8px; padding:10px 12px; cursor:pointer; font-size:13px; font-weight:bold;">Top 10 by power</button>
  <button id="more-btn" style="display:none; width:100%; background:transparent; border:1px solid #E0E0E0; color:#1B1B1B; border-radius:8px; padding:8px 12px; cursor:pointer; font-size:12px; margin-top:12px;">More</button>
</div>
"""

    if _fullscreen:
        _drawer_open_t = "translateY(0)"
        _drawer_closed_t = "translateY(102%)"
        _drawer_style = "position:absolute; top:56px; left:0; right:0; bottom:0; width:auto; background:#FAFAFA; border-top:1px solid #E0E0E0; box-shadow:0 -4px 20px rgba(0,0,0,0.15); transform:translateY(102%); transition:transform 0.25s ease; z-index:9; font-family:sans-serif; display:flex; flex-direction:column;"
        _drawer_content_style = f"flex:1; overflow-y:auto; padding:24px 28px 40px; max-width:{_fmt(_detail_max_w)}px; margin:0 auto; width:100%; box-sizing:border-box;"
        _drawer_header_extra = f'<button id="drawer-back" aria-label="Back to map" style="background:none; border:none; color:#444; font-size:14px; cursor:pointer; margin-right:12px;">&larr; Back to map</button>'
    else:
        _drawer_open_t = "translateX(0)"
        _drawer_closed_t = "translateX(105%)"
        _drawer_style = "position:absolute; top:56px; right:0; bottom:0; width:340px; background:#FAFAFA; border-left:1px solid #E0E0E0; box-shadow:-4px 0 20px rgba(0,0,0,0.15); transform:translateX(105%); transition:transform 0.25s ease; z-index:9; font-family:sans-serif; display:flex; flex-direction:column;"
        _drawer_content_style = "flex:1; overflow-y:auto; padding:16px;"
        _drawer_header_extra = ""

    drawer = f"""
<div id="drawer" style="{_drawer_style}">
  <div style="display:flex; align-items:center; justify-content:space-between; padding:14px 16px; border-bottom:1px solid #E0E0E0;">
    <div style="display:flex; align-items:center; flex:1; min-width:0;">
      {_drawer_header_extra}
      <div id="drawer-title" style="font-size:{_fmt(_t_drawer_title)}px; font-weight:bold; color:#1B1B1B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Details</div>
    </div>
    <button id="drawer-close" aria-label="Close details" style="background:none; border:none; font-size:22px; color:#444; cursor:pointer;">&times;</button>
  </div>
  <div id="drawer-content" style="{_drawer_content_style}"></div>
</div>
"""

    money_legend = """
<div id="money-legend" style="display:none; position:absolute; bottom:16px; left:300px; background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:8px 12px; font-family:sans-serif; font-size:12px; color:#1B1B1B; z-index:8; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
  <span style="display:inline-block; width:14px; height:14px; border:2px dashed #B8860B; border-radius:50%; margin-right:6px; vertical-align:middle;"></span>
  <span style="display:inline-block; width:22px; height:2px; background:#B8860B; margin-right:6px; vertical-align:middle;"></span>
  <b>Gold = public money</b> (government-created wealth)
</div>
<div id="coach-money" style="display:none; position:absolute; top:64px; right:180px; background:#1B1B1B; color:#FAFAFA; border:2px solid #E8C547; border-radius:8px; padding:8px 12px; font-family:sans-serif; font-size:13px; font-weight:bold; z-index:20; box-shadow:0 4px 16px rgba(0,0,0,0.3);">
  Click the gold switch above ↑
</div>
"""

    node_data_js = json.dumps(node_data, ensure_ascii=False)

    js = f"""
<script>
const NODE_DATA = {node_data_js};
const domainColor = {domain_color_js};
const domainShape = {domain_shape_js};
const shapeGlyph = {json.dumps(SHAPE_GLYPH)};
const MONEY_RELS = new Set({money_js});
const INFLUENCE_RELS = new Set({influence_js});
const INTERLOCK_RELS = new Set({interlock_js});
let currentFocus = null;
let moneyOn = true;
let drawerOpen = false;

function setFocus(id){{
  document.querySelectorAll('.ring').forEach(r=>{{ r.style.display='none'; r.style.strokeOpacity='0'; }});
  document.querySelectorAll('.node').forEach(n=>{{ n.style.stroke='#fff'; n.style.strokeWidth='1.5'; n.style.opacity='1'; }});
  document.querySelectorAll('.edge').forEach(e=>{{ e.style.stroke='#999'; e.style.strokeOpacity=e.dataset.baseop||'0.3'; e.style.opacity='1'; }});
  if(!id){{ currentFocus=null; return; }}
  currentFocus = id;
  const ring = document.getElementById('ring-'+id);
  if(ring){{ ring.style.display='block'; ring.style.strokeOpacity='1'; }}
  const node = document.getElementById('n-'+id);
  if(node){{ node.style.stroke='#000'; node.style.strokeWidth='3.5'; }}
  const neighbors = new Set([id]);
  document.querySelectorAll('.edge').forEach(e=>{{
    if(e.dataset.u===id||e.dataset.v===id){{ neighbors.add(e.dataset.u); neighbors.add(e.dataset.v); }}
  }});
  document.querySelectorAll('.node').forEach(n=>{{ if(!neighbors.has(n.dataset.id)){{ n.style.opacity='0.15'; }} }});
  document.querySelectorAll('.edge').forEach(e=>{{
    if(e.dataset.u===id||e.dataset.v===id){{ e.style.stroke='#333'; e.style.strokeOpacity='0.7'; }}
    else {{ e.style.opacity='0.12'; }}
  }});
}}

function openDrawer(){{ document.getElementById('drawer').style.transform='{_drawer_open_t}'; drawerOpen=true; }}
function closeDrawer(){{ document.getElementById('drawer').style.transform='{_drawer_closed_t}'; drawerOpen=false; }}

function relClass(rel){{
  if(MONEY_RELS.has(rel)) return 'money';
  if(INFLUENCE_RELS.has(rel)) return 'influence';
  if(INTERLOCK_RELS.has(rel)) return 'interlock';
  return 'structural';
}}
function relIcon(cls){{ return cls==='money'?'$':cls==='influence'?'→':cls==='interlock'?'⬡':'⚙'; }}
function relArrow(cls, dir){{ if(cls==='interlock') return '↔'; return dir==='out' ? '→' : '←'; }}
function relChip(cid, label, rel, dir){{
  const cls = relClass(rel);
  const icon = relIcon(cls);
  const arrow = relArrow(cls, dir);
  const target = NODE_DATA[cid];
  const tcolor = target?domainColor[target.domain]||'#333':'#333';
  let style;
  if(cls==='money') style = 'background:#FFF8E1;border:1px solid #B8860B;color:#B8860B;';
  else if(cls==='influence') style = `background:${{tcolor}}1A;border:1px solid ${{tcolor}};color:${{tcolor}};`;
  else if(cls==='interlock') style = 'background:#1B1B1B;color:#FAFAFA;border:1px solid #1B1B1B;';
  else style = 'background:#eee;border:1px solid #666;color:#666;';
  const sentence = cls==='money' ? `Money ${{dir==='out'?'flows to':'comes from'}} ${{label}}`
    : cls==='influence' ? `${{dir==='out'?'Influences':'Influenced by'}} ${{label}}`
    : cls==='interlock' ? `Board interlock with ${{label}}`
    : `Related to ${{label}}`;
  return `<span onclick="navigateTo('${{cid}}')" role="button" tabindex="0" onkeydown="if(event.key==='Enter')navigateTo('${{cid}}')" aria-label="${{sentence}}" style="display:inline-block;border-radius:4px;padding:3px 8px;margin:3px;font-size:{_fmt(_t_chip)}px;cursor:pointer;${{style}}"><span aria-hidden="true">${{icon}}</span> ${{label}} <span aria-hidden="true">${{arrow}}</span></span>`;
}}
function groupBlock(title, items){{
  if(!items.length) return '';
  return `<div style="font-size:12px;font-weight:bold;margin:8px 0 3px;color:#1a1a1a;">${{title}}</div><div>${{items.join('')}}</div>`;
}}

function renderPanel(id){{
  const d = NODE_DATA[id];
  if(!d) return;
  const color = domainColor[d.domain]||"#333";
  const glyph = shapeGlyph[domainShape[d.domain]]||"&#9679;";
  const facts = (d.facts||[]).map(f=>`<li>${{f}}</li>`).join('');
  const conns = d.conns||{{}};
  let thesis = '';
  if(d.domain==='government') thesis = 'Holds public office → funded by taxpayers → influenced by donors & lobbyists';
  else if(d.domain==='media') thesis = 'Owned by a parent → shapes the public story';
  else if(d.domain==='economic'||d.domain==='institutional') thesis = 'Receives public money → converts it to influence → shapes policy';
  else thesis = 'Sits across the power network → the connections are the story';
  const moneyIn=[], moneyOut=[], inflIn=[], inflOut=[], interlocks=[], structural=[];
  Object.entries(conns).forEach(([cid,rs])=>{{
    const lbl = NODE_DATA[cid]?NODE_DATA[cid].label:cid;
    rs.forEach(r=>{{
      const cls = relClass(r.rel);
      if(cls==='money' && r.dir==='in') moneyIn.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='money' && r.dir==='out') moneyOut.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='influence' && r.dir==='in') inflIn.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='influence' && r.dir==='out') inflOut.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='interlock') interlocks.push(relChip(cid,lbl,r.rel,r.dir));
      else structural.push(relChip(cid,lbl,r.rel,r.dir));
    }});
  }});
  let focal = '';
  if(moneyIn.length){{
    const src = Object.keys(conns).find(cid=>conns[cid].some(r=>MONEY_RELS.has(r.rel)&&r.dir==='in'));
    const srcLabel = NODE_DATA[src]?NODE_DATA[src].label:src;
    const rel = conns[src].find(r=>MONEY_RELS.has(r.rel)&&r.dir==='in').rel;
    focal = `
      <div style="background:#FAFAFA;border:1px solid #B8860B;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:1px;">Where the power comes from</div>
        <div style="font-size:15px;font-weight:bold;color:#B8860B;margin:2px 0;">${{rel.replace(/_/g,' ')}}</div>
        <div style="font-size:12px;color:#1a1a1a;">via <b>${{srcLabel}}</b> — public money granted by government.</div>
      </div>`;
  }} else if(interlocks.length>=2){{
    focal = `
      <div style="background:#1B1B1B;color:#FAFAFA;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#E8C547;text-transform:uppercase;letter-spacing:1px;">Multiple hats — the interlock</div>
        <div style="font-size:12px;margin-top:4px;">${{interlocks.slice(0,3).join('')}}</div>
      </div>`;
  }} else if(inflIn.length){{
    focal = `
      <div style="background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#1a1a1a;text-transform:uppercase;letter-spacing:1px;">Who influences them</div>
        <div style="font-size:12px;margin-top:4px;">${{inflIn.slice(0,3).join('')}}</div>
      </div>`;
  }} else if(inflOut.length){{
    focal = `
      <div style="background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#1a1a1a;text-transform:uppercase;letter-spacing:1px;">Where its power leads</div>
        <div style="font-size:12px;margin-top:4px;">${{inflOut.slice(0,3).join('')}}</div>
      </div>`;
  }}
  const connsHtml = groupBlock('Money flows to', moneyOut)
    + groupBlock('Influences', inflOut)
    + groupBlock('Influenced by', inflIn)
    + groupBlock('Board interlocks', interlocks)
    + groupBlock('Structural', structural);
  let nudge = '';
  if(moneyIn.length){{ const src = Object.keys(conns).find(cid=>conns[cid].some(r=>MONEY_RELS.has(r.rel)&&r.dir==='in')); const srcLabel = NODE_DATA[src]?NODE_DATA[src].label:src; nudge = `Follow the money: see who funds <b>${{srcLabel}}</b>.`; }}
  else if(interlocks.length) nudge = 'Trace the interlock: see the other boards this entity sits on.';
  else if(inflIn.length) nudge = 'See who influences this entity.';
  else nudge = "Explore this entity's connections to see where its power leads.";

  document.getElementById('drawer-title').textContent = d.label;
  const profileBody = d.profile || (
    `<div style="font-size:13px;color:#1a1a1a;line-height:1.5;">${{d.desc?`<p>${{d.desc}}</p>`:''}}${{(d.facts||[]).length?`<ul>${{d.facts.map(f=>`<li>${{f}}</li>`).join('')}}</ul>`:''}}</div>`
  );
  document.getElementById('drawer-content').innerHTML = `
    <div style="font-size:12px;color:#444;margin:0 0 8px;">${{d.type}} · ${{d.domain}} · <span style="background:#E8C547;color:#1B1B1B;border-radius:4px;padding:1px 6px;font-weight:bold;">Power ${{d.power}}</span></div>
    <div style="font-size:13px;color:#1a1a1a;background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:8px 10px;margin-bottom:8px;" aria-label="This entity's role in the money-to-power loop">${{thesis}}</div>
    ${{focal}}
    ${{connsHtml}}
    <div class="profile-wrap" style="margin-top:10px;">${{profileBody}}</div>
  `;
  openDrawer();
  setFocus(id);
}}

function renderTop10(){{
  const top = Object.keys(NODE_DATA).map(k=>NODE_DATA[k]).sort((a,b)=>b.power-a.power).slice(0,10);
  document.getElementById('drawer-title').textContent = 'Top 10 by power';
  document.getElementById('drawer-content').innerHTML = top.map((d,i)=>{{
    const c = domainColor[d.domain]||"#333";
    const glyph = shapeGlyph[domainShape[d.domain]]||"&#9679;";
    const cid = Object.keys(NODE_DATA).find(k=>NODE_DATA[k].label===d.label);
    return `<div onclick="navigateTo('${{cid}}')" role="button" tabindex="0" onkeydown="if(event.key==='Enter')navigateTo('${{cid}}')" style="display:flex;align-items:center;gap:8px;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;color:#1a1a1a;border-bottom:1px solid #eee;">
      <span style="width:18px;text-align:right;color:#888;font-weight:bold;">${{i+1}}</span>
      <span style="color:${{c}};width:16px;text-align:center;">${{glyph}}</span>
      <span style="flex:1;font-weight:500;">${{d.label}}</span>
      <span style="color:#666;font-size:12px;">${{d.power.toFixed(2)}}</span>
    </div>`;
  }}).join('');
  openDrawer();
}}

function navigateTo(id){{
  history.pushState({{node:id}}, '', '#node-'+id);
  renderPanel(id);
}}
window.addEventListener('popstate', (e)=>{{
  if(e.state && e.state.node){{ renderPanel(e.state.node); }}
  else {{ closeDrawer(); setFocus(null); }}
}});

document.querySelectorAll('.node').forEach(n=>{{
  n.addEventListener('click', ()=>navigateTo(n.dataset.id));
  n.addEventListener('keydown', (e)=>{{ if(e.key==='Enter'||e.key===' '){{ e.preventDefault(); navigateTo(n.dataset.id); }} }});
  const showLabel = ()=>{{ const l=document.querySelector(`.label[data-id="${{n.dataset.id}}"]`); if(l) l.style.display='block'; }};
  const hideLabel = ()=>{{ const l=document.querySelector(`.label[data-id="${{n.dataset.id}}"]`); if(l && l.dataset.persist==='0') l.style.display='none'; }};
  n.addEventListener('mouseenter', showLabel);
  n.addEventListener('mouseleave', hideLabel);
  n.addEventListener('focus', showLabel);
  n.addEventListener('blur', hideLabel);
}});
document.getElementById('drawer-close').addEventListener('click', ()=>{{
  history.pushState({{node:null}}, '', '#');
  closeDrawer(); setFocus(null);
}});
const _backBtn = document.getElementById('drawer-back');
if(_backBtn){{ _backBtn.addEventListener('click', ()=>{{
  history.pushState({{node:null}}, '', '#');
  closeDrawer(); setFocus(null);
}}); }}
document.getElementById('bg-clear').addEventListener('click', ()=>{{
  history.pushState({{node:null}}, '', '#');
  closeDrawer(); setFocus(null);
}});
document.getElementById('top10-btn').addEventListener('click', renderTop10);
document.getElementById('about-btn').addEventListener('click', ()=>{{
  document.getElementById('drawer-title').textContent = 'About';
  document.getElementById('drawer-content').innerHTML = `<div style="font-size:14px;color:#1a1a1a;line-height:1.6;"><b>{appbar_label} ({case.get("id","")})</b><br><br>{about_body}</div>`;
  openDrawer();
}});

function applyMoney(on){{
  moneyOn = on;
  document.querySelectorAll('.mring').forEach(r=>{{ r.style.display = on ? 'block' : 'none'; r.style.strokeOpacity = on ? '1' : '0'; }});
  document.querySelectorAll('.edge').forEach(e=>{{
    if(e.dataset.money==='1'){{ e.style.stroke = on ? '#B8860B' : '#999'; e.style.strokeOpacity = on ? '0.6' : (e.dataset.baseop||'0.3'); }}
  }});
  const sw = document.getElementById('money-switch');
  const thumb = document.getElementById('money-thumb');
  sw.style.background = on ? '#B8860B' : '#555';
  thumb.style.left = on ? '18px' : '2px';
  document.getElementById('money-toggle').setAttribute('aria-checked', on ? 'true':'false');
  const legend = document.getElementById('money-legend');
  if(legend){{ legend.style.display = on ? 'block' : 'none'; }}
}}
let userToggledMoney = false;
document.getElementById('money-toggle').addEventListener('click', ()=>{{
  userToggledMoney = true;
  applyMoney(!moneyOn);
  if(missionIdx===1) completeMission();
}});
applyMoney(false);

const MISSIONS = {missions_js};
let missionIdx = -1;
let missionDone = false;

function showMission(i){{
  missionIdx = i;
  const m = MISSIONS[i];
  document.getElementById('guide-card').style.display='block';
  document.getElementById('guide-num').textContent = i+1;
  document.getElementById('guide-title').textContent = m.title;
  document.getElementById('guide-body').textContent = m.body;
  const f = document.getElementById('guide-fact');
  f.textContent = m.fact; f.style.display='block';
  document.getElementById('guide-progress').innerHTML = MISSIONS.map((_,j)=>
    `<span style="width:10px;height:10px;border-radius:50%;background:${{j<i?'#B8860B':(j===i?'#E8C547':'#ddd')}};display:inline-block;"></span>`).join('');
  document.getElementById('appbar-thesis').style.display='inline';
  const ms = document.getElementById('appbar-mission');
  ms.style.display='inline'; ms.textContent = ` · Mission ${{i+1}} of ${{MISSIONS.length}} · ${{m.title}}`;
  document.getElementById('top10-btn').style.display = (m.type==='top10') ? 'block' : 'none';
  document.getElementById('more-btn').style.display = 'block';
  if(m.type==='toggle' && !userToggledMoney){{ applyMoney(false); }}
  if(m.type==='node' && m.target){{ focusNode(m.target); }}
  if(m.type==='anynode'){{ setFocus(null); }}
  if(m.type==='top10'){{ closeDrawer(); }}
  if(m.type==='connection'){{ closeDrawer(); }}
  const cm = document.getElementById('coach-money');
  if(cm){{ cm.style.display = (m.type==='toggle') ? 'block' : 'none'; }}
  document.getElementById('guide-card').setAttribute('aria-live','polite');
}}
function focusNode(id){{
  setFocus(id);
  const n = document.getElementById('n-'+id);
  if(n){{ n.style.stroke='#E8C547'; n.style.strokeWidth='4'; }}
}}
function completeMission(){{
  if(missionIdx < 0) return;
  if(missionIdx >= MISSIONS.length-1){{
    missionDone = true;
    try{{ localStorage.setItem('pcn-mission-done','1'); }}catch(e){{}}
    document.getElementById('guide-card').style.display='none';
    document.getElementById('appbar-mission').style.display='none';
    document.getElementById('appbar-thesis').style.display='inline';
    document.getElementById('begin-btn').textContent = 'Replay investigation';
    document.getElementById('top10-btn').style.display='block';
    document.getElementById('more-btn').style.display='none';
    return;
  }}
  showMission(missionIdx+1);
}}
function startMissions(){{
  if(missionDone){{ missionIdx=-1; missionDone=false; }}
  showMission(0);
}}
document.getElementById('begin-btn').addEventListener('click', startMissions);
document.getElementById('guide-skip').addEventListener('click', ()=>{{
  document.getElementById('guide-card').style.display='none';
  document.getElementById('appbar-mission').style.display='none';
  document.getElementById('appbar-thesis').style.display='inline';
  document.getElementById('top10-btn').style.display='block';
  document.getElementById('more-btn').style.display='none';
  setFocus(null);
}});

document.querySelectorAll('.node').forEach(n=>{{
  n.addEventListener('click', ()=>{{
    if(missionIdx===0 && n.dataset.id==='{missions[0].get("target","") if missions else ""}') completeMission();
    else if(missionIdx===2 && n.dataset.id==='{missions[2].get("target","") if len(missions)>2 else ""}') completeMission();
    else if(missionIdx===3) completeMission();
  }});
}});
document.getElementById('loop-card').addEventListener('click', ()=>{{
  if(missionIdx===4){{ completeMission(); return; }}
  document.getElementById('about-btn').click();
}});
document.getElementById('loop-card').addEventListener('keydown', (e)=>{{
  if(e.key==='Enter'||e.key===' '){{ e.preventDefault(); if(missionIdx===4) completeMission(); else document.getElementById('about-btn').click(); }}
}});
const _origNav = navigateTo;
navigateTo = function(id){{
  if(missionIdx===5 && drawerOpen) completeMission();
  _origNav(id);
}};
document.getElementById('top10-btn').addEventListener('click', ()=>{{
  if(missionIdx===6) completeMission();
}});
document.getElementById('more-btn').addEventListener('click', ()=>{{
  document.getElementById('top10-btn').style.display='block';
  document.getElementById('more-btn').style.display='none';
}});
try{{
  if(!localStorage.getItem('pcn-mission-done')){{ startMissions(); }}
}}catch(e){{}}
</script>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{appbar_label} — Interactive</title>
<style>
  html,body {{ margin:0; padding:0; height:100%; background:{C['page_bg']}; font-family:sans-serif; }}
  #container {{ position:relative; width:100vw; height:100vh; }}
  .node:focus {{ outline:3px solid #ffd700; outline-offset:2px; }}
  text {{ paint-order: stroke; }}
  .label {{ position:absolute; font-size:{_fmt(_t_label)}px; font-weight:700; color:{C['text']};
            text-shadow:0 0 3px #fff, 0 0 3px #fff, 0 0 3px #fff, 0 0 3px #fff;
            white-space:nowrap; pointer-events:none; z-index:5; }}
  @media (prefers-reduced-motion: reduce) {{
    * {{ transition:none !important; animation:none !important; }}
    .node, .edge {{ transition:none !important; }}
  }}
  .profile-wrap h2 {{ font-size:{_fmt(_t_prof_h2)}px; color:{C['ink']}; border-bottom:1px solid {C['border']}; padding-bottom:6px; margin:16px 0 8px; }}
  .profile-wrap h3 {{ font-size:{_fmt(_t_prof_h3)}px; color:{C['ink']}; margin:12px 0 5px; }}
  .profile-wrap p, .profile-wrap li {{ font-size:{_fmt(_t_prof_body)}px; color:{C['text']}; line-height:{_fmt(_t_line_height)}; }}
  .profile-wrap ul, .profile-wrap ol {{ margin:4px 0; padding-left:20px; }}
  .profile-wrap table {{ border-collapse:collapse; width:100%; font-size:{_fmt(_t_prof_table)}px; margin:8px 0; }}
  .profile-wrap th, .profile-wrap td {{ border:1px solid {C['border']}; padding:6px 8px; text-align:left; vertical-align:top; word-break:break-word; }}
  .profile-wrap th {{ background:#F5F5F5; }}
  .profile-wrap a {{ color:{C['link']}; }}
  .profile-wrap code {{ background:#F0F0F0; padding:1px 4px; border-radius:3px; font-size:12px; }}
  .profile-wrap blockquote {{ border-left:3px solid {C['accent']}; margin:8px 0; padding:4px 12px; color:{C['muted']}; }}
</style>
</head>
<body>
<div id="container">
{appbar}
{rail}
{drawer}
{''.join(svg_parts)}
{label_html}
{money_legend}
</div>
{js}
</body>
</html>
"""
    return _apply_theme(html, C, _t_rail, _t_drawer)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 3:
        print("usage: build_site.py GRAPH_JSON SITE_JSON OUT_HTML", file=sys.stderr)
        return 2
    graph_path, site_path, out_path = argv[0], argv[1], argv[2]

    graph_data = _load(graph_path)
    site = _load(site_path)

    # Resolve the profiles dir relative to the SITE CONFIG's own directory (so a
    # case's site.json is self-contained regardless of the caller's CWD).
    base_dir = os.path.dirname(os.path.abspath(site_path))
    profiles_dir = site.get("paths", {}).get("profiles", "profiles")
    if not os.path.isabs(profiles_dir):
        profiles_dir = os.path.join(base_dir, profiles_dir)

    html = build(graph_data, site, profiles_dir)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {os.path.getsize(out_path)/1024:.1f} KB to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
