# W7D3_LAB_GDPR_Same_product_privacy_lens
- Week 7 / Day 3
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-19
---

### Phase 1: Build the fact pattern

#### Transition note / scenario choice

**Scenario selected; continuing from EU AI Act lab:**

”Our loan approval team is drowning in paperwork. We want an AI that takes a look at a customer's credit history, income, and background, and then automatically decides whether to approve or deny their mortgage application. Is that something your team can handle?”

**AI Act tier it fell into: High Risk**

**Decision: Approve with controls**

We are carrying forward Partner Case 1, a mortgage approval AI system. In the EU AI Act analysis, this system is likely high-risk because it assesses creditworthiness and access to essential financial services. It is especially useful for GDPR analysis because it processes sensitive financial and background data and proposes fully automated decisions with major effects on individuals.

#### Fact pattern paragraph

The client is a private mortgage handling firm with 50 employees. They take personal data from the client involving: 1) credit history, 2) income, 3) background, 4) limited personal identifiable information. The geographic region is Germany and clients are German residents. The AI system should automatically assess the clients credit worthiness based on an algorithmic score taking into account the clients risk profile. The vendors in the technology stack would include an OpenAI model that assesses credit worthiness. All models and storage would be local at the mortgage handling firm. Once the decision is made on the customer, all of their data will be removed from the system other than their credit score and their name.

#### Fact pattern checklist

| Question | Your answer |
| --- | --- |
| Who is the client? | A private mortgage handling firm based in Germany with around 50 employees. |
| What personal data is processed? | Credit history, income, background information, and limited personally identifiable information such as name and application details. |
| Who are the data subjects? | Prospective mortgage applicants / prospective clients. |
| Where are the data subjects located? | Germany, within the EU/EEA. |
| Who are the vendors in the stack? | An OpenAI model or similar third-party AI model provider used to assess creditworthiness. |
| What does the AI system actually do with the data? | It analyses the applicant’s credit history, income, and background to assess creditworthiness and create a risk score or decision recommendation. |
| Is there automated decision-making with legal or similarly significant effects? | Yes. The system automatically decides whether to approve or deny a mortgage application, which can significantly affect the applicant’s access to housing finance. |

---

### Phase 2: Mini GDPR audit worksheet

#### Section A — Data map

| Field | Your answer |
| --- | --- |
| Categories of personal data | Name, Email, Phone Number, Credit History, Income, Background information, Application ID and Customer ID. Credit Score and approval or denied decision.  |
| Sources (where data comes from) | Customer provides though the application   |
| Purpose(s) — one row per purpose | **1.** Verify the applicant’s identity and process the mortgage application.
**2.** Assess the applicant’s income, credit history, and financial risk.
**3.** Generate an automated approval or denial decision for the mortgage application.
**4.** Keep a limited record of the decision, score, and applicant identity for audit, complaint handling, and legal compliance.
**5.** If applicable (optional), monitor or improve the AI model’s performance, subject to separate controls and legal review. |
| Lawful basis per purpose — or `TBD — legal review` | **1. Consent / Contract** — processing is necessary to take steps at the applicant’s request before entering into a mortgage contract.
**2**. **Contract / Legal obligation** — needed to assess the mortgage application and may also be required for responsible lending or financial compliance and the duty to check affordability, fraud risk, identity, and compliance.
**3. TBD — legal review.** This creates a significant effect on the applicant and requires Article 22 analysis, safeguards, and possibly human review before launch.
**4. Legal obligation / Legitimate interests** — needed for regulatory, audit, dispute, and compliance purposes. Records for complaints, audits, fraud prevention, or defending legal claims
**5.**  **Legitimate interests or consent**, depending on whether applicant data is reused. This should be subject to separate controls, data minimisation, and legal review. The customer applied for a mortgage; they did not necessarily agree to train or improve AI. |
| Retention period per purpose | **1.** Keep during the application process and until the mortgage decision is final. If the applicant becomes a customer, retain necessary records for the life of the mortgage and any legally required period afterwards.
**2.** Keep only as long as needed to assess the application and support the decision, then delete or minimise unless retention is required for audit, complaints, fraud prevention, or legal compliance.
**3.** Keep the decision outcome, score, main reasons, and audit trail for the period needed to explain, challenge, review, or defend the decision. Exact period: **TBD — legal review**.
**4.** Retain for the legally required financial/regulatory retention period, then delete or anonymise. Exact period: **TBD — legal review**.
**5.** Do not retain identifiable applicant data for model improvement unless separately justified. Prefer anonymised or aggregated data. If identifiable data is needed, define a short retention period and require legal review. |
| Recipients and sub-processors | Internal recipients include the mortgage handling firm’s loan approval team and any other related internal team if applicable.
External recipients/processors may include the AI model provider, such as OpenAI .
Sub-processors: hosting or security providers 
 |
