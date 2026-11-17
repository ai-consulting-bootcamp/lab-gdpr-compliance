# GDPR Audit Pack - Sergii Rostovskyi

**Lab:** Same product, privacy lens  
**Scenario:** Option B(a), fine-tune an LLM on support chat logs  
**Assessment date:** 17 November 2026  
**Decision:** Go with conditions for a redesigned, restricted pilot. The proposed bulk upload is stopped.

## Audit worksheet

### Fact pattern

NordDesk Software GmbH is a fictional Berlin B2B SaaS company with 120 employees that supplies project-management software to 800 EEA businesses.  
It holds 80,000 support conversations from the previous 24 months, involving approximately 20,000 adult customer contacts and 18 support agents in Germany, France and the Netherlands.  
The archive contains names, work email addresses, account and ticket identifiers, timestamps, diagnostic details and free-text complaints, which may incidentally disclose health information or third-party information.  
NordDesk uses fictional EU TicketCloud GmbH in Germany for its own support desk and proposes sending a training dataset to fictional Atlantic Model Services Inc. in the United States, which uses fictional Atlantic Compute LLC as its US infrastructure sub-processor.  
The proposed fine-tuned model will draft technical support replies for NordDesk agents, who must read the underlying ticket and approve or rewrite every reply before sending it.  
The model will not rank people, monitor staff performance, decide refunds, close accounts, determine access to services or communicate directly with customers.  
The existing notice covers support resolution only; no training consent, compatibility assessment, LIA, DPIA or executed AI vendor agreement has been supplied.

### Scope and evidence boundary

All companies, quantities, controls and vendor arrangements above are **synthetic teaching assumptions**, not findings about real organisations. No customer logs were obtained, no model was trained, and no vendor was contacted. The initial archive and intended processing are the baseline; safeguards below are proposed changes, not controls already implemented. Sources and corrections to teaching shorthand appear in [legal_sources.md](legal_sources.md).

NordDesk acts as controller for these direct support conversations about its own service. Customer-uploaded project content processed on business customers' instructions is excluded: NordDesk could be a processor for that separate activity and cannot reuse that content for its own training merely because it hosts it. The analysis covers EEA adults only; a UK variation is isolated in the [additional checks](privacy_design_and_dpia.md).

### Section A - Data map

#### Data inventory and flow

| Field | Scenario answer |
|---|---|
| Categories | Direct identifiers, professional contact details, customer/tenant IDs, ticket IDs, dates, technical error reports, conversation content and agents' replies. Free text can include health, credentials, third-party details and confidential business information. Credentials are security-sensitive, but not automatically Article 9 data. |
| Sources | Contacts submit tickets through NordDesk's authenticated support portal; agents add replies. No scraped data, advertising data, customer project documents or external enrichment. |
| Subjects, scale and sensitivity | Approximately 20,000 customer contacts plus 18 agents, 80,000 conversations across 24 months and three EEA states. Counts are assumptions used to make the risk assessment concrete. |
| Current path | Contact/agent → EU TicketCloud support desk in Germany → authorised NordDesk support team. The 24-month archive exists, but its retention justification is unverified. |
| Proposed training path | EU TicketCloud → restricted NordDesk EU preparation environment → approved, minimised training subset → Atlantic Model Services in the US → Atlantic Compute US infrastructure → private model endpoint. The transfer gate blocks this path until cleared. |
| Proposed inference path | Agent sends the minimum current-ticket context through the same approved vendor chain; the model returns a draft to the agent. A customer receives only the human-approved response through the existing support desk. |
| Linkage and model artifacts | NordDesk retains a separate, access-controlled EU provenance index linking eligible records to subjects, dataset versions and model versions for rights handling. Dataset copies, prompts, evaluations, checkpoints and outputs remain in the personal-data inventory unless a documented assessment establishes otherwise. |
| Recipients | Named NordDesk support/privacy/security staff; EU TicketCloud; Atlantic Model Services; Atlantic Compute only as authorised sub-processor. No advertising recipients, public model release or vendor general-model training. |

#### One row per purpose

Periods below are **proposed maximums**, subject to necessity and legal review. They are not statutory GDPR retention periods. A legal hold must be documented, narrowly scoped, access-restricted and separately reviewed; it cannot justify training reuse.

