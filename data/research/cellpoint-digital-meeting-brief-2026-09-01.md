# Meeting Brief: Yuno <> CellPoint Digital

**Tuesday, September 1, 2026 · 09:30 to 10:00 COT** (09:30 Dallas CDT · 15:30 London BST) · 30 min
**Meet:** https://meet.google.com/jsh-hbnq-qtj
**Event:** "CellPoint Digital + Yuno | Workshop Alignment" (organizer: German)

**Objective:** leave the call with a workshop date on the calendar and the proposal feedback we have been waiting on since August 11.

### ⚠️ Pre-meeting actions
- **Bernabé Murata has not responded to the invite** (status: needsAction). Ping him before the call.
- **Confirm with Justo who owns pricing on the call.** If Andrew opens commercials, Justo answers, not German.
- The event title still says "Workshop Alignment" and was created for a September 4 workshop that no longer exists. Reframe in the first 60 seconds so the agenda does not drift.

---

## 1. TL;DR Battle Card

**Five facts to know cold**

1. **The terms on the table** (sent August 11, still unanswered in writing): **USD 50,000/month platform fee** (white label, Yuno's full platform under CellPoint's brand) + **USD 0.07 per successful transaction** + **50/50 revenue share on net platform revenue** for every deal CellPoint closes, 1-year term. ✅ Verified against the PDF that was sent.
2. **Twenty days of silence on the substance.** German asked for feedback on August 11. None has arrived. All correspondence since has been about calendar logistics.
3. **The September 4 Dallas workshop is dead.** Andrew declined it on August 27 after flagging on August 24 that he cannot travel. Date ping-pong: Andrew offered Sep 9 to 11 (Yuno no), Yuno offered the week of Sep 14 to 18 (no answer), Andrew asked about Sep 7 or 8 (Yuno no, company event), Yuno re-offered the week of Sep 14 "any day". Andrew's last word, August 26: *"we are juggling dates and will revert."* Nothing since.
4. **Their stated driver is speed to market, and secondarily cost.** Andrew on August 11: *"it's going to take us far too long to get to that perfect scenario... there's got to be a quicker way to market than try and build it all ourselves."* Jarrett, who spent four months inside CellPoint: *"I know the goal at CPD is to reduce costs."*
5. **Two very different buyers.** Patrick (CTO, Dallas) is the technical champion and asked the deepest question on the call. Andrew (London) controls the calendar and the commercials, and he is the one whose diary keeps slipping.

**Three hooks, in priority order**

1. **Speed to market.** Yuno ships net-new provider integrations in under a week, and in as little as four hours with working credentials, with a dedicated team absorbing the documentation problem Patrick flagged. That is the gap between their roadmap and their sales promises.
2. **Zero-disruption migration.** Keep the Velocity front end, map their API fields to Yuno's, normalize through to the integrations. Existing merchants do not notice. Jarrett and Mauricio are already running this exact play on another white-label account.
3. **Patrick's intelligence layer.** Full transaction lifecycle visibility (inbound data, the payload sent to the provider, the provider response, latency) plus routing control by API, so his ML models can both read and act in real time.

**THE objection they will raise:** the USD 50,000/month platform fee is net-new fixed opex for a company in shareholder-backed turnaround with a cost-reduction mandate, and it lands before a single new deal closes.

**The answer:** do not defend the number, reframe the comparison. The fee replaces the OSO build path, which is infrastructure plus development plus integrations plus ongoing maintenance plus PCI scope plus the team to run it, and it never gets them to parity on the timeline they need. The 50/50 revenue share means Yuno only makes real money when CellPoint wins, so both sides carry the risk. If they push hard, do not discount on the call. Justo can explore structure (a ramp during the migration months, or fee against term or volume commitment) and take it away to formalize.

**The ask:** a confirmed workshop date agreed live on the call, and either written feedback on the proposal or a dedicated commercial session with Justo booked before the workshop.

