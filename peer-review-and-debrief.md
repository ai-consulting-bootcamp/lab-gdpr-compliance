# Peer review and debrief

> **Disclosure.** My EU AI Act lab partner (S. Rostovskyi) finished this lab earlier, on 17 Nov, using **Option B(a)**: fine-tuning an LLM on support chat logs ([repo](https://github.com/s-rostovskyi/lab-gdpr-compliance)). So we audited **different scenarios**.
> - **Part 1 is a real review:** I reviewed the partner's published memo, acting as their client.
> - **Part 2 is simulated:** the partner hasn't reviewed my memo yet. An AI assistant played my client (Lagerkraft's managing director) and raised the challenges my memo invites. The partner's real review is still pending.
> - **Part 3** compares the two audits. Different facts make it a test of *method*: did we reason about lawful basis and DPIA need the same way?

## Part 1 - My review of the partner's memo (NordDesk, LLM fine-tuning)

| Criterion | Score 1-3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Go with conditions for a restricted pilot", and the bulk upload is explicitly stopped. A CTO knows what they can and can't do on Monday. |
| Lawful basis selection is justified | **3** | Honest `TBD - legal review` for training, with a full three-step LIA showing *why* it doesn't pass yet. Correctly rejects "the corporate customer's contract covers its employees' chats". |
| Top actions are specific and sequenced | **2** | Well gated by owner (legal → procurement → privacy/engineering → CTO sign-off). But each action bundles 5-7 tasks, there are no dates, and the reader has to dig for the first concrete step. |
| Residual risks are named honestly | **3** | Memorisation, the cost of retraining after an erasure request, and unverifiable foreign access. Doesn't pretend SCCs or filtering make them go away. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | The worksheet covers it well (minimal risk, communications confidentiality, cloud switching). The memo squeezes all three into one sentence and doesn't give the *result*, e.g. "the AI Act adds almost nothing here". |

**As the client (NordDesk CTO):** I accept the go-with-conditions call, and I agree we shouldn't upload the archive. **One concern:** you say necessity isn't demonstrated until we compare fine-tuning against a retrieval assistant, but you don't say what result would count as proof. Give engineering a pass/fail threshold (for example, "fine-tuning must beat retrieval by X on first-reply accuracy") so we know when the gate opens.

## Part 2 - Simulated client review of my memo (Lagerkraft, applicant ranking)

| Criterion | Score 1-3 | Simulated client comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Go with conditions" in the first line, with the reason in one sentence. |
| Lawful basis selection is justified | **3** | Explains why it's legitimate interests and not consent, and what makes it hold (the manual route). |
| Top actions are specific and sequenced | **3** | Each action is gated to a moment: before data flows, before the first vacancy, before launch. |
| Residual risks are named honestly | **3** | Rubber-stamping is uncomfortable to read, which is the point. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | The memo mentions neither the AI Act timeline nor the careers-portal cookies. Both are in the worksheet, but a five-minute reader won't find them. |

**Simulated client response:** *"I'll accept the recommendation, but I'm challenging action 2. If recruiters have to open every qualified candidate's full CV, we lose the time saving that's the reason we bought the tool."*

**My answer:** The legal requirement is that a human meaningfully considers each qualified candidate, not that they read every CV in full. Under the controlled version, recruiters see a **one-screen summary card** (parsed fields + the tool's reasons) for every candidate in the qualified bands, and open the full CV only for those they shortlist or skip against the rank. That keeps most of the time saving and still means no qualified candidate is excluded without a human seeing them. **Outcome:** the client accepts. The memo now says "summary card" rather than "application".

**On the law-stacking score:** I accept it, but I'm keeping the memo as it is, because it's at 394 words and the AI Act points belong to the AI Act approval pack the client already has. The worksheet Section C covers both.

## Part 3 - Debrief: where the two audits agree and diverge

### Agreement

| Topic | Both audits concluded |
|---|---|
| **Lawful basis for the AI purpose** | Legitimate interests (6(1)(f)) with a written three-step LIA, **not consent** (power imbalance: employees in NordDesk's case, job seekers in mine) and **not contract** (strict necessity test). |
| **DPIA** | Required before processing starts. Both screened all nine EDPB criteria instead of assuming "AI = DPIA", and both pointed to the German authority's mandatory list ⚖️. |
| **Vendor reuse** | The DPA must **ban the vendor from training on client data**, otherwise the vendor becomes a controller and erasure becomes impossible. |
| **US transfer** | A **release gate**, not a box ticked by signing SCCs. Both prefer an EEA-only alternative where possible. |

### Divergence, and which reading is stronger

| Topic | Partner | Me | Stronger reading |
|---|---|---|---|
| **Firmness of the lawful basis** | `TBD - legal review` for training; LIA currently fails | Conditional *pass* for ranking | **Both are right for their facts, and the reason is purpose limitation.** NordDesk reuses old chats for a *new* purpose (Art 6(4) compatibility problem). Lagerkraft's applicants sent their CV *to be evaluated*, so ranking is the original purpose. Lesson: the same AI technique (an LLM) can be easy or hard to justify depending on whether the data was collected for it. |
| **Art 22** | Doesn't apply (drafts are approved by agents, no decisions about people) | Probably applies unless review is real (*SCHUFA*) | **Both right.** The difference is the output: a draft reply vs a rank that gates a job. |
| **DPF as a transfer route** | Refuses to assume DPF; plans on SCCs + TIA | DPF if certified, else SCCs | **Partner's is stronger as a method.** "If certified" is a fact to check, not an assumption. I've tightened mine to "only if the provider is on the active DPF list *and* its certification covers HR data". |
| **Response deadline** | One month | (Lab text says "30 days") | **Partner is right.** Art 12(3) says one month, extendable by two. I use "one month" in the worksheet and the stretch checklist. |
| **"Vulnerable data subjects" criterion** | Applies to support *agents* (employees) | Applies to *applicants* | **Both valid** under the EDPB guidelines (power imbalance). I'd add the partner's angle to mine: my **recruiters** are also data subjects (override logs), which I'd underplayed. That's now in P5 and the DPIA table (criterion 3). |

### What changed after the review

1. **Memo action 2:** "open every application" → "open the **summary card** of every candidate who meets the minimum requirements". Same legal effect, much lower cost for recruiters.
2. **Transfers:** DPF wording tightened (active list + HR-data scope), following the partner's stricter method.
3. **Deadlines:** "one month", not "30 days", wherever it appears.
4. **Recruiters as data subjects:** made explicit (P5 basis, works-council co-determination, DPIA criterion 3).

**Main takeaway:** on two quite different AI scenarios we picked the same lawful basis and the same DPIA answer, with opposite levels of confidence. What decided it wasn't the technology. It was **purpose limitation**: whether the data was collected for the thing the AI does.
