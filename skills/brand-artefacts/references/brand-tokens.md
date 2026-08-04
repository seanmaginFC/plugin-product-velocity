# Product Velocity — Brand Tokens

The single source of truth for colour in every rendered artefact. `brand-artefacts` reads this file; no stage skill defines its own styling or sources brand values from anywhere else.

**This file is meant to be edited** — it holds values and their verified usage, not logic. If a brand's palette changes, change it here.

---

## Usage classes

A hex value alone isn't enough to render safely: the same colour can be fine as a headline and unusable as body text. Every token therefore carries a class describing what it may actually do.

| Class | Meaning |
|---|---|
| `text-safe` | Usable as body text and headings on the light backgrounds listed for it |
| `heading-only` | Large text only — 24px regular or 18.66px bold and above (WCAG 2.1's large-text threshold, which drops the requirement to 3:1) |
| `fill` | A background for text. The text colour that must sit on it is named — don't assume white |
| `accent-only` | Graphic elements only: rules, dividers, chart fills, icon strokes. Never carries text, never backs text |
| `background` | A surface tier. Text on it comes from that brand's `text-heading` / `text-body` |

**Thresholds used:** WCAG 2.1 AA — 4.5:1 for body text, 3:1 for large text and non-text UI elements. Ratios in this file were computed against the exact hex values below.

**If you change a hex, the class no longer holds.** Classes are derived from contrast maths, not intrinsic to a colour. Re-check any changed token against all three backgrounds and against white before trusting its class, or ask for it to be recalculated.

---

## FC

| Token | Hex | Class | Text on it (as fill) | Safe as text on |
|---|---|---|---|---|
| `brand-primary` | `#d40119` | `fill` + `text-safe` (conditional) | `#ffffff` — 5.50 | base 5.50 ✓ · container 5.05 ✓ · **section 4.17 → `heading-only`** |
| `brand-secondary` | `#a60106` | `fill` + `text-safe` | `#ffffff` — 7.99 | base 7.99 ✓ · container 7.33 ✓ · section 6.05 ✓ |
| `brand-tertiary` | `#0072ea` | `accent-only` | — | none |
| `background-base` | `#ffffff` | `background` | — | — |
| `background-container` | `#f5f5f5` | `background` | — | — |
| `background-section` | `#e0e0e0` | `background` | — | — |
| `text-heading` | `#212121` | `text-safe` | — | base 16.10 · container 14.77 · section 12.20 |
| `text-body` | `#424242` | `text-safe` | — | base 10.05 · container 9.22 · section 7.61 |
| `text-on-fill` | `#ffffff` | — | — | use on `brand-primary` and `brand-secondary` |

**Rules**

- FC red is the brand's signature and the most likely thing to be misused. It is safe as a headline or body text on white and on the container tier, but on `background-section` it drops to 4.17 — use it there for large text only, or switch the text to `text-heading`.
- `brand-tertiary` #0072ea is unsafe in both directions: 4.57 against white and 3.52 against `text-heading` as a fill, and 3.46 as text on `background-section`. Every use is marginal, so it's restricted to graphics. If FC needs a third text-capable accent, that's a brand request, not something to work around here.

---

## TA

| Token | Hex | Class | Text on it (as fill) | Safe as text on |
|---|---|---|---|---|
| `brand-primary` | `#552569` | `fill` + `text-safe` | `#ffffff` — 11.32 | base 11.32 ✓ · container 10.55 ✓ · section 9.50 ✓ |
| `brand-secondary` | `#2e1538` | `fill` + `text-safe` | `#ffffff` — 16.40 | base 16.40 ✓ · container 15.29 ✓ · section 13.76 ✓ |
| `background-base` | `#ffffff` | `background` | — | — |
| `background-alt` | `#fffbf5` | `background` | — | *was supplied as `brand-tertiary` — see note* |
| `background-container` | `#f7f7f5` | `background` | — | — |
| `background-section` | `#ebebeb` | `background` | — | — |
| `text-heading` | `#552569` | `text-safe` | — | base 11.32 · container 10.55 · section 9.50 |
| `text-body` | `#4a4a4a` | `text-safe` | — | base 8.86 · container 8.26 · section 7.43 |
| `text-on-fill` | `#ffffff` | — | — | use on `brand-primary` and `brand-secondary` |

**Rules**

- `#fffbf5` was supplied as `brand-tertiary` but is functionally an off-white: it fails as text on every background (1.03–1.16) and reads as a surface, not an accent. It's recorded here as `background-alt` — a warm fourth surface tier, useful for a full-bleed title slide or a callout panel, with `text-heading` (10.98) or `text-body` (8.60) on it.
- **Consequence: TA has only two accent colours.** Decks in this brand carry less colour hierarchy than FC or TC, so lean on the `background-alt` surface and on weight/scale for emphasis rather than inventing a third accent.
- TA's `text-heading` is the same value as `brand-primary`, so headings are inherently on-brand. Don't also fill a panel with `brand-primary` behind a heading — the heading disappears (1.00).

---

## W360

| Token | Hex | Class | Text on it (as fill) | Safe as text on |
|---|---|---|---|---|
| `brand-primary` | `#001ede` | `fill` + `text-safe` | `#ffffff` — 9.37 | base 9.37 ✓ · container 8.31 ✓ · section 8.60 ✓ |
| `brand-secondary` | `#a1f1ff` | `fill` (light) | `#001ede` — 7.38 · `#616161` — 4.88 · **not white (1.27)** | none — never use as text |
| `brand-tertiary` | `#0057e2` | `fill` + `text-safe` | `#ffffff` — 6.07 | base 6.07 ✓ · container 5.38 ✓ · section 5.56 ✓ |
| `background-base` | `#ffffff` | `background` | — | — |
| `background-container` | `#f4f1ea` | `background` | — | *warm cream — see note* |
| `background-section` | `#f5f5f5` | `background` | — | *cool grey — see note* |
| `text-heading` | `#001ede` | `text-safe` | — | base 9.37 · container 8.31 · section 8.60 |
| `text-body` | `#616161` | `text-safe` | — | base 6.19 · container 5.49 · section 5.68 |
| `text-on-fill` | `#ffffff` | — | — | use on `brand-primary` and `brand-tertiary` only |

**Rules**

- `brand-secondary` #a1f1ff is inverse polarity to the rest of the palette: it's a pale highlight that takes dark text. White on it is 1.27 — effectively invisible. Use `text-heading` or `text-body` on it, and never use it as a text colour itself.
- `brand-primary` and `brand-tertiary` are both saturated blues and read as the same colour family at slide scale. Don't rely on them alone to distinguish two things; use the cyan or a surface tier for separation.
- **Neutral temperature clash:** `background-container` is a warm cream and `background-section` is a cool grey. Adjacent on one slide they look like a mistake rather than two tiers. Use one or the other per slide, not both.
- `text-heading` equals `brand-primary`, so the same caution as TA applies — don't put heading text on a `brand-primary` fill (1.00).

---

## TC

| Token | Hex | Class | Text on it (as fill) | Safe as text on |
|---|---|---|---|---|
| `brand-primary` | `#2f2b43` | `fill` + `text-safe` | `#ffffff` — 13.57 | base 13.57 ✓ · container 13.00 ✓ · section 12.45 ✓ |
| `brand-secondary` | `#423d5c` | `fill` + `text-safe` | `#ffffff` — 10.23 | base 10.23 ✓ · container 9.80 ✓ · section 9.38 ✓ |
| `brand-tertiary` | `#001ede` | `fill` + `text-safe` | `#ffffff` — 9.37 | base 9.37 ✓ · container 8.98 ✓ · section 8.60 ✓ |
| `background-base` | `#ffffff` | `background` | — | — |
| `background-container` | `#fafafa` | `background` | — | — |
| `background-section` | `#f5f5f5` | `background` | — | — |
| `text-heading` | `#111111` | `text-safe` | — | base 18.88 · container 18.09 · section 17.32 |
| `text-body` | `#292929` | `text-safe` | — | base 14.55 · container 13.94 · section 13.34 |
| `text-on-fill` | `#ffffff` | — | — | use on all three brand colours |

**Rules**

- The only brand with no accessibility constraints — every combination passes AA body text. Nothing here needs a workaround.
- The constraint is hierarchy, not contrast: `brand-primary` #2f2b43 and `brand-secondary` #423d5c are both dark desaturated purples and will read as the same colour at slide scale. Use `brand-tertiary` #001ede when two elements genuinely need to be distinguished.
- `brand-tertiary` #001ede is identical to W360's `brand-primary`. Intentional or not, a TC deck's accent is another brand's signature colour — worth a glance before anything goes to a mixed-brand audience.

---

## Typography

| Brand | Headings | Body | Notes |
|---|---|---|---|
| **FC** | Roboto | Roboto | Single family — separate heading and body by weight and scale, not typeface |
| **TA** | Spectral | DM Sans | Only serif-headed brand; the contrast is the brand's signature |
| **W360** | Inter | Inter | Single family, as FC |
| **TC** | Work Sans | Open Sans | Two sans families — closely related, so keep the weight gap wide |

**Fallback stacks.** Always declare one. A deck that loses its webfont should degrade to a sensible local face, not to Times New Roman:

```css
--font-roboto:    'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
--font-spectral:  'Spectral', Georgia, 'Times New Roman', serif;
--font-dm-sans:   'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
--font-inter:     'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
--font-work-sans: 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
--font-open-sans: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
```

**Weights.** Load only what's used — every extra weight is another request before the slide renders. 400 (body), 600 (subheads, emphasis), 700 (headings) covers every layout in `brand-artefacts`. Spectral's 600 is the useful display weight; it gets heavy fast at large sizes.

**Where the fonts come from is a deployment decision, not a styling one** — see the note in `SKILL.md`. Whichever route is used, the fallback stacks above apply unchanged.

**Two brand-specific cautions:**

- **TA** — Spectral is a text serif, not a display face. At title-slide sizes it needs tighter line-height (around 1.1) and a little negative letter-spacing, or it looks loose and airy rather than confident.
- **TC** — Work Sans and Open Sans are similar enough at body sizes to look like an accident rather than a pairing. Keep a clear scale and weight separation between heading and body so the two families read as deliberate.

---

## Logos

Assets live in `assets/logos/`, one **pair** per brand: `-on-light` (brand-colour ink, for white/light backgrounds) and `-on-dark` (solid white ink, for `brand-primary`-fill backgrounds — title and divider slides). Inline the SVG markup directly into the HTML — not `<img src="">`, which breaks the moment the file is shared, and not base64, which is larger than raw markup and can't be styled.

| Brand | Light-surface file | Dark-surface file | Light ink | Size (each) | Aspect |
|---|---|---|---|---|---|
| FC | `fc-logo-on-light.svg` | `fc-logo-on-dark.svg` | `#D40119` | ~38.8 KB | 6.25:1 |
| TA | `ta-logo-on-light.svg` | `ta-logo-on-dark.svg` | `#552569` | ~15.6 KB | 3.10:1 |
| TC | `tc-logo-on-light.svg` | `tc-logo-on-dark.svg` | `#2F2B43` | ~9.3 KB | 7.55:1 |
| W360 | `w360-logo-on-light.svg` | `w360-logo-on-dark.svg` | `#001EDE`, `#2744FF`, `#738EFF`, `#181818` | ~60.7 KB | 3.33:1 |

Every `-on-dark` file is a single solid-white mark — verified `fill="white"` throughout, no other colour. That resolves the earlier W360 constraint: the dark variant is a purpose-made white mark, not a script recolour of the four-colour original, so no paths disappear against `brand-primary`.

**Which file, which surface:**

- `slide--content`, `slide--split`, `slide--cards`, and the one-pager → `-on-light.svg`.
- `slide--title`, `slide--divider` → `-on-dark.svg`.
- Never place the on-light mark on a brand-colour fill, or the on-dark mark on white. If a new layout introduces a different fill, check contrast before choosing which file to use.

**Sizing: normalise on height, never width.** Aspect ratios range from 3.10:1 to 7.55:1, so a fixed width makes the TC mark more than twice the visual weight of TA's. A footer logo height of 24–28px works across all four; let width flow from it and keep the `viewBox` so nothing distorts.

**Naming.** Files are named for the **surface** they sit on (`-on-light` / `-on-dark`), not their ink colour. The source assets were originally inconsistent on exactly this point — one used "light" to mean a light background, another to mean light ink — which is how an invisible logo reaches a stakeholder deck. Keep the surface-based convention if further variants are added.

**Two light-surface assets were modified from source**, with approval: FC and TC each shipped with a full-canvas `<rect fill="white">` behind the mark. Invisible on a white slide, but it draws a white box on any tinted surface. Both rects were removed; all ink paths verified intact.

**Duplicate-ID hardening — read this before inlining.** These are Figma exports. Several carry a `<clipPath id="clip0_…">` inside a `<defs>` block, referenced once via `<g clip-path="url(#clip0_…)">`. That ID is only guaranteed unique *within one export* — not across the several times a logo is inlined into the same deck (once per light-background slide), and not against another asset's ID in the same document. Duplicate IDs in one HTML document are invalid; a browser resolves `url(#id)` to whichever matching element it finds first, which can silently clip the wrong paths on some copies even when every inlined copy is byte-identical. This is the most likely explanation for a logo rendering with letters or path segments missing on some slides but not others.

**Give every inlined copy a unique ID.** Each time a logo's SVG markup is copied into a deck, suffix its `id` and every `url(#…)` reference to it with something unique to that slide — e.g. `clip0_142_1871` → `clip0_142_1871-s4` on slide 4. Do this for every inlined instance, not only the ones that look wrong; a collision is invisible until it isn't.

**Constraints:**

- **FC and TA are single-colour marks**, so deriving their `-on-light` / `-on-dark` pair was straightforward.
- Files are unoptimised. W360 is ~60 KB per file largely because path coordinates carry four decimal places; an SVGO pass would likely halve every file. Not urgent — one logo per artefact.

---

## Cross-brand notes

- **Three of the four brands have a token whose supplied role doesn't match what it can do**: FC's tertiary can't carry text, TA's tertiary is a surface, W360's secondary is a dark-text fill. The usage classes above exist so `brand-artefacts` renders from verified fact rather than inferring from a role name at render time.
- **`background-base` is `#ffffff` in all four brands.** Slide backgrounds are white by default everywhere; brand identity comes from the accent, heading colour and fills, not the page.
- **Never mix tokens across brands** in one artefact. The sub-brand for a project is recorded once in `_workflow-state.md`.
- **When a required combination isn't in this file, don't invent one.** Say which combination is missing and ask, rather than picking a colour that looks close.
