# GDPR Audit Pack --- Louise Plessis

## Scenario: Regional Bank --- AI-Assisted Recruitment Screening

**Course:** AI Consulting Bootcamp\
**Lab:** Same product, privacy lens\
**Author:** Louise Plessis\
**Partner:** Mudit\
**Date:** 18 August 2026

> **Scope note:** This is a first-pass GDPR audit for the agreed
> scenario. Where the fact pattern does not specify a vendor, hosting
> region, retention period, or contractual arrangement, the assessment
> uses **TBD --- legal review** rather than inventing facts.

------------------------------------------------------------------------

# Audit worksheet

## Phase 1 --- Transition note and fact pattern

### Transition note

This audit carries forward the **regional bank recruitment case** from
the EU AI Act exercise. The system ranks incoming resumes and cover
letters for entry-level analyst roles and automatically rejects the
bottom 60% of applicants. It also uses application material and
video-based inputs to assess candidate suitability, including a "culture
fit" component.

Under the EU AI Act, the system was classified as **high-risk** because
it is used to evaluate and select candidates in recruitment. It is
particularly relevant for GDPR analysis because the system processes
extensive applicant personal data, creates inferred scores about
individuals, and uses those scores in a decision that can materially
affect access to employment.

### Fact pattern

The client is a **regional bank with increased hiring volume** that
wants to automate part of its recruitment process for entry-level
analyst roles. Applicants are assumed to include **EU/EEA-based
candidates**.

The system processes names and contact details, resumes, cover letters,
education and employment history, application answers, and candidate
video material. It also creates inferred information such as candidate
scores, rankings, and a "culture fit" assessment.

The bank uses these data to evaluate applications, rank candidates, and
automatically reject the bottom 60% before recruiters review the
remaining applications. The automatic rejection therefore occurs
**before meaningful human review of the rejected candidates**.

The scenario does not specify the AI vendor, model provider, hosting
location, or whether a non-EU processor is involved. These points are
therefore **TBD --- legal review**. Before deployment, the bank would
need to identify every vendor receiving applicant data, establish the
appropriate controller/processor relationship, and assess any
international transfer.

The system may encounter information from which sensitive
characteristics can be revealed or inferred, particularly through
free-text applications and video. However, the scenario does not
establish that the system intentionally processes biometric data for
unique identification or intentionally infers Article 9 characteristics.
This requires technical verification rather than assumption.

The most significant GDPR issue is the **automatic rejection of
applicants**. Rejection from a recruitment process can have a similarly
significant effect on an individual. If the bottom 60% are rejected
solely on the model's output, Article 22 requires specific analysis and
cannot be solved merely by having recruiters review the candidates who
remain.

------------------------------------------------------------------------

# Phase 2 --- Mini GDPR audit worksheet

