# Phase 3: Client recommendation memo

*GDPR Mini Audit - Warehouse Shift AI - Ayhan Demir*


**To:** Legal and CTO, [Client]
**From:** Ayhan Demir
**Re:** AI shift recommendations based on worker emotion analysis

**Bottom line: Stop as designed.** Inferring workers' emotions from webcam and voice data is banned under the EU AI Act and has no lawful basis under GDPR, so the current design cannot launch in any form.

The business goal, filling demanding shifts fairly and reliably, is legitimate. It can be met with a different input. Removing cameras and microphones from the design also removes the biometric and health data, which is the hardest GDPR problem today. What remains is a normal, if still regulated, workforce planning tool.

**Top three actions**

1. **Stop and clean up now.** Switch off any emotion analysis pilot, delete captured video, audio and emotion scores, and confirm deletion in writing from the analytics vendor.
2. **Redesign on objective data, then run a DPIA before first use.** Base recommendations on skills, certifications, rest-time rules, workload, past shift balance and worker-stated preferences. The redesigned tool is still high-risk under the AI Act, so request the vendor's conformity documentation and complete a DPIA before any data flows.
3. **Put the governance in place before go-live.** Sign Art. 28 DPAs (with SCCs or DPF check for the US vendor), agree the system with the works council, update the employee privacy notice, and set up a real human review and appeal route for shift assignments.

**Residual risks**

- **Rubber-stamping:** even with a review step, supervisors may accept most recommendations, which keeps Art. 22 exposure alive. Track override rates monthly and audit a sample of accepted recommendations.
- **Proxy bias:** objective inputs like attendance can still encode health or caregiving patterns and lead to unfair outcomes. Bias testing reduces this but does not remove it.
- **Trust and co-determination:** after an emotion-monitoring proposal, workers and the works council may resist the redesigned tool, which can delay rollout.
