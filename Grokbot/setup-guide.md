# Grokbot setup guide · build the five bots yourself

Written 2026-10-21 from `grokbot-master-prompt.md` v1.0. Follow it top to bottom, one step at a time.

Grokbot's screens are not documented in the master prompt, so this guide names the setting you need ("system prompt", "knowledge", "tools", "schedule") rather than a button. Use the matching field in Grokbot.

## How every bot is built (the recipe)

Every bot, now and later, is the same seven moves:

1. Create the bot and give it its name.
2. Paste its system prompt.
3. Attach its knowledge files.
4. Turn on its tools, at the lowest permission that works.
5. Set its schedule.
6. Run the first test and grade it against the pass criteria.
7. Switch it live.

The prompts are already cut for you in `Grokbot/prompts/`:

- `00-SHARED-CORE.md`: Block 0, used by every bot.
- `N-NAME-full-prompt.md`: Block 0 plus that bot's block, ready to paste as one system prompt.
- `N-NAME-block-only.md`: only that bot's block.
- `06-OPTIONAL-BOTS.md`: Block 6, for later.

**Which file to paste.** If Grokbot lets several bots share one knowledge file, upload `00-SHARED-CORE.md` once, attach it to every bot, and paste only `block-only` as the prompt. Otherwise paste `full-prompt` (about 25,000 to 26,500 characters). If the prompt box rejects that length, use the shared-knowledge route.

## Phase 0 · Prerequisites (one time, about 90 minutes)

### 0.1 Create the "Bot Log" sheet (15 minutes)

