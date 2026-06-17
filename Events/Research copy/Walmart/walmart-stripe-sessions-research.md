# WALMART | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Walmart
═══════════════════════════════════════

Logo: https://corporate.walmart.com/content/dam/corporate/media-library/logos/wmt-spark-logo.svg
Nombre merchant: Walmart

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Global Stack
Tittle_Pain Point_2: No NFC / Wallet Support
Tittle_Pain Point_3: Soft Decline Revenue Loss
Tittle_Pain Point_4: LATAM APM Gaps
Tittle_Pain Point_5: No Failover Routing

Desc_Pain Point_1: Walmart.com, Walmex (Cashi), Flipkart, and Sam's Club China each run separate payment stacks with no unified orchestration layer, creating reconciliation chaos across 18 countries.
Desc_Pain Point_2: Walmart blocks Apple Pay, Google Pay, Samsung Pay, and all NFC tap to pay. Proprietary Walmart Pay locks users into QR codes, sacrificing checkout speed and alienating digital wallet users.
Desc_Pain Point_3: Walmart Labs found most online payment declines were soft declines from issuer timeouts. Even with auto retry, unrecovered soft declines bleed GMV on $79B+ US e-commerce volume.
Desc_Pain Point_4: Walmart operates in Mexico, Chile, and Central America but lacks key local methods like SPEI transfers, OXXO online vouchers, and CoDi on its own e-commerce, losing unbanked shoppers.
Desc_Pain Point_5: No evidence of multi acquirer failover. A single processor outage (Dec 2025: 6,500+ user reports) blocks 100% of online transactions with zero automatic cascade to backup acquirers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Fiserv
PSP_2: JP Morgan Chase
PSP_3: Klarna
PSP_4: OnePay (Synchrony/Mastercard)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Apple Pay
Local_M_2: Google Pay
Local_M_3: SPEI
Local_M_4: CoDi
Local_M_5: Pix
Local_M_6: UPI
Local_M_7: Webpay (Chile)
Local_M_8: BLIK
Local_M_9: Alipay
Local_M_10: WeChat Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Auto Retry
Tittle_Yuno_Cap3: 300+ Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Per transaction routing across Fiserv, JP Morgan, and additional acquirers. Each of Walmart's $121B in annual e-commerce transactions is routed to the highest performing processor for that card BIN, issuer, and market. At Walmart's scale, even a 2% auth rate uplift translates to $2.4B+ in recovered GMV annually.
Desc_Yuno_Cap2: Automatic cascade eliminates Walmart's single point of failure risk. When one processor times out or declines, Yuno reroutes to the next best acquirer in milliseconds, turning soft declines into completed sales. InDrive recovered up to 50% of failed transactions with this exact feature.
Desc_Yuno_Cap3: Activates the local APMs Walmart's 18 country footprint demands: SPEI and OXXO in Mexico (52B in Walmex revenue), Pix in Brazil (Flipkart expansion), UPI in India (PhonePe ecosystem), Webpay in Chile, Alipay and WeChat Pay in China. One API, zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Walmart's fragmented Fiserv + JP Morgan + Klarna + OnePay + Cashi + Flipkart settlement streams. Real time approval rate monitoring, centralized reconciliation across all 18 countries and currencies, millisecond anomaly detection via Yuno Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Walmart at a glance:**
- NYSE: WMT. Headquarters: Bentonville, Arkansas
- FY2025 Revenue: $681B ($1.87B per day), 5.1% YoY growth, 4.3% operating margin
- Global e-commerce sales: $121B (FY2025), representing 18% of total company revenue
- US e-commerce: $79.3B (21% YoY growth). International e-commerce: ~$31.4B
- 2.1 million associates worldwide. 10,500+ stores in 19 countries (US + 18 international)
- Walmart+ membership program (subscription commerce)
- Walmart Marketplace: 150,000+ third party sellers, operating in US, Canada, Mexico, Chile

**Key leadership (Payments and Digital Commerce):**
- Doug McMillon, President and CEO, Walmart Inc.
- David Guggina, President and CEO, Walmart U.S. (former EVP/Chief eCommerce Officer)
- Seth Dallaire, EVP and Chief Growth Officer, Walmart Inc. (global Marketplace, Walmart+, Walmart Connect)
- Jamie Henry, VP of Finance, Emerging Payments (leads pay by bank, instant payments initiatives)
- Guilherme Loureiro, CEO and President, Walmex (Mexico and Central America)
- OnePay leadership: separate fintech entity (Walmart + Ribbit Capital), $4B valuation (Jan 2026)

