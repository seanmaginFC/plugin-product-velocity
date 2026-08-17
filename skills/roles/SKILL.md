---
name: roles
description: >
  Roles help to sharpen the judgement calls other Product Velocity stages make: what to draft, what to challenge, and what a section is still missing before it gets called done. 
  Use this skill whenever a stage is about to draft or finalise a judgement-heavy section in either an artefact of a chat summary. Use when a specialist's checklist would catch something a generic pass wouldn't. Also use when the human explicitly asks to "review this as a [role]", "check this like a [role] would", or names one of the roles directly. This skill does not produce project content on its own — it's a lens applied to content another stage is drafting or has already drafted, the same relationship `brand-artefacts` has to layout rather than content.
---

# Product Velocity — Persona Roles

Every stage in this plugin already asks *what does the evidence support*. Persona roles ask the second question a specialist in the room would ask: *is this good enough judgement, coming from someone who does this for a living?* A Business Analyst reads a requirements list differently from a Product Leader reading the same page. Both readings are worth having before an artefact reaches a stakeholder — this skill is where those readings live. Roles should provide perspective, while the stage itself uses these perspectives to decide what to draft, what to challenge, and what a section is still missing before it gets called done.

## Status

**This skill is scaffolding.** The role reference files below currently hold the template structure only — the substance (checklists, heuristics, voice) hasn't been authored yet. Until a role's file is filled in beyond its template placeholders:

- **Don't fabricate a checklist or voice on its behalf** from a generic idea of what a "Business Analyst" typically does. That produces confident-sounding advice with no actual grounding — the exact failure mode `conventions.md` §4 exists to prevent everywhere else in this plugin, and there's no reason a persona lens should be exempt from it.
- **If a stage would normally consult a role and its file is still a template, say so plainly and skip that lens** rather than improvising one silently. A missing lens is a visible gap, the same way a missing dependency is at pre-flight — not something to paper over.

## The roles

| Role | Primary stage(s) | Default focus |
|---|---|---|
| Product Leader | Intake, Analyse-Explore | Strategic framing, Executive Summary, Success Criteria, the case for funding |
| Business Analyst | Intake, Analyse-Explore | Requirements rigour, scope & constraints precision, Functional/Non-Functional Requirements |
| CX/UX Research | Evidence | Triangulation discipline, bias-checking, insight and confidence quality |
| Senior Product Designer | Intake, Evidence, Analyse-Explore | User-experience read on JTBD & Current State, experience implications of validated insights, recommendation mechanism quality, Design Brief/Prompt build-readiness |
| Delivery Lead | Intake, Analyse-Explore | Feasibility, dependencies, sequencing, risk realism |

This mapping is a starting point recorded here for convenience, not a constraint enforced anywhere in code — a role's own reference file is free to note it applies to an additional stage once it's actually written, and a stage skill should read the role file rather than trusting this table if the two ever disagree.

## How a stage applies a role, once a file is filled in

Two engagement modes, both legitimate, and a given role file should say which of these it supports (a role can support both):

- **Automatic lens.** Before presenting a judgement-heavy section as finished, the drafting stage silently runs the relevant role's checklist against its own draft and folds any catch into the draft — the same way a writer reads their own work back before sending it. This doesn't get narrated blow-by-blow in chat; it's a quality bar, not a performance.
- **On-demand review.** The human asks directly — "review the Functional Requirements as a Business Analyst would", "does this hold up from a Delivery Lead's point of view" — and the stage applies that role's checklist explicitly, reporting back what it caught as its own visible step, not folded silently into a redraft.

Which sections a role applies to, and whether it critiques or drafts in its own voice, is defined in that role's own file — this skill doesn't hard-code either.

## Bundled resources

- `references/_role-template.md` — the structure every role file follows. Read this before drafting a new role or extending one of the roles below.
- `references/product-leader.md`
- `references/business-analyst.md`
- `references/cx-ux-research.md`
- `references/senior-product-designer.md`
- `references/delivery-lead.md`

*Add a line here whenever a new role file is created — this list is a manifest of what's bundled, not a fixed count.*
