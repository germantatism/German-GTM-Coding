# Meeting Brief: Yuno <> PALCO, Technical Deep Dive

**Tuesday, September 15, 2026 · 10:00 to 10:45 COT (17:00 Madrid, 09:00 Mexico City) · 45 min**
**Meet:** https://meet.google.com/njo-shpd-gix
**Event:** "Palco + Yuno | Deep Dive" (organizer: German; created Sep 14 after Fernando confirmed the slot by email)

**Objective:** leave with the integration architecture agreed in principle (direct API vs SDK and what each means for PCI scope), the split-payments question either answered or owned with a date, the business-model facts needed to price and package the deal, and a pilot scope in Mexico with a named technical owner. Do not quote pricing in this session.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state in the call · 🔍 ask in discovery

### ⚠️ Pre-meeting actions
1. **Brief Carlos Medina (Implementation Engineer) today.** He confirmed the slot on Slack but asked "me recuerdas el objetivo?" and first confused the account with ProntoPaga. He is the one who will answer Alfonso and Fernando. Send him section 6 (technical plan) and section 5 (the six questions).
2. **Patricio Villalobos (CEO, co-owner, Madrid) is NOT on the invite.** Fernando asked for the slot and said he would forward the invite to his colleagues. Decide now: keep it technical and send Patricio the recap, or add him. Recommendation: keep it technical, and close the meeting by proposing the commercial session with Patricio.
3. **Alvaro (alvaro@pal.co) has not responded and his role is unknown.** Ask at the open.
4. **Javier Sánchez (SSE) is out of office Sep 14 to end of month.** His questions from Sep 9 will be asked by Alfonso instead.
5. **Get permission to use the GoFundMe marketplace reference** (live since Feb 2026: Stripe, Adyen, Tabapay, splits, recipients, transfers). Without it, speak only in generic terms on split payments.
6. **Reconcile the volume numbers before anyone quotes anything** (see section 3). This changes take rate from 21 bps to about 5 bps and can move the deal from GREEN to YELLOW.
7. **Ask Magdalena for the Fireflies notes of Sep 9.** The recording is hers (not in Gong). The auto-summary mentions "cross-border local is not supported" and "merchant of record responsibilities include token procedure"; you need the exact context before Alfonso quotes it back to you.

---

## 0. What you must know cold, no excuses

1. **Each tenant (promoter or venue) is merchant of record.** Patricio, Sep 2: "cada tenant es merchant of record y gestiona fraude y contracargos directamente con su procesador." PALCO earns a fee per ticket sold. The approval uplift lands with the tenant, not with PALCO. That is why the commercial design question is "how does PALCO monetize the payments layer," not "what does Yuno cost." ✅
2. **Their numbers, as sent:** TPV last twelve months about $457M USD, average ticket $37.09, about 235,000 transactions and $28.3M per month. ✅
3. **The three numbers do not reconcile.** 235,000 × $37.09 = $8.7M, not $28.3M. The processor table sums to 3,087,600 transactions a year (about 257,300 a month) and $457M ÷ 3.09M = about $148 per transaction, which is four tickets at $37.09. ⚠️ Most likely $37.09 is the ticket and a transaction is an order of about four tickets. Confirm live.
4. **Mexico is the deal:** $211M of GTV, about 46% of transactions. The three Mexican card rails run at **Openpay 58.0%, Banorte 59.6%, Santander 56.1%**, a combined 58.5% on 1,001,900 attempts, against a Mexican market benchmark of roughly 72% credit and 69% debit. That is 10 to 16 points below their own market. ✅
5. **Inside one provider, rail selection is worth 24 points:** Mercado Pago Wallet approves at 92.1%, Mercado Pago card at 67.9%. ✅
6. **900,120 declined transactions a year, blended approval 70.85%.** Tail outliers: Line (Venezuela) 8.7%, Fiserv (Uruguay) 43.7%, Pixel Pay (Honduras) 52.3%, Stripe 57.4%, Cybersource 63.7%. Spain is fine: Redsys 88.1%, ECI 99.7%. Dominican Republic: UepaPay 98.0%. ✅
7. **Method mix on annual TPV:** card 75.7% ($346M), cash incl. OXXO and Paynet 13.2% ($60M), box-office pinpad 6.3% ($29M), transfer 3.0% ($14M), wallets/BNPL/gift 1.8% ($8M). ✅
8. **GTV by country:** Mexico $211M, Argentina $62M, Spain $55M, Dominican Republic $36M, Puerto Rico $31M, Paraguay $26M, Panama $12M, Honduras $5M, Guatemala $4.8M, USA $4.6M. ✅
9. **No consolidated fraud or chargeback data exists** because each tenant handles it with its processor. Patricio named this as a reason to centralize the payments layer. ✅
10. **Patricio's six written questions (Sep 2) are the real agenda:** (1) split payments in Mexico with tenant as MoR and PALCO keeping its fee at capture, (2) mandatory 3DS on all card flows and its effect on routing, (3) tokenization and recurring charges for season passes (abonos) with Mexican processors, (4) the commercial model for multi-tenant, (5) direct API without SDK and the PCI scope that follows, (6) processing by specific bank BIN for pre-sale promotions. ✅
11. **They already diagnosed the problem and named the cure.** Patricio: "en México, que es la mitad de nuestro volumen, la aprobación en tarjeta está entre 56% y 68% según el procesador. Es exactamente lo que esperamos resolver con ruteo inteligente y reintentos." You are proving execution, not selling the concept. ✅
12. **September is the decision month.** Patricio: "septiembre es cuando estaremos definiendo el camino a seguir en nuestro orquestamiento de pagos." The competitor is their own engineering roadmap. ✅
13. **They built 50+ native gateway integrations across 18 markets in-house and sell it as a feature.** Alfonso Uribarri, who is in the room, is the co-founder who runs development and support. Never call it a gap. The line: "you built the hard part; we keep it alive and add the brain." ✅
14. **What you already committed to in writing (Sep 10 email):** four agenda points for this session: (1) integration architecture, API vs SDK, PCI scope; (2) split payments with the promoter as MoR and tokenization for abonos and recurring; (3) routing and retries in Mexico including BIN rules for bank pre-sales; (4) local processing coverage in the markets they mentioned, Bolivia and Venezuela. ✅
15. **Pricing modelled but NOT for this session:** $10,000 platform fee plus a three-tier ladder ($0.0427 / $0.0362 / $0.0314, blended $0.0354) at 235,000 transactions = $18,320 a month, about $220K a year, GREEN (score 89.5). Built on $37.09 as order value and billing currency left in COP. If order value is about $148, take rate falls to about 5 bps and the score can drop below 80 (YELLOW). Quote nothing until volume is settled. ✅
16. **PCI:** if PALCO captures the PAN in its own front end and posts server-side, PALCO carries full PCI DSS scope (SAQ-D or Level 1). No public PCI attestation for PALCO was found anywhere. Ask what their current attestation is; do not assert. ✅
17. **3DS on 100% of card flows** may be the single biggest cause of the Mexican approval problem. Ask whose requirement it is (acquirer, tenant, PALCO). Mastercard's updated 3DS data requirements took effect April 1, 2026 with a July 1, 2026 compliance deadline; ask whether they send the full field set. ✅
18. **BIN routing is commercial, not technical:** Mexican bank pre-sales with meses sin intereses (Banamex with Ticketmaster and OCESA, plus the Banamex LineUp concert card launched September 2025; Santander and Banorte run their own). If PALCO cannot execute bank pre-sales cleanly it loses Mexican venues to Ticketmaster. ✅
19. **Ownership:** Bocel Private Equity plus Patricio Villalobos and Miguel Ramírez Lombana acquired PALCO in Oct/Nov 2025, with a stated plan to enter more LatAm markets by mid-2026. Ramírez's phrase: "PALCO can become the silent infrastructure driving the live events industry." Echo "infrastructure." ✅
20. **Yuno facts you can state:** Split Payments Marketplace is documented (rules per recipient, absolute or percentage, fixed or mixed, recipients on more than one provider, onboarding and standalone transfers). Subscriptions run on CARD, PAYPAL_ENROLLMENT and PIX_AUTOMATIC through vaulted instruments; failed renewals move to PAST_DUE. Network Tokens are a product line. Routing rules key on BIN, issuer country, card brand, amount, metadata. 🔍 Not stated in public docs: which Mexican processors support split at capture in PALCO's inverted direction, and Mexican processor coverage for recurring. Carlos owns both as take-aways if not confirmed.

---

## 1. TL;DR Battle Card

**Five facts to know cold**
1. Tenant is MoR, PALCO earns per ticket, uplift lands with the tenant. Commercial design must let PALCO monetize the layer.
2. Mexico runs 10 to 16 points below its own market on the three card rails; Mercado Pago's wallet proves the platform is not the problem.
3. September is the decision window and the competitor is their roadmap.
4. They own 50+ integrations and the person who built them is in the room.
5. The volume numbers do not reconcile; the pricing depends on it.

**Three hooks, in priority order**
1. **Payments as PALCO's next revenue line.** 30 bps on $457M is about $1.37M a year against roughly $220K of Yuno cost. For a PE-backed company that must show revenue growth, that converts procurement into product strategy. (This is Patricio's frame; with Fernando and Alfonso, keep it to one sentence and park it for the commercial session.)
2. **Their own numbers prove routing and rail selection is the variable.** Same codebase: Spain 88 to 99%, DR 98%, US 90%, Mexico 56 to 60%, and 92.1% vs 67.9% inside Mercado Pago.
3. **BIN-level routing is how PALCO competes with Ticketmaster in Mexico.** Bank pre-sales are the standard mechanic.

**THE objection they will raise (Alfonso):** "We built and maintain 50+ gateway integrations ourselves. Why add a layer, a dependency and a per-transaction cost?"

**The answer (Requirement, Benefit, Proof):** the connectors are the commodity; what produces approval is the decision layer above them (rail, order, retry, authentication, per BIN and issuer, updated continuously). You keep every integration and every negotiated contract; Yuno sits above and adds the rails you have not built. Proof on their numbers: +2 points on the three Mexican rails is about 20,000 transactions and about $743K of GTV a year; reaching Mercado Pago's own 67.9% is about $3.49M. Illustrative arithmetic on their data, never a Yuno guarantee.

**The ask:** a scoped pilot in Mexico on Openpay, Banorte and Santander with a defined approval baseline and a fixed review date, a named technical owner on PALCO's side, and a date for the commercial session with Patricio.

**Rapport opener:** thank Fernando for confirming so fast on a Monday, ask Alvaro what he does, and tell Alfonso you read the gateway map on pal.co and counted the integrations. That signals respect for the build before you touch it.

---

## 2. Who is in the room

| Name | Role | Side | Status |
|---|---|---|---|
| Fernando Nava Feldman | Signs as **Technical Account Manager, Palco México (CDMX)**; Patricio introduced him as VP of Engineering | PALCO | Accepted, asked for this slot |
| Alfonso Uribarri Carrasco | Co-founder of Palco4 (2017); Manager of Development and Support, Madrid (⚠️ RocketReach, single source) | PALCO | Accepted |
| Alvaro (alvaro@pal.co) | ⚠️ Unknown | PALCO | No response |
| Patricio Villalobos Cuevas | CEO, co-owner, operates from Madrid (+34) | PALCO | Not invited |
| Javier Sánchez | Senior Software Engineer | PALCO | Out of office Sep 14 to end of month |
| Carlos Medina | Implementation Engineer (Bogotá) | Yuno | Accepted, leads the technical answers |
| Joaquin Mann | Yuno | Yuno | Accepted |
| Magdalena Torrealba | Global Sales Strategy Associate, relationship owner since Jul 30 | Yuno | Accepted |
| German Tatis | BDM, organizer | Yuno | |

**Fernando.** Mexico-based, the person who coordinates on their side and the one who will own the migration effort. Most sensitive to integration cost and to the API-vs-SDK answer. He has read every email since July and written twice: to say "let me coordinate" and to confirm this slot.

