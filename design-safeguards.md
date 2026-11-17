# Design safeguards — vacancy ranking

## DPIA outline

| Section | What Northline should document |
| --- | --- |
| Description of processing | ATS intake, feature extraction, vendor scoring, full-queue review, rights and deletion. Record volumes, access jurisdictions, recipients, and who makes decisions. Ask the DPO, if designated, for advice and seek applicant or representative views where appropriate. |
| Necessity and proportionality | Compare structured manual review and simpler rules. Justify each feature, every retention window, the need for the score and the manual route. Document the legal basis and show how applicants receive and exercise their rights. |
| Risks | Under-ranked applicants overlooked before closure, misread credentials, protected proxies, rank anchoring and unapproved support access. Assess likelihood and severity for applicants and record who owns each risk. |
| Measures and decision | Check complete queue coverage, test rights and deletions, block third-country production access, test role access, sample reasons and track omissions. Record residual risk, consult under Art. 36 if required and reassess after material changes. |

## Proposed DPA clause

**Purpose and support boundary.** RankWorks shall use vacancy inputs, scores, explanations and logs solely to perform Northline's documented recruiting instructions. It shall not use them for product training or benchmarking, and shall prevent direct or indirect production access by non-EEA entities, including support affiliates, unless Northline has first authorized the identified entity and access path in writing and the appropriate Chapter V requirements are satisfied. RankWorks will provide access and deletion evidence on request.

**Why it matters.** A regional hosting promise does not prevent support staff from seeing candidate data in logs. This clause applies the restriction to diagnostic data and gives Northline evidence to verify it.

## UK variation

**Go with conditions, including a separate UK assessment before accepting UK applications.** Keep genuine human review even though the Data (Use and Access) Act 2025 widened when significant solely automated decisions are allowed for ordinary personal data under UK GDPR. If that fallback is considered, check Arts. 22A–22D, including restrictions on special-category data and safeguards for notice, representations, human intervention and contesting decisions. Assess territorial scope, UK recruitment law and any UK export mechanism separately. UK applicants do not displace EU GDPR for processing in the context of Northline's German establishment.

[ICO commencement statement](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa) · [ICO summary of the UK changes](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/data-protection/)

## Privacy by design checklist

Status refers to the original proposal, not the unverified recommended design.

| Control | Status | Acceptance check |
| --- | --- | --- |
| Data minimisation | Fail | Replace free-text ranking input with allowlisted vacancy features and reject unexpected fields. |
| Purpose binding | Unknown | Verify no training reuse or cross-vacancy pools in contracts, tenant settings and logs. |
| Access controls | Fail | Block the assumed US affiliate access and verify least privilege for recruiters and support. |
| Retention enforcement | Unknown | Demonstrate deletion of vendor caches and controlled backup expiry or isolation. |
| Subject rights workflow | Unknown | Test an access, correction and erasure request across the ATS and ranker within one month, subject to lawful exceptions. |
| Incident response | Unknown | Test prompt processor escalation and supervisory notification within 72 hours of awareness where required under Art. 33. |
