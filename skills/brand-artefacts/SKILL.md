---
name: brand-artefacts
description: >
  The single source of truth for every rendered artefact in the Product Velocity plugin —
  HTML slide decks, HTML one-page executive summaries, and any future visual output.
  Owns brand colour, typography, logos, layout, print behaviour and accessibility.
  Use this skill whenever any stage needs to produce, regenerate or restyle a visual
  artefact: a Project Brief deck, an Evidence findings deck, a one-pager, or a stakeholder
  presentation of any kind. Also use it when asked which brand colours, fonts or logos to
  use, or when checking whether an artefact meets WCAG contrast requirements. No stage
  skill defines its own styling or sources brand values from anywhere else — if a stage
  references `takeflight-design-system` or `fcb-leisure-leadership-pptx`, that is stale
  content and this skill supersedes it.
---

# Brand Artefacts

Every visual artefact Product Velocity produces comes from here. The reason is consistency you can rely on without checking: a designer should be able to generate a findings deck in FC on Monday and a brief deck in TA on Thursday and have both look like they came from the same system, because they did.

This skill does not decide *what* an artefact says. It decides how it looks and verifies that it's readable. Content always comes from a canonical markdown document produced by a stage.

## The rule that matters most

**A rendered artefact is a rendering of its source document, never an independently drafted summary.**

Every figure, insight, badge, confidence label and heading in a deck must already exist in the markdown it renders from. If something appears in a deck but not in the source document, that's a fabrication, not a flourish — and it's the failure mode most likely to embarrass a designer in front of stakeholders, because a deck gets read by people who never open the markdown.

Practical consequences:

- Don't "tighten" a finding into something more confident-sounding to fit a slide.
- Don't drop a confidence label or hypothesis tag because it clutters the layout. If it doesn't fit, the layout is wrong.
- Don't fill an empty section with plausible content. Render the gap — see the `gap` component below.
- When the source document changes, regenerate the artefact rather than patching it.

## Step 1 — Resolve the brand

**Invoke this skill fresh at every artefact-producing or artefact-regenerating step** — Intake's deck, Evidence's findings deck, every Analyse-Explore regeneration, any one-pager. Don't carry values forward from an earlier invocation in the same session, even one from a few minutes ago. If this skill was last read anywhere other than *this* step, treat that earlier read as stale and invoke it again before writing anything.

Read the sub-brand (FC / TA / W360 / TC) from `_workflow-state.md`. It's recorded once at Intake; don't re-ask.

Then read `references/brand-tokens.md` for that brand's values. **Read it every time** rather than working from memory — the values change, and a hex recalled wrongly is invisible until someone checks a contrast ratio.

Two things in that file constrain what you can do, so read them properly:

- **Usage classes.** A hex alone doesn't tell you whether a colour can carry text. `text-safe`, `heading-only`, `fill`, `accent-only` and `background` each mean something specific, and they're derived from measured contrast, not from the token's name. FC's `brand-tertiary` is named like an accent colour and cannot legally hold text; TA's supplied `brand-tertiary` is actually a background.
- **Per-brand rules.** Each brand has a short rules block covering its exceptions — FC red dropping below AA on the section tier, W360's pale cyan needing dark text, TC's near-identical primary and secondary.

If a combination you need isn't covered, say which one is missing and ask. Don't pick something that looks close.

## Step 2 — Build from the template

Use `assets/deck-template.html` for slide decks and `assets/onepager-template.html` for one-pagers. Both carry the full layout system, print rules and accessibility defaults. Fill the token block at the top; don't rewrite the CSS.

Starting from the template rather than from scratch is what makes artefacts consistent across designers and across sessions. Re-deriving a grid each time produces four slightly different decks.

**Single self-contained HTML file.** One file, no sidecar assets:

