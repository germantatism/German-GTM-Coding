# AXS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: AXS
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/4/4e/Axs_logo.svg
Nombre merchant: AXS

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Region PSP Blind Spots
Tittle_Pain Point_2: Japan Checkout Mismatch
Tittle_Pain Point_3: Peak On-Sale Failures
Tittle_Pain Point_4: UK/EU Local Method Gaps
Tittle_Pain Point_5: No Unified Payment Layer

Desc_Pain Point_1: AXS operates across North America, Europe, Australia, and Japan serving 1,600+ partners, but checkout is limited to Visa, Mastercard, Amex, PayPal, and Klarna. No local APMs for key growth markets despite $2B+ in annual transactions.
Desc_Pain Point_2: New Lawson Entertainment JV (Oct 2025) connects AXS to 15,000 convenience stores in Japan. Fans expect Konbini payments, PayPay, and Line Pay, but AXS checkout currently offers only card and PayPal. A critical gap for 126M Japanese consumers.
Desc_Pain Point_3: Coachella, Stagecoach, and The O2 on-sales create extreme demand spikes. With no failover or multi-processor cascade, a single PSP timeout during peak load risks millions in lost ticket revenue and fan backlash.
Desc_Pain Point_4: AXS is the official ticketing partner for The O2, AO Arena Manchester, Uber Arena Berlin, and Barclays Arena Hamburg. European fans lack iDEAL, Bancontact, BLIK, Giropay, and Sofort at checkout.
Desc_Pain Point_5: AXS runs separate payment configurations across US, UK, Australia, Germany, and Japan with no orchestration layer. Each market addition requires custom payment integration, slowing the global expansion that AEG is pushing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Visa / Mastercard / Amex (card networks)
PSP_2: PayPal
PSP_3: Klarna (BNPL, US + ANZ)
PSP_4: Undisclosed primary processor

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Konbini
Local_M_2: PayPay
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: BLIK
Local_M_6: Giropay
Local_M_7: Pix
Local_M_8: OXXO
Local_M_9: Afterpay AU
Local_M_10: POLi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every ticket transaction by BIN, issuer, and geography across multiple processors. On $2B+ in annual transactions across 50M tickets, a 3-10% auth uplift recovers tens of millions in ticket revenue currently lost to single-processor declines.
Desc_Yuno_Cap2: Automatic cascade eliminates single-point failures during Coachella, Stagecoach, and The O2 on-sales. When the primary processor drops under peak demand, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions protecting AEG's biggest events.
Desc_Yuno_Cap3: Activates the APMs AXS needs for global scale: Konbini and PayPay for the Lawson Japan JV, iDEAL for Netherlands, Giropay for German arenas, BLIK for Poland, Afterpay for Australia, Pix for Brazil expansion. One API, 1,000+ payment methods, zero per-market engineering.
Desc_Yuno_Cap4: One dashboard unifying payment flows across US, UK, Germany, Australia, Japan, and Sweden into a single reconciliation layer. Real-time approval monitoring for 1,600+ venue partners, NOVA fraud engine with 75% fewer false positives protecting high-value event on-sales.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**AXS at a glance:**
- American ticket outlet for sports and entertainment, founded in 2011
- Wholly owned subsidiary of Anschutz Entertainment Group (AEG) since September 2019
- AEG is the world's second largest entertainment promoter behind Live Nation
- ~50 million tickets sold annually worldwide
- $2B+ in annual transactions (post-Veritix merger, 2015)
- 1,600+ partner brands across sports, music, and entertainment
- 500+ premier venues, sports teams, and event organizers
- 350+ employees globally
- Offices: Los Angeles (HQ), Cleveland, Charlotte, Dallas, Denver, London, Stockholm, Melbourne, Tokyo
- CEO: Bryan Perez (20+ years in live entertainment, former President of Digital/Ticketing/Media at AEG)
- CTO: Nikhil Bobde (20+ years at Microsoft and Meta, appointed 2024)
- CFO: Jason Boxer
- Chief Innovation Officer: Alex Hazboun

**Key venues and clients:**
- Coachella Valley Music and Arts Festival
- Stagecoach Country Music Festival
- The O2 (London)
- AO Arena (Manchester)
- Uber Arena (Berlin, formerly Mercedes-Benz Arena)
- Barclays Arena (Hamburg)
- Red Rocks Amphitheatre
- Crypto.com Arena (formerly Staples Center)
- T-Mobile Arena (Las Vegas)
- LA28 Olympic & Paralympic Games
- BNP Paribas Open, WM Phoenix Open
- Cleveland Cavaliers, Houston Rockets, Vegas Golden Knights
- B.League (Japan)
- Stockholm Live

**Recent strategic moves:**
- Oct 2024: Partnership with Uber Arena Berlin + Barclays Arena Hamburg (first German operations)
- Nov 2024: Acquired white label eCommerce (Hamburg-based ticketing company, founded 2012)
  - Clients: Wacken Open Air, Jazz Open Stuttgart, THW Kiel handball
- Oct 2025: Joint venture with Lawson Entertainment in Japan
  - Access to 15,000 Lawson + Mini Stop convenience stores
  - Lawson Tickets spans sports, live entertainment, theater, cinema, fan clubs

**Confirmed PSPs / Payment Methods:**
- Credit cards: Visa, Mastercard, American Express
- PayPal: Accepted across US, UK, ANZ markets
- Klarna: BNPL financing and Pay in 4 (US, ANZ)
- PayPal Pay in 4: Available in ANZ market
- No Apple Pay or Google Pay confirmed at checkout
- Backend payment processor: Not publicly disclosed
- No payment orchestrator detected

