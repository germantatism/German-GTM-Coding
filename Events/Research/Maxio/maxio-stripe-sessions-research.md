# MAXIO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Maxio
=======================================

Logo: https://companieslogo.com/img/orig/maxio.png
Nombre merchant: Maxio

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 4 Country Payment Limit
Tittle_Pain Point_2: Gateway Fragmentation
Tittle_Pain Point_3: Dunning Gaps Cause Churn
Tittle_Pain Point_4: No Cross Gateway Routing
Tittle_Pain Point_5: Limited Local APM Coverage

Desc_Pain Point_1: Maxio Payments is authorized in only 4 countries: US, Canada, UK, and Australia. Yet Maxio serves 2,000+ SaaS businesses worldwide processing $18B+ in billings. Customers in EU, LATAM, and APAC cannot use Maxio Payments and must rely on third party gateways with separate onboarding and reconciliation workflows.
Desc_Pain Point_2: Maxio integrates with 20+ payment gateways (Stripe, Adyen, Braintree, GoCardless, BlueSnap, Authorize.net, and 14 more). Each gateway requires separate configuration, monitoring, and reconciliation. SaaS businesses managing subscriptions across multiple gateways lack unified routing, reporting, and optimization across all processors.
Desc_Pain Point_3: Maxio offers customizable dunning with automated retries and reminder emails for failed payments. But retries occur within a single gateway. If Stripe declines a subscription renewal, the dunning sequence retries on Stripe only. No cascade to Adyen, Braintree, or an alternative acquirer to recover the payment.
Desc_Pain Point_4: Maxio lets SaaS businesses connect multiple gateways but does not route transactions intelligently between them. Each subscription is assigned to one gateway. No dynamic optimization based on approval rates, transaction costs, or processor health. B2B SaaS companies leave revenue on the table at $18B+ in billings.
Desc_Pain Point_5: Most Maxio gateway integrations focus on cards and ACH. BlueSnap adds some international methods. But no PIX for Brazilian SaaS buyers, no UPI for Indian teams, no BLIK for Polish companies, no iDEAL for Dutch procurement. B2B SaaS expansion into emerging markets faces checkout friction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Maxio Payments (US, CA, UK, AU) PSP_2: Stripe PSP_3: Adyen PSP_4: Braintree PSP_5: GoCardless PSP_6: 16 more gateways

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: UPI (India)
Local_M_3: BLIK (Poland)
Local_M_4: iDEAL (Netherlands)
Local_M_5: Bancontact (Belgium)
Local_M_6: SEPA Instant (EU)
Local_M_7: Boleto (Brazil)
Local_M_8: PayPay (Japan)
Local_M_9: KakaoPay (South Korea)
Local_M_10: MB Way (Portugal)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each B2B SaaS subscription renewal to the optimal gateway per card BIN, issuer, and market across Stripe, Adyen, Braintree, and all 20+ connected gateways. With $18B+ in billings under management, even a 0.5% auth improvement across the portfolio recovers meaningful revenue. Smart Routing boosts approval 3 to 10%.
Desc_Yuno_Cap2: When Stripe dunning fails after all retries, Yuno cascades the payment to Adyen, Braintree, or GoCardless before the subscription cancels. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this approach. Each recovered B2B subscription protects high value recurring contracts.
Desc_Yuno_Cap3: Extend Maxio beyond cards and ACH with PIX in Brazil, UPI in India, BLIK in Poland, iDEAL in Netherlands, and SEPA across EU. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months with Yuno. Maxio's 2,000+ SaaS clients could accept subscriptions from buyers in 50+ countries.
Desc_Yuno_Cap4: Replace 20+ siloed gateway dashboards with one real time view across Stripe, Adyen, Braintree, GoCardless, BlueSnap, and Maxio Payments. Monitor approval rates, dunning effectiveness, and churn recovery by gateway, region, and SaaS vertical. Millisecond anomaly detection catches gateway failures before they cascade into subscriber churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Maxio at a glance:**
- Founded: 2009 (as SaaSOptics). Merged with Chargify in April 2021 to form Maxio
- HQ: Peachtree Corners, Georgia, United States
- Funding: $150M+ growth equity led by Battery Ventures (April 2021). Total raised ~$169M
- Employees: ~235 (as of January 2026)
- Customers: 2,000+ B2B SaaS and subscription businesses worldwide
- Billings Under Management: $18B+
- ARR Under Management: $10B+ across customer base
- Investor Capital: $24B+ in investor capital across customer base
- Products: Subscription Billing, Revenue Recognition (ASC 606/IFRS 15), SaaS Metrics and Analytics, CPQ (via RevOps.io acquisition), Metering (usage based billing), Maxio Payments, MCP (AI for finance workflows)
- Key Partnerships: Rillet (AI finance), Sage Intacct (ERP), NetSuite (ERP), Adyen (global payments)
- Gateway Integrations: 20+ (Stripe, Adyen, Braintree, GoCardless, PayPal, BlueSnap, CSG Forte, Authorize.net, Cybersource, Elavon, Eway, ModusLink, Moneris, NMI, Pin Payments, Square, Stax, TrustCommerce, Windcave, Worldline, Worldpay)

