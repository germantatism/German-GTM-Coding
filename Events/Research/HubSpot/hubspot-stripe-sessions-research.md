# HUBSPOT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: HubSpot
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idchmboHEZ/idVbvoR5JE.svg
Nombre merchant: HubSpot

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 3-Country Payment Lock
Tittle_Pain Point_2: No Auto Retry on Decline
Tittle_Pain Point_3: Single-Processor Stack
Tittle_Pain Point_4: Fraud Tools Lag Scale
Tittle_Pain Point_5: B2B Invoice Bottleneck

Desc_Pain Point_1: Payments only works in the US, UK, and Canada. 132+ other countries must use Stripe with a 0.5% surcharge, still lacking local methods like Pix or UPI.
Desc_Pain Point_2: Failed subscription payments are not retried automatically. Admins can manually retry up to 3 times only. Nearly half of SaaS churn comes from payment failures.
Desc_Pain Point_3: Commerce Hub connects to Stripe or HubSpot Payments only. No Adyen, Worldpay, or Braintree. Zero failover if Stripe declines. One processor for $3.1B revenue.
Desc_Pain Point_4: Built-in fraud detection covers basics but 228K+ customers across 135 countries need enterprise-grade AI fraud scoring, not CRM-level checks.
Desc_Pain Point_5: Enterprise invoices rely on manual payment collection. No wire, SEPA DD, or local transfers on invoices. Large deals stall on cross-border card payments.

SLIDE 1: PSP TOPOLOGY

PSP_1: HubSpot Payments (Stripe-powered, US/UK/Canada)
PSP_2: Stripe (international payment processing)
PSP_3: ACH / SEPA / BACS (bank debit, limited regions)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: iDEAL
Local_M_3: Boleto
Local_M_4: UPI
Local_M_5: SPEI
Local_M_6: BLIK
Local_M_7: Bancontact
Local_M_8: GiroPay
Local_M_9: KakaoPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and buyer geography. With $3.1B revenue, 228K+ customers across 135 countries, and 46% international revenue, routing each payment to the best acquirer per market delivers 3-10% auth uplift on global Commerce Hub transactions.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a Commerce Hub payment. Instead of requiring manual 3-attempt retries, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions turns involuntary churn into retained subscription revenue.
Desc_Yuno_Cap3: Activates methods HubSpot's global base demands: Pix in Brazil, iDEAL in Netherlands, SPEI in Mexico, UPI in India, BLIK in Poland, Bancontact in Belgium, KakaoPay in Korea, GrabPay in SEA. One API, 1,000+ methods. No per-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying HubSpot Payments, Stripe, ACH, SEPA, and BACS into a single view. Real-time approval monitoring per country, centralized reconciliation across Commerce Hub, and NOVA fraud detection (75% reduction) protecting 228K+ merchant accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**HubSpot at a glance:**
- Founded: 2006 by Brian Halligan and Dharmesh Shah. HQ: Cambridge, Massachusetts
- Public: NYSE: HUBS
- Revenue: $3.131B (FY2025), up 19.17% YoY. 2026 guidance: $3.69-3.70B
- Market cap: ~$37.75B (2025)
- Net New ARR: Grew 24% in 2025, expected to outpace revenue growth again in 2026
- Customers: 228,706+ in 135+ countries (Q4 2025), added 40,000+ net new customers in 2025
- International revenue: 46% of total revenue
- Employees: ~8,200+
- Cash: $1.8B in cash and marketable securities
- Free cash flow: ~$740M projected for 2026
- AI strategy: Breeze AI platform across all hubs, driving engagement and upsell
- Products: Marketing Hub, Sales Hub, Service Hub, CMS Hub, Operations Hub, Commerce Hub
- Notable customers: Siemens, FedEx, NVIDIA, KPMG, McKinsey, Novartis, DHL Express, Smartsheet, SurveyMonkey, WWF, Andela

**Confirmed Payment Stack:**
- HubSpot Payments: Native payment processing powered by Stripe, available only in US, UK, and Canada
- Stripe: Direct integration for international payment processing outside US/UK/Canada
- ACH: US bank debit for subscriptions and one-time payments
- SEPA Direct Debit: European bank debit (via Stripe)
- BACS Direct Debit: UK bank debit
- PADs: Canadian pre-authorized debits
- Apple Pay / Google Pay: Enabled automatically when card payments are accepted
- Credit/Debit cards: Visa, Mastercard, Amex, Discover, Diners Club, JCB
- No PayPal accepted natively
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Evidence):**
- HubSpot Payments is limited to US, UK, and Canada only
- International businesses must use Stripe with an additional 0.5% platform fee
- No local APMs: Pix, Boleto, iDEAL, BLIK, UPI, SPEI, Bancontact, GiroPay not supported
- No PayPal integration in Commerce Hub natively
- Community complaints about inability to re-run declined cards automatically
- Manual retry limited to 3 attempts only for subscription failures
- No automatic dunning or smart retry logic
- Users report "credit card limits hit at time of processing" with no fallback

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market, 54% of revenue)
  Accepted: Visa/MC/Amex/Discover, ACH, Apple Pay, Google Pay
  Missing: PayPal, Venmo (for SMB customers)
  Note: Most complete coverage, but no failover processor

