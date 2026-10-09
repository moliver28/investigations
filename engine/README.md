# Hermes Investigation Pipeline

Staged, schema-first, config-driven processing for investigative journalism. Built to
make the **publish step deterministic**: investigations write to a flexible-but-typed
schema, and the HTML web page is a **pure function** of that data — no hard-coded node
ids, counts, colors, acronyms, or copy in the builder.

## The problem this solves

The prior publish step (`build_power_network.py`) was a ~1,000-line monolith that
hard-coded ~60 node ids (`money_nodes`), ~40 relationship types, 50 acronyms, 6 domain
colors/shapes, 17 veto bonuses, and all mission/about/thesis text as Python literals —
while the real graph held **163 nodes, 342 edges, and 109 distinct relationship types**.
The sync whitelist only knew ~45 of those types, so **59 relationships silently
rendered as "structural"** and orphan references (`life-center`) silently did nothing.
Any data change caused silent drift or breakage.

## Architecture

```
investigations/<slug>/
  ├── site.json                    ← SINGLE SOURCE OF TRUTH (case config, validated)
  ├── evidence/<graph>.json        ← nodes + edges (schema-validated)
  ├── profiles/<id>.md             ← researched prose (readability-gated)
  └── evidence/<output>.html       ← rendered page (pure function of the above)
```

The engine is generic (`pipeline/`); each case brings its own `site.json`.

### Stages (`python3 -m pipeline.run site.json`)

| Stage | Module | Contract |
|-------|--------|----------|
| **1. validate** | `pipeline/validate.py` | Schema + cross-reference validation. Exits non-zero on any ERROR. |
| **2. build** | `pipeline/build_site.py` | Pure render: graph + profiles + config → HTML. Zero hard-coded case data. |
| **3. verify** | `pipeline/verify.py` | Post-build gates: readability, zero-power, count/top drift. |

Each stage reads JSON and writes a fresh artifact — no stage mutates another's input,
so the publish step is reproducible and idempotent.

### The schema (`schema/`)

- `graph.schema.json` — nodes (id/label/type/domain, flexible extras) + edges
  (source/target/relationship/weight). Load-bearing fields are **strict**; everything
  else is `additionalProperties: true` so the schema is flexible *and* safe.
- `site.schema.json` — every presentation decision: domain colors/shapes/labels, the
  relationship taxonomy, section titles, acronyms, power bonuses/caps, mission text.

### The relationship taxonomy (4 explicit classes, no silent fallthrough)

Every relationship type must be in exactly **one** of:

- `money` — government-created wealth / campaign finance (donated, federal_funding, …)
- `influence` — money→influence verbs (lobbying, endorses, appoints, …)
- `interlock` — person↔org board/office seats (board, ceo, member, …)
- `structural` — everything else (colleague, partnership, contract, …)

The validator **errors** on any relationship in *none* of these classes, and warns on
ambiguous multi-class membership (except the intentional money+influence dual-class for
campaign-finance verbs). This is the core anti-drift guarantee: you can never silently
misclassify a new relationship type again.

## Error taxonomy (`pipeline/errors.py`)

Structured, JSON-Lines errors with a machine-actionable grammar:

```json
{"code": "GRAPH.ORPHAN", "severity": "ERROR", "message": "edge target 'ghost-node' not in nodes",
 "path": "/edges/342/target", "fix": "Add the node or fix the reference.", "data": {"ref": "ghost-node"}}
```

`<DOMAIN>.<KIND>` codes (GRAPH.*, REL.*, SITE.*, COUNT.*, TOP.*, READABILITY, ZERO_POWER),
severity ladder FATAL > ERROR > WARN > INFO, a JSON-pointer path, and a `fix` hint. A
repair agent (or future `--fix` pass) can pattern-match these and auto-correct, instead
of a human reading a traceback.

## Usage

```bash
# one command: validate → build → verify
/Users/moliver/.hermes/hermes-agent/venv/bin/python3 -m pipeline.run \
    ~/Documents/Investigations/<slug>/site.json

# strict mode: also fail on WARN
python3 -m pipeline.run site.json --strict

# individual stages
python3 -m pipeline.validate <graph.json> <site.json>
python3 -m pipeline.build_site <graph.json> <site.json> <out.html>
python3 -m pipeline.verify <graph.json> <site.json> <out.html> --max-grade 10
```

