# GDPR Audit Pack — Ugo Ahukannah

**Scenario:** Vandermeer Retail CV screening · shared fact pattern:
[`fact-pattern-cv-screening-shared.md`](./fact-pattern-cv-screening-shared.md)
**Carried forward from:** EU AI Act lab, high-risk case (Annex III(4), employment)
**Partner:** Vittal · **Basis:** Regulation (EU) 2016/679 (GDPR), with AI Act and ePrivacy cross-checks

> Consulting-level audit, not legal advice. Items marked **TBD — legal review** are flagged
> deliberately rather than guessed.

---

## 1. Recognize — what is actually in the data

**Categories present:** identity and contact data; full unstructured CV text (education,
employment history, references, and commonly a photograph, nationality, languages and personal
interests); structured pre-screening assessment answers; derived fit scores and tiers; and, in the
training set, five years of prior applicants plus one-year retention outcomes for those hired.

**Special-category data (Art 9) — not collected deliberately, but present and inferable.** A free-text
CV routinely reveals or supports inference of: ethnic origin (name, photograph, nationality),
religious belief (faith schools, religious volunteering), trade union membership (roles held),
and health (employment gaps, references to adjustments or illness). The risk is not only that
such data sits in the file — it is that the **model may use proxies for it** when ranking, which
converts an incidental disclosure into a discriminatory decision. Treat Article 9 as engaged for
risk purposes and assume no comfortable Article 9(2) exception exists.

**Border crossing:** yes. Data is hosted in the EU, but the vendor's **US parent performs
second-line support and model monitoring**, and remote access from the US to EU-stored personal
data is itself a restricted transfer under Chapter V. This is the transfer that clients most often
miss, because nothing is "sent" anywhere.

---

## 2. Apply — audit worksheet

### Section A — Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | Identity and contact; unstructured CV text; photograph (where supplied); assessment answers; derived fit score and tier; historical hiring decisions and one-year retention outcomes for past hires |
| **Sources** | Directly from the applicant via the careers portal; internally from the chain's own five years of ATS and HR records for the training set |
| **Purpose 1 — process the application for the advertised vacancy** | Lawful basis: **Art 6(1)(b)**, steps prior to entering a contract at the data subject's request. Justification: the applicant asked to be considered for a role, and handling their application is what that request consists of |
| **Purpose 2 — automated scoring and ranking against the job description** | Lawful basis: **Art 6(1)(f)**, legitimate interests, with a documented LIA. Justification: triaging 400 applications a week with a two-person team is a real business interest, but this goes beyond what is strictly necessary to process the application, so it cannot ride on 6(1)(b). **See the LIA note below — the balancing test fails as currently designed** |
| **Purpose 3 — training and improving the model on five years of historical hiring and retention outcomes** | **TBD — legal review.** Provisionally Art 6(1)(f), but this is a *secondary* purpose: the data was collected to fill past vacancies, not to build a model. Requires a compatibility assessment under **Art 6(4)** before it can proceed on legitimate interests, and the retention-outcome data concerns employees, where power imbalance makes consent unusable |
| **Purpose 4 — retaining unsuccessful applications for future vacancies (talent pool)** | Lawful basis: **Art 6(1)(a)**, consent. Justification: keeping a CV past the vacancy it was submitted for serves the employer, not the applicant, and consent here is genuinely optional and refusable |
| **Purpose 5 — defending discrimination or employment claims** | Lawful basis: **Art 6(1)(f)**, legitimate interests, or **Art 6(1)(c)** where national law imposes a limitation period. Drives the retention floor rather than the ceiling |
| **Retention — P1/P2** | Application data and derived scores: **4 weeks after the procedure closes** (Dutch AP guidance), extendable to **1 year only with the applicant's consent**. Belgium follows comparable practice — confirm per jurisdiction |
| **Retention — P3** | Training set retained for the life of the deployed model version, then deleted or irreversibly anonymised. Requires a version-linked deletion policy that does not currently exist |
| **Retention — P4** | 1 year from consent, renewable only by fresh consent |
| **Retention — logs** | ≥6 months of automatic logs are required by **AI Act Art 12** — see the stacking conflict in Section C |
| **Recipients and sub-processors** | Kestrel HR Technologies (Ireland) — processor operating the screening tool; Kestrel's **US parent** — sub-processor providing second-line support and model monitoring; the chain's ATS and transactional email provider — processors delivering rejection notices |
| **International transfers and mechanism** | US parent access to EU-stored candidate records = restricted transfer. Mechanism: **EU–US Data Privacy Framework** if and only if the US entity is certified *and* its certification covers **HR data**, which is a distinct DPF commitment; otherwise **SCCs plus a documented transfer impact assessment**. **TBD — legal review**: verify certification scope before launch rather than assuming the group's general certification suffices |

