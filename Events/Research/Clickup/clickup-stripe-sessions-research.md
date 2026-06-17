# CLICKUP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: ClickUp
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/7/7b/ClickUp_logo.svg
Nombre merchant: ClickUp

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Payment Lock
Tittle_Pain Point_2: No PayPal Despite Demand
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: Cross-Border Decline Wall
Tittle_Pain Point_5: Zero Local Method Coverage

Desc_Pain Point_1: Only Visa, MC, Maestro, Amex, and Discover accepted. No wallets, no bank debits. With 20M+ users and 800K joining monthly, card-only checkout blocks conversions.
Desc_Pain Point_2: PayPal feature requests open for years, no resolution. ClickUp says "on the shortlist" but no timeline. Prepaid cards also rejected, blocking prepaid-dominant markets.
Desc_Pain Point_3: Single processor with no cascade. When a card declines, no alternative acquirer retry. $300M+ ARR and 100K paying customers, every failed renewal is permanent churn.
Desc_Pain Point_4: International users see higher declines when cards are issued outside the processor's country. Help docs tell users to call their bank, placing the burden on them.
Desc_Pain Point_5: Zero local methods in any market. No iDEAL, Pix, UPI, SEPA DD, or BLIK. 40% of customers outside the US and 275K+ European teams with no local options.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary card processing)
PSP_2: Cards only (Visa/MC/Maestro/Amex/Discover)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: SEPA Direct Debit
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: Bancontact
Local_M_9: KakaoPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $300M+ ARR, 100K paying customers across 200+ countries, and 40% international base, routing each renewal to the best acquirer per market delivers 3-10% auth uplift on subscriptions.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a subscription renewal. Instead of telling international users to "contact your bank," Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions retains ARR.
Desc_Yuno_Cap3: Activates methods ClickUp's global base demands: PayPal, iDEAL in Netherlands, SEPA DD across Europe, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, KakaoPay in Korea, GrabPay in SEA. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard replacing card-only processing with full orchestration. Real-time approval monitoring per country, centralized reconciliation for 275K+ European teams and global accounts, and NOVA fraud detection (75% reduction) protecting 100K+ paying organizations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ClickUp at a glance:**
- Founded: 2017 by Zeb Evans. HQ: San Diego, California
- Valuation: $4B (Series C, October 2021); estimated ~$6B in 2026
- Total funding: $535M across 4 rounds
- Key investors: Andreessen Horowitz, Tiger Global Management, Lightspeed Venture Partners, 468 Capital, HubSpot Ventures, Meritech Capital Partners
- ARR: $300M+ (September 2025); projected ~$500M by end of 2026
- Users: 20M+ worldwide, 800K new users joining monthly
- Paying customers: 100,000+
- Enterprise customers: Google, McDonald's, Booking.com, Netflix
- Employees: ~1,472 (87 sales reps, 100 engineering, 20 marketing)
- International: 40% of customers outside the US; 275,000+ European teams
- AI: Usage growing 800% YoY; 40%+ of new sales-led deals include AI; 400%+ AI sales growth
- Revenue model: Free, Unlimited ($7/user/mo), Business ($12/user/mo), Enterprise (custom)
- European expansion: New Ireland HQ for R&D, operations, and sales

**Confirmed Payment Stack:**
- Stripe: Inferred as primary payment processor (Stripe-related troubleshooting in help docs)
- Credit/debit cards: Visa, Mastercard, Maestro, American Express, Discover
- No PayPal (explicitly stated: "cannot process PayPal at this time")
- No prepaid debit cards accepted
- No digital wallets (Apple Pay, Google Pay)
- No bank debits (SEPA, ACH, BACS)
- No local APMs of any kind
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Community Evidence):**
- PayPal: Feature request open for years, ClickUp says "shortlist for upcoming features" but no timeline
- Prepaid debit cards: Explicitly not accepted, blocking users in prepaid-dominant markets
- Help docs on decline troubleshooting: "Contacting your bank's tier-two support for further troubleshooting and authorization resolves most payment issues" (burden placed on customer)
- Users advised to "leave the Zip Code field blank" as a troubleshooting step for international cards
- International card declines: "customers use cards issued in a different country than where the Stripe account is registered, they might see an increased rate of declines"
- Zero alternative payment methods beyond credit/debit cards

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (60% of customers, HQ)
  Accepted: Visa/MC/Amex/Discover
  Missing: PayPal, Apple Pay, Google Pay, ACH, Venmo
  Note: Card-only even in home market. No wallets, no bank debits. Single processor.

