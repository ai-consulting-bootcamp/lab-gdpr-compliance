# GDPR Audit Pack - Sean Langsdorf

**Client** Northline Staffing GmbH (fictional) · **Scope** German recruitment pilot · **Date** 17 November 2026

**Transition from the EU AI Act lab.** This audit carries forward Client Brief 2, the nationwide staffing agency that wants AI to parse applications, rank candidates by vacancy and recommend who gets contacted. It is high-risk employment AI under Article 6(2) and Annex III, point 4(a). It is a useful GDPR case because even an advisory score can determine who actually gets considered when shifts fill quickly. The audit distinguishes the proposal as described from the controls recommended below.

## Audit worksheet

### Fact pattern

Northline is a medium-sized staffing agency that hires workers for short-notice warehouse and care-support shifts throughout Germany.\
The agency receives CVs and application forms from adult job applicants in Germany and expects about 25,000 applications a year.\
Applications include names and contact details, employment history, qualifications, availability and free text, which may incidentally disclose health or other sensitive information.\
For this lab, assume Northline stores original applications in its EU-hosted applicant tracking system and sends a vacancy-specific feature set to RankWorks EU GmbH, the fictional vendor operating the ranking service.\
RankWorks returns a score, feature-level reasons and a suggested shortlist. The service is EU-hosted, but a separate US support affiliate could access production records unless that route is disabled.\
Recruiters can confirm or override the shortlist. In short-notice hiring, candidates below the visible cutoff may never be considered before the shift fills, effectively excluding them without individual review.

*Lab assumptions* The names, volume, German geography and vendor arrangements are working assumptions, not verified client facts. Northline makes the hiring decision. Host businesses provide vacancy criteria and do not receive CVs, scores or shortlists in this pilot.

### Section A — Data map

Proposed retention periods are working limits to validate with German employment counsel. They are not statutory defaults. HR records after hiring and any separate candidate pool are out of scope.

| Purpose | Data and sources | Proposed Article 6 basis and rationale | Proposed retention | Recipients |
| --- | --- | --- | --- | --- |
| Receive and assess an application for a named vacancy | Applicant-supplied name, contact details, CV, job qualifications and availability. Employer supplies vacancy requirements. | **Contract, Art. 6(1)(b)** for steps the applicant requests before entering an employment contract with Northline, limited to information objectively needed to assess and contact them. Legal to confirm the German employment-data position, including § 26 BDSG, before launch. | Keep through the decision. Then delete or move only what is needed to the restricted claims record below. Transfer only necessary details for successful candidates to a separate HR record. | Northline recruiting team and its EU applicant tracking system processor, IntakeHub GmbH (fictional). |
| Rank applications for the specific vacancy and support recruiter review | Minimized qualifications, relevant experience bands and availability extracted inside Northline's controlled intake environment. Input uses a vacancy-linked token. Output adds score, reasons and model version. No raw CV, name, contact details or accommodation data sent to RankWorks. | **TBD — legal review.** Candidate basis is legitimate interests, Art. 6(1)(f), for timely selection. A backlog establishes an interest, not necessity. Pass the purpose, necessity and balancing tests before using live data. Do not extend the contract basis to profiling by default. | Delete vendor input and ranking cache within 24 hours after review and in all cases within 7 days of creation. Delete operational scores once the vacancy closes, except for any limited, justified claims record. | Authorized Northline recruiters and RankWorks EU GmbH. US support is technically blocked as a launch condition. |
| Preserve a narrow record to handle selection disputes | Vacancy criteria, model version, material inputs and outputs actually relied on, human decision and reason. Source is the recruitment decision record. | **Legitimate interests, Art. 6(1)(f)** subject to a separate LIA. A narrow record lets Northline investigate or defend a documented claim without keeping full applications on file. Validate German claims timelines, including § 15(4) AGG, and justify what is kept. | Proposed maximum of 6 months after the rejection or closure notice, subject to local legal confirmation. Isolate a case-specific legal hold only where necessary and delete after it ends. | Restricted Northline legal/privacy staff and contracted EEA storage. Outside counsel only as needed, with its role assessed separately. |
| Respond to statutory access, correction, erasure and objection requests | Candidate request, minimum verification information, affected records and response history. Sources are the applicant and Northline's systems. | **Legal obligation, Art. 6(1)(c)** in conjunction with Arts. 12–22. The request record is necessary to respond and document compliance. | Proposed 12 months after closure for a minimal case log, subject to review. Delete verification documents as soon as identity is confirmed unless retaining them is necessary. | Northline privacy team, relevant recruiters and processors solely as needed to locate, correct, erase or restrict data. |

