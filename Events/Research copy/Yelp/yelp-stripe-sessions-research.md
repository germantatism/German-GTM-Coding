# YELP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Yelp
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/yelpblog.com/w/512/h/512/logo
Nombre merchant: Yelp

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Ad Billing
Tittle_Pain Point_2: No Real-Time Payments
Tittle_Pain Point_3: Booking Payment Gaps
Tittle_Pain Point_4: No Failover on Ad Spend
Tittle_Pain Point_5: International Revenue Leak

Desc_Pain Point_1: Yelp's $1.46B ad business accepts only credit/debit cards and checks. Service businesses (68% of ad revenue) often prefer ACH, SEPA, or local methods. No PayPal, no digital wallets, no bank transfers for advertising billing.
Desc_Pain Point_2: Yelp Guest Manager processes restaurant reservations and tableside payments through third-party POS integrations. No unified real-time payment processing for bookings, takeout, or service appointments across 330M cumulative reviews.
Desc_Pain Point_3: Yelp's booking and request-a-quote features handle payments through third-party iframes. When a consumer books a restaurant, home service, or auto repair, the payment experience is controlled by external providers with no Yelp optimization.
Desc_Pain Point_4: With $1.46B in net revenue from advertising, Yelp collects ad payments through a single billing system. If the card processor declines, billing thresholds go unmet and ad delivery is paused, directly impacting both advertiser experience and Yelp revenue.
Desc_Pain Point_5: Yelp operates in 32 countries but generates 90%+ revenue from the US. Zero local payment methods in Canada, UK, or other active markets. International advertisers must pay by US-denominated credit card.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Card (advertising billing)
PSP_2: Check (US/Canada, via sales rep)
PSP_3: Third-party POS (Guest Manager)
PSP_4: Third-party iframes (bookings)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: ACH Direct Debit
Local_M_2: SEPA Direct Debit
Local_M_3: BACS Direct Debit
Local_M_4: PayPal
Local_M_5: Apple Pay
Local_M_6: Google Pay
Local_M_7: iDEAL
Local_M_8: Interac (Canada)
Local_M_9: Open Banking
Local_M_10: Wire Transfer / Invoice

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each advertiser billing charge to the optimal acquirer for that card BIN, issuing bank, and country. With $1.46B in ad revenue across millions of SMB advertisers, even a 3% auth uplift on billing cycles recovers $43M+ in otherwise delayed or failed ad collections.
Desc_Yuno_Cap2: Automatic cascade across multiple acquirers when advertiser card payments are declined. Yuno reroutes in milliseconds to a backup processor. Failed ad billing = paused campaigns = lost Yelp revenue. Up to 50% recovery on soft declines, keeping ad delivery uninterrupted.
Desc_Yuno_Cap3: Accept ad payments locally: ACH for US SMBs, SEPA for European advertisers, BACS for UK businesses, Interac for Canada, PayPal/Apple Pay for digital-native businesses. One API, 1,000+ methods. Service businesses (68% of ad revenue) prefer bank-based payments.
Desc_Yuno_Cap4: One dashboard consolidating Yelp's fragmented ad billing + Guest Manager POS + booking payment streams. Real-time approval monitoring across advertiser segments, centralized reconciliation for $1.46B in annual collections, AI-powered anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Yelp at a glance:**
- Local business discovery and review platform
- Revenue: $1.46B net revenue in 2025 (record, 6% YoY growth)
- 2026 guidance: $1.455B to $1.475B net revenue
- Net income: $146M in 2025 (10% YoY growth)
- Adjusted EBITDA: $369M (25% margin)
- Public company: NYSE: YELP
- 330M cumulative reviews, 22M new reviews added in 2025
- Service-based businesses = 68% of total ad revenue
- Headquartered: San Francisco, California
- Accelerating AI transformation (AI-powered search, recommendations, ad targeting)

**Geographic operations:**
- Available in 32 countries worldwide
- 90%+ of revenue from United States
- Active offices: US, Toronto (Canada), London (UK)
- Closed most international sales/marketing operations in 2016
- International markets maintained as self-serve platforms

**Revenue breakdown:**
- Advertising: primary revenue source ($1.46B)
- Services: Home Services, Restaurants, Auto, Health, Beauty, Professional Services
- Products: Yelp Ads, Yelp Guest Manager, Request a Quote, Yelp Connect, Yelp Guaranteed
- Guest Manager: reservations, waitlist, kiosk, takeout, table management

