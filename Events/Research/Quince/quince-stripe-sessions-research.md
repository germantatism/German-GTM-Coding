# QUINCE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Quince
=======================================

Logo: https://brandfetch.com/quince.com?view=library
Nombre merchant: Quince

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Global Expansion Ceiling
Tittle_Pain Point_2: Shopify Plus Pay Limits
Tittle_Pain Point_3: Triple-Digit Growth Risk
Tittle_Pain Point_4: BNPL Fragmentation
Tittle_Pain Point_5: Cross-Border Cart Abandon

Desc_Pain Point_1: Quince just entered Canada (late 2025) and targets UK and continental Europe next. At $1B+ revenue and $10.1B valuation, expanding into Europe and Asia requires iDEAL, Bancontact, BLIK, Pix, and dozens of local methods Shopify Plus cannot natively orchestrate.
Desc_Pain Point_2: Running on Shopify Plus limits payment routing to whatever Shopify Payments (Stripe) offers. No ability to route by BIN, issuer, or geography across multiple processors. On $1B+ in revenue, even 1% auth improvement recovers $10M+.
Desc_Pain Point_3: Triple-digit YoY growth every fiscal year means transaction volume is scaling faster than payment infrastructure. A single processor outage during peak shopping (Black Friday, holiday) could cost millions with no failover path.
Desc_Pain Point_4: Quince uses Klarna, Sezzle, Zip, and Afterpay for BNPL but each is a separate integration with its own reconciliation, fraud rules, and reporting. No unified BNPL orchestration across the four providers.
Desc_Pain Point_5: Direct-from-factory shipping means many orders come from Asian manufacturing hubs. International shoppers in target expansion markets (UK, EU) face card-only checkout, inflating cart abandonment in the highest-growth segments.

SLIDE 1: PSP TOPOLOGY

PSP_1: Shopify Payments (Stripe)
PSP_2: PayPal
PSP_3: Amazon Pay
PSP_4: Shop Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: BLIK
Local_M_4: Giropay
Local_M_5: Pix
Local_M_6: OXXO
Local_M_7: Mada
Local_M_8: Konbini
Local_M_9: Swish
Local_M_10: Interac e-Transfer

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every transaction by BIN, issuer, and geography across Shopify Payments, PayPal, and additional processors. On $1B+ in annual revenue with triple-digit growth, a 3-10% auth uplift recovers $30M-$100M+ that currently fails at single-processor checkout.
Desc_Yuno_Cap2: Automatic cascade eliminates single-point-of-failure risk during Black Friday, holiday peaks, and viral product launches. When Shopify Payments drops, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions protecting the fastest-growing DTC brand in the market.
Desc_Yuno_Cap3: Unlocks the APMs Quince needs for UK and European expansion: iDEAL for Netherlands, Bancontact for Belgium, BLIK for Poland, Giropay for Germany, Swish for Sweden, Mada for Middle East, Pix for Brazil. One API, 1,000+ payment methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying Shopify Payments, PayPal, Amazon Pay, Klarna, Sezzle, Zip, and Afterpay into a single reconciliation layer. Real-time approval monitoring across all markets, NOVA fraud engine with 75% fewer false positives reducing chargebacks on high-volume DTC orders.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Quince at a glance:**
- American DTC e-commerce brand offering "affordable luxury" via Manufacturer-to-Consumer (M2C) model
- Founded in 2018, headquartered in San Francisco, CA
- Revenue: $1B+ (surpassed in 2025/2026)
- Valuation: $10.1B (Series E, March 2026)
- Total funding: $913M+ across multiple rounds
  - Series E: $500M led by ICONIQ (March 2026, $10.1B valuation)
  - Series D: $200M led by ICONIQ (Jan 2025, $4.5B valuation)
- Key investors: ICONIQ, Basis Set Ventures, Wellington Management, Wndrco, MarcyPen Capital Partners, Baillie Gifford, Notable Capital, DST Global, Insight Partners
- ~800 employees (as of Nov 2025)
- CEO/Co-Founder: Sid Gupta (BoF 500 honoree)
- CTO/Co-Founder: Sourabh Mahajan
- Co-Founder: Zunu Mittal (and Becky Mortimer per some sources)
- Triple-digit YoY growth every fiscal year since launch
- Forbes Next Billion-Dollar Startups (2023)
- Products: Cashmere, Italian leather, Turkish cotton, silk, home goods, jewelry, wellness, beauty

**Markets and expansion:**
- Primary market: United States
- First international market: Canada (launched late 2025)
- Next targets: UK, continental Europe (confirmed), Australia, Middle East (planned)
- Manufacturer partners in Italy, Turkey, Portugal, China, Mongolia
- Platform: Shopify Plus

**Confirmed PSPs / Payment Methods:**
- Shopify Payments (powered by Stripe): Primary processor
- PayPal: Accepted at checkout
- Amazon Pay: Accepted at checkout
- Shop Pay: Shopify's accelerated checkout
- Apple Pay: Accepted at checkout
- Google Pay: Not confirmed
- Klarna: BNPL (Pay in 4)
- Sezzle: BNPL (4 interest-free payments over 6 weeks)
- Zip: BNPL (split payments)
- Afterpay: BNPL financing
- No payment orchestrator detected

