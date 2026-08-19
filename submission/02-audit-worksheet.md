## Phase 2: Mini GDPR Audit Worksheet

### Section A — Data Map

| Field | Answer |
|---|---|
| **Categories of personal data** | (1) Productivity metrics — output volume, quality-error rate; (2) attendance records; (3) content and metadata of internal chat messages (Slack/Teams) used to derive the "collaboration" tone/responsiveness signal; (4) the composite quarterly score itself, which is a new, derived personal data point about each employee. |
| **Sources** | Productivity/quality/attendance data from existing internal operational systems (already collected for standard performance reporting); chat data pulled directly from the Slack/Teams platforms via API or export. |
| **Purpose(s) — one row per purpose** | (1) Standard performance reporting (productivity, quality, attendance) — pre-existing purpose. (2) Deriving a "collaboration" signal from chat tone/responsiveness — new purpose. (3) Generating a composite score to inform promotion nominations — new purpose. (4) Generating the same composite score to flag termination-risk coaching — new purpose, distinct from (3) even though it reuses the same score. |
| **Lawful basis per purpose** | (1) Productivity/attendance reporting: **Legitimate interests** — employer has a reasonable interest in tracking operational performance; lower privacy intrusion since this is existing-purpose data. (2) Chat tone/sentiment analysis: **TBD — legal review.** Legitimate interests is the most likely candidate, but the three-step test is genuinely uncertain here — necessity is questionable (is analyzing private message tone actually necessary, versus a less intrusive proxy?), and the balancing test is close given the intrusiveness of analyzing communication content. (3) & (4) Composite score used for promotion/termination decisions: **TBD — legal review**, specifically because Article 22 automated decision-making constraints interact with lawful basis selection here — consent is likely unsuitable (power imbalance in an employment relationship undermines "freely given" consent), and legitimate interests is questionable given the significant effect on the employee. |
| **Retention period per purpose** | Not specified in the fact pattern for any category — **TBD — legal review** across all four purposes. This is itself a finding: no retention period was defined in the original design, which is a gap on its own regardless of what the ultimately correct period turns out to be. |
| **Recipients and sub-processors** | Slack and/or Microsoft Teams (processing/hosting the underlying chat data); the scoring/dashboard tool provider, if third-party (TBD — legal review, build vs. buy unconfirmed); internal recipients: the employee's manager and HR, who see the composite score and use it in promotion/termination-risk decisions. |
| **International transfers and transfer mechanism** | Likely present — Slack and Microsoft Teams are US-headquartered providers; even with EU-region hosting options, the corporate parent's US jurisdiction raises transfer questions. Transfer mechanism (Standard Contractual Clauses, adequacy reliance, or otherwise) — **TBD — legal review**, needs direct confirmation of each vendor's specific data residency and transfer setup, not assumed from company headquarters alone. |

### Section B — Risk and Rights

**Are any special-category data present or inferable from the outputs (Article 9)?**
Plausibly yes. Sentiment/tone analysis on private workplace messages carries a real risk of inadvertently inferring special-category data — for example, communication patterns that reflect stress, mental health status, or a disability accommodation, none of which were the intended target of the analysis but could be inferred as a side effect. This is a genuine open risk, not a hypothetical one, since the system was never designed to exclude or filter for this possibility.

**Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?**
Yes — the composite score directly informs promotion and termination-risk decisions, both recognized as having a legal or similarly significant effect. The required safeguard is meaningful human review, the right to contest the decision, and the right to express one's point of view. Per our linked AI Act finding, the current human review step is nominal (managers are expected to simply act on the score given hiring/review volume) — this means the Article 22 safeguard is very likely **not currently satisfied in practice**, even if a human technically has override authority on paper.

**Is a DPIA required?** Using the EDPB's nine criteria, this processing likely meets several: (1) evaluation/scoring of individuals, (2) automated decision-making with legal/significant effect, (3) systematic monitoring (ongoing quarterly scoring), and arguably (4) sensitive data or data of a highly personal nature, given the special-category inference risk above. Meeting two or more criteria is generally sufficient to trigger a DPIA requirement — this processing meets at least three. **A DPIA is required.**

**What data subject friction points are most likely?**
Right to object to profiling is the most likely friction point, given the direct link between the score and employment consequences. Right of access is also likely, since employees will reasonably want to know their own score and the reasoning behind it. Right to erasure is less likely to be exercised proactively but would be complicated to honor given the score's role in ongoing HR decision-making and record-keeping.

**What is the controller/processor split?**
The manufacturing client is the **controller** — it determines the purposes and means of processing (why the score is generated and how it's used). Slack/Microsoft Teams act as **processors** for the underlying chat data. If a third-party HR analytics vendor built the scoring tool, that vendor is also a **processor**, acting only on the client's instructions — this needs confirming per the "build vs. buy" TBD noted in Section A.

**Is a DPA needed with any vendor? Which ones?**
Yes. A DPA is needed with Slack and/or Microsoft Teams (for the underlying chat data processing) and, if applicable, with any third-party scoring/dashboard vendor. Neither should be assumed to already exist in a form that covers this specific new use case (tone/sentiment analysis for HR decision-making) — this is a materially different processing purpose than standard workplace messaging, and existing platform-level DPAs may not contemplate it.

### Section C — Law Stacking

**AI Act cross-check:** This system was classified as **High-risk (Annex III — employment decisions)** in our linked AI Act audit. The AI Act adds obligations GDPR does not directly cover — specifically, a formal risk management system, technical documentation, conformity assessment, and bias/accuracy testing requirements on the AI model itself. GDPR's DPIA and AI Act's risk management obligations should be coordinated rather than run as two disconnected processes, since they overlap substantially on this fact pattern.

**ePrivacy check:** Yes, this scenario involves device-level/communications data in a meaningful sense — the system analyzes the *content* of private workplace chat messages, which touches confidentiality-of-communications principles under ePrivacy, not just standard GDPR personal data rules. This is a genuine stacking question worth flagging distinctly: even if GDPR's legitimate-interests balancing test were satisfied, ePrivacy's stricter confidentiality-of-communications framing could still impose an independent constraint that GDPR's flexibility alone does not resolve.

**Data Act check:** Not applicable. This scenario does not involve a connected product or cloud-switching data — N/A, no IoT or infrastructure-switching element present.