1. In Google Drive, create a new Google Sheet named `Bot Log`.
2. Rename the first tab to `Log`.
3. Type these headers in row 1, A to H: `Date` · `Bot` · `Account` · `Action` · `Link` · `Next step` · `Rating (1 to 5)` · `What German changed`.
4. Add a second tab named `Seen signals` with headers `Date` · `Company` · `Signal` · `Source URL` (SCOUT's "seen" list, Block 1).
5. Apply the house format to both header rows: fill `#10284A`, Roboto 10 bold white.
6. Set the body to Roboto 10 with wrapping, thin black borders, and URLs in blue.
7. Freeze the first row and the first column (View > Freeze).
8. Hide gridlines (View > Show > Gridlines off).
9. Copy the sheet's ID from its URL into a note. You will paste it into the bots in Phase 1.

Columns A to F come from Block 0.10. Column G is the 1 to 5 rating from Block 7.6. Column H is the "what German changed" note from Block 7.6.

### 0.2 Create the "Daily Tasks" sheet (10 minutes)

1. Create a new Google Sheet named `Daily Tasks`.
2. Type these headers in row 1: `Date` · `Account` · `Task` · `Why now` · `Draft link` · `Due` · `Status`.
3. Apply the same house format as 0.1, steps 5 to 8.
4. Add data validation on `Status` with these values: `Open`, `Done`, `Dropped`. (This is my addition; the file does not list status values.)
5. Save the ID in your note.

### 0.3 Create the "Owned elsewhere" tab (15 minutes)

Block 7.9 asks for one shared tab but gives no columns. These columns are my proposal; change them if you prefer.

1. Open the Deal Status GTM sheet (`1WPz1JW9zQm06SQg9ncrBM-4BH8ZKWh5O2Pn18XvKKPc`).
2. Add a tab named `Owned elsewhere`. If you can't edit that sheet, add the tab to `Bot Log` instead.
3. Type headers: `Account` · `Category` (Other rep / Customer / Partner / Do not touch) · `Owner` · `Note` · `Date added`.
4. Fill in what Block 0.11 already lists:
   - Samuel Vieira owns Waymo, Collinson, Adobe, Discord and the OnlyFans vault RFP.
   - Rasheed owns DoorDash.
   - Alejandro Bernal owns Upwork.
   - Maria Jose Pineda owns Yango.
   - Justo owns Carry1st, CellPoint and OnlyFans banking.
   - The partners are PayPal, EBANX, dLocal, Google Pay, Apple Pay, Shopify, Affirm, Nium, Bitso and Coinbase.
5. Apply the house format.

One-line flag: Block 0.11 lists Carry1st and CellPoint under Justo, but you work both deals. Add each as "shared with Justo" so COACH doesn't stop on them.

### 0.4 Build the "Yuno GTM Brain" folder (20 minutes)

1. In Google Drive, create a folder named `Yuno GTM Brain`.
2. Upload `Grokbot/prompts/00-SHARED-CORE.md`.
3. Upload `Claude App Export/MEMORY_FULL.md` (571 KB).
4. Upload `Claude App Export/PROJECT_INSTRUCTIONS.md` (52 KB).
5. Leave room for the Yuno facts sheet and the pricing summary from Block 7.1. SCOUT maintains the facts sheet once it is live; you don't need it to launch.

If Grokbot rejects MEMORY_FULL.md for size, split it into two files at a section heading and upload both halves.

### 0.5 Check your connectors and scopes (30 minutes)

You've already connected tools. Open each connection and confirm the scope below. This table is the hard rule: no send, no delete, no Salesforce.

| Tool | Allow | Must be OFF |
|---|---|---|
| Gmail | read, search, create draft, reply as draft | send, forward, trash, delete, mark spam, change labels |
| Google Calendar | read, search | create, update, delete, respond to invites |
| Google Drive | search, read, create file, copy file | trash, delete, share |
| Google Docs | create, edit | none needed beyond Drive |
| Google Sheets | read, append, update values | delete sheets or files |
| Google Slides | read, edit (DECK only) | none |
| Slack | read, search, message drafts | send message, schedule message |
| Gong | read | anything else |
| Web search and browsing | on | n/a |
| Salesforce | do not connect | everything |

Do these steps:

1. For each tool, turn off every action in the right-hand column if Grokbot shows per-action switches.
2. If a tool has no per-action switches, write it down. It goes into the "unscoped" line of the gap table below.
3. If Grokbot connects through a service account instead of your login, share only these files with that account's email: Bot Log, Daily Tasks, Deal Status GTM, the Target Company List, AI Prospects Master, the pricing docs from Block 0.12, the deck templates, and the Yuno GTM Brain folder. Grant Editor only on Bot Log and Daily Tasks; Viewer on everything else.

**If Gmail send can't be switched off.** That is the Milo risk from Block 7.3. Stay safe in two ways:

1. Leave the Block 0.10 drafts-only rule in every prompt, which it already is.
2. Turn on Gmail's "Undo send" at the maximum 30 seconds as a seatbelt.
3. Watch your Sent folder daily for the first week.

If an unapproved send ever happens, disconnect Gmail from all bots the same day.

One-line flag: Block 0.10 says to "create a new [draft] and delete the old" when a reply draft would detach. Deleting drafts needs a delete scope, which conflicts with the hard rule. If you keep delete off, the bot should leave the old draft and tell you which one to discard.

## Phase 1 · One card per bot, in launch order

Before you start, fill in the IDs. In each prompt you paste, Block 0.10 mentions "Bot Log" and Block 5 mentions "Daily Tasks" by name only. Add one line at the very end of every prompt:

`Bot Log sheet ID: {paste}. Daily Tasks sheet ID: {paste}. Owned elsewhere tab: {sheet ID and tab name}.`

### Card 1 · COACH

**Purpose:** your chief of staff. Each morning COACH reads your inbox, calendar, pipeline and signals, then writes the day's plan with drafts ready.

1. Create a bot named `COACH`.
2. Paste `prompts/1-COACH-full-prompt.md` as the system prompt, or `1-COACH-block-only.md` if you attached `00-SHARED-CORE.md` as shared knowledge.
3. Add the sheet ID line at the end of the prompt.
4. Attach as knowledge: `MEMORY_FULL.md` and `PROJECT_INSTRUCTIONS.md`.
5. Turn on these tools:
   - Gmail: read and create draft.
   - Calendar: read.
   - Sheets: read and write.
   - Drive: read.
   - Gong: read.
   - Slack: read and drafts.
   - Web search.
6. Set the schedule to `07:00, Monday to Friday, America/Los_Angeles`.
7. Set the delivery channel to a Gmail draft to you, subject `Daily Plan · {Weekday, Mon DD}`, plus rows in Daily Tasks. If Grokbot also posts in its own chat, keep that on.
8. Run the first test. Type exactly:
   `Run today's Daily Plan now. It is Thursday, so include the Thursday forecast section. Create the drafts, add the rows to Daily Tasks, and log the run in the Bot Log.`

**Pass criteria (accept if all are true):**

- There is one draft to you, 350 words or fewer, with 3 to 7 ranked moves.
- Each move names the account, the exact action, a one-line "why now", and a link to a draft that sits inside the real thread.
- The follow-ups section uses the right thresholds: 3 business days for prospects, 5 for internal threads, 7 for proposals with no feedback.
- There is a Thursday forecast block, or a question asking you for the target.
- New rows appear in Daily Tasks and one row appears in the Bot Log.
- No em-dashes, no URLs inside the prospect drafts, and two time options per ask.

**Reject if any of these happen:**

- Anything was sent.
- It claims "no reply" on a thread where the latest message shows a reply.
- It repeats the Pipeline Brief instead of turning it into actions.
- It invents a person or an email address.
- It recommends a discount.

**Common failure and fix.** COACH says you never followed up when you did. That is the 14 September 2026 problem. Add this line to its prompt: "Open every thread and read the newest message before calling it unanswered."

**Go live** when two runs in a row pass. Leave the schedule on.

**Flag.** After 2026-11-05 COACH runs at 07:00 Bogotá, which is before the Pipeline Brief (6:30 PT is 9:30 Bogotá after US clocks change on 2026-11-01). Either move the Pipeline Brief routine to 06:00 Bogotá or COACH to 10:00 Bogotá. The spec is unchanged until you decide.

### Card 2 · PREP

**Purpose:** a one-page brief for every meeting with an outside attendee, ready the evening before.

1. Create a bot named `PREP`.
2. Paste `prompts/2-PREP-full-prompt.md` (or the block-only version with the shared core attached).
3. Add the sheet ID line.
4. Attach `MEMORY_FULL.md` and `PROJECT_INSTRUCTIONS.md`.
5. Turn on these tools:
   - Calendar: read.
   - Gmail: read and create draft.
   - Drive and Docs: create and edit.
   - Sheets: read, plus append to the Bot Log.
   - Gong: read.
   - Web search and browsing.
6. Set schedule A to `18:00 daily, America/Los_Angeles`, for next-day meetings.
7. Set schedule B to `06:30 Monday to Friday, America/Los_Angeles`, as a catch-up for meetings added late.
8. Set the delivery channel to a Google Doc with no parent folder, plus one message (an email draft or the Grokbot chat) with the link, the ⚠️ actions and the battle card.
9. Run the first test on your nearest real external meeting, for example the Arrive Recommerce call on 2026-10-29. Type exactly:
   `brief Arrive Recommerce`

**Pass criteria:**

- The Doc title is `Brief: Yuno <> Arrive Recommerce (Oct 29, 2026)`.
- It is one page, 400 to 600 words.
- The header shows the time with its time zone and a list of ⚠️ actions.
- Sections run 1 to 8 in order, with Agenda and Discovery last and "Notes: ____" on every item.
- "Prior meetings" is stated plainly.
- The payments stack carries ✅/⚠️ labels.
- The discovery questions don't re-ask what the emails already answered.

**Reject if:**

- It runs over one page.
- It includes generic sales advice.
- An unverified fact is used as a talking point.
- It tells the prospect they "lack" something.
- A section is padded when it should have been dropped.

**Common failure and fix.** It misses earlier meetings because the company name differs from the email domain. Tell it: "Search past events by attendee email and domain, not only by company name."

**Go live** when the test passes and the next 18:00 run briefs tomorrow's meetings without being asked.

### Card 3 · SCOUT

**Purpose:** daily market and account signals, the Monday Market Pulse, and alerts for urgent triggers.

1. Create a bot named `SCOUT`.
2. Paste `prompts/3-SCOUT-full-prompt.md` (or block-only).
3. Add the sheet ID line.
4. Attach `MEMORY_FULL.md` and `PROJECT_INSTRUCTIONS.md`.
5. Turn on these tools:
   - Web search and browsing.
   - Sheets: read the Target Company List, AI Prospects Master and Deal Status GTM; write to the Bot Log, Seen signals and new lists.
   - Gmail: create draft, for alerts.
   - Drive and Docs: create.
   - Gong: read, for the ownership check.
6. Set schedule A to `06:30 Monday to Friday, America/Los_Angeles` (the Signals run).
7. Set schedule B to `07:00 Monday, America/Los_Angeles` (Market Pulse).
8. Set delivery to an email draft to you (the subject for alerts is `SCOUT alert: {company}`), with lists going to a Google Sheet in the house format.
9. Run the first test on accounts you know well, so you can judge accuracy. Type exactly:
   `scan Lululemon, Thinkific, Flair Airlines, Autodesk, Super.com`

**Pass criteria:**

- There is one signal card per company in the Block 1 format.
- Every signal has a date and a source URL from the last 90 days, or the card says "None detected".
- The ICP score follows the rubric.
- Every card carries a verdict (ATTACK NOW / MONITOR / SKIP) and an ownership check result.
- The run ends with a ranked hit list and a two-line "could not verify" note.
- Signals are logged in Seen signals.

**Reject if:**

- A signal has no date or no source.
- Old news is called "recent".
- PayPal or Apple Pay is listed as a processor.
- A PSP is treated as a prospect.

**Common failure and fix.** It reports the same news every day. Check that it can write to `Seen signals`, and remind it in the prompt to read that tab first.

**Go live** when the test passes. Then let the next Monday 07:00 Market Pulse arrive on its own.

Note: the "immediate alert" only fires when SCOUT runs, so with this schedule alerts arrive at 06:30, not in real time.

### Card 4 · DEEP

**Purpose:** a 2 to 4 page research doc per company, starting from the money and ending with payments and the Yuno angle.

1. Create a bot named `DEEP`.
2. Paste `prompts/4-DEEP-full-prompt.md` (or block-only).
3. Add the sheet ID line.
4. Attach `MEMORY_FULL.md` and `PROJECT_INSTRUCTIONS.md`.
5. Turn on these tools:
   - Web search and browsing.
   - Drive and Docs: create.
   - Sheets: read the lists and append to the Bot Log.
   - Gong: read.
   - Gmail: read, for the ownership check.
6. Leave the schedule off; DEEP runs on demand.
7. Set delivery to a Google Doc plus a 10-line summary in chat.
8. Run the first test on an account you already researched, so you can spot errors. Type exactly:
   `Research Thinkific for a proposal`

**Pass criteria:**

- The Doc is titled `Research: Thinkific (Oct 2026)` with the 11 sections in order.
- Every number carries a period and a source.
- Volumes show the method used.
- At least 8 competitors are named.
- The payments section separates what Thinkific offers its creators from what it uses to get paid.
- The checkout is tested, or marked "not testable".
- The ICP rubric table appears, with the indicative deal size marked INTERNAL ONLY.
- The summary is 10 lines.

**Reject if:**

- A market share is guessed.
- An install-base source is used as revenue share.
- A material fact has only one source.
- A payment method is called missing without a checkout test.

**Common failure and fix.** It re-researches from scratch. Tell it to read MEMORY_FULL and the Bot Log first and to update, not duplicate.

**Go live** after one passing run. DEEP stays on demand.

### Card 5 · DECK

**Purpose:** a Google Slides proposal in your exact look, plus the model sheet behind every number.

1. Create a bot named `DECK`.
2. Paste `prompts/5-DECK-full-prompt.md` (or block-only).
3. Add the sheet ID line.
4. Attach `MEMORY_FULL.md` and `PROJECT_INSTRUCTIONS.md`.
5. Turn on these tools:
   - Drive: search, copy and create (no delete, no share).
   - Slides: read and edit.
   - Sheets: create and edit.
   - Docs: create.
   - Gmail: read and create draft.
   - Gong: read.
   - Web search.
6. Leave the schedule off; DECK runs on demand.
7. Set delivery to the Slides link, the Model link and the 6-line summary in chat.
8. Run test 1, the duplicate guard. Type exactly:
   `Build the proposal for Thinkific`
   - Pass: it finds and reports the deck you already built in October 2026, and asks before building another.
9. Run test 2, the full build, on a merchant with no deck yet. Type exactly:
   `Build the proposal for {merchant}. English. Pricing missing.`
   - Pass: the deck is copied from the right template, the pricing slide reads "PRICING PENDING: German to confirm", and one pricing option is offered in chat with its policy zone.

**Pass criteria for test 2:**

- The deck is copied from the right template family into a folder named after the merchant and renamed `Proposal - {Company} + Yuno`.
- A Model sheet exists, and every number on the slides traces to a cell.
- No leftover template names remain (Eventbrite, Luni, Palco, FlightHub).
- Reconciliation is footnoted as roadmap.
- Only USD is used.
- The stack slide carries ✅/⚠️ labels.

**Reject if:**

- It builds a deck in a different design.
- A minimum price appears.
- A banned stat from Block 0.4 appears.
- An existing deck is overwritten.

**Common failure and fix.** Slides edits break the layout or overflow the slide. Tell DECK to use the fallback in Block 4: a slide-by-slide spec in a Doc, plus the Model sheet, built with the Slides engine in `Deals/{Company}/build`.

**Go live** after both tests pass.

## Phase 2 · Operating the system

### Your daily routine

| Time (local) | What arrives | What you do | Time |
|---|---|---|---|
| 06:30 | Pipeline Brief, SCOUT signals | Skim SCOUT's hit list only | 3 min |
| 07:00 | COACH Daily Plan draft | Read it, open each linked draft, edit and send by hand the ones you agree with | 20 to 30 min |
| During the day | DEEP or DECK on demand | Ask, review, edit | as needed |
| 18:00 | PREP briefs for tomorrow | Read each battle card | 3 min per meeting |
| End of day | n/a | Rate today's outputs 1 to 5 in the Bot Log | 2 min |

### Weekly

1. **Monday 07:00.** Read SCOUT's Market Pulse. Forward the High-rated accounts to DEEP.
2. **Thursday 07:00.** Use COACH's forecast block to prepare for Sean's noon forecast.
3. **Friday 07:00.** Read COACH's 10-line weekly review.
4. **Friday, 15 minutes.** Sort the Bot Log by `Rating`. For every 1 or 2, write what was wrong in `What German changed`.

### Keeping your voice (the Block 7.6 loop)

1. Every time you edit a bot's draft before sending, paste a one-line summary of the change into `What German changed`. For example: "Cut the second paragraph, too salesy."
2. On the first Friday of each month, filter that column and look for changes you made three or more times.
3. Add each repeated change as one new line to Block 0.9 in `grokbot-master-prompt.md`.
4. Regenerate the prompt files (or edit `00-SHARED-CORE.md` and the full prompts by hand).
5. Re-paste the updated prompt into every bot on the same day, so they stay in sync.

### Adding the Block 6 bots later

1. Use the same seven-step recipe from the top of this guide.
2. Build the prompt as `00-SHARED-CORE.md` plus that bot's paragraph from `06-OPTIONAL-BOTS.md`.
3. The order the file recommends is RECAP, then DESK (Block 7.10).
4. TRIAGE needs a two-hour schedule. Check that Grokbot allows that interval before you build it.

### When a bot goes quiet or gets something wrong

1. Check the Bot Log. Is there a row for the last scheduled run?
2. No row means the run didn't happen or failed. Check the schedule and its time zone, then check whether a connector token expired, and reconnect it.
3. If there is a row but bad output, check whether a tool was unreachable. Every bot must say so in one line (Block 0.10). If it didn't say so, that is a prompt failure: re-paste the prompt.
4. If facts are wrong, ask the bot for its source on the specific claim. A missing source is a reject: rate it 1 and note it.
5. If anything was sent, deleted or written to Salesforce, disconnect that tool from all bots right away and check its scopes again.

## Gap table

Fill in the right-hand column as you confirm each capability in Grokbot.

| Spec item | Needs | Fallback if Grokbot can't |
|---|---|---|
| Drafts only (Block 0.10, 7.3) | Gmail without send | Prompt rule + Undo send + daily Sent check (Phase 0.5) |
| Delete old detached draft (0.10) | Gmail draft delete | Leave the old draft, the bot names it, you delete it |
| PREP and SCOUT run twice a day | Two schedules per bot | Create a second copy of the bot with the other schedule |
| SCOUT immediate alerts | Event or frequent runs | Alerts arrive with the 06:30 run |
| Time zone switch on 2026-11-05 | Per-schedule time zone | Change it by hand on 2026-11-05 (set a calendar reminder) |
| Shared Block 0 | Shared knowledge | Paste the full prompt in every bot |
| MEMORY_FULL.md (571 KB) | Large knowledge files | Split it into two or three files |
| Bots reading each other | Sheets access | The Bot Log is the bus; it already works with Sheets |
| DECK editing Slides | Slides write | Spec in a Doc + Model sheet + Slides engine in the repo (Block 4) |
| Gong | Gong connector | The bot says "Gong not connected" and goes on (0.10) |
| Slack | Slack read | COACH skips Slack mentions and says so |
| LinkedIn | Not allowed to scrape | Public pages only; a best-guess URL is marked ⚠️ |
| Salesforce | Never connected | Paste-ready spec every time (Block 7.8) |

## First-week calendar

| Day | Build | Test | Live |
|---|---|---|---|
| Thu 2026-10-22 | Phase 0 (90 min), then COACH | COACH test with the Thursday forecast | n/a |
| Fri 2026-10-23 | PREP | COACH runs on schedule at 07:00 (2nd pass); PREP test "brief Arrive Recommerce" | COACH live if both runs pass |
| Sat to Sun | n/a | PREP 18:00 Sunday run briefs Monday | PREP live if Sunday passes |
| Mon 2026-10-26 | SCOUT | SCOUT scan test | SCOUT live; first Market Pulse next Monday |
| Tue 2026-10-27 | DEEP | DEEP Thinkific test | DEEP live (on demand) |
| Wed 2026-10-28 | DECK | DECK test 1 (duplicate guard) | n/a |
| Thu 2026-10-29 | n/a | DECK test 2 (full build); PREP brief used for the Arrive call | DECK live |
| Fri 2026-10-30 | n/a | First weekly review and rating pass | All five live |
| Thu 2026-11-05 | n/a | Switch every schedule to America/Bogota; decide the COACH vs Pipeline Brief timing | n/a |

## Open points

1. Grokbot's exact settings for per-action scopes, the prompt length limit, shared knowledge and multiple schedules per bot. Fill in the gap table once you see them.
2. The `Owned elsewhere` columns and the `Status` values are my proposals, not from the file.
3. The COACH timing clash with the Pipeline Brief after 2026-11-05.
4. The draft-delete conflict in Block 0.10.
5. Carry1st and CellPoint ownership in Block 0.11 vs your work on them.
6. The quarterly target for COACH's Thursday forecast. COACH will ask for it on the first Thursday.