**Legitimate interests assessment (Purpose 2), three steps:**
*Purpose* — triage application volume the HR team demonstrably cannot process manually.
*Necessity* — defensible: 400 applications a week against two staff is a genuine constraint, and
no less intrusive method achieves the same triage at that volume.
*Balancing* — **currently fails.** Applicants would not reasonably expect a rejection issued with
no human involvement, they are in a position of power imbalance, and the consequence is exclusion
from employment. The balance tips back only once human review of every rejection is mandatory and
candidates are told AI is used. The LIA is passable *after* the conditions in the memo, not before.

### Section B — Risk and rights

**1. Special-category data (Art 9).** Present and inferable rather than deliberately collected —
see section 1. No Article 9(2) exception fits comfortably: explicit consent is unreliable in a
recruitment power imbalance, and none of the employment-law or public-interest gateways cover
model training. Mitigation is technical, not paperwork: strip photographs before ingestion,
exclude fields that carry proxies, and test outputs for disparate impact across protected groups.

**2. Automated decision-making (Art 22).** **Yes, as currently designed.** A rejection email that
issues with no human involvement is a decision based solely on automated processing producing
legal or similarly significant effects. Legitimate interests is **not** a gateway under Art 22(2)
— the only routes are contract necessity, authorisation in law, or explicit consent, and none is
sound here. The safeguard that actually works is to stop Article 22 applying: insert **meaningful**
human review before any rejection sends. Meaningful is the operative word — EDPB guidance is clear
that a reviewer who rubber-stamps the model does not count, and a recruiter who only ever opens the
strong-fit folder is not reviewing the rejections at all. Where Art 22 does apply, Art 22(3)
requires human intervention, the right to express a point of view, and the right to contest.

**3. DPIA — required, not optional.** Article 35(3)(a) makes it mandatory outright: systematic and
extensive evaluation of personal aspects based on automated processing, including profiling, on
which decisions producing legal or similarly significant effects are based. Against the EDPB's nine
criteria, **six or seven apply** where two are sufficient: evaluation and scoring; automated
decision-making with legal or similarly significant effect; sensitive or highly personal data
(inferable Art 9, plus the employment context); large-scale processing (~20,000 applicants a year);
matching and combining datasets (application data joined to retention outcomes); vulnerable data
subjects (applicants face the same power imbalance the EDPB recognises for employees); and
innovative use of new technology. It must be completed **before** processing begins.

**4. Data subject friction points.** *Access (Art 15)* — applicants will ask for their score and,
under Art 15(1)(h), meaningful information about the logic involved; the vendor must be
contractually obliged to supply it, or the controller cannot answer. *Erasure (Art 17)* — deleting
an application is straightforward; removing that person's influence from an already-trained model
is not, and the honest answer is retraining on a cleaned set. *Objection to profiling (Art 21)* —
because Purpose 2 runs on legitimate interests, an objection puts the burden on the controller to
show compelling grounds, which is difficult mid-recruitment. *Rectification* of an inferred tier
is also likely, and there is currently no workflow for it.

**5. Controller / processor split.**
- **Vandermeer Retail — controller.** Decides that applicants will be screened, for what purpose, and on what data.
- **Kestrel HR Technologies (IE) — processor** for the screening service. **Watch the boundary:** if Kestrel reuses client data to improve its own general-purpose model, it acts as a **controller** for that purpose and needs its own lawful basis. Either forbid it in the contract or document it properly; silence is the dangerous option.
- **Kestrel's US parent — sub-processor**, engaged for second-line support and model monitoring, requiring Art 28(4) flow-down and its own transfer mechanism.
- **ATS and email provider — processors** for delivery of outcomes.

**6. DPAs required.** Article 28 DPA with **Kestrel**, with authorisation and flow-down for the US
parent as sub-processor, plus the Chapter V transfer mechanism; DPAs with the **ATS** and **email
provider**. No DPA is needed for the chain's own internal HR use — that is controller-side processing.

### Section C — Law stacking

