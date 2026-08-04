---
name: analyse-explore
description: >
  Stage 3 (Analyse-Explore) of the Product Velocity plugin. Turns a validated research
  repository and Project Brief into a set of comparable, evidence-backed recommendations for
  how to solve the problem, then — once the human has chosen, adjusted or combined a
  direction — records it in the Project Brief and produces a Design Brief for whoever builds
  the design. Use whenever the human wants to move from "what did we learn" to "what should
  we do about it"; asks for recommendations, opportunity framing or solution directions
  grounded in research; wants to compare design approaches before committing to one; or wants
  a Design Brief for a design tool or another designer to build from. Assumes a Project Brief
  and a research repository both exist — run the `orchestrator` skill first; it establishes
  project state and routes back if either input is missing.
---

# Analyse-Explore — Stage 3

Converts validated research into a small set of genuinely different, comparable ways to solve the problem — not one obvious answer dressed up as a choice.

This stage produces no design. It produces the reasoning and the decision artefacts a design can then be built from: a direction recorded in the Project Brief, and a Design Brief to build against. Every recommendation traces back to something actually in the research repository. An appealing idea with no evidence behind it is a hypothesis, and should be labelled as one if it's included at all.

**Before starting**, read `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md`. It carries the rules this stage follows and no longer restates: language, question format, living-document mechanics, anti-fabrication and confidence labelling, write discipline (locate → verify → write → verify), file paths, and Confluence formatting.

## Flow overview

1. Read the Project Brief and research repository; detect fresh run vs update
2. Confirm the design output target(s)
3. Optionally suggest a competitor or market scan
4. Generate three comparable recommendation approaches
5. Present them, then a consolidated comparison table
6. Iterate — open-ended, persisting each round
7. Record the chosen direction in the Project Brief
8. Regenerate any existing rendered artefacts
9. Human reviews the updated Brief
10. Ask who it's for, then produce the Design Brief and/or Design Prompt
11. Human reviews whichever was produced
12. Hand off

## Step 1 — Read the inputs

Read `project-brief.md` and `research-repository.md`. If either is missing, stop rather than inferring recommendations from a partial picture.

From the **Project Brief**:

- Executive Summary and Problem Statement — the frame every recommendation must serve
- Scope & Boundaries, Success Criteria, Constraints — the guardrails. Don't propose something the Brief has already ruled out of scope
- Intake Notes — any P0 gap or designer override. A recommendation resting on a success metric that was never defined needs to say so

From the **research repository**:

- The full Hypothesis Validation Map and Additional Insights. Every recommendation cites specific entries by name, with their confidence label carried through
- Anything flagged thin or still-unvalidated — this decides which directions can be recommended confidently and which are higher-risk bets

From **`_workflow-state.md`**: the sub-brand, the design output target(s), and the Artefact Registry.

**Fresh run or update** comes from the Stage Status in `_workflow-state.md`. If it records this stage as complete, read the existing `opportunities-analysis.md` in full — you need the prior options and the human's earlier feedback before regenerating anything. If state and folder contents disagree, ask.

## Step 2 — Confirm the design output target(s)

Evidence recorded these in `_workflow-state.md` — one or more. Carry the full list forward; don't ask again.

Ask a multi-select to confirm only if it's missing, ambiguous, or the human's current request implies something different from what's on file — for example the state lists only "UI screen" but they're now also asking about the journey. This decision determines which pattern(s) Step 4 uses, so it's worth getting right before generating anything.

If it's missing entirely, that means Evidence didn't write it to state. Note that to the human rather than silently patching it, so the gap gets fixed rather than recurring every project.

## Step 3 — Optional: suggest a competitor or market scan

This stage doesn't gather new primary research by default; it synthesises what Evidence validated. One exception: if a competitor or market-positioning gap would **materially change which recommendation is strongest** — the Problem Statement references competitive parity, or all candidate directions are evidence-thin on the same point — suggest a scan rather than running one unprompted:

> The repository doesn't have anything on how [comparable products] handle this. A quick scan
> could sharpen these options — want me to run one before I draft recommendations?

If approved: run it, then feed the findings into `research-repository.md` using **Evidence's own update mechanics** — overwrite in place, confidence-labelled, sourced, one slim Changelog line. Don't invent a parallel logging format here. Re-read the updated repository before Step 4.

If declined, proceed. The absence of a competitor view isn't a blocker.

## Step 4 — Generate recommendation approaches, one pattern group per target

Full detail of each pattern, and how to handle more than one target, is in `references/recommendation-patterns.md`. In summary:

- **UI screen / feature design** → three approaches to solving the interaction problem, described in text. Not designs, not wireframes. Each genuinely different in **mechanism** — reduce steps, surface information earlier, change the entry point, shift a decision from user to system. Two options that differ in button placement are one approach with a cosmetic edit.
- **Customer journey map / Service blueprint** → three approaches to the sequence or structure of the journey, each listing its key stages so the human can see the shape without reading a script.
- **Content / communications design** → three messaging strategies, each with its content structure (ordered message beats), channel and sequencing, and tone.

**If Step 2 recorded more than one target, generate each pattern's set of approaches independently** — a separate group of (usually three) options per target, not one blended set. Don't let a UI mechanism and a journey structure compete as if they were comparable options; they answer different questions. Keep pattern groups in the order the targets were recorded.

Every approach, whichever pattern:

- **Cites specific repository insights by name**, with confidence labels carried through. Don't launder a Low-confidence insight into sounding like settled evidence — the confidence label is what lets the human weigh the option rather than just like it.
- **Names what it deliberately doesn't address**, where that's a meaningful trade-off between the options. "Approach B doesn't resolve the mobile drop-off in Insight 4 — it's optimised for the desktop-heavy segment" is what makes a comparison honest rather than one-sided.
- **Stays solution-agnostic about visual design.** No screens, no layouts.

**If the evidence only cleanly supports two distinct directions, present two and say so.** A manufactured third option is worse than an honest two: it wastes the human's evaluation time and implies a breadth of evidence that doesn't exist.

## Step 5 — Present the recommendations

**If more than one target was recorded, present one pattern group at a time**, each under its own heading naming the pattern ("Pattern A — UI screen / feature design"), with its own approaches and its own comparison table. Don't interleave approaches from different groups, and don't merge them into a single table — see `recommendation-patterns.md` for why.

Format each approach so it stands out from the surrounding text:

### **Approach [N]: [Name]**

[1–2 sentence description]

[For UI: the mechanism of change. For Journey/Blueprint: key stages as a short ordered list. For Content: message beats, channel and sequencing, tone.]

> *Why this is credible:* [reasoning citing named repository insights and their confidence labels]