**Alfonso.** Co-founder and the builder of the 50+ integrations. Any phrase that sounds like "replace" loses him. He will ask what changes in PALCO's code, how per-tenant credentials are modelled, what the API returns, and how retries are triggered. Let Carlos answer; do not let a vague answer stand.

**Alvaro.** Unknown. Possibilities range from product to finance. Ask.

**Relationship timeline**

| Date | Event |
|---|---|
| Jul 30 | First call, Magdalena and Patricio. A pilot was discussed. No recording |
| Jul 31 | Magdalena requests volumes, mix, approval by method, fraud and chargebacks |
| Sep 2 | Patricio sends the full data set plus the six questions |
| Sep 7 | Patricio confirms the demo, "bienvenido German al equipo", "venga!" |
| Sep 9 | Demo and payment orchestration review (Patricio, Fernando, Javier; Magdalena, German). Fireflies recording by Magdalena |
| Sep 10 | German proposes three technical-session slots. Fernando: "dame la oportunidad de coordinar con el equipo" |
| Sep 14 | Fernando confirms Tuesday 10:00 COT. Invite sent. Alfonso and Alvaro added by Fernando |
| Sep 15 | This session |

---

## 3. The numbers Patricio sent (Sep 2, confidential)

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
| **Total** | | **3,087,600** | **70.85%** | **900,120** |

**Illustrative uplift on the three Mexican card rails** (1,001,900 attempts a year, at $37.09 per ticket): +2 points = 20,038 transactions, about $743K; +5 points = about $1.86M; up to Mercado Pago's own 67.9% = about $3.49M. Label as arithmetic on their data.

⚠️ Do not use Spain as the target for Mexico. Mexican issuer behaviour is structurally different; use the Mexican benchmark and PALCO's own best Mexican rail as goalposts.

---

## 4. What happened on Sep 9 (what is known)

