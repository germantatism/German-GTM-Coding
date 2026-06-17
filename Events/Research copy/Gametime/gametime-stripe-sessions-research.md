# GAMETIME | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Gametime
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/0/0e/Gametime_logo.svg
Nombre merchant: Gametime

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US/Canada Only Ceiling
Tittle_Pain Point_2: No Failover on Peak Sales
Tittle_Pain Point_3: Limited APM Coverage
Tittle_Pain Point_4: Affirm Web-Only BNPL Gap
Tittle_Pain Point_5: Seller Payout Friction

Desc_Pain Point_1: Gametime operates in 60+ cities across only US and Canada. International expansion requires local payment methods (Pix, iDEAL, OXXO) that current checkout cannot support without per-market payment integrations.
Desc_Pain Point_2: Last-minute ticket purchases create extreme time pressure. Users buying minutes before events need instant auth. A single-processor failure during peak demand (NFL Sunday, concert on-sales) means permanent lost sales with no recovery window.
Desc_Pain Point_3: Checkout accepts cards, Apple Pay, Google Pay, Venmo, and Affirm. Missing Cash App Pay (57M+ US users skewing young), PayPal (which Gametime does not offer for buying), and any international methods for future expansion.
Desc_Pain Point_4: Affirm BNPL is only available on web checkout, not in the mobile app where most Gametime transactions occur. Mobile-first users (core demographic: millennials, Gen Z) cannot split payments on the platform they actually use.
Desc_Pain Point_5: Sellers on Gametime receive payouts exclusively via PayPal. No direct bank transfer, no Venmo payout option, limiting the seller supply side and creating reconciliation complexity at scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple Pay
PSP_2: Google Pay
PSP_3: Venmo
PSP_4: Affirm (BNPL, web only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal (buying side)
Local_M_2: Cash App Pay
Local_M_3: Pix
Local_M_4: OXXO
Local_M_5: iDEAL
Local_M_6: Klarna
Local_M_7: Afterpay
Local_M_8: Bancontact
Local_M_9: BLIK
Local_M_10: Interac

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every last-minute ticket purchase by BIN, issuer, and geography to the optimal processor. On millions of time-sensitive transactions, a 3-10% auth uplift directly recovers revenue that is permanently lost when a buyer cannot complete checkout seconds before an event.
Desc_Yuno_Cap2: Automatic cascade eliminates single-point failures during NFL Sunday, playoff on-sales, and concert rushes. When the primary processor drops, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions. For last-minute tickets, there is no second chance.
Desc_Yuno_Cap3: Unlocks international expansion beyond US/Canada: Pix for Brazil, OXXO and SPEI for Mexico, iDEAL for Netherlands, Interac for Canada (beyond cards), Cash App Pay for the 57M US users Gametime is missing today. One API, 1,000+ payment methods, zero per-market engineering.
Desc_Yuno_Cap4: One dashboard unifying Apple Pay, Google Pay, Venmo, Affirm, and card processors into a single reconciliation layer. Real-time approval monitoring across mobile and web checkout, NOVA fraud engine with 75% fewer false positives protecting high-velocity last-minute transactions.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gametime at a glance:**
- Mobile-first marketplace for last-minute tickets to sports, music, and theater events
- Founded in 2012 in San Francisco, CA (now headquartered in Menlo Park, CA)
- 60+ cities across US and Canada
- Total funding: $76.4M across 6 rounds (Series C: $30M, May 2022)
- Key investors: Accel, Google Ventures (GV), StartX, Sacramento Kings, San Francisco Giants
- The company has reached profitability (reported by CEO Brad Griffith)
- Revenue: ~$49M reported in 2016; current revenue not publicly disclosed but growing
- CEO/Founder: Brad Griffith (Sports Business Journal Forty Under 40)
- VP Engineering: Marco Huerta
- Former CRO: Colin Evans (StubHub co-founder, served 2014-2018)
- ~100-200 employees

**Key product features:**
- Two-tap purchase process (fastest checkout in ticketing)
- Panoramic seat view photos and interactive venue maps
- All-in pricing (no hidden fees displayed upfront)
- "Last Call" feature: purchase tickets even after events start
- Digital ticket delivery (Apple Wallet / Google Wallet)
- Gametime Sell: peer-to-peer resale marketplace

**Confirmed PSPs / Payment Methods:**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- Apple Pay: Accepted on iOS
- Google Pay: Accepted on Android
- Venmo: Integrated for purchases
- Affirm: BNPL, web checkout only (not mobile app)
- Seller payouts: PayPal only
- PayPal: NOT accepted for buying tickets
- Backend processor: Not publicly disclosed
- No payment orchestrator detected

**Tech stack (confirmed):**
- React Native (mobile), Angular (web)
- MongoDB, Kubernetes, OpenTelemetry
- Mixpanel (analytics)
- ISO/IEC 27001 certified

**Top Market Gap Analysis:**

MARKET 1: United States (primary market, 60+ cities)
  Accepted: Cards, Apple Pay, Google Pay, Venmo, Affirm (web only)
  Missing: Cash App Pay (57M+ users), PayPal (buying), Klarna/Afterpay
  Note: Core demographic is millennials/Gen Z who heavily use Cash App

MARKET 2: Canada (active market)
  Accepted: Cards, Apple Pay, Google Pay
  Missing: Interac Online, Interac e-Transfer
  Note: Interac dominates Canadian digital payments

MARKET 3: Mexico (potential expansion via StubHub/partners)
  Accepted: None currently
  Missing: OXXO, SPEI, CoDi, Mercado Pago
  Note: Natural expansion market for US-based ticketing platforms

MARKET 4: Brazil (potential expansion)
  Accepted: None currently
  Missing: Pix, Boleto
  Note: Pix has 150M+ users; massive live events market

MARKET 5: United Kingdom (potential expansion)
  Accepted: None currently
  Missing: Open Banking, Klarna UK
  Note: Largest English-speaking market outside US/Canada for live events

**Key Meeting Angles:**
1. **Last-minute = zero tolerance** | Every failed transaction is permanently lost revenue because buyers cannot wait for retries; failover is existential for the business model
2. **Mobile-first, BNPL gap** | Affirm only works on web, but Gametime is 80%+ mobile; mobile users cannot split payments, depressing AOV
3. **Cash App blind spot** | 57M+ US Cash App users (skewing young, matching Gametime's demographic) have no way to pay on the platform
4. **Profitability unlocked** | Company has reached profitability; now positioned to invest in international expansion that requires multi-APM infrastructure
5. **Series C growth capital** | $30M raised in 2022 to scale; international markets are the next frontier
6. **Seller-side friction** | PayPal-only payouts limit seller supply; orchestrated payouts could improve marketplace liquidity
7. **Two-tap checkout** | Gametime's core differentiator is speed; any payment friction directly hurts conversion on time-sensitive purchases

**Sources:**
- [Gametime Wikipedia](https://en.wikipedia.org/wiki/Gametime)
- [Gametime Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Gametime_logo.svg)
- [Gametime Payment Methods (Support)](https://support.gametime.co/en_us/draft-updating-and-adding-a-payment-method-rJsdam1a9)
- [Gametime Affirm Integration](https://support.gametime.co/en_us/how-to-complete-your-purchase-using-affirm-SyVrKWDn)
- [Gametime Apple/Google Wallet](https://support.gametime.co/en_us/apple-google-wallet-S1oC9HqT2)
- [Gametime x Venmo (Tumblr)](https://gametimeapp.tumblr.com/post/138177256120/gametime-teams-up-with-venmo-to-help-fans-pay-even)
- [Gametime Apple Pay Blog](https://gametimeapp.tumblr.com/post/146574255930/apple-pay-your-ticket-to-the-world-series)
- [Gametime About Page](https://gametime.co/about)
- [Gametime Crunchbase](https://www.crunchbase.com/organization/gametime)
- [Gametime International Cities](https://gametime.co/cities/international)
- [Gametime Sell Launch](https://gametime.co/blog/introducing-gametime-sell/)
- [Gametime New Logo](https://gametime.co/blog/gametime-new-logo/)
- [Gametime Series C TechCrunch](https://techcrunch.com/2019/02/07/gametime-lastcall/)
- [Gametime $20M Raise (TechCrunch)](https://techcrunch.com/2016/09/21/gametime-raises-20-million-to-sell-last-minute-textable-tickets-to-sports-and-concerts/)
- [Gametime $4M Raise (GeekWire)](https://www.geekwire.com/2014/gametime-raises-4m/)
- [Gametime Accel/GV Investors (PRNewswire)](https://www.prnewswire.com/news-releases/gametime-raises-4-million-from-accel-partners-and-prominent-professional-sports-team-investors-from-the-sacramento-kings-san-francisco-giants-vancouver-whitecaps-fc-and-derby-county-fc-276437311.html)
- [Gametime Growth Strategy (CanvasBusinessModel)](https://canvasbusinessmodel.com/blogs/growth-strategy/gametime-growth-strategy)
- [Gametime Tech Stack (Bitscale)](https://bitscale.ai/directory/gametime)
- [Brad Griffith (The Org)](https://theorg.com/org/gametime/org-chart/brad-griffith)
- [Gametime CBInsights](https://www.cbinsights.com/company/gametime-united-inc)
