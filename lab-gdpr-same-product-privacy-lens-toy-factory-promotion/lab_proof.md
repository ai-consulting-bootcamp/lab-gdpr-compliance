# lab_proof — Same product, privacy lens (smart-toy factory: worker scoring and promotion)

**Entry point for the reviewer.** Read in this order:
1. [`gdpr_audit_worksheet_toy_factory_promotion.md`](gdpr_audit_worksheet_toy_factory_promotion.md) — Part 1: transition note, fact pattern, CFU 1, Sections A–C
2. [`client_recommendation_memo_toy_factory_promotion.md`](client_recommendation_memo_toy_factory_promotion.md) — Part 2: memo as exchanged, 383 words
3. [`peer_review_rubric_and_debrief.md`](peer_review_rubric_and_debrief.md) — swap, both reviews, client responses, debrief

## 1. Code or workflow export

**NOT APPLICABLE — documentary audit.** The case is a written client scenario.

The only code here is a read-only check of the fact pattern: [`proof/source_fact_check.py`](proof/source_fact_check.py).

## 2. One query actually run

- **Date:** 18 Nov 2026, ~10:05 CET.
- **Where:** the tutor's sandbox.
- **Input:**
  - the fact pattern (116 words) in `Jaime_Memo_GDPR_Fabrica_Juguetes.docx`, the document sent to Sandra. SHA‑256 of the file: `022fae6e…dccd155b`;
  - term list [`proof/terms_lab1_toy.txt`](proof/terms_lab1_toy.txt).

```text
chars_in_scope 802 words_in_scope 116
FOUND     production and QC records (1)
FOUND     units assembled (1)
FOUND     defects attributed (1)
FOUND     individual score (1)
FOUND     promotion recommendation (1)
FOUND     human supervisor decides (1)
FOUND     workers are data subjects (1)
FOUND     EU/EEA assumption stated (1)
NOT FOUND vendor named (0)
NOT FOUND retention period stated (0)
NOT FOUND workers' devices / terminal equipment (0)
```

The full log is in [`proof/lab1_toy_fact_check.txt`](proof/lab1_toy_fact_check.txt).

## 3. Final output (how the evidence was used)

- **FOUND** facts are tagged [F] in the worksheet.
- Vendor and retention are **not stated**, so they are [NS]. They drive the "confirm vendor roles, DPA, transfers and retention" action.
- **No devices in the facts:** this supports Section C's "ePrivacy N/A on the stated facts, confirm data sources". Sandra asked for exactly this check in her review (law stacking, 2/3).
- **Memo:** 383 words (`wc -w`). Peer review received: **14/15**.

## 4. Failure or limitation hit

1. **Case version mix-up (real, fixed on 18 Nov).**
   - At first, the tutor prepared this lab on **Sandra's** recruitment case.
   - The memo Jaime actually exchanged is about **his own revised Case 2** (toy factory, promotion).
   - Sandra's debrief note, which compares "the recruitment case" with "the promotion case", exposed the mismatch.
   - The folder was rebuilt around the case actually exchanged. The recruitment-case draft was removed from this submission.
2. **The case was revised.** The original Case 2 (a motorised toy, Annex I) carried almost no personal data. Sandra proposed the factory version during *Classify Your Product* and Jaime accepted it (Slack, 17 Nov 2026, 16:56).
3. **Thin scenario.** Vendors, volume, hosting and retention are not specified, so the lawful basis for AI scoring stays `TBD — legal review`.
4. **Missing official source:** the official `01_gdpr-fundamentals.md` lesson was not available and has not been read.

## 5. Debrief conclusion (received from Sandra Obregón, 18 Nov 2026, 09:49 CET — verbatim)

> Both cases need a Data Protection Impact Assessment and a human review that can change the outcome. In the recruitment case, the AI ranking can leave applicants out before HR reads their CVs. In the promotion case, the supervisor can check the records and reject the AI recommendation before proposing a worker for promotion. This makes the Article 22 concern clearer in the recruitment case. In both cases, the company should confirm the lawful basis for AI scoring before using real personal data.