**Rapport opener:** Andrew had an urgent personal commitment that killed the September 4 travel. One warm line acknowledging it, then move on. Do not pry, and do not mention document tracking.

---

## 2. Who Is in the Room

| Name | Role | Side | Status |
|---|---|---|---|
| Andrew Goddard | Chief Partnerships & Marketing Officer ⚠️ (see below) | CellPoint | Accepted |
| Patrick Uckermark | CTO, based in Dallas | CellPoint | Accepted |
| Justo Benetti | CRO, owns the relationship | Yuno | Accepted |
| Jarrett Falasco | Senior Sales Engineer, ex-CellPoint | Yuno | Accepted |
| German Tatis | BDM, organizer | Yuno | Accepted |
| Bernabé Murata | Business Development | Yuno | ⚠️ No response |

**Andrew Goddard** (London, Surbiton area). Brought in by CellPoint's shareholders at the start of 2026 to turn the business around. He is candid about the past: *"some of our predecessors were slightly guilty in the way they did things... we're over promising and under delivering massively."* He reacted to the Yuno demo with *"this is beyond an expectation, which is great."* He is the buyer for the commercial frame and the one who has to clear travel.

⚠️ **His title has moved three times in five weeks**, from "Chief Product & Partnerships Officer" (July 29 and August 4 signatures) to "Chief Partnerships & Marketing Officer" (August 24 signature), while the August 11 call listed him as "Chief Strategy & Product Officer". The drift is away from Product. This is an inference and must never be said out loud, but it is the reason to ask who else needs to be in the workshop room on product and engineering.

**Patrick Uckermark** (CTO, Dallas, travels to London regularly and was there August 10 to 12). The strongest technical signal in the account. He is personally building a data project: ingesting historical transaction data to train ML models, splitting the live API so every transaction feeds his intelligence layer, and having that layer respond with dynamic routing decisions based on BIN-level knowledge of which PSP will decline. Phase two is ecosystem observability, meaning provider availability per country. He accepts every invite promptly and asks the concrete questions. Treat him as the champion.

**Mauricio Madrigal** is on Yuno's side, leading Yuno's white-label product. He is not a CellPoint employee. (Correcting an earlier note in memory.)

---

## 3. Where the Deal Stands

| Date | What happened |
|---|---|
| Jun 26, 2026 | Intro call, Justo and Bernabé |
| Jul 29, 2026 | Andrew returns the mutual NDA signed |
| Aug 3, 2026 | German returns the NDA countersigned by both parties |
| Aug 11, 2026 | Discovery and demo call. Very well received, zero objections raised. Proposal sent same day with a request for feedback and three Dallas workshop dates |
| Aug 12, 2026 | Andrew and Patrick both open the proposal |
| Aug 19 and 21 | German chases the workshop date, then sends the September 4 invite |
| Aug 24, 2026 | Andrew: cannot travel, offers Sep 9 to 11. German counters with the week of Sep 14 to 18 |
| Aug 26, 2026 | Andrew asks about Sep 7 or 8. German declines (company event) and re-offers the week of Sep 14, any day. Andrew: *"juggling dates and will revert."* |
| Aug 27, 2026 | Andrew formally declines the September 4 invite |
| Aug 31, 2026 | Andrew opens the proposal again from London, the morning before this call 🔍 |

**Read:** the relationship is warm and the technical fit is agreed. What has not moved is the commercial conversation. The date friction is real but it is also a convenient surface for a decision that has not been made. Tomorrow is the moment to separate the two: get the date locked, then find out what is actually happening with the proposal internally.

---

## 4. Be Ready For

