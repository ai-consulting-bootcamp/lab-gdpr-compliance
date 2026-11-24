# GDPR Audit Pack — HR Tech Startup Perspective

**CV screening with human review** — an HR tech startup sells a tool that ranks job applicants using structured and unstructured resume data, with a recruiter confirming or overriding the shortlist.

## Phase 1 — Shared fact pattern

> **Working fact pattern (assumptions and gaps are labelled):**
>
> - **Startup under audit:** An HR tech startup sells an AI-assisted CV-screening tool; its ownership, size, establishment, and hosting locations are TBD.
> - **Customer/controller/deployer:** A privately held logistics company with approximately 150,000 employees operates worldwide and hires in Europe. Assume about 20 role profiles across departments in a typical hiring cycle; this is an estimate. The employer determines hiring purposes and criteria and makes advancement decisions.
> - **Applicants and geography:** Applicants may be located anywhere in the world and apply for European positions. The relevant employer entities and hiring countries are TBD.
> - **Personal data:** The employer sends applicant contact details, education, employment history, skills, and structured and unstructured resume content. The tool generates rankings or shortlist recommendations; resumes may disclose sensitive details.
> - **Purpose and human involvement:** The startup processes the data to provide role-specific rankings to its customer. A recruiter or HR manager reviews, confirms, rejects, or overrides the recommendation and decides which applicants proceed.
> - **Roles:** Assume the employer is controller/deployer and the startup is its processor for applicant data, acting on documented instructions. The startup may be a separate controller for its own account, billing, or security data; verify each purpose and role.
> - **Vendor and decisions:** OpenAI was suggested but is not selected; model provider, sub-processors, and data locations are TBD. No final decision is described as fully automated, but confirm review is meaningful and no applicants are rejected automatically.

## Phase 2 — Mini GDPR audit worksheet

### Section A — Data map

| Field | Working answer |
|---|---|
| **Categories of personal data** | Applicant identity and contact details; resume/application content; education, qualifications, work history, and skills; role applied for; and generated scores, rankings, or shortlist recommendations. Resumes may contain or reveal special-category data, which should not be used for ranking. |
| **Sources** | Applicants provide resumes and application details to the employer. The employer supplies role descriptions and criteria to the startup. The tool generates rankings from those inputs. No external applicant-data sources are stated. |
| **Purpose(s)** | **Customer purpose:** assess applicants for a specific role and support recruiter shortlisting. The startup provides this processing service on the customer’s instructions. Any startup use for account administration, security, product improvement, or model training is a separate purpose and is not confirmed. |
| **Lawful basis per purpose** | **Recruitment data:** the employer/controller must select and document its Article 6 basis; the startup, as processor, acts on instructions and does not choose the customer’s basis. **Startup’s own purposes:** **TBD — legal review**; define each purpose, data set, and basis separately. Do not use applicant data for model training or product improvement without separately establishing roles, lawful basis, transparency, and contractual permission. |
| **Retention period per purpose** | **Recruitment data:** follow customer instructions and contract; set deletion/return at the end of service and a defined backup-deletion schedule. **Startup’s own data:** set separate periods for necessary account, billing, and security records. Exact periods are **TBD — legal review**; do not retain applicant data indefinitely. |
| **Recipients and sub-processors** | The employer/customer receives rankings and shortlist recommendations; only authorized startup personnel should access applicant data for support. Hosting, support, and model vendors are TBD. OpenAI is not selected. Document and obtain required authorization for each sub-processor. |
| **International transfers and transfer mechanism** | Global applicants do not by themselves establish a Chapter V transfer. Confirm the startup and customer establishments, processing/access locations, and any non-EEA recipient. If GDPR-covered data is made available to a recipient outside the EEA, identify an adequacy decision or another valid transfer mechanism (often SCCs), complete a transfer impact assessment, and add safeguards as needed. No transfer route is confirmed. |

### Section B — Risk and rights

