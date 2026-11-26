# GDPR Audit Pack - Ben Mayer

**Scenario:** Option A, carried forward from the EU AI Act lab (Case B, applicant ranking) · **Date:** 26 Nov 2026 · **Not legal advice.** Items marked ⚖️ need confirmation by counsel.

## Transition note

I'm carrying forward **Case B** from my [EU AI Act approval pack](https://github.com/benmayer/lab-eu-ai-act-compliance/blob/main/eu-ai-act-approval-pack-ben-mayer.md): a German staffing agency using a vendor tool that ranks job applicants. It was classified **high-risk (Annex III §4(a))** and approved with controls. It's the most interesting case for GDPR because it is the only one where personal data *is* the product: the system profiles tens of thousands of people and decides, in practice, who gets an interview. The AI Act asked "is the tool safe and well-governed?" GDPR asks a different question: "is the agency allowed to process these people's data this way, and can they push back?" Case A (rail chat) touched personal data only incidentally, and Cases C and D involved none or were already banned.

Company names below are **fictional**. Facts beyond the original brief (volumes, vendor stack, US sub-processor) are assumptions I added so the audit has something concrete to test. Each one is a question I'd confirm with the client.

---

# Part 1 - Audit worksheet

## Fact pattern

**Lagerkraft Personal GmbH** (fictional) is a German temporary-staffing agency with ~350 internal staff across 14 branches in NRW and Lower Saxony, placing ~2,500 temp workers a year in warehouse and logistics roles. It receives **~60,000 applications a year** through its own careers portal and job boards. Applications contain CVs (often with a photo and date of birth, as is common in Germany), contact details, work history, forklift and medical-fitness certificates, language skills and shift availability. Applicants are almost all **in Germany or other EU states** (about a quarter are Polish, Romanian or Bulgarian nationals), plus a small number of third-country nationals, some applying from Ukraine or Moldova. The ranking tool is supplied by **RankFlow B.V.** (fictional, Amsterdam), hosted on **AWS Frankfurt** (US parent company), and RankFlow sends each CV to a **US-based LLM API** to parse it into structured fields. The system scores each applicant against the vacancy, shows a ranked list inside qualification bands with job-related reasons, and ~40 recruiters invite candidates from it. The tool never rejects anyone automatically, but recruiters usually start with the top 20, so **a low rank can mean no human ever looks at the application**.

## 1. Recognize

| Question | Answer |
|---|---|
| **Categories of personal data** | Identity and contact (name, address, phone, email, photo, date of birth); eligibility (nationality, work permit); professional (work history, gaps, qualifications, forklift licence, languages); availability (shifts, start date, commuting distance); **derived data** (parsed fields, score, rank, band, reasons); recruiter notes; **recruiter data** (who overrode what and why, logged for the AI Act). |
| **Article 9, included** | Likely, without anyone asking for it. A *G25 occupational medical certificate* (fitness for forklift work) is **health data**. German CVs often mention a recognised severe disability (*Schwerbehinderung*), which is also health data. Union or works-council roles in work history can reveal **trade-union membership**. |
| **Article 9, inferable** | Photos and names can reveal ethnic origin. Availability limits ("no Friday evenings") can point to religion. Gaps in a CV can point to illness or pregnancy. Postcode and language patterns act as ethnicity proxies. The model must not learn from any of these. |
| **Does data cross an EU border?** | **Yes, at one point.** Portal (DE) → RankFlow (NL) → AWS Frankfurt (EU region, but US parent, so a US government access risk under the CLOUD Act) → **US LLM API (a Chapter V transfer)** → structured fields back to the EU. Applicants applying from Ukraine/Moldova send data *into* the EU, which isn't a transfer problem; GDPR applies to them through the agency's EU establishment (Art 3(1)). |

