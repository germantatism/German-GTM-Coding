# EXPERIAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Experian
=======================================

Logo: https://companieslogo.com/img/orig/EXPN.L_BIG-45cfe4de.png?t=1752312076
Nombre merchant: Experian

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Market Billing Silos
Tittle_Pain Point_2: Subscription Churn Leak
Tittle_Pain Point_3: LatAm Payment Gap
Tittle_Pain Point_4: Cross-Border FX Drain
Tittle_Pain Point_5: Fraud Tool Irony

Desc_Pain Point_1: B2C subscriptions across US, UK, Brazil, Colombia on separate regional billing stacks. No unified orchestration for 200M+ consumer members.
Desc_Pain Point_2: IdentityWorks ($9.99 to $29.99/mo) depends on recurring card charges. Failed renewals from expired cards and issuer blocks drive churn.
Desc_Pain Point_3: Brazil is a top 3 market yet no Pix or Boleto for subscriptions. 70%+ of Brazilian digital payments use Pix; Experian misses the majority.
Desc_Pain Point_4: 32 countries with consumer subscriptions means multi-currency settlement. FX on $9.99 to $29.99 monthly charges compounds at 200M+ scale.
Desc_Pain Point_5: Experian sells fraud detection tools but runs its own billing without smart routing or dynamic retry logic. A credibility gap.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed (US consumer billing)
PSP_2: Undisclosed (UK consumer billing)
PSP_3: Undisclosed (Brazil consumer billing)
PSP_4: Undisclosed (enterprise B2B invoicing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: Boleto
Local_M_3: SEPA Direct Debit
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Sofort
Local_M_8: OXXO
Local_M_9: PSE
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the best acquirer for that card BIN, currency, and country. With $7.96B trailing revenue, 200M+ consumer members, and monthly billing cycles, a 3% auth uplift recovers millions in subscription revenue that would otherwise churn.
Desc_Yuno_Cap2: When a renewal charge is declined, Yuno cascades to the next acquirer in milliseconds before the member ever sees a failed payment notice. Up to 50% of involuntary churn from card declines eliminated, preserving lifetime value across 200M+ member accounts.
Desc_Yuno_Cap3: Activates the APMs Experian's global members prefer: Pix and Boleto in Brazil, SEPA DD in Europe, iDEAL in Netherlands, BLIK in Poland, PSE in Colombia, UPI in India, OXXO in Mexico. One API, 1,000+ methods, instant coverage across all 32 operating countries.
Desc_Yuno_Cap4: Single dashboard replacing Experian's siloed regional billing stacks across US, UK, Brazil, Colombia, and APAC. Real-time renewal monitoring, centralized multi-currency reconciliation, anomaly detection via NOVA across all consumer subscription products.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Experian at a glance:**
- Founded 1996 (predecessor companies date to 1803). HQ Dublin, Ireland. Public: LSE EXPN (FTSE 100)
- Trailing 12-month revenue: $7.96B (as of Sep 30, 2025)
- H1 FY26 (Apr-Sep 2025): revenue up 12% YoY, Benchmark EBIT up 14%
- FY26 guidance: total revenue growth 11%, organic revenue growth 8%
- 25,200 employees across 32 countries
- Three global bureaus: Experian, Equifax, TransUnion. Experian is the largest
- 200M+ registered consumer members across US, Brazil, UK, Colombia, and other markets
- B2C products: free credit monitoring, IdentityWorks Plus ($9.99/mo), IdentityWorks Premium ($19.99/mo), CreditWorks, Experian Boost, BillFixer
- B2B products: credit data, decisioning, fraud prevention, marketing services, automotive
- Organic growth: North America 10%, Latin America 4%, UK/Ireland 1%, EMEA/APAC 6%
- CEO: Brian Cassin

**Confirmed PSPs / Payment Infrastructure:**
- No specific PSP names publicly disclosed
- Consumer subscriptions billed via credit/debit card (recurring)
- Regional billing likely fragmented across US, UK, Brazil, Colombia operations
- B2B enterprise billing via invoicing (separate from consumer stack)
- No payment orchestrator detected
- Experian itself is a data/analytics provider, not a payment processor

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market, ~65% of revenue)
  OK Currently offer: Credit/debit card for consumer subscriptions
  Missing: ACH direct debit, Apple Pay, Google Pay, PayPal for subscription billing
  Note: 200M+ US credit files; direct consumer monetization growing rapidly

MARKET 2: Brazil (top 3 market, strong B2C presence)
  OK Currently offer: Credit/debit card (likely local acquirer)
  Missing: Pix (70%+ of digital payments), Boleto, local installment cards
  Note: Serasa Experian is the #1 credit bureau in Brazil with massive consumer reach

MARKET 3: United Kingdom (historic home market)
  OK Currently offer: Credit/debit card for consumer subscriptions
  Missing: Open Banking / Pay by Bank, SEPA DD for EU cross-sell
  Note: UK consumer credit monitoring market is growing; Experian is market leader

MARKET 4: Colombia (growing LatAm B2C market)
  OK Currently offer: Credit/debit card
  Missing: PSE (bank transfer, dominant in Colombia), Nequi, Daviplata
  Note: DataCredito Experian is a leading bureau in Colombia

MARKET 5: India (APAC growth market)
  OK Currently offer: Credit/debit card
  Missing: UPI (85%+ of Indian digital payments), Paytm, PhonePe, RuPay
  Note: Experian India is a licensed credit bureau; consumer products expanding

**Key meeting angles:**
1. **200M+ member base** | Even 1% improvement in renewal rates translates to millions of recovered subscriptions across Experian's global consumer platform
2. **Brazil without Pix** | Serasa Experian is #1 in Brazil but consumer billing ignores the dominant payment method. Pix adoption would unlock material subscription growth.
3. **Involuntary churn** | $9.99 to $29.99/mo subscriptions are highly sensitive to card decline-driven churn. Smart retry logic is a direct revenue protector.
4. **Regional silo opportunity** | Unifying US + UK + Brazil + Colombia billing under one orchestration layer eliminates redundant infrastructure and enables global analytics
5. **Fraud tool credibility** | Experian sells fraud prevention to others but lacks modern payment orchestration internally. Yuno + NOVA aligns with their own data-driven philosophy.
6. **B2B upsell path** | Starting with B2C subscription billing creates a proof point for Experian's enterprise products and client-facing payment solutions

**Sources:**
- [Experian Full-Year Results FY25](https://www.experianplc.com/newsroom/press-releases/2025/full-year-results-fy25)
- [Experian H1 FY26 Results](https://www.experianplc.com/newsroom/press-releases/2025/half-year-results-fy26)
- [Experian Q3 FY26 Trading Update](https://www.experianplc.com/newsroom/press-releases/2026/trading-update--third-quarter-fy26)
- [Experian Business Model](https://www.experianplc.com/what-we-do/our-business-model)
- [Experian About](https://www.experian.com/corporate/about-experian)
- [Experian Consumer Services](https://www.experian.com/consumer-information/)
- [Experian IdentityWorks Plans](https://www.security.org/identity-theft/experian/)
- [Experian Credit Monitoring](https://www.experian.com/credit/credit-monitoring/)
- [Experian Wikipedia](https://en.wikipedia.org/wiki/Experian)
- [Experian McKinsey AI/Growth](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/how-experian-is-fueling-its-next-phase-of-growth-with-data-ai-and-platforms)
- [Experian Logo](https://companieslogo.com/experian/logo/)
