# GDPR Audit Pack — CV Screening with Human Review
# Author: Parisa Dehghani

**Scenario:** HR-tech CV-ranking tool with recruiter review  
**Option:** B(b) — CV screening with human review   
**Date:** 23 August 2026

> This is an educational audit exercise, not legal advice. Items marked **TBD — legal review** require confirmation from the client’s DPO or counsel.

## 1. Fact pattern and transition note

TalentRank GmbH is a German HR-tech startup with approximately 80 employees. It sells a recruitment platform to medium-sized employers in the EU/EEA. The platform receives approximately 50,000 applications per year through customer applicant-tracking-system integrations and recruitment portals. It analyses structured data such as years of experience, education, location, language, work authorisation, and skills, plus unstructured CVs, cover letters, and recruiter notes.

TalentRank’s model produces a candidate ranking and shortlist recommendation against a job description. A customer recruiter is expected to review the recommendation, confirm or override it, and decide whom to invite to interview. The stack is assumed to include an EU-hosted application database, an ATS integration, an EU cloud environment, an analytics/monitoring provider, and a non-EU AI/API vendor used for model inference or development. The exact vendor locations, sub-processors, retention settings, and transfer mechanism are **TBD — legal review**.

The applicants are EU/EEA job candidates. CVs may contain photographs, dates of birth, nationality, health/disability information, family information, trade-union activity, or other special-category or highly sensitive details even when those fields are not required. The model is intended to support recruitment, not to make a final hiring decision. However, a ranking that causes a candidate to be screened out may have a significant effect if the recruiter’s review is only a rubber stamp.

**Transition note:** This scenario applies the earlier GDPR/EU-stack lens to a new product: personal data is used not only to store applications but to score and rank people for employment. The core consulting question is whether the human review is genuinely meaningful and whether the AI Act, GDPR, and employment-law safeguards operate together.

## 2. Recognize: data categories and cross-border flow

### Personal-data categories

- Identity and contact data: name, email, phone number, address, applicant ID.
- Professional data: education, employment history, skills, certifications, languages, salary expectations, work authorisation, references.
- Free-text data: CV, cover letter, recruiter notes, interview notes.
- Potentially sensitive data: photograph, date of birth, nationality, disability/health information, family status, religion, trade-union activity, political activity, or inferred ethnicity.
- Inferred or scored data: match score, ranking, recommended shortlist, confidence, skills inferred from wording, and possible “culture fit” or personality indicators.

### Data subjects

Job applicants, including unsuccessful applicants, internal candidates, referees, and other people mentioned in CVs or references. Applicants may be vulnerable because the employment opportunity and their future income are at stake.

### Geography and transfers

Applicants are assumed to be in the EU/EEA and the startup is established in Germany. The non-EU AI/API vendor may create an international transfer or remote-access issue. Confirm whether data stays in the EU, whether the vendor is subject to an adequacy decision, whether Standard Contractual Clauses are used, whether a transfer impact assessment exists, and which supplementary measures apply.

## 3. Section A — Data map

