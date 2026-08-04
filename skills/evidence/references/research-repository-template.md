`research-repository.md`

# Research Repository Template

Copy this structure. Section order is fixed — downstream stages read top-to-bottom and should reach validation status before wading into detail.

Living-document mechanics (stable filename, `Last Updated`, overwrite-in-place, Changelog-only history) and confidence labelling are defined in `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/conventions.md` §3 and §4. Three points bear repeating here because this is the file where they're most often broken — see Notes at the end.

---

```markdown
# Research Repository — [Project Name]

Last Updated: dd/MM/YYYY
Project Brief: [path to project-brief.md]
Sub-brand: [FC / TA / W360 / TC]
Design Output Target: [e.g. customer journey map, UI screen/feature design, service
blueprint — as recorded in _workflow-state.md. Describes emphasis, not a hard restriction.]

---

## Hypothesis Validation Map

One entry for every `(hypothesis)`-tagged item in the Project Brief's Users & JTBD section.
None may be silently dropped — a hypothesis with no entry reads as though it was never
raised.

### [Hypothesis statement, verbatim from the Project Brief] (hypothesis)

**Status:** Confirmed / Revised / Still Unvalidated
**Evidence:** [what was found — attitudinal, behavioural, or both]
**Confidence:** [High — triangulated across N sources / Medium — single strong source /
Low — indicative only, thin evidence]
**Source(s):** [named, with type and window — e.g. "FullStory session data, checkout flow,
Jan–Mar 2026" / "Great Question interview transcript, P4, 10/02/2026"]

[Repeat per hypothesis.]

---

## Additional Insights

Insights that emerged from the research but don't map to an existing Brief hypothesis. No
badge or special treatment — these are net-new, not lesser.

### [Insight title]

**Finding:** [the claim, in your own words — not a quoted extract from the source]
**Confidence:** [High / Medium / Low, with brief justification]
**Source(s):** [named]

[Repeat per insight.]

---

## Source Log

Every source consulted this stage, whether or not it produced a usable insight. Include
sources checked and found irrelevant or empty — that tells downstream readers the search was
thorough, rather than only showing where it succeeded.

The FCTG Research Repository Confluence space is a standing source checked every run: log it
here even on a run where it turned up nothing. If a whole source category was unreachable
this run, log that too, with the reason — an evidence base missing four source types is
materially thinner than one that reached them, and a later stage can't infer that from
silence.

**For any Confluence, Jira, Miro or FullStory row, the Notes column must say whether it was
retrieved via `leisure-research-insights`** ("delegated") **or wasn't** ("not delegated —
[reason]"). A blank Notes cell on one of these rows reads as compliant whether or not it
actually was — don't leave that ambiguous.

| Source | Type | Date/Window | Used? | Notes |
|---|---|---|---|---|
| [name/link] | Confluence / Jira / Miro / FullStory / Great Question / Qualtrics / Usabilla / PowerBI / Attachment / URL | | Y/N | |

---

## Changelog

Append-only, most recent first. One line per change. This is the *only* place prior versions
of an insight live; every section above shows current state only.

- dd/MM/YYYY — [what changed and why, one line, with source reference]
```

---

## Notes on use

**Overwrite, don't duplicate.** When new evidence changes an entry, edit that entry in place. Don't leave the old version above or below it "for reference" — two versions of a finding in one document means a downstream stage has to guess which is current, and it will sometimes guess wrong.

**"Still Unvalidated" is a legitimate, permanent-until-changed status.** Don't manufacture a Confirmed or Revised verdict to avoid an awkward gap. "No evidence found either way" is more useful to Analyse-Explore than a confident-sounding guess, because it can be acted on — someone can go and get the evidence.

**Confidence labelling replaces source-count gating.** Never refuse to record a single-source insight. Record it and label it Low.