MARKET 2: Europe (275K+ teams, new Ireland HQ)
  Accepted: Visa/MC/Maestro/Amex
  Missing: PayPal, iDEAL (Netherlands), SEPA DD, Bancontact (Belgium), BLIK (Poland), GiroPay (Germany), Sofort
  Note: Investing heavily in European expansion but offering zero European payment methods. Localized product for France, Germany, Spain with no local payment options.

MARKET 3: Brazil / LATAM (growing productivity market)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of Brazilian digital payments. Card-only blocks self-serve adoption in all of LATAM.

MARKET 4: India / South Asia (large tech workforce)
  Accepted: Visa/MC (cross-border)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of Indian digital payments. Cross-border card declines are common, and ClickUp tells users to call their bank.

MARKET 5: Japan / APAC (enterprise presence, Netflix/Booking.com)
  Accepted: Visa/MC (cross-border)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: Enterprise customers like Booking.com signal APAC presence, but zero local methods for self-serve conversion.

**Key meeting angles:**
1. **$300M+ ARR with card-only checkout** | The most restrictive payment stack of any SaaS company this size. Zero non-card methods in any market.
2. **800K new users/month, card-only conversion** | Massive PLG funnel with the narrowest payment acceptance. Every missing method is thousands of lost upgrades monthly.
3. **40% international base, zero local methods** | Investing in Europe (Ireland HQ), localizing product, but no payment localization at all. 275K+ European teams with no SEPA, no iDEAL.
4. **PayPal demand, years unresolved** | Public feature requests with community votes. Confirmed on "shortlist" but no action. Signals payment infrastructure limitations.
5. **Cross-border decline blame on customer** | Help docs tell users to call their bank. Smart routing and failover solve this without customer effort.
6. **AI-driven growth surge** | 800% AI usage growth. 400% AI sales growth. Payment infrastructure must keep pace with explosive adoption.
7. **Competitor pressure** | Asana, Monday.com, and Notion accept broader payment methods. Payment acceptance is a competitive gap.

**Sources:**
- [ClickUp Help: Intro to Billing](https://help.clickup.com/hc/en-us/articles/9180575416215-Intro-to-billing)
- [ClickUp Help: Update Credit Card](https://help.clickup.com/hc/en-us/articles/6303292421399-Update-your-credit-card-information)
- [ClickUp Help: Troubleshoot Payment Issues](https://help.clickup.com/hc/en-us/articles/7558864862999-Troubleshoot-payment-issues)
- [ClickUp Feature Request: PayPal Payment Option](https://feedback.clickup.com/feature-requests/p/paypal-payment-option-for-clickup)
- [ClickUp Feature Request: Additional Payment Methods](https://feedback.clickup.com/feature-requests/p/add-additional-payment-methods)
- [ClickUp Canny: PayPal Request](https://clickup.canny.io/feature-requests/p/paypal-payment-option-for-clickup)
- [Knoji: Does ClickUp Accept PayPal?](https://clickup.knoji.com/questions/clickup-paypal/)
- [Yahoo Finance: ClickUp $300M ARR](https://finance.yahoo.com/news/clickup-accelerating-300-million-annual-130000796.html)
- [Sacra: ClickUp Revenue & Valuation](https://sacra.com/c/clickup/)
- [Getlatka: ClickUp Revenue](https://getlatka.com/companies/clickup)
- [Fueler: ClickUp Statistics 2026](https://fueler.io/blog/clickup-usage-revenue-valuation-growth-statistics)
- [Growth Letter: ClickUp $278.5M ARR](https://www.growth-letter.com/p/clickups-2785m-arr-plg-formula)
- [TechCrunch: ClickUp $400M Series C](https://techcrunch.com/2021/10/27/clickup-raises-400m-at-a-4b-valuation-to-expand-its-all-in-one-workplace-productivity-platform-to-europe/)
- [ClickUp: Brand Assets](https://clickup.com/brand)
- [Brandfetch: ClickUp Logo](https://brandfetch.com/clickup.com)
