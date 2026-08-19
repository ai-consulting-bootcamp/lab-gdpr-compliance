# GDPR Audit Pack - Kimia Asgari

## Transition Note

This audit continues from the EU AI Act lab. The case carried forward is **Case 1 — Loan Applicant Scoring Tool**, submitted by my partner in the AI Act lab and reviewed by me as consultant. That case was classified as **High-risk under Annex III, point 5(b)** (creditworthiness and credit scoring), with a critical Article 14 human-oversight defect (auto-rejection with zero human review). It is the most interesting case for GDPR purposes because it combines financial data with social media activity and browsing history — a combination that raises Article 9 special-category inference risk, Article 22 automated-decision-making concerns, and a likely international transfer, all in one system.

---

## Setup / first run

**Document title:** GDPR Audit Pack - Kimia Asgari
**Sections:** Audit worksheet (below) and Client recommendation memo (Phase 3)

### Fact Pattern

A retail bank operating in Germany is piloting an AI-based loan application scoring tool. The tool ingests each applicant's financial data (income, existing debts, credit history) alongside social media activity and browsing history collected via an optional social login and a third-party data broker. Data subjects are prospective retail banking customers located in Germany and other EU member states. The scoring engine is licensed from a US-based fintech vendor, which hosts and processes the data on cloud infrastructure in the United States. The AI model outputs a binary risk flag that currently triggers automatic rejection of "high-risk" applicants with no human review before the decision is communicated.

---

## Expected output of first step

The fact pattern above identifies: financial data, social/behavioral data, EU-based data subjects, a US vendor in the stack, and an AI system that scores and auto-rejects loan applicants. This is the shared ground the rest of the audit builds on.

---

## CFU checkpoints

### 1. Recognize

- **Categories of personal data present:** Identification data (name, contact details), financial data (income, debts, repayment history), behavioral data (browsing history via cookies/tracking), and social media activity data.
- **Special-category data (Article 9):** Not directly collected, but plausibly **inferable** — social media activity can reveal political opinions, religious beliefs, trade union membership, or sexual orientation, even without the bank intending to collect it. This inference risk must be treated as if Article 9 data is present until ruled out.
- **EU border crossing:** Yes — the scoring engine is hosted and processed by a US-based vendor, meaning applicant data leaves the EU/EEA.

### 2. Apply

See full worksheet in Phase 2 below.

### 3. Integrate

See client recommendation memo in Phase 3 below.

### 4. Verify

See Phase 4 — Partner swap and peer review below.

### 5. Debrief

See closing comparison notes at the end of Phase 4.

---

## Core

### Phase 1: Build the fact pattern

Transition note and fact pattern completed above (see **Transition Note** and **Setup / first run**).

### Phase 2: Mini GDPR audit worksheet

#### Section A — Data map

| Field | Your answer |
|---|---|
| Categories of personal data | Identification data (name, contact); financial data (income, debts, repayment/credit history); behavioral data (browsing history, cookies); social media activity data |
| Sources (where data comes from) | Financial data: direct from applicant (loan form) + credit bureau (e.g. SCHUFA); social media: optional social login; browsing history: third-party ad-tech/analytics broker |
| Purpose(s) — one row per purpose | (1) Assess creditworthiness for loan approval decision; (2) fraud/risk scoring |
| Lawful basis per purpose — or `TBD — legal review` | (1) Contract (Art. 6(1)(b)) — necessary to enter into the loan contract at the applicant's request, for core financial data only; (2) social media + browsing enrichment: `TBD — legal review` — likely legitimate interests, but proportionality is questionable and an LIA has not been documented |
| Retention period per purpose | Core financial application data: per German banking/tax retention rules (typically ~10 years); social media/browsing enrichment data: `TBD — legal review`, should be minimized and retained only as long as needed for the specific scoring run |
| Recipients and sub-processors | Credit bureau (e.g. SCHUFA); US-based scoring vendor (sub-processor); third-party social/browsing data broker |
| International transfers and transfer mechanism | Yes — transfer to US-based vendor for hosting/processing. Mechanism: `TBD — legal review` to confirm whether the vendor is certified under the EU-US Data Privacy Framework or relies on Standard Contractual Clauses (SCCs) |

For the lawful basis column, the six Article 6 options were considered: consent, contract, legal obligation, vital interests, public task, legitimate interests. Legitimate interests was flagged as the most plausible basis for the social/browsing data, but it requires a documented three-part LIA (purpose, necessity, balancing) that does not yet exist.

#### Section B — Risk and rights

