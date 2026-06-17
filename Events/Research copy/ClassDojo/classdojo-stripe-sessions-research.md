# CLASSDOJO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ClassDojo
=======================================

Logo: https://brandfetch.com/classdojo.com
Nombre merchant: ClassDojo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Three-Channel Payment Split
Tittle_Pain Point_2: 180 Countries, Zero APMs
Tittle_Pain Point_3: App Store Fee Leakage
Tittle_Pain Point_4: Churn from Failed Renewals
Tittle_Pain Point_5: School Payments Gap

Desc_Pain Point_1: Parent subscriptions split across Stripe (web), Apple App Store, and Google Play with no unified view. Each channel has different refund policies, billing cycles, and fee structures. With hundreds of thousands of paying families, ClassDojo reconciles revenue across three disconnected payment rails with no single orchestration layer.
Desc_Pain Point_2: ClassDojo operates in 180 countries reaching 51M+ students, but subscriptions accept only credit cards via Stripe or app store billing. Parents in Europe cannot pay with SEPA Direct Debit or iDEAL. LATAM families lack Pix, OXXO, or Boleto options. No local payment methods means capping conversion in markets where 25%+ of teachers already use the platform.
Desc_Pain Point_3: Apple and Google take 15 to 30% commission on in-app subscription purchases. At $7.99/month or $59.99/year, app store fees consume $1.20 to $2.40 per monthly subscriber. Shifting parents from app store billing to direct web checkout via Stripe saves 12 to 27% margin per subscription, but ClassDojo has no routing logic to optimize this.
Desc_Pain Point_4: ClassDojo uses Churn Buster for billing reminders but has no multi-acquirer retry cascade. When a parent's stored card expires or is declined on Stripe, the subscription fails with no automatic reroute through an alternate processor. Every failed renewal on hundreds of thousands of paying families is lost revenue with no recovery path.
Desc_Pain Point_5: ClassDojo Payments (powered by Pay Theory) launching late 2026 for school fees, but the consumer subscription stack and school payment stack will operate independently. Field trip fees, PTO dues, and technology charges will flow through Pay Theory while parent subscriptions flow through Stripe and app stores, creating a fourth payment silo.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (web subscription processor)
PSP_2: Apple App Store Payments (iOS subscriptions)
PSP_3: Google Play Store (Android subscriptions)
PSP_4: Pay Theory (embedded school payments, late 2026)
PSP_5: RevenueCat (subscription analytics layer)
PSP_6: Churn Buster (billing recovery automation)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (EU)
Local_M_2: iDEAL (Netherlands)
Local_M_3: Bancontact (Belgium)
Local_M_4: Pix (Brazil)
Local_M_5: OXXO (Mexico)
Local_M_6: Boleto Bancario (Brazil)
Local_M_7: UPI (India)
Local_M_8: GrabPay (Southeast Asia)
Local_M_9: Open Banking (UK)
Local_M_10: BLIK (Poland)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each parent subscription through the optimal payment path by geography, device, and cost. Intelligently direct web signups to Stripe (2.9% fee) instead of app store billing (15 to 30% commission), recovering 12 to 27% margin per subscriber. With hundreds of thousands of paying families across 180 countries, Smart Routing delivers +3 to 10% authorization uplift on recurring charges.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor dependency. When a parent's card declines on Stripe, Yuno retries through an alternate acquirer before the subscription lapses. Up to 50% recovery on failed recurring transactions, working alongside Churn Buster to maximize retention across the entire paying family base.
Desc_Yuno_Cap3: Unlocks subscription payments in 180 countries where ClassDojo already has users but no local payment rails: SEPA Direct Debit for EU parents, iDEAL for Netherlands, Pix and Boleto for Brazil, OXXO for Mexico, UPI for India, Open Banking for UK. One API, 1,000+ payment methods, converting free users to paying subscribers with their preferred local method.
Desc_Yuno_Cap4: One dashboard unifying Stripe web subscriptions, Apple App Store, Google Play, Pay Theory school payments, and RevenueCat analytics into a single reconciliation layer. Real-time monitoring across all parent and school transactions, NOVA fraud engine with 75% fewer false positives ensuring COPPA/FERPA-compliant payment security across the entire ClassDojo ecosystem.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ClassDojo at a glance:**
- Founded: 2011 in San Francisco, CA by Sam Chaudhary (CEO) and Liam Don (President)
- Status: Private (Series D)
- Funding: $221M total across 9 rounds from 45 investors
- Valuation: $1.25B (post-money, Series D July 2022 led by Tencent at $125M)
- Earlier investors: General Catalyst (Seed), Y Combinator, Paul Graham, Adams Street Partners
- Revenue: ~$75M estimated (2025); $51.9M (2023); nearly tripled revenue in 2020
- Employees: ~400+
- Headquarters: San Francisco, CA
- Profitable since 2019 (four months after launching Beyond School subscription)

