# Tab 1

## Mudit's cases:

**Case 1**

Mid-size furniture manufacturer. Wants a tool to predict which machines on the factory floor are likely to need maintenance in the next two weeks, based on sensor readings, so they can schedule downtime instead of dealing with breakdowns. Signals: vibration data, temperature, run-hours, past maintenance logs. Affects: internal maintenance scheduling — no customer- or employee-facing decisions. A technician reviews every flagged machine before any work order goes out.

**Case 2**

D2C skincare brand, growing fast, support team is overwhelmed. Wants a chatbot on the website and in-app that handles order status, returns, and product recommendations, escalating anything complex to a live agent. Signals: order history, browsing behavior, FAQ text. Affects: customers chatting with support. Human agents pick up anything the bot can't resolve, and there's a queue for escalations, but the bot currently doesn't disclose upfront that it's not a person.

**Case 3**

Regional bank's HR team, hiring volume is up and they're drowning in applications. Wants a model to rank incoming resumes and cover letters for entry-level analyst roles, auto-rejecting the bottom 60%. Signals: resume text, past employer names, education, a "culture fit" score derived from a short video intro. Affects: job applicants. Human review exists on paper (a recruiter can override) but in practice nobody looks at the bottom 60% — they never enter the pipeline.

**Case 4**

Mid-size staffing agency, call center division. They want a system that uses webcam and voice data during shifts to flag agents as "disengaged" or "at risk of burnout" in real time, feeding a dashboard managers use for coaching conversations and shift reassignments. Signals: facial expression analysis, tone of voice, keystroke pace. Affects: call center employees. No human review before the flag hits the manager's dashboard — the whole pitch was "catch it before it becomes a performance issue."

# Tab 2

## Answer key to Mudit's cases:

| Case | Client brief for partner | Intended category in your private answer key | Why you chose it |
| :-: | :-- | :-: | :-- |
| **1 – Predictive maintenance** | Mid-size furniture manufacturer. Wants a tool to predict which machines on the factory floor are likely to need maintenance in the next two weeks, based on sensor readings, so they can schedule downtime instead of dealing with breakdowns. Signals: vibration data, temperature, run-hours, past maintenance logs. Affects: internal maintenance scheduling — no customer- or employee-facing decisions. A technician reviews every flagged machine before any work order goes out. | **Minimal risk** | The AI predicts machine maintenance needs using industrial sensor and maintenance data. It does not make decisions about people and does not appear to fall under an Annex III use case. |
| **2 – Customer support chatbot** | D2C skincare brand, growing fast, support team is overwhelmed. Wants a chatbot on the website and in-app that handles order status, returns, and product recommendations, escalating anything complex to a live agent. Signals: order history, browsing behavior, FAQ text. Affects: customers chatting with support. Human agents pick up anything the bot can't resolve, and there's a queue for escalations, but the bot currently doesn't disclose upfront that it's not a person. | **Limited risk / transparency** | Customers interact directly with an AI system. Article 50 therefore requires them to be informed that they are interacting with AI unless this is obvious from the circumstances. The current lack of disclosure is the main AI Act issue. |
| **3 – Recruitment ranking** | Regional bank's HR team, hiring volume is up and they're drowning in applications. Wants a model to rank incoming resumes and cover letters for entry-level analyst roles, auto-rejecting the bottom 60%. Signals: resume text, past employer names, education, a "culture fit" score derived from a short video intro. Affects: job applicants. Human review exists on paper (a recruiter can override) but in practice nobody looks at the bottom 60% — they never enter the pipeline. | **High-risk** | AI used to analyse/filter job applications and evaluate candidates falls within Annex III employment high-risk use cases. Auto-rejecting 60% makes the system highly consequential. The nominal ability to override does not amount to meaningful human oversight if recruiters never review rejected candidates. |
| **4 – Employee engagement/burnout detection** | Mid-size staffing agency, call center division. They want a system that uses webcam and voice data during shifts to flag agents as "disengaged" or "at risk of burnout" in real time, feeding a dashboard managers use for coaching conversations and shift reassignments. Signals: facial expression analysis, tone of voice, keystroke pace. Affects: call center employees. No human review before the flag hits the manager's dashboard — the whole pitch was "catch it before it becomes a performance issue." | **Prohibited** | The system uses facial expressions and tone of voice to infer emotional states such as "disengaged" or "at risk of burnout" in the workplace. AI emotion recognition in workplaces is prohibited. |
