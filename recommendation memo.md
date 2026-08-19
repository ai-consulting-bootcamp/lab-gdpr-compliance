To: John Adams, operator, Virtual Coffee Chat Bot
From: Gordan, GDPR audit
Date: 19 August 2026
Re: Can this go live and stay live

Bottom line: go, with conditions. Nothing in the design is unlawful, but the widget is public, it sends recruiter conversations to five non-EU vendors with no processor contracts in place, and nothing deletes anything. Those are paperwork and configuration gaps, fixable in a week.

Three actions, in this order.

Paper the vendors before the widget is public again. Execute DPAs with OpenAI, Pinecone, Cohere, Calendly, Resend and your hosting provider. Record each one's transfer route, DPF certification or standard contractual clauses, checked against the Commerce Department list rather than the vendor's website. Ask OpenAI and Cohere for zero data retention while you are in there.
Put a notice and an AI disclosure at the chat entry point. Who the controller is, that every turn is logged, which vendors receive the text, how long it is kept, and how to object or ask for deletion. Add one line asking users not to type sensitive personal information, and repeat it in the system prompt. The AI disclosure is separately mandatory under Article 50 of the AI Act, which has applied since 2 August 2026.
Set retention and a deletion path. Thirty days on chat_log, ninety on error_log, automated rather than remembered. Add a documented way to remove one person's turns. The Pinecone rebuild looks like a deletion mechanism and is not one: it never touches transcripts.

Residual risks after all three are done.

US transfers stay legally exposed. The Data Privacy Framework is valid today, but the appeal in C-703/25 P is pending at the Court of Justice and the EDPB asked the Commission on 31 July 2026 to re-examine adequacy after the Supreme Court's ruling on FTC independence. If adequacy falls you re-paper onto standard clauses with a transfer assessment per vendor.

Free text cannot be controlled. A recruiter can type health or union information into the box in one sentence. You can warn, minimise and delete quickly. You cannot prevent it, and you have no Article 9 condition for it if it arrives.

Erasure is only partly deliverable. Once a turn reaches OpenAI's abuse-monitoring logs it sits on their thirty-day clock, not yours, unless zero data retention is approved. Promise users what you can actually execute.

Outside privacy scope but raising it anyway: the bot emails using an address a stranger typed, unverified. Add rate limiting and confirmation before someone uses your domain as a relay.