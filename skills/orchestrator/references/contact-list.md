# Product Velocity — Contact List

**This file is meant to be edited.** It is deliberately separate from any skill logic so contacts can be reviewed and updated without touching how the plugin behaves. Change a name here and every stage picks it up.

Read this file when escalating. Don't reproduce these names from memory in a response — read them, so an out-of-date copy never reaches a designer.

---

## Contacts

| Area | Contact | When to point the human here |
|---|---|---|
| `leisure-research-insights` skill — access or availability | **Will Yanko** | The skill isn't available in the designer's Claude account. Stage 2 can't retrieve Confluence, Jira, Miro or FullStory sources without it. |
| Everything else — plugin errors, unexpected behaviour, connector problems, skill bugs, feature requests | **Sean Magin** | Any failure or oddity not covered by a row above. This is the default fallback; when in doubt, use it. |

---

## How to escalate

Escalating is not a substitute for reporting honestly. Say what failed and what you could and couldn't confirm first, then name the contact. A designer needs to know what state their project is in before they know who to message.

Suggested wording:

> Stage 2 uses the `leisure-research-insights` skill to read Confluence, Jira, Miro and FullStory, and it isn't available in this account — so those four source types are off the table for now. Anything else you've got (interview transcripts, survey or usability exports, PowerBI, attachments, links) I can still read directly, so Evidence can go ahead on those. Contact **Will Yanko** to get the skill installed if you want the Confluence and Miro material included — worth knowing that without it we can't check the standing FCTG Research Repository space, so the evidence base will be thinner and fewer insights will reach High confidence. I'll note the gap in the Source Log either way.

> The Confluence page update returned an error and I couldn't verify the change landed — the page may be unchanged. This is usually an authentication or permissions issue: check Settings → Connectors and confirm the Atlassian connection is active with write access to that space. If it looks fine and this keeps happening, contact **Sean Magin**. The updated content is saved in `project-brief.md` either way, so nothing is lost.

> At pre-flight, I couldn't reach Confluence or Miro, even after checking again. If you can see them listed as connected in Settings → Connectors, it's more likely a permissions issue — the connection exists but may not have access to the specific space or board this project needs — than the connection being down. Worth a quick look either way. In the meantime, Intake isn't affected; Evidence will lose those two source categories if the gap doesn't clear. Let me know if you'd like me to check again once you've had a look, and contact **Sean Magin** if it still doesn't resolve.

---

## Planned

**Slack notification on error** — the intention is for the plugin to message the relevant contact automatically when an error is encountered, rather than relying on the designer to pass it on. Not built yet. Until it is, escalation is manual: tell the human who to contact and let them decide whether to.

When this is added, the routing should read from the table above rather than hard-coding Slack handles, so this stays the one file to edit.
