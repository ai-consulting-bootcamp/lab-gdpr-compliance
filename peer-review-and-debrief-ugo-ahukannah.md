# Peer review and debrief — Ugo Ahukannah

Internal working document for the lab exchange with Vittal Navale — deliberately kept out of
[`gdpr-audit-pack-ugo-ahukannah.md`](./gdpr-audit-pack-ugo-ahukannah.md), which is the client-facing
audit and memo.

# Phase 4 — Partner swap and peer review

_CFU 4 Verify._

**My review of Vittal's memo** (his pack: [`from_vittal/GDPR-Audit-Pack-VittalNavale.md`](./from_vittal/GDPR-Audit-Pack-VittalNavale.md)):

| Criterion | Score 1–3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | **3** | "Go, with conditions" stated up front, restated at the close, and the reason given in one sentence. No hedging, and a reader with five minutes gets the answer immediately. |
| Lawful basis selection is justified | **3** | Four purposes, each with a basis and a reason. Correctly splits Art 6(1)(b) for handling the application from Art 6(1)(f) for the ranking, and — the part most people get wrong — marks the automated rejection and the model-training purposes as **TBD — legal review** rather than inventing a basis. The Art 6(4) compatibility point on repurposing employee retention records is exactly right. |
| Top actions are specific and sequenced | **3** | Named, ordered, and each tied to the exposure it closes. Action 3 goes further than mine by making the processor-vs-controller question a contractual deliverable rather than an observation. |
| Residual risks are named honestly | **3** | Three real ones, and he resists the temptation to imply they are solvable. The explainability risk — "no clear answer beyond 'the model said so'" — is the sharpest line in either memo, and it is a risk I under-weighted in mine. |
| Law stacking is addressed (AI Act / ePrivacy) | **2** | AI Act tier correct and the obligations list is sound, and the observation that the undecided human-review question is an AI Act gap *as well as* a GDPR one is a good one. Two gaps: no **timing** — the memo implies AI Act conformity work is due before launch, when Annex III obligations apply from **2 December 2027**; and the conformity assessment is described without noting it is **internal control under Annex VI**, so a client could infer a notified body is needed. ePrivacy is flagged but waved off as secondary; consent under Art 5(3) is not optional where non-essential cookies are set. |

**As the client, in three sentences:** Accepted, with one challenge. Action 1 is right and we will
mandate recruiter review of every "not a fit" before launch — but your memo reads as though the AI
Act conformity work must also land inside the six weeks, and if that is wrong it changes what we
can realistically commit to, so tell us plainly which obligations bite now and which bite in
December 2027. Second, your retention recommendation of 6–12 months is asserted rather than
justified: we hire across the EEA, expectations differ sharply by country, and we need the
reasoning per jurisdiction before we can adopt a single figure.

**Vittal's review of my memo** ([`from_vittal/peer-review-of-ugo-memo-vittal-navale.md`](./from_vittal/peer-review-of-ugo-memo-vittal-navale.md)): **15 / 15** — 3 on all five criteria.

He confirms the split worked: *"I only received the cleanly split files … no earlier mixed version
reached me, so nothing anchored this read."* He credited three things specifically: the five-purpose
lawful-basis breakdown with the LIA written out and honestly concluding the balancing test currently
fails; the DPF-certification-**scope** check in Action 3 (covers HR data, not certification
generally); and the erasure residual risk, which he had as a Section B friction point but did not
carry into his own memo.

**His one concern, as the client, and how it resolves.** He challenged the Section C reliance on
**Article 4a**, believing the Digital Omnibus to be "a Commission proposal, not yet adopted or in
force", and asked that the bias-testing mitigation rest on a current Art 9(2) gateway instead.

Checked independently, and the challenge does not hold: **Regulation (EU) 2026/1744 was published in
the Official Journal on 24 July 2026 and entered into force on 27 July 2026** — it is amending law,
not a proposal. The likely source of the error is the **7 May 2026 provisional agreement**, which is
precisely why the position should always be cited to the instrument rather than asserted. Article 4a
itself is real and does what the pack relies on: it permits the exceptional processing of special
categories of personal data where necessary for bias detection and correction, extended beyond
high-risk systems to other AI systems and models.

