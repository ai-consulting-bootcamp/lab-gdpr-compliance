# GDPR Audit Pack — AI-Assisted CV Screening

# Phase 1 — Fact Pattern

**Scenario:** New case — AI-assisted CV screening with human review (Option B(b)).

## Fact pattern

A fictional German HR technology startup, **TalentBridge GmbH**, with approximately 40 employees, offers an AI-assisted applicant-screening tool to medium-sized employers recruiting across Germany and other EU/EEA countries. The tool processes approximately 10,000 applications annually, including applicants' names, contact details, CVs, employment and education histories, skills, and recruiter notes; CVs may also contain photographs or voluntarily disclosed health, disability, religious or other sensitive information. Applicants are primarily located in the EU/EEA, although some may apply from outside it. Employers upload applications to the platform, which uses a third-party cloud-hosted language-model service to extract job-relevant information, compare it with published role criteria, and propose a ranked shortlist. The model vendor and hosting location, any non-EU access or transfers, and sub-processor arrangements **have not yet been confirmed**. Recruiters review the recommendations and can change or reject them before inviting candidates to interview; whether this review is sufficiently meaningful in practice requires verification. The system therefore influences access to employment, and its processing warrants particular attention under GDPR and the EU AI Act.

## Required questions

| Question | Answer |
|---|---|
| Who is the client? | TalentBridge GmbH, a **fictional** German HR-tech startup (~40 employees) serving medium-sized employers. |
| What personal data is processed? | Applicant identifiers, contact details, CVs, work and education history, skills, recruiter notes and AI-generated suitability scores/rankings; approximately 10,000 applications/year (scenario assumption). Special-category information may appear in CVs and must be assessed separately. |
| Who are the data subjects? | Job applicants. |
| Where are they located? | Primarily Germany and other EU/EEA countries; some third-country applicants possible. |
| Who are the vendors? | TalentBridge, its employer clients, a cloud/LLM provider and possible hosting sub-processors. **Specific vendors and any non-EU transfers: TBD — confirm in scenario before Phase 2.** |
| What does the AI do? | Extracts application information, compares it with role criteria and recommends a ranked shortlist for recruiter review. |
| Are there automated decisions with legal or similarly significant effects? | **Potentially.** Hiring outcomes are significant. The stated design includes human review, but whether decisions are *solely automated* for GDPR Article 22 purposes depends on whether recruiter review is genuine and can alter outcomes. **TBD — verify.** |

## Points to confirm with the partner before Phase 2

1. Agree that **Option B(b)** and the fictional TalentBridge case will be the shared scenario.
2. Choose a specific model/hosting vendor and establish whether EU applicant data is accessible from outside the EEA.
3. Confirm whether recruiters genuinely review every shortlist and can override AI rankings before any rejection or invitation.
4. Agree whether sensitive CV information is excluded from scoring and how long applications are retained.

*This is a proposed fictional fact pattern, not a description of a deployed system. All invented details are scenario assumptions to be agreed with the partner.*


---

# Phase 2 — Mini GDPR Audit Worksheet

*Scenario: TalentBridge's fictional AI-assisted CV screening service. This assessment uses the Phase 1 assumptions; vendor identity, hosting, review practices and retention remain unverified. Proposed controls are recommendations, not existing safeguards.*

## Section A — Data map

