# Peer review rubric and debrief — partner: Sandra Obregón

Each partner audited a case from their own *Classify Your Product* scenarios:
- **Jaime:** smart-toy factory, worker scoring and promotion (his revised Case 2);
- **Sandra:** logistics company, AI ranking of job applications (her Case 1).

Memos were swapped, and each partner reviewed the other's memo acting as the client.

## A. Exchange log

| Step | Date | Evidence |
|---|---|---|
| Sandra's memo received (recruitment case) | 17 Nov 2026 | `Memo.docx` |
| Jaime's memo + fact pattern sent (toy-factory case) | 17 Nov 2026 | `Jaime_Memo_GDPR_Fabrica_Juguetes.docx` |
| Jaime's review of Sandra's memo sent | 17 Nov 2026 | `Review_of_Sandra_memo.docx` |
| Sandra's review of Jaime's memo received | 17–18 Nov 2026 | `Sandra_Peer_Review_Jaime_GDPR_Memo.docx` |
| Debrief conclusion received from Sandra | 18 Nov 2026, 09:49 | Recorded in section D and in `lab_proof.md` §5 |

## B. Sandra reviews JAIME's memo (she acts as the client) — received

| Criterion | Score 1–3 | Comment (Sandra, verbatim) |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Proceed with conditions only" is clear from the start. The memo explains why using AI scores to recommend promotions needs safeguards. |
| Lawful basis selection is justified | **3** | The memo explains why the company should check necessity and balance its interests against workers' rights before relying on legitimate interests. It also explains why the company should check whether it can reuse production records for promotions. |
| Top actions are specific and sequenced | **3** | First, confirm the lawful basis. Then complete the DPIA, test the scores and plan human review. Finally, check vendor agreements, transfers and retention. |
| Residual risks are named honestly | **3** | A machine problem or a difficult shift could lower a worker's score even if the worker did their job well. This example makes the risk clear. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | The memo identifies the system as high risk under the AI Act. I would add one specific AI Act duty and a short ePrivacy check to confirm whether the system accesses data on workers' devices. |
| **Total** | **14/15** | |

**Client response (Sandra):**

> We accept the recommendation to proceed with conditions. Before we approve the pilot, please explain how supervisors will check whether a low score comes from the worker's performance, a machine problem or shift conditions.

**What changed after her review:**
- The worksheet (Section C) now names a specific AI Act duty: **Art. 26(7)**, informing workers and their representatives.
- It adds an **ePrivacy check**: N/A unless data is read from workers' devices.
- Section B adds **rectification (Art. 16)** of wrongly attributed defects, which answers her client question.
- The memo itself was not changed after the swap.

## C. Jaime reviews SANDRA's memo — sent 17 Nov 2026

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | The decision is right at the start ("go with conditions") with the reason in one sentence. Anyone reading it knows straight away what you recommend. |
| Lawful basis selection is justified | **2** | You separate the application itself (pre-contract step) from the AI ranking, which goes to Legal, and you keep consent apart for the candidate database. What's missing is naming Art. 6 and saying which bases Legal should look at (contract or legitimate interest). Action 1 is really an Art. 22 safeguard, but the article never appears. |
| Top actions are specific and sequenced | **3** | Very concrete: DPAs with Microsoft 365 and OpenAI, an EEA transfer check and testing the filter with fictional CVs, including one with health data. The order makes sense. Action 1 packs three things together (DPIA, lawful basis and human review). |
| Residual risks are named honestly | **3** | The three risks are realistic: unusual CVs ranked too low, the filter missing sensitive data, and HR following the list under pressure. Indirect discrimination (e.g. through shift availability) could be added. |
| Law stacking is addressed (AI Act / ePrivacy) | **3** | Links human review to the AI Act's human oversight requirement, and only asks for cookie consent "if ePrivacy requires it", which is correct. Could mention that the AI Act high-risk obligations apply from December 2027, while GDPR applies now. |
| **Total** | **14/15** | |

**Jaime's response as the client:**

> We accept "go with conditions" and the order of the actions. Before we commit, though, we need to know how many HR hours per vacancy it takes to review everyone left out, and what the minimum is to stay compliant. We'd also like you to tell us which lawful basis you expect Legal to choose for the ranking.

## D. Debrief (CFU 5) — compare notes

| Topic | Jaime (toy-factory promotion) | Sandra (recruitment ranking) | Agreed reading |
|---|---|---|---|
| DPIA needed? | Yes | Yes, before the pilot | **Agree:** both cases need a DPIA |
| Human review | Supervisor must understand the evidence, be able to reject and record a reason | HR reviews applicants who would be left out, with authority to change the outcome | **Agree:** review must be able to change the outcome |
| Article 22 | Less likely: the supervisor checks the records before proposing anyone | More likely: the ranking can exclude applicants before anyone reads their CV | **Agree:** the Art. 22 concern is clearer in the recruitment case |
| Lawful basis for AI scoring | `TBD — legal review` (legitimate interests only after the LIA; not consent) | "Ask Legal to confirm" | **Agree:** confirm before using real personal data |

**Joint conclusion (Sandra, 18 Nov 2026, 09:49 — verbatim):**

> Both cases need a Data Protection Impact Assessment and a human review that can change the outcome. In the recruitment case, the AI ranking can leave applicants out before HR reads their CVs. In the promotion case, the supervisor can check the records and reject the AI recommendation before proposing a worker for promotion. This makes the Article 22 concern clearer in the recruitment case. In both cases, the company should confirm the lawful basis for AI scoring before using real personal data.
