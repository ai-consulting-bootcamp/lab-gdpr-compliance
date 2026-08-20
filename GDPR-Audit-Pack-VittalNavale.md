# GDPR Audit Pack — Vittal Navale

**Partner:** Ugo · **Scenario:** Option B(b) variant — AI-assisted CV screening for a national retail chain


---

## Section 0 — Fact pattern

The client is a national retail chain (~15,000 employees across EU/EEA stores and distribution warehouses) whose two-person HR team receives roughly 400 CVs a week for store and warehouse roles. They are piloting an AI-based CV screening tool, licensed from a US-based HR-tech vendor, that ingests each resume plus a short online skills assessment and scores the candidate against the job description. Candidates are auto-sorted into "strong fit," "maybe," or "not a fit" tiers. Recruiters currently only open the "strong fit" folder before making outreach calls; "not a fit" candidates receive an automated rejection email with **no confirmed human review step**. The scoring model was trained on five years of the client's historical hiring and retention data (who was hired, and who stayed past one year). Data subjects are job applicants located in the EU/EEA; the vendor processes and stores assessment and scoring data on US infrastructure. HR wants to launch within six weeks and has not yet decided whether a recruiter must review "not a fit" outcomes before rejection goes out.

---

## CFU Checkpoint 1 — Recognize

- **Categories of personal data present:** identity data (name, contact details), education and employment history, assessment responses, derived scores/tier labels, and — for the training set — historical employee retention outcomes (who stayed past one year).
- **Special-category data (Article 9):** none is *collected* directly, but it is plausibly **inferable**: name and address can proxy for ethnicity or national origin, resume gaps can proxy for disability, pregnancy, or caregiving status, and a retention-outcome model trained on past hires risks encoding historical bias correlated with protected characteristics. This must be treated as a live Article 9 risk, not dismissed because no explicit special-category field exists.
- **Cross-border data flow:** yes. The vendor stores and processes CV and assessment data on US infrastructure, so personal data leaves the EU/EEA at the point of transfer to the vendor.

---

## Section A — Data map

| Field | Answer |
|---|---|
| **Categories of personal data** | Identity/contact data (name, email, phone, address); education & employment history; free-text CV content; online assessment answers/scores; system-generated fit-tier label; historical hiring/retention outcomes (training set only) |
| **Sources** | Direct from candidates (CV upload, assessment portal); internal HR systems (historical hiring/retention records used for model training) |
| **Purpose(s) — one row per purpose** | (1) Evaluate and shortlist a specific candidate for a specific role; (2) Rank/score candidates via the AI tool; (3) Send automated rejection notice to "not a fit" tier; (4) Train/improve the scoring model using historical hiring & retention data |
| **Lawful basis per purpose** | (1) Contract — Art. 6(1)(b), necessary to take steps at the applicant's request prior to entering an employment contract. (2) Legitimate interests — Art. 6(1)(f); efficient shortlisting of high application volume, subject to a documented LIA and to the Art. 22 safeguard described in Section B. (3) TBD — legal review (depends on whether rejection stays "solely automated"; see Section B). (4) TBD — legal review (repurposing former employees' records for model training is a new purpose not covered by their original employment-relationship processing; needs a fresh compatibility assessment under Art. 6(4) or a documented LIA, ideally with anonymized/aggregated training data) |
| **Retention period per purpose** | Application/assessment data for unsuccessful candidates: recommend 6–12 months (to defend against discrimination claims), then delete/anonymize; successful candidates' data folds into the employee HR file under normal retention rules; training dataset: TBD — legal review on how long historical outcome data can be retained and reused for this secondary purpose |
| **Recipients and sub-processors** | Internal: HR team, hiring recruiters. External: the US-based AI scoring vendor (processor); any cloud/infra sub-processors the vendor uses (TBD — legal review, needs vendor disclosure) |
| **International transfers and transfer mechanism** | EU/EEA → US, via the vendor's infrastructure. Requires Standard Contractual Clauses (SCCs) plus a Transfer Impact Assessment (Schrems II), and/or confirmation the vendor is certified under the EU-US Data Privacy Framework. Currently: TBD — legal review, no mechanism confirmed |

---

## Section B — Risk and rights

**Are any special-category data present or inferable from the outputs (Article 9)?**
Yes, by inference rather than direct collection. Name, address, resume gaps, and education institutions can act as proxies for race, ethnicity, disability, or age, and a model trained on past retention outcomes can reproduce historical discriminatory patterns. This should be treated as Article 9 in-scope and requires bias/fairness testing, not just a "we don't collect that field" defense.

**Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?**
Yes — the "not a fit" tier currently triggers an automated rejection email with no confirmed human review, and access to employment is a legally/similarly significant effect. As designed, this is a solely automated decision that Article 22(1) prohibits unless an exception applies (explicit consent, contract necessity, or authorized by law) with suitable safeguards (Art. 22(3)): the right to obtain human intervention, to express a point of view, and to contest the decision. Employment consent is inherently weak due to the power imbalance, and "contract necessity" is a thin basis for wholesale auto-rejection. **The safest and simplest fix is procedural: require a recruiter to review every "not a fit" outcome before rejection is sent**, which removes the decision from "solely automated" and sidesteps Article 22 restriction entirely.

**Is a DPIA required?** Using the EDPB's nine criteria, this processing meets at least four: (1) evaluation/scoring of individuals, (2) automated decision-making with legal/similarly significant effect, (3) sensitive data or data of a highly personal nature (inferable special-category data), and (4) data processed at scale (~400 CVs/week, ~20,000+/year) affecting a group in a dependent position (job seekers). Meeting two or more criteria triggers a DPIA under EDPB guidance — **a DPIA is required** before this system goes live.

**What data subject friction points are most likely?**
Right of access and explanation (candidates asking why they were rejected and what data/logic drove the score), right to object to profiling, and the right to human intervention under Article 22(3) once the automated-rejection flow is live.

**What is the controller/processor split?**
The retail chain is the **controller** — it determines the purposes (who to hire) and means (using the tool to screen at this volume). The AI vendor is the **processor**, acting on the retailer's instructions to score CVs — unless the vendor also uses client data to improve its product across other customers, in which case the vendor becomes an independent controller (or joint controller) for that secondary purpose, and that needs to be checked in the vendor contract.

**Is a DPA needed with any vendor? Which ones?**
Yes — a Data Processing Agreement (Art. 28) is required with the AI scoring vendor before any live candidate data is sent to it, covering processing instructions, sub-processor disclosure, security measures, and international-transfer terms (SCCs).

---

## Section C — Law stacking

- **AI Act cross-check:** CV screening/ranking for recruitment is an **Annex III high-risk** use case. Beyond GDPR, the AI Act adds: a documented risk-management system, data governance requirements for training data, technical documentation and logging, **human oversight** built into the system design (not left to informal practice), accuracy/robustness/bias testing, and a conformity assessment before deployment, plus a transparency obligation to inform candidates an AI system is used. The undecided "should recruiters review 'not a fit'" question is a live AI Act gap, not just a GDPR one.
- **ePrivacy check:** The online assessment portal likely sets session cookies; if it also runs analytics/tracking cookies, ePrivacy consent requirements apply on top of GDPR before any non-essential cookie is set. This is a secondary risk here — flag it for the assessment vendor, but it is not the primary exposure.
- **Data Act check:** N/A — no connected product or cloud-switching data involved in this scenario.

---

## Phase 3 — Client recommendation memo

**To:** Retail Chain HR Leadership & Legal
**From:** Vittal Navale, Privacy Advisory
**Re:** AI CV Screening Tool — GDPR/AI Act Go-Live Assessment

**Bottom line: Go, with conditions.** The tool addresses a real operational problem, but as currently configured — automated rejection with no confirmed human review — it creates an unlawful Article 22 automated-decision exposure and an unassessed AI Act high-risk deployment. Neither is fixable after launch without real cost, so both need to close before the six-week date, not after.

**Top three actions, in order:**

1. **Mandate human review of every "not a fit" rejection before it's sent**, no exceptions, and document this as a process control. This single change takes the rejection flow out of "solely automated" territory and resolves the Article 22 exposure without redesigning the model.
2. **Complete a DPIA before first live processing.** The scoring system meets at least four of the EDPB's nine trigger criteria (evaluation, automated decision-making, inferable special-category data, and scale). This is not optional, and it should include a bias/fairness test on the historical training data before it goes near a live candidate.
3. **Sign a Data Processing Agreement and Transfer Impact Assessment with the vendor before any candidate data is sent to US infrastructure.** Confirm whether the vendor operates as a processor only, or also reuses client data to improve its own model — that distinction changes the contract terms and the DPIA scope.