| They ask | You answer |
|---|---|
| "The platform fee is a lot of fixed cost for us right now." | Compare it to the OSO build, not to zero: infrastructure, development, integrations, maintenance, PCI scope and the team, with no timeline that gets them to parity. And the 50/50 share means we only win when you win. Then hand to Justo for any structural discussion. Do not name a lower number. |
| "Can we do the workshop remotely instead?" | The value of the room is scoping the migration of the existing Velocity book and sequencing the first joint deal, which is hard over video. If travel is the blocker, offer **London** instead of Dallas. Andrew is there and Patrick travels there. |
| "How does our existing merchant base move over without disruption?" | Keep your front end. We map your API fields to ours and normalize through to the integrations. On the comparable account Jarrett and Mauricio are running, the end merchants do not know they were converted. |
| "Can I get the transaction data into my own models?" (Patrick) | Full lifecycle: inbound transaction data, the exact payload sent to each provider, the provider response and latency, by API or scheduled report. Routing is controllable by API in real time, and merchants can also change their own routes in the dashboard. Put a dedicated block on the workshop agenda for this. |
| "What if a provider we need is missing?" | We build it. Net-new integrations in under a week, four hours with working credentials, dedicated team, no separate integration fee. The proposal commits to delivery on anything missing. |
| "Who carries PCI?" | Yuno carries PCI DSS Level 1 with the vault, tokenization, 3DS authentication and fraud orchestration inside the white label. |

**Landmines**
- Never say or imply that CellPoint's orchestration is behind, broken or losing. The frame is facelift and speed to market, partner to partner.
- Jarrett can speak from his time inside CellPoint. German should not repeat that insider commentary.
- Do not mention that we can see when they open the proposal.
- Do not name a discount, a revised fee or a new structure without Justo saying it.

---

## 5. Agenda (30 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 3 | Warm open, acknowledge the travel change, reframe: this call is to lock the workshop date and agenda | Notes: ____ |
| 3 to 10 | **Workshop date.** Put the week of September 14 to 18 on the table and ask for a day. If travel is still the blocker, offer London as the venue | Notes: ____ |
| 10 to 20 | **The proposal.** Ask directly how it landed, who has seen it internally, and what needs to change for it to move. Listen, do not defend | Notes: ____ |
| 20 to 27 | **Workshop agenda.** Agree the blocks: migration of the existing Velocity book, Patrick's data and intelligence layer, integration process, first joint deal, commercial close-out | Notes: ____ |
| 27 to 30 | Recap, confirm who else joins from their side, confirm next step and owner | Notes: ____ |

---

## 6. Questions to Ask

1. When we sent the proposal on the 11th we asked for your feedback. How did it land, and who on your side has been through it? **Notes: ____**
2. What has to be true internally for this to get a yes, and who signs it? **Notes: ____**
3. The week of September 14 to 18, which day works? And if travel is still difficult, would London be easier than Dallas for both of you? **Notes: ____**
4. Beyond the two of you, who needs to be in the workshop room, particularly on product and engineering? **Notes: ____**
5. Patrick, for the workshop: which parts of your intelligence layer are already built, and which would you want Yuno to feed rather than replace? **Notes: ____**
6. If we started the migration, which merchants or which part of the Velocity book would you move first, and what does that timeline look like on your side? **Notes: ____**
7. Is there anything in the commercial structure, as opposed to the technology, that is the sticking point? **Notes: ____**

---

## 7. Post-Meeting

- Same-day recap email confirming the workshop date, the venue and the agreed agenda blocks.
- If the fee was challenged, brief Justo the same day before anything is put in writing.
- Log the outcome and update memory: workshop date, proposal status, any new names on their side.

---

### Sources
Google Calendar (event `CellPoint Digital + Yuno | Workshop Alignment`, Sep 1, 2026) · Gmail threads "Follow up" and "CellPoint Digital + Yuno: Dallas Workshop, September 4" (Jul 27 to Aug 27, 2026) · Papermark view notifications (Aug 12 and Aug 31, 2026) · Google Meet transcript, "CellPoint Digital + Yuno", Aug 11, 2026 · `Proposal - CellPoint Digital + Yuno.pdf` (commercial terms read directly from the file sent).
