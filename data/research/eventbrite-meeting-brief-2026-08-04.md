# Meeting Brief: Yuno <> Eventbrite

**Tuesday, August 4, 2026 · 16:30 to 17:00 COT (30 minutes) · https://meet.google.com/zoj-mucn-hyd**
Organizer: German Tatis · Prepared 2026-08-03
Google Doc: https://docs.google.com/document/d/17TUFSuhggGtWqcS6tR2rTxnXbPchujrFYLhcqhPpS0E/edit

> **Read this first. The account changed identity five months ago.** Eventbrite is no longer NYSE: EB. Bending Spoons S.p.A. (Milan) closed its acquisition on **2026-03-10** for $4.50 per share, roughly $505M total, and the stock was delisted from the NYSE on 2026-03-23. Julia Hartz, CFO Anand Gandhi, CPO Ted Dworkin, CLO Lisa Gorman and the entire board are gone. Bending Spoons itself IPO'd on Nasdaq (ticker **BSP**) on 2026-07-01. Referring to Eventbrite as a public company, citing quarterly earnings calls, or naming Julia Hartz as CEO would be an immediate credibility loss.

**Objective, what winning looks like:** leave with Paul agreeing to a working session that includes whoever owns payment routing today, either inside Eventbrite or at Bending Spoons in Milan, scoped around processing cost and local acceptance in the non-US markets.

## ⚠️ Pre-meeting actions

| Action | Why |
|---|---|
| **Open Paul Pasion's LinkedIn profile logged in and note his title and career path.** https://www.linkedin.com/in/phpasion/ | The attendee is confirmed as **Paul Pasion** (German confirmed the profile). His profile is set to private for logged-out viewers, so automated retrieval was blocked and no public source states his title or history. German has LinkedIn access; two minutes logged in closes the gap. Do not greet him by an assumed title until then. |
| **Confirm Jarrett Falasco is attending.** | He has not responded to the invite (needsAction). |
| **Get gong@y.uno to accept, or the call will not be recorded.** | The Gong recorder is on the invite but still needsAction. |
| **Read the email thread with Paul yourself.** | The Gmail connector is not authorized in this session, so no thread history could be pulled. What was already sent, who introduced whom, and what was promised are all unknown. |
| **Consider whether a second Eventbrite name belongs on the invite.** | Paul is the only external attendee. |

No prior Gong call history exists for this account (GONG_ACCESS_KEY not configured), and there was no prior research file for Eventbrite in `data/research/`. Treat as a first meeting. Parent-account file: `data/research/bending-spoons-2026-06-17.md`.

---

# 1. TL;DR Battle Card

### Five facts to know cold

1. **Eventbrite is a private Bending Spoons subsidiary as of 2026-03-10.** Francesco Patarnello (Bending Spoons) is President and Secretary, Mattie Maharaj is Treasurer, and **Andrea Parodi** is the general manager running the business. Capital allocation sits in Milan. ✅
2. **Eventbrite is the merchant of record and carries payments in its own P&L.** Under Eventbrite Payment Processing (EPP) the 10-K states it "is the merchant of record," acts as principal and books revenue gross. FY2025: gross ticket sales over $3.0B, 78.9M paid tickets, net revenue $291.8M, cost of net revenue $94.5M (32%). ✅
3. **Their own 10-K names processing fees as the biggest cost line.** Verbatim: *"Processing fees are the largest component of cost of net revenue."* And: *"Our payment processing costs for credit and debit card payments are generally lower outside of the United States due to a number of factors, including lower card network fees and lower cost alternative payment networks."* ✅
4. **Five payment vendors, no third-party control plane.** Eventbrite's own sub-processor page lists under Payment Services: **Cybersource (Visa), Adyen B.V., Braintree (a division of PayPal), MercadoLibre, and Stripe**. The 10-K describes self-built failover: *"We have multiple integrations in place at one time allowing for back up processing alternatives on our payments system if a single provider is unable or unwilling to process any given transaction, payment method or currency."* ✅
5. **The 2026 to 2030 plan is a margin plan.** Management's own long-range forecast, disclosed in the merger proxy: revenue $308M (2026E) rising to $452M (2030E), while adjusted EBITDA nearly triples from $31M to $90M. ✅

### Three hooks, in priority order

| # | Hook | Why it lands |
|---|---|---|
| **1** | **They already wrote the business case.** "Processing fees are the largest component of cost of net revenue," and processing costs run lower internationally because of lower network fees and lower cost alternative payment networks. Meanwhile 41% of paid tickets are non-US but only 28% of revenue is. And on the final earnings call (2025-11-06), Julia Hartz stated the 2026 plan verbatim: *"increasing localization and monetization in our existing regions through the addition of more payment options and expanded creator tools."* ✅ | You are not introducing a thesis, you are quoting theirs back. Their own last public roadmap named more payment options as the international lever; that item now sits with a small GM-led team. With a finance-side attendee this is the fastest route to a real number, and it maps onto a plan that needs EBITDA to triple. |
| **2** | **Speed to market with a smaller team.** Parodi's stated post-acquisition priorities include *"ticketing and checkout."* Adding or switching a processor, a local method or a routing rule becomes configuration rather than an engineering project. | Talks to the actual constraint. Never frame this as a deficiency, frame it as cycle time and reliability. |
| **3** | **Local acceptance where the entities and volume already exist.** Payment-processing entities in Mexico, Canada, Australia, Singapore, Hong Kong and Ireland, plus operating entities in Brazil and Argentina, across 21 payout countries. Brazil, Mexico, Argentina, Singapore and Hong Kong currently transact on cards. | The legal and entity work, the hardest part, is already done. This is acceptance and conversion, not market entry. |

