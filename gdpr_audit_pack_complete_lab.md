# GDPR Audit Pack

**Selected Scenario:** Option B(a) — Fine-tune an LLM on support chat logs  
**Entry Point Link:** [lab_proof_entry_point.md](./lab_proof_entry_point.md)
**Collaboration:** I completed this audit with my study partner and compared our findings during the peer-review stage.

---

## Section 1: Audit Worksheet

### Phase 1: Fact Pattern & CFU 1 (Recognize)

#### Fact Pattern
CloudFlow GmbH is a mid-size B2B SaaS workflow automation company (approx. 220 employees) headquartered in Berlin, Germany. CloudFlow wants to fine-tune a foundation model on two years of historical live support conversations ($180,000$ chat transcripts involving roughly $45,000$ unique data subjects) to build an automated tier-1 customer support assistant. The raw dataset contains end-user full names, corporate email addresses, IP addresses, browser/device metadata, job titles, and unstructured free-text complaint and troubleshooting conversations. The data subjects are employees and contractors of CloudFlow's corporate clients located across the EU/EEA (with a recent expansion cohort in the UK). The technical stack extracts chat logs from Zendesk (CRM processor) and transmits them via API to a US-based AI vendor, ApexAI Inc. (hosted on AWS US-East in Virginia), for supervised fine-tuning and managed inference. The AI system will automatically classify incoming support tickets, assign urgency priority scores, and draft or send tier-1 troubleshooting responses to users. While the system triages ticket routing automatically, human support engineers review all billing disputes, SLA credits, and high-severity technical escalations, meaning there is no solely automated decision-making with legal or similarly significant effects.

#### CFU 1 — Recognize Checkpoint
1. **Categories of personal data present:**
   * *Direct identifiers:* Full names, corporate email addresses, user account IDs.
   * *Technical/device identifiers:* IP addresses, browser headers, session cookie IDs.
   * *Professional profile data:* Company name, job role/title, system permissions level.
   * *Unstructured behavioural/conversational data:* Two years of free-text customer support complaints, timestamps, frustration sentiment, and pasted troubleshooting logs.
2. **Special-category data (Article 9) inferred or included:**
   * While CloudFlow does not *intentionally* collect Article 9 data, two years of unstructured free-text chat logs almost certainly contain **incidental Article 9 disclosures**. Examples include users mentioning health/disability conditions when requesting UI accessibility accommodations (e.g., screen-reader bugs or seizure triggers) or explaining delayed responses due to medical leave.
3. **Cross-border data flow outside the EU/EEA:**
   * **Yes.** The historical dataset and live inference prompts flow from CloudFlow GmbH (Germany) and Zendesk's EU data centre across the Atlantic to **ApexAI Inc.** and its underlying cloud infrastructure (**AWS US-East**) in the United States (a third country).

---

### Phase 2: Mini GDPR Audit Worksheet (CFU 2 — Apply)

#### Section A — Data Map

