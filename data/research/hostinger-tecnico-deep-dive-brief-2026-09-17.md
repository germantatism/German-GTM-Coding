# Técnico Deep Dive Brief: Hostinger

**Thursday, September 17, 2026 · 06:00 to 06:45 COT · 14:00 Vilnius · 13:00 Amsterdam and Warsaw · 45 min**
**Meet:** https://meet.google.com/uri-otwr-mua · Event "Hostinger + Yuno | Demo" (organizer: German)
**Hostinger:** Paulius Lapenas, Head of Payments (accepted Sep 4).
**Yuno:** German (lead, discovery, close) · Dirk Van Der Meulen (demo, accepted) · Piotr Sierpinski (relationship, accepted) · Tautvydas "TJ" (local presence, 10 min, pending) · Justo (India and commercial, pending) · Antoine Cathelin (declined Sep 15).

**Purpose:** internal alignment on what we present, what we focus on and how we run it. Built from the Sep 3 call transcript, the RFP answers, the Sep 2 and Sep 15 internal syncs, Gmail and docs.y.uno. Deeper material: [Sep 3 meeting brief](https://docs.google.com/document/d/1CqI5ig5Z-K4iE0uPrLol6-aab49BRiIPh89Tu8YYYCU/edit), [Sep 15 sync brief](https://docs.google.com/document/d/1dawyrxuyxnN3lGYGnIYzfEeGHq6GqMKUyZPpDKAejPI/edit), [Sep 3 call in Gong](https://app.gong.io/call?id=8546116675641297982).

Labels: ✅ verified · ⚠️ unverified, roadmap or internal only · 🔍 open, needs an owner

---

## 1. TL;DR

- **What Paulius is buying: the vault as a standalone service, for business continuity.** His words on Sep 3: 60 to 70% of revenue is subscription payments; he wants to own the tokens and keep charging if the orchestration layer goes down. Decision this year, execution plan next year.
- **What decides Thursday: precision.** He is a practitioner who has been oversold before (including by Yuno, in a prior evaluation that we never bring up). RFP question 3.6 exists to catch overclaiming. Every claim gets a live proof or a stated limit.
- **Format: not a from-scratch demo.** Piotr's read, and he knows them: no time for an interactive tour, focus on a few big points. Four proof points in the dashboard or API, then India in five minutes with verified facts only.
- **Position: the vault is the product, orchestration is the reason it is safer to buy from Yuno.** Connectors already running volume, regions, 24/7 NOC. Never "you lack orchestration": Paulius built the stack and runs a third-party layer today.
- **The ask: a working session with his engineers plus a written proposal (vault standalone and India) within a week.** Pricing is not improvised in the room; Justo owns it.

---

## 2. What has been discussed so far

| Date | What happened | Source |
|---|---|---|
| Apr 29 | Met in person at Stripe Sessions SF (Juan Pablo Ortega, Justo, German, Paulius). India opened the door | Calendar ✅ |
| Jul 7 | Paulius: Q3 closed, "readiness for Q4", revisit in August or early September. Questionnaire sent Jul 8 | Gmail ✅ |
| Aug 6 | RFP answers returned. 17 sections, titled "Questions to orchestrators" (plural: we are being compared in writing) | Gmail ✅ |
| Sep 3 | 45 min debrief call. Paulius alone; German, Justo, Antoine, Dirk | Transcript ✅ |
| Sep 3 | Recap sent the same day with the NDA entity and signatory, cc Justo, Antoine, Dirk | Gmail ✅ |
| Sep 9 | NDA reminder sent. No email reply from Paulius since Jul 8; he accepted the Sep 17 invite on Sep 4 | Gmail ✅ |
| Sep 15 | Internal sync German, Piotr, Dirk (15 min) | Transcript ✅ |

### What Paulius told us on Sep 3 (his words, paraphrased where noted)

- **Modular first.** His opening question: can the blocks (PCI proxy, vault, orchestration) be used separately or only as a bundle? Justo and Antoine: yes, all standalone (3DS, network tokens, account updater, vault, subscriptions, reconciliation).
- **Business continuity is the priority.** "We still continue to look into the business redundancy problem and how we can be the owners of all the tokens we have, so we could continue our subscription business in case the orchestrator goes down."
- **Timing.** "It would be good to finalize this year and then have a plan at least for next year."
- **Current setup.** Card subscriptions run through a third-party orchestration layer with real-time fallbacks between PSPs and retry rules set there. Recurring APMs (PayTM and other India and LatAm methods) are direct integrations with no fallback. Billing engine is Chargebee: dunning is up to 5 retries in 21 days, then a manual renewal flow. Billing is moving in-house gradually.
- **Chargebee pain.** It only controls the gap between retries. No time-of-day or day-of-month logic; customers get charged at the hour they first purchased, even in the middle of the night. Batches of renewals trigger fraud rules at the PSPs ("tens of thousands of requests in a short period"), and he cannot explain that to issuers.
- **The retry constraint, verbatim.** "If I send you a request today, Thursday, my next request will come on Saturday. If your intelligence tells that don't charge on Thursday but attempt on Friday, that's okay with me because it will not impact my dunning. But if your intelligence will say delay for one week, then for us it's no use."
- **Issuer-specific logic is not wanted.** On Revolut Pay signals: "I really don't want them to be building some logical flow just for a single issuer." He wants one approach that covers all subscriptions, not five logics.
- **India as its own topic.** Direct integrations with Razorpay and BillDesk, cross-border, roughly 70% UPI and 30% cards, two different customer journeys. Wants one integration and clarity on whether tokens can move between providers ("as far as I know the central bank does not allow it, but I'm not fully sure").
- **Agentic.** Prioritizes stablecoin protocols (x402, Cloudflare wallet, MPP) over card rails for service businesses; already talking to Stripe on specs; open question on how to invoice micro-payments. Wants to be kept posted, not demoed.
- **NDA on Hostinger's paper.** Asked for entity and signatory by email (sent Sep 3).

### What Piotr added on Sep 15

- He was Hostinger's account manager at Braintree and PayPal for years and sold them Braintree through ProcessOut. He knows Paulius well.
- History: talks with the previous Europe GM (Miguel) early in 2025 went nowhere; Piotr's messages in June 2025 went unanswered. At MPE Berlin (end of March 2026) they told him: "we are so happy with ProcessOut, we are not shopping for any solution, but if you can help us establish connections in India, let's talk." ✅ **ProcessOut (Checkout.com) is the third-party layer Paulius did not name.**
- His read: ProcessOut is strong in Europe and the US and likely weaker in APAC. India is the wedge.
- As a Hostinger customer: everything is tokenized and auto-renewal is effectively forced, including domains, charged to card or PayPal.
- On Thursday he stays silent unless history helps. He invited TJ because a Yuno engineer based in Vilnius matters to a Lithuanian merchant ("it's really important for them to have somebody local"). ⚠️ Piotr calls TJ VP of Engineering; the Slack directory says Engineering Management Consultant. 🔍 Confirm the title before we introduce him.
- Dirk's question stayed open: **"there's a reason they're looking for alternatives, what are those reasons?"** We have never asked. It goes in the first five minutes.

### Their stack as we know it

| Layer | What we know | Source |
|---|---|---|
| PSPs | Stripe, Adyen, Checkout.com, local providers in APAC and LatAm | Paulius ✅ |
| India | Razorpay and BillDesk, direct, cross-border, ~70% UPI / 30% cards | Paulius ✅ |
| Orchestration | Third-party layer for card subscriptions with PSP fallbacks (Paulius). ProcessOut, as of March 2026 (Piotr) | ✅ |
| Billing | Chargebee, migrating in-house gradually; 5 retries in 21 days | Paulius ✅ |
| Wallets and APMs | PayPal, Apple Pay, Google Pay; Revolut Pay launched recently (small); PayTM, LatAm and India APMs direct | Paulius ✅ |
| Payments org | Product-side "hPayments" technical team plus a strategy team (PSP relationships, fraud and disputes) | Public interview ⚠️ |
| Checkout observed Sep 2 | Netherlands: cards, PayPal, Google Pay, Apple Pay, CoinGate, Alipay HK and CN, no iDEAL. Colombia: PayPal, Google Pay, Apple Pay, Nequi | Antoine and German ✅ |

---

## 3. What they care about, in priority order

Ranked by weight in the RFP plus what Paulius chose to spend the call on.

| # | Topic | Evidence | What "good" looks like on Thursday |
|---|---|---|---|
| 1 | **Vault standalone for business continuity**: own the tokens, charge through any PSP, migrate in without losing data, export if they leave | Call: his stated interest and the only thing he asked to go deeper on. RFP 2.3, 2.4, 3.4, 9.1 to 9.3 | One vaulted card charged through two of his providers. Import with network transaction IDs. PCI proxy placeholder. Export path in one sentence. Permissions on PAN visibility |
| 2 | **Renewal authorization: network tokens, network transaction IDs, account updater** | Roughly half the RFP (sections 2, 3, 10, 11). Renewals price at 2x to 5x the intro price, so a declined renewal is the most expensive event in their model | Enrollment with their TRID or ours. Token-type selection per provider at payment time (3.6). Matrices for network transaction ID, network token and wallet MIT acceptance scoped to Stripe, Adyen, Checkout.com, Razorpay, BillDesk. Limits stated first |
| 3 | **Retries that respect his dunning schedule**, and renewal batches that stop tripping PSP fraud rules | Call: the Chargebee pain and the verbatim constraint. RFP 11.1, 11.2 | A clear statement of what happens to a charge his billing engine sends us: real-time fallback across PSPs on the same request, and where time-shifting applies (see section 5) |
| 4 | **India as one integration** over Razorpay and BillDesk, one journey, UPI recurring, and where token or mandate portability stands | Call. The topic that opened the door in April and the reason they answered Piotr in March | Razorpay and BillDesk behind one integration. Portability status stated only as verified. Owner named for the follow-up |
| 5 | **Routing, fallback, Monitors, operational safety** | RFP 5, 6, 7 (validation against user error, version control, webhook visibility). Table stakes: he runs this today | One rule, one fallback, one Monitor, the audit log. Say plainly what is not there (webhook delivery logs in the payment screen) |
| 6 | **Data and BI**: order-level approval rate, data warehouse export | RFP 4.3, 4.4. They have a BI team; 4.4 was our weakest written answer | A real answer on export and connectors. Report columns shown live |
| 7 | Secondary RFP items: PayPal billing agreements (12), Apple Pay MPAN (13.4), pinless debit (8), co-badged cards (18) | RFP only, not raised on the call | Answer if asked, with the limit first |
| 8 | Agentic payments (MPP, x402) | Call, early stage, "keep us posted" | One sentence: Antoine is designing the MPP integration and asked for his merchant feedback; separate session |

---

## 4. How to approach it

**4.1 Positioning.** Vault standalone is the product. Orchestration is why it is safer with us than with a vault-only vendor: the connectors are already plugged in and running volume, regions in the US, EU, APAC, KSA and India, 24/7 NOC (as Justo said on the call). Show orchestration as what the vault plugs into, never as a second pitch. The independence argument (a layer bought by a PSP stops being independent) is made once and only if Paulius brings up ProcessOut or Checkout.com himself. We never name ProcessOut, Credorax, Finaro or Shift4.

**4.2 Four proof points, each live.** No slides between them.

| Proof point | Show | Say | State the limit before he asks |
|---|---|---|---|
| A. One token, two PSPs | A vaulted card charged on Stripe and Adyen test connections; export path; user permissions on PAN visibility | "If a layer goes down, you charge from the vault through any of these" | Bulk backfill outside a migration is handled with the Yuno team, not a self-serve endpoint (2.3) |
| B. Migration keeps the data | Token import with network transaction IDs; PCI proxy request with the network transaction ID placeholder; report with network transaction ID, network token and merchant order ID columns | "Card data and network transaction IDs import together. Order-level approval rate comes straight from the report" | Vault health analysis (share of tokens with a network transaction ID) is run by our team, not a self-serve view; offer to run it during the evaluation (2.4) |
| C. Renewal authorization | Enrollment with their TRID or ours; token type chosen per provider at payment time; hand over the three matrices | "Enrollment below 100% never blocks a charge" (his 3.6 trap, answered honestly) | Account updater is Visa and Mastercard only; scheme registration up to 10 working days. Amex network tokens: see section 5 |
| D. Retries and routing | One routing rule by country or BIN, one fallback on provider error, one Monitor with a threshold, the audit log; retry strategy configuration | "Real-time fallback on every request your billing engine sends. Retry timing moves the attempt inside your window, never past it" (only what Dirk confirms, see section 5) | Production cap is 6 attempts (our written answer said 5; correct it). Webhook delivery logs are not in the payment screen (7.1) |

**4.3 India in five minutes, verified facts only.** Razorpay and BillDesk behind one integration and one journey. UPI recurring runs on UPI Autopay mandates. On portability: NPCI plans to make UPI Autopay mandates portable so merchants can move existing mandates when they change payment gateway or acquiring bank (Mint report, Aug 31, 2026; announcement expected at Global Fintech Fest). ⚠️ Planned, not live, no date. Say: "NPCI has announced plans for mandate portability; we are confirming the live date and Razorpay and BillDesk readiness through our India GM." Do not repeat "the mandate exists and players comply by year-end" as fact.

**4.4 Discovery in the first five minutes.** We have never asked why they are looking. Two questions before any demo: what triggered the business-continuity review this year, and if the orchestration layer went down for 48 hours today, what exactly stops. The second answer becomes the success criterion for proof point A.

**4.5 Roles.**

| Who | Does | Does not |
|---|---|---|
| German | Opens, runs discovery, keeps time, closes with the ask, sends every written follow-up (Piotr cc'd) | Improvise pricing |
| Dirk | Proof points A to D in the sandbox; the three matrices; the retry-timing answer | Claim anything not built |
| Piotr | Relationship, one line of history at the open if useful, listens for what Paulius does not say | Run a parallel thread with Paulius |
| TJ | Joins at the open for a short hello: Yuno engineering, based in Vilnius | Stay past 10 minutes |
| Justo (if he joins) | India status and the commercial frame at the close | |
| Antoine (declined) | Agentic is not on the agenda; if Paulius raises it, German offers a separate session | |

**4.6 The ask and the commercial posture.** Ask Paulius for a working session with his hPayments engineers (Dirk plus their integration team) and tell him a written proposal for vault standalone and India follows within a week. Pricing structure is platform fee plus a fee on successful transactions; numbers need volume and Justo. ⚠️ Vault standalone pricing is not in the deal calculator; Justo has to own it before the proposal goes out.

---

## 5. Facts to have straight

| Topic | Say | Do not say | Status |
|---|---|---|---|
| Retry strategies (subscriptions engine) | Three per plan: DEFAULT fixed schedule (5h, 12h, 24h, 36h, 48h, 96h), SMART (ML timing on decline reason, country, issuer, provider), CUSTOM_SCHEDULE (per-attempt delay from seconds to 7 days). Stop on hard decline. A/B split | "Unlimited retries", "5 in production" | docs.y.uno ✅ (cap is 6 in production) |
| Retry timing for charges his own billing engine sends | 🔍 Dirk confirms before Thursday: does SMART or CUSTOM_SCHEDULE timing apply to merchant-scheduled MITs, or only to cycles the engine creates? Until then the safe line is: real-time fallback across PSPs on every request; time-shifted retries are a feature of our subscription engine that fits his in-house scheduler when he moves billing | "We pick the moment" for standalone charges without confirmation | 🔍 open |
| Subscriptions engine, payment methods | 🔍 Confirm with Product (Daniel Lozano) before stating. Our written RFP answer (Aug 6) said cards only; the Sep 2026 launch deck lists cards, Apple Pay, Google Pay, PayPal and Pix Automático live | "UPI Autopay inside the engine" (said on the Sep 3 call, not in the launch deck) | ⚠️ conflicting internal sources |
| Subscriptions engine, results | Externally: the published 7% uplift and 30% recovered revenue only | The internal launch deck numbers (16 merchants, 135K active subscriptions, 86% per cycle after retries) unless Product clears them for external use | ⚠️ internal only |
| Account updater | Visa and Mastercard; asynchronous; vaulted token and fingerprint stay stable; enrollment.update webhook; registration up to 10 working days | Amex | docs.y.uno ✅ |
| Network tokens | Visa and Mastercard live via Visa Token Service and Mastercard's network token API; TRID: theirs or ours | Amex live. Our RFP 3.1 answer lists Amex; Antoine (Sep 2): not true yet, months away with the scheme | ⚠️ correct if asked |
| Network transaction IDs | Stored per credential; merchant-supplied value accepted in the payment request; imported with card data in migration; injected by the PCI proxy placeholder | A self-serve bulk backfill endpoint | docs.y.uno ✅ |
| PCI proxy | Forward proxy through Yuno's PCI environment; placeholders for PAN, expiry, holder, network transaction ID; response redaction header; proxied calls are audited but are not payments in the payments list | Proxied calls appear as payments | docs.y.uno ✅ |
| Fallbacks and Monitors | Condition-based chains on decline, timeout or error; Monitors redirect traffic below an approval threshold and auto-recover; alerts by email and Opsgenie | | docs.y.uno ✅ |
| Webhooks | At-least-once, seven attempts out to 96 hours, HMAC and OAuth2, unified event model | Delivery logs visible in the payment screen | RFP ✅ (7.1 is a no) |
| Pinless debit | Acquirer capability; Yuno segments debit traffic and routes it to connections where it is enabled | A Yuno-side debit switch | RFP ✅ |
| Backend SDKs | REST API only, by design; Postman collection | Kotlin, Java or Node server SDKs | RFP ✅ |
| Data warehouse export (4.4) | 🔍 Real answer needed: Reporting API plus which connectors exist, if any | "Confirm with your account team" again | 🔍 open |
| India cards | RBI card-on-file tokens are issued by the networks and issuers, not by the acquirer, so a network token is not tied to Razorpay or BillDesk | | ⚠️ confirm with Product for the MIT flow on both |
| Interchange and scheme fee effect of network tokens and 3DS | ⚠️ Antoine quoted 5.5 bps (Mastercard) and 7.5 bps (Visa) reductions on Sep 2. Not verified against scheme bulletins; do not quote in writing | | ⚠️ |
| Infrastructure | Regions: two in the US, one EU, one APAC, KSA, India; 24/7 NOC | | Justo on the call ✅ |

---

## 6. Open items before Thursday

| Item | Owner | Status Sep 15 |
|---|---|---|
| Sandbox with Stripe, Adyen and Checkout.com test connections; one vaulted card with a network transaction ID charged on two of them; one routing rule, one fallback, one Monitor; a PCI proxy request ready; a report with the three columns | Dirk | 🔍 |
| The three matrices (network transaction ID 2.1, network token 3.5, wallet MIT 13.3) scoped to Stripe, Adyen, Checkout.com, Razorpay, BillDesk, as documents he can keep | Dirk with Solutions | 🔍 |
| Retry-timing answer for merchant-scheduled charges (section 5) | Dirk | 🔍 committed Sep 3, no answer visible |
| Subscription engine facts: payment methods live, and whether engine results can be quoted | German with Daniel Lozano | 🔍 |
| Data warehouse connectors (4.4) and routing audit trail (6.3) | Dirk | 🔍 |
| India: Razorpay and BillDesk readiness for UPI Autopay recurring and token migration; NPCI mandate portability live date | Justo via India GM; Dirk said he would look at India | 🔍 committed Sep 3, nothing sent |
| Vault standalone material "full breadth and depth" | Justo | 🔍 committed Sep 3, nothing sent. The demo can replace it if the proposal follows within a week |
| Revolut Pay and Mastercard funded-card notification info | Justo | Low priority: Paulius said Revolut is small for them |
| NDA on Hostinger's paper | Paulius | Unanswered since the Sep 9 reminder. Ask at the open |
| Piotr's notes from the March 2026 meeting in Berlin | Piotr | Promised Sep 15 |
| TJ's title and 10-minute slot; Justo's RSVP | Piotr, Justo | Both pending on the invite |
| Vault standalone pricing for the proposal | Justo | Not in the deal calculator |

---

## 7. Other things worth knowing

- **This is a re-engagement after a failed one.** Paulius told German at Stripe Sessions that the earlier Yuno contact (previous Europe GM and a BD) had terrible response times and never answered his questionnaire. Never raise it. If he does, acknowledge once and point at what is different: answers on paper, specifics in hand, one owner.
- **Competitive frame, once.** The RFP is addressed to orchestrators, plural. Their optimization partner (ProcessOut) was bought by Checkout.com in 2020 and their acquirer (Credorax, later Finaro) by Shift4 in 2022. Independence from any PSP is our argument. We do not name any of them.
- **Org context.** Paulius on Sep 3: "the overall organization is shifting priorities for the way we position ourselves in the market." New CEO since June 2026 with an AI-first mandate. Q4 is the window he set himself.
- **Local payment methods are a later thread, not Thursday.** The RFP has no payment-method questions, but the Sep 2 checkout check showed no iDEAL in the Netherlands and a thin Colombia mix. Keep it for after the vault decision.
- **Account ownership.** German is owner of record (Salesforce transfer Sep 9). Piotr supports with the relationship. One written voice to Paulius: German sends, Piotr in cc.
- **Ask the NDA question early.** He wanted it to share more of his data; without it, keep the session on our proof points and his stated numbers.

---

## 8. Run of show (45 minutes)

| Min | Block | Owner | Notes |
|---|---|---|---|
| 0 to 5 | Open. TJ and Piotr say hello (one line each). NDA status. What he reviewed since Sep 3. The two discovery questions (section 4.4) | German | Notes: ____ |
| 5 to 18 | Proof points A and B: one token through two PSPs; migration with network transaction IDs; PCI proxy; export; permissions | Dirk | Notes: ____ |
| 18 to 28 | Proof point C: network tokens, TRID, token-type selection, account updater. Hand over the matrices. Limits first | Dirk, German | Notes: ____ |
| 28 to 35 | Proof point D: routing rule, fallback, Monitor, audit log, retry strategies and the dunning-window answer | Dirk | Notes: ____ |
| 35 to 40 | India: one integration over Razorpay and BillDesk, UPI Autopay, portability status as verified | Justo or German, Dirk | Notes: ____ |
| 40 to 45 | Close: the working session with his engineers, the proposal date, who joins from his side | German | Notes: ____ |

If he asks for the subscription engine: two minutes at most. "You keep the schedule, we execute the charge, route the retry through a different PSP and pick the moment inside your window." Do not pitch replacing Chargebee.

---

## 9. Questions for Paulius

1. What triggered the business-continuity review this year, and what does "decide this year, plan next year" need to contain to get approved? Notes: ____
2. If the orchestration layer went down for 48 hours today, what exactly stops, and what would you need from a vault to keep charging? Notes: ____
3. Where do the tokens live today, how many are there, and what share carries a network transaction ID? Notes: ____
4. Network token enrollment today: coverage, and is the TRID yours or the provider's? Notes: ____
5. How much Amex card-on-file volume do you carry? Notes: ____
6. Which providers must be in the acceptance matrices beyond Stripe, Adyen, Checkout.com, Razorpay and BillDesk? Notes: ____
7. When billing moves in-house, will your scheduler send us each charge with a deadline, so retry timing can work inside the window? Notes: ____
8. India: what would "one integration" have to cover on day one (UPI Autopay, cards, mandates already live)? Notes: ____
9. Who else is part of this decision, and who from hPayments joins the engineering session? Notes: ____
10. Where is the NDA? Notes: ____