**Fourth hook, hold in reserve for a Bending Spoons audience:** the parent's IPO prospectus states that in Q1 2026, 75% of group revenue came through electronic payments, 67% of that via "providers such as Adyen, PayPal, and Stripe" and 33% via app stores at 15% to 30% fees, versus "5% or less" for the processors. It carries a risk factor headed "A significant portion of our products depend on third-party payment processors."

### THE objection, and the answer

> **"We already run several processors with failover built in. Why add a layer?"**

**Answer:** "That's right, and it's why this is a shorter conversation than usual. You already made the architectural decision that no single provider should carry every transaction, method and currency. What you built is redundancy, which answers the reliability question. The part redundancy does not answer by itself is the economics: which processor should take a given transaction based on cost and authorization rate rather than availability, what happens on a soft decline, and how long it takes to turn on a local method in a market where you already have the entity. That is the difference between failover and routing, and it is the layer we operate. Nobody gets replaced. Stripe, Braintree, Adyen, Cybersource and Mercado Pago all stay exactly where they are."

### Second most likely objection

**"Payments decisions are made at Bending Spoons now, not here."** Answer: "Understood, and honestly that makes the conversation bigger rather than smaller. Their own prospectus puts numbers on this at the portfolio level and flags processor dependence as a risk factor. Eventbrite is the piece with a merchant-of-record model and real acquiring cost, so it is the natural first case. What would be most useful is if you point me at whoever owns routing in Milan and we bring them into the next conversation."

### The ask

A 45 to 60 minute technical and commercial working session in the next two weeks, with whoever owns payment routing and processing cost. Deliverable offered: a cost and authorization-rate model built on their non-US markets. Fallback: permission to send the model plus a warm introduction to the routing owner.

### Rapport opener

The product feed shipped **real-time sold-out status and a real-time waiting room on 2026-07-13**, and **order-level transfers with full refund on 2026-07-24**. High-demand onsale and refund mechanics, genuinely payments adjacent, three weeks old. Avoid opening on the acquisition.

---

# 2. Who Is in the Room

| Name | Role | Side | Invite status |
|---|---|---|---|
| German Tatis | Account Executive | Yuno | Organizer, accepted |
| Justo | Yuno | Yuno | Accepted |
| Jarrett Falasco | Yuno | Yuno | ⚠️ No response |
| gong@y.uno | Call recorder | Yuno | ⚠️ No response, recording at risk |
| **Paul Pasion** | ⚠️ Title unconfirmed (private profile) | Eventbrite | Accepted |

### Profile: Paul Pasion (paul@eventbrite.com) ✅ identity · ⚠️ role

**Identity confirmed by German: https://www.linkedin.com/in/phpasion/.**

- **What automated research could and could not get.** The profile is set to private for logged-out viewers (LinkedIn returns "Profile Not Found... may be private" to anonymous fetches), and no public source (DuckDuckGo, Bing, TheOrg, RocketReach, ZoomInfo, press) ties a Paul Pasion to Eventbrite. His **title, tenure and career history are therefore unknown** in this brief and must be read manually from the logged-in profile. ⚠️ Pre-meeting action above.
- **What the first-name-only address suggests:** nothing. `firstname@` is Eventbrite's most common email format at roughly 57% of addresses, so it carries no seniority signal. That he kept the address through the April 2026 reduction does confirm he is a current employee.
- **Earlier candidates now ruled out as the attendee:** Paul Bach (Manager, Finance), Paul Pieralde (ex Director of Security, now Amazon), Paul Duan (early data scientist, left years ago).

**How to play an attendee whose role you do not know:** open by asking him to describe what he owns today, in his own words, before positioning anything. If finance, lead hook 1 (cost). If product or engineering, lead hook 2 (speed to market and reliability). Do not guess his title out loud.

### Relationship timeline

- **2026-07-29** German creates the "Eventbrite + Yuno" event for 2026-08-04.
- **By 2026-08-03** Paul has accepted. Justo has accepted. Jarrett and the Gong recorder have not responded.
- **2026-08-03** Two internal prep blocks: "Eventbrite Prep GT" at 14:30 (solo) and "Eventbrite Prep" at 16:00 with Jarrett and Justo.

**Implication:** Paul accepted a meeting with an unfamiliar vendor and has stayed on the invite. That is a real signal, but it is all that is on file. ⚠️ Whatever was said in email is not reflected here.

### Other contacts in the account

| Name | Role | Relevance |
|---|---|---|
| Andrea Parodi | General Manager, Eventbrite (Bending Spoons) | Runs the business. Stated priorities include ticketing and checkout. The real economic buyer. |
| Francesco Patarnello | President and Secretary, Eventbrite; Bending Spoons co-founder | Officer of record post-close. |
| Mattie Maharaj | Treasurer, Eventbrite (Bending Spoons) | Treasury title in a merchant-of-record business with $278M payable to creators. High-value follow-on. |
| Luca Ferrari | Co-founder and CEO, Bending Spoons | Named "creating a system for the secondary ticket market" among his priorities at deal announcement. ⚠️ Follow-through has been weak: of his four named ideas (messaging, AI event creation, searchability, secondary ticketing), only searchability survived into the actual post-close roadmap. Treat his list as aspiration, not plan. |
| Davide Scarpazza | Co-CFO, Bending Spoons | Quoted in the 2026-07-28 6-K (€500M SACE-backed term loan): "we remain focused on deploying capital in a disciplined way ... primarily through acquisitions." Finance-side door in Milan. |