- Fireflies auto-summary (Magdalena's recording): backend ticketing is popular in Puerto Rico; Openpay and Mercado Pago discussed as options; "dollar marketplace and local processing for Bolivia and Venezuela" discussed; "cross-border local is not supported" (⚠️ context unclear); "merchant of record responsibilities include token procedure" (⚠️ Patricio on MoR and tokens); success cases and the dashboard were shown; a product deep dive was planned.
- Your own follow-up (Sep 10) set the four agenda points now in section 0, item 14.
- Nothing from Sep 9 is in Gong; no transcript exists on our side beyond Fireflies.

---

## 5. The six questions: where each answer stands

| # | Patricio's question | Answer status | Who closes it Tuesday |
|---|---|---|---|
| 1 | Split payments in Mexico, tenant MoR, PALCO keeps its fee at capture | Yuno Split Payments Marketplace is documented ✅. 🔍 Which Mexican processors support the inverted direction (tenant collects, PALCO deducts) at capture rather than by later transfer is not public. Live marketplace reference exists (permission needed) | Carlos: confirm per processor or take away with a date |
| 2 | Mandatory 3DS and routing | Yuno routes 3DS dynamically per rule ✅. 🔍 Whose requirement is 100% 3DS? Are they sending Mastercard's full data set? | German asks; Carlos explains selective 3DS |
| 3 | Tokenization and recurring for abonos with Mexican processors | Subscriptions on vaulted instruments ✅; network tokens survive reissue ✅. 🔍 Mexican processor coverage for recurring not public | Carlos |
| 4 | Commercial model for multi-tenant | This is Patricio's question, not Fernando's. One sentence Tuesday: "you can absorb it as a cost or package it to tenants; we price it for the commercial session." | German, parked for Patricio |
| 5 | Direct API without SDK, PCI scope | Direct API supported ✅; full PCI scope follows ✅. Middle path: card capture through a Yuno-hosted field or vault call, everything else server-to-server | Carlos, with the PCI consequence stated plainly |
| 6 | Processing by bank BIN for pre-sales | Routing rules key on BIN ✅ | Carlos shows it live |

---

## 6. Technical deep dive plan (for Carlos)

**What they said they want (German on Slack, Sep 14):** "tomar un deep dive en el dashboard y hablar de cómo funcionaría la integración."

Show in this order, in the dashboard, with their own processors named where Yuno has the connector:

1. **Connections library:** search Openpay, Banorte, Santander, Mercado Pago, Redsys, Cybersource, Stripe, Authorize.net, Fiserv. Say which are in the catalog today; say "not today" for the ones that are not (Line VE, Pixel Pay HN, Recurrente GT, Bancard PY, UepaPay DR, ECI ES are likely gaps 🔍 verify before the call; never bluff in front of Alfonso).
2. **How a multi-tenant platform is modelled** 🔍: one account per tenant with its own processor credentials, or one account with per-tenant routing and metadata. Carlos must know Yuno's answer cold; it is the first thing Alfonso will ask.
3. **Routing rules:** a rule on issuer country plus BIN range (the bank pre-sale case), a fallback from Openpay to Banorte on decline codes, a retry, and a Monitor that redirects when approval drops.
4. **3DS:** dynamic 3DS by rule, so 3DS runs where it lifts and not where it kills.
5. **Vault and tokens:** vaulted card reused across processors; network tokens for abono renewals.
6. **Split payments:** the recipient and rule configuration screen. State the model Yuno supports (platform collects, recipients onboarded) and ask how PALCO's flow maps.
7. **Integration options:** direct API (full control, full PCI scope), SDK Lite or hosted field for capture only, full SDK. Webhooks, sandbox credentials, typical timeline (connection in 1 to 2 days once credentials exist; full integration with QA in 3 to 5 days is what Jarrett told FlightHub; use it only if Carlos agrees).
8. **Reporting:** approval by processor, by BIN, by tenant metadata; the consolidated fraud and chargeback view they do not have today.

Do not show: pricing, the deal calculator, any other merchant's data.

---

## 7. Be ready for

| They ask | You answer |
|---|---|
| "How do tenant credentials and contracts work? We have 50+ processor accounts across 500+ venues." | Bring your own credentials per connection; Yuno never sits in the flow of funds; settlement stays between the tenant and its processor. 🔍 The exact account model (per tenant or per platform) is Carlos's to state precisely. |
| "What changes in our code?" | One integration to Yuno replaces the per-processor integrations for the flows you route through it. You can start with Mexico card only and keep everything else as is. |
| "Can we keep direct API and avoid PCI scope?" | No. Direct API with PAN in your front end means full scope. The middle path is Yuno-hosted capture for the card field only. State it as a choice with a cost. |
| "Does the split work with the tenant as MoR?" | Documented model is platform-collects. Whether a Mexican processor supports deducting PALCO's fee at capture with the tenant as MoR is confirmed per processor. Take it away with a date; do not guess. |
| "Bolivia and Venezuela?" | Only what the catalog confirms. Line VE approves 8.7% on their data; a better local rail matters more than orchestration there. 🔍 Verify catalog before the call. |
| "What does it cost per tenant?" | Structure only: platform fee plus a fee on successful transactions, priced at the PALCO level, not per tenant. Numbers with Patricio once volume is reconciled. |
| "How fast could a Mexico pilot go live?" | Only a number Carlos stands behind. Connection setup is days once credentials exist; the pilot scope and baseline take longer than the integration. |
| "Do you have a ticketing or marketplace reference?" | Generic unless GoFundMe permission is granted. |

**Landmines:** never "you lack an orchestrator"; never compare Mexico to Spain as a target; no pricing numbers; no client names without permission; no claims about Bolivia, Venezuela or Mexican recurring coverage that Carlos has not verified; no em-dashes in the recap.

---

## 8. Agenda (45 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 5 | Open: roles (Alvaro), objective, confirm the four points. Thank Fernando for the fast confirmation | Notes: ____ |
| 5 to 15 | Business discovery (German): how PALCO earns, who the tenant is, who pays processing fees, what scale looks like (section 9 A to C). Do this before the technical part or it never happens | Notes: ____ |
| 15 to 35 | Technical deep dive (Carlos): connections, tenant model, routing and BIN, 3DS, vault, split, integration options (section 6) | Notes: ____ |
| 35 to 42 | The open items: split at capture per processor, Mexican recurring coverage, Bolivia and Venezuela, PCI attestation. Assign owners and dates | Notes: ____ |
| 42 to 45 | Close: Mexico pilot scope, PALCO technical owner, commercial session with Patricio | Notes: ____ |

---

## 9. Discovery questions

**A. Margins and how they make money**
1. How is the fee per ticket structured: fixed, percentage or mixed, and does it vary by country or tenant? Notes: ____
2. Do you earn anything on payments today, or does the tenant pay its processor directly and PALCO sees none of it? Notes: ____
3. Who pays the processing fee and to whom: tenant to processor, or PALCO invoices and passes through? Notes: ____
4. Roughly what share of revenue is the ticket fee versus SaaS, pinpad, access control and other modules? Notes: ____
5. What does maintaining 50+ integrations cost you: people, hours a month, incidents during on-sales? Notes: ____

**B. The underlying customer**
6. Tenants are promoters, venues or both? How many are active, and what share of GTV sits in the top ten? Notes: ____
7. Who chooses and negotiates the processor for a tenant, PALCO or the tenant? Notes: ____
8. Who would contract with Yuno: PALCO as one multi-tenant account, or each tenant? Notes: ____
9. How do you onboard a tenant today: KYC, processor account, time to first sale? Notes: ____
10. In the split, does the tenant collect and PALCO deducts its fee at capture, or does PALCO collect and settle to the tenant? Notes: ____

**C. Scale**
11. Which markets are next in 2026 and 2027, and what is missing in each: local processor, entity, method? Notes: ____
12. Peak load: Bad Bunny DR sold out three times in eight hours. What is peak TPS, and what happens to the processor at peak? Is there a fallback today? Notes: ____
13. $37.09 is the ticket and the order is about four tickets, correct? And is 235,000 or 257,000 the monthly transaction count? Notes: ____
14. For a Mexico pilot on Openpay, Banorte and Santander: what baseline do you trust, and what review date works? Notes: ____
15. Who decides build versus Yuno, and what would Fernando need to see to recommend Yuno? Notes: ____

**D. Technical (Carlos)**
16. How is the payments layer built: one abstraction with per-tenant configuration, or one integration per processor? Notes: ____
17. 3DS on 100% of cards: whose decision, and are you sending Mastercard's full 3DS data set since July 1? Notes: ____
18. Do you store PAN today? What is your current PCI attestation? Notes: ____
19. Which Mexican processors do you use for recurring charges on abonos today? Notes: ____
20. How do you reconcile 50+ processors across tenants, and who responds to disputes? Notes: ____

---

## 10. Post-meeting checklist

- Same-day recap in Spanish to Fernando, Alfonso and Alvaro, cc Patricio and Magdalena, with every open item, owner and date.
- Carlos delivers the per-processor answers (split at capture, Mexican recurring, Bolivia and Venezuela catalog) within 48 hours.
- Reconcile volume in the pricing sheet, fix billing currency (COP to USD), rerun the score.
- Propose the commercial session with Patricio with the pilot scope attached.
- Update memory: Alvaro's role, tenant model answer, PCI attestation, 3DS decision owner, pilot baseline.

### Sources
Google Calendar (event "Palco + Yuno | Deep Dive", Sep 15, 2026) · Gmail thread "Palco + Yuno - Próximos Pasos" (Patricio's data email Sep 2; Magdalena Sep 4; Patricio Sep 7; German Sep 10 and Sep 14; Fernando Sep 10 and Sep 14; Javier out-of-office Sep 14) · Fireflies recap email Sep 9 (Magdalena's recording) · Slack DM German and Carlos Medina, Sep 14 · Slack user directory (Carlos Medina) · data/research/palco-meeting-brief-2026-09-09.md · data/research/palco-ticketing-2026-09-08.md · Deals/Palco/palco-followup-email-2026-09-10.md · RocketReach profile for Alfonso Uribarri Carrasco (single source) · pal.co gateway map · docs.y.uno (split payments marketplace, subscriptions, routing) · RankingsLatAm Mexican approval benchmarks (Sept 2024) · El Financiero on Banamex LineUp (Sep 18, 2025).
