# NINTENDO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Nintendo
=======================================

Logo: https://companieslogo.com/img/orig/NTDOY-e1382f3e.png
Nombre merchant: Nintendo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Region Locked eShop Silos
Tittle_Pain Point_2: Card Decline Dead Ends
Tittle_Pain Point_3: Japan Payment Fortress
Tittle_Pain Point_4: Zero APMs Outside Japan
Tittle_Pain Point_5: No Failover Architecture

Desc_Pain Point_1: Nintendo eShop locks payment methods to the account's country. Cards from one region are automatically rejected in another. Users cannot change region without losing wallet balance. This fragments 128M annual active Switch users into 50+ isolated payment silos with no cross border flexibility.
Desc_Pain Point_2: Error codes 2813-2470 and 9001-2470 appear at eShop checkout with the message "contact your card issuer." No retry logic, no alternative payment suggestion. Users are directed to buy prepaid gift cards as the only workaround, adding friction and abandonment.
Desc_Pain Point_3: Since March 25, 2025, Japan eShop rejects all overseas credit cards and foreign PayPal accounts, citing fraud prevention. Only Japanese issued cards, Japanese PayPal, and prepaid eShop codes accepted. This locks out international fans and limits payment flexibility in Nintendo's home market.
Desc_Pain Point_4: US eShop accepts only credit cards, PayPal, and prepaid cards. No Apple Pay, no Google Pay, no BNPL. Europe has Apple Pay and Google Pay but lacks BLIK, iDEAL, and local wallets. LATAM has cards only. No PIX, no Boleto, no local wallets in any non Japan market.
Desc_Pain Point_5: No payment orchestration layer confirmed for Nintendo eShop. When a card is declined, there is no cascade to PayPal or wallet. With 34M Switch Online subscribers and digital sales now 55%+ of software revenue, each failed transaction is lost recurring or impulse purchase revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Internal/Regional Acquirers PSP_2: PayPal PSP_3: Apple Pay (EU only) PSP_4: Google Pay (EU only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: BLIK (Poland)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Boleto (Brazil)
Local_M_5: KakaoPay (South Korea)
Local_M_6: GrabPay (SE Asia)
Local_M_7: DANA (Indonesia)
Local_M_8: PayPay (outside Japan)
Local_M_9: Apple Pay (US eShop)
Local_M_10: Google Pay (US eShop)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each eShop and Switch Online transaction to the optimal acquirer per card BIN, issuer, and market. With 2.25 trillion yen (~$15B) in FY2026 net sales and 34M Switch Online subscribers, even a 1% auth uplift recovers tens of millions annually. Smart Routing boosts approval rates 3 to 10%.
Desc_Yuno_Cap2: When a card is declined at eShop checkout, Yuno cascades instantly to PayPal, wallet, or an alternative acquirer. NOVA AI recovers up to 75% of soft declines, replacing dead end error codes like 2813-2470 with automatic retry. Livelo recovered 50% of failed transactions with this approach.
Desc_Yuno_Cap3: Activate PIX and Boleto in Brazil, BLIK in Poland, iDEAL in Netherlands, KakaoPay in South Korea, and Apple Pay/Google Pay in US eShop. One API integration, no per region engineering. InDrive launched 10 LATAM markets in under 8 months using Yuno's single connection.
Desc_Yuno_Cap4: Replace Nintendo's 50+ siloed regional eShop payment configurations with one real time dashboard. Centralized approval rate monitoring for 128M annual active users across all markets. Millisecond anomaly detection catches payment issues before they cascade during game launches or Switch Online renewal cycles.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Nintendo at a glance:**
- TYO: 7974 / OTC: NTDOY. Japanese multinational video game company
- FY2026 (ending March 2026) Revised Net Sales Forecast: 2.25 trillion yen (~$15B), up 93.1% YoY
- FY2026 Revised Net Profit Forecast: 350 billion yen (~$2.3B), up 25.5% YoY
- Q3 FY2026 (Holiday 2025): $5.147B in net sales, $991M operating profit
- Nintendo Switch lifetime sales: 155.37M units (Nintendo's best selling console)
- Nintendo Switch 2: Launched June 5, 2025 at $449.99. 17.37M units sold by December 2025. Revised target: 19M units FY2026
- Annual Active Switch Users: 128M (April 2024 to March 2025)
- Nintendo Switch Online Subscribers: 34M (September 2025), 35% on premium Expansion Pack tier
- Nintendo Accounts: 400M total
- Digital software sales: 55%+ of total software revenue FY2025, up from 50.2% FY2024
- Switch Online revenue: $1.19B in 2024 (up 19% YoY)
- Indie titles: 24% of total eShop digital sales volume

**Confirmed PSPs and Payment Infrastructure:**
- Internal/Regional Acquirers: Nintendo processes eShop payments through regional infrastructure, with no global acquirer publicly confirmed. Payment methods strictly tied to account region
- PayPal: Confirmed for US, Canada, Mexico eShop. Also confirmed in Japan (Japanese accounts only, since March 25, 2025). Available in Europe
- Apple Pay: Confirmed for My Nintendo Store Europe (UK, EU). NOT available on US eShop
- Google Pay: Confirmed for My Nintendo Store Europe. NOT available on US eShop
- Credit/Debit Cards: Visa, Mastercard accepted across regions. Region locked (card must match account country)
- Nintendo eShop Prepaid Cards: Available globally via retail. Currency/region specific
- No BNPL confirmed (no Klarna, Afterpay, Zip)
- No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**eShop Payment Methods by Region:**

REGION: United States / Canada / Mexico
  Accepted: Visa, Mastercard, PayPal, Nintendo eShop prepaid cards
  Missing: Apple Pay, Google Pay, Cash App Pay, Venmo, any BNPL
  Note: Most limited major region. No digital wallets at all

REGION: Europe (UK, Germany, France, etc.)
  Accepted: Credit/debit cards, PayPal, Apple Pay, Google Pay, Nintendo eShop prepaid cards
  Missing: BLIK (Poland), iDEAL (Netherlands), Bancontact (Belgium), Giropay (Germany), MB Way (Portugal)
  Note: Best non Japan coverage with Apple Pay and Google Pay

REGION: Japan
  Accepted: Japanese credit/debit cards, Japanese PayPal, Nintendo eShop prepaid cards
  Missing: PayPay (70M+ users), LINE Pay, Rakuten Pay, Merpay, Suica/IC cards
  Note: As of March 25, 2025, foreign cards and foreign PayPal accounts blocked. Cited "fraudulent use"

REGION: Latin America (Argentina, Chile, Colombia, Peru, Brazil)
  Accepted: Visa and Mastercard credit/debit cards, Nintendo eShop cards
  Missing: PIX (Brazil, 150M+ users), Boleto, MercadoPago, OXXO (Mexico), PSE (Colombia)
  Note: PayPal NOT accepted. Cards only plus prepaid

REGION: South Korea
  Accepted: Credit/debit cards, Nintendo eShop prepaid cards
  Missing: KakaoPay, NaverPay, Toss (dominant local wallets)

REGION: Southeast Asia / Oceania
  Accepted: Credit/debit cards, Nintendo eShop prepaid cards
  Missing: GrabPay, DANA, GCash, TrueMoney, OVO

**Payment Issues and Incidents:**
- Error 2813-2470: "There was an issue processing your transaction. Contact your card issuer." Common eShop checkout error. No retry, no alternative offered. Users must manually try gift cards
- Error 9001-2470: Similar transaction processing failure. Nintendo support suggests waiting and trying again or using a different payment method
- "Credit card's issuing country is not compatible": Region lock enforcement error. Card must be issued in the same country as the Nintendo Account. No workaround except purchasing region specific prepaid cards
- Japan foreign payment block (March 25, 2025): All overseas credit cards and foreign PayPal accounts blocked on Japanese eShop and My Nintendo Store. Only Japanese issued payment methods accepted. Community backlash from international Nintendo fans
- No automatic failover: When card payment fails, no cascade to PayPal or wallet. User must navigate away from checkout to add alternative payment. High abandonment risk during impulse game purchases
- Duplicate/held charges: Nintendo support documents cases of held funds, pending, or duplicate charges appearing on cards. Payment processing delays create user confusion

**Key meeting angles:**
1. **US eShop has zero digital wallets** | Nintendo's largest revenue market offers only credit cards, PayPal, and prepaid cards. No Apple Pay, no Google Pay, no BNPL. Sony and Xbox accept Apple Pay, Cash App Pay, and Venmo. Nintendo trails competitors in checkout modernization. Yuno enables all wallets via one integration.
2. **128M active users, 34M subscribers, no orchestration** | Every failed Switch Online renewal at $19.99 to $49.99/year is lost recurring revenue. With no failover or smart retry, Nintendo relies on users manually resolving payment errors. NOVA AI could recover up to 75% of soft declines automatically.
3. **Japan payment lockdown creates opportunity** | Nintendo blocked foreign payments in Japan to fight fraud. An orchestration layer with real time fraud scoring (like Yuno's) could enable cross border payments while filtering bad actors, rather than blanket blocking legitimate international customers.
4. **Switch 2 launch amplifies the gap** | At $449.99, Switch 2 is Nintendo's most expensive console. 17.37M sold in 6 months with 19M target. High ticket purchases increase decline rates. No BNPL option on any Nintendo store means price sensitive buyers have no installment path.
5. **Digital is now majority revenue** | Digital sales crossed 55% of software revenue. The eShop is no longer supplementary, it is the primary sales channel. Payment infrastructure that was acceptable when physical was dominant now directly gates revenue growth. Each missing APM is a conversion ceiling.

**Nintendo Payments and Leadership:**
- Shuntaro Furukawa: President and Representative Director of Nintendo Co., Ltd.
- Ko Shiota: Director and Senior Managing Executive Officer. Oversees technology and platform development
- Satoru Shibata: Director. Former President of Nintendo of Europe
- Shigeru Miyamoto: Representative Director, Fellow. Creative lead
- Doug Bowser: President of Nintendo of America
- No dedicated VP of Payments or CFO publicly highlighted for payment strategy
- Nintendo does not operate its own payment services subsidiary (unlike Sony Payment Services)

**Recent corporate developments:**
- June 2025: Nintendo Switch 2 launches at $449.99. 17.37M units sold by December 2025
- March 2025: Japan eShop blocks all foreign credit cards and foreign PayPal accounts (effective March 25, 2025)
- November 2025: Nintendo reports 34M Switch Online subscribers, 400M Nintendo Accounts, 128M annual active Switch users
- FY2026 revised forecast: Net sales 2.25 trillion yen (up 93.1%), net profit 350 billion yen (up 25.5%)
- FY2025: Digital software ratio crosses 55% of total. Switch Online revenue $1.19B (up 19%)
- Nintendo Switch total lifetime sales: 155.37M units
- Switch 2 FY2026 target raised: 19M hardware units, 48M software units

**Sources:**
- [Nintendo eShop Payment Methods US (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/22327/)
- [My Nintendo Store Payments UK (Nintendo UK)](https://www.nintendo.com/en-gb/Support/Purchases-Subscriptions/My-Nintendo-Store-Payments-3057873.html)
- [Nintendo eShop LATAM (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/56056/)
- [LATAM Add Funds (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/53942/)
- [Japan eShop Blocks Foreign Payments (Nintendo Life)](https://www.nintendolife.com/news/2025/01/japans-switch-eshop-will-soon-no-longer-accept-overseas-payment-methods)
- [Japan eShop Foreign Payment Discontinued (Play Asia)](https://play.asia/blog/2025/01/31/nintendo-eshop-japan-foreign-payment-methods-will-be-discontinued-on-march-25/)
- [Japan eShop Rejects Foreign Cards (Game8)](https://game8.co/articles/latest/nintendo-japan-eshop-now-rejects-foreign-credit-cards-and-paypal-accounts)
- [Error Code 2813-2470 (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/48688/)
- [Error Code 9001-2470 (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/48692/)
- [Credit Card Country Error (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/28987/)
- [Contact Card Issuer Error (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/28989/)
- [Unable to Use Credit Card (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/49641/)
- [Blocked Digital Content Purchase (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/3085/)
- [Link PayPal to Nintendo (Nintendo Support)](https://en-americas-support.nintendo.com/app/answers/detail/a_id/27248/)
- [Does Nintendo Take Apple Pay (Kudos)](https://www.joinkudos.com/blog/does-nintendo-take-apple-pay)
- [Nintendo Statistics 2025 (SQ Magazine)](https://sqmagazine.co.uk/nintendo-statistics/)
- [Nintendo Switch Statistics 2026 (Icon Era)](https://icon-era.com/statistics/nintendo-switch/)
- [Nintendo Q2 FY2026 Financial Results (GoNintendo)](https://gonintendo.com/contents/54587)
- [Nintendo Q3 FY2026 (TweakTown)](https://www.tweaktown.com/news/110002/nintendo-scores-dollars5-1-billion-net-sales-and-19-percent-margin-through-holiday-2025/index.html)
- [Nintendo Revised Forecast (Niko Partners)](https://substack.nikopartners.com/p/nintendo-revised-earnings-forecast)
- [Nintendo FY2025 Results (Nintendo IR)](https://www.nintendo.co.jp/ir/pdf/2025/250508_4e.pdf)
- [Nintendo Q1 FY2026 Results (Nintendo IR)](https://www.nintendo.co.jp/ir/pdf/2025/250801_2e.pdf)
- [Nintendo Switch Online Subscribers (Nintendo Life)](https://www.nintendolife.com/news/2025/11/nintendo-shares-updated-figures-for-registered-accounts-and-switch-online-members)
- [Nintendo Switch Online Wikipedia](https://en.wikipedia.org/wiki/Nintendo_Switch_Online)
- [Nintendo eShop Not Available Guide (DevRunners)](https://devrunners.com/blog/nintendo-eshop-region-guide/)
- [Nintendo Logo (CompaniesLogo)](https://companieslogo.com/nintendo/logo/)
