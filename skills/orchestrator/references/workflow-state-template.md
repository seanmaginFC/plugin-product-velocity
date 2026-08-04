# Workflow State Template

Copy this structure to `<connected-root>/<project-slug>/_workflow-state.md` when a project starts — a direct child of the connected folder, never a `projects` folder invented along the way. Orchestrator-owned. Stage skills update only their own rows (see the orchestrator's State file ownership section).

Keep it short. This file is read at the start of every session, so it earns its place by being scannable — it records *where things are*, not what they say.

---

```markdown
# Workflow State — [Project Name]

Slug: [project-slug]
Created: dd/MM/YYYY
Last Updated: dd/MM/YYYY
Sub-brand: [FC / TA / W360 / TC]
Design output target(s): [one or more of: Customer journey map / UI screen-feature design /
Service blueprint / Content-communications design / other — as recorded in Stage 2. List all
selected, comma-separated, even if there's only one — Stage 3 reads this as a list, not a
single value. "Not yet set" until then.]
Environment: [Cowork / other]

---

## Stage Status

| Stage | Status | Completed | Notes |
|---|---|---|---|
| 1 — Intake | Not started / In progress / Complete / Complete (override) | dd/MM/YYYY | |
| 2 — Evidence | Not started | | |
| 3 — Analyse-Explore | Not started | | |

"Complete (override)" means the stage's exit gate was not fully met and the human chose to
proceed — the reason is recorded under Open Gaps & Overrides below.

---

## Artefact Registry

The canonical record of what exists and where. One row per artefact **actually produced** —
never pre-populate rows for artefacts that were offered but not chosen, or a later stage will
try to update something that doesn't exist.

| Artefact | Type | Location / URL | Produced by | Sub-brand | Last regenerated |
|---|---|---|---|---|---|
| Project Brief | Markdown | project-brief.md | Stage 1 | n/a | dd/MM/YYYY |
| Project Brief deck | HTML deck | `Project Brief - [Project Name].html` | Stage 1 | FC / TA / W360 / TC | dd/MM/YYYY |

For Confluence rows, record the **page ID, space key and full URL** — a title alone isn't
enough to locate a page reliably.

For rendered artefacts (decks, one-pagers), record the sub-brand used, so a later stage
restyles consistently rather than re-asking or guessing. Filenames follow `conventions.md`
§6 — `<Artefact type> - <Project Name>.html`, project name in full, never the slug.

---

## Open Gaps & Overrides

Carried forward into every later stage. A recommendation built on a Brief with no success
metric needs to say so.

| Date | Stage | Gap or override | Reason given |
|---|---|---|---|
| dd/MM/YYYY | 1 | e.g. P0 "success metric" unanswered — proceeded on designer override | e.g. "analytics owner on leave, will backfill" / "no reason given" |

---

## Dependency Check

Result of the orchestrator's pre-flight, per session. Based on an actual check made this
session — never carried forward from a previous one.

| Date | leisure-research-insights | Atlassian | Miro | Notes |
|---|---|---|---|---|
| dd/MM/YYYY | Assumed present / Confirmed missing — Stage 2 degraded | Connected / Not connected (retried once) | Connected / Not connected (retried once) | |

Skill presence can't be verified in advance, only at the point of use — record "Assumed
present" until a delegation attempt proves otherwise, then "Confirmed missing — Stage 2
degraded", noting which source categories were unavailable and the contact the human was
given. Degraded means Confluence, Jira, Miro and FullStory couldn't be read; sources Stage 2
reads directly are unaffected.

For Atlassian and Miro, "Not connected" means the check was retried once after an initial
failure (per `conventions.md` §9) and still didn't succeed — not a single failed attempt.
Note in this row whether the human was already told what to check (Settings → Connectors)
before this was recorded, so the next session doesn't repeat advice already given.

---

## Changelog

Append-only, most recent first. One line per session or material change.

- dd/MM/YYYY — [what changed]
```
