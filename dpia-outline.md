# DPIA outline and Reinforce work

**System:** Virtual Coffee Chat Bot · 

**Auditor:** Gordan · 

**Date:** 19 August 2026
Companion to `gdpr-audit-pack-gordan.md`. This is an outline, not a completed DPIA.

---

## 1. DPIA outline: logging of free-text conversations and their transit to non-EU model vendors

This is the highest-risk activity in the scenario, not because any single field is sensitive, but because the content is unbounded, the retention is currently unlimited, and the data leaves the EEA on every turn.

### 1.1 Systematic description of the processing

- **What:** every chat turn (user message, generated answer, thumbs feedback, session ID, timestamp) written to `chat_log`. Each turn is also transmitted to OpenAI for embedding and generation, to Pinecone for retrieval, and to Cohere for reranking.
- **Who:** end users are recruiters and hiring managers, self-selected, unauthenticated. Volume is low, likely tens to low hundreds of conversations.
- **Controller:** the operator. **Processors:** OpenAI, Pinecone, Cohere, plus hosting.
- **Model and region:** `gpt-5-mini` and `text-embedding-3-small`, Pinecone index `curious-john` at dimension 512, Cohere `rerank-v3.5`. Record the region of each, since the DPIA has to say where data rests, not just who holds it.
- **Transfers:** US on every turn. Basis to be recorded per vendor, DPF certification or standard contractual clauses.
- **Retention:** none configured today. This is the single fact that makes the risk assessment come out badly, and the single cheapest thing to fix.

### 1.2 Necessity and proportionality

- Is the AI necessary for the purpose? For answering questions about a CV in natural language, yes. A static FAQ page would serve a narrower purpose but not the same one.
- Is the data minimum? No. Full-turn logging exceeds what quality improvement requires. Truncated turns or feedback counts alone would carry most of the value.
- Could it run locally? Partly. A self-hosted embedding model would keep retrieval inside the EEA, at a quality cost. Worth stating as the alternative considered and rejected, with the reason, because a DPIA that shows no alternatives were weighed reads as decoration.
- Is the lawful basis solid? Legitimate interests for delivery, weaker for logging. Documented LIA required for the logging purpose.

### 1.3 Risk identification

| Risk to the data subject | Likelihood | Severity |
|---|---|---|
| Special-category data volunteered in free text and stored without an Article 9 condition | Medium | High |
| Indefinite retention of an identifiable conversation about the user's employer or hiring plans | High today | Medium |
| Loss of confidentiality via the public webhook or an exposed Data Table | Low | High |
| Inability to satisfy an erasure request because copies sit with vendors | Medium | Medium |
| Inaccurate generated statements about a named person repeated to third parties | Medium | Medium |
| Transfer risk if DPF adequacy is annulled while transfers rely on it | Low to medium | Medium |

### 1.4 Measures to mitigate

Retention rules on both Data Tables. Truncation of error payloads. A do-not-enter-sensitive-data warning at the entry point and in the system prompt. Executed DPAs with recorded transfer routes. Zero data retention requested from OpenAI and Cohere. Documented subject-rights procedure including the identification problem. Basic Auth reviewed and rate limiting added on the public webhook. Residual risk after mitigation: acceptable, with the free-text and vendor-log items remaining as disclosed residuals.

**Consultation:** no DPO required under Article 37 on these facts. Views of data subjects under Article 35(9) can be met proportionately by asking two or three recruiters what they would expect. Cheap, and it is the step most people skip.

---

## 2. One DPA clause to insist on, with the main model vendor

**Clause: no training or model improvement on customer content, and abuse-monitoring logs excluded on request (zero data retention), with the retention period stated in the contract rather than in a policy page.**

Why this one. The entire audit rests on the assumption that recruiter conversations do not end up in a training corpus. Today OpenAI's position is that API inputs and outputs are not used for training by default and are retained up to thirty days for abuse monitoring, with zero data retention available to approved customers. "By default" and "policy page" are the weak words. A default can be changed unilaterally; a contractual term cannot. Without this clause the client cannot honestly describe purposes in the privacy notice, cannot bound retention in the record of processing, and cannot promise erasure. It is the clause that converts three separate compliance claims from hope into commitment.

Second choice if only one more is available: a sub-processor change notification term with a right to object, since the client is signing up to a chain he cannot inspect.

---

## 3. Bottom line rewritten for UK data subjects

**Assumption:** half the recruiters using the bot are in the UK.

**Revised bottom line: go with conditions, and the conditions grow by one.** UK GDPR mirrors the EU regime closely enough that the audit findings, the lawful bases and the DPIA reasoning all carry over unchanged. What changes is the transfer layer and the paperwork, not the analysis.

What actually moves:

1. **A second transfer route is needed.** EU standard contractual clauses do not work for UK exports. The client needs the UK International Data Transfer Agreement or the UK Addendum to the EU SCCs, or he can rely on a vendor's UK Extension to the DPF where it exists. Resend already holds the UK extension, which is a point in its favour; the others must be checked separately.
2. **A UK representative may be required.** Article 27 UK GDPR applies to controllers outside the UK offering services to UK data subjects. There is an exemption for occasional processing that is low risk and involves no special-category data at scale. A low-volume job-search chatbot has a decent argument for the exemption, but the argument has to be written down rather than assumed. Mark this `TBD - legal review`.
3. **Two regulators, not one.** The ICO joins the picture alongside the lead EU authority. There is no one-stop-shop between the two regimes, so a breach affecting both populations means two notifications, both within 72 hours.
4. **Watch the drift.** UK reform legislation has been steadily loosening parts of the UK regime relative to the EU. Anything written today as "UK GDPR is essentially the same" needs a review date attached, and the client should not build a process that assumes the two regimes stay aligned indefinitely.

Nothing here changes the go decision. It adds paperwork and a second regulator relationship, which is precisely the kind of thing a client would rather hear before the launch than after.
