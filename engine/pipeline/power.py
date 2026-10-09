"""Config-driven composite power scoring (single source of truth, no hard-coded ids).

Ported from the case's `compute_power.py` but with every node id, bonus, and cap
moved into the site config (config/site.json → `power`). Weighting is fixed by the
methodology (evidence/26-power-methodology.md): 35% weighted degree + 25%
betweenness + 20% eigenvector + 20% PageRank, then veto bonuses and hub/party caps.

No scipy — PageRank via numpy power iteration. Deterministic (fixed seed, no RNG).
"""
from __future__ import annotations

import numpy as np
import networkx as nx


WEIGHTS = {"wdeg": 0.35, "btw": 0.25, "eig": 0.20, "pr": 0.20}


def build_graph(data: dict) -> nx.Graph:
    G = nx.Graph()
    for n in data["nodes"]:
        G.add_node(n["id"], label=n.get("label", n["id"]),
                   type=n.get("type", "organization"), domain=n.get("domain", "institutional"))
    for e in data["edges"]:
        if e["source"] in G and e["target"] in G:
            G.add_edge(e["source"], e["target"],
                       relationship=e.get("relationship", ""),
                       weight=e.get("weight", 1))
    return G


def _normalize(dd: dict) -> dict:
    vals = list(dd.values())
    mn, mx = min(vals), max(vals)
    if mx == mn:
        return {k: 0.5 for k in dd}
    return {k: (v - mn) / (mx - mn) for k, v in dd.items()}


def compute_power(G: nx.Graph, power_config: dict | None = None) -> dict:
    """Composite power per node. `power_config` = site config `power` object."""
    power_config = power_config or {}
    wdeg = dict(G.degree(weight="weight"))
    btw = nx.betweenness_centrality(G, weight="weight")
    eig = nx.eigenvector_centrality(G, max_iter=1000, weight="weight")

    nodes = list(G.nodes())
    idx = {n: i for i, n in enumerate(nodes)}
    N = len(nodes)
    A = np.zeros((N, N))
    for u, v, d in G.edges(data=True):
        w = d.get("weight", 1)
        A[idx[u], idx[v]] = w
        A[idx[v], idx[u]] = w
    d = A.sum(axis=1)
    d[d == 0] = 1
    M = A / d[:, None]
    beta = 0.85
    pr = np.ones(N) / N
    for _ in range(200):
        pr_new = (1 - beta) / N + beta * M.T @ pr
        if np.abs(pr_new - pr).sum() < 1e-9:
            break
        pr = pr_new
    pagerank = {nodes[i]: pr[i] for i in range(N)}

    n_wdeg, n_btw, n_eig, n_pr = _normalize(wdeg), _normalize(btw), _normalize(eig), _normalize(pagerank)
    composite = {
        n: WEIGHTS["wdeg"] * n_wdeg[n] + WEIGHTS["btw"] * n_btw[n]
           + WEIGHTS["eig"] * n_eig[n] + WEIGHTS["pr"] * n_pr[n]
        for n in G.nodes()
    }

    # Veto / structural bonus (config-driven; add, capped at 1.0).
    for nid, bonus in (power_config.get("veto_bonus") or {}).items():
        if nid in composite:
            composite[nid] = min(1.0, composite[nid] + float(bonus))

    # Hub / party caps (config-driven). `cap` = absolute ceiling; `below`+`delta`
    # = cap at (score of `below` minus delta).
    for spec in (power_config.get("hub_caps") or []):
        nid = spec.get("id")
        if not nid or nid not in composite:
            continue
        if "cap" in spec and spec["cap"] is not None:
            composite[nid] = min(composite[nid], float(spec["cap"]))
        elif "below" in spec:
            below = spec["below"]
            if below in composite:
                delta = float(spec.get("delta", 0.01))
                composite[nid] = min(composite[nid], composite[below] - delta)

    return composite


def ranked_nodes(G: nx.Graph, power: dict) -> list[str]:
    return sorted(G.nodes(), key=lambda n: -power[n])