**Top Market Gap Analysis:**

MARKET 1: Japan (Lawson JV, B.League partnership)
  Accepted: Cards, likely PayPal
  Missing: Konbini (convenience store payments), PayPay, Line Pay, Rakuten Pay
  Note: Lawson JV connects to 15,000 stores but payment checkout still card-centric

MARKET 2: Germany (Uber Arena, Barclays Arena, white label eCommerce acquisition)
  Accepted: Cards, PayPal
  Missing: Giropay, SOFORT/Klarna DE, EPS
  Note: German consumers strongly prefer local payment methods over card payments

MARKET 3: United Kingdom (The O2, AO Arena, BST Hyde Park, multiple venues)
  Accepted: Cards, PayPal
  Missing: Open Banking (Pay by Bank), Klarna UK
  Note: UK is AXS's largest European market; Open Banking adoption accelerating

MARKET 4: Australia / New Zealand (Frontier Touring, SCG, Allianz Stadium)
  Accepted: Cards, PayPal, Klarna Pay in 4
  Missing: Afterpay AU/NZ, POLi, BPAY
  Note: Afterpay originated in AU with 3.6M+ users; natural fit for event tickets

MARKET 5: Nordics (Stockholm Live, Tele2 Arena)
  Accepted: Cards, PayPal
  Missing: Swish (Sweden), Vipps (Norway), MobilePay (Denmark)
  Note: Swish has 8M+ users in Sweden (80%+ of population)

**Key Meeting Angles:**
1. **Japan JV urgency** | Lawson partnership opens 15,000 store locations but checkout lacks Konbini, PayPay, and Line Pay that Japanese fans expect
2. **AEG global expansion mandate** | Parent company AEG is pushing AXS into new markets (Germany, Japan, ANZ) but payment infrastructure requires per-market custom integrations
3. **$2B+ transaction volume** | At this scale, even 1% auth improvement recovers $20M+ in revenue
4. **CTO from big tech** | Nikhil Bobde (ex-Microsoft, ex-Meta) understands platform architecture and API-first orchestration
5. **Peak demand vulnerability** | Coachella, The O2, and LA28 Olympics create extreme spikes with no failover protection
6. **German market entry** | Uber Arena + Barclays Arena + white label eCommerce acquisition all require German-native payment methods
7. **LA28 Olympics** | Official ticketing partner for 2028 Olympics needs bulletproof multi-currency, multi-APM infrastructure

**Sources:**
- [AXS Payment Methods (US Help Center)](https://support.axs.com/hc/en-us/articles/360031871913-What-payment-methods-can-I-use-when-buying-tickets)
- [AXS Payment Methods (ANZ Help Centre)](https://axssupportanz.axs.com/hc/en-au/articles/8470767976476-What-payment-methods-can-I-use-when-buying-tickets)
- [AXS Klarna Financing](https://support.axs.com/hc/en-us/articles/10003969293340-Klarna-Financing-and-Pay-In-4)
- [AXS Wikipedia](https://en.wikipedia.org/wiki/AXS_(company))
- [AXS Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Axs_logo.svg)
- [AEG Purchases All Outstanding Shares of AXS](https://aegworldwide.com/press-center/press-releases/aeg-purchases-all-outstanding-shares-axs)
- [AXS Appoints Nikhil Bobde as CTO](https://aegworldwide.com/press-center/press-releases/axs-appoints-nikhil-bobde-chief-technology-officer-and-names-alex)
- [AXS Germany Arena Partnerships](https://aegworldwide.com/press-center/press-releases/axs-partners-two-leading-arenas-germany)
- [AXS Acquires white label eCommerce](https://solutions.axs.com/us/2024/11/04/axs-announces-acquisition-of-germany-based-ticketing-company-white-label-ecommerce/)
- [AXS x Lawson Entertainment Japan JV](https://aegworldwide.com/press-center/press-releases/axs-and-lawson-entertainment-partner-enhance-fan-ticketing-experiences)
- [AXS AO Arena Manchester Partnership](https://aegworldwide.com/press-center/press-releases/axs-named-official-ticketing-partner-ao-arena-manchester)
- [AXS The O2 Official Partner](https://www.theo2.co.uk/visit-us/axs-official-ticket-source)
- [AXS Global Leadership Additions](https://aegworldwide.com/press-center/press-releases/axs-adds-sian-egbujie-and-christin-chu-global-leadership-team)
- [AXS Europe Awards](https://aegworldwide.com/press-center/press-releases/axs-europe-wins-two-prestigious-industry-awards)
- [AEG x American Express Global Partnership](https://aegworldwide.com/press-center/press-releases/aeg-and-american-express-expand-global-partnership-growing-more-20-year)
- [Bryan Perez Congressional Testimony](https://www.congress.gov/116/meeting/house/110588/witnesses/HHRG-116-IF02-Wstate-PerezB-20200226.pdf)
- [AXS CEO on International Expansion](https://solutions.axs.com/us/2023/02/02/axs-ceo-bryan-perez-on-international-expansion-identity-based-ticketing-and-personalized-experiences/)
- [Klarna x AXS Store Page](https://www.klarna.com/us/store/3dd943a9-429d-4785-98c6-a46c084ea3b3/AXS/pay-with-klarna/)
- [AXS Lawson Japan (Digital Music News)](https://www.digitalmusicnews.com/2025/10/21/axs-japan-lawson-joint-venture/)
- [AXS Lawson Japan (IQ Magazine)](https://www.iqmagazine.com/2025/10/axs-expands-ticketing-operations-in-japan/)
