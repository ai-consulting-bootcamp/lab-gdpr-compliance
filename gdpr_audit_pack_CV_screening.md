# GDPR Audit Pack — CV Screening & Ranking (Recruitment)

**Scenario:** Case 2 — CV Screening and Ranking (Recruitment)
**Client:** National recruitment company
**Auditors:** Akansha Verma and Vincent de Paul
**Date:** 19 August 2026

---

# Part I — Audit Worksheet

## Transition Note — From EU AI Act to GDPR

This audit carries forward Case 2 — CV Screening and Ranking from the EU AI Act peer-audit exercise. Under the previous assessment, the system was classified as a high-risk AI system under Annex III(4)(a) because it is intended to be used for recruitment and candidate selection or ranking. This case is particularly relevant for a GDPR audit because the system processes candidate personal data, creates candidate rankings and profiles, and may significantly influence access to employment opportunities. The proposed human review does not remove the need to assess GDPR requirements, particularly lawful basis, purpose limitation, data minimisation, Article 22 automated decision-making, data subject rights, DPIA requirements, retention, and international transfers.

---

## Phase 1 — Fact Pattern

A national recruitment company wants to reduce the time recruiters spend screening applications for large-volume vacancies. The company proposes an AI system that analyses candidate CVs, application answers, and relevant professional information, then ranks candidates against the requirements of each vacancy. Recruiters receive a recommended shortlist together with an explanation of the factors that influenced each candidate's ranking. A recruiter reviews the shortlist before candidates are invited to interviews and has authority to reject or add candidates. The recruitment company intends to use the system across several recruitment offices and retain assessment results for future hiring campaigns. The scenario does not specify the volume of candidate data, the exact categories of professional information processed, the geographic location of candidates, the retention period, or whether any special-category data may be present in the source material. The architecture may also include a licensed CV-parsing or NLP component supplied by a third-party vendor.

---

## CFU 1 — Recognize

### Personal Data Categories

The system processes personal data contained in:

* CVs
* Application answers
* Professional information
* Candidate ranking results
* Factors contributing to the ranking
* Recommended shortlist status
* Recruiter decisions to reject or add candidates
* Assessment results retained for future campaigns

These data are linked to identifiable job applicants and therefore fall within the scope of GDPR personal-data processing.

### Special-Category Data — Article 9

The scenario does not state that special-category personal data is intentionally processed.

However, CVs and application answers may potentially contain information revealing characteristics such as health information, disability, racial or ethnic origin, religious beliefs, trade-union membership, or other Article 9 categories.

The system should therefore not assume that Article 9 data is absent merely because it is not an explicit input field.

**Assessment: TBD — privacy/legal review required to determine whether special-category data is collected, inferred, or used in the ranking process.**

### Data Subjects

The primary data subjects are job applicants and candidates.

The system therefore processes personal data in the context of recruitment and employment-related decision-making.

### Geographic Scope

The scenario describes a national recruitment company and several recruitment offices, but does not specify the country or countries involved.

**Assessment: TBD — confirm the relevant EU/EEA jurisdictions and whether any candidates are located outside the EU/EEA.**

### Automated Decision-Making

The system automatically analyses candidate information and ranks candidates against vacancy requirements.

However, the scenario states that a recruiter reviews the recommended shortlist before candidates are invited to interviews and that recruiters can reject or add candidates themselves.

The available facts therefore do not establish that the AI system makes the final recruitment decision by itself.

Nevertheless, the system materially influences the recruitment process because its ranking determines the recommended shortlist presented to recruiters.

The applicability of GDPR Article 22 should therefore be assessed carefully, including whether any recruitment decision produces legal or similarly significant effects on candidates and whether the human review is genuinely meaningful rather than merely formal.

**Assessment: TBD — legal/privacy review required before deployment.**

### Future Campaign Reuse

The proposed retention of candidate assessment results for future hiring campaigns creates a specific purpose-limitation and retention question.

Candidate information collected for one vacancy cannot automatically be assumed to be appropriate for unrestricted reuse in future recruitment campaigns.

The audit must establish:

1. The original purpose for which the candidate data was collected.
2. Whether future recruitment campaigns are compatible with that original purpose.
3. Whether candidates were informed about future reuse.
4. What data will be retained.
5. For how long it will be retained.
6. Whether the candidate can object to or request deletion of the retained information.
7. Whether old assessment results will be reused to rank candidates against substantially different vacancy requirements.

