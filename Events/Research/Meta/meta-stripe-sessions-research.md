# META | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Meta
=======================================

Logo: https://companieslogo.com/img/orig/META-b2eb7a39.png
Nombre merchant: Meta

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Mass Ad Payment Failures
Tittle_Pain Point_2: Billing Model Upheaval
Tittle_Pain Point_3: Single Acquirer Dependency
Tittle_Pain Point_4: Cross Border Card Declines
Tittle_Pain Point_5: Quest Store Checkout Gaps

Desc_Pain Point_1: In 2025, Meta's updated anti fraud module triggered widespread payment errors across advertiser accounts. Even long trusted accounts saw payments declined. Stricter BIN screening and 3DS enforcement paused campaigns with no warning, directly reducing Meta's $164B ad revenue stream.
Desc_Pain Point_2: Starting April 2026, Meta removed credit card payments for high spend ad accounts (est. $50K+/month), forcing monthly invoicing or direct debit. Direct debit only works in US and SEPA. Advertisers in LATAM, APAC, and Africa face limited payment options and churn risk.
Desc_Pain Point_3: Adyen confirmed as a key payment processor for Meta. No secondary acquirer or orchestration layer publicly identified. A single processor dependency across 10M+ advertisers creates systemic risk if Adyen experiences latency or regional outages.
Desc_Pain Point_4: Banks flag Meta's international charges, especially for advertisers outside the US and EU. Geo/IP mismatches between account location and card origin trigger automatic rejections. Non 3DS cards and regional debit cards are frequently declined without retry logic.
Desc_Pain Point_5: Meta Quest / Horizon Store accepts only Visa, Mastercard, Amex, PayPal, and gift cards. No BNPL, no local wallets, no regional methods. Users report persistent "payment declined" errors when adding cards, with no alternative offered at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen PSP_2: Stripe PSP_3: PayPal/Braintree PSP_4: Internal (Meta Pay)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: BLIK (Poland)
Local_M_3: iDEAL (Netherlands)
Local_M_4: GrabPay (SE Asia)
Local_M_5: DANA (Indonesia)
Local_M_6: GCash (Philippines)
Local_M_7: KakaoPay (South Korea)
Local_M_8: PayPay (Japan)
Local_M_9: M Pesa (Africa)
Local_M_10: MercadoPago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Payment Dashboard

Desc_Yuno_Cap1: Route each of Meta's billions of annual ad billing transactions to the optimal acquirer per card BIN, issuer, and geography. With $164B in ad revenue across 10M+ advertisers globally, even a 0.5% auth rate improvement recovers hundreds of millions. Smart Routing analyzes real time PSP performance per corridor, boosting approval 3 to 10%.
Desc_Yuno_Cap2: Add secondary processors alongside Adyen with automatic cascade in milliseconds. When a processor declines or slows, Yuno reroutes instantly. NOVA AI recovers up to 75% of soft declines, the exact error type that paused thousands of advertiser campaigns in 2025. Livelo recovered 50% of failed transactions using this approach.
Desc_Yuno_Cap3: Activate PIX in Brazil, BLIK in Poland, iDEAL in Netherlands, GrabPay in Southeast Asia, M Pesa in Africa, and local wallets across all Meta markets. One API integration enables 1,000+ methods. InDrive launched 10 LATAM markets in under 8 months with Yuno's single connection.
Desc_Yuno_Cap4: Replace siloed payment visibility across Adyen, Stripe, PayPal, and internal systems with one real time dashboard. Centralized approval rate monitoring across all advertiser billing channels and regions. Millisecond anomaly detection catches mass payment failures before they cascade and pause campaigns at scale.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Meta at a glance:**
- NASDAQ: META. World's largest social media and advertising company
- FY2025 Total Revenue: $200.97B (up 22% YoY). Q4 2025 Revenue: $59.89B (up 24% YoY)
- Q1 2026 Revenue Guidance: $53.5B to $56.5B (foreign currency ~4% tailwind)
- Advertising Revenue: ~98% of total revenue. Ad impressions up 12% YoY FY2025, average price per ad up 9%
- Family of Apps Daily Active People (DAP): 3.58B (December 2025, up 7% YoY)
- Operations in 80+ cities globally, 100+ subsidiaries worldwide
- FY2025 Operating Income: ~$24.7B in Q4 alone, 41% operating margin
- FY2026 Capex Guidance: $115B to $135B (massive AI infrastructure investment)
- FY2026 Total Expense Guidance: $162B to $169B
- Key products: Facebook, Instagram, Messenger, WhatsApp, Meta Quest / Horizon, Threads

