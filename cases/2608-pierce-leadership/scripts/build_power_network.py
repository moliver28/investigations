#!/usr/bin/env python3
"""
Build the Pierce County power network interactive HTML (evidence/11-power-network.html).

Reproducible build: reads /tmp/pierce_graph.json (or a path passed as argv[1]),
computes the composite power score, lays out the graph, and emits a self-contained
SVG+JS HTML file with:
  - WCAG-compliant node colors (all domains >= 4.5:1 contrast vs background)
  - WCAG-compliant labels (near-black #1a1a1a text + white halo via paint-order:stroke)
  - Collision-free label placement (no overlapping labels)
  - Accessibility: keyboard nav, focus ring, dimming, "In focus" banner, ARIA, pushState back

Usage: python3 build_power_network.py [graph.json] [out.html]
"""
import os, sys, json, math, re
import networkx as nx
import numpy as np

GRAPH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "29-power-graph-v2.json")
OUT   = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "11-power-network.html")
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_DIR = os.path.join(REPO_DIR, "..", "profiles")

# ── Full-profile rendering: extracted to scripts/profile_render.py (Task 2.2) ──
# v2 output must remain byte-identical: same transforms, now imported.
from profile_render import (ACRONYMS, SECTION_TITLES, _expand_acronyms,
                            _normalize_headers, _strip_academic_cites,
                            _strip_checkboxes, _strip_edge_machine_lines,
                            render_profile_html)


# ── Import sentinel (Task 2.2): this script executes its FULL build at module level ──
# (module-level statements below run on import). The transforms used elsewhere live in
# profile_render.py; this builder is a run-only script, not a library. Keeps byte-identity
# of the emitted HTML (no reindentation of string-literal-heavy build code).
if __name__ != "__main__":
    raise ImportError(
        "build_power_network.py is a run-only script (full build at module level); "
        "import profile_render for rendering transforms."
)

with open(GRAPH) as f:
    graph_data = json.load(f)
all_nodes = graph_data["nodes"]
all_edges = graph_data["edges"]

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_power import build_graph, compute_power
G = build_graph(graph_data)

# ── Composite power score (delegated to compute_power.py — single source of truth) ──
composite = compute_power(G)
max_comp = max(composite.values())
# Relational node size: node AREA is proportional to power (bubble-chart convention),
# so r ∝ sqrt(power). Balanced for 163 nodes on a 2560x1440 screen — big enough to
# see/click but not crowded: R_MIN=14 → 28px floor, R_MAX=36 → 72px max.
R_MIN, R_MAX = 14.0, 36.0
def node_radius(nid):
    s = composite[nid]/max_comp          # 0..1 relative power
    r = R_MIN + (R_MAX - R_MIN) * (s ** 0.5)   # area ∝ power (sqrt makes area scale with s)
    if G.nodes[nid]["type"] == "organization": r *= 1.2
    return r

LABEL_THRESHOLD = 0.06  # label only the top ~24 most powerful nodes (reduces crowding)
label_nodes = {nid for nid in G.nodes() if composite[nid] >= LABEL_THRESHOLD}
# First-impression calm: only the top 5 most powerful are persistently labeled;
# the rest appear on hover. (Honors "persist" for the top actors while reducing overload.)
TOP5_LABELS = set(sorted(label_nodes, key=lambda n: composite[n], reverse=True)[:5])

# ── WCAG-compliant domain colors (all >= 4.5:1 contrast vs #fafafa) ──
# Verified: government #1f77b4=4.62, economic #c05600=4.5+, institutional #1e7d32=5.4,
# political #b71c1c=6.3, legal #6a1b9a=6.0, media #5d4037=7.0
domain_colors = {
    "government":   "#1f77b4",  # 4.62:1
    "economic":     "#b84a00",  # 5.01:1 (darkened from #ff7f0e which was 2.43:1)
    "institutional": "#1e7d32", # 4.99:1 (darkened from #2ca02c which was 3.26:1)
    "political":    "#b71c1c",  # 6.29:1 (darkened from #d62728)
    "legal":        "#6a1b9a",  # 9.00:1 (darkened from #9467bd which was 4.08:1)
    "media":        "#5d4037",  # 8.93:1 (darkened from #8c564b)
}
# ── Universal design: dual-coding — domain encoded by SHAPE as well as color ──
# (color-blind + screen-reader users get the same signal from shape alone)
domain_shapes = {
    "government":   "square",   # ■
    "economic":     "circle",   # ●
    "institutional":"triangle", # ▲
    "political":    "diamond",  # ◆
    "legal":        "hexagon",  # ⬢
    "media":        "pentagon", # ⬟
}
# ── Money channel: which nodes receive government-created wealth, and which
#    edges are money flows (from evidence/28-source-of-economic-power.md) ──
money_nodes = {
    "jblm","multicare","puyallup-tribe","weyerhaeuser","port-tacoma","chamber",
    "gtcf","county-council","pierce-transit","tacoma-schools","puyallup-schools",
    "bethel-schools","clover-park-schools","sound-transit","metro-parks",
    "west-pierce-fire","central-pierce-fire","superior-court","district-court",
    "uw-tacoma","plu","tcc","vmfh","catholic-archdiocese","life-center",
    # new money-source actors from the audit (evidence/28 structural capture)
    "rush-development","miles-sand-gravel","southport","tucci-sons","lincoln-park",
    "nall-capital","wa-realtors-pac","tacoma-housing-auth","saltchuk","nwsa",
    "pierce-county-econ-dev","edb","sumner-bonney-lake","university-place-schools",
    "east-pierce-fire","gig-harbor-fire","pierce-county-library","flood-control-zone",
    "tacoma-public-utilities","wellfound","commonspirit","bates-tech","cheney-foundation",
}
# relationship types that represent money flowing (public $ → actor, or $ → influence)
# SURGICAL: only actual money-flow / government-created-wealth relationships, so the
# "Follow the money" view highlights the structural-capture loop (evidence/28), not everything.
money_rels = {
    # government-created wealth (the structural-capture loop, step 1)
    "federal_appropriations","tax_exemption","sovereignty","federal_land_grant",
    "property_tax_levy","tax_exempt","levy","levy_funding","taxing","municipal",
    "federal_funding","state_funding","transit_funding","appropriates",
    "school_bond","ballot_measure",
    # money → influence (campaign finance, lobbying, PACs)
    "donated","ie","lobbying","lobbies","endorses","trains_candidates",
    # money flowing through partnerships / ownership
    "wellfound_jv","jv","owned_by","operates","parent",
}
money_edges = set()
for e in all_edges:
    if e.get("relationship","") in money_rels:
        money_edges.add((e["source"], e["target"]))
        money_edges.add((e["target"], e["source"]))

