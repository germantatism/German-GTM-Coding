# MERPAY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-27*

```
═══════════════════════════════════════
DATABASE FIELDS: Merpay
═══════════════════════════════════════

Logo: https://about.mercari.com/en/press/press-kit/mercari/
Nombre merchant: Merpay

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Japan Only Coverage
Tittle_Pain Point_2: Single Ecosystem Trap
Tittle_Pain Point_3: BNPL Credit Risk
Tittle_Pain Point_4: Multi PSP Fragmentation
Tittle_Pain Point_5: Cross Border Gap

Desc_Pain Point_1: Merpay operates only in Japan. 18.8M users locked into a single market while Mercari pushes US and global expansion with no Merpay rails outside JP.
Desc_Pain Point_2: 90% of TPV depends on Mercari Marketplace flow. Outside the app, acceptance at 1.7M merchants relies on partners like SBPS, KOMOJU, Antom, NORBr.
Desc_Pain Point_3: Smart Pay later (BNPL) is core product. Late repayments and credit losses concentrated in JCB network with no reinsurance or risk diversification.
Desc_Pain Point_4: Each integration path runs through a different PSP (KOMOJU, SBPS, Antom, NORBr, GMO PG). No central acquiring layer, no smart routing across them.
Desc_Pain Point_5: Mercari ships Japan to US cross border via Mercari Hop, but Merpay has zero presence outside Japan. Foreign buyers cannot pay with Merpay rails.

SLIDE 1: PSP TOPOLOGY

PSP_1: KOMOJU
PSP_2: SoftBank Payment Service
PSP_3: Antom (Ant Group)
PSP_4: NORBr

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: KakaoPay
Local_M_4: UPI
Local_M_5: Pix
Local_M_6: iDEAL
Local_M_7: BLIK
Local_M_8: GrabPay
Local_M_9: TrueMoney
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across KOMOJU, SBPS, Antom, NORBr, and GMO PG optimizes each Merpay payin by issuer, BIN, and merchant category. With JPY 400B TPV in 2025, even a 3% auth uplift translates to JPY 12B in recovered annual volume across 1.7M merchants.
Desc_Yuno_Cap2: Automatic cascade across Merpay's 4+ integration partners eliminates single PSP outage risk. When KOMOJU or SBPS declines, Yuno reroutes instantly to the next best provider, turning failed Smart Pay later renewals into recovered BNPL revenue with zero customer friction.
Desc_Yuno_Cap3: Activates the rails Merpay needs to expand beyond Japan: Alipay and WeChat Pay for Chinese tourists, KakaoPay for Korea, UPI for India, Pix for Brazil. One API, 1,000+ payment methods, instant geo-routing for Mercari Hop cross border flows.
Desc_Yuno_Cap4: One dashboard replacing Merpay's fragmented KOMOJU, SBPS, Antom, NORBr, and GMO PG consoles. Real-time approval rate monitoring, centralized reconciliation across all integration partners, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Merpay at a glance:**
- Subsidiary of Mercari, Inc. (TYO: 4385), Japan
- 18.8M identity-verified accounts (Sept 2025), 94% of users verified
- 1.7M merchants accept Merpay across Japan
- JPY 400B Total Payment Volume (TPV) in FY2025 (~$2.6B USD)
- Parent Mercari FY2025 revenue: JPY 192.63B (~$1.27B), +2.79% YoY
- Mercari Core operating profit: JPY 27.5B (+46% YoY), exceeded forecasts
- Fee structure: 2.6% per transaction to merchants, no startup fees
- Mercari FY2026 guidance: JPY 200B to 210B revenue, JPY 28B to 32B core operating profit

**Confirmed integration partners (PSPs):**
- KOMOJU: featured Merpay as Japanese payment method
- SoftBank Payment Service (SBPS): Merpay payment integration documented
- Antom (Ant Group): Merpay supported as payment method
- NORBr: white label gateway includes Merpay
- GMO Payment Gateway: standard Japanese acquirer (likely)
- Mercard (JCB): credit card launched Nov 2022, integrated into Merpay/Mercari ecosystem

**Strategic partnerships:**
- NTT DOCOMO d Payment: shared QR code since September 2020, joint merchant promotion
- DOCOMO iD contactless: integrated for tap to pay
- JCB merchant network: Mercard accepted across all JCB locations in Japan

**Top 5 Markets Gap Analysis:**

MARKET 1: Japan (100% of users, 18.8M)
  ✅ Currently offer: Visa/MC/JCB, Merpay QR, iD contactless, Mercard, Smart Pay later
  ❌ Missing: Alipay (Chinese tourists), WeChat Pay (Chinese tourists), Konbini (third party), PayPay competitor parity
  💡 Inbound tourism (China, Korea) demands Alipay/WeChat Pay integration. Merpay only serves Japanese residents.

MARKET 2: United States (Mercari Marketplace expansion target)
  ✅ Currently offer: Cards via Mercari US (separate stack)
  ❌ Missing: Merpay rails entirely, ACH, Cash App Pay, Venmo
  💡 Mercari Hop bridges Japan to US shipping but Merpay has no US payment presence. Lost cross border opportunity.

MARKET 3: South Korea (high inbound tourism to Japan)
  ✅ Currently offer: International cards only
  ❌ Missing: KakaoPay, Naver Pay, Toss
  💡 Korean tourists are top inbound source for Japan. KakaoPay has 47M users. Yuno could activate at 1.7M Merpay merchants.

MARKET 4: China (top inbound tourism to Japan)
  ✅ Currently offer: International cards only
  ❌ Missing: Alipay, WeChat Pay, UnionPay
  💡 Alipay and WeChat Pay process majority of Chinese consumer payments. Inbound Chinese tourists cannot use preferred methods at Merpay merchants.

MARKET 5: Southeast Asia (long term Mercari expansion)
  ✅ Currently offer: None
  ❌ Missing: GrabPay, GCash, TrueMoney, DANA, OVO
  💡 SEA digital wallets are dominant. Merpay has zero SEA presence despite Mercari corporate strategy targeting global growth.

**Key meeting angles:**
1. Cross border revenue unlock: Activate inbound tourist payments (Alipay, WeChat Pay, KakaoPay) at 1.7M Merpay merchants
2. Multi PSP orchestration: Replace 5+ fragmented integrations (KOMOJU, SBPS, Antom, NORBr, GMO PG) with single Yuno API
3. BNPL credit risk diversification: Smart routing across acquirers reduces concentration on single network failures
4. Mercari global strategy: Yuno enables Merpay rails to follow Mercari into US, SEA, and beyond without per market engineering
5. Mercard JCB optimization: Smart routing improves card auth rates across JCB merchant network
6. IPO scrutiny: Mercari is publicly listed (TYO: 4385). Payment infrastructure efficiency directly impacts core operating profit reported to investors

**Sources:**
- [Mercari Press Kit and Brand Assets](https://about.mercari.com/en/press/press-kit/mercari/)
- [Merpay Overview, KOMOJU](https://en.komoju.com/blog/payment-method/merpay/)
- [SoftBank Payment Service Merpay Integration](https://www.sbpayment.jp/en/support/how_to_pay/merpay_net/)
- [Antom Docs Merpay Payment Method](https://docs.antom.com/ac/antomop/merpay)
- [NORBr White Label Gateway for MerPay](https://norbr.com/payment-methods/merpay/)
- [Mercari Q4 2025 Financial Results, IR Library](https://about.mercari.com/en/ir/library/results/)
- [Mercari Mercard Launch Press Release](https://about.mercari.com/en/press/news/articles/20221108_mercard/)
- [Mercari, Merpay and NTT DOCOMO Partnership](https://about.mercari.com/en/press/news/articles/docomo/)
- [Japan BNPL Business Report 2026, GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/03/3230815/28124/en/Japan-Buy-Now-Pay-Later-Business-Report-2026-A-52-85-Billion-Market-by-2031-from-16-Billion-in-2025-Featuring-Paidy-PayPal-TsukePay-ZOZO-and-Merpay-Mercari-Smart-Payment.html)
- [Mercari TYO 4385 Stock and Earnings, Stockanalysis](https://stockanalysis.com/quote/tyo/4385/)
