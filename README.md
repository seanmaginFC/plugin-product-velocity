# Product Velocity

An evidence-led UX design workflow for Claude. It takes a stakeholder kickoff through to a Design Brief, producing the documents designers would otherwise write by hand — and keeping the seams visible while it does.

**Status: v0.1.0 — beta.** Stage 4 (Design) is not included; the Design Brief is the current end of the workflow.

## Why this exists

The documents that communicate design work to the business — briefs, research repositories, findings decks, one-pagers — are slow to write and easy to write dishonestly. Not deliberately: a confident-sounding document simply outruns the evidence behind it, and nobody notices until a stakeholder quotes a number back that nobody ever measured.

Product Velocity speeds up the writing and refuses the dishonesty. Every stage distinguishes what is confirmed, what is a hypothesis, and what nobody has checked yet — and carries that distinction into the artefacts stakeholders actually read.

## Stages

| # | Stage | Input | Output |
|---|---|---|---|
| 1 | **Intake** | Kickoff notes, or a chat interview | `project-brief.md` |
| 2 | **Evidence** | The Project Brief | `research-repository.md` |
| 3 | **Analyse-Explore** | Brief + repository | `opportunities-analysis.md`, `design-brief.md` and/or `design-prompt.md` |

Plus three supporting skills:

- **`orchestrator`** — the entry point. Owns project setup, workflow state, dependency checks, stage routing and gates. Always runs first.
- **`brand-artefacts`** — the single source of truth for every rendered artefact: brand colour, typography, logos, layout, print behaviour and accessibility.
- **`roles`** — persona lenses that sharpen judgement-heavy sections at each stage, improving thinking and planning for responses and wrting content for artefacts. Applicable once a role is promoted from Draft to Active.

## Install

**In Cowork:** open the Cowork tab, then Customize → Plugins → **+** → upload the plugin file, or add a marketplace by repository URL.

**In Claude Code:** `claude plugin install product-velocity@<marketplace>`

After installing, start with a plain description of what you want. You don't need to name a skill:

> I've just come out of a kickoff for a checkout upsell project. Here are my notes — can you turn this into a project brief?

The orchestrator picks it up, sets up the project, and routes to Intake.

## Requirements

| Dependency | Needed for | If missing |
|---|---|---|
| `leisure-research-insights` skill | Stage 2 — Confluence, Jira, Miro, FullStory retrieval | Stage 2 runs **degraded**: those four source types are unavailable, everything else works. Contact the person named in `skills/orchestrator/references/contact-list.md` |
| Atlassian connector | Confluence pages, Jira sources | Confluence output unavailable; markdown unaffected |
| Miro connector | Miro board sources | Not blocking; the gap is logged |

The orchestrator checks these once at session start rather than letting a stage discover a gap mid-flow.

## Where things are written

The project folder is a direct child of whatever folder you've connected or selected for the session — the plugin never invents an intermediate folder (like one literally named `projects`) to hold it. Connecting a folder is how you choose the root; the project folder goes straight inside it:

```
<the folder you connected>/<project-slug>/
├── _workflow-state.md          orchestrator-owned: stage status, artefact registry, gaps
├── project-brief.md            Stage 1, updated by Stage 3
├── research-repository.md      Stage 2
├── opportunities-analysis.md   Stage 3
├── design-brief.md             Stage 3, if "Human designer" or "Both" chosen
└── design-prompt.md            Stage 3, if "AI design tool" or "Both" chosen
```

All are living documents: stable filenames, overwritten in place, history in a Changelog. Rendered artefacts (HTML decks, one-pagers) are recorded in the Artefact Registry.

## Configuring it for your team

Two files are meant to be edited. Neither contains logic, so changing them can't break the workflow:

- **`skills/orchestrator/references/contact-list.md`** — who to contact for a missing dependency or an error.
- **`skills/brand-artefacts/references/brand-tokens.md`** — brand colour, typography and logos for FC, TA, W360 and TC.

**A caution on brand tokens.** Each colour carries a *usage class* (`text-safe`, `heading-only`, `fill`, `accent-only`) derived from measured WCAG contrast against that brand's backgrounds. **If you change a hex, its class is no longer true.** Re-check the changed value, or ask Claude to recalculate it. Three of the four brands already have a token whose supplied role doesn't match what it can safely do — the classes are what stop that reaching a stakeholder deck.

## Known limitations in v0.1.0

- **Cowork only.** Chat support is planned; the stages assume a project folder.
- **Logo SVGs are Figma exports with non-unique clip-path IDs.** Each inlined copy needs its `id`/`url(#...)` references suffixed uniquely per slide, or duplicate IDs across a deck can cause a logo to render with paths clipped incorrectly. See "Duplicate-ID hardening" in `brand-tokens.md`.
- **Fonts load from the Google Fonts CDN.** A deck opened offline, or on a network that blocks the CDN, falls back to the stacks in `brand-tokens.md`. Embedding is costed at roughly 90–110 KB per deck if this becomes a problem.
- **Confluence writes are not yet exercised end to end.** Reads are tested; the first live write should be treated as a test, and the create-then-verify discipline applied especially carefully.
- **16:9 print-to-PDF is untested.** If slides don't export at the right page size, the fix is in `assets/deck-template.html`.

## For maintainers

**Run checks locally before committing.** `scripts/check.sh` runs the same two checks CI runs — `claude plugin validate . --strict` (structure) and `scripts/lint_plugin.py` (this repo's own conventions: cross-references resolve, no stage restates a rule that lives in `conventions.md`, role Status lines are well-formed, no stray `[TBD]` in an Active role). Run it any time with:

```bash
scripts/check.sh
```

To have it run automatically before every commit, opt in once per clone:

```bash
git config core.hooksPath .githooks
```

CI (`.github/workflows/plugin-checks.yml`) runs the identical checks on every push and PR — the backstop for anyone who skips the hook, not the primary way to find out something's broken.

**Versioning.** `version` is set in `plugin.json`, which means **you must bump it for teammates to receive changes** — pushing commits alone won't do it, because Claude sees the same version string and keeps the cached copy. While iterating rapidly, either remove the `version` field (updates then follow the git commit SHA) or bump the patch number on each change. Local and skills-directory installs pick up `SKILL.md` edits immediately, so version only matters once you're distributing.

**Cross-skill references** use `${CLAUDE_PLUGIN_ROOT}` because installed plugins can't reference files outside their own directory — relative traversal like `../orchestrator/` breaks after install. Keep that form when adding references.

**Architecture note.** Shared rules live in one place: `skills/orchestrator/references/conventions.md`. Every stage reads it and none restate it. If you find a stage duplicating a rule from that file, that's drift — remove the copy rather than maintaining two.
