# GDPR Audit Pack — Vittal Navale

**Partner:** Ugo · **Scenario:** Option B(b) variant — AI-assisted CV screening for a national retail chain

> **Transition note.** The intended Option A source (`W6_LAB-Classify-your-product`, the EU AI Act lab repo) was empty at the time of this lab, so no prior AI Act tiering could be carried forward. Instead we use a self-authored case in the same spirit as Option B(b) "CV screening with human review": a retail chain's automated CV ranking and rejection tool. Under the EU AI Act, an AI system used for recruitment or selection of natural persons — including CV-sorting/ranking software — falls under **Annex III, high-risk** use cases (employment, workers management, self-employment access). That classification is treated as a given below and cross-checked in Section C, mirroring how an AI Act tier would normally be inherited from a prior audit.

---

## Section 0 — Fact pattern

The client is a national retail chain (~15,000 employees across EU/EEA stores and distribution warehouses) whose two-person HR team receives roughly 400 CVs a week for store and warehouse roles. They are piloting an AI-based CV screening tool, licensed from a US-based HR-tech vendor, that ingests each resume plus a short online skills assessment and scores the candidate against the job description. Candidates are auto-sorted into "strong fit," "maybe," or "not a fit" tiers. Recruiters currently only open the "strong fit" folder before making outreach calls; "not a fit" candidates receive an automated rejection email with **no confirmed human review step**. The scoring model was trained on five years of the client's historical hiring and retention data (who was hired, and who stayed past one year). Data subjects are job applicants located in the EU/EEA; the vendor processes and stores assessment and scoring data on US infrastructure. HR wants to launch within six weeks and has not yet decided whether a recruiter must review "not a fit" outcomes before rejection goes out.

---

## CFU Checkpoint 1 — Recognize

- **Categories of personal data present:** identity data (name, contact details), education and employment history, assessment responses, derived scores/tier labels, and — for the training set — historical employee retention outcomes (who stayed past one year).
- **Special-category data (Article 9):** none is *collected* directly, but it is plausibly **inferable**: name and address can proxy for ethnicity or national origin, resume gaps can proxy for disability, pregnancy, or caregiving status, and a retention-outcome model trained on past hires risks encoding historical bias correlated with protected characteristics. This must be treated as a live Article 9 risk, not dismissed because no explicit special-category field exists.
- **Cross-border data flow:** yes. The vendor stores and processes CV and assessment data on US infrastructure, so personal data leaves the EU/EEA at the point of transfer to the vendor.

---

## Section A — Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | Identity/contact data (name, email, phone, address); education & employment history; free-text CV content; online assessment answers/scores; system-generated fit-tier label; historical hiring/retention outcomes (training set only) |
| **Sources** | Direct from candidates (CV upload, assessment portal); internal HR systems (historical hiring/retention records used for model training) |
| **Purpose(s) — one row per purpose** | (1) Evaluate and shortlist a specific candidate for a specific role; (2) Rank/score candidates via the AI tool; (3) Send automated rejection notice to "not a fit" tier; (4) Train/improve the scoring model using historical hiring & retention data |
| **Lawful basis per purpose** | (1) Contract — Art. 6(1)(b), necessary to take steps at the applicant's request prior to entering an employment contract. (2) Legitimate interests — Art. 6(1)(f); efficient shortlisting of high application volume, subject to a documented LIA and to the Art. 22 safeguard described in Section B. (3) TBD — legal review (depends on whether rejection stays "solely automated"; see Section B). (4) TBD — legal review (repurposing former employees' records for model training is a new purpose not covered by their original employment-relationship processing; needs a fresh compatibility assessment under Art. 6(4) or a documented LIA, ideally with anonymized/aggregated training data) |
| **Retention period per purpose** | Application/assessment data for unsuccessful candidates: recommend 6–12 months (to defend against discrimination claims), then delete/anonymize; successful candidates' data folds into the employee HR file under normal retention rules; training dataset: TBD — legal review on how long historical outcome data can be retained and reused for this secondary purpose |
| **Recipients and sub-processors** | Internal: HR team, hiring recruiters. External: the US-based AI scoring vendor (processor); any cloud/infra sub-processors the vendor uses (TBD — legal review, needs vendor disclosure) |
| **International transfers and transfer mechanism** | EU/EEA → US, via the vendor's infrastructure. Requires Standard Contractual Clauses (SCCs) plus a Transfer Impact Assessment (Schrems II), and/or confirmation the vendor is certified under the EU-US Data Privacy Framework. Currently: TBD — legal review, no mechanism confirmed |

---

## Section B — Risk and rights

**Are any special-category data present or inferable from the outputs (Article 9)?**
Yes, by inference rather than direct collection. Name, address, resume gaps, and education institutions can act as proxies for race, ethnicity, disability, or age, and a model trained on past retention outcomes can reproduce historical discriminatory patterns. This should be treated as Article 9 in-scope and requires bias/fairness testing, not just a "we don't collect that field" defense.

**Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?**
Yes — the "not a fit" tier currently triggers an automated rejection email with no confirmed human review, and access to employment is a legally/similarly significant effect. As designed, this is a solely automated decision that Article 22(1) prohibits unless an exception applies (explicit consent, contract necessity, or authorized by law) with suitable safeguards (Art. 22(3)): the right to obtain human intervention, to express a point of view, and to contest the decision. Employment consent is inherently weak due to the power imbalance, and "contract necessity" is a thin basis for wholesale auto-rejection. **The safest and simplest fix is procedural: require a recruiter to review every "not a fit" outcome before rejection is sent**, which removes the decision from "solely automated" and sidesteps Article 22 restriction entirely.

