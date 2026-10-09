"""Hermes Investigation Pipeline.

Staged, schema-first, config-driven processing for investigative journalism.

Stages (each is a distinct, cacheable, idempotent step with a clean contract):

  1. validate   — schema + cross-reference validation of graph data & site config.
                  Emits structured errors (errors.py) and exits non-zero on ERROR+.
  2. sync       — normalize profile edge submissions into the graph (dedupe, alias,
                  direction-correction, backfill).  (portable from case scripts)
  3. score      — recompute composite power from the graph (single source of truth).
  4. prose      — deterministic readability transforms on profiles (mechanical pass).
  5. build      — render HTML from (graph + profiles + site config). Pure function.
  6. verify     — post-build checks: readability gate, zero-power nodes, count drift,
                  orphan config refs.

All data flows through JSON / JSON-Lines. No stage mutates another stage's input;
each writes a fresh artifact under `build/` so the publish step is reproducible.
"""
__all__ = ["errors", "validate", "build_site"]
