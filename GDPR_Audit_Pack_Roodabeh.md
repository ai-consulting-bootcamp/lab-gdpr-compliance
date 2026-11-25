# GDPR Audit Pack - Roodabeh

## Audit worksheet

### Transition note

This audit carries forward the Interview Prep Agent (Project 3) from the Week 7 Day 1 EU AI Act exercise. The first-pass classification recorded for the project was limited risk with transparency obligations. This case is relevant to GDPR because it processes CV and professional-profile data to generate personalised interview-preparation reports.

### Fact pattern

For this audit, the client is a one-person career-technology prototype project operated in Germany; it is at prototype stage, with one project operator and no recorded production-scale user base. Its intended users and data subjects are job seekers in the German recruitment market. A user provides a CV with direct identifiers removed, a job advertisement, and optionally a public GitHub or LinkedIn profile. The data may include work history, education, skills, projects, profile details, and personal information appearing in a job advertisement. The workflow uses n8n and an AI model to prepare company information, relevant CV evidence, skill gaps, interview questions, draft STAR answers, and suggestions for similar companies. It checks generated claims against the supplied sources and removes unsupported claims. The report is returned to the job seeker; the system does not rank, shortlist, accept, or reject candidates for employers. OpenAI and connected services such as Notion, search, or email may process data; their exact roles, processing locations, retention periods, and transfer safeguards are not yet confirmed.

### Section A — Data map

| Field | Your answer |
|---|---|
| Categories of personal data | Professional history, education, skills, projects, and profile information from the CV or public profile. Direct identifiers are intended to be removed from the CV before processing. Job advertisements may contain recruiters’ names or contact details. Generated reports and workflow logs may also contain personal data. |
| Sources | CV and optional GitHub or LinkedIn profile supplied by the job seeker; job advertisement and company information from public sources or links supplied by the user. |
| Purpose 1 | Generate and validate a personalised interview-preparation report using the user’s CV/profile and job advertisement. |
| Lawful basis for Purpose 1 | **TBD — legal review.** Contract may be appropriate if the operator provides a service requested by the user and this processing is necessary to deliver it; confirm the service arrangement and controller role first. |
| Retention for Purpose 1 | **TBD — legal review.** No confirmed retention period is recorded. Define when the source CV, profile data, and report are deleted. |
| Purpose 2 | Keep technical or quality logs to operate, troubleshoot, and secure the workflow. The exact fields stored in Notion or other logs are not confirmed. |
| Lawful basis for Purpose 2 | **TBD — legal review.** If legitimate interests are proposed, document the purpose, necessity, and balancing test. Do not retain CV or report content in logs by default. |
| Retention for Purpose 2 | **TBD — legal review.** Define a separate retention period for logs and confirm whether deletion is automated. |
| Recipients and sub-processors | The job seeker receives the report. The project operator and the services actually used in the workflow may access or process data. OpenAI, n8n hosting, Notion, and any search or email service must each be checked to establish their role and any sub-processors. |
| International transfers and transfer mechanism | A non-EEA transfer is possible because external AI and workflow vendors are used, but the contracting entities and processing locations are unconfirmed. **TBD — legal review:** identify each location and document any required adequacy decision or Standard Contractual Clauses and related safeguards. |

### Section B — Risk and rights

- **Special-category data:** The tool does not intentionally request special-category data. A CV could nevertheless include sensitive information, such as health or disability information. Users should be told not to include unnecessary sensitive data; any such processing requires separate legal review.
- **Automated decision-making:** Based on the current design, the tool gives preparation advice to the job seeker and does not make hiring decisions or determine access to employment. Article 22 therefore does not appear to apply on these facts. Reassess if an employer uses the report to rank or select candidates.
- **DPIA:** Complete a DPIA screening before wider use. Evaluation of professional information and use of AI are relevant risk criteria; combining a CV with a public profile may add another. A full DPIA is recommended before production use if these criteria and the processing context indicate likely high risk. The final requirement depends on the actual scale, data flows, and applicable supervisory-authority list.
- **Data-subject rights and friction points:** Users may need to access, correct, or erase their CV and report, including copies in logs or vendor systems. The right to object may be relevant if profiling is based on legitimate interests. The current deletion and rights-request workflow is **TBD**.
- **Controller / processor roles:** For this audit, assume the project operator determines the service’s purposes and means and is the controller. Job seekers are data subjects. OpenAI, n8n hosting, Notion, and any search or email vendor may be processors if they process data on the operator’s documented instructions; confirm each role from the actual service terms and data flow.
- **DPA needed with which vendors:** A DPA is needed with each vendor acting as a processor. Confirm the agreements and sub-processor lists for OpenAI, n8n hosting, Notion, and any search or email provider before processing real users’ data.

### Section C — Law stacking

- **AI Act:** The Week 7 Day 1 first-pass classification was limited risk with transparency obligations. On the current facts, the tool supports the applicant and is not intended to recruit or select candidates for an employer, so it does not appear to be an Annex III recruitment or selection system. Confirm the applicable transparency duties for AI-generated content and the provider/deployer roles.
- **ePrivacy:** The current scenario does not involve cookies, tracking pixels, or device-level tracking. ePrivacy is not applicable on the stated facts. Reassess if analytics or tracking technologies are added.
- **Data Act:** Not applicable on the current facts. The tool does not involve connected products, IoT data, or cloud-switching data.

## Client recommendation memo

**Bottom line: Go with conditions.** The applicant-facing prototype supports interview preparation and is not intended to select or reject candidates. However, it processes identifiable professional information through external AI and workflow services. Do not use real users’ CVs beyond controlled testing until the data flows, lawful bases, vendor terms, and retention are documented.

1. **Map and minimise data before the next test.** Record each field sent through n8n to OpenAI, Notion, and any search or email service. Keep direct identifiers removed. Prevent CV and report content from being written to logs by default. Confirm each vendor’s role, sub-processors, DPA, processing location, and transfer mechanism. Define deletion periods for source CVs, reports, and logs.

2. **Complete a DPIA screening and legal-basis review before external use.** The tool evaluates professional information and uses AI; combining a CV with GitHub or LinkedIn data may increase risk. Document the Article 6 basis for report generation and logging separately. Confirm whether a full DPIA is required and ensure the privacy notice describes all purposes and vendors.

3. **Build rights and quality controls into the workflow.** Give users a clear way to access, correct, and delete their CV and report, including copies in logs. Explain that the report is AI-generated and ask users to verify company information and draft STAR answers. Keep the tool limited to preparation support; do not use its output to rank or select applicants without a new legal and AI Act assessment.

Residual risks remain. A redacted CV may still identify someone through a distinctive work history or linked profile. Generated advice may be inaccurate or biased and could influence career choices despite source checks. External providers also create security, retention, and possible cross-border-transfer risks that the project operator cannot eliminate entirely.

This memo is a first-pass consulting assessment, not a legal opinion, completed DPIA, or compliance certification. Obtain qualified legal review of the lawful basis, vendor contracts, transfer safeguards, and national requirements before launch.

## Partner review

Complete this section after exchanging the memo with your partner.

| Criterion | Score 1–3 | Comment |
|---|---:|---|
| Clear bottom-line recommendation |  |  |
| Lawful basis selection is justified |  |  |
| Top actions are specific and sequenced |  |  |
| Residual risks are named honestly |  |  |
| Law stacking is addressed |  |  |

**Client response:** [After the review, write 2–3 sentences accepting the recommendation, raising one concern, or asking for one section to be reconsidered.]