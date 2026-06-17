# ZENDESK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Zendesk
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idJFz4OxMQ/idV3ALaQ6Z.svg
Nombre merchant: Zendesk

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-Processor Dependency
Tittle_Pain Point_2: Cross-Border Cost Drain
Tittle_Pain Point_3: Local Method Gaps
Tittle_Pain Point_4: Billing Complaint Backlog
Tittle_Pain Point_5: AI Monetization at Risk

Desc_Pain Point_1: Stripe is the sole card processor since 2022. 97% auth rate leaves 3% failing with no cascade. At $2B+ revenue, that 3% is tens of millions in lost renewals.
Desc_Pain Point_2: Actively expanding local acquiring in Brazil and India. Without local entities in every market, international cards face higher declines and $1.5M+ in extra costs.
Desc_Pain Point_3: Self-serve accepts cards, PayPal, ACH, and direct debit only. No Pix, UPI, SEPA DD, BLIK, or iDEAL. 173K+ customers in 160 countries with minimal local coverage.
Desc_Pain Point_4: Community shows year-long billing disputes, collection notices from failed payments, and prepaid rejections. Billing support rated poorly. Each issue risks churn.
Desc_Pain Point_5: AI ARR projected $500M by 2026 (150% YoY). New AI add-on purchases require frictionless payment. If emerging market buyers cannot pay locally, growth stalls.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (card processing, primary since Jan 2022)
PSP_2: PayPal (self-serve alternative)
PSP_3: ACH / Direct Debit (US bank accounts)
PSP_4: Wire Transfer / Check (enterprise invoicing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: SPEI
Local_M_8: Bancontact
Local_M_9: KakaoPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $2B+ revenue, 173K+ customers in 160 countries, and active local acquiring expansion in Brazil and India, routing each renewal to the best acquirer per market pushes auth rates beyond 97% and delivers 3-10% uplift.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a subscription renewal. Instead of losing 3% of transactions to a single-processor ceiling, Yuno retries through the next best acquirer in milliseconds. Up to 50% recovery on failed transactions directly reduces involuntary churn at scale.
Desc_Yuno_Cap3: Activates methods Zendesk's global base demands: Pix in Brazil, UPI in India, SEPA DD across Europe, iDEAL in Netherlands, BLIK in Poland, Boleto in Brazil, SPEI in Mexico, Bancontact in Belgium. One API, 1,000+ methods. Accelerates AI add-on purchases in emerging markets.
Desc_Yuno_Cap4: One dashboard unifying Stripe card processing, PayPal, ACH, direct debit, and wire transfers. Real-time approval monitoring per country, centralized reconciliation for 173K+ accounts, and NOVA fraud detection (75% reduction) protecting $500M in AI ARR growth.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Zendesk at a glance:**
- Founded: 2007 in Copenhagen, Denmark. HQ: San Francisco, California
- Ownership: Private since 2022 ($10.2B buyout by Hellman & Friedman and Permira)
- Pre-buyout public valuation: $17B
- Current estimated private valuation: ~$9.6B
- Revenue: ~$2B+ annually (estimated 2025). $1.93B reported (2024)
- AI ARR: $200M (end of 2025), projected $500M by end of 2026 (150% YoY growth)
- Marketplace revenue: On track to surpass $200M by 2026
- Customers: 173,000+ companies in 160+ countries
- Market share: ~28% of customer support software market (2025 leader)
- Products: Zendesk Support, Zendesk Sell, Zendesk Guide, Zendesk Chat, Zendesk Talk, Zendesk Explore, Zendesk Sunshine
- AI focus: AI agents, AI copilot, AI-powered workflows
- Languages: ~31 supported
- Marketplace: 1,900+ apps across 5 core categories
- Notable customers: Shopify, Uber, Slack, Airbnb, Amazon, Walmart, Apple, Toyota, Shell, Samsung, T-Mobile, CVS Health
- 85% of Zendesk's book of business uses 1+ technology partner integration

**Confirmed Payment Stack:**
- Stripe: Primary card processor since January 2022 (migrated from previous provider)
- Stripe auth rate: ~97% (1-2pp improvement over prior provider)
- PayPal: Alternative for self-serve accounts (supports multi-currency)
- ACH / Direct Debit: US bank account payments for eligible accounts
- Wire Transfer: Enterprise and managed accounts
- Check: Enterprise payment option
- Credit/Debit cards: Standard card brands
- Currencies supported: USD, EUR, GBP, BRL (for Support accounts)
- ChargeDesk: Third-party integration connecting Stripe/Braintree/PayPal to support tickets
- Local acquiring expansion: Targeting Brazil and India for local entities
- Cost savings: $1.5M annually from Stripe migration
- No payment orchestrator detected
- No multi-processor failover

**Payment Method Gaps (Evidence):**
- No SEPA Direct Debit for European recurring subscriptions
- No Pix for Brazil (despite active local acquiring expansion there)
- No UPI for India (despite targeting it as a key growth market)
- No iDEAL, BLIK, Bancontact, or other European local methods
- No LATAM methods (Boleto, OXXO, SPEI)
- No APAC methods (KakaoPay, GrabPay, PromptPay, LINE Pay)
- Pre-paid credit cards often rejected due to local bank policies
- Community complaints about billing disputes lasting 8+ months
- Users report receiving collection notices from failed payment processes
- Billing support rated poorly in community ("worst 1/10")

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, majority of revenue)
  Accepted: Visa/MC/Amex, ACH, PayPal, Wire, Check
  Missing: Venmo (direct), Apple Pay, Google Pay (for self-serve)
  Note: Best coverage. Stripe local acquiring already active.

