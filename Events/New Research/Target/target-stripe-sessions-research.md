# TARGET | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Target
=======================================

Logo: https://corporate.target.com/media/collection/b-roll-and-press-materials/target-logos/target_bullseye-logo_red-jpg
Nombre merchant: Target

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Holiday Outage Exposure
Tittle_Pain Point_2: Intl Checkout Gaps
Tittle_Pain Point_3: Circle Card Lock-In
Tittle_Pain Point_4: Authorization Hold Fails
Tittle_Pain Point_5: Omnichannel Fragmentation

Desc_Pain Point_1: Dec 2025 outage hit POS, app, website, curbside, returns for 12+ hours at holiday peak. 4,000%+ spike in reports. Frozen registers, abandoned carts. No failover
Desc_Pain Point_2: Intl.Target.com ships to 200+ countries via Borderfree but accepts cards only. No Pix, iDEAL, or Bancontact. 60 currencies shown but no local payment methods.
Desc_Pain Point_3: Target Circle Card cannot be added to Apple Pay, Google Pay, or Samsung Pay. Customers use the Target app barcode instead, fragmenting loyalty checkout.
Desc_Pain Point_4: During Dec 2025 outage, shoppers got auth holds on cards for transactions that never completed. No automated release or cascade to alternative processor.
Desc_Pain Point_5: Target runs POS in 1,960+ stores, Target.com, app, Target+, curbside, Shipt. Each channel runs its own payment flow with no unified orchestration or fallback.

SLIDE 1: PSP TOPOLOGY

PSP_1: FIS Global (Target Circle Card management) PSP_2: Borderfree/Pitney Bowes (international checkout) PSP_3: PayPal (online + in-store via Google Pay) PSP_4: Affirm, Sezzle, Afterpay, Klarna, Zip (BNPL)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Bancontact (Belgium)
Local_M_5: Bizum (Spain)
Local_M_6: MBWay (Portugal)
Local_M_7: Konbini (Japan)
Local_M_8: GrabPay (SE Asia)
Local_M_9: DANA (Indonesia)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Omnichannel View

Desc_Yuno_Cap1: Route each of Target's transactions to the optimal acquirer by card BIN, issuer, and channel. With $104.8B in revenue and 20.6% from e-commerce, even 1% auth uplift recovers $1B+ in captured sales. Smart Routing delivers +3-10% authorization improvement across all channels.
Desc_Yuno_Cap2: Automatic cascade across processors when one goes down. The Dec 2025 outage (12+ hours, frozen registers) would have been mitigated by Yuno rerouting in ms. NOVA AI recovers 75% of soft declines. Livelo recovered 50% of failed transactions.
Desc_Yuno_Cap3: Expand Intl.Target.com beyond cards to 1,000+ local methods: iDEAL in Netherlands, Bancontact in Belgium, Pix in Brazil, Konbini in Japan, GrabPay in SE Asia. One API activates every local method across 200+ countries. InDrive deployed 10 markets via Yuno.
Desc_Yuno_Cap4: Unify payment visibility across 1,960+ stores, Target.com, Target app, Target+, curbside, and Shipt into one dashboard. Monitor approval rates per channel, detect outages before they spread, and optimize routing across all touchpoints.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Target at a glance:**
- NYSE: TGT. America's sixth-largest retailer
- FY2025 Revenue: $104.78B ($24.2B from Target.com e-commerce, 20.6% of total)
- 1,960+ stores across all 50 US states
- 415,000+ team members
- Headquarters: Minneapolis, Minnesota
- CEO: Michael Fiddelke (since Feb 2026; replaced Brian Cornell who became Executive Chairman)
- E-commerce: 3.1% online sales growth in FY2025 despite overall 1.68% revenue decline
- Target+ marketplace and Roundel ad network ($915M in advertising revenue, +41% YoY)
- Intl.Target.com: ships to 200+ countries via Borderfree (Pitney Bowes), prices in 60 currencies
- Target Circle loyalty program: rebranded from RedCard; 5% discount on all purchases
- BNPL: Affirm, Sezzle, PayPal Pay in 4, Afterpay, Klarna, Zip

**Confirmed PSPs / Payment Infrastructure:**
- FIS Global: manages Target Circle Card accounts (confirmed via tgtprelim.fisglobal.com domain)
- Borderfree (Pitney Bowes): international checkout and cross-border payments for Intl.Target.com
- PayPal: accepted online, in-app, and in-store via Google Pay/Samsung Pay contactless
- Apple Pay: accepted in-store and online at all Target locations
- Google Pay: accepted at registers and self-checkouts
- Samsung Pay: accepted at registers
- Affirm, Sezzle, Afterpay, Klarna, Zip: BNPL installment options
- Healthcare cards: HRA, FSA, HSA accepted
- Target Circle Card (credit, debit, Mastercard, reloadable): proprietary card program
- Primary merchant acquirer not publicly disclosed (likely one of Chase Payment Solutions, FIS/Worldpay, or Fiserv)

