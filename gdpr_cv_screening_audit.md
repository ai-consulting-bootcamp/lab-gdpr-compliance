# GDPR Audit Pack — CV Screening and Ranking

**Scenario:** Case 2 — CV Screening and Ranking (Recruitment)
**Client:** National recruitment company
**Auditors:** [Your Name] and [Teammate Name]
**Date:** 19 August 2026

---

# Part I — Audit Worksheet

## Transition Note — From EU AI Act to GDPR

This audit carries forward Case 2 — CV Screening and Ranking from the EU AI Act peer-audit exercise. Under the previous assessment, the system was classified as a high-risk AI system under Annex III(4)(a) because it is intended to be used for recruitment and candidate selection or ranking. This case is particularly relevant for a GDPR audit because the system processes candidate personal data, creates candidate rankings and profiles, and may significantly influence access to employment opportunities. The proposed human review does not remove the need to assess GDPR requirements, particularly lawful basis, purpose limitation, data minimisation, Article 22 automated decision-making, data subject rights, DPIA requirements, retention, and international transfers.

---

## Phase 1 — Fact Pattern

### Fact Pattern

A national recruitment company wants to reduce the time recruiters spend screening applications for large-volume vacancies. The company proposes an AI system that analyses candidate CVs, application answers, and relevant professional information, then ranks candidates against the requirements of each vacancy. Recruiters receive a recommended shortlist together with an explanation of the factors that influenced each candidate's ranking. A recruiter reviews the shortlist before candidates are invited to interviews and has authority to reject or add candidates. The recruitment company intends to use the system across several recruitment offices and retain assessment results for future hiring campaigns. The scenario does not specify the company's exact size, the precise EU/EEA countries in which candidates are located, the volume of candidate data, the exact categories of professional information processed, the retention period, or whether any special-category data may be present in the source material. The architecture may also include a licensed CV-parsing or NLP component supplied by a third-party vendor, but the vendor's location and processing arrangements are not specified.

### Required Fact-Pattern Questions

| Question                                                                            | Assessment                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Who is the client?**                                                              | A national recruitment company operating across several recruitment offices.                                                                                                                                                                                       |
| **Approximate size**                                                                | **TBD — scenario does not specify.** The company is described as national and operating across several offices.                                                                                                                                                    |
| **What personal data is processed?**                                                | CVs, application answers, education and qualifications, employment history, professional skills and experience, ranking results, ranking factors, shortlist status, recruiter decisions, and retained assessment results.                                          |
| **Who are the data subjects?**                                                      | Job applicants and candidates.                                                                                                                                                                                                                                     |
| **Where are the data subjects located?**                                            | **TBD — scenario does not specify.** EU/EEA and third-country locations must be confirmed.                                                                                                                                                                         |
| **Who are the vendors?**                                                            | The architecture may include a licensed third-party CV-parsing/NLP component. The vendor identity, location, and processing role are **TBD — legal review**.                                                                                                       |
| **Does a non-EU vendor process the data?**                                          | **TBD — scenario does not specify.** Vendor processing locations must be verified before assessing international transfers.                                                                                                                                        |
| **What does the AI system do?**                                                     | Analyses candidate information, ranks candidates against vacancy requirements, generates explanations of ranking factors, and produces a recommended shortlist for recruiter review.                                                                               |
| **Is there automated decision-making with legal or similarly significant effects?** | **TBD — legal review.** The system automatically ranks candidates, but a recruiter reviews, rejects, or adds candidates before interview invitations. The meaningfulness of this human intervention and any significant effects must be assessed under Article 22. |

---

## CFU 1 — Recognize

### Personal Data Categories

The system processes personal data contained in:

* CVs
* Application answers
* Professional information
* Education and qualifications
* Employment history
* Professional skills and experience
* Candidate ranking results
* Factors contributing to the ranking
* Recommended shortlist status
* Recruiter decisions to reject or add candidates
* Assessment results retained for future campaigns

These data are linked to identifiable job applicants and therefore fall within the scope of GDPR personal-data processing.

### Special-Category Data — Article 9

The scenario does not state that special-category personal data is intentionally processed.

However, CVs and application answers may potentially contain information revealing characteristics such as health information, disability, racial or ethnic origin, religious beliefs, trade-union membership, or other Article 9 categories.

The system should therefore not assume that Article 9 data is absent merely because it is not an explicit input field.

**Assessment: TBD — privacy/legal review required to determine whether special-category data is collected, inferred, or used in the ranking process.**

### Data Subjects

The primary data subjects are job applicants and candidates.

The system therefore processes personal data in the context of recruitment and employment-related decision-making.

### Geographic Scope

The scenario describes a national recruitment company and several recruitment offices, but does not specify the country or countries involved.

**Assessment: TBD — confirm the relevant EU/EEA jurisdictions and whether any candidates are located outside the EU/EEA.**

### Automated Decision-Making

The system automatically analyses candidate information and ranks candidates against vacancy requirements.

However, the scenario states that a recruiter reviews the recommended shortlist before candidates are invited to interviews and that recruiters can reject or add candidates themselves.

The available facts therefore do not establish that the AI system makes the final recruitment decision by itself.