**Initial assessment: Significant privacy risk requiring further analysis.**

---

## Phase 2: Mini GDPR Audit Worksheet

### Section A — Data Map

| Field | Answer |
|---|---|
| **Categories of personal data** | Identity data (name, contact details), employment/professional history, education and qualifications, free-text application answers, CV file content, derived data (ranking score, factor explanations), possibly inferred data (e.g. career gaps, seniority signals) |
| **Sources** | Directly from applicants (CV upload, application form); potentially third-party sources if the system pulls professional profile data (e.g. LinkedIn) — needs confirmation |
| **Purpose(s) — one row per purpose** | (1) Screening and ranking candidates for a specific vacancy; (2) generating an explanation of ranking factors for recruiter review; (3) retaining assessment results for reuse in future hiring campaigns |
| **Lawful basis per purpose** | (1) Screening/ranking for the current vacancy: **contract** (necessary steps prior to entering an employment contract, Art. 6(1)(b)) — but only for the employer's own recruitment; for the recruitment company acting on the employer's behalf, this may instead rest on **legitimate interests** (LIA) since the recruitment company itself isn't going to employ the candidate. (2) Explanation output: same basis as (1), as it's part of the same processing activity. (3) Retention for future campaigns: **TBD — legal review** (candidate consent is one possible basis, since reusing someone's data for a different, future vacancy is a new purpose not covered by the original application) |
| **Retention period per purpose** | Current vacancy screening: length of the recruitment process + defined post-decision window (e.g. for potential discrimination claims). Future-campaign retention: **TBD — legal review**; requires a specific, bounded retention period and a distinct lawful basis, not indefinite storage |
| **Recipients and sub-processors** | Employer clients (recipients of the shortlist); the AI vendor/developer of the screening tool (processor, if the recruitment company built or licensed it); potentially a cloud hosting provider |
| **International transfers and transfer mechanism** | None confirmed yet — flagged as **TBD pending vendor due diligence.** If the AI vendor or hosting infrastructure is non-EU, an Art. 46 transfer mechanism (SCCs) plus a transfer impact assessment would be required |

For the lawful basis column: where legitimate interests is proposed, the three-step test is: (1) purpose — efficient, consistent shortlisting at scale; (2) necessity — is AI screening necessary or would a simpler method serve the same purpose; (3) balancing — the applicant's interest in not being algorithmically ranked without transparency must be weighed against the recruiter's efficiency interest, especially given the power imbalance in a job application.

### Section B — Risk and Rights

**Are any special-category data present or inferable from the outputs (Article 9)?**
Special-category data isn't directly requested, but it can be *inferred* — CVs and free-text answers can reveal health information (career gaps, disability disclosures), religious observance (holidays, affiliations), or other Article 9 categories through proxy signals the model picks up on. This inference risk needs explicit testing, not just an assumption that it won't happen.

**Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?**
Article 22 restricts decisions "based solely on automated processing" that produce legal or similarly significant effects. Being excluded from a shortlist for a job can qualify as "similarly significant." The safeguard here is whether recruiter review is *meaningful* — a recruiter who reflexively approves AI-ranked shortlists without genuine authority or capacity to override does not count as meaningful human involvement, and the processing would then fall inside Article 22's restriction. This needs to be tested in practice (e.g. override rates, time recruiters spend per shortlist), not assumed from the design document.

**Is a DPIA required? Use the EDPB's nine criteria.**
Yes, a DPIA is required. At minimum it meets: (1) evaluation/scoring of individuals; (2) automated decision-making with legal/significant effect (or borderline, per above); (3) systematic monitoring, arguably, if assessment data is retained and reused across campaigns; (4) use of new technologies (AI ranking model) at scale. Any one of these can trigger a DPIA under the EDPB criteria; this scenario likely meets three or four.

**What data subject friction points are most likely?**
Right of access (candidates asking why they weren't shortlisted, and for the ranking rationale); right to object to profiling; right to erasure, especially for candidates who want their data removed from the future-campaign retention pool after being rejected.

**What is the controller/processor split?**
The recruitment company is a **controller** for the screening and shortlisting activity, since it determines the purposes and means. The employer client is likely a **joint controller** or a separate controller for the ultimate hiring decision. The AI vendor is a **processor**, acting only on the recruitment company's instructions — unless the vendor also uses applicant data to improve its own model, in which case it becomes a controller for that secondary purpose and needs its own lawful basis.

**Is a DPA needed with any vendor? Which ones?**
Yes — a DPA is needed with the AI screening vendor (processor) covering the processing of CVs and application data, and with any hosting/cloud provider that stores this data.

### Section C — Law Stacking

- **AI Act cross-check:** This system falls into the **high-risk** tier (Annex III, employment/recruitment). The AI Act adds obligations GDPR doesn't directly cover: a mandatory risk management system, technical documentation, human oversight design requirements, accuracy/robustness testing, and registration in the EU high-risk AI database — these are additive, not substitutes for the DPIA.
- **ePrivacy check:** No cookies or tracking pixels are indicated in this scenario as described (this is an internal screening tool, not a public-facing web tracker), so ePrivacy is not directly triggered — flag as N/A unless the application portal itself uses tracking technology.
- **Data Act check:** N/A — no connected product or cloud-switching data is involved in this scenario.

---

## Phase 3: Client Recommendation Memos

### Akansha's memo

**To:** National Recruitment Company
**Re:** GDPR readiness — AI-assisted CV screening and ranking system
**From:** Akansha Verma

**Bottom line: Go, with conditions.** The system is workable under GDPR, but three gaps need to close before any live candidate data flows through it — the current design leaves the human-oversight question and the future-campaign retention purpose unresolved, and both carry real regulatory exposure.

**Top three actions:**

1. **Resolve the Article 22 question before launch.** Define and document what "meaningful human review" looks like in practice — recruiter authority, time allocated, and override tracking — and build in monitoring so you can prove, not just assert, that the shortlist isn't a rubber-stamped automated decision. If you can't guarantee meaningful review, you'll need an alternative Article 22 safeguard (e.g. an explicit right for candidates to contest the outcome and request human intervention).
2. **Complete a DPIA before the system processes its first live application.** This isn't optional — the scoring, profiling, and scale of this system trigger at least three of the EDPB's nine criteria. Build the DPIA around the recruitment-specific risks: discriminatory inference, opacity of ranking factors, and re-use of historic assessment data.
3. **Separate out the future-campaign retention purpose and give it its own lawful basis.** Screening for a specific vacancy and reusing a candidate's data for future, unrelated vacancies are two different purposes. The first can likely rest on contract/legitimate interests; the second almost certainly needs a fresh, informed consent from the candidate, with a clear opt-out and a defined retention limit — not indefinite storage "for future hiring campaigns."

**Residual risks (even with the above in place):**

- **Inferred special-category data.** Even a well-designed model can pick up proxy signals for health, religion, or other protected characteristics from free-text CVs. This risk can be reduced through testing and monitoring, but not fully eliminated — plan for ongoing bias/inference audits, not a one-time check.
- **Multi-jurisdiction inconsistency.** Running this across several regional offices means local recruiters may apply the "meaningful review" standard inconsistently. Central governance can reduce this but human variability across offices is a standing risk.
- **Vendor dependency.** If the AI screening tool is provided by a third party, you're relying on their model behaviour and any future changes to it. A DPA governs data handling, but it can't fully control model drift or retraining decisions made on the vendor's side — build in a review clause and require advance notice of material model changes.

### Vincent's memo

**To:** National Recruitment Company
**Subject:** GDPR assessment — AI CV Screening and Ranking
**From:** Vincent de Paul

**Bottom line: Go with conditions.** The system should not enter production until its lawful bases, DPIA, Article 22 position, data-retention rules, and vendor and international-transfer arrangements have been documented and verified.

The proposed system analyses CVs, application answers and professional information to rank candidates and generate recommended shortlists. Because the rankings may materially influence access to employment opportunities, the company needs controls that address both GDPR compliance and the risks created by profiling and AI-supported recruitment.

**Top four actions before go-live:**

1. **Establish the lawful basis and complete the DPIA.** Document the Article 6 basis for each purpose, including the three-step legitimate-interests test if that basis is considered. Complete the DPIA and document the Article 22 assessment, including whether recruiter intervention is genuinely meaningful.
2. **Implement candidate-data governance.** Define retention periods for current recruitment and future-campaign reuse, document purpose compatibility, update transparency information, establish deletion rules, and determine how candidates can exercise applicable access, erasure and objection rights.
3. **Separate out the future-campaign retention purpose and treat its lawful basis as open pending legal review.** Screening for a specific vacancy and reusing a candidate's data for future, unrelated vacancies are two different purposes. The first can likely rest on contract/legitimate interests. The second is **TBD — legal review**: consent is a plausible outcome, but the correct basis depends on candidate expectations, purpose compatibility, and applicable national law, and shouldn't be asserted before that analysis is complete. Whatever basis is selected, it needs its own transparency notice and a defined retention limit — not indefinite storage "for future hiring campaigns."
4. **Complete vendor and transfer controls.** Identify every vendor processing candidate data, confirm controller/processor roles, put Article 28 DPAs in place where required, and verify processing locations and any Chapter V transfer mechanism before non-EU/EEA transfers occur.

*Note: Action 3 was revised after peer review — see the Peer Verification Record below — to reflect TBD — legal review rather than asserting consent, consistent with the Phase 5 debrief conclusion. Action 4 (vendor and transfer controls) is retained from the original draft so the bottom line's reference to vendor and transfer arrangements is actually covered by an action.*

**Residual risks:** Even after these controls are implemented, residual risks remain. The ranking model may produce inaccurate or biased results, historical assessment data may become unsuitable for a different vacancy, and candidates may challenge profiling or decisions influenced by the system. Special-category information may also be present or inferred from candidate material despite controls designed to minimise its use.

**Recommendation:** Proceed only as a **conditional go-live**. The organisation should verify the required GDPR controls before production deployment and periodically reassess the system as its use, vendors, vacancies, or data sources change.

---

## Phase 4: Partner swap and peer review

### Peer Review — Reviewer: Vincent de Paul (of Akansha's memo)

| Criterion | Score (1–3) | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go, with conditions" is stated in the first sentence with the reason attached — the human-oversight and retention gaps carry regulatory exposure. No hunting required. |
| Lawful basis selection is justified | 3 | Strongest part of the memo. Action 3 proposes a specific split — contract/legitimate interests for current-vacancy screening, consent for future-campaign reuse — with reasoning for why the two purposes can't share a basis. Gives legal something concrete to confirm or push back on. |
| Top actions are specific and sequenced | 3 | Each action names a mechanism, not just a task — recruiter authority, time allocated, override tracking; opt-out and retention limit for consent. These read as decisions, not to-dos. |
| Residual risks are named honestly | 2 | Explicitly says bias risk "can be reduced... but not fully eliminated" rather than implying controls solve it. Could go one step further by naming a concrete inference pathway rather than staying at "proxy signals for health, religion." |
| Law stacking is addressed (AI Act / ePrivacy) | 1 | The gap. The worksheet correctly identifies Annex III(4)(a) high-risk status, but that never appears in the memo. A reader of the memo alone wouldn't know this system triggers AI Act obligations at all, only GDPR ones. |

**As the client:** The lawful-basis split and Article 22 action plan are exactly what my legal team needs — I can hand this to them today. One concern: my compliance team specifically asked whether this counts as "high-risk" under the AI Act, and this memo doesn't answer that. Can you add one line stating the classification and what it adds on top of the GDPR controls already listed?

### Peer Verification Record — Reviewer: Akansha Verma (of Vincent's memo)

**Date:** 19 August 2026

**1. Did the reviewer accept the recommendation?**
**Yes.** The reviewer accepted the overall **"Go with conditions"** recommendation.

The reviewer agreed that the system is workable under GDPR but should not process live candidate data until the key compliance gaps are resolved.

**2. Finding challenged by the reviewer**
The reviewer challenged the level of certainty around two areas:

* **Article 22 / meaningful human review:** The audit should not simply state that a recruiter is present in the process. It should define and document what meaningful human intervention means in practice, including recruiter authority, time for review, ability to override the AI ranking, and evidence of actual overrides.
* **Future-campaign reuse:** The reviewer agreed that reuse for future vacancies must be treated as a separate purpose with its own lawful-basis analysis, retention limit and transparency requirements. The reviewer suggested fresh informed consent for unrelated future campaigns.

**Audit response:** The first point is accepted and should be strengthened. For future-campaign reuse, the audit will not automatically conclude that consent is legally mandatory. The appropriate Article 6 basis remains **TBD — legal review**, because the correct basis depends on the purpose, candidate expectations, compatibility of further processing, applicable national law and the specific recruitment relationship.

**3. Requested redesign or clarification**
The reviewer requested that the system design and audit controls be strengthened in three areas:

1. Define measurable **meaningful human review** controls, including recruiter override authority, review time and override tracking.
2. Complete the **DPIA before the first live candidate data is processed**, addressing profiling, discrimination, opacity, special-category inference and historical assessment reuse.
3. Separate **future-campaign reuse** from the original recruitment purpose and establish a specific lawful-basis, transparency, retention and deletion framework before enabling reuse.

**4. Reviewer comments**
The reviewer identified three residual risks that remain even if the recommended controls are implemented:

* **Inferred special-category data:** The model may identify proxy signals relating to health, religion or other protected characteristics from free-text CVs. Testing and monitoring can reduce this risk but cannot necessarily eliminate it.
* **Multi-jurisdiction inconsistency:** Recruiters across different offices may apply meaningful human review differently. Central governance and documented procedures are therefore required.
* **Vendor dependency:** A third-party AI or CV-processing vendor may change model behaviour over time. A DPA alone does not eliminate model-drift or vendor-change risks, so contractual review and advance-notice requirements should be considered.

---

## Phase 5: Debrief

### Points of Agreement
* **DPIA is required.** Both audits reached this conclusion independently and without hedging — both pointed to evaluation/scoring of individuals, automated decision-making, and the scale of impact on employment access as the triggering factors. Neither treated this as deferrable past go-live.
* **Article 22 is the central open question.** Both audits treated "is recruiter review meaningful" as something that has to be demonstrated — through recruiter authority, override tracking, and documented process — rather than assumed from the system's design description.
* **Future-campaign reuse is a distinct purpose.** Both audits agreed that reusing candidate data for future, unrelated vacancies cannot ride on the lawful basis established for the current screening. Whatever basis is ultimately chosen, it needs its own purpose definition, transparency notice, and retention limit.
* **AI Act high-risk classification.** Both worksheets identified the system as high-risk under Annex III(4)(a), and agreed this adds obligations (risk management, technical documentation, human oversight design, logging) on top of — not instead of — the GDPR analysis.

### Points of Divergence

| Point | Vincent's position | Akansha's position |
|---|---|---|
| Lawful basis for current-vacancy screening | Legitimate interests, pending completion of the LIA test | Contract or legitimate interests could both potentially apply |
| Lawful basis for future-campaign reuse | Fresh, informed consent with opt-out and retention limit (later revised — see below) | TBD — legal review, not automatically consent |
| Action framing in the memo | Actions written as decisions/mechanisms | Actions written as workstream instructions ("complete," "establish," "document") |
| AI Act visibility | Correctly identified in worksheet but not carried into either memo initially | Same gap, corrected in final agreed position below |

### Lawful Basis Discussion

**Vincent's original position:** For each processing purpose, the lawful basis should be established separately. Legitimate interests may potentially be relevant to recruitment screening, but only after completing the three-step LIA test — legitimate purpose, necessity, and balancing. Contractual necessity should not be assumed simply because a candidate has submitted an application. Future-campaign reuse initially proposed fresh, informed consent, with a clear opt-out and a defined retention limit.

**Akansha's position:** Screening for a specific vacancy could potentially rely on contract or legitimate interests, while future-campaign reuse should remain **TBD — legal review** until the purpose, candidate expectations, and applicable legal framework are confirmed, rather than defaulting to consent as the assumed answer.

**Agreed position:** The stronger reading is to keep the lawful basis for future-campaign reuse as TBD — legal review, rather than defaulting to consent as the assumed answer. Consent is a plausible outcome, but naming it prematurely risks the same error the audit is trying to avoid elsewhere — asserting a basis before the necessity and balancing work is done. Both audits agree, regardless of which basis is ultimately chosen, that future reuse must have its own defined purpose, its own transparency measures, and its own retention limit, and that if consent is the outcome, it must independently satisfy GDPR's validity requirements — freely given, specific, informed, and unambiguous, with a genuine opt-out that doesn't disadvantage candidates who decline. Vincent's memo has been revised to reflect this agreed position.

### DPIA Discussion

Both audits agreed a DPIA is required before the system processes any live application, and both converged on largely the same triggering criteria: evaluation or scoring of individuals, automated decision-making with potential legal or similarly significant effect, and the scale/significance of impact on access to employment opportunities. Where the audits added value differently: Akansha's audit specified the DPIA should be structured around three recruitment-specific risks — discriminatory inference from CV text, opacity of the ranking factors shown to recruiters, and reuse of historic assessment data — while Vincent's worksheet more explicitly enumerated the EDPB criteria being met (evaluation/scoring, systematic monitoring, vulnerable data subjects, automated decision-making). The agreed approach is to combine both: use Vincent's criteria-mapping to justify that a DPIA is required, and Akansha's structure to organize what the DPIA actually investigates.

### Reviewer Comments

**On Akansha's memo (reviewed by Vincent):** The lawful-basis split and Article 22 action plan were assessed as strong enough to hand directly to legal for drafting. The gap flagged was the AI Act classification missing from the memo itself, despite being correctly identified in the worksheet.

**On Vincent's memo (reviewed by Akansha):** The bottom line and data-governance actions were concrete enough to act on. The gap flagged was the same in reverse — lawful basis stayed at "TBD" through both drafts without a working hypothesis, and the AI Act classification didn't survive from worksheet to memo either.

**Shared finding:** In both cases, the worksheet analysis was stronger than what reached the client-facing memo. The recurring failure mode wasn't the underlying legal reasoning — it was analysis not fully carrying through to the document the client actually reads.

### Final Debrief Conclusion

The two audits agreed on every major trigger — DPIA necessity, the Article 22 meaningful-review test, the need to treat future-campaign reuse as a separate purpose, and the AI Act high-risk classification — which suggests the underlying legal analysis was sound on both sides rather than a coincidence of independent guessing. The genuine divergence was about how much certainty to assert in writing: Vincent's audit initially leaned toward staking a provisional consent position so the client has something concrete to react to, while Akansha's audit leaned toward preserving TBD until the underlying test is actually completed. On lawful basis for current screening, staking a position was more useful to the client. On lawful basis for future reuse, preserving TBD was the stronger call, since asserting consent prematurely would have repeated the exact error the review process was designed to catch — which is why Vincent's memo was revised. The combined takeaway for the final audit pack: assert a position wherever the reasoning is far enough along to support one, keep TBD wherever it isn't, and make sure whatever the worksheet correctly identifies — especially the AI Act classification — actually makes it into the memo the client reads.

---

## Reinforcement Notes

**DPIA outline (most sensitive activity: automated ranking of candidates)**
- *Description of processing:* CVs and application answers ingested, features extracted, candidates scored/ranked per vacancy, shortlist + explanation surfaced to recruiter.
- *Necessity and proportionality:* Is AI ranking necessary at this volume, or would keyword filtering / manual triage suffice for smaller vacancy pools? Document why the chosen approach is proportionate to the volume problem it solves.
- *Risk identification:* discriminatory bias in ranking; opacity of "explanation" factors to candidates; re-identification risk in retained assessment data; Article 22 exposure if review isn't meaningful.
- *Proposed mitigation:* bias testing pre-launch and on a recurring schedule; plain-language explanation surfaced to candidates on request; retention limits and pseudonymisation for archived assessments; documented recruiter override authority and tracking.

**One DPA clause to prioritise with the AI vendor:**
A clause restricting the vendor from using applicant CVs or application data to train or improve its underlying model beyond the recruitment company's own instance — otherwise the vendor becomes a controller for that secondary purpose, and the recruitment company has effectively authorised a use it never disclosed to candidates.

**If the client also serves UK data subjects:**
The bottom-line recommendation doesn't change, but the compliance mechanics do: UK GDPR runs in parallel to EU GDPR post-Brexit, so transfers of UK candidate data to the EU (or to any non-UK vendor) need their own UK-specific transfer assessment, and the ICO — not an EU supervisory authority — becomes the relevant regulator for UK data subjects' complaints. The DPIA and Article 22 analysis are largely portable, but the paperwork needs a UK-facing version.

---

## Stretch: Data Protection by Design Checklist — Automated CV Ranking

| Item | Status |
|---|---|
| Data minimisation — is only the minimum necessary data collected? | **Unknown** — needs confirmation on whether third-party profile data (e.g. LinkedIn) is pulled beyond what's submitted |
| Purpose binding — is data technically restricted to the stated purpose? | **Fails (currently)** — future-campaign reuse isn't yet separated from current-vacancy screening at a technical/access level |
| Access controls — is access limited to those who need it? | **Unknown** — needs confirmation on cross-office access to candidate data |
| Retention enforcement — automated deletion or anonymisation policies? | **Fails (currently)** — no defined retention limit for the future-campaign data pool |
| Subject rights workflow — can the client respond within 30 days? | **Unknown** — no confirmed process for candidates requesting access to their ranking rationale |
| Incident response — documented breach detection/72-hour notification process? | **Unknown** — not addressed in the scenario as described; needs confirmation from the client's security team |
