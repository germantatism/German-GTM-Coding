# WELLHUB | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Wellhub
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idfDTLbMpP/idOX2GJVwi.svg
Nombre merchant: Wellhub

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 13-Country Payment Maze
Tittle_Pain Point_2: Subscription Churn Leak
Tittle_Pain Point_3: LATAM APM Gaps
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: B2B + B2C Billing Split

Desc_Pain Point_1: Wellhub operates across 13 countries (US, Canada, UK, Ireland, Brazil, Mexico, Argentina, Chile, Spain, Germany, Portugal, Italy) with no visible payment orchestrator. Each market likely uses separate acquiring setups with no unified routing.
Desc_Pain Point_2: 2M+ employee subscribers pay monthly via credit/debit cards. When a renewal fails, Wellhub retries for 30 days then cancels the plan. No automated cascade to a second acquirer means every soft decline is a lost subscriber.
Desc_Pain Point_3: Four LATAM markets (Brazil, Mexico, Argentina, Chile) but only cards accepted on web. No confirmed Pix in Brazil, no OXXO/SPEI in Mexico, no Rapipago in Argentina. Cash and local debit dominate these economies.
Desc_Pain Point_4: US-headquartered entity processing subscriptions across 13 countries. Employees in Brazil, Mexico, Argentina, and Chile absorb cross-border interchange markup on every monthly renewal charge.
Desc_Pain Point_5: B2B corporate invoicing and B2C employee subscriptions run through different channels. No single view across corporate payments, employee card charges, and paycheck deductions creates reconciliation complexity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Primary)
PSP_2: Apple Pay
PSP_3: Credit/Debit Cards
PSP_4: Paycheck Deduction
PSP_5: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: Boleto
Local_M_5: Rapipago
Local_M_6: SEPA Direct Debit
Local_M_7: iDEAL
Local_M_8: Bancontact
Local_M_9: Bizum
Local_M_10: MB Way

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every employee subscription charge to the best performing acquirer per card BIN, country, and issuer across 13 markets. With $319M+ revenue and 2M+ subscribers, a 3-10% auth uplift recovers millions annually without touching any existing integration.
Desc_Yuno_Cap2: When a renewal fails, Yuno cascades to an alternate acquirer in milliseconds instead of waiting 30 days to cancel. Recovers up to 50% of failed recurring charges, directly cutting involuntary churn across Wellhub's corporate subscriber base.
Desc_Yuno_Cap3: Unlocks the local methods Wellhub's 13-country footprint demands: Pix/Boleto in Brazil, OXXO/SPEI in Mexico, Rapipago in Argentina, SEPA DD in Europe, Bizum in Spain, MB Way in Portugal. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating B2B corporate payments and B2C employee subscriptions across all 13 markets. Real-time auth rate monitoring per country, centralized reconciliation, and millisecond anomaly detection via NOVA replaces fragmented multi-market management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Wellhub at a glance:**
- Founded: 2012 (as Gympass); rebranded to Wellhub in August 2024
- CEO: Cesar Carvalho (Co-Founder, originally from Brazil, based in New York)
- HQ: New York City (Union Square)
- Valuation: $2.4B (Series F, August 2023)
- Total funding raised: $605-868M (varies by source)
- Revenue: $319M (September 2025)
- Subscribers: 2M+ employee subscribers
- Corporate clients: 26,000+ (including Amazon, Oracle, Accenture, KPMG, Santander, Unilever, Aflac)
- Partner network: 50,000+ fitness and wellness partners
- Countries: 13 (US, Canada, UK, Ireland, Brazil, Mexico, Argentina, Chile, Spain, Germany, Portugal, Italy + 1 more)
- Employees: ~2,215 (Dec 2025)
- Engineering: 500+ engineers across 3 tech hubs (Brazil, Portugal, US)
- Products: Corporate wellness platform, gym access, wellness apps, therapy, nutrition, sleep
- Plan tiers: Starter through Premium, priced per employee per month

**Confirmed PSPs/Payment Methods:**
- Credit and debit cards: primary payment method across all markets
- Apple Pay: accepted for subscriptions
- Paycheck deduction: available where employer enables it
- No specific PSP publicly confirmed (Stripe inferred from Stripe Sessions attendance)
- No payment orchestrator detected
- Help Center documents payment decline handling with 30-day retry window before plan cancellation