⚠️ No Head of Payments, payment operations lead or treasury contact could be verified by name at Eventbrite. Finding that person is a legitimate goal of this call.

---

# 3. The Company

Eventbrite is a self-service ticketing and event-discovery marketplace. Creators publish events, Eventbrite sells the tickets, and it earns a service fee per paid ticket plus a payment processing fee, with a growing advertising line. Free events are free to publish. Legal entity: **Eventbrite, Inc.**, a Delaware corporation (reg. 4742147), HQ at 95 Third Street, 2nd Floor, San Francisco, CA 94103, now wholly owned through Bending Spoons US Inc. by Bending Spoons S.p.A. (Nasdaq: BSP).

### Key metrics, FY2025 (final 10-K, filed 2026-03-12) ✅

| Metric | FY2025 | FY2024 |
|---|---|---|
| Gross ticket sales | over $3.0B | over $3.2B |
| Net revenue | $291.8M (down 10%) | $325.1M |
| Cost of net revenue | $94.5M (32% of revenue) | $98.5M (30%) |
| Gross margin | 68% | 70% |
| Net loss | $(10.5)M | $(15.6)M |
| Adjusted EBITDA | $25.3M | $35.1M |
| Paid tickets | 78.9M (down 6%) | 83.8M |
| Total tickets issued | 258M | 270M |
| Events | ~4.6M | ~4.7M |
| Implied take rate | ~9.7% | 9.9% |
| Non-US share of paid tickets | 41% | 40% |
| Employees | 636 (319 US, 317 non-US) | 748 |

**Revenue by geography, FY2025:** United States $209.1M (71.6%), United Kingdom $30.6M (10.5%), all other international $52.1M (17.9%). The UK is the only non-US country above 10% of revenue. **41% of paid tickets are non-US but only 28% of revenue is.** That gap is the single most useful number available.

**Payments-relevant balance sheet at 2025-12-31:** accounts payable to creators **$278.2M**, advance payouts outstanding $101.1M, funds receivable from processors $27.1M, chargebacks and refunds reserve $10.5M, and a **$48.0M letter of credit** established to mitigate refunds and chargebacks. The parent's prospectus restates this as "a collateralized cash account established by Eventbrite, Inc. in 2024 amounting to $48.0 million ... set up to manage and mitigate potential risks related to refunds and chargebacks," a hard payment-risk number now sitting on the acquirer's balance sheet.

**Creator concentration (final earnings call, 2025-11-06, Hartz verbatim):** *"Today, 13% of paid creators drive nearly 60% of paid tickets and about half of gross ticket fees."* Expanding offerings for the largest creators was named the top 2026 priority. Useful context: the volume that matters is concentrated, so a conversion or cost gain lands on a identifiable cohort.

**Post-close stub disclosed by the parent (424B4):** Eventbrite revenue $18.7M and loss before tax $31.5M for March 10 to March 31, 2026 only.

### Corporate structure and payment entities ✅

Sixteen subsidiaries on the FY2025 Exhibit 21.1. What matters is which entity contracts and which entity processes.

| Region | Entity used for Eventbrite Payment Processing | Location |
|---|---|---|
| Europe | Eventbrite Operations (IE) Limited | Citywest Business Campus, Dublin 24 |
| Australia | Eventbrite AU Pty Limited | Southbank, VIC (ABN 38 167 488 593) |
| Canada | Eventbrite Canada Inc. | Vancouver, BC |
| Singapore | Eventbrite Singapore Pte. Ltd. | Marina Bay Financial Centre |
| Hong Kong | Eventbrite Hong Kong Limited | Hopewell Centre, Wan Chai |
| Mexico | Eventbrite Mexico Payment Processing S. de R.L. de C.V. | Polanco, CDMX |
| Argentina (general contracting) | Eventbrite Argentina S.A. | Mendoza (CUIT 30-71038876-4) |
| Brazil (general contracting) | Eventbrite Brasil Gestao Online De Eventos Ltda. | São Paulo (CNPJ 15.913.672/0001-65) |
| Everywhere else | Eventbrite, Inc. | Delaware / San Francisco |

**Framing rule:** Mexico has a subsidiary literally named "Payment Processing." The entity groundwork in LatAm and APAC is done. Eventbrite UK Limited, Eventbrite ES SL and Eventbrite DE GmbH exist but are *not* contracting or payments entities, so do not name them in outreach. Europe runs through Dublin. Entity count fell from 29 (FY2018) to 16 (FY2025); the dedicated Eventbrite Payment Processing (IE) Limited was consolidated into Eventbrite Operations (IE) Limited in FY2023.

### Ownership and strategy

**Bending Spoons S.p.A.** (Milan, Nasdaq: BSP) is a leveraged roll-up of consumer software: Eventbrite, Vimeo, AOL, Evernote, **Meetup**, WeTransfer, Brightcove, komoot, Remini, Splice, StreamYard and more. FY2025 revenue $1.306B (up 95%), Q1 2026 revenue $601.3M (up 132%), net income $27.5M, total debt $4.36B at 2026-03-31. IPO priced at $29.00 on 2026-06-30, first traded 2026-07-01, closed day one at $40.50, trading around $36 as of 2026-08-03 at roughly $23B market cap.

Stated playbook, verbatim from a 2026-07-28 filing: *"The transformation is typically deep and entails reorganizing teams, overhauling technology, redesigning user interfaces, accelerating product development, and enhancing marketing and monetization. AI is often both a central component of the vision and a key tool."*

