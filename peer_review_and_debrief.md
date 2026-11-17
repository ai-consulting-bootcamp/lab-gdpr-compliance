# Partner swap — peer review & debrief

**Partner:** Elif Yurdakul

We swapped cases between the two AI Act labs: **I audited Elif's Case 2** (AI CV screening at a logistics company, see [GDPR_Audit_Pack_Pieter_Albrecht.md](GDPR_Audit_Pack_Pieter_Albrecht.md)), and **Elif audited my Case 2** (an online lender, *FlexKrediet B.V.*, making loan decisions with a model built on open-banking data). Both systems are **high-risk** under the AI Act, so the audits are directly comparable on structure: Art. 22, DPIA need, US vendor, bias.

## A. Elif's review of my memo (reviewer acts as the client)

*To be added once Elif has completed her review.*

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

**Client response:**

> _…_

## B. My review of Elif's memo (FlexKrediet AI credit scoring)

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | 3 | "Go with conditions" in the first line, with a one-sentence reason a CTO can act on: the system works, but the safeguards are missing today. |
| Lawful basis selection is justified | 2 | The worksheet is strong. Each purpose has a basis and a justification, and the hard calls (PSD2 explicit consent vs. GDPR consent, model training, bias testing under AI Act Art. 10(5)) are honestly marked *TBD*. Two gaps: (1) "legal obligation" for P1 covers the *duty* to assess creditworthiness, not the choice to use 12 months of full transactions and an ML model. That choice still needs its own proportionality argument. (2) The memo itself never names the lawful basis for the credit decision, so the client has to dig into the worksheet. |
| Top actions are specific and sequenced | 2 | Clear "before data flows → before launch → at launch" structure, and the Art. 9 category filtering in action 1 is a smart, concrete step. But the DPIA comes *after* live data starts flowing. Under Art. 35 it must be done *before* processing starts, and its outcome may change the vendor contract. Action 3 also bundles four separate tasks; splitting it would make ownership clearer. |
| Residual risks are named honestly | 3 | All three are real and specific: proxies like postcode and merchant type, a forced vendor change if the US framework falls, and credit officers rubber-stamping the score. Nothing is downplayed. |
| Law stacking is addressed (AI Act / ePrivacy) | 2 | AI Act is very good: correctly adds the fundamental rights impact assessment (Art. 27) and the right to explanation (Art. 86), and pairs the FRIA with the DPIA. ePrivacy is handled well in the worksheet (fraud fingerprinting) but is missing from the memo. Main gap: the **revised Consumer Credit Directive (CCD2, Directive (EU) 2023/2225)** applies from **20 November 2026**. It gives consumers a right to human intervention and an explanation when a creditworthiness assessment is automated, so it reinforces the Art. 22 findings and is in force before launch. Also worth one line: the AI Act's high-risk obligations for credit scoring apply from 2 December 2027. |

**Client response (as FlexKrediet):**

> We accept the recommendation, with one concern. Your own checklist marks data minimisation as a **fail** because we collect 12 months of full transaction history, but none of the three actions addresses that. Before we sign anything, tell us whether fewer months or aggregated features would be enough, because that changes what we ask the open-banking provider for.

## C. Debrief

*Draft notes to go through with Elif. Adjust once we've compared notes.*

| Question | Notes |
|---|---|
| Where did our audits agree on lawful basis? | Both use legitimate interests (with an LIA) for **model training on historic data** and flag it *TBD — legal review*, including the Art. 6(4) compatibility test. Both rely on pre-contract/contract steps for the core process. Both treat the US vendor as a processor *only if* the DPA bars it from training its own models, and we proposed almost the same DPA clause. |
| Where did they agree on DPIA need? | Both: DPIA clearly required, **7 of 9 EDPB criteria** each (scoring, automated decision, sensitive/inferred data, large scale, matching datasets, innovative technology, blocking access to a contract or job). |
| Where did we diverge? | **(1) The Art. 22 route.** Elif keeps automation under Art. 22(2)(a) with safeguards: *favourable* decisions (approvals under €5,000) are automated, and every *negative* decision goes to a credit officer. I removed the automated rejection entirely. **(2) Lawful basis anchor.** A lender has a *legal obligation* to assess creditworthiness; an employer has no legal duty to screen CVs, so my scoring rests only on legitimate interests. **(3) FRIA.** Required for Elif's case (AI Act Art. 27 covers credit scoring) but not for mine (private employer). |
| Which reading is stronger, and why? | On Art. 22 the two approaches turn out to be the same principle: **automate the positive outcome, keep a human on the negative one.** Elif's version is the cleaner design pattern and fits my case too: the tool can advance candidates automatically, but only a recruiter can reject. On lawful basis, her case is stronger by nature, because a legal obligation to assess plus CCD2's explicit rules give a firmer footing than my legitimate-interests balancing, which depends on safeguards being in place. Both audits share the same residual risk: human review that becomes rubber-stamping. |

**What I'd change after the swap:** borrow Elif's "automate positive, human on negative" wording in my action 3, and state the lawful basis for scoring in my memo in one line (the same gap I flagged in hers).
