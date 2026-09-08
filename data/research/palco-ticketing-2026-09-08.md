# SDR Research Brief: Palco (formerly Palco4, "Palco Ticketing")
*Framework v8.0 | Date: 2026-09-08 | Analyst: Yuno payments intelligence*

**Entity researched (confirmed, HIGH confidence):** Palco, formerly **Palco4**, rebranded to "Palco Ticketing" at **pal.co** (verified live redirect chain palco4.com → palcoticketing.com → pal.co; LinkedIn company page renamed). Legal name: **PALCO4 TECNOLOGIA Y SERVICIOS SL**, CIF B87730628, Registro Mercantil de Madrid, HQ Calle Copenhague 4, Las Rozas de Madrid, Spain. Not to be confused with Grupo Palco SAS (Bogotá consulting, unrelated), Palco MP3 (Brazilian music site) or Palco23 (Spanish sports media).

---

## EXECUTIVE SUMMARY

Palco is a Spanish B2B **white-label ticketing platform** (500+ venues, 30 countries, 8M+ tickets/year) that powers promoter and venue owned ticket stores across Spain and Latin America, with marquee 2025 on-sales for Bad Bunny (DR), Tini (AR), Don Omar (MX) and Shakira (UY). The key payments finding: **Palco built and maintains its own quasi-orchestration layer with 50+ native payment gateway integrations across 18 markets** (Adyen, Stripe, Mercado Pago, Openpay, GETNET, Redsys, VisaNet/Niubiz, Datafast, Yappy, etc.), sells it as a core feature, and settles funds directly to each promoter's account. In Oct/Nov 2025 the company was **acquired by Bocel Private Equity together with Mexican entrepreneurs Patricio Villalobos and Miguel Ramírez Lombana**, with a stated plan to enter additional LatAm markets by mid-2026, meaning more local connectors to build and maintain per market. The Yuno opportunity is an **infrastructure/embed play**: one Yuno integration replaces a 50+ connector factory, adds smart routing, monitoring and instant market launches for every venue on the platform (the only public product review literally asks for "more payment methods").

---

## SECTION 1: Traffic by Country

Caveat: Palco is white-label B2B. Consumer ticket volume runs on client-branded storefronts (e.g., pr-usa.palco4.com/prtickets, boletos.fullpass-ticket.com), so corporate-domain traffic massively understates processed volume. [INFERENCE, not confirmed]

**palco4.com** (legacy domain, still hosts client stores):

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|---|---|---|---|---|---|
| 1 | Dominican Republic | 33.25% | part of 7.8K visits/3mo | +257.8% MoM | https://www.similarweb.com/website/palco4.com/ |
| 2 | Argentina | 27.57% | " | " | https://www.similarweb.com/website/palco4.com/ |
| 3 | Spain | 14.85% | " | " | https://www.similarweb.com/website/palco4.com/ |
| 4 | Mexico | 11.41% | " | " | https://www.similarweb.com/website/palco4.com/ |
| 5 | Puerto Rico | 7.99% | " | " | https://www.similarweb.com/website/palco4.com/ |