**Note for later, not for this call:** Bending Spoons also owns Meetup. One owner now holds both, and no integration has been announced.

---

# 4. Payments Money Map

### Architecture ✅

**Two models.** Under **Eventbrite Payment Processing (EPP)**, the 10-K states Eventbrite "is the merchant of record," is the principal and records revenue gross. Under **Facilitated Payment Processing (FPP)** the creator receives proceeds directly through a third-party service "such as PayPal," and Eventbrite books net. FPP is explicitly restricted: offered only "when you select a currency and payout country that isn't supported by Eventbrite Payment Processing," and it costs the organizer reserved seating, in-app card payments, fee absorption and order modification. In practice, EPP is the business.

| Vendor | Role | Evidence |
|---|---|---|
| **Stripe** | Verification, processing and payouts in AU, CA, UK, US via Stripe Connect | ✅ Help centre states it "uses Stripe to verify and process payments in Australia, Canada, the United Kingdom, and the United States"; Merchant Agreement requires the Stripe Connected Account Agreement |
| **Braintree** (a division of PayPal) | Card acquiring and gateway | ✅ Named sub-processor; live flag `enableNonceBraintreePayments` true in US, UK, IE, DE, NL, ES, CA, AU (probed 2026-08-03) |
| **MercadoLibre / Mercado Pago** | LatAm acquiring | ✅ Named sub-processor; live flag `should_accept_mercado_pago_credit_cards` true in MX and AR only |
| **Adyen B.V.** | Named payment sub-processor, specific role not disclosed | ✅ Listed, ⚠️ role unverified |
| **Cybersource** (a Visa company) | Named payment sub-processor, specific role not disclosed | ✅ Listed, ⚠️ role unverified |
| Authorize.Net, Moneris | Legacy integrations present in the platform, currently switched off | ✅ `accept_authnet` and `accept_moneris` flags present and false |
| LexisNexis Risk Solutions | Risk and analytics | ✅ Named sub-processor |
| reCAPTCHA v3 | Bot defence at checkout | ✅ `disableRecaptcha3: false` |
| Concentrix, Teleperformance | Outsourced payment operations | ✅ 10-K: BPOs in the Philippines and El Salvador support "creator payouts, chargeback management, and fraud identification" |

**Counting rule to respect on the call:** that is **five payment vendors**. PayPal itself is a wallet and an alternative method, and the FPP fallback rail. Braintree is the acquiring relationship. Never count PayPal as a processor.

**Orchestration status:** no third-party orchestrator appears in the sub-processor list or the checkout bundle. The 10-K describes what they built themselves: *"multiple integrations in place at one time allowing for back up processing alternatives on our payments system if a single provider is unable or unwilling to process any given transaction, payment method or currency."* That is failover. ✅

### Methods by market ✅ (Eventbrite help centre, 21 payout countries)

| Payout country | Currency | Attendee payment methods |
|---|---|---|
| United States | USD | Card, PayPal, PayPal Pay in 4, Klarna, Afterpay |
| United Kingdom | GBP | Card, PayPal, PayPal Pay in 3, Klarna, Afterpay |
| Canada | CAD + USD | Card, PayPal, Klarna, Afterpay, Affirm |
| Australia | AUD | Card, PayPal, PayPal Pay in 4, Afterpay |
| New Zealand | NZD | Card, Afterpay |
| Austria, Germany | EUR | Card, SOFORT, PayPal, Klarna |
| Belgium, Netherlands | EUR | Card, Bancontact, iDEAL, PayPal, Klarna |
| Finland, France, Greece, Ireland, Italy, Portugal, Spain | EUR | Card, PayPal, Klarna |
| Brazil | BRL | Card, Hipercard, Elo |
| **Mexico** | MXN | **Card only** |
| **Argentina** | ARS | **Card only** |
| **Singapore** | SGD | **Card only** |
| **Hong Kong SAR** | HKD | **Card only** |

**The detail that makes hook 3 concrete:** the live checkout payload already carries dormant flags for `should_accept_oxxo`, `should_accept_rapipago`, `should_accept_pagofacil`, `should_accept_boleto_bancario` and `maxInstallments`, all inactive across the twelve locales sampled on 2026-08-03. The plumbing was built and is switched off. Do not say this as an accusation. Say it as an observation that the hard part is already done.

⚠️ Apple Pay and Google Pay appear in Eventbrite documentation only for in-person Tap to Pay in AU, CA, UK and US, and no Apple Pay or Google Pay keys were found in the online checkout payload. High confidence, not absolute. Ask, do not assert.

### 3D Secure and fraud posture ✅ (live probe, 2026-08-03)

| 3DS2 enabled | 3DS2 not enabled |
|---|---|
| GB, DE, NL, ES, IE | US, CA, AU, MX, AR, SG, HK |

Maps cleanly to the PSD2 and UK SCA perimeter and nowhere else, which is a normal and defensible posture. The commercial read: outside Europe there is no exemption engine and no risk-based authentication to trade authorization against fraud. Chargeback costs fell **$10.1M year over year** in FY2025 "reflecting the impact of fraud remediation initiatives." That team already knows this number well, so treat them as sophisticated. Chargeback liability contractually sits with the organizer (Merchant Agreement §5.4), and Eventbrite reimburses its processors for card network fines.

### Payout mechanics ✅

