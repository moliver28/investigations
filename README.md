# Investigations

Published investigations — source documents, entity profiles, and the
connections between them. Built with
[sitefactory](https://github.com/moliver28/sitefactory) (journalism template
v0.1.0, @sitefactory/theme 0.1.1). Migrated from the legacy publishing
pipeline on 2026-11-02; the original case files remain in git history.

- Live: https://moliver28.github.io/investigations/
- PR previews: `https://moliver28.github.io/investigations/pr-preview/pr-<n>/`

## Routes

| Route | What it is |
| --- | --- |
| `/investigations/` | Index: case pages + entity list |
| `/investigations/pages/<slug>/` | Case pages (2 cases, 7 pages) |
| `/investigations/entities/<id>/` | 163 entity profiles |
| `/investigations/graph/` | Interactive entity graph (163 nodes, 342 edges) |
| `/investigations/graph.json` | Graph document compiled at build time |
| `/investigations/evidence/<case>/…` | Source documents, served as-is |
| `/investigations/evidence/2608-pierce-leadership/network/` | Archived interactive network app |
| `/investigations/admin/` | Sveltia CMS (staff-only) |

Legacy URLs still resolve via meta-refresh stubs: `/investigations/cards/<slug>.html`
→ `/investigations/pages/<slug>/`, and
`/investigations/assets/network/2608-pierce-leadership/index.html` →
`/investigations/evidence/2608-pierce-leadership/network/index.html`.

## Cases

| Case | ID | Page |
| --- | --- | --- |
| 2026-08-16: Lakewood City Council Investigation | INV-2026-001 | [/investigations/pages/2608-lakewood-council/](https://moliver28.github.io/investigations/pages/2608-lakewood-council/) |
| 2026-08-17: Pierce County Leadership Investigation | INV-2026-002 | [/investigations/pages/2608-pierce-leadership/](https://moliver28.github.io/investigations/pages/2608-pierce-leadership/) |

## Structure

| Path | What it is |
| --- | --- |
| `src/content/entities/` | Entity YAML (163: people and organizations) |
| `src/content/edges/` | Typed, evidence-cited relations between entities (342) |
| `src/content/pages/` | Narrative pages (markdown, 7) |
| `src/content/custom-entities/` | Fast path for brand-new entity kinds |
| `static/evidence/` | Source documents, referenced by content (`MANIFEST.sha256` records migration integrity) |
| `static/cards/`, `static/assets/` | Legacy-URL meta-refresh stubs |
| `static/admin/` | Sveltia CMS (`/admin/`) |
| `vendor/theme/` | Vendored `@sitefactory/theme` (pinned via `site.config.yaml`) |
| `site.config.yaml` | Machine-readable site identity for factory tooling |
| `AGENTS.md` | Editorial + agent rules (read before writing content) |

Working files kept unserved: `cases/2608-pierce-leadership/{scripts/, .hermes/,
AGENTS.md, IDEA.md, templates/}` — build tooling and internal docs, not part
of the site.

## Commands

```sh
npm install
npm run dev        # local dev server
npm run build      # validates content (Zod) and builds
npm run typecheck  # astro check
```

## Updating the theme

The theme is vendored (`file:./vendor/theme`) and pinned in `site.config.yaml`.
Theme updates ship as a new `@sitefactory/theme` version; update `vendor/theme`
to that version and let CI rebuild. See sitefactory's `AGENTS.md` for the
update procedure.
