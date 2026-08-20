# GDPR Audit Pack - Ugo Ahukannah

**Lab:** Same product, privacy lens · **Partner:** Vittal Navale · **Basis:** Regulation (EU) 2016/679
(GDPR), with EU AI Act and ePrivacy cross-checks
**Scenario carried forward (Option A):** the retail CV screening case from the EU AI Act lab,
classified there as high-risk, Annex III(4).

> Consulting-level audit, not legal advice. Items marked **TBD — legal review** are flagged
> deliberately rather than guessed.

## Fact pattern (Phase 1)

Agreed with my partner before either audit began; full version, including the transition note, in
[`fact-pattern-cv-screening-shared.md`](./fact-pattern-cv-screening-shared.md).

A national retail chain (~15,000 employees across EU/EEA stores and distribution warehouses) has a
two-person HR team receiving roughly 400 CVs a week for store and warehouse roles. It is piloting an
AI CV screening tool, licensed from a **US-based HR-tech vendor**, that ingests each resume plus a
short online skills assessment and scores the candidate against the job description, sorting them
into "strong fit", "maybe" or "not a fit". Recruiters open only the "strong fit" folder; "not a fit"
candidates receive an automated rejection email with **no confirmed human review step**. The model
was trained on five years of the chain's own hiring and retention data. Data subjects are job
applicants located in the **EU/EEA**; the vendor **processes and stores assessment and scoring data
on US infrastructure**. HR wants to launch within six weeks and has not decided whether a recruiter
must review "not a fit" outcomes before rejection is sent.

---

# Audit worksheet

## CFU 1 — Recognize: what is actually in the data

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

**Border crossing:** yes, and not marginally. The vendor is **US-based and processes and stores
assessment and scoring data on US infrastructure**, so applicant data leaves the EEA at the point
it reaches the vendor — this is a Chapter V restricted transfer on the main processing path, not an
incidental support-access edge case. Every CV screened crosses the border.

---

## CFU 2 — Apply: the worksheet (Phase 2)

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
| **Retention — P1/P2** | Application data and derived scores: delete promptly after the procedure closes, retaining only where a documented claims-defence justification applies. **No single figure works EEA-wide** — supervisory expectations range from roughly 4 weeks by default (Dutch AP) to several months where discrimination-claim limitation periods justify it, so the chain needs a per-jurisdiction retention matrix rather than one number. Anything beyond the procedure itself needs either that justification or the applicant's consent |
| **Retention — P3** | Training set retained for the life of the deployed model version, then deleted or irreversibly anonymised. Requires a version-linked deletion policy that does not currently exist |
| **Retention — P4** | 1 year from consent, renewable only by fresh consent |
| **Retention — logs** | ≥6 months of automatic logs are required by **AI Act Art 12** — see the stacking conflict in Section C |
| **Recipients and sub-processors** | The **US-based HR-tech vendor** — processor operating the screening tool and hosting the data; that vendor's own cloud and infrastructure sub-processors — **TBD — legal review**, the chain cannot assess the transfer chain without full sub-processor disclosure; internally, the two-person HR team and hiring recruiters; the chain's ATS and transactional email provider for delivering outcomes |
| **International transfers and mechanism** | EEA → US on the main processing path: the vendor stores and processes assessment and scoring data on US infrastructure. Mechanism: **EU–US Data Privacy Framework** only if the vendor is certified *and* its certification covers **HR data**, which is a distinct DPF commitment rather than an automatic part of certification; otherwise **SCCs plus a documented transfer impact assessment** post-*Schrems II*. Sub-processor transfers need the same treatment. **TBD — legal review** — no mechanism is confirmed today, and nothing may flow until one is |

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
- **The retail chain — controller.** Decides that applicants will be screened, for what purpose, and on what data.
- **The US-based HR-tech vendor — processor** for the screening service. **Watch the boundary:** if the vendor reuses client data to improve its own product across other customers, it acts as an independent (or joint) **controller** for that purpose and needs its own lawful basis. Either forbid it in the contract or document it properly; silence is the dangerous option.
- **The vendor's cloud and infrastructure providers — sub-processors**, requiring Art 28(4) authorisation and flow-down, and their own transfer treatment. The chain currently has no disclosure of who they are.
- **ATS and email provider — processors** for delivery of outcomes.

**6. DPAs required.** Article 28 DPA with the **screening vendor** before any live candidate data
reaches it, covering processing instructions, sub-processor authorisation and disclosure, security
measures, and the Chapter V transfer terms; DPAs with the **ATS** and **email provider**. No DPA is
needed for the chain's own internal HR use — that is controller-side processing.

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
directly against GDPR's storage limitation and the short retention expected for unsuccessful
applications, so logs must be scoped to what the AI Act requires and separated from the candidate
record; and the Digital
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


---

# Client recommendation memo

_Phase 3 · CFU 3 Integrate. 300–400 words as the lab requires._

**To:** Retail chain — Legal and CTO · **From:** Ugo Ahukannah · **Re:** CV screening tool, privacy assessment

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
3. **Fix the vendor paperwork before any data flows.** Every CV screened crosses to US
   infrastructure: an Article 28 agreement, full sub-processor
   disclosure, and a verified transfer mechanism — confirm the vendor's Data Privacy Framework
   certification actually covers HR data, or fall back to standard contractual clauses with a
   transfer impact assessment. Add a clause barring reuse of your candidate data to improve the
   vendor's own product.

**Residual risks, disclosed.** CV free text carries proxies for ethnicity, religion, health and
union membership; you can strip photographs and test for disparate impact, but you cannot stop a
model finding proxies, so bias testing has to be continuous. Erasure requests are only partly
satisfiable — deleting an application does not remove its influence on a model already trained on
it, and honouring the right properly means retraining on a cleaned set. And reusing five years of
past applications as training data changes the purpose they were collected for; if the
compatibility assessment fails, that dataset needs a different basis or has to go.

**On the six weeks:** actions 1 and 3 are achievable, and the DPIA is if you start now. Full AI
Act conformity work is not, and need not be — those obligations apply from 2 December 2027.

_(memo body: 399 words — lab requires 300–400)_

---

---

_Phase 4 peer review and the CFU 5 debrief are held separately in
[`From_Ugo_peer-review-and-debrief-ugo-ahukannah.md`](./From_Ugo_peer-review-and-debrief-ugo-ahukannah.md). This
document stays what a client would actually receive: the worksheet behind the advice, and the advice
itself._
