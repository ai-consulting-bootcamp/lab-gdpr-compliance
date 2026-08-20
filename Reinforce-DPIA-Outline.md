# Reinforce — DPIA outline, DPA clause, and UK GDPR variant

Companion to [`GDPR-Audit-Pack-VittalNavale.md`](./GDPR-Audit-Pack-VittalNavale.md). Covers the "if you finish early" extension items.

## DPIA outline — AI CV scoring and automated rejection

**Description of processing.** Candidate CVs and online-assessment responses are ingested by a vendor-hosted AI model, scored against the job description, and sorted into "strong fit," "maybe," "not a fit." "Not a fit" candidates currently receive an automated rejection email. The model was trained on five years of the client's historical hiring and one-year retention outcomes.

**Necessity and proportionality assessment.** Screening ~400 CVs/week with a two-person HR team is not feasible manually at this volume, so some automated triage is proportionate. However, fully automating the *rejection* step (not just the sorting) is not necessary to solve the volume problem — a recruiter can review a ranked "not a fit" list far faster than 400 raw CVs, so full automation of the rejection decision fails the necessity test as currently designed.

**Risk identification.**
- Discriminatory bias inherited from historical hiring/retention data, disproportionately affecting protected groups.
- Unlawful solely-automated decision-making under Article 22 (no confirmed human review).
- Inadequate transparency: candidates cannot get a meaningful explanation of their score.
- Unlawful international transfer if SCCs/DPF certification are not in place before go-live.
- AI Act non-conformity as a high-risk Annex III system (missing human oversight design, technical documentation, logging).

**Proposed mitigations.**
- Mandatory recruiter review of every "not a fit" outcome before rejection is sent.
- Pre-launch bias/fairness audit of the training data and model outputs, with defined outcome-parity thresholds by protected characteristic proxy (e.g., age band, gender-coded names) and periodic re-testing post-launch.
- A short, plain-language explanation generated alongside each score, so recruiters can answer candidate access requests.
- SCCs + Transfer Impact Assessment (or confirmed EU-US DPF certification) executed with the vendor before any live data transfer.
- AI Act conformity documentation: risk-management file, data governance record, human oversight procedure, logging enabled from day one.

## DPA clause to request from the vendor

**Sub-processor and model-training-use restriction clause.** The DPA should state explicitly that the vendor may not use the client's candidate data (CVs, assessments, scores) to train, fine-tune, or improve its model for the benefit of other customers, and must disclose the full current list of sub-processors with advance notice of any change.

**Why this one:** it's the clause most likely to be missing by default in a generic vendor DPA, and it directly determines the controller/processor split from Section B of the audit. If the vendor quietly reuses client candidate data to improve its shared product, it becomes an independent controller for that purpose — which changes the lawful basis analysis, the transparency notice, and the client's liability exposure. Locking this down in the contract removes the ambiguity instead of leaving it as a "trust the vendor" assumption.

## UK data subjects — does the recommendation change?

If the client also serves data subjects in the UK (e.g., UK stores), the bottom line stays **go, with conditions**, but two things change:

- The transfer analysis needs a second track: UK GDPR uses the **International Data Transfer Agreement (IDTA)** or the UK Addendum to the EU SCCs, not the EU SCCs alone — the client's vendor contract needs both instruments, not just the EU version.
- The ICO, not an EU supervisory authority, becomes the relevant regulator for UK candidates, and the client should confirm whether the UK's DPIA guidance (materially similar to EDPB's but issued separately by the ICO) is also referenced in the DPIA documentation, since inspectors will expect the UK-specific framing for UK data subjects even though the substantive analysis is nearly identical to the EU one.
