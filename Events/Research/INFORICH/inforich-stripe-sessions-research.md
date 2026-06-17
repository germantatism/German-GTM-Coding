# INFORICH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: INFORICH
=======================================

Logo: https://cdn.brandfetch.io/inforich.net/w/512/h/512/logo
Nombre merchant: INFORICH (ChargeSPOT)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 9-Market Payment Sprawl
Tittle_Pain Point_2: QR Code Drop-Off Rate
Tittle_Pain Point_3: Micro-Txn Decline Spikes
Tittle_Pain Point_4: No Failover on Rentals
Tittle_Pain Point_5: FX on Tourist Payments

Desc_Pain Point_1: 9 markets, each with different methods and compliance. 80,000+ stations with no unified orchestration layer to route and reconcile across all providers.
Desc_Pain Point_2: Users scan QR and pay before getting battery. Payment friction = walkaway. At 80,000+ stations with millions of micro-txns, 1% drop-off is major revenue loss.
Desc_Pain Point_3: Rentals at 165 yen (~$1.10). Banks flag micro-charges, raising decline rates. Millions of daily rentals across 9 markets makes this leakage compound.
Desc_Pain Point_4: Stripe cut failures 20%, but no cascade when Stripe declines. User sees failure, abandons rental. Each declined micro-payment is a lost rental at need.
Desc_Pain Point_5: Stations at airports/train stations serve tourists. Foreign cards face FX surcharges on $1 rentals. No multi-currency processing lowers conversion.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: d-Barai (NTT Docomo)
PSP_3: PayPay
PSP_4: Merpay
PSP_5: WeChat Pay
PSP_6: Alipay
PSP_7: Apple Pay
PSP_8: AEON Pay
PSP_9: Rakuten Pay
PSP_10: Paidy (BNPL)
PSP_11: SoftBank Carrier Billing
PSP_12: au Kantan Kessai

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PromptPay (Thailand)
Local_M_2: GrabPay (Singapore/SEA)
Local_M_3: Octopus Card (Hong Kong)
Local_M_4: FPS (Hong Kong)
Local_M_5: DuitNow (Malaysia)
Local_M_6: Satispay (Italy)
Local_M_7: Bancomat Pay (Italy)
Local_M_8: LINE Pay (Taiwan/Japan)
Local_M_9: JKO Pay (Taiwan)
Local_M_10: TrueMoney (Thailand)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each micro-transaction to the best acquirer by card BIN, issuer, and geography. 80,000+ stations across 9 markets processing millions of rentals. A 3% auth uplift at $1.10 average scales to significant daily revenue recovery.
Desc_Yuno_Cap2: When Stripe declines a rental, Yuno cascades to the next processor in milliseconds. Up to 50% recovery on soft declines means thousands of extra successful rentals daily. Each recovered payment is a customer saved at point of need.
Desc_Yuno_Cap3: Native methods in every market: PromptPay for Thailand, GrabPay for Singapore, Octopus/FPS for Hong Kong, Satispay for Italy. One API, 1,000+ methods. Users tap their local wallet and get a battery instantly, maximizing conversion per station.
Desc_Yuno_Cap4: One dashboard for ChargeSPOT volume across Stripe, PayPay, WeChat Pay, Alipay, d-Barai, and all local methods in 9 markets. Real-time approval monitoring per station and geography. Unified reconciliation replacing fragmented 12+ provider reporting.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**INFORICH at a glance:**
- Operates ChargeSPOT, Japan's first mobile battery sharing service
- Founded in Tokyo, Japan; headquartered in Shibuya-ku, Tokyo
- Public company: TSE Growth Market: 9338
- Revenue: $82.6M trailing 12 months (as of June 2025), growing 30% YoY
- EBITDA growth: +13% YoY
- Employees: ~200-300 across 5 cities in 4 countries
- Total funding: $119.59M
- 80,000+ battery stations installed globally
- Markets: Japan (47,330 stations), Hong Kong, China, Thailand, Taiwan, Singapore, Macau, Australia, Italy (newest)
- Directly operates in Japan, China, Hong Kong; franchise model in Thailand, Singapore, Macau
- Ezycharge brand in Australia

**ChargeSPOT product:**
- Users scan QR code at battery stand to rent portable battery charger
- Batteries can be returned at any ChargeSPOT station
- Installed in convenience stores, train stations, airports, commercial facilities
- Pricing: starts at 165 yen (~$1.10) for 30 minutes in Japan
- Also operates signage advertising business on ChargeSPOT stations

