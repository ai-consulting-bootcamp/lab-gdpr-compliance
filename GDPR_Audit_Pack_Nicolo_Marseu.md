# GDPR Audit Pack - Nicolò Marseu

**Scenario:** Case B, contact-centre outsourcer "wellbeing assistant" (Option A: carried forward from the EU AI Act lab with Friedrich) · **Date:** 17 Nov 2026

*First-pass audit for a training exercise. Not legal advice. Where I'm not sure of the lawful basis, I say "TBD – legal review" rather than guess.*

---

## Transition note (from the EU AI Act lab)

I'm carrying forward **Case B** from Friedrich's four client briefs. In the AI Act lab I classified it as follows:

- **Agent module: prohibited** under Art. 5(1)(f), because it is emotion recognition in the workplace based on biometric data (voice and face).
- **Customer-mood module: high-risk** under Annex III 1(c), plus an Art. 50(3) duty to inform callers.
- **Decision: deny and redesign.** The redesign is text-only, team-level workload analytics with no individual mood scores.

It's the most interesting case for GDPR because it combines employee monitoring, likely special-category data (stress is mental-health information), two groups of data subjects with different controllers, a US vendor and an automated input into shift decisions. It's also a good test of how the two laws stack: the AI Act bans the agent module outright, and GDPR has to explain why the data processing would be unlawful even without that ban, and what a lawful redesign needs.

The audit covers **the system as proposed** and **the redesign** I recommended, because the client needs to know both what to stop and what it can do instead.

## Fact pattern

> The client is a **contact-centre outsourcer with about 600 agents** at two sites in Germany *(assumed)*. It runs inbound customer-service lines for **telecom and insurance companies** *(assumed)*, handling roughly **30,000 calls a day** *(assumed)*, with callers mostly in Germany and Austria (EU). To tackle high sick leave and turnover, it wants a **"wellbeing assistant"** bought from a **US-headquartered emotion-AI SaaS vendor** that processes audio and video in its US cloud region *(assumed)*. The tool analyses each **agent's voice tone during calls** and **webcam images at the workstation** to detect stress and frustration in real time. It shows **team leads a per-agent dashboard** and feeds the signals into **shift planning and coaching conversations**. It also scores **each customer's mood** from their voice. Personal data: agents' identity, voice, face images, inferred emotional and stress states, shift and coaching records; callers' phone numbers, voice, call content (for insurance lines, possibly health information) and an inferred mood score. HR says no one is dismissed on the basis of the tool, and a team lead always reviews the data first.

*Shared with Friedrich as [`case_b_fact_pattern_shared_with_friedrich.md`](case_b_fact_pattern_shared_with_friedrich.md).*

### CFU 1: Recognize

- **Categories of personal data:**
  - *Agents:* identity data (name, employee ID, team), voice recordings, face images and video, real-time stress and frustration scores, shift and coaching records.
  - *Callers:* phone number, voice, call content, mood score.
- **Special-category data (Art. 9):**
  - *Agent stress, frustration and fatigue scores* are, in my view, **health data** (mental health, Art. 4(15)), especially once they are linked to sick-leave reduction and shift decisions. So Art. 9 applies.
  - *Voice and face* are biometric data under GDPR only if they are processed in a way that allows unique identification (Art. 4(14)). Art. 9 then covers them only when used *to identify*. If the tool attributes signals to agents by login rather than face or voice matching, the biometric route may not apply, but the health route still does.
  - *Insurance calls* may contain callers' health information in the call content.
- **Crosses an EU border?** **Yes.** Audio and video go to the US vendor's cloud. There may also be onward access by the vendor's support staff (unknown).

---

## Part 1: Audit worksheet

### Section A: Data map

