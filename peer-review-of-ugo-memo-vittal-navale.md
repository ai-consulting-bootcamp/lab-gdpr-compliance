# Peer review of Ugo's memo — Vittal Navale

Reviewing: [`From_Ugo_gdpr-audit-pack-ugo-ahukannah (1).md`](./From_Ugo_gdpr-audit-pack-ugo-ahukannah%20(1).md), Phase 3 client recommendation memo.

**Note on anchoring:** I only received the cleanly split files (audit pack and peer-review document separate) — no earlier mixed version reached me, so nothing anchored this read before the scores below were written.

## Rubric scores

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Go with conditions" stated up front, one-sentence reason, restated at the close with the six-week caveat attached. |
| Lawful basis selection is justified | **3** | Five purposes — more granular than mine — separating the talent-pool retention purpose (Art 6(1)(a)) and the claims-defence purpose (Art 6(1)(f)/(c)) out from the core two. The three-step LIA is written out explicitly and honestly concludes the balancing test *currently fails*, a stronger, more falsifiable claim than a bare LIA reference. |
| Top actions are specific and sequenced | **3** | Same three actions in substance as mine, but Action 3 separates out the DPF-certification-scope check ("covers HR data, not just certification generally") — real vendor due-diligence detail I hadn't isolated. |
| Residual risks are named honestly | **3** | The erasure risk is sharper than mine: deleting an application doesn't remove its influence on an already-trained model, and the honest fix is retraining on a cleaned set — I had this as a friction point in Section B but didn't carry it through as a residual risk in the memo itself. |
| Law stacking is addressed (AI Act / ePrivacy) | **3** | Gets the timing right (Annex III obligations from 2 Dec 2027, not inside the six weeks), correctly routes the conformity assessment to internal control under Annex VI with no notified body, and states ePrivacy consent under Art 5(3) overrides GDPR flexibility without hedging it as secondary. One item flagged below rather than accepted outright. |

## As the client

**Accepted, with one concern.** Section C cites  the company's new Art 4a as already providing a legal basis for bias-detection processing of special-category data — as far as I can verify, the Digital Omnibus is a Commission proposal, not yet adopted or in force, so the bias-testing mitigation shouldn't rest its legal basis on it yet. Until it's enacted, that mitigation needs to stand on a current Art 9(2) gateway or explicit consent, with the Omnibus noted as a future simplification rather than present law. Everything else — the Article 22 fix, the DPIA trigger under Art 35(3)(a), and the AI Act timing split — is accepted as written.
