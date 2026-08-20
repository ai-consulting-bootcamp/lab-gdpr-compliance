# GDPR Audit Pack — Paola Hintze and Gretel

## Audit worksheet

### Transition note

This lab carries the Intellectus social-impact consulting product into a privacy review. The system is best treated as **non-high-risk AI with transparency and governance obligations in the agreed use case**, because it supports an organisational diagnostic and does not make decisions about employment, eligibility for essential services, or another Annex III outcome. The GDPR analysis is nevertheless material because production use introduces internal documents containing information about employees, volunteers, donors, and potentially vulnerable beneficiaries. If the purpose changes to ranking or deciding outcomes for individuals, the AI Act classification and this GDPR assessment must be reopened before use.

### Agreed fact pattern

River Learning Collective is a fictional medium-sized German non-profit with approximately 75 employees and contractors and 250 active volunteers, serving communities in Germany and other EEA countries. It uses Intellectus to prepare an organisational diagnostic before a consultant-led workshop. An authorised staff member enters the organisation name, website, country, current challenge, and a research period, and uploads selected internal documents such as volunteer-process notes, staff hand-off records, donor-contact summaries, and redacted beneficiary-service reports. Intellectus sends the intake through its web application to n8n Cloud, retrieves relevant public sources, and sends minimised excerpts to the OpenAI API for evidence extraction and diagnostic drafting. The output separates evidence, findings, hypotheses, unknowns, and proposed actions. An Intellectus consultant must meaningfully review, correct, or reject the output before it is shown to the client; the system must not rank people or make employment, funding, or service-access decisions. Data subjects are primarily in the EU/EEA. OpenAI Ireland is an external processor, with possible onward transfers outside the EEA under its DPA; n8n hosting location and subprocessors must be verified before launch.

### CFU 1 — Recognise

- **Ordinary personal data:** names, work contact details, job or volunteer roles, correspondence, application and interaction records, work-pattern observations, donor contacts, and opinions written in internal notes.
- **Potential Article 9 data:** beneficiary reports or free text may reveal or allow inference of health, disability, racial or ethnic origin, religion, political opinions, trade-union membership, or sexual orientation. These data are not necessary by default and must be excluded unless a specific Article 9 condition is documented.
- **Cross-border flow:** EEA data reaches OpenAI Ireland and may be accessed by approved affiliates or subprocessors outside the EEA. The n8n region and remote-support paths are currently unverified, so no production upload may begin until that transfer map is completed.

## Section A — Data map

| Purpose | Personal data and source | Lawful basis and justification | Proposed retention | Recipients / subprocessors | Transfer position |
| --- | --- | --- | --- | --- | --- |
| Create and administer the diagnostic engagement | Client contact name, work email, role, organisation, access and request metadata; supplied by the client | **Article 6(1)(b)** only where the individual is personally party to the contract; otherwise **Article 6(1)(f), legitimate interests**, because limited business-contact processing is necessary to deliver and administer the requested engagement. Record an LIA. | Active engagement plus 12 months, unless a documented legal hold or contract requires longer | River Learning Collective, Intellectus operator, n8n | EEA region preferred; verify n8n hosting, support access, and subprocessors |
| Produce the organisational diagnostic | Current-challenge text, internal document excerpts, staff/volunteer process records, donor contacts, and public professional information; supplied by client or retrieved from public sources | **Article 6(1)(f), legitimate interests**, subject to a purpose–necessity–balancing LIA. The purpose is improving organisational operations; only data demonstrably necessary for the diagnostic may be used. | Raw uploads and extracted working text: delete within 30 days after client acceptance; final reviewed report: 12 months, then delete or irreversibly anonymise | Intellectus consultants, n8n, OpenAI API | OpenAI Ireland DPA; verify onward-transfer basis and safeguards. Use SCCs/TIA where no adequacy decision applies |
| Process any special-category information found in documents | Health, disability, ethnicity, religion, politics, union membership, sexual orientation, or equivalent in free text; client documents | **TBD — legal review under Article 9.** An Article 6 basis alone is insufficient. Default control is to block, redact, or exclude this content. Consent must not be assumed, particularly for employees or vulnerable beneficiaries | Reject before upload where possible; detected content quarantined for immediate redaction and deletion; no inclusion in final report without documented necessity and Article 9 condition | Restricted Intellectus reviewer only; no LLM transfer until condition and safeguards are approved | No third-country transfer until Article 9 condition, DPA, transfer basis, and supplementary safeguards are approved |
| Public-source research and source verification | Public staff names, professional roles, published statements, organisation website content, public reports | **Article 6(1)(f), legitimate interests**, because verification supports a reliable diagnostic, subject to an LIA, source quality checks, relevance limits, and the right to object. Article 9 data must not be collected merely because it is public | Source URLs and necessary excerpts: 12 months; refresh or remove stale material when challenged | Intellectus, n8n, OpenAI API; original publishers remain separate controllers for their publication | Same vendor-transfer controls; store the minimum excerpt rather than full pages |
| Security, auditability, and incident investigation | Account IDs, timestamps, correlation/run IDs, access logs, error metadata; system-generated | **Article 6(1)(f), legitimate interests**, because proportionate logs are necessary to secure the service, prove human review, and investigate incidents. Logs must exclude document bodies and prompts | Security logs: 90 days; minimal review/approval record: 12 months | Authorised Intellectus security personnel, n8n hosting provider | Verify log location and support access; apply DPA and transfer mechanism as required |