**Supported Payment Methods (as of 2026):**
- Credit/debit cards: Visa, Mastercard, American Express, Discover, JCB (max 2 card tenders per transaction)
- Target Circle Card (credit, debit, Mastercard, reloadable account)
- Digital wallets: Apple Pay, Google Pay, Samsung Pay (in-store); Apple Pay (online)
- PayPal (online, in-app, in-store via Google Pay)
- BNPL: Affirm, Sezzle, PayPal Pay in 4, Afterpay, Klarna, Zip
- Target GiftCards, eGiftCards, mobile GiftCards
- Healthcare cards (HRA, FSA, HSA)
- International: credit cards from foreign banks (via Borderfree)
- NOT accepted: Venmo (standalone), Cash App Pay, checks (online), cryptocurrency

**December 2025 Outage (Critical):**
- Date: December 19, 2025 (Friday before Christmas)
- Duration: 12+ hours, partial recovery by late afternoon, full digital restoration by Saturday Dec 20
- Scope: POS registers, Target app, Target.com, curbside pickup, returns, order fulfillment
- DownDetector reports spiked 4,000%+ in less than an hour starting ~6 AM ET
- Symptoms: checkout screens stuck on "connecting" or blacked out; app showed "technical difficulties" error; customers reported "authorization holds" on cards for transactions that never completed
- Impact: frozen registers, long lines, abandoned carts, heated exchanges at checkout, return processing halted
- Cause: not officially disclosed; experts suggested botched software update or cloud server failure
- No automated failover to alternative processors activated
- Estimated significant revenue loss during peak holiday week

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (1,960+ stores, $104.8B revenue)
  Offer: Visa, MC, Amex, Discover, JCB, Target Circle Card, Apple Pay, Google Pay, Samsung Pay, PayPal, Affirm, Sezzle, Afterpay, Klarna, Zip, FSA/HSA
  Missing: Venmo (standalone), Cash App Pay, Paze
  Why it matters: Strong domestic payment coverage. Main gap is failover resilience (Dec 2025 outage) rather than missing methods.

MARKET 2: International via Borderfree (200+ countries)
  Offer: Credit cards from foreign banks in 60 currencies
  Missing: ALL local payment methods. No Pix, no iDEAL, no Bancontact, no SEPA, no UPI, no Konbini, no GrabPay
  Why it matters: Intl.Target.com shows prices in 60 currencies but only accepts credit cards. International conversion is severely limited by cards-only checkout.

