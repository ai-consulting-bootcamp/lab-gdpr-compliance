# GDPR Audit Pack - Friedrich Tschoepke

Same product, privacy lens · 23 November 2026 · Partner: Nicolò Marseu

Not legal advice. Facts rest on Nicolò's system brief and his public repository (commit `4abe2d2`). His answers to my written questions of 16 November are still pending; where they matter, the assumption is stated.

---

## Transition note (from the EU AI Act lab)

I carry forward the **Application Prep Agent**, the system I audited in the EU AI Act peer lab. Under the AI Act it fell into **limited risk / transparency** (Article 50(2): generated text must be marked as AI-generated). It stays outside Annex III area 4(a) only while the fit score serves the candidate and is not used by a third party to select or rank people. It is the most interesting case for GDPR because, unlike my own Project 3, it processes complete CVs of identifiable people. It scores them and decides automatically what they receive, and the form is already live and open to the public.

## Fact pattern

The client is a one-person start-up (Nicolò Marseu, Germany) that runs an n8n workflow called the Application Prep Agent. It is offered as a free public demo and is planned as a paid product for career services at bootcamps, universities and outplacement firms. Job seekers, or coaches acting for them, upload a CV as PDF, a job posting, optional free-text achievements and an email address. CVs contain name, contact details, work and education history, and possibly a photo, date of birth, nationality or health information. The data subjects are mainly in the EU, with Germany and the DACH region as target market. The CV text goes to OpenAI (US parent, EU entity in Ireland) for scoring and writing. The workflow runs on an n8n instance hosted by Ironhack, and the report is sent through a personal Gmail account. The AI system scores the candidate's fit for the job from 0 to 100, rewrites CV bullets, drafts a cover letter and interview notes, and emails the result. A score below 50 automatically replaces the full pack with a short note on the gaps.

**CFU 1 – Recognize**

- **Personal data:** identity and contact data, employment and education history, skills, self-reported achievements, email address, and a derived fit score (an inference about the person).
- **Special categories (Article 9):** not requested, but likely in practice. CVs often show a photo (can reveal ethnic origin or religion), disability status, union roles or health-related career gaps. Free text can contain anything.
- **Border crossing:** yes. OpenAI processes EEA data through OpenAI Ireland Limited, with a US parent and sub-processors. Google (Gmail) is US-based. The hosting location of the Ironhack n8n instance is unknown.

---

# Part 1 – Audit worksheet

## Section A – Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | (1) CV content: name, contact data, work history, education, skills, languages, possibly photo, date of birth, nationality, gaps. (2) Free-text achievements. (3) Email address. (4) Generated data: fit score, strong/partial/gap ratings, rewritten bullets, cover letter. (5) Technical data: IP address and timestamps in n8n and web server logs. |
| **Sources** | Directly from the job seeker (self-use), or from a coach about a candidate (third-party submission). Job posting and company research contain no personal data about the candidate. |
| **Purposes** | P1 Generate and deliver the application pack. P2 Score fit and route to full pack or short note. P3 Operate and debug the workflow (run logs). P4 Planned: pilot feedback and time measurement (sprint 1). P5 Planned: saved candidate profiles and partner dashboard with scores (sprint 3). |
| **Lawful basis per purpose** | **P1 Contract (6(1)(b))** for self-use: the person asks for the service and it cannot be delivered without processing the CV. **Coach submission: TBD – legal review**; the institution needs its own basis (likely contract with the candidate or legitimate interests) and is probably controller. **P2 Contract (6(1)(b))**, but only if the gate is part of the service as described before submission and the person can override it (see Article 22 below). **P3 Legitimate interests (6(1)(f))**: purpose is security and fault-finding; necessary only for a short window; balancing passes only with deletion within days. **P4 Legitimate interests**, limited to pseudonymised feedback; otherwise consent. **P5 TBD – legal review**, consent likely needed for stored profiles; scores visible to an organisation need a separate assessment. **Special-category data:** no Article 9(2) exception fits the scoring. Explicit consent (9(2)(a)) is possible but fragile; better to strip such data before scoring. |
| **Retention per purpose** | P1/P2: none intended; the public claim is "Nothing you submit is stored". Actual state: n8n keeps each run (CV text, email, report) under default settings; the Gmail sent folder keeps every report; OpenAI keeps API content for abuse monitoring for up to 30 days. **Target:** P1/P2 delete on delivery; P3 maximum 7 days; OpenAI 30 days unless Zero Data Retention is approved; P4 until end of pilot; P5 to be defined. |
| **Recipients and sub-processors** | OpenAI (language models and embeddings; CV text and name in several calls). Ironhack, as host of the n8n instance (all data). Google, through the Gmail account (report, email address, name). Jina Reader, Tavily, NewsAPI and Pinecone receive only the job link, company name or fixed text, so no candidate data. Planned: career services as recipients of reports, outplacement firms as recipients of scores. |
| **International transfers** | **OpenAI:** for EEA data, OpenAI's DPA names OpenAI Ireland Limited; onward transfer to the US parent and sub-processors relies on OpenAI's transfer terms. **TBD – verify** the mechanism (EU-US Data Privacy Framework or standard contractual clauses) in the current DPA. **Google via personal Gmail:** consumer terms, so no processor agreement and no transfer mechanism on the client's side. This is a gap. **Ironhack n8n:** location and contract unknown, **TBD**. |

