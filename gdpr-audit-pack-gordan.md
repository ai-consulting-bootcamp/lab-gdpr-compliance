# GDPR Audit Pack: Virtual Coffee Chat Bot

**Auditor:** Gordan
**System:** [Virtual Coffee Chat Bot](https://github.com/jp92672/johna-project3-week6-virtural-coffee-chat-bot), John Adams, Project 3 Week 6
**Date:** 19 August 2026
**Contents:** Transition note · Fact pattern · Recognize · Audit worksheet (Sections A, B, C) · Client recommendation memo

> **Assumptions flagged for confirmation before this goes to a real client**
> 1. The controller is established in Germany. This matters: it decides whether the DSK "Muss-Liste" makes a DPIA mandatory (Section B).
> 2. The AI Act tier assigned in the previous lab was limited risk / transparency risk. If the partner lab recorded a different tier, replace the Section C line.
> 3. No DPA has been executed with any vendor yet, and no retention rule is configured on the Data Tables. Both are inferred from the repo showing no such artefact. Confirm with the client rather than assuming.

---

## Transition note

The EU AI Act lab classified this system by risk tier. That analysis asked what the system is. This one asks whose data it touches and on what legal footing. The Virtual Coffee Chat Bot is the more interesting of the two partner cases for GDPR because its AI Act profile is comparatively light while its data protection profile is not: it is publicly reachable, it accepts unbounded free text from third parties, it logs every turn, it ships that text to five non-EU vendors, and it can act in the world by sending email and booking calendar slots without a human between the request and the action. Low AI Act tier, real GDPR surface. That gap is exactly the pattern a client misreads.

---

## Fact pattern

The client is a sole operator, an individual job seeker running a public-facing chatbot as a career tool with no employees, no DPO and no legal function. The bot is a RAG agent built on self-hosted n8n. Its knowledge base holds the client's own CV, CliftonStrengths profile, career narrative and prepared recruiter answers. Anyone can open the widget: the intended data subjects are recruiters and hiring managers, assumed to be predominantly EU and EEA based with a realistic share in the US and UK. Every turn is logged to a `chat_log` Data Table with the question, the answer and thumbs feedback; failures are logged to `error_log` and emailed to the client. The agent has five tools, including Calendly availability and booking, and outbound email through Resend sent on the end user's behalf. Personal data leaves the EU to OpenAI, Pinecone, Cohere, Calendly and Resend, plus the hosting and tunnel layer. No decision about the end user is produced: the system answers questions and executes what the user asks for.

**Household exemption check.** Article 2(2)(c) does not rescue this. The processing is published to an indeterminate group of third parties on the open internet and serves a professional purpose, which is the *Lindqvist* and *Ryneš* line. GDPR applies in full.

---

## CFU 1: Recognize

**Categories present:** identity and contact data (booking name and email, recipient address), employment and CV data about the client, psychometric profile data about the client (CliftonStrengths), free-text conversation content from end users, generated output about a named individual, interaction metadata (session ID, timestamps, thumbs feedback), technical data at the hosting and tunnel layer (IP, user agent), and error payloads that can contain fragments of the above.

**Article 9:** none by design. Two live inference paths. First, end users type into an open box and can volunteer health, religion, union membership or political views, none of which the client asked for and none of which he has an Article 9 condition to process. Second, the `kb/narrative` content is written by the client about himself and may reveal Article 9 categories depending on what the career story says. That one is checkable: read the files.

**Border crossing:** yes, on every single turn. There is no path through this system that keeps personal data inside the EEA, because retrieval, embedding, reranking and generation all sit with non-EU vendors.

---

## CFU 2: Apply

### Section A: Data map

**A0. Lab worksheet format.** The seven required fields, answered directly. Purposes are numbered P1 to P7 and the same numbering is used in every row below, so basis, retention and recipients line up by index. The expanded grid in A1 to A3 is the working detail behind these answers.

| Field | Your answer |
|---|---|
| Categories of personal data | **About the client:** CV and employment history, education, psychometric profile (CliftonStrengths), career narrative, prepared recruiter answers. **About end users:** free-text message content and anything volunteered inside it, generated answers referring to a named person, session ID, timestamps, thumbs feedback, booking name and email, selected slot and invitee notes, outbound email recipient and body, error payloads containing request fragments, IP and user agent at the hosting layer. No special-category data by design; incidental Article 9 content is possible in free text. |
| Sources (where data comes from) | Client directly (`kb/facts`, `kb/narrative`). End user directly (chat box, Calendly invitee fields, email tool inputs). System-generated (model output, `chat_log`, `error_log`). Observed at infrastructure level (webhook, tunnel and hosting logs). No third-party or scraped sources. |
| Purpose(s), one row per purpose | **P1** answer the user's question from the knowledge base. **P2** log conversations and feedback for quality. **P3** check availability and book a call. **P4** send an email on the end user's behalf. **P5** error logging and alerting. **P6** publish the client's own CV and narrative through the bot. **P7** any reuse of transcripts as training or tuning data (not currently done). |
| Lawful basis per purpose, or `TBD - legal review` | **P1** Art. 6(1)(f), the user initiated the exchange and the message cannot be answered without processing it. **P2** Art. 6(1)(f), weakest basis in the set, valid only with notice, short retention and a working objection route. **P3** Art. 6(1)(b) pre-contractual steps, fallback 6(1)(f), since a coffee chat is arguably not a contract. **P4** Art. 6(1)(f), same requested-action logic as P3 but weaker balancing because the address is unverified. **P5** Art. 6(1)(f), service integrity, Recital 49. **P6** Art. 6(1)(f), client is controller and data subject, so consent to oneself is not meaningful. **P7** `TBD - legal review`, a new purpose that would fail the Art. 6(4) compatibility test. |
| Retention period per purpose | **Today: none configured on any store, which is the single worst finding in this map.** Recommended: **P1** duration of the turn. **P2** 30 days on `chat_log`, then delete or strip identifiers. **P3** aligned to documented Calendly settings. **P4** 30 days on Resend logs. **P5** 90 days on `error_log`, payloads truncated. **P6** while the bot is live. Retention must be automated, not remembered. |
| Recipients and sub-processors | OpenAI (generation and embeddings), Pinecone (vector store), Cohere (reranking), Calendly (scheduling), Resend (email delivery), hosting and tunnel provider for the self-hosted n8n instance and static chat UI. Each carries its own sub-processor chain, notably OpenAI's cloud infrastructure providers and Calendly's published sub-processor list, authorised generally and not inspectable by the client. No DPA executed with any of them today. |
| International transfers and transfer mechanism | Transfer to the US occurs on every turn; no EEA-only path exists through this system. Resend is certified under the EU-US DPF and the UK extension. Cohere may be reachable through the Canadian adequacy decision depending on entity and region, with SCCs in its DPA for the US route. OpenAI, Pinecone and Calendly: verify DPF certification on the US Commerce Department participant list, otherwise SCCs plus a transfer impact assessment. Record the date checked. DPF is valid today but under review: appeal pending in C-703/25 P and the EDPB letter of 31 July 2026 asking the Commission to reassess adequacy. |

**A1. Categories and sources**

| Category | Source |
|---|---|
| CV, employment history, education, psychometric profile, career narrative (all about the client) | Client, via `kb/facts` and `kb/narrative` |
| Free-text questions and any personal data volunteered inside them | End user, directly |
| Generated answers about a named individual | System output |
| Session ID, timestamps, thumbs up/down | System, via widget and `chat_log` |
| Booking name, email, selected slot, invitee notes | End user, via Calendly |
| Recipient address and message body for outbound mail | End user, via the email tool |
| Error payloads containing request fragments | System, via `error_log` |
| IP address, user agent, connection logs | End user's device, via hosting and tunnel layer |

**A2. Purposes, lawful basis, retention, recipients, transfers**

| # | Purpose | Lawful basis (Art. 6) | One-line justification | Retention today | Retention recommended | Recipients |
|---|---|---|---|---|---|---|
| P1 | Answer the user's question from the knowledge base | 6(1)(f) legitimate interests | The user initiated the exchange and the message cannot be answered without processing it; consent would be misleading because processing is unavoidable to deliver what was asked for | Not defined | Duration of the turn | OpenAI, Pinecone, Cohere |
| P2 | Log conversations and feedback for quality improvement | 6(1)(f) legitimate interests | Improving answer quality is a real interest, but it is the client's interest and not the user's, so it needs notice and a working objection route | None configured | 30 days, then delete or strip identifiers | n8n Data Tables (self-hosted) |
| P3 | Check availability and book a call | 6(1)(b) pre-contractual steps, fallback 6(1)(f) | The user asked for the meeting, so processing is necessary to take the step they requested; (b) is arguable because a coffee chat is not a contract, which is why the fallback is stated | Calendly account defaults | Align to Calendly retention settings, documented | Calendly |
| P4 | Send an email on the end user's behalf | 6(1)(f) legitimate interests | Same requested-action logic as P3, but the balancing is weaker because the address is unverified (see Section B risk) | Resend log defaults | 30 days | Resend |
| P5 | Error logging and alerting | 6(1)(f) legitimate interests | Recital 49 supports processing for service integrity; payloads must be truncated so this does not become a shadow transcript store | None configured | 90 days | n8n Data Tables, Resend for the alert mail |
| P6 | Publish the client's own CV and narrative through the bot | 6(1)(f) legitimate interests | The client is both controller and data subject here; consent to oneself is not a meaningful legal basis | Ongoing | While the bot is live | OpenAI, Pinecone, Cohere |
| P7 | Any reuse of transcripts as training or tuning data | `TBD - legal review` | Not currently done. If it ever is, it is a new purpose and fails the Article 6(4) compatibility test on its own facts | n/a | n/a | n/a |

**LIA note for P2, the weakest basis.** *Purpose:* improve answer quality and catch failures. *Necessity:* partly. Aggregate feedback counts and truncated turns would achieve most of it; storing full transcripts indefinitely is more than necessary. *Balancing:* users do not expect a job-search chatbot to keep a permanent record of what they typed. This tips to acceptable only with clear notice at the entry point, a short retention window, and a working opt-out. Without those three, P2 fails.

**A3. International transfers**

| Vendor | Role | Transfer basis to verify | Note |
|---|---|---|---|
| OpenAI | Processor | DPF certification, otherwise SCCs in the OpenAI DPA | The DPA must be actively executed from a business account. There is no consumer DPA. API data is not used for training by default, but inputs and outputs sit in abuse-monitoring logs for up to 30 days unless Zero Data Retention is approved |
| Pinecone | Processor | DPF or SCCs; DPA requested through their security centre form | Index region also determines where vectors rest |
| Cohere | Processor | Canadian adequacy decision may cover the Canadian entity; SCCs are in their DPA for the US route | Zero data retention is available on request and would remove reranked chunks from their logs |
| Calendly | Processor for booking data, arguably controller for its own platform purposes | DPF or SCCs; published sub-processor list | The dual role is the one to check, not assume |
| Resend | Processor | Certified under the EU-US DPF and the UK extension | The cleanest transfer position in the stack |
| Hosting and tunnel provider | Processor | Depends on provider and region | Often forgotten in student audits and in real ones |

Verify each certification on the US Commerce Department DPF participant list rather than on the vendor's own marketing page, and record the date checked.

### Section B: Risk and rights

**Special-category data.** Not by design, non-trivial by accident. The open text box is the exposure: a recruiter can disclose a disability, a religious employer, or union involvement in one sentence, and there is no Article 9 condition covering it. Mitigation is a warning at the entry point, a system prompt instruction not to solicit or repeat such information, and short log retention. Separately, `kb/narrative` should be read for Article 9 content about the client himself.

**Article 22.** No, and the reasoning matters more than the verdict. The agent produces no decision about the end user. It answers questions about a third party (the client), and the only consequential decision in the picture, whether to hire, is made by the human recruiter outside the system. *SCHUFA* (C-634/21) extended "decision" to scoring that another party predictably relies on, but there is no scoring of the end user here at all. The boundary is worth naming: if the bot ever ranked, filtered or triaged which enquiries get a calendar slot, this answer flips.

**DPIA.** Two routes, and they disagree.

Against the EDPB nine criteria: innovative use of new technology (yes), sensitive or highly personal data (partial, incidental only), systematic monitoring (weak, the logging is of a service the user opted into, not surveillance). Evaluation and scoring, automated decisions, large scale, dataset matching, vulnerable subjects, and blocking access to a service are all no. That is roughly one solid criterion plus two partials, short of the usual two-criteria rule of thumb, so a DPIA is not clearly mandatory on the EDPB test alone.

Against the German position: the DSK "Muss-Liste" (v1.1) item 11 requires a DPIA for the use of AI to process personal data in order to steer the interaction with data subjects or to evaluate personal aspects of them. A public chatbot that conducts the interaction is squarely within the first limb. If the controller is established in Germany, the DPIA is mandatory and the EDPB count is irrelevant.

**Conclusion:** treat it as required. Even if the client sits outside Germany, Article 35(1) is a risk test rather than a checklist, and a two-page assessment costs less than defending the decision not to do one. Document the negative threshold analysis either way.

**Data subject friction points.**

1. *Identification.* The widget collects no identity. Transcripts are keyed to a session ID held in the browser. An access request from "the person who chatted with you on Tuesday" may be unmatchable, which is Article 11 and 12(2) territory. The client must not solve this by collecting more identity data than the service needs.
2. *Erasure.* Deleting a `chat_log` row does not reach OpenAI's abuse-monitoring logs, Resend's delivery logs, or Calendly's event record. The Pinecone rebuild wipes and recreates the index, which handles the knowledge base but touches no user data at all, so it looks like an erasure mechanism and is not one.
3. *Objection to logging.* Because P2 rests on legitimate interests, Article 21(1) gives an absolute-in-practice route to stop it, and there is no switch in the current build to honour it.
4. *Rectification.* Cheap and worth stating: if the bot states something wrong about the client, fixing the KB and re-running ingestion is a two-minute fix. Not every finding is bad news.

**Controller and processor split.**

| Entity | Role |
|---|---|
| John Adams (operator) | Controller for all seven purposes |
| OpenAI | Processor |
| Pinecone | Processor |
| Cohere | Processor |
| Resend | Processor |
| Calendly | Processor for the booking, likely independent controller for its own platform and analytics purposes |
| Hosting and tunnel provider | Processor |
| Recruiter's employer | Not a party. The recruiter acts as an individual here |

**DPAs needed.** All processors above: OpenAI, Pinecone, Cohere, Resend, Calendly and the hosting provider. Article 28(3) requires them in writing before processing, not after. The one to look at carefully is Calendly, where a pure processor assumption may be wrong and a controller-to-controller position changes what the client can promise users.

### Section C: Law stacking

**AI Act cross-check.** Limited risk / transparency tier, assumed carried over from the AI Act lab. Not Annex III high risk: the system is not used by an employer to evaluate candidates, it answers questions about one candidate. Article 50(1) still adds an obligation GDPR does not: users must be told they are interacting with an AI system unless it is obvious from context. That duty has applied since 2 August 2026 and was deliberately left out of the Digital Omnibus deferral that pushed the high-risk deadlines to December 2027, so it is live today and enforceable by national authorities.

**ePrivacy check.** Yes, engaged. `@n8n/chat` writes a session identifier to browser localStorage under the `n8n-chat/sessionId` key, which is storage of and access to information on the user's terminal equipment under Article 5(3) ePrivacy, implemented in Germany as section 25 TDDDG. The likely correct answer is that it falls within the strictly-necessary exemption because the session identifier is required to deliver the chat the user asked for, so no consent banner is needed. That conclusion holds only if nothing else is stored and no analytics, fonts or CDN calls with tracking capability ride along. Verify in the browser, one minute of work, and document it. If anything non-essential is present, ePrivacy consent applies and GDPR legitimate interests cannot substitute for it.

**Data Act check.** N/A. No connected product data, no IoT telemetry, no cloud switching scenario. The self-hosted n8n instance is infrastructure the client already controls.

---

## CFU 3: Integrate. Client recommendation memo

**To:** John Adams, operator, Virtual Coffee Chat Bot
**From:** Gordan, GDPR audit
**Date:** 19 August 2026
**Re:** Can this go live and stay live

**Bottom line: go, with conditions.** Nothing in the design is unlawful, but the widget is public, it sends recruiter conversations to five non-EU vendors with no processor contracts in place, and nothing deletes anything. Those are paperwork and configuration gaps, fixable in a week.

**Three actions, in this order.**

1. **Paper the vendors before the widget is public again.** Execute DPAs with OpenAI, Pinecone, Cohere, Calendly, Resend and your hosting provider. Record each one's transfer route, DPF certification or standard contractual clauses, checked against the Commerce Department list rather than the vendor's website. Ask OpenAI and Cohere for zero data retention while you are in there.
2. **Put a notice and an AI disclosure at the chat entry point.** Who the controller is, that every turn is logged, which vendors receive the text, how long it is kept, and how to object or ask for deletion. Add one line asking users not to type sensitive personal information, and repeat it in the system prompt. The AI disclosure is separately mandatory under Article 50 of the AI Act, which has applied since 2 August 2026.
3. **Set retention and a deletion path.** Thirty days on `chat_log`, ninety on `error_log`, automated rather than remembered. Add a documented way to remove one person's turns. The Pinecone rebuild looks like a deletion mechanism and is not one: it never touches transcripts.

**Residual risks after all three are done.**

*US transfers stay legally exposed.* The Data Privacy Framework is valid today, but the appeal in C-703/25 P is pending at the Court of Justice and the EDPB asked the Commission on 31 July 2026 to re-examine adequacy after the Supreme Court's ruling on FTC independence. If adequacy falls you re-paper onto standard clauses with a transfer assessment per vendor.

*Free text cannot be controlled.* A recruiter can type health or union information into the box in one sentence. You can warn, minimise and delete quickly. You cannot prevent it, and you have no Article 9 condition for it if it arrives.

*Erasure is only partly deliverable.* Once a turn reaches OpenAI's abuse-monitoring logs it sits on their thirty-day clock, not yours, unless zero data retention is approved. Promise users what you can actually execute.

Outside privacy scope but raising it anyway: the bot emails using an address a stranger typed, unverified. Add rate limiting and confirmation before someone uses your domain as a relay.

*(Memo body: 399 words)*

---

## CFU 4: Verify

Peer review of the partner memo goes in `peer-review-coffee-chat-bot.md`, using the Phase 4 rubric plus the client-voice response. Pending the swap.

## CFU 5: Debrief

Completed after the swap. Both audits covered the same system, so divergence here is about legal reading rather than about facts.

### Where the two audits agreed

- **Bottom line.** Both landed on go with conditions, and for the same underlying reason: the system design is sound and the governance layer was never built. Neither of us treated the AI itself as the problem.
- **No Article 22.** Neither audit found automated decision-making with legal or similarly significant effects. The partner memo put it in one line, "it doesn't score, rank, or decide anything about a recruiter", which is the correct test stated more economically than mine.
- **Vendor paperwork is the first action.** Both put DPAs and transfer routes ahead of everything else, and both flagged that OpenAI's no-training position needs to be contractual rather than a default.
- **Retention is the cheapest high-value fix**, and free text is the risk that cannot be engineered away.

### Where the two audits diverged

**1. Lawful basis for the conversation itself. The real disagreement.**

The partner memo proposes a consent opt-in at the first message. This audit uses Article 6(1)(f) for delivery and treats consent as unworkable for that purpose. Stronger reading: legitimate interests. Consent must be freely given and withdrawable without detriment, and here the processing of the message is unavoidable to answer it, so a withdrawal mid-conversation leaves the service with no lawful way to complete an action the user asked for. That is the classic case where the EDPB says consent is the wrong instrument.

Where the partner reading is stronger, and this audit has been corrected on it: the partner separates permission-to-log from the Article 50 AI disclosure and argues that bundling two different asks into one line is how consent gets challenged later. That is right, and it is sharper than the single entry-point notice recommended in the memo above. **Agreed final position: legitimate interests for delivery (P1, P3, P4, P5), a separate and specific consent or clearly signposted objection route for logging (P2), and the Article 50 disclosure kept distinct from both.**

**2. Why a DPIA is required. Same conclusion, different route.**

The partner memo counts three EDPB triggers: logging every turn, novel AI/RAG technology, and a volume jump on going public. This audit counts one solid criterion and two partials, short of the usual two-criteria threshold, and reaches "required" through the German DSK Muss-Liste item 11 instead, which mandates a DPIA for AI used to steer the interaction with data subjects.

Stronger reading: the DSK route, on the condition that the controller is established in Germany. The partner's "systematic monitoring" trigger is the weak link, because logging a service the user deliberately opened is not monitoring in the WP248 sense, and this system will never be large scale. Both audits get to the same answer, but only one of them survives a regulator asking why.

**3. Who the processors are. Both audits got this partly wrong, in opposite directions.**

The partner memo lists n8n as a vendor, which is incorrect for a self-hosted Docker deployment where n8n GmbH receives nothing, and omits the actual hosting provider. This audit lists the hosting provider but never established what the Cloudflare tunnel logs on its own side. **Agreed final position: n8n comes off the processor list, the hosting provider and the tunnel provider go on it, and the tunnel's own logging is an open item rather than a closed finding.**

**4. Unresolved: Calendly's role.** Processor for the booking, or independent controller for its own platform purposes. Neither audit settled it, and it changes what the privacy notice can truthfully promise. Carried forward as `TBD - legal review`.

### Process note

The lab asks partners to agree a shared fact pattern before building. In practice this audit was built from the partner's public repository rather than from a jointly written paragraph. It worked because the repository documentation is unusually complete, but it is why the two audits diverged on the processor list: neither of us had confirmed the deployment and hosting facts with the other before writing. Agreeing the fact pattern first would have caught it in five minutes.
