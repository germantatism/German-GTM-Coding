# ZETA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Zeta
=======================================

Logo: https://cdn.brandfetch.io/zeta.tech/w/512/h/512/logo
Nombre merchant: Zeta

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Market Card Issuing
Tittle_Pain Point_2: No Payment Orchestration
Tittle_Pain Point_3: Cross-Border Settlement
Tittle_Pain Point_4: APM Gap in Key Markets
Tittle_Pain Point_5: Fraud Cost at Scale

Desc_Pain Point_1: Zeta processes 25M+ issued cards across 35+ bank clients in the US, India, UK, Brazil, Philippines, Italy, Spain, and Vietnam. Each market requires different acquirer routing, local scheme compliance, and regulatory alignment that a single PSP cannot optimize across all regions.
Desc_Pain Point_2: At $72M+ revenue (605 Cr INR) and growing, Zeta's platform processes card transactions for banks across 8+ countries. Without payment orchestration, each bank client's transaction routing is siloed, preventing cross-client optimization of approval rates and processing costs.
Desc_Pain Point_3: Zeta operates across US, India, UK, Brazil, Philippines, Italy, Spain, and Vietnam. Cross-border settlement between these markets creates FX complexity, regulatory overhead, and multi-day settlement delays that smart routing could reduce to hours.
Desc_Pain Point_4: Zeta's bank clients serve end consumers who increasingly demand local APMs beyond cards. In India (UPI dominates), Brazil (PIX), Philippines (GCash), and Vietnam (MoMo), card-only issuing misses the majority of digital transaction volume in these markets.
Desc_Pain Point_5: With 25M+ cards issued and transaction processing across 8+ countries, fraud management is fragmented per market. A unified orchestration layer with NOVA-grade AI fraud scoring (75% false positive reduction) would reduce fraud losses while maintaining approval rates.

SLIDE 1: PSP TOPOLOGY

PSP_1: Zeta Tachyon (proprietary processing)
PSP_2: Mastercard (strategic partner, $30M investment)
PSP_3: Visa (network connectivity)
PSP_4: Local acquirers per market

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI (India)
Local_M_2: PIX (Brazil)
Local_M_3: GCash (Philippines)
Local_M_4: MoMo (Vietnam)
Local_M_5: SEPA Direct Debit (EU)
Local_M_6: Faster Payments (UK)
Local_M_7: Boleto (Brazil)
Local_M_8: BACS Direct Debit (UK)
Local_M_9: Paymaya (Philippines)
Local_M_10: ZaloPay (Vietnam)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each card transaction to the best-performing acquirer by card BIN, issuer country, merchant category, and transaction amount. With 25M+ cards across 8+ countries, even a 3% auth uplift across Zeta's bank clients translates to millions in recovered transaction volume annually.
Desc_Yuno_Cap2: Automatic retry cascades across multiple acquirers protect Zeta's bank clients from declined transactions. When the primary processor declines, Yuno reroutes in milliseconds to a backup acquirer. Up to 50% recovery on soft declines directly improves end-cardholder experience.
Desc_Yuno_Cap3: Expand Zeta's bank clients beyond card rails: UPI for Indian banks, PIX for Brazilian banks, GCash/Paymaya for Philippine banks, SEPA for EU expansion. One API, 1,000+ methods, enabling Zeta to offer multi-rail processing without building each integration in-house.
Desc_Yuno_Cap4: One dashboard consolidating transaction processing across all of Zeta's bank clients, markets, and payment rails. Real-time approval monitoring per bank, per market, centralized reconciliation, and cross-market fraud analytics across the 25M+ card portfolio.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Zeta at a glance:**
- Next-gen banking technology platform: card issuing, transaction processing, core banking, BNPL, fraud, rewards
- Revenue: 605 Cr INR (~$72M USD) as of March 2025
- Valuation: $2B (Series D, February 2025)
- Total funding: $390M over 4 rounds; $50M Series D at $2B valuation
- 1,700+ employees across US, India, Middle East
- 35+ bank/FI clients globally; 25M+ cards issued on platform
- Founded 2015 by Bhavin Turakhia and Ramki Gaddipati
- Headquartered in San Francisco, CA; offices in Bangalore, Hyderabad, Dubai
- Expects profitability by March 2026
- Key product: Tachyon (credit processing platform)

**Strategic partnerships:**
- Mastercard: 5-year strategic partnership with $30M investment
- HDFC Bank: powering Credit Line on UPI (CLOU) solutions
- Visa: network connectivity for card programs
- Sodexo: first client in Philippines and Vietnam

**Global presence:**
- United States (headquarters, primary market)
- India (engineering hub, major market)
- United Kingdom
- Brazil
- Philippines
- Italy
- Spain
- Vietnam
- Dubai/UAE (office)
- First Indian fintech to launch in ASEAN region

