# GDPR Audit Pack — Sandra Obregón

## Phase 1 — Transition and fact pattern

I am continuing my job application ranking case from the EU AI Act lab. I classified it as high risk because it evaluates and ranks applicants. I chose it for this audit because applicants may lose the chance to get an interview if the vacancy is filled before HR reviews their CVs.

The fictional client is a logistics company with 50 employees. It receives about 60 applications per vacancy from people who live in Spain. The form collects names, emails, phone numbers, CVs, work experience, salary expectations and start availability. Free-form CVs may contain health or disability information. In the proposed design, Microsoft 365 collects and stores applications and sends emails. The OpenAI API receives an extract with relevant experience, qualifications and start availability for ranking. The exact vendors’ entities, processing locations and transfers are pending contract and configuration checks.

The system prepares the extract automatically. The design calls for filtering before submission to the API. HR can see salary expectations and a field for job requirements that need clarification, such as a start date. HR chooses whom to call from the applications it reviews. If the company hires one of the first ten applicants, lower-ranked applicants may lose the chance to interview without individual review. Before submitting, applicants see a notice about AI ranking. If they leave the form at that point, they do not submit an application. After closure, the proposed workflow asks the remaining applicants separately if the company can keep a limited profile for similar vacancies.

## Phase 2 — Audit worksheet

### A — Data map

| Purpose | Data and source | Lawful basis and reason | Retention | Recipients and sub-processors | International transfers |
| --- | --- | --- | --- | --- | --- |
| Process the application for the current vacancy | Form and CV from the applicant. HR records follow-up outcomes. | Contract, Art. 6(1)(b), for necessary steps at the applicant’s request before a possible employment contract. | Active until the vacancy closes. Any longer retention and its basis are TBD. | HR and Microsoft 365. Confirm sub-processors. | Confirm entities, locations, access and the applicable transfer mechanism, if needed. |
| Rank applications for the current vacancy | Relevant experience and qualifications from the CV, start availability from the form, and the ranking created by the system. | TBD — legal review. If legitimate interests is considered, document the purpose, show why the ranking is necessary and balance the company’s interest against applicants’ rights. | Proposed for the active selection period. Provider logs and any retention after closure are TBD. | HR, Microsoft 365 for the case records, and OpenAI API for the planned extract. Confirm sub-processors. | Confirm entities, locations, access and the applicable transfer mechanism, if needed. |
| Invite applicants to join the pool | Email from the application form, vacancy status and response. | TBD — legal review before using contact details to send the invitation. | TBD for the invitation and response records outside the pool. | HR and Microsoft 365. Confirm sub-processors. | Check the Microsoft 365 setup and any applicable mechanism. |
| Keep a profile for similar future jobs | Name, contact details, short work summary and record of opt-in. | Consent, Art. 6(1)(a), because joining is optional and requires a positive choice. | Up to six months from consent, or until withdrawal if earlier. | HR and Microsoft 365. Confirm sub-processors. | Check the Microsoft 365 setup and any applicable mechanism. |

### B — Risks and rights

- **Article 9.** Free-form CVs may include health or disability data. The proposed design excludes this information from ranking, the clarification field and the pool, but testing is needed to check what reaches the API and what can be inferred from outputs.
- **Article 22.** In this scenario, the automated order can determine who loses the chance to interview without an individual review, so the audit treats those exclusions as falling under Article 22. Before the final hiring decision, HR should independently assess applications that would otherwise be excluded, have the authority to change who advances and record the reason.
- **DPIA.** Complete a DPIA before using real CVs because systematic scoring can significantly affect access to an interview. The criteria below explain how the case was screened.
- **Rights.** Applicants may ask to see the data used to rank them or correct a wrong start date. The company needs to locate and remove a pool profile after consent is withdrawn where no other basis applies. If the company relies on legitimate interests for ranking, it must assess objections individually.
- **Roles.** The logistics company is the controller because it decides why and how applicant data is used. Microsoft 365 and the OpenAI API are assumed processor services for the tasks in the data map, subject to checking their contracts.
- **DPAs.** Verify that a binding Article 28 agreement covers both Microsoft 365 and the OpenAI API before sending real applicant data. Confirm the legal entities, sub-processors and transfer arrangements.

| DPIA criterion | Case assessment |
| --- | --- |
| Evaluation or scoring | Yes. AI evaluates and ranks applicants. |
| Automated decision with significant effect | Yes. The order can decide who loses a chance to interview. |
| Systematic monitoring | Not identified in the recruitment flow. |
| Sensitive or highly personal data | Possible. Free-form CVs may contain health or disability details. |
| Large scale | Not established. About 60 candidates per vacancy. Annual volume is unknown. |
| Combining datasets | No external matching planned. The CV and form are part of the same application. |
| Vulnerable people | Possible. Assess the power imbalance between employer and applicant. |
| Innovative use of technology | Relevant. AI takes over the initial classification previously done by HR. |
| Barrier to a right, service or contract | Relevant. Losing the chance to interview may block access to the job contract. |

### C — Law stacking

- **AI Act** — High risk under Annex III 4(a). Article 26 adds a specific duty to give trained staff the authority to oversee the system.
- **ePrivacy** — Tracking is outside the proposed design. Check the actual form and obtain consent if it uses tracking technologies that require it.
- **Data Act** — The ranking uses no connected-product data. Check cloud switching rules if the company later moves its recruitment files to another provider.

## Phase 3 — Client recommendation memo

**To the HR and IT leads**

**Go with conditions.** The AI system could save HR time by sorting CVs, but the company should wait before using real applications because the ranking can leave applicants without a chance to interview or an individual review.