**Confirmed PSPs and Payment Infrastructure:**
- Adyen: Confirmed processor. Adyen publicly lists Meta as a key client. Adyen grew alongside Meta as a scaling platform per Scuttleblurb analysis and Adyen investor materials
- Stripe: Powers one click checkout for Facebook ads (announced March 2026). Stripe's Agentic Commerce Protocol enables merchants like Fanatics and Quince to sell directly inside Facebook ad units. Stripe processes payments on behalf of merchants advertising on Meta, not Meta's own ad billing
- PayPal / Braintree: PayPal accepted as a payment method for Meta ads billing and Meta Quest Store. Braintree (PayPal subsidiary) likely processes some PayPal wallet transactions within Meta ecosystem
- Internal (Meta Pay): Meta's own digital wallet across Facebook, Instagram, Messenger, WhatsApp. Stores card credentials for one click purchases. Operates as a wallet layer, not a processor
- Apple Pay: Accepted on Meta Quest Store (limited availability)
- Google Pay: Accepted on Meta Quest Store (limited availability)
- No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Ad Billing Payment Methods by Region:**
- Global (automatic billing): Visa, Mastercard, American Express, PayPal
- United States: Credit/debit cards, PayPal, direct debit, monthly invoicing (for high spend accounts post April 2026)
- EU/SEPA: Credit/debit cards, PayPal, direct debit, monthly invoicing
- Brazil: Boleto Bancario (manual payments), credit/debit cards. PIX NOT confirmed for Meta ads
- India: Credit/debit cards, UPI, Paytm, Net Banking (manual payments)
- Most other markets: Credit/debit cards only, with limited local method support

**Meta Quest / Horizon Store Payment Methods:**
- Credit/debit cards: Visa, Mastercard, American Express
- PayPal
- Meta Horizon Store gift cards
- Apple Pay and Google Pay (limited availability)
- No BNPL options (Sezzle lists Meta Quest on its site but not natively integrated)
- No local wallets or regional methods

**WhatsApp Pay Status (April 2026):**
- Live for consumers: India (UPI based), Singapore
- Brazil: Consumer P2P and PIX continue, but direct card payments to businesses discontinued January 15, 2026
- NOT available: US, EU, UK, or any other market
- India limits: Rs. 1 lakh per transaction, 20 transactions/day
- Brazil limits: R$1,000 per transaction, R$5,000/month

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~$100B+ estimated US ad revenue, primary market)
  Offer: Visa, Mastercard, Amex, PayPal, direct debit, monthly invoicing
  Missing: Venmo for ad billing, Cash App Pay, ACH for smaller accounts
  Why it matters: Strong coverage for US. Billing changes in April 2026 disrupted workflows for high spend advertisers who lost credit card rewards (2 to 3% cash back lost).

MARKET 2: Brazil (WhatsApp dominant market, large advertiser base)
  Offer: Boleto Bancario (manual), credit cards
  Missing: PIX (used by 150M+ Brazilians), local credit installments (parcelamento)
  Why it matters: PIX processes more transactions than cards in Brazil. Not accepting PIX for ad billing forces Brazilian SMBs to use international cards with high decline rates.

