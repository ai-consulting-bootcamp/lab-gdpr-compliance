# Mini Data Protection by Design Checklist

**Highest-risk activity:** uploading and analysing internal documents that may contain employee, volunteer, donor, or beneficiary personal data.

| Control | Status | Assessment and required evidence |
| --- | --- | --- |
| Data minimisation | **Fail** | The proposed upload can contain unrestricted free text. Introduce field allowlists, approved document types, client-side redaction, sensitive-data detection, and a block on unnecessary Article 9 content. |
| Purpose binding | **Unknown** | Contracts and technical controls must restrict use to the named organisational diagnostic and prohibit model training, unrelated analytics, and decisions about individuals. Verify vendor settings and instructions. |
| Access controls | **Unknown** | The MVP requires human review but production RBAC is not evidenced. Define client uploader, assigned consultant, security administrator, and support roles; log and review access. |
| Retention enforcement | **Fail** | The source project identifies retention and run-ID deletion as production gaps. Implement automated deletion for uploads, extracted text, prompts, outputs, n8n executions, caches, and backups, with confirmation. |
| Subject-rights workflow | **Fail** | No demonstrated workflow connects a person to all source and derived records. Add per-run data lineage, identity verification, controller routing, search, correction, export, objection, and erasure actions. |
| Incident response | **Unknown** | Document detection, containment, processor-to-controller notice, risk assessment, evidence preservation, and support for the controller's 72-hour supervisory-authority deadline. Test the process before launch. |

## Release gate

The production pilot does not pass privacy by design until every **Fail** is remediated and every **Unknown** has documented evidence, an owner, and approval in the DPIA.
