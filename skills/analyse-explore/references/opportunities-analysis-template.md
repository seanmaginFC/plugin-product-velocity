`opportunities-analysis.md`

# Opportunities Analysis Template

Living document, edited in place every round. Mechanics per `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md` §3 — history lives only in the Changelog, with one exception noted below.

---

```markdown
# Opportunities Analysis — [Project Name]

Last Updated: dd/MM/YYYY

## Context

- **Design output target(s):** [as recorded in _workflow-state.md — list all, even if one]
- **Pattern(s) applied:** [A — UI / B — Journey or Service Blueprint / C — Content or Comms —
  one line per target if more than one]
- **Source Project Brief:** [path]
- **Source research repository:** [path, with its "Last Updated" date at time of reading —
  so it's clear which version of the evidence these recommendations were built on]

## Recommendation Options — Pattern A: UI screen / feature design

*(Repeat this whole block — options, comparison table, decision log entries, final
direction, deferred options — once per recorded target, using its own pattern letter. If
only one target was recorded, drop the "— Pattern X: …" suffix from every heading below and
number options plainly (1/2/3); the group structure exists to keep multiple targets apart,
not to add ceremony to the single-target case.)*

### Option A1 — [Approach name]

[Description]

[Mechanism / Key stages / Content structure, per pattern]

> *Why this is credible:* [reasoning citing named repository insights and their confidence
> labels]

**Trade-off:** [what this option doesn't address]

### Option A2 — [Approach name]

[Same structure]

### Option A3 — [Approach name]

[Same structure — or omit entirely if only two genuinely distinct options were possible, and
say so here rather than leaving an empty heading]

### Comparison Table — Pattern A

| # | Approach name | Summary | Key insight(s) referenced | Confidence |
|---|---|---|---|---|
| A1 |  |  |  |  |
| A2 |  |  |  |  |
| A3 |  |  |  |  |

## Recommendation Options — Pattern B: Customer journey map / Service blueprint

*(Same structure as Pattern A above, numbered B1/B2/B3, only present if this target was
recorded. Iterates and reaches its own chosen direction on its own timeline — it doesn't need
to wait for Pattern A's group to be settled, and Pattern A's group doesn't wait for this one.)*

### Comparison Table — Pattern B

| # | Approach name | Summary | Key insight(s) referenced | Confidence |
|---|---|---|---|---|

## Recommendation Options — Pattern C: Content / communications design

*(Same structure again, numbered C1/C2/C3, only present if this target was recorded.)*

### Comparison Table — Pattern C

| # | Approach name | Summary | Key insight(s) referenced | Confidence |
|---|---|---|---|---|

## Decision Log

*Append-only within this section — the exception to overwrite-in-place. This is the audit
trail of how the direction was reached, so prior human input is never overwritten.*

- **[dd/MM/YYYY]** — [Pattern A/B/C, if more than one group exists] Human response: [chose /
  adjusted / combined / rejected, and what they said]. Action taken: [regenerated options /
  refined option N / etc.]

## Final Direction

*Filled once a direction is chosen — per pattern group, since one group can be decided before another.*

- **Pattern A — chosen approach(es):** [option number(s), or the described hybrid — omit this
  line if Pattern A wasn't a recorded target]
- **Pattern B — chosen approach(es):** [as above, omit if not applicable]
- **Pattern C — chosen approach(es):** [as above, omit if not applicable]
- **Chosen on:** [dd/MM/YYYY — per group if they were decided on different dates]
- **Summary for Project Brief:** [1–2 sentences per decided group, ready to drop in]

## Deferred Options

*Considered but not chosen — kept, not discarded. If the direction changes later, this is the
first place to check before regenerating from scratch.*

- [Option name, with its pattern letter if more than one group exists] — not chosen because
  [reason, if the human stated one]

## Changelog

- **[dd/MM/YYYY]** — [slim one-line summary of what changed this update]
```

---

## Notes on use

**The Decision Log is append-only** — unlike every other living document in this workflow. The reasoning: elsewhere, history is noise once superseded, but here the sequence of human decisions *is* the value. Knowing that an approach was rejected in round two, and why, prevents it being re-proposed in round four.

**Persist every round, not just the final one.** A session that ends mid-discussion should leave the options and the human's latest steer captured. Waiting for a chosen direction means an interrupted session loses the whole conversation.

**Deferred options are not failures.** Recording why something wasn't chosen is often more useful later than recording what was — particularly if the chosen direction runs into a constraint and the team needs a fallback that's already been thought through.

**One document, several groups — never several documents.** When more than one design output target was recorded, this stays a single `opportunities-analysis.md` with clearly separated pattern groups, the same principle the Design Brief template already uses for its own Section A/B/C. Keeping the groups apart (separate option numbering, separate comparison tables, separate decision dates) is what lets the human review and adjust one pattern's logic without the other becoming collateral damage.
