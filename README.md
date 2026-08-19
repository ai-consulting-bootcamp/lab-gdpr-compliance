# Same product, privacy lens: Virtual Coffee Chat Bot

**Track:** Module 7, GDPR · **When:** Week 7, Day 3 · **Status:** Required

This repository contains a mini GDPR audit and client recommendation memo for the **Virtual Coffee Chat Bot**, a RAG-backed conversational agent that stands in for a first coffee chat with a candidate and lets recruiters book a call or send a message from inside the conversation.

**System under audit:** https://github.com/jp92672/johna-project3-week6-virtural-coffee-chat-bot (John Adams, Project 3, Week 6)

The same system was mapped through EU AI Act risk tiers in the previous lab. This repo re-examines it under GDPR, which is how the two analyses usually run in a real engagement: in parallel, not in sequence.

## Files

- [`instructions.md`](./instructions.md) the lab instructions, scoped to this scenario
- [`rubric.md`](./rubric.md) how the submission is graded; this is what the AI reviewer checks the PR against
- [`gdpr-audit-pack-gordan.md`](./gdpr-audit-pack-gordan.md) the deliverable: fact pattern, transition note from the AI Act lab, audit worksheet (Sections A, B, C) and the 300 to 400 word client recommendation memo
- [`peer-review-coffee-chat-bot.md`](./peer-review-coffee-chat-bot.md) completed peer feedback rubric and the client-voice response from the partner swap
- [`dpia-outline.md`](./dpia-outline.md) optional Reinforce work: DPIA outline for the highest-risk processing activity
- [`privacy-by-design-checklist.md`](./privacy-by-design-checklist.md) optional Stretch work: data protection by design checklist with pass / fail / unknown per item

## Scenario summary

| Element | Detail |
|---|---|
| Client | Sole operator running the bot as a public-facing job search tool |
| Data subjects | Recruiters and hiring managers who open the widget, plus the owner himself |
| Personal data | Knowledge base (CV, CliftonStrengths, career narrative), free-text chat transcripts, thumbs feedback, booking details, outbound email content, error logs |
| Vendors in the stack | OpenAI, Pinecone, Cohere, Calendly, Resend, plus the hosting layer for self-hosted n8n |
| Autonomy | Retrieve, generate, log and call tools with no human between messages |

## How to complete this lab

1. **Fork** the upstream lab repository.
2. Do the work described in `instructions.md`, committing to the fork.
3. Open a **pull request** back into the upstream repository.
4. Address any blocking AI feedback on the PR and push updates to the same PR.

## Submission hygiene

- Repository scoped to this lab only. No unrelated projects or personal files.
- Clear, descriptive filenames.
- No secrets, API keys or tokens committed. None of the source project's credentials appear here; the audit references vendors by name only.