**User base and reach:**
- Students: 51M+ worldwide
- Schools: 95% of U.S. K-8 schools
- Countries: 180+
- App downloads: 100M+ (iOS + Android)
- Paying families: Hundreds of thousands of subscribers
- Key international markets: UK, Germany, France, Spain, Singapore, Australia, Hong Kong, UAE, Japan, South Korea, India, Nigeria, Kenya, South Africa
- In 10 countries, 25%+ of all primary school teachers use ClassDojo

**Key 2025/2026 milestones:**
- ClassDojo Payments launch (late 2026): Embedded payments for school districts powered by Pay Theory
- Dojo Tutor: AI-powered 1-on-1 tutoring for K-8 (reading and math)
- Dojo Sparks: Subscription learn-to-read program for families
- ClassDojo for Districts: Enterprise product for district-wide deployment
- Canva integration for school communications
- Districts in 8+ states signed for districtwide deployment
- Plus pricing increase (Nov 2024): First in five years

**Product suite:**
- ClassDojo (free): Classroom communication, behavior management, student portfolios, messaging
- ClassDojo Plus: Premium family subscription ($7.99/month, $39.99/6 months, $59.99/year) with Homework Helper, Magic Books, Memories, Progress Reports
- Dojo Sparks: Learn-to-read subscription (up to 3 kids per family)
- Dojo Tutor: 1-on-1 online tutoring (variable pricing by session)
- ClassDojo for Districts: Enterprise offering with SSO, analytics, support
- ClassDojo Payments: School fee collection (launching late 2026)
- Shopify: Merchandise sales

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary web/app subscription payment processor
- Apple App Store Payments: iOS in-app subscription billing
- Google Play Store: Android in-app subscription billing
- Pay Theory: Embedded school payments (launching late 2026, PCI-DSS Level 1)
- RevenueCat: Technical subscription/payment data collection and analytics
- Churn Buster: Automated billing reminders and failed payment recovery
- Shopify: Merchandise store payments
- No payment orchestrator detected
- No local payment methods for international subscribers

**Technology stack:**
- AWS: Servers, databases, analytics, encrypted storage
- MongoDB Atlas: Data storage
- DataDog: Server performance monitoring
- Google Firebase: Crashlytics, push notifications (FCM)
- PubNub: Real-time communication
- SendGrid: Email
- Twilio: SMS
- Anthropic + OpenAI: AI features (zero data retention agreements)
- Blueshift: Email communications and analytics
- EdLink: School information system syncing

**Key Meeting Angles:**
1. **180 countries, credit card only** | 51M students worldwide, but international parents cannot subscribe with local payment methods, capping monetization in markets where teachers already use ClassDojo daily
2. **Three payment silos (soon four)** | Stripe, Apple, Google Play each operate independently; Pay Theory adds a fourth rail with no unified reconciliation
3. **15 to 30% app store tax** | Every in-app subscriber loses margin to Apple/Google; intelligent routing to web checkout recovers 12 to 27% per subscription
4. **Failed renewal = lost family** | Churn Buster sends reminders but cannot reroute a declined card to an alternate processor; no multi-acquirer cascade
5. **95% U.S. schools, monetization gap abroad** | In 10 countries 25%+ of teachers use ClassDojo, but no local payment rails to convert free international users to paid
6. **Pay Theory solves school fees, not subscriptions** | Embedded school payments launching late 2026 will not optimize or unify the consumer subscription stack
7. **$1.25B valuation, $75M revenue** | Profitability depends on subscription conversion; every percentage point improvement in international payment acceptance compounds across 180 countries
8. **Competitor pressure** | Remind (free messaging), Seesaw (student portfolios), Bloomz (all-in-one), Google Classroom (free, massive scale)