**LIA for ranking.** (1) Purpose: reduce delays without excluding qualified applicants. (2) Necessity: compare structured manual review and rules-based verification on accuracy, workload and speed. If either meets the need with less intrusion, do not deploy ranking. (3) Balancing: applicants may expect job-fit assessment, not a score they cannot see or contest. Account for time pressure, unequal bargaining power, bias and lost work. Limit fields, show the entire queue, offer a manual route and document the test outcome and remaining risks. Reject the basis if the balance does not support it.

**International transfers.** In the proposal, remote access by RankWorks US Inc., a separate US support affiliate, would be an EU-to-US disclosure even with EU hosting. No transfer mechanism is established. Block access by default and verify staff access, telemetry, backups and the full subprocessor chain. If Northline later approves US support, RankWorks must verify active EU–US Data Privacy Framework coverage for the importer and processing (Art. 45), or use the applicable SCCs (normally processor-to-processor Module 3 for this chain), a transfer impact assessment and effective supplementary safeguards (Art. 46). Also obtain Northline's Art. 28 authorization. Keep access blocked if those conditions cannot be met.

**Purpose limits.** Do not reuse applicant data for product training, cross-vacancy candidate pools, marketing or vendor benchmarking. Any new purpose requires its own assessment, including Art. 6(4) where applicable, and appropriate notice before reuse. Route accommodation information separately with tightly restricted access and a verified Art. 6 basis and Art. 9 condition before processing it.

### Section B — Risk and rights

**1. Special-category data (Art. 9).** Free text may disclose disability, health, religion or trade union membership, and explanations could reproduce or infer protected facts if free text or proxies enter ranking. Block raw text and unjustified proxies from the ranker, prohibit protected inferences and do not assume that a general Art. 6 basis also permits Art. 9 processing.

**2. Automated decisions (Art. 22).** Losing a realistic chance of paid work can be similarly significant, and an override button does not prevent a decision from being solely automated in practice if staff rubber-stamp the score or never see low-ranked applicants. Block that workflow absent a verified Art. 22(2) exception and its safeguards, including at least human intervention, the opportunity to express a view and a way to contest for exceptions under (a) or (c), and check Art. 22(4) if special-category data are used. For this pilot, require empowered recruiters to check all eligible applicants before the decision, see job-relevant evidence and record independent reasons, or use manual selection if timely review is not possible.

**3. DPIA (Art. 35).** Required before using live applicant data because the repeated profiling informs significant shortlisting decisions and creates a likely high risk even with genuine review. Article 35(3)(a) is relevant, and the WP248 screen below supports a DPIA without relying on an exact volume threshold. Consult the supervisory authority before processing if high residual risk cannot be mitigated (Art. 36).

| Criterion | Assessment |
| --- | --- |
| Evaluation or scoring | **Yes.** Vacancy-specific candidate suitability is scored. |
| Automated decision with legal or similarly significant effect | **Credible in proposal.** An unseen candidate can be excluded in practice. Not intended in the redesigned workflow, which must be tested. |
| Systematic monitoring | **No on assumed scope.** No ongoing tracking or worker surveillance. |
| Sensitive or highly personal data | **Potential.** Raw CVs can contain Art. 9 disclosures. Verify they cannot enter ranking or its logs. |
| Large scale | **Likely.** Recurring nationwide processing of an estimated 25,000 applications per year. Confirm unique subjects, duration and data breadth. |
| Matching or combining datasets | **No on assumed scope.** One applicant submission is compared with job criteria, without unrelated datasets or third-party enrichment. |
| Vulnerable data subjects | **Yes.** Job seekers have less bargaining power and may depend on rapid access to shifts. |
| Innovative use or new solutions | **Likely.** AI-assisted parsing and profiling are newly deployed for this client. Verify the technology and use rather than assuming every AI tool qualifies. |
| Blocks a right, service or contract | **Potential in proposal.** A hidden ranking cutoff can gate access to a job contract. Remove it and require full-queue review. |

**4. Rights friction.** Access must cover profiles, scores and relevant decision records across both systems, and correction must reach parsing errors and trigger a rerun or manual reassessment where appropriate. Propagate valid erasures to the vendor, manage backups and justified holds, and give candidates an easy Art. 21 route to object to legitimate-interest profiling, which must stop unless the controller demonstrates applicable grounds to continue. Explain ranking and the manual review route upfront, include the additional notice information where Art. 22 applies, and respond to rights requests within Art. 12's one-month deadline unless a permitted extension applies.

