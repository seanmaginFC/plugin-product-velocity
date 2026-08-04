# Source Elicitation & Discover-Approve Loop

Prompt wording for Evidence's question rounds and the secondary-artefact approval loop.

Question format — including the button-tool option caps and when a round switches to a numbered list — is defined in `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md` §2. This file covers wording only.

---

## Design output question (Step 2)

Single-select, four named options, no "Other" button:

- Customer journey map
- UI screen / feature design
- Service blueprint
- Content / communications design

Swap an option for a better-fitting one if the Project Brief already implies a likely target — for example if Scope & Boundaries names a specific deliverable. If none of the four fits, the human can free-type a reply instead of tapping; don't prompt separately for that unless their answer is ambiguous.

---

## Round 1 — source categories (Step 3)

Always precede the question with a short text note confirming the standing source. This is a statement, not a choice, so it isn't a button:

> I'll always check the FCTG Research Repository Confluence space
> (fctg-pme.atlassian.net/wiki/spaces/FCRR) by default. Anything else to draw on?

If the orchestrator's pre-flight found a dependency missing, add the constraint **here**, before the question:

> Heads-up: I can't reach Confluence, Jira, Miro or FullStory this session — the
> `leisure-research-insights` skill isn't available. Everything else I can read directly.
> If you have any of that material as an export or a paste, send it through and it still counts.

Then the multi-select. This narrows category only — it does not collect the source:

- Confluence or Jira
- Miro boards
- Survey or test data (Great Question, Qualtrics, Usabilla)
- Other (attachments, URLs, FullStory, PowerBI, anything else)

Then follow up in plain text:

> Great — for [selected bucket(s)], send me the actual links, files or content when ready.

Accept whatever mix they provide. If they chose "Other", invite them to name what it is rather than guessing from the label.

---

## Round 2 — follow-ups (Step 5)

Count the issues before asking anything, and tell the human roughly how many are coming:

> A few things came up while reading the sources — I'll ask about them one at a time.

Per-issue option sets, single-select, four each:

**No evidence found for a hypothesis**
- Search further
- Mark as still unvalidated
- I can explain
- Skip for now

**Conflicting signals between sources**
- I have context that resolves it
- Present both, unresolved
- Investigate further
- Skip for now

**Thin coverage in a flagged-important area**
- I know another source
- Proceed with what's there
- Deprioritise this area
- Skip for now

If the human's real answer doesn't fit an option, a free-text reply works — the tool doesn't block it. Any answer resembling "I have context" or "I can explain" is a prompt to ask a plain follow-up next, not a complete answer by itself.

Don't proceed to synthesis until every issue raised this round is resolved or explicitly waived.

---

## Discover → approve loop

Use this every time a source references another artefact: a hyperlink inside a PDF, a Confluence page citing another page, a Miro board linking to a second board.

This is a listing-and-approval exchange, not a fixed-option question — the candidates vary too much in number and description to fit four buttons, so handle it as plain text.

1. **Don't fetch it yet.**

2. List every secondary artefact found so far, in one message, with enough context for the human to judge relevance without opening each one:

> While reading [source], I found links to these secondary artefacts:
>
> 1. [name/link] — [one-line context, e.g. "Miro board cited as 'related workshop output'"]
> 2. [name/link] — [context]
>
> Want me to read all of these, some, or none before I continue?

3. **Wait for the response.** Don't proceed to synthesis or output until it's resolved, or the human explicitly says to skip and proceed with what's gathered.

4. If a secondary artefact links onward, repeat the loop. Don't cap it arbitrarily, but do mention when you're going more than one layer deep so the human can decide whether to keep following the chain.

The point of the loop is that following links silently changes the scope of what the human asked for without telling them — and an agent five links deep has usually stopped answering the original question.
