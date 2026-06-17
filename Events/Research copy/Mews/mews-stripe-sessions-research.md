# MEWS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Mews
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idVJTfaifh/idKGOUOmWI.svg
Nombre merchant: Mews

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Gateway Lock-In
Tittle_Pain Point_2: Virtual Card Chaos
Tittle_Pain Point_3: Limited Currency Support
Tittle_Pain Point_4: No Multi-Acquirer Routing
Tittle_Pain Point_5: Guest APM Blind Spots

Desc_Pain Point_1: Hotels can enable only one gateway (Adyen OR Stripe), never both. With $19.7B in platform transaction volume across 15,000 properties, a single processor creates systemic risk. No failover if the chosen gateway degrades.
Desc_Pain Point_2: OTA virtual cards from Booking.com and Expedia fail or delay charges depending on the gateway. Adyen and Stripe handle virtual card timing differently, causing payment failures and reconciliation mismatches across bookings.
Desc_Pain Point_3: Mews Merchant accounts support only CZK, EUR, and GBP. Hotels in 85 countries processing in USD, AED, THB, or SGD must use own accounts with complex setup, or face forced currency conversion and margin erosion.
Desc_Pain Point_4: With only one gateway enabled, there is zero intelligent routing. A declined card cannot cascade to an alternative acquirer. Every failed authorization on a $19.7B platform is a permanent revenue loss.
Desc_Pain Point_5: Apple Pay, PayPal, and other digital wallets are not supported through Mews Merchant for direct processing. Guests expecting mobile wallet checkout at booking or check-in face a card-only wall.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (embedded gateway option, card processing)
PSP_2: Adyen (embedded gateway option, card processing)
PSP_3: External gateways (OTA virtual cards, manual reconciliation)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Alipay
Local_M_3: WeChat Pay
Local_M_4: iDEAL
Local_M_5: SEPA Direct Debit
Local_M_6: Pix
Local_M_7: UPI
Local_M_8: GrabPay
Local_M_9: KakaoPay
Local_M_10: Klarna

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each hotel transaction by card BIN, issuer country, and currency to the optimal acquirer. With $19.7B platform transaction volume and 15,000 properties in 85 countries, per-market routing delivers 3-10% auth uplift. At this scale, a 3% improvement recovers hundreds of millions in otherwise lost room revenue.
Desc_Yuno_Cap2: Automatic cascade between Stripe and Adyen (and additional acquirers) when the primary gateway declines. No more single-attempt failures. Up to 50% recovery on failed transactions. Virtual card charges from OTAs retry seamlessly instead of requiring manual intervention by front desk staff.
Desc_Yuno_Cap3: Activate guest payment methods Mews cannot offer natively: Alipay and WeChat Pay for Chinese travelers, UPI for Indian guests, iDEAL for Dutch bookers, Pix for Brazilian tourists, GrabPay across Southeast Asia, PayPal globally. One API, 1,000+ methods. Meet every guest in their preferred payment experience.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Adyen, and OTA virtual card processing across 15,000 properties. Real-time approval monitoring per country and property, centralized reconciliation replacing manual matching, and NOVA fraud detection (75% reduction) protecting high-value hotel transactions from chargebacks and stolen card fraud.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Mews at a glance:**
- Founded: 2012 by Richard Valtr. HQ: Amsterdam, Netherlands (originally Prague, Czech Republic)
- CEO: Matthijs Welle (since January 2017)
- Valuation: $2.5B (January 2026, Series D)
- Total funding: $710M over 15 rounds from 21 investors
- Key rounds: Series B ($33M, 2019), Series C ($185M, 2022), Series D ($110M, 2024), Series D extension ($300M, January 2026)
- Key investors: EQT Growth (led Series D), Kinnevik, Battery Ventures, Tiger Global, Atomico, HarbourVest, Goldman Sachs AM, Salesforce Ventures, Notion Capital
- Revenue: $200M+ (crossed in 2024); SaaS gross profit grew 55% in 2025
- Platform transaction volume: $19.7B (2025)
- Properties: 15,000 customers across 85 countries
- Monthly active hoteliers: 132,000+
- Checked-in reservations: 42.3M in 2025 (3.2M via Mews Kiosk)
- Employees: 1,000+
- Mews Spaces: Generated $537M in additional revenue for hoteliers (2M+ non-room reservations)
- Recognition: Best PMS (2024, 2025, 2026), Best POS (2026) by Hotel Tech Report; IDC MarketScape Leader (2025)
- Acquisition: Clarity Hospitality Software Solutions (January 2025, APAC expansion)
- Products: PMS, POS, RMS, Housekeeping, Payments, Kiosk, Business Intelligence, Mews Spaces