- **Special-category data (Article 9):** Resumes may disclose health, disability, ethnicity, religion, or other sensitive traits, but these are not needed for the stated ranking purpose. As processor and product provider, minimise inputs and design the service not to use or infer these traits; escalate any requested Article 9 processing for legal review.
- **Automated decision-making (Article 22):** The employer/controller assesses Article 22. Design the tool so recruiters can inspect relevant evidence and meaningfully confirm, reject, or override recommendations before a candidate is screened out. If the customer uses scores as automatic rejection decisions, it must assess Article 22 exceptions and safeguards, including human intervention and a way to express a view and contest the decision.
- **DPIA:** The customer/controller should lead a DPIA before launch; it is likely warranted because the tool scores applicants for employment, uses AI, and affects people in a potentially vulnerable position. The startup should provide the data-flow, model, sub-processor, security, and mitigation information the customer needs, and separately manage provider-side AI risks.
- **Data-subject friction:** Applicants may seek access to the data and ranking, correction of inaccurate CV information, erasure, or a challenge to an outcome. The employer responds as controller; the startup must support it under the DPA with search, correction, export, deletion, and explanation workflows.
- **Controller / processor split:** The employer is the controller/deployer for recruitment on the stated assumption; the startup is its processor if it acts only on documented instructions. The startup may be a separate controller for its own defined account/security purposes. Any model or hosting vendor is a sub-processor only if its actual role and contract support that classification.
- **Data Processing Agreements:** Sign an Article 28 DPA with each customer before processing, specifying instructions, security, rights assistance, deletion/return, audits, and sub-processor controls. Put appropriate processor terms and transfer safeguards in place with any sub-processor before sharing applicant data.

### Section C — Law stacking

- **AI Act:** The tool is likely high-risk under Annex III, point 4(a), because it analyses or filters job applications and evaluates candidates. If the startup places the system on the market under its name, it is likely the provider and should confirm applicable provider requirements, including risk management, data governance, technical documentation, logging, conformity assessment, and post-market monitoring. The employer remains responsible for deployer duties such as human oversight and use according to instructions.
- **ePrivacy:** No cookies, tracking pixels, or device-level data are described, so ePrivacy is not currently implicated. Reassess if application tracking or similar technologies are added.
- **Data Act:** No connected-product or cloud-switching data is described; this is currently not applicable.

## Phase 3 — Client recommendation memo

**To:** HR tech startup leadership

**Subject:** Conditions for offering AI-assisted CV screening

**Recommendation: Go with conditions.** The product can support recruiters, but it ranks applicants for employment and is likely a high-risk AI system. The startup’s processor role, sub-processor chain, transfer locations, and provider compliance are not yet confirmed. Do not process live applicant data or launch the tool for customer hiring until the following actions are complete.

**Top three actions**

1. **Set the roles and data terms before onboarding a customer.** Confirm that the employer determines recruitment purposes and lawful basis, while the startup processes applicant data only on documented instructions. Sign an Article 28 DPA, define retention and deletion, support applicant rights, and list all sub-processors. Confirm each vendor’s location and data use; prohibit model training on applicant data unless separately assessed, disclosed, and agreed. Put a valid transfer mechanism and transfer-impact safeguards in place where required.
2. **Complete provider compliance and customer DPIA support before the pilot.** Treat the tool as likely high-risk under the EU AI Act’s recruitment category. Build the required provider documentation and risk-management process, validate data quality and performance, plan conformity assessment and post-market monitoring, and give customers the information needed for their DPIAs and deployer duties.
3. **Build meaningful human review into the product before production.** Show recruiters relevant factors and limitations, allow them to independently reject or change rankings, prevent automatic candidate rejection, and keep appropriate logs. Test for accuracy and unfair outcomes across relevant groups, provide customer-facing instructions, and implement workflows to help customers answer access, correction, erasure, and challenge requests.

**Residual risks:** CVs can contain sensitive information, and rankings can reproduce bias or disadvantage applicants even after testing. Recruiters may over-rely on scores, so product safeguards and customer training require ongoing monitoring. Worldwide applicants, changing vendor access, and differences in national employment and privacy laws create residual compliance uncertainty; contracts, transfer safeguards, and audits can reduce but not eliminate it.