# Audit workflow and evidence

**Run ID:** NORDDESK-AUDIT-001  
**Date:** 17 November 2026  
**Execution type:** Document-based analytical walkthrough with synthetic inputs, assisted by AI. This is a workflow export and completed reasoning trace, not a software execution log, production audit or model-training experiment.

## Workflow export

1. Freeze one fact pattern and label assumptions.
2. Recognise personal, potentially special-category and cross-border data.
3. Map sources, purpose-specific bases, recipients and retention.
4. Apply purpose compatibility and the three-stage LIA to training.
5. Screen all nine DPIA criteria, Article 22 and rights feasibility.
6. Check processor terms, transfer safeguards and the other law layers.
7. Make a release decision, sequence actions and write the client memo.
8. Challenge that decision through an explicitly simulated review, record the stronger readings and verify deliverable coverage.

## Run input

**Question evaluated:** Can NordDesk send its two-year support archive to Atlantic Model Services in the US to fine-tune a private model that drafts replies for human agents, and what must happen before a pilot may proceed?

**Input bundle:** 80,000 conversations, approximately 20,000 EEA customer contacts, 18 agents, three EEA countries, a support-only notice, no training consent or approved LIA/DPIA, and no supplied AI vendor contracts or transfer evidence. The model drafts technical replies only. All values are fictional assumptions from the seven-line [fact pattern](gdpr_audit_pack_sergii_rostovskyi.md#fact-pattern), not measurements or collected customer data.

## Evidence produced by the analytical run

Each row records a conclusion actually documented in this submission. Evidence here means **reasoning artifacts**, not proof that a fictional company's controls operate.

| Step / evidence ID | Observation from input | Evaluation and result | Result artifact |
|---|---|---|---|
| E1 Recognise | Names, work emails and private complaints exist in the assumed archive. | Personal data is present; free text may include Article 9 material. Names-only redaction does not establish anonymity. | Audit Pack, Section A inventory and Section B question 1. |
| E2 Apply | Original notice covers support; no training approval exists. | P2 is a separate purpose. Compatibility is not demonstrated, and training remains TBD. | Audit Pack, purpose table and compatibility assessment. |
| E3 Apply | Full archive proposed without alternatives comparison. | LIA purpose is identifiable, but necessity is unproven and balancing does not support the bulk plan. | Audit Pack, three-row LIA. |
| E4 Apply | US model vendor and US infrastructure are proposed without verified agreements. | Transfers are blocked until processor terms, appropriate transfer tool, TIA and effective safeguards are evidenced. | Audit Pack, transfer table. |
| E5 Apply | Historical private text, scale and innovative training combine. | DPIA required on the assumed facts; the remaining criteria are assessed rather than indiscriminately marked yes. | Audit Pack, nine-criterion screening. |
| E6 Integrate | No autonomous consequential decision; human-controlled drafts. | Article 22 is not triggered on this scope; scope changes reopen the analysis. AI Act, ePrivacy and Data Act are checked separately. | Audit Pack, Sections B–C. |
| E7 Verify | Simulated client challenges necessity and model erasure. | Retain the training hold and require an alternative-design comparison and effective model retirement/retraining path. | Simulated peer review, client response and challenge log. |
| E8 Debrief | Competing interpretations of lawful basis and DPIA need. | Select case-specific legal assessment over blanket contract/AI assumptions; record the outcome as simulated. | Simulated peer review, debrief. |

## Final output

**Go with conditions for a redesigned restricted pilot; stop the current bulk upload and all new personal-data preparation/training until the gates close.** The [client memo](gdpr_audit_pack_sergii_rostovskyi.md#client-recommendation-memo) sequences legal approval, vendor/transfer clearance and DPIA/control evidence. The [additional checks](privacy_design_and_dpia.md) define the proposed risk treatment and evidence needed to release.

## Failure / limitation encountered

The proposed release gate **fails** because the scenario provides no defensible training authorisation, no completed DPIA and no verified vendor/transfer safeguards. The workflow therefore produces a hold and redesign conditions rather than inventing compliance evidence. Because all data are synthetic, this exercise cannot establish actual anonymisation, model leakage rates, vendor practices or successful erasure; those remain required operational checks.

A second limitation is the absence of a human partner: the review and debrief are simulated, and only the instructor can decide whether that substitutes for the prescribed exchange.