- **Logos inline as SVG markup** — not `<img src="">`, which breaks the moment the file is emailed, and not base64, which is larger than the raw markup and can't be styled. **Copy the file's full contents from `assets/logos/` byte-for-byte** — open it, copy everything between `<svg>` and `</svg>`, and paste it in. **Never redraw, approximate, simplify or shorten the path data to save space or context** — a lookalike path that renders roughly the right shape and colour is not the same logo, and this is a brand-integrity failure a designer will notice immediately even when nothing else is wrong. If file size is a genuine concern, say so and ask, rather than quietly substituting a smaller stand-in.
- **Fonts via the Google Fonts CDN**, in the marked block in the template. Keep only the brand's families and only weights 400/600/700; every extra weight is another request before the slide paints.
- **No JavaScript required to read the artefact.** A stakeholder printing to PDF should get the same thing they see on screen.

The font block is deliberately isolated and commented so it can be swapped for embedded woff2 later without hunting through generated markup. Known trade-off, accepted for beta: a deck opened offline, or on a network that blocks the Google CDN, falls back to the stacks in `brand-tokens.md`. Those fallbacks are per-typeface-class, so a TA deck degrades to a serif rather than to Arial.

## Step 3 — Compose the artefact

### Slide layouts

Five patterns cover every slide in the system. They're defined in the template; use them rather than inventing a sixth.

| Layout | Use |
|---|---|
| `slide--title` | Opening slide. Full-bleed `brand-primary` fill, `text-on-fill` text, logo (on-dark variant) |
| `slide--divider` | Section break. Full-bleed `brand-primary`, single line of text, logo (on-dark variant) |
| `slide--content` | The workhorse. White background, heading plus body or list |
| `slide--split` | Two columns for comparisons, before/after, or a list beside a callout |
| `slide--cards` | Two to four cards on the `background-container` tier — insights, options, risks |

**One idea per slide.** A wall of bullets is a document that has been mistaken for a presentation. If a section has six points, it's two or three slides.

**Every slide carries a logo, bottom-left, at 24–28px height** — sized by height so the four brands' very different aspect ratios don't produce wildly different visual weights. Which file depends on the surface: white/light-background slides (`slide--content`, `slide--split`, `slide--cards`) use the `-on-light.svg` mark; brand-colour-fill slides (`slide--title`, `slide--divider`) use the `-on-dark.svg` mark, a solid white version of the same mark. Never place the wrong variant on the wrong surface — see `brand-tokens.md` for the full pairing table.

**Give every inlined copy of a logo a unique ID.** These are Figma exports; several use a `<clipPath id="clip0_…">` that's only unique within its own export, not across the several times the same logo gets inlined into one deck. Duplicate IDs in a single HTML document are invalid and can cause a browser to clip the wrong paths on some copies — the most likely cause of a logo rendering with letters or segments missing on some slides but not others. Suffix the `id` and every `url(#…)` reference to it with something unique per slide (e.g. `clip0_142_1871-s4`) every time the markup is copied in — full detail in `brand-tokens.md`.

### Components

- **`badge`** — for hypothesis-linked insights. Text label, not colour alone: "Validates hypothesis" or "Revises hypothesis". Net-new insights carry no badge.
- **`confidence`** — High / Medium / Low, visible on the slide, never hidden in speaker notes. A confidence label that isn't shown is the same as a confidence label that doesn't exist.
- **`gap`** — for anything unresolved: an unanswered P0, an unvalidated hypothesis, a missing metric. Renders visibly rather than being omitted. Omitting a gap makes the artefact *look* more complete than the project is, which is precisely backwards.

Never encode meaning in colour alone — WCAG 1.4.1. Every badge, confidence level and status carries text.

## Artefact structures

**Filenames** for every artefact below follow `conventions.md` §6: `<Artefact type> - <Project Name>.html`, project name in full, not the slug. Never save these as `<project-slug>-<artefact-type>.html` — that reads slug-first in a file explorer, which is exactly the pattern §6 exists to avoid.

### Project Brief deck (Stage 1)

Save as `Project Brief - <Project Name>.html`. Renders `project-brief.md`. Twelve slides:

1. **Title** — project name, "Project Brief", stage, date
2. **Executive Summary**
3. **Problem Statement** — what isn't working, why it matters. Split across two slides if dense
4. **Users & JTBD** — primary user segment(s), job(s) to be done, known pain points with source. Every item on this slide carries its `(hypothesis)` tag verbatim, the same as in the source document — this slide is hypothesis content, not settled fact, and looks like it
5. **Current State**
6. **Proposed State** — a placeholder slide stating this is defined at a later stage. Keep it rather than omitting it, so deck structure matches the written Brief and later-stage decks that will fill it in
7. **Scope & Boundaries**
8. **Success Criteria**
9. **Constraints**
10. **Stakeholders & Governance**
11. **Risks, Assumptions & Open Questions**
12. **Next steps** — handoff to Evidence

