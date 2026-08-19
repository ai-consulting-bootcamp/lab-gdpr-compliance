# GDPR Audit Pack — CV Screening and Ranking

**Scenario:** Case 2 — CV Screening and Ranking (Recruitment)
**Client:** National recruitment company
**Auditors:** Vincent de Paul and Akansha
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

| Question                                                                            | Assessment                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Who is the client?**                                                              | A national recruitment company operating across several recruitment offices.                                                                                                                                                                                                                                                                    |
| **Approximate size**                                                                | **TBD — scenario does not specify.** The company is described as national and operating across several offices.                                                                                                                                                                                                                                 |
| **What personal data is processed?**                                                | CV content; identification and contact information contained in CVs; education and qualifications; employment history; professional skills and experience; application answers; vacancy-specific assessment information; AI-generated ranking results; ranking factors; shortlist status; recruiter decisions; and retained assessment results. |
| **Who are the data subjects?**                                                      | Job applicants and candidates.                                                                                                                                                                                                                                                                                                                  |
| **Where are the data subjects located?**                                            | **TBD — scenario does not specify.** The relevant EU/EEA jurisdictions and any third-country locations must be confirmed.                                                                                                                                                                                                                       |
| **Who are the vendors?**                                                            | The architecture may include a licensed third-party CV-parsing/NLP component. The vendor identity, location, contractual role, and processing arrangements are **TBD — legal review**.                                                                                                                                                          |
| **Does a non-EU vendor process the data?**                                          | **TBD — scenario does not specify.** Vendor processing locations must be verified before assessing international transfers.                                                                                                                                                                                                                     |
| **What does the AI system do?**                                                     | Analyses candidate information, ranks candidates against vacancy requirements, generates explanations of ranking factors, and produces a recommended shortlist for recruiter review.                                                                                                                                                            |
| **Is there automated decision-making with legal or similarly significant effects?** | **TBD — legal review.** The system automatically ranks candidates, but a recruiter reviews the recommended shortlist and can reject or add candidates before interview invitations. The meaningfulness of this human intervention and any significant effects must be assessed under Article 22.                                                |

---

## CFU 1 — Recognize

### Personal Data Categories

The system processes personal data contained in:

* CVs
* Application answers
* Identification and contact information
* Education and qualifications
* Employment history
* Professional skills and experience
* Candidate ranking results
* Factors contributing to the ranking
* Recommended-shortlist status
* Recruiter decisions to reject or add candidates
* Assessment results retained for future campaigns

These data are linked to identifiable job applicants and therefore fall within the scope of GDPR personal-data processing.

### Special-Category Data — Article 9

The scenario does not state that special-category personal data is intentionally processed.

However, CVs and application answers may potentially contain or reveal information relating to Article 9 categories, including health or disability information, racial or ethnic origin, religious or philosophical beliefs, or trade-union membership.

The system should therefore not assume that Article 9 data is absent merely because these categories are not explicit input fields.

**Assessment: TBD — privacy/legal review required to determine whether special-category data is collected, inferred, or used in the ranking process.**

### Data Subjects

The primary data subjects are job applicants and candidates.

The system therefore processes personal data in the context of recruitment and employment-related decision-making.

### Geographic Scope

The scenario describes a national recruitment company and several recruitment offices, but does not specify the country or countries involved.

**Assessment: TBD — confirm the relevant EU/EEA jurisdictions and whether any candidates or vendors are located outside the EU/EEA.**

### Automated Decision-Making

The system automatically analyses candidate information and ranks candidates against vacancy requirements.

However, the scenario states that a recruiter reviews the recommended shortlist before candidates are invited to interviews and that recruiters can reject or add candidates themselves.

The available facts therefore do not establish whether the system falls within Article 22's prohibition on solely automated decisions producing legal or similarly significant effects.

The key issue is whether recruiter intervention is genuinely meaningful, involves sufficient authority and competence to challenge the AI output, and actually influences the final recruitment decision rather than merely confirming the system's recommendation.

**Assessment: TBD — legal/privacy review required before deployment.**

### Future Campaign Reuse

The proposed retention of candidate assessment results for future hiring campaigns creates a specific purpose-limitation, transparency, and retention question.

Candidate information collected for one vacancy cannot automatically be assumed to be appropriate for unrestricted reuse in future recruitment campaigns.

The audit must establish:

1. The original purpose for which candidate data was collected.
2. Whether future recruitment campaigns are compatible with that original purpose.
3. Whether candidates were informed about future reuse.
4. What data will be retained.
5. For how long it will be retained.
6. Whether candidates can exercise applicable erasure or objection rights.
7. Whether historical assessment results will be reused to rank candidates against substantially different vacancy requirements.