| Field | Purpose 1: Live Customer Support & Troubleshooting | Purpose 2: Historical LLM Fine-Tuning (Model Training) | Purpose 3: Automated Ticket Triage & Tier-1 AI Responses |
| :--- | :--- | :--- | :--- |
| **Categories of personal data** | Names, corporate emails, account IDs, IP/device metadata, free-text issue descriptions. | Historical free-text chat transcripts ($180,000$ logs), account tier metadata, user names/emails (prior to redaction). | Live incoming user prompt/complaint text, user ID, account metadata, urgency score. |
| **Sources (where data comes from)** | Directly from B2B end-users via the in-app Zendesk chat widget. | Repurposed internally from CloudFlow's Zendesk relational database (24-month archive). | Directly from B2B end-users via in-app chat widget + model inference output from ApexAI. |
| **Purpose(s)** | Resolve active technical bugs and answer user workflow inquiries. | Fine-tune a domain-specific LLM on historical Q&A pairs to improve automated answer accuracy. | Automatically generate tier-1 troubleshooting replies and score ticket urgency for queue routing. |
| **Lawful basis per purpose & 1-line justification** | **Legitimate Interests (Art. 6(1)(f))** — *Note: Art. 6(1)(b) Contract applies only when the data subject is a sole-trader contracting party; since data subjects are employees of corporate B2B clients, CloudFlow has a legitimate interest in fulfilling its B2B support obligations.* | **Legitimate Interests (Art. 6(1)(f)) [Conditional on PII Redaction / LIA]** — *Justification:* CloudFlow has a valid commercial interest in improving support efficiency (Purpose), training requires real domain transcripts (Necessity), and data subject rights are protected **only if** identifiers are stripped beforehand and an opt-out is provided (Balancing). *(Without PII stripping: **TBD — legal review** due to Art. 5(1)(b) compatibility risks).* | **Legitimate Interests (Art. 6(1)(f))** — *Justification:* Delivering fast, 24/7 tier-1 technical responses benefits both the B2B user and CloudFlow (Purpose/Necessity), and human escalation remains available at one click (Balancing). |
| **Retention period per purpose** | Duration of active enterprise client contract + 24 months for audit/dispute resolution. | Staging dataset deleted **30 days** post-fine-tuning run; model weights retained for **12 months** (until next annual base-model refresh). | Inference logs retained for **90 days** for quality assurance and drift monitoring, then purged. |
| **Recipients and sub-processors** | Internal CloudFlow support staff; **Zendesk Inc.** (CRM processor). | Internal ML engineering team; **ApexAI Inc.** (US LLM processor); **Amazon Web Services (AWS)** (sub-processor). | Internal support team; **Zendesk Inc.**; **ApexAI Inc.**; **AWS**. |
| **International transfers & mechanism** | Hosted in Zendesk EU (Frankfurt); US support escalation covered by **EU-US Data Privacy Framework (DPF)** + **SCCs (Module 2)**. | Transfer from Germany to US (ApexAI / AWS US-East). Mechanism: **EU-US DPF** (if certified) backed by **Standard Contractual Clauses (Module 2: Controller-to-Processor)** and a **Transfer Impact Assessment (TIA)**. | Transfer from Germany to US via real-time API. Mechanism: **EU-US DPF** + **SCCs (Module 2)** + TLS 1.3 encryption in transit and zero-data-retention API flags. |

---

#### Section B — Risk and Rights

1. **Are any special-category data present or inferable from the outputs (Article 9)?**
   Yes, incidental Article 9 data (such as health or disability details disclosed during accessibility support requests) is likely embedded in the $180,000$ unstructured free-text chat transcripts. Because CloudFlow lacks explicit Article 9(2)(a) consent for AI training, an automated PII and sensitive-entity scrubbing pipeline must strip all health references and personal identifiers before the dataset leaves the EU for fine-tuning.

2. **Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?**
   No, Article 22 is not triggered because automated tier-1 software troubleshooting and ticket queue prioritisation for B2B employees do not produce legal effects or similarly significant effects (unlike hiring rejections or credit denials). Furthermore, users retain an immediate "Escalate to Human Engineer" button in the interface, ensuring meaningful human involvement for any complex dispute.

3. **Is a DPIA required? Use the EDPB's nine criteria: explain which apply and why.**
   Yes, a Data Protection Impact Assessment (DPIA) is mandatory under Article 35 because the processing meets at least three of the EDPB's nine criteria (where two or more generally trigger a DPIA):
   * **Criterion 8 (Innovative use or applying new technological solutions):** Fine-tuning generative LLM weights on historical conversational logs introduces novel risks of model memorisation and unintended training data regurgitation.
   * **Criterion 5 (Data processed on a large scale):** Processing $180,000$ full conversation transcripts across $45,000$ EU data subjects over a two-year window constitutes large-scale data processing.
   * **Criterion 1 (Evaluation or scoring):** The system profiles user messages and historical account context to assign urgency priority scores that determine support wait times.

4. **What data subject friction points are most likely?**
   * **Right to Erasure (Art. 17):** Deleting a user's record in Zendesk is straightforward, but erasing their conversational patterns once baked into an LLM's neural weights ("machine unlearning") is practically impossible without full retraining—making pre-training anonymisation/redaction critical.
   * **Right to Object (Art. 21):** Because CloudFlow relies on Legitimate Interests (Art. 6(1)(f)), data subjects have an absolute right to object to their historical tickets being used for AI model training, requiring a technical filter to exclude opted-out User IDs.
   * **Right of Access (Art. 15):** Data subjects may request to know whether their specific support chats were included in the training corpus, requiring CloudFlow to maintain an immutable dataset manifest mapping Ticket IDs to training runs.