**Confirmed Payment Stack:**
- Adyen: Embedded gateway option (card processing, terminals)
- Stripe: Embedded gateway option (card processing, terminals including S1 and S2)
- Critical limitation: Hotels can only enable ONE gateway at a time (Adyen OR Stripe, never both)
- Mews Merchant: Managed account mode (CZK, EUR, GBP currencies only)
- Own Account: Hotels manage their own Adyen/Stripe contracts (more currencies, more complex)
- Apple Pay / Google Pay: NOT supported through Mews Merchant for direct processing
- PayPal: NOT supported through Mews Merchant
- Virtual card detection: Automatic recognition of OTA virtual cards
- Multicurrency: Launched feature allowing guests to pay in home currency
- PCI DSS and PSD2 compliant
- Zero Dollar Authorization: Launched to reduce payment failures and protect revenue
- No payment orchestrator detected
- No multi-acquirer routing; single gateway per property

**Payment Challenges (Community Evidence):**
- Virtual cards from Booking.com frequently fail or are not chargeable until check-in
- Expedia payments scheduled for arrival date, not booking date, causing cash flow delays
- Adyen and Stripe handle virtual cards differently, creating inconsistent behavior
- External payment gateways require manual registration of advance payments
- Payments misallocated or bookings charged twice when using external providers
- Business partner invoicing workflow described as "extremely poor"
- Fraud: Credit card fraud reported in community forums, though Mews claims 60% fraud reduction for users

**Top 5 Markets Gap Analysis:**

MARKET 1: Europe (core market, largest property base)
  Accepted: Visa/MC/Amex via Stripe or Adyen, EUR/GBP/CZK Merchant accounts
  Missing: PayPal, iDEAL (Netherlands), SEPA DD, Bancontact (Belgium), Sofort (Germany), Klarna
  Note: Amsterdam HQ, European dominance. Dutch hotels cannot accept iDEAL through Mews Payments.

MARKET 2: North America (growth focus, US expansion)
  Accepted: Visa/MC/Amex via Stripe or Adyen
  Missing: PayPal, Venmo, Apple Pay (direct), Google Pay (direct), ACH
  Note: $75M raised specifically for US expansion. American guests expect digital wallet options.

MARKET 3: Asia Pacific (post-Clarity acquisition expansion)
  Accepted: International cards via Stripe or Adyen
  Missing: Alipay, WeChat Pay, GrabPay, LINE Pay, PayPay, UPI, QR code payments
  Note: Chinese and Southeast Asian travelers are the fastest-growing hotel guest segments. Alipay/WeChat Pay essential.

MARKET 4: Middle East (emerging hospitality market)
  Accepted: International cards via Stripe or Adyen
  Missing: Mada (Saudi Arabia), KNET (Kuwait), Benefit (Bahrain), Apple Pay (local), STC Pay
  Note: UAE and Saudi Arabia hotel boom. Local payment methods critical for domestic guests.

MARKET 5: Latin America (tourism growth market)
  Accepted: International cards via Stripe or Adyen
  Missing: Pix (Brazil), PSE (Colombia), OXXO (Mexico), Mercado Pago, Boleto
  Note: Brazilian and Mexican tourists increasingly traveling globally. Pix is 70%+ of Brazilian digital payments.

**Key meeting angles:**
1. **$19.7B transaction volume locked to a single gateway** | Only one PSP active per property. Zero failover, zero routing, zero redundancy across 15,000 hotels.
2. **"Choose Adyen OR Stripe" is a false choice** | Orchestration enables both (and more) simultaneously, routing each transaction to the optimal acquirer.
3. **Virtual card reconciliation nightmare** | OTA virtual cards from Booking.com/Expedia behave differently on each gateway. Unified orchestration standardizes processing.
4. **Guest payment expectations unmet** | Apple Pay, PayPal, Alipay, WeChat Pay all unsupported through Mews Merchant. International travelers expect local methods.
5. **85 countries, 3 Merchant currencies** | CZK/EUR/GBP limitation forces complex own-account setup for most of the world.
6. **$300M raised to scale globally** | Payment orchestration is the missing infrastructure to support 85-country expansion without per-market gateway integrations.
7. **Competitor pressure** | Oracle Hospitality (OPERA), Cloudbeds, and Apaleo all expanding payment capabilities and multi-gateway support.