**Confirmed PSPs / payment methods:**
- Credit/debit cards: primary billing method for advertising
- Checks: accepted for advertising (US/Canada, via sales rep, minimum payment requirements)
- Third-party POS integrations: Guest Manager tableside payments
- Third-party iframes: booking and appointment payments
- No direct PayPal, Apple Pay, or Google Pay for ad billing
- No payment orchestrator detected

**Billing structure:**
- Threshold-based billing (e.g., charged after $100 in ad spend)
- Monthly billing on 1st of month or every 30 days from ad launch
- Automatic charges to card on file
- No automatic bank account (ACH) billing option

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (90%+ of revenue)
  Currently offer: Credit/debit cards, checks
  Missing: ACH Direct Debit, PayPal, Apple Pay, Google Pay
  US SMBs increasingly expect ACH billing for recurring B2B payments. Digital wallets are standard.

MARKET 2: Canada (Toronto office)
  Currently offer: Credit/debit cards, checks
  Missing: Interac, EFT, PayPal
  Interac is the dominant payment network in Canada. Canadian SMBs expect local billing.

MARKET 3: United Kingdom (London office)
  Currently offer: Credit/debit cards
  Missing: BACS Direct Debit, Open Banking, PayPal
  BACS DD is the UK standard for recurring B2B billing.

MARKET 4: Germany
  Currently offer: Credit/debit cards (self-serve)
  Missing: SEPA Direct Debit, Sofort, invoice
  ~35% card penetration. German businesses strongly prefer SEPA for recurring payments.

MARKET 5: Australia
  Currently offer: Credit/debit cards (self-serve)
  Missing: BPAY, PayTo, direct debit
  Australian businesses commonly use BPAY and direct debit for B2B services.

**Key meeting angles:**
1. **$1.46B ad billing at risk** | Every failed card charge pauses ad campaigns and delays revenue collection. Smart routing protects the full revenue stream
2. **Service businesses (68% of ad rev)** | Home services, auto repair, restaurants prefer bank-based billing over credit cards. ACH/SEPA unlocks frictionless collection
3. **SMB advertiser retention** | Billing failures lead to paused campaigns, frustrated advertisers, and churn. Failover cascades keep campaigns running
4. **Guest Manager payment unification** | Yelp's restaurant product handles reservations, waitlist, and tableside payments through fragmented third-party POS. Orchestration unifies this
5. **AI transformation investment** | Yelp is investing heavily in AI. Modern payment infrastructure aligns with this modernization push
6. **International self-serve opportunity** | 32 countries with self-serve platforms but zero local payment methods. Even modest APM additions could reactivate international ad spend

**Sources:**
- [Yelp: Record 2025 Revenue Press Release](https://www.yelp-ir.com/news/press-releases/news-release-details/2026/Yelp-Delivers-Record-Net-Revenue-in-2025-Accelerating-Investment-in-AI-Transformation/default.aspx)
- [Yelp Brand Center](https://www.yelp.com/brand)
- [Brandfetch: Yelp Logo](https://brandfetch.com/yelpblog.com)
- [Yelp Privacy Policy](https://terms.yelp.com/privacy/en_us/20220831_en_us/)
- [Yelp Terms of Service](https://terms.yelp.com/tos/en_us/20260101_en_us/)
- [Yelp Billing & Payments Help](https://biz.yelp.com/support-center/Billing_Payments)
- [Yelp: Accepted Payment for Advertising](https://biz.yelp.com/support-center/article/What-forms-of-payment-does-Yelp-accept-to-pay-for-my-advertising)
- [Yelp Guest Manager](https://business.yelp.com/restaurants/products/yelp-guest-manager/)
- [Yelp Wikipedia](https://en.wikipedia.org/wiki/Yelp)
- [WiserReview: Yelp Statistics 2026](https://wiserreview.com/blog/yelp-statistics/)
- [CompaniesMarketCap: Yelp Revenue](https://companiesmarketcap.com/yelp/revenue/)
- [Yelp International Operations Retreat](https://diginomica.com/yelp-retreats-to-the-us-homeland-as-international-expansion-fails)