| Field | Working answer | Confidence / next check |
|---|---|---|
| Categories of personal data | Identity/contact, CV and cover-letter text, education, employment, skills, location, language, work authorisation, salary expectations, recruiter notes, ranking/score, and possible sensitive data in free text or photographs. | Medium. Run a field inventory and sample CV review. |
| Sources | Applicant portal, employer ATS, job boards, CV uploads, cover letters, references, recruiter notes, and possibly public professional profiles. | Medium. Confirm whether public-profile scraping is used and whether applicants are informed. |
| Purpose 1 | Administer recruitment for the employer’s vacancy and select candidates for interview. | High. Employer’s core recruitment purpose. |
| Lawful basis for purpose 1 | For the employer controller, likely steps at the applicant’s request or legitimate interests, depending national employment law and the exact processing. TalentRank normally acts as processor on the employer’s documented instructions. | **TBD — legal review** per Member State and customer role. |
| Purpose 2 | Provide ranking, matching, and shortlist recommendations. | High. Same recruitment context but materially higher-risk profiling. |
| Lawful basis for purpose 2 | Usually follows the employer’s lawful recruitment purpose when TalentRank is a processor; if TalentRank determines its own purposes, it may need a separate documented basis and transparency analysis. Do not rely on consent merely because it is easy to collect from applicants. | **TBD — legal review**. |
| Purpose 3 | Improve TalentRank’s model and product using applicant data. | Medium. This is a secondary purpose and may not be covered by the employer’s instructions or applicant notice. | 
| Lawful basis for purpose 3 | **TBD — legal review.** Consider whether data can be anonymised or trained using synthetic/consented data; if legitimate interests is proposed, document purpose, necessity, balancing, safeguards, and objection handling. |
| Retention per purpose | Active recruitment: vacancy and hiring-record period set by the employer and national law. Unsuccessful applicants: limited period for challenge/recruitment compliance, then delete or anonymise. Model-training extracts: shortest documented period; do not retain raw CVs indefinitely. | **TBD — legal review** and automate deletion. |
| Recipients and sub-processors | Employer recruiters, TalentRank staff, ATS provider, EU cloud/GPU provider, monitoring/logging provider, non-EU AI/API vendor, and support/security vendors. | Obtain current sub-processor list and role matrix. |
| International transfers | Possible non-EU inference, support access, telemetry, or model-development processing. | Confirm adequacy/SCC/TIA, encryption, access controls, and deletion settings. |

### Lawful-basis note

The six Article 6 bases are consent, contract, legal obligation, vital interests, public task, and legitimate interests. In recruitment, the employer’s role, national employment law, the application context, and whether the processing is necessary must be assessed together. For TalentRank’s own model-improvement purpose, do not assume that the employer’s recruitment basis transfers automatically. If legitimate interests is considered, document the three-step test: **purpose, necessity, and balancing**.

## 4. Section B — Risk and rights

### Special-category data — Article 9

CVs and cover letters may contain health/disability information, trade-union membership, religious beliefs, political opinions, ethnicity or nationality information, or biometric information in photographs. The tool should not collect or infer these fields for ranking. The safest design is to exclude photographs and free-text sensitive fields, apply redaction and sensitive-attribute detection, and prohibit “culture fit,” personality, emotion, or protected-trait proxies unless legal review establishes a narrow lawful basis and safeguards. A special-category exception cannot be assumed. **TBD — legal review.**

### Automated decision-making — Article 22

The ranking and shortlist recommendation is profiling. If a recruiter independently reviews the recommendation, understands its limitations, can access the relevant information, and can genuinely override it, the final decision may not be “solely automated.” However, a nominal human click is not enough. If the recruiter routinely accepts the ranking, cannot see why a candidate was excluded, lacks time or authority to challenge it, or the score automatically blocks applicants, Article 22 risk remains high.

If Article 22 applies, the client must assess whether the decision has legal or similarly significant effects, whether an exception applies, and what safeguards are available, including meaningful human intervention, the ability to express a view, and the ability to contest the decision. National employment law may add stronger safeguards. The system should never silently reject a candidate based only on a model score.

### DPIA assessment

**Recommendation: a DPIA is required before deployment.** The EDPB’s high-risk criteria strongly point in that direction:

1. **Evaluation or scoring:** candidates are ranked and scored for employment selection.
2. **Systematic monitoring:** the system may continuously evaluate application pools and candidate characteristics.
3. **Sensitive data:** CVs may include Article 9 data or proxies for it.
4. **Large scale:** approximately 50,000 applications per year across multiple employers.
5. **Matching or combining data:** ATS records, CVs, job descriptions, recruiter notes, and possibly public-profile data are combined.
6. **Vulnerable data subjects:** applicants depend on fair treatment in access to employment.
7. **Innovative technology:** generative or machine-learning ranking introduces opacity, bias, and drift risks.
8. **Cross-border processing:** a non-EU AI/API vendor may access applicant data.
9. **Denial or exclusion risk:** a low score can stop an applicant from reaching a recruiter or interview.

