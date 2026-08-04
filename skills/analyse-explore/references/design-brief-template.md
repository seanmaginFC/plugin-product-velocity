`design-brief.md`

# Design Brief Template

**Audience: human designer.** This template is for the human-designer half of Step 10's choice. If the human instead chose "AI design tool" or "Both", the AI-tool-facing content goes in `design-prompt.md` via `references/design-prompt-template.md` — a separate file, not a section bolted onto this one. This file means rationale and room to interpret; the other means precise, unambiguous build instructions. Don't blend the two styles into this document even if "Both" was chosen — write this one exactly as it reads below, and let the other file be the other file.

Living document. Regenerate whenever the Project Brief's Proposed State or Recommendations section changes; overwrite in place, history in the Changelog.

**Derived only from the Project Brief's finalised recommendation** — never independently re-synthesised from the research repository. If the two disagree, the Project Brief wins and this file is regenerated from it rather than patched around the discrepancy.

---

```markdown
# Design Brief — [Project Name]

Last Updated: dd/MM/YYYY
Source Project Brief: [path]
Audience: Human designer

## 1. Project Context

[One paragraph: the problem, who's affected, why now. Summarised from the Project Brief's
Executive Summary and Problem Statement — don't re-derive it from the research.]

## 2. Chosen Recommendation

[The chosen direction, restated plainly in a sentence or two. Reference which
Opportunities Analysis option(s) it came from.]

## 3. Design System & Brand

**This is the solution's design system — not this workflow's own document styling.** `brand-artefacts` and `brand-tokens.md` govern how Product Velocity renders its own decks and one-pagers; they say nothing about the actual product being designed, and don't belong in this section.

- **Sub-brand:** [FC / TA / W360 / TC — from _workflow-state.md — which brand the *solution itself* belongs to]
- **Design system:** [the design system, component library or Figma library this solution should be built in — name the actual one used for this project's product work. For a journey map, service blueprint or content/comms direction, this may mean brand voice and tone guidance instead of a component library. Name the real source; don't invent one, and don't substitute this workflow's own rendering system for it.]
- **Known gaps:** [anything the actual design system doesn't cover for this solution — flag it rather than substituting a value that looks close]

## 4. Evidence Summary

[The specific repository insights this recommendation is built on, each with its confidence
label. This is what lets whoever builds the artefact understand *why* this direction, not
just *what* to build — and lets them push back if the evidence looks thin.]

- [Insight name] — [confidence label] — [one-line summary]

---

## Section A — UI screen / feature design

*(Include if the Proposed State applies. Omit if the recommendation is purely
journey, blueprint or content.)*

### Screens / states to be created
[From the Project Brief's Proposed State]

### Key UI components involved
[Existing components to reuse versus new components needed, where known]

### Surrounding context
[Where this sits in the broader product or journey — what comes before and after, so the
design isn't built in isolation]

### Expected interactions & behaviour
[What happens on each key action. Note loading, empty and error states where relevant —
these are the states most often omitted from a brief and most often needed]

### Functional Requirements
[Carried directly from the Project Brief]

### Non-Functional Requirements
[Carried directly — accessibility to WCAG 2.1 AA baseline, performance, localisation]

---

## Section B — Customer journey map / Service blueprint

*(Include if the Recommendations section applies. Omit otherwise.)*

### Research insights to be visually communicated
[The actual payload of a journey artefact — the diagram exists to make evidence legible, so
list the specific insights it needs to surface, not just the steps]

### Sequence / stages to depict
[Carried from the Project Brief's Recommendations section]

### Known friction, delight or handoff moments
[Front-stage and back-stage detail for a service blueprint; anything the artefact needs to
surface rather than smooth over]

---

## Section C — Content / communications design

*(Include if applicable. Omit otherwise.)*

### Key messages that must land
[Carried from the Project Brief]

### Constraints
[Legal and compliance, brand voice, channel limits, translation and locale requirements]

### Content structure & channel plan
[Ordered message beats, channel and sequencing, tone and framing]

---

## 5. Open Items

[Anything still thin, unvalidated or ambiguous that whoever builds the design will need to
handle or flag — carried from the Analyse-Explore handoff table. Don't quietly drop these:
they're the difference between a design built on evidence and one built on evidence plus
undisclosed guesswork.]

## Changelog

- **[dd/MM/YYYY]** — [slim one-line summary of what changed this update]
```

---

## Notes on use

**Audience is fixed for this file — human designer.** The AI-tool audience has its own template and its own file (`design-prompt-template.md` → `design-prompt.md`), not a mode switch on this one. See Step 10 in `SKILL.md` for how the choice between them (or both) gets made.

**If multiple sections apply**, structure the one file with clearly separated sections per artefact, each weighted per the rules above. One Design Brief, several sections — not several briefs.

**Open Items are not a disclaimer.** They're the handover of known risk. A designer who discovers mid-build that a key insight was Low confidence will make worse decisions than one who knew from the start.
