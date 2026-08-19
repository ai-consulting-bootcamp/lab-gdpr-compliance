# Peer review: John Adams, client recommendation memo

**Reviewer:** Gordan

**Memo reviewed:** `Client Recommendation Memo - John Adams.md`

**System:** Virtual Coffee Chat Bot

**Date:** 19 August 2026

**Total: 12 / 15**

---

## Rubric

| Criterion | Score 1-3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Conditional go" appears in the first three words, with the reason compressed into one line: the problem is upstream of the AI. Framing the bot itself as fine and the governance around it as the gap is the correct diagnosis and it lands immediately. A CTO reads this in ten seconds and knows what they are being told. |
| Lawful basis selection is justified | **1** | The weak point, in two ways. First, no Article 6 basis is named anywhere. Consent is implied by "opt-in" but never stated as a legal basis, and no alternative is weighed. Second, the choice is probably wrong. Consent for the chat itself is unworkable: processing the message is unavoidable to answer it, so if consent is withdrawn mid-conversation the service cannot function, which is exactly the case where the EDPB says consent is not freely given. Legitimate interests for delivery, with consent or LI plus a working opt-out for the logging, is the defensible split. "No one has agreed to have their conversation logged" states a fact and skips the analysis. |
| Top actions are specific and sequenced | **3** | Explicitly sequenced, concrete, and vendors are named rather than gestured at. Two things worth stealing: the instruction to get OpenAI's no-training position in writing rather than taking the default on faith, and "until I remember to clear it isn't a policy". Two corrections. The DPIA cannot really precede the DPAs, because vendor transfer routes and retention terms are inputs to it, so actions 2 and 3 are the wrong way round. And the DPIA justification is shaky: logging turns of a service the user opted into is not systematic monitoring in the WP248 sense, and this will never be large scale. The stronger argument is the German DSK Muss-Liste item 11, which makes a DPIA mandatory for AI used to steer the interaction with data subjects. Right conclusion, reasoning that would not survive a challenge. |
| Residual risks are named honestly | **3** | The strongest section. All three risks are real, none are padding, and the third is the one most consultants never say out loud: a written retention policy and a retention policy that actually deletes across seven systems are different projects. Naming Cloudflare and the widget as unaudited is honest about the boundary of the work rather than pretending the audit was complete. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | Half addressed, half absent. The AI Act point is sharp: separating the Article 50 "this is AI" disclosure from consent to logging, because they are two different asks and bundling them invites a challenge, is better than most reviewers will produce. But no risk tier is stated, and ePrivacy does not appear at all. That is a real gap here, because the chat widget writes a session identifier to browser localStorage under `n8n-chat/sessionId`, which engages Article 5(3) ePrivacy and section 25 TDDDG. It most likely falls within the strictly-necessary exemption, but the memo does not know that, because it did not look. Data Act is unmentioned, even to dismiss it. |

---

## Response as the client

I accept the recommendation and I will start on the vendor paperwork this week.

One thing I want you to rethink: the opt-in. You are asking me to put a consent gate in front of a chatbot whose whole purpose is to lower the friction of a first conversation with a recruiter, and if someone withdraws consent halfway through, I do not understand what the bot is supposed to do with the message it is already holding. Come back to me with the case for legitimate interests on the conversation itself and consent reserved for the logging, and tell me which one you would defend to a regulator.

Also, you list n8n as one of seven vendors, but I self-host it in Docker, so I am not sure they process anything at all. My actual hosting provider is not on your list.
