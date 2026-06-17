# eBAY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: eBay
═══════════════════════════════════════

Logo: https://images.prismic.io/ebayevo/Zm_StJm069VX1ywC_logo_I6728-54758-3626-50811.png?auto=format%2Ccompress&fit=max&w=3840&q=100
Nombre merchant: eBay

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock In
Tittle_Pain Point_2: Cross Border Decline Rate
Tittle_Pain Point_3: Local APM Coverage Gaps
Tittle_Pain Point_4: Reconciliation Drag
Tittle_Pain Point_5: Checkout Friction

Desc_Pain Point_1: Adyen is the sole acquirer for $74.7B GMV across 190+ markets. Zero failover path: any Adyen processing issue blocks buyer checkout globally in real time.
Desc_Pain Point_2: 25% of GMV is cross border. International card declines run 15 to 25% higher than domestic, costing eBay billions in lost transaction value annually.
Desc_Pain Point_3: 135M buyers in 190+ markets but checkout offers only cards, PayPal, Apple Pay, and Google Pay. No Pix, UPI, iDEAL, or BLIK available for buyers.
Desc_Pain Point_4: Revenue split is 50.9% US and 49.1% international across Adyen, PayPal, Klarna, and Afterpay. Multi provider settlement adds reconciliation load.
Desc_Pain Point_5: Germany (14% of GMV) added invoice pay only in 2025. UK (17.3% GMV) still lacks Open Banking. Buyers abandon when preferred method is missing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: PayPal
PSP_3: Klarna
PSP_4: Afterpay (AU)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: iDEAL
Local_M_4: BLIK
Local_M_5: Sofort
Local_M_6: Open Banking (UK)
Local_M_7: OXXO
Local_M_8: Konbini
Local_M_9: KakaoPay
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each of eBay's $74.7B in transactions to the optimal acquirer by card BIN, issuer, and market. With 25% cross border GMV, local acquiring alone can recover 3 to 10% of currently declined international payments, translating to hundreds of millions in recovered GMV.
Desc_Yuno_Cap2: Break Adyen single acquirer dependency. When Adyen declines or experiences latency, Yuno cascades to the next best processor in milliseconds. Up to 50% recovery on soft declines across 190+ markets, protecting both buyer experience and seller conversion.
Desc_Yuno_Cap3: Activate the APMs eBay's 135M buyers demand: Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland, Konbini in Japan, OXXO in Mexico. One API, 1,000+ methods. No per market engineering sprints, live in weeks not quarters.
Desc_Yuno_Cap4: One dashboard unifying Adyen, PayPal, Klarna, and Afterpay settlement streams. Real time approval monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via Monitors. Up to 90% reconciliation reduction.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**eBay at a glance:**
- 135 million active buyers, 17+ million sellers, 190+ markets, 2.5 billion live listings
- Full Year 2024 Revenue: $10.3B (up 2% YoY). Full Year 2025 Revenue: ~$11.1B (up ~7% YoY)
- Full Year 2024 GMV: $74.7B. Full Year 2025 GMV: ~$80B (up ~6%)
- Q1 2025 Revenue: $2.6B. Q1 2025 GMV: $18.8B
- CEO: Jamie Iannone. CTO: Mazen Rawashdeh (expanded engineering scope May 2025)
- 25% of GMV is cross border. Revenue split: 50.9% US, 49.1% international
- GMV by country: US 42.2%, UK 17.3%, Germany 14%, rest of world 26.5%
- eBay owns Adyen warrants/shares (403,724 shares acquired at EUR240 in Oct 2024)

**Confirmed PSPs:**
- Adyen: primary acquirer and payment processor (since 2018 migration from PayPal, 18M+ sellers transitioned)
- PayPal: offered as buyer payment method at checkout (renewed partnership post July 2023)
- Klarna: BNPL partner in UK, Austria, France, Italy, Netherlands, Spain, and US (since Dec 2024)
- Afterpay/Zip: BNPL in Australia
- Riverty: invoice payments in Germany (launched 2025)
- Apple Pay + Google Pay: digital wallets
- No payment orchestrator detected
- No payments specific hiring found in current job postings

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (42.2% of GMV)
  Accepted: Visa/MC/Discover, PayPal, Apple Pay, Google Pay, Venmo, Klarna
  Missing: ACH, Cash App Pay
  Note: AmEx no longer accepted. Cash App has 57M+ young users overlapping with eBay collectibles buyers.

MARKET 2: United Kingdom (17.3% of GMV)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay, Klarna
  Missing: Open Banking, PayByBank
  Note: Open Banking adoption is accelerating in UK ecommerce. eBay added Open Banking for Seller Capital but not buyer checkout.

MARKET 3: Germany (14% of GMV)
  Accepted: Visa/MC, PayPal, Riverty invoice, SEPA Direct Debit (seller side)
  Missing: Sofort/Klarna Direct, Giropay (discontinued but migration to other methods ongoing)
  Note: Germany has ~35% credit card penetration. Invoice payment only added in 2025, years behind competitors.

MARKET 4: Australia (est. 5% of GMV)
  Accepted: Visa/MC, PayPal, Afterpay, Zip, Apple Pay, Google Pay
  Missing: POLi (bank transfer), BPAY
  Note: Afterpay/Zip presence is strong but no real time bank transfer option.