- **Special-category data (Article 9):** Not directly collected, but plausibly inferable from social media content (political opinions, religion, sexual orientation). This must be treated as a live risk, not dismissed because the bank does not explicitly request such data.
- **Automated decision-making (Article 22):** Yes. The current design auto-rejects applicants with no human review — this is a decision based solely on automated processing that produces a legal effect (denial of credit). As currently designed, **no valid safeguard is in place**: there is no human intervention, no clear path to contest the decision, and no explanation mechanism. This is a compliance gap, not a borderline case.
- **Is a DPIA required?** Yes — multiple EDPB criteria are met: (1) systematic and extensive evaluation/scoring of individuals; (2) automated decision-making with legal effect; (3) potential special-category or highly personal data via inference; (4) likely large-scale processing given bank-wide loan volume; (5) innovative use of technology (AI scoring); (6) matching/combining datasets from different sources (financial + social + browsing) in a way applicants would not reasonably expect. Meeting two or more criteria makes a DPIA mandatory under Article 35; this scenario meets at least four.
- **Most likely data subject friction points:** Right to object to profiling (Article 21) — applicants are unaware profiling is occurring; right to an explanation of automated decision logic (Article 15 + Article 22(3)); right of access, since applicants do not currently see their own score or the data behind it.
- **Controller / processor split:** The bank is the data controller (determines purposes and means). The US scoring vendor is a processor (or potentially a joint controller if it independently determines how social/browsing data is weighted — this needs contractual clarification). The social/browsing data broker is a processor if acting solely on the bank's instructions, or a separate controller if it determines its own purposes for collecting the data.
- **Is a DPA needed?** Yes — with the US scoring vendor and with the data broker, if not already in place.

#### Section C — Law stacking (one line each)

- **AI Act cross-check:** High-risk under Annex III, point 5(b) (credit scoring). The AI Act adds obligations GDPR does not cover on its own: conformity assessment, technical documentation, a mandatory Fundamental Rights Impact Assessment (FRIA) under Article 27, and Article 14's genuine human-oversight requirement — which is the same underlying defect Article 22 GDPR flags, but the AI Act requires it as a structural, documented control rather than only an individual right to contest.
- **ePrivacy check:** Yes — browsing history is collected via cookies/tracking technology. ePrivacy's prior-consent requirement applies to that collection and **cannot** be substituted with a GDPR legitimate-interests basis; this is a separate legal gate that must be satisfied independently.
- **Data Act check:** N/A — no connected product, IoT device, or cloud-switching data is involved in this scenario.

### Phase 3: Write the client recommendation memo

**To:** Legal & Compliance, [Bank Name]
**From:** Kimia Asgari, AI Consultant
**Re:** Loan Applicant Scoring Tool — GDPR & AI Act Audit Findings

**Bottom line: Go, with conditions.** The underlying use case — using AI to support credit scoring — is legitimate and regulatable, not prohibited. But the system cannot launch as currently designed. The combination of a missing human-oversight step (Article 22 GDPR / Article 14 AI Act) and an undocumented lawful basis for the social/browsing data creates real legal exposure, both in terms of individual complaints and regulatory fines.

**Top three actions, in order:**

1. **Insert mandatory human review before any rejection is finalized.** No applicant should be auto-rejected without a human loan officer reviewing the case, particularly borderline or negative scores. This single change resolves the Article 22 gap and moves the AI Act's Article 14 oversight requirement from "missing" to "present," and it should be built before any further work continues.
2. **Document a Legitimate Interests Assessment (LIA) for the social media and browsing data — or drop it.** Right now, using this data has no documented lawful basis. Either commission a proper three-part LIA (purpose, necessity, balancing) that can withstand regulator scrutiny, or remove these signals from the scoring model until that documentation exists. Given the proportionality concerns already flagged, we recommend seriously considering removal.
3. **Confirm and document the international transfer mechanism with the US vendor** — either Data Privacy Framework certification or Standard Contractual Clauses — before any further applicant data is processed through that pipeline. This is currently an open gap with no fallback if challenged.

**Residual risks, even after these actions:**

- Inferred special-category data (political opinions, religion, sexual orientation) from social media cannot be fully eliminated by process fixes alone; some residual Article 9 exposure remains as long as social data feeds the model at all.
- A DPIA has not yet been conducted. Until it is completed and any high residual risk is either mitigated or referred to the supervisory authority, the system carries regulatory risk beyond what these three actions alone resolve.
- Even with human review in place, "rubber-stamp" oversight is a real operational risk if loan officers are incentivized by volume — the human-in-the-loop control is only as strong as how it is actually used day to day, not just how it is documented.

We recommend a follow-up engagement to draft the full DPIA and the LIA before go-live.

### Phase 4: Partner swap and peer review

**Reviewer:** Nelly Pourmehr

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go, with conditions" is stated in the first line with a one-sentence reason. No hedging. |
| Lawful basis selection is justified | 3 | Contract basis for financial data is justified in one line. Legitimate interests for social/browsing data is correctly flagged as TBD, not guessed at. |
| Top actions are specific and sequenced | 3 | All three actions name a concrete step and an order. Action one names the exact fix (human review before rejection is finalized). |
| Residual risks are named honestly | 3 | The DPIA gap and the "rubber-stamp" review risk are both named directly, not softened. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | AI Act and ePrivacy are both covered in the worksheet, but the memo itself does not carry the ePrivacy consent gate into the top three actions. It should appear as a fourth flag or be folded into action two. |

