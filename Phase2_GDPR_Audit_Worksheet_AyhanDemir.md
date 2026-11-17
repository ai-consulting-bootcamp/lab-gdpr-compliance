# Phase 2: Mini GDPR audit worksheet

*GDPR Mini Audit - Warehouse Shift AI - Ayhan Demir*


### Section A: Data map

| Field | Your answer |
| --- | --- |
| Categories of personal data | Facial images, voice recordings, inferred emotional states, employee ID, shift and attendance history, assignment outcomes, override logs |
| Sources | Warehouse webcams and microphones; scheduling system; supervisor inputs |
| Purpose 1 | Infer workers' emotional state (stress, frustration, motivation) |
| Purpose 2 | Recommend assignments to demanding shifts |
| Purpose 3 | Log recommendations and overrides for audit |
| Lawful basis: Purpose 1 | No valid basis. Consent is not freely given in employment; legitimate interests fails the balancing test (intrusive, continuous, sensitive). No Art. 9(2) exception fits. TBD legal review, but expected outcome: unlawful. |
| Lawful basis: Purpose 2 | TBD legal review. Possible legitimate interests (LIA: purpose = fair shift planning; necessity = only if based on objective data, not emotions; balancing = fails while emotion data is the input) |
| Lawful basis: Purpose 3 | Legitimate interests (accountability and contestability of decisions) |
| Retention: Purpose 1 | Not defined in brief. Should be zero: raw video and audio must not be stored; feature not to be launched |
| Retention: Purpose 2 | Not defined. Proposed: assignment records for the current planning period plus 6 months |
| Retention: Purpose 3 | Proposed: 6 months minimum (aligns with AI Act deployer log duty), then delete unless a dispute is open |
| Recipients and sub-processors | Supervisors, HR, workforce planning team; emotion analytics vendor and its sub-processors; cloud host; scheduling system vendor |
| International transfers and mechanism | US vendor: EU-US Data Privacy Framework if certified, otherwise SCCs plus transfer impact assessment. Cloud host: keep in EU region. |

### Section B: Risk and rights

- **Special-category data (Art. 9):** Yes. Facial and voice data processed to analyse individuals is biometric data, and inferred stress or mental state can reveal health data. No Art. 9(2) exception covers this use.
- **Automated decision-making (Art. 22):** Likely yes. Shift assignment has a similarly significant effect, and an override that is rarely used does not count as meaningful human involvement. Safeguards needed: real human review with authority and time, right to contest, explanation of the main factors.
- **DPIA:** Required. At least 7 of the EDPB's 9 criteria apply: evaluation or scoring, systematic monitoring, sensitive data, large scale, vulnerable data subjects (employees), innovative technology, and automated decisions with significant effect. Two are enough to trigger a DPIA.
- **Data subject friction points:** Access requests for inferred emotion scores and the logic behind assignments; objection to profiling (Art. 21); erasure of recordings; contesting shift decisions under Art. 22(3).
- **Controller / processor split:** Logistics company = controller. Emotion analytics vendor, cloud host and scheduling vendor = processors. If the emotion vendor reuses the data to train its own models, it becomes a separate controller for that use.
- **DPA needed:** Yes, Art. 28 DPAs with all three processors: emotion analytics vendor (including SCCs and sub-processor list), cloud host, scheduling vendor.

### Section C: Law stacking

- **AI Act cross-check:** Emotion inference at work is prohibited (Art. 5(1)(f)); shift allocation without it is high-risk (Annex III pt. 4(b)). The AI Act adds an outright ban that GDPR does not have, plus provider conformity duties and deployer duties such as informing workers' representatives before use.
- **ePrivacy check:** No cookies or pixels. Device-level data is involved only if webcams or microphones on employee-used terminals are accessed; flag for legal review under the national ePrivacy rules (Germany: TDDDG §25). It does not change the outcome.
- **Data Act check:** N/A. No connected product data sharing or cloud switching in scope.
