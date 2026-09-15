# Meeting Brief: Yuno <> Appmaking, Proposal Inputs Call

**When:** to confirm. German offered "in a few hours" on Tuesday, September 15 or on Wednesday, September 16, 2026 (they are on EEST, Cyprus and Minsk, 8 hours ahead of Bogotá). Short call, 30 minutes.
**How:** phone or text first (German shared his number in the Meet chat), then the shared Slack channel Jarrett proposed.
**Who:** Tatsiana Hubarevich (Payment Manager; signs Gubarevich by email) and Dzmitry Katsiushchyk for Appmaking. German for Yuno; Jarrett Falasco and Joaquin Mann optional.
**Why this call exists:** on the September 15 call the proposal was not shown. German closed with "I'll get to the proposal and then we can get a couple of things settled." Tatsiana asked "do you need some more information from me for the proposal?" and agreed to speak in a couple of hours.

**Objective, what winning looks like:** leave with the ten inputs that move the proposal closed (timelines, markets, MIDs, volume split, performance criteria, routing ownership, subscriptions, reconciliation, integration path, second orchestrator), the list of Yuno products they will actually use, a contracting entity, and a committed date for the written proposal: Thursday, September 17 or Friday, September 18. Tatsiana has asked for pricing three times (September 8, September 10, September 15). A fourth time without a date is a problem.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state in the call · 🔍 ask in discovery

---

## ⚠️ Pre-meeting actions

1. **Schedule the call.** No calendar event exists yet. Text Tatsiana, fix the slot, and create the shared Slack channel Jarrett offered on the call.
2. **Talk to Piotr.** Justo's instruction: "Habla con Piotr que los conoce bien." Ask what he knows about their Solidgate setup, who holds the MIDs, and their relationship with Unlimit and the other phase 1 providers.
3. **Jarrett, four confirmations:** the formal timeline for a merchant-owned TRID (he said "a week or so" on the call); the real status of Verifi and Visa RDR (he told them both are supported; internally Verifi was unconfirmed on September 14); whether a separate MID through the Unlimit partnership is viable; and whether Shift4 and Payabl are in the catalog before anyone repeats "full coverage of your phase 1 providers."
4. **Leo:** which providers deliver TC40 and SAFE today beyond dLocal, so the scope against their phase 1 list is honest. Jarrett described the reports as customizable on the call.
5. **Sean:** the agreed sentence on bank introductions (section 7), and the Deal Desk framing for Wednesday 08:00: ARR $180,000 steady state, $155,575 year 1, decision maker Dzmitry with Butrym signing.
6. **Fix the deck before the proposal call:** slide 13 "Expected" months and the "What it means" box still sit on the first assumed ramp; slide 11 carries two FlightHub bullets. Values in section 6.
7. **Send the Top 10 ahead of the call** by Slack or email so Tatsiana arrives with the volume split, the MID map and the provider list.
8. **Run the calculator.** Duplicate "Yuno — Pricing Palco" as "Yuno — Pricing Appmaking" (150,000 transactions, AOV $18, Digital Business / Goods) so the score is on file before Deal Desk.

---

## 1. TL;DR Battle Card

### Five facts to know cold

1. **They process about 500,000 transactions a month** across all providers (August 2026, Tatsiana on the September 15 call). Their ramp gives Yuno 150,000 by month 7, about 30% of today's volume. ✅
2. **Their curve, in their words (September 8 email):** 20K, 30K, 45K, 65K, 90K, 120K, 150K successful transactions in months 1 to 7, AOV exactly $18, fully ramped in month 7. What drives it: "performance. We would be testing which transactions work better at Yuno, and as soon as we find what works best we would be giving you more volume. We do have big volumes at the moment." ✅
3. **Solidgate is in the money flow with almost all of their volume.** No written minimum, but "they do get cheaper the more transactions you send through them, so we tend to keep bigger volumes there." Justo's question is the one that decides the shape of the proposal: are the MIDs theirs or Solidgate's? ✅
4. **The second orchestrator is the volume that moves first.** "A small team, a small gateway, they don't always have the resources. If something breaks it takes them a lot of time to fix, and that causes approval rate drops and billing problems. If we were looking to transfer, that would probably be from them." ✅
5. **They want their own TRID.** Reason given: "we just like to be secure, owning those tokens, it's our responsibility and we are flexible." Legal is checking readiness; they do not vault tokens on their side today. Jarrett: Yuno is a certified token requestor, a merchant TRID takes about a week, tokens are portable as a batch file to a new requestor. ✅