## Section A --- Data map

  -----------------------------------------------------------------------
  Field                               Answer
  ----------------------------------- -----------------------------------
  **Categories of personal data**     Identity/contact data; CV and
                                      cover-letter content; education and
                                      employment history; skills and
                                      qualifications; application
                                      answers; video/audio content if
                                      submitted; inferred candidate
                                      scores, rankings and "culture fit"
                                      assessments; recruitment outcome.
                                      Special-category data may appear
                                      incidentally or potentially be
                                      inferred, but this is not
                                      established by the fact pattern.

  **Sources**                         Primarily applicants directly
                                      through the recruitment process.
                                      Potentially recruitment/HR systems
                                      already operated by the bank. No
                                      additional external datasets are
                                      assumed without confirmation.

  **Purpose 1**                       Receive and administer applications
                                      for analyst roles.

  **Lawful basis --- Purpose 1**      **TBD --- legal review.** Depending
                                      on Member State employment law and
                                      the exact recruitment process, the
                                      appropriate Article 6 basis may
                                      include steps taken at the
                                      applicant's request prior to
                                      entering a contract and/or another
                                      basis applicable to recruitment
                                      processing.

  **Purpose 2**                       Assess applicants' qualifications
                                      and suitability for the role.

  **Lawful basis --- Purpose 2**      **TBD --- legal review.** The bank
                                      must establish and document the
                                      appropriate Article 6 basis for
                                      algorithmic evaluation rather than
                                      assuming that the basis for
                                      receiving an application
                                      automatically covers every new form
                                      of profiling.

  **Purpose 3**                       Rank candidates to prioritise
                                      recruiter review.

  **Lawful basis --- Purpose 3**      **TBD --- legal review.** A
                                      separate necessity and
                                      proportionality assessment is
                                      required because ranking creates
                                      inferred data and affects how
                                      candidates progress through
                                      recruitment.

  **Purpose 4**                       Automatically reject the bottom 60%
                                      based on AI ranking.

  **Lawful basis --- Purpose 4**      **TBD --- legal review and Article
                                      22 assessment required.** A general
                                      Article 6 lawful basis is not
                                      enough to resolve the additional
                                      restriction on solely automated
                                      significant decisions.

  **Retention period per purpose**    **TBD --- legal review.** The bank
                                      should define separate retention
                                      periods for unsuccessful
                                      applications, successful-hire
                                      records, raw video, model-generated
                                      scores and audit/log data. Data
                                      should not be retained indefinitely
                                      "for future hiring" without a
                                      justified purpose and basis.

  **Recipients and subprocessors**    Bank HR/recruitment staff; relevant
                                      hiring managers where necessary; AI
                                      recruitment vendor/model provider
                                      and hosting/infrastructure
                                      providers if they receive applicant
                                      data. Exact vendor chain: **TBD**.

  **International transfers**         **TBD.** The scenario does not
                                      identify vendor or hosting
                                      geography. If applicant data leaves
                                      the EEA, the bank must identify and
                                      document an applicable Chapter V
                                      transfer mechanism such as an
                                      adequacy decision or SCCs, as
                                      appropriate.
  -----------------------------------------------------------------------

### Purpose limitation

The bank should distinguish **administration of an application** from
**algorithmic profiling, ranking, culture-fit inference, and automatic
rejection**. Data supplied to apply for a job should not automatically
be treated as available for every AI-derived evaluation simply because
the bank already possesses it.

### Legitimate interests note

If the bank proposes **legitimate interests** for any non-Article-22
processing, it should complete the three-part LIA:

1.  **Purpose:** Is improving recruitment efficiency a specific and
    legitimate interest?
2.  **Necessity:** Is the particular AI processing necessary, or could
    the objective be achieved through a less intrusive method?
3.  **Balancing:** Do the bank's interests outweigh the applicant's
    rights and reasonable expectations, considering the power imbalance
    and consequences of recruitment decisions?

Until that analysis is complete, the relevant basis remains **TBD ---
legal review**.

------------------------------------------------------------------------

## Section B --- Risk and rights

### 1. Special-category data --- Article 9

Special-category data are **not necessarily part of the intended
input**, but they could appear in cover letters, CVs, or video---for
example information revealing health, religion, ethnicity, political
views, trade-union membership, or sexual orientation.

Video footage itself is not automatically Article 9 biometric data. The
bank should test what the "culture fit" feature actually infers. If it
intentionally derives Article 9 characteristics, the bank would need
both an Article 6 lawful basis and an applicable Article 9 condition. If
no valid condition exists, that processing should not proceed.

### 2. Automated decision-making --- Article 22

**Article 22 is a major concern.** The bottom 60% of candidates are
automatically rejected based on the AI ranking, and rejection from a
recruitment process can significantly affect an applicant.

The fact that recruiters subsequently review the remaining 40% does
**not** provide human intervention for applicants who have already been
rejected.

Before deploying this design, the bank should either establish that the
automated decision falls within a valid Article 22 exception together
with the required safeguards, or redesign the process so that a person
conducts meaningful review **before** rejection. Human review must be
capable of changing the outcome rather than functioning as a rubber
stamp.

### 3. DPIA requirement

A **DPIA should be conducted before deployment**. Several EDPB screening
criteria are implicated:

-   **Evaluation or scoring:** yes --- candidates are scored and ranked.
-   **Automated decision-making with significant effect:** yes --- the
    bottom 60% are automatically rejected.
-   **Systematic monitoring:** not clearly established.
-   **Sensitive/highly personal data:** potentially, depending on
    application/video content and model inference.
-   **Large-scale processing:** **TBD** --- hiring volume is described
    as high, but scale is not quantified.
-   **Matching/combining datasets:** potentially, if CV, cover-letter,
    video, and other applicant data are combined.
