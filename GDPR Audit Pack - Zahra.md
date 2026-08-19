# GDPR Audit Pack - Zahra

## Fact pattern

Nordfracht Logistik GmbH is a mid-size logistics and freight company. It has about 1,800 employees and is headquartered in Germany, with warehouses and delivery routes across the EU. The company receives roughly 6,000 job applications per year for warehouse and driver roles, and it wants to speed up the first round of screening. The AI system reads uploaded CVs (name, contact details, work history, keyword matches) and analyzes short video interviews (recorded speech, including tone of voice). It gives each candidate a numeric score and a rank. Candidates below the cut off score get an automated rejection email, with no human involved. Candidates above the cut off go to a recruiter for interview, but in practice recruiters rarely change the AI ranking. The video analysis and scoring engine is licensed from a US based HR tech vendor, which processes the video and audio data on its own cloud infrastructure. The data subjects are job applicants, not employees or customers. Most of them are in Germany or other EU/EEA countries, though some applicants from outside the EU also apply.

**Answers to the required fact pattern questions:**

| Question | Answer |
|---|---|
| Who is the client? | Nordfracht Logistik GmbH, a mid-size logistics and freight company with about 1,800 employees, headquartered in Germany |
| What personal data is processed? | CV and resume data (name, contact info, work history, education, keywords), video interview recordings (voice, speech content, tone of voice), and the score and rank produced for each candidate. Volume is about 6,000 applicants per year. Sensitivity looks moderate at first glance, but voice and tone analysis can risk revealing special category data (see Section B) |
| Who are the data subjects? | Job applicants, not employees and not customers |
| Where are data subjects located? | Mostly in the EU/EEA (Germany and other member states), with some applicants from outside the EU |
| Who are the vendors in the stack? | A US based HR tech vendor that runs the video and audio scoring engine on its own cloud infrastructure, outside the EU |
| What does the AI system do with the data? | It reads CVs and analyzes the audio and tone of video interviews to produce a score and a rank. That rank drives an automatic rejection for candidates below the cut off |
| Is there automated decision making with legal or similarly significant effects? | Effectively yes. Rejection is fully automated for most applicants, and the human review of the shortlist is close to symbolic, since recruiters rarely override it. This still raises Article 22 concerns even though a human is nominally involved for the shortlisted group |

---

## Audit worksheet

### Section A - Data map

| Field | Your answer |
|---|---|
| Categories of personal data | - Identity and contact data from the CV<br>- Career history and keywords<br>- Video interview recording (voice, tone, face)<br>- AI generated score and rank |
| Sources | - Application form, uploaded CV<br>- Recorded video interview |
| Purpose(s) | 1. Parse CV, match keywords<br>2. Analyze tone of voice as a soft skill score<br>3. Combine both into one rank<br>4. Auto reject below the cut off<br>5. Send shortlist to a recruiter |
| Lawful basis, or `TBD, legal review` | 1. Contract, Art 6(1)(b)<br>2. `TBD, legal review`, likely legitimate interest, needs a three step test<br>3. Same, `TBD, legal review`<br>4. `TBD, legal review`, legitimate interest is probably not enough here, see Section B<br>5. Contract, Art 6(1)(b) |
| Retention | - Rejected applicants: about 6 months, matches common German practice for discrimination claim windows, confirm exact figure with legal review<br>- Video: delete sooner if possible<br>- Hired applicants: moves to the employment file |
| Recipients and sub processors | - HR and recruiter staff<br>- US HR tech vendor running the scoring engine, as processor<br>- Possibly a separate CV storage or ATS vendor |
| International transfers | - Transfer: yes, video and audio go to the US vendor<br>- Mechanism: Standard Contractual Clauses plus a transfer impact assessment<br>- `TBD, legal review` on extra safeguards |

Lawful basis options under Article 6: consent, contract, legal obligation, vital interests, public task, legitimate interests. Legitimate interest needs a three step test on file: purpose, necessity, balancing.