**Top Market Gap Analysis:**

MARKET 1: United States (primary, $1B+ revenue)
  Accepted: Cards, Apple Pay, PayPal, Amazon Pay, Shop Pay, Klarna, Sezzle, Zip, Afterpay
  Missing: Cash App Pay, Venmo
  Note: Strong payment coverage domestically; BNPL fragmentation is the main issue

MARKET 2: Canada (first international market, late 2025)
  Accepted: Cards, PayPal, Apple Pay
  Missing: Interac Online, Interac e-Transfer
  Note: Interac dominates Canadian payments; critical for new market conversion

MARKET 3: United Kingdom (confirmed expansion target)
  Accepted: None launched yet
  Missing: Open Banking (Pay by Bank), Klarna UK, Clearpay UK
  Note: UK is priority expansion market; Open Banking growing fast

MARKET 4: Continental Europe (confirmed expansion target)
  Accepted: None launched yet
  Missing: iDEAL (NL), Bancontact (BE), BLIK (PL), Giropay (DE), Swish (SE), EPS (AT)
  Note: Each EU market has dominant local methods that cards cannot replace

MARKET 5: Australia (logical expansion market)
  Accepted: None launched yet
  Missing: Afterpay AU, POLi, BPAY
  Note: Afterpay originated in AU; natural fit for affordable luxury positioning

**Key Meeting Angles:**
1. **$10.1B valuation, global mandate** | Series E capital ($500M) is explicitly earmarked for global expansion; payment infrastructure must scale to UK, EU, and beyond
2. **$1B revenue at stake** | On $1B+ revenue, even 1% auth improvement from smart routing recovers $10M+; 3-10% uplift means $30M-$100M
3. **Shopify Plus ceiling** | Shopify Payments offers limited routing and processor flexibility; as Quince scales internationally, the platform's payment constraints become a bottleneck
4. **CTO is a co-founder** | Sourabh Mahajan co-founded Quince and leads technology; will understand API orchestration and integration architecture
5. **BNPL chaos** | Four BNPL providers (Klarna, Sezzle, Zip, Afterpay) each with separate integrations; orchestration unifies them into one dashboard
6. **M2C model = global by design** | Products ship from factories worldwide; customers should be able to pay with local methods regardless of origin
7. **Triple-digit growth** | Fastest-growing DTC brand in the market needs payment infrastructure that can keep pace without per-market engineering

**Sources:**
- [Quince Homepage](https://www.quince.com/)
- [Quince About Us](https://www.quince.com/about-us)
- [Quince Privacy Policy](https://www.quince.com/privacy-policy)
- [Quince Wikipedia](https://en.wikipedia.org/wiki/Quince_(company))
- [Quince $500M Series E (TechCrunch)](https://techcrunch.com/2026/03/11/quince-series-e-10b-valuation-with-500m-round-led-by-iconiq/)
- [Quince $500M Series E (PRNewswire)](https://www.prnewswire.com/news-releases/quince-raises-500m-series-e-resulting-in-10-1b-valuation-to-accelerate-the-manufacturer-to-consumer-platform-302710298.html)
- [Quince $500M Series E (WWD)](https://wwd.com/business-news/financial/quince-10-1-billion-valuation-500-million-series-e-1238663323/)
- [Quince $500M Series E (Retail Dive)](https://www.retaildive.com/news/Quince-500-million-series-e-valuation-tops-10b/814412/)
- [Quince $10.1B Valuation (TechFundingNews)](https://techfundingnews.com/quince-500m-series-e-10-1b-valuation-m2c-platform/)
- [Quince $200M Series D (Caproasia)](https://www.caproasia.com/2025/07/31/united-states-affordable-luxury-brand-quince-raised-200-million-in-funding-round-at-4-5-billion-valuation/)
- [Quince Gen Z Appeal (Retail Brew)](https://www.retailbrew.com/stories/2025/07/29/quince-is-the-anti-luxury-luxury-brand-taking-over-gen-z-s-feed)
- [Quince Revenue & Profile (Sacra)](https://sacra.com/c/quince/)
- [Quince Crunchbase](https://www.crunchbase.com/organization/Quince)
- [Quince Leadership (The Org)](https://theorg.com/org/quince/teams/leadership-team)
- [Sid Gupta (BoF 500)](https://www.businessoffashion.com/people/sid-gupta/)
- [Quince Tech Blog](https://tech.onequince.com/meet-quince-9a4b92466f5e)
- [Quince Canada Launch (VentureBurn)](https://ventureburn.com/quince-raises-500m/)
- [Klarna x Quince](https://www.klarna.com/us/store/62634bdf-1356-4773-8c9a-9456cd288812/Quince/pay-with-klarna/)
- [Sezzle x Quince](https://sezzle.com/shop/quince/)
- [Zip x Quince](https://zip.co/us/store/quince)
- [Quince Brand Logo (Brandfetch)](https://brandfetch.com/quince.com)
- [Quince eCommerce Insights (InternetResearchUnit)](https://internetresearchunit.com/brands/quince)
