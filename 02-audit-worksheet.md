# GDPR Audit Worksheet — Composite Employee Scoring Tool

## Section A — Data map

| Field | Answer |
|---|---|
| Categories of personal data | Productivity output volume; quality-error rate; attendance records; internal chat message **content** (tone, word choice, responsiveness patterns) and **metadata** (timestamps, message frequency, response latency); derived "collaboration signal" score; derived quarterly composite score |
| Sources | Existing operational systems (productivity, quality, attendance — already collected for ops reporting); Slack/Teams via the bundled "workplace collaboration insights" feature |
| Purpose(s) — one row per purpose | (1) Operational/production reporting (pre-existing purpose for productivity/attendance data); (2) Generating a composite score to support promotion nominations; (3) Generating a composite score to flag termination-risk for early coaching/documentation |
| Lawful basis per purpose | (1) Legitimate interests — employer operational management (pre-existing, likely defensible on its own, but repurposing into the composite score needs a fresh compatibility-of-purpose check under Art. 6(4)). (2) & (3) chat-derived "collaboration signal": **TBD — legal review.** Legitimate interests is the only realistic candidate (consent is not appropriate here — in an employment relationship it is rarely "freely given" per Recital 43/EDPB guidance), but the three-step test is weak on the facts as given: necessity is arguable, but balancing likely fails given the covert rollout and the significant effect on promotion/job security |
| Retention period per purpose | Productivity/attendance: per existing ops retention policy — TBD, confirm with client. Chat-derived collaboration signal and underlying message analysis: **TBD**, but should be scoped to the review cycle only — indefinite retention of scores or raw message analysis is hard to justify |
| Recipients and sub-processors | Slack and/or Microsoft Teams (processor, US-headquartered); third-party HR analytics vendor if build-vs-buy resolves to "buy" (processor) — **TBD**; internally, HR leadership and department managers (internal recipients, not separate processors) |
| International transfers and transfer mechanism | Yes — Slack/Teams are US-headquartered. Mechanism: SCCs (Standard Contractual Clauses) expected under existing platform DPAs, but **must be verified that the existing DPA/SCC scope covers this specific new purpose** (message-content analysis for HR scoring), not just baseline chat hosting. A Transfer Impact Assessment (TIA) per Schrems II is needed given the sensitivity of the use case |

## Section B — Risk and rights

**1. Special-category data (Article 9) — present or inferable?**
Yes, plausibly. Tone/sentiment analysis on private workplace messages carries a real risk of incidentally inferring special-category data — e.g., health/stress indicators, religious observance, or union/collective-action activity mentioned in chat. Even if not the intended output, an inference risk from profiling still engages Article 9, and it isn't addressed anywhere in the current design.

**2. Automated decision-making with legal or similarly significant effects (Article 22)?**
Borderline-to-yes in substance, even though a manager formally writes the recommendation. The score is described as the "primary input," and the linked AI Act finding already established the human review step was **nominal, not genuinely exercised**, because of volume. EDPB guidance requires human involvement to be meaningful — someone with the authority, competence, and time to actually deviate from the score — not a rubber stamp. As currently designed, this likely falls under Art. 22 in practice, which requires: the right to obtain human intervention, the right to contest the decision, and the right to an explanation of the logic involved.

**3. Is a DPIA required?**
Yes, clearly. At least five of the EDPB's nine criteria are met: (a) systematic and extensive profiling with legal/similarly significant effects on employees; (b) sensitive data / data of a highly personal nature (inferred Art. 9 risk); (c) large-scale processing (~1,200 employees); (d) use of new/innovative technology (sentiment analysis on chat); (e) processing that prevents data subjects from exercising a right or using a service, combined with a lack of transparency (the "quiet rollout"). Any one of these triggers a DPIA; five together makes it non-negotiable.

**4. Most likely data subject friction points?**
Right to be informed (currently unmet — employees don't know their messages are scored for this purpose); right of access (employees will reasonably ask "what does my collaboration score say and why"); right to object to profiling (Art. 21); and, if Art. 22 applies, the right to contest the promotion/termination-risk outcome and get a human review that is demonstrably real.

**5. Controller / processor split**
Client (automotive manufacturer) = controller for all purposes. Slack/Microsoft Teams = processor for chat hosting and the bundled analytics feature. Third-party HR analytics vendor, if engaged, = processor for the composite scoring layer — **TBD pending build-vs-buy decision.**

**6. Is a DPA needed with any vendor?**
Yes. With Slack/Microsoft: a DPA/SCC framework almost certainly already exists for baseline hosting, but it needs to be checked against this specific new purpose — repurposing chat content for HR scoring is very likely outside the scope of what a standard collaboration-tool DPA contemplates. With any third-party HR analytics vendor: a DPA is required before any data flows, not after.

## Section C — Law stacking

- **AI Act cross-check:** High-risk (Annex III — employment decisions), per the prior AI Act lab. The AI Act adds obligations GDPR doesn't independently require — bias/accuracy testing on the sentiment-analysis component, technical documentation, and a *genuinely exercised* human oversight mechanism. The GDPR DPIA and the AI Act risk assessment should be cross-referenced rather than run as two disconnected documents, since they're assessing the same nominal-human-review defect from two different angles.
- **ePrivacy check:** Yes — this scenario involves analyzing the *content* of internal communications, not just metadata, which is a stronger trigger than typical cookie/tracking scenarios. Employee communications monitoring is also frequently subject to stricter national rules (e.g., works council co-determination rights in Germany) layered on top of both GDPR and ePrivacy-adjacent law — **flag for jurisdiction-specific legal review** once the in-scope manufacturing sites are confirmed.
- **Data Act check:** N/A — no connected product or cloud-switching data involved in this scenario.
