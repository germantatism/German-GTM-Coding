# OURA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Oura
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idtHPmMZhj/idz1smtQLY.svg
Nombre merchant: Oura

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock-In
Tittle_Pain Point_2: Subscription Churn Leak
Tittle_Pain Point_3: New Market Blind Spots
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: Checkout Drop-Off

Desc_Pain Point_1: Shopify Payments (Stripe) is the sole acquirer for all DTC sales. Any outage or rate dip blocks 100% of ring purchases and renewals in 30+ markets.
Desc_Pain Point_2: 2M+ subscribers at $5.99/mo renew on a single processor. Expired cards and soft declines churn paying members with no automatic retry across a second acquirer.
Desc_Pain Point_3: Oura launched India, Mexico, and UAE in 2026 but offers zero local APMs. No UPI in India, no OXXO in Mexico, no Mada in UAE. Only Visa/MC/Amex at checkout.
Desc_Pain Point_4: Rings ship from Finland with USD/EUR settlement. Buyers in India, Mexico, UAE, and Australia absorb cross-border FX markup on every ring purchase and renewal.
Desc_Pain Point_5: Facebook community posts report repeated checkout rejections. Oura's own support flags 3DS friction and card security blocks as top purchase failure reasons.

SLIDE 1: PSP TOPOLOGY

PSP_1: Shopify Payments (Stripe)
PSP_2: PayPal
PSP_3: Affirm
PSP_4: Apple Pay
PSP_5: Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: OXXO
Local_M_3: Pix
Local_M_4: Mada
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: Konbini
Local_M_8: BLIK
Local_M_9: Boleto
Local_M_10: SPEI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every ring purchase and membership renewal to the best performing acquirer per card BIN, country, and issuer. With $1B+ revenue and 2M+ subscribers, a 3% auth uplift recovers $30M+ annually without touching checkout UX or Shopify stack.
Desc_Yuno_Cap2: When Shopify Payments declines a membership renewal, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly cutting involuntary churn on Oura's fastest growing revenue line.
Desc_Yuno_Cap3: Unlocks the local methods Oura's new markets demand: UPI in India (500M+ users), OXXO/SPEI in Mexico, Mada in UAE, iDEAL in Netherlands, BLIK in Poland, Pix in Brazil. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating Shopify Payments, PayPal, Affirm, Apple Pay, and Google Pay into one view. Real-time auth rate monitoring across every PSP and market, centralized reconciliation, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Oura at a glance:**
- 5.5M+ rings sold lifetime; 2.7M+ sold in 2024 alone (half of all-time sales)
- Revenue: $1B in 2025 (doubled from $500M in 2024), targeting ~$1.5B to $2B in 2026
- Revenue mix: ~80% hardware, ~20% subscription ($5.99/mo or $69.99/yr)
- 2M+ paying subscribers (end 2024), growing rapidly
- Valuation: $11B (Series E, October 2025, led by Fidelity), raised $900M
- HQ: Oulu, Finland / San Francisco, CA
- CEO: Tom Hale (ex-Momentive, joined March 2022)
- Products: Oura Ring 4, Oura Ring 4 Ceramic, Oura Membership

**Confirmed PSPs:**
- Shopify Payments (powered by Stripe): primary card acquirer for DTC store
- PayPal: secondary payment option at checkout
- Affirm: BNPL financing for ring purchases
- Apple Pay / Google Pay: digital wallet options
- Klarna: referenced in privacy policy code for UK/DE, not publicly listed
- No payment orchestrator detected
- Headless commerce stack: Next.js + Vercel + Shopify Plus + Contentful

**International Expansion (2026):**
- Launched in Australia, New Zealand, India, Mexico, UAE in early 2026
- Previously available: US, Canada, UK, Germany, France, Italy, Finland, Sweden, Norway, Denmark, Netherlands, Belgium, Austria, Spain, Ireland, Japan
- Retail partners: Target, Amazon, Best Buy (US), JB Hi-Fi/Harvey Norman (AU), Croma/Amazon (India), Liverpool (Mexico), Go Sport/Virgin Megastores/Dubai Duty Free (UAE)

**Top Markets Gap Analysis:**

MARKET 1: United States (~55% of revenue)
  Offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Affirm
  Missing: ACH Direct Debit, Cash App Pay, Venmo (standalone)
  Affirm handles BNPL but no native debit option for subscription billing

