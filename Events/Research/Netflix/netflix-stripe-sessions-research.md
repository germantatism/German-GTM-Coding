# NETFLIX | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Netflix
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Netflix_logo.svg/1024px-Netflix_logo.svg.png
Nombre merchant: Netflix

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: In-House Routing Ceiling
Tittle_Pain Point_2: Involuntary Churn Drain
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: Cross-Border Decline Wall
Tittle_Pain Point_5: Fragmented Settlement Ops

Desc_Pain Point_1: Netflix built proprietary dynamic routing for 1B+ annual transactions. Internal systems hit optimization limits without multi-acquirer failover; even basis-point gains translate to tens of millions in recovered revenue.
Desc_Pain Point_2: With 325M subscribers renewing monthly, even 1% involuntary churn from payment failures costs $54M+ ARR. Card expiry, issuer declines, and retry logic gaps silently erode the subscriber base every billing cycle.
Desc_Pain Point_3: 190+ countries served but local APM coverage remains thin. No Pix in Brazil (16.6M subs), no BLIK in Poland, no GCash in Philippines, no Nequi in Colombia. Millions of potential subscribers blocked at checkout.
Desc_Pain Point_4: Card-not-supported-in-territory errors force users to find alternative payment methods. Cross-border card declines in emerging markets create friction for the 72% of subscribers outside North America.
Desc_Pain Point_5: Netflix reconciles settlement files from every payment processor separately, each with non-uniform data formats. Managing Adyen, dLocal, Bango, carrier billing partners across 190 countries creates operational drag.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: dLocal
PSP_3: Bango
PSP_4: DOCOMO Digital

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: BLIK
Local_M_3: GCash
Local_M_4: Nequi
Local_M_5: Konbini
Local_M_6: Maya
Local_M_7: PSE
Local_M_8: Yape
Local_M_9: MoMo
Local_M_10: Mercado Pago

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Retry Recovery
Tittle_Yuno_Cap3: Local Payment Activation
Tittle_Yuno_Cap4: Unified Observability Layer

Desc_Yuno_Cap1: ML-driven per-transaction routing across all acquirers and processors. Each of Netflix's 1B+ annual renewals routed to the highest-performing acquirer for that card BIN, issuer, currency, and market. Yuno Smart Routing delivers +3 to 10% auth uplift. At $45B revenue, even 1% translates to $450M in recovered annual billings. InDrive achieved 90% approval rates across 10 LATAM markets.
Desc_Yuno_Cap2: When the primary acquirer declines, Yuno reroutes in milliseconds to the next best processor, turning failed renewals into retained subscribers with zero friction. Up to 50% recovery on soft declines. For Netflix, recovering just 0.5% of failed renewals across 325M subscribers means millions of saved accounts per year. Rappi cut anomaly detection from 5 to 10 minutes down to milliseconds.
Desc_Yuno_Cap3: One API activates 1,000+ payment methods Netflix does not currently offer: Pix in Brazil (16.6M subs), BLIK in Poland, GCash in Philippines, Konbini in Japan (9M subs), Nequi in Colombia, Yape in Peru. No per-market engineering sprints. McDonald's LATAM unlocked local APMs across 15+ markets through Yuno with zero custom integration.
Desc_Yuno_Cap4: Replaces Netflix's fragmented settlement reconciliation across Adyen, dLocal, Bango, and carrier billing partners. One dashboard with real-time approval rate monitoring, centralized reconciliation, and millisecond anomaly detection via NOVA. NOVA reduces false positive rates by 75%, freeing Netflix's payments analytics team from manual fraud review and decline analysis.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Netflix at a glance:**
- 325M+ paid subscribers globally (end 2025), 190+ countries
- Revenue: $45.18B (2025), +15.84% YoY growth
- 1B+ payment transactions processed annually
- Ad tier: 94M global MAU, ad revenue doubled in 2024 and projected to double again in 2025
- Password sharing crackdown drove 27% subscriber growth since May 2023
- Pursuing $72B acquisition of Warner Bros. Discovery
- Co-CEOs: Ted Sarandos and Greg Peters