5. **What is the controller / processor split? Name each entity and its role.**
   * **CloudFlow GmbH:** **Data Controller** for its own product telemetry and support operations (and **Joint Controller / Processor** depending on B2B client contract terms when handling enterprise client employee data—for this audit, CloudFlow acts as an independent **Controller** for service improvement and AI development).
   * **Zendesk Inc.:** **Data Processor** hosting the ticketing database on CloudFlow's behalf.
   * **ApexAI Inc.:** **Data Processor** providing the fine-tuning infrastructure and private model inference endpoints (must be contractually restricted from using CloudFlow's data to train ApexAI's foundational models for other customers).
   * **AWS Inc.:** **Sub-processor** to ApexAI Inc., providing the underlying GPU compute in US-East.

6. **Is a DPA (Data Processing Agreement) needed with any vendor? Which ones?**
   Yes, an Article 28 DPA is mandatory with both **Zendesk Inc.** and **ApexAI Inc.** Most critically, the DPA with **ApexAI Inc.** must explicitly prohibit ApexAI from acting as a Controller over the training data (i.e., strictly banning cross-customer foundation model training) and incorporate the EU Standard Contractual Clauses (Module 2).

---

#### Section C — Law Stacking (One Line Each)

* **AI Act cross-check:** The system falls into the **Limited Risk tier (Article 50 transparency obligations for chatbots)** built atop a **General-Purpose AI (GPAI) model (Article 53)**; the EU AI Act adds a strict legal obligation to clearly inform users at the start of every chat that they are interacting with an AI system, alongside internal AI literacy training for support staff (Article 4).
* **ePrivacy check:** Yes—the in-app chat widget uses local storage, session cookies, and diagnostic telemetry scripts on the user's terminal equipment, meaning **Article 5(3) of the ePrivacy Directive overrides GDPR Legitimate Interests** for device-level tracking: non-essential analytics metadata cannot be scraped from the user's browser for AI profiling without prior ePrivacy opt-in consent.
* **Data Act check:** **N/A for IoT connected products**, though under the EU Data Act's cloud switching provisions (Chapter VI), CloudFlow should verify that ApexAI Inc. allows the export of fine-tuned LoRA adapter weights so CloudFlow is not locked into a single cloud AI processor.

---

## Section 2: Client Recommendation Memo (Phase 3 / CFU 3 — Integrate)

**TO:** Chief Technology Officer & General Counsel, CloudFlow GmbH  
**FROM:** External Privacy & AI Governance Practice  
**DATE:** November 18, 2026  
**SUBJECT:** GDPR & EU AI Act Audit Recommendation — Customer Support LLM Fine-Tuning  

### Bottom Line
**GO WITH CONDITIONS.** You may proceed with fine-tuning the customer support LLM on your two years of Zendesk chat transcripts, provided you strip personal identifiers prior to export, execute a zero-retention Data Processing Agreement with ApexAI Inc., and complete a formal DPIA before any data leaves the EU.

### Top Three Required Actions (Sequenced)

1. **Execute an AI-Specific DPA and Transfer Impact Assessment (TIA) with ApexAI Inc. (Before Any Data Export):**  
   Sign an Article 28 DPA with ApexAI incorporating EU Standard Contractual Clauses (Module 2) or verifying active EU-US Data Privacy Framework certification. The contract must contain an explicit "Zero Foundation-Model Training" clause prohibiting ApexAI from retaining your chat logs or using your fine-tuned weights to train models for other customers.
