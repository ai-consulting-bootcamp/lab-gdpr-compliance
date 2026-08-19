# GDPR Audit Pack - John Adams

## Transition note

Carrying forward the Virtual Coffee Chat Bot (Project 3) from the Week 7 Day 2 EU AI Act self-audit. That audit classified it as limited risk under Article 50. The bot generates AI content and talks to end users without disclosing it is AI. It is a good case for GDPR because it has real data handling to audit. Chat conversations are logged and may contain recruiter PII. That data is processed by several third parties. I also plan to use logged feedback, such as thumbs up or down and errors, to improve the model and find gaps or mistakes in my own history. The bot also represents me as an agent. My personal image is on the line if it is handled or represented wrong.

## Fact pattern

John Adams runs a personal AI chatbot that lets recruiters and hiring managers have a virtual coffee chat with him. The bot logs open-ended chat content that may include names, companies, hiring locations, and other interview details, plus contact info for booking and email actions, and feedback ratings. Data subjects are recruiters and hiring managers, located anywhere in the world including the EU, since the bot is shared on LinkedIn and with international recruiters. The stack includes OpenAI, Pinecone, Cohere, Calendly, Resend, self-hosted n8n, and Cloudflare, all non-EU vendors, with no data residency or transfer mechanisms reviewed yet. The bot retrieves career info to answer questions, logs conversations, checks and books calendar slots, sends emails on John's behalf, and feedback signals will be used to improve answers and find gaps in his career info. No automated decision-making affects recruiters; John may manually review logs for patterns.

---

# Audit worksheet

## CFU 1 - Recognize

- **Categories of personal data present:** names, email addresses, employer/company names, location/region data, free-text interview-context content, behavioral/feedback data (ratings, error logs).
- **Special-category data (Article 9):** low risk but not zero. The bot's guardrails prevent it from disclosing sensitive info about John (age, sex, religion), but nothing currently stops a recruiter from typing sensitive info about themselves into open chat text (e.g. a disability accommodation request). Inferable, not solicited.
- **EU border crossing:** yes. Data subjects can be anywhere including the EU, and every vendor in the stack is non-EU (US or Canada), so any EU-based recruiter's data leaves the EU immediately with no reviewed transfer mechanism.

## Section A - Data map