| ID / purpose | Data and recipients | Article 6 basis and one-line justification | Retention / deletion rule |
|---|---|---|---|
| P1 Resolve support tickets | Contact details, relevant ticket content, agent replies; NordDesk and EU TicketCloud | **Legitimate interests, 6(1)(f), subject to a documented LIA:** answering business users' support requests is expected and necessary to operate the service; the customer company, rather than its employee, holds the contract, so Article 6(1)(b) is not automatically available for each contact. | Closed tickets: proposed 12 months from closure for recurrence analysis and follow-up; review the existing 24-month archive now and delete excess records unless specifically justified. Never retain old tickets solely to populate training. |
| P2 Prepare and fine-tune a private support model, including validation | A capped 5,000-conversation subset, without direct identifiers, third-party content, agent identifiers or special-category material; EU preparation staff, then approved US processors | **TBD — legal review.** Article 6(1)(f) is a candidate only after compatibility, necessity and balancing are demonstrated; the current bulk plan does not pass the proposed LIA. Separate valid consent under 6(1)(a) could support a redesigned future cohort but is not assumed for the archive. | Temporary EU extracts: 7 days maximum; approved train/evaluation files: 30 days after pilot evaluation, with a 90-day absolute cap from creation. Private checkpoints: expire after 90 days unless a new documented review authorises continued necessity. Rights requests can require earlier deletion or model retirement. |
| P3 Generate support drafts | Minimum relevant live-ticket text, no persistent customer profile; NordDesk and approved model vendor chain | **Legitimate interests, 6(1)(f), conditional on a separate LIA:** assisting agents can improve requested support, but less intrusive alternatives and customer expectations must be assessed; this basis does not authorise training reuse. | Vendor prompts/outputs: no storage beyond transient processing, to be contractually and technically verified; draft is discarded when replaced, and the approved reply follows P1. No prompt contents in diagnostics. |
| P4 Protect service and investigate security incidents | Pseudonymous access events, user/admin identifiers and limited network metadata; security staff and relevant processors | **Legitimate interests, 6(1)(f), subject to LIA:** limited event records are needed to detect misuse and investigate incidents without duplicating chat content. | Routine events: 90 days; documented incident evidence: reviewed at closure and deleted within 12 months thereafter unless a specific hold applies. |
| P5 Fulfil rights requests and demonstrate responses | Verified contact information, request history, provenance references and response evidence; privacy team and processors on instruction | **Legal obligation, 6(1)(c):** Articles 12–22 and accountability duties require handling and documenting applicable requests. | Proposed 24 months after closure, reviewed for necessity; do not keep extra identity-document copies. Provenance links last only while the corresponding dataset/model needs rights handling, then are deleted. |

Source anchors: GDPR Articles 5–6, 12–22, 25 and 28 [S1]; AI-model reasoning [S3]. No blanket Article 9 exception is claimed for any row: special-category handling requires the separate gate below.

#### Purpose limitation and legitimate interests

**Compatibility, Article 6(4):** Support and better replies are related, but two years of historical text used to change model weights is a substantial change in use. Contacts were told only about ticket resolution, the text may be sensitive, US processing broadens exposure, and extraction from trained weights can make rights harder to honour. Minimisation and private deployment reduce risk but do not establish compatibility by themselves; the original bulk proposal has **not demonstrated compatibility** and remains blocked.

| LIA step | Application to P2 | Finding |
|---|---|---|
| Purpose | Improve accuracy and reduce drafting time for NordDesk's own technical support, with no advertising, profiling or general-model development. | A specific business interest can be legitimate; commercial benefit alone does not settle lawfulness. |
| Necessity | Compare a documentation-only retrieval assistant, synthetic examples and a smaller curated dataset against fine-tuning on archived personal conversations. There is no measured evidence that personal-data fine-tuning is necessary. | **Not demonstrated.** Run the alternatives comparison first using public/product documentation and synthetic data. |
| Balancing | Users did not reasonably expect historical complaints to be used in US model training; sensitive disclosures, agents' employment relationship, third-party details and hard-to-reverse memorisation weigh against the bulk plan. | **Not passed for the current proposal.** Redesign, assess expectations, establish rights controls and obtain counsel's decision before personal-data preparation/training. |

A new label of legitimate interests cannot cure an incompatible further purpose. If the documented legal route fails, abandon archive reuse and use genuinely anonymous/synthetic data or a separately designed consent-based collection; consent must be freely given, specific and withdrawable, and cannot be inferred from a new notice. Customers cannot consent for every person mentioned in a ticket, and employee consent may not be freely given. Even anonymising existing personal records is processing that requires lawful authority. [S1, S3]

P1, P3 and P4 need their own LIAs: expected support, supervised drafting and proportionate security each have different necessity and balancing questions. A record's existence is not evidence that the original collection or 24-month retention was lawful.

