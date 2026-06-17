# GAMMA AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Gamma AI
=======================================

Logo: https://asset.brandfetch.io/id3MVif4x0/idL0iThUdI.svg
Nombre merchant: Gamma

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: USD-Centric Billing
Tittle_Pain Point_3: Limited APM Reach
Tittle_Pain Point_4: Subscription Churn Risk
Tittle_Pain Point_5: Enterprise Invoice Gap

Desc_Pain Point_1: Stripe is the sole payment processor for 70M users and $100M+ ARR. Checkout, Billing, Invoicing, Adaptive Pricing, and Link all flow through one provider. Zero acquirer redundancy means every Stripe outage blocks new sign-ups, upgrades, and renewals globally.
Desc_Pain Point_2: Prices listed in USD and converted at checkout via Stripe Adaptive Pricing. Users in India, Brazil, Southeast Asia, and Africa absorb FX markups from their banks, inflating the effective price. Majority of revenue comes from outside the US, amplifying this friction.
Desc_Pain Point_3: Stripe enables UPI (India) and SEPA Debit (Europe), but 70M global users span 190+ countries. No Pix for Brazil, no GCash for Philippines, no M-Pesa for Africa, no Boleto, no BLIK, no local wallets across Southeast Asia where AI tool adoption is exploding.
Desc_Pain Point_4: $100M+ ARR from subscriptions across Plus ($8), Pro ($18), Team ($20), Business ($40), and Ultra ($100) tiers. Card expiration, issuer declines, and currency conversion failures erode revenue. Stripe Link handles 40% of volume but no multi-acquirer retry path for failures.
Desc_Pain Point_5: Gamma recently launched Stripe Invoicing for sales-led enterprise deals with custom contracts. Scaling B2B billing across geographies requires local tax compliance (VAT, GST, digital services taxes), local payment methods (bank transfers in Germany, invoice pay in Japan), and multi-currency invoicing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Checkout (self-serve subscriptions)
PSP_2: Stripe Billing (subscription management)
PSP_3: Stripe Invoicing (enterprise contracts)
PSP_4: Stripe Adaptive Pricing (local currency)
PSP_5: Stripe Link (40%+ of payment volume)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: GCash (Philippines)
Local_M_4: GrabPay (Southeast Asia)
Local_M_5: M-Pesa (Africa)
Local_M_6: BLIK (Poland)
Local_M_7: Konbini (Japan)
Local_M_8: OXXO (Mexico)
Local_M_9: iDEAL (Netherlands)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription charge to the highest-performing acquirer by card BIN, issuer, and country. With $100M+ ARR from 70M users spanning 190+ countries, even a 3% auth uplift recovers $3M+ in annual revenue. Smart Routing maximizes approval rates in markets like India, Brazil, and Southeast Asia where local acquiring outperforms cross-border processing.
Desc_Yuno_Cap2: Automatic cascade removes Gamma's sole Stripe dependency. When Stripe declines a subscription renewal or upgrade, Yuno reroutes to the next best acquirer in milliseconds, recovering failed transactions with zero user friction. Up to 50% recovery on soft declines across millions of monthly subscription charges worldwide.
Desc_Yuno_Cap3: Activates the APMs Gamma's global user base needs: Pix in Brazil, GCash and GrabPay in Southeast Asia, M-Pesa in Africa, Konbini in Japan, BLIK in Poland, iDEAL in Netherlands, OXXO in Mexico. One API, 1,000+ payment methods. Converts free users to paid in markets where cards are not the dominant payment method.
Desc_Yuno_Cap4: One dashboard consolidating Stripe Checkout, Billing, Invoicing, Adaptive Pricing, and Link into a unified view alongside additional acquirers and local payment methods. Real-time approval rate monitoring across all 190+ markets, centralized tax compliance and reconciliation. Full visibility as Gamma scales enterprise sales globally.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gamma at a glance:**
- AI-powered presentation, document, and website builder platform
- Founded early 2020s by Grant Lee, James Fox, and Jon Noronha
- HQ: San Francisco, California. ~318 employees (March 2026), was just 50 at Series B
- Revenue: $100M+ ARR (November 2025). Profitable for 2+ years
- Valuation: $2.1B (Series B, November 2025). Total funding: $87M over 3 rounds
- Investors: Andreessen Horowitz (lead Series B), Accel, Uncork Capital
- 70M users globally. Majority of revenue from outside the United States
- Products: AI presentations, documents, webpages, and visual content
- Pricing tiers: Free, Plus ($8/user/mo), Pro ($18), Team ($20), Business ($40), Ultra ($100)
- AI credit-based usage model combined with subscription tiers
- 28% discount on annual billing vs monthly
- Competes with Microsoft PowerPoint, Google Slides, Canva, Beautiful.ai, Tome

