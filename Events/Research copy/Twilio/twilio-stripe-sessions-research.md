# TWILIO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Twilio
═══════════════════════════════════════

Logo: https://www.vectorlogo.zone/logos/twilio/twilio-ar21.svg
Nombre merchant: Twilio

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Billing Stack
Tittle_Pain Point_2: Cross-Border Decline Spike
Tittle_Pain Point_3: Single Acquirer Lock-In
Tittle_Pain Point_4: Invoice-Only Flex Payments
Tittle_Pain Point_5: Billing Outage Exposure

Desc_Pain Point_1: 335K+ active accounts across 180 countries pay via credit card or PayPal only. Zero local APMs accepted. Developers in Brazil, India, and Southeast Asia face systematic card declines from issuer fraud blocks.
Desc_Pain Point_2: International cards from 230 countries frequently declined by US-based fraud detection. Non-US developers report bank holds on "suspicious US charges," forcing manual bank calls before they can even activate accounts.
Desc_Pain Point_3: Stripe is the sole card acquirer after Twilio migrated from its previous processor. No failover path exists. Any Stripe disruption blocks billing for 335K+ accounts and freezes usage-based services instantly.
Desc_Pain Point_4: Enterprise invoice payments limited to wire transfer or ACH only. No credit card, no SEPA Direct Debit, no local bank transfer options for EU and LATAM enterprise customers.
Desc_Pain Point_5: Documented billing infrastructure failure caused cascading Redis crashes, repeated auto-recharge attempts, and mass account suspensions. A single billing pipeline with no redundancy amplified the outage impact.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: Boleto
Local_M_5: BLIK
Local_M_6: iDEAL
Local_M_7: Bancontact
Local_M_8: Konbini
Local_M_9: GCash
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal based on card BIN, issuer country, and transaction type. With $5B+ annual revenue from 335K accounts in 180 countries, even a 3% auth uplift recovers $150M+ in previously lost billing volume.
Desc_Yuno_Cap2: Automatic cascade eliminates Twilio's single-Stripe dependency. When Stripe declines or experiences downtime, Yuno reroutes to the next best acquirer in milliseconds. Prevents the mass account suspensions seen in past billing outages. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates the APMs Twilio's global developers need: Pix in Brazil, UPI in India, SEPA DD in Europe, iDEAL in Netherlands, Konbini in Japan, OXXO in Mexico. One API, 1,000+ payment methods. Eliminates card-only friction across 180 markets.
Desc_Yuno_Cap4: One dashboard replacing Twilio's fragmented Stripe + PayPal + wire/ACH invoice streams. Real-time approval rate monitoring across all payment flows, centralized reconciliation for usage-based and subscription billing, millisecond anomaly detection via NOVA intelligence.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Twilio at a glance:**
- 335,000+ active customer accounts, 10M+ developers, 180+ countries
- Revenue: $5.07B (FY2025), 13.7% YoY growth; Q4 2025 revenue $1.37B (+14.3% YoY)
- FY2026 guidance: 11.5% to 12.5% reported revenue growth (~$5.65B)
- Non-GAAP operating income: $924M (FY2025), 18.2% margin; FY2026 guidance $1.04B to $1.06B
- Free cash flow guidance FY2026: $1.04B to $1.06B
- CEO: Khozema Shipchandler (since January 2024); CFO: Aidan Viggiano; CRO: Thomas Wyatt
- Public: NYSE: TWLO. Market cap ~$15B+
- Leader in 2025 Gartner Magic Quadrant for CPaaS (third consecutive year)
- Products: Programmable Voice, Messaging, Video, Email (SendGrid), Segment (CDP), Flex (contact center)
- Nearly 1.8 trillion digital interactions processed annually

**Confirmed PSPs:**
- Stripe: primary card acquirer (confirmed via Stripe case study; migrated from unnamed previous provider)
- PayPal: secondary (accepted for account funding)
- Wire/ACH: for enterprise invoice payments only
- No payment orchestrator detected
- Twilio itself offers Twilio Pay connectors (for their customers' payments), connecting to Stripe, Worldpay, Checkout.com, Adyen via Shuttle

**Key Stripe relationship detail:**
- Twilio ran A/B tests with multiple global processors before selecting Stripe
- 10% authorization rate uplift vs. previous provider (5.5% from network connectivity, 1% ML, 2% Card Account Updater, 1.5% account management)
- Local acquiring in Japan, EU, and Americas

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~40% of revenue)
  Accepted: Visa/MC/Amex/Discover, PayPal, ACH (invoices)
  Missing: Real-time account debits, Cash App Pay
  Usage-based billing model means frequent micro-charges that benefit from high auth rates.

MARKET 2: Europe (significant presence, EMEA infrastructure)
  Accepted: Visa/MC via Stripe, PayPal, wire transfer (invoices)
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BLIK, Sofort
  European enterprises forced to pay via wire for invoices. No recurring debit option.

MARKET 3: Brazil (growing developer market)
  Accepted: International cards via Stripe
  Missing: Pix, Boleto, local installment cards
  Pix handles 70%+ of Brazil digital payments. Developers without international cards cannot onboard.

MARKET 4: India (large developer community)
  Accepted: International cards via Stripe, PayPal
  Missing: UPI, RuPay, Paytm, net banking
  75%+ of Indian digital payments use UPI. Many developers cannot pay for Twilio services.

MARKET 5: Japan (local acquiring via Stripe)
  Accepted: Visa/MC/Amex, JCB
  Missing: Konbini, Pay-easy, carrier billing
  Local acquiring helps, but convenience store payments (Konbini) are critical for non-card users.

**Billing outage history:**
- Documented major billing infrastructure failure: Redis cluster crash caused repeated auto-recharges, incorrect balances, and mass account suspensions
- SendGrid (Twilio subsidiary) uses PCI-compliant third-party billing provider as additional single point of failure
- 3DS authentication errors reported on SendGrid billing

**Key meeting angles:**
1. **Already Stripe-dependent** | Twilio chose Stripe after rigorous A/B testing but created single-acquirer risk
2. **Usage-based model sensitivity** | Micro-transactions across 335K accounts magnify every basis point of auth rate improvement
3. **Developer-first DNA** | Single API integration resonates with Twilio's engineering culture
4. **Billing outage precedent** | Past Redis billing crash proves need for redundant payment paths
5. **$5B+ revenue scale** | Even 1% improvement in collection rates represents $50M+ annually
6. **International developer access** | Card-only billing excludes developers in markets where cards are not dominant
7. **Competitor context** | Other SaaS platforms (Atlassian, HubSpot) accept local payment methods in key markets

**Sources:**
- [Stripe Case Study: Twilio](https://stripe.com/customers/twilio)
- [Stripe Newsroom: Twilio 10% Auth Rate Uplift](https://stripe.com/newsroom/stories/twilio)
- [Twilio Q4/FY2025 Earnings](https://www.twilio.com/en-us/press/releases/Q4-full-year-2025-earnings)
- [Twilio Q1 2025 Earnings](https://www.twilio.com/en-us/press/releases/q1-2025-earnings)
- [Twilio Billing Incident Post-Mortem](https://www.twilio.com/en-us/blog/company/communications/billing-incident-post-mortem-breakdown-analysis-and-root-cause-html)
- [Twilio Support: Payment Options](https://support.twilio.com/hc/en-us/articles/360042138913)
- [Twilio Support: Why Credit Card Fails](https://support.twilio.com/hc/en-us/articles/223183308)
- [Twilio Leadership](https://www.twilio.com/en-us/company/leadership)
- [Twilio Global Infrastructure](https://www.twilio.com/en-us/global-infrastructure)
- [Twilio About](https://www.twilio.com/en-us/company)
- [Twilio 2025 Gartner MQ Leader](https://investors.twilio.com/news-releases/news-release-details/twilio-recognized-leader-2025-gartnerr-magic-quadranttm-cpaas)
- [Twilio Pay Connectors](https://www.twilio.com/docs/voice/twiml/pay/pay-connectors)
