# Internal Sync Brief: Hostinger demo prep

**Tuesday, September 15, 2026 · 10:45 to 11:00 COT (17:45 Warsaw, 17:45 Amsterdam) · 15 min**
**Meet:** https://meet.google.com/hsw-brha-hdv
**Event:** "Sync before Hostinger" (organizer: Piotr Sierpinski; attendees Piotr, Dirk van der Meulen, German)
**Prepares:** "Hostinger + Yuno | Demo", Thursday September 17, 06:00 to 06:45 COT (14:00 Vilnius). Paulius Lapenas accepted. Yuno invitees: Justo, Antoine Cathelin, Dirk, Piotr, Tautvydas (TJ).

**Objective:** leave the 15 minutes with (1) a demo plan for Thursday with a named owner per block, (2) clarity on who owns the account and who speaks to Paulius, and (3) the status of every commitment Yuno made on September 3, with a chaser assigned for each.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed · 🔍 to settle in the sync

### ⚠️ Pre-sync actions
1. **Send the Hostinger recap and NDA email today.** The September 3 follow-up never left Gmail. Paulius has the demo invite and nothing else: no recap, no Yuno entity, no signatory. The draft is in Gmail ("Hostinger + Yuno: Call Recap and Next Steps", to Paulius, cc Justo). Piotr and Dirk should hear from you that it went out on the 14th, not on the 3rd, before they hear it from Paulius.
2. **Accept Piotr's invite.** You are still "needsAction" on the sync (he moved it from 10:30 to 10:45 so it clears Palco).
3. **Justo is not in the sync but owns three of the five open commitments.** Bring the list and agree in the room who chases him.
4. **Ask Dirk before the sync whether the retry-timing check is done** (he committed on Sep 3 to confirm that Yuno's retry intelligence operates inside Hostinger's dunning window). It is the one technical claim Paulius said would make or break the subscriptions story.
5. **Tautvydas (TJ) is on Thursday's invite.** Slack lists him as Engineering Management Consultant. 🔍 Ask Piotr what his role on this account is and whether he presents.

---

## 1. Where the deal stands

| Date | What happened | Source |
|---|---|---|
| Before 2026 | Prior Yuno evaluation that did not convert. German, May 6: "your experience with Yuno will be very different this time." Never raise it | Gmail ✅ |
| Apr 29, 2026 | Met in person at Stripe Sessions SF (Juan Pablo Ortega, Justo, German, Paulius). India opened the door | Calendar ✅ |
| Jul 7, 2026 | Paulius: Q3 closed, "as readiness for Q4 maybe we could revisit this somewhere in August or early September" | Gmail ✅ |
| Jul 2026 | Piotr was "discussing Europe and APAC with them in July" at European events | Slack DM ✅ |
| Aug 6, 2026 | Yuno returns the RFP answers ("Questions to orchestrators", 17 sections) | Gmail ✅ |
| Sep 3, 2026 | Debrief call, 45 min: German, Justo, Antoine, Dirk with Paulius alone. Transcript in Deals/Hostinger | Transcript ✅ |
| Sep 3, 2026 | Slack group "Hostinger" (Justo, Antoine, Dirk, German). Dirk: "they ARE interested in our orchestration capabilities, not just our standalone products right?" German: "conversation did move around vaulting mainly but we should give him a demo on everything as in the questionnaire he did mention routing and fallback logic." Plan was to be made at the Cancún offsite | Slack ✅ |
| Sep 3, 2026 | Piotr DM: "congrats on progress with Hostinger. They are my old merchant from Braintree times. Actually worked with Paulius and Mindaugas a lot in the past. I didn't have any opp in SF since we've been meeting each other on events in Europe and they been always saying they are happy with current Provider." | Slack ✅ |
| Sep 3, 2026 | #piotr-salesforce: Piotr had an opportunity on account 001Ps00000a47hL and flagged "German opened opp for the same merchant" | Slack ✅ |
| Sep 3, 2026 | Ivvy Soberay (legal) provides NDA entity and signatory in #salesops-legal | Slack ✅ |
| Sep 9, 2026 | Salesforce: opportunity "Hostinger-" transferred to German | Gmail ✅ |
| Sep 3 to 14 | No email to Paulius. The recap and NDA details were drafted on the 3rd and never sent | Gmail ✅ |
| Sep 14, 2026 | Recap and NDA email drafted again, pending send | Gmail draft |
| Sep 15, 2026 | This sync | |
| Sep 17, 2026 | Demo with Paulius, 06:00 COT | Calendar ✅ |

