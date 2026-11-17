# Lab proof — same product, privacy lens

**Scenario** EU AI Act Client Brief 2, reused for a GDPR audit of AI-assisted staffing.\
**Final recommendation** Go with conditions. The proposal stays off live applicant data until necessity and lawful basis, vendor and transfer controls, and DPIA and meaningful review gates are closed.

## Reproduce one audit query

From the repository root, run the following with Python 3.8+ and no third-party dependencies or network access.

```bash
python3 shortlist-review-check.py synthetic-shortlist-input.json
```

- **Workflow:** [shortlist-review-check.py](shortlist-review-check.py) checks whether each eligible synthetic applicant has a reviewer ID, a recorded reason and a review timestamp before the shortlist closed. It does not score applicants or select who is hired.
- **Input:** [synthetic-shortlist-input.json](synthetic-shortlist-input.json) represents one warehouse shift and three eligible applicants. Rank 1 has a pre-close review, rank 2 has no review and rank 3 has a review entered after the shortlist closed.
- **Observed evidence:** [synthetic-shortlist-evidence.json](synthetic-shortlist-evidence.json) records one timely review, three missing review fields for `DEMO-A02`, and a late review for `DEMO-A03`. The command exited with status 2 by design and returned `BLOCK_AI_SHORTLIST`.
- **Final output:** [GDPR audit pack and client memo](gdpr-audit-pack-sean-langsdorf.md) contains the fact pattern, purpose-level data map, rights and DPIA screen, law stacking and the recommendation. The run supports one recommendation in the memo: do not close an AI-supported shortlist before every eligible candidate has been reviewed.
- **Limitation:** A timely reason can be boilerplate. The script cannot establish that a reviewer understood the evidence, could overturn the rank or covered applicants omitted upstream. Production validation needs full ATS queue reconciliation and sampled recruiter interviews or observed reviews. This proof is a synthetic control check, not evidence of live GDPR compliance.

## Partner step and extensions

The [peer review sheet](peer-review-rubric.md) contains the partner handoff, rubric and debrief prompts. Actual partner feedback is pending. The [design safeguards](design-safeguards.md) add a DPIA outline, a proposed DPA clause, the UK variation and a concise privacy-by-design checklist. See [README](README.md) for the full file index.
