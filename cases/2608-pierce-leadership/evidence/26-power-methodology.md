# Power Measurement Methodology — Composite Power Score

**Case:** INV-2026-002 · **File:** evidence/26-power-methodology.md
**Summary:** How the composite power score is computed, with academic grounding
**Key actors:** All 112 nodes in the power network
**Pull when:** Any question about how node size / power scores were calculated, or to defend the method

---

## Purpose

The interactive power network (`11-power-network.html`) sizes every node by a **composite power score** so that visual size corresponds to measured influence — not subjective judgment. This document records the method, the academic grounding, and the exact formula so the measurement is **reproducible and defensible**.

## Intellectual Foundation

The method sits at the intersection of two research traditions:

1. **Community power structure research** — the study of who actually governs a locality. Foundational works:
   - **Floyd Hunter (1953), *Community Power Structure: A Study of Decision Makers*** — the first systematic study of local power, using a "reputational approach" (asking knowledgeable observers who holds power). Established that power in a community is a *network* of people and institutions, not a list of officeholders.
   - **G. William Domhoff, *Who Rules America?*** — extended Hunter's network approach, emphasizing interlocking directorships and the corporate/social upper class as the power core.
   - **C. Wright Mills (1956), *The Power Elite*** — the national-level counterpart, mapping the interlock of corporate, military, and political elites.

2. **Social network analysis (SNA)** — the quantitative toolkit for measuring centrality/power in a network:
   - **Wasserman & Faust (1994), *Social Network Analysis: Methods and Applications* (Cambridge UP)** — the standard textbook; Chapter 5 covers centrality, prestige, and prominence.
   - **Freeman (1979), "Centrality in social networks: Conceptual clarification," *Social Networks* 1:215-239** — defined degree, betweenness, and closeness centrality.
   - **Bonacich (1987), "Power and Centrality: A Family of Measures," *American Journal of Sociology* 92:1170-1182** — eigenvector centrality as a measure of power (connections to well-connected others).
   - **Brin & Page (1998)** — PageRank, the influence-flow algorithm underlying Google Search.

## The Composite Power Score

Each node's power is the weighted blend of four network metrics, each **normalized to 0-1** (min-max scaling):

| Metric | Weight | What it measures | Source |
|--------|--------|------------------|--------|
| **Weighted degree** | 35% | Direct influence — sum of edge weights (donations, board seats, employment, partnerships) | Freeman (1979) |
| **Betweenness centrality** | 25% | Bridging power — how often a node lies on the shortest path between other nodes (connects groups) | Freeman (1979) |
| **Eigenvector centrality** | 20% | Power of connections — being connected to well-connected others | Bonacich (1987) |
| **PageRank** | 20% | Influence flow — how influence propagates through the network | Brin & Page (1998) |

**Formula:**
```
composite = 0.35 * wdeg_norm + 0.25 * btw_norm + 0.20 * eig_norm + 0.20 * pagerank_norm
```

**Rationale for the blend:** No single centrality measure captures all facets of power. Degree captures direct reach; betweenness captures the ability to bridge otherwise-disconnected groups (a key form of structural power); eigenvector captures the quality of connections; PageRank captures influence flow. Combining them into a composite is supported by the composite-centrality literature (e.g., arXiv:2111.04529, "A Composite Centrality Measure for Improved Identification of Influential Nodes"). The weights (35/25/20/20) reflect that direct influence and bridging are the two most consequential forms of structural power in a local governance network.

## Implementation Notes

- **Weighted degree** = sum of edge weights incident to the node (from `networkx.degree(weight='weight')`).
- **Betweenness** = `networkx.betweenness_centrality(G, weight='weight')`.
- **Eigenvector** = `networkx.eigenvector_centrality(G, max_iter=1000, weight='weight')`.
- **PageRank** = computed via a **numpy power-iteration** (since scipy is not always available in the sandbox): build the weighted adjacency matrix, column-stochastic normalize, iterate `pr = (1-β)/N + β·Mᵀ·pr` with β=0.85 until convergence.
- **Normalization** = min-max scaling to 0-1 per metric.
- **Node radius** = `8 + (composite/max_composite)*22`, multiplied by 1.2 for organizations (so orgs read slightly larger than individuals at equal power).

## Label Display Rule

Labels are shown for all nodes with `composite >= 0.04` (a threshold that typically covers the top ~40-50% of actors by power). This ensures every significant actor is identifiable at a glance, not just the top 5-10.

## Reproducibility

- The graph is built from the evidence files in this investigation (campaign finance, lobbying, board memberships, employment, partnerships).
- Edge weights encode the strength of each relationship (e.g., a $175,500 party contribution weighs more than a $2,400 donation).
- The full node/edge dataset and composite scores are reproducible from the evidence files and the `networkx`/`numpy` computation described above.

## Limitations

- The composite score measures **structural/network power** — it reflects position in the mapped network, not necessarily real-world impact, charisma, or informal influence that isn't captured as an edge.
- Edge weights are analyst-assigned based on documented relationships; they are defensible but not objective measurements.
- The network is a snapshot (2026); power shifts as people and relationships change.
- This is a **measurement aid**, not a verdict — it should be combined with the qualitative analysis in `12-power-matrix.md`.