# ── Layout: viewBox matches a 2560x1440 screen (1:1 pixels, no downscaling) ──
W, H = 2560, 1440
PAD = 60
pos = nx.spring_layout(G, k=1.8, iterations=400, seed=7)
xs = [pos[n][0] for n in G.nodes()]; ys = [pos[n][1] for n in G.nodes()]
minx, maxx = min(xs), max(xs); miny, maxy = min(ys), max(ys)
def to_svg(x, y):
    return (PAD + (x-minx)/(maxx-minx)*(W-2*PAD), PAD + (y-miny)/(maxy-miny)*(H-2*PAD))
svg_pos = {n: to_svg(*pos[n]) for n in G.nodes()}

# ── Robust label placement: greedy ring search with exact rect-overlap check ──
# Place labels one at a time (strongest first), each at the nearest position to
# its node that does NOT overlap any already-placed label rect. Exact check, so
# the result is guaranteed overlap-free and deterministic. Leader lines connect
# each label to its node.
FONT = 40  # big, readable labels on a 2560x1440 screen (only 24 labels now, so room to be large)
def text_width(txt):
    return 0.62 * FONT * len(txt)
def label_bbox(cx, cy, txt):
    w = text_width(txt); h = FONT * 1.4
    return (cx - w/2, cy - h, w, h)
def rects_overlap(b1, b2, pad=6):
    return not (b1[0]+b1[2]+pad < b2[0] or b2[0]+b2[2]+pad < b1[0] or
                b1[1]+b1[3]+pad < b2[1] or b2[1]+b2[3]+pad < b1[1])

import math as _m
placed_rects = []  # list of (x, y, w, h) bboxes for already-placed labels (x,y = top-left)
label_placements = {}  # node -> (x, y) center
# order by power so strongest get prime placement
ordered = sorted(label_nodes, key=lambda n: -composite[n])
for n in ordered:
    x, y = svg_pos[n]; r = node_radius(n); label = G.nodes[n]["label"]
    w = text_width(label); h = FONT * 1.4
    # search outward in expanding rings for the nearest non-overlapping position
    placed = False
    for radius in range(0, 2000, 12):
        for ang in range(0, 360, 10):
            cx = x + radius * _m.cos(_m.radians(ang))
            cy = y + radius * _m.sin(_m.radians(ang))
            cx = max(w/2+10, min(W-w/2-10, cx))
            cy = max(h+10, min(H-10, cy))
            rect = (cx - w/2, cy - h, w, h)  # proper bbox: top-left at (cx-w/2, cy-h)
            if not any(rects_overlap(rect, pr, pad=6) for pr in placed_rects):
                label_placements[n] = (cx, cy)
                placed_rects.append(rect)
                placed = True
                break
        if placed: break
    if not placed:
        # fallback: place at node (should never happen on a large canvas)
        label_placements[n] = (x, y)
        placed_rects.append((x - w/2, y - h, w, h))

# verify no overlaps remain (exact, pad=4)
overlap_count = 0
for i in range(len(placed_rects)):
    for j in range(i+1, len(placed_rects)):
        if rects_overlap(placed_rects[i], placed_rects[j], pad=4):
            overlap_count += 1
print(f"Labels placed: {len(label_placements)} | remaining overlaps: {overlap_count}")

# ── Build SVG ──
svg_parts = [f'<svg id="net" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" height="100%" style="background:#fafafa" role="img" aria-label="Pierce County power network graph">',
             f'<rect id="bg-clear" x="0" y="0" width="{W}" height="{H}" fill="transparent" style="cursor:default;"/>']
for u, v, d in G.edges(data=True):
    x1, y1 = svg_pos[u]; x2, y2 = svg_pos[v]; w = d.get("weight", 1)
    op = min(0.12 + w/22, 0.55); sw = 0.5 + w/7
    is_money = "1" if (u,v) in money_edges else "0"
    svg_parts.append(f'<line id="e-{u}-{v}" class="edge" data-u="{u}" data-v="{v}" data-money="{is_money}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#999" stroke-width="{sw:.2f}" stroke-opacity="{op:.2f}"/>')
