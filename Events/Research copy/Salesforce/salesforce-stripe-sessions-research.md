# SALESFORCE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Salesforce
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id7Kew_cTi/idYmRkLckn.svg
Nombre merchant: Salesforce

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Sprawl
Tittle_Pain Point_2: Commerce Cloud Geo Gaps
Tittle_Pain Point_3: Renewal Payment Failures
Tittle_Pain Point_4: AppExchange Middleware Tax
Tittle_Pain Point_5: Fraud Across Clouds

Desc_Pain Point_1: Stripe, Adyen, Cybersource, Braintree, and PayTrace each run independently via AppExchange. Own API, reporting, reconciliation. No unified routing layer for $41.5B.
Desc_Pain Point_2: Salesforce Payments is geo-restricted. Merchants in LATAM, Africa, and APAC cannot activate native checkout. Pix, UPI, M-Pesa require custom integrations.
Desc_Pain Point_3: 40% of subscription churn is from failed payments. Billing retries on a schedule with no real-time cascade. Expired cards leak 4-10% of ARR annually.
Desc_Pain Point_4: Third-party apps (Chargent, Breadwinner, Asperato) needed for extra gateways. Each adds cost, maintenance, and a failure point between checkout and settlement.
Desc_Pain Point_5: B2C Commerce, B2B Commerce, Order Management, and Agentforce process payments independently. No single fraud engine spans every cloud for 150K+ customers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Salesforce Payments, native)
PSP_2: Adyen (BYOP native integration, 2026)
PSP_3: Cybersource (AppExchange cartridge)
PSP_4: Braintree (AppExchange cartridge)
PSP_5: PayTrace (AppExchange cartridge)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: M-Pesa
Local_M_4: SPEI
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: PromptPay
Local_M_8: GCash
Local_M_9: KakaoPay
Local_M_10: Dana

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, geography, and processor cost across Stripe, Adyen, Cybersource, and Braintree simultaneously. With $41.5B revenue and 150K+ customers across every continent, routing to the best acquirer per market delivers 3-10% auth uplift at scale.
Desc_Yuno_Cap2: Automatic cascade when the primary PSP declines a Commerce Cloud or Billing transaction. Instead of scheduled retries hours later, Yuno retries through the next best processor in milliseconds. Up to 50% recovery turns involuntary churn into retained revenue.
Desc_Yuno_Cap3: Activates local methods across every Salesforce Cloud: Pix in Brazil, UPI in India, SPEI in Mexico, M-Pesa in Kenya, BLIK in Poland, PromptPay in Thailand, GCash in Philippines, KakaoPay in Korea. One API, 1,000+ methods. No per-market cartridge builds.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Adyen, Cybersource, Braintree, and PayTrace across B2C, B2B Commerce, and Order Management. Real-time approval monitoring, centralized reconciliation, and NOVA fraud detection (75% reduction) spanning every Salesforce cloud.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Salesforce at a glance:**
- Founded: 1999 by Marc Benioff. HQ: San Francisco, California
- Public: NYSE: CRM
- Revenue: $41.525B (FY ending Jan 31, 2026), up 9.58% YoY. FY30 target: $60B+
- Market cap: ~$250B (2025)
- Customers: 150,000+ (90% of Fortune 500)
- Employees: ~73,000
- Products: Sales Cloud, Service Cloud, Marketing Cloud, Commerce Cloud, Data Cloud, MuleSoft, Tableau, Slack, Agentforce
- Data Cloud & AI ARR: $1.2B (Q2 FY2026), up 120% YoY
- Agentforce ARR: $500M+ (Q3 FY2026), up 330% YoY
- Total Agentforce + Data 360 ARR: ~$1.4B
- FY26-FY30 revenue CAGR target: 10% organic
- Key acquisitions: Slack ($27.7B), Tableau ($15.7B), MuleSoft ($6.5B), Informatica (2025)
- Commerce Cloud: Powers B2C storefronts for major retailers and brands globally
- Salesforce Billing: CPQ-to-cash for subscription, usage, and one-time billing

**Confirmed Payment Stack:**
- Salesforce Payments: Native, powered by Stripe as the payment gateway and merchant account
- Adyen: Native BYOP (Bring Your Own Payments) integration, generally available 2026. Merchants keep existing Adyen accounts and rates
- Cybersource: AppExchange cartridge for Commerce Cloud
- Braintree: AppExchange cartridge for Commerce Cloud
- PayTrace: AppExchange cartridge
- Chargent: Third-party app for credit card, ACH, and subscription billing
- Breadwinner: Third-party integration syncing Stripe, Square, and Braintree
- Asperato: Multi-provider connector (Stripe, PayPal, GoCardless)
- ACH, SEPA DD, BACS: Supported via Stripe/Adyen layer
- Apple Pay, Google Pay: Via Stripe/Adyen
- PayPal: Via Braintree or third-party apps
- No single payment orchestrator unifying all processors

**Payment Method Gaps (Evidence):**
- Salesforce Payments has geographic restrictions; not available in all markets
- Commerce Cloud checkout requires cartridge/plugin per PSP, creating fragmentation
- Each PSP integration is independent: separate reporting, separate reconciliation
- "Payment Zones" in Adyen BYOP help, but only cover Adyen-specific routing
- No cross-PSP smart routing or failover between Stripe and Adyen
- Local APMs in emerging markets (Pix, UPI, M-Pesa, SPEI) require custom integrations
- B2B Commerce has more limited payment gateway options than B2C
- 58.5% of enterprises operate with fragmented payment setups (industry data)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (HQ market, majority of revenue)
  Accepted: Visa/MC/Amex, ACH, Apple Pay, Google Pay, PayPal (via Braintree)
  Missing: Venmo (direct), Cash App Pay
  Note: Best coverage, but multi-PSP reconciliation across clouds is fragmented