**Residual risks, even with these fixes:**

- **Bias in the training data.** Five years of "who stayed past one year" reflects whoever your past hiring and management practices favored — including any historical bias. A fairness audit reduces this risk but cannot fully certify the model as neutral; expect to monitor outcomes by group after launch, not just before.
- **Candidate transparency and explainability.** Even with human review added, candidates will ask why they scored "not a fit," and today there's no clear answer beyond "the model said so." Recruiters need enough visibility into the scoring rationale to give a real answer, or this becomes a recurring access-request and reputational problem.
- **Vendor dependency.** Even with a signed DPA and SCCs, the client is trusting a third party's infrastructure and practices for a high-risk process. A transfer mechanism reduces legal exposure; it does not eliminate the operational risk of relying on a US vendor for a decision this sensitive.

**Recommendation stands as go-with-conditions — not go as-is, and not stop.** The business need is real and the fixes are achievable inside six weeks if action 1 starts immediately.

---

## Phase 4 — Partner swap and peer review

### Ugo's review of this memo

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go, with conditions" stated up front, restated at the close, reason given in one sentence. |
| Lawful basis selection is justified | 3 | Correctly splits Art 6(1)(b) for the application from Art 6(1)(f) for the ranking; marks the rejection and training-data purposes as TBD rather than inventing a basis; the Art 6(4) compatibility point on repurposed retention records called out as exactly right. |
| Top actions are specific and sequenced | 3 | Named, ordered, tied to the exposure each closes; making the processor-vs-controller question a contractual deliverable in Action 3 noted as going further than his own memo. |
| Residual risks are named honestly | 3 | The explainability line ("no clear answer beyond 'the model said so'") flagged as the sharpest line in either memo — a risk he says he under-weighted in his own. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | Two gaps: no timing distinction — the memo reads as if AI Act conformity work is due inside the six weeks, when Annex III obligations don't apply until 2 Dec 2027; and "a conformity assessment before deployment" is unqualified, which could lead a client to assume a notified body is required when Annex III(4) is internal control under Annex VI. ePrivacy flagged but called "not the primary exposure" — correct on priority, but consent under Art 5(3) isn't discretionary and that should be stated plainly regardless of priority. |

**As the client, Ugo's three sentences:** Accepted, with one challenge. Action 1 is right and we will mandate recruiter review of every "not a fit" before launch — but your memo reads as though AI Act conformity work must also land inside the six weeks, and if that's wrong it changes what we can realistically commit to, so tell us plainly which obligations bite now and which bite in December 2027. Second, your retention recommendation of 6–12 months is asserted rather than justified: we hire across the EEA, expectations differ sharply by country, and we need the reasoning per jurisdiction before we can adopt a single figure.

**Response to the challenge:** Fair on both counts. The AI Act timing point is a real gap — the memo should have separated "binds now" (the GDPR/Article 22 fix) from "binds from Dec 2027" (Annex III conformity documentation), and conflating them risks the client either over-investing in the wrong six weeks or, worse, assuming the AI Act problem is solved once the December deadline is met when the Article 22 exposure is live today. On retention, agreed that 6–12 months was asserted, not derived — the correct fix is a per-jurisdiction matrix with the discrimination-claims defence as the *floor* for the shortest defensible figure, not a single EEA-wide number.

### My review of Ugo's memo (`From_Ugo_gdpr-audit-pack-ugo-ahukannah (1).md`)

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go with conditions" up front, one-sentence reason, restated at the close with the six-week caveat attached. |
| Lawful basis selection is justified | 3 | Five purposes (mine has four) — splits out the talent-pool retention purpose under Art 6(1)(a) consent and the claims-defence purpose under 6(1)(f)/6(1)(c) separately, which is more granular than my worksheet. The three-step LIA is written out explicitly and honestly concludes the balancing test *currently fails* — that's a stronger, more falsifiable claim than my own LIA reference. |
| Top actions are specific and sequenced | 3 | Same three actions in substance as mine, but Action 3 bundles the DPF-certification-scope check ("covers HR data, not just certification generally") which I didn't think to separate out — that's a real gap in vendor due diligence I missed. |
| Residual risks are named honestly | 3 | The erasure risk is sharper than mine: deleting an application doesn't remove its influence on an already-trained model, and the honest fix is retraining on a cleaned set — I treated erasure as a friction point in Section B but didn't carry it through as a residual risk in the memo itself. |
| Law stacking is addressed (AI Act / ePrivacy) | 3 | Gets the timing right (Annex III obligations from 2 Dec 2027, not inside the six weeks), correctly routes the conformity assessment to internal control under Annex VI with no notified body, and states plainly that ePrivacy consent under Art 5(3) overrides GDPR flexibility rather than hedging it as secondary. One item I can't independently verify: the Digital Omnibus Art 4a citation as a live legal basis for bias-testing special-category data — flagged below as the one concern. |

