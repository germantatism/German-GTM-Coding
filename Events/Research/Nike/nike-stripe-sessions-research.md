# NIKE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Nike
=======================================

Logo: https://about.nike.com/content/dam/nikeinc/masterbrand/global/en/logos/swoosh/nike-swoosh-black.png
Nombre merchant: Nike

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock In
Tittle_Pain Point_2: 9 Quarter Digital Decline
Tittle_Pain Point_3: Checkout Decline Loops
Tittle_Pain Point_4: APAC Local APM Gaps
Tittle_Pain Point_5: No Failover Layer

Desc_Pain Point_1: Adyen handles Nike's online and in store payments globally with no secondary acquirer confirmed. A single processor dependency across 190+ markets creates systemic risk and zero routing flexibility.
Desc_Pain Point_2: Nike Digital down 9% in Q3 FY2026, the ninth consecutive quarterly decline. Digital revenue fell 21% in Greater China and 12% in APLA. Every lost checkout basis point compounds.
Desc_Pain Point_3: Users report error codes (cb8d4682, 98D2586B) with no explanation. "Payment failed" on SNKRS and Nike App pushes buyers to TikTok for workarounds instead of completing purchases.
Desc_Pain Point_4: Nike operates in Japan, South Korea, and China but PayPay (70M users), KakaoPay, NaverPay, and standalone Alipay/WeChat Pay are not confirmed at checkout.
Desc_Pain Point_5: No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX). When Adyen has issues, Nike has no automatic cascade to a backup processor.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen PSP_2: Klarna PSP_3: Afterpay PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: BLIK (Poland)
Local_M_2: iDEAL (Netherlands)
Local_M_3: PayPay (Japan)
Local_M_4: KakaoPay (South Korea)
Local_M_5: NaverPay (South Korea)
Local_M_6: Toss (South Korea)
Local_M_7: LINE Pay (Japan)
Local_M_8: Przelewy24 (Poland)
Local_M_9: GrabPay (SE Asia)
Local_M_10: DANA (Indonesia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each of Nike's ~56 to 70M annual digital transactions to the optimal acquirer per card BIN, issuer, and market. With $18.8B in DTC revenue across 50+ subsidiaries, even a 1% auth uplift recovers tens of millions. Smart Routing analyzes real time PSP performance per corridor.
Desc_Yuno_Cap2: Add secondary acquirers alongside Adyen with automatic cascade in milliseconds. When a processor declines or slows, Yuno reroutes instantly. NOVA AI recovers up to 75% of soft declines. Livelo recovered 50% of failed transactions using this exact approach.
Desc_Yuno_Cap3: Activate BLIK in Poland, iDEAL in Netherlands, PayPay in Japan, KakaoPay and NaverPay in South Korea, and local wallets across all Nike markets. One API integration, zero per market engineering. InDrive launched 10 LATAM markets in under 8 months.
Desc_Yuno_Cap4: Replace Nike's siloed per market Adyen configuration with one real time dashboard. Centralized approval rate monitoring across all regions and processors. Millisecond anomaly detection via Monitors catches issues before they cascade across 190+ markets.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Nike at a glance:**
- NYSE: NKE. World's largest athletic footwear and apparel company
- FY2025 Total Revenue: $46.3B (down 10% YoY). FY2026 Q3 Revenue: $11.3B (flat reported, down 3% currency neutral)
- Nike Direct (DTC) Revenue: $18.8B in FY2025 (down 13% YoY). Q3 FY2026 Nike Direct: $4.5B (down 4% reported, down 7% currency neutral)
- Nike Digital: down 9% YoY in Q3 FY2026, marking the ninth consecutive quarterly decline
- Greater China Q3 FY2026: digital revenue fell 21% YoY; APLA digital dropped 12%
- Nike.com global monthly visits: ~110M to 148M (range across recent months per Altindex)
- Operates 50+ subsidiaries globally across 190+ countries, with regional domains per market (nike.com.br, nike.com.mx, nike.co.uk, nike.co.jp, etc.)
- New CEO Elliott Hill (October 2024) launched "Win Now" turnaround strategy
- CTO role eliminated December 2025; COO Venkatesh Alagirisamy now oversees Technology + Supply Chain
- CFO Matt Friend now oversees global sales and Nike Direct (digital commerce + retail stores)
- $230M in severance costs in Q3 FY2026, primarily in Supply Chain and Technology units
- No payment orchestration platform confirmed

**Confirmed PSPs:**
- Adyen: Primary acquirer/processor globally (online + in store). Confirmed via Adyen July 2022 press release naming Nike as Tap to Pay on iPhone launch partner. Adyen's unified commerce platform consolidates Nike's global payments.
- Klarna: BNPL provider (Pay in 4, Pay in 30 days) confirmed in US, UK, Ireland, EU. Available via Nike help center.
- Afterpay: BNPL alternative confirmed in US via Afterpay merchant directory.
- PayPal: Digital wallet confirmed for US via Nike help center.
- Venmo: Confirmed for US via third party reporting.
- Apple Pay: Confirmed globally (in app + online) via Nike help center.
- Google Pay: Confirmed globally via Nike help center.
- No third party payment orchestrator detected (Spreedly, Primer, Gr4vy, CellPoint, APEXX, BR DGE, Pagos, or Yuno)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States ($19.6B North America revenue FY2025, ~55 to 65M monthly visits estimated)
  Offer: Visa, Mastercard, Amex, Discover; PayPal, Venmo, Apple Pay, Google Pay; Klarna (Pay in 4), Afterpay; Nike Gift Cards
  Missing: Cash App Pay, ACH direct debit
  Why it matters: US coverage is strong. Minor gap with Cash App Pay (57M+ users). Low priority.

MARKET 2: United Kingdom (~8 to 12M monthly visits estimated, operates via Nike Retail B.V. Netherlands)
  Offer: Visa, Mastercard; Apple Pay, Google Pay; Klarna (BNPL)
  Missing: Open Banking / Pay by Bank (growing adoption in UK e commerce)
  Why it matters: UK open banking usage is accelerating. Not a critical gap but an optimization opportunity.

MARKET 3: Greater China ($6.6B revenue FY2025, operates via nike.com.cn)
  Offer: Not confirmed from Nike specific sources for Chinese local methods
  Missing: Standalone Alipay confirmation, standalone WeChat Pay confirmation
  Why it matters: Alipay + WeChat Pay account for ~90%+ of digital payments in China. Any gap in acceptance directly caps conversion in Nike's third largest revenue market.

MARKET 4: Japan (operates via nike.co.jp, confirmed subsidiary)
  Offer: Credit cards confirmed; additional methods not verified from Nike Japan help page (403 blocked)
  Missing: PayPay (70M+ users), LINE Pay, Rakuten Pay, Konbini payments (not confirmed)
  Why it matters: PayPay has over 70M users. Japan's mobile payments market is ~$280B and growing to $1.07T by 2030. Local wallet coverage is critical.

MARKET 5: Poland (confirmed legal entity per Nike 10 K subsidiary list)
  Offer: Card payments via Adyen; Klarna (EU wide)
  Missing: BLIK (15M+ active users), Przelewy24
  Why it matters: BLIK is the dominant digital payment method in Poland. Nike has operational presence but likely routes Polish customers through EU card networks without local APM support.

**Additional market gaps:**
- Netherlands (Nike European HQ, Hilversum): iDEAL used for ~60% of online transactions. No standalone iDEAL integration confirmed, only possible indirect access via Klarna.
- South Korea (confirmed subsidiary): KakaoPay, NaverPay, and Toss are dominant local wallets. No confirmation of local wallet support at Nike Korea checkout.
- Brazil (nike.com.br, ~6.77M/month): PIX, Boleto, and credit installments confirmed. Strong local coverage.
- Mexico (nike.com.mx): OXXO and SPEI confirmed. Adequate local coverage.
- India (nike.co.in): UPI via Paytm partially confirmed. PhonePe, Google Pay India not confirmed directly from Nike sources.

**Outage and incident history:**
- March 2025: Users reported being unable to place orders through Nike's website or mobile app for nearly a month, with errors appearing when adding products to cart. Messages stated "Mastercard and Visa is unable to process your payment."
- Recurring checkout errors: Error codes cb8d4682, 98D2586B, 1033953938, 0b206bff, cda1b56b appear at checkout with no user friendly explanation. Nike help page only advises "double check shipping and payment details."
- Nike App / SNKRS payment failures: Sufficient volume of issues that dedicated TikTok content exists for troubleshooting. Multiple third party guides published (DigiStatement, tech tips sites).
- Trustpilot (nike.com, 1.5 stars; nike.co.uk): Recurring reports of card declines with no explanation, billing address mismatch declines, false fraud declines on legitimate cards, and inability to use credit cards (only Klarna/PayPal accepted after card change).
- Processing delays: "We're sorry, processing your order is taking longer than usual" messages reported across 2024 to 2025.

**Key meeting angles:**
1. **Nine consecutive quarters of digital decline** | Nike Digital fell 9% in Q3 FY2026 and 21% in Greater China. No payment orchestration layer exists to diagnose whether checkout friction, failed transactions, or APM gaps are contributing. Yuno provides a unified dashboard to finally see why transactions fail.
2. **Technology leadership in flux** | CTO role eliminated. COO Venky Alagirisamy now leads technology. CFO Matt Friend oversees Nike Direct and digital commerce. $230M severance in tech + supply chain. New leadership evaluates vendor relationships. Window to propose payment infrastructure modernization.
3. **Single acquirer dependency** | Adyen processes Nike's global online and in store payments with no confirmed secondary acquirer. A single point of failure across 190+ markets. Yuno adds multi acquirer routing alongside Adyen without replacing the incumbent.
4. **APAC/Europe local APM blind spots** | BLIK in Poland, iDEAL in Netherlands, PayPay in Japan, KakaoPay/NaverPay in South Korea all unconfirmed. Each is the dominant local payment method in its market. Yuno activates all via one API with no per market engineering.
5. **Checkout error pattern** | Users encounter opaque error codes and "payment failed" messages with no recovery path. No automatic retry, no alternative payment suggestion, no failover. NOVA AI could recover up to 75% of soft declines automatically.
6. **Win Now mandate** | CEO Elliott Hill's turnaround strategy means every conversion metric is under scrutiny. With DTC revenue at $18.8B, a 1% approval rate improvement translates to $56M to $87M in recovered revenue at Nike's scale.

**Nike Payments and Technology Leadership:**
- Elliott Hill: President and CEO (returned October 2024). Launched "Win Now" turnaround strategy
- Matthew Friend: EVP and CFO. Now oversees global sales and Nike Direct (digital commerce + retail stores) per December 2025 reorganization
- Venkatesh Alagirisamy: EVP and COO (December 2025). Nearly 20 year Nike veteran. Leads Technology, Supply Chain, Planning, Operations, Manufacturing, Sustainability
- Muge Dogan: Former CTO, departed December 2025 when Nike eliminated the CTO role
- Craig Williams: Former EVP and CCO, departed December 2025 when Nike dissolved the CCO title
- No dedicated external facing VP of Payments identified in public sources

**Recent corporate developments:**
- October 2024: Elliott Hill returns as CEO, replacing John Donahoe
- December 2025: Major C suite restructure. COO role created (Venky Alagirisamy). CTO and CCO roles eliminated. Four regional presidents elevated. CFO takes over Nike Direct
- Q3 FY2026 (March 2026): Total revenue $11.3B (flat). Nike Direct $4.5B (down 7% currency neutral). Nike Digital down 9%. Greater China digital down 21%. Gross margin 40.2% (down 130 bps due to tariffs). $230M severance charge in Tech + Supply Chain
- FY2025: Total revenue $46.3B (down 10%). Nike Direct $18.8B (down 13%). Nike Digital down 20% for full year. Greater China $6.6B (down from $7.7B)
- September 2024: Sofort discontinued as standalone payment method, folded into Klarna. Affected Nike's European checkout (Germany, Austria)
- Strategic pivot: Re engaging wholesale/retail partners (Foot Locker, DSW) after pulling back from DTC only model

**Sources:**
- [Nike FY2025 Investor Release](https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2025/NIKE-Inc--Reports-Fiscal-2025-Fourth-Quarter-and-Full-Year-Results/default.aspx)
- [Nike Q3 FY2026 Earnings Release](https://about.nike.com/en/newsroom/releases/nike-inc-reports-fiscal-2026-third-quarter-results)
- [Nike Q3 FY2026 Investor Relations](https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2026/NIKE-Inc--Reports-Fiscal-2026-Third-Quarter-Results/default.aspx)
- [Nike Q3 FY2026 Earnings Call Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/04/01/nike-nke-q3-2026-earnings-call-transcript/)
- [CNBC: Nike Earnings Q3 2026](https://www.cnbc.com/2026/03/31/nike-nke-earnings-q3-2026.html)
- [CNBC: Nike Q3 2026 Turnaround Drags](https://www.cnbc.com/2026/04/01/nike-q3-2026-turnaround-drags-china-sales-slump.html)
- [Nike 10 K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm)
- [Nike Digital Sales Decline (Digital Commerce 360)](https://www.digitalcommerce360.com/article/nike-digital-sales/)
- [Nike Leadership Changes December 2025 (Digital Commerce 360)](https://www.digitalcommerce360.com/2025/12/03/nike-c-suite-coo-leadership-team-changes/)
- [Nike Leadership Announcement (BusinessWire)](https://www.businesswire.com/news/home/20251202080982/en/NIKE-Inc.-Announces-Senior-Leadership-Changes-to-Accelerate-Win-Now-Actions)
- [Nike Cuts CTO CCO Roles (Retail Dive)](https://www.retaildive.com/news/nike-cuts-chief-technology-commercial-officer-roles-leadership-overhaul/806913/)
- [Nike Salary Data Tech Strategy (Business Report)](https://www.businessreport.com/article/what-nikes-salary-data-reveals-about-its-tech-strategy)
- [Adyen Tap to Pay Press Release (Jul 2022)](https://www.adyen.com/press-and-media/adyen-goes-live-with-tap-to-pay-on-iphone)
- [Adyen Wikipedia (Nike listed as client)](https://en.wikipedia.org/wiki/Adyen)
- [Nike Help: Payment Options](https://www.nike.com/help/a/payment-options)
- [Nike GB Help: Payment Options](https://www.nike.com/gb/help/a/payment-options)
- [Nike Help: Klarna](https://www.nike.com/help/a/klarna-payment)
- [Nike GB Help: BNPL](https://www.nike.com/gb/help/a/buy-now-pay-later)
- [Afterpay: Nike Store](https://www.afterpay.com/en-US/stores/nike)
- [Nike Help: Order Error](https://www.nike.com/help/a/order-error)
- [Nike SNKRS Payment Failed (DigiStatement)](https://digistatement.com/nike-snkrs-third-party-payment-failed-how-to-fix-it/)
- [NikeTalk: Error Code 98D2586B](https://niketalk.com/threads/sorry-we-are-unable-to-process-your-order-for-more-information-code-98d2586b.695355/)
- [UpDownRadar: Nike Status](https://updownradar.com/status/nike.com)
- [Nike Checkout Not Working (Tech Tips Now)](https://tech-tips-now.com/nike-checkout-not-working/)
- [TikTok: Nike App Checkout Error](https://www.tiktok.com/discover/nike-app-checkout-error)
- [Trustpilot: nike.com](https://www.trustpilot.com/review/www.nike.com)
- [Trustpilot: nike.co.uk](https://www.trustpilot.com/review/nike.co.uk)
- [Sofort Deprecation (Solidgate)](https://solidgate.com/blog/klarna-deprecated-sofort-as-a-payment-method/)
- [SimilarWeb: nike.com](https://www.similarweb.com/website/nike.com/)
- [Altindex: Nike Web Traffic](https://altindex.com/ticker/nke/webtraffic)
- [Nike Inc Logos Newsroom](https://about.nike.com/en/newsroom/collections/nike-inc-logos)
- [Brandfetch: Nike Logo](https://brandfetch.com/nike.com)
- [Modern Retail: Nike Digital Decline](https://www.modernretail.co/operations/nike-posts-its-first-digital-decline-in-nine-years/)
- [Nike Digital Transformation (Golden Owl)](https://goldenowl.asia/blog/nikes-digital-transformation-real-examples)
- [Nike DTC Journey (ZoomMetrix)](https://zoommetrix.com/marketing-strategy/nike-dtc-journey-ambition-challenges-and-realignment/)
- [WWD: Nike Q3 2026 Earnings](https://wwd.com/footwear-news/shoe-industry-news/nike-nke-q3-2026-earnings-china-declines-1238694938/)
- [Nike Q3 FY2026 (YSBR)](https://youthsportsbusinessreport.com/nike-q3-fy2026-flat-revenue-tariff-pressure-and-wholesale-channel-growth/)
- [Does Nike Take Apple Pay (Kudos)](https://www.joinkudos.com/blog/does-nike-take-apple-pay)
- [PayPay Japan Users and Market (Shuttle Global)](https://www.shuttleglobal.com/blog/the-most-popular-payment-methods-in-japan/)
- [KakaoPay vs NaverPay (Inquivix)](https://inquivix.com/naver-pay-vs-kakao-pay/)
- [South Korea Local Payments (Tazapay)](https://tazapay.com/blog/south-korea-local-payment-methods)
- [Nike MX Help: OXXO](https://www.nike.com/mx/help/a/oxxo)
- [Nike BR Terms of Sale](https://atendimento.nike.com.br/hc/pt-br/articles/21912374813587)
