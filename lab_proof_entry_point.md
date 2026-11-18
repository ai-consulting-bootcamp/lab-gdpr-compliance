# Lab Proof: GDPR & AI Act Parallel Audit Workflow

**Repository Entry Point** | **Scenario:** Option B(a) — Fine-tuning an LLM on B2B Support Chat Logs  

I completed this audit workflow with my study partner. We worked from the same CloudFlow fact pattern, compared our legal readings, and reviewed the recommendation from the client's perspective.

---

## 1. Workflow Export

I used the following workflow with my study partner to audit **CloudFlow GmbH**'s proposed LLM fine-tuning pipeline across GDPR, the EU AI Act, and ePrivacy frameworks:

```text
[1. Fact Pattern & Data Ingestion Mapping]
       │  (180k Zendesk tickets, EU/EEA B2B users, US LLM API vendor)
       ▼
[2. Lawful Basis & Article 9 Screening]
       │  (Evaluating Art. 6(1)(f) LIA vs. Unstructured Free-Text Risks)
       ▼
[3. International Transfer & Processor Split]
       │  (Controller: CloudFlow ──► Sub-processors: Zendesk & US AI Vendor)
       ▼
[4. DPIA & EDPB 9-Criteria Assessment]
       │  (3 Criteria Triggered: New Tech, Large Scale, Evaluation/Scoring)
       ▼
[5. Law Stacking Cross-Check]
       │  (GDPR + EU AI Act Art. 50/53 + ePrivacy Art. 5(3) Session Metadata)
       ▼
[6. Client Memo, UK GDPR Extension & Data Protection by Design Checklist]
```

---

## 2. Audit Query & Input (Fact Pattern)

* **Audit Query:** Can a mid-size German B2B SaaS provider lawfully export two years of historical live customer support chat logs ($180,000$ tickets) to a US-based AI vendor to fine-tune a proprietary customer service LLM, and deploy that model to triage incoming EU support tickets?
* **Input Fact Pattern:** 
  > CloudFlow GmbH is a mid-size B2B SaaS workflow automation company (approx. 220 employees) headquartered in Berlin, Germany. CloudFlow wants to fine-tune a foundation model on two years of historical live support conversations ($180,000$ chat transcripts containing roughly $45,000$ unique data subjects) to build an automated tier-1 customer support assistant. The dataset includes end-user full names, corporate email addresses, IP addresses, browser metadata, account role titles, and free-text complaint transcripts. Data subjects are employees and contractors of CloudFlow's enterprise customers located across the EU/EEA. The technical stack routes chat logs from Zendesk (CRM processor) to a US-based LLM fine-tuning provider (ApexAI Inc., hosted on AWS US-East) via API. The resulting fine-tuned model will generate automated troubleshooting responses and assign priority urgency scores to tickets, though a human support engineer handles escalations and account termination decisions.

---

## 3. Evidence Produced (Our Audit Findings Summary)

1. **Purpose Separation & Lawful Basis Split (Section A):** 
   * Live chat resolution relies on **Legitimate Interests** (Art. 6(1)(f)) because B2B end-users expect issue resolution under their employer's SaaS contract.
   * However, **retroactive LLM fine-tuning** on two years of raw historical logs faces a severe Art. 6(1)(f) Balancing Test hurdle and Purpose Limitation challenge (Art. 5(1)(b)). It requires mandatory pre-training PII scrubbing/pseudonymisation, an updated notice, and an immediate opt-out mechanism before relying on Legitimate Interests.
2. **DPIA Trigger & Unstructured Special Category Data (Section B):**
   * **EDPB Criteria Met:** (1) Innovative use of new technological solutions (LLM weight updates on conversational logs), (2) Data processed on a large scale ($180,000$ transcripts), and (3) Evaluation or scoring (automated ticket urgency profiling).
   * **Article 9 Contamination:** Unstructured complaint logs contain incidental special-category disclosures (e.g., accessibility accommodations or medical leave mentions) and client credentials/API keys pasted during troubleshooting.
3. **Cross-Framework Law Stacking (Section C):**
   * **EU AI Act:** Classified as a **Limited Risk AI System** (Chatbot under Art. 50 requiring clear human-interaction disclosure) built on a **General-Purpose AI (GPAI)** model. Does not reach Annex III High-Risk tier because B2B support triage does not deny essential public/financial services.
   * **ePrivacy Directive:** Session replay scripts and diagnostic tracking cookies embedded in the chat widget fall under Art. 5(3) of the ePrivacy Directive, requiring prior consent before non-essential telemetry can be bundled into training data.

---

## 4. Final Output (Our Client Recommendation Executive Summary)

* **Bottom Line:** **GO WITH CONDITIONS** — You may proceed with fine-tuning the customer support LLM only after implementing an automated PII-scrubbing pipeline on the raw chat logs and locking down your US vendor contract and DPIA.
* **Top Three Sequenced Actions:**
  1. **Execute an AI-specific DPA and Transfer Impact Assessment (TIA) with ApexAI Inc.** (binding them to EU-US DPF / Module 2 SCCs and zero-retention on raw training payloads).
  2. **Deploy an automated PII redaction filter and complete a formal DPIA** before exporting any of the $180,000$ historical tickets.
  3. **Update the privacy notice, launch a 30-day retroactive opt-out window for historical tickets, and add an EU AI Act Art. 50 disclosure banner** in the live chat widget.

---

## 5. Issue Identified During Our Audit

### The "Machine Unlearning" & Weight Memorisation Bottleneck (GDPR Art. 17 vs. LLM Architecture)

* **The issue:** During Section B (Data Subject Rights) and the Stretch Checklist evaluation, we identified a critical technical-legal failure point: **Once personal data is baked into the neural network weights of a fine-tuned LLM, it cannot be surgically deleted upon receiving an Article 17 Right to Erasure request** without deleting the model and retraining it from scratch.
* **Why Standard Mitigations Failed:** Simply deleting a user's chat transcript from the Zendesk database and the AWS S3 staging bucket satisfies database erasure, but LLM fine-tuning carries a documented risk of *verbatim memorisation* (where specific prompt anomalies can cause the model to regurgitate an email address, name, or complaint snippet embedded in its parameters).
* **Remediation We Applied:** Because full model retraining every 30 days to honour individual erasure requests is economically unviable for a mid-size SaaS company, we changed the architectural requirements:
  1. Raw transcripts **must not** enter the fine-tuning loop; an upstream NER (Named Entity Recognition) & regex redaction layer must strip personal identifiers (`[REDACTED_NAME]`, `[REDACTED_EMAIL]`, `[REDACTED_KEY]`) prior to weight updates so the training dataset is strictly pseudonymised/anonymised.
  2. Output guardrails (inference-time PII filters) must be placed in front of the live chatbot as a secondary fail-safe to block any accidental regurgitation of residual identifying context.
