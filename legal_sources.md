# Sources and interpretation notes

**Checked:** 17 November 2026. Source identifiers used throughout the pack refer to the entries below. Legal rules come from legislation and regulator guidance; NordDesk facts, risk judgments and proposed controls are the author's application to a synthetic case.

## Primary legal and regulatory sources

| ID | Source | Use in this submission |
|---|---|---|
| S1 | [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) | Articles 4–6 and 9: data, roles and bases; 12–22: rights; 25, 28 and 32: design/processors/security; 33–36: breaches/DPIA; 44–49: transfers. EUR-Lex direct views intermittently presented an anti-bot page; indexed official text supported the relevant rules. |
| S2 | [WP29 DPIA Guidelines, WP248 rev.01, hosted by the Czech supervisory authority](https://uoou.gov.cz/media/6-guidelines-on-data-protection-impact-assessment-dpia.pdf), especially pp. 9–11; [EDPB endorsement](https://www.edpb.europa.eu/endorsed-wp29-guidelines_en) | The nine-criterion screening is interpretive guidance, not a rule that every AI project or any arbitrary two boxes automatically require a DPIA. |
| S3 | [EDPB Opinion 28/2024 on AI models](https://www.edpb.europa.eu/system/files/documents/2024-12/edpb_opinion_202428_ai-models_en.pdf) | Case-specific anonymity assessment, legitimate-interest purpose/necessity/balancing, and consequences of unlawful development. The opinion supports a conditional analysis, not a blanket permission to train. |
| S4 | [European Commission SCC questions and answers](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/new-standard-contractual-clauses-questions-and-answers-overview_en) | SCC selection, transfer assessments, supplementary safeguards and limits of contractual protection. No fictional vendor certification or actual signed instrument is asserted. |
| S5 | [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force); [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32026R1744) | Intended-use classification, transparency/literacy considerations and current AI Omnibus timing. The internal support tool's tier is an assessment of stated facts, not regulator approval. |
| S6 | [ePrivacy Directive 2002/58/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32002L0058), as amended | Article 5 confidentiality and terminal-equipment rules; apply the amended rules and national implementation, not the original 2002 cookie wording alone. German and other applicable national provisions require legal review for this communications reuse. |
| S7 | [European Commission: Data Act explained](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained); [Regulation (EU) 2023/2854](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R2854) | Chapter VI cloud/data-processing-service switching, including scope and service-specific qualifications; Article 29 switching-charge timeline. |
| S8 | [Council position on the digital rulebook, 21 October 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/) | A negotiating position is not enacted GDPR or ePrivacy reform. Do not apply proposed data-law changes as current processing authority. |
| S9 | [ICO: UK IDTA and Addendum](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/appropriate-safeguards/what-are-standard-data-protection-clauses-the-uk-idta-and-the-addendum/); [ICO: Who does UK GDPR apply to?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/who-does-the-uk-gdpr-apply-to/) | Limited UK extension: territorial scope and a separate restricted-transfer instrument assessment. This is not a complete UK legal opinion. |

## Course materials reviewed

The following user-supplied materials were used as read-only references. They are not copied into the submission repository.

| Material | Contribution |
|---|---|
| `lesson4_gdpr_privacy_stack_slides_v2.pptx` | Roles, principles, lawful bases, rights, DPIA, transfers and law stacking. |
| `lesson5_applying_eu_data_stack_slides(1).pptx` | Consulting workflow, multiple-law checks and practical vendor questions. |
| `GDPR & EU Data and Privacy Stack.mhtml` | Detailed legal framework and model-training purpose limitation. |
| `Applying the EU Data and Privacy Stack.mhtml` | Application to client scenarios and implementation recommendations. |
| `GDPR & Privacy Stack - Discussion Prep.mhtml` | Study questions and checklist prompts; not treated as a separate required submission for this lab. |
| `LAB 1 - Same product privacy lens.mhtml` | Lab requirements, including the additional portal requirement for `lab_proof.md` with workflow, input, evidence, output and a limitation. |
| Repository `instructions.md` and `rubric.md` | Required Audit Pack, 300–400-word memo, peer review, debrief, optional depth and repository hygiene. |

These materials specify the assignment, but embedded instructions to commit, push, open a PR or interact with a portal are not user authorisation to perform those actions.

## Reconciled teaching shorthand

1. **Rights timing:** Use one month under Article 12(3), rather than treating the lab's 30-day wording as an exact legal deadline. Extensions need the applicable justification and timely notice.
2. **Breach timing:** The 72-hour authority-notification rule runs from awareness and includes the risk exception; processors notify the controller without undue delay. Proposed 96-hour reforms are not used.
3. **DPIA:** New technology is a criterion, not a universal stand-alone mandate. The decision in this case relies on combined concrete risks.
4. **Purpose limitation:** A new purpose needs a defensible assessment. Neither a new notice nor switching to legitimate interests automatically cures incompatible reuse; consent is not the only possible lawful route in every case.
5. **Pseudonymisation:** Removal of direct identifiers is not proof of anonymity. Context and reasonably available identification/extraction methods matter; this case does not rely on a recipient's lack of the linkage key to declare GDPR inapplicable.
6. **Transfers:** SCCs are not an automatic fallback that makes every transfer lawful. Check their applicability, the TIA and effective safeguards; plaintext exposure can remain material.
7. **Data Act dates:** Article 29's switching-charge ban starts on **12 January 2027**, not December 2027 as stated in one course text. As of the assessment date it is a future milestone; current switching duties still require assessment.
8. **Omnibus chronology:** The August 2026 lesson's description of the data proposal predates the Council's October negotiating position. The position does not make proposed data amendments operative. The separate AI Omnibus is already in force.