**Is a DPIA required?** Using the EDPB's nine criteria, this processing meets at least four: (1) evaluation/scoring of individuals, (2) automated decision-making with legal/similarly significant effect, (3) sensitive data or data of a highly personal nature (inferable special-category data), and (4) data processed at scale (~400 CVs/week, ~20,000+/year) affecting a group in a dependent position (job seekers). Meeting two or more criteria triggers a DPIA under EDPB guidance — **a DPIA is required** before this system goes live.

**What data subject friction points are most likely?**
Right of access and explanation (candidates asking why they were rejected and what data/logic drove the score), right to object to profiling, and the right to human intervention under Article 22(3) once the automated-rejection flow is live.

**What is the controller/processor split?**
The retail chain is the **controller** — it determines the purposes (who to hire) and means (using the tool to screen at this volume). The AI vendor is the **processor**, acting on the retailer's instructions to score CVs — unless the vendor also uses client data to improve its product across other customers, in which case the vendor becomes an independent controller (or joint controller) for that secondary purpose, and that needs to be checked in the vendor contract.

**Is a DPA needed with any vendor? Which ones?**
Yes — a Data Processing Agreement (Art. 28) is required with the AI scoring vendor before any live candidate data is sent to it, covering processing instructions, sub-processor disclosure, security measures, and international-transfer terms (SCCs).

---

## Section C — Law stacking

- **AI Act cross-check:** CV screening/ranking for recruitment is an **Annex III high-risk** use case. Beyond GDPR, the AI Act adds: a documented risk-management system, data governance requirements for training data, technical documentation and logging, **human oversight** built into the system design (not left to informal practice), accuracy/robustness/bias testing, and a conformity assessment before deployment, plus a transparency obligation to inform candidates an AI system is used. The undecided "should recruiters review 'not a fit'" question is a live AI Act gap, not just a GDPR one.
- **ePrivacy check:** The online assessment portal likely sets session cookies; if it also runs analytics/tracking cookies, ePrivacy consent requirements apply on top of GDPR before any non-essential cookie is set. This is a secondary risk here — flag it for the assessment vendor, but it is not the primary exposure.
- **Data Act check:** N/A — no connected product or cloud-switching data involved in this scenario.

---

## Phase 3 — Client recommendation memo

**To:** Retail Chain HR Leadership & Legal
**From:** Vittal Navale, Privacy Advisory
**Re:** AI CV Screening Tool — GDPR/AI Act Go-Live Assessment

**Bottom line: Go, with conditions.** The tool addresses a real operational problem, but as currently configured — automated rejection with no confirmed human review — it creates an unlawful Article 22 automated-decision exposure and an unassessed AI Act high-risk deployment. Neither is fixable after launch without real cost, so both need to close before the six-week date, not after.

**Top three actions, in order:**

1. **Mandate human review of every "not a fit" rejection before it's sent**, no exceptions, and document this as a process control. This single change takes the rejection flow out of "solely automated" territory and resolves the Article 22 exposure without redesigning the model.
2. **Complete a DPIA before first live processing.** The scoring system meets at least four of the EDPB's nine trigger criteria (evaluation, automated decision-making, inferable special-category data, and scale). This is not optional, and it should include a bias/fairness test on the historical training data before it goes near a live candidate.
3. **Sign a Data Processing Agreement and Transfer Impact Assessment with the vendor before any candidate data is sent to US infrastructure.** Confirm whether the vendor operates as a processor only, or also reuses client data to improve its own model — that distinction changes the contract terms and the DPIA scope.

**Residual risks, even with these fixes:**

- **Bias in the training data.** Five years of "who stayed past one year" reflects whoever your past hiring and management practices favored — including any historical bias. A fairness audit reduces this risk but cannot fully certify the model as neutral; expect to monitor outcomes by group after launch, not just before.
- **Candidate transparency and explainability.** Even with human review added, candidates will ask why they scored "not a fit," and today there's no clear answer beyond "the model said so." Recruiters need enough visibility into the scoring rationale to give a real answer, or this becomes a recurring access-request and reputational problem.
- **Vendor dependency.** Even with a signed DPA and SCCs, the client is trusting a third party's infrastructure and practices for a high-risk process. A transfer mechanism reduces legal exposure; it does not eliminate the operational risk of relying on a US vendor for a decision this sensitive.

**Recommendation stands as go-with-conditions — not go as-is, and not stop.** The business need is real and the fixes are achievable inside six weeks if action 1 starts immediately.

---

## Phase 4 — Partner swap and peer review

*To be completed after swapping this memo with Ugo. Fill in the table and closing note once the swap has actually happened — do not fabricate a partner's feedback.*

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

**As the "client" (Ugo), two to three sentences: accept / flag one concern / ask for a redesign of one section.**

_(pending swap with Ugo)_

## CFU Checkpoint 5 — Debrief

*To be completed after comparing notes with Ugo: where the two audits agreed on lawful basis or DPIA need, where they diverged, and which reading was stronger and why.*

_(pending debrief with Ugo)_
