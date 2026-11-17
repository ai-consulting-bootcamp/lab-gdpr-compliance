# Phase 1: Fact pattern

*GDPR Mini Audit - Warehouse Shift AI - Ayhan Demir*

## Transition note

I am carrying forward Julia's warehouse case from the EU AI Act lab: a logistics company that infers workers' stress, frustration and motivation from webcam images and voice recordings and uses this to recommend assignments to demanding shifts. In the first pass I rated it high-risk (Annex III pt. 4(b)). Re-reading the facts, inferring emotions of workers in the workplace is prohibited under Art. 5(1)(f) AI Act, and shift allocation alone would be high-risk. It is the most interesting case for GDPR because it combines biometric and possibly health data, employees who cannot freely consent, and automated recommendations about working conditions.

## Fact pattern


Facts not in the brief are marked *(assumed)*.

| Question | Answer |
| --- | --- |
| Client | Large warehouse and logistics company, ~5,000 warehouse workers across sites in Germany and Poland *(assumed)* |
| Personal data | Webcam images of faces, voice recordings, inferred stress, frustration and motivation scores, employee ID, shift history and assignments, supervisor overrides. Continuous capture during shifts, high volume, highly sensitive. |
| Data subjects | Employees (warehouse workers); supervisors whose override decisions are logged |
| Location | EU only (Germany, Poland) *(assumed)* |
| Vendors | US-based emotion analytics SaaS vendor *(assumed)*; EU-region cloud host; existing workforce management (scheduling) system |
| What the AI does | Analyses faces and voices to infer emotional state per worker, then ranks workers for demanding shifts |
| Automated decision-making | Yes in effect: the system recommends shift assignments and supervisors can override. If supervisors mostly accept the recommendation, it is close to a solely automated decision with a significant effect on working conditions. |
