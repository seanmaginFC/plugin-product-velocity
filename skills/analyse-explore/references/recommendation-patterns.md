# Recommendation Patterns

Three patterns, chosen by the design output target(s) recorded in `_workflow-state.md`. Each produces three — or honestly sometimes two — comparable approaches. Never designs, never wireframes. These describe *how the problem could be solved*, so the human can choose a direction before any visual work begins.

Confidence labelling and the anti-fabrication rules in `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md` §4 apply throughout.

---

## When more than one target was recorded

Evidence's Step 2 is multi-select, so `_workflow-state.md` may list two or more design output targets for one project — a journey map alongside a UI screen is the common case. This section is the only thing that changes; **Patterns A, B and C below stay exactly as written, run independently.**

**Run each applicable pattern separately, in full, as its own group.** Don't blend approaches from different patterns into one merged set of three, and don't force a single comparison table across them — "reduce the number of steps" (a UI mechanism) and "front-stage versus back-stage emphasis" (a journey structure) aren't the same comparison axis, and a table that mixes them asks the human to compare things that can't be compared.

**Keep each group's numbering scoped to its own pattern** — Approach A1/A2/A3 for the UI-pattern group, B1/B2/B3 for the journey-pattern group, and so on — so "go with 2" is never ambiguous about which group it refers to once more than one is on the table.

**Present, iterate and settle on a chosen direction for each group on its own timeline.** The human might settle on the UI direction in round one and still be iterating on the journey map in round three; don't hold one group hostage to the other being settled, and don't treat a group as decided just because a different group is done — only the human's own sign-off makes it so.

**When only one target was recorded**, none of this applies — a single pattern group, numbered plainly (Approach 1/2/3) exactly as the sections below describe, with no group label cluttering the output for a case that doesn't need one.

---

## Pattern A — UI screen / feature design

**What varies between approaches: the underlying mechanism.** Not visual style, not layout. Two options differing only in button placement are one approach with a cosmetic edit, and presenting them as a choice wastes the human's judgement on a decision that doesn't matter.

Genuinely different mechanisms for the same problem:

- Reduce the number of steps required
- Surface information earlier in the flow rather than on demand
- Change the entry point — a proactive nudge versus on-request
- Shift a decision from the user to the system (defaults, automation), or the reverse
- Consolidate several surfaces into one, or split one overloaded surface into several

**Per-approach structure:**

- **Approach name** — short, describes the mechanism: "Progressive disclosure", "Smart defaults", "Single consolidated view"
- **Description** — 1–2 sentences, plain language
- **Mechanism of change** — what specifically shifts versus the current state
- **Insight(s) referenced** — named, with confidence label carried from the repository
- **Trade-off** — what this approach doesn't solve

**Functional and non-functional requirements are authored once, after a direction is chosen** — they go into the Project Brief's Proposed State, not into each of the three options. Writing three sets of requirements for options that won't be built is wasted effort, and it makes the options harder to compare.

- Functional: what the solution must do, as a structured list
- Non-functional: accessibility (WCAG 2.1 AA baseline unless the project states otherwise), performance, localisation where relevant, plus any brand or platform constraint already in the Brief

---

## Pattern B — Customer journey map / Service blueprint

**What varies between approaches: the sequence or structure of the journey itself** — not the visual layout of the eventual map.

Genuinely different structural approaches:

- Linear versus branching — does every user follow the same steps, or does the journey fork by segment or context?
- Where the journey starts and ends — does it include pre-purchase research, or begin at the moment of booking?
- Front-stage versus back-stage emphasis, for a service blueprint — does the recommendation focus on the visible customer-facing steps, or foreground the operational layer causing the friction?
- Consolidated touchpoints (fewer, larger stages) versus granular staging (more, smaller stages) — this changes how actionable the eventual artefact is, and for which audience

**Per-approach structure:**

- **Approach name**
- **Description** — 1–2 sentences
- **Key stages** — an ordered list of the high-level stages this approach structures the journey around. This is the real comparison point: the human should see the shape of the journey without reading a script
- **Insight(s) referenced** — named, with confidence label
- **Trade-off** — what this structure de-emphasises or leaves out

**Recommendations content, authored once after a direction is chosen** (into the Project Brief's Recommendations section): the confirmed sequence of stages, the evidence backing each stage's inclusion, and a stakeholder-facing justification for producing the artefact.

---

## Pattern C — Content / communications design

**What varies between approaches: messaging strategy** — what gets said, in what order, through which channels, in what tone. Not the copywriting itself; that's a later task. This is the strategic shape of the communication.

Genuinely different strategies:

- A single consolidated announcement versus a staged drip sequence
- One message for everyone versus segmented messaging by audience or traveller type
- Proactive push versus reactive, available-on-request framing
- Leading with reassurance versus leading with the practical "what to do"

**Per-approach structure:**

- **Approach name**
- **Content structure** — ordered message beats, e.g. 1. Problem acknowledgement → 2. What's changing → 3. What to do → 4. Reassurance. This is the comparison point, analogous to Pattern B's key stages
- **Channel & sequencing** — where each beat lands (email, in-app banner, agent-facing note) and the timing across channels
- **Tone & framing** — one line. Often the real point of difference between content options, more than structure is
- **Insight(s) referenced** — named, with confidence label
- **Trade-off** — what this strategy risks or doesn't address. A single announcement risks information overload; a drip sequence risks message fatigue or missed steps

**Recommendations content, authored once after a direction is chosen**, using this pattern's own frame rather than FR/NFR, since content has no functional requirements in the UI sense:

- **Key messages that must land** — the non-negotiable content points, as a structured list
- **Constraints** — legal and compliance, brand voice, channel limits, translation and locale requirements, plus anything already in the Brief's Constraints
- Evidence backing the chosen structure
- Stakeholder-facing justification for producing the artefact

---

## When a target doesn't cleanly match a pattern

If a design output target was recorded as free text that doesn't map onto A, B or C, pick whichever pattern's **comparison axis** is closest to what's actually being decided — mechanism, sequence, or messaging — and say explicitly which pattern you're borrowing and why. This applies per target: if one of several recorded targets is free text and the others map cleanly, only the free-text one needs a borrowed pattern.

Forcing a mismatched template silently is worse than borrowing one openly: the human can correct an acknowledged approximation, but not one they can't see.
