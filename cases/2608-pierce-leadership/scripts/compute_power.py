#!/usr/bin/env python3
"""Composite power scoring shared by the HTML build and the profile generator.

Single source of truth for the academically grounded composite
(evidence/26-power-methodology.md): 35% weighted degree + 25% betweenness
+ 20% eigenvector + 20% PageRank, plus the veto/structural bonus and the
hub/party caps added after the skeptic ranking audit (skeptic-ranking.md).
No scipy — PageRank via numpy power iteration.

Usage: python3 compute_power.py --selftest
"""
import json, os, sys
import networkx as nx
import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DEFAULT_GRAPH = os.path.join(REPO, "evidence", "29-power-graph-v2.json")

VETO_BONUS = {
    "ryan-mello":     0.30,   # County Executive, veto + $3.5B budget (evidence/12 #1)
    "puyallup-tribe": 0.30,   # sovereignty/veto (evidence/12 ranks #3)
    "jblm":           0.28,   # federal veto, largest employer (#5)
    "chamber":        0.20,   # agenda/narrative power (CRITICAL in /13)
    "keith-swank":    0.16,   # legal autonomy (#7)
    "mary-robnett":   0.14,   # prosecutorial discretion (#8)
    "multicare":      0.10,   # largest private employer (#4)
    "anders-ibsen":   0.10,   # Tacoma Mayor, county's largest city (#16)
    "nathe-lawver":   0.10,   # labor-civic interlock (evidence/27)
    "john-wiborg":    0.08,   # interlock economy (#11)
    "dona-ponepinto": 0.08,   # 7+ board interlock (evidence/27)
    "tom-pierson":    0.10,   # revolving door (Chamber CEO + County Econ Dev)
    "john-mccarthy":  0.06,   # (#12)
    "news-tribune":   0.05,   # narrative control (#15)
    "ltg-mcfarlane":  0.05,   # (#22)
    "bill-sterud":    0.05,   # (#23)
}

def build_graph(data):
    G = nx.Graph()
    for n in data["nodes"]:
        G.add_node(n["id"], label=n["label"], type=n["type"], domain=n["domain"])
    for e in data["edges"]:
        if e["source"] in G and e["target"] in G:
            G.add_edge(e["source"], e["target"],
                       relationship=e.get("relationship", ""), weight=e.get("weight", 1))
    return G

def compute_power(G):
    wdeg = dict(G.degree(weight="weight"))
    btw = nx.betweenness_centrality(G, weight="weight")
    eig = nx.eigenvector_centrality(G, max_iter=1000, weight="weight")
    nodes = list(G.nodes()); idx = {n: i for i, n in enumerate(nodes)}; N = len(nodes)
    A = np.zeros((N, N))
    for u, v, d in G.edges(data=True):
        w = d.get("weight", 1); A[idx[u], idx[v]] = w; A[idx[v], idx[u]] = w
    d = A.sum(axis=1); d[d == 0] = 1; M = A / d[:, None]; beta = 0.85
    pr = np.ones(N) / N
    for _ in range(200):
        pr_new = (1 - beta) / N + beta * M.T @ pr
        if np.abs(pr_new - pr).sum() < 1e-9:
            break
        pr = pr_new
    pagerank = {nodes[i]: pr[i] for i in range(N)}

    def normalize(dd):
        vals = list(dd.values()); mn, mx = min(vals), max(vals)
        if mx == mn:
            return {k: 0.5 for k in dd}
        return {k: (v - mn) / (mx - mn) for k, v in dd.items()}

    n_wdeg, n_btw, n_eig, n_pr = normalize(wdeg), normalize(btw), normalize(eig), normalize(pagerank)
    composite = {n: 0.35*n_wdeg[n] + 0.25*n_btw[n] + 0.20*n_eig[n] + 0.20*n_pr[n] for n in G.nodes()}
    for nid, bonus in VETO_BONUS.items():
        if nid in composite:
            composite[nid] = min(1.0, composite[nid] + bonus)
    # Kelly Chambers: holds no office (left WA House Jan 2025, lost 2024 Exec race) — cap below top-25.
    if "kelly-chambers" in composite:
        composite["kelly-chambers"] = min(composite["kelly-chambers"], 0.06)
    # Council hub discount: cap below the Executive so ranking follows evidence/12.
    if "county-council" in composite and "ryan-mello" in composite:
        composite["county-council"] = min(composite["county-council"], composite["ryan-mello"] - 0.02)
    # Chamber hub discount: the Chamber aggregates 27+ 'member'/'trains_candidates'
    # edges and over-ranks on raw centrality (same hub artifact as a party node —
    # skeptic-ranking.md). evidence/12 ranks Mello #1, Chamber #2 — cap Chamber just
    # below Mello but ABOVE Council (Mello-0.01 vs Council at Mello-0.02).
    if "chamber" in composite and "ryan-mello" in composite:
        composite["chamber"] = min(composite["chamber"], composite["ryan-mello"] - 0.01)
    # Party-node artifact: caps well below elected officials.
    for nid in ["pierce-dem", "pierce-gop"]:
        if nid in composite:
            composite[nid] = min(composite[nid], 0.12)
    return composite

def load_default_graph():
    with open(DEFAULT_GRAPH) as f:
        return json.load(f)

def selftest():
    data = load_default_graph()
    G = build_graph(data)
    power = compute_power(G)
    ranked = sorted(G.nodes(), key=lambda n: -power[n])
    top5 = [G.nodes[n]["label"] for n in ranked[:5]]
    print("top5:", top5)
    assert top5 == ["Ryan Mello", "Chamber of Commerce", "Pierce County Council",
                    "Puyallup Tribe", "JBLM"], f"ranking drift: {top5}"
    assert all(power[n] > 0 for n in G.nodes()), "zero-power node found"
    print("selftest PASS")

if __name__ == "__main__":
    selftest()