**Confirmed PSPs:**
- Zeta Tachyon: proprietary transaction processing platform
- Mastercard and Visa network rails
- Local acquirer connections per market
- No third-party payment orchestrator detected
- $400M+ invested in platform since inception

**Product capabilities:**
- Instant card issuing (credit, debit, prepaid)
- Real-time transaction processing
- Core banking engine
- BNPL/lending
- Fraud and risk management
- Rewards and loyalty
- Mobile banking experiences
- Cloud-native, fully API-enabled stack
- 70%+ of employees in technology roles

**Top 5 Markets Gap Analysis:**

MARKET 1: India (engineering hub + major market, HDFC partnership)
  Currently offer: Card issuing, transaction processing
  Missing: UPI as alternate rail for bank clients, INR real-time settlement optimization
  UPI processes 75%+ of Indian digital payments. Zeta's bank clients need UPI alongside card rails.

MARKET 2: United States (headquarters, primary commercial market)
  Currently offer: Card issuing, transaction processing
  Missing: ACH optimization, RTP, multi-acquirer routing
  US card-not-present approval rates average 85-90%. Smart routing across acquirers could push this to 93%+.

MARKET 3: Brazil (expansion market)
  Currently offer: Card issuing
  Missing: PIX integration, Boleto, BRL instant settlement
  PIX processes 45B+ transactions annually. Zeta's Brazilian bank clients need multi-rail beyond cards.

MARKET 4: Philippines / Vietnam (ASEAN expansion)
  Currently offer: Card issuing (Sodexo partnership)
  Missing: GCash, Paymaya, MoMo, ZaloPay, local wallet integration
  Mobile wallets dominate ASEAN payments. Card-only issuing reaches a fraction of the addressable market.

MARKET 5: UK / EU (expansion markets)
  Currently offer: Card issuing
  Missing: SEPA DD, Faster Payments, Open Banking, BACS
  European and UK banks expect multi-rail processing. Card-only limits Zeta's value proposition vs. incumbents.

**Key meeting angles:**
1. **$2B valuation, path to profitability** | Zeta is at an inflection point. Payment orchestration would help bank clients optimize transaction economics and accelerate revenue per card.
2. **25M+ cards across 8+ countries** | Multi-market card processing without orchestration creates siloed routing and suboptimal approval rates.
3. **Mastercard strategic partnership** | $30M investment shows network confidence. Adding Yuno orchestration would extend Zeta's value beyond Mastercard rails.
4. **ASEAN first-mover** | First Indian fintech in Philippines/Vietnam. Local wallet integration (GCash, MoMo) would differentiate vs. legacy issuers.
5. **HDFC Bank + UPI** | India's largest private bank partnering with Zeta. UPI orchestration would multiply transaction volume for HDFC's credit line product.
6. **Bank-as-a-service model** | Zeta's platform serves banks. Embedding Yuno orchestration means every bank client gets multi-rail, multi-acquirer capabilities without additional integration.

**Sources:**
- [Zeta Homepage](https://www.zeta.tech/us/)
- [Zeta About Us](https://www.zeta.tech/us/about-us/)
- [Zeta $2B Valuation (TechCrunch)](https://techcrunch.com/2025/02/10/zeta-valued-at-2b-in-new-funding/)
- [Zeta $2B Valuation (Fintech Global)](https://fintech.global/2025/02/11/zeta-raises-50m-as-valuation-surges-to-2bn-in-strategic-funding/)
- [Zeta Wikipedia](https://en.wikipedia.org/wiki/Zeta_(company))
- [Zeta Mastercard Partnership](https://www.businesswire.com/news/home/20220304005146/en/Zeta-and-Mastercard-Partner-to-Power-Next-gen-Credit-Processing-for-Banks-and-Fintechs)
- [Zeta Mastercard Partnership (Mastercard)](https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2022/zeta-and-mastercard-partner-to-power-next-gen-credit-processing-for-banks-and-fintechs/)
- [Zeta ASEAN Expansion](https://bfsi.eletsonline.com/zeta-becomes-first-indian-fintech-firm-to-launch-business-in-asean-region/)
- [Zeta Transaction Processing](https://www.zeta.tech/us/platform/tachyon/transaction-processing/)
- [Brandfetch: Zeta Logo](https://brandfetch.com/zeta.tech)
- [Tracxn: Zeta Profile](https://tracxn.com/d/companies/zeta/__BIQS1R54gpLBM5yisW_NwOI1xObGUSxqcodKR18NOfs)
- [CBInsights: Zeta](https://www.cbinsights.com/company/zeta-tech)
- [Zeta UPI Innovation](https://www.zeta.tech/us/resources/blog/reimagining-payment-strategy-with-upi-innovation/)