**Payment issues documented:**
- BBB complaints: double billing, unauthorized charges after pause/cancellation
- "Pause" feature continues charging; reactivates in 30 days without notification
- No customer service phone number; AI chatbot only
- Users report being billed for services they did not select
- Accounts blocked when payments are disputed, preventing account management
- Payment decline retry is automated but only for 30 days, then plan is canceled
- Temporary virtual cards cause recurring payment failures

**Top Markets Gap Analysis:**

MARKET 1: United States (largest market)
  Offer: Visa/MC/Amex, Apple Pay, paycheck deduction
  Missing: ACH Direct Debit, Google Pay, Cash App Pay
  Solid coverage but missing direct bank payment option for recurring billing

MARKET 2: Brazil (origin market, massive TAM)
  Offer: Credit/debit cards
  Missing: Pix, Boleto Bancario
  Pix handles 45B+ transactions/year. Without it, unbanked/underbanked employees cannot subscribe

MARKET 3: Mexico (LATAM growth market)
  Offer: Credit/debit cards only
  Missing: OXXO, SPEI, CoDi
  60%+ unbanked population. OXXO processes 55M+ transactions/month

MARKET 4: Argentina (LATAM market)
  Offer: Credit/debit cards only
  Missing: Rapipago, Pago Facil, Mercado Pago
  Cash payment networks dominate consumer transactions

MARKET 5: Spain (European market)
  Offer: Credit/debit cards
  Missing: Bizum, SEPA Direct Debit
  Bizum has 27M+ registered users in Spain (60%+ of population)

**Key meeting angles:**
1. **13-country complexity**: Each market has different acquiring needs. Yuno centralizes routing, reconciliation, and monitoring across all 13 countries in one dashboard
2. **LATAM origin story**: Wellhub was founded in Brazil but has no confirmed local APMs in any LATAM market. Pix, OXXO, and Rapipago unlock the unbanked employee segment
3. **Enterprise scale**: 26,000 corporate clients, 2M+ subscribers, $319M revenue. Payment failures at this scale directly impact client retention and NPS
4. **30-day retry gap**: Current retry logic waits 30 days to cancel. Smart Routing + Failover resolves failed charges in milliseconds, not months
5. **IPO trajectory**: $2.4B valuation with strong growth. Payment infrastructure optimization is investor diligence material
6. **B2B/B2C convergence**: Corporate invoicing and employee billing need unified visibility. Yuno orchestrates both channels under one roof

**Sources:**
- [Wellhub Payment Methods Help Center](https://helpcenter.gympass.com/en-us/articles/what-payment-methods-are-available-for-your-wellhub-subscription)
- [Wellhub Payment Declined Help](https://helpcenter.gympass.com/en-us/articles/how-to-prevent-your-subscription-payment-from-being-declined)
- [Wellhub Subscription Payment Help](https://helpcenter.gympass.com/en-us/articles/how-does-the-payment-work)
- [Wellhub About Us](https://wellhub.com/en-us/about/)
- [Wellhub Series F Funding](https://wellhub.com/en-us/blog/press-releases/gympass-raises-series-f-funding/)
- [Wellhub Rebrand Announcement](https://wellhub.com/en-us/blog/press-releases/wellhub-makes-every-company-a-wellness-company/)
- [Wellhub Revenue - GetLatka](https://getlatka.com/companies/wellhub.com)
- [Wellhub Wikipedia](https://en.wikipedia.org/wiki/Wellhub)
- [Fortune: Wellhub CEO Cesar Carvalho](https://fortune.com/2025/07/23/wellhub-ceo-cesar-carvalho-billion-dollar-wellness-platform-lifestyle-mckinsey-harvard-business-school-corporate-america/)
- [Wellhub BBB Complaints](https://www.bbb.org/us/ny/new-york/profile/internet-service/wellhub-0121-87144588/complaints)
- [Wellhub Tracxn Profile](https://tracxn.com/d/companies/wellhub/__I6U-Liifj_wvn1Hxv0sdmgCYRGCsqbw7eWTxwkcEfLs)
- [Wellhub International Travel Help](https://helpcenter.gympass.com/en-us/articles/is-it-possible-to-use-gympass-while-traveling)
- [Brandfetch: Wellhub Logo](https://brandfetch.com/wellhub.com)
