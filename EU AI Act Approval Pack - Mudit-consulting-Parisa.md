
# EU AI Act Approval Pack
Consulting review of Parisa's four proposed AI use cases, performed by Mudit Airan

## Executive Summary

Of the four systems reviewed, **one cannot be launched as designed**, **one can launch only with binding controls**, **one can launch once disclosure requirements are met**, and **one is largely clear to proceed**. The overall risk picture (of all cases together) is uneven: the use cases have both a genuinely low-risk internal tool (product description generator) and a system that sits in the EU AI Act's prohibited category (In-store shoplifting risk scoring). Before any of these go live, I recommend a single sign-off gate (legal + compliance) rather than letting each business unit launch independently — the shoplifting-detection system in particular needs to be paused now.

| **Case** | **System** | **Inferred Category** | **Decision** |
| :-: | :-: | :-: | :-: |
| 1 | In-store shoplifting risk scoring (CCTV + biometrics) | **Prohibited** | Deny as proposed — redesign required |
| 2 | Travel booking support chatbot | **Limited risk / transparency** | Approve, with disclosures |
| 3 | Product description generator | **Minimal risk** | Approve, with flags |
| 4 | Graduate recruitment screening/ranking | **High-risk** | Approve, with controls |

## Case 1 — In-Store Shoplifting Risk Scoring

**Business problem:** Reduce shrinkage from theft across supermarket locations.

**Proposed system:** Computer vision on CCTV feeds analyzing facial expressions, body language, and movement patterns to generate a "risk score" per shopper, auto-flagged to security staff; the system also builds cross-visit behavioral profiles.

**Data/signals:** Live video, inferred facial expression/emotion, gait and movement analysis, historical visit profiles.

**Who's affected:** Every customer entering a monitored store, disproportionately anyone whose expression or movement pattern reads as "suspicious" to the model.

**Human role:** Security staff see the alert but do not independently assess before intervention — the AI determines who gets flagged; humans only act on the flag.