**Trade-off:** [what this approach doesn't address]

Then a comparison table for that group's decision:

| # | Approach name | Summary | Key insight(s) referenced | Confidence |
|---|---|---|---|---|
| 1 | … | … | … | … |
| 2 | … | … | … | … |
| 3 | … | … | … | … |

**If only one target was recorded**, number plainly (1/2/3) as above. **If more than one**, prefix the index with the pattern letter (A1/A2/A3, B1/B2/B3, …) in both the approach headings and every table, so a reference to "2" is never ambiguous about which group it's in.

The index is what the human references when responding — "go with 2", "combine 1 and 3", "adjust 2 to also cover mobile", or, with multiple groups, "go with A2, and combine B1 and B2".

## Step 6 — Iterate

Open-ended by design, no cap on rounds. The human may choose one as-is, adjust or extend one, combine several into a hybrid, or reject all three and redirect. If they reject everything, treat their steer as new input and regenerate — don't just reword the rejected options.

**Each pattern group reaches its own chosen direction on its own timeline when more than one is in play.** The human might settle on the UI direction in round one while still iterating on the journey map in round three — that's normal, not a stall. Don't hold a settled group open waiting for another to catch up, and don't treat one group being decided as implicit sign-off on a group the human hasn't actually addressed.

**Update `opportunities-analysis.md` in place after every round**, with a slim Changelog entry naming which group changed if more than one exists, using `references/opportunities-analysis-template.md`. Don't wait until a direction is chosen: a session that ends mid-discussion should leave the reasoning captured, not lost.

Proceed to Step 7 for a given pattern group only once the human has clearly chosen a direction **for that group**. "I like A2 but…" is not a decision on Pattern A, even if Pattern B is already decided. Once every recorded target's group has a chosen direction, move on to Step 7 for all of them together.

## Step 7 — Record the direction in the Project Brief

Edit `project-brief.md` in place. It stays the single canonical Brief — don't fork a copy.

**If the target is UI screen / feature design**, replace the **Proposed State** placeholder that Intake deliberately left with:

- Description of the chosen solution — what it is, how it works, in plain terms
- Evidence backing it — cited references to repository insights, not restated from scratch
- **Functional Requirements** — structured list of what the solution must do
- **Non-Functional Requirements** — accessibility (WCAG 2.1 AA baseline), performance, localisation, as relevant
- The screens and states needed to support it
- A short stakeholder-facing paragraph justifying the benefit of building it — the "why fund this", not a repeat of the requirements

**If the target is a journey map, service blueprint, or content/communications design**, add or update a **Recommendations** section instead:

- The key sequence of stages, or message beats for content
- Evidence backing it — cited repository insights
- A short stakeholder-facing justification for producing the artefact

**If more than one target was recorded** — a journey map plus supporting UI screens, say — include both sections, one per pattern group with a chosen direction, cross-referenced so it reads as one combined direction rather than two unrelated ideas. Recommendations first, then Proposed State. This is the normal path once Step 2 allows multiple targets, not a rare edge case.

## Step 8 — Regenerate existing artefacts

Read the Artefact Registry in `_workflow-state.md`. For every artefact beyond the markdown Brief, regenerate it from the now-updated Brief so it doesn't drift.

Apply the **locate → verify → write → verify** discipline in `conventions.md` §5 to each one. The Registry is a reliable starting point, not a guarantee — it doesn't know whether someone renamed a file or moved a Confluence page outside this workflow. If a target has moved or can't be found, stop before writing, tell the human what the Registry says versus what you found, and correct the Registry once resolved.

Regenerate rendered artefacts by **invoking `brand-artefacts` fresh** — don't reuse tokens or layout recalled from when it was last invoked earlier in this project, even earlier this same session. Pass it the sub-brand recorded in state; let it re-read its own token file rather than being told the values directly.

One artefact-specific note: regenerating the one-page executive summary now is exactly when its **"What we're doing about it"** section stops being pure next-actions and starts leading with the chosen direction — one sentence, sourced from the Brief's now-filled-in Proposed State — before the action list. Regenerate every section that may have shifted, not just Success Criteria: the direction changes what "next steps" even are.

If the Registry lists nothing beyond the markdown Brief, skip this step.

## Step 9 — Human reviews the Project Brief

Give the human the chance to review and adjust — by editing the file, or by describing changes for you to apply. Don't proceed until they've confirmed it's correct, because the Design Brief and/or Design Prompt are derived directly from it.

## Step 10 — Ask who this is for, then produce the artefact(s)

**Ask first, single-select, three options:**

- Human designer
- AI design tool
- Both

The two audiences genuinely need different documents, not just a different tone on the same one: a human designer needs rationale and room to interpret; an AI design tool needs precise, unambiguous build instructions with no room to interpret at all. Trying to serve both in one file produces a document that's longer than either audience needs and still under-serves the one reading it literally.

- **Human designer** → produce `design-brief.md` only, using `references/design-brief-template.md`.
- **AI design tool** → produce `design-prompt.md` only, using `references/design-prompt-template.md`.
- **Both** → produce **both files**, each from its own template. Neither is a subset of the other — generate them as two independent artefacts derived from the same chosen recommendation, not one derived from the other.

**Both files, whichever are produced, are derived only from the finalised recommendation now recorded in the Project Brief** — never independently re-synthesised from the research repository. If the two ever disagree, the Project Brief is the source of truth: regenerate from it rather than patching around the discrepancy.

Living documents — regenerate whenever the Brief's Proposed State or Recommendations section changes, overwriting in place with a slim Changelog entry each.

Every artefact produced here includes project context, the chosen recommendation restated plainly, the solution's own design system and brand, and an evidence summary with confidence labels so whoever — or whatever — builds from it understands *why*, not just *what*. This is never `brand-artefacts` — that's this workflow's own document styling, not the product being designed. Weighting per target type is in each template.

## Step 11 — Human reviews the artefact(s)

Same principle as Step 9. Whatever was built directly against — `design-brief.md`, `design-prompt.md`, or both — an error here propagates into the design, so don't proceed until reviewed. If both were produced, both need review; a human signing off on the brief hasn't necessarily read the prompt meant for the AI tool.

## Handoff

The stage is done when: `opportunities-analysis.md` reflects the final state of the discussion including the paths not taken; the Project Brief has a completed Proposed State and/or Recommendations section backed by cited evidence; existing artefacts have been regenerated or their failure flagged; and every artefact chosen in Step 10 exists and has been reviewed.

Then give the human a table:

| Status | Item |
|---|---|
| **Decided** | The chosen recommendation and what's now in the Project Brief |
| **Deferred** | Options considered but not chosen — kept in `opportunities-analysis.md`, not discarded |
| **Open for the next stage** | Anything still thin, unvalidated or ambiguous that whoever builds the design will need to handle or flag |

Product Velocity currently ends here. If the human asks what comes next, say plainly that the Design Brief is the current end of the workflow and the design itself is built outside the plugin.

## Bundled resources

- `references/recommendation-patterns.md` — full detail of the three patterns, including what varies between approaches in each.
- `references/opportunities-analysis-template.md` — canonical structure for the living `opportunities-analysis.md`.
- `references/design-brief-template.md` — canonical Design Brief structure for a **human designer** audience, covering UI, journey and content weighting.
- `references/design-prompt-template.md` — canonical Design Prompt structure for an **AI design tool** audience: the same underlying recommendation, restructured as precise, unambiguous build instructions.