**Initial assessment: Significant privacy risk requiring further analysis.**

---

# Phase 2 — Mini GDPR Audit Worksheet

## Section A — Data Map

| Field                                                       | Your answer                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Categories of personal data**                             | CV content; identification/contact information; education and qualifications; employment history; professional skills and experience; application answers; vacancy-specific assessment information; AI-generated ranking results; ranking factors; shortlist status; recruiter decisions; retained assessment results. **Special-category data: TBD — legal review.** |
| **Sources (where data comes from)**                         | Candidate CVs; candidate application forms and application answers; professional information submitted during recruitment; and potentially a third-party CV-parsing/NLP service. The scenario does not establish any additional data sources.                                                                                                                         |
| **Purpose 1 — Recruitment screening and candidate ranking** | Analyse candidate information and rank applicants against the requirements of a specific vacancy to support recruiter screening and shortlist preparation.                                                                                                                                                                                                            |
| **Lawful basis — Purpose 1**                                | **TBD — legal review.** Legitimate interests may potentially be considered, subject to the three-step LIA test: legitimate recruitment/screening purpose, necessity of the processing, and balancing against candidates' rights and interests. Consent should not be assumed merely because candidates submit an application.                                         |
| **Purpose 2 — Recruiter review and interview selection**    | Provide recruiters with a recommended shortlist and explanations so recruiters can review, reject, or add candidates before interview invitations are issued.                                                                                                                                                                                                         |
| **Lawful basis — Purpose 2**                                | **TBD — legal review.** The appropriate Article 6 basis depends on the recruitment relationship, controller roles, candidate expectations, and applicable national employment law.                                                                                                                                                                                    |
| **Purpose 3 — Retention for future hiring campaigns**       | Retain candidate assessment results for possible reuse in future recruitment campaigns.                                                                                                                                                                                                                                                                               |
| **Lawful basis — Purpose 3**                                | **TBD — legal review.** The original recruitment purpose does not automatically justify indefinite or unrestricted reuse for future vacancies. Compatibility, transparency, retention limits, and applicable objection/erasure rights must be assessed.                                                                                                               |
| **Retention period per purpose**                            | **TBD — legal review.** The scenario does not specify a retention period. A documented retention schedule should distinguish data needed for the current recruitment process from assessment results retained for future campaigns.                                                                                                                                   |
| **Recipients and sub-processors**                           | Recruitment company and relevant recruitment offices/client organisations; authorised recruiters; and potentially a licensed third-party CV-parsing/NLP vendor. The exact vendor list and controller/processor relationships are **TBD — legal review**.                                                                                                              |
| **International transfers and transfer mechanism**          | **TBD — legal review.** The scenario does not establish whether data leaves the EU/EEA. Vendor locations and processing arrangements must be verified before determining whether a Chapter V transfer mechanism, such as an adequacy decision or appropriate safeguards, is required.                                                                                 |

### Article 6 Lawful-Basis Options Considered

The six Article 6 lawful-basis options are:

* **Consent**
* **Contract**
* **Legal obligation**
* **Vital interests**
* **Public task**
* **Legitimate interests**

For this scenario, **legitimate interests may be relevant for some recruitment-processing purposes**, but this cannot be confirmed from the available facts. The organisation must complete the three-step LIA test:

1. **Purpose:** Is there a legitimate recruitment/screening interest?
2. **Necessity:** Is the proposed AI processing necessary to achieve that purpose?
3. **Balancing:** Do the organisation's interests override the candidates' rights and freedoms?

**Final position: TBD — legal review.**

---

## Section B — Risk and Rights

### 1. Special-Category Data — Article 9

**Assessment: TBD — legal review.**

CVs and application answers may contain or reveal special-category personal data even where these categories are not explicitly requested. The recruitment company should determine whether Article 9 data is collected, inferred, used by the ranking model, or included in retained assessment results. If Article 9 data is processed, an applicable Article 9(2) condition and appropriate safeguards must be identified before deployment.

### 2. Automated Decision-Making — Article 22

**Assessment: TBD — legal review.**

The system ranks candidates automatically, but a recruiter reviews the recommended shortlist and can reject or add candidates. The key question is whether this human intervention is genuinely meaningful and whether the resulting recruitment decision produces legal or similarly significant effects. If Article 22 applies, the organisation must implement the applicable safeguards, including appropriate human intervention and the candidate's ability to contest the decision where required.

### 3. DPIA Requirement — EDPB Criteria

**Assessment: DPIA likely required — legal review/confirmation recommended.**

The proposed processing presents several EDPB DPIA criteria:

1. **Evaluation or scoring** — candidates are automatically evaluated and ranked.
2. **Automated decision-making** — AI-generated rankings may influence recruitment decisions.
3. **Systematic evaluation** — candidate information is systematically assessed against vacancy requirements.
4. **Sensitive or highly personal data** — CVs may contain sensitive information or reveal Article 9 data.
5. **Data concerning vulnerable data subjects** — job applicants may be in a position of reduced power relative to recruitment organisations.
6. **Innovative technological or organisational solutions** — the system introduces AI-based recruitment ranking.
7. **Large-scale processing** — the company operates nationally and across several offices, although the exact volume is **TBD**.
8. **Matching or combining datasets** — CV information, application answers and professional information are combined to generate rankings.
9. **Preventing data subjects from exercising a right or using a service** — ranking may influence access to employment opportunities.

Because several criteria are present, a DPIA should be completed before deployment and used to identify and mitigate risks to candidates' rights and freedoms.

### 4. Data Subject Rights and Friction Points

The main friction points are likely to include the right of access, the right to erasure, and the right to object to processing or profiling. Candidates may also request information about how their data contributed to a ranking. Future-campaign reuse may create additional difficulties if candidates reasonably expect their information to be used only for the original vacancy.

### 5. Controller / Processor Split

The recruitment company would provisionally be treated as the **controller** for the recruitment processing because it determines the purposes and essential means of processing candidate data.

A third-party CV-parsing/NLP vendor would potentially act as a **processor** if it processes candidate data solely on the recruitment company's documented instructions. The exact role must be confirmed from the contractual and technical arrangement.

If recruitment-office clients determine their own purposes and essential means rather than acting solely under the recruitment company's instructions, their role may require separate controller or joint-controller analysis.

### 6. Data Processing Agreements

A DPA would generally be required where a vendor qualifies as a processor under Article 28 GDPR.

The recruitment company should identify every vendor processing candidate personal data and verify whether an appropriate Article 28 agreement, confidentiality requirements, security measures, subprocessor controls, and assistance obligations are in place.

---

## Section C — Law Stacking

### AI Act Cross-Check

**High-risk — Annex III(4)(a).** The system is intended for recruitment and candidate selection/ranking. The AI Act adds AI-specific requirements such as risk management, data governance, technical documentation, logging, human oversight, accuracy, robustness, and cybersecurity controls that are not replaced by GDPR compliance.

### ePrivacy Check

**N/A based on the current scenario.** The scenario does not mention cookies, tracking pixels, electronic communications metadata, or device-level tracking. If recruitment websites later use cookies or similar tracking technologies to collect candidate information, ePrivacy requirements must be assessed separately.

### Data Act Check

**N/A based on the current scenario.** The system does not involve a connected product, IoT-generated data, or connected-device data. The Data Act therefore does not appear to be a primary requirement for this use case based on the available facts.

---

# Part II — Client Recommendation Memo

## Phase 3 — Client Recommendation Memo

### Recommendation: GO WITH CONDITIONS

**To:** National Recruitment Company
**Subject:** GDPR assessment — AI CV Screening and Ranking

**Bottom line: Go with conditions.** The system should not enter production until its lawful bases, DPIA, Article 22 position, data-retention rules, vendor arrangements, and international-transfer position have been documented and verified.

The proposed system analyses CVs, application answers and professional information to rank candidates and generate recommended shortlists. Because the rankings may materially influence access to employment opportunities, the company needs controls that address both GDPR compliance and the risks created by profiling and AI-supported recruitment.

**Top three actions before go-live:**

1. **Establish the lawful basis and complete the DPIA.** Document the Article 6 basis for each purpose, including the three-step legitimate-interests test if that basis is considered. Complete the DPIA and document the Article 22 assessment, including whether recruiter intervention is genuinely meaningful.
2. **Implement candidate-data governance.** Define retention periods for current recruitment and future-campaign reuse, document purpose compatibility, update transparency information, establish deletion rules, and determine how candidates can exercise applicable access, erasure and objection rights.
3. **Complete vendor and transfer controls.** Identify every vendor processing candidate data, confirm controller/processor roles, put Article 28 DPAs in place where required, and verify processing locations and any Chapter V transfer mechanism before non-EU/EEA transfers occur.

**Residual risks:** Even after these controls are implemented, residual risks remain. The ranking model may produce inaccurate or biased results, historical assessment data may become unsuitable for a different vacancy, and candidates may challenge profiling or decisions influenced by the system. Special-category information may also be present or inferred from candidate material despite controls designed to minimise its use.

**Recommendation:** Proceed only as a **conditional go-live**. The organisation should verify the required GDPR controls before production deployment and periodically reassess the system as its use, vendors, vacancies, or data sources change.

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
