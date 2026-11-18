# GDPR Audit Pack, Part 1 — Audit worksheet · Smart-toy factory: worker scoring and promotion

**Author:** Jaime Garate Marquerie · **Partner:** Sandra Obregón · **Option A** (case carried forward from *Classify Your Product*) · 18 Nov 2026
**Part 2** (client memo, as exchanged): [`client_recommendation_memo_toy_factory_promotion.md`](client_recommendation_memo_toy_factory_promotion.md)

**Tags:**
- **[F]** stated in the shared fact pattern;
- **[A]** auditor's inference or assumption;
- **[NS]** not specified in the scenario.

## 1. Transition note

- **Case carried forward:** **Case 2** of the four client cases Jaime wrote for Sandra in *Classify Your Product*.
- **The original Case 2 and its revision:**
  - The original Case 2 was a motorised ride-on toy for 18-month-olds with AI braking. It was high-risk through the **Art. 6(1) / Annex I** route (product safety), and its personal data was marginal.
  - During *Classify Your Product*, Sandra proposed replacing it so the high-risk example follows the Annex III pattern, and Jaime accepted (Slack, 17 Nov 2026, 16:51–16:56). The final Case 2: same smart-toy manufacturer, but the AI **scores assembly-line workers and recommends them for promotion**.
  - **AI Act category of the revised case:** **high-risk, Art. 6(2) and Annex III 4(b)**, decisions on promotion and evaluation of workers' performance.
- **Why it deserves a GDPR review:**
  - it profiles identifiable employees;
  - it reuses production records for a new purpose;
  - its output shapes careers;
  - all of this happens in a relationship with a power imbalance.

  The AI Act high-risk duties apply from 2 Dec 2027; the GDPR applies now.

## 2. Fact pattern (shared with Sandra inside the memo document, 17 Nov 2026)

> A company that manufactures smart toys wants to streamline quarterly appraisals of assembly-line employees. Its proposed AI system would use production and quality-control records for individual workers, including units assembled and parts arriving at inspection with defects. It would produce an individual score and recommend workers for promotion to line supervisor. A human supervisor could inspect the underlying records and would decide which candidate to put forward to HR. Workers are the affected data subjects; their precise location, the company's size, the data volume, vendors, hosting locations, retention rules and any existing agreements were not specified in the client scenario. This assessment assumes an EU/EEA workplace; it does not assume the proposed system is already operating.

## 3. CFU 1 — Recognize

- **Categories of personal data:**
  - worker identity (ID, line, shift);
  - units assembled per worker;
  - defects traced to the worker;
  - the AI score and promotion recommendation (newly created data);
  - the supervisor's decision [F/A].
- **Article 9:** not processed by design. **Inferable through proxies** [A]: lower output or more defects can reflect health, disability, pregnancy or caring duties. This is a discrimination risk even without explicit Art. 9 data.
- **EU border:** cannot be determined; vendors and hosting are [NS].

## 4. Section A — Data map (one row per purpose)

| # | Purpose | Data | Source | Art. 6 basis — justification | Retention (proposal) | Recipients / sub-processors | Transfers |
|---|---|---|---|---|---|---|---|
| P1 | Run production and quality control (existing purpose) | Units, defects per worker | Production and QC systems [F] | 6(1)(b) employment contract, or 6(1)(f) operational management [A] | Existing policy [NS] | Line managers, QC | [NS] |
| P2 | **AI scoring of individual performance (profiling)** | P1 data → score | Reused from P1 | **`TBD — legal review`**. Candidate: 6(1)(f) with the LIA below. **Not consent**: not freely given between employer and worker. **New purpose:** Art. 6(4) compatibility test required; it is not automatically covered by P1 | One appraisal cycle plus the challenge period (**TBD**) | AI vendor as processor [A] | Depends on vendor [NS] |
| P3 | Promotion recommendation and supervisor decision | Score, records, supervisor's reasons | System + supervisor | 6(1)(b) / 6(1)(f): managing the employment relationship [A] | Personnel file under national law (**TBD**) | Supervisor, HR | Internal |
| P4 | Bias and error testing; AI Act logs | Scores, overrides, outcomes | System | 6(1)(f) now; **6(1)(c)** once AI Act Art. 26(6) applies (2 Dec 2027) [A] | At least 6 months for AI Act logs | Compliance / HR | Internal |
| P5 | Vendor reuse of worker data to train its own models | All | — | **No basis identified.** Incompatible purpose; prohibit it in the DPA | n/a | — | — |

