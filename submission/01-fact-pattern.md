# GDPR Audit Pack - Jay & Anand

## Phase 1: Fact Pattern

### Transition Note

This audit carries forward **Case 2 from our EU AI Act "Classify Your Product" lab** — the automotive component manufacturer's AI-driven promotion and termination-risk scoring system. Under the AI Act, this case was classified as **High-risk (Annex III — employment decisions)**, approved with controls contingent on fixing a nominal (not genuinely exercised) human review step, adding bias/accuracy testing on the chat-sentiment component, and disclosing AI use to candidates and employees.

This is the strongest of our eight combined scenarios for a GDPR audit specifically because it stacks several distinct privacy triggers at once that the other seven scenarios don't combine as cleanly: profiling with a legal/similarly significant effect (Article 22), a plausible special-category data inference risk from sentiment analysis on private messages (Article 9), a real international transfer question (Slack/Teams as US-headquartered processors), and a genuine ePrivacy angle from analyzing the content of private workplace communications — a dimension none of our other cases raise. Running the GDPR lens on the same fact pattern we already AI Act-classified also mirrors how these two audits happen in parallel on a real engagement, not as separate, disconnected exercises.

### Fact Pattern

**Client:** An automotive component manufacturer, approximately 1,200 employees, spanning production, quality, and logistics functions across multiple EU manufacturing sites.

**What personal data is processed:** Individual employee productivity metrics (output volume, quality-error rate), attendance records, and a "collaboration signal" derived from automated tone and responsiveness analysis of employees' internal Slack/Teams messages. These are combined quarterly into a composite per-employee score.

**Who are the data subjects:** All salaried and hourly employees whose teams use the in-scope chat platforms — a broad population, not a narrow subset of leadership or a specific department.

**Where are the data subjects located:** EU/EEA, across the client's multiple manufacturing sites (exact jurisdictions TBD — legal review, pending confirmation of which specific facilities are in scope).

**Who are the vendors in the stack:** Slack and/or Microsoft Teams (both US-headquartered platforms) supply the underlying chat data; the composite scoring/dashboard tool itself is either built internally or by a third-party HR analytics vendor (TBD — legal review, pending confirmation from the client on build vs. buy).

**What the AI system does with the data:** Analyzes tone, word choice, and responsiveness patterns in employees' internal chat messages to generate a "collaboration" component of a broader composite score, combined with productivity and attendance data. The composite score is the primary input managers use when deciding promotion nominations and identifying employees for termination-risk coaching conversations.

**Automated decision-making with legal or similarly significant effects:** Yes — the score directly informs promotion and termination-risk decisions, both of which are recognized as having a legal or similarly significant effect on the individual under Article 22. Per our AI Act findings, the human review step in the current design was found to be nominal rather than genuinely exercised (managers were expected to simply act on the score given volume), which is directly relevant to whether Article 22's "solely automated" threshold and its required safeguards are actually being met in practice, not just on paper.
