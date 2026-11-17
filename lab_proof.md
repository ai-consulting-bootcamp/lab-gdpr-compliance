# GDPR Audit Pack – Elif Yurdakul
### Lab: Same product, privacy lens

> First-pass consulting assessment, not legal advice. Items marked **TBD – legal review** or ⚖️ need confirmation by a lawyer or DPO.

---

## Transition note (from the EU AI Act lab)
I carry forward **Case 2 from Pieter's set: the online lender** that approves or declines loans with a model built on open-banking data. In the EU AI Act lab it was classified **high-risk (Annex III point 5(b), creditworthiness of natural persons)**, with the decision *approve with controls*. It is the most interesting case for GDPR because it combines almost every trigger in one system: large-scale financial data, possible inference of sensitive data from bank transactions, automated decisions with a legal effect (credit refused), several data sources matched together, and a non-EU vendor. The other cases are either banned outright (contact centre) or carry little personal data (bakery, voice agent).

---

# Part 1 · Audit worksheet

## Phase 1: Fact pattern
**FlexKrediet B.V.** is an Amsterdam-based online consumer lender (about 120 staff) offering personal loans of €1,000–€25,000 to customers in **the Netherlands and Germany**, with around **40,000 applications a year**. Applicants fill in an online form (identity, contact details, income, employment, housing costs) and connect their bank account through a licensed **open-banking provider (account information service, EU-based)**, which shares 12 months of transactions. FlexKrediet also queries the national **credit bureau** (BKR in the Netherlands, SCHUFA in Germany). A **scoring model** turns this into a risk score and an approve / decline / refer outcome; the model runs on a **US-based machine-learning platform** (SaaS, EU hosting region, US parent company), and the model is retrained every quarter on past applications and repayment outcomes. Approvals under €5,000 are sent automatically; declines and borderline cases go to a credit officer. All data subjects are in the EU.

**Recognise:**
- **Personal data:** identity and contact data, ID document, income and employment, credit bureau records, full bank transaction history, device and IP data, model score and decision.
- **Special-category data (Art. 9):** not collected directly, but **inferable from transactions**: payments to doctors, pharmacies or clinics (health), trade-union dues, churches or mosques (religion), political parties.
- **Crossing an EU border:** yes, potentially. The ML platform has a US parent, so remote access or support from the US counts as a transfer.

