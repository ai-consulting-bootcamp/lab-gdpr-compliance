# GDPR Audit Pack - Adam Valois

## Part 1 --- Audit Worksheet

### Fact Pattern

The client is a private mortgage handling firm with 50 employees in
Germany.\
The firm's clients are German residents and provide personal data
including credit history, income, background information, and limited
personally identifiable information.\
The proposed AI system automatically assesses clients' creditworthiness
using an algorithmic score based on their risk profile.\
The technology stack includes an OpenAI model used to assess
creditworthiness.\
All models and storage are intended to operate locally at the mortgage
handling firm in a ring-fenced environment.\
Once a decision is made, the client's data will be removed from the
system other than their credit score and name.\
The proposed system would automatically decide whether to approve or
deny a mortgage application.

## Section A --- Data Map

  -----------------------------------------------------------------------
  Field                               Your answer
  ----------------------------------- -----------------------------------
  **Categories of personal data**     **Identification Data:** Name,
                                      address, date of birth, customer
                                      ID. **Financial Data:** Salary,
                                      assets, liabilities, debts.
                                      **Credit History:** Credit score,
                                      defaults, repayment history.
                                      **Employment Data:** Employer,
                                      employment status, length of
                                      employment. **Profiling Data:**
                                      Risk score. **Decision Data:**
                                      Approve/deny and reason for
                                      decision. **Article 9 special
                                      category (should not use):**
                                      Race/ethnicity, health, religion,
                                      political opinions, etc.

  **Sources (where data comes from)** **Customer application:** Name/ID,
                                      salary, employment,
                                      assets/liabilities. **Credit
                                      reference agency:** Credit
                                      history/score. **Derived by
                                      system:** Risk profile/AI model.
                                      **Mortgage firm employee:** Final
                                      decision.

  **Purpose(s), lawful basis, and     **Name / ID:** To process and
  retention period**                  administer mortgage application ---
                                      **Art. 6(1)(b)** --- duration of
                                      application. **Salary:** Evidence
                                      supporting credit assessment ---
                                      **Art. 6(1)(b)** --- duration of
                                      application. **Employment
                                      information:** Assess stability ---
                                      **Art. 6(1)(b)** --- duration of
                                      application. **Assets /
                                      liabilities:** Assess affordability
                                      and risk --- **Art. 6(1)(b)** ---
                                      duration of application. **Credit
                                      history / score:** Assess
                                      creditworthiness --- **Art.
                                      6(1)(b)** --- duration of
                                      application. **Risk profile / AI
                                      assessment:** Generate credit
                                      assessment --- **Art. 6(1)(b)** ---
                                      applicable regulatory retention
                                      period. **Final mortgage
                                      decision:** Documented outcome ---
                                      **Art. 6(1)(b)** --- applicable
                                      regulatory retention period.

  **Recipients and sub-processors**   **Mortgage firm's authorized loan
                                      officer:** Receives application;
                                      human review/decision. **Mortgage
                                      firm's credit risk team:** Receives
                                      credit and risk information; credit
                                      assessment. **Mortgage firm's
                                      IT/security team:** Receives
                                      technical information; system
                                      administration. **Credit reference
                                      agency:** Receives relevant
                                      application information; provides
                                      credit score. **AI model:**
                                      Receives required application data;
                                      automated analysis. **Local
                                      database:** Stores applicant data
                                      during processing.

  **International transfers and       No international transfer is
  transfer mechanism**                intended as all work will be done
                                      on premise in a ring-fenced
                                      environment.
  -----------------------------------------------------------------------

## Section B --- Risks and Rights

### 1. Are any special-category data present or inferable from the outputs (Article 9)?

Potentially, but not necessarily. The stated inputs---credit history,
income, background and limited identification data---are not themselves
Article 9 special-category data, but "background" must be tightly
defined because it could inadvertently include or allow inference of
health, ethnicity, religion, political opinions, etc.; these should be
explicitly excluded from the model. Article 9 data should not be used
for creditworthiness assessment without a specific Article 9(2)
condition.

### 2. Is there automated decision-making with legal or similarly significant effects (Article 22)? If yes, what safeguard applies?

Yes. The proposed automatic mortgage approval/denial is a significant
decision and the European Commission specifically identifies automatic
refusal of a credit application as an example of significant automated
decision-making. The safest proposed safeguard is meaningful human
intervention before the final decision, with the applicant able to
obtain human intervention, express their viewpoint and contest the
decision.

### 3. Is a DPIA required? Use the EDPB's nine criteria: explain which apply and why.

Yes, a DPIA is clearly required. The applicable criteria are (1)
evaluation/scoring through credit-risk profiling, (2) automated
decision-making with significant effects, (4) sensitive/highly personal
data because financial/credit information is highly personal, (6)
matching/combining datasets if credit, income and background sources are
combined, and (8) innovative technology through AI; the other
criteria---systematic monitoring, large-scale processing, vulnerable
subjects, and preventing exercise of rights/service---are not
established by the facts. The EDPB's nine criteria are specifically
intended to identify processing likely to create high risk, and this
system clearly meets multiple criteria.

### 4. What data subject friction points are most likely?

