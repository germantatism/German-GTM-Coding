# GODADDY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: GoDaddy
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/6/6e/GoDaddy_logo.svg
Nombre merchant: GoDaddy

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US/CA Only Payments
Tittle_Pain Point_2: Zero LATAM/APAC APMs
Tittle_Pain Point_3: No Multi-Acquirer Failover
Tittle_Pain Point_4: International Card Blocks
Tittle_Pain Point_5: Renewal Churn at Scale

Desc_Pain Point_1: GoDaddy Payments is available only in the US and Canada. The remaining 32.6% of revenue ($1.6B) from 200+ international markets has no native payment solution. Merchants outside North America depend entirely on third-party integrations like Stripe or PayPal.
Desc_Pain Point_2: 20.4M customers across 200+ markets, but no Pix, no UPI, no OXXO, no M-Pesa, no BLIK. Only GCash in Philippines is offered as a regional method. India, Brazil, Mexico, Colombia, and Africa have zero local coverage despite being high-growth regions.
Desc_Pain Point_3: GoDaddy Payments and Stripe operate as separate, disconnected processors. When one declines, there is no automatic cascade to the other. Each failed transaction is a lost merchant sale and platform fee with no recovery path.
Desc_Pain Point_4: International customers report card declines due to billing address mismatches, cross-border flags, and regional card restrictions. GoDaddy has a documented history of processing issues with cards from certain geographic areas.
Desc_Pain Point_5: 20.4M customers with 85% retention, but 15% annual churn on a $4.95B revenue base means $740M+ at risk. Failed card renewals for domains, hosting, and subscriptions directly erode the recurring revenue engine that drives GoDaddy's business model.

SLIDE 1: PSP TOPOLOGY

PSP_1: GoDaddy Payments (US/CA)
PSP_2: Stripe
PSP_3: PayPal
PSP_4: Square

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: M-Pesa
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: PSE
Local_M_8: SPEI
Local_M_9: Nequi
Local_M_10: SEPA Direct Debit

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across GoDaddy Payments, Stripe, PayPal, and Square based on BIN, issuer, currency, and geography. With $4.95B in revenue, 20.4M customers, and 81M domains under management, even a 3% auth uplift on renewals recovers over $100M in annual revenue currently lost to silent declines.
Desc_Yuno_Cap2: Automatic cascade when one processor declines. Yuno reroutes to the next best acquirer in milliseconds, turning failed domain renewals, hosting payments, and merchant checkouts into recovered revenue. Up to 50% recovery on soft declines, directly reducing the 15% churn rate that costs GoDaddy $740M+ annually.
Desc_Yuno_Cap3: Activates APMs for GoDaddy's 200+ markets: Pix in Brazil, UPI in India, OXXO and SPEI in Mexico, PSE and Nequi in Colombia, M-Pesa in Kenya, BLIK in Poland, SEPA DD in Europe. One API, 1,000+ payment methods. No per-market engineering sprints for the world's largest domain registrar.
Desc_Yuno_Cap4: One dashboard replacing GoDaddy's fragmented Payments + Stripe + PayPal + Square settlement streams. Real-time approval rate monitoring, centralized reconciliation for domain, hosting, commerce, and subscription revenue across 200+ markets, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GoDaddy at a glance:**
- 20.4M customers, 81M domains under management (~21% global market share), 200+ markets
- Revenue: $4.95B (FY2025), up 8.3% YoY. Total bookings: $5.4B (up 7.2%)
- 2026 guidance: $5.195B to $5.275B revenue (~6% growth)
- Applications & Commerce segment: $1.89B (38.2%), up 14.3% YoY (highest growth segment)
- Core Platform (domains, hosting): $3.06B (61.8%)
- US revenue: 67.4% ($3.34B). International: 32.6% ($1.61B)
- Customer retention: ~85% overall, ~90% for 3+ year customers
- Public company (NYSE: GDDY). Market cap ~$25B+

**Confirmed PSPs:**
- GoDaddy Payments: native processor (US and Canada only). Cards, ACH, Apple Pay, Google Pay
- Stripe: third-party integration for WordPress Managed Ecommerce and Websites + Marketing
- PayPal: available globally
- Square: available for POS and online
- Authorize.Net: legacy integration
- 2Checkout: available for MENA region (71 countries)
- No payment orchestrator detected