MARKET 2: Europe (significant international revenue)
  Accepted: Visa/MC/Amex, SEPA DD, BACS (UK)
  Missing: iDEAL (Netherlands), GiroPay (Germany), Bancontact (Belgium), BLIK (Poland), Sofort, MB Way
  Note: SEPA DD available but limited. Many local methods missing.

MARKET 3: Latin America (growing SaaS market)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix handles 70%+ of digital payments in Brazil. Card-only blocks SMB adoption.

MARKET 4: Asia Pacific (expanding presence, Singapore office)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: UPI, Alipay, WeChat Pay, KakaoPay, GrabPay, LINE Pay, PromptPay
  Note: UPI handles 75%+ of India digital payments. Critical gap in SEA markets.

MARKET 5: Middle East / Africa (emerging growth)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: M-Pesa, Fawry, STC Pay, mada
  Note: Mobile money dominates Africa. Zero local method support.

**Key meeting angles:**
1. **$3.1B revenue with 3-country payment lock** | 46% of revenue is international but Commerce Hub payments restricted to US/UK/Canada
2. **No automatic retry = silent churn** | Community demands auto-retry; HubSpot caps at 3 manual attempts while half of SaaS churn is payment failures
3. **Single-processor dependency** | Stripe is the only processor for 228K+ customers. No failover, no routing optimization
4. **135 countries, minimal local methods** | Global CRM platform with card-only checkout in most markets
5. **Commerce Hub is young and growing** | Launched 2023, expanding rapidly. Payment orchestration layer would accelerate global rollout
6. **Enterprise invoice friction** | Large B2B deals require wire/local bank transfers not supported in Commerce Hub
7. **Competitor pressure** | Salesforce Commerce Cloud, Zoho, and standalone CPQ tools offer broader payment processor choice

**Sources:**
- [HubSpot: Set Up Payments](https://knowledge.hubspot.com/payment-processing/set-up-payments)
- [HubSpot: Payments FAQ](https://knowledge.hubspot.com/payment-processing/payments-frequently-asked-questions)
- [HubSpot: Connect Stripe](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot)
- [HubSpot: Commerce Hub](https://www.hubspot.com/products/commerce)
- [HubSpot: Payment Processing](https://www.hubspot.com/products/commerce/payments)
- [HubSpot: Update Failed Subscription Payments](https://knowledge.hubspot.com/subscriptions/update-payment-method-for-failed-subscription-payments)
- [HubSpot: Manage Payments](https://knowledge.hubspot.com/payments/manage-payments)
- [HubSpot: Currency Setup](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub)
- [HubSpot: Mitigate Fraud Risk](https://knowledge.hubspot.com/payments/mitigate-risk-with-payments)
- [HubSpot Community: Re-run Credit Card Request](https://community.hubspot.com/t5/HubSpot-Ideas/Need-the-ability-to-re-run-a-credit-card/idi-p/774922)
- [HubSpot Community: Payment Frustrations](https://community.hubspot.com/t5/Commerce-Tools/Seeking-Advice-Frustrations-with-HubSpot-Payments/m-p/1088438)
- [HubSpot Community: Commerce Hub 2025 Updates](https://community.hubspot.com/t5/Commerce-Product-Updates/Commerce-Hub-2025-Update-Roundup-Transforming-the-Way-You-Do/td-p/1232633)
- [HubSpot: Q4 2025 Results](https://ir.hubspot.com/news-releases/news-release-details/hubspot-reports-strong-q4-and-full-year-2025-results)
- [HubSpot: Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/HUBS/hubspot/revenue)
- [Sacra: HubSpot Revenue](https://getlatka.com/blog/hubspot-revenue/)
- [Brandfetch: HubSpot Logo](https://brandfetch.com/hubspot.net)
- [Stream Creative: HubSpot Payments 2025](https://www.streamcreative.com/blog/hubspot-payment-processing)
- [Shuttle Global: HubSpot Payment Links](https://www.shuttleglobal.com/blog/boosting-conversions-how-to-use-payment-links-in-hubspot/)
