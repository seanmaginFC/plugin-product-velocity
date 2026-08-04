---
name: intake
description: >
  Stage 1 (Intake) of the Product Velocity plugin. Turns a stakeholder kickoff meeting into
  a structured Project Brief that later stages build on. Use whenever the human wants to
  start a new feature or product initiative, mentions a "kickoff", "project brief" or
  "intake", attaches a completed Kickoff Template, or asks to turn meeting notes into a
  brief, a Confluence page, a slide deck, or a one-pager. This is always the first stage —
  Evidence and Analyse-Explore both read its output, so a request to start later without a
  Project Brief routes back here. Run the `orchestrator` skill first; it establishes the
  project folder, the workflow state file and the dependency check this stage depends on.
---

# Intake — Stage 1

Converts a stakeholder kickoff into a Project Brief. Nothing here is final. The stage's real job is to document what's actually known and make what isn't known visible, so Evidence and Analyse-Explore start from an honest position rather than a tidy-looking one.

A Brief built on invented specifics is worse than one that plainly says "not yet known" — the invented version gets quoted in a stakeholder meeting six weeks later.

**Before starting**, read `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md`. It carries the rules this stage follows and no longer restates: language, question format, living-document mechanics, anti-fabrication and labelling, write discipline, file paths, and Confluence formatting.

## Flow overview

1. Collect the kickoff — attached document, or conversational fallback
2. Synthesise the canonical Project Brief
3. Ask which artefacts to produce
4. Produce them via `brand-artefacts`
5. Report the gate status and hand off

## Step 1 — Collect the kickoff

**If a kickoff document is attached** — raw Kickoff Template markdown, an export from the Kickoff Worksheet, or anything else clearly serving that purpose — read it directly. Match its fields against `references/kickoff-question-map.md` by **meaning, not exact string**; field names drift between versions and a rigid match will drop content that's plainly there.

**If nothing is attached**, ask for one and offer the fallback in the same message, so the human isn't forced into a second round-trip to find out there's an alternative:

> Attach a completed kickoff doc if you have one — otherwise I can walk through the key questions here in chat.

**Running the fallback:** work through `references/kickoff-question-map.md` section by section. Ask all P0 fields in a section together, wait, then move to the next. Only surface P1 fields once the P0 sections are done or explicitly deferred. A twenty-question interrogation before the Brief exists kills momentum, and the designer stops answering carefully.

**Partial or pre-flagged kickoffs:** if the attached document has a completed Intake Completeness Gate with unchecked items, or a designer override already written in, that context carries into the Brief's Intake Notes in Step 2. Don't leave it behind in the source file where no later stage will see it.

**Confirming the sub-brand.** Every visual artefact downstream — every deck, one-pager, and the Design Brief/Prompt's own design-system section — depends on this one field (FC / TA / W360 / TC), so settle it here rather than letting a later stage inherit a guess.

Counts as established, proceed without asking:

- The kickoff states one of the four codes directly, or
- It names one of these known aliases:
  - **FC** — Flight Centre, FCB
  - **TA** — Travel Associates, Luxury
  - **W360** — World360, Loyalty
  - **TC** — Travel Connect, Trip Manager, CoConsult

Doesn't count as established, ask directly:

- None of the above appears anywhere in the kickoff, or
- The scope described could plausibly span more than one of these brands (e.g. a platform capability being rolled out across brands), so a single inferred code would be a guess dressed up as a fact.

When in doubt, ask — it's one cheap question against an expensive-to-unwind downstream styling mistake once decks and briefs are already generated against the wrong brand.

Write the confirmed value to the Sub-brand line in `_workflow-state.md` before Step 4 produces anything visual. Every stage after this reads it from there and doesn't re-ask.

## Step 2 — Synthesise the Brief

Draft `project-brief.md` using `references/project-brief-template.md`. This markdown is the **source of truth** — every artefact in Step 4 is a rendering of it, never a separate draft.

Required sections: Executive Summary, Problem Statement, Users & JTBD, Current State, Proposed State, Scope & Boundaries, Success Criteria, Constraints, Stakeholders & Governance, Risks/Assumptions/Open Questions, and Intake Notes.

**Before drafting, run a field-by-field checklist against `references/kickoff-question-map.md`.** This applies whether the kickoff came from an attached document or the chat fallback. Walk every field in the map and decide where it lands — one of three outcomes, no fourth option:

1. **Mapped** to a specific Brief section.
2. **Carried to Intake Notes as unmapped** — "captured in kickoff, not reflected in Brief sections — see source" — for anything real that has no clean destination.
3. **Marked "not present in source"** — the kickoff never covered it.

