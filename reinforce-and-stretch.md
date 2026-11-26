# Reinforce and stretch - Applicant ranking (Lagerkraft / RankFlow)

Scenario facts: see [`gdpr-audit-pack-ben-mayer.md`](./gdpr-audit-pack-ben-mayer.md). Not legal advice; ⚖️ = confirm with counsel.

## Reinforce 1 - DPIA outline (P2: AI scoring and ranking)

| DPIA section (Art 35(7)) | Content |
|---|---|
| **Description of processing** | ~60,000 applicants/year. Flow: careers portal/job boards → RankFlow (NL) → LLM parsing (US, or EU endpoint) → field stripping → scoring model → banded ranking with reasons → recruiter. Data categories, recipients and retention as in Section A. |
| **Necessity and proportionality** | Lawful basis 6(1)(f) + LIA. Minimisation: photo, DOB, nationality, full address and health certificates stripped before scoring. Retention 6 months. Transparency: notice + AI Act Art 26(11) notice. Rights: manual route for objections, a correction screen for parsed fields. |
| **Risk identification** | (1) Ranking works as a de facto automated rejection (Art 22). (2) Indirect discrimination via proxies (AGG). (3) Parsing errors that lower a rank. (4) US government access to CVs via the LLM transfer. (5) Vendor reuse of data for its own models. (6) Over-monitoring of recruiters through override logs. |
| **Mitigation** | (1) Summary card for every qualified candidate + override reasons + monthly override-rate metric. (2) Vendor Art 10 bias tests + agency outcome monitoring by group (P6). (3) Applicant can view and correct parsed fields. (4) EU parsing endpoint, or DPF/SCCs + TIA. (5) DPA ban on training + audit right. (6) Works-council agreement limiting the use of logs to system oversight, not recruiter performance reviews. |
| **Residual risk and sign-off** | Medium after mitigation (rubber-stamping and proxies can't be fully removed). DPO opinion recorded. Prior consultation with the authority (Art 36) only if residual risk stays high. Review annually or when the model changes. |

## Reinforce 2 - One DPA clause I'd insist on

> **No own-purpose processing.** *The Processor shall not use Customer Personal Data, or any data derived from it (including parsed fields, embeddings, scores and feedback signals such as recruiter overrides), to train, fine-tune, evaluate or otherwise improve any model or service other than the instance provided to the Customer. The Processor shall impose the same restriction, including zero data retention settings, on every sub-processor, and shall certify compliance annually and on request.*

**Why this one:** it's the clause that keeps RankFlow a processor. Without it, recruiter overrides are a very valuable training signal for the vendor, and using them makes RankFlow a **controller** with no lawful basis, puts Lagerkraft's applicants into other agencies' rankings, and makes an erasure request practically impossible to honour. It also covers *derived* data, which a generic "no reuse of personal data" clause often misses.

## Reinforce 3 - Bottom line if the client also serves UK applicants

**Still go with conditions**, plus three changes:

1. **ADM rules differ.** UK GDPR Art 22A-22D (inserted by the Data (Use and Access) Act 2025 ⚖️ commencement) allows significant automated decisions on more lawful bases, *provided* safeguards are in place: tell the person, let them make representations, offer human intervention and let them contest. That makes the UK more permissive than the EU, but the rules stay strict where special-category data is involved, and here it is (health certificates). In practice: keep the EU design, which already meets the UK safeguards.
2. **Transfers.** EU → UK is covered by the EU's UK adequacy decision (renewed in 2025 ⚖️). UK → US needs the **UK Extension to the DPF** ("data bridge") or the IDTA / UK Addendum to the SCCs.
3. **Admin.** If the agency has no UK establishment but targets UK applicants, it needs a **UK representative** (UK GDPR Art 27). The regulator is the ICO, and the anti-discrimination law is the Equality Act 2010 instead of the AGG. The EU AI Act doesn't apply to UK-only placements.

## Stretch - Data protection by design checklist (P2: AI ranking)

| Item | Status | Note |
|---|---|---|
| **Data minimisation** | ❌ Fail | Today the full CV, including photo, DOB and health certificates, goes to the parser and the model. Needs field stripping before scoring. |
| **Purpose binding** | ❓ Unknown | No technical barrier stops RankFlow from reusing data. Needs a DPA clause (above) + evidence that its training pipelines are tenant-isolated. |
| **Access controls** | ❓ Unknown | Are all 40 recruiters able to see all 14 branches' applicants? Should be limited to own branch and vacancy. |
| **Retention enforcement** | ❌ Fail | No automated deletion configured. The 6-month rule must be a scheduled job in RankFlow *and* the portal, with deletion logs. |
| **Subject rights workflow** | ❌ Fail | No way yet to export the reasons for a score or correct parsed fields. Can't meet the **one-month** deadline for an Art 15(1)(h) explanation request at scale. |
| **Incident response (72 h)** | ❓ Unknown | The DPA needs RankFlow to notify the agency of breaches *without undue delay* (aim for 24 h) so the agency can make its 72-hour report to the authority (Art 33). Not yet in the draft contract. |

**Reading:** 3 fails, 3 unknowns, 0 passes. The tool can't go live on its current setup. All six are fixable before launch. Most need contract terms or configuration (DPA clauses, access roles, deletion jobs) rather than new engineering. The exception is the rights workflow, which RankFlow has to build.