Nevertheless, the system materially influences the recruitment process because its ranking determines the recommended shortlist presented to recruiters.

The applicability of GDPR Article 22 should therefore be assessed carefully, including whether any recruitment decision produces legal or similarly significant effects on candidates and whether the human review is genuinely meaningful rather than merely formal.

**Assessment: TBD — legal/privacy review required before deployment.**

### Future Campaign Reuse

The proposed retention of candidate assessment results for future hiring campaigns creates a specific purpose-limitation and retention question.

Candidate information collected for one vacancy cannot automatically be assumed to be appropriate for unrestricted reuse in future recruitment campaigns.

The audit must establish:

1. The original purpose for which the candidate data was collected.
2. Whether future recruitment campaigns are compatible with that original purpose.
3. Whether candidates were informed about future reuse.
4. What data will be retained.
5. For how long it will be retained.
6. Whether the candidate can object to or request deletion of the retained information.
7. Whether old assessment results will be reused to rank candidates against substantially different vacancy requirements.

**Initial assessment: Significant privacy risk requiring further analysis.**

---

# Phase 2 — Mini GDPR Audit Worksheet

## Section A — Data Map

| Field                                                       | Your answer                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Categories of personal data**                             | CV content; identification/contact information contained in CVs; education and qualifications; employment history; professional skills and experience; application answers; vacancy-specific assessment information; AI-generated ranking results; factors contributing to rankings; recommended-shortlist status; recruiter decisions; retained assessment results. **Special-category data: TBD — legal review.** |
| **Sources (where data comes from)**                         | Candidate CVs; candidate application forms and application answers; professional information submitted during recruitment; potentially third-party CV-parsing/NLP services. The scenario does not establish any additional data sources.                                                                                                                                                                            |
| **Purpose 1 — Recruitment screening and candidate ranking** | Analyse candidate information and rank applicants against the requirements of a specific vacancy in order to support recruiter screening and shortlist preparation.                                                                                                                                                                                                                                                 |
| **Lawful basis — Purpose 1**                                | **TBD — legal review.** Legitimate interests may be considered, subject to the three-step LIA test: a legitimate recruitment/screening purpose, necessity of the processing for that purpose, and balancing against candidates' rights and interests. Consent should not be assumed merely because candidates submit an application.                                                                                |
| **Purpose 2 — Recruiter review and interview selection**    | Provide recruiters with a recommended shortlist and explanations so that recruiters can review, reject, or add candidates before interview invitations are issued.                                                                                                                                                                                                                                                  |
| **Lawful basis — Purpose 2**                                | **TBD — legal review.** The appropriate Article 6 basis depends on the recruitment relationship, controller roles, candidate expectations, and applicable national employment law.                                                                                                                                                                                                                                  |
| **Purpose 3 — Retention for future hiring campaigns**       | Retain candidate assessment results for possible reuse in future recruitment campaigns.                                                                                                                                                                                                                                                                                                                             |
| **Lawful basis — Purpose 3**                                | **TBD — legal review.** The original recruitment purpose does not automatically justify indefinite or unrestricted reuse for future vacancies. Compatibility, candidate information, retention limits, and any applicable objection/erasure rights must be assessed.                                                                                                                                                |
| **Retention period per purpose**                            | Current scenario does not specify a retention period. **TBD — legal review.** A defined retention schedule should distinguish between data needed for the current recruitment process and assessment results retained for future campaigns.                                                                                                                                                                         |
| **Recipients and sub-processors**                           | Recruitment company and relevant recruitment offices/client organisations; authorised recruiters; potentially a licensed third-party CV-parsing/NLP vendor. The exact vendor list and controller/processor relationships are **TBD — legal review**.                                                                                                                                                                |
| **International transfers and transfer mechanism**          | **TBD — legal review.** The scenario does not establish where vendors process data or whether any data leaves the EU/EEA. The locations and processing arrangements of all non-EU/EEA vendors must be verified before determining whether a Chapter V transfer mechanism, such as an adequacy decision or appropriate safeguards, is required.                                                                      |

---

## Section B — Risk and Rights

### 1. Special-Category Data — Article 9

**Assessment: TBD — legal review.**

CVs and application answers may contain or reveal special-category personal data even where these categories are not explicitly requested. The recruitment company should determine whether Article 9 data is collected, inferred, used by the ranking model, or included in retained assessment results. If Article 9 data is processed, an applicable Article 9(2) condition and appropriate safeguards must be identified before deployment.

### 2. Automated Decision-Making — Article 22

**Assessment: TBD — legal review.**

The system ranks candidates automatically, but a recruiter reviews the recommended shortlist and can reject or add candidates. The key question is whether this human intervention is meaningful and whether the resulting recruitment decision produces legal or similarly significant effects. The organisation should document the human-review process and assess Article 22 before deployment.

### 3. DPIA Requirement

**Assessment: DPIA likely required — legal review/confirmation recommended.**

The proposed processing involves AI-based evaluation and ranking of candidates in a recruitment context and therefore presents significant risks to individuals. Relevant DPIA criteria include evaluation or scoring, automated decision-making, systematic evaluation, vulnerable data subjects, and the potentially significant impact on access to employment opportunities. A DPIA should be completed before deployment if the processing is likely to result in a high risk to candidates' rights and freedoms.