**pal.co** (new brand domain, Aug 2026): Brazil 59.59%, United States 25.1%, Spain 15.31% (https://www.similarweb.com/website/pal.co/).

Flags: 100% of measurable traffic is LATAM + Spain. DR, Argentina, Mexico and Puerto Rico all >5%. Company claims operations in 30 countries; only one legal entity found (Spain), see Section 2.

---

## SECTION 2: Legal Entities

| Country | In Top Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| Spain | Yes (#3) | Yes: PALCO4 TECNOLOGIA Y SERVICIOS SL, CIF B87730628, Las Rozas de Madrid | No | https://www.iberinform.es/empresa/7298047/palco4-tecnologia-y-servicios |
| Mexico | Yes (#4) | Not found | ⚠️ Potential cross-border operation, no local entity found | https://es.linkedin.com/company/palco4 (no other offices listed) |
| Dominican Republic | Yes (#1) | Not found | ⚠️ Potential cross-border operation, no local entity found | https://es.pal.co/es/home (footer names no entity) |
| Argentina | Yes (#2) | Not found | ⚠️ Potential cross-border operation, no local entity found | https://es.pal.co/privacy-policy (no entity named) |
| Puerto Rico | Yes (#5) | Not found | ⚠️ Potential cross-border operation, no local entity found | N/A |

Mitigating context: Palco markets "hassle-free payments directly to your account" (Capterra), i.e., **the venue/promoter is merchant of record and settles locally through its own gateway contracts**, so Palco itself may not need local entities. [INFERENCE, not confirmed] OpenCorporates was CAPTCHA-blocked this session.

> ⚠️ MANUAL: Verify entity structure on official T&Cs and post-acquisition filings (new Mexican ownership may create a Mexican entity).

---

## SECTION 3: Payment Stack

### 3A. PSPs & Acquirers (official per-country integration map, published on Palco's own site)

Evidence type for all rows: [Partner Page], extracted from live HTML of https://es.pal.co/es/home on 2026-09-08. Several countries show "+ Ver N más" (additional hidden connectors).

| Country/Region | PSP / Acquirer / Gateway | Source URL |
|---|---|---|
| Mexico | Adyen, Aplazo (installments), Mercado Pago (Point pinpad, card, tienda/cash), Pagando Check, Santander GETNET, Openpay (card + tienda), Stripe, Banorte, PayPal (+9 more) | https://es.pal.co/es/home |
| Colombia | Adyen, Mercado Pago (Point, card, convenience store, PSE), Openpay (card + tienda) (+5 more) | https://es.pal.co/es/home |
| Peru | Adyen, Mercado Pago, Openpay (tienda), VisaNet incl. payment button, Stripe, PayPal (+5 more) | https://es.pal.co/es/home |
| Chile | Mercado Pago, PayPal, Travelpay (Transbank) | https://es.pal.co/es/home |
| Brazil | Mercado Pago, Stripe, PayPal | https://es.pal.co/es/home |
| Bolivia | RedEnlace (card + QR) | https://es.pal.co/es/home |
| Ecuador | Datafast, DeUna!, PayPal | https://es.pal.co/es/home |
| Dominican Republic | UEPA Pay, PayPal | https://es.pal.co/es/home |
| El Salvador | Powertranz, Serfinsa, PayPal | https://es.pal.co/es/home |
| Guatemala | Cybersource, Recurrente, PayPal | https://es.pal.co/es/home |
| Honduras | Cybersource, PayPal | https://es.pal.co/es/home |
| Costa Rica | Cybersource, Stripe, PayPal | https://es.pal.co/es/home |
| Panama | Yappy, Authorize.net, Powertranz | https://es.pal.co/es/home |
| Paraguay | Bancard (card + QR), PayPal | https://es.pal.co/es/home |
| Uruguay | Fiserv, Mercado Pago (Point, card), Stripe, PayPal (+2 more) | https://es.pal.co/es/home |
| Spain / Europe | Redsys (pinpad + card), Adyen, ECI TPV (El Corte Inglés), Stripe, PayPal (+3 more); Bizum and SEPA marketed | https://es.pal.co/es/home |
| USA | Adyen, Authorize.net, Stripe, PayPal | https://es.pal.co/es/home |
| Puerto Rico | Authorize.net, PayPal | https://es.pal.co/es/home |

Headline claims on the same page: "+50 pasarelas de pago", "integraciones nativas con más de 50 pasarelas de pago en Latinoamérica y España... nuestra arquitectura permite integrar nuevas pasarelas cuando el proyecto lo requiere."

### 3B. Orchestrator

**No public evidence of a third-party orchestrator.** Dedicated searches for Spreedly, Primer, Gr4vy, CellPoint and APEXX returned nothing (the "Primer" hits on their site are the Spanish word "primer nivel"). All evidence points to a **home-built orchestration layer** maintained in-house; the platform exposes a server-side per-tenant payment config interface (`PaymentsAjax.getCompanyPaymentMethod` observed in live store HTML: https://pr-usa.palco4.com/prtickets/es/listaEventos). [INFERENCE, not confirmed: in-house build]

> ⚠️ MANUAL, DevTools on a live client checkout: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4: APMs (Agent D findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| Mexico | OXXO (cash), SPEI, meses sin intereses (Aplazo + MSI), local cards, Mercado Pago | Official site payment map + marketing copy | https://es.pal.co/es/home |
| Argentina | Mercado Pago, Rapipago, PagoFácil, bank transfers | Official site marketing copy | https://es.pal.co/es/home |
| Colombia | PSE (via Mercado Pago), convenience-store cash, cards | Official site payment map | https://es.pal.co/es/home |
| Spain | Bizum, SEPA, cards via Redsys | Official site payment map | https://es.pal.co/es/home |
| Ecuador | DeUna!, PayPal, cards via Datafast | Official site payment map | https://es.pal.co/es/home |
| Panama | Yappy | Official site payment map | https://es.pal.co/es/home |
| Bolivia / Paraguay | QR payments (RedEnlace / Bancard) | Official site payment map | https://es.pal.co/es/home |
| Platform-wide | Installments ("Configuración del Pago a Plazos"), per-method service charges, PinPad in-person card | Official help center (Palco Academy) | https://academy.palco4.net/ |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (context only) |
|---|---|---|---|
| Mexico (live store: FunTicket) | Yes | JS shell page, checkout not renderable without session | OXXO, SPEI, MSI |
| Puerto Rico (live store: PRticket) | Yes | Payment buttons render only inside a live reservation; FAQ payment section is JS-loaded | ATH Móvil |
| Ecuador (live store: Fullpass) | Yes | HTTP 403 on fetch | DeUna!, Payphone |
| en.pal.co (English site) | Yes | HTTP 403 (Spanish site fetched instead) | N/A |

> "Not verified" ≠ "not available." Per-client store payment mixes are tenant-configured server-side. MANUAL: VPN checkout walk-through on 2-3 live client stores before any APM claims in conversation.

---

## SECTION 5: Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Product gap: reviewer wants "más métodos de pago" (more payment method options) | Capterra (B2B review, 4.0/5, incentivized) | 1 review (the only one) | Mar 2023 | https://www.capterra.com/p/200482/Palco4/ |
| Consumer complaints under Palco brand | Trustpilot / Reddit / Profeco | None found; no Trustpilot profile exists (404) | N/A | https://www.trustpilot.com/review/palco4.com |

Analysis: as a white-label platform, consumer payment complaints surface under client brands (PRtickets, Fullpass, etc.), not Palco's, so absence of complaints is structural, not proof of clean payments. The one existing product review asking for **more payment methods** maps directly to Yuno's catalog (1,000+ methods through one integration). Industry context: 5,652 ticket-market complaints in Mexico 2022-2024 per Profeco (Palco not named): https://verificado.com.mx/estafas-en-conciertos-compra-boletos/

---

## SECTION 6: Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | Oct 31 / Nov 2025 | **Acquired by Mexican entrepreneurs Patricio Villalobos Cuevas + Miguel Ramírez Lombana with Bocel Private Equity** (Roberto Terrazas, René Fernández). Press reports Bocel took a majority stake; Preqin classifies it as a minority/buyout deal. Amount undisclosed. | M&A / ownership | https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/ ; https://techla.pro/2025/10/31/22111/ ; https://www.preqin.com/data/profile/asset/palco/776852 |
| 2 | 2025-2026 | Rebrand Palco4 → Palco / Palco Ticketing (pal.co), LinkedIn page renamed | Brand | Live redirect chain palco4.com → palcoticketing.com → pal.co |
| 3 | Post-deal | Stated strategy: accelerate international expansion, strengthen LatAm + Spain leadership, **enter additional LatAm markets by mid-2026**, dynamic pricing, upgrades, omnichannel, data/personalization | Expansion | https://www.preqin.com/data/profile/asset/palco/776852 ; https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/ |
| 4 | 2025 | Marquee on-sales (vendor claims): Bad Bunny DTMF Tour DR (3 sellouts in 8h), Tini Futttura AR (200K+ tickets in 18h), Don Omar MX (200K+ in 24h), Shakira UY (86K in 48h); testimonials from ATP Chile Open and FIBA World Cup accreditation | Client wins | https://en.pal.co/en/home |
| 5 | 2023 → 2026 | Headcount 15 (2023, Spanish registry) → 42-47 (2026, Tracxn/LinkedIn), roughly 3x | Hiring | https://www.einforma.com/informacion-empresa/palco4-tecnologia-servicios ; https://tracxn.com/d/companies/palco4/__3EL-njJanf8X9S1gb-Axu7-Iei34VOWsC8_n2Xt20PY |
| 6 | N/A | Leadership hires (CTO/CFO/VP Payments), payment job postings, public RFPs: no public information found | N/A | N/A |

Founding-year discrepancy reported as-is: 2014 (Tracxn/LinkedIn), May 2015 (founder interview), 2017 (acquisition coverage). Founders: Vicente Vara (CEO), Juan José Delgado, Carlos Lara, Alfonso Uribarri (https://www.starterstory.com/stories/how-we-started-a-1m-event-ticketing-platform-from-spain).

---

## SECTION 7: Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | Nov 2025 | 🟢 Bocel PE + Mexican investors acquire Palco; expansion capital for LatAm | New markets = new local gateway integrations to build in-house | https://www.preqin.com/data/profile/asset/palco/776852 |
| 2 | 2026 (ongoing) | 🟢 Palco publicly markets "+50 pasarelas de pago" with per-country integration map incl. Adyen, Stripe, Mercado Pago, Openpay, GETNET | Confirms home-built multi-gateway layer; payments is a headline feature of their pitch | https://es.pal.co/es/home |
| 3 | N/A | 🔴 PSP removals/breakups: none found | N/A | N/A |

No public information found on dedicated payment partnerships announced via press release in the last 12 months.

---

## SECTION 8: Checkout Audit

Live store inspected: PRticket (Puerto Rico), https://pr-usa.palco4.com/prtickets/es/listaEventos and event page https://pr-usa.palco4.com/prtickets/es/nochesdeimpro (2026-09-08).

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Embedded white-label, 3 steps on same domain: "1 Compra → 2 Pago → 3 Confirmación", reservation countdown timer | Good | Runs on palco4.com subdomains or fully custom client domains |
| Guest checkout | Not verified | N/A | Login/Registro prominent; a form named "formRegisteredToPurchaseFlow" wires registration into purchase; no claim either way |
| Steps to purchase | 3 (selection → payment → confirmation), manual or auto "best seats" | Good | Discount codes, memberships, vouchers, upsells, ticket transfer, season passes, ID capture |
| 3DS | Not verified | N/A | Payment step not reachable without live reservation |
| Mobile experience | Responsive web (viewport meta tags); GA4/GTM/Meta Pixel present | Not fully assessed | N/A |
| APM display logic | Server-configured per tenant (`PaymentsAjax.getCompanyPaymentMethod`); methods vary by country per official map; multi-currency selector (USD, CLP, EUR, GBP, HKD, IDR, JPY, MXN), ES/EN | Good | Installments in MX via Aplazo integration |

> ⚠️ MANUAL: Walk a full checkout in Mexico and one more market (DR or PR) with a small real purchase.

---

## SECTION 9: PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| No public information found | Not published; no PCI mention on pal.co, privacy policy, archived palco4.com or archived T&Cs. [INFERENCE, not confirmed: likely gateway-hosted/tokenized flows via the 50+ connectors] | Yuno full API + vault: offload PCI scope, network tokens, one certification story to sell to their venues | https://es.pal.co/es/home ; https://web.archive.org/web/20201101032600/https://palco4.com/2020/10/29/seguridad-es-tranquilidad/ |

---

## SECTION 10: Strategic Insights

**Insight #1: Palco IS its own orchestrator, and that is the opportunity, not the objection.**
Evidence: S3A (50+ native gateway integrations across 18 markets, self-maintained, marketed as a feature) | Pain Point: a ~45-person company is maintaining a connector factory (versioning, certifications, gateway API changes, per-market quirks) that companies 100x their size struggle with | Yuno Value Prop: embed Yuno as the payments infrastructure under the platform; one integration keeps their entire per-country map alive, plus every rail they have not built yet | Best Case: InDrive (10 LATAM markets live in under 8 months, 90% approval) | Outreach Angle: "You built 50+ gateway integrations in-house. What does connector maintenance cost you per new market, and what if one API kept all of them current?"

**Insight #2: PE money + "new LatAm markets by mid-2026" = a connector-building race Yuno can shortcut.**
Evidence: S6 (Bocel deal, stated expansion timeline) | Pain Point: every new market means sourcing, contracting and integrating new local gateways before selling a single ticket | Yuno Value Prop: new market live in weeks, no-code PSP enablement on an already-integrated catalog | Best Case: InDrive multi-market rollout | Outreach Angle: expansion timeline pressure, "mid-2026 is two quarters away."

**Insight #3: Their only public product review asks for more payment methods.**
Evidence: S5 (Capterra, Mar 2023: cons = "más métodos de pago") | Pain Point: venues/promoters feel APM gaps; each request lands on Palco's own roadmap | Yuno Value Prop: 1,000+ payment methods through the single existing integration; per-tenant method enablement | Best Case: Livelo (+5% approval, 50% recovery) | Outreach Angle: turn their clients' feature requests into a switch they flip, not a project they scope.

**Insight #4: High-stakes on-sales are an approval-rate and monitoring story.**
Evidence: S6 (200K+ tickets in 18-24h for Tini and Don Omar; 15,000+ requests/second platform claim per Preqin) | Pain Point: during a stampede on-sale, every failed or falsely declined payment is a lost seat and an angry fan on the client's brand; a gateway degradation mid-on-sale is catastrophic | Yuno Value Prop: smart routing (+7% approval uplift), automatic failover between the gateways they already use, real-time monitors (Rappi: millisecond detection vs 5-10 min manual) | Best Case: Rappi (zero implementation time, 80% less analyst resolution time) | Outreach Angle: "What happens to the Bad Bunny on-sale if your MX gateway degrades at minute 4?"

**Insight #5: Mexican ownership shifts the decision center to Mexico.**
Evidence: S6 (Villalobos + Ramírez, Bocel PE, Mexico) and S1 (MX top-4 traffic; largest connector roster is Mexico's) | Pain Point: new owners will scrutinize unit economics and engineering spend; payments infra is a visible cost line | Yuno Value Prop: LatAm-native orchestrator with Mexico depth (OXXO, SPEI, MSI already in catalog) and local team | Best Case: Rappi (LatAm reference at scale) | Outreach Angle: reach the new Mexican leadership in Spanish with a LatAm-native infrastructure story.

---

## SECTION 11: Pipeline

### 11A. Direct Competitors (white-label / venue-controlled ticketing tech)

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| vivenu | vivenu.com | Not stated on site | 1,000+ organizers, 50+ countries | US, Europe | https://vivenu.com/ |
| SecuTix (ELCA Group) | secutix.com | Pully, Switzerland | 204 live customer sites, 75M tickets/yr | Europe | https://www.secutix.com/ |
| Tixly | tixly.com | Nordic focus (HQ not stated on site) | Performing-arts venues, Northern Europe | Europe | https://tixly.com/ |
| AudienceView, Paylogic, Seat Unique, Tickitto, SquadUP, Ticketleap, ACME Technologies | N/A | N/A | Listed as Palco4 top competitors (Palco4 ranked 57 of 606) | Global | https://tracxn.com/d/companies/palco4/__3EL-njJanf8X9S1gb-Axu7-Iei34VOWsC8_n2Xt20PY |

### 11B. Industry Peers (B2C ticketers competing for the same venues/promoters)

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Ticketmaster México (OCESA / Grupo CIE) | ticketmaster.com.mx | Ticketing | Mexico, Brazil | Dominant incumbent in Palco's #1 growth market | https://en.wikipedia.org/wiki/Grupo_CIE |
| Superboletos | superboletos.com | Ticketing | Mexico | Promoter-aligned MX ticketer | https://www.superboletos.com/ |
| eTicket | eticket.mx | Ticketing | Mexico | Concerts/sports/theater + POS network | https://www.eticket.mx/ |
| TuBoleta | tuboleta.com | Ticketing | Colombia | Colombia leader (Movistar Arena, DAVIarena) | https://www.tuboleta.com/ |
| PuntoTicket | puntoticket.com | Ticketing | Chile | Official ticketer for major Chilean venues | https://www.puntoticket.com/ |
| Joinnus | joinnus.com | Ticketing | Peru | Peru events platform | https://www.joinnus.com/ |
| Wegow | wegow.com | Ticketing/discovery | Spain, Mexico, US, Europe | Spain+MX overlap | https://www.wegow.com/ |
| Boletia | boletia.com | Ticketing | Mexico | Self-serve MX ticketing | https://www.cbinsights.com/company/boletia/alternatives-competitors |

### 11C. Adopting Orchestration

No ticketing-vertical company was found publicly using a third-party payment orchestrator this session. SecuTix runs its own in-house payment product (S-PAY, https://www.secutix.com/); Palco aggregates 50+ gateways in-house. The orchestration layer in this vertical is being home-built, which makes it greenfield for Yuno. Adjacent signal: experiences platform Peek acquired ticketing provider ACME Ticketing in Nov 2025 (https://www.prnewswire.com/news-releases/peek-acquires-acme-ticketing-and-connectgo-raises-70m-to-double-down-on-ai-for-the-travel-and-experiences-industry-302621253.html), consolidation pressure on independents.

### 11D. Scoring (Palco, verified only)

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ 30 countries, 500+ venues (LevelUp/Techla/Capterra) |
| Multiple PSPs | +3 | ✅ 50+ gateways, per-country map on pal.co |
| Recent expansion (24 mo.) | +2 | ✅ Bocel acquisition + mid-2026 LatAm expansion plan |
| Public payment issues | +2 | ❌ None under own brand (structural, white-label) |
| Funding >$10M | +2 | ❌ Deal value undisclosed; pre-deal unfunded/bootstrapped |
| LATAM/APAC/MENA traffic | +2 | ✅ DR, AR, MX, PR, BR dominate traffic |
| No orchestrator | +2 | ✅ No public evidence of third party; home-built layer |
| Payment job postings | +1 | ❌ None found |
| Public RFP | +3 | ❌ None found |

**Total: 12 → 🔴 HIGH priority.**

**Top 10 Pipeline** (scores directional, from verified attributes only):

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | Palco (target) | White-label ticketing platform | MX, ES, DR, AR, PR + 25 more | 12 | 🔴 | 50+ self-built gateway integrations + PE-funded expansion |
| 2 | vivenu | White-label ticketing | 50+ countries | ~10 | 🟡 | Multi-country enterprise white-label, no orchestrator flagged |
| 3 | SecuTix | Ticketing tech | Europe | ~8 | 🟡 | 75M tickets/yr, but in-house S-PAY (displacement sale) |
| 4 | Ticketmaster México / OCESA | Ticketer/promoter | MX, BR | ~8 | 🟡 | Massive MX volume, Live Nation-owned (hard access) |
| 5 | TuBoleta | Ticketer | CO | ~7 | 🟡 | Colombia leader, LatAm rails |
| 6 | PuntoTicket | Ticketer | CL | ~7 | 🟡 | Major-venue exclusives in Chile |
| 7 | eTicket | Ticketer | MX | ~7 | 🟡 | Online + physical POS mix |
| 8 | Superboletos | Ticketer | MX | ~7 | 🟡 | Promoter-aligned, MX APM needs |
| 9 | Wegow | Ticketing/discovery | ES, MX, US, EU | ~7 | 🟡 | Spain+Mexico cross-border footprint |
| 10 | Joinnus | Ticketer | PE | ~6 | 🟢 | Peru single-market |

Pipeline Summary: 11 companies surfaced, 1 high-priority (the target). Strongest vertical: white-label ticketing infrastructure in LatAm + Spain, where payments orchestration is universally home-built.

---

## SECTION 12: Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| €750K-1.5M band (Spanish registry, SaaS fees only, +6.46% YoY); founder-stated ~$1.2M/yr in 2019 | Not found (ticket face values vary by event) | 8M+ tickets/yr (registry listing); 4M/yr founder-stated in 2019; 50M+ lifetime | EUR (corporate), MXN/DOP/ARS/USD at store level | Mexico, Spain, Dominican Republic/Argentina |

[INFERENCE, not confirmed] 8M tickets against the €0.75-1.5M revenue band implies a platform fee around €0.10-0.19 per ticket. The payments opportunity is not Palco's own revenue but the **GMV flowing through its 500+ venues**: at 8M+ tickets/yr, even modest per-ticket values put platform GMV in the hundreds of millions. Business-case lever for Yuno: approval uplift and recovery on that GMV benefits every venue, and Yuno pricing ($50K processed free, then $0.05 per transaction) maps cleanly onto their per-ticket fee model.

Sources: https://www.einforma.com/informacion-empresa/palco4-tecnologia-servicios ; https://empresite.eleconomista.es/PALCO4-TECNOLOGIA-SERVICIOS.html ; https://www.starterstory.com/stories/how-we-started-a-1m-event-ticketing-platform-from-spain

---

## SECTION 13: Outreach (verified findings only)

Best-known contacts: CEO/co-founder Vicente Vara; new owners Patricio Villalobos Cuevas and Miguel Ramírez Lombana (Mexico). No VP Payments identified.

```
--- LINKEDIN MESSAGE ---

Hola [Nombre], vi el anuncio de Bocel y la nueva etapa de Palco. Felicitaciones.

Lo que más me llamó la atención de pal.co: mantienen 50+ integraciones nativas de pasarelas en 18 mercados, construidas in-house. Es exactamente el tipo de infraestructura que en Yuno operamos como producto: una sola API que mantiene vivas todas esas conexiones (Adyen, Stripe, Mercado Pago, Openpay, GETNET y el resto de su mapa), con smart routing y failover automático para on-sales tipo Tini o Don Omar, donde cada decline es un asiento perdido.

InDrive lanzó 10 mercados LatAm con nosotros en menos de 8 meses; Rappi detecta degradaciones de procesador en milisegundos. Si el plan es entrar a nuevos mercados LatAm a mitad de 2026, esa expansión puede ser configuración, no ingeniería.

¿Les hace sentido una llamada de 25 minutos el martes o jueves próximo?

--- COLD EMAIL ---

Subject: Las 50+ pasarelas de Palco, con un solo equipo de ingeniería

Hola [Nombre],

Vi dos cosas en pal.co que motivan este correo: el mapa de 50+ pasarelas integradas por país, y el plan de entrar a nuevos mercados LatAm a mediados de 2026 tras la entrada de Bocel.

Mantener ese mapa in-house (versiones, certificaciones, cambios de API de cada pasarela, particularidades por mercado) es un costo de ingeniería que crece con cada país nuevo. Y cada venue que pide un método de pago adicional se convierte en un proyecto de roadmap.

Yuno es un sistema operativo de pagos: una sola integración conecta 1,000+ métodos de pago, procesadores y herramientas antifraude en 200+ países, con smart routing que sube la tasa de aprobación ~7%, failover automático entre las pasarelas que ya usan, y monitoreo en tiempo real, crítico cuando venden 200,000 boletos en 18 horas y un procesador se degrada en el minuto cuatro.

Para Palco significa: nuevos mercados en semanas en lugar de trimestres, y métodos de pago nuevos como configuración por tenant, no como desarrollo.

¿Tienen 25 minutos el martes o el jueves de la próxima semana? Puedo mostrar cómo se vería su mapa actual de pasarelas operando sobre una sola API.

Saludos,
German Tatis
Yuno
```

---

## APPENDIX: Source URLs

```
[S1] https://www.similarweb.com/website/palco4.com/
[S1] https://www.similarweb.com/website/pal.co/
[S2] https://www.iberinform.es/empresa/7298047/palco4-tecnologia-y-servicios
[S2] https://www.einforma.com/informacion-empresa/palco4-tecnologia-servicios
[S2] https://www.axesor.es/Informes-Empresas/9135019/PALCO4_TECNOLOGIA_Y_SERVICIOS_SL.html
[S2] https://empresite.eleconomista.es/PALCO4-TECNOLOGIA-SERVICIOS.html
[S2] https://es.linkedin.com/company/palco4
[S3/S4] https://es.pal.co/es/home
[S4] https://academy.palco4.net/
[S4] https://pr-usa.palco4.com/prtickets/es/listaEventos
[S4] https://prticket.online/faq
[S4] https://ft-mx.palco4.com/ticketsventafunticket/es/
[S4] https://boletos.fullpass-ticket.com/tickets/es/listaEventos
[S5] https://www.capterra.com/p/200482/Palco4/
[S5] https://www.trustpilot.com/review/palco4.com
[S5] https://verificado.com.mx/estafas-en-conciertos-compra-boletos/
[S6] https://www.levelup.com/noticia/palco-ticketing-inicia-una-nueva-era-tras-ser-adquirida-por-empresarios-mexicanos-y-bocel-private-equity/
[S6] https://techla.pro/2025/10/31/22111/
[S6] https://www.preqin.com/data/profile/asset/palco/776852
[S6] https://pitchbook.com/profiles/company/551549-35
[S6] https://www.iqmagazine.com/2025/11/mexican-private-equity-firm-acquires-ticketing-solution-palco/
[S6] https://www.theticketingbusiness.com/2025/11/mexicos-bocel-private-equity-invests-in-palco-ticketing/
[S6/S12] https://www.starterstory.com/stories/how-we-started-a-1m-event-ticketing-platform-from-spain
[S6/S11] https://tracxn.com/d/companies/palco4/__3EL-njJanf8X9S1gb-Axu7-Iei34VOWsC8_n2Xt20PY
[S9] https://web.archive.org/web/20201101032600/https://palco4.com/2020/10/29/seguridad-es-tranquilidad/
[S11] https://vivenu.com/
[S11] https://www.secutix.com/
[S11] https://tixly.com/
[S11] https://en.wikipedia.org/wiki/Grupo_CIE
[S11] https://www.superboletos.com/
[S11] https://www.eticket.mx/
[S11] https://www.tuboleta.com/
[S11] https://www.puntoticket.com/
[S11] https://www.joinnus.com/
[S11] https://www.wegow.com/
[S11] https://www.cbinsights.com/company/boletia/alternatives-competitors
[S11] https://www.prnewswire.com/news-releases/peek-acquires-acme-ticketing-and-connectgo-raises-70m-to-double-down-on-ai-for-the-travel-and-experiences-industry-302621253.html
```

*Notes: en.pal.co, iqmagazine.com, theticketingbusiness.com, boletia.com and preqin.com blocked direct fetches (403); facts from those domains rest on search-index snippets or the Spanish-site equivalent, flagged in-line. Bocel stake reported as majority by press (LevelUp/Techla) and minority by Preqin; discrepancy reported as-is.*