| Field | As proposed | Redesign ("workload, not mood") |
|---|---|---|
| **Categories of personal data** | **Agents:** name, employee ID, team, live voice, webcam images and video, real-time stress and frustration scores, shift and coaching records. **Callers:** number, voice, call content, mood score. | **Agents:** employee ID linked to call transcripts (pseudonymised before analytics), team, shift data. **Callers:** number, call transcript (audio only until transcription). No voice-tone or face features. |
| **Sources** | Agents: headset audio, workstation webcam, workforce-management and HR systems. Callers: telephony platform. | Telephony platform → speech-to-text. Workforce-management system for queue and team volumes. Voluntary anonymous pulse survey. |
| **Purposes (one row each)** | **P1** Detect agent stress and frustration in real time. **P2** Use agent signals for shift planning and coaching. **P3** Score customer mood per call. | **P4** Record and transcribe calls for service quality (on the end-clients' instructions). **P5** Team- and queue-level workload analytics to trigger break rotation and queue rebalancing. **P6** Voluntary anonymous wellbeing pulse survey. |
| **Lawful basis per purpose** | **P1: none valid. Stop.** <br>• Consent: not freely given in employment (Recital 43; EDPB Guidelines 05/2020). <br>• Contract: not necessary to employ someone. <br>• Legitimate interests: fails the balancing test. Continuous webcam and voice emotion monitoring is far more intrusive than the aim needs, and agents can't reasonably expect it. <br>• Art. 9: no 9(2)(b) employment-law condition authorises it. <br>• The AI Act Art. 5 ban makes it unlawful anyway (Art. 5(1)(a) GDPR, lawfulness). <br>**P2: none valid. Stop.** It inherits P1's unlawfulness. It would also be a new purpose not compatible with P1 (Art. 6(4)). <br>**P3: TBD – legal review, likely fails.** The end-client is the controller and would need legitimate interests. Callers don't expect voice-based mood profiling, and it is also high-risk under the AI Act. Recommend dropping it. | **P4: legitimate interests (Art. 6(1)(f)) of the end-client** for quality and complaint handling. Purpose: service quality. Necessity: transcripts are needed to analyse topics and resolution. Balancing: notice at call start plus short retention. For the *recording itself*: **TBD – legal review**. Recording calls in Germany typically needs the caller's consent (§201 StGB). For insurance health content: **TBD – legal review** of the Art. 9 condition the insurer relies on. <br>**P5: legitimate interests (Art. 6(1)(f)) of the outsourcer, framed by a works agreement (Art. 88 GDPR).** Purpose: prevent overload and burnout. Necessity: only aggregated team and queue data, minimum group size of 10. Balancing: no individual scores, so no individual impact. *Note: §26(1) BDSG is shaky as a stand-alone basis after CJEU C-34/21 (2023), so I rely on Art. 6(1)(f) directly.* <br>**P6: consent.** Genuinely voluntary because it is anonymous and run by an external provider. If it is truly anonymous, GDPR may not apply at all. |
| **Retention per purpose** | P1–P3: **none**. Don't process. If anything was piloted, delete it and document the deletion. | **P4:** audio deleted within 24h of transcription, unless the end-client contract requires a recording. Transcripts kept for 30 days (to agree with each end-client). **P5:** only anonymised aggregates are kept, for 24 months. Access logs: 12 months. **P6:** anonymous, no personal data kept. |
| **Recipients and sub-processors** | Team leads, workforce planning, HR; the US emotion-AI vendor and its cloud host; end-clients (customer mood scores). | Team leads see team and queue dashboards only. No HR access to call-level data. An EU-hosted speech-to-text vendor. End-clients receive topic and resolution reports for their own lines. External survey provider for P6. |
| **International transfers and mechanism** | US vendor: the **EU–US Data Privacy Framework** if the vendor is certified (check the DPF list), otherwise **SCCs** (2021/914, controller-to-processor module) plus a transfer impact assessment. The DPF is valid today, but an appeal against it is pending at the CJEU, so SCCs should be ready as a fallback. *(Academic for P1–P3, since they stop.)* | Default: **EU hosting, no transfer.** If the speech-to-text vendor or cloud has a US parent: DPF or SCCs, plus contractual limits on remote support access from outside the EU. |

### Section B: Risk and rights

- **Special-category data (Art. 9)?** **Yes.**
  - Real-time stress and frustration scores about named agents reveal mental-health information. That is health data, and its link to sick-leave reduction makes it explicit.
  - Insurance calls can contain callers' health data.
  - Face and voice become Art. 9 biometric data if used to identify agents.
  - In the redesign, health content in transcripts must be redacted or excluded from P5 analytics.
- **Automated decision-making (Art. 22)?** **As proposed: likely yes, in effect.**
  - Signals feed shift planning (hours, pay, schedule) and coaching (performance). Those are similarly significant effects.
  - "A team lead always looks first" isn't enough if leads rely mainly on the score. Under CJEU *SCHUFA* (C-634/21), a score that decisively shapes a decision can itself count as a "decision".
  - The safeguards needed (meaningful human review, right to contest, explanation) wouldn't cure P1 anyway.
  - **Redesign:** no individual decisions, so Art. 22 isn't engaged. Workload triggers act on teams and queues.
- **DPIA required?** **Yes. At least 8 of the EDPB's 9 criteria apply**, against a threshold of 2:
  1. Evaluation and scoring of agents ✓
  2. Automated decisions with significant effect (shifts) ✓
  3. Systematic monitoring (continuous webcam and voice at work) ✓
  4. Sensitive data (health inference) ✓
  5. Large scale (600 agents, about 30,000 calls a day) ✓
  6. Combining datasets (emotion + workforce-management + HR) ✓
  7. Vulnerable data subjects (employees, power imbalance) ✓
  8. Innovative technology (emotion AI) ✓
  9. Prevents people using a service: partial (callers can only avoid it by hanging up)

  The redesign still needs a DPIA (criteria 3, 5, 6, 7).
- **Most likely data subject friction points:**
  - *Agents:* right of access to their own stress scores and how they were produced (Art. 15). Objection to legitimate-interest processing (Art. 21). Rectification of inferences they dispute ("I wasn't frustrated"). Contesting shift decisions (Art. 22(3)).
  - *Callers:* access to recordings and mood scores. Objection to profiling. All of these requests go to the end-client as controller, so the outsourcer needs a routing process.
- **Controller / processor split:**
  - **Outsourcer:** controller for agent data (as employer). **Processor** for caller data on behalf of each end-client. If it reuses caller data for its own aims (e.g. agent coaching), it becomes a controller for that use and breaches Art. 28(10).
  - **Telecom and insurance end-clients:** controllers for caller data.
  - **Emotion-AI vendor:** processor for the outsourcer and sub-processor for caller data. It becomes a **controller** if it uses the data to train its own models (must be ruled out by contract).
  - **Cloud host:** sub-processor.
  - **Works council:** part of the controller (§79a BetrVG), not a separate controller.
- **DPAs needed?** **Yes.**
  - Art. 28 DPA with the AI vendor (or, in the redesign, the speech-to-text vendor), covering a ban on training, sub-processor list, EU hosting, deletion and audit rights.
  - Updated DPAs with each **end-client**, approving the new sub-processor (Art. 28(2)) and documenting their instructions for P4.
  - A DPA with the cloud host, and with the survey provider if it receives any personal data.

### Section C: Law stacking

- **AI Act:**
  - Agent module is **prohibited** (Art. 5(1)(f), since Feb 2025). Customer mood is **high-risk** (Annex III 1(c), deployer duties from Dec 2027 under the Digital Omnibus) plus an **Art. 50(3)** notice to callers (since Aug 2026).
  - The AI Act adds what GDPR doesn't: a ban that **consent or legitimate interests can't override**, a biometric definition that doesn't require identification, Art. 50(3) disclosure, and the Art. 26(7) duty to inform workers' representatives before using a high-risk system at work.
  - The redesign stays outside Annex III 4(b) only while it never evaluates *individual* agents.
- **ePrivacy:**
  - No cookies or pixels. Webcams sit on employer-owned workstations, so Art. 5(3) device-access consent is likely not triggered (TBD).
  - Confidentiality of communications does matter for call recording and analysis. In Germany, recording also triggers §201 StGB. **TBD – legal review** on whether caller consent rather than legitimate interests is needed for P4 recordings.
- **Data Act:** **N/A.** No connected product or cloud-switching data. Headsets and webcams are standard work equipment, not IoT products generating usage data for the user.

---

## Part 2: Client recommendation memo

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