#### International transfers and agreements

| Flow | Mechanism and required evidence | Current decision |
|---|---|---|
| NordDesk → EU TicketCloud, Germany | Article 28 DPA; verify storage, backups, support access and its complete sub-processor list. No Chapter V mechanism for the assumed EEA-only processing. | Review existing agreement and access evidence before reuse. |
| NordDesk → Atlantic Model Services, US | Proposed 2021 SCCs **Module 2** for controller-to-processor transfers, completed annexes, transfer impact assessment (TIA), Article 28 terms and effective supplementary measures. Confirm applicability of the selected SCC instrument, including the importer's GDPR status, with counsel. | **Blocked:** fictional vendor has no verified DPF certification, signed terms or TIA. DPF is not asserted as an available route. |
| Atlantic Model Services → Atlantic Compute, US | Prior specific or general written sub-processor authorisation, equivalent Article 28 obligations and documented SCC onward-transfer safeguards; confirm all further recipients and jurisdictions. | **Blocked** until chain is disclosed and approved. |
| Any third-country remote support access | Assess as a potential transfer even where servers are in Europe; cover relevant recipient/access path in the transfer assessment. | No unapproved access. EU hosting alone is insufficient. |

Encryption in transit and at rest, tenant isolation and EU-held linkage keys are required safeguards, but do not eliminate exposure when a vendor must read plaintext to train or infer. SCC signatures alone are insufficient: if effective protection cannot be achieved, do not transfer and use an EEA-only alternative with verified access restrictions. [S1, S4]

### Section B - Risk and rights

**1. Are Article 9 data present or inferable?** Yes: free-text complaints may reveal health or other protected attributes, although this is an assumed risk rather than an inspected finding. There is no established Article 9 condition for training or even sensitive-data preprocessing, so counsel must authorise an appropriate handling route before inspection/filtering, exclude such material from the training scope, and block processing if exclusion cannot be reliably achieved; no sensitive inference feature is allowed. [S1]

**2. Does Article 22 apply?** On the fixed facts, the system drafts technical replies and makes no solely automated decision with legal or similarly significant effects. Agents must examine the ticket and independently approve/edit the draft, while refund, account-access and other consequential decisions stay outside the system; adding those uses or rubber-stamping outputs requires a fresh assessment before deployment. [S1]

**3. Is a DPIA required?** Treat it as required before new personal-data preparation or training: innovative model development, highly personal correspondence and plausible large-scale reuse together indicate likely high risk. The nine-criterion screening below supports that conclusion without claiming that all AI automatically requires a DPIA; check the competent German authority's Article 35(4) list and consult under Article 36 if high residual risk remains. [S1, S2]

**4. What rights friction is likely?** Access and rectification require locating a person's information across tickets, training/evaluation datasets, outputs and model versions while protecting other people's data. Erasing source rows does not guarantee removal from weights, so NordDesk needs provenance, exclusion lists and a verified retraining/retirement path; objections to legitimate-interests processing require an Article 21 assessment, whereas any future direct-marketing objection would be absolute. Respond without undue delay and within **one month**, with only a justified extension notified within that month, and apply portability only where its consent/contract and automated-processing conditions are met. [S1]

**5. Who is controller or processor?** NordDesk is controller for its direct support and proposed training purposes, EU TicketCloud and Atlantic Model Services are processors, and Atlantic Compute is the model vendor's sub-processor. No independent vendor reuse is authorised; an entity deciding its own reuse purpose would require separate controller analysis, while this lab's consultant receives synthetic information only and is not assumed to process real customer records. [S1]

**6. Which DPAs are needed?** NordDesk needs Article 28 agreements with EU TicketCloud and Atlantic Model Services, and the latter must impose equivalent obligations on Atlantic Compute with the required authorisation. These must cover instructions, confidentiality, security, rights/DPIA assistance, breaches, deletion/return, sub-processors and audit evidence, with training reuse expressly prohibited outside NordDesk's documented purpose. [S1]

#### Nine-criterion DPIA screening

This table is scenario-specific reasoning using the EDPB-endorsed WP29 framework, not a mechanical legal score. [S2]

