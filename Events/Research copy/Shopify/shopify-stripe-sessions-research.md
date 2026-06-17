# SHOPIFY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Shopify
═══════════════════════════════════════

Logo: https://cdn.shopify.com/b/shopify-brochure2-assets/b2e2f48c81f4ae49a1f1f3c128238f50.svg
Nombre merchant: Shopify

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Platform Lock-In
Tittle_Pain Point_2: Cross-Border Decline Gap
Tittle_Pain Point_3: Cyber Monday Outage Risk
Tittle_Pain Point_4: Merchant Data Captivity
Tittle_Pain Point_5: Involuntary Churn Drain

Desc_Pain Point_1: Shopify charges 0.5 to 2% extra on every third-party PSP transaction. This fee wall locks 5.6M+ stores into one acquirer with zero multi-PSP routing.
Desc_Pain Point_2: 36% of GMV ($136B+) comes from international markets, but Shopify Payments only covers ~23 countries. Cross-border declines spike without local acquiring.
Desc_Pain Point_3: Dec 2025 Cyber Monday outage locked 4,000+ merchants out during peak sales. Single-acquirer dependency means zero payment failover when systems go down.
Desc_Pain Point_4: Card credentials in Shopify Payments cannot be ported to another PSP. Failed transactions cannot be retried through an alternate acquirer. Sale lost.
Desc_Pain Point_5: Failed recurring payments cause up to 40% of subscription churn. No smart retry or cascade logic means expired cards and soft declines kill revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Shopify Payments (Stripe white-label)
PSP_2: PayPal
PSP_3: Shop Pay
PSP_4: Apple Pay / Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: BLIK (Poland)
Local_M_4: GCash (Philippines)
Local_M_5: Maya (Philippines)
Local_M_6: DANA (Indonesia)
Local_M_7: GrabPay (SE Asia)
Local_M_8: KakaoPay (South Korea)
Local_M_9: MoMo (Vietnam)
Local_M_10: Nequi (Colombia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each of Shopify's $378B in annual GMV to the best acquirer per card BIN, issuer, and geography. With 65% flowing through one processor, a 3% auth uplift on cross-border transactions recovers $100M+ in lost merchant revenue annually.
Desc_Yuno_Cap2: Automatic cascade eliminates the single-acquirer dependency exposed on Cyber Monday 2025. When Shopify Payments declines or goes down, Yuno reroutes to the next best processor in milliseconds. Up to 50% recovery on failed transactions, protecting merchants' peak-season revenue.
Desc_Yuno_Cap3: Activates APMs Shopify merchants need: UPI in India, GCash and Maya in Philippines, BLIK in Poland, GrabPay and DANA in SE Asia, KakaoPay in South Korea. One API, 1,000+ payment methods, no per-market engineering sprints required.
Desc_Yuno_Cap4: One dashboard replacing fragmented Shopify Payments + PayPal + Shop Pay + Apple/Google Pay streams. Real-time approval monitoring across providers, centralized reconciliation for 5.6M+ merchants, millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Shopify at a glance:**
- 5.6M+ active online stores across 175+ countries
- Revenue: $11.56B (FY 2025), +30.1% YoY from $8.88B in 2024
- GMV: $378.44B (FY 2025), +29.5% YoY. Q4 2025 was first quarter GMV crossed $100B ($123.84B)
- GPV (Shopify Payments volume): 65% of GMV in Q3 2025 (~$60B out of $92B). Penetration rose from 60% in Q1 2024 to 65% in Q3 2025
- B2B GMV nearly doubled in 2025, growing 96% YoY
- International revenues grew 36% YoY in FY 2025, outpacing overall revenue growth
- CEO: Tobi Lutke (co-founder). President: Harley Finkelstein
- Shopify Payments powered by Stripe since 2013 (white-label partnership)
- Also leverages Stripe Treasury (for Shopify Balance) and Stripe Issuing (merchant cards)

**Confirmed PSPs:**
- Shopify Payments (Stripe white-label): primary acquirer, processing 65% of GMV
- PayPal: default secondary option in nearly every Shopify country
- Shop Pay: accelerated checkout (150M+ users, up to 50% higher checkout-to-order conversion)
- Apple Pay / Google Pay: accelerated wallets
- 100+ third-party payment gateways available but penalized with 0.5 to 2% additional transaction fees
- Stripe stablecoin payments partnership announced (USDC support for merchants)
- No external payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (57.65% of stores, highest traffic)
  Currently offer: Visa/MC/Amex/Discover, Shop Pay, Apple Pay, Google Pay, PayPal, Klarna, Afterpay
  Missing: Limited; well-served domestically
  Note: 35% of GMV is international. U.S. merchants selling globally face cross-border decline issues.

MARKET 2: United Kingdom (3.97% of stores, 220K+ merchants)
  Currently offer: Visa/MC, Shop Pay, PayPal, Klarna, Apple Pay, Google Pay
  Missing: Open Banking (A2A payments), stronger local debit routing
  Note: UK shoppers rely heavily on PayPal; local acquiring would improve auth rates.

MARKET 3: Brazil (growing merchant base, $200B ecommerce by 2026)
  Currently offer: Shopify Payments recently launched in Mexico; Brazil coverage limited
  Missing: Pix (70%+ of digital payments in Brazil), Boleto for non-banked, local installment cards
  Note: Latin America is fastest-growing ecommerce region. Pix is essential for conversion.

MARKET 4: India ($200B ecommerce projected by 2026)
  Currently offer: Shopify Payments NOT available. Third-party gateways only (Razorpay, PayU)
  Missing: UPI (75%+ of digital payments), RuPay, Paytm, PhonePe
  Note: India's merchants must use third-party gateways, paying extra Shopify transaction fees.

MARKET 5: Southeast Asia (Indonesia, Philippines, Vietnam, Thailand)
  Currently offer: Shopify Payments NOT available in most SE Asian markets
  Missing: GCash, Maya, GrabPay, DANA, OVO, MoMo, PromptPay
  Note: Credit card penetration below 10% in most SE Asian markets. Mobile wallets dominate.

**Key Pain Points Detail:**

1. **Platform lock-in economics**: Shopify charges 0.5% (Plus), 1% (Shopify), or 2% (Basic) extra on every third-party PSP transaction. A $10M/year merchant on Plus pays $50K annually just in penalty fees to use an external processor. This creates artificial lock-in, not performance-based loyalty.

2. **Cyber Monday 2025 outage**: December 1, 2025, Shopify backend went down during peak Cyber Monday. 4,000+ merchants locked out of dashboards and POS. Storefronts stayed up but merchants couldn't adjust prices, push promotions, or manage orders. No payment failover existed.

3. **Card data captivity**: Stored credentials within Shopify Payments are non-portable. Merchants cannot retry a failed transaction through a different acquirer. No network tokenization strategy enables multi-PSP routing without re-collecting card details.

4. **Mobile conversion gap**: 79% of Shopify traffic comes from mobile but only 68% of transactions complete on mobile. The 11-point conversion gap represents billions in lost GMV. Shop Pay helps (91% mobile conversion lift) but only for returning Shop Pay users.

5. **Subscription churn**: Failed payments cause 20 to 40% of all subscription churn. Shopify's native subscription billing lacks smart retry/cascade logic. Third-party apps (Recurpay, Recharge) patch the gap but add cost and complexity.

**Key meeting angles:**
1. **$378B GMV platform** | Even fractional auth-rate improvements translate to massive merchant revenue recovery
2. **65% PSP concentration** | Two-thirds of volume flows through one white-label acquirer with no failover
3. **Cyber Monday precedent** | The Dec 2025 outage proved single-acquirer risk is not theoretical
4. **International growth outpacing domestic** | 36% international revenue growth demands local APMs and acquiring
5. **India + SE Asia black holes** | Shopify Payments unavailable in the world's fastest-growing ecommerce markets
6. **Third-party fee wall** | 0.5 to 2% penalty fees prevent merchants from adopting multi-PSP strategies
7. **Stablecoin signal** | Stripe partnership for USDC shows Shopify is actively evolving payment infrastructure
8. **Competitor precedent** | Amazon (multi-acquirer), Mercado Libre (own orchestration), eBay (Adyen migration)

**Sources:**
- [Shopify Brand Assets (Logo)](https://www.shopify.com/brand-assets)
- [Shopify Q4 2025 Financial Results](https://www.shopify.com/news/shopify-q4-2025-financial-results)
- [Shopify Revenue & GMV Growth (Digital Commerce 360)](https://www.digitalcommerce360.com/article/shopify-revenue-gmv/)
- [Shopify Statistics 2026 (DemandSage)](https://www.demandsage.com/shopify-statistics/)
- [Shopify Payments & PSP Architecture Guide](https://what.digital/shopify-payments-third-party-psp-architecture/)
- [Shopify Payments vs Third-Party PSPs: Hidden Costs](https://www.flatlineagency.com/blog/shopify-payments-vs-third-party-psps/)
- [Stripe + Shopify Case Study](https://stripe.com/customers/shopify)
- [Stripe + Shopify Stablecoin Payments](https://stripe.com/newsroom/news/shopify-stripe-stablecoin-payments)
- [Shopify Cyber Monday Outage (CNBC)](https://www.cnbc.com/2025/12/01/shopify-outage-cyber-monday-shopping.html)
- [Shopify Cyber Monday Outage (TechCrunch)](https://techcrunch.com/2025/12/01/shopify-resolves-outage-disrupting-merchants-on-cyber-monday/)
- [Shopify Cyber Monday Outage (PYMNTS)](https://www.pymnts.com/news/ecommerce/2025/shopify-outage-locks-merchants-out-on-cyber-monday)
- [Shopify Supported Countries for Payments](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries)
- [Shopify Local Payment Methods](https://help.shopify.com/en/manual/payments/shopify-payments/local-payment-methods)
- [Shopify Payment Authorization Rates](https://www.shopify.com/enterprise/blog/authorization-rates)
- [Shopify ML Pre-Authorization (+0.26% auth, $471M recovered)](https://www.shopify.com/enterprise/blog/shopify-payments-pre-authorization)
- [Shopify Merchant Data Portability (Basis Theory)](https://blog.basistheory.com/shopify-merchants-gain-back-independence)
- [Shopify Market Share 2026 (DemandSage)](https://www.demandsage.com/shopify-market-share/)
- [Shopify Payments Statistics 2025 (CoinLaw)](https://coinlaw.io/shopify-payments-statistics/)
- [Involuntary Churn on Shopify (LoopWork)](https://www.loopwork.co/blog/voluntary-vs-involuntary-churn-shopify-subscription-revenue)
- [Shopify International Expansion (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/shopifys-global-expansion-efforts-drive-150800926.html)