**Client response:** Accept the bottom line and the first two actions as written. One concern: the memo does not tell us what happens to the ePrivacy consent gap before launch. Cookie consent for the browsing data feed needs its own line item, not just a mention in the worksheet. Please add it as an explicit action or confirm it is covered inside action two.

Full peer review on record in [`Peer-Review-Kimia-Asgari.md`](./Peer-Review-Kimia-Asgari.md).

### Debrief

Nelly and I ran the same fact pattern independently. Comparing the two audits:

**Where we agree:**
- Both audits land on Contract (Article 6(1)(b)) for core financial data, and flag legitimate interests as TBD for social/browsing data pending an LIA.
- Both flag Article 22 as an active violation, not a borderline case — the auto-rejection has zero human review.
- Both call the DPIA mandatory, citing overlapping EDPB criteria (systematic scoring, automated legal effect, inferred special-category data, novel data combination).
- Both memos reach the same bottom line — go, with conditions — and both name human review as action one.
- Both flag the ePrivacy consent gate as independent from GDPR's legitimate-interests basis, though in both cases this stayed in the worksheet and didn't fully carry into the memo's top three actions — a shared gap worth fixing in a real engagement.

**Where we diverge:**
- Nelly's memo weights removal of the social/browsing data more heavily as the default position while the LIA is pending. My memo also flags removal but frames it as the fallback if the LIA can't be justified, treating the LIA path as the first option to exhaust. Her framing puts the burden of proof on keeping the data; mine puts it on documenting it first. I think her framing is actually the stronger one — it forces the "necessity" question up front rather than defaulting to build first, document later.
- My residual risk section leans harder on the "rubber-stamp" review risk as an operational, ongoing concern rather than a one-time design fix. Nelly's memo picked this up in her own debrief and proposed carrying it forward as a named monitoring step, not just a caution — I'm adopting that framing going forward.
- My worksheet leaves the data broker's controller/processor status as an open contractual question; Nelly's read is the same but she'd push to resolve it before any broker feed goes live rather than flag it as a pending risk. Her position is more actionable and I'd apply it in a real engagement.

**Stronger reading overall:** Nelly's "resolve before build" posture — on both the data broker contract and the necessity case for behavioral data — is the stronger consulting instinct here. My audit tends to sequence documentation before restriction; hers sequences restriction before documentation when the case for necessity is weak. For a first-pass client memo, her ordering reduces regulatory exposure faster.

---

## Reinforce

**DPIA outline (most sensitive processing activity: credit scoring using social/browsing data):**
- Description of processing: automated scoring of loan applicants combining financial, social media, and browsing data to produce a risk flag.
- Necessity and proportionality: financial data is clearly necessary for creditworthiness assessment; social/browsing data's necessity is unproven and should be the central question of the DPIA.
- Risk identification: discriminatory outcomes from proxy variables in social/browsing data; inferred special-category data; lack of transparency to data subjects; automated rejection with no recourse.
- Proposed mitigation: remove or strictly justify social/browsing inputs; mandatory human review; clear applicant-facing explanation of scoring logic; regular bias audits.

**One clause to request in the DPA with the US vendor:** A data-processing-location and sub-processor-disclosure clause requiring the vendor to notify the bank of any change in processing location or new sub-processors before it takes effect — this is essential because the current transfer mechanism has not yet been confirmed, and any silent change in where data is processed could invalidate whatever mechanism is eventually put in place.

**If the client also serves UK data subjects:** The bottom-line recommendation would need a parallel UK GDPR lawful-basis and international-transfer analysis, since the UK is a separate adequacy jurisdiction post-Brexit. The DPA would need to reference both the EU SCCs (or DPF) and the UK's International Data Transfer Agreement (IDTA) or UK Addendum, since a single EU-only transfer mechanism does not automatically cover UK data subjects.

---

## Stretch — Data Protection by Design Checklist (Credit Scoring Activity)

| Item | Status |
|---|---|
| Data minimisation — only minimum necessary data collected | **Fails** — social/browsing data collection is broader than demonstrated necessity |
| Purpose binding — data technically restricted to stated purpose | **Unknown** — no evidence of technical purpose-limitation controls on the social/browsing data pipeline |
| Access controls — access limited to those who need it | **Unknown** — not documented in the fact pattern; flag for follow-up |
| Retention enforcement — automated deletion/anonymisation policies | **Fails** — no defined retention period exists for social/browsing enrichment data |
| Subject rights workflow — can respond to access/erasure requests within 30 days | **Unknown** — no evidence of an operational workflow for this system specifically |
| Incident response — documented process to detect/notify breach within 72 hours | **Unknown** — likely exists at the bank level generally, but not confirmed for this specific vendor integration |
