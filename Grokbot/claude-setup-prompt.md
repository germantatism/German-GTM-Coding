# Prompt for Claude: step-by-step setup of my Grokbot bots

Paste everything below the line into Claude. If you are in Claude Code inside the GTMCoding repo, Claude reads the master prompt from the file. If you are in the Claude app, attach `Grokbot/grokbot-master-prompt.md` (and, if you have them, Grokbot's docs or a screenshot of the bot creation screen).

---

I am German Tatis, Business Development Manager at Yuno. I am setting up five bots in Grokbot, a bot platform where each bot gets a system prompt, knowledge files, tool connectors and scheduled runs. The complete spec of what each bot does is in the file `Grokbot/grokbot-master-prompt.md` (Block 0 is the shared core; Blocks 1 to 5 are SCOUT, PREP, DEEP, DECK and COACH; Block 6 lists optional bots; Block 7 explains how they work together). Read that file completely before answering. Do not redesign the bots; your job is to get them built and working exactly as specified.

I want a step-by-step implementation guide I can follow in order, with nothing left to interpretation.

**Step 1, before you plan anything:** ask me in ONE message, at most six questions, what you need to know about Grokbot that the file does not say: which connectors it offers (Gmail, Google Calendar, Drive, Docs, Sheets, Slides, Slack, Gong, web search, browsing), whether tools can be scoped (for example Gmail read plus create draft, but never send), whether it supports scheduled runs and at what minimum interval, whether bots can share a knowledge base or read each other's output, how it delivers results (email, Slack, chat), and what model it runs on. If I give you a docs URL instead, read it and skip the questions. If something is unknown, state the assumption you will build on and keep going.

**Step 2, the guide.** Produce it in this exact order:

1. **Phase 0, prerequisites** (one-time, with time estimates): the Google Sheets the bots need and do not exist yet (Bot Log, Daily Tasks, the "Owned elsewhere" tab) with their exact columns and the house format from Block 0; the "Yuno GTM Brain" Drive folder and what goes in it (Block 0 as a file, `Claude App Export/MEMORY_FULL.md`, `Claude App Export/PROJECT_INSTRUCTIONS.md`); the connectors to authorize and with which scopes; anything to share with a service account if Grokbot uses one.
2. **Phase 1, one setup card per bot**, in launch order COACH, PREP, SCOUT, DEEP, DECK. Each card: bot name and one-line purpose · exactly what to paste as the system prompt (Block 0 plus its own block, or Block 0 as knowledge plus its block as prompt, depending on what Grokbot allows) · knowledge files to attach · tools to enable and the permission level of each (least privilege; drafts only, never send) · triggers and schedule in my time zone (Pacific until 2026-11-04, then Bogotá) · delivery channel · the first test I run and the exact message I type · pass criteria (what a correct first output contains, what would make me reject it) · common failure and the fix · go-live switch.
3. **Phase 2, operating the system**: my daily routine with the bots (what arrives when, what I do with it, how long it takes), the weekly review, how I give feedback so the bots keep my voice (the "what German changed" log in Block 7), how to add the Block 6 bots later, and what to check when a bot goes quiet or produces something wrong.
4. **Gap table**: anything in the master prompt that Grokbot cannot do with the capabilities you confirmed, with the fallback for each (for example, no Slides write access means DECK delivers the slide-by-slide spec and the model sheet, as Block 4 already allows).
5. **First-week calendar**: day by day, which bot I set up, which test I run, and when each goes live.

**Rules for your answer**
- Follow the file; do not invent capabilities, numbers or rules that are not in it. If you think something in the file is wrong or risky, say so in one line and keep the spec as is.
- Hard rule across every bot: no bot ever sends an email or message, deletes mail, or writes to Salesforce. If Grokbot cannot restrict a scope, tell me and propose how to stay safe.
- Write in English, no em-dashes, no " - " as punctuation, short paragraphs, numbered steps, one action per step. If you are in Claude Code, also save the guide as `Grokbot/setup-guide.md`, commit and push.
- Do not ask me to confirm the plan; deliver it complete, then list the open points at the end.
