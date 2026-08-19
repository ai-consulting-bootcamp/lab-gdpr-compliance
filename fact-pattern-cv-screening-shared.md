# Shared fact pattern — CV screening (Vandermeer Retail)

**Agreed common ground for:** Ugo Ahukannah and Vittal · **Lab:** Same product, privacy lens
**Carried forward from:** the EU AI Act lab, Vittal's Case 2 (retail CV screening)

> Proposed by Ugo. Details not fixed by the original brief are marked **[assumed]** — Vittal,
> change anything here before we start our audits, so long as we both work the identical version.

## Transition note — why this case

We are carrying forward the **retail CV screening** case. Under the AI Act it classified as
**high-risk, Annex III(4) (employment: recruitment and selection)**, and was approved with
controls. It is the most interesting of our eight cases for GDPR purposes because the AI Act
analysis already surfaced a live privacy problem that the AI Act itself does not resolve: the
automated rejection emails are an **Article 22 GDPR** issue *today*, whereas the Annex III
obligations do not apply until 2 December 2027. It is the clearest example of the two regimes
running in parallel rather than in sequence.

## Fact pattern

Vandermeer Retail **[assumed name]** is a national grocery and general-merchandise chain
operating around 180 stores across the Netherlands and Belgium **[assumed]**, with roughly 6,000
employees. It receives about 400 applications a week — some 20,000 a year — for store and
warehouse roles, screened by a two-person HR team that cannot keep up. Applicants are located in
the EU/EEA **[assumed: no UK or third-country applicants in the base case]**.

The system scores each applicant's CV and a short structured assessment against the job
description, returning a ranked tier: strong fit / maybe / not a fit. It was trained on five
years of the chain's own hiring decisions plus one-year retention outcomes for those hired.
Recruiters in practice open only the strong-fit folder; candidates in the lower tiers receive an
automated rejection email, and it is **still undecided** whether a recruiter must review a
"not a fit" result before that email sends. HR wants to launch in six weeks.

The tool is licensed from **Kestrel HR Technologies [assumed]**, an HR-tech SaaS vendor
incorporated in Ireland, which hosts the application on EU infrastructure but uses a **US-based
parent company for second-line technical support and model monitoring [assumed]** — so support
staff outside the EU can access candidate records when troubleshooting.

## Personal data in scope

| Category | Detail |
|---|---|
| Identity and contact | Name, address, email, phone, date of birth |
| Application content | Full CV free text: education, employment history, references; frequently also photograph, nationality, languages, personal interests |
| Assessment data | Structured answers to a short pre-screening questionnaire |
| Inferred/derived | Fit score and tier, plus whatever the model derives from unstructured CV text |
| Employee data (training set) | Five years of past applicants and hires, including one-year retention outcome per hire |

**Data subjects:** job applicants (external), plus former and current employees whose historical
hiring and retention records constitute the training data.

**Automated decision-making:** yes as currently designed — rejection emails may issue with no
human involvement, which is a decision producing legal or similarly significant effects on the
applicant.

## Questions each of us must answer independently

Purposes and lawful basis per purpose · retention per purpose · special-category data present or
inferable (Art 9) · Art 22 safeguards · whether a DPIA is required against the EDPB's nine
criteria · controller/processor split · which vendors need a DPA · transfer mechanism for the US
support access · AI Act and ePrivacy stacking.
