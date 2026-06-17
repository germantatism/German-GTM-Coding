# WEBFLOW | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Webflow
=======================================

Logo: https://cdn.brandfetch.io/webflow.com/w/512/h/512/logo
Nombre merchant: Webflow

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe + PayPal Only
Tittle_Pain Point_2: No SEPA or Local APMs
Tittle_Pain Point_3: Country Coverage Gaps
Tittle_Pain Point_4: No Failover Logic
Tittle_Pain Point_5: FX Revenue Leakage

Desc_Pain Point_1: Webflow Ecommerce supports only Stripe and PayPal as payment providers. With 20,378 ecommerce stores across 100+ countries and $200M+ ARR, merchants cannot offer SEPA, iDEAL, Klarna, or bank transfers that EU and DACH buyers demand for online purchases.
Desc_Pain Point_2: EU/DACH merchants on Webflow cannot accept SEPA Direct Debit, Sofort, Giropay, or Klarna despite Europe representing 25%+ of the user base. Community feature requests for these methods have been open for years with no resolution, creating a competitive gap vs. Shopify.
Desc_Pain Point_3: Stripe does not support transaction fees in Brazil, India, or Malaysia. Webflow merchants in these markets must use Stripe Atlas to incorporate a US entity, adding cost and complexity. This blocks organic ecommerce growth in three of the world's fastest-growing digital markets.
Desc_Pain Point_4: Single PSP dependency on Stripe means zero failover. When Stripe experiences an outage or declines a transaction, there is no backup acquirer to route payments through. For high-value ecommerce stores, this means lost sales with no recovery path.
Desc_Pain Point_5: Webflow Ecommerce stores billing in USD lose revenue to FX conversion costs. UK (8.0% of merchants), France (5.8%), and Germany represent significant international volume where local currency checkout would increase conversion rates by 5-15%.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, confirmed)
PSP_2: PayPal (secondary, confirmed)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Klarna
Local_M_4: Sofort
Local_M_5: Giropay
Local_M_6: Bancontact
Local_M_7: PIX
Local_M_8: UPI
Local_M_9: Boleto
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Webflow Ecommerce transaction to the best-performing acquirer by card BIN, issuer, and geography. With 20,378 stores across 100+ countries, even a 3% auth uplift at checkout recovers significant GMV otherwise lost to false declines across global storefronts.
Desc_Yuno_Cap2: Eliminate single-PSP dependency. When Stripe declines a transaction or experiences an outage, Yuno reroutes in milliseconds to a backup acquirer. Up to 50% recovery on soft declines, protecting Webflow merchants from revenue loss during peak traffic events.
Desc_Yuno_Cap3: Unlock checkout conversion across Webflow's 100+ country footprint: iDEAL for Netherlands, SEPA for EU, Klarna for Nordics, PIX for Brazil, UPI for India, OXXO for Mexico. One API, 1,000+ methods, zero custom code per market.
Desc_Yuno_Cap4: One dashboard consolidating Webflow Ecommerce billing across Stripe, PayPal, and any additional processors. Real-time approval monitoring per geography, centralized reconciliation, and conversion analytics tied to payment method availability across all storefronts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Webflow at a glance:**
- No-code website builder with visual CMS, ecommerce, and enterprise site management
- Revenue: $200M+ ARR as of 2023 (48% YoY growth from $135M in 2022)
- Valuation: $4B (Series C, March 2022)
- Total funding: $334.9M; Series C of $120M led by Silversmith Capital Partners
- 1,292-1,689 employees (growing)
- 20,378 ecommerce stores worldwide; 100+ countries
- Founded 2013, headquartered in San Francisco
- Investors: Y Combinator, Accel, CapitalG (Google), Khosla Ventures
- Enterprise customers include TED, PostNL, SoftwareONE

**Ecommerce customer distribution:**
- United States: 36.5%
- United Kingdom: 8.0%
- France: 5.8%
- Europe collectively: 25%+
- English-speaking countries: 52.6%
- 92% of Webflow Ecommerce stores are from businesses with <50 employees

