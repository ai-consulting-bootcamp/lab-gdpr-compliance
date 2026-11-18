# Recommendation Memo – Can we build the RCSA Evidence & Challenge Agent?

**To:** Head of Operational Risk, [Bank] · **From:** Murat Çömez, consultant · **Date:** 18 November 2026 (v2, after peer feedback)

**Purpose.** Should you build an AI agent that suggests process risks and challenges RCSA answers with loss events and KRIs? This memo covers applicable rules, responsibilities and main risks.

**Which rules apply.**
- **GDPR applies.** It processes employee data (process owners, staff named in loss events) and some customer references.
  - **Lawful basis:** Art. 6(1)(f), legitimate interest in effective operational risk management, with a documented balancing test. Art. 6(1)(c) does not fit (no law requires this specific processing); employee consent is not valid.
  - **Health and fraud details** (Art. 9 and 10) are not needed; they must be filtered out rather than given a legal basis.
- **EU AI Act:** not high-risk.
  - The provider must mark AI-generated report text in a machine-readable way (Art. 50(2)).
  - Users need basic AI training (Art. 4).
- **DORA and MaRisk outsourcing rules:** the language model is an external ICT service.
- **German employment law:** works council involvement, because the tool could be used to monitor staff.
- **ePrivacy:** not applicable (internal tool, no device tracking).

**Who is responsible.**
- **The bank** is the GDPR **controller** and the AI Act **deployer**.
- **The build team** is the AI Act **provider**, and a GDPR processor if it hosts the tool.
- **OpenAI** is a **processor** and an ICT third-party provider. *Confirm once the delivery model is fixed.*

**Main risks.**
1. **Sensitive data leaves the EU.** Loss event texts may contain names, health details or suspected fraud, and would go to a US provider. Verify the transfer mechanism (EU–US Data Privacy Framework, or Standard Contractual Clauses with a transfer impact assessment).
2. **Staff monitoring.** Results shown per person could be used to judge employees: a GDPR and works council issue, and possibly high-risk under the AI Act.
3. **No privacy design yet:** no retention rule, privacy notice or impact assessment.

**Recommendation: go ahead, with conditions.**
1. **Redact and pseudonymise** before anything reaches the language model.
2. Report **per process, never per person**; write this into the tool's purpose.
3. **DPIA and legitimate interest assessment** with the DPO before real data is used.
4. **OpenAI due diligence:** data processing agreement, transfer mechanism, EU region or zero retention, DORA register entry.
5. Inform the **works council** early.

Build and test on synthetic data now; move to real data after steps 3 and 4.

*First-pass consulting view, not legal advice; Legal and the DPO should confirm.*