**Confirmed PSPs / Payment methods:**
- Stripe: core payment processor (reduced payment failures by 20% after A/B testing vs competitors)
- Credit/debit cards: Visa, Mastercard (via Stripe)
- Mobile payments: PayPay, Merpay, d-Barai, Apple Pay, Rakuten Pay, AEON Pay
- International wallets: Alipay, WeChat Pay
- Carrier billing: SoftBank, au Kantan Kessai
- BNPL: Paidy
- No payment orchestrator detected despite 12+ payment providers

**Stripe relationship (confirmed case study):**
- INFORICH expanded Stripe to core ChargeSPOT service after A/B testing
- Stripe demonstrated significantly lower payment failure rate vs competitors
- Payment failures dropped 20% after Stripe adoption
- Japanese and English documentation enabled smooth integration by overseas dev team
- Stripe's international capabilities supported expansion to Australia, Europe

**Brand update (October 2025):**
- Unified brand notation from "ChargeSPOT" to "CHARGESPOT"
- New black logotype for higher visibility and accessibility
- Reflects evolution toward global infrastructure service positioning

**Top 5 Markets Gap Analysis:**

MARKET 1: Japan (47,330+ stations, primary market)
  Currently offer: Credit cards, PayPay, Merpay, d-Barai, Apple Pay, Rakuten Pay, AEON Pay, Paidy, SoftBank/au billing
  Missing: LINE Pay, Suica/Pasmo (transit IC cards)
  Strong local method coverage but missing transit card payments, which are the most natural payment method at train station locations.

MARKET 2: Thailand (franchise market)
  Currently offer: Credit cards (via Stripe)
  Missing: PromptPay, TrueMoney, Rabbit LINE Pay
  PromptPay is the dominant mobile payment in Thailand. Card-only payments at tourist stations miss 80%+ of local users.

MARKET 3: Hong Kong (directly operated)
  Currently offer: Credit cards, Alipay, WeChat Pay
  Missing: Octopus Card, FPS, PayMe
  Octopus is used for 99% of transit-related micro-payments in Hong Kong. Not accepting it at transit stations is a major conversion gap.

MARKET 4: Singapore (franchise market)
  Currently offer: Credit cards (via Stripe)
  Missing: GrabPay, PayNow, Nets QR
  GrabPay and PayNow dominate Singaporean micro-payments. Card-only rental at MRT stations misses the convenience users expect.

MARKET 5: Italy (newest market)
  Currently offer: Credit cards (via Stripe)
  Missing: Satispay, Bancomat Pay, PostePay
  Italy has rapid mobile payment adoption. Satispay has 5M+ users specifically for micro-transactions, making it ideal for battery rentals.

**Key meeting angles:**
1. **80,000+ stations, 9 markets** | Massive physical footprint with fragmented payment infrastructure. Orchestration consolidates 12+ providers into one layer
2. **Micro-transaction economics** | $1.10 average rental means every declined payment matters. Smart routing maximizes auth rates on small amounts that banks often flag
3. **Already a Stripe customer** | INFORICH chose Stripe after A/B testing. Yuno adds orchestration on top of their existing Stripe relationship
4. **30% revenue growth** | Rapidly expanding into new markets (Italy, more to come). Each new country requires new payment methods without engineering sprints
5. **Tourist conversion** | Stations at airports and train stations serve international visitors. Multi-currency processing removes FX friction on micro-payments
6. **12+ payment providers** | PayPay, Merpay, WeChat Pay, Alipay, d-Barai, Apple Pay, Rakuten Pay, and more. No unified dashboard exists to monitor and optimize across all providers

**Sources:**
- [Stripe Case Study: INFORICH](https://stripe.com/en-jp/customers/inforich)
- [INFORICH Official Website](https://inforich.net/en/)
- [INFORICH Brand Logo Revision Announcement](https://inforich.net/en/8518/announcement-of-chargespot-brand-logo-revision)
- [ChargeSPOT Global Franchise](https://franchise.chargespot.global/)
- [INFORICH Shared Research Profile](https://sharedresearch.jp/en/companies/9338)
- [Yahoo Finance: INFORICH (9338.T)](https://finance.yahoo.com/quote/9338.T/profile/)
- [PitchBook: INFORICH](https://pitchbook.com/profiles/company/433980-46)
- [Nanikoko: ChargeSPOT Guide](https://nanikoko.com/blogs/experience-japan/chargespot-your-mobile-battery-rental-solution-in-japan)
- [Fun-Japan: ChargeSPOT Guide 2026](https://www.fun-japan.jp/en/articles/14478)
- [CBInsights: INFORICH](https://www.cbinsights.com/company/inforich)
- [Dealroom: INFORICH](https://app.dealroom.co/companies/inforich)