### Legitimate Interests Assessment summary

1. **Purpose:** deliver a requested, evidence-based organisational diagnostic and protect the service.
2. **Necessity:** the diagnostic cannot be produced without limited organisational context, but names and sensitive details can often be removed; therefore redaction and field-level minimisation are mandatory.
3. **Balancing:** staff, volunteers, donors, and beneficiaries may not expect their information to enter an AI workflow. The balance is acceptable only with advance notice, restricted purposes, no individual scoring, human review, short retention, strong access controls, and an effective objection/erasure route.

## Section B — Risk and rights

### Special-category data

Article 9 data may be present or inferable in beneficiary reports and unstructured notes. Intellectus must default to excluding it. If the client asserts that sensitive data is necessary, legal review must document both an Article 6 lawful basis and a valid Article 9(2) condition before processing; ordinary consent language in a client contract is not enough.

### Automated decision-making — Article 22

The agreed use does not involve a solely automated decision with legal or similarly significant effect. The output is advisory, a consultant performs meaningful review with authority to correct or reject it, and the client is prohibited from using it to rank or decide outcomes for individuals. Human review must be evidenced, not reduced to a rubber stamp; any repurposing requires a new Article 22 and AI Act assessment.

### DPIA determination

**A DPIA is required before production processing.** The EDPB criteria engaged are: evaluation or scoring; sensitive or highly personal data; combining client and public datasets; vulnerable data subjects; and innovative AI-based processing. Large scale is plausible given multiple client organisations, while systematic monitoring and legal-effect automated decisions are outside the approved purpose. Meeting several criteria, combined with the uncertainty of unstructured documents, makes pre-processing assessment the defensible conclusion.

### Likely data-subject friction points

- **Access:** locating a person's data across uploads, extracted text, prompts, outputs, logs, and source excerpts.
- **Erasure:** deleting both source material and derived findings without corrupting necessary audit records.
- **Objection to profiling or legitimate-interests processing:** stopping further use and reassessing whether compelling grounds exist.
- **Rectification and contestability:** correcting inaccurate public information or AI-generated inferences that appear in a draft.
- **Transparency:** providing Articles 13/14 information when data came from the client or public sources rather than directly from the person.

Each run needs a data-lineage record linking source, excerpt, output, controller instruction, and deletion status. The client-facing process must route requests to River Learning Collective and enable Intellectus to assist within the controller's deadline.

### Controller / processor split

