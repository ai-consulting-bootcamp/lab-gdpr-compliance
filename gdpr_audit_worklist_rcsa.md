# GDPR Audit Worklist – RCSA Evidence & Challenge Agent (pre-build)
**Consultant:** Murat Çömez · **Client:** [Bank], Operational Risk Management · **Date:** 17 Nov 2026
**Stage:** before build. Planned use with real bank data.

## Section A – Scope and data
| # | Question | Answer |
|---|---|---|
| A1 | Is personal data processed? | **Yes.** Process owner names, roles and emails; RCSA answers; names of reporters and employees in loss events; customer references; free-text loss narratives; challenge flags linked to owners. |
| A2 | Whose data? | Employees (1st and 2nd line), customers, occasionally third parties named in loss events. |
| A3 | Sources | Owner input, RCSA records, internal loss database, KRI reporting. No external sources. |
| A4 | Purposes | Risk identification, evidence-based challenge, rating and reporting. **Not** employee evaluation. |
| A5 | Controller | The bank. |
| A6 | Processors / vendors | OpenAI (LLM API); the tool provider if hosted as SaaS; cloud hosting; LangSmith only if tracing is enabled. |
| A7 | Transfers outside EEA | **Yes, likely** (OpenAI, US). Needs DPF or SCCs and a TIA. |
| A8 | Lawful basis | Art. 6(1)(f) legitimate interest with LIA (legal-obligation basis too indirect; consent invalid for employees). |
| A9 | Retention | Not defined. Must align with the RCSA cycle and audit retention. |
| A10 | Data minimisation possible? | **Yes:** pseudonymise names and customer refs before the LLM; use role instead of owner name. |

## Section B – Risks and rights
| # | Question | Answer |
|---|---|---|
| B1 | Special category data (Art. 9)? | Not requested, but **possible in loss narratives** (injuries, sickness). |
| B2 | Criminal offence data (Art. 10)? | **Possible:** internal fraud events. |
| B3 | Profiling / evaluation of people? | Not intended, but challenge flags per owner could be used to evaluate staff. Design it out. |
| B4 | Automated decisions with legal / similar effect (Art. 22)? | No. Human approval of ratings; nothing decided about individuals. |
| B5 | DPIA required? | **Likely yes:** employees, new technology, possible sensitive data, transfer, evaluative output (≥ 2 EDPB criteria). |
| B6 | Information to data subjects | Staff privacy notice (Art. 13); Art. 14 for employees named in loss events. |
| B7 | Access, rectification, erasure, objection | Export per owner; owners can edit answers; retention rule; objection process (needed under 6(1)(f)). |
| B8 | Security (Art. 32) | Access limited to ORM; encryption; audit log; vendor zero-retention settings. |

## Section C – Law tracking
| Law | Applies? | Note |
|---|---|---|
| EU AI Act | Yes | Limited risk (Art. 50(2)); Art. 4 AI literacy; avoid Annex III 4(b) (worker evaluation) |
| DORA | Yes | OpenAI and hosting are ICT third parties: register, risk assessment, contract terms |
| MaRisk AT 9 / EBA outsourcing | Yes | Outsourcing analysis |
| BDSG §26 / BetrVG §87(1) Nr. 6 | Yes | Employee data; works council co-determination |
| ePrivacy / TDDDG | No | Internal tool, no tracking |
| Data Act | No | No connected products |
| Banking secrecy | Yes | Customer references |
