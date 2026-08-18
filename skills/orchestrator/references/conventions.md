# Product Velocity — Shared Conventions

The rules that apply across every stage of the plugin. This file is the single source of truth: the orchestrator reads it at session start, and every stage skill reads it too. Stage skills deliberately do **not** restate these rules — if you find a stage repeating something here, that's drift worth flagging.

If a stage skill contradicts this file, this file wins.

---

## 1. Language

All generated content is **English (Australian)**: "colour", "realise", "organisation", "prioritise". The audience for every artefact is Australian English speakers. This applies to files, decks, Confluence pages and chat responses alike, not just the formal deliverables.

Dates in documents are `dd/MM/YYYY`.

**Plain language, Grade 6 reading level, by default.** Chat responses, every markdown document, and every rendered deck or one-pager are written so a Year 6 reader could follow them: short sentences, one idea per sentence, everyday words instead of jargon, active voice. This is the default register to draft in the first time, not a simplifying pass applied afterwards.

- **Short, everyday words over long ones** — "use" not "utilise", "help" not "facilitate", "show" not "demonstrate", "start" not "commence".
- **Short sentences over long ones.** If a sentence needs a semicolon or several commas to hold together, split it into two.
- **Explain a term the first time it appears**, in the same sentence, rather than assuming the reader already knows it — e.g. "WCAG 2.1 AA (the accessibility standard we're building to)".
- **Complexity is earned, not default.** State a precise idea — a statistic, a named methodology, a confidence rating — precisely, even if that costs a harder word. Reach for the plain word first; keep the complex one only when the plain one would lose the point.

**This changes how something is said, never what is said.** Plain language governs framing and explanation. It does not touch the evidence itself:

- Quotes, figures, dates, sample sizes and names stay exactly as sourced — see §4. Simplifying a direct quote is fabrication with extra steps.
- Confidence labels (`High` / `Medium` / `Low`), hypothesis tags (`(hypothesis)`), and status words (`Confirmed`, `Still Unvalidated`, `Deferred`) are fixed vocabulary. Keep them exactly as defined; don't soften them into something friendlier-sounding.
- Required technical terms (WCAG 2.1 AA, P0/P1, a named research method) stay as-is once introduced. Plain language means explaining a term, not replacing it with something vaguer.

**Don't invent the "why."** A confident explanation for a rule, a finding, a design choice or a convention reads to a stakeholder exactly like a documented fact — even when the reasoning behind it is a guess. This is a different failure from the ones §4 already covers: those are about inventing *what* was found; this is about inventing *why* something is true, why a rule exists, or why a decision was made.

- **A plausible reason is not a documented reason.** If you're about to write "this happens because X" or "the rule exists to prevent Y," check whether X or Y is actually stated somewhere — the source material, the Project Brief, a named convention in this file — or whether it's your own inference filling a gap. Only the first is a fact.
- **When the real reason isn't written down anywhere, say so first**, then offer your own reasoning clearly labelled as a guess — "the docs don't say why; my best read is…" — never folded in as if it were the settled explanation. This extends §4's "flag your own inference" rule from research synthesis to any explanatory sentence, in any stage's output, including this file.
- **This matters most in anything that might reach an executive.** A stakeholder rarely checks a "because" clause against its source — it's the line most likely to be read, trusted and repeated exactly as written. An invented rationale that ships in a Design Brief or an executive summary is fabrication with extra steps, the same as an invented figure, and does more damage for being harder to spot.

**Visual space between ideas.** A wall of text is as hard to read as a wall of jargon, so break content up rather than running it together.

- **One idea per paragraph.** When a paragraph is doing two jobs, split it into two.
- **Short paragraphs, most of the time 2–4 sentences**, with a blank line between them — in chat and in every generated markdown file.
- **Use headings and bullet lists to carry structure**, rather than one continuous block of prose holding an entire section together.
- Applies everywhere content is drafted: chat responses, and every markdown artefact (`project-brief.md`, `research-repository.md`, `opportunities-analysis.md`, `design-brief.md`). Decks and one-pagers already enforce this at the layout level (one idea per slide, a fixed page container) via `brand-artefacts` — this rule is what makes sure the source document isn't a wall of text before it ever reaches that stage.