**Two things I am adopting from the challenge even though it was wrong on the facts.** First, every
Omnibus-dependent claim in the pack now carries its instrument and in-force date inline, so a
client's counsel can verify in one step rather than taking it on trust — the discipline his own
first pack demonstrated. Second, his instinct that a mitigation should not rest on shaky ground is
right in general, so the pack now records *why* the ground is firm here: Art 4a is an **exceptional**
basis subject to a necessity test, and this system reaches it by the **high-risk route** via Article
10(2)(f) and (g), rather than by the broader extension to non-high-risk systems that the EDPB and
EDPS asked to see circumscribed.

# CFU 5 — Debrief: agreement and divergence

Both audits were written independently against the same agreed fact pattern.

**Where we agreed** — and the agreement is substantive, not superficial:

- **Bottom line.** Both landed on **go with conditions**, and both refused both alternatives: neither
  of us treated this as launchable as-is, and neither of us reached for "stop".
- **Article 22 is the crux, and the fix is procedural.** We independently concluded that the
  automated rejection is a solely automated decision, that consent and contract necessity are both
  unsound gateways in a recruitment power imbalance, and that the correct remedy is to make Article
  22 stop applying by requiring genuine human review — not to hunt for a better legal basis.
- **DPIA is mandatory**, and both of us made it action 2, before first processing.
- **Article 9 by inference, not collection.** Same conclusion, same reasoning: proxies in free-text
  CVs and a model trained on historical outcomes, and both of us rejected the "we don't collect that
  field" defence explicitly.
- **Controller/processor split**, including the same warning that the vendor becomes a controller in
  its own right if it reuses client data to improve its product.
- **Transfers** need SCCs plus a transfer impact assessment, or verified DPF certification.

**Where we diverged, and which reading is stronger:**

| Point | Vittal | Me | Stronger reading |
|---|---|---|---|
| **Retention for unsuccessful applicants** | 6–12 months, to preserve a discrimination-claims defence | Initially anchored to the Dutch 4-week norm, corrected to a per-jurisdiction matrix once the fact pattern went EEA-wide | **Neither as first written.** His figure is defensible but asserted without jurisdictional grounding; my original was precise but wrong for an EEA-wide employer — a national norm cannot govern a 15,000-employee chain hiring across member states. The stronger answer is his *purpose* (claims defence sets the floor) with my *structure* (a documented per-jurisdiction matrix, shortest defensible default). |
| **DPIA trigger** | At least four of the EDPB's nine criteria | Six or seven of nine, **plus Art 35(3)(a) making it mandatory outright** | **Mine**, narrowly — counting criteria is the softer argument, and citing Art 35(3)(a) directly means the DPIA obligation does not depend on how a supervisory authority scores the criteria. His conclusion is identical; the route is just less robust. |
| **AI Act timing** | Implies conformity work must precede launch | Annex III obligations apply from 2 Dec 2027; the GDPR fixes are what bind the six-week window | **Mine.** Conflating the two clocks would have the client spend six weeks on documentation that is not yet due while the Article 22 exposure is live now. |
| **Conformity assessment route** | "A conformity assessment before deployment" | Internal control under **Annex VI**; no notified body for Annex III(4) | **Mine** — the unqualified phrasing invites a client to procure a third-party assessment the Act does not require here. |
| **ePrivacy** | Flagged, but "not the primary exposure" | Consent under Art 5(3) overrides GDPR flexibility for non-essential cookies | **Mine on the law, his on the priority.** He is right that it is not where the risk sits; I am right that it is not discretionary. Both belong in the memo. |
| **Explainability as a residual risk** | Named as a standing operational and reputational problem | Treated mainly as an Art 15(1)(h) access-request duty | **His.** Framing it as "recruiters need enough visibility to give a real answer" is the more useful consulting output — mine described the legal duty without the operating consequence. Adopted. |
| **Digital Omnibus interactions** | Not raised | Art 4a as the basis for bias testing on special-category data; Art 12 logging vs storage limitation | **Mine**, but this is coverage rather than a disagreement — the Art 4a point removes the obstacle his own bias-testing recommendation would otherwise hit. |

**One process note for the debrief conversation.** Vittal's transition note records that the AI Act
lab repository "was empty at the time of this lab", so he could not carry a tier forward under
Option A and wrote a self-authored case instead. That is a consequence of our AI Act work not yet
being pushed, not of anything he did — and it is worth saying so on the record, since his pack
otherwise reads as though the prior lab produced nothing.