**Sources:**
- [ClassDojo Business Breakdown (Contrary Research)](https://research.contrary.com/company/classdojo)
- [ClassDojo Crunchbase Profile](https://www.crunchbase.com/organization/classdojo)
- [ClassDojo Wikipedia](https://en.wikipedia.org/wiki/ClassDojo)
- [ClassDojo Third-Party Service Providers (GitHub)](https://github.com/classdojo/policies/blob/master/third-party-service-providers.md)
- [ClassDojo Third-Party Providers (Official)](https://www.classdojo.com/third-party-service-providers/)
- [ClassDojo Launches Embedded Payments (PRNewswire)](https://www.prnewswire.com/news-releases/classdojo-launches-classdojo-payments-embedded-payments-for-the-platform-used-in-95-of-us-schools-302696743.html)
- [ClassDojo Embedded Payments (Embedded Finance Review)](https://www.embeddedfinancereview.com/classdojo-brings-embedded-payments-to-us-school-districts/)
- [ClassDojo Profitability & 51M Students (PRNewswire)](https://www.prnewswire.com/news-releases/as-education-shifts-online-classdojo-serves-51-million-students-worldwide-announces-profitability-and-new-solo-capitalist-funding-301216471.html)
- [ClassDojo $35M Series C (PRNewswire)](https://www.prnewswire.com/news-releases/classdojo-raises-35-million-series-c-building-worlds-most-loved-consumer-brand-in-education-300804152.html)
- [ClassDojo Revenue $51.9M (GetLatka)](https://getlatka.com/companies/classdojo.com)
- [ClassDojo Revenue Estimate (Growjo)](https://growjo.com/company/ClassDojo)
- [ClassDojo International Growth (Medium)](https://medium.com/design-bootcamp/how-classdojo-can-grow-revenue-through-international-4b9454b73c99)
- [ClassDojo Adams Street Investment](https://www.adamsstreetpartners.com/insights/classdojo-investment/)
- [ClassDojo Premium Features Terms](https://www.classdojo.com/premium-features-terms/)
- [ClassDojo Plus FAQ (Help Center)](https://help.classdojo.com/hc/en-us/articles/360018137732-ClassDojo-Plus-FAQ)
- [ClassDojo Plus Updates U.S. (Help Center)](https://help.classdojo.com/hc/en-us/articles/23430793537293-ClassDojo-Plus-Updates-for-Existing-Members-in-the-United-States)
- [Dojo Tutor Billing FAQ](https://tutor-help.classdojo.com/hc/en-us/articles/26283441383053-Billing-and-Payment-FAQs)
- [Dojo Tutor Pricing](https://tutor-help.classdojo.com/hc/en-us/articles/38422325579021-Dojo-Tutor-Pricing)
- [ClassDojo Districts in 8 States (PRNewswire)](https://www.prnewswire.com/news-releases/districts-in-eight-states-choose-classdojo-for-districtwide-communication-and-family-engagement-302474527.html)
- [ClassDojo Canva Integration (PRNewswire)](https://www.prnewswire.com/news-releases/media-alert-from-classdojo-for-districts-new-classdojo--canva-integration-helps-districts-control-school-communications-at-scale-302732645.html)
- [ClassDojo Tracxn Profile](https://tracxn.com/d/companies/classdojo/__vmj61u8rVaGiykJZq1nONoWLxGNi28-gj6IfTMUvfH4)
- [ClassDojo Logo (Brandfetch)](https://brandfetch.com/classdojo.com)
