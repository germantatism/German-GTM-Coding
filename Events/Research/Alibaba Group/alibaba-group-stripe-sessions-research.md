# ALIBABA GROUP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Alibaba Group
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/BABA-98fb82ef.png
Nombre merchant: Alibaba Group

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border Declines
Tittle_Pain Point_2: APM Coverage Gaps
Tittle_Pain Point_3: Fragmented PSP Stack
Tittle_Pain Point_4: Africa Payments Void
Tittle_Pain Point_5: Fraud False Positives

Desc_Pain Point_1: Cross-border card declines hit 150+ countries. Banks flag transactions as fraud; CSC_7200015 is the top error. Prepaid cards systematically rejected.
Desc_Pain Point_2: No UPI in India, no GrabPay in SEA, no Nequi in Colombia, no CoDi in Mexico. Africa outside Kenya/Nigeria has zero local wallets despite 150+ country reach.
Desc_Pain Point_3: Adyen acquires internationally, JPMorgan handles US, Ant/Alipay covers China. Each platform runs its own stack with no unified orchestration layer.
Desc_Pain Point_4: Only M-Pesa (Kenya) and Opay (Nigeria) supported despite launching 6 African markets in March 2025. No MTN MoMo, no Airtel Money across 48 others.
Desc_Pain Point_5: Risk controls trigger CSC_7200026 and CSC_7200054 errors blocking legitimate buyers. Aggressive fraud screening declines valid transactions from new devices.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: Ant Group / Alipay
PSP_3: JPMorgan
PSP_4: Klarna

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: GrabPay
Local_M_3: Dana
Local_M_4: OVO
Local_M_5: MTN MoMo
Local_M_6: Nequi
Local_M_7: Efecty
Local_M_8: CoDi
Local_M_9: Airtel Money
Local_M_10: GoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen, JPMorgan, and Ant Group. Each purchase routed to the best acquirer for that card BIN, issuer, and market. With AIDC at $18.4B revenue and 33% growth, a 3% auth uplift recovers hundreds of millions in GMV.
Desc_Yuno_Cap2: Automatic cascade across Alibaba's multi-PSP stack. When Adyen declines, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on soft declines. NOVA AI recovers 75% of failed transactions, turning CSC errors into orders.
Desc_Yuno_Cap3: Activates the APMs AliExpress growth markets demand: UPI in India, GrabPay and Dana in Southeast Asia, MTN MoMo across Africa, Nequi in Colombia, CoDi in Mexico. One API, 1,000+ payment methods, 200+ countries. No separate integration per market or platform.
Desc_Yuno_Cap4: One dashboard replacing fragmented Adyen + JPMorgan + Ant + Klarna streams across AliExpress, Lazada, Trendyol. Real-time approval monitoring, centralized reconciliation. Rappi achieved 80% fewer payment analysts with Yuno's unified view.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Alibaba Group at a glance:**
- Parent company of AliExpress, Taobao, Tmall, Lazada, Trendyol, Alibaba.com, 1688
- FY2025 consolidated revenue: ~$137.3B (5.33% YoY growth)
- AIDC (International Digital Commerce) revenue: RMB 133.7B (~$18.4B), up 25% YoY
- International commerce retail revenue: RMB 108.5B ($14.9B), up 33% YoY
- AliExpress top markets by traffic: Spain (7.91%), South Korea (7.71%), France (6.88%), Brazil (6.39%), United States (20% of revenue)
- 78% of growth driven by emerging markets; SEA +22.3% and LATAM +18.7% order growth YoY
- Strategy: "User first, AI-driven" under CEO Eddie Wu and Chairman Joe Tsai
- AIDC led by Jiang Fan, who now oversees unified e-commerce group integrating TTG, AIDC, 1688, Idle Fish
- Qwen AI app: 300M MAU (Dec 2025), with Alipay "AI Pay" reaching 120M transaction milestone

**Confirmed PSPs:**
- Adyen: Primary international acquirer outside China for AliExpress, Taobao, Tmall, and Alibaba.com (partnership announced Aug 2019, reaffirmed Aug 2024)
- Ant Group / Alipay: In-house payment infrastructure, handles China domestic + Alipay+ global network (88M merchants, 57 countries, 1.5B consumer accounts)
- JPMorgan: US card processing for Alibaba.com; tokenized cross-border payments via JPMD blockchain infrastructure (announced Nov 2025)
- Klarna: BNPL partner for AliExpress in Germany, Netherlands, Austria, Finland (via Adyen integration)
- No unified payment orchestrator detected across AIDC platforms