**As the client, my three sentences:** Accepted, with one concern. Your Section C cites the Digital Omnibus's new Art 4a as already providing a legal basis for bias-detection processing of special-category data — as far as I can verify, the Digital Omnibus is a Commission proposal, not yet adopted or in force, so building the bias-testing mitigation's legal basis on it is premature; until it's enacted, we need the mitigation to stand on a current Art 9(2) gateway or explicit consent, with the Omnibus noted as a future simplification rather than present law. Everything else — the Article 22 fix, the DPIA trigger under Art 35(3)(a), and the AI Act timing split — is accepted as written.

## CFU Checkpoint 5 — Debrief

**Note on the anchoring question Ugo raised:** in this exchange I only ever received the cleanly split files (the audit pack and the peer-review document separately) — I did not see an earlier mixed version, so nothing anchored my read of his memo before I wrote my own scores above.

**Where we agreed — substantively, not superficially:**

- **Bottom line:** both landed on go-with-conditions; neither of us treated it as launchable as-is or reached for stop.
- **Article 22 is the crux, and the fix is procedural:** both independently concluded the automated rejection is a solely-automated decision, that consent and contract necessity are both unsound gateways given the recruitment power imbalance, and that mandatory human review is the correct fix — not a search for a better legal basis.
- **DPIA is mandatory**, made action 2 in both memos, before first processing.
- **Article 9 by inference, not collection:** same conclusion — proxies in free-text CVs and a model trained on historical outcomes — and both of us rejected the "we don't collect that field" defence explicitly.
- **Controller/processor split**, including the same warning that the vendor becomes a controller in its own right if it reuses client data to improve its product.
- **Transfers** need SCCs plus a transfer impact assessment, or verified DPF certification.

**Where we diverged, and which reading is stronger:**

| Point | Mine | Ugo's | Stronger reading |
|---|---|---|---|
| Retention for unsuccessful applicants | 6–12 months, tied to claims-defence | Per-jurisdiction matrix, claims-defence as the floor, not a single EEA-wide figure | **His structure, my rationale.** A single number can't govern an EEA-wide employer; the claims-defence purpose is still the right floor to build the matrix from. |
| DPIA trigger | "At least four of the EDPB's nine criteria" | Six or seven criteria, plus Art 35(3)(a) making it mandatory outright | **His.** Citing Art 35(3)(a) directly means the obligation doesn't depend on how a supervisory authority scores the criteria — a more robust route to the same conclusion. |
| AI Act timing | Implied conformity work precedes launch | Annex III obligations apply from 2 Dec 2027; GDPR fixes bind the six-week window | **His.** Conflating the two clocks risks the client spending the six weeks on documentation that isn't yet due while the live Article 22 exposure goes unaddressed. |
| Conformity assessment route | "A conformity assessment before deployment" (unqualified) | Internal control under Annex VI, no notified body for Annex III(4) | **His** — the unqualified phrasing invites the client to over-procure a third-party assessment the Act doesn't require here. |
| ePrivacy | Flagged, called "not the primary exposure" | Consent under Art 5(3) is not discretionary regardless of priority | **His on the law, mine on the priority** — both points belong in the memo together. |
| Explainability as a residual risk | Named as a standing operational/reputational problem | Framed mainly as an Art 15(1)(h) access-request duty | **Mine**, per Ugo's own read — he called it the sharpest line in either memo and said he under-weighted it in his own. |
| Digital Omnibus Art 4a | Not raised | Cited as removing the Art 9 obstacle to bias testing | **Unresolved** — I've flagged this above as needing verification before it's relied on as present law, rather than accepting it outright. |

**Process note:** my transition note records that the AI Act lab repo was empty at the time of this lab, so I wrote a self-authored case instead of carrying a tier forward under Option A. Ugo flagged, correctly, that this is a consequence of our AI Act work not yet being pushed to that repo, not something to read as the prior lab having produced nothing.