| International transfers and transfer mechanism | Yes, if the AI model provider, hosting provider, or security provider processes or stores applicant data outside Germany or the EU/EEA. If the system is fully locally hosted in Germany and no personal data is transferred to non-EU providers, then international transfers may not apply. |


#### Section B — Risk and rights

Answer each question in 1–3 sentences.

#### 1. Special-category data

**Are any special-category data present or inferable from the outputs under Article 9?**

Based on the information provided, the answer is no. However, “background information” is ambiguous and could include special-category data (e.g., health status, ethnicity, religion, disability, or trade union membership). This should be assessed more closely and limited to what is strictly necessary for the credit-scoring task.

#### 2. Automated decision-making

**Is there automated decision-making with legal or similarly significant effects under Article 22? If yes, what safeguard applies?**

Yes. The system makes an automated credit score and approval/denial decision for the loan application. It should include human oversight and final sign-off on the AI output. The credit score and decision should be retained only for a legally permitted period, to support review and to provide information to the applicant on request. The applicant should also be informed that AI was used and of their right to request an explanation.

#### 3. DPIA requirement

**Is a DPIA required? Use the EDPB's nine criteria and explain which apply and why.**

Yes. A Data Protection Impact Assessment (DPIA) is required under Article 35 because the system makes automated decisions about individuals’ eligibility for a mortgage product, which can significantly affect their lives. Several EDPB criteria apply, including systematic and extensive evaluation of personal aspects (creditworthiness), profiling, automated decision-making with legal or similarly significant effects, and the processing of financial and background data.

**European Data Protection Board** 

| **EDPB criterion** | Applicability |
| --- | --- |
| 1. Evaluation or scoring | Yes. The system evaluates the applicant’s creditworthiness and creates a credit risk score. |
| 2. Automated decision-making with significant effects | Yes. The AI automatically approves or denies a mortgage application, which can significantly affect access to housing finance. |
| 3. Systematic monitoring | No / limited. The scenario does not describe ongoing monitoring of applicants, but this should be reviewed if the system tracks applicants over time. |
| 4. Sensitive data | Partly. Income, credit history, and financial background are not usually Article 9 special-category data, but they are still sensitive financial personal data in practice. |
| 5. Large-scale processing | Maybe / TBD. This depends on the actual number of mortgage applicants processed by the firm. |
| 6. Matching or combining datasets | Yes. The system combines application data, income data, credit history, and background information. |
| 7. Vulnerable data subjects | Maybe / limited. Mortgage applicants may be in a weaker position because the decision affects access to important housing finance, but they are not automatically a vulnerable group. |
| 8. Innovative technology | Yes. AI is being used to assess applicants and support or make credit decisions. |
| 9. Preventing access to a service | Yes. A mortgage denial can block access to an important financial service. |

#### 4. Data subject friction points

**What data subject friction points are most likely?**

The most likely friction points are the applicant’s right of access, right to meaningful information about how the automated decision was made, and right to challenge the decision or request human review. Applicants may also object to profiling, especially if they believe the AI score is unfair or based on incorrect background or credit data. The right to rectification is important because inaccurate income, credit history, or application data could lead to a wrong mortgage decision. The right to erasure may be more limited because the firm may need to retain some records for audit, complaint handling, fraud prevention, or legal compliance.

#### 5. Controller / processor split

**What is the controller / processor split? Name each entity and its role.**

The mortgage handling firm is the controller because it decides the purposes and means of processing: mortgage assessment, creditworthiness scoring, and approval/denial decisions.

The AI model provider, such as OpenAI or a similar vendor, would likely be a processor if it processes applicant data only under the firm’s instructions.

Hosting, cloud, or security providers may be sub-processors if they support the AI service or can access applicant data.

**NB: If the AI vendor reuses applicant data for its own model training or analytics, its role requires legal review and could shift toward separate controller or joint controller. The firm remains responsible for ensuring appropriate contracts, security controls, and instructions are in place.**

#### 6. DPA requirement

**Is a Data Processing Agreement needed with any vendor? Which ones?**

Article 28 says that when a controller uses a processor, there must be a contract with specific protections.

Yes. A DPA is needed with the AI model provider and any hosting, cloud, or security provider that processes or can access applicant data on behalf of the mortgage firm. The DPA should cover instructions, confidentiality, security, sub-processors, deletion/return of data, audit rights, and support for data subject rights. Any credit reference agency should be reviewed separately because it may be a processor, independent controller, or joint controller.

#### Section C — Law stacking

#### AI Act cross-check

**What tier did the AI system fall into, or what tier would you hypothesize? Does the AI Act add any obligation that GDPR does not cover?**

High-risk under the EU AI Act.