## Placeholders (computed at build time, never hard-coded)

Node/edge counts and ranking names are substituted from data, so they can never drift
out of sync with the graph:

- `{node_count}`, `{edge_count}` — in `about_body` and mission `body`
- `{top_actor}`, `{top_three}` — in mission `fact`

## Why the page "updates with little to no breakage"

1. **Schema-validated data** — a bad field fails at validate, before any render.
2. **Config-driven render** — add a domain/color/acronym/relationship by editing
   `site.json`, not Python. No code change = no breakage surface.
3. **Computed counts/names** — "163 nodes / 342 edges / Ryan Mello #1" is computed,
   so the About text and missions can't go stale.
4. **Post-build verify** — re-checks the output against the data (count drift, top
   drift, readability, zero-power) and blocks publish on failure.
5. **Loud, structured errors** — the validator reports *exactly* what's wrong and how
   to fix it, in machine-actionable form, so fixes can be automated.

## Porting notes

`pipeline/power.py` is a config-driven port of the case's `compute_power.py` — the
35/25/20/20 weighting is unchanged; only the veto bonuses and hub caps moved from
Python literals into `site.json` → `power`.


## Publishing to GitHub — the investigations monorepo

The engine lives here; cases live in sibling case repos. Everything pushes to
the public monorepo **github.com/moliver28/investigations**, laid out as:

```
investigations/            (public repo)
├── engine/                ← this repo: pipeline/, schema/, scripts/, config/
├── cases/<slug>/          ← mirror of each case worktree (evidence included)
├── site/                  ← generated: index.html, cards/, style.css, registry.json,
│                            assets/network/<slug>/ (approved bundles), artifact-manifest.json
└── .github/workflows/ci.yml
```

Live site: **https://moliver28.github.io/investigations/** — deployed ONLY by CI
(actions/deploy-pages) AFTER every gate passes. A red build can never publish.

### The one command

```bash
# full round: sync → engine gates (--strict) → case bundle gates → hub build →
# README regen → dep pins → fingerprints → secret scan → commit → push
PUBLISH_DRY_RUN=1 scripts/publish.py run     # rehearse: everything except push
scripts/publish.py run                       # real round
publish.py selftest                          # CI parity check, local
```

This runs automatically at every session end via the `on_session_end` shell hook
(`~/.hermes/agent-hooks/publish-round.sh` → profile config `hooks.on_session_end`),
so **pushing changes = publishing changes**, with zero manual steps.

### Enforcement (MECE, three layers)

1. **Publish-time derivation** — `case2hub.py` regenerates cards, index, registry,
   and README from case frontmatter in one pass; stale cards are deleted, so the
   four artifacts can never disagree by construction.
2. **Approval gate** — a case is public only with `publish:\n  approved: true`
   frontmatter. Unapproved cases are mirrored (source public) but never rendered.
3. **CI re-verification** — on every push: installs EXACT dep pins
   (`engine/requirements-ci.txt`), rebuilds every `cases/*/site.json` from the
   checked-in engine (`--strict`), re-derives the hub (`case2hub selftest`),
   checks README↔index↔cards↔registry MECE parity, compares SHA256 fingerprints
   (engine tree, dep pins, graphs) against `site/artifact-manifest.json`, secret-scans
   the tree, verifies unapproved cases render nothing — then deploys.

The engine build is byte-deterministic (verified: identical SHA256 across runs on
macOS AND the CI ubuntu rebuild) — so fingerprint equality is a real guarantee,
not an aspiration. Changing deps or engine code without a fresh publish round
fails CI loudly.

### Adding a new case (zero registration)

Create the case per the case-manager skill (bare repo + worktree + `<slug>/<slug>.md`,
symlink into the profile cases dir, Notion page). The next publish round
discovers it automatically. For a rendered/network case, add a case-root
`site.json` and CI will build and fingerprint it too. To publish it publicly,
flip the frontmatter flag — the next round applies it and CI enforces the rest.