### Three hooks, in priority order

**Hook 1: turn "performance" into a written scale-up rule.** Volume follows performance, so define performance with them: approval rate by market and BIN, latency, cost per transaction, chargeback rate, against a baseline from their current reports, over a fixed window. Ask for two to three months of approvals and declines by geo and PSP under the NDA. Without a baseline nothing can be measured and the ramp stays a promise.

**Hook 2: monitors with automatic redistribution are the answer to the second orchestrator's failure mode.** Their pain is slow reaction when something breaks. Yuno detects the failure from the error responses, bypasses the provider, keeps one percent of traffic to test it, and restores the routing when it recovers. German said it on the call: "your approval rates will never be affected by outages." Position Yuno as the destination for that volume, not a third of an experiment.

**Hook 3: new markets are greenfield.** LatAm is the stated interest; Korea and Africa are on the list; "many regions we are not processing to our full capacity." Pix, Pix Automático, UPI and UPI Autopay already run on Solidgate, so the argument for new markets is new rails and local acquiring through one connection, not migration.

### THE objection they will raise, and the answer

> Dzmitry, P&L first: "$9,000 for 20,000 transactions is $0.45 each. That is expensive for month one."

The band is set by what they actually process, not by the calendar. Month one is the only month above $0.30. By month four they are at $0.165, by month seven at $0.10. Year 1 lands at $0.12 all-in with every connector, KAM and TAM included, and above 150,000 every extra transaction is five cents. If they push: on their own curve the standard structure costs more in year 1. Do not move the fully ramped $15,000 yourself; Sean decides live if anything moves.

### The ask

The ten inputs answered, the products confirmed, the contracting entity named, and a date for the written proposal that German then meets.

### Rapport opener

They went through the sandbox and liked it ("intuitively understandable," Tatsiana). Thank them for the ramp curve too: few prospects send a month-by-month plan unprompted, and the proposal is built on it.

---

## 2. Who is in the room

| Name | Role | Side | Status |
|---|---|---|---|
| Tatsiana Hubarevich (Gubarevich) | Payment Manager, group. The operator and champion; writes every email; asked every question so far | Appmaking | Agreed to the short call |
| Dzmitry Katsiushchyk | P&L owner in the room. Gave the ramp and the "profitability" framing; decides whether $15,000 a month makes sense | Appmaking | On both calls |
| German Tatis | BDM NA, runs the deal | Yuno | |
| Jarrett Falasco | Senior Sales Engineer, ran the demo and the technical answers | Yuno | Optional for the short call |
| Joaquin Mann | BDM NA, joined the team the week of September 7, observing | Yuno | Optional |
| Sean Calabro | General Manager NA. Wants timelines and markets, routing and partner strategy, subscriptions and reconciliation answered | Yuno | Not on the short call; reads the outcome |

**How to read Tatsiana:** precise and procedural. She asked about RDR alongside Ethoca, whether TC40 reports are customizable, and how long an own TRID takes. She is checking that Yuno's answers survive contact with her legal and finance teams. Give her exact scopes and dates, not adjectives.

**How to read Dzmitry:** he speaks when the topic is money or performance. He owns the "as soon as we find what works we give you more" logic. Show him the unit-cost curve and the scale-up rule.

### Relationship timeline

| Date | Event |
|---|---|
| Sep 2 | Phase 1 provider list confirmed in writing: Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI, plus one unclear |
| Sep 4 | Call 1, 44 min. Subscription business, 95% web. Two orchestrators, Yuno as third layer. Recap sent with NDA |
| Sep 8 | Tatsiana sends the ramp curve, asks for a TC40/SAFE sample and whether Yuno introduces merchants to banks |
| Sep 10 | Tatsiana chases the pricing: "Will you be able to share the pricing this week?" |
| Sep 14 | German answers TC40/SAFE, TRID, Ethoca and the provider list by email |
| Sep 15 | Call 2, 47 min. Answers reviewed, ramp discussed, full dashboard demo. Proposal not shown. Short call agreed |
| Next | Proposal inputs call, then the written proposal on September 17 or 18 |

