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
| Lawful basis per purpose | (1) Consent. Recruiter must opt in at the start of the chat, alongside the Article 50 AI disclosure. Not yet implemented; bot is currently testing-only. (2) Consent, layered on top of Purpose 1. Triggered only when the recruiter explicitly asks to book or message. Should be its own clear opt-in line, since it involves sharing their email with two more vendors (Calendly, Resend). (3) Consent. Logging happens automatically starting with the first message, so this consent must be captured in the same opening opt-in as Purpose 1, clearly labeled as its own line (e.g. "your chat may be logged and used to improve this assistant"), not buried inside a general T&Cs agreement. |
| Retention period per purpose | TBD - legal review. No retention policy currently exists for any purpose. All data is kept indefinitely by default. Must be defined before public launch. |
| Recipients and sub-processors | OpenAI, Pinecone, Cohere, Calendly, Resend, n8n (self-hosted), Cloudflare (tunnel, logging unclear). No DPAs confirmed with any of them yet. |
| International transfers and transfer mechanism | All vendors are non-EU (US: OpenAI, Pinecone, Calendly, Resend, Cloudflare; Canada: Cohere). Any EU-based recruiter's data leaves the EU immediately upon use. No transfer mechanism (e.g. Standard Contractual Clauses) has been reviewed or confirmed with any vendor. TBD - legal review. |

For the lawful basis column, all three purposes rely on consent (Article 6), captured through a single opening opt-in that must be granular and specific per purpose, not one blanket agreement.

## Section B - Risk and rights

1. **Special-category data present or inferable (Article 9)?** Low risk but not zero. The bot's guardrails prevent it from disclosing sensitive info about John (age, sex, religion), but nothing currently stops a recruiter from typing sensitive info about themselves into open chat text (e.g. a disability accommodation request). This is inferable, not solicited, and should be monitored rather than ignored.

2. **Automated decision-making with legal or similarly significant effects (Article 22)?** No. The bot only answers questions and books calls. It does not score, rank, or filter recruiters. Any pattern review (e.g. repeated errors on a topic) is manual, done by John on the logs, to improve the bot, not to make a decision about any person.

3. **Is a DPIA required?** Yes, a DPIA is likely required. At least three EDPB criteria apply: systematic monitoring (every turn logged), innovative technology (AI agent, RAG, cross-border processing), and large-scale processing once launched publicly. A DPIA should be completed before public launch, not after.

4. **Most likely data subject friction points?** Right of access ("what did you store about me?") and right to erasure ("delete my chat"). Right to object to profiling is not relevant, since the bot doesn't profile. No workflow currently exists to handle these requests. The intended design is that the bot never resolves these itself; it should flag the request and route it to John directly so it can be logged and manually actioned.

5. **Controller / processor split?** Controller: John Adams. He decides the purpose and means of processing (recruiting tool, training on feedback, etc.). Processors: OpenAI, Pinecone, Cohere, Calendly, Resend, n8n, Cloudflare, all acting on John's instructions with no independent purpose of their own. OpenAI's API terms state customer data isn't used to train their models by default, but this should be confirmed in writing (DPA or documented terms), not just assumed.

6. **Is a DPA needed with any vendor?** Yes. A DPA is needed with every processor handling recruiter personal data: OpenAI, Pinecone, Cohere, Calendly, Resend, and n8n (if using n8n Cloud; less clear for self-hosted). Cloudflare needs one if it logs any identifiable traffic data. None are currently confirmed in place.

## Section C - Law stacking

- **AI Act cross-check:** Limited risk / Article 50 transparency. The AI Act adds a disclosure obligation (tell users it's AI) that GDPR doesn't require on its own; GDPR separately requires consent and a privacy notice for the data processing itself.
- **ePrivacy check:** Currently no cookies or tracking pixels in the custom chat UI code, though the third-party `@n8n/chat` widget's internal storage behavior hasn't been verified. Plan is to add basic analytics to the site later, not ad-tracking or marketing/sales pixels. If analytics cookies are added, ePrivacy consent will be required before they load, separate from the GDPR chat opt-in.
- **Data Act check:** N/A. No connected product or cloud-switching data involved.

---

# Client recommendation memo

**TO:** John Adams
**RE:** GDPR Audit, Virtual Coffee Chat Bot

**Bottom line: Go, with conditions.** The system itself is low risk. It doesn't score or profile recruiters, doesn't make automated decisions about anyone, and isn't public yet. But it cannot launch as-is. Right now there is no consent flow, no retention policy, and no confirmed data processing agreements with any of the seven vendors handling recruiter data. These are fixable gaps, not reasons to stop the project, but they have to close before a real recruiter ever types into this bot.

**Top three actions:**

1. **Build an explicit, granular opt-in at the first message.** It must be separate from the AI Act Article 50 disclosure ("this is AI") and state clearly that chat content is logged and may be used to improve the bot. A single blanket "I agree to T&Cs" does not meet GDPR's bar for specific consent, since answering a question and training a model are two different purposes with two different expectations.
2. **Complete a DPIA before public launch.** The system already hits three of the EDPB's nine triggers: systematic monitoring (every turn logged), innovative technology (AI agent with RAG and cross-border processing), and large-scale processing once it goes live. That clears the threshold for requiring one.
3. **Confirm DPAs and set a retention policy.** Every vendor touching recruiter data (OpenAI, Pinecone, Cohere, Calendly, Resend, n8n, and Cloudflare if it logs identifiable traffic) needs a signed DPA. Get written confirmation that OpenAI's API terms exclude this data from their own model training. Set a defined retention window for chat logs, feedback data, and error logs; indefinite retention by default is not defensible.

**Residual risks:**

- Recruiters can type sensitive personal information into open chat text (health conditions, accommodations) that the bot never asks for and cannot reliably block. This risk cannot be fully removed in a free-text system, only monitored.
- Third-party infrastructure logging, including Cloudflare and the embedded `@n8n/chat` widget, has not been fully audited. Some data handling may stay outside direct visibility even after every fix above is made.
- Writing a retention policy is easier than enforcing it. Deleting data across seven separate vendors on request is an operational burden that will need a real process, not just a documented intention.

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