-   **Vulnerable data subjects / power imbalance:** relevant in the
    employment context.
-   **Innovative technology:** yes --- AI-based applicant assessment.
-   **Processing preventing access to an opportunity:** relevant because
    the system determines progression toward employment.

This is well beyond a borderline screening case. The bank should
complete the DPIA before first production processing and use it to
assess necessity, proportionality, discrimination/error risks, human
oversight, and mitigation.

### 4. Data-subject friction points

**Access:** Applicants may ask what personal data and inferred scores
the bank holds about them. The system therefore needs traceable records
linking source application data to generated scores and recruitment
outcomes.

**Erasure:** The bank needs a defined process for deleting application
material, video, inferred scores, and vendor-held copies when erasure
applies. Retention in model, logging, or other infrastructure must be
included in the deletion design.

**Objection/profiling:** Where processing relies on legitimate interests
and constitutes profiling, applicants may object. The bank needs an
operational route for receiving and evaluating objections.

**Automated-decision safeguards:** Where Article 22 applies and an
exception permits the processing, appropriate safeguards include the
ability to obtain human intervention, express a point of view, and
contest the decision.

### 5. Controller / processor split

  --------------------------------------------------------------------------
  Entity                  Role                       Why
  ----------------------- -------------------------- -----------------------
  **Regional bank**       **Controller**             Determines why
                                                     applicant data is
                                                     processed and decides
                                                     to use AI
                                                     ranking/rejection as
                                                     part of recruitment.

  **Recruitment/AI        **Likely processor if      Processes applicant
  vendor**                operating on the bank's    data to provide the
                          documented instructions**  screening/ranking
                                                     service. If it
                                                     independently
                                                     determines purposes for
                                                     some processing, its
                                                     role requires separate
                                                     assessment.

  **Model/API provider**  **Processor or             Performs model
                          subprocessor where it      inference or related
                          receives applicant data on processing. Exact role
                          instructions through the   depends on contracts
                          service chain**            and data flow.

  **Cloud/hosting         **Processor/subprocessor   Provides infrastructure
  provider**              where it stores or         rather than determining
                          processes applicant data   the recruitment
                          for the service**          purpose.
  --------------------------------------------------------------------------

The bank remains responsible for its controller obligations even when
the scoring technology is supplied by a vendor.

### 6. DPAs

**Yes.** Article 28 DPAs are required with entities that act as
processors on the bank's behalf. The bank should identify the full
processing chain, including subprocessors, and verify instructions,
confidentiality, security, assistance with data-subject rights,
deletion/return of data, audit rights, and subprocessor conditions.

The scenario does not name the vendor, so whether compliant DPAs already
exist is **TBD --- legal review**.

------------------------------------------------------------------------

## Section C --- Law stacking

**AI Act cross-check:** The recruitment system is **high-risk** because
it is intended to evaluate/select candidates for employment. The AI Act
adds system-specific obligations around risk management, data
governance, documentation/logging, transparency, accuracy/robustness,
and human oversight. GDPR simultaneously governs the processing of
applicant personal data. The regimes therefore apply in parallel.

**ePrivacy check:** **N/A on the current fact pattern.** No cookies,
tracking pixels, or device-level tracking are described. If the
recruitment portal later adds non-essential tracking technologies,
ePrivacy requirements would need a separate assessment.

**Data Act check:** **N/A on the current fact pattern.** The system does
not involve connected-product or IoT data.

------------------------------------------------------------------------

# Phase 3 --- Client recommendation memo

**To:** Regional Bank --- Legal / Data Protection & HR Leadership\
**From:** Louise Plessis, AI Product Consultant\
**Subject:** GDPR assessment of AI-assisted applicant screening

## Bottom line: GO WITH CONDITIONS

The bank can continue exploring AI-assisted recruitment, but I would
**not deploy the current automatic-rejection design without changes**.
The system processes extensive applicant data, profiles and ranks
individuals, and automatically rejects the bottom 60% without meaningful
human review. This creates material GDPR risk, particularly under
Article 22, and warrants a DPIA before deployment.

I recommend three actions in sequence.

