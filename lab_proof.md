> **Lab project notice:** This document is for educational purposes only. The scenario and analysis are hypothetical and do not use real personal data about marketplace users or confidential client information. Do not add such information. This document is not legal advice.

# GDPR Audit Pack

**Scenario:** Kleinanzeigen sellers lose buyers by replying late. Idea: an opt-in assistant in the in-app chat that answers buyer questions while the seller is offline, using the listing, the seller's past replies and price rules, in the seller's own tone. Messages appear under the seller's name with no label. Nobody reviews them live; sellers can read the thread later and switch it off.  
**Prepared by:** Julia Antunes  
**Partner:** Ayhan Demir  
**Date:** 17 November 2026
## Phase 1: Build the fact pattern

### Scenario and transition note

This audit continues [Case 1 from the EU AI Act lab](https://github.com/antunesjulia/lab-eu-ai-act-compliance/blob/main/lab_proof.md): a limited-risk system subject to transparency obligations, with consumer-protection concerns. It is the most interesting case for GDPR purposes because its consumer-facing use may involve personal data and influence people's understanding or choices, raising questions about transparency, lawful basis, purpose limitation, and data subject rights even though the system is not classified as high-risk.

### Fact pattern

- **Who is the client?** Kleinanzeigen, an online classifieds marketplace. Company size and user counts are not specified in this case.
- **What personal data is processed?** The described inputs are listing details, seller price rules and past replies, and buyer questions and chat messages. The exact fields, any associated account identifiers, volume, and sensitivity are not specified; chat content could include other personal information.
- **Who are the data subjects?** Marketplace users, especially sellers who opt in and buyers who message them.
- **Where are the data subjects located?** Not specified in the scenario; confirm before assessing territorial scope or transfer obligations.
- **Who are the vendors in the stack?** No AI, hosting, or other vendor is named. Whether the assistant uses a non-EU processor, and where data is hosted or accessed, are TBD.
- **What does the AI system do with the data?** When a seller opts in, it uses the listing, the seller's past replies, and price rules to draft and send buyer responses in the seller's tone while the seller is offline. Messages appear under the seller's name without an AI label; sellers can review the thread later and switch the feature off.
- **Is there automated decision-making with legal or similarly significant effects?** The system automatically generates and sends messages without live human review. The case does not establish that it makes decisions with legal or similarly significant effects under Article 22; assess whether its messages could materially affect a buyer's transaction.

### Recognize

- **Personal data categories:** Listing and price information, seller replies, and buyer-seller communications. Associated account identifiers and any additional personal information in chat are not specified.
- **Special-category data (Article 9) present or inferable:** None is specified, but free-text chat could contain or reveal special-category data. Confirm whether the assistant processes or retains such content and whether safeguards or exclusions are needed.
- **EU/EEA border crossing:** Data subject locations, data hosting, vendor access, and processing locations are unspecified. International transfers cannot be ruled out until the relevant locations are identified.
- **Automated decision-making:** The assistant sends messages without live review, so it automates communication. No legal or similarly significant effect is established by the available facts; evaluate the impact on buyers and any transaction decisions.

## Phase 2: Mini GDPR audit worksheet

### Section A — Data map

| Field | Your answer |
|---|---|
| Categories of personal data | Listing details; seller price rules and past replies; buyer questions and chat messages. Associated account identifiers, volume, and sensitivity are not specified; free-text messages could contain other personal data. |
| Sources | The listing, seller's price rules and past replies, and buyer questions and chat messages. Other sources or account fields are not specified. |
| Purpose(s) | Generate and send buyer responses in the opted-in seller's tone while the seller is offline. |
| Lawful basis per purpose | TBD — legal review for processing seller and buyer data. Seller opt-in is part of the described feature, but the facts do not establish that it constitutes GDPR consent or identify a basis for processing buyers' messages. |
| Retention period per purpose | Not specified. |
| Recipients and sub-processors | The seller can review the thread later; the generated response is sent to the buyer under the seller's name. No AI, hosting, or other vendor is identified, so sub-processors cannot be named. |
| International transfers and transfer mechanism | Not specified. Vendor, hosting, and access locations must be identified before determining whether transfers occur or what mechanism applies. |

No lawful basis is proposed yet, so a legitimate-interests assessment cannot be completed. If legitimate interests are considered, document:

1. **Purpose:** TBD — legal review.
2. **Necessity:** TBD — legal review.
3. **Balancing:** TBD — legal review.

### Section B — Risk and rights

- **Special-category data (Article 9):** None is identified in the case facts. Because the assistant processes free-text chat, such data could be included in messages; whether it is present or inferred is unknown.
- **Automated decision-making (Article 22):** The assistant sends messages without live human review, but the facts do not establish decisions with legal or similarly significant effects. The messages' effects on buyers and transactions need assessment; no Article 22 safeguard can be specified from the information given.
- **DPIA:** The facts are insufficient to conclude that a DPIA is legally required. Screen all nine EDPB criteria: evaluation or scoring is not established; significant-effect automated decisions are not established; systematic monitoring is not stated; special-category data may occur in free text but is unconfirmed; processing scale is unknown; several inputs are used together, but whether this constitutes high-risk dataset matching is unclear; vulnerable data subjects are not identified; use of AI makes innovative technology relevant; and no restriction on rights or access to a service is stated. Complete the screening before launch and conduct a full DPIA if it indicates likely high risk.
- **Data subject friction points:** Buyers see messages under the seller's name with no AI label, which may make the origin of a response unclear. The case does not describe how access, erasure, or objection requests are handled, or whether profiling occurs; those points need clarification.
- **Controller / processor split:** Kleinanzeigen operates the marketplace feature, but the facts do not establish the formal role of each party. The seller opts in and supplies past replies and price rules; the buyer supplies questions and chat messages. No AI or hosting vendor is named, so its role, if any, is unknown.
- **Data Processing Agreements:** No vendor is identified, so no specific DPA can be named. If a third-party vendor processes personal data on Kleinanzeigen's behalf, determine its processor role and put the required DPA in place before sharing data.

### Section C — Law stacking

- **AI Act cross-check:** The linked EU AI Act case identifies this as limited risk with transparency obligations and consumer-protection concerns. The assistant sends messages without an AI label; ensure the relevant transparency obligation is addressed. No further AI Act details are established here.
- **ePrivacy check:** No cookies, tracking pixels, or device-level data are mentioned. Applicability cannot be determined beyond the facts provided.
- **Data Act check:** No connected product or cloud-switching data is mentioned; no Data Act issue is identified from the available facts.

## Phase 3: Write the client recommendation memo

**Case:** Kleinanzeigen  
**From:** Ayhan Demir  
**Subject:** GDPR recommendations for the seller messaging assistant  
**Date:** 17 November 2026 by Julia Antunes

**Bottom line — Go with conditions.** The assistant may help opted-in sellers respond while offline, but the available facts do not establish the lawful basis, vendor and transfer arrangements, retention, or how buyers are informed. Resolve these points before enabling the feature.

**Top three actions**

1. **Map the processing before launch.** Identify the AI and hosting providers, their locations and roles, the data each receives, and applicable retention periods. Determine whether any data leaves the EU/EEA and document the transfer mechanism if it does.
2. **Complete the GDPR assessments and notices.** Determine and document an Article 6 lawful basis for processing sellers' past replies and buyers' messages; do not treat seller opt-in alone as proof of consent for all processing. Screen the processing against the EDPB's DPIA criteria and complete a DPIA if the screening indicates likely high risk. Explain the assistant's role to sellers and buyers, including that it sends messages without live review and under the seller's name. Because chat content may contain special-category data, confirm whether it does; if so, assess Article 9 conditions and safeguards before processing it.
3. **Set up accountability and user controls.** Confirm the controller/processor roles and put a DPA in place before any vendor processes personal data on Kleinanzeigen's behalf. Specify retention and how access, erasure, and objection requests will be handled. Preserve the seller's ability to switch the feature off and review the conversation.

**Residual risks:** Free-text chats may contain sensitive information that is not identified in the current facts. Buyers may still misunderstand who authored a message, even if the feature is disclosed. The system sends messages without live human review, so inaccurate or unsuitable responses may affect a transaction before the seller sees them.

This is a preliminary recommendation based only on the scenario facts provided. Vendor details, data volumes, locations, and the legal effects of messages remain unknown and could change the assessment.

**Word count:** 318

## Phase 4: Partner swap and peer review

### Colleague's memo

**GDPR Mini Audit - Warehouse Shift AI - Ayhan Demir**  
**To:** Legal and CTO, [Client] **From:** Ayhan Demir **Re:** AI shift recommendations based on worker emotion analysis

**Bottom line: Stop as designed.** Inferring workers’ emotions from webcam and voice data is banned under the EU AI Act and has no lawful basis under GDPR, so the current design cannot launch in any form.

The business goal, filling demanding shifts fairly and reliably, is legitimate. It can be met with a different input. Removing cameras and microphones from the design also removes the biometric and health data, which is the hardest GDPR problem today. What remains is a normal, if still regulated, workforce planning tool.

**Top three actions**

1. **Stop and clean up now.** Switch off any emotion analysis pilot, delete captured video, audio and emotion scores, and confirm deletion in writing from the analytics vendor.
2. **Redesign on objective data, then run a DPIA before first use.** Base recommendations on skills, certifications, rest-time rules, workload, past shift balance and worker-stated preferences. The redesigned tool is still high-risk under the AI Act, so request the vendor’s conformity documentation and complete a DPIA before any data flows.
3. **Put the governance in place before go-live.** Sign Art. 28 DPAs (with SCCs or DPF check for the US vendor), agree the system with the works council, update the employee privacy notice, and set up a real human review and appeal route for shift assignments.

**Residual risks**

- **Rubber-stamping:** even with a review step, supervisors may accept most recommendations, which keeps Art. 22 exposure alive. Track override rates monthly and audit a sample of accepted recommendations.
- **Proxy bias:** objective inputs like attendance can still encode health or caregiving patterns and lead to unfair outcomes. Bias testing reduces this but does not remove it.
- **Trust and co-determination:** after an emotion-monitoring proposal, workers and the works council may resist the redesigned tool, which can delay rollout.

This is a firs-pass recommendation based only on the scenario  provided. Details, and unknown parts can change the assessment result and details.

### Peer review

The colleague's memo addresses a warehouse workforce scenario, not the Kleinanzeigen seller-messaging scenario in this audit pack. The scores below assess the memo itself; the comparison in the debrief is limited by the different fact patterns.

| Criterion | Score (1–3) | Comment |
|---|---:|---|
| Clear bottom-line recommendation | 3 | "Stop as designed" is clear and consistent with the identified workplace emotion-analysis concern. |
| Lawful basis selection is justified | 1 | The memo states there is no GDPR lawful basis but does not analyze an Article 6 basis or, if special-category data is processed, an Article 9 condition. Separate that analysis from any AI Act prohibition. |
| Top actions are specific and sequenced | 3 | The memo orders shutdown, redesign and governance steps. Verify applicable retention or preservation requirements before deletion. |
| Residual risks are named honestly | 2 | Proxy bias and trust are concrete residual risks. The Article 22 point should be framed as a risk to assess: the stated facts do not establish whether human review would be meaningful or whether decisions have the required significant effect. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | The AI Act and transfer mechanisms are mentioned. State the scope and medical/safety exception to the workplace emotion-recognition prohibition; no ePrivacy issue is identified in the memo. |

### Client response

We accept stopping the emotion-analysis design and considering a redesign, but ask you to distinguish the AI Act restriction from the GDPR lawful-basis analysis. Please also clarify what data the redesigned tool uses and whether human review would be meaningful before making a final recommendation.

### Debrief

- **Where the audits agreed:** Both memos call for assessing risks before launch, clarifying vendors and data flows, and giving people clearer information about the AI-assisted processing. The warehouse memo calls for a full DPIA; this pack's available facts support screening but do not establish whether a full DPIA is required.
- **Where they diverged:** The scenarios differ, so their go/stop recommendations are not directly comparable. This pack leaves the seller-messaging lawful basis unresolved; the colleague's memo concludes that the warehouse system has none, but does not provide an Article 6 or Article 9 analysis. Its Article 22 concern also needs assessment against the actual effect of decisions and whether human review is meaningful.
- **Follow-up or revision:** Confirm the workplace emotion-recognition rule and whether a medical or safety exception applies; analyze the GDPR basis separately, including Article 9 if special-category data is involved. For the redesigned system, verify the input data, AI Act classification, vendor roles and transfers, DPIA need, and safeguards before revising the recommendation.