Payouts land within about five business days of the event, with a reserve applied against net sales and a US-only Instant Payout at a 3% fee (minimum $2.99, maximum $40). Merchant Agreement §9.2 gives reserve and offset rights, §10.1 lets Eventbrite cap and withhold advance payouts. Notably: *"Event Proceeds collected in a currency may only be paid out to you in the currency in which they are collected. We do not provide currency conversion services."* This is the opening for the pay-out side, not just pay-in.

Corroboration that payouts are an active product surface (Q4 2024 earnings call, 2025-02-27, Hartz): they described *"rolling out stripe point-of-sale at scale"* and, on Timed Entry, *"the ability to consolidate the payout for the creator... instead of getting a payout on whatever schedule they've chosen for every event, they're getting one account level payout."* The stack is Stripe-anchored on acquiring and POS, and payout consolidation is something they already build product around.

### Fee card ✅

| Market | Service fee | Payment processing fee |
|---|---|---|
| United States | 3.7% + $1.79 per ticket | 2.9% per order |
| Canada | 3.5% + C$1.29 | 2.9% per order |
| New Zealand | 4.2% + NZ$0.55 | 2.4% per order |
| Australia | 5.35% + A$1.19 | Bundled into the service fee |
| United Kingdom | 6.95% + £0.59 | Bundled into the service fee |
| Ireland | 5.9% + €0.79 | Bundled into the service fee |

Eventbrite's own fee page splits countries into current "Standard" packages (US, UK, Canada, Australia, Ireland, New Zealand) and **"Legacy Package Countries"** (including Spain, Netherlands, Germany, Mexico, Brazil, Argentina, Hong Kong, Singapore). ✅ The legacy label is Eventbrite's own word, and it is the honest framing: a long tail that still transacts but is not being invested in. Orchestration is how a smaller team keeps monetizing a long tail it no longer staffs.

### Hiring signal ✅

`eventbrite.com/careers/jobs` now redirects to `jobs.bendingspoons.com` (verified 2026-08-03), and across the full Bending Spoons job board the keyword counts are: payment 1, fraud 0, billing 0, treasury 0, fintech 0. No payments organization is being staffed up. Do not say this out loud. Use it to calibrate: the buyer is a small generalist team that will value not having to build.

### Peer context ✅

| Company | Processors | Orchestration |
|---|---|---|
| Ticketmaster (Live Nation) | Braintree (primary), Adyen, Nuvei, Paybilt | In-house "TMPay" with a live provider enum, plus a Hyperwallet payout migration Aug 2025. FY2025: $37.1B fee-bearing GTV, 346M tickets. |
| Resident Advisor | Braintree plus multi-acquiring | **BR-DGE**, three-year deal signed Feb 2025 for multi-acquiring, dynamic routing and method connectivity |
| Fever (owns DICE since Jun 2025) | Checkout.com, Nuvei, PayU, Mercado Pago (AR), PayPal | **ProcessOut** in production, plus Forter and Queue-it. ProcessOut is owned by Checkout.com, one of Fever's own acquirers. |
| DICE | Stripe only (Stripe Connect) | None found. India is card-only with no UPI. |
| Luma, Posh, Partiful, Humanitix | Stripe Connect | None. The organizer, not the platform, is the merchant. |
| StubHub | Afterpay, Klarna, Zip, Affirm in the US | None found (Yuno research, 2026-07-09) |

**Use only if asked "is anyone in ticketing doing this?"** Yes: Resident Advisor runs a third-party orchestrator, Fever runs one, and Ticketmaster built its own. Eventbrite sits alongside Ticketmaster as one of the two large merchant-of-record ticketing platforms, and Ticketmaster chose to build a routing layer rather than rely on failover alone. Peer-behaviour argument, not a criticism.

---

# 5. Markets and Local Payment Behaviour

⚠️ **Honest limitation.** Only a small number of canonical market statistics were verified; the rest were dropped rather than estimated. The Worldpay Global Payments Report 2026 is download-gated and would close the gaps for UK, Canada, Australia, Netherlands, Germany, Mexico, New Zealand and Singapore. Do not quote numbers for those markets.

| Market | Verified statistic | For the call |
|---|---|---|
| **Brazil** | Pix has roughly 200M monthly active users, about 80% of the population (Central Bank of Brazil, Q1 2026), moving roughly R$3.4 trillion a month. Pix processed **8.6 times** more transaction value than credit and debit cards combined (2024). | Eventbrite has a Brazilian operating entity and sells in BRL on cards plus Elo and Hipercard. Ask what share of Brazilian checkouts complete today. The least arguable slide available. |
| **Spain** | Bizum reached 27.6M active users (2024) and joined EuropPA on 2025-03-31, interoperable with Bancomat Pay (Italy) and MB Way (Portugal). | Spain is a Legacy Package country with an EU-wide method now interoperable across three of Eventbrite's EUR markets. |
| **India** | UPI runs roughly 84% of digital payments (2025); about 20B transactions and ₹25 trillion in August 2025. ⚠️ Secondary aggregation, directional only. | India is not a payout country for Eventbrite, but it is where the engineering team sits. Context on how fast a market moves to a local rail, not an opportunity claim. |

**More useful than any market statistic:** Mexico, Argentina, Singapore and Hong Kong currently transact on cards, Brazil on cards plus two domestic schemes, and installments are inactive across every locale sampled. In Mexico, Brazil and Argentina, installments (meses sin intereses, parcelamento) are ordinary consumer expectation.

---

# 6. News and Signals

### Fresh, last 21 days 🔥

