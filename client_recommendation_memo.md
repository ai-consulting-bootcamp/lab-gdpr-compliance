# Client Recommendation Memo

**To:** Executive and legal teams, River Learning Collective  
**From:** Paola Hintze and Gretel  
**Subject:** GDPR readiness of the Intellectus diagnostic deployment

## Bottom line — Go with conditions

River Learning Collective may proceed with a limited Intellectus pilot, but no internal document may enter the production workflow until the controller–processor chain, DPIA, lawful-basis controls, retention enforcement, and international-transfer safeguards are complete. The mandatory consultant review reduces automated-decision risk, but it does not resolve excessive collection, sensitive-data, transparency, or vendor risks.

## Top three actions

**1. Complete and approve the DPIA before the first upload.** Map each field and document from the browser through n8n, OpenAI, logs, backups, consultant review, and deletion. Test necessity against safer alternatives such as client-side redaction, structured summaries, and pseudonymised excerpts. Disable special-category processing by default; if it is genuinely necessary, obtain legal approval for a specific Article 9 condition rather than relying on general consent.

**2. Put the contractual and transfer chain in place.** River Learning Collective and the Intellectus operator must sign an Article 28 DPA. Intellectus must verify n8n's hosting region, support access, subprocessors, and deletion terms, and contract with OpenAI under the applicable DPA. Any transfer outside the EEA must rely on a valid Chapter V mechanism—such as an adequacy decision or SCCs supported by the required transfer assessment and supplementary safeguards—before data flows.

**3. Implement enforceable operational controls.** Limit uploads to approved document types; scan and redact names and sensitive content; restrict access by role; retain raw documents, extracted text, prompts, and draft outputs for no more than 30 days after client acceptance; keep metadata-only security logs for 90 days; and maintain per-run lineage and deletion records. Update Articles 13/14 notices and provide workable access, correction, erasure, restriction, and objection procedures. Record the consultant's approval, correction, or rejection so human review is meaningful and auditable.

## Residual risks

Even after these actions, free text may reveal unexpected sensitive information, model outputs may contain inaccurate or stigmatising inferences, and public-source data may be outdated. Overseas subprocessor or support access may also create transfer exposure that contracts cannot eliminate completely. Finally, staff may over-rely on a polished report despite the human-review requirement. The pilot should therefore prohibit individual ranking or service-access decisions, use synthetic or strongly redacted initial data, and undergo periodic legal, security, and output-quality review.

**Word count (memo body): 363 words.**
