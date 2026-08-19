# Client recommendation memo

**TO:** John Adams
**RE:** GDPR Audit, Virtual Coffee Chat Bot

**Bottom line: conditional go.** Nothing about the bot itself is unlawful. It doesn't score, rank, or decide anything about a recruiter. The problem is upstream of the AI: no one has agreed to have their conversation logged, no vendor has signed anything, and nothing gets deleted. Three fixes close that gap before this touches a real recruiter.

**Three actions, in order:**

1. **Put a real opt-in at the first message, not a T&Cs link.** State plainly that the conversation is logged and may be used to improve the bot. This has to be separate from the Article 50 "this is AI" notice; disclosing that it's a bot and getting permission to log the conversation are two different asks, and bundling them into one line is how consent gets challenged later.
2. **Run a DPIA before this goes public.** It already trips three EDPB triggers on its own: every turn is logged, it's a novel AI/RAG setup, and traffic volume jumps the moment it's public instead of just you testing it. That's enough to require one, not optional.
3. **Get DPAs signed and set a retention clock.** Seven vendors touch this data (OpenAI, Pinecone, Cohere, Calendly, Resend, n8n, Cloudflare) and none have a signed agreement. Get OpenAI's confirmation in writing that API traffic isn't used for their own training, don't take the default on faith. Pick an actual number of days for how long chat and error logs live; "until I remember to clear it" isn't a policy.

**What's still exposed even after all three:**

- A recruiter can type something sensitive into a text box in one sentence: health status, an accommodation request, anything. There's no filter that catches that reliably, only monitoring after the fact.
- Cloudflare and the third-party chat widget both touch this data and neither has been checked for what they log on their own side. The fixes above cover the vendors we know about, not the ones we haven't audited yet.
- A retention policy on paper and a retention policy that actually deletes data across seven separate systems are two different projects. The second one is the harder one, and it isn't done just because the first one is written.

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