Any P0 gap or designer override recorded in the Brief's Intake Notes surfaces using the `gap` component, on the slide it relates to. A deck that hides a missing success metric is worse than no deck.

### Evidence findings deck (Stage 2)

Save as `Evidence Findings - <Project Name>.html`. Renders `research-repository.md`. Regenerate on **every** repository update — this is a live artefact, stable filename, overwritten each time, never a dated snapshot.

1. **Title** — project name, sub-brand, the repository's own `Last Updated` date
2. **Current State Pain Points** — brief. Context-setting, not the payload
3. **Insights** — one per slide or grouped by theme, whichever suits the volume. Hypothesis-linked insights carry a `badge`; net-new ones don't. `confidence` visible on every one. Order and weight them by the design output target(s) recorded in state — if more than one is recorded, weight for each rather than favouring whichever appears first
4. **Opportunities** — as How Might We statements, each tracing back to at least one insight. An HMW with no evidentiary root doesn't belong here
5. **Recommendations & Next Steps** — concrete. This is the slide stakeholders and the next stage act on

Every insight, badge and confidence label must match the repository exactly.

### One-page executive summary

Save as `Executive Summary - <Project Name>.html`. Renders from `project-brief.md`. A **narrative memo** for a senior exec audience — full sentences and short paragraphs, not slides. One section is the exception: "What we're doing about it" is a short bulleted list, because a leader scanning for momentum reads a list of actions faster than a paragraph, and this is the section carrying the momentum.

**The anchor is action, not gaps.** The most common failure mode — seen in the first pre-flight test — is a one-pager that reads as a list of everything unresolved (no baseline, no owner, stakeholders disagreeing) dressed up in full sentences. That's an internal status update, not an executive summary. Every open item still belongs on the page — never hide a gap, see `conventions.md` §4 — but framed as *what the team is already doing about it*, not as a problem sitting there unattended. "Confirming the attach-rate baseline with Analytics this week" is one sentence away from "no baseline has been agreed." Same fact. Opposite read.

- **Title + one-line pitch.** The pitch is the customer or business problem in one sentence a stakeholder could repeat in a hallway — not a process description ("we haven't defined success yet"). A stake in the ground about what's broken and for whom.
- **The problem** — customer and business pain, current state, in plain terms. **Strictly external and commercial.** A missing metric definition, a disagreement between two stakeholders, or an unnamed owner is not a customer problem — that's internal process detail, and it belongs in "What we're doing about it," not here. If this section is doing double duty as a list of what's unresolved internally, that's the anti-pattern this rule exists to prevent.
- **Why now** — what's driving the timing. If nothing was said at kickoff, say so plainly; inventing urgency is worse than reporting none.
- **What we're doing about it** — 3 to 5 concrete, near-term actions. Draw them from the Brief's Intake Notes (unresolved P0s, flagged gaps) and its `Next stage` line. State the action and, where known, who owns it and roughly when: "Confirming the baseline with Analytics — this week," not "the baseline is unresolved." If the Brief has already been updated post-Analyse-Explore with a chosen direction, lead this section with that direction in one sentence before the action list. Source every item from the Brief itself; if it doesn't name an owner or a timeframe, write "owner TBD" rather than inventing one.
- **What success looks like** — the metrics from Success Criteria, with baselines where known.
- **What could go wrong** — the top one or two risks, in a sentence each.
- **Decision needed** *(optional — include only if genuinely applicable)* — a specific decision or resource the team cannot resolve itself. Omit the heading entirely if every open item already has an owner and a next action under the team's own steam in "What we're doing about it." Don't manufacture an ask to fill the section.

Still deliberately **no invented solution at Intake.** "What we're doing about it" describes the workflow's next actions — what Evidence will validate, what's being chased down — never a product answer that doesn't exist yet. That distinction is what keeps the section honest rather than just relocating the fabrication risk to a friendlier heading.