### What Paulius said he wants (his words, September 3)

- **Vault standalone, for business continuity.** "Most likely, the interest would be to better understand the vaulting part as a standalone service... the main concern is our business continuity as... 60 percent or 70 percent of our money comes from subscription payments." He wants to own the tokens and keep charging if "the orchestrator goes down."
- **Modular, not a bundle.** His first question was whether Yuno's blocks (proxy, vault, orchestration) can be used separately. Justo and Antoine said yes: 3DS, network tokens, account updater, vault, subscriptions, reconciliation, all standalone.
- **Decision this year, plan next year.** "It would be good to finalize this year and then just have already a plan at least for next year."
- **India as its own topic.** Direct integrations with Razorpay and BillDesk, cross-border, roughly 70% UPI / 30% cards, two different customer journeys. Wants one integration and clarity on UPI token portability.
- **Subscriptions constraint.** Billing on Chargebee, migrating in-house gradually. Dunning: up to 5 retries in 21 days. Yuno may move an attempt inside the window ("Thursday to Friday is okay") but never delay it ("delay for one week... no use").
- **Agentic.** Prioritizes stablecoin protocols (x402, Cloudflare wallet, MPP) over card rails; talking to Stripe on specs; open question on billing micro-payments. Antoine asked for his merchant-side feedback.
- **NDA on Hostinger's paper.** He asked for entity name and signatory by email.

### Dirk's question, answered for the sync

Paulius is buying the vault first. The RFP (sections 5, 6, 7) asked about fallbacks, routing and webhooks in detail, and he already runs a third-party orchestration layer for card subscriptions with PSP fallbacks (unnamed). So the position on Thursday is: **vault standalone is the product, orchestration is the reason it is safer to buy from Yuno than from a vault-only vendor.** Justo said it on the call: connectors already plugged in and running volume, 24/7 NOC, regions in US, EU, APAC, KSA and India, "a few clicks away" from enabling a connection. Show orchestration as what the vault plugs into, not as a second pitch.

---

## 2. Account ownership: the Piotr conversation

Facts to have straight before you talk about it:

- Piotr Sierpinski is **Sales Manager Europe** (Warsaw). Hostinger was his merchant at Braintree. He knows Paulius and a **Mindaugas** at Hostinger personally. ⚠️ Mindaugas's role is unverified: LinkedIn shows a Mindaugas Barzdenis (Hostinger International, Kaunas) and a Mindaugas Krasauskas (Hostinger, Lithuania), neither with a visible payments title.
- Piotr had no Salesforce opportunity because "they been always saying they are happy with current Provider," but he did discuss Europe and APAC with them in July 2026.
- On September 3 he raised the duplicate-opportunity problem with Felipe Triboni. On September 9 Salesforce transferred the "Hostinger-" opportunity to German. ⚠️ Whether that resolved Piotr's opportunity or simply moved one of the two is not visible.
- Piotr's tone in the DM is collaborative ("congrats", "LMK how it goes", handshake). He organized this sync. Treat him as an asset, not a threat.

🔍 What to settle in the sync (2 to 3 minutes, not more):
1. Owner of record is German per the September 9 transfer. Confirm Piotr sees it the same way.
2. Piotr's role: European relationship, in-person coverage at events and in Vilnius, history with Paulius, and the Europe/APAC thread he opened in July. Propose he joins Thursday as the person who has known them for years.
3. Single voice to Paulius: German sends all written follow-ups, Piotr cc'd. No parallel threads.
4. Credit split, if any, is a Sean and Justo decision. Do not negotiate it in a 15-minute prep call; just agree to raise it with them.

🔍 What to extract from Piotr (he knows things no research can find):
- Who is Mindaugas and does he decide anything today?
- Which orchestrator do they use for card subscriptions? (Paulius refused to name it.)
- What did "Europe and APAC" mean in July: which providers, which countries, which pains?
- Is Gediminas Griška (named as Head of Payments in a public ProcessOut interview) still there, and does he sit above, beside or below Paulius?
- Anything on pricing expectations from the Braintree days.
- Why they said "happy with current provider" for years and what changed (⚠️ the research answer is that ProcessOut went to Checkout.com and Credorax/Finaro went to Shift4; Piotr may confirm or correct this).

