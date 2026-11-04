import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

/**
 * Content schemas. Known fields are typed; `.catchall(z.unknown())` lets any
 * unknown field through validation so the theme's fallback renderers display
 * it — new data fields need zero component code changes.
 *
 * Edge `from`/`to` are validated against existing entities at build time by
 * the theme's graph compiler (dangling references fail the build).
 */
const entities = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: './src/content/entities' }),
  schema: z
    .object({
      name: z.string(),
      type: z.string().default('entity'),
      summary: z.string().optional(),
    })
    .catchall(z.unknown()),
});

const edges = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: './src/content/edges' }),
  schema: z
    .object({
      from: z.string(),
      to: z.string(),
      kind: z.string(),
      evidence: z.array(z.string()).default([]),
      confidence: z.enum(['high', 'medium', 'low']).default('medium'),
    })
    .catchall(z.unknown()),
});

const pages = defineCollection({
  // Migrated pages carry legacy `slug` frontmatter (case-level metadata,
  // identical across all pages of one case). Astro's default entry id would
  // take that slug and collapse every page of a case onto one route — so ids
  // are forced to the file path instead (id = filename stem, e.g.
  // `2608-lakewood-council-update`). Kept through the 0.5.0 recopy (issue
  // tracking: moliver28/sitefactory#50 — the template default clobbers this).
  loader: glob({
    pattern: '**/*.md',
    base: './src/content/pages',
    generateId: ({ entry }) => entry.replace(/\.[^.]+$/, ''),
  }),
  // .catchall keeps migrated legacy case-metadata frontmatter (case_id, slug,
  // status, tags, ...) instead of stripping it at validation time.
  schema: z
    .object({
      title: z.string(),
      description: z.string().optional(),
      order: z.number().default(10),
    })
    .catchall(z.unknown()),
});

// Fast path for brand-new entity kinds: loose schema, generic renderers.
const customEntities = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: './src/content/custom-entities' }),
  schema: z
    .object({
      name: z.string(),
      kind: z.string().default('custom'),
      summary: z.string().optional(),
    })
    .catchall(z.unknown()),
});

export const collections = { entities, edges, pages, customEntities };