**LIA for P2 (three steps):**
1. **Legitimate interest?** Yes: fair, consistent and faster appraisal and promotion decisions.
2. **Necessary?** Not yet shown.
   - Supervisors already see the records [F].
   - Less intrusive options: a structured, non-AI dashboard of the same records, or criteria-based reviews.
   - Raw defect counts may be wrong if defects are caused by machines or shifts.
3. **Balancing?** It leans against the employer until safeguards exist:
   - workers are in a dependent position (Recital 155, Art. 88);
   - continuous productivity tracking affects their reasonable expectations;
   - careers are at stake.

   → **`TBD — legal review`**, after the DPIA.

**Purpose-limitation flag:** P1 records were collected to run production, and using them to rank people for promotion is a **new purpose** (P2). It needs a documented Art. 6(4) assessment and information to workers (Art. 13(3)).

## 5. Section B — Risk and rights

- **Special category data (Art. 9):** not collected [F]. Proxy risk: health, disability, pregnancy or caring duties can lower output [A]. Test for indirect discrimination before use.
- **Automated decision-making (Art. 22):** **less likely than in a recruitment ranking**, as Sandra's and my debrief conclusion records.
  - The supervisor can inspect the records and decides whom to put forward [F].
  - Art. 22 would be engaged if, in practice, supervisors simply follow the score. Promotion is a "similarly significant" effect.
  - **Safeguards:** the supervisor understands the evidence, can reject the score and records an independent reason; workers can contest the outcome.
- **DPIA (Art. 35):** **required.** It fits Art. 35(3)(a), and 6 of the 9 EDPB criteria apply:

  | # | EDPB criterion | Applies? | Why |
  |---|---|---|---|
  | 1 | Evaluation or scoring | **Yes** | Performance score [F] |
  | 2 | Automated decisions with legal or similar effect | Possible | Only if supervisor review is nominal |
  | 3 | **Systematic monitoring** | **Yes** | Continuous per-worker production tracking (WP248 cites employee monitoring) |
  | 4 | Sensitive data | Proxy only | [A] |
  | 5 | Large scale | Unknown | [NS] |
  | 6 | Matching or combining datasets | **Yes** | Production records + QC defect records |
  | 7 | Vulnerable data subjects | **Yes** | Employees are named in WP248 |
  | 8 | Innovative technology | **Yes** | AI scoring |
  | 9 | Prevents a right or a contract | No / arguable | A promotion opportunity, not access to a contract |

  The national authority's Art. 35(4) list was not consulted [A].
- **Data subject rights friction:**
  - **Access (Art. 15):** score, inputs and meaningful logic.
  - **Rectification (Art. 16):** **key in this case.** A defect wrongly attributed to a worker (a machine fault or a shift problem) must be correctable before it affects a promotion.
  - **Objection (Art. 21):** applies if P2 relies on 6(1)(f).
  - **Erasure:** limited by employment-record duties.
- **Controller / processor split:**
  - toy manufacturer = **controller** [A];
  - AI supplier = **processor** if it acts only on instructions, and controller for any reuse;
  - production and QC system vendors = possible sub-processors [NS].

  Not to be confused with the AI Act roles (supplier = provider; manufacturer = deployer).
- **DPA needed?** **Yes, with the AI supplier (Art. 28)**: no reuse for training, sub-processor flow-down, deletion and audit. None exists [NS].
- **National labour law [A, EU/Spain assumption]:** worker representatives may have information or consultation rights. In Spain, Art. 64.4(d) of the Estatuto de los Trabajadores covers algorithms that affect working conditions. To be checked by counsel.

## 6. Section C — Law stacking

- **AI Act cross-check:** **high-risk, Annex III 4(b).** One specific duty GDPR does not cover:
  - **Art. 26(7):** before putting the system into service at the workplace, the deployer must **inform workers' representatives and the affected workers**.
  - Other duties: human oversight by competent staff (Art. 26(2)); logs kept at least 6 months; the right to an explanation (Art. 86).
  - These apply from 2 Dec 2027.
- **ePrivacy check (added after Sandra's review):** **N/A on the stated facts.** The data comes from production and QC records [F], not from workers' own devices.
  - Art. 5(3) would apply if the system read data from terminal equipment, e.g. workers' phones, or company tablets or scanners used as terminals. **Confirm** the data sources before deployment.
- **Data Act check:** **possibly relevant, not a privacy issue.** If the production records come from connected assembly machines supplied by a third party, the Data Act governs access to and sharing of that machine data. Personal data in it remains under the GDPR. There is no cloud-switching question.