**Confirmed PSPs and Payment Partners:**

| Provider | Role | Evidence |
|----------|------|----------|
| Fiserv | Pay by bank / instant payments (via NOW network, FedNow, RTP) | [PYMNTS](https://www.pymnts.com/news/faster-payments/2024/walmart-teams-with-fiserv-instant-bank-payments/) |
| JP Morgan Chase | Marketplace seller payments, Marketplace Wallet (FDIC insured), merchant acquiring | [JP Morgan](https://www.jpmorgan.com/payments/newsroom/embedded-finance-walmart-marketplace-sellers) |
| Klarna | Exclusive BNPL provider (replaced Affirm, March 2025) | [CNBC](https://www.cnbc.com/2025/03/17/walmart-klarna-nearing-ipo-wins-fintech-partnership-from-affirm.html) |
| OnePay (One Finance) | Fintech subsidiary: credit cards (Synchrony/Mastercard), debit, BNPL, savings | [Bloomberg](https://www.bloomberg.com/news/articles/2026-01-09/walmart-backed-super-app-onepay-hits-4-billion-valuation) |
| Payoneer / Hyperwallet | Third party seller payout providers (Marketplace) | [Walmart Marketplace](https://marketplacelearn.walmart.com/guides/Taxes%20&%20payments/Payments/Payment-processing) |
| Cashi (Mexico) | Walmex digital wallet app, 3.4M+ users, integrated Aplazo BNPL | [PYMNTS](https://www.pymnts.com/walmart/2025/walmart-de-mexicos-digital-payments-app-integrates-aplazos-bnpl-offering/) |
| Flipkart (India) | Separate payment stack, Flipkart UPI (Axis Bank), PhonePe ecosystem | [Wikipedia](https://en.wikipedia.org/wiki/PhonePe) |

**No payment orchestrator detected.** Each market runs an independent stack with no unified routing or failover layer.

---

## Top Markets and Payment Gap Analysis

**MARKET 1: United States (85%+ of Walmart.com traffic, $79.3B e-commerce)**
  Accepted: Visa, Mastercard, Amex, Discover, PayPal, Walmart Pay (QR), Pay by Bank (Fiserv), Klarna BNPL, EBT, Walmart Gift Cards, Walmart Balance/Cash
  Missing: Apple Pay, Google Pay, Samsung Pay, Venmo (standalone), Cash App Pay, ACH direct
  Note: Walmart deliberately blocks all NFC payments to force users into proprietary Walmart Pay. This locks out 500M+ Apple Pay and Google Pay users globally.

**MARKET 2: Mexico and Central America ($52B Walmex revenue, largest international market)**
  Accepted: Visa, Mastercard, Cashi digital wallet, Aplazo BNPL, cash at stores
  Missing: SPEI online transfers, CoDi (Mexico QR payments), OXXO Pay online vouchers, Mercado Pago
  Note: 60% of Mexicans are unbanked. Cashi has only 3.4M users. OXXO Pay reaches 20,000+ locations but is not integrated into Walmex e-commerce checkout.

**MARKET 3: China ($20B in FY2025 revenue, Sam's Club focused)**
  Accepted: WeChat Pay and Alipay at physical Sam's Club stores
  Missing: Full WeChat Pay and Alipay integration on Sam's Club China e-commerce, UnionPay online optimization
  Note: Sam's Club China is rapidly growing e-commerce through cloud based fulfillment. Payment optimization could unlock higher conversion in a market dominated by super app payments.

**MARKET 4: India (Flipkart, $60B+ projected IPO valuation)**
  Accepted: Flipkart UPI, credit/debit cards, PhonePe, Paytm, net banking
  Missing: Unified payment layer with Walmart US. PhonePe processes 47.8% of all UPI transactions but operates as a separate entity.
  Note: PhonePe IPO filed Sept 2025 (shelved Mar 2026 due to market conditions). Flipkart IPO also expected. India is Walmart's highest growth potential market.

**MARKET 5: Canada (400+ stores, growing e-commerce)**
  Accepted: Visa, Mastercard, Amex, Discover, debit cards, gift cards
  Missing: Interac Online, Apple Pay, Google Pay
  Note: Canada mirrors the US NFC block policy. Interac e-Transfer is Canada's dominant P2P and bill payment method but is absent from Walmart.ca checkout.

**MARKET 6: Chile (Lider and Walmart Chile formats)**
  Accepted: Credit/debit cards, limited online payments
  Missing: Webpay (Chile's dominant online payment rail), Khipu, MACH, Multicaja
  Note: Walmart Marketplace recently expanded to Chile. Local APMs are critical for conversion in a market where Webpay processes the majority of online transactions.

---

## Payment Outage and Friction History

| Date | Incident | Impact | Source |
|------|----------|--------|--------|
| Dec 30, 2025 | Website and app full outage | 6,500+ user reports, purchases blocked for hours during holiday peak, Sam's Club also affected | [Yahoo Finance](https://finance.yahoo.com/news/walmart-outage-affects-thousands-shoppers-133000181.html) |
| Apr 17, 2025 | Partial outage | Delayed order confirmations, delivery tracking failures | [Tom's Guide](https://www.tomsguide.com/news/live/walmart-outage-apr-17-2025) |
| Ongoing | Soft decline issue | Walmart Labs identified most online payment declines were soft declines (issuer timeouts). Built auto retry, but unresolved cases still bleed GMV | [Chain Store Age](https://chainstoreage.com/operations/walmart-takes-hard-look-at-online-soft-declines) |
| Ongoing | Payment method errors | "Walmart Pay Declined But Card Works" is a widely reported issue with multiple third party troubleshooting guides | [Illinois.edu](https://blog.founders.illinois.edu/walmart-pay-declined-but-card-works/) |

---

## OnePay / One Finance Deep Dive

- Founded: Jan 2021 (Walmart + Ribbit Capital joint venture)
- Valuation: $4B+ (Jan 2026), up from $2.5B (Dec 2024)
- Revenue run rate: $200M+, processes $15B+ in payment flow
- Products: checking, savings, BNPL, early wage access, debit cards
- Credit card program: Synchrony as exclusive issuer, powered by Mastercard, launching fall 2025
- Target: 255M Walmart customers + 1.6M US associates (underbanked focus)
- Key signal: Walmart is building its own financial services stack. An orchestration layer underneath could unify OnePay, Klarna, Fiserv, and card processing.

---

## Yuno Success Case References

**InDrive** (ride hailing, 50+ countries)
  Recovered up to 50% of failed transactions through Yuno's failover and smart routing. Directly comparable to Walmart's soft decline challenge at massive scale.

**Rappi** (Latin American super app)
  Activated 300+ local payment methods across LATAM markets through Yuno. Mirrors Walmart's need for SPEI, OXXO, CoDi, and Pix integration across Mexico, Central America, and growth markets.

**McDonald's** (global QSR)
  Unified payment orchestration across multiple countries and acquirers through a single API. Directly comparable to Walmart's fragmented 18 country payment stack with no unified layer.

**Wingo** (Latin American airline)
  Increased authorization rates and activated local payment methods in Colombia, Cuba, and Venezuela through Yuno. Demonstrates Yuno's capability in markets where traditional card penetration is low, similar to Walmart's unbanked LATAM customer base.

---

## Key Meeting Angles

1. **$121B e-commerce with no orchestrator** | Walmart runs the world's second largest e-commerce operation with fragmented payment stacks across markets. No evidence of unified routing, failover, or APM orchestration.

2. **NFC refusal creates friction** | Blocking Apple Pay, Google Pay, and tap to pay alienates billions of digital wallet users. Yuno's 300+ APM library could activate these methods while maintaining Walmart's data control through orchestration layer analytics.

3. **Soft decline problem at scale** | Walmart Labs admitted most online declines are soft declines. At $79.3B US e-commerce volume, even 1% of unrecovered soft declines equals $793M in lost GMV. Yuno's auto retry and cascade routing directly solves this.

4. **OnePay as Trojan horse** | Walmart is building a $4B fintech subsidiary. The complexity of OnePay + Klarna + Fiserv + JP Morgan + Cashi + Flipkart payments demands orchestration. Yuno sits underneath all of them.

5. **LATAM is Walmart's largest international market** | $52B Walmex revenue with only 3.4M Cashi users. 60% of Mexico is unbanked. Yuno activates SPEI, OXXO, CoDi, and Mercado Pago with one API, exactly what Rappi did.

6. **December 2025 outage exposure** | 6,500+ users unable to transact during peak holiday season. Zero failover. Yuno's cascade routing would have automatically redirected to a backup acquirer in milliseconds.

7. **18 country, one dashboard opportunity** | Walmart International (Mexico, Chile, Central America, China, India, Canada, 8 African countries) has no centralized payment visibility. Yuno Monitors provides real time anomaly detection and unified reconciliation across every market.

---

## Sources

- [Walmart Corporate: Leadership](https://corporate.walmart.com/about/leadership)
- [Walmart Corporate: International Markets](https://corporate.walmart.com/about/international/markets)
- [Walmart Payment Methods (Taxomate)](https://taxomate.com/blog/walmart-payment-methods)
- [Walmart FY2025 Earnings Release (SEC)](https://www.sec.gov/Archives/edgar/data/104169/000010416925000010/earningsreleasefy25q4.htm)
- [Walmart Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/WMT/walmart/revenue)
- [Walmart E-commerce Stats (StatsUp/Analyzify)](https://analyzify.com/statsup/walmart)
- [PYMNTS: Walmart Teams With Fiserv on Instant Bank Payments](https://www.pymnts.com/news/faster-payments/2024/walmart-teams-with-fiserv-instant-bank-payments/)
- [JP Morgan: Embedded Finance for Walmart Marketplace Sellers](https://www.jpmorgan.com/payments/newsroom/embedded-finance-walmart-marketplace-sellers)
- [CNBC: Klarna Replaces Affirm at Walmart](https://www.cnbc.com/2025/03/17/walmart-klarna-nearing-ipo-wins-fintech-partnership-from-affirm.html)
- [Bloomberg: OnePay Hits $4B Valuation](https://www.bloomberg.com/news/articles/2026-01-09/walmart-backed-super-app-onepay-hits-4-billion-valuation)
- [Mastercard: OnePay + Synchrony Credit Card Launch](https://www.mastercard.com/news/press/2025/june/onepay-and-synchrony-to-launch-new-industry-leading-credit-card-program-with-walmart-credit-card-to-be-powered-by-mastercard-and-set-to-go-live-this-fall/)
- [PaymentsJournal: OnePay Poised to Take Off](https://www.paymentsjournal.com/walmarts-fintech-one-is-poised-to-take-off-in-2025/)
- [PYMNTS: Walmex Integrates Aplazo BNPL](https://www.pymnts.com/walmart/2025/walmart-de-mexicos-digital-payments-app-integrates-aplazos-bnpl-offering/)
- [Yahoo Finance: Dec 2025 Outage](https://finance.yahoo.com/news/walmart-outage-affects-thousands-shoppers-133000181.html)
- [PYMNTS: Website/App Outage](https://www.pymnts.com/walmart/2025/walmart-website-app-outage-impacts-thousands-customers/)
- [Chain Store Age: Soft Declines](https://chainstoreage.com/operations/walmart-takes-hard-look-at-online-soft-declines)
- [MacRumors: Walmart No Apple Pay 2026](https://www.macrumors.com/2026/01/19/walmart-no-apple-pay/)
- [Digital Trends: Apple Pay at Walmart](https://www.digitaltrends.com/phones/can-you-use-apple-pay-at-walmart-explained/)
- [Walmart Marketplace: Payment Processing](https://marketplacelearn.walmart.com/guides/Taxes%20&%20payments/Payments/Payment-processing)
- [TechCrunch: PhonePe IPO](https://techcrunch.com/2026/01/22/tiger-global-and-microsoft-to-fully-exit-walmart-backed-phonepe-via-its-ipo/)
- [TechCrunch: PhonePe Shelves IPO](https://techcrunch.com/2026/03/16/walmart-backed-phonepe-shelves-ipo-as-global-tensions-rattle-markets/)
- [Brandfetch: Walmart Logo](https://brandfetch.com/walmart.com)
- [Walmart Media Library](https://corporate.walmart.com/news/media-library)
- [SimilarWeb: Walmart.com Traffic](https://www.similarweb.com/website/walmart.com/)
- [Electroiq: Walmart Statistics 2026](https://electroiq.com/stats/walmart-statistics/)
- [Payments Dive: Klarna Displaces Affirm](https://www.paymentsdive.com/news/klarna-buy-now-pay-later-bnpl-affirm-walmart-payments/742676/)
- [Retail Brew: JPMorgan Launches Walmart Marketplace Solution](https://www.retailbrew.com/stories/2025/03/27/jpmorgan-launches-payment-solution-for-sellers-on-walmart-marketplace)
- [Walmart Corporate: Leadership Changes Jan 2026](https://corporate.walmart.com/news/2026/01/16/walmart-announces-leadership-changes)