MARKET 5: Brazil (1.3% of traffic, growing market)
  Accepted: Visa/MC, PayPal
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of digital payments in Brazil. Without it, eBay is locked out of the majority payment rail.

**Payment issues documented:**
- eBay Community forums show recurring "payment declined" threads: cards rejected despite sufficient funds, cross border purchases blocked by issuer fraud rules
- 281+ documented outages over 6 years per StatusGator monitoring
- Community thread: "eBay declining payments" with systematic debit card rejections
- Community thread: "Payment Rejected" with international buyers unable to complete purchases
- eBay admits to "security blocks" that reject valid payments for risk scoring reasons
- Cross border transactions see 15 to 25% higher decline rates industry wide (2025 data)

**Key meeting angles:**
1. **$18.7B cross border opportunity** | 25% of $74.7B GMV crosses borders; local acquiring + smart routing could recover 3 to 10% of declines
2. **Adyen single point of failure** | Sole acquirer for 190+ markets; eBay even owns Adyen shares, deepening the lock in
3. **Germany and UK are underserved** | 31.3% of GMV from markets where local payment coverage lags behind competitors like Amazon
4. **BNPL fragmentation** | Klarna in 7 markets, Afterpay in AU, Riverty in DE; no unified BNPL orchestration layer
5. **Brazil is wide open** | 1.3% traffic share could grow significantly with Pix; the #1 payment method in Brazil's digital economy
6. **AmEx dropped** | eBay stopped accepting American Express, signaling willingness to optimize payment stack economics
7. **Competitor pressure** | Amazon uses multi PSP with Worldpay, Adyen, and own acquiring. Walmart, Shopify have multi provider setups.

**Sources:**
- [eBay Managed Payments Announcement](https://www.ebayinc.com/stories/news/ebay-to-intermediate-payments-on-its-marketplace-platform/)
- [Adyen x eBay Partnership](https://www.adyen.com/en_GB/knowledge-hub/ebay)
- [eBay FY2024 Results](https://investors.ebayinc.com/investor-news/press-release-details/2025/eBay-Inc.-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx)
- [eBay Q1 2025 Results](https://investors.ebayinc.com/investor-news/press-release-details/2025/eBay-Inc--Reports-First-Quarter-2025-Results/default.aspx)
- [eBay FY2025 10K Annual Report](https://www.stocktitan.net/sec-filings/EBAY/10-k-ebay-inc-files-annual-report-41236fc5f63a.html)
- [eBay Statistics 2026 (ZIK Analytics)](https://www.zikanalytics.com/blog/ebay-statistics/)
- [eBay Statistics (Chargeflow)](https://www.chargeflow.io/blog/ebay-statistics/)
- [eBay Statistics 2026 (Thunderbit)](https://thunderbit.com/blog/ebay-statistics)
- [eBay Statistics (Yaguara)](https://www.yaguara.co/ebay-statistics/)
- [eBay GMV by Country (Statista)](https://www.statista.com/forecasts/1427935/ebay-marketplace-gmv-share-by-country)
- [eBay Payments Terms of Use](https://pages.ebay.com/payment/2.0/terms.html)
- [eBay Payment Methods Policy](https://www.ebay.com/help/policies/payment-policies/payment-methods-policy?id=4269)
- [eBay x Klarna Partnership](https://fintech.global/2025/04/25/ebay-and-klarna-bring-flexible-payment-options-to-u-s-shoppers-through-expanded-partnership/)
- [eBay Germany Invoice Payment](https://www.ebayinc.com/stories/news/new-payment-option-on-ebay-buy-now-pay-by-the-middle-of-the-next-month-in-one-invoice/)
- [eBay Leadership](https://www.ebayinc.com/company/our-leaders/)
- [eBay Adyen Share Warrants (Bloomberg)](https://news.bloomberglaw.com/banking-law/ebay-acquires-payment-firm-adyens-shares-in-warrant-tranche)
- [eBay Open Banking for Sellers](https://thepaypers.com/payments/news/ebay-adds-open-banking-to-seller-capital)
- [eBay Community: Payment Declined](https://community.ebay.com/t5/Payments/eBay-declining-payments/td-p/32252057)
- [eBay Community: Payment Rejected](https://community.ebay.com/t5/Buying/Payment-Rejected/td-p/32338897)
- [eBay Community: Debit Card Refused](https://community.ebay.com/t5/Ask-a-Mentor/I-am-new-on-ebay-and-it-automaticly-refuse-my-debit-cards/td-p/34020450)
- [Card Decline Statistics 2026](https://coinlaw.io/card-decline-statistics/)
- [eBay Outage History (StatusGator)](https://statusgator.com/services/ebay)
- [eBay Logo (Official Playbook)](https://playbook.ebay.com/foundations/logo)
- [CNBC: Why eBay Abandoned PayPal for Adyen](https://www.cnbc.com/2018/02/01/why-ebay-abandoned-paypal-for-a-smaller-european-competitor.html)
- [American Banker: eBay Move to Adyen](https://www.americanbanker.com/payments/opinion/ebays-move-to-adyen-shows-importance-of-local-processing)
