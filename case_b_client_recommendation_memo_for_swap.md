# Client recommendation memo: Case B "wellbeing assistant" (for peer swap)

*Extract of Part 2 of [`GDPR_Audit_Pack_Nicolo_Marseu.md`](GDPR_Audit_Pack_Nicolo_Marseu.md). Fact pattern: [`case_b_fact_pattern_shared_with_friedrich.md`](case_b_fact_pattern_shared_with_friedrich.md).*

**To:** Managing Director and Data Protection Officer, [Contact-centre client]
**From:** Nicolò Marseu
**Re:** GDPR review of the "wellbeing assistant"
**Date:** 17 November 2026

**Bottom line: Stop the wellbeing assistant as proposed. Go with conditions on a redesigned, team-level workload tool.**

Inferring agents' stress from their voice and webcam images has no valid legal basis under GDPR. It is also banned outright under the EU AI Act. You can still tackle sick leave and turnover, just not by monitoring individual faces and voices.

**What we found**

Agent stress scores count as health data, which is the most protected category under GDPR. Consent doesn't work between employer and employee. Your legitimate interest in reducing sick leave doesn't outweigh continuous webcam and voice monitoring of 600 people. Feeding the scores into shift planning adds automated decisions about people's hours, and a team lead "looking first" doesn't fix that if they follow the score. The customer mood module is your end-clients' call, not yours, and carries high-risk AI obligations. Drop it.

**Top three actions, in this order**

1. **Stop the procurement and confirm no data has flowed.** Don't sign the vendor contract for the agent or customer emotion modules. If anything was piloted, delete the recordings and scores and keep evidence of the deletion.
2. **Run a DPIA and agree a works agreement on the redesign before any build.** The redesign uses call transcripts (no voice tone, no video), shows only team- and queue-level workload with a minimum group size of 10, and triggers break rotation. Wellbeing is handled through an anonymous, voluntary survey and occupational health. Involve the works council from day one.
3. **Fix the contract chain before the first transcript.** Use an EU-hosted speech-to-text vendor with a DPA that bans model training. Get each telecom and insurance client to approve the new sub-processor in writing and confirm their call-recording notices cover transcription.

**Residual risks, even if you follow this**

- **Text analytics can drift back into emotion scoring.** Topic and "complaint language" analysis sits close to the legal line. Legal should confirm the redesign is outside the AI Act's emotion-recognition definition, and you'll need a technical guardrail against per-agent views.
- **Small teams can re-identify agents.** Aggregates on night shifts or niche queues can point to one person. The minimum group size must be enforced in the dashboard, not just in policy.
- **Insurance transcripts will contain health data.** Redaction isn't perfect, and some sensitive content will reach the analytics layer.

*This is a first-pass advisory note, not a legal opinion. Points marked TBD need confirmation by counsel.*