MARKET 2: Europe (major enterprise market)
  Accepted: Visa/MC, SEPA DD, BACS, iDEAL (via Adyen), Bancontact (via Adyen)
  Missing: BLIK (Poland), GiroPay (Germany, ending but still relevant), MB Way (Portugal)
  Note: Adyen BYOP improves EU coverage but doesn't unify with Stripe transactions

MARKET 3: Latin America (growing Commerce Cloud adoption)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE, Nequi
  Note: Pix processes 70%+ of Brazilian digital payments. Commerce Cloud merchants lose conversions without it.

MARKET 4: Asia Pacific (enterprise CRM dominance)
  Accepted: Visa/MC, Alipay/WeChat (via Adyen in select markets)
  Missing: UPI, KakaoPay, LINE Pay, PromptPay, GrabPay, Dana, GCash
  Note: UPI handles 75%+ of Indian digital payments. SEA methods critical for Commerce Cloud.

MARKET 5: Africa / Middle East (emerging market)
  Accepted: Visa/MC (cross-border)
  Missing: M-Pesa, Fawry, STC Pay, mada, MTN Mobile Money
  Note: Mobile money dominates Sub-Saharan Africa. No native support in Salesforce Payments.

**Key meeting angles:**
1. **$41.5B revenue, fragmented payment stack** | Stripe, Adyen, Cybersource, Braintree, and PayTrace all run independently with no unified orchestration
2. **150K+ customers across every continent** | 90% of Fortune 500 use Salesforce but payment method coverage varies wildly by cloud and region
3. **Multi-cloud payment silos** | B2C Commerce, B2B Commerce, Order Management, and Billing each have separate payment configurations
4. **Subscription churn from failed payments** | 40% of subscription churn is involuntary. Scheduled retries lack real-time cascade to alternative processors
5. **Adyen BYOP is a step, not the solution** | Native integration with Adyen is welcome, but still doesn't orchestrate across Stripe + Adyen + others
6. **AppExchange middleware adds cost and risk** | Each third-party payment app (Chargent, Breadwinner, Asperato) is another failure point and fee layer
7. **Emerging market blind spot** | Pix, UPI, M-Pesa, SPEI absent from native Salesforce Payments. Commerce Cloud merchants lose conversions in highest-growth geographies

**Sources:**
- [Salesforce: Payments Processing for Commerce](https://help.salesforce.com/s/articleView?id=commerce.payments_commerce_integrations.htm&language=en_US&type=5)
- [Salesforce: Commerce Payment Gateway Options](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-payment-gateway-options.html)
- [Salesforce: Native Adyen Integration Blog](https://www.salesforce.com/blog/salesforce-native-integration-adyen/?bc=OTH)
- [Salesforce: Add Adyen as Payments Option (26.1)](https://help.salesforce.com/s/articleView?id=commerce.b2c_rn_26_1_adyen.htm&language=en_US&type=5)
- [Salesforce: Billing Processing Payments](https://help.salesforce.com/s/articleView?id=sales.blng_processing_payments.htm&language=en_US&type=5)
- [Salesforce: Billing Payment Methods](https://help.salesforce.com/s/articleView?id=sales.blng_payment_methods.htm&language=en_US&type=5)
- [Salesforce: Billing Troubleshooting](https://help.salesforce.com/s/articleView?id=000394340&language=en_US&type=1)
- [Salesforce AppExchange: Commerce Cloud Payments](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N4V00000H0jIVUAZ)
- [Salesforce AppExchange: Chargent](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N300000016jrcEAA)
- [Salesforce AppExchange: Adyen B2C Commerce](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FMdTNUA1)
- [Salesforce Developer: B2C Commerce PSP](https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-csc-psp.html)
- [Stripe: Salesforce Platform App Docs](https://stripe.com/docs/billing/integrations/salesforce)
- [Adyen: Salesforce Commerce Cloud Docs](https://docs.adyen.com/plugins/salesforce-commerce-cloud)
- [Adyen: Supported Payment Methods for SFCC](https://docs.adyen.com/plugins/salesforce-commerce-cloud/supported-payment-methods)
- [Salesforce: FY30 Revenue Target $60B+](https://investor.salesforce.com/news/news-details/2025/Salesforce-Announces-New-FY30-Revenue-Target-of-60B-10-Organic-FY26-FY30-CAGR/default.aspx)
- [MacroTrends: Salesforce Revenue](https://www.macrotrends.net/stocks/charts/CRM/salesforce/revenue)
- [Salesforce Ben: Ultimate Guide to Salesforce Payments](https://www.salesforceben.com/the-ultimate-guide-to-salesforce-payments/)
- [EBizCharge: Salesforce Subscription Billing](https://ebizcharge.com/blog/salesforce-subscription-billing-automating-recurring-payments/)
- [AppFrontier: Reduce Churn in Recurring Billing](https://appfrontier.com/blog/reduce-churn-in-recurring-billing-salesforce)
- [Brandfetch: Salesforce Logo](https://brandfetch.com/salesforce.com)