| Date | Item |
|---|---|
| 2026-08-03 | Bending Spoons Q2 2026 results not yet published. First post-IPO print is imminent, and margin levers are exactly what will be probed. |
| **2026-07-24** | Product: refund for order-level transfers. Move a whole order to a new date or event, then refund in full. **Rapport opener.** |
| 2026-07-23 | Product: bot-view filtering added to traffic and conversion reporting. |
| 2026-07-17 | Product: cross-event sales tracking by day, week and month. |
| 2026-07-15 | Product: add-on revenue broken out on the dashboard. |
| **2026-07-13** | Product: real-time sold-out status and real-time waiting room. **Rapport opener.** |

### Earlier, newest first

| Date | Item |
|---|---|
| 2026-07-01 | Bending Spoons IPOs on Nasdaq (BSP) at $29.00, raising roughly $1.68B, closing day one at $40.50. |
| 2026-06-08 | Bending Spoons files its F-1. Q1 2026 revenue $601.3M (up 132%), net income $27.5M. Prospectus quantifies group payment mix and names processor dependence as a risk factor. |
| 2026-05-03 | Julia Hartz gives her first post-sale interview, confirming she stepped away as CEO. |
| **2026-04-13** | Layoffs announced by GM Andrea Parodi, weighted toward India. Stated forward priorities: reliability, creator tools, event discovery, and **ticketing and checkout**. ⚠️ Do not raise the layoffs. |
| 2026-03-23 | NYSE removes EB from listing and registration. |
| 2026-03-12 | Final FY2025 10-K filed, two days after the deal closed. No Q4 2025 earnings release or call ever took place. |
| **2026-03-10** | Merger consummated. Entire board resigns. Patarnello, Maharaj and Mulligan appointed. Dworkin and Gorman step down. Hartz and Gandhi step down after the 10-K filing. |
| 2026-02-27 | Stockholders approve the merger (212.4M for, 1.17M against). |
| 2026-01-12 | ⚠️ *Juniper International LLC et al. v. Eventbrite, Inc.* filed in Delaware Chancery (C.A. 2026-0045-PAF) over Class B voting power. **Do not raise.** |
| 2025-12-01 / 12-02 | Merger agreement signed and announced. $4.50 per share, roughly $505M, an 81% premium to the 2025-11-28 close. |
| 2025-11-06 | Last Eventbrite earnings call ever. Q3 2025 revenue $71.7M (down 8%), gross ticket sales $748.3M, Eventbrite Ads up 38% year over year. |
| 2025-05-16 / 2025-05-02 | CTO Vivek Sagi and General Counsel Julia Taylor resign, weeks apart, shortly before the sale process began. |

⚠️ **Open regulatory matter, do not mention:** in April 2026 Bending Spoons received initial questions from the US Treasury unit that reviews foreign investment transactions not voluntarily filed with CFIUS, in connection with the Eventbrite acquisition. Unresolved.

---

# 7. Selling Yuno Here

### Core frame

Yuno is the unified operating system for global financial infrastructure, orchestrating across payment methods, processors, antifraud, KYC and KYB, reconciliation and stablecoins through one integration. For Eventbrite: **you already decided that no single provider should carry every transaction, method and currency. We operate the layer that turns that decision into routing, economics and speed, without displacing anyone you work with today.**

Keep returning to three words: **cost, authorization rate, and time to launch a method**. Not gaps, not what is missing.

### Hooks with proof points

| Hook | The evidence you cite | Yuno proof point |
|---|---|---|
| **Processing cost is the biggest controllable line** | Their 10-K: processing fees are the largest component of cost of net revenue, and non-US processing costs are lower because of lower network fees and lower cost alternative payment networks. Cost of net revenue $94.5M on $291.8M. Plus Hartz on the final call: 2026 international monetization comes "through the addition of more payment options," in a product "used in 180 countries every year." | **Rappi**: multi-PSP routing at scale in LatAm, routing on cost and authorization rather than availability. |
| **Local acceptance where the entity already exists** | 41% of paid tickets non-US against 28% of revenue. Payment entities already stood up in Mexico, Singapore, Hong Kong, Canada, Australia and Ireland, plus Brazil and Argentina operating entities. | **InDrive**: emerging-market local method coverage at scale, one integration across many countries. |
| **Speed to market with a smaller team** | Parodi's own priority list names ticketing and checkout. Adding a method or a processor becomes configuration. | **Reserva**: multiple brands operating under one orchestration layer. |
| **Recovery on declines and renewals** | Chargeback cost already fell $10.1M through fraud remediation, so they measure this. 3DS2 runs only in the European perimeter. | **Livelo**: recurring and high-volume flows with a recovery focus, smart retries and network tokenization. |
| **Portfolio consolidation (reserve for a Milan audience)** | The BSP prospectus: 75% of Q1 2026 revenue through electronic payments, 67% of that via Adyen, PayPal and Stripe, 33% via app stores at 15% to 30% against "5% or less" for processors, plus a named processor-dependence risk factor. | **Rappi** and **Reserva**: absorb each brand's existing rail as configuration rather than an integration project. |

### Landmines, what NOT to say

