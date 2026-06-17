# Royal Caribbean | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Royal Caribbean
=======================================

Logo: https://images.seeklogo.com/logo-png/55/1/royal-caribbean-logo-png_seeklogo-555254.png
Nombre merchant: Royal Caribbean

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: High-Value Txn Fraud Filters
Tittle_Pain Point_2: Zero Int'l Payment Methods
Tittle_Pain Point_3: Checkout Connection Errors
Tittle_Pain Point_4: Onboard Billing Disputes
Tittle_Pain Point_5: Multi-Brand PSP Complexity

Desc_Pain Point_1: Cruise bookings are high-value transactions ($2K to $15K+) that trigger aggressive bank fraud scoring. Royal Caribbean's system assigns risk scores based on transaction value, location mismatches, repeated attempts, and verification errors. Even genuine travelers with valid cards get declined. Immediate retries worsen the problem. The recommendation to "wait 20 to 30 minutes before retrying" signals systemic false-positive friction on the highest-revenue transactions.
Desc_Pain Point_2: Royal Caribbean operates in 45+ markets with localized websites (US, UK, Australia, Singapore, China, Brazil, Germany, and more). Yet checkout accepts only Visa, Mastercard, Amex, Discover, and Diners Club. No Alipay or WeChat Pay for Chinese guests (China is the #2 market), no Pix for Brazilians, no iDEAL for Dutch, no Klarna for Europeans. For a company generating 45% of revenue from international markets, the local method gap is massive.
Desc_Pain Point_3: Cruise Critic and Royal Caribbean Blog forums document recurring "CONNECTION ERROR: There Was An Error Processing Your Payment, Please Try Again Later" messages. Users report the error persists across multiple browsers, devices, and cards. Payment pages fail to load, timeout, or loop. High-value cruise bookings lost to checkout friction cannot easily be recovered, as travelers often turn to travel agents who add commissions.
Desc_Pain Point_4: Cruise Critic and Royal Caribbean Blog document debit cards charged daily with pending holds, then re-charged for the full onboard total at disembarkation. Guests report unauthorized purchases (drink packages charged without consent), double-charge incidents, and difficulty obtaining itemized billing. Post-cruise dispute resolution requires multiple emails and phone calls over weeks. These billing inconsistencies inflate chargeback costs.
Desc_Pain Point_5: Royal Caribbean Group operates three distinct cruise brands (Royal Caribbean International, Celebrity Cruises, Silversea) plus joint ventures (TUI Cruises, Hapag-Lloyd Cruises). Each brand and market requires payment processing across multiple currencies and regulations. The SeaPass onboard system adds another payment layer. No public orchestration layer unifies these flows, creating duplicated integration overhead and inconsistent checkout experiences across brands.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card acquiring (primary gateway unconfirmed)
PSP_2: Affirm (BNPL)
PSP_3: Klarna (BNPL, US)
PSP_4: SeaPass (proprietary onboard payment system)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: Pix
Local_M_4: iDEAL
Local_M_5: Bancontact
Local_M_6: Sofort/Giropay
Local_M_7: Mercado Pago
Local_M_8: KakaoPay
Local_M_9: GrabPay
Local_M_10: PayPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & NOVA AI Recovery
Tittle_Yuno_Cap3: Global Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple acquirers based on card BIN, issuer country, and historical approval performance. With $16.5B in annual revenue and high-value cruise bookings ($2K to $15K+), even a 2% auth uplift from intelligent routing translates to hundreds of millions in recovered bookings. InDrive achieved 90% approval rates across 10 markets. Wingo Airlines saw +14% authorization improvement with this same technology.
Desc_Yuno_Cap2: Automatic cascade eliminates the "Connection Error" dead ends plaguing Royal Caribbean's checkout. When a UK traveler's Barclays card gets declined by the primary acquirer, Yuno reroutes to a UK-optimized processor in milliseconds. 50% recovery on soft declines via standard failover. NOVA AI pushes recovery to 75% on hard declines, proven at Viva Aerobus. No more "wait 20 to 30 minutes before retrying."
Desc_Yuno_Cap3: Activates the local methods Royal Caribbean's global guests demand: Alipay and WeChat Pay (China, #2 market, 1.5B+ combined users), Pix (Brazil, 170M+ users), iDEAL (Netherlands), Sofort (Germany), KakaoPay (Korea), GrabPay (Singapore), PayPay (Japan). One API, 1,000+ payment methods, 300+ processors, 200+ countries. Each method goes live without a dedicated integration project per brand.
Desc_Yuno_Cap4: One orchestration layer unifying Royal Caribbean International + Celebrity Cruises + Silversea across all markets. Real-time approval rate monitoring, centralized reconciliation across multiple currencies and brands, millisecond anomaly detection. Eliminates duplicated PSP management overhead across three brands and five joint ventures. Single integration powers both web booking and potential SeaPass onboard modernization.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Royal Caribbean Group at a glance:**
- World's second-largest cruise company. Three brands: Royal Caribbean International, Celebrity Cruises, Silversea
- Revenue: $16.5B (FY2024, +18.6% YoY). Net income: $2.9B (+70% YoY). Adjusted EBITDA: $6.0B
- Profit margin improved to 18% from 12% in FY2023
- Adjusted net income: $3.2B ($11.80 per diluted share)
- Fleet of 66 to 69 ships traveling to nearly 1,000 destinations
- Total guest count increased 45% since 2019. Millennial and younger guests nearly doubled
- Headquarters: Miami, Florida (1080 Caribbean Way). Incorporated in Liberia. ~41,000 employees across 6 continents
- Ticker: NYSE: RCL
- CEO & Chairman: Jason Liberty (since January 2022, nearly two decades at company)
- CFO: Naftali Holtz (since 2019, previously MD and Head of Lodging & Leisure at Goldman Sachs)
- CIO: Martha Poulter (SVP & CIO since December 2017, previously CIO at Starwood Hotels and GE Capital. 2021 Miami CIO of the Year ORBIE Award)
- SVP Data Analytics & AI: Matthew Denesuk
- Joint ventures: TUI Cruises, Hapag-Lloyd Cruises. Previously held stake in Silversea (now fully owned)
- February 2024: broke ground on new headquarters campus in Miami
- International expansion: China grew from 45th to 2nd largest market. Singapore hub with Quantum of the Seas. Australia/South Pacific expansion with Royal Beach Club Lelepa. China and Singapore sailings for 2027-28 season
- ~55% revenue from US, ~45% from international markets (UK, Australia, Singapore, China, Brazil, Germany, etc.)
- 2025 guidance issued with launch of River Vacations brand
- AI-driven personalization and loyalty program innovations across all three brands

**Confirmed PSPs and payment partners:**
- Card acquiring: primary payment gateway not publicly disclosed. Accepts Visa, Mastercard, American Express, Discover, Diners Club International. Visa and Mastercard debit cards also accepted
- Affirm: BNPL option for cruise financing (pay over time with fixed monthly payments)
- Klarna: BNPL option (buy now, pay in 4 installments)
- Sezzle: BNPL option (split into 4 interest-free installments over 6 weeks)
- SeaPass: proprietary onboard cashless payment system linked to guest's credit/debit card. All onboard charges in USD
- Royal Caribbean Gift Cards: accepted for booking payments
- UATP: accepted for corporate/travel agency bookings

**Payment methods currently confirmed:**
- Cards: Visa, Mastercard, American Express, Discover, Diners Club International, Visa/MC debit
- BNPL: Affirm, Klarna, Sezzle
- Other: Royal Caribbean Gift Cards, UATP (corporate), SeaPass (onboard)
- Notably absent: any digital wallets, bank transfers, or local payment methods

**Top 5 International Markets Gap Analysis:**

MARKET 1: China (#2 market globally, grew from 45th largest)
  Currently offer: Visa/MC/Amex (cards only)
  Missing: Alipay (1B+ users), WeChat Pay (900M+ users), UnionPay QR
  Note: China is Royal Caribbean's second-largest market. Spectrum of the Seas operates dedicated China sailings. Chinese travelers overwhelmingly prefer Alipay and WeChat Pay. Without them, direct bookings are lost to Ctrip/Trip.com.

MARKET 2: United Kingdom (major European source market)
  Currently offer: Visa/MC/Amex/Discover/Diners
  Missing: Open Banking (Pay by Bank), Klarna (exists for US only), PayPal checkout
  Note: UK travelers represent a significant share of Royal Caribbean's European bookings. Open Banking adoption is accelerating in the UK with 10M+ active users.

MARKET 3: Australia/New Zealand (expanding with Royal Beach Club)
  Currently offer: Visa/MC/Amex
  Missing: POLi (bank transfer), Afterpay/Zip (local BNPL), BPAY
  Note: Royal Caribbean is investing in Australia/South Pacific with Royal Beach Club Lelepa. Australian travelers expect local payment options. Afterpay has 3.6M+ active Australian users.

MARKET 4: Germany (TUI Cruises joint venture market)
  Currently offer: Visa/MC/Amex
  Missing: Sofort/Giropay, PayPal (checkout), Klarna, SEPA Direct Debit
  Note: Germany is Europe's largest cruise market. German consumers strongly prefer bank transfer-based payment methods over credit cards. Credit card penetration in Germany is under 40%.

MARKET 5: Brazil/Latin America (growing source market)
  Currently offer: Visa/MC/Amex
  Missing: Pix (170M+ users), Boleto Bancario, Mercado Pago, installment payments (parcelamento)
  Note: Brazil is a fast-growing cruise market. Pix dominates digital payments. Credit card penetration under 35%. Local installment payments (parcelamento) are expected for high-value purchases.

**Pain point evidence (sourced):**

1. High-Value Transaction Fraud Filtering: Daily Cruise Info documents that Royal Caribbean's automated fraud scoring systems assign risk scores based on transaction value, location mismatches, repeated attempts, and verification errors. Cruise payments ($2K to $15K+) are "automatically placed in a higher fraud-risk category." Even genuine travelers get declined. Recommendation: "wait at least 20 to 30 minutes before retrying." Source: dailycruiseinfo.com/royal-caribbean-fraud-checks-why-payments-get-declined/

2. Checkout Connection Errors: Cruise Critic forum and Royal Caribbean Blog document recurring "CONNECTION ERROR: There Was An Error Processing Your Payment, Please Try Again Later" messages. Users report persistence across multiple browsers, devices, and cards. Payment pages fail to load or timeout. Source: boards.cruisecritic.com/topic/2778295-payment-page-not-working/, royalcaribbeanblog.com/boards/index.php?/topic/30574-payment-error/

3. Online Payment Processing Issues: Cruise Critic thread documents users unable to make payments on existing bookings, with the payment page not loading or returning errors. Multiple users confirm the issue is not browser or card-specific, suggesting server-side payment processing problems. Source: boards.cruisecritic.com/topic/2487546-issues-with-payments-online, boards.cruisecritic.com/topic/2761527-payment-issues/

4. Double-Charge and Onboard Billing: Cruise Critic forums document debit cards charged daily with pending holds plus a final full-amount charge, creating apparent double-billing. Guests report unauthorized charges (family members purchasing without consent), difficulty obtaining itemized bills, and extended post-cruise dispute resolution. One user documented being "charged twice for the cruise" in August 2024. Source: boards.cruisecritic.com/topic/2684889-debit-card-charged-twice/, justanswer.com (August 2024 double charge), royalcaribbeanblog.com/boards/index.php?/topic/30926

5. Cross-Border Payment Friction: Royal Caribbean operates localized websites for 15+ countries, but payment acceptance is uniform (cards only) regardless of market. Chinese guests (Royal Caribbean's #2 market) cannot pay with Alipay or WeChat Pay. Brazilian guests cannot use Pix. German guests cannot use Sofort. Many banks require customers to "enable international online payments" before attempting a cruise booking, adding pre-purchase friction. Source: royalcaribbean.com/resources/select-location, dailycruiseinfo.com

**Key meeting angles:**

1. **$16.5B revenue, high-value transactions** | Cruise bookings are $2K to $15K+ per transaction, making each lost booking expensive. With $16.5B revenue and 45% from international markets, even a 2% auth uplift from Smart Routing represents hundreds of millions in recovered bookings. These are not $50 widget sales: every declined cruise is a catastrophic revenue loss.

2. **China is market #2, zero local payments** | China grew from Royal Caribbean's 45th to 2nd largest market. Spectrum of the Seas runs dedicated China sailings. Yet Chinese guests cannot pay with Alipay (1B+ users) or WeChat Pay (900M+ users) on royalcaribbean.com. Yuno activates both through a single API alongside 1,000+ methods.

3. **Eliminate "Connection Error" dead ends** | Forums document years of checkout failures across browsers and devices. Yuno's failover routing ensures that when one processor fails, the transaction cascades to a backup acquirer in milliseconds. No more "wait 20 to 30 minutes."

4. **Multi-brand orchestration** | Royal Caribbean International + Celebrity Cruises + Silversea, each with its own checkout. One Yuno integration layer powers all three brands across all markets, eliminating duplicated PSP management and ensuring consistent payment experiences.

5. **CIO Martha Poulter is the buyer** | Poulter (former CIO at Starwood Hotels and GE Capital) focuses on data analytics, predictive capabilities, and differentiated guest experiences. Payment orchestration with real-time analytics and AI-driven recovery fits directly into her strategic agenda. 2021 CIO of the Year ORBIE Award winner.

6. **BNPL is already adopted** | Royal Caribbean already works with Affirm, Klarna, and Sezzle. This proves willingness to add alternative payment methods. Yuno extends this beyond BNPL to local payment methods in every market: Pix, Alipay, iDEAL, Sofort, and hundreds more.

7. **Airline-proven, travel-tested** | Wingo Airlines (+14% auth improvement), Viva Aerobus (75% hard-decline recovery with NOVA AI). Both are high-value travel purchases in the same category as cruise bookings. Yuno already powers payment orchestration for the travel and leisure vertical.

**Sources:**
- [Royal Caribbean Payment FAQ](https://www.royalcaribbean.com/faq/questions/how-can-i-make-a-payment)
- [Royal Caribbean SeaPass Onboard Payments](https://www.royalcaribbean.com/faq/questions/seapass-onboard-spending-account)
- [Royal Caribbean Vacation Financing](https://www.royalcaribbean.com/programs/financing)
- [Royal Caribbean FY2024 Results Press Release](https://www.prnewswire.com/news-releases/royal-caribbean-group-reports-2024-results-issues-2025-guidance-and-announces-launch-of-river-vacations-302361851.html)
- [Royal Caribbean FY2024 Results (Cruise Industry News)](https://cruiseindustrynews.com/cruise-news/2025/01/royal-caribbean-reports-2024-q4-and-full-year-results/)
- [Royal Caribbean Annual Report 2024](https://www.annualreports.com/HostedData/AnnualReports/PDF/NYSE_RCL_2024.pdf)
- [Jason Liberty CEO Bio](https://www.royalcaribbean.com/about-us/jason-liberty)
- [Royal Caribbean Inside Bold Plan (Skift)](https://skift.com/2025/08/18/royal-caribbean-ceo-ai-innovation-cruises/)
- [Naftali Holtz CFO Bio](https://www.royalcaribbeanpresscenter.com/executive-bio/31/naftali-holtz/)
- [Martha Poulter CIO (Metis Strategy Interview)](https://www.metisstrategy.com/interview/martha-poulter-2/)
- [Martha Poulter CIO Appointment](https://www.rclinvestor.com/press-release/martha-poulter-named-senior-vice-president-chief-information-officer-for-royal-caribbean-cruises-ltd/)
- [Daily Cruise Info: Royal Caribbean Fraud Checks](https://www.dailycruiseinfo.com/royal-caribbean-fraud-checks-why-payments-get-declined/)
- [Cruise Critic: Payment Page Not Working](https://boards.cruisecritic.com/topic/2778295-payment-page-not-working/)
- [Cruise Critic: Issues With Payments Online](https://boards.cruisecritic.com/topic/2487546-issues-with-payments-online)
- [Cruise Critic: Debit Card Charged Twice](https://boards.cruisecritic.com/topic/2684889-debit-card-charged-twice/)
- [Royal Caribbean Blog: Payment Error Thread](https://www.royalcaribbeanblog.com/boards/index.php?/topic/30574-payment-error/)
- [Royal Caribbean Blog: Overcharged Without Consent](https://www.royalcaribbeanblog.com/boards/index.php?/topic/30926-mad-at-royal-caribbean-charged-without-consent-and-overcharged/)
- [Royal Caribbean Emerging Markets (Kenan-Flagler)](https://www.kenan-flagler.unc.edu/news/how-royal-caribbean-charted-a-new-course-in-emerging-markets/)
- [Royal Caribbean Country Selector](https://www.royalcaribbean.com/resources/select-location)
- [Royal Caribbean New HQ Groundbreaking (HOK)](https://www.hok.com/news/2024-02/royal-caribbean-breaks-ground-on-new-headquarters/)
- [Klarna at Royal Caribbean](https://www.klarna.com/us/store/220d1f6c-2c76-4848-a59a-18615258d8fe/Royal-Caribbean-International/pay-with-klarna/)
- [Sezzle at Royal Caribbean](https://sezzle.com/shop/royal-caribbean/)
- [Royal Caribbean Logo (Seeklogo)](https://seeklogo.com/vector-logo/555254/royal-caribbean)
