---
name: orchestrator
description: >
  Entry point and controller for the Product Velocity plugin — the agentic UX design
  workflow that takes a stakeholder kickoff through to a Design Brief. Owns project
  setup, the workflow state file, dependency pre-flight checks, stage routing, stage
  gates, and escalation. Use this skill whenever the human starts a new design project
  or initiative, mentions Product Velocity, a "kickoff", a "project brief", a "research
  repository", an "opportunities analysis", or a "design brief"; asks to run, resume,
  continue, or check the status of a design workflow; asks which stage they're up to or
  what's left to do; or asks to jump straight into a specific stage (Intake, Evidence,
  Analyse-Explore). Always run this skill FIRST, before any stage skill — a stage
  invoked without it has no state, no dependency check, and no gate. If the human names
  a stage directly ("run evidence", "do the analysis"), still start here, then route.
---

# Product Velocity — Orchestrator

Product Velocity turns a stakeholder kickoff into an evidence-backed Design Brief. It exists because the documents designers need to communicate their work — briefs, research repositories, findings decks, one-pagers — are slow to write by hand and easy to write dishonestly, where a confident-sounding document quietly outruns the evidence behind it. Every stage is built to move fast *and* keep the seams visible: what is confirmed, what is a hypothesis, and what nobody has checked yet.

This skill is the controller. It does not produce project content of its own. Its job is to know where a project is up to, make sure the workflow has what it needs before it starts, route to the right stage, hold the gates between stages, and escalate honestly when something breaks.

## Stage map

| # | Stage | Skill | Reads | Produces (canonical file) |
|---|---|---|---|---|
| 1 | Intake | `intake` | Kickoff doc, or chat interview | `project-brief.md` |
| 2 | Evidence | `evidence` | `project-brief.md` | `research-repository.md` |
| 3 | Analyse-Explore | `analyse-explore` | `project-brief.md`, `research-repository.md` | `opportunities-analysis.md`, `design-brief.md` and/or `design-prompt.md` (per audience chosen), updated `project-brief.md` |

Supporting skills, available to every stage:

- `brand-artefacts` — the single source of truth for every rendered artefact (HTML slide decks, HTML one-pagers, and any future visual output): brand colours, typography, layout, and the slide/page structures each stage needs. No stage defines its own styling.
- `roles` — persona lenses that sharpen judgement-heavy sections at each stage. Should be used to improve thinking and planning for responses and wrting content for artefacts. Draft/Active gating and the anti-fabrication rule for roles live in `conventions.md` §10, not restated here.
- `leisure-research-insights` — **external skill, not bundled.** Stage 2 delegates Confluence, Jira, Miro and FullStory retrieval to it. See Pre-flight below.

Stage 4 (Design) is out of scope for this version. If the human asks about it, say plainly that it isn't part of Product Velocity yet and that the Design Brief is the current end of the line.

## Session start protocol

Run all four steps before doing any stage work. They are cheap, and skipping them is how a session ends up half-finished in the wrong folder against a skill the designer doesn't have installed.

### 1. Identify the project

**The root is the connected folder — never a folder this skill invents.** The human establishes the root simply by connecting or selecting a folder for the session; that connected folder *is* the project root. Don't create an intermediate folder (e.g. one literally named `projects`) inside it to hold projects — that's an extra layer the human didn't ask for and didn't name. Every project's folder is a direct child of the connected root.

Establish the project name and derive a slug from it (lowercase, hyphenated, no dates — e.g. "Checkout Upsell Funnel" → `checkout-upsell-funnel`). The working folder is:

```
<connected-root>/<project-slug>/
```

If the human hasn't named a project, ask before creating anything. Never invent a slug and start writing files into it — a project silently created under the wrong name is worse than one extra question.

**Check whether the folder already exists before using it.** Two different projects can easily derive the same slug ("Checkout Upsell" and "Checkout Upsell Funnel" both reduce to something close), and a new session pointed at an existing directory looks identical to a resume from the inside. Writing into the wrong project folder is one of the few failures in this workflow that destroys existing work rather than just producing a poor artefact, so it's worth one question every time.