| Field / processing purpose | Assessment |
|---|---|
| Categories of personal data | Names, contact details, CV text and optional photos, qualifications, employment history, skills, application status, recruiter notes, job criteria, and inferred suitability scores/rankings. CVs may incidentally contain health, disability, religious or other Article 9 information. Approximately 10,000 applications per year is a scenario assumption. |
| Sources | Applicant-submitted CVs and forms; employer recruitment systems and recruiter notes; published job requirements; AI-generated scores, explanations and rankings. |
| Purpose 1 — Receive and administer applications | **Lawful basis: TBD — legal review.** The recruiting employer should assess Art. 6(1)(b) where processing is necessary for steps requested by an applicant before an employment contract, or Art. 6(1)(f) where justified; applicable national employment rules (including Germany's §26 BDSG where relevant) require review. **Retention:** define a documented recruitment retention schedule; no verified period provided. |
| Purpose 2 — AI extraction, matching and ranked shortlists | **Lawful basis: TBD — legal review.** A possible Art. 6(1)(f) legitimate-interest case requires an LIA: **purpose** = efficient, consistent initial assessment; **necessity** = demonstrate why AI ranking is needed rather than less intrusive screening; **balancing** = weigh applicants' expectations, discrimination/error risks and safeguards. Art. 6(1)(b) should not be assumed to cover profiling automatically. **Retention:** minimise derived scores and delete according to the agreed recruitment schedule. |
| Purpose 3 — Recruiter review and interview decisions | **Lawful basis: TBD — legal review** (potential Art. 6(1)(b), depending on recruitment context and necessity). Human review must be substantive, with documented ability to override. **Retention:** same recruitment schedule, with proportionate audit trail. |
| Purpose 4 — Security and accountability logs | **Lawful basis: TBD — legal review** (potential Art. 6(1)(f) for necessary security or Art. 6(1)(c) for a specific legal obligation). Keep minimal access/security logs under a separately justified, limited schedule. |
| Purpose 5 — Training or improving a vendor's general model | **Not part of the stated purpose; prohibit by default.** Any proposed reuse requires separate purpose, lawful basis and assessment; no such authorisation is established. |
| Retention per purpose | **Not yet specified.** Employer and TalentBridge must set deletion periods for unsuccessful and successful applications, AI scores, recruiter notes, backups and logs; align with recruitment needs, legal claims and applicable national law. No fixed duration should be represented as agreed. |
| Recipients and sub-processors | Recruiting employers; TalentBridge as platform operator; unidentified cloud/LLM and hosting providers and any authorised sub-processors. Confirm which receives raw CVs, scores and logs, and whether data is used for model improvement. |
| International transfers | **TBD — legal review.** Provider location, hosting region and remote access are unknown. If personal data is transferred or made accessible outside the EEA, verify an adequacy decision where applicable (including valid EU–US DPF certification for the relevant recipient), or suitable SCCs plus transfer assessment and supplementary measures where needed. |

## Section B — Risk and rights

**Article 9 — Special-category data.** CVs may reveal health, disability, religion or other protected characteristics, and a model may infer them from indirect clues. The service should minimise or mask irrelevant sensitive information before ranking; if Article 9 data is processed, identify a valid Article 9(2) condition *in addition to* an Article 6 basis, with legal review of applicable employment rules.

**Article 22 — Significant automated decisions.** Shortlisting can materially affect access to employment; meaningful recruiter assessment may keep the final decision from being *solely* automated, but a rubber-stamp review would not. Verify that reviewers examine relevant evidence, can override rankings, and document reasons; if Article 22 applies, establish a permitted exception and required safeguards before use.

**DPIA — Required?** **Strongly indicated; complete a DPIA before deployment**, subject to the controller's formal assessment under Art. 35 and relevant supervisory-authority lists. EDPB criteria: (1) evaluation/scoring **yes**; (2) significant automated decisions **possible**, depending on actual review; (3) systematic monitoring **not established**; (4) sensitive data **possible**; (5) large-scale processing **needs assessment** (10,000 applications/year alone is not conclusive); (6) dataset matching **possible** if CVs, employer records and notes are combined; (7) vulnerable individuals **relevant** given applicant/employer power imbalance; (8) innovative technology **yes**; (9) exclusion from a job opportunity **relevant**. Several criteria indicate likely high risk; do not treat a numerical threshold as an automatic legal rule.

**Data subject rights.** Applicants may request access to CV-derived profiles and scores (Art. 15), correction of inaccurate qualifications or extracted facts (Art. 16), erasure where applicable (Art. 17), and objection where Art. 6(1)(f) is relied on (Art. 21). Define who receives requests, how TalentBridge helps employer clients respond, and how corrections propagate to vendors and derived outputs; provide meaningful information about profiling and decision-making as required.

**Controller/processor split.** The recruiting employer is generally **controller** for applicant assessment and hiring purposes. TalentBridge is likely a **processor** when acting solely on employer instructions, but may be an independent or joint controller for any purposes it determines itself; confirm actual contractual and operational control. The LLM/hosting services are likely subprocessors for instructed processing, subject to their actual terms and data use.

**DPAs.** An **Art. 28 DPA** is needed between each employer-controller and TalentBridge where TalentBridge acts as processor, and between TalentBridge and authorised subprocessors, with appropriate flow-down obligations. Verify subprocessor approvals, security, deletion, breach notification, audit assistance and international-transfer terms; consider an Art. 26 arrangement only if joint controllership is actually established.

## Section C — Law stacking

| Law | Cross-check |
|---|---|
| **EU AI Act** | **High risk** for recruitment/selection and applicant evaluation under **Art. 6(2) and Annex III, point 4(a)**, on the stated intended purpose. Provider/deployer obligations (including risk management, data governance, technical documentation, logging, transparency to deployers and human oversight) extend beyond GDPR; confirm role allocation and applicable commencement dates before deployment. |
| **ePrivacy** | No cookies, tracking pixels or device access are described in the fact pattern, so no specific ePrivacy consent issue is established. Reassess if applicant tracking or analytics tools are added. |
| **EU Data Act** | No connected-product data is involved. Cloud-switching provisions may become relevant to cloud-service contracting, but do not replace GDPR processor or transfer requirements. |

## Unresolved facts before a final compliance decision

1. Identify the LLM and hosting vendors, their locations, subprocessor chain and model-training terms.
2. Confirm whether every affected applicant receives meaningful human review before rejection or invitation.
3. Define the treatment of Article 9 data and the actual retention/deletion schedule.
4. Confirm the controller's lawful basis for each purpose, complete the LIA if applicable, and conduct the DPIA.

*Educational assessment only; not legal advice or a completed DPIA.*


---

# Phase 3 — Client Recommendation Memo

**To:** Management, Legal Team and CTO, TalentBridge GmbH  
**Subject:** GDPR readiness of the AI-assisted CV screening platform

**Recommendation: GO WITH CONDITIONS.** TalentBridge should not process live applicant data until it has verified its lawful bases, completed a Data Protection Impact Assessment (DPIA), and established effective human oversight and vendor safeguards.

TalentBridge's platform could help recruiters review applications more efficiently. However, it handles sensitive career information and produces rankings that may influence employment opportunities. The main concern is not simply whether the AI performs well, but whether applicants are assessed fairly, transparently and lawfully.

### Three priority actions

**1. Confirm legal responsibilities and secure vendor arrangements before processing.** Establish which organisation controls each processing purpose. Agree Article 28 Data Processing Agreements with employer clients and relevant subprocessors. Identify the cloud and AI providers, hosting locations and any access from outside the EEA. Confirm an appropriate international transfer mechanism where required, and prohibit vendors from reusing applicant data to train their own models without separate authorisation. Document the Article 6 lawful basis for each purpose and complete a legitimate interests assessment wherever that basis is proposed.

**2. Complete a DPIA and test human oversight before launch.** Assess risks of discriminatory rankings, inaccurate CV extraction, inappropriate use of sensitive information and excessive reliance on AI recommendations. Exclude irrelevant sensitive information from scoring wherever possible. Recruiters must be able to examine, challenge and override recommendations before consequential decisions are made. Test these safeguards and document the results.

**3. Implement transparency, retention and applicant rights procedures.** Update applicant privacy notices to explain AI-assisted screening, data recipients, retention and relevant rights. Establish clear procedures for access, correction, erasure and objections. Set documented deletion periods for CVs, rankings, recruiter notes and logs, including copies held by vendors.

### Residual risks

Even with these measures, three risks remain: AI rankings may reproduce historical recruitment bias; recruiters may over-trust recommendations despite formal oversight; and errors or unintended access may still occur within third-party infrastructure.

**Final advice:** Proceed only after the identified controls are implemented and verified. TalentBridge should also complete its separate EU AI Act high-risk compliance assessment before the relevant obligations apply.

---

# Phase 4 — Partner Swap and Peer Review

**Reviewer:** Barsha Mishra. **Reviewed document:** Phase 3 TalentBridge recommendation memo. The scores and comments below are Barsha’s feedback, reproduced in substance.

| Criterion | Score (1–3) | Barsha’s comment |
|---|---:|---|
| Clear bottom-line recommendation | **3** | “Go with conditions” is clear; prohibiting live applicant data until safeguards are in place makes it concrete. |
| Lawful basis selection is justified | **2** | Name provisional bases by purpose: Art. 6(1)(b) for necessary applicant-requested pre-contractual processing; assess an LIA or applicable employment law for AI ranking; do not rely casually on applicant consent given the power imbalance. Review §26 BDSG in light of CJEU C-34/21. |
| Top actions are specific and sequenced | **3** | The sequence is effective: responsibilities/vendors, then DPIA/oversight, then transparency/rights. Vendor identity and transfer mechanism could be separated out more explicitly. |
| Residual risks are named honestly | **3** | Bias, recruiter automation bias and third-party errors are realistic. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | Explicitly cite AI Act Annex III 4(a) and additional high-risk obligations; state that ePrivacy tracking consent is not triggered by the stated facts. |

**Total: 13/15.** Barsha described the memo as practical and recommended more specific lawful bases and clearer law stacking.

**Barsha’s client response:** “I accept the recommendation with one request: please state which lawful basis you propose for each main purpose (screening for the employer, and any model improvement by TalentBridge), so our legal team can review a concrete position.”

**Our client response (2–3 sentences):** Thank you for the detailed review. I accept the request to identify provisional lawful bases separately for employer recruitment and any TalentBridge model improvement, while leaving their final suitability to legal review. I will also make the Article 22 safeguards, AI Act high-risk duties, and the ePrivacy non-applicability conclusion explicit.

## Clarifications following the review

- **Application administration:** The employer-controller can assess **Art. 6(1)(b)** for steps taken at the applicant’s request before a contract, to the extent each operation is necessary; national employment-law provisions also require legal review.
- **AI-assisted ranking:** **TBD — legal review.** A proposed **Art. 6(1)(f)** basis needs a documented purpose/necessity/balancing LIA and consideration of whether it is available and appropriate in the employment context. Do not assume Art. 6(1)(b) automatically covers AI profiling. Review the applicable German legal framework, including §26 BDSG and CJEU C-34/21.
- **TalentBridge model improvement:** **Not authorised in the current scenario.** Prohibit reuse by default. If TalentBridge decides to reuse identifiable applicant data for its own model improvement, it may become a separate controller for that purpose and must establish a valid purpose, Art. 6 basis, any applicable Art. 9 condition, transparency and other safeguards *before* processing.
- **Article 22 and employment safeguards:** No automatic rejection; recruiters must perform genuine, documented review and be able to override outputs. Assess whether the real workflow nevertheless amounts to solely automated significant decisions; consider works council participation and Germany’s AGG alongside GDPR.
- **Retention and minimisation:** Assess an illustrative **six-month post-rejection retention period** against the employer’s legal claims, circumstances and local advice; it is **not** an automatic GDPR rule. Exclude CV photographs and irrelevant sensitive details from AI scoring wherever possible.
- **Law stacking:** Recruitment screening is presumptively **high risk under AI Act Annex III, point 4(a)**. Map provider/deployer duties, including oversight, logging and applicable information duties, with attention to commencement dates. **No cookies, pixels or device tracking are stated**, so no specific ePrivacy consent requirement is identified on these facts.

# Phase 5 — Joint Debrief

**Where we agree:** Both reviews support **GO WITH CONDITIONS**, require a pre-deployment **DPIA**, and prioritise transparent processing, vendor safeguards, meaningful human review and protection against discrimination. Both recognise that personal data used for a separate model-improvement purpose cannot simply inherit the recruitment purpose’s legal basis.

**Where our readings differ:** My initial memo deliberately left each Article 6 basis open for verification. Barsha’s review makes the advice more actionable by proposing Art. 6(1)(b) for necessary application handling and a separately assessed legitimate-interests or employment-law route for AI ranking, while cautioning against applicant consent. She also called for clearer Article 22, works council, AGG and AI Act obligations and a possible six-month retention benchmark.

**Which reading is stronger, and why:** Barsha’s **purpose-by-purpose provisional legal-basis analysis** is stronger for client decision-making because the legal team can review a concrete proposal rather than a blank “TBD”. The combined position remains appropriately cautious: a proposed basis is not confirmed until necessity, applicable German law and the actual technical workflow are checked. The same applies to whether human review prevents Article 22 from applying.

**Remaining work before real deployment:** Confirm controller/processor roles, cloud and model vendors, cross-border access, final lawful bases, retention schedule, DPIA outcome and tested human-oversight controls. The review was document-based; no live system was inspected or tested.

# Reinforce — Optional Consulting Depth

## Mini DPIA outline: AI ranking of applicants

- **Processing:** Employers upload CVs and job criteria; the service extracts applicant attributes and generates ranked shortlists for recruiter review.
- **Necessity and proportionality:** Test whether automated ranking is necessary compared with simpler screening; restrict inputs to job-relevant information, prohibit unnecessary reuse, define retention and give applicants appropriate notice.
- **Risks:** Discrimination from biased training patterns, inaccurate extraction, exposure of sensitive CV information, recruiter automation bias, and unauthorised vendor access.
- **Mitigations:** Mask irrelevant sensitive fields; test across relevant applicant groups; require substantive reviewer checks and override; enforce access controls, DPA terms and deletion; document complaints and incident handling.
- **Decision:** The DPIA is not completed here. The employer-controller must assess residual risk and, if high risk remains despite measures, consider prior consultation with the supervisory authority under Article 36.

## One vendor DPA clause to require

**Purpose restriction and model training:** The vendor may process applicant data only on documented instructions for CV extraction and ranking and must not use applications, prompts, outputs or derived information to train or improve its general models without separate documented authorisation and an appropriate lawful basis. **Why:** It prevents a secondary use that applicants and employer-controllers may not expect and supports purpose limitation and processor accountability.

## If TalentBridge also serves UK applicants

**GO WITH CONDITIONS remains unchanged**, but the client must also assess the UK GDPR and Data Protection Act 2018 for UK applicant processing, UK-specific transfer rules and any relevant UK regulatory guidance. A UK GDPR DPIA, lawful basis and safeguards against solely automated significant decisions must be checked separately rather than assuming EU compliance is sufficient; identify any UK representative obligation where applicable.

# Stretch — Privacy by Design Checklist

**Highest-risk activity:** AI-assisted applicant scoring and ranking. Statuses describe the *unverified fictional scenario*, not findings from a deployed system.

| Control | Status | Evidence needed / action |
|---|---|---|
| Data minimisation | **Unknown** | Confirm irrelevant personal and Article 9 fields are removed or excluded from scoring. |
| Purpose binding | **Unknown** | Verify technical restrictions prevent secondary model training or unrelated reuse. |
| Access controls | **Unknown** | Inspect recruiter roles, vendor privileges and audit logs. |
| Retention enforcement | **Unknown** | Confirm automatic deletion/anonymisation of CVs, scores and vendor copies. |
| Subject rights workflow | **Unknown** | Test request routing and the GDPR's usual one-month response deadline (subject to lawful extensions). |
| Incident response | **Unknown** | Verify detection, processor-to-controller escalation, and controller notification to authority within 72 hours **where required and feasible**. |

*These optional sections are desk-based recommendations, not evidence of tested controls.*