**Confirmed PSPs and Infrastructure (official Stripe case study):**
- Stripe Checkout: prebuilt checkout page, 30+ languages, AI-powered payment method selection
- Stripe Billing: subscription management for individuals and businesses
- Stripe Invoicing: recently launched for sales-led enterprise deals with custom contracts
- Stripe Adaptive Pricing: automatic local currency display at checkout
- Stripe Link: consumer wallet, handles 40%+ of Gamma's total payment volume
- Stripe Radar: fraud prevention (implied)
- Accepted: credit/debit cards, UPI (India), SEPA Debit (Europe)
- No payment orchestrator detected
- No secondary acquirer identified
- Stripe is sole payment infrastructure provider

**Accepted payment methods:**
- Credit/debit cards: Visa, Mastercard, Amex (via Stripe)
- SEPA Direct Debit (Europe)
- UPI (India)
- Stripe Link wallet (40%+ of volume)
- Prices in USD, converted to local currency via Stripe Adaptive Pricing
- No Pix, Boleto, M-Pesa, GCash, GrabPay, BLIK, Konbini, OXXO, or iDEAL

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (HQ market)
  Accepted: Visa/MC/Amex, Stripe Link
  Missing: Cash App Pay, Venmo, Apple Pay
  Note: Well served via Stripe. Link adoption at 40%+ is strong

MARKET 2: India (major growth market)
  Accepted: Visa/MC, UPI
  Missing: Paytm, PhonePe wallet, RuPay, Net Banking, INR localized pricing
  Note: UPI enabled via Stripe. India is likely a top 3 market given 70M global users

MARKET 3: Brazil (high-growth AI market)
  Accepted: Visa/MC (cross-border, USD)
  Missing: Pix, Boleto, BRL pricing, installments (parcelamento)
  Note: Pix handles 70%+ of digital payments in Brazil. Major conversion barrier

MARKET 4: Europe (significant user base)
  Accepted: Visa/MC, SEPA Debit
  Missing: iDEAL (NL), BLIK (PL), Bancontact (BE), Klarna, local EUR pricing
  Note: SEPA Debit enabled. But country-specific methods missing in key markets

MARKET 5: Southeast Asia (fast-growing AI adoption)
  Accepted: Visa/MC (cross-border)
  Missing: GCash (PH), GrabPay, OVO (ID), DANA (ID), PromptPay (TH)
  Note: Card penetration below 20% in most SEA markets. Local wallets are essential

**Key meeting angles:**
1. **Stripe-only with $100M+ ARR** | Every dollar of revenue flows through Stripe. Zero redundancy for a $2.1B unicorn serving 70M users globally
2. **Majority of revenue from outside US** | International users face FX markups, limited APMs, and USD-only pricing. Local acquiring would improve approval rates and conversion
3. **40% of volume via Stripe Link** | Heavy reliance on a single wallet. Multi-wallet strategy (Apple Pay, Google Pay, local wallets) would reduce concentration risk
4. **Enterprise motion just starting** | Stripe Invoicing recently launched for sales-led deals. B2B expansion requires local tax compliance, bank transfers, and multi-currency invoicing
5. **70M users, low paid conversion** | $100M ARR / 70M users = ~$1.43 ARPU. Enabling local payment methods in emerging markets would lift free-to-paid conversion in high-growth regions
6. **AI tool competition intensifying** | Canva, Beautiful.ai, Microsoft Copilot all expanding AI presentation capabilities. Payment friction in emerging markets hands free users to competitors
7. **Profitable and capital-efficient** | Only $87M raised, profitable for 2+ years. Payment optimization directly flows to bottom line

**Sources:**
- [Stripe: Gamma and Stripe Partnership](https://stripe.com/newsroom/news/gamma-and-stripe)
- [Gamma Wikipedia](https://en.wikipedia.org/wiki/Gamma_(app))
- [TechCrunch: Gamma $2.1B Valuation](https://techcrunch.com/2025/11/10/ai-powerpoint-killer-gamma-hits-2-1b-valuation-100m-arr-founder-says/)
- [BusinessWire: Gamma $100M ARR](https://www.businesswire.com/news/home/20251110805751/en/Gamma-Surpasses-$100M-ARR-Raises-at-$2.1B-Valuation-as-It-Replaces-PowerPoint-for-the-AI-Era)
- [Gamma Pricing Page](https://gamma.app/pricing)
- [Gamma About Page](https://gamma.app/about)
- [Sacra: Gamma Revenue](https://sacra.com/c/gamma/)
- [Tracxn: Gamma Company Profile](https://tracxn.com/d/companies/gamma/__fU9G1eXiWu7iez1HO_-6ZN7vBNibrpNO-Q621b8JYqU)
- [Gamma Blog: How We Built $100M Business](https://gamma.app/insights/how-we-built-a-usd100m-business-differently)
- [Brandfetch: Gamma Logo](https://brandfetch.com/gamma.app)
