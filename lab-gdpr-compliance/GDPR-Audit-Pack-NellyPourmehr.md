# GDPR Audit Pack - Nelly Pourmehr

## Transition Note

This audit carries forward from the EU AI Act lab. The case is **Case 1 - Loan Applicant Scoring Tool**. In that lab, this case was classified as **High-risk under Annex III, point 5(b)** (creditworthiness and credit scoring). The critical defect found was under **Article 14**: the system auto-rejects applicants with zero human oversight.

This is the strongest case for a GDPR audit because it mixes financial data with social media and browsing data. That mix raises three separate GDPR issues at once: possible special-category inference (Article 9), automated decision-making with legal effect (Article 22), and a likely international data transfer.

My partner for this lab is Kimia Asgari. She ran her own GDPR audit on the same case. I reference her findings in the debrief section below.

---

## Setup / First Run

**Document title:** GDPR Audit Pack - Nelly Pourmehr
**Sections:** Audit worksheet (below) and Client recommendation memo (Phase 3)

### Fact Pattern

The client is a retail bank operating in Germany and other EU member states. The bank is piloting an AI tool that scores loan applicants for creditworthiness. The tool uses three data sources: the applicant's financial data (income, debt, repayment history), social media activity collected through an optional social login, and browsing history supplied by a third-party ad-tech vendor. Data subjects are prospective retail loan customers located in the EU. The scoring model runs on a US-based vendor's cloud infrastructure. The tool outputs a binary flag. Applicants flagged "high risk" are auto-rejected with no human review before the rejection is sent.

---

## CFU Checkpoints

### 1. Recognize

- **Categories of personal data present:** Identity data (name, contact details), financial data (income, debt, credit history), and behavioral data (browsing history, social media activity).
- **Special-category data (Article 9):** Not collected directly, but inferable. Social media activity can reveal political views, religion, or sexual orientation without the bank asking for that data. Treat this as a live risk, not a theoretical one.
- **EU border crossing:** Yes. The scoring model runs on US cloud infrastructure. Applicant data leaves the EU/EEA every time a score is generated.

### 2. Apply

Full worksheet is in Phase 2 below.

### 3. Integrate

Client memo is in Phase 3 below.

### 4. Verify

Peer review of Kimia Asgari's memo is in the file `Peer-Review-Kimia-Asgari.md`.

### 5. Debrief

See the Debrief section at the end of this document.

---

## Core

### Phase 1: Fact Pattern

Completed above under Transition Note and Setup / First Run.

### Phase 2: Mini GDPR Audit Worksheet

#### Section A - Data map

| Field | Answer |
|---|---|
| Categories of personal data | Identity data (name, contact); financial data (income, debt, credit history); behavioral data (browsing history); social media activity data |
| Sources | Financial data: applicant form plus credit bureau. Social media data: optional social login. Browsing history: third-party ad-tech vendor |
| Purpose(s) | (1) Assess creditworthiness for the loan decision. (2) Flag fraud risk |
| Lawful basis per purpose | (1) Contract, Article 6(1)(b) - needed to process the loan the applicant asked for. Applies to core financial data only. (2) Social media and browsing data: TBD - legal review. Legitimate interests is the likely fit, but no Legitimate Interests Assessment exists yet |
| Retention period per purpose | Financial application data: set by German banking retention rules, around 10 years. Social/browsing data: TBD - legal review. Should be held only as long as one scoring run needs it |
| Recipients and sub-processors | Credit bureau; US-based scoring vendor; third-party browsing data broker |
| International transfers and mechanism | Yes, to the US vendor. Mechanism: TBD - legal review. Must confirm Data Privacy Framework certification or Standard Contractual Clauses |

Legitimate interests is the most likely basis for the social and browsing data. It needs a documented three-part test: purpose, necessity, balancing. That test has not been done.

#### Section B - Risk and rights

- **Special-category data (Article 9):** Not directly collected. Plausibly inferable from social media content. Must be treated as present until the bank proves otherwise.
- **Automated decision-making (Article 22):** Yes. The tool auto-rejects applicants with no human review. This is a decision made solely by automated means with a legal effect - denial of credit. No valid safeguard exists today. There is no human check, no way to contest the decision, and no explanation given to the applicant.
- **Is a DPIA required?** Yes. At least four EDPB criteria are met: systematic scoring of individuals, automated decisions with legal effect, likely special-category data by inference, and combining data from different sources in a way the applicant would not expect. Two criteria are enough to trigger a mandatory DPIA under Article 35. This case clears that bar easily.
- **Data subject friction points:** Right to object to profiling (Article 21), since applicants do not know profiling is happening. Right to an explanation of automated decisions (Article 15 and Article 22(3)). Right of access, since applicants cannot currently see their own score.
- **Controller / processor split:** The bank is the controller - it sets the purpose and means. The US scoring vendor is a processor, unless it independently decides how to weight the social and browsing signals, which would make it a joint controller. This needs a contract check. The browsing data broker is a processor if it only follows the bank's instructions, or a separate controller if it sets its own purpose for collecting that data.
- **Is a DPA needed?** Yes, with the US scoring vendor and with the data broker.

#### Section C - Law stacking

- **AI Act cross-check:** High-risk under Annex III, point 5(b). The AI Act adds obligations GDPR does not: a conformity assessment, technical documentation, a Fundamental Rights Impact Assessment under Article 27, and a structural human-oversight requirement under Article 14. Article 14 and Article 22 point at the same defect, but Article 14 demands it as a built-in control, not just an individual right to complain.
- **ePrivacy check:** Yes. Browsing history comes from cookies or tracking tech. ePrivacy requires prior consent for that collection. A GDPR legitimate-interests basis cannot replace that consent. It is a separate legal requirement that must be met on its own.
- **Data Act check:** N/A. No connected product or cloud-switching data is involved in this case.

