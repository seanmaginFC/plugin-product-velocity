# Kickoff Question Map

The canonical field list for Intake. Two uses:

1. **Parsing an attached kickoff** — match its fields against this map, tolerating minor rewording, to populate the Brief.
2. **Conversational fallback** — if nothing is attached, ask these in chat, one **section** at a time in the order below. All P0 fields in a section before that section's P1 fields.

"Unknown / TBD" is a valid answer to any field. Record it as such — don't leave it blank and don't invent something plausible.

## Priority meaning

- **P0 — required.** If unanswered, name it explicitly and prompt for it. If it stays unanswered, it becomes a designer override: recorded with its reason, then the workflow proceeds. It is never silently carried forward as though it were answered.
- **P1 — valuable, not blocking.** Ask once; if deferred, move on without re-prompting.

The gate that governs how P0 gaps are handled belongs to the `orchestrator` skill, not to this file. Follow its rule: **prompt, then advance only on a recorded override.** If this document and the orchestrator ever appear to disagree, the orchestrator wins.

---

## 0. Document Control

- Project / feature name
- Date of kickoff meeting
- Designer (author)
- Stakeholders present
- Meeting source (live notes / recording / async doc)

## 1. Business Context [P0]

- **Problem or opportunity statement** — What are we solving or pursuing, in the stakeholder's own words? Capture what is affected and what is currently happening. "20% of mobile checkout users abandon at the payment step" beats "checkout needs improvement".
- **Business goal this supports** — Which outcome: revenue, retention, cost, compliance, strategic bet? Include the target if one was stated; write "no target set" if not.
- **Why now?** — What's driving the timing. If nothing was said, record that explicitly — the absence tells you whether this is strategic or reactive, which is signal, not a gap.
- **Strategic alignment** [P1] — The named OKR, roadmap theme or initiative. If stakeholders couldn't name one, record "not tied to a named initiative".

## 2. Users & Jobs-to-be-Done

> Everything in this section is a **hypothesis** until validated in Evidence. Carry the `(hypothesis)` label into the Brief verbatim.

- **Target user(s) / segment** *(hypothesis)* — Who is this for? Use stakeholders' own language, even if informal ("repeat customers", "TA advisors").
- **Job-to-be-done / core user need** *(hypothesis)* — Phrase as "When [situation], I want to [motivation], so I can [outcome]". If you were given a feature request ("add a filter"), push one level deeper before writing it down — the filter is a solution, not the need.
- **Known pain points** [P1] *(hypothesis)* — Attribute each to its source: research, support tickets, sales feedback, or one stakeholder's opinion. An unattributed pain point is itself a hypothesis for Evidence to test.

## 3. Scope & Platform [P0]

- **In scope** — Concrete capabilities or flows, not themes. "Redesign the payment step of checkout" can be scoped; "improve checkout" can't.
- **Explicitly out of scope** — Often the single most valuable field in the document, because an unstated boundary is the most common source of rework. If exclusions weren't raised, ask directly rather than leaving it blank.
- **Platform(s) / touchpoint(s)** — Web, native app, mobile web, admin console, or named systems. Be specific about named platforms; it determines which stakeholders matter.
- **Brand / market / locale scope** [P1] — A solution scoped to one brand's flow is a materially different project from a global one. Don't default to "all" if it wasn't discussed.

## 4. Success Metrics [P0]

- **How will success be measured?** — Metric or KPI, with the current baseline if anyone knows it. A metric with no baseline can't demonstrate impact later. If there genuinely isn't one, record "no success metric defined" as an explicit gap.
- **Metric owner / source of truth** — Name the actual dashboard, tool or person ("FullStory funnel: Checkout v2", "Jane Doe, Analytics"). "The data team" isn't specific enough to act on.

## 5. Constraints [P0]

- **Timeline / key dates** — Actual dates, not "soon". Say so if a date is soft.
- **Technical constraints** — Note who raised it and how firm it is. A constraint stated by an engineer in the room is more reliable than one relayed secondhand.
- **Compliance / brand / legal constraints** [P0] — Name the actual standard: "WCAG 2.1 AA required", "PCI-DSS applies to payment fields". Specificity here drives requirements later; "needs to be accessible" doesn't.
- **Dependencies on other teams or parallel initiatives** [P1] — Name the initiative and its owner. A missed dependency is a common cause of late rework.

## 6. Stakeholders & Decision Rights [P0]

Table: Name / Function-discipline / Decision authority (approver, consulted, informed).

Name actual people, not roles alone ("Jane Doe, Eng Lead", not "engineering"). Capture explicitly who has final sign-off versus who is only informed. If sign-off authority is unclear or contested, record that — ambiguous approval is a risk, not a detail.

## 7. Risks, Assumptions & Open Questions [P1]

- **Assumptions being made right now** — Phrase as falsifiable statements ("we're assuming mobile users behave like desktop users") so Evidence can test them directly.
- **Open questions raised but not answered** — Note who owes the answer and by when. An open question with no owner stays open.
- **Risks flagged** — State the likely impact, not just the topic: "if legal review slips, the launch date is at risk", not "legal review".

## 8. Intake Completeness Gate

Confirm each:

- [ ] Job-to-be-done is filled, or explicitly marked "Unknown / TBD"
- [ ] Business goal and success metric are stated in terms someone outside the meeting could verify
- [ ] At least one decision-maker is named
- [ ] Persona and JTBD content is labelled as hypothesis, not fact
- [ ] Scope **exclusions** have been discussed, not just inclusions

**Designer override** — if proceeding with P0 gaps, the stated reason. This carries into the Brief's Intake Notes and into `_workflow-state.md` verbatim. If no reason was given, record "no reason given" rather than inventing one or omitting the override.