The AI Act adds AI-specific obligations that GDPR does not fully cover, including risk management, data quality controls, technical documentation, logging, human oversight, accuracy, robustness, cybersecurity, and post-market monitoring.

#### ePrivacy check

**Does the scenario involve cookies, tracking pixels, or device-level data? If yes, does ePrivacy's consent requirement override GDPR's flexibility?**

Based on the stated facts, the scenario does not appear to involve cookies, tracking pixels, or device-level data, so ePrivacy is not a main issue for the mortgage AI assessment itself. The main legal issues are under GDPR and the EU AI Act. However, if the mortgage application website uses analytics cookies, tracking pixels, device fingerprinting, or similar tracking technologies, ePrivacy consent requirements may apply separately and could require consent before those technologies are used.

#### Data Act check

**Is there connected product or cloud switching data involved?**

No, based on the stated facts. The scenario does not involve connected products, IoT data, machine-generated product data, or cloud switching. The main issues are GDPR and the EU AI Act. The Data Act should only be revisited if connected-device data or cloud switching becomes part of the system.

---

### Phase 3: Write the client recommendation memo

#### Memo draft

**To:** Client legal and compliance team / CTO / project owner / DPO
**From:** AI Consultant
**Subject:** GDPR recommendation for Automated Credit Worthiness and Credit Scoring System
**Date:** 19/08/2025

**Bottom line:** The proposed system is feasible. We recommend proceeding, subject to specific constraints and conditions. Both GDPR and the EU AI Act apply to this tool, and additional work is required to ensure the system is lawful and compliant.

**Top Three Actions:**

1. **Redesign the workflow so the AI does not make the final mortgage decision alone.** Use the AI as a decision-support tool, but require meaningful human review and final sign-off before approval or denial.
2. **Complete a DPIA and Article 22 legal review before launch.** The review should confirm the lawful basis, assess automated decision-making risks, test for bias or unfair outcomes, and define the applicant’s rights to explanation, challenge, and human review.
3. **Put vendor and governance controls in place before any applicant data is processed.** This includes a DPA with the AI provider and any hosting/security providers, restrictions on using applicant data for model training, data minimisation, retention rules, logging, security controls, and clear applicant notices.

**Residual risks:**

1. **Bias and unfairness:** The AI may still produce unfair outcomes if the data reflects historical bias or if the model weighs factors in a way that disadvantages some applicants.
2. **Incorrect or incomplete data:** Wrong income, credit history, or background data could lead to an incorrect mortgage decision, even with human review.
3. **Explainability and regulatory risk:** Applicants may challenge decisions if they do not understand how the AI influenced the outcome, and regulators may scrutinise the system because it is high-risk under the EU AI Act and involves automated decision-making under GDPR.

---

### Phase 4: Partner swap and peer review

#### Peer feedback rubric

| Criterion | Score 1–3 | Comment |
| --- | --- | --- |
| Clear bottom-line recommendation | 3 | Yes — the memo states “Go with conditions” with a clear one-sentence reason: Article 22, DPIA, and AI Act requirements must be addressed before the system can decide automatically. |
| Lawful basis selection is justified | 2 | The memo works through Article 22 safeguards and the DPIA in depth, but never names or justifies a specific Article 6 lawful basis (e.g., contract or legitimate interests) for the underlying processing. |
| Top actions are specific and sequenced | 3 | Yes — each action is concrete and logically sequenced: redesign the workflow for human review, complete the DPIA and AI Act assessment, then lock down vendor and data-flow arrangements before go-live. |
| Residual risks are named honestly | 3 | Yes, though the risk of incorrect or incomplete data is only folded into the bias/inaccuracy risk rather than named as its own line, and none of the three top actions directly mitigate it. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | The memo engages meaningfully with the AI Act (action 2 covers risk management, logging, and human oversight), but stays silent on ePrivacy. Given the facts, ePrivacy likely doesn't apply here, so the memo could say that explicitly instead of leaving the gap unaddressed. |

#### Client-style response

Based on the review, I accept that this project is feasible and beneficial to pursue. However, I will first ensure the project complies with the EU AI Act and GDPR, and that all necessary and meaningful procedures, contractual relationships (DPAs, etc.), security measures, and policies are in place and fully documented. I will also ensure that mortgage applicants are fully informed of their rights and the involvement of AI, and that staff at the mortgage firm are properly trained in using the tool and in GDPR requirements.

I accept that the system will be deployed locally, but this may prove expensive and difficult to maintain. There is a chance that, after running the system for some time, the company decides to move to a remote hosting environment without the proper assessment. Data security is another major concern and may be challenging to ensure in a small-business setting.

It may be worth rethinking remote hosting on a provider’s premises, as long as the proper and necessary contractual relationship, DPA, and procedures are in place.