**Implication:** this is the third conversation and the fourth time pricing is on the table. Every question in this brief builds on what they already said; nothing below re-asks what the emails or the two calls answered.

---

## 3. What the September 15 call established

| Topic | What they said | Where |
|---|---|---|
| Total volume | About 500,000 transactions in August 2026 across all providers | 15:41 |
| Ramp driver | Performance. They test which transactions work better at Yuno and move more as they find it. "We do have big volumes at the moment" | 14:30 |
| Solidgate | No written minimum, cheaper with volume, so they concentrate volume there. Justo: Solidgate is in the money flow with almost all the flow | 16:11 |
| Second orchestrator | Small team and gateway, slow fixes, approval drops and billing problems. Any migration starts there | 17:48 |
| One PSP through two orchestrators | They want to use the same bank (Unlimit was the example) through the current orchestrator and through Yuno. Jarrett: possible with the same credentials; the cost is reconciliation and duplicate alerts; a separate MID through the Unlimit partnership is an option | 21:20 |
| Coverage | LatAm is the interest; Korea and Africa are being looked at. Pix, Pix Automático, UPI and UPI Autopay already integrated on Solidgate | 20:21, 23:50 |
| 3DS | Each orchestrator's native 3DS | 28:27 |
| Tokens | No tokens vaulted on their side; both providers are PCI. Own TRID wanted for security, ownership and flexibility; legal checking requirements | 5:34 to 13:25 |
| Alerts | Jarrett: Ethoca and Visa RDR supported, pre-chargeback notification project under way. ⚠️ Verifi unconfirmed internally on September 14; verify before writing it | 3:06 |
| TC40 and SAFE | Jarrett: customizable if the data point is in the file; TC40 already normalized. ⚠️ Internally only dLocal delivers it today (SFTP, Leo); none of their phase 1 providers confirmed | 4:17 |
| Sandbox | Their team went through it and liked it | 1:52, 25:21 |
| Entity and markets | Cyprus entity. Global sales, strongest in the US and Europe, strong interest in LatAm where they have few connections (German to Justo) | WhatsApp |
| Demo covered | Routing conditions, decline groups, retries, failover, traffic split for commitments and A/B tests, smart routing on conversion, latency and cost, monitors with automatic redistribution, checkout builder, tenant structure. Subscriptions shown on call 1 | 25:32 to 46:14 |
| Bank introductions | Tatsiana's September 8 question. Not touched on September 15. Still open | Email Sep 8 |
| Next steps | Short call to close the proposal inputs; shared Slack channel | 46:14 |

---

## 4. The internal asks this call must resolve

| From | The ask | Why it matters | Resolved by |
|---|---|---|---|
| Sean | Timelines: when do they want to go live, and which markets come first | Sets phase 1 scope and the "expected months" on the proposal | Block A |
| Sean | What drives the routing strategy once live; the payments partner strategy | Decides whether Yuno is the routing brain or extra rails, and which providers sit behind it | Block B |
| Sean | Subscriptions and reconciliation: in house, or something Yuno can support | Decides whether standalone modules enter the proposal | Block C |
| Justo | Are the MIDs theirs or Solidgate's? Where do they have entities and where do they sell? | If the MIDs are Solidgate's, Yuno has to onboard them with processors and the proposal includes that plan. If the MIDs are theirs, it is connection and credentials | Block B, first six questions |
| German | Which Yuno capabilities they are willing to use | Turns "Pending scoping" lines into priced lines, or drops them | Section 5 checklist |
| German | The largest possible volume | 150K is 30% of what they process. The lever is a written performance rule plus greenfield markets through Yuno | Block E |

---

## 5. Capabilities checklist: what they would actually use