**Inferred category: Prohibited.** This combines biometric categorisation (emotion/behavior inference from a person's face and body) with automated risk-profiling used to predict the likelihood of a criminal act, applied to the general public in a physical retail space, with no meaningful human judgment upstream of the flag. That combination lands in Article 5 unacceptable-risk territory — it functions as a social-scoring-adjacent, predictive-criminality system rather than a straightforward security tool.

**Compliance implications:** Even a "monitoring only" version doesn't cure the core problem, because the profiling and the inference of intent from biometric/emotional signals is itself the violation — not just the downstream action. Data protection exposure (biometric data is special-category under GDPR) compounds this.

**Decision: Deny as proposed.**

**Lawful redesign path:**

- Drop emotion/behavior inference and facial profiling entirely.
- Replace with **rules-based loss-prevention tools**: EAS tags, POS exception reporting (voids, discount overrides, scan-avoidance patterns at self-checkout), and standard CCTV reviewed by trained staff using their own judgment — not an AI-generated suspicion score per person.
- If any computer vision is retained, restrict it to **object/inventory-level detection** (e.g., item left unscanned at self-checkout) rather than person-level risk scoring.
- Security staff make the judgment call; AI at most surfaces an operational exception, never a "this person is suspicious" verdict.

*Borderline argument:* One could argue the system isn't "law enforcement" and Article 5(1)(d) is scoped to public authorities — a private retailer using it internally might sit in a grey zone. **Legal should verify this reading**, but I don't recommend relying on it; regulators and DPAs have signaled retail emotion-recognition/biometric profiling is a priority enforcement area regardless of the law-enforcement carve-out debate.

*Next artifact needed:* A **Fundamental Rights Impact Assessment (FRIA)** is not the right first step here — a **redesign scoping note** documenting what was removed and why should come first, before any FRIA is considered for the replacement system.

## Case 2 — Travel Booking Support Chatbot

**Business problem:** Provide 24/7 customer support without scaling headcount.

**Proposed system:** Generative AI chatbot handling bookings, baggage, cancellations, and destination questions, escalating complex cases to a human agent; designed to converse "naturally," resembling a human employee.

**Data/signals:** Customer booking data, support documentation/FAQ content, conversation history.

**Who's affected:** Customers seeking support, who may not always realize they're talking to a bot.

**Human role:** Human agent takes over for complex issues — a real escalation path exists.

**Inferred category: Limited risk / transparency obligation.** This is a standard generative AI customer-interaction system. It doesn't make eligibility, pricing, or legal-status decisions about people — it's a comms tool. The risk is entirely about **disguising itself as human**, which the client explicitly wants.

**Compliance implications:** Article 50-style transparency obligations require that a person interacting with an AI system be informed they're doing so, unless it's obvious from context. "Communicate naturally so it feels like a human employee" is the part that needs correcting — natural language is fine, concealment is not.

**Decision: Approve with disclosures.**

Conditions:

- Clear, upfront disclosure at the start of any chat session ("You're chatting with our virtual assistant").
- Easy, discoverable path to a human agent at any point, not just after the bot fails.
- No design pattern that actively implies a human identity (no fake employee name/photo presented as a person).
- Log conversations for quality/audit purposes with a retention policy customers can be informed of.

**Borderline argument:** The company may argue "it's obvious from context it's a bot" given industry norms, removing the strict disclosure need — **legal should verify** whether implicit-obviousness is defensible here, but given the explicit brief to make it feel human, I don't think this exception applies.

*Next artifact needed:* A short **AI-interaction transparency notice** (chat opening message + support page copy) — this is the one blocking item before launch.

## Case 3 — Product Description Generator

**Business problem:** Marketing team is stretched thin writing product listings.

**Proposed system:** Generative AI drafts product descriptions from structured inputs (dimensions, materials, colour, features); a human marketer reviews and edits before publishing.

**Data/signals:** Product attribute data entered by staff; no customer data involved.

**Who's affected:** Internal marketing staff only, directly. Customers indirectly, as readers of the final published copy.

**Human role:** Full human review and edit before anything goes live — human is fully in the loop.

**Inferred category: Minimal risk.** No profiling, no ranking of people, no eligibility or pricing decision, internal tool with human sign-off on every output.

**Compliance implications:** No AI Act obligations apply at this risk tier beyond voluntary good practice. The real exposure is **consumer protection / advertising law**, not the AI Act:

- AI-generated claims about materials, durability, or origin must be factually accurate — an AI hallucinating "solid oak" for an engineered-wood product is a mislabeling/consumer-protection issue, not a hypothetical.
- Check for unintentional reuse of copyrighted competitor description language in training/output.
- GDPR is not really in play here since no personal data is processed, but confirm no customer reviews or personal data get fed in as context later.

**Decision: Approve.** Recommend a lightweight **fact-check checklist** for marketers reviewing AI drafts (materials, dimensions, care claims) rather than a compliance program — this is a quality-control issue, not a legal blocker.

**Borderline argument:** If descriptions later start incorporating competitor pricing or customer review data to "personalize" copy, this could shift risk tier — flag as a scope boundary, not a current issue.

*Next artifact needed:* None required for launch; optionally, a one-page internal usage guideline for marketing staff.

## Case 4 — Graduate Recruitment Screening

**Business problem:** High application volume is slowing down graduate hiring.

**Proposed system:** AI scores each candidate from CV, qualifications, work history, and application answers, and recommends who proceeds to interview.

**Data/signals:** CV content, qualifications, work history, free-text application answers.

**Who's affected:** Job applicants — directly, since low-ranked candidates may be filtered out of the process entirely.

**Human role:** Recruiters review the shortlist but "normally follow the AI ranking unless they notice an obvious error" — this is **nominal oversight, not real oversight**.

**Inferred category: High-risk** (Annex III — employment, recruitment, and selection of natural persons).

**Compliance implications:** This is squarely regulated, not a grey area. Requirements include: risk management system, data governance and bias testing on training data, technical documentation, logging/traceability, transparency to the deployer, **genuine human oversight** (not rubber-stamping), accuracy/robustness testing, and — for the deployer — a **Fundamental Rights Impact Assessment** before first use, plus registration obligations.

**Decision: Approve with controls — not automatic denial, but not launch-ready today.**

Required before go-live:

1. Bias/fairness testing across protected characteristics (gender, ethnicity-correlated proxies like name/school, disability-related gaps in work history) with documented results.
2. Redesign the review process so recruiters see and can act on *all* candidates, not just review exceptions in the shortlist — "follow the ranking unless something looks wrong" does not meet the oversight bar.
3. Full technical documentation and audit logging of scores and rationale.
4. FRIA completed before first use.
5. Candidate-facing notice that AI is used in screening, with a route to request human review.

*Borderline argument:* The agency may argue recruiters "always could" override, so oversight exists on paper — **legal should verify** whether documented-but-unused override rights satisfy the "genuine human oversight" standard, but current practice (default deference to AI ranking) is a weak position to defend under audit.

*Next artifact needed:* **FRIA draft** and a **bias testing report template** — both required before this can move to controlled launch.

## Consulting Review — Detailed Architecture Pass

| **Case** | **Likely category** | **Why this is your first-pass call** | **Proposed AI architecture** | **Provider / deployer / vendor** | **Required obligations or controls** | **Decision** |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **1 — In-store shoplifting scoring** | **Prohibited** | Combines biometric categorisation (facial expression, body language) with automated inference of likely criminal intent, applied to the general public in a physical space, with no real human judgment before the flag is acted on. This is Article 5 unacceptable-risk territory, not just "high-risk." | **Trigger:** shopper enters camera range. **Model behavior:** CV model reads facial expression/gait/movement, cross-references prior-visit profile, outputs a risk score. **Human review point:** none before the flag — security only sees the output. **Output/decision:** real-time "high-risk" alert pushed to security dashboard, triggering closer monitoring/intervention. **Logging layer:** persistent cross-visit biometric profile store (itself a separate exposure). | **Vendor:** CV/analytics provider building the model. **Deployer:** supermarket chain operating it in-store. | N/A as proposed — cannot be brought into compliance via controls; must be redesigned (see redesign path below) | **Deny as proposed** — offer lawful redesign (rules-based loss prevention, no person-level biometric profiling) |
| **2 — Travel chatbot** | **Limited risk / transparency** | Generative AI handling customer conversations — no eligibility, pricing, or legal-status decisions about people. The only regulated concern is that it's designed to pass as human, triggering the disclosure obligation rather than a high-risk classification. | **Trigger:** customer opens support chat. **Model behavior:** LLM with RAG over booking record + support docs generates a natural-language response. **Human review point:** live agent takes over on escalation (complex/failed queries), not before every response. **Output/decision:** answer delivered directly to customer, or handoff to human. **Disclosure layer:** session-opening notice identifying the bot as AI; conversation log retained per stated policy. | **Vendor:** LLM/chatbot platform provider. **Deployer:** travel company operating the bot on its own site/app. | Upfront AI disclosure at session start; visible, easy path to a human agent; no design element implying a human identity; conversation logging with a stated retention policy | **Approve with disclosures** — blocked only on adding the transparency notice before launch |
| **3 — Product description generator** | **Minimal risk** | Internal content-drafting tool. No profiling of people, no ranking, no eligibility or pricing decisions, and every output is reviewed and edited by a human before publishing. Real exposure is factual-accuracy/consumer-protection, not the AI Act. | **Trigger:** marketer enters product attributes (dimensions, materials, colour, features). **Model behavior:** LLM drafts a description from those inputs. **Human review point:** marketer reads, edits, and approves before anything is saved or published. **Output/decision:** final listing copy published to the storefront. **Logging layer:** none required beyond normal CMS version history. | **Vendor:** LLM/content-tool provider. **Deployer:** furniture retailer's internal marketing team (sole users). | Lightweight fact-check step for material/dimension/care claims before publishing; confirm no personal or customer data gets fed in later | **Approve** — no AI Act blockers; flag consumer-protection/misleading-claims risk as a quality-control item |
| **4 — Graduate recruitment screening** | **High-risk** | Squarely Annex III (employment/recruitment selection of natural persons). Directly determines who does and doesn't get an interview. "Recruiters follow the ranking unless they notice an obvious error" is nominal oversight, not genuine human oversight — the specific gap keeping this from being launch-ready. | **Trigger:** candidate submits CV, qualifications, work history, application answers. **Model behavior:** scoring model ranks each candidate against the role. **Human review point:** recruiter checks the shortlist, but by default defers to the ranking, only intervening on "obvious" errors — this is the control gap. **Output/decision:** ranked shortlist determines who is invited to interview; low-ranked candidates are effectively filtered out. **Logging layer:** score + rationale must be logged per candidate for audit and appeal, currently not specified. | **Vendor:** scoring/screening model provider. **Deployer:** recruitment agency running it against live applicant pools for employer clients. | Bias/fairness testing on this client's actual applicant data; redesigned oversight giving recruiters real visibility/authority over all candidates, not just exceptions; full technical documentation and score/override logging; FRIA before first use; candidate-facing AI-use notice with a route to request human review | **Approve with controls** — not automatic denial, but not launch-ready until the above are in place |

## Case 4 (Recruitment Screening) - Implementation Roadmap

**Before market placement (provider/vendor side):**

- Conformity assessment against Annex III high-risk requirements (internal or third-party, depending on final classification route).
- Risk management system documented across the full lifecycle.
- Training data documentation: provenance, representativeness, known limitations, bias mitigation steps taken.
- CE marking / EU database registration for the high-risk AI system.
- Instructions for use that clearly state intended purpose, limitations, and required human oversight measures.

**Before first use (deployer/client side):**

- Completed FRIA specific to this deployment context (graduate hiring, this candidate pool).
- Assign named human reviewers with authority, time, and training to meaningfully override — not just spot-check — the AI ranking.
- Internal policy defining what counts as an "obvious error" trigger vs. mandatory full review.
- Logging and retention policy for scores, overrides, and outcomes (minimum retention per Act requirements).
- Candidate transparency notice + complaint/appeal channel.

**Evidence to request from the vendor:**

- Bias/fairness test results broken out by protected characteristic, on data representative of this vendor's actual applicant pool (not just vendor's generic benchmark).
- Accuracy and robustness metrics, including performance on edge cases (non-traditional CV formats, career gaps, non-native language answers).
- Documentation of what the model actually weighs (feature importance/explainability output) — needed for both oversight and candidate appeals.
- Incident/change log process — how the client notifies the client of model updates that could shift scoring behavior.
- Confirmation of data handling (is candidate data used to further train the model; deletion/retention terms).

