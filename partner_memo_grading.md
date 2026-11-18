# Phase 4 – Partner swap: memo grading

Rubric from class (score 1–3 per criterion, max 15).

## My partner graded my memo
**Grader:** _Max_ · **Date:** 18 Nov 2026 · **Memo graded:** RCSA Evidence & Challenge Agent memo (v1)

| Criterion | Score (1–3) | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | Clearly recommends proceeding with conditions; separates synthetic-data development from real-data deployment. |
| Lawful basis selection is justified | 1 | GDPR applicability identified, but no Art. 6 basis specified or justified; possible Art. 9 data needs assessment. |
| Top actions are specific and sequenced | 3 | Five concrete actions (pseudonymisation, process-level reporting, DPIA, vendor due diligence, works council). |
| Residual risks are named honestly | 3 | Sensitive data transfers, employee monitoring and missing privacy safeguards clearly communicated. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | GDPR, AI Act, DORA, MaRisk and employment law covered; ePrivacy not assessed; AI Act roles and Art. 50 need more precision. |
| **Overall** | **12 / 15** | Clear, practical first assessment; open questions on lawful basis, transfers and role/transparency precision. |

**Client response (partner as client):** accepts development on synthetic data; before deployment wants the lawful basis, the transfer mechanism and the AI provider's contractual responsibilities clarified, and the DPIA completed.

## I graded my partner's memo
**Memo author:** _Max_ · **Client brief:** AI-Powered Health Data Analytics for Insurance Companies (smartwatch manufacturer) · **Date:** 18 Nov 2026

| Criterion | Score (1–3) | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Stop the insurance data-sharing launch" is clear, and the fallback (launch only the optional personal analytics service) gives the client a usable path. |
| Lawful basis selection is justified | 2 | Correctly separates the two purposes and names Art. 6 and Art. 9 with consent requirements, but does not commit to a basis. For health data, explicit consent (Art. 9(2)(a)) is realistically the only option for the insurance purpose, and this should be stated. Art. 22 (automated decisions on pricing and eligibility) is not addressed, although the human review by insurers may be only formal. |
| Top actions are specific and sequenced | 2 | Three relevant, concrete actions. The order is implied (DPIA "before processing begins") but there are no owners, no timeline, and no clear gate saying which conditions must be met before the insurance channel can open. |
| Residual risks are named honestly | 3 | Inaccurate predictions, security of health profiles and pressure on consent validity are well chosen and honest. Discrimination against people with chronic conditions could be added. |
| Law stacking is addressed (AI Act / ePrivacy) | 1 | The AI Act is mentioned only as "verify requirements". Risk assessment and pricing for **life and health insurance is high-risk under Annex III 5(c)**, and the scoring could even be argued as **social scoring (Art. 5(1)(c))** because it uses data from an unrelated context. ePrivacy / TDDDG §25 (reading data from the user's device) and the **Data Act** (data from connected products) are not covered. |
| **Overall** | **11 / 15** | Strong, honest GDPR memo with a clear stop decision. Main improvement: classify the system under the AI Act and add the device-data laws (ePrivacy, Data Act). |

## What I changed in my memo after the feedback (v1 → v2)
- **Lawful basis:** added Art. 6(1)(f) with the reason why 6(1)(c) and consent do not fit; stated that Art. 9/10 data is filtered out rather than given a basis.
- **Transfers:** named the mechanism to verify (EU–US Data Privacy Framework or Standard Contractual Clauses plus a transfer impact assessment).
- **AI Act precision:** specified Art. 50(2) machine-readable marking as a provider duty, plus Art. 4 AI literacy; flagged that roles must be confirmed once the delivery model is fixed.
- **ePrivacy:** added an explicit assessment (not applicable: internal tool, no device tracking).
- Sequenced the actions: real data only after the DPIA/LIA and OpenAI due diligence.