| Field | Answer |
|---|---|
| Categories of personal data | Names, email addresses, employer/company names, location/region data, free-text interview-context content, behavioral/feedback data (ratings, error logs). |
| Sources (where data comes from) | Directly from the recruiter, typed into the chat, plus what they submit when booking a call or triggering an email. |
| Purpose(s) | (1) Answering recruiter questions. (2) Booking calls and sending emails on John's behalf. (3) Using feedback/logs to improve the bot and find gaps in John's career info. |
| Lawful basis per purpose | (1) Legitimate interests. Answering the message the recruiter just sent is unavoidable to deliver the service they asked for; consent doesn't fit here because it has to be freely withdrawable, and withdrawing mid-conversation can't un-process a message the bot is already holding. LIA three-step test: purpose (respond to the recruiter's own question), necessity (processing the message is the only way to answer it), balancing (a recruiter who opens the chat and types a question has a reasonable expectation their message will be read and answered). (2) Consent. Triggered only when the recruiter explicitly asks to book or message, a distinct affirmative action, and involves sharing their email with two more vendors (Calendly, Resend). This should be its own clear opt-in line at the point the action is requested. (3) Consent. Logging for training/improvement is a separate, lower-expectation purpose than just answering the question, so it needs its own opt-in, captured at the first message but as a clearly separate line (e.g. "your chat may be logged and used to improve this assistant"), not folded into the legitimate-interests basis for Purpose 1 or buried in a general T&Cs agreement. |
| Retention period per purpose | TBD - legal review. No retention policy currently exists for any purpose. All data is kept indefinitely by default. Must be defined before public launch. |
| Recipients and sub-processors | OpenAI, Pinecone, Cohere, Calendly, Resend, Cloudflare (tunnel, logging unclear). n8n is self-hosted in Docker by John, not a third-party processor, so it is removed from this list; the actual hosting provider for the Docker host (unconfirmed as of this audit) is the real unlisted party and needs to be identified and added. No DPAs confirmed with any of the vendors above yet. |
| International transfers and transfer mechanism | All confirmed vendors are non-EU (US: OpenAI, Pinecone, Calendly, Resend, Cloudflare; Canada: Cohere). Any EU-based recruiter's data leaves the EU immediately upon use. No transfer mechanism (e.g. Standard Contractual Clauses) has been reviewed or confirmed with any vendor. The Docker host's location is unconfirmed and needs to be added to this assessment once identified. TBD - legal review. |

Lawful basis is split by purpose: legitimate interests covers answering the recruiter's own message (Purpose 1), since consent is not workable for a service that can't function once withdrawn mid-conversation; consent covers booking/email (Purpose 2) and logging for training (Purpose 3), both of which are distinct, affirmative, and not required just to receive an answer.

## Section B - Risk and rights

1. **Special-category data present or inferable (Article 9)?** Low risk but not zero. The bot's guardrails prevent it from disclosing sensitive info about John (age, sex, religion), but nothing currently stops a recruiter from typing sensitive info about themselves into open chat text (e.g. a disability accommodation request). This is inferable, not solicited, and should be monitored rather than ignored.

2. **Automated decision-making with legal or similarly significant effects (Article 22)?** No. The bot only answers questions and books calls. It does not score, rank, or filter recruiters. Any pattern review (e.g. repeated errors on a topic) is manual, done by John on the logs, to improve the bot, not to make a decision about any person.

3. **Is a DPIA required?** Yes, a DPIA is likely required. At least three EDPB criteria apply: systematic monitoring (every turn logged), innovative technology (AI agent, RAG, cross-border processing), and large-scale processing once launched publicly. A DPIA should be completed before public launch, not after.

4. **Most likely data subject friction points?** Right of access ("what did you store about me?") and right to erasure ("delete my chat"). Right to object to profiling is not relevant, since the bot doesn't profile. No workflow currently exists to handle these requests. The intended design is that the bot never resolves these itself; it should flag the request and route it to John directly so it can be logged and manually actioned.

5. **Controller / processor split?** Controller: John Adams. He decides the purpose and means of processing (recruiting tool, training on feedback, etc.). Processors: OpenAI, Pinecone, Cohere, Calendly, Resend, Cloudflare, all acting on John's instructions with no independent purpose of their own. n8n is self-hosted in Docker by John; it is not a separate processor, since no n8n-the-company entity ever receives the data. The actual hosting provider running that Docker host is unconfirmed and is the real unlisted party. OpenAI's API terms state customer data isn't used to train their models by default, but this should be confirmed in writing (DPA or documented terms), not just assumed.

6. **Is a DPA needed with any vendor?** Yes. A DPA is needed with every processor handling recruiter personal data: OpenAI, Pinecone, Cohere, Calendly, Resend, and Cloudflare if it logs any identifiable traffic data. n8n itself does not need a DPA since it is self-hosted, not a vendor processing data on John's behalf; whichever infrastructure provider hosts the Docker host does need one once identified. None are currently confirmed in place.

## Section C - Law stacking

- **AI Act cross-check:** Limited risk / Article 50 transparency. The AI Act adds a disclosure obligation (tell users it's AI) that GDPR doesn't require on its own; GDPR separately requires consent and a privacy notice for the data processing itself.
- **ePrivacy check:** Currently no cookies or tracking pixels in the custom chat UI code, though the third-party `@n8n/chat` widget's internal storage behavior hasn't been verified. Plan is to add basic analytics to the site later, not ad-tracking or marketing/sales pixels. If analytics cookies are added, ePrivacy consent will be required before they load, separate from the GDPR chat opt-in.
- **Data Act check:** N/A. No connected product or cloud-switching data involved.

---

# Client recommendation memo

**TO:** John Adams
**RE:** GDPR Audit, Virtual Coffee Chat Bot

**Bottom line: Go, with conditions.** The system itself is low risk. It doesn't score or profile recruiters, doesn't make automated decisions about anyone, and isn't public yet. But it cannot launch as-is. Right now there is no opt-in for logging, no retention policy, and no confirmed data processing agreements with the vendors handling recruiter data. These are fixable gaps, not reasons to stop the project, but they have to close before a real recruiter ever types into this bot.

**Top three actions:**

1. **Confirm DPAs, and pin down the full vendor list, before anything else.** OpenAI, Pinecone, Cohere, Calendly, Resend, and Cloudflare (if it logs identifiable traffic) each need a signed DPA. n8n itself doesn't need one, since it's self-hosted in Docker and never sends data to an n8n-the-company entity, but whoever hosts that Docker instance does, and that provider hasn't been identified yet. Get written confirmation that OpenAI's API terms exclude this data from their own model training. This has to come first, since the DPIA below depends on knowing each vendor's transfer route and retention terms.
2. **Build a two-part opt-in: legitimate interests for answering the message, consent for logging.** Processing the recruiter's own question to answer it runs on legitimate interests, not consent, since consent has to be freely withdrawable and the bot can't un-process a message it's already answering. Logging the conversation for training and improvement is a separate, lower-expectation purpose and needs its own clear consent line, captured at first message but not bundled with the Article 50 "this is AI" disclosure or a general T&Cs agreement.
3. **Complete a DPIA before public launch, once the vendor picture above is settled.** The system logs every turn of a service the user actively opted into, so "systematic monitoring" in the strict sense is a stretch; the stronger trigger is that this is an AI system that steers the interaction with the data subject. Either way it clears the bar for requiring a DPIA before this goes live.

**Residual risks:**

- Recruiters can type sensitive personal information into open chat text (health conditions, accommodations) that the bot never asks for and cannot reliably block. This risk cannot be fully removed in a free-text system, only monitored.
- Third-party infrastructure logging, including Cloudflare and the embedded `@n8n/chat` widget, has not been fully audited. Some data handling may stay outside direct visibility even after every fix above is made.
- Writing a retention policy is easier than enforcing it. Deleting data across every processor on request is an operational burden that will need a real process, not just a documented intention.

---

# Phase 4: Partner swap and peer review

Reviewing Gordan's memo (`recommendation memo.md`) on the same scenario.

| Criterion | Score 1-3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go, with conditions" stated in the first line, with the reason attached immediately. No ambiguity. |
| Lawful basis selection is justified | 2 | Never names or justifies a lawful basis (consent, legitimate interests, etc.) under Article 6. Jumps straight to controls (DPAs, notices, retention) without saying what basis those controls are supporting. |
| Top actions are specific and sequenced | 3 | Concrete: named vendors, specific retention numbers (30/90 days), and catches that Pinecone's `deleteAll` rebuild doesn't touch transcripts, a real technical detail. Clearly sequenced with reasoning for the order. |
| Residual risks are named honestly | 2 | Genuinely honest in shape (says outright that erasure can't be fully delivered once data hits OpenAI's abuse-monitoring logs), but backs the US-transfer risk with a specific case number and a dated EDPB letter that can't be verified. Overclaiming legal specificity on an unverified point undercuts an otherwise strong section. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | AI Act addressed directly (Article 50, dated). ePrivacy is not mentioned at all, despite this being a public web widget where cookies/analytics is the natural next question. |

**Total: 12/15**

**Client reaction:** Flagging one section before I can accept this. The residual risks section cites a specific CJEU case number and an EDPB letter with a date, and I can't verify either exists. If they're real, cite the source; if not, drop the specific numbers and state the risk in plain terms, that US adequacy could shift and DPAs would need to move to SCCs. The rest of the memo is strong and I'd act on it as written, but I don't want to circulate a legal citation internally that hasn't been checked.

---

## CFU 5 - Debrief

**Where we agreed:**
- Bottom line: both audits landed on "go, with conditions." Nothing about the bot's design is unlawful; the gaps are missing paperwork and configuration (consent, DPAs, retention), not a reason to kill the project.
- DPIA need: both flagged that the system needs review before public launch, though Gordan's memo didn't name the DPIA or EDPB criteria explicitly the way this audit did.
- Vendor exposure: both identified the same core vendor list as unpapered (no DPAs in place) and both flagged that erasure is harder in practice than "delete the data" implies.

**Where we diverged, and which reading is stronger:**

- **Lawful basis.** This audit named consent under Article 6 and explained why, split per purpose. Gordan's memo never named a lawful basis at all, it moved straight to controls (DPAs, notices) without stating what legal basis those controls support. Stronger reading: this audit's. A GDPR audit has to answer the Article 6 question directly, not just describe good data hygiene.
- **Where erasure actually breaks down.** Gordan's memo flagged Pinecone's `deleteAll` rebuild as looking like deletion but not touching transcripts. On debrief, this was corrected: Pinecone only ever stores John's own career/knowledge-base data, not recruiter chat content, so it was never the erasure mechanism in the first place. The real gap is the same conclusion by a different route: there is no deletion path for the n8n `chat_log`/`error_log` Data Tables, which is where recruiter data actually lives. Stronger reading: this audit's correction, but Gordan's memo is what surfaced the question worth asking.
- **OpenAI's own retention clock.** Gordan's memo raised that OpenAI holds API traffic on its own abuse-monitoring retention window (around 30 days) independent of whatever retention policy John sets, unless zero-data-retention is negotiated. This audit's original worksheet did not raise this. Stronger reading: Gordan's. This needs to be checked directly with OpenAI and added as a residual risk, since it means "we deleted it" may not be fully true even after John's own systems comply.
- **Email relay abuse.** Gordan flagged that the bot sends email to an address a stranger typed, unverified, and called it out as outside strict privacy scope but worth raising. This audit did not include it. Stronger reading: Gordan's, it's a real operational risk (domain abuse, spam relay) adjacent to the privacy review, worth carrying forward even if it's not a GDPR finding proper.
- **ePrivacy / cookies.** This audit addressed ePrivacy directly (no cookies currently, analytics planned later, consent will be needed then). Gordan's memo didn't mention ePrivacy at all. Stronger reading: this audit's, since the rubric explicitly asks for law stacking to cover both AI Act and ePrivacy.
- **Unverified legal citations.** Gordan's memo cited a specific CJEU case number and a dated EDPB letter to support the US-transfer risk. Neither could be verified. Agreed on debrief that the underlying risk (US adequacy could shift) is legitimate to flag, but it should be stated as a directional risk, not dressed with unconfirmed legal specifics.

**Net result:** two follow-ups carried into this audit that weren't there originally: (1) confirm OpenAI's own data retention window and whether zero-data-retention is available, and (2) flag the unverified email address / relay abuse risk as an operational item alongside the GDPR findings. No changes made to the worksheet or memo text itself; captured here as the debrief output per the lab instructions.

---

## Gordan's peer review of this memo (`peer-review-coffee-chat-bot.md`)

Gordan scored `Client Recommendation Memo - John Adams.md` at **12/15**. Full rubric and his client-reaction note are in that file. Two of his findings were corrections to the underlying analysis, not just style notes, and were applied directly to Section A, Section B, and the memo above rather than only logged here:

- **Lawful basis for the chat itself.** Gordan's strongest point: consent doesn't fit for answering a recruiter's own message, because consent has to be freely withdrawable, and there's no coherent way to un-process a message the bot is already answering mid-conversation. Legitimate interests is the correct basis for that purpose, with consent reserved for logging/training and for booking/email, which are separate, affirmative asks. This audit's original worksheet named consent for all three purposes; that was wrong, and has been corrected throughout Section A, Section B, and the memo.
- **n8n on the vendor list.** Gordan pointed out that self-hosted n8n running in Docker never sends data to an n8n-the-company entity, so it shouldn't be listed as a third-party processor alongside OpenAI or Pinecone. The real gap is that the actual Docker hosting provider was never identified or added to the vendor list. Corrected: n8n removed from the processor/DPA lists, hosting provider flagged as unconfirmed and outstanding.
- **DPIA justification.** Gordan argued the original "systematic monitoring" framing was a stretch for a service the user opted into, and that the stronger trigger is that this is an AI system steering the interaction with the data subject. Reflected in the memo's DPIA action item.
- **ePrivacy gap on the widget.** Gordan flagged that the `@n8n/chat` widget writes a session identifier to browser localStorage (`n8n-chat/sessionId`), which engages ePrivacy Article 5(3), something this audit's Section C did not catch since it only checked for cookies, not localStorage. Not yet fixed in the worksheet; carried forward as an open item, since it needs direct verification of the widget's actual storage behavior before writing a firm conclusion.

Not corrected, left as-is: Gordan disputed the DPIA action's original sequencing (DPIA before DPAs); the memo already listed DPAs first in the "top three actions," so this was already consistent with his point once the numbering is read in order rather than by label.
