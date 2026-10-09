# Progressive-Disclosure Entity Panel — Design Spec

**Target:** `evidence/11-power-network.html` drawer (`#drawer`, 340px). Goal: clicking a node feels calm — one focal point, not 8 stacked sections — and relationships are *seen* (color + icon + arrow), not read.

## 1. Above-the-fold layout (always visible on open)

Three blocks, in order, nothing else:

1. **Header** — unchanged: glyph + name (domain color), `type · domain · Power badge`.
2. **Thesis strip** — unchanged single-line card (domain-driven thesis string).
3. **ONE focal element** — chosen by a priority switch, first match wins:

| Entity profile | Focal element |
|---|---|
| Receives public money (`MONEY_RELS` edge, dir `in`) | **Money-source callout** (gold box) |
| Board-interlock person (≥2 `INTERLOCK_RELS` edges) | **"Multiple hats" strip** — the 2–3 boards/roles as interlock chips |
| Government actor (no money-in) | **"Who influences them"** — top 3 influence chips (dir `in`) |
| Everything else | **"Where its power leads"** — top 3 outbound influence chips |

The focal element is the *only* content below the thesis strip. Everything else is hidden.

## 2. Disclosure mechanism — staged accordion

A single **"More"** button (full-width, `border:1px solid #E0E0E0`, 8px radius) sits directly under the focal element. Clicking it reveals **three collapsible `<details>` sections**, in this order:

1. **About** — description + key-facts bullet list.
2. **Connections** — the full thesis-grouped relationship list (see §4).
3. **Follow the thread** — the nudge line.

`<details>`/`<summary>` gives native keyboard + ARIA disclosure semantics for free. The "More" button toggles to "Less" and collapses all three when clicked again. **One section open at a time** (close siblings on open) — keeps the drawer calm even when expanded.

## 3. Relationship visual system — the core change

Every relationship renders as a **chip with three redundant cues: color + icon + direction arrow.** Redundancy is the UDL move: color-blind users read the icon, low-vision users read the color, everyone reads the arrow.

**Exact mapping (color / icon / arrow):**

| Relationship class | Color | Icon | Direction |
|---|---|---|---|
| **Money flows** (`MONEY_RELS`) | Gold `#B8860B` | `$` | `→` (out) / `←` (in) |
| **Influence** (`INFLUENCE_RELS`) | **Target's domain color** | `→` | `→` (out) / `←` (in) |
| **Board interlock** (`INTERLOCK_RELS`) | `#1B1B1B` on `#FAFAFA` | `⬡` | `↔` (bidirectional, no arrow) |
| **Structural/other** (veto, oversight, owns) | `#666` | `⚙` | `→` / `←` |

**Direction rule:** the arrow always points *from the source of power to the receiver*. `dir:"out"` = this entity is the source → arrow points away (`→`); `dir:"in"` = this entity receives → arrow points in (`←`). Money and influence are directional; interlocks are always `↔` (a seat is mutual).

**Chip anatomy:** `[icon] [label] [arrow]` — e.g. `$ MultiCare →`, `→ County Council ←`, `⬡ Port of Tacoma ↔`. The icon and arrow are the *first* and *last* glyphs so the eye lands on them; the label sits between.

## 4. Connection chip redesign

Three visually distinct chip styles (all `border-radius:4px`, `padding:2px 6px`, `font-size:12px`, clickable → `navigateTo`):

- **Money chip:** `background:#FFF8E1; border:1px solid #B8860B; color:#B8860B;` — gold-tinted fill, gold border, `$` prefix, `→`/`←` suffix.
- **Influence chip:** `background:<domainColor>1A; border:1px solid <domainColor>; color:<domainColor>;` — the *target's* domain color at ~10% fill, `→`/`←` suffix. (Domain color = the color of the entity being influenced, so the eye maps influence to the domain it reaches.)
- **Interlock chip:** `background:#1B1B1B; color:#FAFAFA;` — solid dark pill, `⬡` prefix, `↔` suffix. Reads as a "seat," visually heaviest = most structural.

Group headers keep the thesis grouping ("Money flows to / Influences / Influenced by / Board interlocks") but now the chips *self-identify* by type, so a user can scan a mixed group without reading.

## 5. In-grain tokens

Reuse exactly: `#1B1B1B` / `#FAFAFA` / `#E8C547` / `#B8860B`; domain colors `#1f77b4 #b84a00 #1e7d32 #b71c1c #6a1b9a #5d4037`; `border-radius:8px` cards, `4px` chips; `#E0E0E0` borders; `#FFF8E1` gold-tint (already used in guide-fact). No new palette, no new radius, no new visual layer.

## 6. Accessibility

- **Keyboard:** `<details>/<summary>` and the "More" button are natively focusable; chips already handle Enter/Space. Focus moves to the "More" button on open.
- **Screen reader:** each chip gets `aria-label` = full sentence, e.g. `"Money flows from MultiCare to Ryan Mello"` — the icon/arrow are `aria-hidden`, the label carries meaning. Drawer content wrapped in `role="region" aria-live="polite"`.
- **Contrast:** gold `#B8860B` on `#FFF8E1` and `#1B1B1B` on `#FAFAFA` both pass WCAG 4.5:1. Domain-color chips use the *darkened* domain palette (already contrast-verified in the skill).
- **Reduced motion:** `@media (prefers-reduced-motion)` disables the drawer slide and accordion animation (instant open/close).
- **Color redundancy:** icon + arrow carry the meaning, so color is never the sole channel.

## 7. Graceful degradation

- **No money source:** the money callout simply doesn't render; the switch falls through to the next focal element (interlocks → influence-in → influence-out). The panel still opens calm and thesis-shaped.
- **No interlocks:** the "Multiple hats" strip is skipped; a person with only influence edges gets the influence focal element.
- **Sparse entity (1–2 connections):** the "More" button still appears but the Connections section is short; the nudge adapts ("Explore this entity's connections…"). Empty groups render nothing, never an empty header.
- **No JS / old browser:** `<details>` degrades to always-open content; chips remain clickable links. The panel never breaks — it just shows more at once.

**Net effect:** open = header + thesis + one gold/domain-colored focal card. The user sees *the one thing that matters* about this entity, and every relationship chip is scannable by color, icon, and arrow without reading a word.
