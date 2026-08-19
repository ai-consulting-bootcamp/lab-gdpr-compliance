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
|---|---|---|---|
| 1 – Predictive maintenance | Mid-size furniture manufacturer. Wants a tool to predict which machines on the factory floor are likely to need maintenance in the next two weeks, based on sensor readings, so they can schedule downtime instead of dealing with breakdowns. Signals: vibration data, temperature, run-hours, past maintenance logs. Affects: internal maintenance scheduling — no customer- or employee-facing decisions. A technician reviews every flagged machine before any work order goes out. | Low GDPR risk / mostly non-personal industrial data | The core data is machine telemetry, not personal data. GDPR only becomes relevant if technician names, IDs, or other employee-linked logs are used, in which case ordinary controller, retention, and access controls apply. |
| 2 – Customer support chatbot | D2C skincare brand, growing fast, support team is overwhelmed. Wants a chatbot on the website and in-app that handles order status, returns, and product recommendations, escalating anything complex to a live agent. Signals: order history, browsing behavior, FAQ text. Affects: customers chatting with support. Human agents pick up anything the bot can't resolve, and there's a queue for escalations, but the bot currently doesn't disclose upfront that it's not a person. | Article 6 lawful basis + transparency obligations | The system processes customer personal data for support and recommendations, so a lawful basis and clear notices are needed. If tracking cookies or similar device access are involved, ePrivacy consent may override GDPR flexibility, and the bot must be disclosed clearly as AI. |
| 3 – Recruitment ranking | Regional bank's HR team, hiring volume is up and they're drowning in applications. Wants a model to rank incoming resumes and cover letters for entry-level analyst roles, auto-rejecting the bottom 60%. Signals: resume text, past employer names, education, a "culture fit" score derived from a short video intro. Affects: job applicants. Human review exists on paper (a recruiter can override) but in practice nobody looks at the bottom 60% — they never enter the pipeline. | Article 22 risk / DPIA required / special-category inference risk | This is a consequential employment decision with nominal human review only, so the automated-decision rules and DPIA triggers are strong. The video-based scoring also raises special-category inference concerns and a likely need for strict transparency, bias controls, and human intervention. |
| 4 – Employee engagement/burnout detection | Mid-size staffing agency, call center division. They want a system that uses webcam and voice data during shifts to flag agents as "disengaged" or "at risk of burnout" in real time, feeding a dashboard managers use for coaching conversations and shift reassignments. Signals: facial expression analysis, tone of voice, keystroke pace. Affects: call center employees. No human review before the flag hits the manager's dashboard — the whole pitch was "catch it before it becomes a performance issue." | Article 9 special-category inference + Article 22 workplace monitoring risk | The system infers emotional or health-related states from biometric-like signals in an employment setting, which makes the privacy and employment-law risk very high. As designed, it also lacks meaningful human review before the output affects workers, so a DPIA and redesign are the realistic next steps. |