**Confirmed PSPs and Payment Infrastructure:**
- Maxio Payments: In house payment processing. Authorized in US, Canada, UK, Australia only. Automated bank reconciliation, batch reporting, journal entries
- Stripe: Cards and ACH. Automatic card updater feature
- Adyen: International payment processing partner for Maxio Payments Global (launched May 2025)
- Braintree: Cards, PayPal, Apple Pay support
- GoCardless: Direct debit (recurring and one time)
- PayPal: Multiple payment methods through PayPal integration
- BlueSnap: Global currencies and alternative payment methods
- CSG Forte: Multiple payment types for scaling
- Authorize.net: Credit/debit cards and ACH
- Cybersource: Visa owned gateway
- Plus 11 more gateways (Elavon, Eway, ModusLink, Moneris, NMI, Pin Payments, Square, Stax, TrustCommerce, Windcave, Worldline/Worldpay)
- Multi currency support: 150+ currencies
- Payment methods: Cards, ACH, direct debit, PayPal, Apple Pay (via Braintree)

**Pricing Structure:**
- Build: Free (testing and integration sandbox)
- Grow: $599/month (up to $100K in monthly billings, core billing and reporting)
- Scale: Custom pricing (enterprise, multi entity, global compliance)
- Revenue Recognition: Optional module (ASC 606/IFRS 15)
- Default annual contracts. Premium options for monthly/quarterly billing

**Payment Issues and Incidents:**
- Dunning limited to single gateway: When a subscription payment fails, Maxio retries on the same gateway only. No cross gateway failover during dunning sequences
- Gateway fragmentation: 20+ gateways available but each configured in silo. No unified routing optimization. SaaS businesses manage each gateway independently
- Maxio Payments limited jurisdiction: Only US, CA, UK, AU. European SaaS customers (Germany, France, Netherlands, etc.) cannot use Maxio Payments
- Expired card churn: Maxio identifies expired cards as a major involuntary churn driver. Dunning automation helps but cannot cascade to an alternative processor when retries fail
- Multi gateway complexity: SaaS businesses using 3 to 5 gateways simultaneously face reconciliation overhead. Each gateway produces separate reports, settlement timelines, and dispute workflows

**Key meeting angles:**
1. **$18B+ in billings, no cross gateway routing** | Maxio connects to 20+ gateways but routes each subscription to a single gateway with no dynamic optimization. Yuno's Smart Routing directs each renewal to the optimal acquirer across all connected gateways, boosting approval rates 3 to 10% and recovering meaningful revenue from the $18B+ portfolio.
2. **Dunning retries on one gateway only** | Maxio's dunning automation retries failed payments on the same gateway (Stripe, Adyen, etc.) until the sequence ends. No cascade to an alternative processor. NOVA AI recovers up to 75% of soft declines by instantly routing to the next available acquirer. Each recovered B2B subscription protects high value annual contracts.
3. **4 country limit blocks global SaaS growth** | Maxio Payments operates in US, CA, UK, and AU only. Yet 2,000+ SaaS clients sell globally. Buyers in Brazil, India, Germany, and Japan need local payment methods. Yuno adds 1,000+ APMs across 50+ countries through one integration, complementing Maxio's existing 20+ gateway connections.
4. **2,000+ SaaS clients, one orchestration layer** | Every Maxio customer manages gateways independently. Yuno provides unified orchestration across Stripe, Adyen, Braintree, and all 20+ gateways with one dashboard. The value multiplies across 2,000+ SaaS businesses managing $18B+ in annual billings.
5. **Maxio Payments Global needs global APMs** | Maxio launched Payments Global with Adyen in May 2025 for multi currency processing. But multi currency cards are only part of global coverage. PIX in Brazil, UPI in India, iDEAL in Netherlands are not card based. Yuno extends Maxio's global ambitions with 1,000+ local methods alongside card processing.