The main friction points are access, erasure, and objection/restriction
relating to profiling and automated decision-making. Applicants may also
challenge the accuracy of their credit information or seek an
explanation/review of an adverse automated assessment, making
transparency and meaningful human review particularly important.

### 5. What is the controller / processor split? Name each entity and its role.

The private mortgage handling firm is the controller, because it
determines the purposes and means of processing applicants' personal
data and makes/arranges the mortgage decision. The OpenAI/model vendor
would be a processor only if it processes applicant data on the firm's
behalf; under the stated architecture where the model and storage are
genuinely operated locally by the firm, the external model vendor may
not process the personal data at all and therefore may not be a GDPR
processor for this processing.

### 6. Is a DPA (Data Processing Agreement) needed with any vendor? Which ones?

Yes, if any vendor processes applicants' personal data on behalf of the
mortgage firm. Under the stated local architecture, no DPA would be
required with the OpenAI/model provider if applicant data never leaves
the firm's environment and the vendor has no access to it; however, any
external provider handling the data---for example cloud hosting,
credit-data services, external support or analytics---would need to be
assessed and, where it acts as a processor, covered by an Article
28-compliant DPA.

## Section C --- Law Stacking

### 1. AI Act cross-check

**High-risk (Annex III, 5(b))** because the system evaluates the
creditworthiness/credit score of natural persons for mortgage decisions.
The AI Act adds obligations beyond GDPR, including requirements around
risk management, data governance, technical documentation, logging,
transparency, human oversight, accuracy and robustness for high-risk
systems.

### 2. ePrivacy check

**N/A** --- the scenario does not involve cookies, tracking pixels,
electronic communications metadata, or device-level tracking, so there
is no additional ePrivacy consent requirement to assess.

### 3. Data Act check

**N/A** --- the scenario does not involve connected products/IoT data or
switching between cloud/data-processing services; it is primarily a
financial decision-making and personal-data processing use case.

------------------------------------------------------------------------

## Part 2 --- Client Recommendation Memo

**To:** Client Legal and Technology Teams\
**Subject:** GDPR and AI Act assessment of proposed mortgage
creditworthiness system

### Bottom line

**Go with conditions.** The proposed system can potentially be
implemented, but it should not automatically approve or deny mortgage
applications until the Article 22 GDPR requirements, DPIA, and AI Act
high-risk requirements have been addressed.

### Top three actions

**1. Redesign the decision workflow to include meaningful human
review.**\
The AI should produce a creditworthiness/risk assessment for review by
an authorized credit officer rather than making the final mortgage
decision autonomously. The process should allow the applicant to obtain
human intervention, provide their viewpoint, and challenge an adverse
decision where required by GDPR Article 22.

**2. Complete a DPIA and high-risk AI Act assessment before processing
customer data.**\
The system involves profiling and evaluation of individuals using
financial and credit information to support a significant decision,
creating a high-risk processing profile under GDPR. The DPIA should
document the purposes and lawful bases, data minimization, retention
periods, security controls, human oversight, applicant rights, and
measures preventing the use or inference of special-category data. The
AI Act assessment should also address the requirements applicable to
high-risk creditworthiness systems, including risk management, data
governance, logging, transparency, human oversight, accuracy and
robustness.

**3. Confirm the vendor and data-flow arrangements before production
use.**\
Because the proposed architecture keeps the model and storage locally at
the mortgage firm, applicant data should not be sent to OpenAI or
another external provider unless this is explicitly approved. Confirm
technically and contractually that no personal data leaves the firm's
environment; if a vendor processes applicant data on the firm's behalf,
put an Article 28-compliant DPA in place before that processing begins.
The privacy notice should also explain the creditworthiness assessment,
profiling, automated processing, retention, and applicants' relevant
rights.

### Residual risks

Even after these controls are implemented, **model bias and inaccurate
credit assessments cannot be completely eliminated**. The firm will need
ongoing monitoring to identify discriminatory outcomes, data-quality
problems, and changes in model performance.

There is also a residual **explainability and challenge risk**:
applicants may dispute the assessment or struggle to understand why
their application received a particular risk score, particularly where
the underlying model is complex.

Finally, **data-security and misuse risks remain** because the system
processes highly consequential financial information. Local deployment
reduces external-transfer risk but does not eliminate risks from
unauthorized internal access, compromised infrastructure, excessive
retention, or inappropriate use of the model.

------------------------------------------------------------------------

## Part 3 --- Partner Review

  ------------------------------------------------------------------------
  Criterion                             Score (1--3) Comment
  --------------------- ---------------------------- ---------------------
  **Clear bottom-line                              2 Bottom line has a
  recommendation**                                   clear recommendation
                                                     however there isn't
                                                     the

  **Lawful basis                                   3 There is reference to
  selection justified**                              relevant laws that
                                                     fit feasibility.

  **Top actions are                                3 Actions fit scenario
  specific and                                       and legal
  sequenced**                                        requirements
                                                     perfectly.

  **Law stacking is                                3 Law stacking is
  addressed**                                        addressed.
  ------------------------------------------------------------------------

### Further Recommendations

Should include a statement about removing automation from mortgage
application in the bottom line statement more explicitly. Top 3 actions
though are well in line with requirements and should enable the success
of the project.