A field that isn't one of these three has been silently dropped. This is the failure mode the checklist exists to catch: prose synthesis is easy to write well and still lose a line that had nowhere obvious to go — an unattributed pain point, a JTBD statement, anything that doesn't map cleanly onto a template heading. Do this pass before drafting a single sentence of the Brief, not as a check afterwards.

Four rules while drafting. The first is the one most likely to be quietly broken:

**Proposed State is descoped at Intake — this is firm, not a default.** Leave the template's placeholder text in place. Do not articulate a target future state here, even vaguely, even if the kickoff contained a clear-sounding solution. Naming a direction before Evidence has run anchors the entire project to it, and everything downstream inherits that anchor. Stage 3 fills this section once a direction is actually chosen.

**A stakeholder-proposed solution goes under Risks, Assumptions & Open Questions** — recorded as an unvalidated solution direction. Don't discard it (it's real signal about what stakeholders expect) and don't promote it to Proposed State (it hasn't been tested).

**Preserve `(hypothesis)` labels verbatim.** Anything from the kickoff's Users & JTBD section stays tagged. A tidier document doesn't make a guess into a fact.

**Don't silently resolve gaps.** A P0 left "Unknown / TBD" goes into Intake Notes, not papered over with something plausible.

After drafting, read the Brief back against the kickoff and tell the human out loud which parts you inferred rather than found stated. They can't audit that from the document itself.

## Step 3 — Ask which artefacts to produce

Once the Brief content exists, ask which formats the human wants. One multi-select question, not a sequence of yes/no prompts:

- Confluence page
- HTML slide deck
- Markdown only
- One-page executive summary

Any number, including none beyond markdown — the canonical Brief is always saved regardless.

**If Confluence is selected**, follow up with which space. Load the options via the Atlassian tools (`tool_search` for "confluence", then `getConfluenceSpaces`) and present them as choices rather than asking the human to recall a space key from memory.

If the orchestrator's pre-flight found the Atlassian connector unavailable, still offer the option and say why it can't be produced this run — silently removing it leaves the human wondering what happened to it.

## Step 4 — Produce the artefacts

**Markdown Brief — always.** Saved as `project-brief.md` in the project folder. Every other artefact renders from it.

**Everything visual — slide deck, one-pager — via a fresh invocation of `brand-artefacts`.** That skill owns brand colour, typography, logos, layout, print behaviour and the slide sequence for a Project Brief deck. Don't specify styling here or source brand values from anywhere else — and don't work from a memory of that skill's tokens either; invoke it so it re-reads `brand-tokens.md` itself.

Pass it: the Brief content, the sub-brand from `_workflow-state.md`, and which artefact type to build. Any P0 gap or designer override must reach it too, so it renders using the `gap` component rather than being smoothed out of the visual version — the deck is what stakeholders actually read.

**Confluence page** — convert the Brief's markdown to what `createConfluencePage` expects (check its schema at call time), create it in the selected space, then apply the create-then-verify discipline in `conventions.md` §5 and the formatting rules in §7. Report the honest status: "created" only after the read-back confirms it, otherwise "attempted, unverified" or "failed".

*Not yet exercised end to end:* live Confluence writes have only been tested as reads. Treat the first real use as a test, apply the verification especially carefully, and say so if it's genuinely the first attempt.

**Something else** — same discipline: render from the Step 2 Brief, don't re-derive from the raw kickoff.

**Record every artefact produced** in the Artefact Registry in `_workflow-state.md` — one row per artefact that actually exists, with its location and the sub-brand used for anything visual. Never pre-populate rows for artefacts that were offered but not chosen; a later stage will try to update something that was never made.

## Handoff

Report the **P0 gate status** explicitly — this is what the orchestrator checks before advancing to Evidence:

- Every P0 field answered, or
- Named as unresolved and prompted for, then advanced on a designer override with the reason recorded in both Intake Notes and the state file.

Advancing past a missing P0 *without prompting* is the one outcome this stage must never produce.

Then give the human the status table from the orchestrator's Handoff section: what's confirmed, what's still a hypothesis, what's deferred, and what's open for Evidence. That table is the actual deliverable of this stage — the file is just where it's written down.

## Bundled resources

- `references/kickoff-question-map.md` — the canonical field list. Used both to parse an attached kickoff and to run the conversational fallback.
- `references/project-brief-template.md` — the Brief structure every artefact renders from.