| Capability | What we know | Ask | If yes, in the proposal as |
|---|---|---|---|
| Routing rules (conditions, BIN, metadata) | Demoed, understood | Will you manage routing yourselves in the dashboard, or want us to configure phase 1 with you? | Included |
| Smart routing | Demoed; today they hand-tune geo and OS splits | Would you enable smart routing on a share of traffic from day one? Which share? | Included |
| Monitors with automatic redistribution | "It looks cool"; answers the second orchestrator's pain | Which thresholds and alert channels do you want? | Included |
| Failover, retries, decline groups | Demoed | What retry logic do you have today that we should replicate or improve? | Included |
| Decoupled 3DS | Today each orchestrator's own 3DS | Would you move 3DS to Yuno for cross-provider retries without re-authentication? | Included |
| Network tokens under their own TRID (passthrough) | Strong interest; legal reviewing; about a week per Jarrett | Own TRID from day one, for all cards or renewals first? | Pending scoping (vault and tokens) |
| Agnostic vault and proxy (tokens usable outside Yuno) | They asked for portability; no vault on their side today | Which providers outside Yuno would consume the tokens? | Pending scoping |
| Subscriptions engine, standalone | Shown on call 1; where billing lives today is unconfirmed | Would you run a segment on our engine? | Pending scoping |
| Reconciliation | Normalized reports explained | Standalone reconciliation, for which sources? | Pending scoping |
| Reports (approval by provider, country, BIN; export) | Part of the dashboard | Which views does Dzmitry need for the bake-off? | Included |
| TC40 and SAFE, bank and fraud rates per PSP | Customizable per Jarrett; internally dLocal only today | Launch requirement on your phase 1 providers, or nice to have once live? | Scoped provider by provider |
| Verifi RDR and Ethoca | Ethoca confirmed; Verifi to verify | Alerts through Yuno for Yuno traffic only, or for everything? | Pending scoping, priced separately, never improvised |
| Fraud engine and risk conditions | Not discussed | Who does antifraud today? Interested in risk conditions on routes? | Pending scoping |
| Checkout: full SDK, lite SDK or server to server | They own the quiz funnel UI | Which path, who builds it, when? | Defines the integration |
| Tenant structure (accounts per region, brand or entity) | Explained | How do you want data split? | Included |
| New payment methods and APMs | Pix and UPI live; gaps in LatAm, Korea, Africa | Which APMs per priority market for phase 1? | Included; connectors confirmed in writing |
| Nova and Payments Concierge | Promised since September 4, not yet shown | Do you want a 20 minute session? | Separate session |
| Marketplaces, installments | Not their model | Do not ask | Out |

---

## 6. The proposal: current model and what this call changes

**Current model (deck "Proposal - AppMaking + Yuno", slide 13):** a platform fee plus a rate per successful transaction, both stepping by the month's successful transactions: $5,000 + $0.20 (0 to 25K) · $5,500 + $0.12 (25,001 to 50K) · $6,500 + $0.065 (50,001 to 100K) · $7,500 + $0.05 (100,001 to 150K) · $7,500 + $0.05 per transaction above 150K. Declines free, no setup fee. Fully ramped $15,000 a month, $180,000 a year. On their curve: months 1 to 7 $80,575 for 520,000 transactions; year 1 $155,575 for about 1.27M ($0.12). The September 10 fixed-fee draft is a backup, not what is presented.

- **Deck fixes before it is shown (brief of September 15, sections 4.3 and 4.7):** "Expected" column becomes Month 1 / Months 2 to 3 / Months 4 to 5 / Months 6 to 7 / Month 8 onward. "What it means for AppMaking" becomes Months 1 to 7 $80,575 (520k, $0.155), Months 8 to 12 $75,000 (750k, $0.10), Year 1 $155,575 (about 1.27M, $0.12). Slide 11: remove the two FlightHub bullets.
- **The band above 150,000 now matters.** With 500,000 a month in play, show what a larger share costs: 250,000 transactions is $20,000 a month ($0.08); 500,000 is $32,500 a month ($0.065). This is the number behind the target-share question in Block E.
- **Scale-up criteria in writing.** Their volume follows performance. Convert the answer to Top 10 question 5 (metric, baseline, window) into a clause in the proposal.
- **Onboarding with processors.** If the MIDs are Solidgate's, the proposal includes the plan to open their own MIDs with each phase 1 provider and the timelines. If the MIDs are theirs, it is connection and credentials only.
- **Standalone modules** enter only if they say yes in section 5, and only after the calculator is run for each. Everything else stays "Pending."
- **Contracting entity and term.** Appmaking LTD or Appsella LTD (Butrym signs). Ask which term they would sign: 12, 24 or 36 months. Billing in USD.
- **Date.** Commit to Thursday, September 17 or Friday, September 18 for the written proposal, and meet it.

