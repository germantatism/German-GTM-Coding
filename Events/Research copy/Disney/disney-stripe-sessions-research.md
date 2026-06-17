# DISNEY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Disney
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/DIS_BIG-38bf9cd8.png
Nombre merchant: Disney

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Payment Stack
Tittle_Pain Point_2: Cross-Border Decline Rate
Tittle_Pain Point_3: Single Point of Failure
Tittle_Pain Point_4: Missing Local APMs
Tittle_Pain Point_5: Involuntary Churn Leak

Desc_Pain Point_1: Disney operates siloed payment systems across Disney+, Parks, Cruise, and shopDisney. No unified orchestration layer connects streaming, ecommerce, and in-park POS, creating reconciliation blind spots across $94.4B in annual revenue.
Desc_Pain Point_2: International cards are systematically declined on Disney+ and park booking flows. Foreign bank verification systems are incompatible with Disney's gateway, auto-rejecting valid cards before they reach the issuer.
Desc_Pain Point_3: September 2024: company-wide payment outage killed Lightning Lane, Mobile Checkout, Mobile Food Orders, and shopDisney simultaneously for 100K+ guests. No failover routed transactions to a backup processor.
Desc_Pain Point_4: Disney+ Brazil has no Pix (70%+ of local digital payments). No Konbini in Japan. No KakaoPay in Korea. No iDEAL in Netherlands. 75% of revenue outside the Americas has limited local method coverage.
Desc_Pain Point_5: Disney+ churn hit 8% in Sept 2025 (2x normal). With 40% of churn typically involuntary (failed payments), optimizing retry logic and smart routing could recover millions in lost recurring revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: PayPal / Braintree
PSP_2: Chase Paymentech (JPMorgan)
PSP_3: Apple App Store (IAP)
PSP_4: Google Play (IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: Konbini
Local_M_3: KakaoPay
Local_M_4: iDEAL
Local_M_5: Bancontact
Local_M_6: GrabPay
Local_M_7: DANA
Local_M_8: GCash
Local_M_9: Naver Pay
Local_M_10: BLIK

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Disney's multiple processors. Each Disney+ renewal, park booking, and merchandise purchase routed to the highest performing acquirer for that card BIN, issuer, and market. On $94.4B revenue with 150+ country exposure, even a 3% auth uplift translates to hundreds of millions in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates the single point of failure exposed in September 2024. When the primary processor declines or goes down, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions, turning the 8% churn spike into retained subscribers and park bookings.
Desc_Yuno_Cap3: Activates the APMs Disney is missing: Pix in Brazil (5.88% of Disney+ traffic), Konbini in Japan, KakaoPay and Naver Pay in Korea, iDEAL in Netherlands, BLIK in Poland, GrabPay and DANA in Southeast Asia. One API, 1,000+ payment methods, instant geo-routing per market.
Desc_Yuno_Cap4: One dashboard replacing Disney's fragmented payment stacks across Disney+, shopDisney, Parks, and Cruise. Real-time approval rate monitoring, centralized reconciliation across all processors and currencies, millisecond anomaly detection via NOVA (75% faster fraud review). Single integration for streaming, ecommerce, and omnichannel.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Disney at a glance:**
- The Walt Disney Company (NYSE: DIS). Market cap ~$195B
- Fiscal year 2025 revenue: $94.4B (+3% YoY from $91.4B in FY2024)
- Revenue by region: Americas 79% ($72.2B), Europe 11.3% ($10.3B), Asia Pacific 9.8% ($8.9B)
- Revenue by segment: Entertainment $41B+, Parks & Experiences $34.2B, ESPN/Sports ~$18B
- Disney+ subscribers: 132M globally (Q4 2025). Available in 150+ countries, 39 languages
- DTC streaming operating income: $1.3B in FY2025 (up ~9x from prior year; was a $4B annual loss just 3 years ago)
- Parks & Experiences: 6 resort destinations, 12 theme parks, 5 cruise ships (Disney Treasure launched Dec 2024)
- shopDisney: ecommerce for merchandise across US, UK, EU, Japan
- Disney+ ARPU: Core $7.30, Hotstar $0.78 (Q4 2024)

**Disney+ Top Traffic Markets:**
1. United States: 24.76%
2. United Kingdom: 6.53%
3. Brazil: 5.88%
4. Canada: 4.71%
5. Germany: 4.37%

**Confirmed PSPs and Payment Infrastructure:**
- PayPal: confirmed on Disney Store, Disney+, and Parks (was the only working method during Sep 2024 outage). Braintree (PayPal subsidiary) likely handles card processing for Disney+ based on PayPal's deep integration
- Chase Paymentech (JPMorgan): Disney's primary banking relationship is with JPMorgan Chase; Chase Paymentech is the likely card acquirer for Parks and ecommerce given Disney's enterprise scale and JPMorgan relationship
- Apple App Store: mobile IAP for Disney+ on iOS
- Google Play: mobile IAP for Disney+ on Android
- NCR/Omnico (MATRA): POS system used across Walt Disney World and Disneyland for merchandise and food & beverage
- MagicBand/MagicMobile: proprietary NFC/RFID payment wearable linked to credit cards for in-park purchases
- No payment orchestrator detected
- No dedicated VP/Head of Payments identified publicly. Payment infrastructure likely sits under Product Engineering (Commerce, Data & Identity division)

**Key Leadership:**
- CEO: Bob Iger (returned November 2022)
- CFO: Hugh Johnston (Senior EVP and CFO)
- EVP Finance: Brent A. Woodford (Controllership, Finance & Tax)
- CTO/Product Engineering: oversees Commerce, Data & Identity platform (streaming, identity, growth)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (24.76% of Disney+ traffic, 79% of total revenue)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Disney Gift Cards, Click to Pay, MagicBand (parks)
  Missing: ACH Direct Debit, Venmo (standalone), Cash App Pay, Affirm/BNPL
  Insight: Disney already covers cards well domestically. The gap is in alternative checkouts for younger audiences and BNPL for high-ticket park bookings ($5K+ family vacations).

MARKET 2: Brazil (5.88% of Disney+ traffic, fastest growing LATAM market)
  Currently offer: Visa/MC via international rails, Boleto referenced in some docs
  Missing: Pix, Mercado Pago, local installment cards (parcelamento)
  Insight: Pix processed 6.2B+ monthly transactions by March 2025 and handles 70%+ of digital payments in Brazil. Disney+ does NOT accept Pix directly. Users must workaround via prepaid cards. Massive conversion loss.

MARKET 3: United Kingdom (6.53% of Disney+ traffic)
  Currently offer: Visa/MC/Amex, PayPal
  Missing: Open Banking (Pay by Bank), Klarna
  Insight: UK Open Banking adoption is growing rapidly. Pay by Bank reduces interchange costs. Klarna has 18M+ UK users.

MARKET 4: Germany (4.37% of Disney+ traffic)
  Currently offer: Visa/MC, PayPal
  Missing: SEPA Direct Debit, Sofort/Wero, Giropay, Klarna PayNow
  Insight: Only ~35% credit card penetration in Germany. SEPA DD is the backbone of subscription billing. Without it, Disney+ is friction-heavy for 65% of the population.

MARKET 5: Japan (major market, Tokyo Disney Resort)
  Currently offer: Visa/MC/JCB, carrier billing (via app stores)
  Missing: Konbini, PayPay (70M+ users), Rakuten Pay, LINE Pay
  Insight: Konbini is the #2 online payment method in Japan at 10% of ecommerce. PayPay has 70M+ users (1 in 2 Japanese people). Tokyo Disney Resort is the only Disney park NOT owned by Disney (operated by Oriental Land Co.), but Disney+ and merchandise sales go through Disney's own payment rails.

**Additional Market Gaps:**
- South Korea: Missing KakaoPay, Naver Pay, Toss. Korea has 95%+ digital payment adoption.
- Netherlands: Missing iDEAL (handles $141B+ annually, dominant local method)
- Belgium: Missing Bancontact (73% of consumers prefer it)
- Indonesia: Missing DANA, OVO, GoPay. Disney+ rebranded from Hotstar in Oct 2025.
- Philippines: Missing GCash (60M+ users), Maya
- Poland: Missing BLIK (dominant mobile payment, 70%+ of online payments)
- India: Disney+ merged with JioCinema in Feb 2025 to form JioHotstar (joint venture with Reliance). Payment is now handled by Jio's infrastructure.

**Payment Outage History:**

September 23, 2024: Major Company-Wide Outage
- ALL domestic Disney Parks payment systems went down simultaneously
- Affected: shopDisney.com, My Disney Experience app, Disneyland app
- Guests could not book Lightning Lanes, use Mobile Checkout, or use Mobile Food Orders
- Guest Services was also unable to make Lightning Lane selections or dining reservations
- Only PayPal was partially functional in select flows during the outage
- Impact: 100,000+ guests affected across Walt Disney World and Disneyland
- Resolution: Systems restored by ~12:15 PM ET (approximately 4+ hour outage)
- Root cause: Never publicly disclosed, but all card processing failed simultaneously while PayPal remained partially operational, suggesting the primary card acquirer/gateway went down

October 2024: Second Outage
- Walt Disney World and Disneyland websites experienced widespread technical issues
- Both website and app systems were affected

September 2024: Earlier Digital Outage
- MagicBand and app issues reported at both Disneyland and Disney World

July 2024: Global Lockout
- Disney guests worldwide locked out of parks and hotels systems

Disney+ Payment Issues (Ongoing):
- "Why is Disney+ not taking my payment?" is a permanent help article on Disney's support site
- International card declines are widely reported: foreign bank verification systems are incompatible with Disney's gateway
- Cards are auto-declined before the request reaches the issuer
- Multiple user forums document persistent payment failures

**Key Meeting Angles:**

1. September 2024 Outage as Proof Point: A single acquirer failure shut down payments across every Disney property simultaneously. Yuno's failover would have automatically cascaded to a backup processor in milliseconds.

2. Streaming Profitability Inflection: Disney+ just went from $4B annual loss to $1.3B profit. Every basis point of auth rate improvement directly hits the bottom line at a critical moment for investor confidence.

3. Involuntary Churn at Scale: At 132M subscribers and 8% churn, even recovering 10% of involuntary churn (failed payments) at $7.30 ARPU = $77M+ annually.

4. Brazil is Bleeding Conversions: 5.88% of Disney+ traffic comes from Brazil where Pix is 70%+ of digital payments and Disney does NOT accept it. Direct revenue loss.

5. Omnichannel Complexity: Disney processes payments across streaming (Disney+), ecommerce (shopDisney), theme parks (6 resorts), cruise ships (5 vessels), and mobile apps. No single orchestration layer ties them together.

6. Parks International Expansion: International parks grew operating income 28% in Q1 FY2025. WeChat Pay, Alipay, and local wallets for Chinese, Korean, and Japanese tourists visiting US parks would lift per-capita spend.

7. Competitor Precedent: Netflix (multi-PSP with Adyen + Stripe + local acquirers), Spotify (Adyen as primary orchestrator), Apple TV+ (native payment orchestration). Disney's payment sophistication lags these peers.

**Yuno Reference Points:**
- Smart Routing: +3-10% authorization uplift per transaction
- Failover: Up to 50% recovery on initially failed transactions
- NOVA (Anti-Fraud): 75% faster fraud review with ML-powered decisioning
- 1,000+ APMs available across 40+ countries
- Success Cases: InDrive (global ride-hailing, multi-PSP routing), Rappi (LATAM super-app, local APM coverage), McDonald's (omnichannel orchestration), Wingo (airline, cross-border payments)

**Sources:**
- [Disney FY2025 Earnings](https://thewaltdisneycompany.com/press-releases/the-walt-disney-company-reports-fourth-quarter-and-full-year-earnings-for-fiscal-2025/)
- [Disney FY2024 Annual Report](https://thewaltdisneycompany.com/app/uploads/2025/01/2024-Annual-Report.pdf)
- [Disney Revenue by Region](https://bullfincher.io/companies/the-walt-disney-company/revenue-by-geography)
- [Disney+ Subscriber Stats (DemandSage)](https://www.demandsage.com/disney-users/)
- [Disney+ Subscriber Stats (Evoca)](https://evoca.tv/disney-plus-users-statistics/)
- [Disney+ Payment Methods Help](https://help.disneyplus.com/article/disneyplus-payment-methods)
- [Disney Store Payment Types](https://support.disneystore.com/hc/en-us/articles/5610168888339-What-payment-types-can-I-use)
- [Disney Sept 2024 Payment Outage (WDWNT)](https://wdwnt.com/2024/09/disney-experiencing-company-wide-payment-issues/)
- [Disney Sept 2024 Outage (InsideTheMagic)](https://insidethemagic.net/2024/09/disney-payment-options-shut-down-ad1/)
- [Disney Sept 2024 Outage (AllEars)](https://allears.net/2024/09/23/disney-is-having-a-rough-morning-issues-with-payment-options-are-affecting-disney-world-and-disneyland/)
- [Disney Oct 2024 Tech Issues](https://wdwnt.com/2024/10/walt-disney-world-disneyland-technical-issues-10/)
- [Disney+ Payment Declined Help](https://help.disneyplus.com/article/disneyplus-payment-not-processed)
- [Disney+ International Card Issues (TripAdvisor)](https://www.tripadvisor.com/ShowTopic-g34515-i19-k7133883-Disney_keep_declining_my_Credit_card-Orlando_Florida.html)
- [Disney+ Churn Rate (Yahoo Finance)](https://finance.yahoo.com/news/disney-churn-rate-one-number-222645851.html)
- [Disney+ Pix Brazil Workaround (RecargaPay)](https://recargapay.com.br/pix/disney-plus-pagar-pix)
- [Disney DTC Profitability (StreamTV)](https://www.streamtvinsider.com/video/disney-dtc-profitability-surges-ceo-outlines-3-pillars-streaming-growth)
- [Disney Parks Revenue Record](https://www.themeparkinsider.com/flume/202411/10567/)
- [Disney International Parks Growth](https://www.themeparkinsider.com/flume/202502/10704/)
- [Disney Privacy Policy](https://privacy.thewaltdisneycompany.com/en/current-privacy-policy/)
- [Disney Leadership](https://thewaltdisneycompany.com/about/)
- [Disney+ Press Logos](https://press.disneyplus.com/about/logos)
- [Disney Logo (CompaniesLogo)](https://companieslogo.com/walt-disney/logo/)
- [Walt Disney World POS System Forum](https://forums.wdwmagic.com/threads/odd-question-wdw-pos-system.898963/)
- [Walt Disney World Payment Methods](https://touringplans.com/blog/faq-how-can-i-pay-for-things-at-disney-world/)
- [Failed Payments $129B Cost (Recurly)](https://recurly.com/press/failed-payments-could-cost-subscription-companies-more-than-129-billion-in-2025-us/)
- [Disney+ Nearing 200M Subscribers](https://senalnews.com/en/data/disney-nears-200-million-streaming-subscribers-amid-strategic-shift)
- [Disney WDW Apple Pay Forums](https://forums.wdwmagic.com/threads/does-disney-world-accept-apple-pay.923977/)
- [Pix Q1 2025 Statistics](https://fasterpaymentscouncil.org/userfiles/2080/files/Pix%20by%20the%20Numbers%20Q1%202025.pdf)
