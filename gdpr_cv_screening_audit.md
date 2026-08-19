# GDPR Audit Pack — CV Screening and Ranking

**Scenario:** Case 2 — CV Screening and Ranking (Recruitment)  
**Client:** National recruitment company  
**Auditors:** [Your Name] and [Teammate Name]  
**Date:** 19 August 2026

---

# Part I — Audit Worksheet

## Phase 1 — Fact Pattern
### Fact Pattern

A national recruitment company wants to reduce the time recruiters spend screening applications for large-volume vacancies. The company proposes an AI system that analyses candidate CVs, application answers, and relevant professional information, then ranks candidates against the requirements of each vacancy. Recruiters receive a recommended shortlist together with an explanation of the factors that influenced each candidate's ranking. A recruiter reviews the shortlist before candidates are invited to interviews and has authority to reject or add candidates. The recruitment company intends to use the system across several recruitment offices and retain assessment results for future hiring campaigns. The scenario does not specify the volume of candidate data, the exact categories of professional information processed, the geographic location of candidates, the retention period, or whether any special-category data may be present in the source material. The architecture may also include a licensed CV-parsing or NLP component supplied by a third-party vendor.

## CFU 1 — Recognize

### Personal data categories

The system processes personal data contained in:

- CVs
- Application answers
- Professional information
- Candidate ranking results
- Factors contributing to the ranking
- Recommended shortlist status
- Recruiter decisions to reject or add candidates
- Assessment results retained for future campaigns

These data are linked to identifiable job applicants and therefore fall within the scope of GDPR personal-data processing.

### Special-category data — Article 9

The scenario does not state that special-category personal data is intentionally processed.

However, CVs and application answers may potentially contain information revealing characteristics such as health information, disability, racial or ethnic origin, religious beliefs, trade-union membership, or other Article 9 categories.

The system should therefore not assume that Article 9 data is absent merely because it is not an explicit input field.

**Assessment: TBD — privacy/legal review required to determine whether special-category data is collected, inferred, or used in the ranking process.**

### Data subjects

The primary data subjects are job applicants and candidates.

The system therefore processes personal data in the context of recruitment and employment-related decision-making.

### Geographic scope

The scenario describes a national recruitment company and several recruitment offices, but does not specify the country or countries involved.

**Assessment: TBD — confirm the relevant EU/EEA jurisdictions and whether any candidates are located outside the EU/EEA.**

### Automated decision-making

The system automatically analyses candidate information and ranks candidates against vacancy requirements.

However, the scenario states that a recruiter reviews the recommended shortlist before candidates are invited to interviews and that recruiters can reject or add candidates themselves.

The available facts therefore do not establish that the AI system makes the final recruitment decision by itself.

Nevertheless, the system materially influences the recruitment process because its ranking determines the recommended shortlist presented to recruiters.

The applicability of GDPR Article 22 should therefore be assessed carefully, including whether any recruitment decision produces legal or similarly significant effects on candidates and whether the human review is genuinely meaningful rather than merely formal.

**Assessment: TBD — legal/privacy review required before deployment.**

### Future campaign reuse

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