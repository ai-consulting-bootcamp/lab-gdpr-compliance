# Reinforce — DPIA outline, DPA clause, and the UK question

Companion to [`gdpr-audit-pack-ugo-ahukannah.md`](./gdpr-audit-pack-ugo-ahukannah.md).

## 1. DPIA outline — automated scoring, ranking and rejection

The most sensitive processing in scope. Not a full DPIA; the sections it needs and what goes in each.

**A. Description of the processing.** Applicants upload a CV and complete a short skills assessment;
the vendor's model scores both against the job description and assigns a tier. ~400 applicants a
week, ~20,000 a year, EU/EEA-wide. Data: identity and contact, unstructured CV text, assessment
answers, derived score and tier. Training set: five years of the chain's own hiring decisions and
one-year retention outcomes. Recipients: the US-based vendor as processor and its undisclosed
infrastructure sub-processors. Transfers: EEA → US on the main processing path. Retention: currently
undefined. Automated decision-making: yes as designed.

**B. Necessity and proportionality.** The business interest is real — two staff cannot triage 400
applications a week, and no less intrusive method achieves it at that volume. Proportionality is
where it strains: ingesting the *entire* CV free text, including photograph and nationality, exceeds
what the purpose requires, and the automated rejection is not necessary to the triage at all — the
model can rank without also issuing the decision. Necessary in principle, disproportionate as
configured.

**C. Risk identification** — to applicants' rights, not to the business:

| Risk | Likelihood | Severity | Why |
|---|---|---|---|
| Discriminatory exclusion via proxies for ethnicity, health, age | High | High | Free-text CVs carry proxies; model trained on who was historically hired and who stayed |
| Exclusion with no human involvement (Art 22) | High as designed | High | Rejection may send unreviewed; access to employment is a significant effect |
| Inability to explain a rejection (Art 15(1)(h)) | High | Medium | Controller holds no logic information; vendor not obliged to supply it |
| Loss of control over data transferred to the US | Medium | Medium | No confirmed transfer mechanism; sub-processors undisclosed |
| Excessive retention | Medium | Medium | No schedule, no automated deletion |
| Function creep into employee monitoring | Medium | High | Same vendor, same data, adjacent use case |

**D. Measures.** Mandatory human review before any rejection, with recorded override capability;
feature minimisation — strip photographs and fields carrying protected proxies before ingestion;
bias testing across demographic groups pre-launch and on every model version, using the **Art 4a** basis
(inserted into the AI Act by Regulation (EU) 2026/1744, in force 27 July 2026) for processing
special-category data where necessary for bias detection and correction; a contractual
right to logic information sufficient to answer Art 15(1)(h); an Art 28 DPA with full sub-processor
disclosure and a verified transfer mechanism; a per-jurisdiction retention matrix with automated
deletion; and a documented scope boundary requiring a fresh DPIA before any extension to employee
monitoring.

**Residual risk after measures: medium.** Proxy discrimination cannot be fully engineered out, which
is why the ongoing monitoring commitment matters more than the pre-launch test.

## 2. One DPA clause I would insist on, and why

Beyond the standard Article 28 terms:

> **Explainability support.** On the controller's request, and within five working days, the
> processor shall provide information sufficient for the controller to satisfy Article 15(1)(h) in
> respect of any individual decision — the meaningful information about the logic involved, and the
> significance and envisaged consequences of the processing for that data subject — including the
> features that materially contributed to the tier assigned. This obligation survives termination
> for the duration of the controller's retention period.

**Why this one.** Every other obligation in the audit can be discharged by the controller acting
alone: mandate human review, write the notice, set retention, run the DPIA. **The right of access to
the logic is the only one the controller structurally cannot satisfy without the vendor** — the
model is the vendor's, and a standard DPA obliges them to *assist* with data subject requests
without ever defining what assistance means for an opaque model. The gap surfaces when the first
applicant asks why they were rejected, by which point the leverage to negotiate is gone: the system
is live and the contract signed. The five-day SLA matters because the controller's own Art 12(3)
clock is one month, and a vendor with no deadline will consume all of it.

Runner-up for the same section: an express prohibition on the vendor using client candidate data to
train or improve its general model — that is what converts the vendor from processor into a
controller in its own right.

## 3. If the client also serves UK data subjects

UK GDPR and the Data Protection Act 2018 would apply in parallel for UK applicants — a second
compliance stack, not an extension of the first. Concretely:

- **UK representative** under UK GDPR Art 27 if the chain has no UK establishment.
- **Transfers need UK paperwork.** EU SCCs do not cover UK transfers: the UK requires its own
  International Data Transfer Agreement, or the UK Addendum to the EU SCCs, plus a UK transfer risk
  assessment. The UK Extension to the Data Privacy Framework is the alternative, and the vendor's
  certification must specifically cover it.
- **Automated decision-making has diverged.** UK reform has moved the Article 22 equivalent away
  from a general prohibition toward a permit-with-safeguards model for decisions not involving
  special-category data. **Verify against the current statutory text and ICO guidance before using
  this with a client** — it is the fastest-moving part of this answer, and it moves opposite to the EU.
- **ICO employment-practices guidance** is more prescriptive than most EU authorities on retention
  of applicant data.

**Does the bottom line change? No — and that is the point to make to the client.** It stays **go with
conditions**, and action 1 stays mandatory human review, because the EU analysis alone requires it.
Even if the UK route would tolerate a more automated flow, running two rejection workflows split by
applicant nationality is operationally absurd and would itself become a discrimination story. Build
to the stricter standard once. What genuinely changes is action 3: the transfer paperwork doubles,
and a UK-specific mechanism must be in place before any UK applicant's data reaches the US.