**Payment leadership:**
- Jia Hang: Former Global Head of Payment and Financial Services, AIDC. Left Nov 2025 to become Executive Chairman of DCS (Singapore). Previously held senior roles at Ant Group, UnionPay, Lazada.
- Key signal: The departure of the global payments leader creates a gap in payment strategy continuity

**Top 5 Markets Gap Analysis:**

MARKET 1: Spain (7.91% of traffic, top EU market)
  Currently supported: Visa/MC, PayPal, Klarna BNPL, iDEAL (NL), Bancontact (BE)
  Missing: Bizum (Spain's dominant P2P/e-comm wallet, 28M+ users)
  Insight: Spain is AliExpress's single largest traffic source. Bizum has become the default payment for younger Spanish shoppers.

MARKET 2: South Korea (7.71% of traffic)
  Currently supported: Visa/MC, international cards
  Missing: KakaoPay, Naver Pay, Samsung Pay, Toss Pay
  Insight: Korea's mobile wallet penetration exceeds 80%. Without KakaoPay and Naver Pay, AliExpress misses the majority of Korean payment preferences.

MARKET 3: Brazil (6.39% of traffic, key LATAM growth)
  Currently supported: Visa/MC, Pix, Boleto, PayPal, Klarna (limited)
  Missing: Mercado Pago installments, local debit card networks
  Insight: Pix was recently added; however, Pix Parcelado (installments) launched Feb 2025 via Pagaleve. Full BNPL and installment coverage still limited.

MARKET 4: France (6.88% of traffic)
  Currently supported: Visa/MC, PayPal, Klarna BNPL, Apple Pay
  Missing: Carte Bancaire local routing, Bancontact
  Insight: Carte Bancaire processes 75%+ of French card transactions. Without local acquiring through CB, every French card runs as cross-border via Visa/MC networks.

MARKET 5: Southeast Asia / Lazada Markets (22.3% order growth)
  Currently supported: Cards, bank transfers, COD
  Missing: GrabPay, Dana, OVO, GoPay, ShopeePay, TouchnGo
  Insight: SEA mobile wallet penetration exceeds 70% in markets like Indonesia and Philippines. Lazada competes directly with Shopee, which natively supports all local wallets.

**Africa Expansion (critical growth frontier):**
- March 2025: AliExpress expanded local currency to Egypt, South Africa, Algeria, Ethiopia, Morocco, Tanzania
- Payment methods: M-Pesa (Kenya), Opay + Verve (Nigeria) only
- Massive gap: No MTN MoMo (300M+ users across 19 African countries), no Airtel Money, no Flutterwave wallets, no local bank integrations in 40+ African markets
- Opened first African showroom in Ethiopia

**Payment error/decline analysis (documented CSC codes):**
- CSC_7200015: Bank-side payment block (most common), banks flag cross-border transactions
- CSC_7200001/7200006/7200022/7200051: Card cannot be used for this payment
- CSC_7200009: Spending/transaction limit reached
- CSC_7200026: Additional verification required (overly aggressive fraud screening)
- CSC_7200040: Bank card restrictions, multiple purchase blocks
- CSC_7200054: Unusual activity detected (new device/location triggers decline)
- Multiple YouTube tutorials and community guides exist for "How to Fix AliExpress Payment Error," indicating systemic decline volume

**Cross-border payment innovations:**
- JPMorgan tokenized deposits (USD/EUR) via blockchain for B2B cross-border settlement (Nov 2025)
- Alibaba backed Singapore's MetaComp for hybrid stablecoin payments (Mar 2026), targeting Middle East, Africa, LATAM
- Alipay+ network now connects 88M merchants across 57 countries to 1.5B consumer accounts
- Worldpay integrated Alipay+ for cross-border merchant acquiring

**Alibaba Cloud infrastructure incidents:**
- 10 documented outages since July 2023 (IsDown tracker)
- Last outage: Aug 12, 2025 (Beijing mobile network access anomaly)
- 27+ outages over past 5 years affecting cloud users

**Key meeting angles:**
1. **Payments leader vacuum** | Jia Hang (Global Head, Payments) left in Nov 2025. No successor publicly named. Yuno fills the strategic gap with turnkey orchestration.
2. **AIDC unification opportunity** | Jiang Fan is merging AliExpress, Lazada, Trendyol, 1688 under one e-commerce umbrella. Payments orchestration is the missing piece for unified commerce.
3. **Africa land grab** | 6 countries launched in March 2025 with only 3 local methods. Yuno's 1,000+ APMs unlocks the full continent instantly.
4. **SEA competitive gap** | Lazada competes with Shopee, which natively supports all local wallets. Yuno closes the APM gap overnight.
5. **Cross-border auth recovery** | CSC error codes show systemic decline volume. Smart Routing + NOVA AI could recover millions in failed transactions.
6. **$18.4B AIDC revenue at stake** | 33% YoY growth means every basis point of auth improvement is worth tens of millions.
7. **Case parallel: Rappi** | Multi-market LATAM orchestration with zero implementation effort and 80% fewer payment analysts. Direct parallel to AIDC's multi-platform challenge.

**Sources:**
- [Adyen x Alipay Partnership](https://www.adyen.com/press-and-media/alipay-and-adyen-partner-to-streamline-global-payment-experiences-for-users-merchants-and-businesses)
- [Alibaba FY2025 Results (Nasdaq)](https://www.nasdaq.com/press-release/alibaba-group-announces-march-quarter-2025-and-fiscal-year-2025-results-2025-05-15)
- [Alibaba Dec 2025 Quarter Results](https://www.businesswire.com/news/home/20260318501558/en/Alibaba-Group-Announces-December-Quarter-2025-Results)
- [Alibaba x JPMorgan Tokenized Payments (CNBC)](https://www.cnbc.com/2025/11/14/alibaba-plans-ai-subscriptions-stablecoin-like-payments-with-jpmorgan.html)
- [Alibaba x JPMorgan Blockchain (CoinDesk)](https://www.coindesk.com/business/2025/11/15/alibaba-to-use-jpmorgan-s-blockchain-for-tokenized-dollar-and-euro-payments-cnbc)
- [Alibaba Backs MetaComp Stablecoin Payments](https://www.cryptotimes.io/2026/03/13/alibaba-backs-singapores-metacomp-to-scale-hybrid-stablecoin-payments/)
- [Jia Hang Joins DCS (FFNews)](https://ffnews.com/newsarticle/hiring/alibaba-group-veteran-payments-leader-jia-hang-joins-dcs-to-accelerate-a-new-era-of-payments-innovation/)
- [AliExpress Error Codes (AliHelper)](https://alihelper.net/blog/en/errors-on-aliexpress-what-to-do/)
- [AliExpress Payment Methods (Accio)](https://www.accio.com/blog/aliexpress-payment-methods-worth-noting)
- [AliExpress Africa Expansion (Daily News Egypt)](https://www.dailynewsegypt.com/2025/03/17/aliexpress-expands-local-currency-payment-options-for-shoppers-in-egypt-across-africa/)
- [AliExpress Africa Expansion (CIO Africa)](https://cioafrica.co/aliexpress-expands-payment-methods-in-africa/)
- [Klarna x Alipay x Adyen AliExpress BNPL (Klarna)](https://www.klarna.com/international/press/alipay-and-klarna-enable-consumers-to-buy-now-pay-later-at-aliexpress/)
- [Ant Group Global Expansion (CNBC)](https://www.cnbc.com/2024/05/06/chinese-fintech-ant-group-doubles-down-on-global-expansion-with-alipay.html)
- [Alibaba Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/BABA/alibaba/revenue)
- [AliExpress Traffic (SimilarWeb)](https://www.similarweb.com/website/aliexpress.com/)
- [Alibaba Logo (CompaniesLogo)](https://companieslogo.com/alibaba/logo/)
- [JPMorgan x Alipay US Card Processing (BusinessWire)](https://www.businesswire.com/news/home/20210916005216/en/J.P.-Morgan-Supports-Alipay-to-Provide-Card-Payment-Services-for-Alibaba.com-in-the-U.S.)
- [Worldpay x Alipay+ Integration (Fintech Times)](https://thefintechtimes.com/worldpay-to-integrate-alipay-to-give-merchant-cross-border-payments-a-boost/)
- [Alibaba 2025 Shareholder Letter](https://www.alizila.com/aliviews-alibaba-joe-tsai-eddie-wu-2025-letter-shareholders/)
- [Alibaba Cloud Outages (IsDown)](https://isdown.app/status/alibaba-cloud)