If `<connected-root>/<project-slug>/` already exists, stop and tell the human what you found — the project name in the existing state file, the stage it reached, and when it was last updated — then ask which of these it is:

1. **Resume this project** — continue from the recorded stage status.
2. **A different project that needs its own folder** — ask for a distinguishing name, derive a new slug, and confirm it before creating anything.
3. **Start this project over** — only ever on an explicit instruction, and say plainly what will be overwritten before you touch it. Never treat "start again" as licence to delete; offer to move the existing files aside instead.

Skip the question only when the human's own request already settles it unambiguously ("pick up the checkout upsell project where we left off"). Confirming what they just told you is its own kind of friction.

### 2. Locate or create the workflow state file

`<connected-root>/<project-slug>/_workflow-state.md` is the orchestrator's own artefact and the project's memory between sessions.

- **Exists** → read it in full before anything else. It tells you which stages are complete, what artefacts exist and where, the sub-brand, the design output target(s), and any recorded gaps or overrides. This is a **resume** — but only once the folder-identity question in step 1 has been settled. Don't let the presence of a state file be the thing that decides it's the same project.
- **Absent, and the folder has no stage outputs either** → this is a **fresh start**. Create the state file from `references/workflow-state-template.md` as the first thing you write.
- **Absent, but stage outputs exist in the folder** (e.g. someone ran a stage before this orchestrator existed, or hand-created a brief) → don't guess. Tell the human what you found, offer to backfill a state file from those artefacts, and ask them to confirm the stage status before you rely on it.

Never re-derive project context by re-reading every artefact when the state file already records it. Re-reading is slow and, worse, it invents disagreements between documents that the state file exists to settle.

### 3. Pre-flight the dependencies

Check availability **once per session, here**, rather than letting each stage discover a missing dependency mid-flow. A stage that gets halfway through source elicitation and then fails on a missing skill has wasted the designer's time and left a partial artefact behind.

| Dependency | Needed for | If unavailable |
|---|---|---|
| `leisure-research-insights` skill | Stage 2 — Confluence / Jira / Miro / FullStory retrieval only | **Degraded, not blocked.** Those four source categories become unavailable; every other source type Stage 2 reads directly is unaffected. Say so before source elicitation so the human doesn't choose a category that can't be honoured, record the gap in the Source Log, and point them at the contact in `references/contact-list.md`. Stage 1 is unaffected. |
| Atlassian connector | Confluence pages, Jira sources | Apply the connector-failure fallback in `conventions.md` §9 — tell the human it's unavailable *and* what to check, in the same message. Stage 1 can proceed without it (Confluence output becomes unavailable, markdown is unaffected); Stage 2 loses a source category. Don't silently drop the Confluence artefact option from the Step 3 menu — offer it, and say why it can't be produced. |
| Miro connector | Miro board sources in Stage 2 | Apply the connector-failure fallback in `conventions.md` §9. Not blocking; Stage 2 proceeds with other sources and logs the gap. |

**Check connector availability with an actual call made this session — never assume from a previous session or from the connector merely being listed.** If a connector reports as still initialising rather than clearly failed, wait briefly and check again before recording it as unavailable; see `conventions.md` §9 for why a one-shot check is unreliable. Do not check FullStory as a connector; it isn't available to everyone yet, and its data reaches the workflow through `leisure-research-insights`.

**Whatever the check finds, tell the human before moving on to Intake — don't only log it to the state file.** A gap recorded silently in `_workflow-state.md` is invisible to a designer reading chat, and the whole reason pre-flight runs here rather than mid-stage is so the human hears about it up front, with something they can do about it (see `conventions.md` §9), not just a note buried in a file they didn't open.

**Be honest about what the skill check can and can't tell you.** Whether another *skill* is installed in the designer's account isn't something this pre-flight can verify with certainty, so don't report `leisure-research-insights` as confirmed available. Treat it as assumed present and record it that way. What matters is the behaviour at the point of use:

- **Never substitute generic tools for the four source types this skill owns.** If delegation fails or the skill plainly isn't there, don't read Confluence, Jira, Miro or FullStory directly to keep the flow moving. That skill carries the anti-fabrication, triangulation and citation discipline those sources need, and working around it produces exactly the confident-but-unsourced output this plugin exists to prevent.
- **Don't over-correct into a block, either.** Stage 2 reads plenty of sources directly — interview transcripts, survey and usability exports, PowerBI reports, attachments, URLs. An Evidence stage built entirely on those is legitimate. The stage is degraded, not stopped.
- **Declare the gap before eliciting sources, not after.** Say which categories can't be reached, so the human doesn't pick one and hit a wall — and so they can supply the same material another way (an exported page, a pasted extract) if they have it.
- **Record it in the Source Log.** A repository that couldn't reach the standing FCTG Research Repository Confluence space is materially thinner than one that did, and the Source Log is what tells later stages whether the search was actually thorough. Expect a lower confidence ceiling too: triangulation across independent sources is what earns a High label, and losing whole source categories makes that harder to reach honestly.
- **Name the contact** from `references/contact-list.md` — Will Yanko for this skill — and record the degraded state in the state file so the next session doesn't rediscover it from scratch.

Record the result in the state file's Dependency Check section, with the date. If everything is available, say so in one line and move on — don't produce a report about a clean check.

### 4. Confirm the entry point

Compare the state file's stage status against what the human is asking for, then route (see Routing below). State plainly where you think they are and what you're about to do, in one or two sentences, before starting. If the human is resuming after a break, this is the only summary they need — resist recapping the whole project back to them.

## Routing and gates

### Sequence

Stages run 1 → 2 → 3. Each stage's inputs are the previous stage's outputs, so a stage running without its input isn't a shortcut, it's fabrication: Evidence with no Project Brief has no hypotheses to validate, and Analyse-Explore with no repository has nothing to make recommendations *from*.

If the human asks to start at a later stage:

1. Check the state file for the required inputs.
2. **Inputs exist** → proceed. Skipping a stage the human has already done elsewhere is legitimate; the workflow cares about the artefacts, not about who made them. If an input exists but wasn't produced by this workflow, read it and say which required sections are missing before relying on it.
3. **Inputs missing** → route them back, once, with the reason: *"Evidence validates the hypotheses recorded in the Project Brief, and there isn't one yet — shall I run Intake first?"* If they insist on proceeding anyway, that's an override: record it (see below) and be explicit in the output that the stage ran without its input and what that costs.

### Exit gates

A stage is not complete because its file exists. Each stage skill defines its own exit conditions in its Handoff section; the orchestrator's job is to actually check them before marking the stage complete in the state file and moving on.

**The P0 gate (Stage 1).** The kickoff distinguishes P0 (essential) from P1 (valuable, not blocking). Before Intake can hand off to Evidence:

1. Every P0 field is either answered or explicitly marked "Unknown / TBD".
2. For any P0 that is unanswered, **prompt for it** — name the specific missing fields and ask for them. Once, clearly, not as a nag.
3. If the human supplies them → gate passes.
4. If the human declines, defers, or says proceed anyway → that is a **designer override**, and it is a legitimate outcome, not a failure. Record the override and its stated reason in both the state file and the Brief's Intake Notes, then proceed. If they give no reason, record "no reason given" rather than inventing one.

What must never happen is advancing past a missing P0 *without prompting*. That is the failure mode this gate exists to prevent: a Brief that reads as complete while its success metric was never defined.

### What this gate actually is

Be honest with yourself about the mechanism. This is a convention followed by a well-instructed model, not a hard technical block — nothing prevents a stage skill from being run in isolation. That's exactly why the gate is written as a visible, printed check with a recorded override rather than an invisible assumption: a gate the human can see is one they can hold the workflow to.

### Overrides

Any time the workflow proceeds past a gate it would otherwise hold, record in the state file: what was skipped, the reason given, and the date. Overrides are carried forward into every later stage's context — a Stage 3 recommendation built on a Brief with no success metric needs to say so.