The DPIA should include necessity and proportionality, discrimination and proxy analysis, explainability, human oversight, appeal routes, data quality, security, retention, vendor controls, and testing across protected and intersectional groups. If high residual risk remains, consult the supervisory authority before processing.

### Data-subject friction points

Applicants may ask for access to their CV, score, ranking factors, source data, retention period, and logic used in the recommendation. They may object to profiling, request erasure, challenge inaccurate CV extraction, or ask why they were not shortlisted. The controller must be clear about who receives the request: the employer is normally controller for recruitment, while TalentRank must assist as processor. The system needs a searchable audit trail linking source fields, model version, score, recruiter action, and deletion status.

### Controller / processor split

- **Hiring employer:** likely controller because it decides the vacancy, selection purpose, criteria, and final recruitment decision.
- **TalentRank:** likely processor when it ranks applicants on the employer’s documented instructions.
- **TalentRank:** may become an independent controller for its own model training, benchmarking, product analytics, or use of applicant data across customers. The actual purposes and decisions—not only the contract—determine the role.
- **ATS, cloud, AI/API, monitoring, and support vendors:** processors or sub-processors where they process applicant data on instructions.

### DPA requirement

Yes. The employer and TalentRank need a GDPR Article 28-compliant DPA if TalentRank processes applications on the employer’s behalf. TalentRank also needs compliant DPAs with its sub-processors, including the ATS connector, cloud/GPU provider, monitoring service, and non-EU AI/API vendor. The DPA should restrict secondary use, unauthorised model training, sub-processor changes, data retention, and international access, and should require assistance with rights, DPIAs, security incidents, audits, and deletion.

## 5. Section C — Law stacking

### AI Act cross-check

This tool is **likely high-risk under the AI Act employment/recruitment category** because it evaluates or filters natural persons for recruitment and selection. Human review does not remove the high-risk classification. The provider/deployer should plan for risk management, data governance, technical documentation, logging, accuracy/robustness, transparency, human oversight, and post-market monitoring. The recruiter’s review must be meaningful, not a rubber stamp. The client should also document AI literacy and tell affected users when AI is used in the recruitment process where required.

### ePrivacy check

The core screening decision uses CV and ATS data, not necessarily cookies. ePrivacy is therefore **conditional**. If the recruitment portal uses non-essential analytics cookies, tracking pixels, or device-level identifiers, assess consent before storing or accessing information on the applicant’s device. GDPR then governs the later personal-data processing. Do not use cookie consent as a substitute for the recruitment processing analysis.

### Data Act check

The Data Act is **N/A on the current facts** because CV screening does not involve connected products, IoT-generated data, or cloud-switching rights. Recheck only if TalentRank’s platform is embedded in a connected workplace product or the engagement includes regulated cloud portability work.

## 6. Client recommendation memo

**To:** TalentRank CEO, Product Lead, DPO, and Employment-Law Counsel  
**From:** Parisa Dehghani
**Subject:** GDPR and EU AI Act recommendation for CV-ranking tool

### Bottom line: go with conditions, not automatic deployment

TalentRank may continue with a controlled pilot, but it should not deploy the ranking tool for live applicant screening until the DPIA, AI Act high-risk controls, meaningful-human-review design, lawful-basis analysis, and vendor/transfer package are approved. A recruiter clicking “confirm” is not sufficient if the tool silently excludes candidates or the recruiter cannot challenge the score.

### Top three actions

1. **Redesign the decision path.** The model may organise evidence and suggest a shortlist, but it must not automatically reject applicants. Require recruiters to see the relevant CV evidence, uncertainty, missing-data warnings, and reasons for the recommendation. Record the recruiter’s independent decision and allow an override without penalty.
2. **Complete the legal and technical assessment before the pilot.** Run a DPIA, classify the system as likely high-risk under the AI Act, document the employer/TalentRank controller-processor split, confirm Article 22 safeguards, and prohibit photographs, sensitive attributes, and protected-trait proxies from ranking.
3. **Secure the data and vendor chain.** Sign DPAs, confirm retention and deletion, test applicant access/erasure/objection workflows, document the non-EU transfer mechanism, and require the AI/API vendor not to use applicant data for its own training.

