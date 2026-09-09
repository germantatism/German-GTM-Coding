# Meeting Brief: Yuno <> PALCO
**Wednesday, September 9, 2026 · 8:00 to 9:00 AM Bogotá (GMT-5) · 3:00 PM Madrid · 7:00 AM Mexico City**
Google Meet: https://meet.google.com/rsb-uhvx-ffz
Event: "Yuno / PALCO - Demo & Payment Orchestration Review" · organized by Patricio Villalobos (pvilla@pal.co) · created Sep 7, 2026

**Objective, what winning looks like:** leave with a signed-off pilot scope and a named technical owner on PALCO's side, having answered all six of Patricio's written questions and having reframed Yuno from a cost line into a payments revenue line for PALCO. Do not leave without a date for the technical deep dive.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state as fact in the call · 🔍 ask in discovery

---

## ⚠️ PRE-MEETING ACTIONS

1. **Reconcile the volume numbers before quoting anything.** Patricio's three headline figures cannot all be true at once (Section 4). The pricing you modelled today uses $37.09 as average order value; the evidence says $37.09 is the average TICKET and an order carries roughly four tickets. This changes modelled TPV from $8.7M to about $36M per month and the take rate from 21.0 bps to about 5 bps. Ask before you quote.
2. **Susana Awad has not responded to the invite** (status: needsAction as of Sep 8, 21:52 UTC). She is the one who runs Yuno dashboard-overview sessions in your other deals. If she is driving the demo, confirm today.
3. **Saman Mortazavi is not on the invite.** He was cc'd on the original thread as "nuestro manager basado en México" and Mexico is 46% of PALCO's transactions and $211M of GTV. Decide with Magdalena whether to add him.
4. **Get a five-minute download from Magdalena on the July 30 call.** Gong holds this account but has **zero recorded calls** (11 emails only), so there is no transcript of the first conversation and no record of the pilot that was discussed.
5. **Fix the billing currency in the pricing sheet.** It is currently set to COP with a 10% local-invoice premium, almost certainly a leftover template default. PALCO is Spain plus Mexico.
6. **Javier Sánchez (SSE) was added to the invite** and never appeared in the email thread. He is the engineer who will stress-test the API answers. See Section 2.
7. **Logistics:** you and Magdalena are both at the Yuno Cancún offsite (Sept 7 to 10). Book a quiet room and test the connection before 8:00.
8. **Permission gate:** the GoFundMe marketplace reference is the on-point proof for Patricio's split-payments question, but per the standing rule you need permission before sharing details. Get it today or speak only in generic terms.

---

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. **Patricio has already diagnosed the problem and named the solution.** His words, Sept 2: "en México, que es la mitad de nuestro volumen, la aprobación en tarjeta está entre 56% y 68% según el procesador. Es exactamente lo que esperamos resolver con ruteo inteligente y reintentos." You are not selling the concept of orchestration. You are proving Yuno executes it and pricing it. ✅
2. **September is the decision window.** Also his words: "septiembre es cuando estaremos definiendo el camino a seguir en nuestro orquestamiento de pagos." The real competitor is PALCO's own engineering roadmap. ✅
3. **PALCO's Mexican card approval is below the Mexican market, not just below Spain.** Openpay 58.0%, Banorte 59.6%, Santander 56.1% against a Mexican market benchmark of roughly 72% credit and 69% debit. This is a configuration and routing problem, not a country problem. ✅
4. **They built their own orchestration layer:** 50+ native gateway integrations across 18 markets, published on their own site, maintained in house by a team of roughly 42 to 47 people. Never call this a gap. It is the asset you plug into. ✅
5. **New PE ownership, new mandate.** Bocel Private Equity plus Mexican entrepreneurs Patricio Villalobos and Miguel Ramírez Lombana acquired PALCO in Oct/Nov 2025, with a stated plan to enter more LatAm markets by mid-2026. Patricio is an owner, not an employee, and he is in the room. ✅

### Three hooks, in priority order

**Hook 1, the one that matters: turn payments from a cost into PALCO's next revenue line.**
The approval uplift lands mostly with the tenants, because each tenant is merchant of record. PALCO captures only its per-ticket fee on the incremental tickets. So the commercial design question is not "what does Yuno cost", it is "how does PALCO monetize a payments layer it now controls". Even 30 bps on $457M of TPV is about $1.37M a year of new revenue against roughly $220K a year of Yuno cost. For a PE-backed company that must show revenue growth, this converts a procurement conversation into a product-strategy conversation. That is the CEO-level frame for Patricio.

**Hook 2: their own numbers prove the platform is not the problem.**
Same codebase, same checkout: Spain runs Redsys at 88.1% and ECI at 99.7%, Dominican Republic runs UepaPay at 98.0%, the US runs Authorize.net at 90.3%. Mexico runs 56% to 60%. And inside a single provider, Mercado Pago's wallet rail approves at 92.1% while its card rail approves at 67.9%, a 24-point gap. Routing and rail selection is the variable.