**Payments Leadership:**
- **Kristen Morrow-Greven**, VP and Head of Global Payments (since 2015, based in Amsterdam). Previously at PayPal and Federal Reserve Bank of New York. Appointed to advise Federal Reserve Board on FedNow. Leads Strategy, Product, Fintech, and Payment Partnerships globally.
- **Ebi Atawodi**, Director of Payments, EMEA (joined from Uber, previously Uber's Head of Product for Payments). Based in Amsterdam.
- **Gunjan Pradhan**, Director of Payments, India/South Asia/ANZ (based in Sydney). Previously at PayU India and Citrus. Women in Payments Rise Up Power Player, Top 30 in Asia.
- VP, Commerce Finance & Strategy role oversees five areas: Advertising, Partnerships, Pricing & Plans, Payments, and Revenue Forecast & Analytics.

**Confirmed PSPs and Payment Partners:**
- **Adyen**: Primary global card acquirer/processor. Confirmed via multiple sources including Quartz, FinTech Magazine, and Adyen investor materials listing Netflix as a key merchant. Adyen's single-platform, multi-channel processing aligns with Netflix's global recurring billing model.
- **dLocal**: Cross-border processor for LATAM and emerging markets. dLocal confirmed Netflix as a client, handling $2B+ in cross-border payments (2019 data) alongside Amazon, Uber, and DiDi. Enables local currency processing in 40+ emerging markets.
- **Bango**: Carrier billing enablement. Confirmed partnership for Mexico (launched 2018, 12M+ mobile subscribers). Also expanded carrier billing across LATAM in 2024.
- **DOCOMO Digital**: Carrier billing partner for Asia. Confirmed partnership with TrueMove H in Thailand enabling Netflix carrier billing.
- **PayPal**: Accepted as a payment method globally.
- **Carrier billing partners by market**: Claro and Movistar (Colombia), SoftBank (Japan), TrueMove H via DOCOMO Digital (Thailand), ChungHwa Telecom (Taiwan).

**Payment Infrastructure (from Netflix TechBlog and Banking Exchange):**
- Netflix built proprietary dynamic routing: "recommend dynamic routing of transactions to maximize approval rates"
- Processes "over 1 billion payment transactions annually"
- "Tens of millions of customers renewing every month"
- "A small basis point change in approval rates is enough to move the needle"
- Uses MySQL for billing transactions, subscriptions, taxes, and revenue
- Uses CockroachDB for multi-region active-active architecture
- ML observability framework to "understand how they route billions of dollars of transactions in hundreds of countries every year"
- Payments analytics stack: Pig, Hive, Presto, Spark, Tableau, Python, JavaScript
- "Integrates with many global partners and local payment processors in different regions"
- Reconciles "non-uniform settlement data with each payment processor"
- Fraud detection uses "data science techniques to detect anomalies and fraud"
- Runs A/B tests on payment methods and flows

**Top 10 Markets by Subscribers:**

| Rank | Country | Subscribers (Est.) | Key Local APMs Missing |
|------|---------|-------------------|----------------------|
| 1 | United States | 81.4M | Cash App Pay |
| 2 | United Kingdom | 18.4M | Open Banking |
| 3 | Brazil | 16.6M | Pix, Boleto (partial) |
| 4 | Germany | 16.6M | Direct Debit (offered), Giropay |
| 5 | France | 13.6M | Carte Bancaire routing |
| 6 | India | 12.4M | UPI (offered), Paytm, PhonePe |
| 7 | Mexico | ~10M | OXXO (offered), SPEI |
| 8 | Japan | 9M | Konbini, PayPay (partial) |
| 9 | South Korea | ~8M | KakaoPay, Toss |
| 10 | Canada | 8.2M | Interac |

**Confirmed Payment Methods by Region:**

GLOBAL: Visa, Mastercard, Amex, Diners (credit and debit)
GLOBAL: PayPal, Netflix Gift Cards, Prepaid Cards
INDIA: UPI AutoPay (Netflix was FIRST merchant to launch UPI autopay)
MEXICO: OXXO Pay (cash payment at convenience stores)
COLOMBIA: Efecty (cash payment), Claro carrier billing, Movistar carrier billing
GERMANY: SEPA Direct Debit
INDONESIA: GoPay digital wallet
THAILAND: Carrier billing via TrueMove H / DOCOMO Digital
JAPAN: SoftBank carrier billing
TAIWAN: ChungHwa Telecom carrier billing

**Gap Analysis: Missing APMs by Market (Yuno Opportunity)**

| Market | Available | MISSING (Yuno Can Activate) |
|--------|-----------|----------------------------|
| Brazil (16.6M subs) | Cards, PayPal, Gift Cards | Pix (70%+ of digital payments), Boleto full support |
| Japan (9M subs) | Cards, SoftBank DCB | Konbini, PayPay, LINE Pay, Rakuten Pay |
| South Korea (~8M subs) | Cards, DCB | KakaoPay, Toss, PAYCO, Naver Pay |
| Philippines | Cards | GCash (60M+ users), Maya, GrabPay |
| Poland | Cards | BLIK (80%+ online payments) |
| Colombia | Cards, Efecty, Claro/Movistar | Nequi, PSE, Daviplata |
| Peru | Cards | Yape, PagoEfectivo, BCP |
| Vietnam | Cards | MoMo, ZaloPay |
| Nigeria | Cards | OPay, Paystack, bank transfers |
| Turkey | Cards | Papara, Param, local debit |

**Payment Complaints and Pain Points:**

1. **"Card not supported in this territory" errors**: Netflix's help center has a dedicated article for this error. Cross-border card declines are frequent in emerging markets where local banks block international recurring charges.

2. **Double/unauthorized charges**: 24,500+ reviews on PissedConsumer. Complaints about being charged after cancellation, double billing during plan changes, and authorization holds.

3. **Involuntary churn from payment failures**: Industry data shows 30-40% of credit cards used for subscriptions become unviable within a year. 16% of subscribers accidentally lose access because they forgot to update payment details. Netflix's 2% monthly churn rate (industry leading) still means ~6.5M subscribers churning monthly.

4. **Cross-border billing discrepancies**: Users report being charged at higher rates when traveling, with Netflix not adjusting pricing to match service region.

5. **Settlement complexity**: Netflix engineering team explicitly notes "non-uniformity of settlement data with each payment processor" as an operational challenge.

**Corporate Developments:**

| Date | Development | Category |
|------|-------------|----------|
| 2025 | Revenue hits $45.18B (+15.84% YoY) | Financial |
| 2025 | 325M+ global subscribers | Growth |
| 2025 | Ad tier reaches 94M MAU | Ad business |
| 2026 | $72B WBD acquisition announced | M&A |
| 2025 | Password crackdown completed globally | Monetization |
| 2024 | Ad revenue doubled; projected to double again 2025 | Revenue |
| 2025 | Stopped reporting subscriber numbers quarterly | Strategy |
| 2022 | 16 new payment partners added (APAC focus) | Payments |

**Key Meeting Angles:**

1. **Internal routing ceiling**: Netflix built proprietary dynamic routing but integrates with "many global partners and local payment processors." They know routing matters. Yuno's Smart Routing offers incremental gains on top of their internal logic without replacing their billing system. InDrive reference: 90% approval, 4.5% transaction recovery.

2. **Involuntary churn at scale**: With 325M subscribers, even marginal improvement in retry/failover saves millions of accounts. Yuno's 50% transaction recovery on soft declines directly addresses their "small basis point change moves the needle" philosophy. Livelo reference: +5% approval in under 3 months.

3. **APM gaps in growth markets**: Netflix is aggressively localizing content (Korean, Japanese, Indian content) but payment localization lags. Brazil has 16.6M subs but no Pix. Japan has 9M subs but no Konbini. Yuno activates 1,000+ APMs through one API. McDonald's reference: local APMs across 15+ LATAM markets.

4. **Settlement reconciliation pain**: Netflix explicitly describes fragmented settlement data as an operational burden. Yuno's unified dashboard consolidates all processor data. NOVA reduces false positives by 75%. Rappi reference: anomaly detection from minutes to milliseconds.

5. **WBD acquisition complexity**: A $72B merger with WBD means integrating another massive payment stack. Yuno's orchestration layer can unify multiple legacy billing systems under one API.

6. **Payments leadership background**: Kristen Morrow-Greven (ex-PayPal, ex-Fed), Ebi Atawodi (ex-Uber Payments), Gunjan Pradhan (ex-PayU India) all come from payment innovation backgrounds. They understand orchestration value.

**Sources:**

- [J.P. Morgan Q&A with Netflix Head of Global Payments](https://www.jpmorgan.com/payments/payments-unbound/volume-3/talking-with-netflix-global-head-payments)
- [Netflix TechBlog: Billing & Payments Engineering](https://netflixtechblog.com/billing-payments-engineering-meetup-ii-3bec782b3059)
- [Payments @ Netflix (Banking Exchange)](https://www.bankingexchange.com/recent-articles/item/6570-payments-netflix)
- [Netflix TechBlog: ML Observability for Payments](https://netflixtechblog.com/ml-observability-bring-transparency-to-payments-and-beyond-33073e260a38)
- [Netflix: Beyond Cards (APAC payments strategy)](https://about.netflix.com/en/news/alternative-methods-of-payment-apac)
- [Netflix Help Center: How to Pay](https://help.netflix.com/en/node/116380)
- [Netflix Help Center: OXXO Pay](https://help.netflix.com/en/node/121680)
- [Netflix Help Center: UPI AutoPay](https://help.netflix.com/en/node/134188)
- [Netflix Help Center: Card Not Supported](https://help.netflix.com/en/node/100351)
- [Adyen/Netflix: Quartz coverage](https://qz.com/1366219/a-dutch-firm-that-handles-payments-for-netflix-and-spofity-is-one-of-the-markets-hottest-stocks)
- [dLocal/Netflix: Wikitia](https://wikitia.com/wiki/DLocal)
- [Bango/Netflix Mexico: BusinessWire](https://www.businesswire.com/news/home/20180108005975/en/Bango-Brings-Carrier-Billing-to-Netflix-Subscribers-in-Mexico)
- [DOCOMO Digital/Netflix Thailand: Cision](https://news.cision.com/docomo-digital-ltd-/r/truemove-h-and-docomo-digital-partner-to-enable-carrier-billing-for-netflix-in-thailand,c3234301)
- [Netflix Ebi Atawodi: FinTech Futures](https://www.fintechfutures.com/paytech/netflix-bags-uber-s-product-head-ebi-atawodi-as-payments-director)
- [Netflix Gunjan Pradhan: Money20/20 Asia](https://asia.money2020.com/interview-gunjan-pradhan-netflix/)
- [Netflix Subscribers by Country: World Population Review](https://worldpopulationreview.com/country-rankings/netflix-users-by-country)
- [Netflix Revenue: Business of Apps](https://www.businessofapps.com/data/netflix-statistics/)
- [Netflix Brand Assets](https://brand.netflix.com/en/assets/logos/)
- [Netflix PissedConsumer Reviews](https://netflix.pissedconsumer.com/review.html)
- [Churn Rates for Streaming: Churnkey](https://churnkey.co/blog/churn-rates-for-streaming-services/)
- [Netflix Password Crackdown: CNN](https://www.cnn.com/2024/04/18/business/netflix-earnings-first-quarter)
- [Netflix Ad Tier Growth: StreamTV Insider](https://www.streamtvinsider.com/video/netflix-us-password-sharing-crackdown-catalyzes-ad-tier-growth-could-net-11b-2024)
- [Netflix SEC Filings](https://ir.netflix.net/financials/sec-filings/default.aspx)
- [Netflix Diversifies Payments: Advanced Television](https://www.advanced-television.com/2022/06/28/netflix-diversifies-payment-methods/)
- [Kristen Morrow-Greven: The Org](https://theorg.com/org/netflix/org-chart/kristen-morrow-greven)