1. **Complete a Data Protection Impact Assessment before the pilot.** Article 6(1)(b) can cover the necessary steps to process an application at the applicant’s request before a possible job contract. Ask Legal to assess the AI ranking separately, including whether legitimate interests under Article 6(1)(f) can be justified. Address the Article 22 risk by giving trained HR staff time and authority to review applications that would otherwise be excluded. Staff should be able to change who moves forward and should record why before the final hiring decision. This also supports human oversight under the AI Act.

2. **Check both vendor agreements and test what the system sends.** Confirm that the Data Processing Agreements cover Microsoft 365 and the OpenAI API. Check who can access applicant data and whether it is transferred outside the European Economic Area. Test with fictional CVs to check that only relevant experience, qualifications and start availability reach the ranking service. Include a CV where health information is mixed into a work experience paragraph.

3. **Update the application form and closing email.** Before applicants submit a CV, explain how AI affects who gets a call and where they can send privacy requests. Check whether the form uses tracking cookies and request consent if ePrivacy rules require it. At closure, use a separate opt-in for the candidate pool. Store a limited profile for up to six months and remove it earlier if the applicant withdraws consent.

**Residual risks.** The AI may rank qualified people too low if their experience is described in an unusual way. The filter may miss sensitive details in free text. HR may follow the ranking too closely under time pressure, even when staff have the authority to change the outcome.

## Phase 4 — Partner swap and peer review

### Jaime’s review of my memo

| Criterion | Score | Comment summary |
| --- | ---: | --- |
| Clear bottom-line recommendation | 3 | The decision and reason appear at the start. |
| Lawful basis selection is justified | 2 | Name Articles 6 and 22 and explain which basis Legal should review for ranking. |
| Top actions are specific and sequenced | 3 | Clear order and concrete vendor and filter checks. The first action includes several tasks. |
| Residual risks are named honestly | 3 | Realistic risks. Consider indirect discrimination. |
| Law stacking is addressed (AI Act / ePrivacy) | 3 | The memo links human oversight to the AI Act and includes a conditional cookie check. |

**Client reply, summarised.** We accept the recommendation and the order of the actions. Before we commit, we want to know how many HR hours review would take, what review is needed and which basis Legal should consider for ranking.

### My review of Jaime’s memo

| Criterion | Score | Comment |
| --- | ---: | --- |
| Clear bottom-line recommendation | 3 | “Proceed with conditions only” is clear. The memo explains why promotion scoring needs safeguards. |
| Lawful basis selection is justified | 3 | The memo explains the need to balance the company’s interests against workers’ rights and to check whether production records can be reused for promotions. |
| Top actions are specific and sequenced | 3 | First confirm the lawful basis, then complete the DPIA and plan human review, and finally check vendor agreements, transfers and retention. |
| Residual risks are named honestly | 3 | A machine problem or a difficult shift could lower a worker’s score even if they did their job well. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | The memo identifies the AI Act tier. I would add a specific AI Act duty and a short check for access to worker device data. |

**As the client.** We accept the recommendation to proceed with conditions. Before we approve the pilot, please explain how supervisors will check whether a low score comes from the worker’s performance, a machine problem or shift conditions.

### Debrief conclusion

Both cases need a Data Protection Impact Assessment and a human review that can change the outcome. In the recruitment case, the AI ranking can leave applicants out before HR reads their CVs. In the promotion case, the supervisor can check the records and reject the AI recommendation before proposing a worker for promotion. This makes the Article 22 concern clearer in the recruitment case. In both cases, the company should confirm the lawful basis for AI scoring before using real personal data.

For HR capacity, if there are 60 applications and HR reviewed only the first 10, reviewing the other 50 at an assumed five minutes each would take about 4 hours and 10 minutes. This planning estimate still needs to be tested. It does not set a legal minimum.

## Technical evidence — local run

**Run:** `python3 cv_minimisation_demo.py`. Both inputs are fictional and are defined in the [local script](./cv_minimisation_demo.py). The script prints each input, the proposed API payload and whether it still contains the fictional health sentence.


```jsonl
{"case": "separate_fields", "input": {"name": "Fictional Applicant", "email": "applicant@example.invalid", "salary_expectation": 28000, "health_note": "I have asthma.", "experience": "Two years in warehouse operations.", "qualifications": "Forklift certificate", "start_in_days": 15}, "proposed_payload": {"experience": "Two years in warehouse operations.", "qualifications": "Forklift certificate", "start_in_days": 15}, "fictional_health_text_present": false}
{"case": "mixed_free_text", "input": {"experience": "Two years in warehouse operations. I have asthma.", "qualifications": "Forklift certificate", "start_in_days": 15}, "proposed_payload": {"experience": "Two years in warehouse operations. I have asthma.", "qualifications": "Forklift certificate", "start_in_days": 15}, "fictional_health_text_present": true}
```

**Observed output.** The first payload excluded the separate health note, contact data and salary. The second kept the health sentence because it was inside the experience field. This demonstrates a failure of a field allowlist on mixed free text. The run is local and makes no OpenAI or Microsoft 365 calls. The proposed production filter and ranking remain untested.

## References

- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [AEPD guidance on data protection in employment](https://www.aepd.es/guias/la-proteccion-de-datos-en-las-relaciones-laborales.pdf)
- [DPIA screening criteria endorsed by the EDPB](https://www.edpb.europa.eu/system/files/2022-09/in-20-7-4_final_decision_-_redacted.pdf)
- [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ePrivacy Directive](https://eur-lex.europa.eu/eli/dir/2002/58/oj)
- [EU Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