The pilot should start with synthetic and historical cases that have been minimised and reviewed, not unrestricted live applicant data.

### Residual risks

Bias can remain even after protected fields are removed because education, address, language, career gaps, and writing style may act as proxies. Human reviewers may over-trust a confident score, and an applicant may struggle to understand or challenge a ranking created by several model components. Model drift, vendor changes, and inaccurate CV extraction can also produce unfair outcomes. TalentRank should therefore monitor subgroup performance, appeal outcomes, override rates, and recruiter reliance after launch.

## 7. Phase 4 — Peer-review rubric

No partner feedback was supplied, so this is a **self-review / mock client review**, not evidence of a completed partner swap.

| Criterion | Score 1–3 | Self-review comment |
|---|---:|---|
| Clear bottom-line recommendation | 3 | The pilot may continue, but live deployment waits for controls. |
| Lawful basis selection is justified | 2 | The audit distinguishes employer recruitment from TalentRank’s own product-improvement purpose and leaves national-law points for review. |
| Top actions are specific and sequenced | 3 | Redesign decision path, complete legal/technical assessment, then secure vendors and rights workflows. |
| Residual risks are named honestly | 3 | Proxy bias, automation bias, drift, vendor changes, and inaccurate extraction are disclosed. |
| AI Act / ePrivacy / Data Act addressed | 3 | The likely high-risk AI Act classification is central; ePrivacy is conditional; Data Act is currently N/A. |

**Mock client response:** We accept the conditional pilot recommendation. Before testing on live applicants, we want proof that recruiters can override the model, that no automatic rejection is hidden in the workflow, and that the vendor contract prevents secondary training use of applicant data.

## 8. DPIA outline

- **Description:** applicant sources, CV fields, job descriptions, ranking logic, recruiter workflow, vendors, locations, retention, and model lifecycle.
- **Necessity and proportionality:** why ranking is needed, whether a simpler rule-based shortlist is sufficient, data minimisation, applicant notice, and less intrusive alternatives.
- **Risks:** discrimination, proxy use, inaccurate extraction, exclusion, automation bias, lack of contestability, special-category inference, vendor access, transfer, security breach, and retention failure.
- **Mitigations:** remove photographs and sensitive fields, proxy testing, representative validation data, confidence thresholds, human override, explanation/evidence display, logging, appeals, access controls, deletion, DPAs, transfer safeguards, and monitoring.
- **Residual risk decision:** DPO, employment-law, and AI governance approval; supervisory consultation if high residual risk remains.

## 9. Data-protection-by-design checklist

| Control | Status | Recommended action |
|---|---|---|
| Data minimisation | Fails / unknown | Remove photographs, unnecessary demographics, and free-text sensitive data from ranking inputs. |
| Purpose binding | Unknown | Restrict applicant data to the employer’s vacancy purpose; separate product-improvement datasets. |
| Access controls | Unknown | Limit raw CVs and scores to authorised recruiters; isolate vendor and engineering access. |
| Retention enforcement | Unknown | Delete unsuccessful applications and model extracts according to employer/national rules. |
| Subject-rights workflow | Unknown | Provide access, correction, objection, erasure, and contest routes with score and recruiter-action traceability. |
| Meaningful human oversight | Fails / unknown | Require evidence review, override authority, time, training, and logging; prohibit rubber-stamp approval. |
| Bias and accuracy monitoring | Unknown | Test subgroup error rates, proxy effects, drift, override rates, and appeal outcomes. |
| Incident response | Partial / unknown | Define breach detection, escalation, documentation, and notification decisions within 72 hours. |

## Sources

- GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- EDPB automated decision-making and profiling: https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en
- EDPB DPIA guidance: https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en
- EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- ePrivacy Directive: https://eur-lex.europa.eu/eli/dir/2002/58/oj/eng
- Data Act: https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng
