# KAJABI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Kajabi
═══════════════════════════════════════

Logo: https://cdn.prod.website-files.com/693317e747432cd054b3bdc6/693a057a27ade1233a0c9ed9_Footer%20Icon.svg
Nombre merchant: Kajabi

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Stripe Backbone
Tittle_Pain Point_2: Limited Global Reach
Tittle_Pain Point_3: Zero Local APMs
Tittle_Pain Point_4: Pricing Backlash Risk
Tittle_Pain Point_5: Subscription Churn Leak

Desc_Pain Point_1: Kajabi Payments is 100% Stripe, zero failover. Every course, coaching, and community purchase routes through one acquirer. One outage halts all commerce.
Desc_Pain Point_2: Kajabi Payments only works in US, CA, UK, AU, UAE, and select EU. Creators in LATAM, Asia, Africa must use third-party Stripe with added surcharges.
Desc_Pain Point_3: Only cards, Apple Pay, Google Pay, Klarna, and Afterpay. No Pix, UPI, OXXO, or iDEAL. 100,000+ creators sell globally with just 6 payment options.
Desc_Pain Point_4: 2025 price hike sparked Change.org petition. Third-party gateway surcharges push creators into Kajabi Payments but kill all processor flexibility.
Desc_Pain Point_5: Failed membership and coaching renewals churn involuntarily. No cascade retry through alternate acquirers to recover soft declines before members are lost.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Kajabi Payments)
PSP_2: Stripe (direct integration)
PSP_3: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: iDEAL
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: GCash
Local_M_8: Bancontact
Local_M_9: SPEI
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every creator transaction to the best-performing acquirer by card BIN, issuer, and market. With $10B+ in lifetime creator GMV and 100,000+ active creators, even a 3% auth improvement recovers millions in annual revenue that currently declines silently.
Desc_Yuno_Cap2: Automatic cascade eliminates Kajabi's single-Stripe dependency. When a membership renewal declines, Yuno retries through alternate processors in milliseconds. Converts involuntary churn into recovered recurring revenue. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activate Pix in Brazil, UPI in India, OXXO in Mexico, iDEAL in Netherlands, BLIK in Poland, GCash in Philippines, Konbini in Japan. One API, 1,000+ payment methods. Creators unlock buyers who currently cannot pay at all.
Desc_Yuno_Cap4: One dashboard unifying Kajabi's Stripe + PayPal settlement streams. Centralized reconciliation, real-time approval rate monitoring per geography, automated payout tracking. Kajabi Capital lending decisions improve with richer transaction data.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Kajabi at a glance:**
- Private company; $2B valuation (2024); raised $550M total funding
- Company revenue: $75M (2024), up from $60M (2020)
- 100,000+ creators; 19,000 paying customers
- Lifetime creator earnings: $10B+ (crossed $9B in August 2025)
- ~1,800 creator millionaires; 70+ creators past $10M; 1 creator past $100M
- Average creator earnings: $190K
- HQ: Irvine, California
- Kajabi Capital launched December 2025 (embedded creator financing)
- 2025 pricing restructure sparked significant creator backlash
- Plans: Kickstarter ($55/mo), Basic ($119/mo), Growth ($159/mo), Pro ($319/mo)

**Confirmed PSPs:**
- Stripe: powers Kajabi Payments (backend partnership confirmed)
- Stripe: available as direct third-party integration
- PayPal: available as external gateway
- Novalnet: third-party integration available for 100+ payment methods (workaround)
- No payment orchestrator detected
- No multi-acquirer failover

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary creator + buyer market)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Klarna, Afterpay
  Missing: ACH, Cash App Pay, Venmo standalone
  Note: US market well covered; opportunity in alternative payment rails for high-ticket coaching.

MARKET 2: United Kingdom (Kajabi Payments supported)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay, Klarna
  Missing: Open Banking (Pay by Bank), Direct Debit, Clearpay
  Note: UK Open Banking growing rapidly for subscription billing. Direct Debit dominant for recurring.

MARKET 3: EU markets (recently launched Kajabi Payments)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: iDEAL (NL), SEPA Direct Debit, Sofort, Bancontact (BE), Giropay (DE)
  Note: iDEAL handles 70%+ of Dutch e-commerce. SEPA DD is backbone of European recurring payments.

MARKET 4: Brazil (NOT supported by Kajabi Payments)
  Accepted: International cards only (via custom Stripe)
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazilian digital payments. LATAM creators cannot use Kajabi Payments at all.

MARKET 5: India (NOT supported by Kajabi Payments)
  Accepted: International cards only (via custom Stripe)
  Missing: UPI, RuPay, Paytm, PhonePe, NetBanking
  Note: 75%+ of Indian digital payments are UPI. India is a massive English-speaking course buyer market.

**Key payment challenges:**
- Kajabi Payments EU launch (Q2 2025) still missing core EU methods like iDEAL, SEPA DD
- Third-party Stripe integration now carries surcharges, penalizing creators who want processor diversity
- Linktopay.eu exists as workaround for EU methods (iDEAL, Bancontact, Sofort, SEPA) showing clear demand
- Kajabi Capital lending program depends on transaction data quality; orchestration would enhance this
- Price hike backlash means Kajabi must deliver more value (better payment coverage) to justify new pricing

**Key meeting angles:**
1. **$2B valuation, single-processor risk**: investors want resilient infrastructure, not Stripe-only dependency
2. **Kajabi Capital synergy**: embedded lending improves with multi-processor transaction intelligence
3. **EU launch gap**: Kajabi Payments in Europe without iDEAL, SEPA DD, Sofort is like launching half-ready
4. **Creator revolt context**: price hike backlash means Kajabi needs to show more value; APM coverage does that
5. **High-ticket coaching**: average creator earns $190K; high-AOV transactions need maximum auth rates
6. **Competitor pressure**: Teachable (Hotmart) has LATAM APMs; Thinkific is TSX-listed with margin pressure

**Sources:**
- [Kajabi Payments Overview](https://help.kajabi.com/hc/en-us/articles/10426676298267-Kajabi-Payments-Overview)
- [Kajabi Payments: Europe](https://help.kajabi.com/en/articles/12695462-getting-started-with-kajabi-payments-europe)
- [Kajabi Payments: US](https://help.kajabi.com/en/articles/12695455-getting-started-with-kajabi-payments-united-states)
- [Kajabi Payments Fees: Europe](https://help.kajabi.com/hc/en-us/articles/33927134823835-Kajabi-Payments-Fees-Europe)
- [Kajabi Payments EU Launch](https://kajabi.com/updates/kp-eu-launch)
- [Kajabi Multi-Currency Offers](https://help.kajabi.com/hc/en-us/articles/360037763113-How-to-Make-Offers-Available-in-Multiple-Currencies)
- [Stripe Case Study: Kajabi](https://stripe.com/customers/kajabi)
- [Kajabi $10B Creator Revenue (BusinessWire)](https://www.businesswire.com/news/home/20250806424975/en/$10B-in-Creator-Revenue-and-Climbing-Kajabi-Creators-Are-Achieving-Long-Term-Financial-Success)
- [Kajabi Revenue & Customers (Latka)](https://getlatka.com/companies/kajabi)
- [Kajabi Valuation (Sacra)](https://sacra.com/c/kajabi/)
- [Kajabi Statistics (ElectroIQ)](https://electroiq.com/stats/kajabi-statistics/)
- [Kajabi Price Hike Frustration (EzyCourse)](https://ezycourse.com/blog/kajabi-price-hike)
- [Kajabi 2026 Review (Learning Revolution)](https://www.learningrevolution.net/kajabi-review/)
- [Kajabi $0 to $9B Feature Growth](https://www.kajabi.com/updates/0-to-9-billion-how-kajabis-features-drive-growth-in-creator-revenue)
- [Linktopay EU Payment Integration for Kajabi](https://www.linktopay.eu)
- [Novalnet Kajabi Integration](https://www.novalnet.com/integration/kajabi/)
