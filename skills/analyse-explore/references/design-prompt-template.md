`design-prompt.md`

# Design Prompt Template

**Audience: AI design tool.** This template is for the AI-tool half of Step 10's choice. If the human instead chose "Human designer" or "Both", the human-facing content goes in `design-brief.md` via `references/design-brief-template.md` — a separate file, not a section bolted onto this one. That file means rationale and room to interpret; this one means precise, unambiguous build instructions with as little room for interpretation as possible. Don't blend the two styles into this document even if "Both" was chosen — an AI design tool executes what it's given; it doesn't weigh reasoning the way a human designer does.

Living document. Regenerate whenever the Project Brief's Proposed State or Recommendations section changes; overwrite in place, history in the Changelog.

**Derived only from the Project Brief's finalised recommendation** — never independently re-synthesised from the research repository. If the two disagree, the Project Brief wins and this file is regenerated from it rather than patched around the discrepancy.

---

```markdown
# Design Prompt — [Project Name]

Last Updated: dd/MM/YYYY
Source Project Brief: [path]
Audience: AI design tool

## Build Objective

[One or two sentences, imperative: "Build [X] that does [Y]." State the objective directly —
no rationale, no "why it matters." An AI design tool executes; it doesn't need persuading.]

## Design System & Brand

**This is the solution's design system — not this workflow's own document styling.** Never pull values from `brand-artefacts` or `brand-tokens.md`; those govern how Product Velocity renders its own decks and one-pagers, not the product being built. Restate the *solution's* real values here in full, unlike the Design Brief — an AI design tool consuming this prompt may have no separate access to whatever source they come from, so they need to travel with the prompt itself, not just be pointed at.

- **Sub-brand:** [FC / TA / W360 / TC — from _workflow-state.md — which brand the *solution itself* belongs to]
- **Design system:** [the actual design system, component library or Figma library this solution should be built in — name the real one used for this project's product work]
- **Colour:** [exact hex values this build actually uses, sourced from that design system — not from brand-tokens.md]
- **Typography:** [exact font family, weights, and the heading/body scale actually used, from the same source]
- **Spacing / layout:** [any token values the build needs — safe zones, gutters — from the same source]
- **Known gaps:** [anything the actual design system doesn't cover for this solution — flag it rather than inventing a plausible-looking value]

## Evidence Anchor

[Minimal — not a discussion. Which repository insights this recommendation is built on, each
with its confidence label only. No discursive reasoning: an AI design tool doesn't weigh
evidence, and a human sanity-checking the prompt before sending it needs a scannable list, not
a re-argued case.]

- [Insight name] — [confidence label]

---

## Section A — UI screen / feature design

*(Include if the Proposed State applies. Omit if the recommendation is purely journey,
blueprint or content.)*

### Screens / states to build

[Exact, named list — one entry per screen or state, precise enough that two different tools
given this prompt would build the same set]

### Components

[Exact component names. Where an existing component is being reused, name it as recorded in
the design system; where a new one is needed, specify "New component: [name] — behaves as
[…]". Never leave a component unnamed on the assumption the tool will infer one.]

### Exact copy

[Every piece of user-facing text, verbatim — headings, button labels, empty states, error
messages. No placeholder or lorem-ipsum text. If copy hasn't been finalised, write
"COPY TBD: [what it needs to convey]" rather than inventing filler that might get built as-is.]

### Interactions & states

[Every interaction with its exact resulting state, explicitly enumerated: default, hover,
loading, empty, error. These are the states most often left implicit and most often needed —
an AI tool won't infer an error state that isn't written down.]

### Functional Requirements

[Carried directly from the Project Brief, as a literal checklist]

### Non-Functional Requirements

[Carried directly, as a literal checklist — accessibility to WCAG 2.1 AA baseline,
performance, localisation]

---

## Section B — Customer journey map / Service blueprint

*(Include if the Recommendations section applies. Omit otherwise.)*

### Stages to depict

[Exact ordered list, carried from the Project Brief's Recommendations section — the sequence
itself, not a summary of it]

### Insights to surface

[The specific research insights the artefact must make visually legible — named, not
paraphrased into a vaguer "customer pain point"]

### Friction, delight and handoff moments

[Front-stage and back-stage detail for a service blueprint, each tied to where in the
sequence it occurs]

---

## Section C — Content / communications design

*(Include if applicable. Omit otherwise.)*

### Key messages

[Carried from the Project Brief, as exact, non-negotiable content points — not themes to
riff on]

### Content structure & channel plan

[Ordered message beats, exact channel per beat, sequencing and timing, tone and framing —
specific enough to generate from directly]

### Constraints

[Legal and compliance, brand voice, channel limits, translation and locale requirements]

---

## Open Items

[Anything still thin, unvalidated or ambiguous — carried from the Analyse-Explore handoff
table. Never omit these to make the prompt look more finished than the evidence supports: an
AI design tool given a gap-free-looking prompt will build on the gap with full confidence,
which is worse than a human doing the same because there's no one in the loop to notice.]

## Changelog

- **[dd/MM/YYYY]** — [slim one-line summary of what changed this update]
```

---

## Notes on use

**Audience is fixed for this file — AI design tool.** The human-designer audience has its own template and its own file (`design-brief-template.md` → `design-brief.md`), not a mode switch on this one. See Step 10 in `SKILL.md` for how the choice between them (or both) gets made.

**Precision over persuasion.** Every section here should read as an instruction, not an argument. If a sentence is explaining *why* rather than stating *what*, it probably belongs in `design-brief.md` instead, not this file.

**The solution's design tokens travel with the prompt.** Unlike the Design Brief, which can get away with pointing at the solution's design system rather than restating its values, this file inlines the literal values it needs — an AI design tool consuming the prompt in isolation can't be assumed to have read the source. This is never `brand-tokens.md`, which is a different system for a different purpose — see "Design System & Brand" above.

**No placeholder content, ever.** A human designer reading "[copy TBD]" knows to write real copy. An AI design tool given the same bracket may build with the bracket text rendered literally, or invent plausible-sounding filler that then ships. Say "COPY TBD" explicitly rather than leaving a bracket that could be executed as-is.

**If multiple sections apply**, structure the one file with clearly separated sections per artefact, same as the Design Brief. One Design Prompt, several sections — not several prompts.

**Open Items are not a disclaimer here either.** The absence of a human reviewer at build time makes this more important than in the Design Brief, not less — an AI tool won't push back on thin evidence unless it's told the evidence is thin.
