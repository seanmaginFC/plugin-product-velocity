---
name: evidence
description: >
  Stage 2 (Evidence) of the Product Velocity plugin. Turns a Project Brief's hypotheses into
  a validated, living research repository, drawing on whatever user research and behavioural
  data are relevant. Later stages read this repository as their research context. Use
  whenever the human wants to collate, validate or challenge research insights against a
  Project Brief; wants to build, extend or update a research repository; mentions gathering
  evidence from Confluence, Jira, Miro, FullStory, Great Question, Qualtrics, Usabilla or
  PowerBI; shares the results of a completed usability test, survey or interview that should
  feed a project's evidence base; or wants a research findings deck for stakeholders. Always
  checks the FCTG Research Repository Confluence space alongside any project-specific
  sources. Assumes a Project Brief exists — run the `orchestrator` skill first; it establishes
  project state and routes back to Intake if the Brief is missing.
---

# Evidence — Stage 2

Converts the Project Brief's `(hypothesis)`-tagged content into a research repository that confirms, revises, or flags-as-still-unvalidated each hypothesis against real evidence — plus whatever the research surfaces that nobody predicted.

Evidence should be firmer here than at Intake, but it often isn't firm at all, and that's the normal starting point rather than a failure. An honest "still unvalidated" is worth more to Analyse-Explore than a confident-sounding guess. When an insight is thin, say so plainly and tell the human — that's the most useful output this stage produces, because it tells them exactly what research to commission next.

**Before starting**, read `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md`. It carries the rules this stage follows and no longer restates: language, question format, living-document mechanics, anti-fabrication and confidence labelling, write discipline, and file paths.

## Flow overview

1. Read the Project Brief; detect fresh run vs update from `_workflow-state.md`
2. Ask what design output this evidence is meant to inform
3. Ask which research sources are relevant (Round 1)
4. Gather and read them, following the discover-approve loop
5. Ask follow-ups informed by what the sources actually contain (Round 2)
6. Synthesise against the hypotheses, plus net-new insights
7. Produce the repository and the findings deck
8. Hand off

## Step 1 — Read the Project Brief

Read `project-brief.md` from the project folder. If it isn't there, stop — Evidence with no Brief has no hypotheses to validate, and inventing them defeats the point of the stage.

Extract:

- **Executive Summary and Problem Statement** — read these first. They frame how you interpret every source that follows, not just what you pull from the Brief.
- Every `(hypothesis)`-tagged item from Users & JTBD
- **Intake Notes** — gaps, designer overrides, anything flagged unresolved. A hypothesis whose supporting metric was never defined at Intake needs to be read in that light.
- The sub-brand, from `_workflow-state.md`

**Fresh run or update** is determined from the Stage Status in `_workflow-state.md`, not by sniffing for a filename. If it records Evidence as complete, this is an **update**: read the existing `research-repository.md` in full before anything else, because you need its current Hypothesis Validation Map to know what might change. If state and folder contents disagree, ask rather than assuming.

## Step 2 — Ask what design output(s) this evidence will inform

Before any source elicitation, ask what deliverable this evidence base supports. **Multi-select, four options** — more than one can apply. A project can legitimately span, for example, a journey map and a UI screen, and forcing a single choice here just pushes the same ambiguity downstream into Stage 3.

- Customer journey map
- UI screen / feature design
- Service blueprint
- Content / communications design

Swap an option for a better-fitting one if the Brief's Scope & Boundaries already names a specific deliverable. If none fits, the human can free-type — don't prompt separately unless their answer is ambiguous.

Record **all** selected targets in `_workflow-state.md`, as a list even when there's only one, and carry the full list into Step 6 and the findings deck. It should visibly shape what gets foregrounded, not sit as a forgotten preamble — Stage 3 reads it too, and shouldn't have to ask again.

## Step 3 — Ask which sources are relevant

Precede the question with a plain text note, not a button, since it isn't a choice:

> I'll always check the FCTG Research Repository Confluence space (fctg-pme.atlassian.net/wiki/spaces/FCRR) by default. Anything else to draw on?

Then a multi-select on categories. This narrows category only — it doesn't collect the source:

- Confluence or Jira
- Miro boards
- Survey or test data (Great Question, Qualtrics, Usabilla)
- Other (attachments, URLs, FullStory, PowerBI, anything else)

Then follow up in plain text for the actual links, files or pasted content for whichever buckets were chosen. Accept whatever mix they provide. Full prompt wording in `references/source-elicitation-prompts.md`.

**If the orchestrator's pre-flight flagged a missing dependency, say so before this question, not after.** A human who picks "Confluence or Jira" and then hits a wall has wasted a round-trip, and they may well have the same material as an export or a paste.