**AI Act cross-check.** Tier: **high-risk, Annex III(4)** (employment, recruitment and selection).
It adds obligations GDPR does not cover: a lifecycle risk management system (Art 9), data
governance and bias examination (Art 10), technical documentation (Art 11 + Annex IV), automatic
logging (Art 12), instructions for use (Art 13), human oversight *by design* (Art 14), accuracy and
robustness evidence (Art 15), conformity assessment by internal control under **Annex VI** — no
notified body for Annex III(4) — registration (Art 49), and post-market monitoring with incident
reporting on a 15/10/2-day clock (Arts 72–73). **No FRIA**: a private retailer hiring for itself is
not a public body, not a private entity providing a public service, and not an Annex III 5(b)/(c)
deployer. Two interactions worth naming: the AI Act's **Art 12 logging duty (≥6 months)** runs
directly against GDPR's storage limitation and the 4-week Dutch retention norm, so logs must be
scoped to what the AI Act requires and separated from the candidate record; and the Digital
Omnibus's **new Art 4a** now provides a legal basis for processing special-category data for bias
detection and correction, which removes the Article 9 obstacle that used to block exactly the
fairness testing this system needs.

**ePrivacy check.** Yes — the careers portal serves cookies and any analytics or tracking pixels on
it require **prior consent** under Art 5(3) ePrivacy, and that consent requirement **overrides**
GDPR's flexibility: legitimate interests cannot substitute for it, regardless of how the subsequent
processing is justified. Strictly necessary cookies are exempt; analytics are not. If the
assessment step ever adds device fingerprinting or proctoring, the same consent gate applies.

**Data Act check.** N/A — no connected-product or cloud-switching data in scope. Flag only if the
chain later feeds in-store IoT or workforce-device telemetry into the same stack.

---

## 3. Integrate — client recommendation memo

**To:** Vandermeer Retail — Legal and CTO · **From:** Ugo Ahukannah · **Re:** CV screening tool, privacy assessment

**Bottom line: go with conditions.** The tool is lawful to deploy, but not as currently
configured for launch — the automated rejection step is the problem, and it is fixable.

As designed, rejection emails can issue without anyone reading them. That makes this a solely
automated decision with a significant effect on the applicant, and legitimate interests — the basis
you would rely on for the ranking — is not a permitted basis for that kind of decision. Your
two-person team is a real constraint and the triage case is sound; the exposure sits at the bottom
of the ranking, not the top.

**Three actions, in order.**

1. **Make human review mandatory before any rejection sends — before launch.** A recruiter must see
   and be able to overturn every rejection, and it has to be the real workflow, not a permission
   nobody uses. This removes the Article 22 exposure and closes the human oversight gap the AI Act
   review already flagged.
2. **Complete a DPIA before first processing.** Mandatory here, not discretionary: the system
   evaluates people extensively and automatically, with significant effects. Doing it after go-live
   does not cure the breach.
3. **Fix the vendor paperwork before any data flows.** An Article 28 agreement with Kestrel,
   explicit authorisation of the US parent as sub-processor, and a verified transfer mechanism for
   US support access — confirm their Data Privacy Framework certification covers HR data, or fall
   back to standard contractual clauses with a transfer impact assessment. Add a clause barring
   reuse of your candidate data to train Kestrel's general model.

**Residual risks, disclosed.** CV free text carries proxies for ethnicity, religion, health and
union membership; you can strip photographs and test for disparate impact, but you cannot stop a
model finding proxies, so bias testing has to be continuous. Erasure requests are only partly
satisfiable — deleting an application does not remove its influence on a model already trained on
it, and honouring the right properly means retraining on a cleaned set. And reusing five years of
past applications as training data changes the purpose they were collected for; if the
compatibility assessment fails, that dataset needs a different basis or has to go.

**On the six weeks:** actions 1 and 3 and the candidate disclosure are achievable, and the DPIA is
if you start now. Full AI Act conformity work is not, and does not need to be — those obligations
apply from 2 December 2027.

_(memo body: 406 words — lab requires 300–400)_

---

## 4. Verify — peer review exchange

**My memo reviewed by Vittal (he acts as client):** _pending._

**My review of Vittal's memo, against the lab rubric:** _pending his memo._

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

## 5. Debrief — agreement and divergence

_Pending the swap. To record: where our two audits agreed on lawful basis and DPIA need, where
they diverged, and for each divergence which reading is stronger and why._
