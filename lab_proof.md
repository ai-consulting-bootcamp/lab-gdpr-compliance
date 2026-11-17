# Lab proof: GDPR Mini Audit - Warehouse Shift AI

**Student:** Ayhan Demir · **Peer partner:** Julia Antunes · **Date:** 17 November 2026
**Case:** Warehouse shift AI, carried forward from Julia's EU AI Act lab case

## Deliverables

| Phase | Detailed answers | Contents |
| --- | --- | --- |
| 1 | [Phase1_Fact_Pattern_AyhanDemir.md](Phase1_Fact_Pattern_AyhanDemir.md) | Transition note and fact pattern |
| 2 | [Phase2_GDPR_Audit_Worksheet_AyhanDemir.md](Phase2_GDPR_Audit_Worksheet_AyhanDemir.md) | Data map, risk and rights, law stacking |
| 3 | [Phase3_Client_Recommendation_Memo_AyhanDemir.md](Phase3_Client_Recommendation_Memo_AyhanDemir.md) | Client memo: bottom line, top three actions, residual risks |
| 4 | [Phase4_Peer_Review_AyhanDemir.md](Phase4_Peer_Review_AyhanDemir.md) | Julia's memo, rubric scores, client response |

## Phase 1: Fact pattern

- Logistics company with ~5,000 warehouse workers in Germany and Poland *(assumed)*.
- The AI infers stress, frustration and motivation from webcam and voice data, then ranks workers for demanding shifts. Supervisors can override.
- Reclassified under the AI Act: first pass said high-risk (Annex III pt. 4(b)), but emotion inference at work is prohibited (Art. 5(1)(f)).

## Phase 2: GDPR audit worksheet

- **Lawful basis:** none for emotion inference (consent is not free in employment, legitimate interests fails, no Art. 9(2) exception). Shift recommendations only on objective data. Audit logs under legitimate interests.
- **Art. 9:** biometric data, plus possible health data from inferred mental state.
- **Art. 22:** likely, because a rarely used override is not meaningful human involvement.
- **DPIA:** required, 7 of the 9 EDPB criteria apply.
- **Roles:** company is controller. Emotion vendor, cloud host and scheduling vendor are processors with Art. 28 DPAs. US vendor needs DPF or SCCs plus a TIA.
- **Law stacking:** AI Act bans the feature. ePrivacy flagged for review (TDDDG §25). Data Act not applicable.

## Phase 3: Client memo

- **Bottom line: Stop as designed.** The goal of filling demanding shifts fairly is legitimate; the emotion input is not.
- **Actions:** (1) stop the pilot and delete video, audio and scores; (2) redesign on objective data and run a DPIA before first use; (3) DPAs, works council agreement, privacy notice and a real human review route before go-live.
- **Residual risks:** supervisors rubber-stamping recommendations, proxy bias in objective inputs, worker and works council distrust.

## Phase 4: Peer review

- Reviewed Julia's memo on the Kleinanzeigen seller messaging assistant ("Go with conditions").
- **Score: 11 / 15.** Bottom line 3, lawful basis 2, actions 2, residual risks 3, law stacking 1.
- **Client response:** propose a lawful basis for sellers and for buyers, and make a visible "sent by AI assistant" label (AI Act Art. 50(1)) a launch blocker.