### 4. Data Subject Rights and Friction Points

The main friction points are likely to include the right of access, the right to erasure, the right to object to processing or profiling, and requests for information about how candidate data was used in ranking. Future-campaign reuse may create additional difficulties if candidates expect their information to be used only for the original vacancy.

### 5. Controller / Processor Split

The recruitment company would provisionally be treated as the **controller** for the recruitment processing because it determines the purposes and essential means of processing candidate data.

A third-party CV-parsing/NLP vendor would potentially act as a **processor** if it processes candidate data solely on the recruitment company's documented instructions. The exact role must be confirmed from the contractual and technical arrangement.

### 6. Data Processing Agreements

A DPA would generally be required where a vendor qualifies as a processor under Article 28 GDPR. The recruitment company should identify every vendor processing candidate data and verify whether an appropriate Article 28 agreement and required processor safeguards are in place.

---

## Section C — Law Stacking

### AI Act Cross-Check

The system is a **high-risk AI system under Annex III(4)(a)** because it is intended for recruitment and candidate selection/ranking. The AI Act adds AI-specific requirements such as risk management, data governance, technical documentation, logging, human oversight, accuracy, robustness, and cybersecurity controls that are not replaced by GDPR compliance.

### ePrivacy Check

**N/A based on the current scenario.**

The scenario does not mention cookies, tracking pixels, electronic communications metadata, or device-level tracking. If recruitment websites later use cookies or similar tracking technologies to collect candidate information, ePrivacy requirements must be assessed separately.

### Data Act Check

**N/A based on the current scenario.**

The system does not involve a connected product, IoT-generated data, or connected-device data. The Data Act therefore does not appear to be a primary requirement for this use case based on the available facts.

---

# Part II — Client Recommendation Memo

## Phase 3 — Client Recommendation Memo

### Recommendation: Go with Conditions

**To:** National Recruitment Company
**Subject:** GDPR assessment — AI CV Screening and Ranking

The proposed AI recruitment screening system can proceed only with conditions before production deployment. The system processes candidate personal data to analyse CVs, application answers and professional information, generate candidate rankings and support recruiter shortlisting. Because these activities can significantly influence access to employment opportunities, the organisation should treat privacy, fairness and human oversight as core deployment controls rather than as post-deployment measures.

The first priority is to establish and document the lawful basis for each processing purpose. The company should distinguish between screening for a specific vacancy, recruiter decision-making, and retention or reuse for future campaigns. Legitimate interests may potentially be considered for some recruitment activities, but this should not be assumed without completing the purpose, necessity and balancing assessment. Candidate expectations, transparency and applicable national employment rules must also be considered.

The second priority is to complete a DPIA and assess Article 22 GDPR before deployment. The organisation must establish whether the recruiter review constitutes meaningful human intervention and whether any recruitment decisions could have legal or similarly significant effects. The DPIA should also address potential Article 9 data, profiling, discrimination risks, data minimisation, security, retention and candidate rights.

The third priority is to establish clear data-governance controls for future campaign reuse and third-party processing. Candidate assessment results should not be retained indefinitely or automatically reused for unrelated vacancies. The company should define retention periods, purposes, deletion procedures and rules for cross-campaign reuse. All vendors processing candidate data should also be mapped and their processor/controller roles and contractual safeguards confirmed.

**Top three required actions before go-live:**

1. Complete the lawful-basis, Article 22 and DPIA assessment.
2. Establish retention, purpose-limitation and future-campaign reuse controls.
3. Complete vendor, DPA and international-transfer assessments.

**Residual risks:** Even if the project proceeds, residual risks include candidate challenges to automated profiling, potential bias or discrimination, incorrect rankings, inappropriate reuse of historical assessment data, and uncertainty around special-category data contained or inferred from CVs.

**Bottom line:** **Go with conditions.** Deployment should proceed only after the above controls are implemented and verified.

---

# Part III — Peer Verification

## Phase 4 — Verify

**Status:** To be completed after exchanging the recommendation memo with the teammate.

### Peer Review

**Reviewer:** [Teammate Name]
**Date:** [Date]

**1. Did the reviewer accept the recommendation?**

[To be completed.]

**2. Finding challenged by the reviewer:**

[To be completed.]

**3. Requested redesign or clarification:**

[To be completed.]

**4. Reviewer comments:**

[To be completed.]

---

# Part IV — Debrief

## Phase 5 — Debrief

**Status:** To be completed after the peer review.

### Points of Agreement

* [To be completed.]
* [To be completed.]
* [To be completed.]

### Points of Divergence

* [To be completed.]
* [To be completed.]

### Lawful Basis Discussion

**Audit position:** [To be completed.]

**Teammate position:** [To be completed.]

**Agreed position:** [To be completed.]

### DPIA Discussion

**Audit position:** [To be completed.]

**Teammate position:** [To be completed.]

**Agreed position:** [To be completed.]

### Final Debrief Conclusion

[To be completed after discussion with the teammate.]
