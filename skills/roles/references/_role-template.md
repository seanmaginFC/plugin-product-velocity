`references/<role-slug>.md`

*This file defines the structure every persona role follows. Copy it when adding a new role; don't restructure an existing role file without a reason, or the roles stop being comparable at a glance.*

# [Role Name]

*Status: Template / Draft / Active · Last Updated: [dd/MM/YYYY] · Author: [name]*

**Status meanings** — carry the file's actual state, don't leave it saying "Template" once content exists:
- **Template** — placeholders only, not yet usable by a stage.
- **Draft** — partly written; usable for on-demand review if the human accepts it's incomplete, not yet trusted for the automatic lens.
- **Active** — complete enough that a stage can rely on it unprompted.

## Purpose

*One or two sentences. What judgement gap does this role close that the stage wouldn't catch on its own? Not a job description — the specific blind spot.*

[e.g. "A Business Analyst catches requirements that sound complete but aren't testable — a Functional Requirement with no observable pass/fail condition looks fine to everyone else in the room."]

## Primary stage(s)

*Which stage(s) this role applies to, and which section(s) within them. Be specific — "Analyse-Explore" is less useful than "Analyse-Explore, Step 7's Functional Requirements".*

- [Stage — section]
- [Stage — section]

## Engagement mode

*Pick one or both. This determines how a stage actually uses this file — see `SKILL.md`'s "How a stage applies a role" section.*

- [ ] **Automatic lens** — runs silently before the stage presents this section as finished.
- [ ] **On-demand review** — runs only when the human explicitly asks for this role's review.

## Mindset — the questions this role always asks

*Three to six questions this specialist reflexively asks of a document, regardless of what it already says. These are what power both the checklist below and the drafting voice further down — write these first, everything else follows from them.*

1. [Question]
2. [Question]
3. [Question]

## Critique checklist

*Concrete, checkable items — things this role would flag as missing, vague, or wrong. Written so a specific catch is either true or false against a given draft, not a matter of taste. Aim for specific enough that two different people applying this checklist to the same document would flag the same gaps.*

- [ ] [Specific thing to check for]
- [ ] [Specific thing to check for]
- [ ] [Specific thing to check for]

## Voice & drafting notes

*Only needed if this role also drafts content, not just critiques it. Tone, structure, and typical phrasing this role would use — enough that content written "as" this role reads differently from the plugin's default voice, not just differently formatted.*

[e.g. structural habits, preferred sentence patterns, what this role always states explicitly that others might leave implicit]

## Known failure modes this role exists to catch

*Concrete examples of what actually goes wrong without this lens — not hypothetical, drawn from real documents or real feedback if you have it. This is what grounds the role in something other than a generic idea of the job title.*

- [Failure mode, with an example if you have one]
- [Failure mode, with an example if you have one]

## Example prompts

*Sentences a human would actually type to invoke this role on-demand. Helps with discoverability — these are candidates for the trigger phrases in `SKILL.md` once several roles are drafted.*

- "[Example prompt]"
- "[Example prompt]"

## Out of scope

*What this role explicitly does not own, especially where it could be confused with another role. Boundary-setting here is what stops two roles giving contradictory advice on the same section.*

- [Not this role's call — whose is it instead?]