MARKET 3: India (WhatsApp's largest market, 500M+ users)
  Offer: Credit/debit cards, UPI, Paytm, Net Banking (manual accounts only)
  Missing: PhonePe, Google Pay India (UPI apps), RuPay card support unclear
  Why it matters: India has 350M+ UPI users. Manual payment setup required for local methods creates friction. Many Indian SMB advertisers face card decline issues.

MARKET 4: Japan (significant Meta and Instagram user base)
  Offer: Credit/debit cards
  Missing: PayPay (70M+ users), LINE Pay, Konbini, Rakuten Pay
  Why it matters: PayPay alone has 70M users. Japanese advertisers relying on international credit cards face higher decline rates than local payment rails.

MARKET 5: Southeast Asia (Indonesia, Philippines, Thailand, Vietnam)
  Offer: Credit/debit cards
  Missing: GrabPay, DANA, GCash, OVO, TrueMoney, Momo
  Why it matters: Credit card penetration below 10% in Indonesia and Philippines. Local wallets are the primary digital payment method. Advertiser acquisition is capped by card only billing.

**Payment Issues and Incidents:**
- 2025 Mass Payment Errors: Meta's anti fraud module update triggered widespread payment failures. Stricter BIN screening, 3DS enforcement, and geo/IP mismatch detection caused campaigns to pause without warning. Affiliate and advertiser communities reported "explosion of complaints"
- Cross Border Decline Pattern: Banks flag Meta's international charges. Advertisers outside US/EU using local cards face systematic declines. Non 3DS cards and prepaid/regional debit cards are frequently rejected
- April 2026 Billing Disruption: High spend accounts ($50K+/month) forced off credit cards to monthly invoicing or direct debit. Direct debit only available in US and SEPA. Advertisers in LATAM, APAC, Africa left with limited options
- Meta Quest Payment Issues: Users report "payment declined" errors when adding cards to Quest Store. Visa cards specifically flagged in community forums. No alternative payment path offered when primary card fails
- WhatsApp Pay Discontinuation (Brazil): Direct card payments to businesses discontinued January 15, 2026, reducing payment flexibility for WhatsApp Commerce in Meta's second largest WhatsApp market

**Key meeting angles:**
1. **Mass payment failures hit ad revenue directly** | Every declined advertiser payment pauses campaigns and reduces Meta's CPM inventory revenue. In 2025, Meta's own anti fraud update caused widespread billing failures. An orchestration layer with smart retry and failover could have prevented campaign pauses and protected revenue.
2. **Billing model transition creates friction** | April 2026's credit card removal affects high spend accounts globally. Advertisers in markets without direct debit (LATAM, APAC, Africa) face limited options. Yuno's 1,000+ APMs could offer local billing rails (PIX, UPI, GrabPay) as alternatives to international cards.
3. **Single processor risk at $200B scale** | With Adyen as the confirmed primary processor and no orchestration layer, Meta has no automatic failover when processing issues occur. At $200B+ annual revenue, even minutes of downtime equal millions in lost billing cycles.
4. **Quest Store conversion ceiling** | Only accepting Visa/MC/Amex/PayPal limits the Meta Quest Store in markets where local wallets dominate. Adding PayPay in Japan, GrabPay in SE Asia, and BLIK in Poland via one API could unlock incremental hardware and content revenue.
5. **WhatsApp Commerce payments regressing** | WhatsApp Pay only live in India and Singapore. Brazil card payments discontinued. Meta's commerce ambitions for WhatsApp Business are limited by payment infrastructure gaps. Yuno could power WhatsApp checkout across 50+ markets simultaneously.

**Meta Payments and Finance Leadership:**
- Mark Zuckerberg: CEO and Co Founder
- Susan Li: CFO (since 2022). Oversees all financial operations including billing infrastructure
- Stephane Kasriel: Head of Commerce and Financial Technologies. Previously CEO of Upwork. Leads Meta Pay, commerce, and financial services strategy
- Alex Himel: VP of Commerce. Oversees Facebook Marketplace and commerce product
- David Marcus: Former Head of Facebook Financial (Novi/Diem). Departed 2021. Founded Lightspark
- No dedicated external facing VP of Payments Processing identified

**Recent corporate developments:**
- March 2026: Stripe partnership announced for one click checkout in Facebook ads via Agentic Commerce Protocol
- February 2026: Meta began notifying advertisers of credit card payment removal effective April 1, 2026
- January 2026: WhatsApp discontinued direct card payments to businesses in Brazil
- December 2025: Q4 2025 revenue $59.89B (24% YoY growth), net income $22.8B
- 2025: Full year revenue $200.97B (22% YoY), 3.58B daily active people
- 2025: Meta paid nearly $3B to creators (up 35% from 2024)
- 2025: Meta's anti fraud billing module update caused mass advertiser payment failures
- FY2026 Guidance: Capex $115B to $135B, expenses $162B to $169B

**Sources:**
- [Meta FY2025 Q4 and Full Year Results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
- [Meta Revenue 2012 to 2025 (MacroTrends)](https://www.macrotrends.net/stocks/charts/META/meta-platforms/revenue)
- [Meta Q1 2026 Earnings Preview (IndexBox)](https://www.indexbox.io/blog/meta-platforms-q1-2026-earnings-preview-ai-investment-impact/)
- [Meta Ads Billing Changes 2026 (AdAmigo)](https://www.adamigo.ai/blog/meta-ads-billing-change-2026-credit-cards-removed-accounts-guide)
- [Meta Ads Billing Changes 2026 (Rockads)](https://blog.rockads.com/meta-ads-billing-changes-2026-the-complete-guide-to-credit-card-removal-payment-setup-and-what-advertisers-must-do/)
- [Meta Ads Billing Changes (Three Chapter Media)](https://www.threechaptermedia.com/blog/meta-ads-billing-changes-2026)
- [Meta Mass Payment Errors 2025 (Pay2.House)](https://pay2.house/blogs/article/meta-is-acting-up-again-mass-payment-errors-and-real-cases-from-2025?hl=en)
- [Facebook Ads Payment Failed 2026 (TwoOwls)](https://twoowls.io/blogs/facebook-ads-payment-failed/)
- [Meta Ads Payment Failure Guide (AGrowth)](https://agrowth.io/blogs/facebook-ads/facebook-ads-payment-failure)
- [Stripe Checkout for Facebook (Stripe Newsroom)](https://stripe.com/newsroom/news/checkout-for-facebook)
- [Stripe Facebook Agentic Payments (Payment Expert)](https://paymentexpert.com/2026/03/27/stripe-facebook-agentic-payments/)
- [Meta Pay Official Page](https://about.meta.com/technologies/meta-pay/)
- [Meta Quest Payment Settings](https://www.meta.com/help/quest/479408099980937/)
- [Meta Quest Add Payment Method](https://www.meta.com/help/quest/3615735275219825/)
- [WhatsApp Pay 2026 (Kanal)](https://getkanal.com/blog/whatsapp-pay-2026)
- [WhatsApp Payments Guide (YCloud)](https://www.ycloud.com/blog/whatsapp-pay)
- [WhatsApp Payments Countries (Infobip)](https://www.infobip.com/blog/whatsapp-payments)
- [Meta Ads Accepted Payment Options](https://www.facebook.com/business/help/212763688755026)
- [Meta Ads Manual Payment Methods](https://en-gb.facebook.com/business/help/311330675698510)
- [Meta India Payment Methods](https://www.facebook.com/business/help/1410784518969094)
- [Boleto for Meta Ads](https://www.facebook.com/business/help/260294844158119)
- [Meta Fix Failed Payment](https://www.facebook.com/business/help/268196136699959)
- [Meta Preventing Payment Failures](https://www.facebook.com/business/help/2726198024366416)
- [Adyen vs Braintree vs Stripe (Payments Dive)](https://www.paymentsdive.com/news/adyen-braintree-stripe-competition-digital-payments-merchants/691491/)
- [Adyen Deep Dive (Scuttleblurb)](https://www.scuttleblurb.com/adyen/)
- [Meta Subsidiaries (GreyB)](https://insights.greyb.com/meta-subsidiaries/)
- [Meta Subsidiaries SEC Filing](https://www.sec.gov/Archives/edgar/data/1326801/000132680125000017/meta-12312024x10kexhibit211.htm)
- [Meta Wikipedia](https://en.wikipedia.org/wiki/Meta_Platforms)
- [Meta Quest Visa Declined (Community Forums)](https://communityforums.atmeta.com/t5/Get-Help/Visa-payment-method-declined/td-p/1088576)
- [Meta Pay (Shopify)](https://www.shopify.com/blog/what-is-meta-pay)
- [Meta Revamps Ad Payment Policy (Payments Dive)](https://www.paymentsdive.com/news/meta-revamps-ad-payment-policy/814295/)
- [Meta Logo (CompaniesLogo)](https://companieslogo.com/facebook/logo/)