MARKET 3: Canada (Target's largest international market by traffic)
  Offer: Visa, MC, Amex credit cards via Borderfree
  Missing: Interac Online, PayPal Canada
  Why it matters: After closing 133 stores in 2015 ($2.1B loss), Target's only Canadian presence is online. Local payment methods would improve conversion for Canadian shoppers.

MARKET 4: Europe (key international e-commerce audience)
  Offer: Credit cards via Borderfree in EUR, GBP
  Missing: iDEAL (NL), Bancontact (BE), Bizum (ES), MBWay (PT), SEPA, Klarna (EU), Sofort
  Why it matters: European shoppers expect local payment methods. Cards-only checkout drives abandonment from customers accustomed to bank-based payments.

MARKET 5: Latin America (growing cross-border e-commerce)
  Offer: Credit cards via Borderfree
  Missing: Pix (Brazil), Boleto (Brazil), OXXO (Mexico), Mercado Pago, PSE (Colombia)
  Why it matters: LATAM cross-border e-commerce is growing rapidly. Credit card penetration in Brazil and Mexico is much lower than the US, making local methods essential.

**Key meeting angles:**
1. **December 2025 outage as catalyst**: The 12+ hour holiday outage exposed zero-failover architecture. Yuno's automatic cascade would have rerouted transactions in milliseconds, preventing the frozen registers, abandoned carts, and authorization hold issues.
2. **International checkout conversion**: Intl.Target.com supports 60 currencies but only credit cards. Adding Yuno's 1,000+ local APMs (iDEAL, Bancontact, Pix, Konbini) through one API integration dramatically improves international conversion without Borderfree replacement.
3. **Omnichannel unification**: 1,960+ stores, Target.com, Target app, Target+, curbside, and Shipt each run separate payment flows. Yuno provides a single orchestration layer with unified visibility and consistent failover across all channels.
4. **Target+ marketplace growth**: Target+ marketplace and Roundel ($915M ad revenue) are "outsized contributors" to 2026 growth. Marketplace sellers processing payments need the multi-PSP reliability that Yuno orchestration provides.
5. **Circle Card digital wallet gap**: Target Circle Card cannot be added to Apple Pay, Google Pay, or Samsung Pay. Yuno's checkout unification can bridge this gap, allowing Circle Card transactions to flow through the same optimized payment rails.
6. **New CEO, new payment strategy**: Michael Fiddelke (CEO since Feb 2026, former CFO) brings financial operations expertise. A payment orchestration pitch aligns with a finance-minded CEO focused on margin improvement and operational efficiency.

**Target Leadership:**
- Michael Fiddelke: CEO (since Feb 2026; 22-year Target veteran, former COO and CFO)
- Brian Cornell: Executive Chairman (former CEO 2014-2026; grew Target to $100B+ company)
- Rick Gomez: EVP, Chief Food, Essentials and Beauty Officer
- Christina Hennington: EVP, Chief Growth Officer
- Board: 12 directors including Brian Cornell as Executive Chairman

**Recent corporate developments:**
- Feb 2026: Michael Fiddelke becomes CEO; Brian Cornell transitions to Executive Chairman
- Dec 2025: Major system outage (12+ hours) during peak holiday week; POS, app, website all affected
- FY2025: $104.78B revenue (1.68% decline); e-commerce grew 3.1% to $24.2B
- FY2025: Roundel advertising revenue reached $915M (+41% YoY)
- 2025: Target Circle Card rebranded from RedCard
- 2025: BNPL expanded (Affirm, Sezzle, PayPal Pay in 4, Afterpay, Klarna, Zip)
- 2026 Outlook: ~2% net sales growth; comp sales slight increase; new stores and non-merchandise contributing 1+ ppt
- Ongoing: Intl.Target.com ships to 200+ countries via Borderfree; no physical international expansion planned

**Competitive Context:**
- Walmart: $674B revenue, stronger international presence (27 countries), accepts more digital wallets
- Amazon: $716B revenue, 23 marketplaces, blocks PayPal/Google Pay/Apple Pay
- Costco: $254B revenue, limited e-commerce payment options
- All major US retailers faced payment system challenges in 2025 (Target, Walmart, Amazon all had outages)

**Sources:**
- [Target Accepted Payment Options (Target Help)](https://help.target.com/help/subcategoryarticle?childcat=Accepted+payment+options&parentcat=Payment+Options)
- [Target Payment Types (Target Help)](https://help.target.com/help/TargetGuestHelpArticleDetail?articleId=ka95d000000gfjzAAA)
- [Target Payment Methods 2026 (Accio)](https://www.accio.com/blog/target-payment-methods-all-the-ways-you-can-pay)
- [Target Apple Pay Guide (JoinKudos)](https://www.joinkudos.com/blog/does-target-accept-apple-pay)
- [Target PayPal Acceptance (GOBankingRates)](https://www.gobankingrates.com/banking/technology/does-target-accept-paypal/)
- [Target FY2025 Earnings (Target Corporate)](https://corporate.target.com/press/release/2026/03/target-corporation-reports-fourth-quarter-and-full-year-2025-earnings)
- [Target Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/TGT/target/revenue)
- [Target Online Sales (Digital Commerce 360)](https://www.digitalcommerce360.com/article/target-online-sales/)
- [Target E-Commerce 2026 Turnaround (eMarketer)](https://www.emarketer.com/content/target-ecommerce-engine-powers-2026-turnaround)
- [Target December 2025 Outage (WebProNews)](https://www.webpronews.com/target-system-outage-disrupts-holiday-shopping-erodes-customer-trust/)
- [Target December Outage (NBC Chicago)](https://www.nbcchicago.com/news/local/having-issues-with-your-target-order-what-shoppers-should-do-amid-global-outage/3866153/)
- [Target December Outage (FOX 2)](https://fox2now.com/news/national/is-target-com-down-customers-workers-report-issues-with-online-systems/)
- [Target Outage Bloomberg (Bloomberg)](https://www.bloomberg.com/news/articles/2025-12-20/target-says-digital-operations-restored-after-technology-outage)
- [Target Goes Global via Borderfree (Pitney Bowes)](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/target-goes-global-targetcom-now-shoppable-worldwide)
- [Target International Expansion (StartTribune)](https://www.startribune.com/target-tests-international-expansion-through-online-portals/336408791)
- [Target CEO Transition (CNN)](https://www.cnn.com/2025/08/20/business/target-stock-ceo-cornell)
- [Michael Fiddelke CEO (Retail Dive)](https://www.retaildive.com/news/target-ceo-brian-cornell-departure-michael-fiddelke/758105/)
- [Brian Cornell Legacy (Axios)](https://www.axios.com/local/twin-cities/2026/01/30/brian-cornell-tenure-ceo-success-failures)
- [Target Circle Card (Target Help)](https://help.target.com/help/TargetGuestHelpArticleDetail?articleId=ka9Kd000000PFfYIAW)
- [Target Corporate Logos (Target Corporate)](https://corporate.target.com/media/collection/b-roll-and-press-materials/target-logos)
- [Target Corporation Wikipedia](https://en.wikipedia.org/wiki/Target_Corporation)