## 2. Apply - Section A: Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | As in Recognize above. Special categories are present incidentally (health certificates, disability status) and inferable (ethnic origin, religion). |
| **Sources** | Applicants directly (careers portal, email, walk-in at branches); job boards (StepStone, Indeed, Arbeitsagentur job portal), which are independent controllers forwarding applications; recruiters (notes, overrides); RankFlow (derived scores). |
| **Purposes** | See the per-purpose table below (P1-P7). |
| **Lawful basis per purpose** | See table. Key choice: the **AI ranking rests on legitimate interests, not contract or consent**. |
| **Retention** | Default **6 months after rejection or vacancy close**, based on the German claim windows for discrimination (2 months under AGG §15(4), then 3 months to sue under ArbGG §61b, plus a buffer). This also covers the AI Act's ≥6-month log retention. |
| **Recipients and sub-processors** | RankFlow (processor) → AWS (sub-processor) and the US LLM API provider (sub-processor). Hiring client companies receive shortlisted profiles as **independent controllers**. Works council gets aggregate reports only. |
| **International transfers** | RankFlow → US LLM API. Mechanism: **EU-US Data Privacy Framework** (Art 45) *only if* the provider is on the active DPF list and its certification covers HR data ⚖️; otherwise **SCCs Module 3** (processor to processor) + a transfer impact assessment. **Recommended:** move parsing to an EU-region endpoint so there is no transfer at all. |

### One row per purpose

| # | Purpose | Lawful basis (Art 6) | One-line justification | Retention |
|---|---|---|---|---|
| P1 | Receive and manage applications | **6(1)(b)** steps prior to a contract, at the applicant's request | The applicant asked to be considered for work; reading the application is necessary for that. National §26 BDSG is shaky after CJEU C-34/21 (2023), so I don't rely on it alone ⚖️. | 6 months after rejection |
| P2 | **AI scoring and ranking** against a vacancy | **6(1)(f)** legitimate interests | Contract necessity is interpreted strictly (EDPB Guidelines 2/2019), and a human can evaluate a CV without AI, so (b) doesn't fit. LIA below. Consent fails because applicants can't freely refuse a gatekeeper. | Score, rank and reasons: 6 months, kept with P1. RankFlow deletes its copy 30 days after the vacancy closes. |
| P3 | Share shortlisted profiles with hiring client companies | **6(1)(b)** | Placement with a client company is what the applicant applied for. Whether named profiles need a per-client confirmation from the applicant: **TBD - legal review**. | The client company is its own controller; the agency logs what was sent, for 6 months |
| P4 | Talent pool for future vacancies | **6(1)(a)** consent | It goes beyond the vacancy applied for, so the applicant decides. Separate, unticked checkbox, withdrawable at any time. | 12 months, then renew consent or delete |
| P5 | AI Act logging and human-oversight records (includes recruiter data) | **6(1)(c)** legal obligation from 2 Dec 2027 (AI Act Art 12, 26(5)-(6)); **6(1)(f)** until then | Logs are needed to prove the oversight is real. Monitoring recruiters also needs a works-council agreement (BetrVG §87(1) no. 6). | Minimum 6 months, maximum 12 |
| P6 | Fairness monitoring (outcome gaps by sex, age band, nationality) | Sex, age, nationality: **6(1)(f)**. Ethnic origin or disability questions: **6(1)(a) + 9(2)(a)** explicit consent via a separate voluntary survey | Without group data you can't detect discrimination. The survey is kept away from recruiters and the model; only aggregates are reported. Whether consent is free enough here: **TBD - legal review**. | Raw survey 12 months; aggregates indefinitely (anonymous) |
| P7 | RankFlow using agency data to improve its own model | **None. Not permitted.** | RankFlow would become a separate controller, the agency has no basis to hand over applicant data for that purpose, and erasure from a trained model is close to impossible. Banned in the DPA. | - |

### Legitimate interests assessment (P2, AI ranking)

| Step | Finding |
|---|---|
| **Purpose** | Faster, more consistent shortlisting at 60,000 applications a year, with job-related reasons recruiters can check. A real, lawful business interest. ✅ |
| **Necessity** | Partly. Volume justifies *some* automation, but not every field. Photo, date of birth, nationality, full address and certificates of health are **not needed for scoring** and must be stripped before the model sees the CV. ✅ with minimisation |
| **Balancing** | Applicants expect their CV to be evaluated, so this is the **original purpose**, not a new one (no Art 6(4) compatibility problem). Against that: profiling at scale, a power imbalance, and a rank that can shut people out. It passes **only if** there's genuine human review, a right to object with a manual route, and a clear notice. ⚠️ Conditional pass |