## Step 4 — Gather and read sources

**Invoke `leisure-research-insights` before touching Confluence, Jira, Miro or FullStory with any other tool — don't decide it's probably available and skip straight to reading them directly to save a step.** "It's quicker to just check Confluence myself" is not a valid reason to bypass delegation; it's the exact failure this rule exists to prevent. There are only two legitimate paths through this step: invoke the skill and use what it returns, or establish that it's genuinely unavailable (not listed this session, or invocation fails) and follow the degraded branch below. Reading these four source types with generic tools while never actually attempting either path is not a third option.

**Confluence, Jira, Miro and FullStory → delegate to `leisure-research-insights`.** It carries the anti-fabrication discipline, triangulation logic and citation conventions for those four systems.

Apply this stage's flex-down rigour on top: don't inherit its hard escalation and source-count gates verbatim (it expects five-plus sources per major claim and escalation to a named research team). Label confidence instead of blocking. Early evidence is thin by nature.

**If that skill isn't available**, the stage is **degraded, not blocked**:

- Those four source types are unavailable. Don't read them with generic tools instead — that skill exists to carry the citation and triangulation discipline, and working around it produces exactly the confident-but-unsourced output this plugin is built to prevent.
- Everything else proceeds normally.
- Log the unavailable categories in the Source Log, and expect a lower confidence ceiling: High requires triangulation across independent sources, and losing whole categories makes that harder to reach honestly. Don't let a repository full of Medium labels imply nothing was missing — say the ceiling out loud too, per the Handoff requirement below.
- Point the human at the contact in `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/contact-list.md`.

**State the outcome to the human in chat, either way, before reading anything.** Either "Invoking `leisure-research-insights` now to read [sources]" or the degraded-branch message above with the contact named per `conventions.md` §9. The human shouldn't have to open `_workflow-state.md` to find out whether delegation actually happened. If it didn't happen and the reason isn't genuine unavailability, that's an unlogged process gap, not a quiet shortcut — log it in `_workflow-state.md`'s Open Gaps & Overrides table, the same way a skipped Round 2 waiver gets logged.

**Everything else — attachments, Great Question transcripts, Qualtrics and Usabilla exports, PowerBI reports, arbitrary URLs — read directly** with standard file and web tools. No specialist skill covers these yet; expect gaps on first real use and flag them rather than papering over them.

**Discover → approve loop, mandatory.** Whenever a source references a secondary artefact — a hyperlink inside a PDF pointing at another Miro board, a Confluence page citing another page — **stop**. List every secondary artefact found so far, with enough context for the human to judge relevance without opening each one, and wait for explicit approval before fetching any of them. All, some, or none.

Do this before producing any output. Never silently expand scope: an agent that follows five links deep has changed what the human asked for without telling them. If a secondary artefact links onward, repeat the loop, and mention when you're going more than one layer deep so they can decide whether to keep following the chain. Script in `references/source-elicitation-prompts.md`.

## Step 5 — Ask follow-up questions (Round 2)

This step runs every time, even when the sources look complete. Informed by what the sources actually contained — not generic. Three likely triggers:

- A hypothesis with **no evidence either way**
- **Conflicting signals** between sources, or between attitudinal and behavioural data
- **Thin coverage** in an area the Brief flagged as important

**Check for these triggers explicitly, against the draft Hypothesis Validation Map and Additional Insights you're about to write — not from memory.** Before moving to Step 6, re-read every entry you're about to record. Any entry landing on Still Unvalidated, any pair of entries that disagree, and any hypothesis the Brief flagged as important but sourced thinly, is a trigger — even if a source's own caveats already discuss it. A source explaining its own limitation is not the same as the human confirming what to do about it.

**Don't resolve a trigger yourself and move on.** If you find a trigger, it goes to the human — even ones you're confident you already understand from the source material. Surfacing it costs one round-trip; silently deciding on the human's behalf is exactly the failure this step exists to prevent.

Count the issues first and tell the human roughly how many are coming. Per-issue option sets are in `references/source-elicitation-prompts.md`. Treat any "I can explain" / "I have context" answer as a prompt to ask a plain follow-up, not as a complete answer.

**If, after this check, there are genuinely zero triggers, say so explicitly to the human as a one-line statement** (e.g. "No Round 2 follow-ups this time — every hypothesis has either clear single-direction evidence or was already flagged Still Unvalidated with nothing to adjudicate") **before moving to Step 6.** A silent skip and an explicit "nothing to ask" look identical in the output; only one of them is auditable.