---

## 7. Be ready for

| They ask | You answer |
|---|---|
| "Can you send the pricing in writing after this call?" | Yes: the slide plus a one-page summary of the rules, on the date agreed. |
| "What is the contract term?" | Proposed in the written proposal once products are confirmed. Ask which term works for them; do not improvise one. |
| "Is $15,000 negotiable?" | $15,000 fully ramped is the standard price for their size; the ramp already halves the platform fee while they grow. If they want a lower steady state, platform fee and per-transaction rate move together. Sean decides live if anything moves. |
| "Which providers have TC40 and SAFE today?" | The ones Leo confirms. Not their phase 1 list yet. Scope together. |
| "Is Verifi live?" | Exactly what Jarrett confirms internally, nothing more. |
| "Do you have Shift4 and Payabl?" | Only if verified in the catalog before the call. |
| "Can we keep our own TRID?" | Yes, passthrough: they register as token requestor and send their token requestor ID by API. Confirm it works with their phase 1 PSPs. |
| "Do you introduce merchants to banks?" | Yuno has commercial relationships with the acquirers and PSPs on its catalog and can introduce the merchant to its contacts; the merchant contracts directly. Yuno is not a paid referrer, takes no part in underwriting and is not in the flow of funds. Ask which markets, which entity and what volume. Do not promise a formal program unless Sean agrees one. |
| "Which entity should contract?" | Their call: Appmaking LTD or Appsella LTD. Butrym signs for the Cyprus entities. |
| "How fast can phase 1 go live?" | Connections come up in days once credentials exist; the integration is one API and web SDK. Only quote a timeline Jarrett stands behind. |

**Landmines:** never "you don't have an orchestrator" or "your PSP shortlist is open"; never name Truegate; never include Adyen, JPMorgan or Checkout.com; never promise consolidated TC40/SAFE reports; never quote subscriptions, vault or reconciliation prices before the calculator is run; never assert the Wowmaking name or the four-entity group map; no em-dashes in anything written.

---

<!-- live -->

## 8. Agenda (30 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 3 | Open: thank them for the sandbox feedback and the ramp curve; confirm the goal is to close the inputs for the written proposal | Notes: ____ |
| 3 to 9 | Block A: timelines and priority markets | Notes: ____ |
| 9 to 17 | Block B: money flow and MIDs first, then routing after go-live | Notes: ____ |
| 17 to 22 | Block C: subscriptions and reconciliation | Notes: ____ |
| 22 to 26 | Section 5 checklist: which capabilities they will use | Notes: ____ |
| 26 to 30 | Close: contracting entity, Slack channel, date for the written proposal | Notes: ____ |

---

## 9. Discovery questions

### Top 10, if the call is short

1. When do you want the first live transaction, and what has to be true on your side first (legal on TRID, dev capacity, signature)? Notes: ____
2. Rank your phase 1 markets: US, EU (which countries), LatAm (which), Japan, Korea, Africa. Notes: ____
3. Are the MIDs in your name or Solidgate's? Which providers do you contract directly today? Notes: ____
4. Of the roughly 500,000 monthly transactions, how are they split between Solidgate, the second orchestrator and direct integrations? Notes: ____
5. What performance result would make you move more volume to Yuno, measured against which baseline and over what window? Notes: ____
6. Once live, who decides routing and on what rules? Would you let smart routing run on a share of traffic? Notes: ____
7. Where does subscription logic live today (plans, trials, renewals, retries)? Would you run a segment on Yuno's engine? Notes: ____
8. How do you reconcile across Solidgate, the second orchestrator and the app stores today? Who does it and with what tools? Notes: ____
9. Which integration path: full SDK, lite SDK or server to server? Who builds it and when? Notes: ____
10. What would it take to move the second orchestrator's full volume to Yuno, and when? Notes: ____

### Block A. Timelines and priority markets (Sean, point 1)