### Section B - Risk and rights

- **Special category data (Art 9):** Likely inferable even if not directly collected. Voice tone can reflect a speech impediment, a health condition, or an accent tied to ethnic origin. Inferred data still counts under EDPB guidance. Worth checking against how the vendor's model actually works.
- **Automated decision making (Art 22):** Yes in practice. No human at all for auto rejects. For the shortlist, recruiter sign off is rarely a real check, which likely does not count as genuine human review. Art 22 only permits solely automated decisions on contract necessity, a permitting law, or explicit consent, not legitimate interest. Needs a real human check before rejection, plus a way to contest the result.
- **DPIA required?** Yes. Meets at least six of the EDPB's nine criteria: scoring, automated decisions with legal effect, sensitive data, likely large scale (6,000 applicants a year), combining data sets, vulnerable subjects, innovative technology. Two or more already triggers the presumption, so a DPIA is needed before go live.
- **Friction points:** Access requests for the CV, video, score, and the logic behind the decision. Erasure requests for video and audio from rejected applicants. Objections to profiling and to a solely automated rejection.
- **Controller / processor split:** Nordfracht is the controller. The US vendor is the processor for the scoring engine. `TBD, legal review`, if the vendor trains its model across clients it may be a joint controller for that part, check the contract.
- **DPA needed?** Yes, with the US vendor, plus SCCs for the transfer. Also with any separate ATS or storage vendor.

### Section C - Law stacking (one line each)

- **AI Act:** Falls under the Annex III high risk category (employment decisions), adding duties GDPR does not cover: risk management, data quality checks, documentation, logging, human oversight by design, accuracy testing, conformity assessment, EU database registration.
- **ePrivacy:** Unclear if the careers site uses cookies or tracking pixels, if so, a separate consent banner is needed, `TBD, confirm with the website team`.
- **Data Act:** Not applicable, no connected product or cloud switching data here.

---

## Client recommendation memo

**To:** Nordfracht Logistik GmbH, HR and Legal
**Re:** AI CV and video screening tool, GDPR readiness

**Bottom line: go, with conditions.** The screening idea itself is fine under GDPR, but the current design has three gaps that need to close before it touches real applicants. The biggest one is the auto reject step, which right now has no valid legal basis for a fully automated decision.

**Top three actions, in order:**

1. **Before the tool processes any live applicant:** put a real human check in front of every rejection, not a rubber stamp. A recruiter has to actually look at borderline cases and be able to overturn the score. Without this, Article 22 blocks the auto reject flow as designed.
2. **Before go live:** complete a DPIA covering both the CV parsing and the video tone analysis. This audit already found at least six of the nine EDPB triggers, so this is not optional, and it is the right place to test whether the tone of voice feature can even infer traits like accent or a health condition.
3. **Before any video or audio data leaves the EU:** sign an Article 28 Data Processing Agreement with the US vendor and put Standard Contractual Clauses in place, backed by a transfer impact assessment. No data should flow to the vendor's US infrastructure until this is signed.

**Residual risks, even after these fixes:**

- A human review step on paper does not guarantee a human review in practice. If recruiters keep approving the AI's ranking without real scrutiny, the Article 22 exposure comes right back. This needs monitoring, not just a policy change.
- Tone of voice analysis carries a built in risk of picking up accent, speech patterns, or health related traits, and scoring people on it. A DPIA and safeguards can reduce this risk, but they cannot fully remove the chance of an indirect discrimination claim.
- SCCs and a transfer impact assessment lower the risk of the US transfer, but they cannot fully rule out government access to the data once it sits on the vendor's US infrastructure. That is a legal limit, not a gap in this company's paperwork.

One more note: this system is also high risk under the EU AI Act, which brings its own documentation and oversight duties on top of everything above.

---

## Phase 4 - Partner swap and peer review

Reviewing [`GDPR Recommendation Memo - Nevena.md`](./GDPR%20Recommendation%20Memo%20-%20Nevena.md), Nevena's memo for the same scenario.

