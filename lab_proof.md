# Lab proof: Same product, privacy lens

**Author:** Sergii Rostovskyi  
**Scenario:** Option B(a), fine-tune an LLM on support chat logs  
**Client:** NordDesk Software GmbH, a fictional B2B SaaS company  
**Assessment date:** 17 November 2026

## Reviewer entry point

Read the [GDPR Audit Pack](gdpr_audit_pack_sergii_rostovskyi.md) for the core submission: a seven-line fact pattern, Sections A–C, all nine DPIA criteria and the client recommendation memo. Then read the [workflow and evidence](audit_workflow_and_evidence.md) for the input, completed analytical run, produced findings, final output and limitation.

The decision is **go with conditions for a redesigned restricted pilot**, with the initial bulk upload and personal-data preparation/training blocked. This is an educational assessment of synthetic facts, not an assertion that a real company is compliant.

## Required proof elements

| Required element | Submitted evidence |
|---|---|
| Code or workflow export | [Eight-step analytical workflow](audit_workflow_and_evidence.md#workflow-export); a document audit does not require application code. |
| One run/query and its input | [NORDDESK-AUDIT-001 input question and synthetic facts](audit_workflow_and_evidence.md#run-input). |
| Evidence the run produced | [E1–E8 reasoning trace](audit_workflow_and_evidence.md#evidence-produced-by-the-analytical-run), linked to the final audit findings. |
| Final output | [Client recommendation memo](gdpr_audit_pack_sergii_rostovskyi.md#client-recommendation-memo), with three sequenced actions and three residual risks. |
| Failure or limitation | [Failed release gate and evidence limitations](audit_workflow_and_evidence.md#failure--limitation-encountered). |

## Rubric coverage

| Requirement / checkpoint | Where addressed | Status and qualification |
|---|---|---|
| Learning objective: mini audit plus advisory memo | Audit Pack, both principal sections | Complete as a written synthetic exercise. |
| Recognize (rubric rows 2 and 7) | Fact pattern, data inventory, Article 9 and transfer analysis | Complete. |
| Apply (rows 3 and 8) | Sections A–C; bases with justifications, retention, roles, rights, LIA and DPIA | Complete; legal uncertainties are explicitly labelled rather than guessed. |
| Integrate (rows 4 and 9) | Client memo | Complete; **365 words**, excluding heading and To/From/Subject/Date fields. |
| Verify (rows 5 and 10) | [Five-criterion review and client response](simulated_peer_review_and_debrief.md) | Completed **simulation**; no human partner exchange claimed. |
| Debrief (rows 6 and 11) | Simulated review, agreements/divergences and selected reasoning | Completed **simulation**; acceptance as a substitute remains an instructor decision. |
| Reinforce | [DPIA outline, DPA clause and UK variation](privacy_design_and_dpia.md) | Included; UK variation is separate from base facts. |
| Stretch | Additional checks, six-row privacy-by-design checklist | Included with Fail/Unknown status based on the assumed current setup. |
| Submission hygiene | [README file inventory](README.md) and this entry point | Lab-only Markdown files; no real customer data or credentials. |

## Integrity and submission status

All client and vendor details are invented for this exercise. Proposed controls and target risk ratings are not described as implemented. [Sources and interpretation notes](legal_sources.md) distinguish course requirements from legal authority and document important wording/date corrections.

The work is prepared locally. No commit, push, pull request or portal submission is performed as part of this preparation; those actions require the author's separate confirmation. The original `instructions.md` and `rubric.md` are retained as assignment references.
