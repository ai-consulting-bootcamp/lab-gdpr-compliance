# Shared fact pattern — AI-assisted CV screening

**Agreed common ground for:** Ugo Ahukannah and Vittal Navale · **Lab:** Same product, privacy lens
**Authored by:** Vittal · **Agreed by:** Ugo, 19 August 2026 (Slack) · **Status:** final — both audits run on this text

## Transition note — carrying the case forward (Option A)

This is the **retail CV screening** case from the EU AI Act lab, now examined through the privacy
lens. Under the AI Act it classifies as **high-risk, Annex III(4)** (employment: recruitment and
selection), and the AI Act review issued *approve with controls*. It is the most interesting of
our cases for GDPR purposes because that review already surfaced a privacy problem the AI Act does
not itself resolve: the automated rejection step is an **Article 22 GDPR** issue *today*, while the
Annex III obligations do not apply until **2 December 2027**. Two regimes, same system, different
clocks — which is exactly the parallel-not-sequential pattern this lab is teaching.

## Fact pattern (agreed text)

> The client is a national retail chain (~15,000 employees across EU/EEA stores and distribution
> warehouses) whose two-person HR team receives roughly 400 CVs a week for store and warehouse
> roles. They are piloting an AI-based CV screening tool, licensed from a US-based HR-tech vendor,
> that ingests each resume plus a short online skills assessment and scores the candidate against
> the job description. Candidates are auto-sorted into "strong fit," "maybe," or "not a fit" tiers.
> Recruiters currently only open the "strong fit" folder before making outreach calls; "not a fit"
> candidates receive an automated rejection email with **no confirmed human review step**. The
> scoring model was trained on five years of the client's historical hiring and retention data (who
> was hired, and who stayed past one year). Data subjects are job applicants located in the EU/EEA;
> the vendor processes and stores assessment and scoring data on US infrastructure. HR wants to
> launch within six weeks and has not yet decided whether a recruiter must review "not a fit"
> outcomes before rejection goes out.

## Personal data in scope

| Category | Detail |
|---|---|
| Identity and contact | Name, email, phone, address |
| Application content | Full CV free text: education, employment history, references; commonly also photograph, nationality, languages, personal interests |
| Assessment data | Answers and scores from the short online skills assessment |
| Inferred/derived | Fit score and tier label, plus whatever the model derives from unstructured CV text |
| Employee data (training set) | Five years of historical hiring decisions and one-year retention outcomes |

**Data subjects:** job applicants in the EU/EEA, plus former and current employees whose hiring and
retention records constitute the training data.

**Automated decision-making:** yes as currently designed — rejection emails may issue with no
confirmed human review, a decision producing legal or similarly significant effects.

**Key facts that drive the audit:** the vendor is **US-based and stores data on US infrastructure**
(so this is a straightforward Chapter V transfer, not merely remote access); the applicant
population is **EU/EEA-wide**, so no single national retention norm governs; and the human-review
question is **explicitly undecided**, which is the crux of the Article 22 analysis.