## Phase 2 · Section A: Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | Identity (name, date of birth, address, ID number), contact, income and employment, housing costs, bank transactions (12 months), credit bureau data, device/IP, risk score, decision and reasons |
| **Sources** | Applicant (form, ID upload) · open-banking provider (with the applicant's authorisation) · credit bureau · FlexKrediet's own repayment records (for model training) |

| Purpose | Lawful basis (Art. 6) + one-line justification | Retention |
|---|---|---|
| **P1 · Creditworthiness assessment and loan decision** | **Legal obligation (c)** + **contract (b)**: EU consumer credit law requires lenders to assess creditworthiness before granting credit, and the assessment is needed to enter the loan contract. | Declined applicants: **TBD – legal review** (proposal: 6 months, for complaints). Customers: loan term + legally required period. |
| **P2 · Using open-banking transaction data** | **Contract (b)**, with the applicant's explicit authorisation under payment-services rules (PSD2) as a separate, non-GDPR requirement. Whether PSD2 "explicit consent" also needs GDPR consent: **TBD – legal review** ⚖️ | Only derived features kept after the decision; raw transactions deleted within **30 days** (proposal) |
| **P3 · Fraud and identity checks** | **Legitimate interests (f)**: purpose (preventing fraud), necessity (identity and device checks are the least intrusive way), balancing (expected by applicants, limited data) → LIA to document. Anti-money-laundering identity checks: **legal obligation (c)**. | AML records: 5 years after the relationship ends (legal requirement); fraud signals: **TBD** |
| **P4 · Model training and monitoring** | **Legitimate interests (f)**, pseudonymised data: purpose (accurate, fair lending), necessity (past outcomes needed), balancing (high impact on people) → **TBD – legal review**; LIA required. Note: the new purpose must be compatible with P1 (Art. 6(4)). | Training snapshots: **TBD** (proposal: 2 years, pseudonymised) |
| **P5 · Bias testing** | AI Act Art. 10(5) allows processing special-category data strictly for bias detection in high-risk systems, with safeguards; GDPR basis: **TBD – legal review** ⚖️ | Deleted once bias testing is done |

| Field | Answer |
|---|---|
| **Recipients and sub-processors** | Open-banking provider (independent controller for the bank connection) · credit bureau (independent controller) · US ML platform (processor) · cloud hosting (sub-processor of the ML platform) · credit officers (internal) |
| **International transfers + mechanism** | Possible transfers to the **US** via the ML platform (support access, US parent). Mechanism: the **EU–US Data Privacy Framework** if the vendor is certified; otherwise **Standard Contractual Clauses + a transfer impact assessment**. Check certification and the current status of the Framework. ⚖️ |

## Phase 2 · Section B: Risk and rights

**Special-category data (Art. 9)?** Not collected, but it can be **inferred from transaction descriptions** (health, religion, trade union, politics), and a model may learn to use these patterns. Mitigation: filter or mask these merchant categories before features are built, and test whether the model uses proxies for them.

**Automated decision-making (Art. 22)?** **Yes.** Approvals under €5,000 are fully automated, and the score largely determines declines. Following the CJEU's SCHUFA judgment (C-634/21, 2023), a score that plays a **determining role** in a credit decision can itself be an automated decision. Safeguards: Art. 22(2)(a) (necessary for the contract) **plus** the right to human intervention, to express one's view and to contest the decision; meaningful information about the logic involved (Arts. 13–15). Declines always reviewed by a credit officer.

**DPIA required?** **Yes, clearly.** Applicable EDPB criteria (two or more normally require a DPIA): (1) evaluation or scoring ✔ · (2) automated decision with legal effect ✔ · (4) sensitive or highly personal data (financial data, possible Art. 9 inference) ✔ · (5) large scale ✔ · (6) matching datasets (form + bank + bureau) ✔ · (8) innovative technology (ML scoring) ✔ · (9) prevents people from using a service or contract (credit refused) ✔. Seven of nine criteria apply.

**Likely data subject friction points:**
- **Access and explanation:** declined applicants asking "why?". FlexKrediet must explain the main reasons and the logic, not only the score.
- **Objection and contest:** people contesting a decline; this needs a fast route to a human.
- **Erasure:** declined applicants asking for deletion, in tension with complaint handling and AML retention.

**Controller / processor split:**
| Entity | Role |
|---|---|
| FlexKrediet | **Controller** (decides purposes and means) |
| US ML platform | **Processor** (runs the model on FlexKrediet's instructions) |
| Cloud hosting | Sub-processor |
| Open-banking provider | Independent controller for the account connection (regulated payment service) |
| Credit bureau | Independent controller |

**DPA needed?** Yes, an **Art. 28 DPA with the ML platform** (and its sub-processors listed). Data-sharing agreements with the open-banking provider and the credit bureau (controller-to-controller, not Art. 28).

## Phase 2 · Section C: Law stacking
- **AI Act:** **high-risk** (Annex III 5(b)). Adds what GDPR does not: risk management, data governance and bias testing, technical documentation, logging, human oversight design, conformity assessment and registration (provider); **fundamental rights impact assessment** (Art. 27) and the right to an explanation (Art. 86) for the deployer. The FRIA and the DPIA can be prepared together.
- **ePrivacy:** applies to the application website and app. Analytics cookies, tracking pixels and **device fingerprinting for fraud** need consent unless strictly necessary; ePrivacy consent overrides GDPR's legitimate-interests option for this layer. Security-related fingerprinting may be "strictly necessary": **TBD – legal review**.
- **Data Act:** **N/A** (no connected products or cloud-switching data). The future EU Financial Data Access rules (FIDA) would be relevant for open banking once adopted.

---

# Part 2 · Client recommendation memo

**To:** CTO and Legal, FlexKrediet B.V. · **From:** Elif Yurdakul · **Re:** GDPR review of the AI credit-scoring system

**Bottom line: Go with conditions.** The system can be lawful, but today it makes automated credit decisions on sensitive financial data without the safeguards GDPR and the AI Act require.

**What we found.** Your scoring model is high-risk under the AI Act and, under GDPR, combines almost every risk factor: credit decisions with a legal effect, 12 months of bank transactions that can reveal health, religion or union membership, data matched from three sources, and a US-owned ML vendor. A data protection impact assessment is mandatory. The biggest gap is that approvals are fully automated and declines are driven by the score, while applicants have no clear way to get an explanation or contest the result.

**Top three actions, in order:**
1. **Before any live data flows:** sign an Art. 28 data processing agreement with the ML platform, confirm its EU–US Data Privacy Framework certification (or put Standard Contractual Clauses and a transfer impact assessment in place), and filter transaction categories that reveal health, religion, union or political data before the model sees them.
2. **Before launch:** complete a DPIA together with the AI Act fundamental rights impact assessment, including bias testing and a legitimate-interests assessment for model training.
3. **At launch:** give every declined applicant the main reasons, a route to a human review and a way to contest; update the privacy notice to cover open-banking data, scoring and model training; set deletion rules (raw transactions within 30 days).

**Residual risks (even with these steps):**
- **Hidden proxies:** the model can still learn indirect signals for protected traits (e.g. postcode, merchant types). Bias testing reduces this but cannot eliminate it.
- **US access:** with a US-owned vendor, a legal challenge to the transfer framework could force a fast vendor change.
- **"Human review" in name only:** under time pressure, credit officers may simply confirm the score. That would weaken your Art. 22 position.

This memo is not legal advice; the TBD items in the worksheet need confirmation by your DPO and counsel.

*(≈ 370 words)*

---

# Part 3 · Partner swap (Phase 4)
**Pieter's scenario:** he carried forward **my Case 2** from the EU AI Act lab: AI CV screening for a logistics company in Germany and Poland with a US vendor (fictional client *Kranich Logistik GmbH*; AI Act high-risk, Annex III 4(a)). So we each audited the other's high-risk case: I took his lender, he took my recruiter.

*Reviewed from Pieter's `lab_proof.md` summary of his worksheet and memo.*

**My review of Pieter's memo:**
| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Go with conditions, but not in the current design" is clear and honest: the project can go ahead, the auto-rejection cannot. |
| Lawful basis selection is justified | **2** | Strong that he states there is **no valid basis for auto-rejection as designed** and uses consent only for the talent pool. Weaker point: legitimate interests for scoring and for the "top performer" profiles is left as TBD. Those profiles reuse **existing employees'** data for a new purpose, so a compatibility test (Art. 6(4)) and informing employees are needed, not only an LIA. |
| Top actions are specific and sequenced | **3** | Works council → DPA + DPIA + bias test → human sign-off replacing auto-rejection. The order is right: in Germany nothing can launch without works council agreement. |
| Residual risks are named honestly | **3** | Rubber-stamping, hidden bias from top-performer data, US transfer: realistic and not softened. |
| Law stacking is addressed (AI Act / ePrivacy) | **3** | AI Act deployer duties, DPF/SCC with the pending CJEU appeal, plus German works council law (BetrVG §§ 87, 95), which goes beyond the template. ePrivacy is light here, which fits: an applicant portal has few tracking issues. |

**As the client (Kranich Logistik):** *We accept the recommendation, with one concern. Using five years of our own employees' performance data to build "top performer" profiles feels risky for employee trust and may teach the model our past hiring bias. Please rethink that section: can the scoring work from the job description and published criteria alone, and what would we lose without the profiles?*

**Debrief: where we agreed**
- **DPIA:** both mandatory, both 7 of 9 EDPB criteria.
- **Art. 22:** both triggered, both citing the SCHUFA judgment (C-634/21), and both choose real human review over relying on Art. 22(2)(a) alone. Pieter documents the alternative route as defensible, which is fair.
- **Transfers:** both EU–US Data Privacy Framework if the vendor is certified, Standard Contractual Clauses as fallback.
- **Art. 9:** both see inference as the main risk (transactions for me; photos, health mentions and proxies for him).

**Debrief: where we diverged, and which reading is stronger**
| Topic | Elif (lender) | Pieter (recruiter) | Stronger reading |
|---|---|---|---|
| Main lawful basis | Legal obligation + contract (credit law requires an assessment) | Pre-contract steps + legitimate interests | **Both right for their case:** a lender is legally required to assess creditworthiness; an employer has no such duty, so recruitment rests on pre-contract steps and an LIA. |
| AI Act application date | High-risk obligations from 2 August 2026 (Art. 113) | From **2 December 2027**, citing Reg. (EU) 2026/1744 | **Pieter's, if confirmed.** He cites a later amending regulation; my date comes from the original text. I need to verify it and update my memo and the earlier approval pack. ⚖️ |
| Sector law | Consumer credit, payment services (PSD2) | German works council law, unsettled § 26 BDSG after CJEU C-34/21 | Not a disagreement: each case brings its own sector rules. Pieter's works council point is a hard launch blocker I would also have flagged for the original case. |
| Gap I would add to Pieter's audit | — | Polish employment law limits what data employers may request from applicants; the Polish entity may be a separate controller | Pieter flagged the entity question himself; the Polish data limits are worth one line. |

**What the swap showed:** reviewing my own case through Pieter's eyes, the auto-rejection after one week is the part I wrote as an innocent detail; he correctly made it the centre of the GDPR analysis.

---

# Reinforce

**DPIA outline (P1, credit decision):**
1. *Description:* data flows from form, bank and bureau → features → score → decision; actors and vendors.
2. *Necessity and proportionality:* why 12 months of transactions (vs. 3?), why automated approvals, retention periods, lawful bases.
3. *Risks:* wrongful decline, discrimination via proxies, Art. 9 inference, US access, data breach of bank data, ineffective human review.
4. *Mitigation:* category filtering, bias testing, human review of declines, explanations and contest route, encryption and access control, DPA and SCCs, deletion rules.

**One DPA clause to insist on:** *"The processor shall not use FlexKrediet's personal data, or models trained on it, to train or improve its own or other customers' models."* Why: ML vendors often reserve the right to use customer data for "service improvement", which would turn them into a controller for a new purpose and break purpose limitation.

**If FlexKrediet also serves UK customers:** the bottom line stays **go with conditions**, but three things change: (1) UK GDPR applies alongside EU GDPR; transfers from the UK to the US use the UK's own route (the UK–US "data bridge" or the UK transfer addendum). (2) The UK has reformed its automated-decision rules (Data (Use and Access) Act 2025), allowing automated decisions more broadly with safeguards, but stricter limits remain where special-category data is involved, so the Art. 9 filtering matters even more. ⚖️ (3) The EU AI Act does not apply to UK-only processing; the FCA's Consumer Duty and fair lending expectations take its place.

---

# Stretch: data protection by design checklist (P1, credit decision)

| Item | Status | Note |
|---|---|---|
| Data minimisation | **Fail** | 12 months of full transactions collected; unclear if fewer months or aggregated features would do |
| Purpose binding | **Unknown** | No technical separation yet between data used for decisions and for model training |
| Access controls | **Unknown** | Not specified who can see raw transactions (credit officers? data scientists? vendor support?) |
| Retention enforcement | **Fail** | No automated deletion of raw transactions or declined applications defined |
| Subject rights workflow | **Fail** | No process to explain a decline or handle a contest within 30 days |
| Incident response | **Unknown** | No documented process for detecting and reporting a breach within 72 hours, incl. the vendor's duty to notify |

---

## Lab evidence

- **Input:** Pieter's Case 2 from the EU AI Act lab ("an online lender wants to approve or decline loans with a model built on open-banking data"), expanded into the fact pattern above.
- **Evidence:** the audit worksheet (Sections A–C).
- **Final output:** the client recommendation memo (Part 2).
- **Failure or limitation:** Pieter's original case was one sentence. The details (company, volumes, the US ML platform, automated approvals under €5,000) are my assumptions to make the audit concrete, so the conclusions hold for this fact pattern, not necessarily for Pieter's intended scenario. Several lawful-basis questions (PSD2 explicit consent vs. GDPR, model training, bias testing under AI Act Art. 10(5)) cannot be settled without legal review and are marked TBD.