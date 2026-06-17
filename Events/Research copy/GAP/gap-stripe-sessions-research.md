# GAP INC. | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: GAP Inc.
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/9/9a/Gap_logo.svg
Nombre merchant: GAP Inc.

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Brand PSP Sprawl
Tittle_Pain Point_2: UK Platform Dependency
Tittle_Pain Point_3: Franchise Payment Blind
Tittle_Pain Point_4: BNPL Fragmentation
Tittle_Pain Point_5: Fraud Decline Friction

Desc_Pain Point_1: Four brands (Gap, Old Navy, Banana Republic, Athleta) each run separate e-commerce sites with Barclays issuing co-branded Mastercards, Klarna and Afterpay handling BNPL, and PayPal processing digital wallet payments. No unified orchestration layer connects 3,569 stores across 40 countries with the digital checkout experience.
Desc_Pain Point_2: Gap closed all 81 UK/Ireland stores and migrated to Next's Total Platform. UK checkout now runs through Next's infrastructure, accepting Next credit accounts, Klarna, PayPal, and Apple Pay. Gap has limited control over its own UK payment optimization, routing, and customer checkout experience.
Desc_Pain Point_3: Over 1,000 franchise stores across Asia, Europe, Latin America, the Middle East, and Africa operate independently. Gap has no visibility into franchise payment performance, no ability to optimize authorization rates, and no unified data on payment method preferences across franchise markets.
Desc_Pain Point_4: Afterpay and Klarna both serve the US market across all four brands. Each BNPL provider has a separate contract, separate reconciliation, and separate dispute handling. Neither extends to franchise international markets where installment payment demand is highest.
Desc_Pain Point_5: Customers report orders cancelled due to fraud flags with no explanation and no recourse. The refund claim system requires credit card information through an AI chat interface, which customers describe as confusing and untrustworthy. BBB complaints show persistent payment processing and refund failures.

SLIDE 1: PSP TOPOLOGY

PSP_1: Barclays (co-branded Mastercard issuer)
PSP_2: Klarna (BNPL, US + UK)
PSP_3: Afterpay (Block) (BNPL, US)
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Venmo
Local_M_2: Cash App Pay
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: PIX
Local_M_6: Konbini
Local_M_7: OXXO
Local_M_8: Mada
Local_M_9: GCash
Local_M_10: Open Banking (UK)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route each transaction to the optimal acquirer by market, card BIN, and issuer in real time. With $15.1B in annual revenue and 38% flowing through e-commerce (~$5.7B digital), even a 2% authorization uplift translates to $114M+ in recovered annual revenue. Smart Routing dynamically selects the best processor for Gap, Old Navy, Banana Republic, and Athleta from a single integration.
Desc_Yuno_Cap2: When Barclays declines a co-branded Mastercard or a standard Visa transaction fails, Yuno automatically cascades to the next best processor in milliseconds. Orders flagged as fraud by one processor get a second chance through an alternative route before the customer ever sees a decline. Gap's "cancelled due to fraud" problem disappears.
Desc_Yuno_Cap3: One API integration activates Konbini and PayPay in Japan, OXXO and SPEI in Mexico, PIX and Boleto in Brazil, Mada in Saudi Arabia, GCash in the Philippines, and iDEAL in the Netherlands. Yuno connects 1,000+ payment methods across 40+ countries. Gap's 40-country franchise footprint gets local payment coverage without individual market integrations.
Desc_Yuno_Cap4: Replace Gap Inc.'s fragmented stack of Barclays, Klarna, Afterpay, PayPal, and Next's UK platform with a single orchestration dashboard. Real-time approval rate monitoring across Gap, Old Navy, Banana Republic, and Athleta in all 40 countries from one console. Franchise markets gain visibility. Centralized settlement and millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GAP Inc. at a glance:**
- Founded 1969 in San Francisco, California. Publicly traded (NYSE: GAP)
- CEO: Richard Dickson (former Mattel COO, joined 2023)
- CTO: Sven Gerjets (former Mattel CTO, joined June 2024, established Office of AI)
- Four brands: Gap, Old Navy, Banana Republic, Athleta
- 3,569 stores across ~40 countries (2,506 company-owned + ~1,063 franchise)
- Revenue: $15.09B (fiscal 2025), up 1.3% YoY. $14.89B (fiscal 2024)
- E-commerce: 38% of total net sales (~$5.7B digital), grew 4% in fiscal 2024
- US revenue: ~86% of total. International: ~14%
- Company-owned stores: US, Canada, Japan, Taiwan, Mexico
- Franchise markets: Asia, Europe, Latin America, Middle East, Africa
- UK operated through 51/49 joint venture with Next plc (online + shop-in-shops)
- AI-forward: Office of AI established 2024, AI monetization initiatives for 2025
- Barclays acquired $3.8B Gap credit card portfolio from Synchrony (April 2022)

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| Barclays | Co-branded Mastercard issuer (Gap, Old Navy, Banana Republic, Athleta cards) | US |
| Klarna | BNPL (Pay in 4, Pay in Full) across all four brands | US, UK |
| Afterpay (Block) | BNPL (4 installments) across all four brands | US |
| PayPal | Digital wallet | US, UK, international |
| Apple Pay | Mobile wallet (online + in-store) | US, UK |
| Google Pay | Mobile wallet | US, UK |
| Next plc (Total Platform) | UK e-commerce checkout infrastructure | UK |

**No payment orchestrator detected.** Each brand and market runs separate payment integrations.

**Top Markets Gap Analysis:**

MARKET 1: United States (~86% of revenue, ~2,100+ company-owned stores)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Klarna, Afterpay, Barclays Mastercard/Store Card, gift cards
  Missing: Venmo, Cash App Pay, Amazon Pay, Sezzle, Affirm
  Insight: 38% of revenue is e-commerce (~$5.7B). Both Klarna and Afterpay serve US, creating duplicate BNPL infrastructure. Old Navy (largest brand by revenue) drives highest transaction volume.

MARKET 2: United Kingdom (Next joint venture, shop-in-shops + gap.co.uk on Next Total Platform)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Klarna, Next credit accounts
  Missing: Clearpay/Afterpay UK, Open Banking, Revolut Pay
  Insight: Gap closed 81 UK stores in 2021, migrated to Next's platform. Re-opened London stores Dec 2025 (Westfield, Wembley). Limited payment optimization control since checkout runs through Next infrastructure.

MARKET 3: Canada (company-owned stores + e-commerce)
  Accepted: Visa/MC, PayPal, Apple Pay
  Missing: Interac Online, Klarna Canada, Affirm Canada, Google Pay
  Insight: Second-largest company-owned market. Cross-border e-commerce from gap.com ships to Canada but local payment method coverage is thin.

MARKET 4: Japan (company-owned stores, gap.co.jp)
  Accepted: Visa/MC/Amex, local credit cards
  Missing: Konbini, PayPay, LINE Pay, Rakuten Pay, JCB (unconfirmed)
  Insight: Old Navy exited Japan in 2016 but Gap brand remains. Japan's cash-preferring culture and Konbini payment network make card-only checkout insufficient for online conversion.

MARKET 5: Mexico (company-owned stores, franchise)
  Accepted: Visa/MC
  Missing: OXXO, SPEI, Mercado Pago, CoDi
  Insight: OXXO is Mexico's dominant cash payment method. SPEI (instant bank transfer) is the fastest growing digital payment rail. Card-only checkout excludes the majority of Mexican online shoppers.

MARKET 6: Middle East & Africa (franchise, 40+ countries including Saudi Arabia, UAE, Egypt)
  Accepted: Visa/MC (through franchise operators)
  Missing: Mada (SA), STC Pay (SA), Tamara (SA/UAE), Tabby (UAE/SA), M-Pesa (Africa)
  Insight: Franchise operators control payment stack. Gap has zero visibility into authorization rates or local payment method performance. Mada has 93% card market share in Saudi Arabia.

MARKET 7: Asia Pacific (franchise, India, Philippines, Indonesia, etc.)
  Accepted: Visa/MC (through franchise operators)
  Missing: UPI (IN), GCash (PH), DANA (ID), GrabPay (SEA), local wallets
  Insight: Credit card penetration under 10% in Philippines, Indonesia. Without mobile wallets and bank transfers, franchise e-commerce cannot convert local shoppers.

**Payment and checkout error history:**
- Orders cancelled "due to fraud" with no explanation or recourse
- AI chat refund system requires credit card info, described as confusing and untrustworthy
- BBB complaints cite persistent payment processing failures and delayed refunds
- Customers report receiving 6 of 7 items with no refund or replacement for missing item
- Refund delays exceeding 12 months documented in consumer complaints
- Online checkout flow disruptions when applying discounts and rewards