---

## 3. Commitments made on September 3 and their status

| Commitment | Owner | Status as of Sep 14 | Chaser 🔍 |
|---|---|---|---|
| Recap email with NDA entity and signatory | German | Drafted Sep 3, never sent. New draft Sep 14, send today | German |
| Schedule the deep dive | German | Done, Sep 17 06:00 COT, Paulius accepted Sep 4 | |
| Full vault standalone material ("the full breadth and depth") | Justo | Nothing visible in German's mailbox or Slack | 🔍 |
| India status: UPI token portability mandate, where Razorpay and BillDesk stand, via the local GM | Justo | Nothing visible. Justo asserted on the call that the mandate exists and Razorpay "had it for this year." Verify before repeating in writing | 🔍 |
| Revolut Pay intelligence and Mastercard funded-card notification info | Justo | Nothing visible. Paulius pushed back that Revolut is small for them; low priority | 🔍 |
| Confirm retry intelligence operates inside their dunning schedule | Dirk | Unknown, ask before the sync | Dirk |
| NDA on Hostinger's paper | Paulius (needs our data first) | Blocked on our email since Sep 3 | German |

---

## 4. Thursday demo plan: what Paulius will test

He is a practitioner who has been oversold before and who wrote RFP question 3.6 ("token enrollment is far from 100%") to catch overclaiming. Every block below should show a real flow in the dashboard or the API, with the limit stated before he asks for it.

| Min | Block | Show | Say | Do not say | Owner 🔍 | RFP link |
|---|---|---|---|---|---|---|
| 0 to 5 | Open | Nothing | NDA status, what he read since the 3rd, confirm the three topics he asked for (vault, subscriptions, India) | The prior evaluation | German | |
| 5 to 20 | **Vault standalone** | One vaulted card charged through two of his providers (Stripe and Adyen test connections). Token import with network transaction IDs. PCI proxy call with the `{{vaulted_token.<TOKEN>.network_transaction_id}}` placeholder. Export path if he leaves. User permissions on PAN visibility | "The vault is the product. The connectors are why it is safe: if a layer goes down you charge from the vault through any of these." Regions and NOC | "Migration is trivial." Bulk backfill outside a migration is handled with the Yuno team, not self-serve (2.3) | Dirk | 2.3, 2.4, 3.4, 9.1 to 9.3 |
| 20 to 30 | **Network tokens, account updater, the matrices** | Enrollment with Yuno's TRID or their own (3.2, 3.3). Token type selection at payment time: network token plus cryptogram where accepted, vaulted PAN where not (3.6). Hand over the matrices for network transaction ID acceptance (2.1), network token acceptance (3.5) and wallet-token MITs (13.3) scoped to Stripe, Adyen, Checkout.com, Razorpay, BillDesk | Card-on-file drives 60 to 70% of revenue; renewals at 3.5 to 4x the intro price make every declined renewal a large event | Amex on account updater (10.1 is Visa and Mastercard only). A generic "we support everything" list | Dirk + German | 2.1, 3.1 to 3.9, 10.1 to 10.3, 13.3 |
| 30 to 38 | **Routing, fallbacks, retries** | A routing rule by country and BIN, a Monitor that redirects traffic when approval drops, fallback on provider error, the retry-timing model | "We move the attempt inside your dunning window, we never delay your cycle" (only if Dirk confirmed it). Batch renewals spread so PSP fraud rules stop flagging them | Unlimited retries (production cap is 5, 11.2). Webhook delivery logs in the payments screen (7.1 is a no) | Dirk | 5.1, 5.2, 6.1 to 6.3, 7.1, 11.2 |
| 38 to 43 | **India** | Razorpay and BillDesk behind one integration, one journey, UPI Autopay for recurring | Token portability status only if verified with the India GM | "The mandate is live" without a source | Justo or India GM; Piotr on the APAC thread | |
| 43 to 45 | **Close** | Nothing | The ask (section 6) with a date | | German | |

