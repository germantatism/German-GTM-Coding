# POSTMAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Postman
=======================================

Logo: https://asset.brandfetch.io/idmWS3Oze5/idYBOCqUEN.svg
Nombre merchant: Postman

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Exposure
Tittle_Pain Point_2: No Local APMs Globally
Tittle_Pain Point_3: Free-to-Paid Conversion
Tittle_Pain Point_4: US-Only Direct Debit
Tittle_Pain Point_5: FX Markup on Renewals

Desc_Pain Point_1: Stripe is the sole payment processor for all Postman subscriptions. Any outage or decline spike blocks signups and renewals for 500,000+ organizations, including 98% of the Fortune 500, across Solo, Team, and Enterprise tiers simultaneously.
Desc_Pain Point_2: 40M+ developers in 190+ countries but checkout accepts only credit cards globally. No UPI for India (15% of customers), no SEPA DD for Europe, no Pix for Brazil. Developers in card-averse markets hit a paywall at upgrade.
Desc_Pain Point_3: Converting free users to paid has "taken longer than expected." Cards-only checkout in markets where 60%+ of developers prefer local payment methods creates unnecessary friction at the exact moment of purchase intent.
Desc_Pain Point_4: ACH direct debit is available only in the United States. Enterprise customers in Europe, India, Japan, and LATAM cannot use bank debit for recurring billing, forcing manual wire transfers or credit card dependency.
Desc_Pain Point_5: Pricing is in USD only. Developers and organizations in India, Japan, Europe, Brazil, and the UK absorb cross-border FX fees on every monthly or annual renewal, inflating the effective cost of Solo ($9), Team ($19), and Enterprise ($99) plans.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Apple Pay (via Stripe)
PSP_3: Google Pay (via Stripe)
PSP_4: ACH Direct Debit (US only)
PSP_5: Wire Transfer (Enterprise only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: SEPA Direct Debit
Local_M_3: Pix
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Konbini
Local_M_8: OXXO
Local_M_9: SPEI
Local_M_10: Boleto

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge and renewal to the best performing acquirer per card BIN, country, and issuer. With $313M+ revenue and 500,000+ paying organizations, a 3-10% auth uplift on renewals recovers millions annually across Solo, Team, and Enterprise tiers.
Desc_Yuno_Cap2: When Stripe declines a Team or Enterprise subscription renewal, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly cutting involuntary churn for high-value enterprise accounts worth $99/user/month.
Desc_Yuno_Cap3: Unlocks the local methods 40M+ developers worldwide need: UPI in India (15% of customer base, 500M+ UPI users), SEPA DD in Europe, Pix in Brazil, Konbini in Japan (400K+ developers), iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ payment methods, accelerating free-to-paid conversion.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe, Apple Pay, Google Pay, ACH, and wire transfer flows into one view. Real-time auth rate monitoring across every market and plan tier, centralized reconciliation, and NOVA provides millisecond anomaly detection to protect enterprise renewal cycles.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Postman at a glance:**
- Founded: 2014 in Bangalore, India (incorporated in San Francisco)
- Co-Founders: Abhinav Asthana (CEO), Ankit Sobti (CTO), Abhijit Kane
- HQ: San Francisco, CA; Offices: Bangalore, Boston, New York City, Tokyo
- Valuation: $5.6B (Series D, August 2021); secondary market estimated ~$3.2B in 2026
- Total funding raised: $434M across 6 rounds (Nexus Venture Partners, CRV, Insight Partners, Coatue, Battery Ventures, BOND)
- Revenue: $313M in 2024 (+82% YoY); projected $450-500M+ by end of 2025
- Revenue growth: 37x over 6 years ($8.4M in 2018 to $313M in 2024)
- Users: 40M+ developers globally (up to 33M registered as of 2026 report; 40M cited in March 2026 announcement)
- Organizations: 500,000+ companies, including 98% of the Fortune 500
- Employees: ~273 (as of August 2025)
- Products: API Platform (design, build, test, collaborate), AI-native platform (March 2026), API Catalog, Postman Flows
- Acquisitions: liblab (SDK generation), Fern (SDK tooling, Dec 2025), Orbit (developer communities)
- New plans (March 2026): Free (1 user), Solo ($9/mo), Team ($19/user/mo), Enterprise ($99/user/mo)

**Confirmed PSPs:**
- Stripe: sole payment processor for all subscription billing (confirmed in billing docs: "payment provider Stripe")
- Apple Pay: available for certain payment scenarios (via Stripe)
- Google Pay: available for certain payment scenarios (via Stripe)
- ACH Direct Debit: US customers only, processed through Stripe
- Wire Transfer: Enterprise invoice-based teams only
- No secondary PSP detected
- No payment orchestrator detected

**Billing details:**
- Payment methods: Credit card (global), ACH direct debit (US only), Apple Pay, Google Pay
- Currency: USD only
- Invoice customization: Company name, billing email, address, VAT ID
- Failed payments: Auto-retried on saved payment method
- Enterprise: Can pay via wire transfer or ACH on invoice basis
- Stripe handles all payment data; Postman stores no card information

**Key payment gaps identified:**
- Cards-only checkout for 40M+ global developers; no local payment methods
- India is 15% of customer base (3,191 organizations, 400K+ developers) but no UPI
- Japan has 400K+ developers and 82% of Nikkei 225 using Postman but no Konbini or PayPay
- ACH only for US; no SEPA DD for European enterprise customers
- USD-only pricing creates FX drag in every non-US market
- Free-to-paid conversion underperforming expectations; payment friction is a contributing factor

**Top Markets Gap Analysis:**

MARKET 1: United States (49.56% of customers, ~10,360 orgs)
  Offer: Visa/MC via Stripe, ACH, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo
  Best-served market; ACH available for subscription billing

MARKET 2: India (15.27% of customers, ~3,191 orgs)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: UPI, Netbanking, Paytm, RuPay
  UPI has 500M+ users; most Indian developers prefer UPI for digital purchases

MARKET 3: United Kingdom (8.52% of customers, ~1,781 orgs)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: Open Banking, PayByBank, GBP pricing
  UK developers pay FX on every renewal; no bank debit option

MARKET 4: Japan (office in Tokyo, 400K+ developers)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: Konbini, PayPay, LINE Pay, JCB optimization
  82% of Nikkei 225 uses Postman; local methods critical for expansion

MARKET 5: Germany / Europe (significant developer community)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: SEPA Direct Debit, Giropay, iDEAL, BLIK
  SEPA DD is standard for SaaS subscriptions in Europe; ~35% card penetration in Germany

**Key meeting angles:**
1. **Free-to-paid conversion**: 40M developers, 500K orgs, but conversion has underperformed. Adding UPI, SEPA DD, Pix at checkout removes friction at the exact moment of purchase intent.
2. **India is 15% of the business**: Second-largest market by customers. UPI alone could materially lift conversion in a market where 85%+ of digital payments use UPI.
3. **Revenue protection at scale**: $313M+ revenue through a single processor. Failover to an alternate acquirer protects enterprise renewals worth $99/user/month.
4. **Japan enterprise opportunity**: 82% of Nikkei 225 on Postman, Tokyo office, 400K+ developers. Konbini and PayPay acceptance unlocks deeper enterprise penetration.
5. **Developer-first DNA**: Postman serves the developer community; payment orchestration via API (Yuno's model) aligns perfectly with their technical buyer persona.
6. **$500M ARR trajectory**: At 82% YoY growth, every percentage point of conversion improvement translates to millions in additional revenue.

**Sources:**
- [Postman Official Website](https://www.postman.com/)
- [Postman About Page](https://www.postman.com/company/about-postman/)
- [Postman Billing Documentation](https://learning.postman.com/docs/billing/billing)
- [Postman Purchase Documentation](https://learning.postman.com/docs/billing/buying)
- [Postman Pricing Page](https://www.postman.com/pricing/)
- [Postman Series D $225M at $5.6B - TechCrunch](https://techcrunch.com/2021/08/18/api-platform-postman-valued-at-5-6-billion-in-225-million-fundraise/)
- [Postman $313M Revenue 2024 - Getlatka](https://getlatka.com/companies/postman)
- [Postman Valuation 2026 - PremierAlts](https://www.premieralts.com/companies/postman/valuation)
- [Postman Investor Report 2026 - VFS](https://valueforstartups.in/postman_report)
- [Postman Financials - Affluense](https://www.affluense.ai/company/postman-financials-4836dc)
- [Postman Claude Integration - BusinessWire](https://www.businesswire.com/news/home/20260331672097/en/Postman-Integrates-Anthropics-Claude-on-Amazon-Bedrock-to-Bring-AI-Native-API-Development-to-40-Million-Developers)
- [Postman New Plans March 2026 - Blog](https://blog.postman.com/new-capabilities-march-2026/)
- [Postman Market Share - 6sense](https://6sense.com/tech/api-management/postman-market-share)
- [Postman Wikipedia](https://en.wikipedia.org/wiki/Postman_(software))
- [Postman Valuation Plunge - The Arc](https://www.thearcweb.com/article/postman-valuation-plunges-40-in-secondary-market-faQV7VkMLbUivVGt)
- [Brandfetch: Postman Logo](https://brandfetch.com/postman.com)
- [Postman - Tracxn](https://tracxn.com/d/companies/postman/__5xdlPCDqiJBrCfWaFC6jpq_1zwxQ_9rsAK3jz5bhWd4)