**Key meeting angles:**
1. **$15B, four brands, zero orchestration** | Gap, Old Navy, Banana Republic, and Athleta each run separate payment stacks with no unified optimization. One Yuno integration serves all four.
2. **UK platform dependency** | Gap migrated to Next's checkout infrastructure, losing control over payment optimization. Yuno could sit between Gap and Next, enabling routing control.
3. **Franchise blind spot** | 1,000+ franchise stores in 40 countries with no payment visibility. Yuno's dashboard provides centralized authorization rate monitoring even across franchise partners.
4. **Japan + Mexico = APM opportunity** | Company-owned markets with card-only checkout where local methods (Konbini, OXXO) dominate. Immediate conversion uplift.
5. **Dual BNPL redundancy** | Both Afterpay and Klarna in the US, but zero BNPL in Japan, Canada, franchise markets. One Yuno API unifies all BNPL providers and extends coverage globally.
6. **AI-forward leadership** | CEO from Mattel, CTO from Mattel, Office of AI established. Payment orchestration fits the AI/optimization narrative.
7. **Fraud decline problem** | Orders cancelled without explanation. Smart routing with cascade retries reduces false fraud flags by offering alternative processing paths.

**Sources:**
- [Gap Payment Options (US)](https://www.gap.com/customer-service/payment-options?cid=1192374)
- [Gap UK Payment Methods (Zendesk)](https://gapuk.zendesk.com/hc/en-gb/articles/6869039877393-What-payment-methods-do-you-accept)
- [Gap International Orders](https://www.gap.com/customer-service/international-orders?cid=81267)
- [Gap + Klarna Partnership (Retail Dive)](https://www.retaildive.com/news/gap-inc-klarna-payments-BNPL/760118/)
- [Gap + Klarna (PYMNTS)](https://www.pymnts.com/bnpl/2025/gap-adopts-klarna-payment-options-across-apparel-brands/)
- [Gap + Afterpay Partnership](https://www.afterpay.com/en-US/stores/gap)
- [Old Navy + Afterpay](https://www.afterpay.com/en-US/stores/old-navy)
- [Gap + Barclays Credit Card Program](https://www.gapinc.com/en-us/articles/2022/06/gap-inc-launches-new-credit-card-program-in-partne)
- [Barclays Acquires Gap Portfolio from Synchrony](https://www.americanbanker.com/news/barclays-buying-3-8-billion-gap-card-portfolio-from-synchrony)
- [Gap FY2024 Results](https://www.gapinc.com/en-hk/articles/2025/03/gap-inc-reports-fourth-quarter-and-fiscal-2024-res)
- [Gap Inc. CTO Sven Gerjets Appointment](https://www.gapinc.com/en-us/articles/2024/06/sven-gerjets-named-chief-technology-officer-at-gap)
- [Gap CTO AI Strategy (Retail Tech Innovation Hub)](https://retailtechinnovationhub.com/home/2026/3/8/gap-inc-cto-sven-gerjets-ai-isnt-changing-who-we-are-its-extending-whats-possible)
- [Gap CEO Digital-First (Diginomica)](https://diginomica.com/back-cultural-conversation-perhaps-why-does-gap-inc-ceo-richard-dickson-say-firms-digital-first)
- [Gap UK Next Joint Venture](https://www.gapinc.com/en-us/articles/2022/03/gap-inc-opens-first-uk-shop-in-shop-on-oxford-stre)
- [Gap UK Next Platform Migration (Retail Bulletin)](https://www.theretailbulletin.com/fashion/gaps-uk-online-business-now-fully-migrated-to-nexts-platform-18-08-2022/)
- [Gap UK Returns to High Street (Retail TouchPoints)](https://www.retailtouchpoints.com/features/news-briefs/after-4-years-gap-returns-to-uk-high-street-with-london-stores)
- [Gap Apple Pay Guide](https://www.joinkudos.com/blog/does-gap-take-apple-pay)
- [Gap BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/clothing/gap-inc-1116-15912/complaints)
- [Gap Inc. Wikipedia](https://en.wikipedia.org/wiki/Gap_Inc.)
- [Gap Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Gap_logo.svg)
- [Gap Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/GAP/gap/revenue)