**Sources:**
- [Mews: Payments Product Page](https://www.mews.com/en/products/payments)
- [Mews: POS Payment Processing](https://www.mews.com/en/products/pos-payment-processing)
- [Mews: Payment Terminals](https://www.mews.com/en/products/terminals)
- [Mews: Hotel Payment Tools](https://www.mews.com/en/blog/hotel-payment-tools-options)
- [Mews: Hotel Chargebacks](https://www.mews.com/en/blog/hotel-chargebacks-how-to-handle)
- [Mews: Preventing Chargebacks](https://www.mews.com/en/blog/preventing-hotel-chargebacks)
- [Mews: Credit Card Fraud Types](https://www.mews.com/en/blog/hotel-credit-card-scam)
- [Mews: Hidden Costs of OTAs](https://www.mews.com/en/blog/the-hidden-rising-costs-of-otas)
- [Mews: How Payments Transform Your Property](https://www.mews.com/en/blog/how-mews-payments-can-transform-your-property)
- [Mews: Why PMS POS Payments Combined](https://www.mews.com/en/blog/why-combining-pms-pos-and-payments-matters)
- [Mews Freshdesk: Payment Integrations](https://mewssystems.freshdesk.com/support/solutions/articles/31000129943-payment-integrations)
- [Mews Freshdesk: Merchant FAQ](https://mewssystems.freshdesk.com/support/solutions/articles/31000132918-mews-merchant-faq)
- [Mews Community: Stripe Payment](https://community.mews.com/mews-marketplace-85/stripe-payment-905)
- [Mews Community: Terminal S1 Stripe](https://community.mews.com/mews-payments-84/mews-terminal-s1-stripe-payment-1789)
- [Mews Community: External Payments](https://community.mews.com/mews-payments-84/external-payments-2120)
- [Mews Community: Virtual Card Automation](https://community.mews.com/nordic-based-customers-72/payment-automation-virtual-cards-2596)
- [Mews Community: Fraud Environment](https://community.mews.com/mews-beta-program-43/creating-hostile-environment-for-fraud-stolen-card-details-chargebacks-1308)
- [Mews Community: Multicurrency Feature](https://community.mews.com/mews-updates-38/new-feature-multicurrency-by-mews-payments-1961)
- [Mews: $300M Series D Press Release](https://www.mews.com/en/press/mews-secures-300-million-investment)
- [Mews: Series C $185M](https://www.mews.com/en/press/series-c)
- [Mews: About Us](https://www.mews.com/en/about-us)
- [Mews: 2025 Year in Review](https://www.mews.com/en/blog/2025-hospitality-highlights)
- [TechCrunch: Mews $75M Round](https://techcrunch.com/2025/03/04/hotel-management-platform-mews-books-75m-round-led-by-tiger-global/)
- [SiliconANGLE: Mews $300M at $2.5B](https://siliconangle.com/2026/01/23/hotel-software-maker-mews-nabs-300m-2-5b-valuation/)
- [Vestbee: Mews $300M Raise](https://www.vestbee.com/insights/articles/mews-raises-300-m)
- [Skift: Mews $75M Growth](https://skift.com/2025/03/04/mews-raises-75-million-for-hotel-tech-growth-and-ma/)
- [Kinnevik: Mews Investment](https://www.kinnevik.com/investor-relations/press-releases/2026/kinnevik-invests-in-mews-eur-264m-funding-round/)
- [Hotel Tech Report: Mews PMS Reviews](https://hoteltechreport.com/operations/property-management-systems/mews)
- [Contrary Research: Mews Breakdown](https://research.contrary.com/company/mews)
- [Hospitality Upgrade: Zero Dollar Authorization](https://www.hospitalityupgrade.com/news/mews-launches-zero-dollar-authorization-to-protect-hotel-revenue-and-reduce-payment-failures)
- [Brandfetch: Mews Logo](https://brandfetch.com/mews.com)