MARKET 2: Europe (strong enterprise presence, UK focus)
  Accepted: Visa/MC, PayPal, Wire
  Missing: SEPA DD, iDEAL (Netherlands), BLIK (Poland), Bancontact (Belgium), GiroPay, Sofort, MB Way
  Note: EUR is supported but no recurring SEPA DD for subscriptions. Major gap for European expansion.

MARKET 3: Brazil (active local acquiring expansion)
  Accepted: Visa/MC (local acquiring in progress), PayPal
  Missing: Pix, Boleto
  Note: Zendesk explicitly targeting Brazil for local acquiring. Pix processes 70%+ of digital payments. Critical gap despite strategic focus.

MARKET 4: India (active local acquiring expansion)
  Accepted: Visa/MC (local acquiring in progress)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: Zendesk explicitly targeting India for local acquiring. UPI handles 75%+ of digital payments. Essential for AI add-on growth.

MARKET 5: Japan / APAC (high adoption, concentrated user base)
  Accepted: Visa/MC (cross-border)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: Japan and South Korea among top Zendesk markets. Local payment methods critical for self-serve conversion.

**Key meeting angles:**
1. **$2B+ revenue, single processor** | Stripe is the only card processor. 97% auth is strong but 3% failure with no failover leaves millions on the table
2. **Active local acquiring in Brazil and India** | Zendesk is already investing in local entities. Yuno accelerates this without building per-market infrastructure
3. **$500M AI ARR at risk** | AI add-ons are the growth engine. Buyers in emerging markets need local payment methods to purchase
4. **173K+ customers in 160 countries, minimal APMs** | Cards, PayPal, and ACH cover basics. No Pix, UPI, SEPA DD, or regional methods
5. **$1.5M saved on Stripe migration** | Cost-conscious platform. Payment orchestration delivers further savings via routing optimization
6. **Billing support is a known pain point** | Community complaints about year-long disputes. Better payment infrastructure reduces support tickets
7. **Marketplace ecosystem stickiness** | 1,900+ apps, 85% of customers use integrations. Frictionless payments strengthen retention

**Sources:**
- [Stripe: Zendesk Case Study](https://stripe.com/customers/zendesk)
- [Zendesk: What Payment Methods Accepted](https://support.zendesk.com/hc/en-us/articles/4408837764122-What-forms-of-payment-does-Zendesk-accept)
- [Zendesk: Managing Payments](https://support.zendesk.com/hc/en-us/articles/4408821572506-Managing-payments)
- [Zendesk: Billing FAQ](https://support.zendesk.com/hc/en-us/articles/4408839289498-Billing-FAQ-and-resources)
- [Zendesk: Troubleshooting Payment Issues](https://support.zendesk.com/hc/en-us/articles/9317629048730-Troubleshooting-common-payment-issues)
- [Zendesk Community: Billing Support Complaint](https://support.zendesk.com/hc/en-us/community/posts/5545839866650-Zendesk-billing-support-is-the-worst-1-10)
- [Zendesk: Customers Page](https://www.zendesk.com/why-zendesk/customers/)
- [Zendesk: Wikipedia](https://en.wikipedia.org/wiki/Zendesk)
- [The AI Economy: Zendesk AI ARR $500M](https://theaieconomy.substack.com/p/zendesk-ai-arr-2026-growth)
- [Sacra: Zendesk Revenue & Valuation](https://sacra.com/c/zendesk/)
- [GetLatka: Zendesk Revenue](https://getlatka.com/blog/zendesk-revenue/)
- [SQ Magazine: Zendesk Statistics 2026](https://sqmagazine.co.uk/zendesk-statistics/)
- [Enlyft: Companies Using Zendesk](https://enlyft.com/tech/products/zendesk)
- [DataCaptive: Top Companies Using Zendesk](https://blog.datacaptive.com/top-companies-using-zendesk/)
- [AppDirect: Zendesk Ecosystem](https://www.appdirect.com/blog/ecosystems-in-action-zendesk)
- [Phrase: Zendesk Localization](https://phrase.com/customers/zendesk/)
- [Brandfetch: Zendesk Logo](https://brandfetch.com/zendesk.com)
