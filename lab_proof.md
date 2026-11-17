# Lab proof — Same product, privacy lens

**Student:** Pieter Albrecht
**Scenario:** Option A, carried forward from my partner's EU AI Act lab: Case 2, AI CV screening for a logistics company in Germany and Poland with a US vendor (high-risk under the AI Act). Client name fictional: Kranich Logistik GmbH.

This is the entry point for the reviewer. Each section below links to the supporting file.

## 1. Workflow

```
AI Act lab case ──► Transition note + fact pattern ──► CFU 1 Recognize
                                                            │
                     ┌──────────────────────────────────────┤
                     ▼                                      ▼
            Section A Data map                    Section B Risk & rights
         (lawful basis per purpose)          (Art. 9 · Art. 22 · DPIA · roles)
                     └──────────────┬───────────────────────┘
                                    ▼
             Section C Law stacking (AI Act · ePrivacy · Data Act · BetrVG)
                                    ▼
                 Client memo (go / go with conditions / stop)
                                    ▼
               Reinforce + Stretch ──► Partner swap & debrief
```

## 2. One run: input → evidence → output

**Input (fact pattern, condensed):** about 400 hires a year in DE and PL, up to 300 applications per role, two recruiters. A US vendor scores CVs against the job description and 5 years of "top performer" employee profiles. Only the top 20 are read; the rest are auto-rejected after a week.

**Evidence produced (from the [audit worksheet](GDPR_Audit_Pack_Pieter_Albrecht.md#part-1--audit-worksheet)):**

| Check | Result |
|---|---|
| Lawful bases | 6 purposes mapped. Pre-contract steps for the application process; legitimate interests for scoring and top-performer profiles (*TBD — legal review*); **no valid basis for the auto-rejection as designed**; consent for the talent pool |
| Art. 9 | Present (photos, health mentions) and inferable (proxies). Bias risk from top-performer profiles |
| Art. 22 | **Triggered.** Solely automated rejection with significant effect; nominal human review doesn't count (*SCHUFA*, C-634/21) |
| DPIA | **Required.** 7/9 EDPB criteria |
| Transfers | US vendor: EU-US DPF if certified for HR data, SCC fallback (DPF appeal pending at the CJEU, C-703/25 P) |
| AI Act | High-risk (Annex III 4(a)). Deployer duties: human oversight, logs, inform workers and applicants. Applies from 2 Dec 2027 (Reg. (EU) 2026/1744) |
| Other | Works-council consent (BetrVG §§87, 95) is a hard blocker for a Q1 launch |

**Final output:** [Client recommendation memo](GDPR_Audit_Pack_Pieter_Albrecht.md#part-2--client-recommendation-memo). **Go with conditions, but not in the current design.** Three sequenced actions (works council → DPA + DPIA + bias test → human sign-off replacing auto-rejection) and three residual risks (rubber-stamping, hidden bias, US transfer).

## 3. Failure / limitation I hit

- **The Art. 22 analysis has two defensible routes.** Redesigning to human sign-off is the safe answer. Keeping automated rejection under Art. 22(2)(a) with safeguards is legally arguable at high volume. I picked the safer route but flagged it for legal review and the debrief.
- **I had to add facts.** The partner's case doesn't say whether the Polish operation is a separate entity, how many employees there are or whether works councils exist. I stated my assumptions in the fact pattern; they change the controller split and the rollout timeline.
- **German employee-data law is unsettled.** After CJEU C-34/21, whether §26 BDSG is a valid basis is unclear, so I relied on GDPR Art. 6 directly.
- **Fictional vendor:** I couldn't check a real DPF certification, DPA or AI Act conformity documentation.
- **Peer review pending** until the partner swap (see [peer_review_and_debrief.md](peer_review_and_debrief.md)).

## 4. Supporting files

- [GDPR_Audit_Pack_Pieter_Albrecht.md](GDPR_Audit_Pack_Pieter_Albrecht.md) — transition note, fact pattern, audit worksheet (CFU 1, Sections A–C), client memo
- [reinforce_DPIA_outline_DPA_clause_UK.md](reinforce_DPIA_outline_DPA_clause_UK.md) — DPIA outline, key DPA clause, UK GDPR variant
- [stretch_privacy_by_design_checklist.md](stretch_privacy_by_design_checklist.md) — data-protection-by-design checklist
- [peer_review_and_debrief.md](peer_review_and_debrief.md) — rubric and debrief for the partner swap