- **Do not call them NYSE: EB, do not mention earnings calls, do not name Julia Hartz as CEO.** The single fastest way to lose this room.
- **Do not raise the April 2026 layoffs, the India cuts, or headcount.** If Paul raises it, acknowledge briefly and move to how a smaller team ships faster with less to maintain.
- **Do not mention CFIUS or the Juniper Delaware lawsuit.** Both are live and neither is your business.
- **Do not mention the privacy letters.** The parent's prospectus discloses that in December 2025 Eventbrite received hundreds of substantially similar letters alleging violations of the California Invasion of Privacy Act. Live legal matter, off the table.
- **Never say they "lack" an orchestrator, or that anything is missing, broken or behind.** They built deliberate multi-provider failover. Respect it, then distinguish failover from routing.
- **Do not quote a dollar figure for their payment processing cost.** It has never been disclosed in any year. Cost of net revenue ($94.5M) is disclosed; the processing share of it is not.
- **Do not call PayPal a processor.** Braintree is the acquiring relationship and PayPal is the wallet and the FPP fallback.
- **Do not assert creator payout complaints or Trustpilot ratings.** None of it could be sourced, so it does not exist for this call.
- **Do not assert Adyen's or Cybersource's specific role.** Named sub-processors, function not disclosed. Ask instead.
- **Do not pitch replacement.** Say explicitly and early that Stripe, Braintree, Adyen, Cybersource and Mercado Pago all stay.

---

# 8. Be Ready For

| What they may ask | Ready answer |
|---|---|
| "How do you price?" | Per-transaction, on volume, decoupled from the processor economics so our incentive is to lower your cost per transaction. Give the shape now and the number after seeing volume by market and method. Do not invent a rate in the room. |
| "How long does integration take, and what does it cost my engineers?" | One integration to Yuno, then each processor and method after that is configuration rather than new code. Offer an SDK and API walkthrough in the working session. Be honest that the first integration is real work; the savings are on every one after. |
| "Do we have to replace Stripe or Braintree?" | No. Everything stays. We sit above what you already run and route across it. Say this before they ask. |
| "We already have failover. What is different?" | Failover answers availability. Routing answers economics: which processor takes a transaction based on cost and authorization rate, what happens on a soft decline, and how quickly a method turns on in a market. |
| "Why not build it? We have engineers." | You can, and Ticketmaster did. The question is what those cycles are worth right now against reliability, creator tools, discovery and checkout. The maintenance cost is the real number: every processor version change, every new method, every new market is ongoing engineering. |
| "PCI and security?" | Yuno is PCI DSS Level 1 certified and card data is tokenized, so this reduces rather than expands your PCI scope. ⚠️ Confirm the current certification wording with Justo or Jarrett before the call. |
| "Who holds the money? Does this change our merchant-of-record model?" | No. Yuno is an orchestration layer, not a merchant of record and not a processor. Funds continue to settle through your existing acquirers into your existing entities. You remain the merchant of record under EPP. |
| "Do you have references in ticketing or marketplaces?" | Lead with marketplace and high-volume consumer references (Rappi, InDrive, Reserva, Livelo). If pressed on ticketing specifically, be straight: point to what peers do (Resident Advisor runs BR-DGE, Fever runs ProcessOut, Ticketmaster built TMPay) rather than claiming a ticketing logo we do not have. |
| "What about payouts to creators, not just pay-ins?" | Strong ground. $278.2M payable to creators, reserves, a 3%-fee US-only Instant Payout, and no currency conversion service. Orchestration covers pay-in and pay-out on one layer. Ask whether payouts are in scope. |
| "Bending Spoons decides this, not us." | Convert it into an introduction request, do not fight it. See the second objection. |
| "What data would you need to show us a number?" | Volume and approval rate by market, method and processor, plus decline reason codes. Offer to work from whatever subset they can share, even one market. |

---

# LIVE ZONE

# 9. Agenda (30 minutes)

| Time | Block | Notes |
|---|---|---|
| 0:00 to 0:03 | Intros. Confirm Paul's role in his own words. Rapport on the July 13 waiting room and July 24 order-level transfer refund. Agree the 30 minutes. | Notes: ____________________ |
| 0:03 to 0:07 | Yuno in 90 seconds, then why you asked for the meeting. Say up front that nobody gets replaced. | Notes: ____________________ |
| 0:07 to 0:19 | **Discovery.** The longest block on purpose. Questions 1 through 6 below. | Notes: ____________________ |
| 0:19 to 0:25 | Where Yuno fits, tailored to what he just said. One proof point only, chosen live. | Notes: ____________________ |
| 0:25 to 0:30 | Next step. Ask for the working session and the name of whoever owns routing. Confirm follow-up and who to copy. | Notes: ____________________ |

# 10. Discovery Questions

These build on what is already public. None re-ask something the filings or help centre already answer.

1. **To start, tell me what sits inside your remit today. Where does payments touch what you own?** (Establishes his seat, genuinely unknown, and decides which hook to lead with.)
   *Notes: ____________________________________________*
2. **Since the transition in March, how have payments decisions been running? Is routing and processor strategy still decided here, or has it moved to Milan?**
   *Notes: ____________________________________________*
3. **Publicly you work with several processors and the 10-K describes multiple integrations with back-up alternatives. In practice, what decides which one takes a given transaction today?** (Pivotal question of the call.)
   *Notes: ____________________________________________*
4. **Processing cost is the biggest line in cost of net revenue, and the 10-K notes it runs lower internationally. With 41% of paid tickets non-US and 28% of revenue, is that mix something the team is actively working, and what does the measurement look like?**
   *Notes: ____________________________________________*
5. **In Brazil, Mexico, Argentina, Singapore and Hong Kong the checkout runs on cards. When you look at completion rates there against your European markets, what does the gap look like, and what has held back turning on local rails and installments?**
   *Notes: ____________________________________________*
6. **Chargeback cost came down materially last year through fraud remediation. Outside the European markets where 3DS is in play, what tools are you using to trade authorization against fraud?**
   *Notes: ____________________________________________*
