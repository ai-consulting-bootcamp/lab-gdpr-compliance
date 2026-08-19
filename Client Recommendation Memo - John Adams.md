# Client recommendation memo

**TO:** John Adams
**RE:** GDPR Audit, Virtual Coffee Chat Bot

**Bottom line: conditional go.** Nothing about the bot itself is unlawful. It doesn't score, rank, or decide anything about a recruiter. The problem is upstream of the AI: there's no consent for logging, no vendor has signed anything, and nothing gets deleted. Three fixes close that gap before this touches a real recruiter.

**Three actions, in order:**

1. **Get the vendor list right and DPAs signed first.** OpenAI, Pinecone, Cohere, Calendly, Resend, and Cloudflare (if it logs identifiable traffic) each need a signed agreement, and none have one. n8n itself doesn't need a DPA, since it's self-hosted in Docker and never sends data to an n8n-the-company entity, but whoever hosts that Docker instance does, and that provider hasn't been identified yet. Get OpenAI's confirmation in writing that API traffic isn't used for their own training, don't take the default on faith. This has to happen first, because the DPIA below needs each vendor's transfer route and retention terms as an input.
2. **Split the lawful basis: answering the message runs on legitimate interests, logging runs on consent.** Processing a recruiter's own question to answer it is unavoidable to deliver the service, so consent doesn't fit; consent has to be freely withdrawable, and there's no way to un-process a message the bot is already answering. Logging the conversation for training is a separate, lower-expectation purpose and needs its own clear opt-in, distinct from the Article 50 "this is AI" notice, not bundled into one line.
3. **Run a DPIA before this goes public, once the vendor picture is settled.** Every turn of a service the user opted into gets logged, so "systematic monitoring" is a stretch as the trigger; the stronger case is that this is an AI system steering the interaction with the person on the other end. Either way, it clears the bar for needing one before launch.

**What's still exposed even after all three:**

- A recruiter can type something sensitive into a text box in one sentence: health status, an accommodation request, anything. There's no filter that catches that reliably, only monitoring after the fact.
- Cloudflare and the third-party chat widget both touch this data and neither has been checked for what they log on their own side. The fixes above cover the vendors we know about, not the ones we haven't audited yet.
- A retention policy on paper and a retention policy that actually deletes data across every processor are two different projects. The second one is the harder one, and it isn't done just because the first one is written.

---

## Peer feedback rubric

*For your partner to complete.*

| Criterion | Score 1-3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

After scoring, write two to three sentences as the "client": either accept the recommendation, flag one concern, or ask the consultant to rethink one section.
