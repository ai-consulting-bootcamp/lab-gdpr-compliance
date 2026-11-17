# Additional privacy checks

**Scenario:** NordDesk, Option B(a). All operational facts are synthetic. These are design requirements and an assessment outline, not evidence of implemented controls. The authoritative fact pattern is in [the Audit Pack](gdpr_audit_pack_sergii_rostovskyi.md).

## DPIA outline: archive preparation and model fine-tuning

| DPIA component | Proposed assessment |
|---|---|
| Description | Controller: NordDesk. Assess the complete path from its 80,000-conversation EU archive through authorised preparation, a proposed capped 5,000-record dataset, US training/evaluation, private checkpoints and human-reviewed inference. Inventory every copy, model version, retention clock and remote-access path. |
| Necessity and proportionality | Establish the original processing basis, Article 6(4) compatibility and the P2 lawful basis. Benchmark documentation retrieval and synthetic training first. Justify why any personal conversations are needed, the minimum dataset and each retention period. Establish an Article 9 handling route before sensitive preprocessing. |
| Individual harms | Private complaints could be disclosed or linked back to a person; one business could receive another's confidential details; false outputs could damage reputation; continued memorisation could prevent effective erasure; foreign access could reduce effective protection. |
| Controls | Separate the EU provenance index, restrict preparation access, exclude sensitive/third-party material, cap the approved dataset, prohibit vendor reuse, isolate tenants, verify processor/transfer terms, expire datasets and models, and provide a usable rights channel. |
| Verification evidence | Approved legal analysis and notices; signed DPA/SCC documents and TIA; dataset inventory and authorised screening report; extraction and cross-tenant test results; access-control review; timed deletion and model-retirement rehearsal. No such operational evidence exists in this lab. |
| Consultation | Seek privacy lead/DPO advice where appointed, consult affected representatives where appropriate, and record the reasoning. Check whether DPO appointment is legally required rather than assuming company size decides it. |
| Approval and review | Legal lead clears lawful processing, security lead clears safeguards, and CTO accepts only risks compatible with law. Article 36 consultation precedes processing if high residual risk cannot be mitigated. Reopen the DPIA for a new purpose, vendor, geography, dataset class or customer-facing deployment. |

### Proposed risk register

Ratings are qualitative teaching judgments about harm to people: low, medium or high. Target residual ratings are conditional design objectives, **not measured results**.

| Risk | Initial | Proposed mitigation and evidence | Target residual / release condition | Owner |
|---|---|---|---|---|
| R1 Unlawful secondary use | High | Legal approval of basis/compatibility; necessity comparison; notice version and delivery record. | Unresolved; no release until a lawful route is established. This cannot be accepted as a commercial risk. | Legal lead |
| R2 Sensitive/contextual identifiers survive preparation | High | Legally authorised screening, sampling, exclusions and quarantine; synthetic adversarial examples before any real-data test. | Medium only if controls are evidenced; otherwise block. | Privacy + ML leads |
| R3 Memorisation or cross-tenant disclosure | High | Private deployment, strict access isolation, output safeguards, extraction tests and disable/rollback capability. | Medium target; any confirmed disclosure blocks that model version. Zero observed leakage is not proof of anonymity. | ML + security leads |
| R4 Erasure cannot reach weights/checkpoints | High | Subject-to-model provenance, dataset exclusion, verified clean retraining or retirement, vendor deletion confirmation. | Medium target; no release without an effective request-handling path. | Engineering + privacy leads |
| R5 US access/onward transfers lack effective protection | High | TIA, appropriate SCCs, approved recipients, effective supplementary measures, access evidence; EEA-only fallback. | Unresolved until assessment; stop transfers if protection is insufficient. | Legal + security leads |
| R6 Staff over-rely on inaccurate drafts | Medium | Train agents, require ticket review, keep consequential actions outside the tool, sample approved replies. | Medium target; suspend if review becomes a rubber stamp or scope changes. | Support lead |

## Specific proposed DPA clause

> The Processor shall process Customer Content, training and evaluation datasets, prompts, outputs and customer-specific model artifacts solely on the Controller's documented instructions to provide the private support-model service. It shall not use them for its own or another customer's model training, evaluation, product improvement or advertising. The Processor shall impose equivalent restrictions on authorised sub-processors, provide an inventory of retained copies and artifacts, and assist with data-subject requests. On instruction or expiry, it shall delete affected datasets and artifacts or support verified clean retraining or retirement where deletion from weights cannot be demonstrated, confirm active-system deletion within seven days, and ensure residual backup copies expire within thirty days and cannot return to production without reapplying deletion instructions. It shall provide evidence sufficient for the Controller to verify these steps and notify the Controller without undue delay of any personal data breach.

**Why this clause:** A generic promise to delete uploaded files leaves vendor reuse, checkpoints and model memorisation unresolved. The proposed seven/thirty-day contractual service levels must be negotiated and tested; they are not existing vendor commitments or statutory GDPR deadlines. A complete Article 28 agreement still needs the other mandatory terms, and a DPA does not itself authorise an international transfer. [S1, S4 in legal_sources.md]

## UK variation: isolated extension, not part of the base facts

**Rewritten recommendation:** Go with conditions for an EEA-and-UK pilot only after a separate UK applicability and transfer review; keep the same hold on personal-data training until both regimes' requirements are satisfied.

Serving UK users is not enough to assume every UK rule applies automatically: assess UK GDPR territorial scope, including offering services to people in the UK or monitoring them. If applicable, review UK notices, rights, DPIA obligations and whether a UK representative is required. EU SCCs alone are not a UK transfer instrument: for restricted UK-to-US transfers, evaluate the UK IDTA or UK Addendum to EU SCCs and the required transfer assessment, or a verified applicable adequacy route. Do not assume the fictional US vendor qualifies for either country's DPF route. UK communications/cookie rules also require a separate PECR assessment. [S9]

## Mini data protection by design checklist

**Activity:** P2, historical support data preparation and fine-tuning. **Status reflects the assumed current proposal**, not proposed mitigations. Unknown means no evidence was supplied.

| Check | Current status | Required change / evidence |
|---|---|---|
| Data minimisation | **Fail** | Whole two-year archive includes identifiers and unnecessary text. Justify the smallest eligible subset and exclude sensitive/third-party material. |
| Purpose binding | **Fail** | Notice covers support only; training legal authority and technical separation are missing. Approve the legal route, prohibit reuse and enforce purpose-scoped access. |
| Access controls | **Unknown** | Supply named roles, least-privilege configuration, tenant-isolation tests and remote-access records. |
| Retention enforcement | **Unknown** | Demonstrate expiry for datasets, vendor copies, checkpoints and backups; review the existing 24-month archive. |
| Subject rights workflow | **Unknown** | Rehearse access and erasure through all copies and model versions within the one-month legal response deadline; use an earlier internal target. |
| Incident response | **Unknown** | Test detection, processor escalation without undue delay, controller assessment and authority notification within 72 hours of awareness unless unlikely to result in risk; high-risk breaches also require affected-person notification without undue delay. |

The lab's phrase "30-day deadline" is treated as shorthand: Article 12(3) says **one month**. Article 33's 72-hour requirement is conditional on risk and starts at awareness; an incident is not automatically reportable. [S1]
