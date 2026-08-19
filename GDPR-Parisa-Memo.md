# GDPR Audit Pack - Parisa Case 1

## Transition note

I am carrying forward **Case 1 — In-Store Shoplifting Risk Scoring** from the EU AI Act approval pack. It was classified there as **prohibited**, which makes it the most important case to carry into the GDPR audit because it also involves live CCTV, inferred biometric or behavioral signals, and profiling of the general public in a retail environment.

## Fact pattern

The client is a mid-sized supermarket chain operating stores across the EU/EEA. It wants to use an AI system on in-store CCTV feeds to estimate whether a shopper is likely to shoplift, based on live video, facial-expression or emotion inference, body movement, and cross-visit behavioral profiles. The system would generate a risk score or alert for security staff in real time, and the alert would influence whether a shopper is watched more closely or stopped for intervention. The affected data subjects are ordinary customers entering monitored stores, including EU residents and visitors. The data stack appears to rely on CCTV infrastructure and a vision analytics vendor, with no confirmed non-EU processor yet, although that must be checked before launch. The processing is high sensitivity because it uses personal data captured in public-facing retail space and may involve biometric or special-category inference. Human review is not meaningful upstream of the flag, because security staff act on the AI output rather than independently assessing each case first.

## Audit worksheet

### Section A - Data map

| Field | Your answer |
|---|---|
| Categories of personal data | Live CCTV footage; facial and body-movement data; inferred emotional or behavioral signals; cross-visit shopper profiles; time/location metadata; security intervention logs tied to specific shoppers. |
| Sources (where data comes from) | In-store CCTV cameras; video analytics software; cross-visit profiling database; security staff actions after alerts are generated. |
| Purpose(s) - one row per purpose | 1) Detect and deter shoplifting in real time. 2) Generate shopper risk scores and alerts for security staff. 3) Retain incident records after an alert or intervention. 4) Build cross-visit behavioral profiles to improve future scoring. |
| Lawful basis per purpose - or `TBD — legal review` | 1) Legitimate interests for ordinary store security monitoring, if narrowly scoped and proportionate. 2) `TBD — legal review` for person-level risk scoring; likely not viable as designed because the system relies on intrusive biometric-like inference and public monitoring. 3) Legitimate interests or legal obligation, depending on local incident-reporting rules. 4) `TBD — legal review`; this looks particularly hard to justify because persistent profiling increases intrusiveness without a clear necessity case. |
| Retention period per purpose | Live footage: short retention only, typically 24-72 hours unless an incident occurs. Risk scores: delete immediately unless attached to a specific incident file. Incident files: keep only as long as needed for investigation, claims handling, or legal retention rules. Cross-visit profiles: do not retain as proposed; if retained at all, a strict, short, documented retention period would be required. |
| Recipients and sub-processors | Internal security staff; store management; IT/admin staff with access to CCTV systems; video analytics vendor; CCTV hosting or cloud provider; legal/compliance team; law enforcement only if a specific incident requires disclosure. |
| International transfers and transfer mechanism | TBD — legal review. If any vendor or cloud service is outside the EEA, the client would need a valid transfer mechanism such as SCCs plus a transfer impact assessment. No transfer should be assumed until the vendor stack is confirmed. |

### Section B - Risk and rights

- Are any special-category data present or inferable from the outputs (Article 9)? Yes. Facial-expression analysis, emotion inference, and biometric-like processing can expose or infer special-category data, and the system is also close to biometric categorisation in practice.
- Is there automated decision-making with legal or similarly significant effects (Article 22)? Yes. The risk score directly changes how a shopper is treated in-store, including closer surveillance or intervention, so the output is not merely informational. As designed, the human role does not look like genuine override before the effect hits the person.
- Is a DPIA required? Yes. Several EDPB criteria are triggered: systematic monitoring, use of innovative technology, monitoring of a publicly accessible area, and likely special-category inference. The case should be treated as high-risk before any launch decision.
- What data subject friction points are most likely? Right to be informed, right of access, right to object to legitimate-interests profiling, and likely requests for erasure or restriction after an adverse intervention. Complaints are also likely if shoppers are not clearly told that AI is involved.
- What is the controller / processor split? The supermarket chain is the controller because it decides why the system is used and what security outcome it wants. The vision analytics vendor is likely a processor if it operates only on instructions, but it could drift toward joint-controller territory if it decides how profiling works or reuses the data for its own purposes.
- Is a DPA (Data Processing Agreement) needed with any vendor? Which ones? Yes. A DPA is needed with the vision analytics vendor, any CCTV hosting or cloud provider, and any subcontractor that can access the footage or profiles. The contract should also restrict any reuse of footage for vendor model training.

### Section C - Law stacking

- **AI Act cross-check:** This is the main blocker. On the current facts it falls in the prohibited category, not just high-risk, because it uses biometric or behavioral profiling to predict shoplifting risk for members of the public. GDPR does not create that prohibition; it only adds separate privacy obligations and risk controls.
- **ePrivacy check:** Probably N/A on the current facts unless the cameras or analytics system also access shopper devices, cookies, or terminal equipment. If that happens, ePrivacy could add extra consent constraints.
- **Data Act check:** N/A. This is not a connected-product or cloud-switching fact pattern.

### Preliminary conclusion

As designed, the project should not proceed. The GDPR worksheet points to a highly intrusive monitoring and profiling setup with special-category inference, a difficult Article 22 position, and a likely need for a DPIA that would confirm the design is too risky to launch without a major redesign.

### Phase 4 - Client response

| Criterion                                     | Score 1–3 | Comment |   |
| --------------------------------------------- | --------- | ------- | - |
| Clear bottom-line recommendation              | 1         | None    |   |
| Lawful basis selection is justified           | 1         | None    |   |
| Top actions are specific and sequenced        | 1         | None    |   |
| Residual risks are named honestly             | 1         | None    |   |
| Law stacking is addressed (AI Act / ePrivacy) | 1         | None    |   |

We accept the recommendation and will not move forward with the current design until the GDPR and AI Act concerns are addressed. Our main concern is the business delay this creates, since the current timeline assumes a faster launch, so we need a clearer sequencing plan for redesign, legal review, and operational testing. Please rethink the cross-visit profiling section first, because that appears to add the most risk without being essential to the core store-security use case.