---

## 2. Question format

Default to the button-based question tool (`ask_user_input`) for questions the workflow asks. It's faster for the human than typing, especially on mobile.

Two constraints shape everything: **maximum 4 options per question**, and **no native free-text field**. A button label is only ever a label — if the real answer isn't an option, the human types a reply instead, and that's fine. Don't add an "Other" button that does nothing.

**The round rule.** Decide the format once per round, before asking anything in it:

- **6 or fewer questions** → ask them one at a time as button questions, in sequence. Say up front roughly how many are coming.
- **More than 6** → skip buttons entirely for that round and present all of them as a single numbered list in chat text, so the human can answer inline ("1. skip, 2. I have context — see below, 3. mark unvalidated").

Never start a round with buttons and switch partway through — the human loses track of what they've answered.

**Treat "I can explain" / "I have context" style answers as a prompt to ask a plain follow-up**, not as a complete answer.

**Ask in sections, not fields.** When running an interview (e.g. the Intake fallback), ask all the essential fields in a section together, wait, then move on. A twenty-question interrogation up front kills momentum before any artefact exists.

**Accept "Unknown / TBD" as a real answer.** Record it as such. Never fabricate a plausible-sounding value to fill a gap — a document that visibly says "not yet known" is more useful than one that invents a number.

---

## 3. Living documents

Every canonical artefact is a living document, not a dated snapshot.

- **Stable filenames.** Never version or date a filename (`research-repository.md`, not `research-repository-v3-270726.md`).
- **`Last Updated: dd/MM/YYYY`** near the top of every generated markdown file, updated every time the file is touched.
- **Overwrite in place.** When new evidence changes an existing entry, edit that entry. Do not leave the old version above or below it "for reference".
- **The Changelog is the only place history lives.** One slim line per change, most recent first, with a source reference: `27/07/2026 — Insight "Upsell timing" revised: was [old], evidence now shows [new]. See [source].`
- **Rendered artefacts regenerate.** A deck or one-pager is a rendering of its source document, never an independently drafted summary. When the source changes, regenerate the rendering so the two can't drift. If a figure appears in a deck but not in the source document, that's a bug, not a flourish.

---

## 4. Anti-fabrication and labelling

This is the discipline the whole plugin rests on. The value of a fast-generated brief collapses the moment a stakeholder finds an invented number in it.

- **Never invent a figure, quote, sample size, date, name or finding** that isn't explicitly present in a source. Not for polish, not to complete a sentence.
- **Synthesis is not a finding.** If a source implies something without stating it, label it as synthesis.
- **Preserve `(hypothesis)` labels verbatim.** Anything unvalidated stays tagged as unvalidated, all the way through, no matter how much tidier the document it now sits in. A hypothesis being *discussed* at a later stage doesn't make it settled.
- **Every insight carries a source and a confidence label:**
  - **High** — triangulated across multiple independent sources
  - **Medium** — single strong source
  - **Low** — indicative only, thin evidence
- **Confidence labelling replaces source-count gating.** Don't refuse to record a single-source insight — record it and label it Low. Early-stage evidence is often thin; that's a normal starting point, not a reason to withhold a finding or to inflate it.
- **"Still Unvalidated" is a legitimate, permanent-until-changed status.** Don't manufacture a verdict to avoid an awkward gap.
- **Where attitudinal and behavioural data diverge, say so.** Divergence between what people say and what they do is itself a finding, not a problem to reconcile away.
- **Flag your own inference.** After drafting, tell the human which parts are direct transcription from a source and which are your synthesis. They can't audit that from the document alone.
- **Thin evidence is an opportunity, not an embarrassment.** Naming a weakly-evidenced insight tells the designer exactly what research to commission next.

---

## 5. Write discipline — locate → verify → write → verify

Applies to **every** write target, local file or remote API. A save that reports success without being checked carries the same risk either way.

**Before writing to an existing artefact:**

