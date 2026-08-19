# Data protection by design checklist

**Activity assessed:** logging of free-text chat turns and their transit to non-EU model vendors, the highest-risk processing in the scenario.
**Basis for each verdict:** what the public repo shows. Where the repo is silent, the verdict is Unknown rather than Fail. That distinction matters: Unknown is a question for the client, Fail is a finding.

| # | Control | Verdict | Evidence and what to do |
|---|---|---|---|
| 1 | **Data minimisation** | Fail | `chat_log` stores the full question and answer per turn. The stated purpose is quality and feedback, which truncated turns or feedback counts would largely serve. Reduce what is stored, or justify the full transcript in the LIA. |
| 2 | **Purpose binding** | Fail | Nothing technically prevents the transcript store being reused later as tuning data. That would be a new purpose failing the Article 6(4) compatibility test. Add an explicit written no-reuse rule now, while the store is small. |
| 3 | **Access controls** | Unknown | Basic Auth protects the widget and credentials sit in n8n's own store, which is correct as far as it goes. Who can read the Data Tables, whether the n8n instance is exposed beyond the tunnel, and whether Basic Auth credentials are shared or rotated are all unanswered. Single-operator setups usually pass this in practice and fail it on paper. |
| 4 | **Retention enforcement** | Fail | No automated deletion or anonymisation on `chat_log` or `error_log` appears anywhere in the repo. This is the cheapest fix in the list and the one that most improves the risk picture. |
| 5 | **Subject rights workflow** | Fail | No documented path for access or erasure, and a structural obstacle underneath it: sessions are anonymous, so matching a requester to their turns may be impossible without collecting more identity data than the service needs. Write the procedure including the honest answer that unidentifiable sessions fall under Article 11. |
| 6 | **Incident response** | Fail | The error-alert workflow detects crashes and verbalised tool failures, which is a reliability control, not a breach-detection control. Nothing detects unauthorised access, an exposed Data Table, or a leaked credential, and there is no written 72-hour notification path. The repo's own known-limitations section already concedes the silent-failure gap. |
| 7 | **Transparency at the point of collection** *(added)* | Fail | No privacy notice at the chat entry point and no AI disclosure. The second is separately mandatory under Article 50 of the AI Act, applicable since 2 August 2026. |

**Summary:** six fails, one unknown, zero passes. That reads harsh for a well-built student project, and the reason is worth stating plainly to the client: every fail here is an absence of a document or a configuration rule, not a defect in the system. The engineering is sound. The governance layer was never built, which is the normal outcome when a working prototype meets real users faster than anyone planned.

**Sequence if the client can only do three:** retention rules (4), entry-point notice with AI disclosure (7), subject-rights procedure (5). Those three convert the highest-severity risks into managed ones and cost roughly a day.