**Payment Methods Currently Accepted (Platform Billing):**
- Cards: Visa, Mastercard, Amex, Discover, JCB, Diners Club, UnionPay
- Wallets: PayPal, Apple Pay, Google Pay
- BNPL: Klarna (select regions)
- Bank: ACH (US only)
- Regional: GCash (Philippines), 2Checkout (MENA)
- In-person: POS via GoDaddy Payments, Tap to Pay on mobile

**GoDaddy Payments Availability:**
- United States and Canada ONLY
- Not available in any other country
- Merchants outside US/CA must use Stripe, PayPal, or Square

**Top Markets:**
- United States: 70.4% of DNS customers (121,263 companies), 67.4% of revenue
- United Kingdom: 8.4% of DNS customers
- Canada: 5.5% of DNS customers
- India: major traffic source, growing market
- Germany, Australia, Brazil: significant customer bases
- International: 32.6% of revenue ($1.61B)

**Payment Issues Documented:**
- International customers frequently report card declines at checkout
- Billing address and postal code mismatches are the #1 cause of declined payments
- GoDaddy has "a history with issues processing cards from some geographic areas"
- Ad-blockers interfere with captcha during payment method addition
- Currency not set in account prevents payment processing
- Forum complaints about inability to process payments from India, Philippines, Middle East

**Key Meeting Angles:**
1. **Domain renewal economics**: 81M domains renew annually. Each failed renewal is permanently lost revenue. Multi-acquirer failover protects the entire portfolio
2. **Commerce is the growth engine**: Apps & Commerce grew 14.3% vs. 4.9% for Core. Better payment conversion accelerates the highest-growth segment
3. **International revenue gap**: 32.6% of revenue from 200+ markets, but GoDaddy Payments only covers 2 countries. Massive infrastructure mismatch
4. **India opportunity**: Major traffic source with zero local payment methods. UPI handles 75%+ of Indian digital payments
5. **Retention leverage**: 85% retention sounds good, but 15% churn on $4.95B = $740M+ annual risk. Reducing payment-driven churn by even 1 point is transformative
6. **Multi-processor unification**: GoDaddy already uses 4+ processors. Yuno orchestrates them under one layer, adding routing intelligence and failover
7. **LATAM web builder market**: Competing with Wix and Squarespace for international SMBs. Local APMs are table stakes

**Sources:**
- [GoDaddy: Payment Methods We Accept](https://www.godaddy.com/help/payment-methods-we-accept-for-purchases-8061)
- [GoDaddy: What Is GoDaddy Payments](https://www.godaddy.com/help/what-is-godaddy-payments-40505)
- [GoDaddy: Set Up Payment Methods for Online Store](https://www.godaddy.com/help/set-up-payment-for-my-online-store-23913)
- [GoDaddy: Switch to GoDaddy Payments](https://www.godaddy.com/help/switch-to-godaddy-payments-in-websites-marketing-41247)
- [GoDaddy: Why Is My Customer's Card Declined](https://www.godaddy.com/help/why-is-my-customers-credit-card-declined-40543)
- [GoDaddy: Troubleshoot Unable to Add Payment Method](https://www.godaddy.com/help/troubleshoot-unable-to-add-a-new-payment-method-40019)
- [GoDaddy: Integrated Stripe Payment Method](https://www.godaddy.com/help/what-is-the-integrated-stripe-payment-method-41338)
- [GoDaddy Investor Relations](https://aboutus.godaddy.net/investor-relations/financials/default.aspx)
- [GoDaddy 2024 Annual Report (PDF)](https://s23.q4cdn.com/406380394/files/doc_financials/2024/ar/GoDaddy-2024-Annual-Report.pdf)
- [MacroTrends: GoDaddy Revenue](https://www.macrotrends.net/stocks/charts/GDDY/godaddy/revenue)
- [Bullfincher: GoDaddy Revenue by Geography](https://bullfincher.io/companies/godaddy/revenue-by-geography)
- [6sense: GoDaddy DNS Market Share](https://6sense.com/tech/domain-name-services/godaddy-dns-market-share)
- [GoDaddy Blog: Domain Trends 2025](https://www.godaddy.com/resources/skills/domain-trends-at-godaddy)
- [FitSmallBusiness: GoDaddy Payments Review 2025](https://fitsmallbusiness.com/godaddy-payments-review/)
- [Wikimedia: GoDaddy Logo](https://commons.wikimedia.org/wiki/File:GoDaddy_logo.svg)