**Hook 3: BIN-level routing is how they compete with Ticketmaster in Mexico.**
Patricio's sixth question asks about processing by specific bank BIN for pre-sale promotions. In Mexico, bank pre-sales with meses sin intereses are the standard mechanic: Banamex runs pre-sales with Ticketmaster and OCESA and launched a dedicated LineUp concert card in Sept 2025, with Santander and Banorte running their own. If PALCO cannot execute bank pre-sales cleanly, it loses Mexican venues to Ticketmaster. Yuno routing rules key on BIN. This is commercial, not technical.

### THE objection they will raise, and the answer

> "We already built and maintain 50+ gateway integrations ourselves. Why add a layer, a dependency and a per-transaction cost?"

**Answer, using the RBP structure:**
*Requirement:* the connectors are the commodity. What produces approval is the decision layer above them: which rail, in what order, with which retry, under which authentication, per BIN and per issuer, updated continuously as issuers change behaviour. That layer is a full-time product, not a project.
*Benefit:* you keep every integration and every commercial relationship you negotiated. Yuno sits above them and makes the routing decision, and adds the rails you have not built.
*Proof:* at your own numbers, moving your three Mexican card rails up by just 2 points recovers about 20,000 transactions a year, roughly $743K of GTV, against an all-in Yuno cost near $220K a year. Getting them merely to the level Mercado Pago already achieves for you in the same market, 67.9%, is about $3.49M a year. And InDrive went live across 10 LatAm markets in under 8 months at 90% approval.

Never say they lack anything. The line is: "you built the hard part; we keep it alive and add the brain."

### The ask

A **scoped pilot in Mexico**, on the three underperforming card rails (Openpay, Banorte, Santander), with a defined approval baseline and a fixed review date, plus a named technical owner and a calendar date for the deep dive with Fernando and Javier.

### Rapport opener

Patricio closed the last thread with "venga!" and an emoji, and joked in August about disappearing on holiday without replying. He is informal and fast. Open in Spanish, warmly, and thank him for the data dump specifically: almost no prospect sends approval rates broken out by processor unprompted. Then say you did the arithmetic on it, and start with the Mercado Pago wallet-versus-card gap. That single observation proves you actually read it.

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status |
|---|---|---|---|
| Patricio Villalobos Cuevas | CEO, co-owner | PALCO | Accepted, organizer |
| Fernando Nava Feldman | VP of Engineering | PALCO | Accepted |
| Javier Sánchez | Senior Software Engineer (SSE) | PALCO | Accepted, added to invite, never in email thread |
| Magdalena Torrealba Zozaya | Global Sales Strategy Associate | Yuno | Accepted, relationship owner |
| German Tatis | Business Development Manager | Yuno | Accepted |
| Susana Awad | Yuno (runs dashboard-overview sessions) | Yuno | ⚠️ Not responded |
| Saman Mortazavi Camacho | Yuno manager based in Mexico | Yuno | ⚠️ Not invited, was on original thread |

### Patricio Villalobos Cuevas, CEO and co-owner
Signs as "CEO - PALCO" with a Spanish mobile (+34 669 561085), so he is operating out of Madrid. ✅ He is one of the Mexican entrepreneurs who acquired PALCO with Bocel Private Equity in Oct/Nov 2025, and he co-founded mediotiempo.com, the Mexican sports site sold to Time Warner in 2010, and juanfutbol in 2014. ✅ Sourced from acquisition coverage: https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/ and https://techla.pro/2025/10/31/22111/

**How to read this person:** a media-and-internet founder turned owner-operator, not a career payments executive, yet he personally wrote a six-point technical agenda covering split payments, 3DS, tokenization, multi-tenant billing, PCI scope and BIN routing. He is commercially sharp and technically literate, he moves in bursts, and he owns the outcome. Sell him the business case; let Fernando and Javier interrogate the mechanics. He is the one who will decide build versus buy this month.

### Fernando Nava Feldman, VP of Engineering
Named by Patricio as attending: "participaríamos Fernando (VP of Engineering)". ✅ He has been cc'd on every message in the thread since July and has never written, which usually means he is reading closely and reserving judgement.

**How to read this person:** the person whose team built the 50+ integrations. Your framing must protect that work explicitly, because "replace what you built" is the fastest way to lose him. He is also the person who will own the migration effort and therefore the one most sensitive to integration cost and to the direct-API-versus-SDK question.

### Javier Sánchez, Senior Software Engineer
Named by Patricio as "Javier Sánchez (SSE)". ✅ He was added to the calendar invite but never appeared in the email thread, so he arrives without context.

**How to read this person:** the hands-on implementer. He will ask the concrete questions: what the API actually returns, how retries are triggered, how tokens move between processors, what changes in PALCO's code. Have Susana or a solutions engineer ready for depth. Do not let a vague API answer stand in front of him.