| Entity | GDPR role |
| --- | --- |
| River Learning Collective | **Controller** for the diagnostic: determines why the diagnostic is performed, which authorised documents are supplied, and how the reviewed report is used |
| Intellectus operator | **Processor** when operating the diagnostic on documented client instructions; **independent controller** only for its own narrowly defined billing, account-security, and legal-compliance records |
| n8n Cloud provider | **Subprocessor** used for orchestration, execution data, and logs, subject to verified region and subprocessor terms |
| OpenAI Ireland Limited | **Subprocessor** for API prompts and outputs in the agreed EEA customer arrangement; onward transfers and subprocessor access must follow the applicable DPA and Chapter V mechanism |
| Public website/report publishers | Separate controllers for their original publication; Intellectus remains accountable for its subsequent collection and reuse |

### Required DPAs

An Article 28 DPA is required between River Learning Collective and the Intellectus operator. Intellectus must also have processor/subprocessor terms with n8n and OpenAI, including processing instructions, confidentiality, security, deletion/return, rights assistance, breach support, audit information, subprocessor authorisation, and transfer terms. The client must receive and approve the current subprocessor list.

## Section C — Law stacking

- **AI Act cross-check:** In the defined organisational-advisory use, Intellectus is not an Annex III high-risk system because it does not make or support decisions about employment, education admission, credit, insurance, or access to essential services. It should still disclose AI involvement, preserve human oversight, train deployers in AI literacy, document limitations, and clearly label generated or inferred material. Repurposing it for decisions about people triggers a fresh classification.
- **ePrivacy check:** The fact pattern does not require analytics cookies, tracking pixels, or device-level profiling, so the diagnostic processing does not currently trigger a separate cookie-consent step. If non-essential analytics or marketing technologies are added, consent must be obtained before storage/access on the device; legitimate interests cannot substitute for that ePrivacy requirement.
- **Data Act check:** **N/A.** No connected product, IoT-generated data, or cloud-switching dataset is part of the diagnostic. Ordinary cloud-contract questions do not by themselves make Data Act access rights central to this audit.

## Reinforce — DPIA outline

### 1. Description of processing

Map collection from intake and uploads; client-side redaction; browser-to-n8n transfer; public research; extraction and prompt construction; OpenAI API processing; draft generation; consultant review; delivery; logging; retention; deletion; and subprocessor/remote-access paths.

### 2. Necessity and proportionality

Test every field and document category against the diagnostic purpose. Compare full-document upload with local redaction, structured questionnaires, pseudonymised excerpts, and client-generated summaries. Record why each retained item is necessary and how data subjects receive notice and exercise rights.

### 3. Principal risks

Sensitive or excessive uploads; prompt leakage; inaccurate inference; hidden repurposing for individual decisions; insufficient notice; inability to erase derived data; unauthorised n8n execution access; international-transfer exposure; and human-review automation bias.

### 4. Mitigations and sign-off

Content scanning and redaction, field allowlists, encryption, role-based access, EEA hosting where available, DPA/SCC/TIA review, no-training configuration, 30-day working-data deletion, 90-day metadata-only logs, per-run lineage and deletion, meaningful human approval, incident runbook, rights workflow, periodic sampling, and DPO/legal approval. If high residual risk remains, consult the competent supervisory authority before processing.

## Reinforce — DPA clause requested

**Deletion and derived-data clause:** On the controller's request or at the end of the 30-day working period, the processor and each subprocessor must delete raw documents, extracted text, prompts, model outputs, embeddings, caches, and identifiable execution data linked to the run; propagate deletion to backups under a documented schedule; return a machine-readable deletion confirmation; and retain only metadata expressly authorised by the controller.

This clause matters because deleting the uploaded file alone would not remove personal data reproduced in prompts, outputs, n8n executions, caches, or backups.

## Sources

- [GDPR — Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [EDPB guidance: when to do a DPIA and the nine criteria](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en)
- [European Commission: controller and processor roles](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en)
- [European Commission: Standard Contractual Clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)
- [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [OpenAI Data Processing Addendum](https://openai.com/policies/data-processing-addendum/)
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data)

This educational audit is a structured consulting assessment, not a substitute for advice from qualified German/EU counsel or the client's DPO.
