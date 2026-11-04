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
  loader: glob({
    pattern: '**/*.md',
    base: './src/content/pages',
    // Issue #50: the glob loader's default id slugs from frontmatter `slug`
    // when present, so migrated pages of one case that carry a case-level
    // `slug:` collapse into ONE route (7 files → 2 routes, silent loss).
    // Derive the id from the filename stem instead — one route per file,
    // matching how entities/edges/custom-entities ids work.
    generateId: ({ entry }) => entry.replace(/\.[^.]+$/, ''),
  }),
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