### Phase 3: Client Recommendation Memo

**To:** Legal and Compliance, [Bank Name]
**From:** Nelly Pourmehr, AI Consultant
**Re:** Loan Applicant Scoring Tool - GDPR and AI Act Findings

**Bottom line: Go, with conditions.** Using AI to support credit scoring is legal and can work. This build cannot launch as it stands. Two gaps create real exposure: no human check before rejection, and no documented legal basis for the social and browsing data.

**Top three actions, in order:**

1. **Add mandatory human review before any rejection is final.** No applicant should be auto-rejected. A loan officer must review the case, especially borderline or negative scores. This closes the Article 22 gap and satisfies the AI Act's Article 14 requirement. Build this first.
2. **Write a Legitimate Interests Assessment for the social and browsing data, or drop that data.** There is no valid legal basis for it today. Either commission a real three-part LIA that would survive a regulator's review, or remove these inputs from the model until it exists. Given the weak proportionality case, removal is the safer path.
3. **Confirm the transfer mechanism with the US vendor before more data moves.** Get written confirmation of Data Privacy Framework certification or signed Standard Contractual Clauses. Right now this is an open gap with no fallback.

**Residual risks that remain even after these fixes:**

- Inferred special-category data from social media cannot be fully removed by process changes alone, as long as social data feeds the model at all.
- No DPIA exists yet. Until it is done and any high residual risk is addressed, regulatory exposure stays above what these three actions alone can close.
- Human review only works if loan officers actually review, not rubber-stamp. Volume incentives can turn a real safeguard into a paper one. This needs monitoring after launch, not just a policy on paper.

We recommend a follow-up engagement to complete the DPIA and the LIA before go-live.

---

## Debrief - Comparing My Audit with Kimia Asgari's

Kimia and I ran the same fact pattern independently. Points of agreement and divergence:

**Where we agree:**
- Both audits land on Contract (Article 6(1)(b)) for core financial data, and flag legitimate interests as TBD for social/browsing data pending an LIA.
- Both flag Article 22 as an active violation, not a borderline case - the auto-rejection has zero human review.
- Both call the DPIA mandatory, citing overlapping EDPB criteria (systematic scoring, automated legal effect, inferred special-category data, novel data combination).
- Both memos land on the same bottom line: go, with conditions, and both name human review as action one.
- Both flag the ePrivacy consent gate as independent from GDPR's legitimate-interests basis.

**Where we diverge:**
- Kimia's worksheet treats the browsing data broker's role as ambiguous between processor and controller and leaves it as a contractual open question. My read is the same, but I would push harder in the memo itself to get that contract term resolved before any data broker feed goes live, not just noted as a risk.
- My memo recommends removal of social/browsing data as the safer default while the LIA is pending. Kimia's memo also flags removal but frames it as a secondary option behind commissioning the LIA. I weight removal more heavily given how weak the necessity case is for behavioral data in a credit decision.
- Kimia's residual risk section is stronger on the "rubber-stamp" review risk. I have folded that into my memo but would adopt her framing that this needs a specific, named monitoring step, not a general caution.

**Stronger reading:** Kimia's framing on treating human review as an operational risk, not just a design fix, is the stronger point. I am carrying that into my final recommendation: action one should include a named monitoring check on review quality, not just the existence of a review step.

---

## Reinforce

**DPIA outline for the most sensitive processing activity (credit scoring using social/browsing data):**
- Description of processing: automated scoring of loan applicants combining financial, social media, and browsing data into a single risk flag.
- Necessity and proportionality: financial data is clearly necessary. Social and browsing data's necessity is unproven and should be the central question the DPIA answers.
- Risk identification: discriminatory outcomes from proxy variables in social/browsing data, inferred special-category data, low transparency to applicants, auto-rejection with no recourse.
- Proposed mitigation: remove or strictly justify social/browsing inputs, mandatory human review, clear applicant-facing explanation of the score, regular bias audits.

**One DPA clause to request from the US vendor:** A data-location and sub-processor-disclosure clause. The vendor must notify the bank before any change in processing location or before adding a new sub-processor. This matters because the transfer mechanism is not yet confirmed, and a silent change in processing location could break whatever mechanism gets put in place.

**If the client also serves UK data subjects:** The bottom line does not change, but the analysis needs a parallel UK GDPR check. The UK is a separate adequacy jurisdiction after Brexit. The DPA needs to reference both the EU mechanism (SCCs or DPF) and the UK's International Data Transfer Agreement or UK Addendum. One EU-only transfer mechanism does not cover UK data subjects automatically.

---

## Stretch - Data Protection by Design Checklist (Credit Scoring Activity)

| Item | Status |
|---|---|
| Data minimisation - only minimum necessary data collected | Fails. Social and browsing data collection goes beyond what has been shown to be necessary |
| Purpose binding - data technically restricted to stated purpose | Unknown. No evidence of technical controls limiting the social/browsing pipeline to the scoring purpose |
| Access controls - access limited to those who need it | Unknown. Not documented in the fact pattern. Flag for follow-up |
| Retention enforcement - automated deletion or anonymisation | Fails. No defined retention period exists for the social/browsing enrichment data |
| Subject rights workflow - can respond within 30 days | Unknown. No evidence of an operational workflow built for this specific system |
| Incident response - detect and notify a breach within 72 hours | Unknown. Likely exists at the bank level generally, but not confirmed for this vendor integration specifically |