## Section B – Risk and rights

**Special-category data (Article 9).** Possible in the inputs (photo, disability, health-related gaps, union roles) and inferable in the output: a model can carry an inferred nationality or age into the score or the cover letter. Nothing removes these details before scoring.

**Automated decision-making (Article 22).** The gate below 50 is a decision based solely on automated profiling. In the free self-use demo its effect is limited: the person can still apply anywhere. It becomes similarly significant if an institution uses the score to decide whom to support or put forward. The CJEU's SCHUFA ruling (C-634/21, 2023) treats a score as a decision when a third party relies on it heavily, which is exactly the sprint 3 dashboard. **Safeguard now:** a "send me the full pack anyway" option, an explanation of the score logic in the privacy notice, and no use of scores by third parties without human review.

**DPIA (Article 35).** **Required**, at the latest before the pilot with real candidates. EDPB criteria that apply:

| EDPB criterion | Applies? | Why |
|---|---|---|
| 1 Evaluation or scoring | Yes | Fit score 0–100 on a person's suitability for a job. |
| 2 Automated decision with significant effect | Partly | The gate is automated; significant once third parties rely on it. |
| 3 Systematic monitoring | No | One-off submissions. |
| 4 Sensitive or highly personal data | Likely | CVs can contain Article 9 data; career history is highly personal. |
| 5 Large scale | Not yet | Sprint 3 target of 200+ reports a month moves towards it. |
| 6 Matching or combining datasets | No | Company research holds no data on the candidate. |
| 7 Vulnerable data subjects | Yes in sprint 3 | Laid-off employees in outplacement depend on the firm. |
| 8 Innovative technology | Yes | Language models score people. |
| 9 Prevents exercise of a right or access to a service | Partly | Below 50 the person does not get the full service. |

Two or more criteria apply today (1, 8, likely 4), which triggers a DPIA under the EDPB guidance.

**Likely data subject friction points.** (1) **Access:** "what did you store about me?" cannot be answered while the storage statement and the actual retention differ. (2) **Erasure:** a CV sits in n8n history, the Gmail sent folder and OpenAI logs; only the first two can be deleted by the client. (3) **Objection to profiling and explanation of the score:** a candidate rejected by the gate will ask why. (4) **Coach submissions:** the candidate may not know the system exists (Article 14 information).

**Controller / processor split.**

| Entity | Role | Note |
|---|---|---|
| Nicolò Marseu | Controller (public demo, self-use) | Decides purposes and means. |
| Career service / outplacement firm | Controller for its candidates (pilot, sales) | Nicolò then becomes its processor. **TBD – legal review**: he becomes controller again for any own purpose, such as product improvement from pilot data. |
| OpenAI | Processor | Under the OpenAI DPA. |
| Ironhack (n8n host) | Processor, or independent controller if it uses data for its own purposes | **TBD**: no contract known. |
| Google (Gmail, consumer account) | Not a usable processor | Consumer terms offer no processor agreement. |
| Jina, Tavily, NewsAPI, Pinecone | No role for candidate data | No personal data shared. |

**Data processing agreements needed.** OpenAI (accept the DPA in the organisation settings and archive it), Ironhack or a replacement host, a transactional email service with an EU DPA in place of Gmail, and Nicolò as processor towards each career service (Article 28 contract).

## Section C – Law stacking

- **AI Act:** limited risk. Adds two duties GDPR does not cover: machine-readable marking of the generated cover letters and CV text (Article 50(2)) and AI literacy (Article 4). It becomes high-risk (Annex III 4(a)) if scores are used to select or rank candidates.
- **ePrivacy (in Germany the TDDDG, § 25):** the landing page loads Google Fonts from Google's servers, which sends visitors' IP addresses to Google without consent (LG München I, 3 O 17493/20, 2022). Fix by hosting fonts locally. No cookies or tracking pixels found in the landing page; the n8n form's cookies are unverified. Consent under ePrivacy does not replace the Article 6 basis for the CV processing; both apply separately.
- **Data Act:** not applicable. No connected products and no cloud switching.

---

# Part 2 – Client recommendation memo

**To:** Nicolò Marseu, Application Prep Agent
**From:** Friedrich Tschoepke
**Date:** 23 November 2026
**Re:** GDPR readiness before the design-partner pilot

