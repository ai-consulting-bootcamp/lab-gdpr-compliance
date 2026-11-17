# GDPR Audit Pack — Warehouse Workforce Planning

**Scenario carried forward from lab lab-eu-ai-act-compliance:** Phase 1, Case 2 — regional grocery distribution workforce planning.  
**Client brief:** We run a regional grocery distribution network with several warehouses, and daily workload changes more than our rota can absorb.

An operations-planning tool would recommend which employees work each shift and which warehouse stations they cover.

It would use individual attendance, task-completion times, error rates, certifications, stated availability and past shift assignments.

Supervisors could override the recommendations, but a per-worker reliability and productivity score would also appear on managers’ monthly dashboards.

Managers say they use the dashboard to identify coaching needs and decide who gets offered preferred shifts.

Workers have asked how the scores affect their hours, but the operations team says this is only workforce planning.

**AI Act tier:** High-risk, provisionally under Annex III, point 4(b), because the system allocates shifts/stations using individual work behaviour and evaluates employee performance. The employer remains responsible for its deployer obligations; the vendor may be the AI Act provider. Annex III obligations are scheduled to apply from 2 December 2027 under the current timeline. [AI Act source](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

## Phase 1 — Shared fact pattern

> **Working fact pattern (assumptions and gaps are labelled):**
>
> **Client:** A regional grocery distribution network operating several warehouses; workforce size and countries of operation are **TBD**.  
> **Geography:** For this audit, assume affected workers are in the EU/EEA; confirm the member states and any non-EEA workforce.  
> **Personal data:** The tool uses employee attendance, task-completion times, error rates, certifications, stated availability and past shift assignments, then produces per-worker reliability/productivity scores and recommendations.  
> **Purpose:** It recommends which employees work each shift and warehouse station; managers also use scores to identify coaching needs and decide who receives preferred shifts. The effect on hours, pay and other working conditions is **TBD**.  
> **Human involvement:** Supervisors can override recommendations, but whether review is substantive, independent and documented is **TBD**.  
> **Vendor:** Assume a third-party supplier hosts or updates the tool for this audit; vendor identity, GDPR role, sub-processors, hosting and support-access locations are **TBD**.  
> **Automated decisions:** No final decision is stated to be fully automated. Confirm whether managers genuinely review each recommendation or routinely rely on the score.

## Phase 2 — Mini GDPR audit worksheet

### A. Data map

| Field | Audit finding / required follow-up |
|---|---|
| Categories of personal data | Employee identifiers and role/location (assumed); attendance, availability, certifications, shift history, task-completion times and error rates; derived reliability/productivity scores, shift/station recommendations, decisions and override logs. Do not add health, disability or other Article 9 data unless the client confirms it is collected or inferred. |
| Sources | HR/employee roster; time-and-attendance system; warehouse management/task records; certification/training records; employee availability or preference submissions. Verify source systems, accuracy and notice at collection. |
| Purpose(s) | (1) Operational shift/station allocation. (2) Separate employee evaluation, coaching and preferred-shift decisions using per-worker scores. Do not treat these purposes as interchangeable; specify each in the record of processing and notices. |
| Lawful basis per purpose | **(1) TBD — legal review.** Article 6(1)(f) legitimate interests may be considered for operational staffing only after documenting the purpose, necessity and balancing tests (LIA); ordinary workforce planning is not automatically necessary to perform the employment contract. **(2) TBD — legal review.** A separate Article 6(1)(f) analysis is needed for performance scoring and preferred-shift decisions; the impact on workers makes the balancing test harder. Do not rely on employee consent without assessing whether it is genuinely freely given. |
| Retention per purpose | **TBD — set before launch.** Define separate, justified periods for raw operational records, scores and decision/override logs; keep each only as long as needed for the stated purpose and applicable employment/payroll obligations, then delete or anonymise. The scenario supplies no periods. |
| Recipients and sub-processors | Employer’s operations supervisors and HR/managers on a need-to-know basis; vendor if it processes the data; vendor hosting, analytics or support sub-processors **TBD**. Confirm any onward sharing and restrict dashboard access. |
| International transfers and mechanism | **TBD — map before data flow.** Identify storage, backups, remote support access and every sub-processor location. If personal data is transferred outside the EEA, document the applicable adequacy decision or Article 46 safeguard (for example, SCCs), and assess any supplementary measures required. |

### B. Risk and data-subject rights

**Special-category data (Article 9).** None is specified. Attendance and productivity scores are personal data, but are not automatically Article 9 data. Check whether error/attendance patterns are used to infer health, disability, union activity or another protected attribute; if so, stop that use pending a valid Article 9 condition and legal review.

**Automated decisions (Article 22).** The brief says supervisors can override, so Article 22 is not established on the current facts. However, a nominal override is insufficient if supervisors simply rubber-stamp scores. Preferred shifts may significantly affect workers depending on their effect on hours, pay or working conditions. Require a meaningful review by a trained manager with authority, relevant evidence, time to assess, and documented reasons. If a decision is in fact solely automated and similarly significant, do not deploy it unless an Article 22(2) exception genuinely applies. Then implement the safeguards applicable to that exception, including human intervention, an opportunity to express a view, and a way to contest where required.

**DPIA — treat as required before the pilot.** The processing is likely to create high risk because the system evaluates employees, monitors work patterns, combines several datasets, uses AI for work allocation, and affects workers who may have limited ability to refuse employer monitoring. Complete the DPIA before processing; consult the DPO and workers or their representatives as appropriate. The EDPB’s nine-criteria screen is:

| EDPB criterion | Assessment for this scenario |
|---|---|
| Evaluation or scoring | **Applies:** individual reliability/productivity scores and coaching flags. |
| Automated decisions with legal or similarly significant effects | **Possible:** preferred shifts and hours may have significant effects; confirm actual impact and whether human review is meaningful. |
| Systematic monitoring | **Likely applies:** ongoing use of attendance, task times and error rates to monitor workforce performance. Confirm frequency and coverage. |
| Sensitive data or data of a highly personal nature | **Unclear:** no Article 9 data stated; worker performance data is sensitive in context. Check inferred health/disability data. |
| Large-scale processing | **Unknown:** several warehouses are in scope, but workforce size and duration are not provided. |
| Matching or combining datasets | **Applies:** attendance, task, error, certification, availability and past-shift data are combined. |
| Vulnerable data subjects | **Applies in context:** workers are in a power-imbalanced employment relationship and may have limited ability to refuse. |
| Innovative technology or organisational solution | **Likely applies:** AI-based scoring and allocation introduce a new form of workplace evaluation; document what is novel in this deployment. |
| Processing prevents exercising a right or using a service/contract | **Not established:** the brief does not say workers are blocked from shifts or rights. Confirm that contesting a score does not disadvantage them. |

The DPIA must describe the processing, assess necessity and proportionality, identify risks and document safeguards. If high residual risk remains after mitigation, consult the supervisory authority before processing.

**Likely data-subject friction points.** Workers may request access to input data, scores, sources and decision records; correction of inaccurate records; restriction or objection if legitimate interests is used; and erasure where applicable (subject to legal exceptions). Give clear notices explaining purposes, data sources, retention, recipients, score use, meaningful human review and how to challenge an outcome. Provide a practical route to correct source data and contest assignments.

**Controller / processor split.** The grocery operator is the likely GDPR controller because it chooses the workforce-planning purpose and how outputs affect workers. The vendor is a processor if it acts only on documented instructions; if it determines its own purposes or essential means, assess independent or joint-controller status. These GDPR roles are separate from the AI Act provider/deployer roles.

**DPA.** A GDPR Article 28 data-processing agreement is needed if the vendor acts as processor. It should cover documented instructions, confidentiality, security, assistance with rights/DPIA/breaches, sub-processor approval, audit information, and return/deletion at end of service.

### C. Law stacking

- **AI Act:** Likely high-risk under Annex III 4(b), covering task allocation based on individual behaviour/personal traits and worker monitoring/evaluation. Human oversight, data quality, logging, instructions and monitoring are relevant AI Act controls; confirm the precise provider/deployer allocation. Current application date for Annex III obligations: **2 December 2027**.
- **ePrivacy:** No cookies, tracking pixels or device-level access are described; likely not applicable on these facts. Recheck if worker devices, apps or connected equipment are monitored.
- **Data Act:** Likely not applicable to the stated staff-planning workflow. Recheck if the solution uses data from connected warehouse products or connected equipment, or raises cloud-switching issues.

## Phase 3 — Client recommendation memo

**To: Operations Director and Data Protection Officer**  
**Subject: Conditions for the warehouse workforce-planning pilot**

**Recommendation: Go with conditions; do not begin employee-level scoring or use scores to allocate preferred shifts until the conditions below are met.** The tool processes identifiable worker data to rank performance and influence work allocation. This creates material privacy and employment risks even when a manager is expected to make the final decision.

First, **complete a DPIA and confirm the lawful basis for each purpose** before the pilot. Separate operational scheduling from employee evaluation and preferred-shift decisions. For any proposed legitimate-interest basis, document the purpose, necessity and balancing assessment; do not assume employment-contract necessity or rely on employee consent without legal review. Assess Article 22 against the real workflow and actual effects on workers’ hours, pay and conditions. Human review must be substantive, not a signature after the model has effectively decided.

Second, **map the data and vendor chain**. Confirm workforce geography, data fields and sources, retention periods, hosting/support locations and all sub-processors. Execute an Article 28 DPA if the vendor is a processor, and put a valid transfer mechanism and any required supplementary measures in place before non-EEA access or transfer.

Third, **put safeguards and worker transparency in place before testing**: limit features to job-relevant data, validate score accuracy across sites and worker groups, restrict dashboard access, log recommendations and overrides, give workers a clear notice and correction/contest channel, and train managers to review underlying evidence independently. Keep the pilot small and time-limited, with success and stop criteria defined in advance.

Residual risks remain: operational data may be incomplete or systematically disadvantage some workers; managers may defer to scores despite formal override rights; and the system’s purpose or vendor chain may expand after launch. Monitor these risks, review the DPIA when the system changes, and pause use if scores cannot be explained, corrected or meaningfully challenged.

## Sources

- [GDPR — Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [EDPB — DPIA criteria and guidance](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en)
- [EU AI Act — consolidated text as at 27 July 2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)
- [European Commission — AI Act framework and application timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