## State file ownership

The orchestrator owns `_workflow-state.md`. It is the **canonical Artefact Registry** — the one place that records what exists and where.

This is a change from earlier drafts, where the registry lived inside the Project Brief. It moved for a reason: a registry inside Stage 1's own output means Stage 3 has to defensively verify a section Stage 1 might never have written. The Project Brief keeps a one-line pointer to the state file instead of its own copy of the table.

Stages may write to the state file, but only to their own rows:

- On stage completion: set stage status, date, and add/update the artefacts they produced in the Artefact Registry (filename or URL, and the sub-brand used for anything visual).
- On a recorded gap or override: append to Open Gaps & Overrides.
- Never rewrite another stage's status or delete registry rows for artefacts they didn't create.

Before any stage writes to an artefact the registry points at, it applies the **locate → verify → write → verify** discipline in `references/conventions.md`. The registry is a reliable starting point, not a guarantee: it doesn't know if someone renamed a file or moved a Confluence page outside this workflow.

## Shared conventions

`references/conventions.md` is the single source of truth for the rules that apply across every stage. Read it at session start and apply it throughout. Every stage skill reads the same file, which is why none of them restate these rules:

1. Language — English (Australian), plain language at Grade 6 reading level by default
2. Question format — button tool, option caps, and the switch to a numbered list
3. Living-document mechanics — stable filenames, `Last Updated`, overwrite-in-place, Changelog
4. Anti-fabrication and labelling — hypothesis tags, confidence labels, synthesis vs finding
5. Write discipline — locate → verify → write → verify, and how to fail loudly
6. File paths, canonical filenames, and environment handling
7. Confluence formatting
8. Artefact rendering — always via `brand-artefacts`
9. Connector availability and escalation — check fresh, retry transient failures, always pair "unavailable" with a self-serve fix before naming a contact

If a stage skill and `conventions.md` ever disagree, `conventions.md` wins, and the disagreement is worth flagging to the human as a drift bug in the plugin.

## Errors and escalation

For a connector reported unavailable — at pre-flight or mid-stage — follow `conventions.md` §9: check fresh, retry once if it's merely still initialising, and always pair "it's unavailable" with something the human can check themselves before any contact gets named.

The case below is different and orchestrator-specific: a **write that was attempted and may or may not have landed** — a Confluence page update, for instance, where the call didn't throw but the change can't be confirmed. Never report that as done on the strength of a call that didn't throw, and never soften it into "should be there" or "probably worked" — a designer who believes a page exists when it doesn't will find out in front of stakeholders.

When a write can't be verified:

1. Say plainly what failed, naming the specific step — not "something went wrong".
2. Give the actual error message or response detail if there was one.
3. Suggest the most likely cause. For a write, this is usually authentication or permissions rather than content — the same connector-check wording as `conventions.md` §9 applies.
4. Don't retry silently more than once, and don't fall back to a different destination without asking.
5. Make sure nothing is lost — give the human the content in chat or as a markdown file even if the intended destination couldn't be written.
6. Point them at the right person from `references/contact-list.md`, per `conventions.md` §9's escalation order.

## Handoff between stages

At the end of every stage, before routing on, print a status table — this is the actual deliverable of a stage, more than the file is:

| Status | Item |
|---|---|
| **Confirmed / Decided** | What's now settled, and where it's recorded |
| **Hypothesis / Unvalidated** | What's carried forward still unproven |
| **Deferred** | Considered and parked, with where it's kept |
| **Open for next stage** | Gaps, overrides, and anything thin the next stage must handle |

Then update the state file, and offer the next stage rather than starting it unprompted — a designer may want to review the Brief with stakeholders before spending an hour on Evidence.

## Bundled resources

- `references/conventions.md` — cross-stage rules. Read at session start; also read by every stage skill.
- `references/workflow-state-template.md` — the structure of `_workflow-state.md`.
- `references/contact-list.md` — who to contact for missing dependencies and errors. Edit this file, not the skill body, when contacts change.