| Criterion | Applies? | Reason for this scenario |
|---|---|---|
| 1. Evaluation or scoring | No on stated facts | Replies concern technical issues; there is no evaluation of customer traits or employee performance. |
| 2. Automated decisions with legal/similar significant effects | No on stated facts | The model cannot grant, refuse or terminate services and drafts are reviewed. |
| 3. Systematic monitoring | No for the training use | Archived user-initiated support is reused, but people are not continuously observed or tracked; security logs do not introduce behavioural monitoring in this scenario. |
| 4. Sensitive or highly personal data | Yes | Private correspondence is highly personal and may contain health disclosures, even when special-category processing is not intended. |
| 5. Large-scale processing | Likely | 80,000 conversations, about 20,000 contacts, two years and three countries justify treating scale as a risk factor; GDPR has no universal numerical threshold. |
| 6. Matching or combining datasets | No | A single support archive is used with a provenance index, not enrichment from unrelated datasets. |
| 7. Vulnerable subjects | Potentially | Agent text concerns employees in a power imbalance; no children are targeted, and agent identifiers and evaluation uses must be excluded. |
| 8. Innovative technology/organisational solution | Yes | Fine-tuning can retain information in weights and complicate deletion compared with the existing ticket desk. |
| 9. Preventing rights or access to a service/contract | No as a functional purpose | Support is available regardless of training participation and no eligibility decision occurs; practical deletion difficulty remains a risk, without automatically equating it to this criterion. |

### Section C - Law stacking

- **AI Act:** Hypothesised minimal-risk internal drafting use, outside Annex III on these facts; assess NordDesk's provider/deployer role, literacy and applicable generated-text marking duties, and reassess Article 50 interaction disclosure if the tool becomes customer-facing. [S5]
- **ePrivacy:** Only strictly necessary authentication/session storage is assumed, with no analytics, retargeting or fingerprinting; any non-essential device access requires the applicable prior-consent route, and communications-confidentiality/national-law applicability to chat reuse is **TBD — legal review**, independent of GDPR legitimate interests. [S6]
- **Data Act:** No connected-product data is involved, but assess cloud/data-processing-service switching rules for the hosting/model contracts and NordDesk's own SaaS; require export/exit provisions without assuming every custom model service has identical duties. [S7]

**Timing note:** The AI Omnibus entered into force on 27 July 2026; its delayed high-risk dates do not postpone GDPR obligations. The Council adopted a Data Omnibus negotiating position on 21 October 2026, which is not enacted GDPR/ePrivacy reform; this pack does not rely on proposed AI-training privileges or a 96-hour GDPR breach deadline. [S5, S8]

## Client recommendation memo

**To:** CTO and Legal Lead, NordDesk Software GmbH  
**From:** Sergii Rostovskyi, AI Consulting  
**Subject:** Conditions for a private support-model pilot  
**Date:** 17 November 2026

<!-- MEMO_START -->
Go with conditions for a restricted pilot, because better support replies may be achievable without exposing the full historical archive or weakening customers' rights. Do not upload the two years of chats or begin personal-data preparation or training yet. The current proposal lacks an established training basis, a completed DPIA and verified transfer safeguards.

First, your legal lead and product owner should settle the data-use decision. Document the original collection basis, assess compatibility with model training, and compare fine-tuning against retrieval from product documentation and synthetic examples. Legitimate interests is only a candidate, not an approval: necessity and balancing remain unproven. Update notices before any approved reuse. If the legal assessment fails, stop archive reuse and redesign around synthetic data or a separately validated consent route. Do not treat removed names as proof of anonymity, or assume that sensitive-data filtering is exempt from legal requirements.

Second, procurement and security should close the vendor gate before any US access. Execute processor terms with Atlantic Model Services, approve Atlantic Compute and verify the existing TicketCloud agreement. Complete the SCC annexes and transfer impact assessment, including remote access and onward transfers. Prohibit vendor reuse, agree deletion evidence and verify whether effective protection is achievable when the provider processes plaintext. If it is not, use an EEA-only alternative with verified access restrictions.

Third, your privacy lead and engineering team should complete the DPIA and prove the controls before releasing the pilot. Cap the dataset, exclude sensitive and third-party content through an authorised process, enforce expiry, test tenant isolation and rehearse access, objection and erasure requests, including model retirement. Keep consequential decisions outside the tool and require agents to review every draft. Check AI Act duties, communications confidentiality and cloud-switching terms alongside GDPR. The CTO should authorise release only after legal and security owners provide the evidence.

Three risks remain: rare contextual details may survive filtering and be memorised; correction or erasure may require expensive retraining or withdrawal of a model; and foreign access or onward processing may remain difficult to verify. A successful technical test does not remove these risks. Record the remaining exposure, and consult the supervisory authority before processing if the DPIA still identifies high residual risk.
<!-- MEMO_END -->