Target 400–550 words of prose plus the action list, but the real test is the rendered output. `assets/onepager-template.html` uses a fixed A4-height container that visibly overflows if content is too long — so the check is: open it and confirm nothing spills past the page boundary. If it overflows, **cut content**. Don't shrink the font below 11pt or reduce margins below 20mm to force a fit; an unreadable page that technically fits is not a one-pager.

Write for someone with ninety seconds and no meeting context. No jargon, no unexpanded internal acronyms.

## Accessibility

WCAG 2.1 AA is the baseline, and these are stakeholder-facing documents that get forwarded, projected and printed, so it isn't theoretical.

- **Contrast**: 4.5:1 body text, 3:1 large text (24px regular / 18.66px bold and above) and non-text elements. All ratios for approved combinations are recorded in `brand-tokens.md` — use them rather than eyeballing. If you need a combination that isn't listed, calculate it before shipping and add it to the file.
- **Never colour alone** for meaning — WCAG 1.4.1.
- **Semantic HTML**: real headings in order (`h1` once per slide), `<ul>` for lists, `<section>` per slide. A screen reader shouldn't meet a wall of `<div>`.
- **`lang="en-AU"`** on the html element. Content is Australian English throughout.
- **Text is text.** Never render body copy as an image.
- **Print colour fidelity**: `print-color-adjust: exact` so brand fills survive PDF export. Without it, browsers helpfully strip your title slide's background.

## Step 4 — Verify before reporting done

A file that saved isn't an artefact that works. Check, in this order:

1. **The file exists and is the expected size** — a 2 KB deck means the content didn't make it in.
2. **Logo fidelity** — for every inlined logo instance, confirm the path data was copied from `assets/logos/<file>.svg`, not redrawn or shortened. Rough tell: the source files run from ~9 KB (TC) to ~61 KB (W360) with dozens of path elements each; an inlined mark with only one or two short paths is not the real logo, regardless of colour or approximate shape. Count `<path>` elements per logo instance and compare to the source file if unsure.
3. **Slide count matches the structure** — twelve slides for a Brief deck, not seven because sections were skipped.
4. **Spot-check content against the source document** — pick two or three specific claims, figures or insights and confirm each appears in the source markdown. This is the check that catches fabrication.
5. **Every hypothesis tag, badge and confidence label carried through.**
6. **One-pager only**: confirm it fits the page container without overflow.
7. **Record it** in the Artefact Registry in `_workflow-state.md` — filename, type, and the sub-brand used, so a later stage restyles consistently instead of guessing.

**Report two disclosures explicitly, every time an artefact is delivered — each its own labelled line, never folded into the other or into an unrelated disclosure (like Intake's inferred-vs-transcribed note):**

- **The spot-check, named as such:** "Spot-checked [N] claims against the source — [list them briefly]." A check that isn't reported this way is indistinguishable from a check that didn't happen — don't let it get absorbed into a different disclosure where it's no longer legible on its own.
- **Logo fidelity, named as such:** "Logo: copied verbatim from `assets/logos/[file].svg`, [N] path elements, unique clip-path ID per instance." If it wasn't copied verbatim, say so plainly rather than letting a roughly-right-looking logo pass unremarked.
- **The standing limitation, even on a clean pass:** "Structural checks passed (file size, slide/section count, content spot-check). I haven't visually rendered this — worth opening it yourself to confirm layout, PDF export, and offline font fallback." No text-based check can confirm layout, print output, or font fallback, so say so every time rather than letting a clean structural pass imply those were checked too.

If a check fails, say which one and what you found. Reporting "deck created" when slide 6 is empty is the kind of error a designer only discovers in the meeting.

## Bundled resources

- `references/brand-tokens.md` — colour with usage classes, typography, logos, per-brand rules. Read every time; edit this file when brand values change.
- `assets/deck-template.html` — 16:9 slide system: layouts, components, print rules, accessibility defaults.
- `assets/onepager-template.html` — A4 narrative memo container.
- `assets/logos/` — one on-light and one on-dark SVG per brand. Inline the markup, and give each inlined copy a unique ID (see `brand-tokens.md`).