## 2. Apply - Section B: Risk and rights

**Are special-category data present or inferable (Art 9)?**
Yes. Health data (G25 certificates, disability status) and trade-union information turn up in CVs without anyone asking. Ethnic origin is inferable from photos, names and postcodes. Fix: strip these fields before parsing output reaches the scoring model, and require RankFlow to prove (via its AI Act Art 10 bias tests) that the model doesn't rebuild them from proxies.

**Automated decision-making with legal or similarly significant effects (Art 22)?**
**Probably yes, unless the review is real.** In *SCHUFA* (C-634/21, 2023) the CJEU held that a score counts as a "decision" when the party using it relies on it heavily. Recruiters starting at the top 20 means a rank of 140 effectively rejects someone, and missing out on a job is a "similarly significant effect". There's no German law authorising this, and it isn't strictly *necessary* for a contract. So the design has to keep the tool **outside** Art 22: a recruiter must open the summary card of every candidate who meets the minimum requirements, and log a reason for each override. The fallback safeguards (Art 22(3): human intervention, the right to contest, an explanation) go in the notice anyway.

**Is a DPIA required?** **Yes, clearly.** 7 of the 9 EDPB criteria apply (two are enough):

| # | EDPB criterion | Applies? | Why |
|---|---|---|---|
| 1 | Evaluation or scoring | ✅ | Ranking candidates is the whole point. |
| 2 | Automated decision with legal/similar effect | ✅ | The rank decides who gets seen (see Art 22 above). |
| 3 | Systematic monitoring | ⚠️ Partly | Not of applicants, but override logs systematically monitor recruiters. |
| 4 | Sensitive or highly personal data | ✅ | Health certificates, disability status, inferable ethnicity. |
| 5 | Large scale | ✅ | ~60,000 applicants a year across 14 branches. |
| 6 | Matching or combining datasets | ✅ | CV + job-board data + certificates + availability + past placement history. |
| 7 | Vulnerable data subjects | ✅ | Job seekers depend on the agency, many are non-native speakers, some are migrants whose work permit depends on getting work. |
| 8 | Innovative technology | ✅ | LLM parsing plus an ML ranking model. |
| 9 | Prevents access to a service or contract | ✅ | A low rank blocks access to a job. |