**5. Roles.** Northline is the controller because it chooses the hiring purposes and essential means. IntakeHub is its intake processor and RankWorks EU its ranking processor on documented instructions. RankWorks US would be a subprocessor if approved for production access. A vendor that determines its own product-training purpose would be a controller for that processing, not covered by this audit.

**6. DPAs.** Sign Art. 28 agreements with IntakeHub and RankWorks EU before they handle live data. Require authorized subprocessors and equivalent downstream duties, including incident notice without undue delay, rights assistance, deletion, access controls and audit evidence. No direct Northline–RankWorks US DPA is assumed for a properly authorized subprocessor relationship.

### Section C — Law stacking

- **AI Act.** High-risk under Art. 6(2) and Annex III 4(a). Profiling prevents reliance on the Art. 6(3) carve-out. Provider conformity assessment and deployer monitoring under Arts. 43 and 26 add duties beyond GDPR. The amended Annex III application date is 2 December 2027, subject to applicable transitional rules. GDPR already applies.
- **ePrivacy.** No tracking pixels, analytics cookies or device-level scoring are assumed. A strictly necessary session cookie may qualify for exemption. Non-exempt storage or access on terminal equipment requires prior consent under Art. 5(3) as implemented in Germany by § 25 TDDDG, regardless of any GDPR basis for subsequent processing.
- **Data Act.** No connected-product data. Check whether hosted ATS or ranking services qualify as data processing services under Chapter VI and, if so, confirm switching and export terms. This does not provide a legal basis for applicant profiling.

## Client recommendation memo

**To Northline Staffing's Legal and Operations leads**

**Go with conditions.** Keep the current shortlist design off live applications because a low score can cost someone a shift before a recruiter ever opens their file. Use synthetic records until the three gates below are met. If they cannot be met without slowing short-notice hiring beyond what your team can handle, keep selection manual.

1. **Settle necessity and legal basis first.** Ask Legal and Operations to compare ranking with a manual queue and a simpler qualifications check. Use synthetic cases and compare recruiter handling time, missed qualified applicants and whether candidates are still reviewed before a shift fills. Document the legitimate interests assessment and the German employment-law analysis. If a less intrusive method does the job, use it instead. Do not treat the applicant's request to be considered as permission to profile them.
2. **Close the vendor and data gaps.** Before any live data flows, sign processing agreements with IntakeHub and RankWorks EU. Limit ranking inputs to vacancy-specific qualifications, experience and availability. Keep names, raw CVs and accommodation disclosures out of the ranking service. Get written confirmation of all subprocessors and test that US production access, including through diagnostic logs, is disabled. Prohibit training reuse and test deletion across both systems.
3. **Make human review work under real shift deadlines.** Complete the DPIA with your privacy team, publish the applicant notice, and test access, correction, erasure and objections end to end. Give recruiters time and authority to review every eligible candidate before closing the shortlist. Record an independent reason for each decision and switch to a manual workflow if the queue cannot be reviewed in time. If high residual risk remains, consult the supervisory authority before any live pilot.

Three risks remain. Job-related signals can still act as proxies for disadvantage. A parser can miss an unusual qualification even if it extracts most fields correctly. And a reviewer under time pressure may still defer to the score. Have Operations check missed qualifications, patterns of overrides and whether low-ranked applications actually get read. Pause the pilot if qualified people are repeatedly overlooked or shifts close before the full queue is reviewed. An override button alone does not protect applicants.

### Primary sources

- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679) (Arts. 5–6, 9, 12–22, 25, 28, 33–36 and 44–46).
- [EDPB-endorsed WP29 guidance](https://www.edpb.europa.eu/endorsed-wp29-guidelines_en) (WP248 rev.01 on DPIAs and WP251 rev.01 on automated decisions) and [CJEU, SCHUFA, C-634/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62021CJ0634) (decisive reliance on a score in a credit case, relevant by analogy).
- [EDPB Guidelines 05/2021 on transfers](https://www.edpb.europa.eu/system/files/documents/2023-02/edpb_guidelines_05-2021_interplay_between_the_application_of_art3-chapter_v_of_the_gdpr_v2_en_0.pdf), [EU–US adequacy decision](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) and [EU standard contractual clauses](https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj).
- [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html), [§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html) and [§ 25 TDDDG](https://www.gesetze-im-internet.de/tdddg/__25.html).
- [EU AI Act, Regulation (EU) 2024/1689 as consolidated](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), [Digital Omnibus on AI, Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) and [Commission implementation timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).
- [ePrivacy Directive, Art. 5(3) as amended](https://eur-lex.europa.eu/eli/dir/2009/136/oj) and [EU Data Act, Chapter VI](https://eur-lex.europa.eu/eli/reg/2023/2854/oj).