**1. Redesign the rejection step before launch.** Use AI ranking as
decision support rather than allowing the model alone to reject
applicants. A trained recruiter should meaningfully review candidates
before rejection, have access to relevant information beyond the model
score, and have genuine authority to override the recommendation. If the
bank wants to retain solely automated rejection, legal counsel must
first establish that an Article 22 exception applies and that all
required safeguards are implemented.

**2. Complete the GDPR assessment and data-governance design.** Conduct
a DPIA covering scoring, ranking, video analysis, "culture fit," error
and discrimination risks, and human oversight. Document an Article 6
lawful basis for each distinct purpose rather than treating submission
of a job application as permission for every form of AI profiling.
Confirm whether the system processes or infers Article 9 data and remove
unnecessary sensitive inference.

**3. Put the vendor and applicant-rights framework in place.** Map every
processor and subprocessor receiving applicant data, execute Article 28
DPAs, verify hosting locations and any international-transfer mechanism,
and establish retention/deletion rules. Update applicant-facing
information to explain the AI processing and create operational
workflows for access, erasure, objection, and---where Article 22
applies---human intervention and contesting a decision.

Residual risks will remain. AI ranking can reproduce bias or generate
inaccurate assessments even with human review; "culture fit" is
inherently difficult to define and validate; and meaningful oversight
can deteriorate into rubber-stamping under hiring pressure.

This is a first-pass compliance assessment, not a legal opinion or
completed DPIA. The bank's DPO/legal counsel should validate the lawful
bases, Article 22 position, Article 9 analysis, and vendor arrangements
before deployment.

------------------------------------------------------------------------

# Phase 4 --- Verify: Partner peer review

**Reviewer:** Mudit\
**Status:** Simulated draft for partner confirmation

  ------------------------------------------------------------------------
  Criterion                               Score 1--3 Comment
  --------------------- ---------------------------- ---------------------
  **Clear bottom-line                          **3** "Go with conditions"
  recommendation**                                   is clear and directly
                                                     connected to the main
                                                     issue: automatic
                                                     rejection without
                                                     meaningful human
                                                     review.

  **Lawful basis                               **3** The audit does not
  selection is                                       force a single lawful
  justified**                                        basis across all
                                                     recruitment
                                                     processing and
                                                     correctly flags
                                                     unresolved points for
                                                     legal review.

  **Top actions are                            **3** Redesigning the
  specific and                                       rejection step first,
  sequenced**                                        completing the
                                                     DPIA/legal analysis
                                                     second, and
                                                     addressing vendors
                                                     and applicant rights
                                                     third gives the
                                                     client a practical
                                                     order of action.

  **Residual risks are                         **3** Bias, inaccurate
  named honestly**                                   assessment, the
                                                     validity of "culture
                                                     fit," and human
                                                     rubber-stamping
                                                     remain credible risks
                                                     even after
                                                     mitigation.

  **Law stacking is                            **3** The analysis clearly
  addressed (AI Act /                                distinguishes GDPR
  ePrivacy)**                                        from the AI Act
                                                     high-risk
                                                     requirements and
                                                     correctly treats
                                                     ePrivacy as not
                                                     triggered by the
                                                     facts currently
                                                     provided.
  ------------------------------------------------------------------------

### Client response

The recommendation to proceed with conditions is convincing. My main
concern is whether requiring human review of every candidate who would
otherwise be automatically rejected removes too much of the efficiency
benefit that motivated the system. I would ask the consultant to clarify
how meaningful human review could be designed proportionately without
simply recreating the entire manual screening process.

------------------------------------------------------------------------

# Phase 5 --- Debrief

The two audits broadly agreed that AI-assisted recruitment requires
particularly careful treatment of **lawful basis, DPIA requirements,
profiling, and automated decision-making**. We also agreed that having a
human somewhere in the recruitment process is not sufficient by itself:
human oversight needs to occur at the relevant decision point and must
be capable of changing the outcome.

The main discussion point was **Article 22 and the automatic rejection
step**. My assessment treats automatic rejection of the bottom 60% as
the most significant GDPR issue because those candidates receive no
human review before the negative decision. The client perspective raised
a useful product challenge: reviewing every potentially rejected
application could undermine the efficiency objective that motivated the
AI system.

