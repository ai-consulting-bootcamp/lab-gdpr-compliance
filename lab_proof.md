# Lab proof · Same product, privacy lens (GDPR audit of Case B)

**Start here.** A mini GDPR audit of the contact-centre "wellbeing assistant" (Case B from Friedrich's client briefs), carried forward from the EU AI Act lab (Option A).

## Result in one line

**Stop as proposed. Go with conditions on a redesign.** Agent stress inference from voice and webcam has no valid lawful basis: it is health data with no Art. 9 condition, and consent is invalid in employment. It is also prohibited under AI Act Art. 5(1)(f). A text-only, team-level workload tool is lawful with a DPIA, a works agreement and a fixed contract chain.

## The run: input → evidence → output

**Input.** Friedrich's Case B brief (600-agent outsourcer; voice-tone and webcam stress detection; per-agent dashboard feeding shifts and coaching; customer mood scoring), plus my EU AI Act classification of the same case from the previous lab. Gaps in the brief (geography, vendor, volumes) are filled with assumptions that are labelled and shared with Friedrich.

**Evidence produced** (in [`GDPR_Audit_Pack_Nicolo_Marseu.md`](GDPR_Audit_Pack_Nicolo_Marseu.md)):

| Check | Finding |
|---|---|
| Art. 9 special-category data | Yes: agent stress scores are health data; insurance call content may hold health data |
| Lawful basis, P1–P2 (agent monitoring, shift use) | None valid. Consent fails in employment; legitimate interests fails balancing; no Art. 9(2)(b) law |
| Lawful basis, P3 (customer mood) | TBD – legal review; likely fails. End-client is the controller |
| Lawful basis, P4–P6 (redesign) | Legitimate interests + works agreement (Art. 88); consent for anonymous survey; §201 StGB recording point TBD |
| Art. 22 | Effectively yes as proposed (shift decisions; *SCHUFA* reasoning); not engaged in redesign |
| DPIA | Required: at least 8 of 9 EDPB criteria |
| Transfers | US vendor: DPF if certified, SCCs as fallback (DPF appeal pending at CJEU); redesign defaults to EU hosting |
| Law stacking | AI Act ban overrides any GDPR basis; Art. 50(3) for callers; ePrivacy only via call confidentiality; Data Act N/A |

**Final output.** Client recommendation memo (about 390 words), in Part 2 of the audit pack and as a stand-alone swap copy: [`case_b_client_recommendation_memo_for_swap.md`](case_b_client_recommendation_memo_for_swap.md).

## One failure / limitation I hit

**The brief doesn't state the facts GDPR depends on most.** It gives no country, vendor location, end-client sectors or call volumes. I assumed Germany, a US vendor and telecom/insurance end-clients. These assumptions drive several findings: German-specific points (BetrVG works council, §26 BDSG after CJEU C-34/21, §201 StGB for call recording), the transfer analysis and the health-data risk in insurance calls. If Friedrich's fact pattern differs, those rows change. The legal points marked TBD are unverified and need counsel.

## Peer swap (Phase 4)

Friedrich, acting as the client, **accepted my recommendation as written**: no finding challenged, no redesign requested. See [`phase4_peer_review_and_swap.md`](phase4_peer_review_and_swap.md).