**Subscriptions engine:** two minutes at most, only if he asks. He is building billing in-house. The line is "you keep the schedule, we execute the charge and pick the moment inside your window." Do not pitch replacing Chargebee.

**Agentic (Antoine):** MPP and x402 design update only if Paulius raises it. He asked to be kept posted, not demoed.

### Environment checklist for Dirk 🔍
- Sandbox account with Stripe, Adyen and Checkout.com test connections (his named providers).
- A vaulted card with a network transaction ID stored, and the same card charged on two connections.
- One routing rule with a BIN or country condition, one fallback, one Monitor with a threshold.
- A PCI proxy request ready to run, showing the redaction header.
- A report with `network_transaction_id`, `network_token` and `merchant_order_id` columns (answers 2.4 and 4.3 live).
- The subscriptions demo account used on Sep 3, in case he asks.
- The three matrices as documents he can keep.

---

## 5. RFP soft answers to close on Thursday

Six answers defer to "on request" or "confirm with your account team." In a written comparison across orchestrators they read as one thing: less specific on paper. Closing them in the room turns the weakest column into the most tailored one.

| RFP | The soft spot | What to bring | Owner 🔍 |
|---|---|---|---|
| 2.1 | PSP support for network transaction ID "on request" | Matrix scoped to Stripe, Adyen, Checkout.com, Razorpay, BillDesk | |
| 2.4 | Token database health "on request" | Offer to run it once during evaluation and then at every account review | |
| 3.5 | Network token acceptance "scoped during solution design" | Same matrix | |
| 4.4 | Data warehouse connectors "confirm with account team" (weakest answer) | A real answer: Reporting API plus which connectors exist, if any. They have a BI team | |
| 6.3 | Routing version control "confirm with account team" | Show audit logs live in the dashboard | |
| 13.3 | Wallet-token MITs "validated per provider" | Same matrix, wallet column | |

Other limits to state before he asks: account updater is Visa and Mastercard only; subscriptions cover cards only (PayPal recurring runs on billing agreements, section 12); retries cap at 5 in production; scheme registration for account updater takes up to 10 working days; no backend SDKs by design (an internal draft claimed Kotlin, Java and Node and was corrected; never resurrect it); pinless debit is an acquirer capability Yuno routes into, not a Yuno switch.

---

## 6. Commercial: the ask and the pricing posture

Paulius set the timeline: decide this year, execute next year. Thursday needs to end with a next step that fits that, and the sync should pick which one:

| Option | What it is | Pro | Con |
|---|---|---|---|
| A. Commercial proposal for vault standalone plus India | A written offer after the demo | Matches "decision this year" | Vault standalone pricing is not in the deal calculator; needs Justo. Network tokens exist in the calculator as reference only (creation $0.2973, update $0.0595 in the Palco mid-margin run; never quote those numbers) |
| B. Scoped PoC | Migrate a token sample, measure network transaction ID coverage, run a fallback drill | Proves the exact thing he fears | Needs engineering time on both sides and an NDA first |
| C. Technical session with hPayments engineers | Their integration team plus Dirk | Cheap, moves the evaluation from Paulius alone to his team | Does not by itself produce a decision |

Recommendation for the sync: **C on the call, A in parallel.** Ask Paulius on Thursday for the engineering session and tell him the proposal follows within a week. 🔍 Confirm with Piotr and Dirk, and get Justo to own the vault standalone pricing.

**Competitive frame, once and plainly:** the RFP is titled "Questions to orchestrators", plural. Hostinger's earlier optimization partner (ProcessOut) was bought by Checkout.com in 2020 and its acquirer (Credorax/Finaro) by Shift4 in 2022; both are now inside PSPs Hostinger uses or competes against. Yuno's independence from any PSP is the argument. Do not name ProcessOut, Credorax or the current orchestrator on the call. If Paulius brings up his own history, make the point once and move on.

---

## 7. Landmines (consolidated)