We therefore considered a stronger middle ground. The AI can remain
useful for **ranking and decision support**, but the process should
introduce a proportionate human-review mechanism before final rejection.
The reviewer should not simply approve the model's recommendation; they
need enough information and authority to identify errors and reverse an
outcome. The exact operational design could use structured review
criteria or prioritised review of borderline cases, but it must preserve
genuinely meaningful human involvement.

The stronger reading is therefore not that AI screening must be
abandoned. It is that **automation can assist recruitment without
automatically becoming the final decision-maker**. This interpretation
also aligns the GDPR analysis with the AI Act's emphasis on human
oversight for high-risk recruitment systems.

------------------------------------------------------------------------

# Reinforce --- DPIA outline

## Processing activity

AI-assisted evaluation, scoring, ranking, and rejection of applicants
for entry-level analyst roles using CVs, cover letters, application
information, and potentially video-based signals.

## Necessity and proportionality

The bank should document the specific recruitment problem the AI system
solves and demonstrate why each input and inference is necessary. In
particular, it should assess whether "culture fit" and video analysis
provide sufficiently valid job-related information to justify their
privacy and fairness impact, and whether automatic rejection is
necessary when AI-assisted prioritisation with human review could
achieve the efficiency objective.

## Main risks

-   Qualified applicants incorrectly rejected because of model error.
-   Discriminatory outcomes or proxy discrimination.
-   Unnecessary inference of sensitive/personal characteristics.
-   Applicants unable to understand or contest an AI-influenced
    decision.
-   Excessive retention of CVs, video, scores, and model outputs.
-   Vendor access or international transfer of applicant data without
    adequate controls.
-   Human reviewers over-relying on model recommendations.

## Proposed mitigations

Use meaningful human review before rejection; minimise input features;
remove unjustified sensitive/proxy features; validate model performance
and bias; provide applicant transparency and contest routes; establish
retention/deletion controls; document vendor/transfer arrangements;
restrict access; and monitor whether human reviewers actually exercise
independent judgment.

------------------------------------------------------------------------

# Reinforce --- DPA clause to prioritise

One clause I would specifically require is a strong **deletion and
return of data clause**, including deletion from subprocessors and
derived stores when the bank instructs deletion or the service ends.

This matters because applicant information may exist not only as the
original CV or video but also in logs, intermediate processing, model
inputs, scores, or other derived records. The bank needs contractual and
technical assurance that a deletion instruction can propagate through
the processing chain rather than deleting only the visible application
record.

------------------------------------------------------------------------

# Stretch --- Data protection by design checklist

**Highest-risk activity:** AI scoring/ranking used to automatically
reject job applicants.

  -----------------------------------------------------------------------
  Design principle        Current state           Pass / Fail / Unknown
  ----------------------- ----------------------- -----------------------
  **Data minimisation**   CV, cover letter,       **Fail**
                          application data and    
                          video may all be        
                          processed; necessity of 
                          every feature,          
                          especially "culture     
                          fit" signals, has not   
                          been demonstrated       

  **Purpose binding**     Recruitment is the      **Unknown**
                          stated purpose, but     
                          distinct uses such as   
                          profiling/ranking and   
                          future reuse are not    
                          technically documented  

  **Access controls**     No access-control model **Unknown**
                          is specified in the     
                          scenario                

  **Retention             No retention or         **Fail**
  enforcement**           automated deletion      
                          period is specified     

  **Subject-rights        No documented access,   **Fail**
  workflow**              erasure, objection,     
                          human-intervention or   
                          contest workflow is     
                          described               

  **Incident response**   No breach-response      **Unknown**
                          process is specified    
  -----------------------------------------------------------------------

### Required redesign

Before production, the bank should minimise features to demonstrably
job-relevant information, define separate purposes and retention
periods, implement role-based access, automate deletion where
appropriate, and create applicant-rights workflows. The
automatic-rejection stage should be replaced with meaningful human
review unless legal counsel establishes a valid Article 22 route for
solely automated decision-making and the necessary safeguards are
implemented.

------------------------------------------------------------------------

# Final recommendation

**GO WITH CONDITIONS.**

The AI system can support recruitment, but the current design should not
move into production unchanged. The priority is to address the automatic
rejection mechanism, complete the DPIA and lawful-basis analysis, and
establish the necessary applicant-rights and vendor controls.

AI-assisted ranking can remain valuable, but the system should support
human decision-making rather than silently becoming the final
decision-maker for access to employment.
