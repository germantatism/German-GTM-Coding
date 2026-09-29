# Meeting Brief: Yuno <> PedidosYa (Sep 29, 2026)

**Meeting:** Tuesday 29 September 2026, 1:30 to 2:00pm COT (11:30am to 12:00pm PT) · [Google Meet](https://meet.google.com/tzv-gczr-zxg) · phone (CO) +57 601 8956307, PIN 331638359
**Event:** "PeYa & Yuno", created 25 September 2026 by Alejandro Albarracín. All three invitees accepted.
**Objective:** 30 minute first call with a warm referral. Winning it means leaving with three things: a precise definition of what Belén wants to change (which flow, which markets, which provider), the name of whoever owns the provider decision, and a booked second session with that person in the room. Not a proposal, not pricing.
**Evidence labels:** ✅ verified with a source · ⚠️ internal or unconfirmed, never state as fact in the call · 🔍 ask in discovery

---

## ⚠️ PRE-MEETING ACTIONS

1. **Open Belén's LinkedIn manually.** LinkedIn blocked automated access (HTTP 999), TheOrg does not list her, and the session's web search budget was exhausted before her profile could be resolved. Search: https://www.linkedin.com/search/results/people/?keywords=Bel%C3%A9n%20Casaret%20PedidosYa. Her title (Regional Collections Manager) comes only from Alejandro's voice note.
2. **Pin down what "collections" means in the first five minutes.** At PedidosYa it can mean three flows: consumer pay-ins at checkout, cash that riders collect and remit, or money collected from merchants. The public dLocal evidence sits on bill payment networks in Paraguay and El Salvador, which looks like a cash-in or remittance flow, not card checkout. The pitch changes completely depending on her answer.
3. **Do not present the Delivery Hero deck V3 as is.** It was built in November 2025 for the Berlin payments team, before the Uber deal, around a "Global Payments Hub". It carries 2024 numbers and approval charts (92% vs 81%, +10pp) that are not Yuno published figures. If a slide is needed, use only the LatAm coverage pages.
4. **Uber is a live Yuno relationship. Keep both sides sealed.** Internal work on an Uber APM strategy is ongoing (Slack #roberto-ai, August 2026). Share nothing about Uber with PedidosYa beyond what Yuno's own website says.
5. **Someone at Yuno emailed Leandro Malandrini (PedidosYa CPO) on 21 September 2026**, subject "Touchpoint" (Gong). Find out who before the call so two Yuno threads do not collide.
6. **The Delivery Hero opportunity belongs to Justo in Salesforce**, and the thread with Elliot Watnik has been silent since December 2025. Agree with Alejandro whether Elliot gets mentioned.
7. **Agree roles with Alejandro.** He organised and holds the referral. Suggested split: Alejandro opens and frames the referral, German runs discovery and the next step.
8. **Confirm reconciliation scope with product before the call.** Belén works in collections, so reconciliation will likely be her first question. Do not promise settlement or fee reconciliation until product confirms what is generally available.

---

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. **She came to us.** Belén told a contact of Alonso that PedidosYa wants to change its collections and payments provider, which she says is mostly dLocal today, and that she wants to talk to Yuno. ⚠️ Internal. What triggered it is the most valuable thing to learn in the first ten minutes. 🔍
2. **PedidosYa is being split between two owners.** Uber signed to acquire Delivery Hero on 16 July 2026 (EUR 41.50 per share, closing expected in the second half of 2027). Uber takes 13 PedidosYa markets. SSW Partners takes Chile and Ecuador, with transition services for up to 24 months. The shareholder acceptance period runs until 5 November 2026. ✅
3. **The stack is a vault plus many providers.** Spreedly is published as vault and distribution layer (✅, evidence dated 2018). Elliot Watnik told Yuno that Spreedly has limitations and that the 2026 goal is faster time-to-market for new payment methods (✅ Gong). Chile names Klap and Webpay in its T&Cs (✅). Fraud ran on Cybersource Decision Manager as of 2021 (✅).
4. **dLocal is already a live Yuno connection.** ✅ Internal (Slack #integration-product-inquiries, 29 September 2026). Moving to Yuno does not require dropping dLocal.
5. **Scale and margin.** About 1 million average daily orders in Q4 2025. Americas GMV EUR 4,079.6M in FY 2025 and +29.4% in H1 2026. Adjusted EBITDA is 2.7% of GMV, so payment cost is a first-order lever. ✅

### Three hooks, in priority order (Requirement, Benefit, Proof)

1. **Requirement:** reduce dependency on one provider without a migration project. **Benefit:** Yuno sits above the providers they already have, dLocal included, so a second provider per market is a configuration and volume can move by cost or approval. **Proof:** Rappi cut new provider implementation time to zero. Yuno's published figure is 27% savings on payment costs.
2. **Requirement:** launch local methods faster across 15 markets. **Benefit:** one integration to local wallets, QR and bank transfers instead of one build per country. **Proof:** inDrive went live in 10 LATAM markets in under 8 months. Yuno publishes a 90% reduction in development time.
3. **Requirement:** one view of collections and refunds across providers. **Benefit:** unified transaction status and real-time monitors, fewer orphan charges and manual refund cases. **Proof:** Yuno's published figure is 30% recovered revenue; Rappi detects provider issues in milliseconds instead of 5 to 10 minutes.

### THE objection they will raise

**"We already have Spreedly and an in-house payments team, and Uber is buying us. Why start anything now?"**

Answer: nothing gets replaced. Yuno connects above the current providers and the current vault, so the first step can be one market or one flow. The ownership change is a reason to move sooner: closing is expected in the second half of 2027, Chile and Ecuador will need a stack that can stand on its own, and a provider-agnostic layer is what keeps the stack portable whoever the owner is. Ask how they are planning for that. Do not assert.

**Second objection, probably unspoken: dLocal is protected internally.** Internal intel says the Head of Payments came from dLocal. ⚠️ Never criticise dLocal. It stays as one of the providers behind Yuno.

### The ask (next step to land)

A 45 minute session with Belén plus whoever owns the payment provider decision, and a Yuno Solutions Engineer. With it, a short data request: **volume by market and by provider, cost per provider, and approval rate by market for the flow she wants to change.**

### Rapport opener

Let Alejandro open with the referral. If something recent helps: on 18 September 2026 PedidosYa published that online supermarket purchases grew 62% year over year in Latin America. ✅ From the last 7 days there is only parent-level news (24 September: Delivery Hero's CEO stays on, citing the Uber offer), which is not a warm opener.

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status |
|---|---|---|---|
| Belén Casaret (belen.casaret@pedidosya.com) | ⚠️ Regional Collections Manager per internal intel | PedidosYa | Accepted |
| Alejandro Albarracín (alejandro@y.uno) | Organiser, holds the referral | Yuno | Accepted |
| German Tatis (german.tatis@y.uno) | Senior AE | Yuno | Accepted |

### Profile: Belén Casaret

| Field | Finding |
|---|---|
| Title | ⚠️ Regional Collections Manager (voice note only) |
| Tenure, career path, education, location | Not retrieved. LinkedIn returned HTTP 999; TheOrg's PedidosYa page does not list her; no search budget remained for other directories |
| How to read this person | ⚠️ A finance-side operator who feels the provider's cost, settlement timing and reconciliation every day, and who reached out through a personal contact instead of a formal process. Expect practical questions and limited authority over the vendor decision. Confirm both in the first minutes |

### Sponsor and intro path

Belén → a friend of Alonso → Alonso → Alejandro Albarracín → this call. ⚠️ Internal.

### Relationship timeline

| Date | Event | Source |
|---|---|---|
| 2025-08-08 | Call "DeliveryHero <> Yuno" | Gong |
| 2025-11-13 to 2026-02-10 | Email thread "Delivery Hero + Yuno, Synergies Catch-up" with Elliot Watnik. An internal review with the PedidosYa team, concluded in late November 2025, prioritised faster time-to-market and new payment methods | Gong |
| 2025-11-20 | Deck "Delivery Hero + Yuno Business Deck V3" created (Justo Benetti, Alejandro Albarracín, Anastasia Makeeva). Same file as deck.y.uno/DeliveryHero | Google Drive |
| 2025-12 onward | No reply or availability from Elliot | Gong |
| 2026-03-17 | Meeting with Lars Hofmann at MPE Berlin | Slack |
| 2026-07-16 | Uber signs agreement to acquire Delivery Hero | SEC filing |
| 2026-09-21 | Yuno "Touchpoint" email to Leandro Malandrini | Gong |
| 2026-09-25 | Alejandro books this call | Calendar |

**Calendar history:** no prior meeting with any attendee of this call exists on German's calendar. Searches by Belén's email, "PedidosYa", "PeYa" and "Delivery Hero" return only today's event. Gmail holds nothing from pedidosya.com or deliveryhero.com except the invite.

**Implication:** first meeting with Belén, follow-up at account level. She has probably never seen the deck or heard of the Elliot thread. Build from zero with her and keep the group history as background.

### Other known contacts in the account

| Name | Role | Why it matters | Source |
|---|---|---|---|
| Head of Payments, name unknown 🔍 | ⚠️ Reportedly ex-dLocal | Likely owner of the provider decision | Internal |
| Elliot Watnik | Delivery Hero, payments strategy | Led the 2025 conversation about PedidosYa | Gong |
| Lars Hofmann | Global Payments Director, Delivery Hero | Met Yuno at MPE Berlin | Slack |
| Saad Saif | Delivery Hero | Asked for coverage and metrics for an APAC RFP in Q2 2026 | Gong |
| Leandro Malandrini | Chief Product Officer | Received the 21 September email | Gong; https://empleos.pedidosya.com/equipo-de-liderazgo |
| Ignacio Costa | VP Fintech | Owns wallet, credits and advances | https://www.mdzol.com/sociedad/pedidosya-reunio-mas-100-socios-mendoza-y-proyecta-el-crecimiento-del-quick-commerce-n1503763 |
| Pablo Setuain | CFO | Collections usually reports into finance 🔍 | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Juan Martín Sotuyo | CTO | Owns the in-house payments engineering teams | same |
| Martin Engert, Camilo de Vargas, Daiana Lopez | Roles unknown | Recipients of a provider incident notice (Visa degradation, 26 September 2025) that also reached Yuno. Not evidence of a Yuno relationship | Gong |

---

## 3. THE COMPANY

PedidosYa is the Latin American delivery and quick-commerce platform of Delivery Hero: restaurants, its own dark stores (PedidosYa Market), courier, subscription (PedidosYa Plus), ads, and a fintech arm for merchants and riders.

| Metric | Value | Date | Source |
|---|---|---|---|
| Countries | 15 | 2026 | https://en.wikipedia.org/wiki/PedidosYa |
| Users | 19M+ in 500+ cities | 2026-01-05 | https://www.prnewswire.com/mx/comunicados-de-prensa/pedidosya-foodie-radar-2025-el-mapa-del-sabor-en-latam-302652661.html |
| Average daily orders | 1 million | Q4 2025 | https://www.tradingview.com/news/eqs:81958b162094b:0-delivery-hero-reports-strong-q4-while-business-transforms-into-everyday-app/ |
| Partner restaurants | 156,000 | 2025-07-08 | https://www.forbesargentina.com/negocios/pedidosya-lanza-nueva-version-su-app-inversion-us-87-millones-tecnologia-n75019 |
| PedidosYa Market stores | 160 in 90+ cities, 14 countries | 2026-01-02 | https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula |
| Subscribers' share of GMV | 40% | Q2 2026 | https://www.investing.com/news/transcripts/earnings-call-transcript-delivery-hero-tops-q2-2026-revenue-forecast-93CH-4879424 |
| Employees | about 5,000 | 2025 | https://en.wikipedia.org/wiki/PedidosYa |
| Credit placed with merchants and riders | more than USD 153M | 2026-01-02 | https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula |

### Corporate structure

| Entity | Role | Source |
|---|---|---|
| Delivery Hero SE (Berlin) | Parent, 100% owner of all entities below | https://ir.deliveryhero.com/media/document/d7cd8a32-bb5e-48d0-a416-c38f9cad59e0/assets/DeliveryHeroSE_Annual_Financial.pdf?disposition=inline |
| Uber Technologies | Holds 24.77% of voting shares; offer pending for the rest. Would own 13 PedidosYa markets | https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm |
| SSW Partners (SDU 1, LLC) | Would own PedidosYa Chile and Ecuador | same |
| Delivery Hero E-Commerce S.A. | Argentina operating entity | https://www.pedidosya.com.ar/about/terminos-condiciones |
| Delivery Hero Financial Services S.A. (formerly Pagos Ya S.A.) | Argentina fintech entity, seller of PeYa Wallet | https://www.indicadores.ar/empresa/30715221159 |
| Delivery Hero Payments Uruguay S.A. | Uruguay payments and collections entity | https://www.pedidosya.com.uy/about/terminos-condiciones |
| Delivery Hero E-Commerce Chile SpA | Chile operating entity (goes to SSW) | https://www.pedidosya.cl/about/terminos-condiciones |
| Delivery Hero Panamá, S.A., Sucursal Venezuela | Special case: Venezuela runs as a branch of the Panama entity | https://www.pedidosya.com.ve/about/terminos-condiciones |

Local entities exist in all 15 countries. Full table in the research brief.

### Leadership and strategy themes

- CEO Esteban Gutiérrez, CFO Pablo Setuain, CTO Juan Martín Sotuyo, CPO Leandro Malandrini, COO Juan Martín López. ✅
- **Depth, not new countries.** Strategy is to grow inside the 15 existing markets. ✅ (2025-03-19)
- **Quick commerce and fintech are the 2026 priorities.** ✅ (2026-01-02)
- **Subscription is now the growth engine.** ✅
- **Technology hub.** PedidosYa is Delivery Hero's global tech hub, with USD 87M of technology investment in 2025. ✅

---

## 4. FINANCIALS

Delivery Hero does not publish a PedidosYa-only P&L. The Americas segment is the proxy. ⚠️ All figures in EUR as reported. No currency conversion made.

### Growth trajectory (verified points only, nothing interpolated)

| Year | Data point | Source |
|---|---|---|
| 2009 | Founded in Montevideo by Ariel Burschtin, Álvaro García and Ruben Sosenke | https://en.wikipedia.org/wiki/PedidosYa |
| 2014 | **Ownership change:** Delivery Hero acquires a majority stake | same |
| 2018 | About nine countries, 10 or 11 payment providers, about 30% of orders paid online. Brazil operation sold to iFood | https://www.spreedly.com/blog/payments-dialog-episode-2-payments-and-delivery-in-latin-america-with-mathias-fonseca |
| 2019 | Valuation USD 1B | https://en.wikipedia.org/wiki/PedidosYa |
| 2020 | Acquires Glovo's Latin America operations for USD 201M | same |
| 2021 | Valuation USD 3B. Enters Peru, Guatemala and Ecuador | same |
| FY 2024 | Americas GMV EUR 3,642.0M; segment revenue EUR 939.6M (as originally reported). First profitable year | https://www.tradingview.com/news/eqs:81958b162094b:0-delivery-hero-reports-strong-q4-while-business-transforms-into-everyday-app/ |
| FY 2025 | Americas GMV EUR 4,079.6M (+12.0% reported, +15.2% constant currency); revenue EUR 977.4M on the harmonized basis; adjusted EBITDA EUR 100.0M | https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline |
| H1 2026 | GMV EUR 2,559.8M (+29.4%); revenue EUR 618.9M (+31.3%); adjusted EBITDA EUR 70.3M (+52.2%) | https://ir.deliveryhero.com/media/document/8efa12b2-3fa3-4ebd-9333-ece6881bae50/assets/DE000A2E4K43-Q2-2026-EQ-E-00.pdf |

Americas segment figures for 2016 to 2023 were not retrieved in this pass.
**Future ownership change:** Uber and SSW Partners, expected second half of 2027.

### Recent quarters (Americas segment)

| Quarter | GMV (EUR M) | Revenue (EUR M) |
|---|---|---|
| Q1 2025 | 1,024.4 | 242.9 |
| Q2 2025 | 953.5 | 228.4 |
| Q3 2025 | 960.6 | 231.3 |
| Q4 2025 | 1,141.2 | 274.8 |
| Q1 2026 | 1,210.3 | 293.6 |
| Q2 2026 | 1,349.4 | 325.3 |

Trend read: growth re-accelerated. Revenue growth went from 21% in Q1 2026 to 31% in Q2 2026. Adjusted EBITDA margin on GMV moved from 2.3% (H1 2025) to 2.7% (H1 2026). Delivery Hero raised FY 2026 group guidance on 27 August 2026.

### Last full year: FY 2025 (January to December 2025)

| Metric | Americas segment | Delivery Hero group |
|---|---|---|
| GMV | EUR 4,079.6M | EUR 49,196.8M |
| Revenue | EUR 977.4M (harmonized) or EUR 1,057.6M (as originally reported) | Not retrieved |
| Adjusted EBITDA | EUR 100.0M (2.5% of GMV) | EUR 903.0M |
| Net income, gross margin | Not published at segment level | Not retrieved |

### Other material items

- **Uber offer:** equity value USD 14.8B; committed bridge facility of about EUR 14B; acceptance period to 5 November 2026; regulatory reviews pending. ✅
- **Group cash generation:** free cash flow before extraordinary items EUR 348.3M in H1 2026, against negative EUR 7.7M in H1 2025. ✅
- **Group debt cost:** interest expense of EUR 169.8M in H1 2026, up after a new USD term loan in March 2026. ✅
- **Argentina hyperinflation accounting (IAS 29)** distorts EUR growth rates for the segment. ✅
- **Customer wallet liabilities:** EUR 22.6M at group level on 30 June 2026. ✅

**So what for the call:** the segment earns 2.7% of GMV in adjusted EBITDA. Payment cost is charged on that same GMV base, so savings on processing and recovered payments land on a thin margin. ⚠️ Use it as a question about where payment cost sits in their plan, not as a claim.

---

## 5. COMPETITIVE LANDSCAPE

**Share basis:** the only regional comparison found is Sensor Tower's Q2 2025 ranking of the top five food delivery apps in Latin America. Shares below are **derived by this brief** from the active-user figures on that page (56M + 12M + 11M + 6.8M + 4.8M = 90.6M). They measure app active users among those five apps, not orders, GMV or revenue, and Sensor Tower does not state whether the figures are weekly or monthly. Source: https://sensortower.com/blog/2025-q2-unified-top-5-food%20delivery%20services-units-latin_am-63da96fbe1714cfff1c1e5a1

| Competitor | Segment | Estimated share (source and basis) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Rappi | Direct, overlapping markets | 13.2% (derived, app active users, Sensor Tower Q2 2025) | About 12M active users; revenue USD 855.52M in 2023 (Sacra estimate) | Super-app with its own fintech; weighing an IPO | Yuno, public case study, 20+ processors |
| Uber Eats | Direct, overlapping markets | 7.5% (same basis) | About 6.8M active users in LatAm; Uber Delivery gross bookings USD 27.463B in Q2 2026 (global) | Future owner of 13 PedidosYa markets; relaunched in Argentina on 2026-03-02 | Uber is named as a customer on Yuno's About page; scope not stated |
| DiDi Food | Direct, overlapping markets | 5.3% (same basis) | About 4.8M active users | Backed by DiDi's mobility base | No public evidence found |
| Mercado Libre Restaurantes | Direct, Argentina | No estimate available | Launched Q4 2025 in Rosario | Owns Mercado Pago and the largest marketplace audience | In-house (Mercado Pago) |
| Yummy | Direct, Venezuela | No estimate available | 18M yearly transactions; valuation above USD 200M | Local super-app | No public evidence found |
| iFood | LatAm, Brazil only | 61.8% (same basis) | About 56M active users; 120M orders per month | Dominant in Brazil; iFood Pago | No public evidence found |
| 99Food (DiDi) | LatAm, Brazil only | No estimate available | Launched April 2025; 60+ cities | New entrant | No public evidence found |
| Keeta (Meituan) | LatAm, Brazil only | No estimate available | USD 1B pledged for Brazil | New entrant with deep capital | No public evidence found |
| DoorDash (Wolt, Deliveroo) | Global peer | No estimate available | FY 2025 revenue USD 13.717B | Post-merger consolidation | No public evidence found |
| Just Eat Takeaway | Global peer | No estimate available | Revenue USD 1.9B in six months after the Prosus acquisition | Marketplace model | Payrails (2025-06-12) |
| Grab | Global peer | No estimate available | Deliveries GMV USD 7.9B in FY 2025 | Super-app; buying foodpanda Taiwan | No public evidence found |
| Swiggy | Global peer | No estimate available | Not retrieved | Food plus quick commerce in India | Juspay |

**Where PedidosYa sits:** 12.1% on the same derived basis (about 11M active users), second in downloads behind iFood. iFood's share comes from Brazil, where PedidosYa does not operate. In Ecuador, PedidosYa claims more than 50% of active delivery users (company claim, 2026-03-16).

**For the call:** the closest competitor in the overlapping markets already orchestrates with Yuno, and the future owner is named on Yuno's customer list. Use Rappi as the public proof point. Say nothing about Uber beyond the website.

---

## 6. PAYMENTS MONEY MAP

| Layer | What we know | Label |
|---|---|---|
| Vault and routing | Spreedly, used mostly as vault | ✅ published, ⚠️ current usage |
| Main provider | dLocal, per Belén | ⚠️ |
| dLocal public trace | "PEDIDOS YA" listed under "Dlocal Service" on Bancard's Infonet portal (Paraguay); biller "Pedidosya, Dlocal" in El Salvador | ✅ |
| Cards | Worldpay and other PSPs through Spreedly | ⚠️ internal deck only |
| Chile debit | Klap and Webpay | ✅ T&C |
| Providers overall | "10 or 11 providers, depending on the country" | ✅ dated 2018 |
| Fraud | Cybersource Decision Manager | ✅ dated 2021 |
| 3DS | Not verified | 🔍 |
| Rider cash remittance | Pago46 in Argentina and Chile | ✅ |
| Merchant wallet, Argentina | PeYa Wallet, with Wibond as the registered payment provider behind the accounts | ✅ |
| Reconciliation | Simetrik and SAP | ✅ job listing |
| In-house | Payments Tribe with a Payment Gateway team | ⚠️ from job listings |
| Hiring | Backend engineers for Fintech and Payment Services (September 2026); Rider Payments Optimization Specialist | ✅ |
| PCI | Self-declared compliance in T&Cs; card data held by third parties | ✅ |

### Methods by market (confirmed only)

| Market | Methods confirmed |
|---|---|
| Argentina | Cash, POS on delivery, cards, virtual wallet, PedidosYa wallet balance |
| Chile | Cash, credit card, debit via Klap, debit via Webpay, prepaid, wallet, MACHBANK app |
| Uruguay | Cash (not after 19:00), cards, POS on delivery, Pluxee food card |
| Peru | Cash, POS on delivery, cards, Yape in-app |
| Bolivia | Cash, cards, QR payments |
| Paraguay | Cash, cards, Tigo Money (2022) |
| Ecuador | Cash, POS on delivery, cards, wallet, Deuna |
| Panama | Cash, POS on delivery, cards, Yappy (2023) |
| Venezuela | Cash, POS, Pago Móvil, cards, Zelle (2022) |
| Central America and Dominican Republic | Cash, POS on delivery, cards |

### Framing rules for this account

- Speak about performance, cost, reliability and speed to market. Never about gaps.
- Reference only the methods in the table above.
- Spreedly and dLocal stay. Yuno is the layer above.

---

## 7. TOP MARKETS

Web traffic shares are derived by the research brief from Similarweb (August 2026) and are not order shares.

| Market | Future owner | Web traffic share | For the call |
|---|---|---|---|
| Argentina | Uber | 42.4% | Largest market. Uber Eats relaunched here in March 2026 and Mercado Libre entered restaurants. Ask how approval rates compare with other markets |
| Chile | SSW Partners | 10.1% | Carve-out market with the most public refund complaints (3,417 at SERNAC in 2024). Best place to ask about standalone stack plans |
| Ecuador | SSW Partners | 6.4% | Carve-out market. T&C requires an "international" card online ⚠️. Deuna added in August 2026 |
| Peru | Uber | 5.3% | Yape live in-app. Regulator sanctioned the pre-selected tip in July 2026 |
| Uruguay | Uber | 3.8% | Home market and volume leader with Argentina and Chile. Cash restricted after 19:00 |
| Panama | Uber | 6.7% (anomalous spike) | Holds the entity that runs Venezuela |
| Bolivia and Paraguay | Uber | 1.5% and 2.5% | QR in Bolivia, Tigo Money in Paraguay, dLocal biller in Paraguay |

---

## 8. NEWS AND SIGNALS

| Date | Item | Why it matters |
|---|---|---|
| 2026-09-24 | Delivery Hero CEO Niklas Östberg stays, contract to April 2029, citing the takeover offer | Parent leadership stable through the deal |
| 2026-09-18 | PedidosYa report: online supermarket purchases +62% in Latin America | Rapport opener |
| 2026-09-17 | PeYa Wallet enables QR payments for merchants in Argentina | Fintech arm keeps adding rails |
| 2026-09-02 | Delivery Hero boards recommend accepting Uber's offer | Deal momentum |
| 2026-08-27 | H1 2026 results; acceptance period opens, runs to 5 November 2026 | Next dated milestone |
| 2026-08-12 | Deuna added as a payment method in Ecuador | New local method, one market |
| 2026-07-22 | Peru's regulator fines PedidosYa for a pre-selected tip at checkout | Checkout under regulatory watch |
| 2026-07-16 | Uber signs agreement to acquire Delivery Hero | Ownership split |
| 2026-07-04 | Chile launches family groups with assigned balance | Stored value feature |
| 2026-05-01 | Uruguay stops accepting cash after 19:00 | Volume moves to digital |
| 2026-04-22 | Fintech ecosystem presented: advances, credits, PeYa Wallet | Payout and wallet flows growing |
| 2026-03-02 | Uber Eats relaunches in Argentina | Competitive pressure in the largest market |
| 2026-01-02 | 2026 plan: more dark stores and fintech push | Stated priorities |

---

## 9. SELLING YUNO HERE

### Core frame

Yuno is an AI native operating system for global financial infrastructure. For PedidosYa: one layer above the providers, vault and methods they already run, so they can add or rebalance providers, launch local methods and see every transaction in one place, in a stack that stays portable while ownership changes.

### Hooks with proof points

| Hook | Proof (real Yuno cases and published figures only) |
|---|---|
| Less dependency on one provider, lower cost | Rappi: new provider implementation time cut to zero. Published: 27% savings on payment costs |
| Faster local methods | inDrive: 10 LATAM markets in under 8 months. Published: 90% reduction in development time |
| Fewer failed and orphan payments | Livelo: +5% approval, 50% recovery. Published: 30% recovered revenue |
| Real-time visibility | Rappi: issue detection in milliseconds versus 5 to 10 minutes manually |

### Landmines

- Never say they have no orchestrator. Spreedly is published.
- Never criticise dLocal.
- Nothing about Uber beyond Yuno's public customer list.
- Do not use the deck's approval charts (92% vs 81%, +10pp).
- Do not name Mercado Pago, MODO, Apple Pay or Google Pay as missing or present. None were verified.
- Do not promise settlement or fee reconciliation until product confirms what is generally available.
- Do not assume "collections" means checkout.
- Do not bring up the Elliot thread unless she does.

---

## 10. BE READY FOR

| They may ask | Ready answer |
|---|---|
| How do you charge? | A platform fee plus a per-transaction fee that steps down with volume. No number today: the proposal follows the data request. Internal: check the Pricing Policy before quoting anything |
| Do you work with dLocal? | Yes, dLocal is a live connection in Yuno. It can stay as one of the providers, with others added next to it |
| What happens to our saved cards in Spreedly? | Yuno can work above the current vault, and tokens can be migrated when it makes sense. The Solutions Engineer defines the approach in the technical session |
| How long does integration take? | One integration through SDK or API. New providers and methods are enabled by configuration afterwards. inDrive reached 10 markets in under 8 months |
| We have our own payments team. Why buy? | The team keeps control of rules and routing. Yuno takes the maintenance of connectors, which is where the engineering time goes |
| Are you certified? | Yuno publishes ISO 27001, ISO 27701, GDPR, PCI DSS and SOC 2 Type 2, and is a Visa Service Provider. Source: https://y.uno/en |
| Who else in delivery uses you? | Rappi and inDrive, both with public case studies |
| What about Uber? | Yuno's layer is provider-agnostic, so the stack stays portable under any owner. Nothing more |
| Can you handle payouts to riders and merchants? | Yuno has a payouts product. Scope per market gets confirmed in the technical session 🔍 |
| Can you reconcile across providers? | Unified visibility across providers today. Confirm the exact reconciliation scope with product before committing 🔍 |

---

# LIVE ZONE

## 11. AGENDA (30 minutes)

| Time | Block | Owner | Notes |
|---|---|---|---|
| 0 to 3 | Intros, roles, the referral | Alejandro | ____ |
| 3 to 15 | Discovery: what she wants to change, which flow, which markets, why now | German | ____ |
| 15 to 21 | Yuno in five minutes, shaped by what she said | German | ____ |
| 21 to 27 | Decision path: who owns it, Berlin, Uber timeline | German | ____ |
| 27 to 30 | Next step and data request | German | ____ |

## 12. DISCOVERY QUESTIONS

**Context and trigger**
1. Belén, para ubicarnos: ¿qué cubre tu rol de collections en PedidosYa y en qué países?
   Notes: ____
2. ¿Qué fue lo que los llevó a evaluar un cambio de proveedor ahora?
   Notes: ____
3. Cuando hablamos de collections, ¿es el cobro al usuario en el checkout, la recaudación del efectivo de los repartidores, el cobro a comercios, o las tres?
   Notes: ____

**Current stack**
4. ¿Qué proveedores tienen hoy por país y qué parte del volumen pasa por cada uno?
   Notes: ____
5. ¿Cómo deciden hoy a qué proveedor va cada transacción? ¿Hay ruteo o cada país tiene un proveedor fijo?
   Notes: ____
6. ¿Qué rol cumple Spreedly hoy en la operación?
   Notes: ____
7. Cuando un proveedor se degrada, ¿cómo se enteran y cuánto tardan en mover el tráfico?
   Notes: ____

**Pain**
8. ¿Qué es lo que más les cuesta hoy: costo, aprobación, tiempos de liquidación, conciliación o soporte del proveedor?
   Notes: ____
9. ¿Qué tasa de aprobación tienen en sus mercados principales y cómo se compara entre países?
   Notes: ____
10. ¿Cuánto tarda hoy sumar un método de pago local nuevo, desde que lo deciden hasta que sale a producción?
    Notes: ____
11. ¿Cómo manejan las devoluciones y la conciliación cuando conviven varios proveedores y métodos?
    Notes: ____
12. ¿Qué parte de los pedidos se paga hoy online y qué parte en efectivo?
    Notes: ____

**Decision**
13. ¿Quién más participa en una decisión así? ¿Payments, producto, finanzas, tecnología?
    Notes: ____
14. ¿Qué se decide hoy en la región y qué se decide en Berlín?
    Notes: ____
15. Con el acuerdo con Uber y SSW, ¿cambió algo en cómo planean el stack de pagos, sobre todo para Chile y Ecuador?
    Notes: ____
16. ¿Tienen alguna fecha que marque el plazo para este cambio, como un vencimiento de contrato?
    Notes: ____
17. ¿Cómo sería un primer paso razonable para ustedes: un país, un flujo, una prueba?
    Notes: ____

## 13. POST-MEETING CHECKLIST

- [ ] Recap email the same day, in Spanish, sober, no links, with the agreed next step and a date
- [ ] Log every confirmed fact: her real title, the flow she wants to change, providers by market, the name of the Head of Payments
- [ ] Book the second session with the decision owner and a Yuno Solutions Engineer
- [ ] Send the data request in writing: volume by market and provider, cost per provider, approval rate by market
- [ ] Align with Justo on how this thread relates to the Delivery Hero opportunity and to the 21 September email to Leandro Malandrini
- [ ] Update memory and the research brief with what was confirmed and correct anything marked ⚠️

---

## APPENDIX: SOURCES

Full research brief with every source URL: `data/research/pedidosya-2026-09-29.md`

Internal sources:
- Alejandro Albarracín's voice note (transcribed by German, 29 September 2026)
- Google Calendar event "PeYa & Yuno"
- Gong, accounts Delivery Hero and PedidosYa
- Google Drive: "Delivery Hero + Yuno _ Business Deck_V3.pptx" (same document as deck.y.uno/DeliveryHero)
- Slack: #mpe-berlin-2026, #roberto-ai, #sdr-salesops, #integration-product-inquiries

Primary public sources:
- Uber and Delivery Hero agreement: https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm
- Delivery Hero H1 2026 report: https://ir.deliveryhero.com/media/document/8efa12b2-3fa3-4ebd-9333-ece6881bae50/assets/DE000A2E4K43-Q2-2026-EQ-E-00.pdf
- Delivery Hero Q1 2026 trading update: https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline
- Spreedly case study and podcast: https://www.spreedly.com/customers/pedidosya
- dLocal biller listings: https://www.infonet.com.py/servicios_disponibles/Dlocal%20Service · https://www.bitrefill.com/sv/es/factura/pedidosya-dlocal-bill-el-salvador/
- Chile T&C: https://www.pedidosya.cl/about/terminos-condiciones
- SERNAC 2024 complaints: https://www.sernac.cl/portal/604/w3-article-83827.html
- Sensor Tower Q2 2025: https://sensortower.com/blog/2025-q2-unified-top-5-food%20delivery%20services-units-latin_am-63da96fbe1714cfff1c1e5a1
- PedidosYa history: https://en.wikipedia.org/wiki/PedidosYa
- Yuno published figures, certifications and customers: https://y.uno/en · https://y.uno/en/about
- Rappi and inDrive case studies: https://y.uno/en/success-stories/rappi · https://y.uno/en/success-stories/indrive