Germany's DSK list of processing that always needs a DPIA also covers AI that evaluates personal aspects ⚖️. AI Act Art 26(9) says deployers should use the provider's Art 13 instructions when doing it. (An AI Act Art 27 fundamental-rights impact assessment is *not* required, because a private staffing agency isn't a public body or a credit or insurance provider.)

**Most likely data subject friction points.**
1. **Access with an explanation (Art 15(1)(h)):** "Why was I ranked 140th?" The CJEU in *Dun & Bradstreet Austria* (C-203/22, 2025) said the controller must explain the procedure and principles actually applied, in plain language. RankFlow must supply per-candidate reasons the agency can pass on. AI Act Art 86 adds a similar right from Dec 2027.
2. **Objection to profiling (Art 21):** Because P2 rests on legitimate interests, an applicant can object. Offer a **manual review route** instead of arguing about "compelling grounds".
3. **Rectification (Art 16):** The LLM parser will misread CVs (wrong dates, a missed licence). Applicants need to see and correct the parsed fields, or their rank is built on wrong data.
4. **Erasure (Art 17):** Easy in the agency's system. Hard if RankFlow has trained on the data, which is why P7 is banned.

All of these must be answered within **one month** (extendable by two more months for complex cases, if the applicant is told within the first month).

**Controller / processor split.**

| Entity | Role |
|---|---|
| Lagerkraft Personal GmbH (agency) | **Controller** for P1-P6 |
| RankFlow B.V. | **Processor** (Art 28). Would become an independent controller if it reused data for its own model (P7), which is why that's banned. Also the AI Act *provider*. |
| AWS (Frankfurt) | **Sub-processor** of RankFlow |
| US LLM API provider | **Sub-processor** of RankFlow, and the importer in the Chapter V transfer |
| Hiring client companies | **Independent controllers** once they receive a profile. They make their own hiring decision, so it isn't joint control. |
| Job boards | **Independent controllers** (data source) |
| Recruiters | The controller's staff, and also **data subjects** of the override logs |

**Is a DPA needed?** Yes, an **Art 28 DPA with RankFlow**, which must flow down equivalent terms to AWS and the LLM API (Art 28(4)) and give the agency the right to object to new sub-processors. Also a DPA with the careers-portal/ATS provider if that's a separate company. With client companies it's a **controller-to-controller data sharing agreement**, not a DPA.

## 2. Apply - Section C: Law stacking

- **AI Act cross-check:** High-risk, Annex III §4(a). It adds what GDPR doesn't: provider conformity assessment, CE marking and **mandatory bias testing (Art 10)**, human-oversight *design* duties (Art 14), deployer duties (Art 26), including informing workers' representatives (26(7)) and telling applicants a high-risk AI system is used (26(11)), plus a right to explanation (Art 86). These apply from **2 Dec 2027** (Digital Omnibus); GDPR applies **today**.
- **ePrivacy check:** The ranking itself reads no device data, so no. But the **careers portal** probably runs analytics cookies and job-board conversion pixels, which need prior consent under **§25 TDDDG** (Germany's ePrivacy implementation). Here ePrivacy *does* override GDPR's flexibility: legitimate interests can't be used for non-essential cookies. Tracking data must never feed into the score.
- **Data Act check:** No connected products, so mostly N/A. One useful lever: the Data Act's cloud-switching rules (Ch. VI, applicable since 12 Sept 2025) give the agency a right to switch away from RankFlow and take its data and logs with it. Write that exit into the contract.

*Legal baseline: GDPR as currently in force. The proposed Digital Omnibus changes to GDPR are not enacted and not relied on here* ⚖️.

---

# Part 2 - Client recommendation memo

**To:** Managing Director and Data Protection Officer, Lagerkraft Personal GmbH
**From:** Ben Mayer, AI Consulting
**Re:** GDPR conditions for the RankFlow applicant-ranking tool
**Date:** 26 November 2026

<!-- MEMO_START -->
**Bottom line: go with conditions.** The tool can lawfully speed up shortlisting, but only if your recruiters genuinely review candidates and no CV leaves the EU without a valid transfer route.

**Why conditions.** Ranking 60,000 applicants a year is profiling at scale. The EU's top court has ruled that a score can count as an automated decision when the people using it rely on it heavily, and your recruiters start with the top 20. If nobody ever opens the application of the candidate ranked 140th, the tool has effectively rejected them, and you would need a legal basis you don't have. Handling applications rests on the applicant's request to be considered. The ranking itself rests on your legitimate interest in efficient shortlisting, which only holds if anyone who objects can get a manual review.

**Top three actions, in this order:**

1. **Before any applicant data reaches RankFlow:** sign a data processing agreement that bans RankFlow from training its models on your applicants, lists every sub-processor, and moves CV parsing to an EU-region endpoint. If the US parser stays, confirm the US provider's Data Privacy Framework certification or sign standard contractual clauses with a transfer impact assessment.
2. **Before the first live vacancy:** complete a DPIA and agree it with your works council. Build in three controls: strip photos, date of birth, nationality and health certificates before scoring; show qualified candidates in bands; and require a recruiter to open the summary card of every candidate who meets the minimum requirements, logging a reason for each override.
3. **Before launch:** update the applicant privacy notice to explain the ranking, the right to object and to human review, and deletion six months after rejection. Prepare a standard reply that explains which factors drove a candidate's score.

**Residual risks you should accept knowingly:**

- **Rubber-stamping.** Recruiters can still follow the rank despite every control. Track override rates monthly. If they fall to near zero, a regulator may treat the tool as the decision-maker.
- **Hidden proxies.** Removing obvious fields doesn't remove bias. Postcode, CV gaps and language can stand in for ethnicity, age or disability, and under the German Equal Treatment Act the burden of proof can shift to you.
- **Transfer instability.** The Data Privacy Framework is under challenge at the EU's top court. If any data still goes to the US, have an EU-only fallback ready.
<!-- MEMO_END -->
