/**
 * Lighthouse CI gate for generated sites (issue #4 / P7.2 S2).
 *
 * Category budgets live in `site.config.yaml` under
 * `performance.lighthouse.categories` (defaults below) — raising a budget in
 * site config tightens CI with no script change. Unknown keys and
 * out-of-range values fail loudly: a budget that silently doesn't bind is
 * worse than a failed run.
 *
 * `yaml` is re-used from Astro's dependency tree — the same zero-new-deps
 * pattern as `vendor/theme/config/preset.js`. Shipped as .cjs because
 * `astro check` skips CommonJS files.
 *
 * Serving contract (see the CI "Stage dist" step): emitted sites build at
 * base `/<repo>/`, so LHCI's built-in static server must serve the PARENT of
 * the site directory. CI stages `dist` at `serve/<repo>/`; this config
 * audits an explicit stratified URL sample (see `sample` below) so absolute
 * assets resolve and the audit stays bounded.
 */
const { existsSync, readFileSync } = require('node:fs');
const path = require('node:path');
const { parse: parseYaml } = require('yaml');

const DEFAULT_BUDGETS = {
  performance: 0.9,
  accessibility: 0.95,
  'best-practices': 0.9,
  seo: 0.9,
};

const VALID_CATEGORIES = Object.keys(DEFAULT_BUDGETS);

function loadSiteConfig(siteRoot) {
  const file = path.join(siteRoot, 'site.config.yaml');
  if (!existsSync(file)) return {};
  return parseYaml(readFileSync(file, 'utf8')) ?? {};
}

/** Budgets from site.config.yaml layered over defaults, shape-validated. */
function readBudgets(siteRoot) {
  const budgets = { ...DEFAULT_BUDGETS };
  const configured = loadSiteConfig(siteRoot)?.performance?.lighthouse?.categories;
  if (configured === undefined) return budgets;
  if (configured === null || typeof configured !== 'object' || Array.isArray(configured)) {
    throw new Error(
      'site.config.yaml: performance.lighthouse.categories must be a map of category -> number',
    );
  }
  for (const [category, value] of Object.entries(configured)) {
    if (!VALID_CATEGORIES.includes(category)) {
      throw new Error(
        `site.config.yaml: unknown Lighthouse category "${category}" (valid: ${VALID_CATEGORIES.join(', ')})`,
      );
    }
    const score = Number(value);
    if (!Number.isFinite(score) || score <= 0 || score > 1) {
      throw new Error(
        `site.config.yaml: Lighthouse budget for "${category}" must be a number in (0, 1], got ${JSON.stringify(value)}`,
      );
    }
    budgets[category] = score;
  }
  return budgets;
}

const siteRoot = path.resolve(__dirname, '..');
const budgets = readBudgets(siteRoot);

/** Only the categories with budgets are asserted; every other audit is off. */
const assertions = {};
for (const [category, minScore] of Object.entries(budgets)) {
  assertions[`categories:${category}`] = ['error', { minScore }];
}

// deploy.base mirrors astro.config's base ("/<repo>/"); "/" covers rooted
// sites.
const base = String(loadSiteConfig(siteRoot)?.deploy?.base ?? '/');

// Stratified sample, not autodiscovery-everything: at 173 built pages the
// full sweep is 519 Lighthouse runs (~80 min on ubuntu runners) and blew
// the 45-min quality timeout (sitefactory#52 — template fix pending).
// Budgets are per-URL category minimums, so a representative sample binds
// them: home (index + island), the graph island (the only route near the
// 0.70 floor — sigma.js force layout, sitefactory#39), entity routes with
// each renderer shape, a case page with Shiki code blocks (the
// sitefactory#51 contrast class), a legacy card, and the interactive
// evidence app.
const sample = [
  '',
  'graph/',
  'entities/boeing/',
  'entities/adam-smith/',
  'entities/bryan-yambe/',
  'pages/2608-lakewood-council-about/',
  'pages/2608-pierce-leadership/',
  'assets/network/2608-pierce-leadership/',
  'cards/2608-lakewood-council.html',
];
const urls = sample.map((p) => new URL(path.posix.join(base, p), 'http://localhost').href);

module.exports = {
  ci: {
    collect: {
      staticDistDir: path.join(siteRoot, 'serve'),
      url: urls,
    },
    assert: {
      assertions,
    },
  },
};
