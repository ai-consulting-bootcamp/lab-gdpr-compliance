## Phase 3: Client Recommendation Memo

**To:** Head of HR / Legal
**From:** Jay Ramamoorthi, AI & Privacy Consulting
**Re:** GDPR assessment — employee promotion/termination scoring system

**Bottom line: Go with conditions.** The underlying goal — using data to make employment decisions more consistent — is legitimate, but the current design has real gaps that need closing before this touches a single employee's chat data or influences a real promotion or termination decision.

**Top three actions:**

1. **Fix human review before anything else.** Right now, managers are expected to act on the score without meaningfully reviewing it, given volume. This isn't just an AI Act problem — it means the required safeguard under GDPR's Article 22 (the right to meaningful human review of an automated decision with legal effect) doesn't currently exist in practice. Build a workflow that requires managers to document their reasoning before acting on the score, not just click accept.

2. **Complete a DPIA before this touches real chat data.** This processing hits at least three of the EDPB's DPIA triggers at once — scoring individuals, automated decisions with real effect, and ongoing systematic monitoring. That's not optional paperwork; it's required before go-live, and it should happen alongside the AI Act's own risk documentation, not as a separate exercise months later.

3. **Get a DPA in place with Slack/Teams (and any third-party scoring vendor) that specifically covers this use case.** Your existing platform agreements almost certainly weren't written with "analyzing employee chat tone for HR decisions" in mind. Don't assume they already cover it.

**Residual risks you should know about, even if we do all of the above:**

- **Special-category inference risk doesn't fully go away.** Sentiment analysis on private messages can pick up signals related to stress, mental health, or a disability accommodation — even with the best intentions, we can reduce this risk, but we can't promise it to zero.
- **International transfer exposure remains until we confirm exact data residency** with Slack/Teams and any third-party vendor — this needs direct legal confirmation, not an assumption based on where the company is headquartered.
- **Employee trust risk is real and not purely legal.** Even a fully compliant system that scores private chat tone for promotion/termination decisions will likely generate genuine employee pushback once understood — that's a change-management problem this memo can flag but can't solve on its own.