1. **Locate** it using the path or URL in the Artefact Registry (`_workflow-state.md`).
2. **Verify** it's still there and is recognisably the artefact the registry claims — for a Confluence page, that it exists, the title matches, and it's in the recorded space; for a local file, that the path resolves to a file of roughly the expected shape, not just that *something* exists there.
3. **If it has moved, been renamed, or can't be found**: stop before writing. Don't guess a new location, don't create a replacement in its place, don't search blindly for a near-match. Tell the human what the registry says versus what you found, ask how to proceed, and once resolved, correct the registry so the next stage doesn't hit the same drift.

**After writing:**

4. **Verify the write itself.** Read the artefact back and confirm the content actually reflects the change — not merely that the call returned without an error.

**Failing loudly.** If a write fails or can't be verified, follow §9 below: name the specific step that failed, give the real error, suggest the likely cause, don't retry silently, preserve the content somewhere the human can reach it, and point them at the right contact. Report the honest status — "attempted, unverified" or "failed" — never "created".

---

## 6. Files, paths and environment

**Primary environment: Claude Desktop (Cowork).** Chat support is planned but parked — if the workflow is running somewhere without a connected folder, say so and ask the human where they want output before creating anything.

**The root is the connected folder, not a folder this plugin invents.** The human establishes it by connecting or selecting a folder for the session — that's the whole action. Never create an intermediate folder (for instance, one literally named `projects`) to hold projects inside it; that's a layer the human didn't ask for.

**Project folder:** `<connected-root>/<project-slug>/` — a direct child of the connected root. Slug is lowercase, hyphenated, derived from the project name, no dates.

**Canonical filenames** (stable, overwritten in place):

| File | Owner | Contents |
|---|---|---|
| `_workflow-state.md` | Orchestrator | Stage status, Artefact Registry, gaps and overrides |
| `project-brief.md` | Stage 1, updated by Stage 3 | The canonical Project Brief |
| `research-repository.md` | Stage 2 | Hypothesis validation, insights, source log |
| `opportunities-analysis.md` | Stage 3 | Recommendation options and decision log |
| `design-brief.md` | Stage 3, if "Human designer" or "Both" chosen | Build instructions for a human designer — rationale, room to interpret |
| `design-prompt.md` | Stage 3, if "AI design tool" or "Both" chosen | Build instructions for an AI design tool — precise, unambiguous, tokens inlined |

**Rendered artefact filenames — human-readable, artefact type first.** These are the files a stakeholder sees listed in a folder, not files the workflow greps by name, so they're named for scanning, not for the machine: `<Artefact type> - <Project Name>.html` — the artefact type first, then the project's actual name exactly as it appears in the Brief's heading (not the slug: title case, spaces, no hyphens standing in for them).

| Artefact | Filename |
|---|---|
| Project Brief deck | `Project Brief - <Project Name>.html` |
| One-page executive summary | `Executive Summary - <Project Name>.html` |
| Evidence findings deck | `Evidence Findings - <Project Name>.html` |

Still governed by the living-document rules in §3 — stable, overwritten in place when regenerated. Regenerating a deck never changes its filename and never adds a date or version suffix, even though the naming pattern here differs from the canonical markdown table above.

Rendered artefacts (HTML decks, HTML one-pagers) are produced by `brand-artefacts`, use stable filenames, and are recorded in the Artefact Registry.

**Never write outside the project folder** without asking. If the folder isn't established yet, that's the orchestrator's job — go back to it rather than picking a location.

**Fresh run vs update** is determined from `_workflow-state.md`, not by sniffing for filenames. If the state file and the folder contents disagree, ask; don't assume either way.

---

## 7. Confluence formatting

- Structure with **Heading 1, Heading 2 and Heading 3** only. All other text uses **Paragraph** style. Don't reach for exotic macros or panels — they render inconsistently and make later programmatic updates fragile.
- Convert markdown to whatever format the Atlassian tool actually expects; check its schema at call time rather than assuming.
- Apply the create-then-verify discipline in section 5 without exception. A Confluence page is the artefact most likely to be shared with stakeholders and least likely to be checked by the designer.
- Once confirmed, record the **page ID, space key and URL** in the Artefact Registry. Later stages update that page rather than creating a second one — and apply the same verification every time, because a page found and edited correctly once doesn't guarantee the next update lands.

