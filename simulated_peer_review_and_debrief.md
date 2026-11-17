# Simulated peer review and debrief

**Author:** Sergii Rostovskyi  
**Date:** 17 November 2026  
**Method:** AI-assisted role simulation requested because no human partner was available.

This is a completed educational simulation, **not an independent human peer review**. No fictional reviewer name, meeting or partner approval is asserted. Acceptance of this substitute for the lab's partner-swap requirement remains an instructor decision. The shared input is the single NordDesk fact pattern in [the Audit Pack](gdpr_audit_pack_sergii_rostovskyi.md); both roles use those same facts.

## Review rubric

Scale: 1 = missing/weak, 2 = adequate with a material limitation, 3 = clear and supported in the written submission. Scores assess the advisory work, not real-world compliance or an official grade.

| Criterion | Score 1–3 | Simulated client-review comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | The memo says go with conditions for a restricted pilot and explicitly stops the current archive upload and personal-data preparation. The client can distinguish planning permission from a processing authorisation. |
| Lawful basis selection is justified | 3 | The worksheet separates support, training, inference, security and rights handling. Training remains TBD, with a concrete three-stage LIA; the memo does not suggest that a new notice or a corporate customer contract settles it. |
| Top actions are specific and sequenced | 3 | Legal/product decisions precede vendor clearance, followed by DPIA/control evidence and CTO release. Each action has an owner and a blocking condition. |
| Residual risks are named honestly | 3 | Contextual leakage, model-level erasure and foreign access remain after controls. The pack never describes filtering, SCCs or a test result as a guarantee. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | The memo flags the relevant layers, but communications-confidentiality applicability and final AI provider/deployer responsibilities still need legal/product review; the worksheet makes those limitations explicit. |

### Simulated client response

I accept the conditional recommendation for planning, but I do not authorise uploading the archive. Before proceeding, show why a documentation-only assistant is insufficient and how a valid erasure request reaches the trained model. If either point cannot be demonstrated, use the alternative design and keep historical chats out of training.

## Challenge and revision log

The statements in the second column are **deliberately constructed challenge propositions**, not quotations from a real partner or claims that an earlier submitted draft contained them. The final column records safeguards included in this pack after the adversarial review.

| Issue | Simulated weaker reading | Stronger reasoning / final treatment |
|---|---|---|
| Training basis | "We already serve these customers, so contract covers training." | Most contacts are employees of corporate subscribers, and training is a distinct purpose. P1 uses a conditional legitimate-interests assessment; P2 remains TBD pending compatibility and a separate LIA. |
| Anonymisation | "Removing names and emails means the vendor receives anonymous data." | Context can identify people and weights can retain facts. The pack treats redacted material and models as personal data until an appropriate assessment establishes otherwise. |
| Sensitive-data filtering | "We may always inspect health disclosures if the goal is removing them." | Filtering is itself processing. An authorised Article 9 handling route is a prerequisite, not an automatic consequence of good intentions. |
| DPIA | "All AI automatically requires a DPIA." | The decision rests on this scenario's highly personal content, scale and innovative reuse, with all nine screening criteria considered. |
| Transfers | "Signing SCCs makes the US transfer safe." | The TIA and effective protection remain release gates, particularly where the vendor sees plaintext. An EEA-only alternative is required if those gates cannot be met. |
| Rights deadline | "Every request has exactly 30 days." | The final pack uses one month, with only the applicable justified extension and notification. |

## Simulated debrief

**Agreement:** The consultant and simulated client positions agree that the unmodified two-year upload must stop and that the proposed training needs a DPIA before processing. They also agree that technical controls cannot substitute for a lawful basis.

**Divergence on lawful basis:** The weaker commercial position treats support improvement as automatically compatible with the original service purpose. The stronger reading examines expectations, sensitivity, consequences and alternatives, leaving training unapproved until those questions are answered; the final memo adopts this reading.

**Divergence on DPIA:** One simulated position infers a DPIA requirement from the word AI alone. The selected reasoning uses the actual nine-factor assessment, so the decision is defensible even if the technology label changes.

**Result:** The final Audit Pack incorporates the stronger readings and the client asks for evidence of necessity and model-level erasure before release. This records a simulated critique and response only; no human exchange or operational sign-off has occurred.