**Maxio Leadership:**
- Branden Jenkins: CEO
- Tracy Kraft: CMO (appointed 2025)
- Jared Mackey: VP of Account Management (appointed 2025)
- Monica Lee: Head of Sales (appointed September 2025)
- No CFO or CTO publicly identified in recent sources

**Recent corporate developments:**
- September 2025: Product innovations and executive hires announced. Maxio CPQ (from RevOps.io acquisition), Maxio Metering, and Maxio MCP (AI for finance) launched
- May 2025: Maxio Payments Global launched in partnership with Adyen for international processing
- 2025: Partnerships with Rillet (AI finance) and Sage Intacct (ERP)
- April 2021: Battery Ventures led $150M+ growth equity investment. SaaSOptics and Chargify merged to form Maxio
- 2026: B2B Growth Report released analyzing $40B+ in billings data from 2,000+ companies
- Platform: $18B+ billings under management, 2,000+ customers, 150+ currencies

**Sources:**
- [Maxio Website (Maxio)](https://www.maxio.com/)
- [Maxio Payment Gateways (Maxio)](https://www.maxio.com/payment-gateways)
- [Maxio Payments Global (Maxio Blog)](https://www.maxio.com/blog/introducing-maxio-payments-global)
- [Maxio Payments Jurisdictions (Maxio)](https://www.maxio.com/payment-jurisdictions)
- [Maxio Billing (Maxio)](https://www.maxio.com/billing)
- [Maxio SaaS Payments (Maxio)](https://www.maxio.com/saas-payments)
- [Maxio Dunning Management (Maxio Blog)](https://www.maxio.com/blog/what-is-dunning)
- [Maxio Dunning How It Works (Docs)](https://docs.maxio.com/hc/en-us/articles/24287076583565-Understanding-How-Dunning-Works)
- [Maxio Gateway Features (Docs)](https://docs.maxio.com/hc/en-us/articles/24176142616333-Gateway-Features)
- [Maxio Growth and Innovation (BusinessWire)](https://www.businesswire.com/news/home/20250930883439/en/Maxio-Drives-Market-Momentum-with-Recent-Product-Innovations-and-Key-Executive-Hires)
- [Maxio Growth Blog (Maxio)](https://www.maxio.com/blog/maxio-drives-growth-with-innovation-and-leadership)
- [Battery Ventures Maxio Investment (Maxio News)](https://www.maxio.com/news/battery-ventures-growth-investment)
- [Maxio Pricing (Maxio)](https://www.maxio.com/pricing)
- [Maxio Pricing Analysis (Vendr)](https://www.vendr.com/marketplace/maxio)
- [Maxio Pricing Analysis (Orb)](https://www.withorb.com/blog/maxio-pricing)
- [Maxio About (Maxio)](https://www.maxio.com/about)
- [Maxio Funding (Crunchbase)](https://www.crunchbase.com/organization/maxio-e85b)
- [Maxio Company Profile (Tracxn)](https://tracxn.com/d/companies/maxio/__9d9HRQ27J9uL8ZJVHf8Mc4wSE8nZEvN3G-ucsEEMyeI)
- [Battery Ventures Maxio (Battery)](https://www.battery.com/company/maxio/)
- [Maxio Multi Currency (Maxio)](https://www.maxio.com/billing/multi-currency-accounting-software)
- [Maxio Logo (BrandFetch)](https://brandfetch.com/maxio.com)
- [Maxio Logo (SeekLogo)](https://seeklogo.com/vector-logo/531648/maxio)
- [BlueSnap Maxio Partnership (BlueSnap)](https://www.bluesnap.com/partners/maxio/)