**Confirmed PSPs:**
- Stripe: primary payment provider (confirmed in help docs)
- PayPal: secondary provider (confirmed)
- Apple Pay, Google Pay, Microsoft Pay: available via Stripe
- Credit/debit cards: Visa, MC, Amex, Discover, Diners Club, JCB, UnionPay
- SCA/3D Secure compliant for EEA merchants
- No payment orchestrator detected

**Key limitations (confirmed):**
- Only Stripe and PayPal supported natively
- No SEPA, iDEAL, Klarna, Sofort, Giropay, or bank transfer
- Stripe unavailable for transaction fees in Brazil, India, Malaysia
- Community wishlist requests for bank transfer and local APMs open for years
- No third-party gateway integration without custom code

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (36.5% of ecommerce stores)
  Currently offer: Stripe, PayPal, Apple Pay, Google Pay
  Missing: ACH Direct Debit, Affirm, Afterpay
  US ecommerce BNPL adoption growing 30%+ YoY. Missing Affirm/Afterpay reduces AOV.

MARKET 2: United Kingdom (8.0% of stores)
  Currently offer: Stripe, PayPal
  Missing: Klarna, Open Banking, BACS
  UK ecommerce has highest Klarna adoption in Europe. Missing BNPL reduces conversion.

MARKET 3: France (5.8% of stores)
  Currently offer: Stripe, PayPal
  Missing: Carte Bancaire optimization, Banque-based payments, Alma (BNPL)
  French ecommerce expects Carte Bancaire processing with local acquirers.

MARKET 4: Germany / DACH
  Currently offer: Stripe, PayPal
  Missing: SEPA Direct Debit, Sofort, Giropay, Klarna
  ~35% card penetration. German ecommerce relies on SEPA, Sofort, and Klarna. Webflow's card-only approach loses 40%+ of potential German buyers.

MARKET 5: Netherlands / Benelux
  Currently offer: Stripe, PayPal
  Missing: iDEAL, Bancontact
  iDEAL processes 70%+ of Dutch online payments. Not offering iDEAL is effectively blocking the Dutch market.

**Key meeting angles:**
1. **Only 2 PSPs** | Stripe and PayPal only, in a world where Shopify offers 100+ payment methods. This is Webflow's biggest competitive gap.
2. **$200M+ ARR** | Platform-level GMV flowing through a single PSP creates massive concentration risk.
3. **25%+ EU merchants** | Zero SEPA, iDEAL, Klarna, or Sofort means losing the EU ecommerce battle to Shopify and Wix.
4. **Brazil, India, Malaysia blocked** | Three of the fastest-growing ecommerce markets have no Stripe support for transaction fees, blocking growth.
5. **Community demand** | Years of open feature requests for bank transfer, SEPA, and BNPL show merchants are asking for exactly what Yuno provides.
6. **SMB ecommerce** | 92% of stores are SMBs. These merchants need plug-and-play local payment methods without custom development.

**Sources:**
- [Webflow Connect a Payment Provider](https://help.webflow.com/hc/en-us/articles/33961361368979-Connect-a-payment-provider)
- [Webflow Payment Methods Help](https://help.webflow.com/hc/en-us/sections/34242355643667-Payment-methods)
- [Webflow Ecommerce](https://webflow.com/ecommerce)
- [Webflow Customers](https://webflow.com/customers)
- [Webflow Wishlist: Bank Transfer](https://wishlist.webflow.com/ideas/WEBFLOW-I-128)
- [Webflow Stripe Integration](https://webflow.com/integrations/stripe)
- [TapTwice: Webflow Statistics](https://taptwicedigital.com/stats/webflow)
- [MyCodelessWebsite: Webflow Statistics](https://mycodelesswebsite.com/webflow-statistics/)
- [Sacra: Webflow Revenue](https://sacra.com/c/webflow/)
- [TechnologyChecker: Webflow Ecommerce Customers](https://technologychecker.io/technology/webflow-ecommerce)
- [Brandfetch: Webflow Logo](https://brandfetch.com/webflow.com)
- [Weglot: Webflow International Ecommerce](https://www.weglot.com/blog/webflow-ecommerce-success-multilingual-market)
