# Meeting Brief: Yuno <> PedidosYa (PeYa)

**Meeting:** Tuesday 29 September 2026, 1:30 to 2:00pm COT (11:30am to 12:00pm PT) · [Google Meet](https://meet.google.com/tzv-gczr-zxg) · phone (CO) +57 601 8956307, PIN 331638359
**Event:** "PeYa & Yuno", created 25 September 2026 by Alejandro Albarracín. Belén Casaret accepted.
**Objective:** 30 minute first call with a warm referral. Winning it means leaving with three things: a precise definition of what Belén wants to change (which flow, which markets, which provider), the name of whoever owns the provider decision, and a booked second session with that person in the room. Not a proposal, not pricing.
**Evidence labels:** ✅ verified with a source · ⚠️ internal or unconfirmed, never state as fact in the call · 🔍 ask in discovery

---

## ⚠️ PRE-MEETING ACTIONS

1. **Belén's title and scope are not publicly verified.** Internal intel says Regional Collections Manager. The web search budget ran out before her profile could be checked. Open LinkedIn manually and search "Belén Casaret PedidosYa" before the call.
2. **Pin down what "collections" means in the first five minutes.** At PedidosYa it can mean three different flows: consumer pay-ins at checkout, cash that riders collect and remit, or money collected from merchants. The only public dLocal evidence sits on bill payment networks in Paraguay and El Salvador, which looks like a cash-in or remittance flow, not card checkout. ⚠️ The pitch changes completely depending on her answer.
3. **Do not present the Delivery Hero deck V3 as is.** It was built in November 2025 for the Berlin payments team, before the Uber deal, around a "Global Payments Hub" for all regions. It carries 2024 numbers and approval charts (92% vs 81%, +10pp) that are not published Yuno figures. If a slide is needed, use only the LatAm coverage pages.
4. **Uber is a live Yuno relationship. Keep both sides sealed.** Internal work on an Uber APM strategy is ongoing (Slack #roberto-ai, August 2026), with an explicit instruction not to mention Delivery Hero in that document. Share nothing about Uber with PedidosYa beyond what Yuno's own website says.
5. **Someone at Yuno emailed Leandro Malandrini (PedidosYa CPO) on 21 September 2026**, subject "Touchpoint" (Gong). Find out who before the call so two Yuno threads do not collide.
6. **The Delivery Hero opportunity belongs to Justo in Salesforce**, and the thread with Elliot Watnik has been silent since December 2025. Agree with Alejandro whether Elliot gets mentioned to Belén.
7. **Agree roles with Alejandro.** He organised and holds the referral. Suggested split: Alejandro opens and frames the referral, German runs discovery and the next step.
8. **Glean was not authenticated in this session (401)**, so internal docs there were not searched.

---

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. **She came to us.** Belén told a friend of Alonso that PedidosYa wants to change its collections and payments provider, which she says is mostly dLocal today, and that she wants to talk to Yuno. ⚠️ Internal, from Alejandro's voice note. Finding out what triggered it is the most valuable thing in the first ten minutes. 🔍
2. **PedidosYa is being split between two owners.** Uber signed to acquire Delivery Hero on 16 July 2026 (EUR 41.50 per share, closing expected in the second half of 2027). Uber takes 13 PedidosYa markets. SSW Partners takes Chile and Ecuador, with Delivery Hero providing transition services for up to 24 months. ✅
3. **The stack is a vault plus many providers, not one orchestrator doing routing.** Spreedly is published as vault and distribution layer (✅, evidence dated 2018). Elliot Watnik told Yuno that Spreedly "has limitations" and that the 2026 goal is faster time-to-market for new payment methods (✅ Gong). The internal deck says cards run through Worldpay and other PSPs via Spreedly (⚠️). Chile names Klap and Webpay in its T&Cs (✅). Fraud ran on Cybersource Decision Manager as of 2021 (✅).
4. **Scale.** About 1 million average daily orders in Q4 2025. Americas segment GMV EUR 4,079.6M in FY 2025, and +29.4% in H1 2026. 15 countries, 19M+ users. 2024 was the first profitable year. ✅
5. **Local methods keep arriving one market at a time.** Yappy in Panama (2023), Yape in Peru (2024), QR in Bolivia (December 2024), Deuna in Ecuador (August 2026), plus Tigo Money, MACH and Pago Móvil. ✅ That matches the priority Elliot described.

### Three hooks, in priority order (Requirement, Benefit, Proof)

1. **Requirement:** reduce dependency on one provider without a migration project. **Benefit:** Yuno sits above the providers they already have, so a second provider per market is a configuration, and volume can move by cost or approval rate. **Proof:** Rappi cut new provider implementation time to zero.
2. **Requirement:** launch local methods faster in 15 markets. **Benefit:** one integration to local wallets, QR and bank transfers instead of one build per country. **Proof:** inDrive went live in 10 LATAM markets in under 8 months.
3. **Requirement:** one view of collections, refunds and reconciliation across providers. **Benefit:** unified transaction status and monitors, fewer orphan charges and manual refund cases. **Proof:** Yuno's published figure is a 7% approval uplift from smart routing; Rappi detects provider issues in milliseconds instead of 5 to 10 minutes.

### THE objection they will raise

**"We already have Spreedly and an in-house payments team, and Uber is buying us. Why start anything now?"**

Answer: nothing gets replaced. Yuno connects above the current providers and the current vault, so the first step can be one market or one flow. The ownership change is a reason to move sooner: closing is expected in the second half of 2027, Chile and Ecuador will need a stack that can stand on its own, and a provider-agnostic layer is what makes the stack portable whoever the owner is. Ask, do not assert, how they are planning for that.

**Second objection, probably unspoken: dLocal is protected internally.** Internal intel says the Head of Payments came from dLocal. ⚠️ Never criticise dLocal. Position it as one of the providers that can stay behind Yuno. 🔍 Confirm with a Solutions Engineer before the call that dLocal is a live Yuno connection in their markets before saying so.

### The ask (next step to land)

A 45 minute session with Belén plus whoever owns the payment provider decision, and a Yuno Solutions Engineer. With it, a short data request: **volume by market and by provider, cost per provider, and approval rate by market for the flow she wants to change.**

### Rapport opener

Let Alejandro open with the referral. If something recent helps: on 18 September 2026 PedidosYa published that online supermarket purchases grew 62% year over year in Latin America, and 2024 was the company's first profitable year. ✅

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status |
|---|---|---|---|
| Belén Casaret (belen.casaret@pedidosya.com) | ⚠️ Regional Collections Manager per internal intel | PedidosYa | Accepted |
| Alejandro Albarracín (alejandro@y.uno) | Organiser, holds the referral | Yuno | Accepted |
| German Tatis (german.tatis@y.uno) | Senior AE | Yuno | Accepted |

### Not in the room, but they shape the decision

| Name | Role | Why it matters | Source |
|---|---|---|---|
| Head of Payments, name unknown 🔍 | ⚠️ Reportedly ex-dLocal | Likely owner of the provider decision and possible defender of dLocal | Internal, Alejandro |
| Elliot Watnik | Delivery Hero, payments strategy | Led the 2025 conversation with Yuno about PedidosYa; silent since December 2025 | Gong |
| Lars Hofmann | Global Payments Director, Delivery Hero | Met Yuno at MPE Berlin on 17 March 2026 | Slack #mpe-berlin-2026 |
| Saad Saif | Delivery Hero | Asked for coverage and metrics for an APAC RFP in Q2 2026 | Gong |
| Leandro Malandrini | Chief Product Officer, PedidosYa | Received a Yuno "Touchpoint" email on 21 September 2026 | Gong; https://empleos.pedidosya.com/equipo-de-liderazgo |
| Ignacio Costa | VP Fintech, PedidosYa | Owns the fintech roadmap (wallet, credits, advances) | https://www.mdzol.com/sociedad/pedidosya-reunio-mas-100-socios-mendoza-y-proyecta-el-crecimiento-del-quick-commerce-n1503763 |
| Pablo Setuain | CFO, PedidosYa | Collections usually reports into finance 🔍 | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Juan Martín Sotuyo | CTO, PedidosYa | Owns the in-house payments engineering teams | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Martin Engert, Camilo de Vargas, Daiana Lopez | PedidosYa, roles unknown | Appear as recipients of a provider incident notice (Visa degradation, 26 September 2025) that also reached Yuno. Not evidence of a Yuno relationship | Gong |

---

## 3. HOW WE GOT HERE

| Date | Event | Source |
|---|---|---|
| 2025-08-08 | Call "DeliveryHero <> Yuno" | Gong |
| 2025-11-13 to 2026-02-10 | Email thread "Delivery Hero + Yuno, Synergies Catch-up" with Elliot Watnik. He confirmed an internal review with the PedidosYa team, concluded in late November 2025, that prioritised faster time-to-market and new payment methods | Gong |
| 2025-11-20 | Deck "Delivery Hero + Yuno Business Deck V3" created (Justo Benetti, Alejandro Albarracín, Anastasia Makeeva) | Google Drive |
| 2025-12 onward | No reply or availability from Elliot. Conversation stalled | Gong |
| 2026-03-17 | Meeting with Lars Hofmann at MPE Berlin | Slack |
| 2026-07-16 | Uber signs agreement to acquire Delivery Hero | SEC filing |
| 2026-09-21 | Yuno "Touchpoint" email to Leandro Malandrini | Gong |
| 2026-09-25 | Alejandro books this call with Belén after the referral through Alonso's contact | Calendar |

**What the deck says about PedidosYa (internal view, November 2025)** ⚠️
- PedidosYa is a cards and cash heavy region, processed via Worldpay and other PSPs through Spreedly, with Spreedly used mainly as a vaulting layer.
- Stated needs: true orchestration (smart routing, failover, A/B testing) and fast rollout of local cash, wallet and bank transfer methods without new builds.
- Group context: Delivery Hero was centralising payments in a Berlin hub for all regions by the second half of 2026, running Checkout.com, Adyen, Fiserv and MPGS plus an internal wallet platform. Glovo suffered a ProcessOut outage.
- The deck is the same file published at deck.y.uno/DeliveryHero.

**What changed since the deck**
- The Uber and SSW transaction. The Berlin hub premise may no longer hold. 🔍
- dLocal was not in the deck at all. Belén now says it is the main provider. ⚠️
- PedidosYa added Deuna and QR payments and launched PeYa Wallet for merchants.

---

## 4. STACK SNAPSHOT

| Layer | What we know | Label |
|---|---|---|
| Vault and routing | Spreedly, used mostly as vault | ✅ published, ⚠️ current usage |
| Main provider | dLocal, per Belén | ⚠️ |
| dLocal public trace | "PEDIDOS YA" listed under "Dlocal Service" on Bancard's Infonet portal (Paraguay); biller "Pedidosya, Dlocal" in El Salvador | ✅ |
| Cards | Worldpay and other PSPs through Spreedly | ⚠️ internal deck |
| Chile debit | Klap and Webpay | ✅ T&C |
| Fraud | Cybersource Decision Manager (2021) | ✅ dated |
| Rider cash remittance | Pago46 in Argentina and Chile | ✅ |
| Merchant wallet, Argentina | PeYa Wallet, with Wibond as the registered payment provider behind the accounts | ✅ |
| Reconciliation | Simetrik and SAP | ✅ job listing |
| In-house | Payments Tribe with a Payment Gateway team | ⚠️ from job listings |

Full detail and every URL: `data/research/pedidosya-2026-09-29.md`

---

## 5. PUBLIC PAIN SIGNALS (use as questions, never as accusations)

- Chile's consumer agency recorded 3,417 complaints against PedidosYa in 2024, with refunds as the top reason across delivery apps. ✅
- Repeated reports of "charged but the order was never created" and of double charges after retrying with a second card. ✅
- Refunds for some methods go to the in-app wallet instead of the original method (Webpay debit in Chile, QR in Bolivia). ✅
- T&Cs in Ecuador, Venezuela, Costa Rica and Honduras require an "international" card for online payment, which may point to cross-border acquiring. ⚠️ Ask, do not assert.
- Uruguay stopped accepting cash after 19:00 in May 2026 for rider safety, which pushes volume to digital methods. ✅

---

## 6. RISKS

| Risk | How to handle it |
|---|---|
| Uber deal freezes vendor decisions until closing | Propose a first step small enough to fit inside the current structure: one market, one flow |
| Head of Payments defends dLocal | Keep dLocal in the picture as a provider behind Yuno. Get Belén to describe the internal dynamics herself |
| Belén may not own the provider decision | Ask who signs and who evaluates. Make her the guide, not the buyer |
| Berlin centralises decisions | Ask what is decided locally versus in Berlin today, and whether that changed after July |
| Spreedly contract and in-house gateway team | Yuno works above the existing vault; tokens stay portable |
| Previous thread with Elliot went silent | Do not lean on it. Use it only if Belén brings him up |

---

## 7. AGENDA (30 minutes)

| Time | Block | Owner |
|---|---|---|
| 0 to 3 | Intros, roles, the referral | Alejandro |
| 3 to 15 | Discovery: what she wants to change, which flow, which markets, why now | German |
| 15 to 21 | Yuno in five minutes, shaped by what she said | German |
| 21 to 27 | Decision path: who owns it, Berlin, Uber timeline | German |
| 27 to 30 | Next step and data request | German |

---

## 8. DISCOVERY QUESTIONS (in Spanish)

**Contexto y disparador**
1. Belén, para ubicarnos: ¿qué cubre tu rol de collections en PedidosYa y en qué países?
   Notes: ____
2. ¿Qué fue lo que los llevó a evaluar un cambio de proveedor ahora?
   Notes: ____
3. Cuando hablamos de collections, ¿es el cobro al usuario en el checkout, la recaudación del efectivo de los repartidores, el cobro a comercios, o las tres?
   Notes: ____

**Stack actual**
4. ¿Qué proveedores tienen hoy por país y qué parte del volumen pasa por cada uno?
   Notes: ____
5. ¿Cómo deciden hoy a qué proveedor va cada transacción? ¿Hay ruteo o cada país tiene un proveedor fijo?
   Notes: ____
6. ¿Qué rol cumple Spreedly hoy en la operación?
   Notes: ____
7. Cuando un proveedor se degrada, ¿cómo se enteran y cuánto tardan en mover el tráfico?
   Notes: ____

**Dolor**
8. ¿Qué es lo que más les cuesta hoy: costo, aprobación, tiempos de liquidación, conciliación o soporte del proveedor?
   Notes: ____
9. ¿Qué tasa de aprobación tienen en sus mercados principales y cómo se compara entre países?
   Notes: ____
10. ¿Cuánto tarda hoy sumar un método de pago local nuevo, desde que lo deciden hasta que sale a producción?
    Notes: ____
11. ¿Cómo manejan las devoluciones y la conciliación cuando conviven varios proveedores y métodos?
    Notes: ____

**Decisión**
12. ¿Quién más participa en una decisión así? ¿Payments, producto, finanzas, tecnología?
    Notes: ____
13. ¿Qué se decide hoy en la región y qué se decide en Berlín?
    Notes: ____
14. Con el acuerdo con Uber y SSW, ¿cambió algo en cómo planean el stack de pagos, sobre todo para Chile y Ecuador?
    Notes: ____
15. ¿Tienen alguna fecha o evento que marque el plazo para este cambio, como un vencimiento de contrato?
    Notes: ____
16. ¿Cómo sería un primer paso razonable para ustedes: un país, un flujo, una prueba?
    Notes: ____

---

## 9. POST-MEETING CHECKLIST

- [ ] Recap email the same day, in Spanish, sober, no links, with the agreed next step and a date
- [ ] Log every confirmed fact: her real title, the flow she wants to change, providers by market, the name of the Head of Payments
- [ ] Book the second session with the decision owner and a Yuno Solutions Engineer
- [ ] Send the data request in writing: volume by market and provider, cost per provider, approval rate by market
- [ ] Align with Justo on how this thread relates to the Delivery Hero opportunity and to the 21 September email to Leandro Malandrini
- [ ] Update memory and the research brief with what was confirmed and correct anything marked ⚠️

---

## APPENDIX: SOURCES

Full research brief with every source URL: `data/research/pedidosya-2026-09-29.md`

Internal sources used here:
- Alejandro Albarracín's voice note (transcribed by German, 29 September 2026)
- Google Calendar event "PeYa & Yuno"
- Gong, accounts Delivery Hero and PedidosYa (call of 2025-08-08 and email threads)
- Google Drive: "Delivery Hero + Yuno _ Business Deck_V3.pptx" (same document as deck.y.uno/DeliveryHero)
- Slack: #mpe-berlin-2026, #roberto-ai, #sdr-salesops

Primary public sources:
- Uber and Delivery Hero agreement: https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm
- Spreedly case study: https://www.spreedly.com/customers/pedidosya
- dLocal biller listings: https://www.infonet.com.py/servicios_disponibles/Dlocal%20Service · https://www.bitrefill.com/sv/es/factura/pedidosya-dlocal-bill-el-salvador/
- Chile T&C (Klap, Webpay): https://www.pedidosya.cl/about/terminos-condiciones
- SERNAC 2024 complaints: https://www.sernac.cl/portal/604/w3-article-83827.html
- Delivery Hero Q1 2026 trading update: https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline
- Yuno customers named publicly: https://y.uno/en/about