**Bottom line: Go with conditions.** The product can be run lawfully, but today it collects real CVs through a public form while telling users that nothing is stored, and that statement is not true.

**What I found.** Each CV passes through four systems: your n8n instance, OpenAI, Gmail and the recipient's inbox. Two of them keep copies you do not control. The fit score is profiling, and the cut-off at 50 decides automatically what a person receives. CVs regularly contain photos, ages and health-related gaps, and nothing filters those out before scoring.

**Top three actions, in this order:**

1. **This week: make the storage claim true.** Switch off saving of run data in n8n (or delete it after seven days). Replace Gmail with an email service that offers an EU data processing agreement. Accept OpenAI's DPA. Until this is done, rewrite the form text to say exactly what is kept, where and for how long.
2. **Before the first pilot candidate: run a DPIA and sign the contracts.** Scoring plus sensitive CV content triggers a DPIA. Sign a processor agreement with each bootcamp, so it is clear that they are controller for their candidates. Give them a short notice to hand to candidates whose CVs coaches upload.
3. **Before the pilot ends: reduce what the model sees and let people override it.** Strip photo, date of birth, nationality and address before scoring. Add a "send me the full pack anyway" option below 50. Explain in plain words how the score is calculated.

**Residual risks you should accept knowingly:**

- **OpenAI retention:** OpenAI keeps inputs for up to 30 days for abuse monitoring unless you qualify for Zero Data Retention. You cannot delete those copies on request.
- **Bias:** a language-model score can still carry bias through job titles, schools or career gaps, even after stripping obvious details. Testing reduces this risk; it does not remove it.
- **Third-party submissions:** coaches will upload CVs of people who never read your notice. Your contract makes the institution responsible, but complaints will reach you first.

Do not build the partner dashboard with scores (sprint 3) before a separate legal review. It changes the GDPR and the AI Act picture at once.

---

# Part 3 – Peer review and debrief

## Peer review of my partner's memo

To complete after the swap with Nicolò.

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

**Client response (2–3 sentences):** _pending_

## Debrief

_Pending: where we agreed on lawful basis and DPIA need, where we diverged, and which reading we agreed is stronger._

---

# Part 4 – Reinforce and stretch

## DPIA outline (fit scoring)

1. **Description of processing:** CV and job posting in, fit score and gate decision out, using OpenAI, n8n and email; data flow and retention as in Section A.
2. **Necessity and proportionality:** is a numeric score needed, or would strong/partial/gap ratings serve the candidate equally well? Is the full CV necessary, or only experience and skills?
3. **Risks:** discriminatory scoring; Article 9 data reaching the model; the gate denying the full service; retention contrary to the public statement; third-party use of scores.
4. **Mitigation:** redaction before scoring, counterfactual tests (same CV, different name or age), override option, no-storage configuration, score use limited by contract.

## One DPA clause for OpenAI

The clause I would want: **retention and deletion of customer content, including abuse-monitoring logs, with a commitment to Zero Data Retention or a fixed maximum period.** It is the only copy of the CV the client cannot delete itself, so it decides whether an erasure request can be fully honoured.

## UK data subjects

The bottom line stays **go with conditions**. Under UK GDPR the transfer to OpenAI is governed by the UK route: OpenAI's DPA names OpenAI OpCo, LLC for UK data, so the client needs the UK International Data Transfer Addendum or the UK extension of the Data Privacy Framework. **TBD – legal review**, plus a UK representative check if the service targets UK users.

## Data protection by design checklist (fit scoring)

| Item | Status | Note |
|---|---|---|
| Data minimisation | Fail | Full CV text, including photo text, age and nationality, goes into scoring. |
| Purpose binding | Unknown | No technical limit; planned partner dashboard would reuse scores. |
| Access controls | Unknown | Who can open past runs on the Ironhack instance is not documented. |
| Retention enforcement | Fail | n8n default history and the Gmail sent folder keep data; no automated deletion. |
| Subject rights workflow | Fail | No contact address, no process, no inventory of copies. |
| Incident response (72 hours) | Fail | No documented process; the host and the email account are outside the client's control. |

---

## Sources

- [OpenAI, Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data)
- [OpenAI, Data Processing Addendum](https://openai.com/policies/data-processing-addendum/)
- EDPB-endorsed WP29 Guidelines on DPIA (WP248 rev.01), the nine criteria
- CJEU, C-634/21 *SCHUFA Holding (Scoring)*, 7 December 2023
- LG München I, 3 O 17493/20, 20 January 2022 (Google Fonts)
- [Nicolò Marseu, Application Prep Agent repository](https://github.com/nmarseu/Project-3-Marseu)
- My EU AI Act peer audit of the same system (16 November 2026)