- Never say Hostinger "lacks" orchestration. Paulius built the stack and runs a third-party layer today.
- Do not raise the prior Yuno evaluation.
- Do not claim Amex on account updater, backend SDKs, unlimited retries, or webhook delivery logs in the payments screen.
- Do not repeat the UPI token portability mandate as fact in writing until the India GM confirms wording and dates.
- Do not name other orchestrators, ProcessOut, Credorax, Finaro or Shift4 as talking points.
- Do not improvise a price. Platform fee plus a fee on successful transactions is the structure; numbers need volume and Justo.
- Do not run two email threads to Paulius (German writes, Piotr cc'd).

---

## 8. Sync agenda (15 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 3 | Ownership and history: confirm German as owner of record, Piotr's role Thursday, what Piotr knows (Mindaugas, current orchestrator, the July Europe/APAC thread) | Notes: ____ |
| 3 to 8 | Demo plan: walk the six blocks in section 4, assign owners, agree the environment checklist and who builds the three matrices | Notes: ____ |
| 8 to 11 | Open commitments: who chases Justo for the vault material and India status; Dirk's retry-timing answer; NDA email going out today | Notes: ____ |
| 11 to 13 | The ask for Thursday (option C plus A) and who owns vault standalone pricing | Notes: ____ |
| 13 to 15 | Logistics: Tautvydas's role, whether Antoine presents agentic, whether to invite Paulius's engineers, Piotr joining Thursday | Notes: ____ |

---

## 9. Open questions

**For Piotr**
1. Who is Mindaugas at Hostinger, and is he part of this decision? Notes: ____
2. Which orchestration layer runs their card subscriptions today? Notes: ____
3. What exactly did you discuss with them in July on Europe and APAC, and with whom? Notes: ____
4. Is Gediminas Griška still Head of Payments, and how does he relate to Paulius? Notes: ____
5. Does your Salesforce opportunity still exist after the September 9 transfer, and how do we want to record ownership? Notes: ____
6. Will you join Thursday, and do you want to open with the relationship history? Notes: ____
7. What is Tautvydas's role on this account? Notes: ____

**For Dirk**
8. Is the retry-timing confirmation done: can the model move an attempt inside a 21-day, 5-retry dunning window without ever delaying the cycle? Notes: ____
9. Can you build the sandbox with Stripe, Adyen and Checkout.com test connections and a vaulted card charged on two of them by Wednesday? Notes: ____
10. Who produces the three matrices (2.1, 3.5, 13.3) scoped to their providers, and by when? Notes: ____
11. What is the real answer on data warehouse connectors (4.4) and on routing audit trail (6.3)? Notes: ____
12. Token export if they leave: what does the process look like, and can you say it in one sentence on Thursday? Notes: ____

**For both**
13. Which ask do we make on Thursday: engineering session, proposal, PoC, or a combination? Notes: ____
14. Who takes the India block if the local GM is not on the call? Notes: ____
15. Does Justo know his three deliverables are still open? Who tells him today? Notes: ____

---

## 10. Post-sync checklist

- Send the recap and NDA email to Paulius (cc Justo) immediately after the sync if not done before.
- Message Justo with the three open deliverables and Thursday's block assignments.
- Confirm with Dirk the sandbox build and the matrices by Wednesday end of day.
- Update the demo invite description with the agreed agenda so Paulius sees the three topics he asked for.
- Log in Salesforce: ownership agreed, next step, close date consistent with "decision this year."
- Update memory: Piotr's role, Mindaugas, current orchestrator if Piotr knows it, demo owners.

### Sources
Google Calendar (events "Sync before Hostinger" Sep 15 and "Hostinger + Yuno | Demo" Sep 17, 2026) · Gmail (thread "Hostinger + Yuno at Stripe Sessions" Apr to Jun 2026; calendar acceptances Sep 4 and Sep 9; Salesforce transfer notice Sep 9; drafts folder and sent folder checks Sep 14) · Deals/Hostinger/hostinger-call-transcript-2026-09-03.md · Deals/Hostinger/Yuno-RFP-Response-Hostinger-Aug2026.md · data/research/hostinger-meeting-brief-2026-09-03.md · Slack: DM with Piotr Sierpinski (Sep 3), #piotr-salesforce (Sep 3), group DM "Hostinger" (Sep 3), #salesops-legal thread "NDA - Hostinger" (Sep 3), Slack user directory (Piotr, TJ, Carlos Medina) · LinkedIn search results for Mindaugas at Hostinger (unverified) · ProcessOut blog interview with Gediminas Griška.
