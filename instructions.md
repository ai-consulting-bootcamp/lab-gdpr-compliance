# Same product, privacy lens: Virtual Coffee Chat Bot

> **Scenario under audit:** [Virtual Coffee Chat Bot](https://github.com/jp92672/johna-project3-week6-virtural-coffee-chat-bot) (John Adams, Project 3, Week 6). This is the same system mapped in the EU AI Act lab, now re-examined through GDPR.

> **How you'll submit this lab**
>
> This repo is your lab. Fork it, do the work described below in your fork, then open a pull
> request back into this repository. An AI reviewer will check your PR against `rubric.md` and
> leave feedback directly on the PR. See `README.md` for the full workflow.

Complete **[GDPR and the EU Data & Privacy Stack](../content/01_gdpr-fundamentals.md)** before starting this lab.

## Lesson alignment

- **Learning objectives:** By the end, you can **complete** a mini GDPR audit for a real-world AI scenario and **write** a short client recommendation memo that identifies obligations, residual risks, and required next steps.
- **Lesson setup requirements:** Revisit the lesson sections on `controllers vs processors`, `lawful bases`, `purpose limitation`, `data subject rights`, `DPIA triggers`, `international transfers`, and `stacking with AI Act and ePrivacy`.

---

## Submission hygiene

- **Filenames:** Use clear, descriptive names (avoid vague names such as `lab.docx` or `audit_final.pdf`).
- **Scope:** Your **GitHub** repository must contain **only materials for this lab**: no unrelated projects, dumps, or personal files.
- **README:** In your GitHub repository, use `README.md` to list each submitted file and what it contains.

**GitHub only:** Submit the URL to a **GitHub repository** that contains everything for this lab (Markdown, code, exports, images, decks). Do **not** submit a standalone Google Doc, Notion page, or cloud-only link as your primary deliverable. Put sources or exports (for example `.md`, `.pdf`, `.pptx`, screenshots) **in the repository**.

## Kick-off

### The committed scenario

This lab carries forward the EU AI Act partner project rather than starting fresh. AI Act and GDPR analysis often happen in parallel in a real engagement, not in sequence, so the same system is audited twice through different lenses.

**System:** Virtual Coffee Chat Bot, a RAG-backed conversational agent that stands in for a first coffee chat with its owner. A recruiter or hiring manager opens a public chat widget, asks about the owner's work history, skills and projects, and can then check availability, book a call, or send a message without leaving the conversation.

**Build facts taken from the source repo (treat these as given, do not invent alternatives):**

| Element | Detail |
|---|---|
| Orchestration | n8n, self-hosted via Docker |
| Generation and embeddings | OpenAI (`gpt-5-mini`, `text-embedding-3-small`) |
| Vector store | Pinecone (index `curious-john`, dimension 512) |
| Reranking | Cohere (`rerank-v3.5`) |
| Scheduling | Calendly API (availability check and booking) |
| Email | Resend API, sends mail on the end user's behalf |
| Logging | n8n Data Tables: `chat_log` (question, answer, thumbs feedback per turn) and `error_log` |
| Knowledge base | `kb/facts` (CV content, CliftonStrengths) and `kb/narrative` (career story, cover letter voice, recruiter Q&A) |
| Front end | Static `chat-ui/index.html` using `@n8n/chat`, public webhook behind Basic Auth |

Commit to this scenario before moving forward. Mixed or hypothetical fact patterns produce weak audit work.

### Setup / first run

1. Open a blank working document titled `GDPR Audit Pack - YourName`.
2. Split the document into two sections: `Audit worksheet` and `Client recommendation memo`.
3. Write a **fact pattern paragraph** (five to eight lines) covering: who the client is, what personal data flows through the bot, where the data subjects are, which non-EU vendors sit in the stack, and what the agent is actually allowed to do on its own.
4. Share the fact pattern with your partner so both of you are working from the same common ground.

### Expected output of first step

A shared, written fact pattern that your partner could read and immediately identify: what data is flowing, to whom, and for what purpose. You will build the rest of the audit on top of this.

---

## CFU checkpoints

### 1. Recognize

Read your fact pattern back and identify: which categories of personal data are present, whether any special-category data (Article 9) might be inferred or included, and whether the data flow crosses an EU border at any point.

Two prompts specific to this system:
- The knowledge base holds the owner's own CV and career narrative. Does that make him a data subject in his own product, and does it change anything?
- End users type free text into an open box. What can land in `chat_log` that nobody designed for?

### 2. Apply

Complete the full audit worksheet (Sections A, B, and C below). For every lawful basis you propose, write a one-line justification. If you are unsure, write `TBD - legal review` rather than guessing.

### 3. Integrate

Write the client recommendation memo. It should reflect the audit findings and include a bottom-line recommendation (go / go with conditions / stop), the top three actions the client must take, and the residual risks you are disclosing even if the project proceeds.

### 4. Verify

Swap your recommendation memo with your partner. Use the peer feedback rubric below. The reviewer acts as the client: they can accept the recommendation, challenge one finding, or ask for a redesign of one section.

### 5. Debrief

After the swap, compare notes. Where did the two audits agree on lawful basis or DPIA need? Where did they diverge? For divergences, agree on which reading is stronger and why.

---

## Core

### Phase 1: Build the fact pattern

Write a brief **transition note** at the top of your document: this scenario is carried forward from the EU AI Act lab, which tier the Virtual Coffee Chat Bot fell into there, and why it is the more interesting case for GDPR purposes. One paragraph. It keeps the two audits connected and mirrors what a real engagement team would document.

Your fact pattern must answer:

- Who is the client? (the bot's owner as a sole operator, and how that changes the compliance burden)
- What personal data is processed? (knowledge base content, chat transcripts, booking details, email content, error logs)
- Who are the data subjects? (recruiters, hiring managers, anyone who opens the public widget, plus the owner himself)
- Where are the data subjects located? (assume EU/EEA plus a realistic share of third-country recruiters, and say so explicitly)
- Who are the vendors in the stack? (OpenAI, Pinecone, Cohere, Calendly, Resend, plus the hosting layer for n8n and the chat UI)
- What does the agent actually do with the data? (retrieve, generate, log, and call tools without a human between messages)
- Is there any automated decision-making with legal or similarly significant effects?

### Phase 2: Mini GDPR audit worksheet

Work through each section in your document. Be specific. Vague answers are not useful in a real client audit.

#### Section A: Data map

| Field | Your answer |
|---|---|
| Categories of personal data | |
| Sources (where data comes from) | |
| Purpose(s), one row per purpose | |
| Lawful basis per purpose, or `TBD - legal review` | |
| Retention period per purpose | |
| Recipients and sub-processors | |
| International transfers and transfer mechanism | |

Run at least these purposes as separate rows: answering questions from the knowledge base, logging conversations for quality and feedback, booking a call through Calendly, sending an email on the end user's behalf, and error logging with alerting.

For the lawful basis column, use the six options from Article 6: consent, contract, legal obligation, vital interests, public task, or legitimate interests. If you are considering legitimate interests, note the three-step test: purpose, necessity, balancing.

#### Section B: Risk and rights

Answer each question in one to three sentences:

- Are any special-category data present or inferable? Consider what a recruiter might volunteer in free text and what the career narrative content itself reveals.
- Is there automated decision-making with legal or similarly significant effects (Article 22)? If your answer is no, defend it. The agent acts without a human in the loop, so the reasoning matters more than the verdict.
- Is a DPIA required? Use the EDPB's nine criteria: explain which apply and why. Say plainly if the count falls short of the usual threshold.
- What data subject friction points are most likely? Consider access and erasure requests against a Pinecone index that is cleared and rebuilt wholesale, and against transcripts already sent to a model provider.
- What is the controller / processor split? Name each entity and its role: the owner, OpenAI, Pinecone, Cohere, Calendly, Resend, and the n8n hosting layer.
- Is a DPA needed with any vendor? Which ones, and is a controller-to-controller relationship hiding among the ones you assumed were processors?

#### Section C: Law stacking (one line each)

- **AI Act cross-check:** Which tier does the system fall into, and does Article 50 transparency add an obligation that GDPR does not cover?
- **ePrivacy check:** Does the chat widget, the hosting layer, or the `@n8n/chat` package set or read anything on the user's device? If yes, does ePrivacy's consent requirement override GDPR's flexibility?
- **Data Act check:** Is there connected product or cloud switching data involved? Flag it or mark it N/A with a reason.

### Phase 3: Write the client recommendation memo

Write **300 to 400 words** addressed to your client. Write it as a consultant delivering a short advisory note, not as a filled-in worksheet.

Your memo must include:

- **Bottom line:** go / go with conditions / stop, plus the one-sentence reason.
- **Top three actions:** specific, concrete, and sequenced. For example: `(1) Execute DPAs with OpenAI, Pinecone, Cohere, Calendly and Resend before the widget goes public; (2) publish a privacy notice at the chat entry point covering logging, transfers and retention; (3) set an automated retention rule on chat_log and error_log.`
- **Residual risks:** two to three risks that remain even if the client follows your recommendations. Be honest. Clients need to know what cannot be fully eliminated.

Avoid academic language. Write as if you are handing this note to the client's legal team or CTO and they have five minutes to read it.

### Phase 4: Partner swap and peer review

Swap your recommendation memo with your partner. Use this rubric when reviewing:

| Criterion | Score 1 to 3 | Comment |
|---|---|---|
| Clear bottom-line recommendation | | |
| Lawful basis selection is justified | | |
| Top actions are specific and sequenced | | |
| Residual risks are named honestly | | |
| Law stacking is addressed (AI Act / ePrivacy) | | |

After the rubric, write two to three sentences as the "client": either accept the recommendation, flag one concern, or ask the consultant to rethink one section.

---

## Reinforce

If you finish early, push the depth of your audit:

- Add a **DPIA outline** for the most sensitive processing activity, most likely the logging of free-text conversations and their transit through a US model provider. Map the main sections only: description of processing, necessity and proportionality, risk identification, proposed mitigation.
- Identify **one specific clause** you would want in the DPA with the main model vendor, and explain why. Training-on-input and retention-on-vendor-side clauses are the obvious candidates.
- Rewrite your bottom line as if the client tells you that half the recruiters using the bot are in the UK. Does anything change under UK GDPR?

---

## Stretch

Take the highest-risk processing activity in the scenario and build a **mini data protection by design checklist**. For each item, note whether the current setup passes, fails, or is unknown based on what the repo actually shows:

- Data minimisation: is only the minimum necessary data collected, and does the chat log need to store full turns?
- Purpose binding: is data technically restricted to the stated purpose, or could the transcript store be reused later as training material?
- Access controls: Basic Auth on the widget and credentials in n8n's own store. Is that sufficient, and who can read the Data Tables?
- Retention enforcement: is there any automated deletion or anonymisation on `chat_log` and `error_log` today?
- Subject rights workflow: can the owner answer an access or erasure request within 30 days, given the Pinecone rebuild pattern and vendor-side copies?
- Incident response: is there a documented path to detect and notify a breach within 72 hours? The error-alert workflow catches crashes, not disclosure incidents. Say what that gap means.

Keep this to half a page. The goal is better consulting depth, not a second memo.