---

## 8. Rendered artefacts

All visual output — HTML slide decks, HTML one-pagers, and anything similar added later — is produced through the **`brand-artefacts`** skill. It owns brand colours, typography, layout, safe zones and the structure of each artefact type.

No stage defines its own styling, and no stage sources brand values from anywhere else. Earlier drafts of this workflow pulled colours from `takeflight-design-system` and `fcb-leisure-leadership-pptx`; both are now out of scope for this plugin. If you find a stage referencing them, that's stale content to remove.

The sub-brand for a project is recorded once in `_workflow-state.md`. Read it; don't re-ask.

---

## 9. Connector availability and escalation

This is the shared fallback for **any** connector-backed tool — Atlassian (Confluence, Jira), Miro, or anything added later. Every stage and the orchestrator's pre-flight both follow it; neither restates it.

**Check fresh, every time.** Connector availability can change session to session, and a skill being installed doesn't mean a connector is currently reachable. Base "available" or "unavailable" on an actual attempted call made *this session* — never on what a previous session found, and never on an assumption.

**A connector still initialising is not a connector that's down.** Some connectors report as "still connecting" for a few seconds after a session starts, rather than failing outright. If that's what's reported, wait briefly and check again before concluding it's unavailable. Reporting a mid-connection tool as broken sends the human off to fix something that was never wrong — this is the single most common way a false "not connected" reaches a designer, so treat one failed check as inconclusive, not final.

**Never report unavailability without also giving the human something to do about it.** Every time a connector is reported as unavailable or a call to it fails, the response carries both halves, in the same message:

1. **What specifically failed** — name the connector and the action, not "something went wrong."
2. **What the human can check or do right now**, before any contact gets named. Default suggestion for a connector-level failure: *"Check Settings → Connectors and confirm the [Atlassian / Miro] connection is active."* If the human says they've checked and it looks fine, say so plainly rather than repeating the same suggestion — a connection that's active but still can't be reached is very often a **permissions or scope issue** (connected, but without access to the specific space or board this project needs), not a dead connection, and that distinction changes what the human should check next. Offer to re-check once they've looked.

**Reporting a failure is not the same as stopping.** State what's affected and what isn't, and keep the workflow moving on whatever isn't blocked — see the degraded-not-blocked handling in the orchestrator's pre-flight for the concrete example.

**Escalate to a named contact only after self-serve steps have been offered and haven't resolved it.** Read `contact-list.md` and direct the human to the contact listed there; don't hard-code names from memory. Escalating first, before the human has had a chance to check their own connector settings, wastes a step they could have resolved themselves in ten seconds.

**The contact name belongs inside the message itself, not in a separate instruction to remember it.** Use this shape for any degraded-source or escalation message:

> "[Source categories / connector] aren't reachable this session because [reason]. [What still works]. Contact **[name from contact-list.md]** if you want this connected."

Treat every bracket as required. A message that reports unavailability but never fills in the contact bracket is incomplete, not just brief — reading `contact-list.md` and then not naming what's in it satisfies the letter of "check the contact list" while missing the entire point of checking it.

---

## 10. Persona roles

`roles` is the single source of truth for the persona lenses that sharpen judgement-heavy sections across every stage. Each stage skill names which role(s) apply at which of its own steps — that mapping lives in the stage skill, not here.

**Whether a named role actually applies, and in which mode, is defined entirely in `skills/roles/SKILL.md` — read it before applying any role**, the same way `brand-artefacts` is read fresh before any rendered artefact rather than worked from memory. Don't restate or re-derive its rules here or in a stage skill. If `roles/SKILL.md` and a stage skill's own text ever disagree about how a role engages, `roles/SKILL.md` wins for roles specifically, the same way this file wins over a stage skill for everything else.
