# Stretch — data protection by design checklist

**Highest-risk processing activity:** automated scoring, ranking and rejection of job applicants.
Each item marked **pass**, **fail** or **unknown** against the client's setup as described in the
agreed fact pattern. "Unknown" is used where the answer depends on vendor disclosure the client does
not yet have — and every unknown here is itself a finding, because a controller that cannot answer
these cannot demonstrate compliance under Art 5(2).

| # | Control | Status | Evidence |
|---|---|---|---|
| 1 | **Data minimisation** — is only the minimum necessary data collected? | **FAIL** | The full CV free text is ingested, including photograph, nationality and personal interests. None is necessary to assess fit against a job description, and each is a proxy for a protected characteristic |
| 2 | **Purpose binding** — is the data technically restricted to the stated purpose? | **UNKNOWN** | Nothing technically prevents the vendor reusing candidate data to improve its general model, and the contract is silent. Until the DPA prohibits it expressly, purpose binding rests on trust rather than design |
| 3 | **Access controls** — is access limited to those who need it? | **UNKNOWN** | The vendor stores and processes on US infrastructure; its sub-processors are undisclosed. The client cannot state who can reach candidate records, which means it cannot answer this question at all |
| 4 | **Retention enforcement** — automated deletion or anonymisation? | **FAIL** | No retention schedule exists for any of the five purposes, no automated deletion, and no per-jurisdiction matrix despite EEA-wide applicants. The training set has no version-linked deletion policy |
| 5 | **Subject rights workflow** — can access or erasure be answered inside 30 days? | **FAIL** | Access fails on Art 15(1)(h): the controller holds no logic information and the vendor is not obliged to supply it. Erasure is only partly satisfiable — deleting an application does not remove its influence on a trained model. No rectification path exists for a disputed tier |
| 6 | **Incident response** — documented detection and 72-hour notification? | **UNKNOWN** | No documented breach process spanning the client and the vendor, and no contractual notification window inside the client's own 72-hour Art 33 clock. A US-hosted processor with no notification SLA makes the deadline unmeetable by design |

**Score: 0 pass, 3 fail, 3 unknown.** No control passes outright, which is the honest summary for a
system six weeks from launch.

**What this changes about the advice.** The memo's bottom line stands — *go with conditions* — but
this checklist shows the conditions are not three discrete tasks; they are a design posture the
build does not currently have. Two observations worth putting to the client:

**The three "unknowns" are all vendor-facing, and all three collapse into one procurement
conversation.** Sub-processor disclosure, a contractual purpose restriction, and an incident
notification SLA are three clauses in one document. That makes them cheap to fix now and expensive
to fix after signature, which is the argument for doing the paperwork before the pilot rather than
alongside it.

**The three "fails" are all controller-side, and all three are fixable without the vendor.**
Minimisation is a decision about which fields to send; retention is a schedule and a cron job;
subject rights is a workflow plus the one DPA clause. None requires the model to change, and none
needs to wait for the December 2027 AI Act date — they are live GDPR obligations today.
