# ASANA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Asana
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/3/3b/Asana_logo.svg
Nombre merchant: Asana

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Upgrade Block
Tittle_Pain Point_2: Cross-Border Card Decline
Tittle_Pain Point_3: Single-Processor Stack
Tittle_Pain Point_4: No Smart Retry Logic
Tittle_Pain Point_5: Enterprise Invoice Drag

Desc_Pain Point_1: Self-serve plans accept only credit cards. No PayPal, iDEAL, or Pix. Forum users report three different cards declined on upgrade. 75K+ customers in 195 countries.
Desc_Pain Point_2: Emerging market users report cards rejected on upgrade. Forum: "three cards not accepted" with bank needing verification. Cross-border auth failures block 39% international revenue.
Desc_Pain Point_3: Zuora + Stripe is the sole processing path. No Adyen, Braintree, or alternative acquirer. Zero failover if Stripe declines. One processor for $791M trailing revenue.
Desc_Pain Point_4: Failed subscription payments lack intelligent retry across processors. No cascade on decline. Involuntary churn hits hardest in international markets with lower auth rates.
Desc_Pain Point_5: 683 enterprise customers at $100K+ ARR rely on manual invoicing with no self-serve wire, SEPA DD, or local bank transfer options. Slows deal velocity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (payment processing via Zuora)
PSP_2: Zuora (subscription management)
PSP_3: Avalara (automated sales tax)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: GiroPay
Local_M_8: Bancontact
Local_M_9: SPEI
Local_M_10: KakaoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $791M trailing revenue, 75K+ customers across 195 countries, and 39% international revenue, routing each payment to the best acquirer per market delivers 3-10% auth uplift on global subscriptions.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a subscription renewal. Instead of losing the subscriber to involuntary churn, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions turns payment failures into retained ARR.
Desc_Yuno_Cap3: Activates methods Asana's global base demands: PayPal, iDEAL in Netherlands, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, SPEI in Mexico, KakaoPay in South Korea. One API, 1,000+ methods. No per-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying Stripe processing, Zuora subscription management, and Avalara tax compliance. Real-time approval monitoring per country, centralized reconciliation, and NOVA fraud detection (75% reduction) protecting 75K+ paying organizations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Asana at a glance:**
- Founded: 2008 by Dustin Moskovitz and Justin Rosenstein. HQ: San Francisco, California
- Public: NYSE: ASAN
- Revenue: $791M trailing 12 months (ending January 31, 2026); FY2025 revenue $756.4M
- Market cap: ~$1.49B (March 2026)
- Customers: 75,000+ paying organizations
- Core customers ($5K+ annual): 25,413 (Q3 FY2026, +8% YoY)
- Enterprise customers ($100K+ annual): 683 (+18% YoY)
- Fortune 500 adoption: 73% of Fortune 500, 80% of Fortune 100
- US revenue: 61% of total; International revenue: 39%
- Employees: ~3,914 total (312 engineering, 159 sales, 60 marketing)
- Global offices: 13 offices worldwide, including Warsaw, Poland (6th EMEA office)
- Notable customers: Google, Disney, Uber, Pinterest, Airbnb, LinkedIn, Lyft, Adidas, Salesforce, NASA, Dropbox, Standard Chartered Bank
- Revenue model: Personal (Free), Starter ($10.99/user/mo annual), Advanced ($24.99/user/mo annual), Enterprise (custom), Enterprise+ (custom)

**Confirmed Payment Stack:**
- Stripe: Primary payment processor for card billing
- Zuora: Subscription management platform
- Avalara: Automated sales tax compliance
- Credit/debit cards: Primary accepted method
- Manually invoiced Enterprise accounts can add payment methods for recurring billing
- No PayPal accepted
- No local APMs detected
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Community Evidence):**
- Forum user: "three different credit cards not accepted" when upgrading to Business Plan
- Bank "needs further" verification message blocks cross-border upgrades
- Users unable to add billing details despite wanting to pay
- Multiple forum threads about billing support being unresponsive
- Users report automatic upgrades and charges after trial periods without confirmation
- No evidence of local payment methods beyond standard cards
- Enterprise invoicing requires sales-assisted manual workflows

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (61% of revenue, largest market)
  Accepted: Visa/MC/Amex (via Stripe)
  Missing: PayPal, Apple Pay, Google Pay, ACH direct debit
  Note: Dominant market, but no payment diversity. Single processor for majority of revenue.

MARKET 2: Europe / EMEA (6 offices, significant presence)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: iDEAL (Netherlands), GiroPay (Germany), SEPA DD, Bancontact (Belgium), BLIK (Poland), Sofort
  Note: Warsaw office opened 2024 signaling EMEA growth push. Local methods critical for SMB adoption.

MARKET 3: Brazil / LATAM (growing SaaS market)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of digital payments in Brazil. Card-only checkout blocks LATAM growth.

MARKET 4: India / South Asia (large enterprise customer base)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of digital payments in India. Standard Chartered is a customer, showing India enterprise presence.

MARKET 5: Japan / APAC (enterprise workflow market)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay
  Note: APAC project management market growing rapidly. Local methods critical for mid-market conversions.

**Key meeting angles:**
1. **$791M revenue with single processor** | Stripe is the only payment path for 75K+ customers across 195 countries. Zero failover capability.
2. **39% international revenue growing faster** | International revenue at $80.4M/quarter with no local payment methods to support conversion
3. **Fortune 100 penetration (80%)** | 683 enterprise customers at $100K+ ARR each. Invoice optimization accelerates cash flow.
4. **Card decline community evidence** | Forum threads document users unable to upgrade with multiple cards. Direct revenue loss.
5. **Zuora + Stripe stack lacks orchestration** | Subscription management exists but no intelligent routing or multi-processor failover
6. **Core customer growth (+8% YoY)** | 25K+ core customers spending $5K+. Every auth improvement drives retention.
7. **Competitor pressure** | Monday.com, Smartsheet, and ClickUp offer broader global payment options

**Sources:**
- [Asana: Payment Methods and Invoices](https://help.asana.com/s/article/payment-methods-and-invoices)
- [Asana: Billing Help](https://help.asana.com/s/article/billing)
- [Asana: Add Payment Method (Invoiced Customers)](https://asana.com/guide/help/faq/add-payment-method)
- [Asana: Pricing](https://asana.com/pricing)
- [Asana Forum: Credit Card Payment Not Possible](https://forum.asana.com/t/credit-card-payment-not-possible/113492)
- [Asana Forum: Unable to Add Billing Details](https://forum.asana.com/t/unable-to-add-billing-details/973988)
- [Asana Forum: Billing Issues from Asana](https://forum.asana.com/t/billing-issues-from-asana/1025569)
- [Asana: Q3 FY2026 Results](https://investors.asana.com/news-releases/news-release-details/asana-announces-third-quarter-fiscal-2026-results)
- [Asana: Q1 FY2026 Results](https://investors.asana.com/news-releases/news-release-details/asana-announces-first-quarter-fiscal-2026-results)
- [MacroTrends: Asana Revenue](https://www.macrotrends.net/stocks/charts/ASAN/asana/revenue)
- [Getlatka: Asana Revenue](https://getlatka.com/companies/asana)
- [Asana: Customers Page](https://asana.com/customers)
- [ElectroIQ: Asana Statistics](https://electroiq.com/stats/asana-statistics/)
- [Efficient.app: Asana Software Stack](https://efficient.app/stacks/asana)
- [Brandfetch: Asana Logo](https://brandfetch.com/asana.com)