Don't proceed to synthesis until every issue raised this round is resolved or explicitly waived by the human. A waiver the agent grants itself doesn't count — log any human waiver in `_workflow-state.md`'s Open Gaps & Overrides table, same as a P0 override at Intake.

## Step 6 — Synthesise

Insights are unrestricted in scope — don't force everything into a hypothesis slot.

Weight emphasis by the design output target(s) from Step 2: journey-wide behavioural patterns lead for a journey map, localised interaction friction leads for a UI screen. **If more than one target was recorded, weight for each — don't pick a dominant one and bury the rest.** An insight that matters for the UI screen doesn't stop mattering because a journey map was also selected; it just gets foregrounded in a different part of the repository. But don't discard what falls outside every selected focus, either. Record it; just don't lead with it. An insight dropped because it didn't fit any current deliverable is an insight the next project has to rediscover.

- **Hypothesis-linked insight** — maps to a `(hypothesis)` from the Brief. Marked Confirmed / Revised / Still Unvalidated, with an explicit link back to the source hypothesis. Carries a badge in the deck.
- **New insight** — doesn't map to anything in the Brief. No special treatment; just as valid, only not pre-existing.

The anti-fabrication and confidence-labelling rules in `conventions.md` §4 apply throughout, and this is the stage they exist for. Two that get broken most often: where attitudinal and behavioural data diverge on the same point, say so explicitly — divergence is itself a finding, not a discrepancy to reconcile. And a hypothesis being *addressed* this stage doesn't make it settled; only an explicit Confirmed status does that.

## Step 7 — Produce the artefacts

**Research repository — always.** Save or update `research-repository.md`. Structure in `references/research-repository-template.md`. Section order is fixed: Hypothesis Validation Map first (what downstream stages scan first), then Additional Insights, Source Log, and Changelog last.

Living-document mechanics per `conventions.md` §3 — stable filename, `Last Updated` refreshed every time, changed insights overwritten in place with one slim Changelog line, never stale versions interleaved in the body.

**HTML findings deck — via a fresh invocation of `brand-artefacts`.** That skill owns the brand tokens, layout, slide sequence, badge and confidence components. Don't specify styling here — and don't reuse tokens from whatever `brand-artefacts` produced at Intake; invoke it again so it re-reads `brand-tokens.md` for this deck rather than working from what it returned last time.

Pass it: the repository content, the sub-brand, and the design output target(s) so it can order and weight the insight slides. **Regenerate the deck on every repository update** — it's a live artefact that should never drift from the repository, stable filename, overwritten each time.

Every insight, badge and confidence label in the deck must match the repository exactly. The deck is a rendering of it, not an independently drafted summary.

Record both artefacts in the Artefact Registry in `_workflow-state.md`.

## Handoff

Evidence is done when: every Brief hypothesis is addressed as Confirmed, Revised or Still Unvalidated with none silently dropped; every insight carries a source and a confidence label; **Round 2 was actually run — either real triggers were surfaced to the human and resolved or waived by them, or the human was explicitly told none were found**; **`leisure-research-insights` was actually invoked for any Confluence, Jira, Miro or FullStory source this stage touched — not bypassed in favour of calling those tools directly, and not left undeclared**; the discover-approve loop was followed for any secondary artefacts; and the repository and deck are saved and in sync.

**Round 2 is not optional and cannot be inferred as complete from the repository alone.** If you can't point to the moment the human was asked (or the moment they were told there was nothing to ask), it didn't happen — go back to Step 5 before declaring Evidence done.

**Delegation is not optional either, and the same test applies.** If you can't point to the moment `leisure-research-insights` was invoked, or the moment the human was told it was unavailable and why, it didn't happen — reading Confluence, Jira, Miro or FullStory directly without either of those moments is a gap to log, not a stage to hand off.

Then give the human a table — what's confirmed, what's revised, what's still unvalidated, and what net-new insights emerged that weren't in the Brief. Call out anything thin, and say what research would firm it up. That table, not the files, is what Analyse-Explore actually consumes.

**If any source category was unreachable this run, state the confidence ceiling as its own line, not folded into the table or left as reasoning the human has to infer:**

> "Confidence ceiling: [High / Medium] this run, because [n] source category/categories were unreachable — [name them]."

This is required whenever Step 4 logged a gap. Triangulation-driven reasoning about why confidence tops out lower than usual is only useful if the human actually reads it — a repository that quietly has no High labels says the same thing far less clearly than this sentence does.

## Bundled resources

- `references/source-elicitation-prompts.md` — Round 1 and Round 2 prompt wording, and the discover-approve loop script.
- `references/research-repository-template.md` — the canonical repository structure, edited in place on every update.