MARKET 2: India (new 2026, massive TAM)
  Offer: Visa/MC/Amex only
  Missing: UPI, RuPay, Paytm, PhonePe
  75%+ of Indian digital payments are UPI. Credit card penetration ~5%. Without UPI, vast majority cannot subscribe.

MARKET 3: Mexico (new 2026)
  Offer: Visa/MC/Amex via Liverpool + online
  Missing: OXXO, SPEI, CoDi
  60%+ of Mexicans are unbanked. OXXO processes 55M+ transactions/month. No cash voucher = no mass market.

MARKET 4: UAE (new 2026)
  Offer: Visa/MC/Amex
  Missing: Mada, Apple Pay (local), STC Pay, Tabby
  Mada is the national debit network in the Gulf region.

MARKET 5: Germany (~5% of traffic)
  Offer: Visa/MC, PayPal, Klarna (in code, not visible)
  Missing: SEPA Direct Debit, Giropay, Sofort
  ~35% credit card penetration. SEPA DD is the standard for subscription billing in DACH.

**Payment issues documented:**
- Facebook community group: multiple posts reporting checkout rejections ("Oura ring checkout error issue?")
- Oura support explicitly documents 3DS friction and card security blocks as common problems
- BBB complaints include billing and payment processing issues
- Subscription renewal failures with no automated recovery path visible

**Key meeting angles:**
1. **Subscription revenue protection**: 2M+ subscribers with zero failover on renewals = involuntary churn risk
2. **New market activation**: India/Mexico/UAE launched with zero local APMs; hardware is there, payment rails are not
3. **IPO trajectory**: $11B valuation, $2B 2026 target; payment infrastructure is investor diligence material
4. **DTC margin optimization**: Smart Routing across Shopify Payments + alternate acquirers lifts auth rates 3-10%
5. **Headless architecture fit**: Oura already runs headless Shopify + Next.js; Yuno API integrates without re-platforming
6. **Competitor benchmark**: Apple Watch accepts local APMs in 40+ markets; Oura accepts cards only

**Sources:**
- [Oura Membership](https://support.ouraring.com/hc/en-us/articles/4409086524819-Oura-Membership)
- [Oura Supported Countries](https://support.ouraring.com/hc/en-us/articles/41056787356307-Supported-Countries)
- [Oura Global Expansion Blog](https://ouraring.com/blog/oura-global-expansion/)
- [Oura Privacy Policy](https://ouraring.com/privacy-policy)
- [Oura Purchase Help](https://support.ouraring.com/hc/en-us/articles/360052018753-Purchase-an-Oura-Product)
- [Oura Affirm Financing](https://support.ouraring.com/hc/en-us/articles/360059513293-Finance-Your-Purchase-with-Affirm)
- [Oura Declined Payments (Organizations)](https://partnersupport.ouraring.com/hc/en-us/articles/18674459285651-Declined-Payments)
- [Oura BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/jewelry-designers/oura-ring-1116-928639/complaints)
- [Oura Facebook Community: Checkout Error](https://www.facebook.com/groups/945310367310036/posts/1365314301976305/)
- [Oura Facebook Community: Payment Issues](https://www.facebook.com/groups/945310367310036/posts/1317582890082780/)
- [CNBC: Oura $11B Valuation](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html)
- [CNBC: Oura $2B 2026 Sales](https://www.cnbc.com/2025/11/11/smart-ring-maker-oura-expects-close-to-2-billion-in-2026-sales-ceo.html)
- [BusinessWire: Oura 5.5M Rings Sold](https://www.businesswire.com/news/home/20250922351288/en/URA-Surpasses-5.5-Million-Rings-Sold-and-Doubles-Revenue-for-the-Second-Year-in-a-Row-Empowering-Millions-to-Live-Better-Longer)
- [Sacra: Oura Revenue](https://sacra.com/c/oura/)
- [Commerce-UI: Oura Headless Shopify Case Study](https://commerce-ui.com/work/oura-website)
- [DigitalSuits: Oura Headless Ecommerce](https://digitalsuits.co/case-studies/headless-e-commerce-platform-for-oura/)
- [Brandfetch: Oura Logo](https://brandfetch.com/ouraring.com)
