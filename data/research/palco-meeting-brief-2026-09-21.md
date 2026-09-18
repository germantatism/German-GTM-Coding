# Meeting Brief: Yuno <> PALCO Commercial Proposal (Sep 21, 2026)

Google Doc: https://docs.google.com/document/d/1h4L49gak_2Nbs_maT9sn2M-SIf1ypWD-aRfLprtL48s/edit

**Monday, September 21, 2026 · 11:00 Bogotá (GMT-5) · 10:00 Mexico City · 18:00 Madrid**
Google Meet: https://meet.google.com/xyh-vxie-ovk · Event "Palco + Yuno | Propuesta", organized by German Tatis, created Sep 15.
⚠️ The calendar event currently ends at **11:30** (30 minutes). The acceptance emails from Fernando, Alfonso, Miguel and Joaquin all say **11:00 to 11:45**; the event was shortened on Sep 16 at 20:44 UTC after they accepted. Decide the length before Monday and re-send if 45.

**Objective, what winning looks like:** leave with the Mexico pilot approved: tenants named, kickoff date, and the person who signs. Not "we will review internally." Patricio wrote that September defines their path; Monday is the 21st.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state as fact in the call · 🔍 ask in discovery.

---

## ⚠️ PRE-MEETING ACTIONS

1. **Fix the meeting length.** Calendar says 30 minutes, invitations said 45. The flow below is sized to 30 with a 45-minute variant. If you want 45, update the event today so Madrid does not drop at 18:30.
2. **Apply the deck corrections** (Deals/Palco/palco-proposal-review-2026-09-18.md, script build/fix_review_0918.py after re-authenticating the Slides API). Do not present Risk conditions at $0.04 or the "Contrato a 3 años" footer. Add the "what you asked, how we cover it" slide and the pilot block.
3. **Ask Fernando one question by Friday:** is $37.09 the average per ticket or per transaction? Their own monthly table gives about $120 per transaction ($28.3M ÷ 235,000). If it is per ticket, the recovered GTV triples and Yuno's cost per order falls from 27 bps to about 8 bps. Ask before Monday, not during.
4. **Get Carlos's three confirmations with a date:** catalog coverage for Openpay, Banorte, Santander, Mercado Pago and Fiserv; which Mexican processors support split at capture with the tenant as MoR; recurring charges with Mexican processors. Without Openpay, Banorte and Santander in the catalog, lever 1 does not exist. Carlos and Magdalena are NOT on the invite; decide whether to add Carlos for the technical answers.
5. **Brief Joaquin (15 minutes):** he takes Mexico (bank pre-sales by BIN with Banamex, Santander and Banorte; on-sale peaks) and writes down every commitment, name and date. German runs numbers and the close.
6. **Decide your trading currency before the call:** a reduced platform fee during the pilot (the calculator allows up to 3 months of fee credit without sign-off). It is given only in exchange for named tenants and a date, never unilaterally.
7. **Miguel Ramírez Lombana is still "Maybe."** He is CRO and co-owner and Fernando said the commercial part needs Patricio and "quizás Miguel." Have one sentence ready for him (Section 1, hook 1). Do not send the deck before the call; send the PDF the same day.
8. **Rapport hooks to verify manually:** Patricio's LinkedIn (https://www.linkedin.com/in/patricio-villalobos-cuevas-9873a025/), Alfonso's (https://es.linkedin.com/in/alfonso-uribarri-carrasco-82a60784/), Fernando's (https://mx.linkedin.com/in/fernando-nava-feldman), Miguel's (https://www.linkedin.com/in/miguel-ram%C3%ADrez-lombana-10886/). Automated fetches were blocked; titles below come from search snippets and the company's own emails.

---

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. **They already diagnosed the problem and named the cure.** Patricio, Sep 2: "en México, que es la mitad de nuestro volumen, la aprobación en tarjeta está entre 56% y 68% según el procesador. Es exactamente lo que esperamos resolver con ruteo inteligente y reintentos." You are pricing execution, not selling orchestration. ✅
2. **Each tenant is merchant of record and the processing accounts belong to Palco's clients** (Patricio Sep 2, corrected by Alfonso Sep 15: partners per country own the account, collect, and settle to Palco monthly; Palco earns a fee per ticket or a fixed price per event). The approval uplift lands with the tenant. Only lever 4 (run-ops) lands in Palco's own P&L. ✅
3. **Their Mexican card rails run 10 to 16 points below their own market:** Openpay 58.0%, Banorte 59.6%, Santander 56.1%, against roughly 72% credit and 69% debit in Mexico (RankingsLatAm, Sep 2024). Inside one provider, Mercado Pago approves 92.1% on wallet and 67.9% on card. Routing is the variable, not the country. ✅
4. **Alfonso's objection is the deal:** "el coste se traslada al cliente final; nuestros clientes escogen pasarela por precio; esperamos que el ahorro por ruteo compense." With the deck's own numbers, routing cost savings alone ($59K to $99K a year) do NOT cover Yuno ($281K). Approval does: $5.2M to $10.2M of recovered GTV, 18 to 36 times the cost. Say it before he computes it. ✅
5. **The number you said on Sep 15 was "alrededor de $15K como fee mínimo."** The proposal is $7,000 fixed plus a per-approved-transaction ladder: $19,044 a month in payments at their volume, $23,404 with selective 3DS and fraud. Alfonso assumed $15K to $30K. Be ready for "dijiste 15." ✅

### Three hooks, in priority order

**Hook 1, for Patricio and Miguel: payments becomes a Palco product, not a cost.** Every point of Palco fee on the $7.7M of recovered GTV is $77K a year; lever 4 alone covers 82% to 128% of Yuno's annual cost. For a PE-backed company with an expansion mandate, that turns a procurement decision into a product decision. One sentence for Miguel if he joins: "esto convierte pagos en una línea de ingreso de Palco, no en un costo."

**Hook 2, for Alfonso: your own numbers prove it is the route, not the platform.** Same checkout: Redsys 88.1% and ECI 99.7% in Spain, UepaPay 98.0% in DR, Authorize.net 90.3% in the US, Mercado Pago wallet 92.1%. Mexico card 56% to 60%. And you keep every integration and every contract; Yuno sits on top and keeps the connectors alive so Fernando does not build the next country.

**Hook 3, for Fernando: integrations without building them.** His own words on Sep 15: "lo que más nos interesa es la posibilidad de contar con las integraciones con los métodos de pago sin tener que trabajarlas nosotros... es un cuello de botella sumamente costoso." Sandbox is already in his hands.

### THE objection they will raise, and the answer

> Alfonso: "Tienes razón en que el ruteo de costo solo no paga esto: son 7 a 12 puntos básicos contra 27. Lo que lo paga es la aprobación. Un tenant que hoy aprueba 62 y pasa a 67 vende 8% más. Nadie cambia de pasarela por 27 bps si vende 8% más."

Requirement: keep costs flat for the end client. Benefit: 27 bps per $37.09 ticket against +8% to +16% approved sales in the main cohort. Proof: their own table, +5 pp is 10,490 extra approved transactions a month at $37.09; +10 pp is 20,980.

### The ask

A Mexico pilot: 3 to 5 tenants on Openpay, Banorte and Santander through sub-accounts and SDK, baseline = their August table, review at 90 days, Carlos onboarding the week of Sep 28. Close with two questions: "¿Qué tenants pondrían en el piloto?" and "¿Quién firma el piloto de su lado, tú o Miguel?"

### Rapport opener

"Patricio, gracias por la data del 2 de septiembre: casi nadie manda aprobación por procesador sin que se lo pidan." Then tell him you did the arithmetic on it and open with the Mercado Pago wallet-versus-card gap. That proves you read it. Patricio closed his last message with "looking fwd man a la propuesta 👊🏽"; match the energy, skip the platform tour.

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Invite status |
|---|---|---|---|
| Patricio Villalobos Cuevas | CEO and co-owner, operates from Madrid (+34) | PALCO | Accepted |
| Alfonso Uribarri Carrasco | Co-founder (2017), Manager of Development and Support, Madrid | PALCO | Accepted |
| Fernando Nava Feldman | Signs as Technical Account Manager, Palco México (CDMX); introduced by Patricio as VP of Engineering | PALCO | Accepted |
| Miguel Ramírez Lombana (mike@pal.co) | Co-owner; Chief Revenue Officer since Sep 2025 (LinkedIn via search snippet) | PALCO | **Tentative ("Maybe")** |
| Joaquin Mann | BDM North America (Mexican; joined the week of Sep 7) | Yuno | Accepted |
| German Tatis | BDM, organizer | Yuno | Accepted |
| Not invited | Carlos Medina (Implementation Engineer), Magdalena Torrealba (relationship owner), Álvaro García Torres, Javier Sánchez (OOO to end of month) | | |

**Patricio Villalobos Cuevas, CEO and co-owner.** Mexican media-and-internet founder (co-founded mediotiempo.com, sold to Time Warner in 2010; juanfutbol in 2014) who bought into Palco with Bocel Private Equity and Miguel in Oct/Nov 2025. ✅ Not a payments executive, yet he personally wrote a six-point technical agenda covering split, 3DS, tokenization, multi-tenant billing, PCI and BIN routing. Informal, fast, decides. **How to read him:** he wants the business case and the price in one breath, and he wants to know how Palco makes money on it. He will not defend the 50 integrations; that is Alfonso's job.

**Alfonso Uribarri Carrasco, co-founder, Manager of Development and Support (Madrid).** LinkedIn title confirmed by search snippet (second source after RocketReach). ✅ Built and owns the 50+ gateway integrations. Spoke the most on Sep 15, corrected the business model, raised the cost objection twice, and closed with "me ha gustado bastante" and "bastante logrado, fácil de configurar y bastante completo." **How to read him:** the risk in the room and also the one who said the product is good. He is thinking about how to package this to his clients, who choose gateways by price. Any word that sounds like "replace" loses him; "you built the hard part, we keep it alive and add the decision layer" keeps him.

**Fernando Nava Feldman, Technical Account Manager Palco México (CDMX).** His LinkedIn headline shows sonder.mut, the company Miguel co-founded in 2022 ⚠️, which is consistent with him arriving with the new owners. Coordinates every agenda on their side; Patricio calls him VP of Engineering. Sep 15: "el principal objetivo... contar con las integraciones con los métodos de pago sin tener que trabajarlas nosotros." **How to read him:** your champion for integrations, the one who will own the implementation, and the one who asked for options so that "por lo menos Patricio, quizás Miguel" attend the commercial session. Primary sandbox user already.

**Miguel Ramírez Lombana, co-owner, CRO (Mexico City).** Founding partner and CRO of mediotiempo.com (1999), co-founder and CEO of juanfutbol (2014, acquired), co-founder of sonder.mut (2022), chairman of tikitaka; Kellogg. ✅ (LinkedIn, Crunchbase, TheOrg via search snippets.) Quoted at the acquisition: "PALCO can become the silent infrastructure driving the live events industry." Reported on the Palco team at BMB 2026 in Mexico City on Aug 25 discussing ticketing operations in Mexico including payments ⚠️ (search snippet, source not opened). Was in the Sep 9 call briefly. **How to read him:** revenue owner. If he joins, hook 1 is his; he is the one who prices what Palco charges its tenants.

**Sponsor and intro path.** Magdalena opened the relationship (Jul 30 call, no recording) and requested the data. German has run it since Sep 4; Patricio welcomed him ("bienvenido German al equipo"). Carlos ran the Sep 15 demo. Neither Magdalena nor Carlos is on Monday's invite.

### Relationship timeline (calendar-verified where marked 📅)

| Date | Event |
|---|---|
| Jul 30 | First call Magdalena + Patricio; a pilot discussed. Not on German's calendar, no recording |
| Jul 31 | Magdalena requests volumes, ticket, TPV, mix, countries, approval by method, fraud |
| Aug 18 | Patricio apologizes, back from holiday |
| Sep 2 | Patricio sends the full data set and six questions; "septiembre es cuando estaremos definiendo el camino" |
| Sep 4 | Magdalena forwards to German |
| Sep 9 📅 | "Yuno / PALCO - Demo & Payment Orchestration Review" 08:00 to 09:00 COT, organized by Patricio; Patricio, Fernando, Javier, Magdalena, German attended; Susana never responded |
| Sep 10 | German proposes technical-session slots |
| Sep 14 | Fernando confirms Tuesday 10:00 COT and adds Alfonso and Álvaro |
| Sep 15 📅 | "Palco + Yuno \| Deep Dive" 10:00 to 10:45 COT (48 min, Gong id 891469394762814345). Alfonso, Fernando, Álvaro; German, Carlos, Joaquin, Magdalena. Same day: follow-up email with sandbox, docs and four slots |
| Sep 15 | Fernando picks Monday Sep 21 11:00 COT |
| Sep 16 📅 | Internal "Propuesta PALCO" (German + Joaquin, 13:15 to 15:00 COT): pricing calculator, tiers, 3DS, network tokens, white-label model, business case |
| Sep 16 | Patricio: "looking fwd man a la propuesta 👊🏽". Fernando, Alfonso, Joaquin accept; Miguel "Maybe" |
| Sep 21 📅 | This meeting |

Prior meetings with the people on this call exist on the calendar: Sep 9 (Patricio, Fernando) and Sep 15 (Alfonso, Fernando). Miguel has not been in a calendar event; he appeared briefly on Sep 9 per Fernando. **Implication:** follow-up framing. They have the demo, the dashboard walkthrough, the sandbox, the SDK and API docs, and your $15K reference. Monday is the first time Patricio hears the answers to his six questions and the first time anyone sees a price on paper.

---

## 3. THE COMPANY

PALCO, formerly Palco4, is a white-label B2B ticketing platform: promoters, venues, clubs and per-country partners sell under their own brand on Palco's technology. Legal entity **PALCO4 TECNOLOGIA Y SERVICIOS SL**, CIF B87730628, Las Rozas de Madrid. ✅ Rebranded to PALCO at pal.co.

| Metric | Value | Source |
|---|---|---|
| Venues | 500+ | techla.pro, Oct 31, 2025 |
| Countries | 30 claimed; 18 markets with native gateway integrations | techla.pro; es.pal.co |
| Tickets | 8M+ per year (registry listing) | einforma |
| Employees | 15 (2023 registry) → 42 to 47 (2026, Tracxn) | einforma; Tracxn |
| Payment gateways | 50+ native integrations | es.pal.co |
| Business model | Fee per ticket sold or fixed price per event (Alfonso, Sep 15) | Call transcript |
| 2025 marquee on-sales | Bad Bunny DR (3 sellouts in 8 hours), Tini AR (200K+ in 18 hours), Don Omar MX (200K+ in 24 hours), Shakira UY (86K in 48 hours) | en.pal.co, vendor-claimed |

### Corporate structure

| Entity / market | Status | Note |
|---|---|---|
| PALCO4 TECNOLOGIA Y SERVICIOS SL (Spain) | ✅ Confirmed | Only legal entity found |
| Mexico, Argentina, DR, Puerto Rico | ⚠️ No local entity found | pal.co footer and privacy policy name none |
| Merchant of record | ✅ The tenant, never Palco | Processing accounts belong to per-country partners (Alfonso, Sep 15); Palco wants its own accounts in Mexico and Europe "eventually" |
| Ownership | Bocel Private Equity + Patricio Villalobos + Miguel Ramírez Lombana, Oct/Nov 2025 | Press says majority investment; PitchBook lists a minority stake ⚠️ |

**Strategy themes:** LatAm expansion (new markets by mid-2026), white-label stores, dynamic pricing, upgrades, omnichannel and data; moving toward large venues and sports clubs as direct clients where Palco could run its own merchant account (Alfonso, Sep 15). Ramírez's phrase, "silent infrastructure driving the live events industry," is worth echoing.

---

## 4. FINANCIALS

Palco is private and discloses no revenue. Everything verifiable:

| Item | Value | Period and source |
|---|---|---|
| Funding | $9.5M raised (total) | Crunchbase / PitchBook profile, date of rounds not shown |
| Ownership change | Bocel Private Equity with Villalobos and Ramírez Lombana | Announced Oct 31, 2025 (levelup.com, techla.pro); majority per press, minority per PitchBook ⚠️ |
| Headcount | 15 (2023) → 42 to 47 (2026) | einforma registry; Tracxn |
| Processed volume | ~$457M TPV LTM, ~$28.3M a month (as reported by Patricio) | Email Sep 2, 2026, confidential. Excluded from the business case by German's rule; the base is 235,000 × $37.09 |
| Payment mix | Card 75.7%, cash 13.2%, box-office pinpad 6.3%, transfer 3.0%, other 1.8% | Email Sep 2 |
| Revenue, margin, debt | Not disclosed | |

**So what for the call:** a PE-owned company eighteen months into new ownership with an expansion mandate, no revenue line from payments, and a cost-sensitive client base. The financial conversation is not "what does Yuno cost" but "what does Palco earn per point of fee on recovered GTV" and "what does the engineering team stop maintaining."

---

## 5. COMPETITIVE LANDSCAPE

Carried over from the Sep 9 brief (verified then). No research house publishes market share for any Spanish or LatAm ticketing player; rows say so rather than guess.

| Competitor | Segment | Estimated share (source, basis) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Ticketmaster México / OCESA | B2C Mexico | No estimate available | Dominant Mexican promoter and ticketer | Owns promotion and venues; Banamex pre-sale partnership | Bank pre-sales with MSI as core mechanic |
| Fever (Kzemos) | B2C, own IP | No valid estimate (raw €74M ÷ €725.6M is not a like-for-like share) | ~€74M revenue 2024, 1,420 staff, $1.8B valuation Jan 2023 | Originates IP, discovery app | "Limited payment collection agent," not MoR; PSP undisclosed |
| Atrápalo | B2C OTA | No estimate available | €233M group revenue FY2023; ~2M tickets/yr | Ticketing as one OTA vertical | Not verified |
| DICE | B2C mobile-first | No estimate available | $122M Series C at $400M (Sep 2021) | App-locked QR, no secondary market | Stripe Connect named in terms; agent, not MoR |
| Wegow | B2C discovery | Derived proxy 0.67% (€3.9M ÷ €578M Spain live music 2023, basis undisclosed) ⚠️ | Revenue €16.6M (2022) → €3.9M (2023) | Artist-following bolted onto ticketing | Intermediary; some events on the organiser's own gateway |
| vivenu | B2B white-label | No estimate available | 1,000+ organizers, 50+ countries | API-first enterprise white-label | Not disclosed |
| SecuTix (ELCA) | B2B white-label | No estimate available | 204 live sites, 75M tickets/yr | Sports, live, culture | Own payment product S-PAY, built in house |
| Tixly | B2B white-label | No estimate available | Performing-arts venues, Northern Europe | Cultural-venue specialist | Not disclosed |
| TuBoleta | B2C Colombia | No estimate available | 26+ years; Movistar Arena | Colombia incumbent | Not disclosed |
| PuntoTicket | B2C Chile | No estimate available | Estadio Nacional, Claro Arena | Chilean major-venue exclusives | Not disclosed |
| Superboletos / eTicket / Boletia | B2C Mexico | No estimate available | eTicket physical POS network | Promoter-aligned Mexican ticketers | Not disclosed |
| Joinnus | B2C Peru | No estimate available | Peru events platform | Single market | Not disclosed |

**Where Palco sits:** the only player that is simultaneously white-label B2B and deep in both Spain and LatAm, and the only one publishing a per-country map of 50+ gateway integrations. Every ticketing player in this set runs an agent model rather than MoR, which makes Palco's structure industry-normal and the split question the vertical's central payments problem. **For the call:** if build-versus-buy surfaces, SecuTix built its own payment product in house and DICE bought a marketplace architecture off the shelf; Palco has been on the SecuTix path and is deciding whether to stay on it.

---

## 6. THE NUMBERS PALCO SENT, AND WHAT THEY SAY

All first-party, from Patricio's email of Sep 2, 2026. Confidential. Per German's rule the business case uses **235,000 transactions a month × $37.09**, never the $457M or the processor-table volumes; from that table only approval rates and relative weights are used.

### 6A. Volume and mix, as sent

| Metric | Value |
|---|---|
| TPV last twelve months | ~$457M USD (excluded from modelling by instruction) |
| Average ticket | $37.09 USD |
| Monthly average | ~235,000 transactions / ~$28.3M USD |
| Method mix on annual TPV | Card 75.7% ($346M), cash incl. OXXO and Paynet 13.2% ($60M), box-office pinpad 6.3% ($29M), transfer 3.0% ($14M), wallets/BNPL/gift 1.8% ($8M) |
| Annual GTV by country | Mexico $211M, Argentina $62M, Spain $55M, DR $36M, Puerto Rico $31M, Paraguay $26M, Panama $12M, Honduras $5M, Guatemala $4.8M, USA $4.6M, rest ~$3M |
| Monthly by country (tx / GTV) | Mexico 94,800 / $14.2M · Argentina 69,300 / $5.1M · USA 32,300 / $3.4M · DR 14,600 / $2.6M · Uruguay 7,900 / $2.1M · Guatemala 6,500 / $334K · Honduras 4,200 / $181K · Paraguay 2,600 / $100K · Colombia 2,500 / $156K |
| Fraud and chargebacks | No consolidated data: each tenant is MoR and manages it with its processor |

### 6B. Approval by processor, as sent

| Processor | Market | Transactions / yr | Approval | Declined |
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

### 6C. What the table says (their figures, our arithmetic)

- **The cohort of lever 1** (Mercado Pago v2, Openpay, Banorte, Santander, Cybersource, Stripe, Bancard) is 1,952,600 attempts a year at a weighted 62.4% approval and holds 55.7% of all approved transactions. Applied to the base, that is about 130,900 approved and 209,800 attempts a month.
- **Same provider, 24 points apart:** Mercado Pago wallet 92.1% vs card 67.9%.
- **Same checkout, different country:** Spain 88% to 99.7%, DR 98%, US 90%, Mexico 56% to 60%.
- **Fiserv and Pixel Pay** (lever 2) are 88,000 attempts at a blended 47.6%, about 1.9% of approved transactions. Line VE at 8.7% is excluded: not a routing problem.
- **900,120 declines a year.** Nobody on their side has a consolidated view of fraud or chargebacks.

### 6D. The reconciliation gap (🔍 ask, never assert)

235,000 × $37.09 = $8.7M a month; Patricio also wrote ~$28.3M a month, and his monthly country table sums to $28.17M (about $120 per transaction). The most likely reading is that $37.09 is the price per ticket and a transaction carries about three tickets. This does not change the deck (German's rule: use the reported ticket), but it is the single question that most changes the case: if true, recovered GTV triples and Yuno's all-in cost per order drops from 27 bps to about 8 bps. Also unlabeled: whether the 235,000 are approved transactions or attempts, and whether they include cash, pinpad and transfer.

---

## 7. THEIR QUESTIONS, ANSWERED

Patricio's six written questions (Sep 2) plus the four asks from Sep 15. This is what the new slide "Lo que nos pidieron y cómo lo cubrimos" carries. Status is honest: ✅ verified, ⚠️ pending Carlos's confirmation.

| # | What they asked | Answer to give | Status |
|---|---|---|---|
| 1 | Split of commission in Mexico at capture, tenant stays MoR, Palco keeps its fee | Split Marketplace in the payment request: Yuno propagates the split instruction and the processor that supports it disperses the funds; sellers and onboarding via API. Shown by Carlos Sep 15 | ⚠️ Which Mexican processors support it in that direction (tenant collects, Palco's fee retained at capture): Carlos to confirm by [date] |
| 2 | 3DS mandatory on all card flows and its impact on approval with routing | 3DS as a routing condition (amount, BIN, risk, metadata), exemptions where they apply, retry on another route if authentication fails. Modelled as selective, about 40% of attempts, in the pricing | ✅ Impact measured in the pilot against their baseline. 🔍 Ask whose requirement the 100% 3DS is: acquirer, tenant, or Palco's own |
| 3 | Tokenization and recurring charges for abonos with Mexican processors | Yuno PCI vault plus multi-processor subscription management; failed renewals move to past-due and recover; network tokens quoted separately | ⚠️ Recurring with Openpay / Banorte / Santander: Carlos to confirm |
| 4 | Commercial model for multi-tenant: how it is contracted and invoiced per tenant | One Palco account with sub-accounts per client, each with its own routing, credentials and checkout. One contract and one invoice to Palco; tiers computed on aggregated volume across all sub-accounts; Palco decides whether to absorb or pass through. Yuno never contracts with Palco's clients | ✅ |
| 5 | Direct API instead of embedded SDK, and the PCI scope for Palco | Both supported. SDK: card capture handled by Yuno, no PCI scope for Palco. Direct API: PAN in Palco's front end, PCI DSS on Palco (SAQ-D or Level 1). Alfonso said 90% SDK | ✅ 🔍 Their current PCI attestation was never found publicly; ask, do not assert |
| 6 | Processing by a specific bank BIN for pre-sale promotions | Native routing condition by BIN, issuer country, brand, amount, installments, CVV and unlimited metadata. Commercially, this is how Palco offers venues the same bank pre-sale mechanic Ticketmaster runs with Banamex, Santander and Banorte | ✅ Shown Sep 15 |
| 7 | Credentials loaded by API (their clients self-configure their keys) | Organization API: GET catalog with required fields, POST connection. Also by dashboard | ✅ Shown Sep 15 |
| 8 | Split fee to one account, ticket price to another | Same Split Marketplace mechanism as #1 | ⚠️ Same processor confirmation as #1 |
| 9 | Real-time activity panel for on-sales, not email alerts | Insights per account: volume, approval by provider, by condition, first attempt vs retry, top issuers; monitors with thresholds, alerts and automatic traffic redistribution | ✅ Shown Sep 15 |
| 10 | Fallback when a gateway rejects, including redirect methods | Card declines and errors re-route to another provider automatically; the buyer never sees the intermediate decline. For redirect methods, fallback applies only if the redirect fails to create; a decline after redirect requires a new purchase | ⚠️ A real limitation; say it before Alfonso finds it in the sandbox |

Also asked on Sep 15 and answered: "¿Cobran por transacción, por volumen de dinero o mensual?" (Alfonso) → per approved transaction plus a fixed platform fee, never on amount. "Si agrupamos todos, ¿mejor tasa?" → yes, tiers on aggregated volume.

---

## 8. WHAT WE HAVE DISCUSSED SO FAR

**Jul 30 to Sep 2.** Magdalena and Patricio agreed to explore a pilot; Patricio sent the full data set and framed September as the decision month.

**Sep 9, demo and payment orchestration review** (Fireflies auto-summary only): Openpay and Mercado Pago, local processing in Bolivia and Venezuela, merchant of record and tokens, success cases, dashboard; agreed a product deep dive.

**Sep 15, technical deep dive (48 min, Carlos on the dashboard).** What they said: processing accounts belong to their clients; in 99% of operations the client collects and settles monthly to Palco; Palco wants its own accounts in Mexico and Europe eventually; main interest is integrations without building them (Fernando); main friction is cost passed to the end client who chooses gateways by price (Alfonso, twice); clients self-configure keys, so credentials by API matter; they want split fee/ticket, a real-time on-sale panel, and fallback on redirect methods; 90% SDK. What Yuno showed: organization with sub-accounts and per-account routing; profiles, permissions, audit; catalog and credentials by dashboard or API; processor cost fields feeding cost-based smart routing; routing canvas with conditions (brand, BIN, country, amount, installments, CVV, metadata), decline and error routes, traffic split, smart routing by conversion plus latency or cost, monitors with alerts and automatic redistribution; anti-fraud and 3DS connectors in the catalog; checkout builder; operations timeline with "ver ruta"; Insights. Two commercial models were put on the table by German: white label (fixed plus variable) and connection-only (variable only); Alfonso sees white label for new large venues and clubs where Palco runs its own merchant, and says current local partners are hard to move. German said "alrededor de $15K como fee mínimo mensual"; Alfonso assumed $15K to $30K. Alfonso's close: "me ha gustado bastante."

**Sep 15, follow-up email (sent):** sandbox (Fernando primary user), SDK and API docs, four slots. It states: "Inicialmente, veremos a Yuno como una solución directa para sus clientes actuales." Fernando chose Monday 11:00 COT; Patricio: "looking fwd man a la propuesta."

**Internal read (Carlos, Slack Sep 15):** "los vi bien, interesados"; simplest phase 1 is Palco using Yuno for connections and routing "como un proveedor," with their merchants' checkout on our SDK. German agreed.

**Sep 16, internal session German + Joaquin (Gemini notes):** pricing calculator, tiers, 3DS, risk conditions, network tokens, token vault, white-label model, business case. Output: deck v2/v3 with the four-lever business case on 235,000 × $37.09 and pricing at $7,000 platform plus $0.06 / $0.055 / $0.045.

**Sep 18, deck review (not yet applied):** arithmetic verified; alignment fixes pending (Deals/Palco/palco-proposal-review-2026-09-18.md).

---

## 9. HOW TO PRESENT: BUSINESS CASE FIRST, THEN THE PROPOSAL

Skip the ten "¿Por qué Yuno?" slides. Say it out loud: "La plataforma ya la vieron con Carlos; si quieren, volvemos ahí al final." Patricio will thank you.

### Step 1. The four levers (slide 13), optimistic headline, one reason each

Open with their data, not ours: "Un dato de su tabla: Mercado Pago les aprueba 92% en wallet y 68% en tarjeta, mismo proveedor. Redsys en España, 88% con el mismo checkout. Openpay, Banorte y Santander, entre 56% y 60%. No es el país ni el producto: es la ruta."

Then the levers, optimistic case, one line of why under each:

| Lever | Optimistic headline | The one reason to say |
|---|---|---|
| 1. Card approval | **$9.3M a year** (62.4% → 72.4% on the main cohort) | Seven processors at 56% to 68% carry 56% of their transactions, about 210,000 attempts a month. Selective 3DS, retry on another route and tokenization close that gap. +10 points is 20,980 more approved transactions a month at $37.09 |
| 2. Failover on broken routes | **$0.86M a year** (47.6% → 68%) | Fiserv approves 43.7% and Pixel Pay 52.3%, about 9,500 attempts a month. Monitors move that traffic to an alternate route instead of losing it. Line VE at 8.7% is left out on purpose: not a routing problem |
| 3. Processing cost | **$99K a year** (12.5 bps) | Route to the cheapest acquirer at equal approval; calibrated with the MDR they share. Say plainly it is the smallest lever |
| 4. Run-ops | **$360K a year** (4 FTE) | One integration frees the team from maintaining 50+ integrations; sub-accounts replace manual onboarding per tenant. The only lever that lands in Palco's own P&L |

Say the total once: "Escenario optimista, $10.7M al año. Conservador, $5.5M." Then move on; do not read assumptions.

⚠️ Correction to carry: lever 2 is $0.86M, eight hundred sixty thousand, not $86M.

### Step 2. The scenarios (slide 14): what is behind the numbers

- **The base:** "Todo está sobre dos números que ustedes reportaron: 235,000 transacciones al mes y un ticket de $37.09. Nada más." (Never say "Palco procesa $104.6M"; say "base de modelación.")
- **The cohort:** "La palanca 1 no es toda su tarjeta; es solo la cohorte que hoy aprueba entre 56% y 68%: Mercado Pago tarjeta, Openpay, Banorte, Santander, Cybersource, Stripe y Bancard."
- **The anchors:** "El conservador, 67.4%, es lo que Mercado Pago ya les da hoy en tarjeta. El optimista, 72%, es el mercado mexicano en crédito. No inventamos un número; pedimos llegar a lo que ya existe."
- **Who captures what:** "$7.7M de GTV recuperado en el punto medio llega a sus clientes, porque son merchant of record. Palco captura su fee sobre eso: cada punto de fee son $77K al año. Lo que cae directo en Palco es la palanca 4, $230K a $360K."
- **Value against cost, said by you first:** "Contra un costo anual de Yuno de $281K: el GTV recuperado es entre 18 y 36 veces ese costo, y el ahorro operativo solo cubre entre 82% y 128%."
- Trial close: "¿Este es el tamaño de problema que tenían en la cabeza?" If Patricio answers "más" or "menos," he is negotiating the case, not the decision.

### Step 3. The proposal (slide 16): structure, number, translation, pilot

- **Structure before number:** "Dos componentes: $7,000 fijos al mes y una tarifa por transacción aprobada que empieza en 6 centavos y baja a 4.5 con volumen. Solo aprobadas, sin setup, subcuentas por cliente incluidas, un solo contrato y una sola factura a Palco; los tramos se calculan sobre el volumen agregado de todos sus clientes."
- **The number:** "A su volumen: $19,000 al mes en pagos, $23,400 si sumamos 3DS selectivo y antifraude." Then silence. Let Alfonso speak.
- **The translation:** "Son 10 centavos por transacción, 27 puntos básicos sobre un ticket de $37. Contra 8% a 16% más ventas aprobadas para el tenant. Por cada dólar que Palco nos paga, sus clientes recuperan entre 18 y 36."
- **Trial close to Alfonso:** "¿Con esta estructura, cómo lo empaquetarían a sus clientes?" He becomes co-designer of the product instead of auditor of the cost.
- **The pilot, instead of a term:** "Por eso no traigo un contrato a tres años. Traigo un piloto: 3 a 5 tenants en México sobre Openpay, Banorte y Santander, subcuentas y SDK, baseline su tabla de agosto, revisión a 90 días. Fernando ya tiene el sandbox; Carlos hace el onboarding la semana del 28."
- **Close with questions, not a summary:** "¿Qué tenants pondrían en el piloto?" then "¿Quién firma el piloto de su lado, tú o Miguel?" Then dates: tenant list by Wednesday, kickoff week of Sep 28, 90-day review on the calendar.

### Selling rules for this account

- Never "les falta orquestador." They call their layer "nuestro orquestamiento de pagos." The line is "you built the hard part; we keep it alive and add the decision layer."
- Never $457M, never the derived $163 ticket. Everything on 235,000 and $37.09.
- Never guarantee an uplift. The pilot with their baseline is the proof.
- Do not read the assumptions or the processor table; offer them to Fernando by email.
- The three ⚠ items are stated with a date, not promised.
- GoFundMe marketplace reference only in generic terms unless permission is obtained.
- Do not compare Mexico to Spain as a target; use Mexico's own benchmark and their own best Mexican rail.
- Proof points you can use: inDrive (11 countries in 8 months, 90% approval, per the deck), Rappi (zero implementation time for new providers), Livelo (+5% approval, 50% recovery). Yuno published figures if needed: 7% authorization uplift, 30% recovered revenue.

---

## 10. BE READY FOR

| They say | Your answer |
|---|---|
| "Dijiste 15K" (Alfonso) | "El fijo bajó a $7,000. Lo demás crece solo si procesan más. En el primer tramo el mes completo son $10,500." |
| "El coste se traslada al cliente final y eligen por precio" | "Tienes razón en que el ruteo de costo solo no paga esto: 7 a 12 puntos básicos contra 27. Lo que lo paga es la aprobación. Un tenant que hoy aprueba 62 y pasa a 67 vende 8% más." |
| "Ya tenemos 50 integraciones" | "Y las siguen teniendo; cuentas y contratos siguen siendo suyos. Ponemos la capa de decisión encima y mantenemos los conectores vivos para que Fernando no construya el siguiente país." |
| "¿Por qué no lo construimos nosotros?" | "Pueden. La pregunta es si quieren que el equipo de Alfonso mantenga 50 conectores y un motor de ruteo, o construya producto de ticketing. Esto está en producción hoy; el piloto arranca en semanas." |
| "¿Garantizan el uplift?" | "No, y desconfiaría de quien lo haga. Por eso el piloto tiene baseline con sus números y revisión a 90 días." |
| "¿Y el split y la recurrencia en México?" | "Yuno propaga el split al procesador que lo soporta; cuáles mexicanos lo hacen en su dirección lo confirma Carlos el [fecha]. Prefiero eso a prometerles algo hoy." |
| "El 3DS nos mata la aprobación" | "Por eso lo modelamos selectivo: condición de ruteo, exenciones por riesgo, reintento por otra ruta. ¿El 3DS al 100% se lo exige el adquirente, el tenant, o es decisión de Palco?" |
| "¿Cobran por transacción o por volumen de dinero?" | "Por transacción aprobada, nunca sobre el monto." (If the ticket question is resolved and the order is ~$120, add: "sobre la orden real son unos 8 puntos básicos.") |
| "¿Y si la cuenta es de Palco y no del cliente?" | "El precio es el mismo. Cubre el caso de recintos grandes y clubes con comercio propio de Palco." (Confirm internally before Monday.) |
| "Bájame el precio" (Patricio) | Not on the table. "Lo que puedo hacer es reducir el fee de plataforma durante el piloto si salimos hoy con los tenants y la fecha." |
| "¿Tienen un caso de marketplace con split?" | Generic only: "Tenemos un marketplace en producción con split, sellers y transfers sobre tres procesadores." No name without permission. |
| "¿Cuánto tarda la integración?" | "Con SDK y subcuentas, semanas, no meses; Carlos pone la fecha con Fernando en el kickoff." Do not say 4 to 6 weeks unless Carlos confirmed it. |
| "¿Qué pasa con PCI si vamos por API?" | "Si el PAN pasa por su front, el alcance PCI es de Palco. Con SDK no lo necesitan; por eso Alfonso dijo 90% SDK." |

---

## 11. AGENDA (30 minutes as the calendar stands; 45-minute variant in brackets)

| Time | Block | Who | Notes |
|---|---|---|---|
| 0 to 2 | Open: thank the data, three things to answer today, skip the platform tour | German | Notes: ____ |
| 2 to 5 | "Lo que nos pidieron y cómo lo cubrimos": six answered, three pending with a date | German | Notes: ____ |
| 5 to 12 | Four levers, optimistic headline, one reason each; total once | German | Notes: ____ |
| 12 to 16 | Scenarios: base, cohort, anchors, who captures what, value vs cost; trial close | German | Notes: ____ |
| 16 to 24 | Proposal: structure, number, silence, translation, pilot | German (Joaquin on Mexico and pre-sales if raised) | Notes: ____ |
| 24 to 28 | Objections (Section 10) | German, Joaquin | Notes: ____ |
| 28 to 30 | Close: which tenants, who signs, dates | German | Notes: ____ |
| [30 to 42] | [Extended discussion: 3DS ownership, split direction, packaging to tenants] | | Notes: ____ |
| [42 to 45] | [Close as above] | | Notes: ____ |

---

## 12. DISCOVERY QUESTIONS

Only what emails and calls have not answered.

1. "¿El ticket de $37.09 es por boleto o por transacción? Su tabla mensual da unos $120 por transacción." (If not answered by Fernando before Monday.) Notes: ____
2. "¿Las 235,000 transacciones al mes son aprobadas o intentos, y cuántas son tarjeta?" Notes: ____
3. "¿El 3DS en todos los flujos se lo exige el adquirente, el tenant, o es decisión de Palco?" Notes: ____
4. "¿Qué tenants pondrían en el piloto de México, y cuáles procesan con Openpay, Banorte o Santander?" Notes: ____
5. "¿Quién firma el piloto de su lado?" Notes: ____
6. "¿Cómo lo empaquetarían a sus clientes: absorbido en su fee por ticket, o como un cargo aparte?" Notes: ____
7. "¿Qué mercado procesa Fiserv?" (only if lever 2 is challenged) Notes: ____
8. "¿Cuál es su atestación PCI actual?" (only if direct API comes up) Notes: ____

---

## 13. POST-MEETING CHECKLIST

- Same day: recap email to Patricio, Alfonso, Fernando (cc Miguel if he attended, Joaquin, Carlos) with the deck PDF, the pilot in five lines (scope, baseline, KPI, dates, commercial condition), the three confirmations with dates, and the ticket question if unresolved. Ask for the tenant list by Wednesday.
- Log outcome, tenants named, signer, and any new numbers in Deals/Palco and memory.
- Put the kickoff (week of Sep 28) and the 90-day review on the calendar; add Carlos.
- Update the pricing calculator if the ticket or the 235,000 basis changes.
- Update memory: project_palco_ticketing.

---

## Appendix: sources

- Gmail thread "Palco + Yuno - Próximos Pasos" (id 1a06e21d4b5dc7d3), Jul 31 to Sep 16, incl. Patricio's data email of Sep 2.
- Google Calendar: "Yuno / PALCO - Demo & Payment Orchestration Review" (Sep 9), "Palco + Yuno | Deep Dive" (Sep 15), "Propuesta PALCO" internal (Sep 16, Gemini notes 1kFP-AtgqXnMvOfzMQc8LYb8plDM_5vSwVZYnvksNGd8), "Palco + Yuno | Propuesta" (Sep 21).
- Gong call 891469394762814345 (Sep 15). Transcript: Deals/Palco/palco-call-transcript-2026-09-15.md.
- Deals/Palco/palco-deal-summary-2026-09-16.md; palco-proposal-2026-09-16.md; palco-deck-qa-2026-09-16.md; palco-proposal-review-2026-09-18.md; palco-proposal-meeting-plan-2026-09-21.md.
- Prior briefs: data/research/palco-meeting-brief-2026-09-09.md and palco-meeting-brief-2026-09-15.md (company, competitors, benchmark sources).
- Pricing: "Yuno — Palco Pricing Calculator" (1Shux23cA23PBCcAlyhAiNrzXgzU6lbtQsLxUHgQ5NH8).
- Deck: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit
- Miguel Ramírez Lombana: https://www.linkedin.com/in/miguel-ram%C3%ADrez-lombana-10886/ ; https://www.crunchbase.com/person/miguel-ram%C3%ADrez-lombana ; https://theorg.com/org/tikitaka/org-chart/miguel-ramirez-lombana
- Alfonso Uribarri: https://es.linkedin.com/in/alfonso-uribarri-carrasco-82a60784/en · Fernando Nava: https://mx.linkedin.com/in/fernando-nava-feldman · Patricio Villalobos: https://www.linkedin.com/in/patricio-villalobos-cuevas-9873a025/
- Acquisition: https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/ ; https://techla.pro/2025/10/31/22111/ ; https://pitchbook.com/profiles/company/551549-35 ; https://www.crunchbase.com/organization/palco-ticketing
- Mexico approval benchmark: RankingsLatAm, Sep 2024 (via Sep 9 brief).
