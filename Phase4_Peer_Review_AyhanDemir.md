# Phase 4: Partner swap and peer review

*Reviewer: Ayhan Demir · Memo reviewed: Julia Antunes, "GDPR recommendations for the seller messaging assistant" (Case 1 Kleinanzeigen), 17 November 2026*

## Julia's Client Memo
Phase 3: Write the client recommendation memo
Case 1 Kleinanzeigen / From: Ayhan Demir
Subject: GDPR recommendations for the seller messaging assistant
Created by Julia Antunes / Date: 17 November 2026

**Bottom line** Go with conditions. The assistant may help opted-in sellers respond while offline, but the available facts do not establish the lawful basis, vendor and transfer arrangements, retention, or how buyers are informed. Resolve these points before enabling the feature.

**Top three actions**

1- Map the processing before launch. Identify the AI and hosting providers, their locations and roles, the data each receives, and applicable retention periods. Determine whether any data leaves the EU/EEA and document the transfer mechanism if it does.

2-Complete the GDPR assessments and notices. Determine and document an Article 6 lawful basis for processing sellers’ past replies and buyers’ messages; do not treat seller opt-in alone as proof of consent for all processing. Screen the processing against the EDPB’s DPIA criteria and complete a DPIA if the screening indicates likely high risk. Explain the assistant’s role to sellers and buyers, including that it sends messages without live review and under the seller’s name. Because chat content may contain special-category data, confirm whether it does; if so, assess Article 9 conditions and safeguards before processing it.

3- Set up accountability and user controls. Confirm the controller/processor roles and put a DPA in place before any vendor processes personal data on Kleinanzeigen’s behalf. Specify retention and how access, erasure, and objection requests will be handled. Preserve the seller’s ability to switch the feature off and review the conversation.

**Residual risks:** Free-text chats may contain sensitive information that is not identified in the current facts. Buyers may still misunderstand who authored a message, even if the feature is disclosed. The system sends messages without live human review, so inaccurate or unsuitable responses may affect a transaction before the seller sees them.

This is a preliminary recommendation based only on the scenario facts provided. Vendor details, data volumes, locations, and the legal effects of messages remain unknown and could change the assessment.

## Rubric

| Criterion | Score 1–3 | Comment |
| --- | --- | --- |
| Clear bottom-line recommendation | 3 | "Go with conditions" is stated up front, and the conditions are clear. The reason is a list of open points rather than one sentence. |
| Lawful basis selection is justified | 2 | No Art. 6 basis is selected, only "determine and document". The warning that seller opt-in is not consent for all processing is a good point. A proposal was missing: e.g. contract for sellers who switch the feature on, and legitimate interests with an LIA for buyers' messages. |
| Top actions are specific and sequenced | 2 | The order is logical: map, then assess, then controls. But the actions are generic ("identify", "determine") with no named owner, deadline or vendor, and the DPA sits in action 3 although it is needed before any data flows. |
| Residual risks are named honestly | 3 | Three concrete risks: sensitive data in free text, buyers misreading authorship, and unreviewed messages affecting a transaction. The closing caveat about unknown facts is honest. |
| Law stacking is addressed (AI Act / ePrivacy) | 1 | Not addressed. The AI Act tier (transparency, Art. 50(1)) is the key issue here, because messages appear under the seller's name with no AI label. ePrivacy is not checked either, e.g. whether the in-app chat counts as a communications service. |

**Total: 11 / 15**

## Client response

We accept "go with conditions", and the residual risks are useful for our product team. One concern: the memo leaves the lawful basis open and does not mention the AI Act, while our current design shows AI messages under the seller's name with no label. Please rethink action 2 so that it proposes a lawful basis for sellers and for buyers, and makes a visible "sent by AI assistant" label a launch blocker.
