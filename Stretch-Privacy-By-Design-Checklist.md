# Stretch — Privacy by design checklist: AI CV scoring & auto-rejection

Highest-risk processing activity in the scenario: **automated scoring and rejection of job candidates.**

| Item | Status | Note |
|---|---|---|
| **Data minimisation** — only the minimum necessary data collected? | Unknown | The full CV plus assessment is ingested; unclear if fields irrelevant to scoring (e.g., photo, marital status, full address) are stripped before the model sees them. Needs a field-level review with the vendor. |
| **Purpose binding** — is data technically restricted to the stated purpose? | Fails | Historical hiring/retention data was collected to manage past employment relationships, not to train a future candidate-scoring model; there is no technical or contractual control currently stopping reuse for this new purpose. |
| **Access controls** — is access limited to those who need it? | Unknown | Not specified whether the vendor platform enforces role-based access (e.g., recruiter vs. HR admin) or whether scores/CVs are visible more broadly than needed. |
| **Retention enforcement** — automated deletion or anonymisation policies? | Fails | No retention period has been set for rejected candidates' data (Section A of the audit worksheet); nothing currently deletes or anonymises it. |
| **Subject rights workflow** — can the client respond to access/erasure requests within 30 days? | Unknown | Two-person HR team, no described process for handling data subject requests about the AI scoring pipeline specifically; likely to struggle without a defined workflow. |
| **Incident response** — documented process to detect and notify a breach within 72 hours? | Unknown | No incident-response process described for the vendor relationship; needs confirmation this is covered in the DPA (breach notification clause, vendor SLA for informing the client). |

**Read across:** most items land on "unknown," which is itself the finding — the client has not yet operationalised privacy-by-design for this system, only built the scoring capability. The DPIA (see [`Reinforce-DPIA-Outline.md`](./Reinforce-DPIA-Outline.md)) is the right vehicle to convert each "unknown" into a pass/fail before launch.
