# Stretch — Data protection by design checklist

**Highest-risk activity:** AI scoring and automatic rejection of applicants (P2/P3).
**Status key:** ✅ Pass · ❌ Fail · ❓ Unknown, based on the client's *current* plan as described in the fact pattern.

| Item | Status | Note |
|---|---|---|
| **Data minimisation** | ❌ | Full CVs with photos, date of birth and nationality go to the vendor, plus 5 years of named employee performance data. Fix: redact before sending; aggregate the top-performer features. |
| **Purpose binding** | ❓ | Unknown whether the vendor's terms allow it to reuse data to improve its product, or whether scores could be reused internally (e.g. in later promotion decisions). Fix: DPA clause + internal rule that scores are used for this vacancy only. |
| **Access controls** | ❓ | Who can see scores of rejected applicants: hiring managers, both countries' teams, vendor support staff? Not defined. Fix: role-based access per country and vacancy; logged vendor support access. |
| **Retention enforcement** | ❌ | No deletion rule set. Rejected applications and scores would stay in the portal and at the vendor indefinitely. Fix: automatic deletion 6 months after rejection, at both the portal and the vendor (deletion confirmation in the DPA). |
| **Subject rights workflow** | ❌ | No process to explain a score, give human review or export an applicant's score within 30 days. The rejection email doesn't mention any rights. Fix: rights section in the email + a recruiter queue for review requests. |
| **Incident response** | ❓ | Group breach procedure presumably exists. Unknown whether the US vendor must notify within e.g. 24h so the client can meet the 72-hour deadline, and whether DE and PL authorities would both need notifying. Fix: DPA notification clause + lead-authority check. |

**Overall:** 3 fails, 3 unknowns. Minimisation, retention and the rights workflow have to be fixed before launch. Resolve the unknowns in the DPIA and the vendor negotiation.
