# Client Recommendation Memo — Employee Composite Scoring Tool

**To:** HR Leadership / CTO
**Re:** GDPR assessment — promotion & termination-risk composite scoring dashboard

**Bottom line: Go, with conditions.** The goal — more consistent, data-supported promotion decisions — is legitimate and achievable, but the tool cannot launch (or continue, if already live) in its current form. The two blockers are the covert rollout of chat-message analysis and a human review step that isn't genuinely exercised, and both are fixable without abandoning the project.

**Top three actions**

1. **Suspend the chat-based "collaboration signal" immediately** and pause any promotion/termination-risk decisions that relied on it, until a lawful basis is confirmed. Legitimate interests is the only realistic basis for analyzing message tone and content, and as currently run — no employee notice, no opt-out — it will not survive the balancing test. This is the single biggest exposure in the current design.

2. **Run a DPIA before any relaunch**, covering three things specifically: the risk that sentiment analysis on private messages inadvertently surfaces special-category data (health, religion, union activity); whether the scoring process meets the Article 22 threshold for automated decision-making given how "nominal" the manager review currently is; and the international transfer exposure from Slack/Teams as US processors. Pair this with a Transfer Impact Assessment and confirm the existing platform DPA actually covers this new use case — it likely doesn't as written.

3. **Rebuild transparency and human review before resuming.** Notify affected employees what's being analyzed and why, update the privacy notice, and give them a real path to object. Separately, redesign the manager review step so it's demonstrably substantive — documented reasoning, training, and enough time per case to actually deviate from the score — not a rubber stamp under volume pressure. This same fix also closes the gap flagged in the AI Act review.

**Residual risks (even after these fixes)**

- **Chilling effect on communication.** Once employees know chat tone is being scored, they may change how they communicate — which can quietly degrade the very "collaboration signal" the tool is meant to measure, and this isn't something a DPA or notice can fully prevent.
- **Local employment-law exposure.** Depending on which manufacturing sites are in scope, employee-monitoring rules (e.g., works council co-determination in Germany) may require separate approval or could block parts of this design outright — this needs country-specific legal review before rollout, not after.
- **Review quality drift over time.** A "genuine" human review is only as real as the ongoing incentive structure supports. Without periodic auditing, manager review can quietly slide back into rubber-stamping as case volume grows, re-creating the Article 22 exposure this memo is meant to close.

---