| Criterion | Score 1-3 | Comment |
|---|---|---|
| Clear bottom line recommendation | 3 | "Go with conditions" stated in the first line, no ambiguity |
| Lawful basis selection is justified | 1 | The memo never names an Article 6 basis or justifies one, it moves straight to Article 22 and the DPIA without saying what lawful basis covers the scoring and profiling in the first place |
| Top actions are specific and sequenced | 2 | Three actions, clearly ordered by priority, but the third one bundles the DPA, SCCs, and privacy notice updates into a single action instead of separating them, which makes it harder to actually assign and track |
| Residual risks are named honestly | 3 | Three real risks named, indirect discrimination from voice analysis, ongoing transfer uncertainty, and applicant perception of a lack of transparency |
| Law stacking is addressed | 2 | AI Act is referenced twice, human oversight and a closing line on AI Act compliance, but ePrivacy is not mentioned at all |

**As the client:** I would accept the overall direction, the human review and DPIA priorities match what our own audit found. But I would challenge one gap before signing off: the memo tells us to fix the process and get a DPIA done, but it never confirms whether we actually have a lawful basis to score and profile applicants in the first place. I need that answered before we spend money on DPIAs and vendor contracts.

### Debrief

Where the two audits agree: both land on go with conditions, both put a real human review before automated rejection as the top priority, both call for a DPIA before processing starts, and both flag the US transfer and the discrimination risk from voice analysis as residual risks that do not fully go away.

Where they diverge: my audit names a specific lawful basis per purpose, contract for the core recruitment steps, legitimate interest with a documented three step test for the scoring itself, and it flags that legitimate interest cannot support the automated rejection under Article 22. Nevena's memo does not name a lawful basis at all. My audit also checks ePrivacy explicitly, hers does not mention it.

The stronger reading is mine on the lawful basis point. Naming the Article 6 basis, and separately checking whether it can support a solely automated decision, is not optional in a real audit, GDPR has never allowed profiling on an unstated basis. Nevena's memo is stronger on plain language, it reads more clearly as something a non-lawyer could act on quickly, which matters for a client facing note. A merged version would keep her tone and structure, but add the lawful basis table underneath.

---

## Reinforce

- **DPIA outline:** Process, video interview goes to the US vendor, tone is scored, combined with the CV score into a rank, low scorers auto rejected. Necessity, check if a simpler method (structured interview, plain keyword match) works about as well before relying on AI tone scoring. Risks, special category inference from voice, discriminatory scoring, no valid Article 22 basis, US government access to the data. Mitigation, real human review before rejection, regular bias testing across accents, short retention, SCCs plus encryption, clear notice to applicants.
- **DPA clause:** A use limitation clause stopping the vendor from training its own models on Nordfracht's video and audio data. Without it, the vendor could end up shaping its model on this data, which risks joint controller status and a fresh Article 9 basis problem.
- **UK applicants:** Bottom line stays go, with conditions. Two changes, Nordfracht needs to comply with UK GDPR in parallel and likely appoint a UK representative, and the transfer to the US vendor needs the UK's own tool, the IDTA or the UK Addendum, EU SCCs alone are not enough.

---

## Stretch

### Data protection by design checklist, video tone of voice scoring and automated rejection

| Item | Status | Note |
|---|---|---|
| Data minimisation | Fails | Full video is recorded and stored, including the applicant's face, even though the model only analyzes audio tone |
| Purpose binding | Unknown | No confirmation yet that the vendor is contractually restricted to using the data only for scoring this client's applicants |
| Access controls | Unknown | No defined list of which HR or recruiter staff can view scores, video, or audio |
| Retention enforcement | Fails | No automated deletion policy exists yet, retention periods in this audit are still marked `TBD, legal review` |
| Subject rights workflow | Unknown | No documented process for responding to an access or erasure request within 30 days |
| Incident response | Unknown | No documented process for detecting and notifying a breach within 72 hours |