for n in G.nodes():
    x, y = svg_pos[n]; domain = G.nodes[n]["domain"]; color = domain_colors.get(domain, "#333")
    r = node_radius(n); label = G.nodes[n]["label"]; shape = domain_shapes.get(domain, "circle")
    # focus ring (gold) — always present, shown on focus
    svg_parts.append(f'<circle id="ring-{n}" class="ring" cx="{x:.1f}" cy="{y:.1f}" r="{r+6:.1f}" fill="none" stroke="#ffd700" stroke-width="4" stroke-opacity="0" style="display:none;"/>')
    # money ring (gold, dashed) — shown when "Follow the money" is ON and node receives public $
    if n in money_nodes:
        svg_parts.append(f'<circle id="mring-{n}" class="mring" cx="{x:.1f}" cy="{y:.1f}" r="{r+11:.1f}" fill="none" stroke="#B8860B" stroke-width="3" stroke-dasharray="6,4" stroke-opacity="0" style="display:none;"/>')
    # node shape by domain (dual-coding: shape + color)
    if shape == "square":
        s = r*0.9
        svg_parts.append(f'<rect id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" x="{x-s:.1f}" y="{y-s:.1f}" width="{2*s:.1f}" height="{2*s:.1f}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    elif shape == "triangle":
        pts = f"{x:.1f},{y-r:.1f} {x+r*0.87:.1f},{y+r*0.5:.1f} {x-r*0.87:.1f},{y+r*0.5:.1f}"
        svg_parts.append(f'<polygon id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    elif shape == "diamond":
        pts = f"{x:.1f},{y-r:.1f} {x+r:.1f},{y:.1f} {x:.1f},{y+r:.1f} {x-r:.1f},{y:.1f}"
        svg_parts.append(f'<polygon id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    elif shape == "hexagon":
        pts = " ".join(f"{x+r*_m.cos(_m.radians(a)):.1f},{y+r*_m.sin(_m.radians(a)):.1f}" for a in range(0,360,60))
        svg_parts.append(f'<polygon id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    elif shape == "pentagon":
        pts = " ".join(f"{x+r*_m.cos(_m.radians(a-90)):.1f},{y+r*_m.sin(_m.radians(a-90)):.1f}" for a in range(0,360,72))
        svg_parts.append(f'<polygon id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" points="{pts}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    else:  # circle (economic)
        svg_parts.append(f'<circle id="n-{n}" class="node" data-id="{n}" data-label="{label}" tabindex="0" role="button" aria-label="{label}, {domain}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" fill-opacity="1" stroke="#fff" stroke-width="1.5" cursor="pointer"/>')
    if n in label_placements:
        lx, ly = label_placements[n]
        # leader line from node to label (drawn under the text, subtle)
        ax, ay = svg_pos[n]
        svg_parts.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="#999" stroke-width="0.8" stroke-opacity="0.35" stroke-dasharray="2,2"/>')
        # NOTE: labels are rendered as HTML overlay divs (not SVG <text>) so they
        # stay at a constant readable pixel size regardless of SVG viewBox scaling.
        # See label_overlays below.
svg_parts.append('</svg>')

# ── HTML label overlays (constant pixel size, NOT scaled with SVG) ──
# Convert SVG coords to percentage of the SVG viewBox so the divs track the nodes
# even as the SVG scales to fit the viewport. Font size is fixed in px (readable).
label_overlays = []
for n in label_placements:
    lx, ly = label_placements[n]
    label = G.nodes[n]["label"]
    pct_x = lx / W * 100
    pct_y = ly / H * 100
    # Top-5 are persistent; the rest are hidden until their node is hovered/focused
    persistent = "1" if n in TOP5_LABELS else "0"
    label_overlays.append(
        f'<div class="label" data-id="{n}" data-persist="{persistent}" aria-hidden="true" style="left:{pct_x:.2f}%;top:{pct_y:.2f}%;'
        f'transform:translate(-50%,-50%);{"display:none;" if persistent=="0" else ""}">{label}</div>'
    )
label_overlays_html = "\n".join(label_overlays)

# ── App bar (top): title + thesis + money switch (the hero control) ──
appbar = """
<div id="appbar" style="position:absolute; top:0; left:0; right:0; height:56px; background:#1B1B1B; color:#FAFAFA; display:flex; align-items:center; padding:0 20px; box-shadow:0 2px 8px rgba(0,0,0,0.3); z-index:10; font-family:sans-serif;">
  <div style="font-size:16px; font-weight:bold; white-space:nowrap;">Pierce County Power Network</div>
  <div style="flex:1; margin-left:20px; font-size:13px; color:#ccc; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
    <span id="appbar-thesis">Government creates wealth → private power converts it → policy returns it. <span style="color:#E8C547; font-weight:bold;">This is the structural-capture loop.</span></span>
    <span id="appbar-mission" style="display:none; color:#E8C547; font-weight:bold;"></span>
  </div>
  <!-- Follow the money: the hero control, a gold-ring chip switch -->
  <button id="money-toggle" role="switch" aria-checked="false" aria-label="Follow the money: show public money flows" style="display:flex; align-items:center; gap:8px; background:transparent; border:2px dashed #B8860B; border-radius:20px; padding:4px 12px; cursor:pointer; margin-right:12px; font-family:sans-serif;">
    <span id="money-switch" style="width:36px; height:20px; border-radius:10px; background:#555; position:relative; flex-shrink:0; transition:background 0.2s;"><span id="money-thumb" style="position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:50%; background:#fff; transition:left 0.2s; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:bold; color:#1B1B1B;">$</span></span>
    <span id="money-label" style="color:#E8C547; font-size:13px; font-weight:bold;">Follow the money</span>
  </button>
  <button id="begin-btn" style="background:#E8C547; border:none; color:#1B1B1B; border-radius:4px; padding:4px 12px; font-size:13px; font-weight:bold; cursor:pointer; margin-right:8px;" aria-label="Begin the guided investigation">Begin investigation</button>
  <button id="about-btn" style="background:transparent; border:1px solid #555; color:#FAFAFA; border-radius:4px; padding:4px 12px; font-size:13px; cursor:pointer;" aria-label="About this investigation">About</button>
</div>
"""

# ── (Guided mission system lives in the rail guide card + app-bar status strip;
#    no modal overlay — see JS MISSION array) ──

# ── Left rail: the loop diagram (legend + thesis), domain legend, money toggle, top-10 ──
# Shape glyphs for the domain legend (dual-coding: shape + color)
shape_glyph = {
    "square": "&#9632;", "circle": "&#9679;", "triangle": "&#9650;",
    "diamond": "&#9670;", "hexagon": "&#11022;", "pentagon": "&#11021;",
}
legend_rows = []
for dom in ["government","economic","institutional","political","legal","media"]:
    c = domain_colors[dom]; g = shape_glyph[domain_shapes[dom]]
    legend_rows.append(f'<div style="display:flex; align-items:center; gap:8px; font-size:13px; color:#1B1B1B; padding:2px 0;"><span style="color:{c}; width:16px; text-align:center;">{g}</span><span style="text-transform:capitalize;">{dom}</span></div>')
legend_html = "\n".join(legend_rows)

rail = """
<div id="rail" style="position:absolute; top:56px; left:0; bottom:0; width:280px; background:#FAFAFA; border-right:1px solid #E0E0E0; padding:16px; box-sizing:border-box; overflow-y:auto; z-index:9; font-family:sans-serif;">
  <!-- Guide card: the in-grain coach (mission system) — slim, one-line prompt + collapsible key fact -->
  <div id="guide-card" style="background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:12px; margin-bottom:16px; display:none;">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
      <span style="font-size:11px; font-weight:bold; color:#B8860B; text-transform:uppercase; letter-spacing:1px;">Mission <span id="guide-num">1</span> of 7</span>
      <button id="guide-skip" style="background:none; border:none; color:#888; font-size:12px; cursor:pointer; text-decoration:underline;">Skip</button>
    </div>
    <div id="guide-title" style="font-size:15px; font-weight:bold; color:#1B1B1B; margin-bottom:4px;"></div>
    <div id="guide-body" style="font-size:13px; color:#333; line-height:1.5; margin-bottom:8px;"></div>
    <div id="guide-fact" style="background:#FFF8E1; border-left:4px solid #B8860B; padding:8px 10px; border-radius:4px; font-size:12px; color:#5D4037; display:none;"></div>
    <div id="guide-progress" style="display:flex; gap:4px; margin-top:10px;"></div>
  </div>
  <!-- The loop: the thesis as a diagram — ALWAYS visible (it's the story) -->
  <div id="loop-card" style="background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:12px; margin-bottom:16px; cursor:pointer;" role="button" tabindex="0" aria-label="The structural-capture loop: Wealth to Power to Policy">
    <div style="font-size:13px; font-weight:bold; color:#1B1B1B; margin-bottom:8px;">How power works here</div>
    <div style="display:flex; align-items:center; justify-content:space-between; font-size:13px; font-weight:bold;">
      <span style="color:#B8860B;">Wealth</span><span style="color:#888;">→</span>
      <span style="color:#1f77b4;">Power</span><span style="color:#888;">→</span>
      <span style="color:#1e7d32;">Policy</span>
    </div>
    <div style="font-size:11px; color:#666; margin-top:6px; line-height:1.4;">
      Public money (levies, appropriations, tax breaks) becomes private power, which shapes policy, which returns more money.
    </div>
  </div>
  <!-- Domain legend — ALWAYS visible (the user must always be able to read the map) -->
  <div id="legend-card" style="margin-bottom:16px;">
    <div style="font-size:13px; font-weight:bold; color:#1B1B1B; margin-bottom:6px;">Domains</div>
    <div>__LEGEND__</div>
  </div>
  <button id="top10-btn" style="display:none; width:100%; background:#1B1B1B; color:#FAFAFA; border:none; border-radius:8px; padding:10px 12px; cursor:pointer; font-size:13px; font-weight:bold;">Top 10 by power</button>
  <!-- More disclosure: reveal all cards for free-exploration users -->
  <button id="more-btn" style="display:none; width:100%; background:transparent; border:1px solid #E0E0E0; color:#1B1B1B; border-radius:8px; padding:8px 12px; cursor:pointer; font-size:12px; margin-top:12px;">More</button>
</div>
""".replace("__LEGEND__", legend_html)

# ── Right drawer (slides in): node details + top-10 list ──
drawer = """
<div id="drawer" style="position:absolute; top:56px; right:0; bottom:0; width:340px; background:#FAFAFA; border-left:1px solid #E0E0E0; box-shadow:-4px 0 20px rgba(0,0,0,0.15); transform:translateX(105%); transition:transform 0.25s ease; z-index:9; font-family:sans-serif; display:flex; flex-direction:column;">
  <div style="display:flex; align-items:center; justify-content:space-between; padding:14px 16px; border-bottom:1px solid #E0E0E0;">
    <div id="drawer-title" style="font-size:15px; font-weight:bold; color:#1B1B1B;">Details</div>
    <button id="drawer-close" aria-label="Close details" style="background:none; border:none; font-size:22px; color:#444; cursor:pointer;">&times;</button>
  </div>
  <div id="drawer-content" style="flex:1; overflow-y:auto; padding:16px;"></div>
</div>
"""

node_data = {}
for n in all_nodes:
    # Build connection info with relationship + direction for thesis-grouping
    conns = {}
    for e in all_edges:
        if e["source"] == n["id"]:
            conns.setdefault(e["target"], []).append({"rel": e.get("relationship",""), "dir": "out"})
        if e["target"] == n["id"]:
            conns.setdefault(e["source"], []).append({"rel": e.get("relationship",""), "dir": "in"})
    node_data[n["id"]] = {
        "label": n["label"], "type": n["type"], "domain": n["domain"],
        "desc": n.get("desc",""), "facts": n.get("facts",[]),
        "profile": render_profile_html(n["id"]),
        "power": round(composite[n["id"]], 3),
        "conns": {cid: conns[cid] for cid in conns},
    }
node_data_js = json.dumps(node_data)

js = """
<script>
const NODE_DATA = __NODE_DATA__;
const domainColor = {government:"#1f77b4",economic:"#b84a00",institutional:"#1e7d32",political:"#b71c1c",legal:"#6a1b9a",media:"#5d4037"};
const domainShape = {government:"square",economic:"circle",institutional:"triangle",political:"diamond",legal:"hexagon",media:"pentagon"};
const shapeGlyph = {square:"&#9632;",circle:"&#9679;",triangle:"&#9650;",diamond:"&#9670;",hexagon:"&#11022;",pentagon:"&#11021;"};
let currentFocus = null;
let moneyOn = true;
let drawerOpen = false;

function setFocus(id){
  document.querySelectorAll('.ring').forEach(r=>{ r.style.display='none'; r.style.strokeOpacity='0'; });
  document.querySelectorAll('.node').forEach(n=>{ n.style.stroke='#fff'; n.style.strokeWidth='1.5'; n.style.opacity='1'; });
  document.querySelectorAll('.edge').forEach(e=>{ e.style.stroke='#999'; e.style.strokeOpacity=e.dataset.baseop||'0.3'; e.style.opacity='1'; });
  if(!id){ currentFocus=null; return; }
  currentFocus = id;
  const ring = document.getElementById('ring-'+id);
  if(ring){ ring.style.display='block'; ring.style.strokeOpacity='1'; }
  const node = document.getElementById('n-'+id);
  if(node){ node.style.stroke='#000'; node.style.strokeWidth='3.5'; }
  const neighbors = new Set([id]);
  document.querySelectorAll('.edge').forEach(e=>{
    if(e.dataset.u===id||e.dataset.v===id){ neighbors.add(e.dataset.u); neighbors.add(e.dataset.v); }
  });
  document.querySelectorAll('.node').forEach(n=>{
    if(!neighbors.has(n.dataset.id)){ n.style.opacity='0.15'; }
  });
  document.querySelectorAll('.edge').forEach(e=>{
    if(e.dataset.u===id||e.dataset.v===id){ e.style.stroke='#333'; e.style.strokeOpacity='0.7'; }
    else { e.style.opacity='0.12'; }
  });
}

function openDrawer(){ document.getElementById('drawer').style.transform='translateX(0)'; drawerOpen=true; }
function closeDrawer(){ document.getElementById('drawer').style.transform='translateX(105%)'; drawerOpen=false; }

// ── Thesis-driven entity panel (HCD/UDL): nudges the user toward the
//    money→people→systems loop. WHO → WHERE power comes from → HOW → WHAT.
//    Progressive disclosure: above the fold = header + thesis + ONE focal element;
//    everything else behind a "More" accordion. Relationships are triple-coded
//    (color + icon + arrow) so they're SEEN, not read. ──
const MONEY_RELS = new Set(["federal_appropriations","tax_exemption","sovereignty","federal_land_grant",
  "property_tax_levy","tax_exempt","levy","levy_funding","taxing","municipal","federal_funding",
  "state_funding","transit_funding","appropriates","school_bond","ballot_measure","donated","ie","lobbying","lobbies","endorses",
  "trains_candidates","wellfound_jv","jv","owned_by","operates","parent"]);
const INFLUENCE_RELS = new Set(["donated","ie","lobbying","lobbies","endorses","trains_candidates",
  "influence","advocates","oversight","appoints","appoints_judges","armed_services_champion"]);
const INTERLOCK_RELS = new Set(["board","board_chair","chair","ceo","president","exec","director",
  "former_board","former","advisor","acting_director","chairman","vice_chair","commissioner",
  "exec_director","ed","council","member","founded_by","legacy","honored"]);

// ── Relationship visual system: color + icon + arrow (triple-redundant cues) ──
function relClass(rel){
  if(MONEY_RELS.has(rel)) return 'money';
  if(INFLUENCE_RELS.has(rel)) return 'influence';
  if(INTERLOCK_RELS.has(rel)) return 'interlock';
  return 'structural';
}
function relIcon(cls){ return cls==='money'?'$':cls==='influence'?'→':cls==='interlock'?'⬡':'⚙'; }
function relArrow(cls, dir){
  if(cls==='interlock') return '↔';
  return dir==='out' ? '→' : '←';
}
function relChip(cid, label, rel, dir){
  const cls = relClass(rel);
  const icon = relIcon(cls);
  const arrow = relArrow(cls, dir);
  const target = NODE_DATA[cid];
  const tcolor = target?domainColor[target.domain]||'#333':'#333';
  let style;
  if(cls==='money') style = `background:#FFF8E1;border:1px solid #B8860B;color:#B8860B;`;
  else if(cls==='influence') style = `background:${tcolor}1A;border:1px solid ${tcolor};color:${tcolor};`;
  else if(cls==='interlock') style = `background:#1B1B1B;color:#FAFAFA;border:1px solid #1B1B1B;`;
  else style = `background:#eee;border:1px solid #666;color:#666;`;
  const sentence = cls==='money' ? `Money ${dir==='out'?'flows to':'comes from'} ${label}`
    : cls==='influence' ? `${dir==='out'?'Influences':'Influenced by'} ${label}`
    : cls==='interlock' ? `Board interlock with ${label}`
    : `Related to ${label}`;
  return `<span onclick="navigateTo('${cid}')" role="button" tabindex="0" onkeydown="if(event.key==='Enter')navigateTo('${cid}')" aria-label="${sentence}" style="display:inline-block;border-radius:4px;padding:2px 6px;margin:2px;font-size:12px;cursor:pointer;${style}"><span aria-hidden="true">${icon}</span> ${label} <span aria-hidden="true">${arrow}</span></span>`;
}
function groupBlock(title, items){
  if(!items.length) return '';
  return `<div style="font-size:12px;font-weight:bold;margin:8px 0 3px;color:#1a1a1a;">${title}</div><div>${items.join('')}</div>`;
}

function renderPanel(id){
  const d = NODE_DATA[id];
  if(!d) return;
  const color = domainColor[d.domain]||"#333";
  const glyph = shapeGlyph[domainShape[d.domain]]||"&#9679;";
  const facts = (d.facts||[]).map(f=>`<li>${f}</li>`).join('');
  const conns = d.conns||{};

  // ── 1. Thesis strip ──
  let thesis = '';
  if(d.domain==='government') thesis = `Holds public office → funded by taxpayers → influenced by donors & lobbyists`;
  else if(d.domain==='media') thesis = `Owned by a parent → shapes the public story`;
  else if(d.domain==='economic'||d.domain==='institutional') thesis = `Receives public money → converts it to influence → shapes policy`;
  else thesis = `Sits across the power network → the connections are the story`;

  // ── Classify all connections ──
  const moneyIn=[], moneyOut=[], inflIn=[], inflOut=[], interlocks=[], structural=[];
  Object.entries(conns).forEach(([cid,rs])=>{
    const lbl = NODE_DATA[cid]?NODE_DATA[cid].label:cid;
    rs.forEach(r=>{
      const cls = relClass(r.rel);
      if(cls==='money' && r.dir==='in') moneyIn.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='money' && r.dir==='out') moneyOut.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='influence' && r.dir==='in') inflIn.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='influence' && r.dir==='out') inflOut.push(relChip(cid,lbl,r.rel,r.dir));
      else if(cls==='interlock') interlocks.push(relChip(cid,lbl,r.rel,r.dir));
      else structural.push(relChip(cid,lbl,r.rel,r.dir));
    });
  });

  // ── 2. ONE focal element (priority switch, first match wins) ──
  let focal = '';
  if(moneyIn.length){
    // Money-source callout
    const src = Object.keys(conns).find(cid=>conns[cid].some(r=>MONEY_RELS.has(r.rel)&&r.dir==='in'));
    const srcLabel = NODE_DATA[src]?NODE_DATA[src].label:src;
    const rel = conns[src].find(r=>MONEY_RELS.has(r.rel)&&r.dir==='in').rel;
    focal = `
      <div style="background:#FAFAFA;border:1px solid #B8860B;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:1px;">Where the power comes from</div>
        <div style="font-size:15px;font-weight:bold;color:#B8860B;margin:2px 0;">${rel.replace(/_/g,' ')}</div>
        <div style="font-size:12px;color:#1a1a1a;">via <b>${srcLabel}</b> — public money granted by government.</div>
      </div>`;
  } else if(interlocks.length>=2){
    // "Multiple hats" strip
    focal = `
      <div style="background:#1B1B1B;color:#FAFAFA;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#E8C547;text-transform:uppercase;letter-spacing:1px;">Multiple hats — the interlock</div>
        <div style="font-size:12px;margin-top:4px;">${interlocks.slice(0,3).join('')}</div>
      </div>`;
  } else if(inflIn.length){
    // Who influences them
    focal = `
      <div style="background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#1a1a1a;text-transform:uppercase;letter-spacing:1px;">Who influences them</div>
        <div style="font-size:12px;margin-top:4px;">${inflIn.slice(0,3).join('')}</div>
      </div>`;
  } else if(inflOut.length){
    // Where its power leads
    focal = `
      <div style="background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:10px 12px;margin:8px 0;">
        <div style="font-size:11px;font-weight:bold;color:#1a1a1a;text-transform:uppercase;letter-spacing:1px;">Where its power leads</div>
        <div style="font-size:12px;margin-top:4px;">${inflOut.slice(0,3).join('')}</div>
      </div>`;
  }

  // ── 3. Full content (behind the "More" accordion) ──
  const connsHtml = groupBlock('Money flows to', moneyOut)
    + groupBlock('Influences', inflOut)
    + groupBlock('Influenced by', inflIn)
    + groupBlock('Board interlocks', interlocks)
    + groupBlock('Structural', structural);
  let nudge = '';
  if(moneyIn.length){
    const src = Object.keys(conns).find(cid=>conns[cid].some(r=>MONEY_RELS.has(r.rel)&&r.dir==='in'));
    const srcLabel = NODE_DATA[src]?NODE_DATA[src].label:src;
    nudge = `Follow the money: see who funds <b>${srcLabel}</b>.`;
  } else if(interlocks.length) nudge = `Trace the interlock: see the other boards this entity sits on.`;
  else if(inflIn.length) nudge = `See who influences this entity.`;
  else nudge = `Explore this entity's connections to see where its power leads.`;

  document.getElementById('drawer-title').textContent = d.label;
  // Default: render the NEARLY-FULL researched profile (sections 0–12) for this entity,
  // with the triple-coded relationship chips as the clickable "expansion" into related
  // entities. Progressive disclosure is preserved only for the (rare) un-researched
  // node, which falls back to the graph desc/facts.
  const profileBody = d.profile || (
    `<div style="font-size:13px;color:#1a1a1a;line-height:1.5;">${
      d.desc?`<p>${d.desc}</p>`:''}${
      (d.facts||[]).length?`<ul>${d.facts.map(f=>`<li>${f}</li>`).join('')}</ul>`:''}</div>`
  );
  document.getElementById('drawer-content').innerHTML = `
    <div style="font-size:12px;color:#444;margin:0 0 8px;">${d.type} · ${d.domain} · <span style="background:#E8C547;color:#1B1B1B;border-radius:4px;padding:1px 6px;font-weight:bold;">Power ${d.power}</span></div>
    <div style="font-size:13px;color:#1a1a1a;background:#fff;border:1px solid #E0E0E0;border-radius:8px;padding:8px 10px;margin-bottom:8px;" aria-label="This entity's role in the money-to-power loop">${thesis}</div>
    ${focal}
    ${connsHtml}
    <div class="profile-wrap" style="margin-top:10px;">${profileBody}</div>
  `;
  openDrawer();
  setFocus(id);
}
function togglePanelMore(){}

function renderTop10(){
  const top = Object.keys(NODE_DATA).map(k=>NODE_DATA[k]).sort((a,b)=>b.power-a.power).slice(0,10);
  document.getElementById('drawer-title').textContent = 'Top 10 by power';
  document.getElementById('drawer-content').innerHTML = top.map((d,i)=>{
    const c = domainColor[d.domain]||"#333";
    const glyph = shapeGlyph[domainShape[d.domain]]||"&#9679;";
    const cid = Object.keys(NODE_DATA).find(k=>NODE_DATA[k].label===d.label);
    return `<div onclick="navigateTo('${cid}')" role="button" tabindex="0" onkeydown="if(event.key==='Enter')navigateTo('${cid}')" style="display:flex;align-items:center;gap:8px;padding:8px;border-radius:6px;cursor:pointer;font-size:13px;color:#1a1a1a;border-bottom:1px solid #eee;">
      <span style="width:18px;text-align:right;color:#888;font-weight:bold;">${i+1}</span>
      <span style="color:${c};width:16px;text-align:center;">${glyph}</span>
      <span style="flex:1;font-weight:500;">${d.label}</span>
      <span style="color:#666;font-size:12px;">${d.power.toFixed(2)}</span>
    </div>`;
  }).join('');
  openDrawer();
}

function navigateTo(id){
  history.pushState({node:id}, '', '#node-'+id);
  renderPanel(id);
}

window.addEventListener('popstate', (e)=>{
  if(e.state && e.state.node){ renderPanel(e.state.node); }
  else { closeDrawer(); setFocus(null); }
});

document.querySelectorAll('.node').forEach(n=>{
  n.addEventListener('click', ()=>navigateTo(n.dataset.id));
  n.addEventListener('keydown', (e)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); navigateTo(n.dataset.id); } });
  // hover/focus reveals the node's label (if it has one)
  const showLabel = ()=>{ const l=document.querySelector(`.label[data-id="${n.dataset.id}"]`); if(l) l.style.display='block'; };
  const hideLabel = ()=>{ const l=document.querySelector(`.label[data-id="${n.dataset.id}"]`); if(l && l.dataset.persist==='0') l.style.display='none'; };
  n.addEventListener('mouseenter', showLabel);
  n.addEventListener('mouseleave', hideLabel);
  n.addEventListener('focus', showLabel);
  n.addEventListener('blur', hideLabel);
});
document.getElementById('drawer-close').addEventListener('click', ()=>{
  history.pushState({node:null}, '', '#');
  closeDrawer(); setFocus(null);
});
// Non-happy-path: clicking empty canvas clears selection (clear-focus affordance)
document.getElementById('bg-clear').addEventListener('click', ()=>{
  history.pushState({node:null}, '', '#');
  closeDrawer(); setFocus(null);
});
document.getElementById('top10-btn').addEventListener('click', renderTop10);
document.getElementById('about-btn').addEventListener('click', ()=>{
  document.getElementById('drawer-title').textContent = 'About';
  document.getElementById('drawer-content').innerHTML = `
    <div style="font-size:14px;color:#1a1a1a;line-height:1.6;">
      <b>Pierce County Leadership Investigation (INV-2026-002)</b><br><br>
      Maps the __NODE_COUNT__ most powerful actors across 6 domains and __EDGE_COUNT__ relationships.<br><br>
      <b>The core finding:</b> Pierce County's major economic institutions derive substantial power from government-granted privileges — federal appropriations (JBLM ~$12.1B across Pierce+Thurston), tax exemptions (MultiCare ~$7.2B), land grants (Weyerhaeuser 10.4M acres), sovereignty (Puyallup Tribe), and public levies (Port of Tacoma). These institutions in turn influence the government that grants those privileges — a structural interdependence that warrants scrutiny.<br><br>
      Node size = composite power score (area ∝ power). Shape = domain. Gold ring = receives public money. Toggle "Follow the money" to see money flows.
    </div>`;
  openDrawer();
});

// ── Follow the money toggle (hero control in the app-bar) ──
function applyMoney(on){
  moneyOn = on;
  document.querySelectorAll('.mring').forEach(r=>{ r.style.display = on ? 'block' : 'none'; r.style.strokeOpacity = on ? '1' : '0'; });
  document.querySelectorAll('.edge').forEach(e=>{
    if(e.dataset.money==='1'){
      e.style.stroke = on ? '#B8860B' : '#999';
      e.style.strokeOpacity = on ? '0.6' : (e.dataset.baseop||'0.3');
    }
  });
  const sw = document.getElementById('money-switch');
  const thumb = document.getElementById('money-thumb');
  sw.style.background = on ? '#B8860B' : '#555';
  thumb.style.left = on ? '18px' : '2px';
  document.getElementById('money-toggle').setAttribute('aria-checked', on ? 'true':'false');
  // money legend (bottom-left of canvas) appears when money is ON
  const legend = document.getElementById('money-legend');
  if(legend){ legend.style.display = on ? 'block' : 'none'; }
}
let userToggledMoney = false;  // non-happy-path: track if the user toggled money themselves
document.getElementById('money-toggle').addEventListener('click', ()=>{
  userToggledMoney = true;
  applyMoney(!moneyOn);
  if(missionIdx===1) completeMission();  // mission 2 (index 1) = follow the money
});
applyMoney(false);  // money starts OFF — calm first impression; appears only when toggled

// ── Guided mission system: learn the investigation BY USING the page ──
// Each mission is a real action the user performs on the page; the guide
// advances only when the action is actually completed (no fake "Next").
const MISSIONS = [
  {title:"Find the most powerful",
   body:"This map holds __NODE_COUNT__ people and organizations. The bigger a node, the more powerful it is. Find the largest node — that's the most powerful actor in Pierce County.",
   fact:"Key fact: The most powerful actor is Ryan Mello, the Pierce County Executive. The Chamber of Commerce and County Council round out the top three.",
   target:"ryan-mello", type:"node"},
  {title:"Follow the money",
   body:"Click the gold 'Follow the money' switch in the top bar. Watch the gold rings and gold lines appear on the map. Gold = public money — government-created wealth.",
   fact:"Key fact: JBLM's economic impact is ~$12.1B across Pierce+Thurston counties (Pierce-only direct ~$3.9B). MultiCare takes in ~$7.2B, largely from government programs. The Puyallup Tribe's 1990 land-claims settlement was $162M + 900 acres.",
   target:null, type:"toggle"},
  {title:"Spot the funded",
   body:"Find an actor with a gold dashed ring — that's one that receives public money. Click it to open its details. The drawer shows who they are, their power score, and key facts.",
   fact:"Key fact: Weyerhaeuser owns 10.4 million acres — originally granted by the federal government in 1864. The Port of Tacoma moves $76 billion in cargo, funded by a public levy.",
   target:"jblm", type:"node"},
  {title:"Read the shapes",
   body:"Each node's SHAPE and COLOR tell you its domain. Squares are government, circles are economic, triangles are institutional, diamonds are political, hexagons are legal, pentagons are media. Click any node to see its domain in the drawer.",
   fact:"Key fact: The six domains are Government, Economic, Institutional, Political, Legal, and Media. Shape matters as much as color — so even color-blind users can read it.",
   target:null, type:"anynode"},
  {title:"Trace the loop",
   body:"Click the loop diagram in the left panel — Wealth → Power → Policy. This is the structural-capture loop: public money becomes private power, which shapes policy, which returns more money.",
   fact:"Key fact: The people who benefit most from public money are often the ones deciding how public money is spent.",
   target:null, type:"loop"},
  {title:"Follow a connection",
   body:"Open any node, then click a 'connected to' chip to jump to that actor. Use your browser's Back button to undo. This is how you explore the web of relationships.",
   fact:"Key fact: One striking detail: Tom Pierson is simultaneously the Chamber of Commerce's interim CEO AND the county's acting economic development director — the same person on both sides of the table.",
   target:null, type:"connection"},
  {title:"See the ranking",
   body:"Click 'Top 10 by power' in the left panel to see the full ranking of the most powerful actors. This is the investigation's bottom line.",
   fact:"Key fact: Pierce County is a 'growth machine' — an interlocking business-political-philanthropic elite that converts public resources into private power, then uses that power to shape public policy.",
   target:null, type:"top10"},
];
let missionIdx = -1;  // -1 = not started
let missionDone = false;

function showMission(i){
  missionIdx = i;
  const m = MISSIONS[i];
  document.getElementById('guide-card').style.display='block';
  document.getElementById('guide-num').textContent = i+1;
  document.getElementById('guide-title').textContent = m.title;
  document.getElementById('guide-body').textContent = m.body;
  const f = document.getElementById('guide-fact');
  f.textContent = m.fact; f.style.display='block';
  // progress dots
  document.getElementById('guide-progress').innerHTML = MISSIONS.map((_,j)=>
    `<span style="width:10px;height:10px;border-radius:50%;background:${j<i?'#B8860B':(j===i?'#E8C547':'#ddd')};display:inline-block;"></span>`).join('');
  // app-bar status — keep the thesis visible alongside the mission status
  // (non-happy-path fix: a skipper should never lose the one-line thesis)
  document.getElementById('appbar-thesis').style.display='inline';
  const ms = document.getElementById('appbar-mission');
  ms.style.display='inline'; ms.textContent = ` · Mission ${i+1} of ${MISSIONS.length} · ${m.title}`;
  // progressive disclosure: reveal the rail card this mission needs
  // (loop-card and legend-card are ALWAYS visible — the thesis and legend are
  //  permanent; only the Top 10 button is mission-revealed)
  document.getElementById('top10-btn').style.display = (m.type==='top10') ? 'block' : 'none';
  document.getElementById('more-btn').style.display = 'block';
  // pre-arm page state per mission
  // (non-happy-path fix: only pre-arm money OFF if the user hasn't toggled it
  //  themselves — don't silently reset their state mid-exploration)
  if(m.type==='toggle' && !userToggledMoney){ applyMoney(false); }  // start OFF so the user flips it ON
  if(m.type==='node' && m.target){ focusNode(m.target); }
  if(m.type==='anynode'){ setFocus(null); }
  if(m.type==='top10'){ closeDrawer(); }
  if(m.type==='connection'){ closeDrawer(); }
  // coach mark: point at the money switch for mission 2
  const cm = document.getElementById('coach-money');
  if(cm){ cm.style.display = (m.type==='toggle') ? 'block' : 'none'; }
  // announce for screen readers
  const card = document.getElementById('guide-card');
  card.setAttribute('aria-live','polite');
}

function focusNode(id){
  // highlight a node without opening the drawer (for the "find it" missions)
  setFocus(id);
  const n = document.getElementById('n-'+id);
  if(n){ n.style.stroke='#E8C547'; n.style.strokeWidth='4'; }
}

function completeMission(){
  if(missionIdx < 0) return;
  if(missionIdx >= MISSIONS.length-1){
    // finished
    missionDone = true;
    try{ localStorage.setItem('pcn-mission-done','1'); }catch(e){}
    document.getElementById('guide-card').style.display='none';
    document.getElementById('appbar-mission').style.display='none';
    document.getElementById('appbar-thesis').style.display='inline';
    document.getElementById('begin-btn').textContent = 'Replay investigation';
    // Non-happy-path fix: a returning user must ALWAYS be able to reach Top 10.
    document.getElementById('top10-btn').style.display='block';
    document.getElementById('more-btn').style.display='none';
    return;
  }
  showMission(missionIdx+1);
}

function startMissions(){
  if(missionDone){ missionIdx=-1; missionDone=false; }
  showMission(0);
}
document.getElementById('begin-btn').addEventListener('click', startMissions);
document.getElementById('guide-skip').addEventListener('click', ()=>{
  document.getElementById('guide-card').style.display='none';
  document.getElementById('appbar-mission').style.display='none';
  document.getElementById('appbar-thesis').style.display='inline';
  // Non-happy-path fix: a skipper must still reach Top 10.
  document.getElementById('top10-btn').style.display='block';
  document.getElementById('more-btn').style.display='none';
  setFocus(null);
});

// ── Completion detection: listen for the REAL actions ──
// mission 1 (index 0): click Ryan Mello; mission 3 (index 2): click JBLM; mission 4 (index 3): any node
document.querySelectorAll('.node').forEach(n=>{
  n.addEventListener('click', ()=>{
    if(missionIdx===0 && n.dataset.id==='ryan-mello') completeMission();
    else if(missionIdx===2 && n.dataset.id==='jblm') completeMission();
    else if(missionIdx===3) completeMission();  // any node click (read the shapes)
  });
});
// mission 2 (index 1): toggle money — handled in the money-toggle listener above
// mission 5 (index 4): click the loop card
document.getElementById('loop-card').addEventListener('click', ()=>{
  if(missionIdx===4){ completeMission(); return; }
  // Non-happy-path fix: for a free user, clicking the loop card opens the About
  // drawer (which explains the thesis) instead of being a dead-click.
  document.getElementById('about-btn').click();
});
document.getElementById('loop-card').addEventListener('keydown', (e)=>{
  if(e.key==='Enter'||e.key===' '){ e.preventDefault(); if(missionIdx===4) completeMission(); else document.getElementById('about-btn').click(); }
});
// mission 6 (index 5): follow a connection (chip click) — detect via navigateTo when drawer already open
const _origNav = navigateTo;
navigateTo = function(id){
  if(missionIdx===5 && drawerOpen) completeMission();
  _origNav(id);
};
// mission 7 (index 6): top 10
document.getElementById('top10-btn').addEventListener('click', ()=>{
  if(missionIdx===6) completeMission();
});
// More disclosure: reveal the Top 10 button for free-exploration users
// (loop-card and legend-card are ALWAYS visible; only Top 10 is hidden)
document.getElementById('more-btn').addEventListener('click', ()=>{
  document.getElementById('top10-btn').style.display='block';
  document.getElementById('more-btn').style.display='none';
});

// Auto-start on first run (immersive: the page invites the user in)
try{
  if(!localStorage.getItem('pcn-mission-done')){ startMissions(); }
}catch(e){}
</script>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Pierce County Power Network — Interactive</title>
<style>
  html,body {{ margin:0; padding:0; height:100%; background:#fafafa; font-family:sans-serif; }}
  #container {{ position:relative; width:100vw; height:100vh; }}
  .node:focus {{ outline:3px solid #ffd700; outline-offset:2px; }}
  text {{ paint-order: stroke; }}
  /* HTML label overlays: fixed pixel size (NOT scaled with SVG viewBox), so they
     stay readable at any window size. White halo via text-shadow for contrast. */
  .label {{ position:absolute; font-size:22px; font-weight:700; color:#1a1a1a;
            text-shadow:0 0 3px #fff, 0 0 3px #fff, 0 0 3px #fff, 0 0 3px #fff;
            white-space:nowrap; pointer-events:none; z-index:5; }}
  @media (prefers-reduced-motion: reduce) {{
    * {{ transition:none !important; animation:none !important; }}
    .node, .edge {{ transition:none !important; }}
  }}
  /* Full-profile rendering inside the drawer (markdown → html from profiles/*.md) */
  .profile-wrap h2 {{ font-size:14px; color:#1B1B1B; border-bottom:1px solid #E0E0E0;
                       padding-bottom:4px; margin:14px 0 6px; }}
  .profile-wrap h3 {{ font-size:13px; color:#1B1B1B; margin:10px 0 4px; }}
  .profile-wrap p, .profile-wrap li {{ font-size:12.5px; color:#1a1a1a; line-height:1.5; }}
  .profile-wrap ul, .profile-wrap ol {{ margin:4px 0; padding-left:18px; }}
  .profile-wrap table {{ border-collapse:collapse; width:100%; font-size:11.5px; margin:6px 0; }}
  .profile-wrap th, .profile-wrap td {{ border:1px solid #E0E0E0; padding:4px 6px;
                                         text-align:left; vertical-align:top; word-break:break-word; }}
  .profile-wrap th {{ background:#F5F5F5; }}
  .profile-wrap a {{ color:#0B6E6E; }}
  .profile-wrap code {{ background:#F0F0F0; padding:1px 4px; border-radius:3px; font-size:11px; }}
  .profile-wrap blockquote {{ border-left:3px solid #B8860B; margin:6px 0; padding:2px 10px;
                               color:#5D4037; }}
</style>
</head>
<body>
<div id="container">
{appbar}
{rail}
{drawer}
{''.join(svg_parts)}
{label_overlays_html}
<!-- Money legend: names what gold means, bottom-left of canvas, appears when money is ON -->
<div id="money-legend" style="display:none; position:absolute; bottom:16px; left:300px; background:#fff; border:1px solid #E0E0E0; border-radius:8px; padding:8px 12px; font-family:sans-serif; font-size:12px; color:#1B1B1B; z-index:8; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
  <span style="display:inline-block; width:14px; height:14px; border:2px dashed #B8860B; border-radius:50%; margin-right:6px; vertical-align:middle;"></span>
  <span style="display:inline-block; width:22px; height:2px; background:#B8860B; margin-right:6px; vertical-align:middle;"></span>
  <b>Gold = public money</b> (government-created wealth)
</div>
<!-- Coach mark: points at the money switch during mission 2 -->
<div id="coach-money" style="display:none; position:absolute; top:64px; right:180px; background:#1B1B1B; color:#FAFAFA; border:2px solid #E8C547; border-radius:8px; padding:8px 12px; font-family:sans-serif; font-size:13px; font-weight:bold; z-index:20; box-shadow:0 4px 16px rgba(0,0,0,0.3);">
  Click the gold switch above ↑
</div>
</div>
{js.replace('__NODE_DATA__', node_data_js).replace('__NODE_COUNT__', str(len(all_nodes))).replace('__EDGE_COUNT__', str(len(all_edges)))}
</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    f.write(html)
print(f"Wrote {os.path.getsize(OUT)/1024:.1f} KB to {OUT}")
print(f"Canvas: {W}x{H}, k=0.9 | {len(label_placements)} labels | remaining overlaps: {overlap_count}")