**What changed after the client discussion?**

My initial classifications matched the client’s intended categories. The discussion did not materially change the risk calls, but it changed the conditions for approval.

The original brief described a system with only nominal oversight — auto-reject bottom 60%, recruiters technically able to override but not actually reviewing anyone in that band. The vendor discussion surfaces that the gaps are broader than just "oversight design":

- Bias testing exists but isn't fit for purpose. It was run on a generic benchmark, not this bank's real applicant pool — so the original assumption that "some fairness testing has been done" overstates what's actually usable as evidence.
- No candidate-level explainability yet. This is new information: the model can't currently produce an individual rationale, which blocks the candidate-appeal requirement entirely — not just an oversight problem, a system-capability gap.
- No client-facing change notification process exists. The vendor updates the model quarterly with no signal to the bank, meaning the bank has been operating without visibility into scoring drift the whole time — this wasn't evident from the original brief.
- Data reuse for training was previously undisclosed to the client. The bank likely didn't know candidate data was feeding future model versions by default.

Net effect: the discussion moves this from "a high-risk system with a fixable oversight process" to "a high-risk system with oversight, evidence, and vendor-transparency gaps." The controls list in the approval pack should be expanded, not narrowed — bias testing needs to be redone on real data, per-candidate explainability needs to be built before appeals can function, and a model-change notification clause needs to go into the vendor contract before this can move toward "approve with controls" in practice rather than in principle.


**Legal References Considered**

- EU Artificial Intelligence Act (Regulation (EU) 2024/1689)
- General Data Protection Regulation (GDPR, Regulation (EU) 2016/679)
- Consumer protection/advertising standards (general, jurisdiction-dependent)