11. What is your target date for the first live transaction? Is there an internal quarter or a business event driving it? Notes: ____
12. What is on the critical path on your side: legal review for your own TRID, engineering capacity, procurement or contract signature? Notes: ____
13. Month 1 in your curve: is that the first month live, or the first month after integration is complete? Notes: ____
14. How long do you expect integration and testing to take? Who is the technical owner on your side? Notes: ____
15. Do you have any commitment with Solidgate or another provider that gates when you can start moving volume? Notes: ____
16. Is there seasonality, for example Q4 user acquisition peaks, that affects when you want to be live? Notes: ____
17. Who takes the final decision and who else needs to approve? When does legal (Butrym) come in? Notes: ____
18. For each priority market, which payment methods must be live on day one: cards, Apple Pay, Google Pay, PayPal, Pix, UPI, local cards? Notes: ____
19. Is the 150K curve Atrix only, or across brands (AstroSoul, Astroline, others)? Which funnels go first? Notes: ____
20. For LatAm, which countries specifically, and do you plan local entities and local acquiring, or cross border from Cyprus? Notes: ____
21. Korea and Africa: a 2027 plan, or phase 1? Notes: ____
22. Which entity will contract and process (Appmaking LTD, Appsella LTD, others)? Who signs? Notes: ____

### Block B. Money flow, MIDs and routing strategy (Sean, point 2, and Justo)

23. Are the merchant IDs with your acquirers in your name or in Solidgate's name? Provider by provider: Stripe, Unlimit, Ecompay, Airwallex, Shift4, Payabl, NMI, Nuvei, Maverick, Checkout.com. Notes: ____
24. Which providers do you contract directly, with your own contract and settlement, versus through Solidgate as aggregator or merchant of record? Notes: ____
25. Where does settlement land per provider: which entity, which currency, which bank? Notes: ____
26. Which providers are contracted but not live (Payabl), and why? Which would you onboard new for phase 1? Notes: ____
27. What is the exact scope and expiry of the Solidgate exclusivity? Adyen, JPMorgan and Checkout.com were mentioned. Anything else? When does the Solidgate contract renew? Notes: ____
28. If the MIDs are Solidgate's: which ones could you open in your own name, and how fast? Notes: ____
29. Bank introductions (your September 8 question): which markets do you need new acquiring in, with which entity, what volume would you put on a new acquirer, and what happened with previous acquirers? Notes: ____
30. Who owns routing decisions today and how often do rules change? Notes: ____
31. What drives routing today in Solidgate and in the second orchestrator: geo, OS, BIN, cost, approval rate, provider commitments? Notes: ____
32. Can you share two or three months of approvals and declines by geo and PSP under the NDA, so the scale-up rule has a baseline? Notes: ____
33. What share of each market do you plan to send to Yuno at the start, and what metric and window would scale it up? Notes: ____
34. Which providers would sit behind Yuno, and which stay only on Solidgate? Notes: ____
35. One PSP through two orchestrators: which providers and markets? Do you want a separate MID via our Unlimit partnership? Who reconciles the two streams? Notes: ____
36. What retry and decline logic exists today? Do you retry across providers? Do you carry network transaction IDs for MITs? Notes: ____
37. Would you move 3DS to Yuno's decoupled 3DS so retries can cross providers without re-authentication? Any SCA exemption strategy in the EU? Notes: ____
38. Monitors: what approval rate thresholds would you set, and where do alerts go (email, OpsGenie, Slack)? Notes: ____
39. Partner strategy going forward: local acquirers in LatAm, Korea or Africa through Yuno connections, or candidates you already have? Notes: ____
40. Second orchestrator: how much volume is on it, what is the timeline to phase it out, and what needs to be true for Yuno to take that volume? Notes: ____

### Block C. Subscriptions and reconciliation (Sean, point 3)

