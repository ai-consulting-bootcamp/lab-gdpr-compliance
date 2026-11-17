# Reinforce — DPIA outline, key DPA clause, UK variant

Scenario: Kranich Logistik AI CV screening (see [GDPR_Audit_Pack_Pieter_Albrecht.md](GDPR_Audit_Pack_Pieter_Albrecht.md)).

## 1. DPIA outline — most sensitive activity: AI scoring and rejection of applicants (P2/P3), trained on top-performer profiles (P4)

| DPIA section | Content |
|---|---|
| **Description of processing** | Applicant portal → CVs and cover letters sent by API to the US vendor → parsed and compared with the job description + top-performer profiles (built from 5 years of HR data) → score and ranking returned → recruiters read the top 20 → the rest are rejected. Tens of thousands of applicants a year in DE and PL. |
| **Necessity & proportionality** | Purpose: manage high application volume with two recruiters. Less intrusive options: knock-out questions on hard requirements (licence, shift availability) and anonymised CV parsing. Data minimisation: no photos, date of birth, nationality or free text on health; employee data aggregated with no names or absences. Lawful bases per the data map. Transparency: AI notice in the job ad and the portal. |
| **Risk identification** | (a) Discrimination via biased training profiles or proxies (age, gender, origin); (b) solely automated rejection without human review (Art. 22); (c) inaccurate CV parsing (non-standard CVs, non-native language, career changers) → good candidates scored low; (d) US government access to transferred data; (e) employees' data reused without their knowledge; (f) breach exposing applicant data at scale. |
| **Mitigation** | (a) Pre-launch and quarterly bias audit (selection rates by group, four-fifths rule as an indicator), features reviewed by HR + works council; (b) recruiter sign-off on every rejection + human review on request; (c) random sample of 10% of below-cut-off CVs read manually each month, with override rate tracked; (d) DPF check + SCC fallback + EU-region processing; (e) inform employees, use aggregate features only, honour Art. 21 objections; (f) encryption, role-based access, deletion after 6 months. Residual risk: **medium**. If the bias audit can't be done before launch, it's **high**, which means prior consultation with the supervisory authority (Art. 36). |

## 2. One DPA clause I would insist on with the US vendor

> *"The Processor shall not use Controller Personal Data, including applicant data, scores, recruiter decisions or any data derived from them, to train, fine-tune, benchmark or improve any model or service of the Processor or of third parties. The Processor shall notify the Controller in advance of any change to the model used to score the Controller's applicants and provide updated accuracy and bias test results before that change takes effect."*

**Why:** first, it keeps the vendor a pure **processor**. If it trains its general model on Kranich's applicants, it decides purposes itself and becomes a controller, and the client has no basis to share the data for that. Second, a silent model update can change who gets shortlisted overnight. The client, as AI Act deployer and GDPR controller, has to monitor the system's behaviour, and it can't do that if the model changes without notice.

## 3. Bottom line rewritten — the client also hires in the UK

**Changes for UK applicants: the automated rejection is *less* blocked, but not free.**

- **ADM rules differ:** since 5 February 2026, UK GDPR Art. 22 has been replaced by **Arts. 22A–22D** (Data (Use and Access) Act 2025, s. 80). Solely automated significant decisions are no longer generally prohibited, *provided* safeguards are in place: informing the applicant, a way to make representations, human intervention and a way to contest. The stricter rule remains where **special-category data** is involved, so stripping photos and health mentions matters even more.
- **But the bottom line barely moves:** the client still needs the safeguards, the ICO is actively looking at AI in recruitment, and the EU (DE/PL) process remains bound by EU Art. 22. Running one process for all three countries is simpler, so I'd **keep human sign-off everywhere**.
- **Transfers:** UK→US needs the **UK Extension to the DPF**, or the IDTA / UK Addendum to the SCCs.
- **Discrimination:** the UK Equality Act 2010 replaces AGG/PL rules, with the same bias-audit need. **No AI Act** in the UK, so the deployer duties disappear there, but the GDPR-side DPIA stays.
- *TBD — legal review:* a UK representative (Art. 27 UK GDPR) if there's no UK establishment.