⚠️ **LinkedIn profiles for all three could not be retrieved in this session** (LinkedIn blocks automated fetches and the session's search budget was exhausted). Pre-meeting action: open manually and skim before the call. Best-guess searches: `site:linkedin.com/in "Patricio Villalobos" PALCO`, `site:linkedin.com/in "Fernando Nava" Palco`, `site:linkedin.com/in "Javier Sánchez" Palco4`.

### The sponsor and intro path
Magdalena Torrealba owns this relationship end to end. She ran the first call on July 30, requested the operating data on July 31, and proposed this slot. Patricio's welcome, "bienvenido German al equipo", means you are being introduced into an existing, warm relationship. Let Magdalena open and hand over; do not restart the relationship.

### Relationship timeline

| Date | Event |
|---|---|
| Jul 30, 2026 | First call, Magdalena and Patricio. A **pilot** was discussed. ⚠️ No Gong recording exists, no transcript. |
| Jul 31, 2026 | Magdalena requests volume, ticket, TPV, method mix, countries, approval rate by method, fraud and chargebacks. Mentions Saman as the Mexico-based manager and the intent to "preparar una propuesta para el piloto que discutimos". |
| Aug 18, 2026 | Patricio apologises, was on holiday. |
| Sep 2, 2026 | **Patricio sends the full data set plus six questions.** The substantive event of this deal. |
| Sep 4, 2026 | Magdalena acknowledges, forwards to German, proposes Wed Sep 9. |
| Sep 7, 2026 | Patricio confirms and sends the invite. German introduces himself. Patricio: "venga!" |
| Sep 9, 2026 | This meeting. |

**Implication:** this is a follow-up, not a first meeting. They already asked for a proposal for a pilot, and they have already given you their numbers. Re-asking discovery basics will cost you credibility. Come with the analysis done.

---

## 3. THE COMPANY

PALCO, formerly Palco4, is a white-label B2B ticketing platform: promoters, venues and clubs sell under their own brand on PALCO's technology. Legal entity **PALCO4 TECNOLOGIA Y SERVICIOS SL**, CIF B87730628, Registro Mercantil de Madrid, HQ Calle Copenhague 4, Las Rozas de Madrid. ✅ The company rebranded from Palco4 to PALCO at **pal.co** (verified live redirect chain palco4.com → palcoticketing.com → pal.co).

| Metric | Value | Source |
|---|---|---|
| Venues | 500+ | https://techla.pro/2025/10/31/22111/ |
| Countries | 30 claimed | https://techla.pro/2025/10/31/22111/ |
| Tickets | 8M+ per year (registry listing); 50M+ lifetime claimed | https://www.einforma.com/informacion-empresa/palco4-tecnologia-servicios |
| Employees | 15 (2023, registry) → 42 to 47 (2026) | einforma; https://tracxn.com/d/companies/palco4/__3EL-njJanf8X9S1gb-Axu7-Iei34VOWsC8_n2Xt20PY |
| Payment gateways | 50+ native integrations, 18 markets | https://es.pal.co/es/home |
| TPV last twelve months | ~$457M USD | Patricio, email Sep 2, 2026 |
| Business model | Fee per ticket sold, "pay only for the tickets you sell" | https://www.capterra.com/p/200482/Palco4/ |

**2025 marquee on-sales, vendor-claimed** (https://en.pal.co/en/home): Bad Bunny DTMF Tour Dominican Republic, three sellouts in 8 hours; Tini Futttura Tour Argentina, 200K+ tickets in 18 hours; Don Omar Mexico, 200K+ in 24 hours; Shakira Uruguay, 86K in 48 hours. These spikes are why routing failover matters to them commercially.

### Corporate structure

| Entity / market | Status | Note |
|---|---|---|
| PALCO4 TECNOLOGIA Y SERVICIOS SL (Spain) | ✅ Confirmed | The only legal entity found |
| Mexico, Argentina, DR, Puerto Rico | ⚠️ No local entity found | pal.co footer names no entity; privacy policy names none |
| Merchant of record | ✅ **The tenant, not PALCO** | Stated by Patricio: "cada tenant es merchant of record y gestiona fraude y contracargos directamente con su procesador" |

The MoR structure is the single most important structural fact in this deal. It determines who benefits from approval uplift, how splits must work, how billing must work, and how PCI scope falls. Every commercial answer must be consistent with it.

### Leadership and strategy
Owners since Oct/Nov 2025: Bocel Private Equity (fund directed by Roberto Terrazas and René Fernández) with Patricio Villalobos Cuevas and Miguel Ramírez Lombana. Stated post-deal strategy: accelerate international expansion, strengthen LatAm and Spain, white-label stores, dynamic pricing, ticket upgrades, omnichannel and data. Ramírez's stated ambition: "PALCO can become the silent infrastructure driving the live events industry." That phrase is worth echoing, because infrastructure is exactly what you are selling him.

---

## 4. THE NUMBERS PATRICIO SENT

Everything below is from Patricio's email of September 2, 2026. This is first-party data, not research. Treat it as confidential.

### 4A. Volume and mix

| Metric | Stated value |
|---|---|
| TPV last twelve months | ~$457M USD |
| Average ticket | $37.09 USD |
| Monthly average | ~235,000 transactions / ~$28.3M USD |

**Method mix on annual TPV:** card 75.7% ($346M), cash including OXXO and Paynet 13.2% ($60M), physical pinpad at the box office 6.3% ($29M), transfer 3.0% ($14M), other wallets/BNPL/gift cards 1.8% ($8M).

**Annual GTV by country:** Mexico $211M, Argentina $62M, Spain $55M, Dominican Republic $36M, Puerto Rico $31M, Paraguay $26M, Panama $12M, Honduras $5M, Guatemala $4.8M, USA $4.6M, rest ~$3M.

### 4B. ⚠️ The three numbers do not reconcile. Fix this before you quote.

- 235,000 transactions × $37.09 = **$8.72M per month**, not the $28.3M stated.
- $28.3M per month × 12 = **$340M**, not the $457M stated.
- The monthly country table sums to $28.17M but **omits Spain, Puerto Rico and Panama entirely**, which are $55M, $31M and $12M annually. Adding them back gives roughly $36.4M per month, about $437M annualised, which does reconcile with $457M.
- The processor table sums to **3,087,600 transactions**, roughly 257,300 per month. $457M ÷ 3.09M = **about $148 per transaction**, which is almost exactly four tickets at $37.09.

**Most likely reading ⚠️:** $37.09 is the average **ticket**, while a transaction is an **order carrying about four tickets**. Confirm live.

**Why this matters commercially:** the deal model you built today uses $37.09 as average order value, producing monthly TPV of $8,716,150 and a take rate of 21.0 bps. If real TPV is around $36M per month, the take rate is closer to **5 bps**, and the take-rate controller in the governance score (15% weight, currently scoring 100 against a 15 bps expectation for V3) would fall sharply, potentially moving the deal from GREEN toward YELLOW. It also means transaction volume may be understated by roughly 10%, since the processor table implies 257,300 per month rather than 235,000.

### 4C. Approval rate by processor, and what the arithmetic says

| Processor | Market | Transactions | Approval | Declined |
|---|---|---|---|---|
| Mercado Pago v2 | AR/MX | 754,700 | 67.9% | 242,259 |
| Openpay Tarjeta | MX | 506,700 | **58.0%** | 212,814 |
| Redsys Tarjeta | ES | 500,300 | 88.1% | 59,536 |
| Banorte Tarjeta | MX | 420,400 | **59.6%** | 169,842 |
| Authorize.net | US | 210,400 | 90.3% | 20,409 |
| UepaPay | DR | 153,100 | 98.0% | 3,062 |
| Cybersource | multi | 109,800 | 63.7% | 39,857 |
| Santander | MX | 74,800 | **56.1%** | 32,837 |
| Mercado Pago Wallet | AR/MX | 72,900 | 92.1% | 5,759 |
| Stripe | multi | 55,900 | 57.4% | 23,813 |
| Fiserv | UY | 48,100 | **43.7%** | 27,080 |
| ECI | ES | 42,000 | 99.7% | 126 |
| Pixel Pay | HN | 39,900 | 52.3% | 19,032 |
| Recurrente | GT | 39,200 | 88.7% | 4,430 |
| Bancard | PY | 30,300 | 58.1% | 12,696 |
| Line | VE | 29,100 | **8.7%** | 26,568 |
| **TOTAL** | | **3,087,600** | **70.85% blended** | **900,120** |

**What this table says, computed from their own figures:**

1. **900,120 declined transactions a year.** At $37.09 per ticket that is about $33.4M of failed attempts; if a transaction is really a four-ticket order at roughly $148, it is closer to $133M.
2. **The three Mexican card rails run at a combined 58.5%** (1,001,900 attempts, 586,407 approved, 415,493 declined). The Mexican market benchmark is roughly **72% credit and 69% debit** (RankingsLatAm, Sept 2024 data). PALCO is 10 to 16 points below its own market. ✅ This is the most important sentence in the brief.
3. **Mercado Pago's wallet approves 24.2 points higher than its card rail** through the same provider, 92.1% against 67.9%. Rail selection alone is worth real money.
4. **Line in Venezuela approves 8.7%.** 26,568 declines on 29,100 attempts. Venezuela does not even appear on PALCO's public gateway map. Worth raising gently as evidence that nobody is watching the tail.
5. **Fiserv at 43.7% and Pixel Pay at 52.3%** are the other outliers. Pixel Pay is also absent from their public map, which lists Honduras as Cybersource and PayPal, so the public map is behind the real stack.

**Illustrative uplift on the three Mexican card rails** (1,001,900 attempts a year, at $37.09 per ticket):

| Scenario | Extra approved transactions | Recovered GTV per year |
|---|---|---|
| +2 points | 20,038 | ~$743K |
| +5 points | 50,095 | ~$1.86M |
| +7 points | 70,133 | ~$2.60M |
| Up to Mercado Pago's own 67.9% (+9.4 points) | 94,179 | ~$3.49M |

Against an all-in Yuno cost of about **$220K a year** at the price you modelled. Even the +2 point case pays for the platform three times over. Present these as arithmetic on their numbers, clearly labelled as illustrative, never as a Yuno guarantee.

⚠️ Do not compare Mexico to Spain as a target. Mexican issuer behaviour is structurally different, and Spain's 88% to 99% is not a reachable Mexican number. Use Mexico's own market benchmark and PALCO's own best Mexican rail as the goalposts.

### 4D. Fraud and chargebacks
Patricio: "Hoy no tenemos ese dato consolidado: cada tenant es merchant of record y gestiona fraude y contracargos directamente con su procesador. Es una de las razones por las que nos interesa centralizar la capa de pagos."

They have **no consolidated fraud or chargeback visibility at all**. That is an opening for the Yuno fraud and reporting layer, and it is a live risk for them: a platform that cannot see chargeback ratios across tenants cannot see a tenant heading for a monitoring programme. Useful benchmark to offer: Mexican ecommerce chargebacks ran at about 0.37% of volume on credit and 0.30% on debit (RankingsLatAm, Sept 2024).

---

## 5. THE SIX QUESTIONS, AND YOUR ANSWERS

Patricio wrote these out. They are the real agenda. Prepare all six; do not improvise the ones marked 🔍.

**1. Split payments in Mexico: which processors support commission split at capture, with the tenant remaining MoR and PALCO retaining its fee.**
Yuno has a documented Split Payments Marketplace product: split rules defined per recipient, absolute or auto-calculated, percentage, fixed or mixed; recipients can be configured against more than one provider; onboarding transfers and standalone transfers are supported (https://docs.y.uno/docs/payment-features/split-payments-marketplace). ✅
🔍 **The structural nuance to raise, not dodge:** Yuno's marketplace model normally has the platform collecting and recipients onboarded beneath it. PALCO's model inverts that: the tenant is MoR and PALCO takes a fee out of the tenant's own collection. Confirm which Mexican processors support that direction at capture rather than by later transfer. Take this away and come back precisely; do not guess in front of Javier.
Yuno has a live marketplace merchant in production since Feb 2026 doing splits, recipients and transfers across three processors. ⚠️ **Get permission before naming the client.**

**2. Mandatory 3DS on all card flows and how it interacts with routing.**
🔍 **This may be the single biggest cause of their Mexican approval problem, and it is the highest-value question you can ask.** Ask: is 3DS on 100% of card flows a requirement of their acquirers, a requirement their tenants impose, or PALCO's own decision? If it is PALCO's own choice, applying it selectively is likely worth more than any routing change. Mexico has lagged on 3DS 2.0 issuer migration, so blanket 3DS in a market with uneven 2.0 coverage drives exactly the 56% to 60% pattern they are seeing.
Timely and specific: **Mastercard's updated 3DS data requirements took effect on 1 April 2026 with a compliance deadline of 1 July 2026**, roughly ten weeks ago, and richer authentication data is associated with a 4 to 6 point improvement in authentication success. Ask whether they are sending the full field set. Fernando and Javier will respect the question.
Sources: https://www.pci-proxy.com/blog-posts/3d-secure-mandates-by-country-which-markets-require-3ds-in-2026 and https://shuftipro.com/blog/mastercard-3ds-data-mandate-2026/

**3. Tokenization and recurring charges for abonos and subscriptions with Mexican processors.**
Yuno Subscriptions processes recurring charges on CARD, PAYPAL_ENROLLMENT and PIX_AUTOMATIC through vaulted instruments; tokenization is required, failed renewals move to PAST_DUE and recover when a later charge succeeds (https://docs.y.uno/docs/payment-features/subscriptions). ✅ The commercial differentiator against Stripe Billing is that the subscriptions engine is multi-PSP: adding a processor is one connection rather than a new integration. Yuno also sells Network Tokens as a product line (creation and update priced separately), which matters for season-ticket renewals: network tokens survive card reissue, which is exactly the failure mode that kills annual abono renewals.
🔍 Mexican-processor coverage for recurring is not stated in the public docs. Confirm before promising.

**4. Commercial model for multi-tenant: how it is contracted and billed per tenant.**
This is where Hook 1 lives. Do not answer it as a billing-mechanics question. Answer it as: "you can buy this as a cost and absorb it, or you can package it and sell it to your tenants." Then walk the arithmetic: 30 bps on $457M is about $1.37M a year of new PALCO revenue against roughly $220K of cost. See Section 6 for the price you are cleared to quote.

**5. Direct API integration rather than embedded SDK, and the resulting PCI scope for PALCO.**
Be straight: if PALCO captures the PAN in its own front end and posts server-side, PALCO carries full PCI DSS scope, SAQ-D or Level 1 with an annual assessment. Direct API is supported; the scope consequence is real. The way to keep direct API everywhere else while cutting scope is to let the card capture happen inside a Yuno-hosted field or vault call, with every other interaction staying server-to-server. Present it as a choice with a cost, not as a blocker.
🔍 Relevant context: **no public PCI DSS certification for PALCO could be found anywhere** (site, privacy policy, archived pages). If they do not hold a current AOC, this question is more urgent for them than they may realise. Ask what their current attestation is rather than asserting anything.

**6. Processing by specific bank BIN for special pre-sale promotions.**
Straightforward yes on the routing engine, and commercially the most interesting of the six. Bank pre-sales with meses sin intereses are the standard Mexican ticketing mechanic: Banamex runs pre-sales with Ticketmaster and OCESA and launched a dedicated LineUp concert credit card in Sept 2025; Santander and Banorte run their own; MSI is typically 3, 6 or 12 months above a minimum spend. BIN-level routing lets PALCO pitch venues the same bank-pre-sale capability Ticketmaster offers.
Sources: https://www.elfinanciero.com.mx/economia/2025/09/18/banamex-lanza-tarjeta-de-credito-lineup-especial-para-preventas-de-conciertos-estos-son-los-requisitos-y-beneficios/ and https://blog.kardmatch.com.mx/preventa-banamex

---

## 6. COMMERCIAL POSITION

You modelled this deal today in "Yuno — Pricing Palco". Current state:

| Line | Modelled |
|---|---|
| Monthly platform fee | $10,000 (suggested $10,000, green down to $6,325, floor $4,000) |
| Pay-ins | 235,000 tx at blended **$0.0354** (3-tier ladder: $0.0427 / $0.0362 / $0.0314), green down to $0.0188, floor $0.0100 |
| **Total quoted** | **$18,320 per month, about $220K per year** |
| Gross margin | 93.6% |
| Modelled TPV / take rate | $8,716,150 per month / 21.0 bps |
| **Governance** | **Score 89.5 → GREEN. "None — book it."** No approvals needed. |

**Priced but not quoted, your upsell room:** Yuno 3DS at $0.0403 (100,000 monthly attempts modelled = $4,032/mo), Fraud Engine at $0.0184 (20,000 calls = $367/mo), Network Tokens creation $0.2973 and update $0.0595, Subscriptions $0.0369, Pay-outs $0.0532, Card Account Updater $0.3235, Reconciliation $0.0188, Risk conditions $0.0139.

Given Section 4D, **3DS and Fraud are the two obvious attachments**: they have no consolidated fraud view, and 3DS sits at the centre of their approval problem.

⚠️ **Two cautions.** First, billing currency in the sheet is set to COP with a 10% local-invoice premium; fix it. Second, if the TPV reconciliation moves take rate from 21 bps to about 5 bps, the take-rate controller drops and the 89.5 score can fall below the 80 pass mark, which would change GREEN to YELLOW and require approval. Quote indicatively today and confirm after the volume is settled.

The ladder is worth defending: it produces $8,320 a month against $7,378 for the cliff, 12.8% better, and it also tells a better story to a customer whose volume is spiky.

---

## 7. COMPETITIVE LANDSCAPE

Patricio will not ask about competitors, so keep this in your pocket. The one genuinely useful pattern is in the right-hand column: **every ticketing player in this market runs an agent model rather than merchant of record, and the ones who solved it did so on a marketplace payments architecture.** That validates PALCO's structure as industry-normal and makes the split-payments question the vertical's central payments problem, not a PALCO quirk.

**Market denominator, Spain live music ticket sales:** €578M (2023) → €725.6M (2024, +25.32%) → over €800M (2025). Source: APM Anuario de la Música en Vivo via https://portaldelamusicaenvivo.com/la-musica-en-vivo-en-espana-factura-mas-de-725-millones-de-euros-en-2024-la-mayor-cifra-jamas-registrada/ and https://www.dodmagazine.es/anuario-de-la-musica-en-vivo-2026/

| Company | Segment | Market share (source and basis) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| **Ticketmaster México / OCESA (Grupo CIE)** | B2C, Mexico | No estimate available | Dominant Mexican promoter and ticketer | Owns promotion and venues; Banamex pre-sale partnership | Bank pre-sales with MSI as the core mechanic |
| **Fever (Kzemos Technologies SLU)** | B2C, own IP | No estimate available. A raw €74M ÷ €725.6M = 10.2% is **not** a valid share: Kzemos is the group's global ops hub (CNAE 8299) and Fever's Candlelight/immersive mix sits outside the live-music denominator | Revenue €14.5M (2020) → ~€74M (2024); 1,420 staff; FY24 loss €36.6M, negative equity −€32.5M; $1.8B valuation Jan 2023 with Goldman Sachs | Originates its own IP and controls demand via a discovery app | **"Limited payment collection agent", explicitly not MoR.** Two entities: Kzemos SLU (EU) and Fever Labs Inc (US). PSP deliberately undisclosed |
| **Atrápalo** | B2C, multi-vertical OTA | No estimate available; entradas revenue is not broken out | €233M group revenue FY2023, Spain €155M; ~2M tickets/year in the entertainment vertical. ⚠️ Press "facturación" is GMV; the registry shows €97.9M statutory sales for Spain 2024 | Ticketing as one vertical of an OTA, plus a SMART subscription | Not verified, JS-rendered legal pages would not load |
| **DICE (DICE FM SLU, Spain)** | B2C, mobile-first | No estimate available; no Spain figures disclosed | $122M Series C at $400M valuation (Sept 2021, SoftBank); ~480 staff group-wide | App-locked QR tickets, no secondary market, face-value waiting list | **Stripe Connect, named explicitly** in its terms. Disclosed agent, not MoR. Settlement 5 business days, 5% chargeback holdback for 6 months |
| **Wegow** | B2C, discovery-led | Derived proxy only: €3.9M ÷ €578M = **0.67%** (FY2023); €16.6M ÷ €458.7M = 3.62% (FY2022). ⚠️ Basis undisclosed (gross vs net), 19 countries against a Spain-only denominator | Revenue peaked €16.6M (2022), collapsed to €3.9M (2023); never profitable in 10 years; €4.9M short-term debt | Artist-following and recommendations bolted onto ticketing | Intermediary, not MoR. Hybrid: some events run on **the organiser's own gateway**. "CES" 3DS branding suggests Redsys ⚠️ inferred |
| **vivenu** | B2B white-label | No estimate available | 1,000+ organizers, 50+ countries, 50,000+ events/yr | API-first enterprise white-label | Not disclosed |
| **SecuTix (ELCA)** | B2B white-label | No estimate available | 204 live customer sites, 75M tickets/yr | Sports, live and culture | Runs its **own** payment product, S-PAY, built in house |
| **Tixly** | B2B white-label | No estimate available | Performing-arts venues, Northern Europe | Cultural-venue specialist | Not disclosed |
| **TuBoleta** | B2C, Colombia | No estimate available | 26+ years; Movistar Arena, DAVIarena | Colombia incumbent | Not disclosed |
| **PuntoTicket** | B2C, Chile | No estimate available | Estadio Nacional, Claro Arena, Teatro Caupolicán | Chilean major-venue exclusives | Not disclosed |
| **Superboletos / eTicket / Boletia** | B2C, Mexico | No estimate available | eTicket runs a physical POS network across several states | Promoter-aligned Mexican ticketers | Not disclosed |
| **Joinnus** | B2C, Peru | No estimate available | Peru events platform | Single-market | Not disclosed |

⚠️ No named research house (Statista, Mordor, IBISWorld, 6sense, Datanyze, SimilarWeb) publishes a market-share figure for any Spanish or LatAm ticketing company. Nothing above is an install-base or traffic figure presented as revenue share; where no sourced share exists the row says so.

⚠️ A claim that Fever acquired DICE in June 2025 appears on Wikipedia with a **fabricated citation** (a placeholder example.com URL). It could not be corroborated anywhere. Do not repeat it.

**Where PALCO sits:** it is the only player in this set that is simultaneously white-label B2B and deep in both Spain and LatAm, and the only one publishing a per-country map of 50+ gateway integrations. **For the call:** if the build-versus-buy question surfaces, the useful observation is that SecuTix built its own payment product in house and DICE bought a marketplace architecture off the shelf. PALCO has been on the SecuTix path and is now deciding whether to stay on it.

---

## 8. SELLING YUNO HERE

**Core frame:** PALCO built the distribution and the integrations. Yuno supplies the decision layer above them and turns payments into a product PALCO can sell. Never "replace", always "on top of".

**Proof points, real Yuno cases only:** InDrive, 10 LATAM markets live in under 8 months at 90% approval with 4.5% recovery. Rappi, zero implementation time and 80% less analyst time to resolve, with millisecond detection of processor degradation against 5 to 10 minutes manually, which maps directly to a Bad Bunny on-sale. Livelo, +5% approval and 50% recovery. Reserva, +4% approval in under 3 months.

**Landmines:**
- Do not say they lack an orchestrator. They call their own layer "nuestro orquestamiento de pagos" and they are proud of it.
- Do not promise +7% as a guarantee. Their Mexican gap is probably part 3DS policy and part routing, and you do not yet know the split.
- Do not name the marketplace reference client without permission.
- Do not repeat any prospect's data to another prospect. This account's numbers are confidential and unusually detailed.
- Do not open with "your public gateway map is out of date." True, but it is a gotcha, not a hook.
- Do not re-ask what the emails already answered. They gave you everything on September 2.

---

## 9. BE READY FOR

| They ask | Your answer |
|---|---|
| "What does it cost?" | $10,000 monthly platform fee plus $0.0354 per pay-in transaction blended on a 3-tier ladder, about $18,320 a month at the volume you shared. Cleared internally without further approval. Frame against the $743K to $3.49M of recoverable Mexican GTV. |
| "How long to integrate?" | Direct API, no SDK required. The reference point is InDrive going live across 10 LatAm markets in under 8 months, and Rappi describing effectively zero implementation time on an existing stack. Pin a real number only with a solutions engineer present. |
| "Do we have to move off our processors?" | No. Keep every contract and every integration. Yuno routes across what you already have and adds what you do not. |
| "What happens to PCI?" | Direct API means PALCO stays in scope for capture. Hosted capture or vault reduces it. Honest trade-off, see question 5. |
| "Can you guarantee the approval uplift?" | No guarantee. A measured pilot on the three Mexican rails with a fixed baseline and a review date. That is the point of the pilot. |
| "How do we bill our tenants?" | The commercial design conversation, see Hook 1. Offer to model both absorb and resell. |
| "Who else in ticketing do you run?" | Do not name accounts you lack permission to name. Speak to the live marketplace merchant generically, and to InDrive, Rappi and Livelo by name. |
| "What if Yuno goes down during an on-sale?" | Failover across the processors already connected, plus real-time monitors. Use the Rappi millisecond-detection point. Offer the architecture review with Fernando. |
| "Why not just build the routing ourselves?" | The answer in Section 1. Connectors are a project; the decision layer is a permanent product. |

---

## 10. AGENDA (60 minutes)

| Time | Block | Notes |
|---|---|---|
| 0-5 | Magdalena opens, introduces German. Confirm the six questions are the agenda. | Notes: ____ |
| 5-15 | Your read of their data. Lead with Mercado Pago wallet vs card, then the three Mexican rails against the Mexican market benchmark. Ask the volume reconciliation question here. | Notes: ____ |
| 15-35 | Demo, aimed at the six questions: routing rules, BIN-level rules, retries, failover, observability, splits. Not a generic tour. | Notes: ____ |
| 35-48 | The six questions, in Patricio's order. Flag the two that need follow-up rather than improvising. | Notes: ____ |
| 48-56 | Commercial model. Absorb versus resell. Indicative pricing, conditional on the volume reconciliation. | Notes: ____ |
| 56-60 | Pilot scope, named technical owner, date for the deep dive. | Notes: ____ |

---

## 11. DISCOVERY QUESTIONS

Do not re-ask anything the September 2 email answered.

1. On the numbers: the monthly country table sums to about $28M but leaves out Spain, Puerto Rico and Panama, and $37.09 against 235,000 transactions gives roughly $8.7M rather than $28.3M. Is $37.09 the price of a ticket, with an order carrying about four of them? Notes: ____
2. The 3DS one: is 3DS on 100% of card flows a requirement from your acquirers, something your tenants impose, or PALCO's own policy? Notes: ____
3. Are you sending the full Mastercard 3DS data field set that became mandatory on 1 July? Notes: ____
4. Openpay, Banorte and Santander sit around 56% to 60% while Mercado Pago does 67.9% in the same market. What decides which Mexican rail a given transaction goes to today? Notes: ____
5. Mercado Pago's wallet approves at 92.1% and its card rail at 67.9%. Is the wallet offered with equal prominence at checkout in Mexico and Argentina? Notes: ____
6. Line in Venezuela is approving 8.7%. Is that rail commercially live, or legacy nobody has switched off? Notes: ____
7. When a card payment fails today, what happens? Any retry, any second rail, or does the buyer just see an error and the seat go back? Notes: ____
8. With each tenant as merchant of record and fraud handled tenant by tenant, how would you find out if one tenant's chargeback ratio was heading for a card-scheme monitoring programme? Notes: ____
9. On the pilot Magdalena discussed in July: what would you want it to prove, on which markets, and by when? Notes: ____
10. If payments performance became something PALCO could sell to venues rather than absorb, does that change how you want this contracted? Notes: ____
11. Who has to say yes for a pilot to start, and is that anyone beyond this room, including Bocel? Notes: ____
12. What is your current PCI attestation, and who signs it? Notes: ____
13. What is on the engineering roadmap for payments between now and year end, and what would Yuno displace? Notes: ____

---

## 12. POST-MEETING CHECKLIST

- Recap email same day, in Spanish, to Patricio with Fernando, Javier, Magdalena and Susana copied. Restate the six answers, mark clearly which two are coming back with a written response.
- Log the corrected volume figures and update "Yuno — Pricing Palco" with the true AOV, then re-check the governance score.
- Schedule the technical deep dive with Fernando and Javier before ending the call.
- Send the written answers on split-payments direction and Mexican recurring-processor coverage within 48 hours.
- Update memory: pilot scope, decision makers, whether 3DS is self-imposed, and the real order value.
- Decide with Magdalena whether to bring Saman in for the Mexico conversation.

---

## APPENDIX: SOURCES

**First-party (confidential):** Patricio Villalobos email thread "Palco + Yuno - Próximos Pasos", Jul 31 to Sep 7, 2026; Google Calendar event "Yuno / PALCO - Demo & Payment Orchestration Review"; Gong account record, 11 emails and zero recorded calls; Google Sheet "Yuno — Pricing Palco" (Deal Calculator), Sep 8, 2026.

**Company:** https://es.pal.co/es/home · https://en.pal.co/en/home · https://academy.palco4.net/ · https://pr-usa.palco4.com/prtickets/es/listaEventos · https://www.capterra.com/p/200482/Palco4/

**Registry and corporate:** https://www.iberinform.es/empresa/7298047/palco4-tecnologia-y-servicios · https://www.einforma.com/informacion-empresa/palco4-tecnologia-servicios · https://www.axesor.es/Informes-Empresas/9135019/PALCO4_TECNOLOGIA_Y_SERVICIOS_SL.html · https://tracxn.com/d/companies/palco4/__3EL-njJanf8X9S1gb-Axu7-Iei34VOWsC8_n2Xt20PY

**Acquisition:** https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/ · https://techla.pro/2025/10/31/22111/ · https://www.preqin.com/data/profile/asset/palco/776852

**Payments benchmarks:** https://rankingslatam.com/blogs/industry-news/insights-into-mexico-s-ecommerce-payments-landscape-credit-and-debit-card-trends-chargebacks-and-market-leaders · https://www.pci-proxy.com/blog-posts/3d-secure-mandates-by-country-which-markets-require-3ds-in-2026 · https://shuftipro.com/blog/mastercard-3ds-data-mandate-2026/

**Mexican pre-sale mechanics:** https://www.elfinanciero.com.mx/economia/2025/09/18/banamex-lanza-tarjeta-de-credito-lineup-especial-para-preventas-de-conciertos-estos-son-los-requisitos-y-beneficios/ · https://blog.kardmatch.com.mx/preventa-banamex

**Yuno product:** https://docs.y.uno/docs/payment-features/split-payments-marketplace · https://docs.y.uno/docs/payment-features/subscriptions

**Prior research:** data/research/palco-ticketing-2026-09-08.md