2. **Deploy an Automated PII Scrubbing Pipeline and Sign Off on the DPIA (Before Training Run #1):**  
   Do not feed raw Zendesk transcripts into the fine-tuning API. Deploy an automated Named Entity Recognition (NER) and regex redaction script inside your EU environment to strip names, email addresses, IP addresses, API tokens, and incidental health/accessibility disclosures (`[REDACTED]`). Document this architecture in a signed Data Protection Impact Assessment (DPIA) alongside your Legitimate Interests Assessment (LIA).
3. **Update Your Privacy Notice, Provide an Opt-Out Mechanism, and Add an AI Act Banner (Before Live Deployment):**  
   Update your external Privacy Policy to explicitly list "AI model fine-tuning for customer support automation" under Article 6(1)(f), notify existing users with a 30-day window to opt out their historical tickets, and embed a visible banner in the chat widget disclosing that users are interacting with an AI assistant (satisfying EU AI Act Article 50).

### Residual Risks Disclosed

* **Contextual Re-identification & Prompt Extraction:** Even after automated NER scrubbing removes names and emails, complex free-text B2B descriptions of unique software architectures or company-specific outages may allow indirect identification or rare verbatim memorisation if an adversarial user attempts a prompt-injection attack.
* **Article 17 Erasure Friction ("Machine Unlearning"):** If a data subject exercises their Right to Erasure *after* a model is fine-tuned, you cannot delete individual neural weights without retraining the model. While pre-training redaction largely mitigates this, a regulator could still challenge whether redacted long-form transcripts are truly anonymous rather than merely pseudonymised.
* **Enterprise B2B Client Pushback:** Even when legally compliant under GDPR, security-conscious enterprise customers may object commercially to their employees' troubleshooting logs being routed through a US-hosted AI vendor, requiring a contractual client-level opt-out toggle.

*(Word count: 394 words)*

---

## Phase 4: Partner Swap, Peer Review & Debrief (CFU 4 & 5)

### Peer Feedback Rubric (Study Partner Review)

| Criterion | Score (1–3) | Reviewer Comment |
| :--- | :---: | :--- |
| **Clear bottom-line recommendation** | **3 / 3** | "Go with conditions" is stated in the very first sentence with a crisp, one-sentence justification covering technical, contractual, and procedural gates. |
| **Lawful basis selection is justified** | **3 / 3** | Smart distinction in the worksheet noting why Art. 6(1)(b) Contract fails for B2B *employees* (who aren't personally party to the SaaS MSA) and why Art. 6(1)(f) LIA requires PII redaction to pass the balancing test. |
| **Top actions are specific and sequenced** | **3 / 3** | Actions follow a logical chronological gate: (1) Legal contract/transfer lock -> (2) Technical redaction & DPIA before training -> (3) Notice & UI transparency before launch. |
| **Residual risks are named honestly** | **3 / 3** | Calling out the difference between pseudonymisation and true anonymisation during free-text NER redaction—and the B2B commercial pushback risk—is realistic consulting advice. |
| **Law stacking is addressed (AI Act / ePrivacy)** | **3 / 3** | Accurately connects EU AI Act Art. 50 chatbot disclosure in the memo and flags ePrivacy Art. 5(3) cookie/device metadata limits in the worksheet. |

#### Study Partner's Client-Side Response

My study partner reviewed the recommendation from the perspective of CloudFlow's CTO and General Counsel and responded:

> "We accept your **Go with Conditions** recommendation and agree to put the automated NER redaction pipeline in place before sending any Zendesk exports to ApexAI. However, we want to challenge **Action #3's 30-day retroactive opt-out wait period**: sending an email blast to $45,000$ enterprise end-users about AI training will create massive commercial noise with our B2B account managers. Can we rethink Action #3 so that if we strictly strip all direct identifiers and tenant names prior to fine-tuning, we provide the opt-out toggle in-app and via admin settings for *future* training runs without pausing our initial training run for 30 days?"

---

### CFU 5 — Debrief: Audit Comparison & Divergence Resolution

After I swapped worksheets with my study partner, who audited the same B2B LLM support scenario, we compared notes across three core dimensions:

1. **Where the Two Audits Agreed:**
   * **DPIA Requirement:** Both audits independently concluded that a DPIA is mandatory under EDPB guidelines, citing the intersection of **large-scale conversational data** and **innovative generative AI fine-tuning** (memorisation risk).
   * **International Transfer Stack:** Both audits agreed that relying solely on the EU-US Data Privacy Framework (DPF) for a US AI start-up is fragile, and that executing **Module 2 SCCs** alongside a zero-data-retention API configuration is essential.
2. **Where the Two Audits Diverged:**
   * **Lawful Basis for Live Chat vs. Model Training:** My study partner initially proposed **Contract (Art. 6(1)(b))** for Purpose 1 (Live Support) and **Consent (Art. 6(1)(a))** via a checkbox in the chat widget for Purpose 2 (LLM Fine-Tuning). I proposed **Legitimate Interests (Art. 6(1)(f))** for both, subject to strict pre-training PII scrubbing and an opt-out right.
3. **Which Reading is Stronger and Why (Consensus Resolution):**
   * We agreed that **Legitimate Interests (Art. 6(1)(f)) paired with mandatory pre-training PII scrubbing is the stronger legal reading** for a B2B SaaS environment:
     * *Why Contract (Art. 6(1)(b)) fails:* Under EDPB Guidelines 2/2019, Art. 6(1)(b) only applies when the contract is directly with the *individual data subject*. In B2B SaaS, the contract is between CloudFlow GmbH and the corporate employer (e.g., Siemens AG), not the individual employee typing into the support chat.
     * *Why Consent (Art. 6(1)(a)) is operationally flawed for historical logs:* Collecting valid, freely given opt-in consent retroactively from $45,000$ employees across two years of closed tickets is practically impossible (response rates are typically $<5\%$, creating severe dataset bias), and bundling consent into the live support widget risks invalidation if users feel pressured to tick the box to get urgent technical help. A rigorous **Legitimate Interests Assessment (LIA)** backed by technical data minimisation (NER PII stripping) and an Art. 21 opt-out aligns with recent European data protection authority guidance (such as the CNIL and Hamburg DPA recommendations on AI training).

---

## Reinforce Section: Deepening the Consulting Audit

### 1. DPIA Outline — Historical Chat Log Fine-Tuning Pipeline

* **A. Systematic Description of Processing:**
  * Extraction of $180,000$ historical customer support transcripts ($2024\text{--}2026$) from Zendesk EU; automated ingestion into an isolated EU staging bucket; execution of an open-source local NER + regex scrubbing model to mask personal identifiers, credentials, and health mentions; encrypted transmission of sanitized JSONL prompt-completion pairs to ApexAI Inc. (AWS US-East) to compute LoRA fine-tuning weights on a base foundation model.
* **B. Necessity and Proportionality Assessment:**
  * *Necessity:* Generic off-the-shelf LLMs lack knowledge of CloudFlow's proprietary workflow syntax and error codes; domain adaptation requires real troubleshooting dialogues.
  * *Proportionality & Less Intrusive Alternatives Evaluated:* We evaluated Retrieval-Augmented Generation (RAG) on documentation alone, which solved $40\%$ of queries but failed on complex multi-turn debugging. To keep fine-tuning proportional, raw user identities are completely unnecessary for teaching the model troubleshooting logic—Therefore, training is restricted strictly to *de-identified* text, ticket metadata is dropped, and the staging corpus is auto-deleted after 30 days.
* **C. Risk Identification (Rights and Freedoms of Data Subjects):**
  * **Risk 1 (Memorisation & Regurgitation):** The fine-tuned model memorises a specific user's unredacted email, secret API key, or sensitive complaint and outputs it to a different customer during live chat inference (High Severity / Medium Likelihood if unmitigated).
  * **Risk 2 (Unlawful International Access):** US intelligence or third-party sub-processors access raw EU customer support logs in AWS US-East (Medium Severity / Low-Medium Likelihood).
  * **Risk 3 (Inability to Honour Erasure):** A user exercises Art. 17 erasure or Art. 21 objection after their chat has been compiled into model weights (Medium Severity / High Likelihood).
* **D. Proposed Technical and Organisational Mitigations:**
  * *Mitigation for Risk 1:* Two-stage redaction pipeline in Berlin prior to export + differential privacy / weight regularisation during training + real-time output guardrail filter blocking any PII/regex pattern during live inference.
  * *Mitigation for Risk 2:* EU-only PII stripping before US transfer; TLS 1.3 encryption in transit and AES-256 at rest; contractual zero-retention on training payloads post-job completion.
  * *Mitigation for Risk 3:* Maintain a hashed Ticket-ID exclusion table; enforce a 12-month model depreciation cycle so any opted-out user's residual conversational patterns are purged on the next scheduled retraining run.

---

### 2. Critical DPA Clause with Main Vendor (ApexAI Inc.)

> **Proposed Clause — Section 4.3 (Prohibition on Cross-Customer Model Training & Weight Isolation):**  
> *"Processor (ApexAI Inc.) acknowledges and agrees that all Customer Personal Data, training datasets, prompt inputs, model outputs, and resulting fine-tuned model weights or adapter layers ('Customer AI Assets') remain the exclusive property and under the sole data protection control of Controller (CloudFlow GmbH). Processor is strictly prohibited from using, retaining, or analyzing Customer Personal Data or Customer AI Assets to train, fine-tune, benchmark, or improve Processor's foundational models, general-purpose AI systems, or any model made available to third parties. All fine-tuned model weights shall be logically and cryptographically isolated per tenant, and all raw training payloads shall be permanently purged from Processor and Sub-processor memory and storage within seventy-two (72) hours of fine-tuning job completion."*

* **Why this clause is essential:** Without this specific covenant, standard AI vendor terms often classify "service improvement and foundation model training" as an independent Controller purpose of the vendor. If ApexAI uses CloudFlow's chat logs to train its base model, CloudFlow commits an unlawful third-party disclosure without a valid GDPR Article 6 basis, and loses all technical ability to enforce data retention or erasure.

---

### 3. UK GDPR Extension: Serving Data Subjects in the United Kingdom

If CloudFlow GmbH also serves B2B data subjects located in the **United Kingdom**, the bottom-line recommendation remains **GO WITH CONDITIONS**, but three specific compliance adjustments are required under the **UK GDPR** and the **Data Protection Act 2018** (as amended by the UK Data (Use and Access) governance framework):

1. **International Transfer Mechanism to the US:** The EU-US Data Privacy Framework and EU SCCs do not cover UK data subjects. CloudFlow must ensure ApexAI Inc. is certified under the **UK Extension to the EU-US Data Privacy Framework**, or attach the **ICO's International Data Transfer Addendum (IDTA)** to the EU SCCs alongside a UK Transfer Risk Assessment (TRA).
2. **UK Article 27 Representative & ICO Jurisdiction:** Because CloudFlow GmbH is established in Berlin with no UK branch office but offers services to UK clients, it must designate a **UK Representative** under Article 27 of the UK GDPR and update its privacy notice to reference the **UK Information Commissioner's Office (ICO)** as a competent supervisory authority alongside the Berlin Commissioner for Data Protection (BlnBDI).
3. **Divergence in AI Act Applicability:** The **EU AI Act does not apply in the United Kingdom** (which relies on a pro-innovation, sector-regulator approach led by the ICO, FCA, and CMA). While CloudFlow should keep the Article 50 AI chatbot disclosure banner globally as a best practice (which also satisfies UK ICO fairness and transparency principles), EU AI Act conformity and literacy mandates are legally enforceable only for its EU operations and EU output deployments.

---

## Stretch Section: Mini Data Protection by Design Checklist

**Target Activity:** Highest-Risk Processing Activity — *Ingesting & Fine-Tuning LLM Weights on $180,000$ Historical Support Chat Logs*

| Design Principle | Audit Question | Current Client Status | Consultant Finding & Required Remediation |
| :--- | :--- | :---: | :--- |
| **1. Data Minimisation** | Is only the minimum necessary data collected and fed into the training pipeline? | **FAIL** | Client currently plans to export full raw Zendesk tickets (including user names, emails, IP headers, and greeting chatter). **Fix:** Strip metadata headers and run an automated EU-hosted NER/regex scrubber before creating training JSONL files. |
| **2. Purpose Binding** | Is the data technically restricted to the stated purpose? | **FAIL** | Raw Zendesk database dumps are currently accessible in a shared analytics data lake without technical segregation, and ApexAI's default API tier logs prompts for general R&D. **Fix:** Provision an isolated S3 bucket with IAM role restrictions and enable ApexAI's "Zero-Retention / Enterprise No-Train" API flag. |
| **3. Access Controls** | Is access limited strictly to those who need it? | **PASS (Partial)** | Production Zendesk has SSO and RBAC, and only three ML Engineers hold API keys to the ApexAI staging environment. **Fix:** Add mandatory MFA and automated audit logging on the fine-tuning dataset export script. |
| **4. Retention Enforcement** | Are there automated deletion or anonymisation policies? | **FAIL** | Zendesk chat logs have accumulated for 24+ months with no automated purge script, and no lifecycle policy exists for fine-tuning checkpoints. **Fix:** Configure a 30-day TTL (Time-To-Live) auto-delete rule on the training staging bucket and a 12-month lifecycle replacement policy on fine-tuned model weights. |
| **5. Subject Rights Workflow** | Can the client respond to an access (Art. 15), erasure (Art. 17), or objection (Art. 21) request within the 30-day deadline? | **FAIL** | While CloudFlow can delete a user in Zendesk within 30 days, they have no lineage tracker showing which Ticket IDs were compiled into which LLM fine-tuning snapshot, nor a way to unlearn weights. **Fix:** Build a hashed `ticket_id -> model_version` manifest and implement pre-training PII scrubbing so model weights do not contain identifiable personal data. |
| **6. Incident Response** | Is there a documented process to detect and notify a breach within 72 hours (Art. 33)? | **UNKNOWN** | CloudFlow has a general SaaS security incident response plan for its Berlin infrastructure, but has not tested prompt-injection data leakage detection or verified whether ApexAI's DPA commits the vendor to notify CloudFlow within 24–36 hours of an upstream AI sub-processor breach. **Fix:** Mandate a 24-hour breach notification SLA in the ApexAI DPA and add LLM output PII-leakage alerts to the SOC dashboard. |