7. **On the creator side, you hold a large payable balance, run reserves and offer instant payouts in the US. Is the payout experience part of the same roadmap as checkout, or is it owned separately?**
   *Notes: ____________________________________________*
8. **If a team wanted to add a new payment method in a market tomorrow, what does that path look like today and roughly how long is it?**
   *Notes: ____________________________________________*
9. **Who else would need to be in the room for a conversation about routing and processing economics to go anywhere?**
   *Notes: ____________________________________________*
10. **If we built a cost and authorization model on two or three of your non-US markets, what would need to be in it for it to be worth your time?**
    *Notes: ____________________________________________*

# 11. Post-Meeting Checklist

- Send the recap email the same day. Confirm what you heard, restate the agreed next step with a date, attach nothing he did not ask for.
- Log the outcome and every new fact learned, especially **Paul Pasion's title and remit**, and who owns payment routing.
- Put the agreed working session on the calendar before the end of the day, with the routing owner invited.
- Update memory: create `project_eventbrite.md` (Bending Spoons ownership, five-vendor stack, merchant-of-record model, LatAm and APAC card-only, contact map) and add the pointer line to `MEMORY.md`.
- Update this file with the outcome, then commit and push.
- Cross-link to the Bending Spoons account: Eventbrite is the strongest single proof point in a portfolio pitch covering Vimeo, WeTransfer, AOL and Meetup.

---

## Appendix: Sources

- Eventbrite FY2025 Form 10-K, filed 2026-03-12: https://www.sec.gov/Archives/edgar/data/1475115/000147511526000005/eb-20251231.htm
- Eventbrite Exhibit 21.1, Subsidiaries: https://www.sec.gov/Archives/edgar/data/1475115/000147511526000005/exhibit211-subsidiariesofr.htm
- Merger completion 8-K, 2026-03-10: https://www.sec.gov/Archives/edgar/data/1475115/000114036126008636/ef20067526_8k.htm
- Definitive merger proxy (DEFM14A), 2026-01-28: https://www.sec.gov/Archives/edgar/data/1475115/000114036126002685/ny20061430x2_defm14a.htm
- Merger announcement 8-K, 2025-12-02: https://www.sec.gov/Archives/edgar/data/1475115/000119312525304531/d86117d8k.htm
- Bending Spoons IPO prospectus (424B4), 2026-07-01: https://www.sec.gov/Archives/edgar/data/2004711/000110465926079884/tm2613674-14_424b4.htm
- Eventbrite Sub-Processors: https://www.eventbrite.com/help/en-us/articles/891292/eventbrite-subprocessors/
- Eventbrite Merchant Agreement: https://www.eventbrite.com/help/en-us/articles/346993/eventbrite-merchant-agreement/
- Comparing payment processing options: https://www.eventbrite.com/help/en-us/articles/705340/comparing-payment-processing-options/
- Verify financial information through Stripe: https://www.eventbrite.com/help/en-us/articles/856831/verify-your-financial-information-through-stripe/
- Ticketing fees by country: https://www.eventbrite.com/help/en-us/articles/755615/how-much-does-it-cost-for-organizers-to-use-eventbrite/
- Chargebacks: https://www.eventbrite.com/help/en-us/articles/545999/how-does-eventbrite-handle-chargebacks/
- Event payouts: https://www.eventbrite.com/help/en-us/articles/640593/get-started-with-event-payouts/
- Eventbrite product updates feed: https://www.eventbrite.com/product-updates/
- Layoffs, 2026-04-13: https://finance.yahoo.com/markets/stocks/articles/bending-spoons-cuts-eventbrite-staff-210453148.html
- Julia Hartz interview, 2026-05-03: https://fortune.com/2026/05/03/eventbrite-ceo-julia-hartz-sold-company-500-million-without-job-since-15-learning-chess-eyeing-internships/
- Bending Spoons IPO pricing, 2026-07-01: https://www.investing.com/news/stock-market-news/bending-spoons-prices-ipo-at-29-per-share-on-nasdaq-432SI-4769553
- Ferrari on secondary ticketing: https://www.musicbusinessworldwide.com/eventbrite-eyes-jump-into-secondary-ticketing-market-after-500m-acquisition-by-bending-spoons/
- BR-DGE and Resident Advisor, Feb 2025: https://br-dge.to/press/br-dge-to-power-payments-for-resident-advisors-enhanced-ticketing-platform/
- Ticketmaster and PayPal/Braintree: https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/
- Live Nation FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1335258/000133525826000009/lyv-20251231.htm
- Fever acquires DICE, 2025-06-05: https://newsroom.feverup.com/en-US/250537-fever-and-dice-join-forces-to-build-a-live-entertainment-tech-powerhouse/
- DICE standard ticket terms (Stripe): https://support.dice.fm/article/286-standard-ticket-terms
- Pix statistics (Central Bank of Brazil, via): https://en.wikipedia.org/wiki/Pix_(payment_system)
- Bizum: https://en.wikipedia.org/wiki/Bizum
- Internal: data/research/bending-spoons-2026-06-17.md and data/research/stubhub-2026-07-09.md
- Live checkout and 3DS flags probed directly on eventbrite.com across 12 locales, 2026-08-03.

*Method note: Gmail and Glean connectors were not authorized in this session and Gong is not configured, so no email or call history is reflected. Web search budget was exhausted during research; the strongest findings come from direct reads of SEC filings and Eventbrite's own live pages and checkout payloads.*