41. Where does the subscription logic live today: your own billing system, Solidgate's subscription product, the second orchestrator, something else? Notes: ____
42. Which features are handled where: plans, trials, phased pricing, per-country pricing, renewals, retries, proration, cancellations? Notes: ____
43. What share of the roughly 500,000 monthly transactions are renewals (merchant initiated) versus first payments? Notes: ____
44. How does approval on renewals compare with first payments? Do you use account updater or network tokens on renewals today? Notes: ____
45. Where are cards vaulted today, how many cards on file, and under whose TRID are the current network tokens? Notes: ____
46. How do you handle failed renewals: retry schedule, dunning emails, downgrade? Who owns that logic, and how much revenue do you lose to failed renewals per month? Notes: ____
47. Would you run a segment on Yuno's subscription engine (a new brand, a new market, the web funnel)? What would be must-have for that? Notes: ____
48. Is Nova or a retry optimization layer interesting for renewal recovery? Do you want a session on it? Notes: ____
49. How do you reconcile today across Solidgate, the second orchestrator and the app stores? Spreadsheets, in-house tool, third party? Notes: ____
50. Who does it and how much time does it take per month? What breaks most often? Notes: ____
51. Which reports do you need and how often: transactional, settlement, fees, chargebacks, TC40 and SAFE, bank and fraud rates per PSP? Which data points must be in them, and who consumes them? Notes: ____
52. Would you use Yuno reconciliation as a standalone module, and for which sources: Yuno only, or also Solidgate and the second orchestrator? Notes: ____
53. Who provides Verifi and Ethoca alerts today, through which descriptor, how many alerts a month, and what do you pay? Alerts through Yuno for Yuno traffic only, or for everything? Notes: ____
54. Who responds to disputes today and with what tool? How many per month? Any MID near a Visa or Mastercard monitoring threshold? Notes: ____

### Block D. Integration path

55. Full SDK, lite SDK or server to server? Who builds it, how many developers, and when can they start? Notes: ____
56. How do you want the tenant structure: accounts by brand, by region, by entity? Notes: ____
57. Who does antifraud today, in house or a provider? Interested in risk conditions on routes? Notes: ____

### Block E. Getting to the largest possible volume

58. Map the roughly 500,000: by provider, by region, by brand, and first payments versus renewals. Notes: ____
59. Solidgate price breaks: at what volumes does your per-transaction cost drop, and how much volume do you need to keep there to hold your current tier? Notes: ____
60. If performance is good by month 7, what does month 12 look like? Would you commit to a target share, for example half of your volume, contingent on agreed performance results? Notes: ____
61. Would a price that drops per transaction as your volume grows change how fast you move volume to us? Notes: ____
62. New markets (LatAm, Korea, Africa) are greenfield: would you route those through Yuno from day one? Notes: ____
63. Anything contractual or technical that caps the share of volume you could send to Yuno in year 1? Notes: ____

---

## 10. Post-meeting checklist

- Same-day recap by email: the inputs closed, the products they want, the entity, and the proposal date, with owners and dates for anything still open (Verifi, TC40 scope by provider, Shift4 and Payabl, bank introductions, Unlimit MID).
- Fix slide 13 and slide 11; run the calculator for Appmaking and for any standalone module they said yes to.
- Send the written proposal on the committed date.
- Deal Desk framing for Sean: ARR $180,000 steady state, $155,575 year 1, close date, decision maker, blocker, the ask.
- Log the outcome and new facts; update memory: MIDs owner, volume split, products selected, contracting entity, reaction to $15,000, next step date.

---

### Sources

- Google Meet transcript, "AppMaking + Yuno," September 15, 2026, 47 min (German, Jarrett Falasco, Joaquin Mann, Sean Calabro; Dzmitry Katsiushchyk, Tatsiana Hubarevich).
- Sean Calabro, written feedback after the September 15 call (three points to understand).
- Justo Benetti, WhatsApp with German, September 15, 2026 (money flow, MIDs, Piotr).
- Tatsiana Gubarevich, email of September 8, 2026 (ramp curve, TC40/SAFE sample, bank introductions) and September 10 (pricing chase).
- data/research/appmaking-meeting-brief-2026-09-15.md (v2, Proposal Debrief), Deals/Appmaking/appmaking-qa-and-discovery-2026-09-15.md, Deals/Appmaking/appmaking-open-questions-2026-09-14.md, Deals/Appmaking/appmaking-discovery-questions-2026-09-15.md.
- Deck "Proposal - AppMaking + Yuno," Google Slides, 18 slides, PDF in Deals/Appmaking.
