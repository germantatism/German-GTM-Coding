# MARRIOTT INTERNATIONAL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Marriott International
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/MAR_BIG-385de746.png
Nombre merchant: Marriott International

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Stack
Tittle_Pain Point_2: Data Breach Fallout
Tittle_Pain Point_3: APM Blind Spots
Tittle_Pain Point_4: Reconciliation Drain
Tittle_Pain Point_5: DCC & FX Complaints

Desc_Pain Point_1: FreedomPay (US/Canada), Planet (150+ EMEA hotels), Shift4 (via Oracle OPI), and Sertifi (global authorizations) each operate on separate dashboards with siloed settlement streams. No unified orchestration layer connects these processors, forcing property level payment handling with minimal economies of scale across 9,300+ hotels.
Desc_Pain Point_2: Three breaches (2014 to 2020) exposed 344M+ guest records including payment card numbers. FTC finalized a consent order in Dec 2024 mandating a robust security program. Marriott paid $52M in state settlements. Chargeback spikes of up to 5% followed each breach, adding millions in recovery costs on top of reputational damage.
Desc_Pain Point_3: Marriott.com accepts only major international credit cards for direct bookings, while OTAs offer 40+ local methods. Missing key APMs in top growth markets: no WeChat Pay broadly, no PIX (Brazil), no UPI (India), no BLIK (Poland), no iDEAL (Netherlands). 74% of travelers abandon bookings without their preferred payment method.
Desc_Pain Point_4: Hotels lose $1.5B+ industry wide annually to inefficient reconciliation. 27% of hotel operators rely on 7+ tech platforms with 11+ hours weekly consolidating data. Marriott properties manually reconcile across PMS, CRS, POS, loyalty, and multiple payment processors. Planet case study confirmed staff re entered card data manually before integration.
Desc_Pain Point_5: Guests report being charged 5% to 15% above quoted USD rates when local currency conversion applies at checkout. FlyerTalk and LoyaltyLobby document systematic DCC markups at Marriott properties globally. Cross border FX fees of 0.5% to 3% compound the problem for international travelers booking direct.

SLIDE 1: PSP TOPOLOGY

PSP_1: FreedomPay
PSP_2: Planet
PSP_3: Shift4
PSP_4: Sertifi (Flywire)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX
Local_M_2: WeChat Pay
Local_M_3: UPI
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Boleto Bancario
Local_M_7: PromptPay
Local_M_8: KakaoPay
Local_M_9: Naver Pay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA AI Recovery
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route every transaction across FreedomPay, Planet, Shift4, and additional acquirers based on card BIN, issuer country, currency, and real time performance data. With $26.2B in annual revenue across 144 countries, even a 2% auth rate uplift from intelligent routing recovers hundreds of millions in bookings. InDrive achieved 90% approval rates across 10 markets using this approach.
Desc_Yuno_Cap2: Automatic cascade eliminates single processor dependency. When FreedomPay declines an international traveler's card, Yuno reroutes to a local acquirer in milliseconds. Standard failover recovers up to 50% of soft declines. NOVA AI pushes recovery to 75% on hard declines, matching Viva Aerobus results. Zero guest friction, zero abandoned reservations.
Desc_Yuno_Cap3: Activate every missing APM Marriott needs across its 144 country footprint: PIX and Boleto (Brazil), UPI (India), WeChat Pay and Alipay (China), iDEAL (Netherlands), BLIK (Poland), PromptPay (Thailand), KakaoPay and Naver Pay (South Korea), GrabPay (SEA). One API, 300+ processors, 200+ countries. No multi month engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing the fragmented FreedomPay + Planet + Shift4 + Sertifi patchwork. Real time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection. Eliminates manual card re entry documented in Planet case study and the 11+ hours weekly operators spend consolidating payment data.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Marriott International at a glance:**
- NYSE: MAR. Headquarters: Bethesda, Maryland, USA
- Full Year 2025 Revenue: $26.186B (+4.33% YoY). Full Year 2024 Revenue: $25.1B (+5.8% YoY)
- 9,361 properties with 1,706,331 rooms across 144 countries and territories (year end 2024)
- Development pipeline: ~3,800 hotels with 577,000+ rooms
- 30+ hotel brands including Marriott, Ritz Carlton, W Hotels, Sheraton, Westin, St. Regis, Courtyard, Fairfield
- Marriott Bonvoy loyalty program: 200M+ members globally
- Full Year 2025 worldwide RevPAR: +2.0% (US/Canada: +0.7%, International: +5.1%)
- Greater China: 10% of existing rooms, 18% of pipeline
- 55% of pipeline rooms are in international markets
- CEO: Anthony Capuano (since 2021)
- CFO: Kathleen Oberg, EVP Development
- Chief Revenue & Technology Officer: Drew Pinto, EVP (leads global sales, revenue management, digital, and IT strategy; portfolio encompasses $35B+ in revenue channels and 67M annual customer contacts)
- Group President, US/Canada/CALA: Satya Anand (effective March 2026)
- President, EMEA: Neal Jones (effective March 2026)

**Segments (Geographic):**
- US & Canada: largest segment, RevPAR +0.7% FY2025
- EMEA (Europe, Middle East & Africa): strong leisure demand
- Greater China: 10% of rooms, 18% of pipeline, key growth market
- APEC (Asia Pacific ex China): international RevPAR leader
- CALA (Caribbean & Latin America): included in unallocated corporate

**Website traffic (marriott.com):**
- ~50.4M monthly visitors (May 2025, SimilarWeb)
- Traffic growth: +7.65% month over month
- Top traffic source: Direct (46.72% desktop), Organic Search (25.21%)
- Top country: United States (dominant)
- Audience: 45% male, 55% female; largest age group 25 to 34
- Competitors: hilton.com, ihg.com, booking.com

**Confirmed PSPs and payment partners:**

1. FreedomPay: Enterprise agreement announced November 2019. Adopted across Marriott's US and Canada lodging portfolio. FreedomPay integrates with 100+ payment processors and acquirers, linking payment data with loyalty systems and marketing platforms. FreedomPay is the global leader in hospitality, serving 70%+ of top North American hotels.
   Source: [FreedomPay Press Release](https://www.prnewswire.com/news-releases/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation-300954692.html) | [Marriott News Center](https://news.marriott.com/news/2019/11/19/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation)

2. Planet (formerly Planet Payment): Provides integrated payments to 150+ Marriott hotels across EMEA, including Arabella properties. Deployed alongside Oracle Opera PMS. Automated end of day settlement, tokenization, pre authorization for no shows. Case study documents that before Planet, receptionists manually re entered card details into PMS and card machines separately.
   Source: [Planet Case Study](https://www.weareplanet.com/we-helped-marriott-hotels-overcome-their-payment-processing-challenges) | [Planet Payment](https://www.planetpayment.com/en/about-us/knowledge-hub/case-studies/marriott/)

3. Shift4: Integrated via Oracle Payment Interface (OPI) with OPERA PMS. Provides EMV, tokenization, PCI validated P2PE. Oracle Platinum Partner with certification for OPERA, Simphony, RES 3700, and e7 POS systems.
   Source: [Shift4 Press Release](https://www.shift4.com/news/shift4-payments-adds-emv-to-certification-with-oracles-opera-property-management-system)

4. Sertifi (by Flywire): Exclusive provider for digital authorizations to ALL Marriotts globally. PCI Level 1, SOC 1 Type 2, SOC 2 Type 2 compliant. Integrates with OPERA Cloud and OPERA On Prem. Includes fraud detection tools that automatically verify cards upon submission.
   Source: [Sertifi: Marriott Customer Story](https://corp.sertifi.com/marriott/)

5. Oracle Hospitality OPERA Cloud PMS: Core property management system. Marriott selected OPERA Cloud for global rollout. Oracle Payment Interface connects to 80+ payment processors worldwide.
   Source: [Oracle PR](https://www.prnewswire.com/news-releases/oracle-cloud-to-help-elevate-property-management-for-marriott-international-302047269.html)

6. Toast: Partnership for restaurant payment technology in select service hotels (Courtyard, SpringHill Suites) across US and Canada.
   Source: [Hotel Dive](https://www.hoteldive.com/news/toast-for-hotel-restaurants-marriott-partnership/652951/)

7. Alipay: Accepted at select Marriott properties in mainland China, Hong Kong, Macau, Thailand, Singapore, Japan, and South Korea. 1,500 hotels enabled as of 2018.
   Source: [NFCW](https://www.nfcw.com/2015/09/09/337651/marriott-hotels-to-accept-alipay/) | [SCMP](https://www.scmp.com/business/companies/article/2142159/instant-noodles-alipay-how-marriott-hotels-are-luring-chinese)

8. Apple Pay: Marriott was the first global hospitality company to offer Apple Pay. Supported at front desk and via Bonvoy app.
   Source: [Retail Dive](https://www.retaildive.com/ex/mobilecommercedaily/marriott-international-checks-in-apple-pay-for-extended-stay) | [SoLoyal](https://www.soloyal.co/blog/deep-dives/how-to-use-google-and-apple-pay-at-marriott-bonvoy)

**Payment orchestrator status:**
No payment orchestration platform confirmed. No evidence of Spreedly, Primer, Gr4vy, CellPoint Digital, BR DGE, or any third party orchestration layer. Marriott operates through property level payment processing with multiple regional processors (FreedomPay in NA, Planet in EMEA, Shift4 via Oracle OPI). This creates the classic "no unified routing, no failover, no centralized analytics" gap that Yuno directly addresses.

**Digital transformation context:**
Drew Pinto is overseeing a major technology transformation replacing three core systems: PMS (Oracle OPERA Cloud), CRS (central reservation system), and loyalty platform. The Marriott Bonvoy Wallet launched globally, combining awards, payments, and gift cards. Marriott has a generative AI incubator for proofs of concept. This transformation window creates an ideal entry point for payment orchestration.

**Data breach and security history:**
- Breach 1 (2014): Starwood POS malware exposed 40,000+ payment cards
- Breach 2 (2014 to 2018): Starwood reservation database compromised, 339M guest records exposed including encrypted payment card numbers and passport data. Went undetected for 4 years
- Breach 3 (March 2020): 5.2M guest account details exposed
- October 2024: FTC took formal action against Marriott/Starwood
- December 2024: FTC finalized consent order mandating comprehensive information security program
- $52M settlement with 49 US states + DC
- $3.5M Texas AG settlement
- Ongoing litigation: Maldini v. Marriott (4th Circuit, 2025)
   Source: [FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2024/10/ftc-takes-action-against-marriott-starwood-over-multiple-data-breaches) | [Huntress](https://www.huntress.com/threat-library/data-breach/marriott-data-breach) | [Cybersecurity Dive](https://www.cybersecuritydive.com/news/ftc-settles-marriott-starwood-data-breaches/729464/)

**Top Market Gap Analysis:**

MARKET 1: United States (dominant market, 45%+ of properties)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay (contactless at properties), FreedomPay processing
  Missing for online direct: Limited APM options vs OTAs. No PayPal on marriott.com, no Affirm/Klarna BNPL for hotel bookings
  Note: OTAs like Booking.com and Expedia offer 40+ payment methods. Marriott.com checkout accepts only major credit cards, pushing price sensitive travelers to OTA channels where Marriott pays 15 to 25% commission.

MARKET 2: Greater China (10% of rooms, 18% of pipeline, critical growth)
  Currently offer: Alipay at select properties (1,500 hotels as of 2018), UnionPay cards
  Missing: WeChat Pay (broadly), Alipay+ (cross border), local bank cards for online booking
  Note: WeChat Pay has 900M+ users. Alipay adoption appears limited to in property payments, not integrated into the online booking checkout on marriott.com. Chinese travelers booking online face credit card only checkout.

MARKET 3: India (APEC growth market)
  Currently offer: Major credit cards only for online booking
  Missing: UPI (57% of all Indian transactions), Paytm, PhonePe, Netbanking
  Note: Credit card penetration in India is under 5%. UPI processes 3,700+ transactions per second. Without UPI, the vast majority of Indian travelers cannot book direct on marriott.com.

MARKET 4: Europe (EMEA segment, strong leisure demand)
  Currently offer: Major credit cards, Planet processing at 150+ EMEA hotels
  Missing: iDEAL (Netherlands, 60% of online transactions), BLIK (Poland, dominant digital payment), Bancontact (Belgium), MB Way (Portugal), Bizum (Spain), Swish (Sweden)
  Note: European travelers increasingly expect local payment methods at checkout. Each missing APM drives bookings to OTAs that support them.

MARKET 5: Latin America (CALA, emerging market)
  Currently offer: Major credit cards
  Missing: PIX (Brazil, used by 76% of population), Boleto Bancario, OXXO (Mexico), PSE (Colombia), Mercado Pago
  Note: PIX processed $1.2T in transactions in 2024. Brazil and Mexico are key Marriott growth markets. Without PIX and OXXO, direct booking conversion is severely limited.

**Hotel industry payment pain points (sourced data):**

1. Property Level Processing: "The hotel industry handles almost all payment processing on property, meaning that it gets few efficiencies of scale." Hotels operate "roughly 20 years behind e commerce, retail, and other industries in payment technology." Source: [Hospitality Upgrade](https://www.hospitalityupgrade.com/techtalk/definitely-doug-4-19-24-why-hotel-payments-are-broken-and-costly-and-how-to-fix-them)

2. Reconciliation Costs: Hotels lose $1.5B+ annually to inefficient reconciliation. 27% of operators use 7+ tech platforms with 11+ hours weekly consolidating data. 91% rely on manual reporting within automated systems. Source: [Payrails Hospitality Report](https://www.payrails.com/blog/hospitality-payment-report) | [Hotel Operations Index 2026](https://www.hotel-online.com/index.php/news/the-2026-hotel-operations-index-progress-pressure-and-the-path-forward)

3. Booking Abandonment: 74% of travelers abandon bookings without their preferred payment method. 91% of guests want prices in their home currency. Source: [Payrails](https://www.payrails.com/blog/hospitality-payment-report)

4. Fraud Costs: 5 to 6% of hospitality revenue lost to fraud annually. 30%+ year over year increase in chargebacks. Card not present fraud accounts for 65% of fraud losses. Source: [Payrails](https://www.payrails.com/blog/hospitality-payment-report)

5. Processing Costs: Hotels spend $21B annually on payment processing. Average card processing fees of 2 to 3%. Hotels can save 0.8% to 2% of total room revenue through better payment practices. Source: [Payrails](https://www.payrails.com/blog/hospitality-payment-report) | [Hospitality Upgrade](https://www.hospitalityupgrade.com/techtalk/definitely-doug-4-19-24-why-hotel-payments-are-broken-and-costly-and-how-to-fix-them)

**Key meeting angles:**

1. **Technology transformation window** | Drew Pinto is replacing all three core systems (PMS, CRS, loyalty). Adding payment orchestration during this transformation is a natural extension, not a separate project. Yuno slots into the new Oracle OPERA Cloud stack via API without disrupting the ongoing migration.

2. **Direct booking revenue recovery** | Every booking lost to OTAs because marriott.com lacks local payment methods costs Marriott 15 to 25% in commission. Adding PIX, UPI, WeChat Pay, iDEAL, BLIK, and 1,000+ other methods through Yuno's single API drives direct booking conversion and eliminates OTA commission leakage.

3. **Post breach security upgrade** | The FTC consent order mandates robust security improvements. Yuno provides PCI Level 1 tokenization, network level fraud scoring, and 3DS orchestration. This directly supports Marriott's regulatory compliance obligations while reducing the 5 to 6% revenue loss from hospitality fraud.

4. **Unified orchestration across regions** | Replace the FreedomPay (NA) + Planet (EMEA) + Shift4 (Oracle OPI) + Sertifi (global auth) patchwork with one orchestration layer. Centralized dashboard, real time analytics across all 9,300+ properties, automated reconciliation. Eliminates the 11+ hours weekly operators spend on manual data consolidation.

5. **Greater China growth play** | With 18% of the pipeline in Greater China and WeChat Pay's 900M+ users largely inaccessible for online bookings, Yuno activates WeChat Pay, Alipay+, and UnionPay online across the full booking flow. This is critical for Marriott's largest international growth market.

6. **Drew Pinto is the buyer** | As Chief Revenue & Technology Officer, he owns both the revenue strategy ($35B+ in channels) and the technology stack. Payment orchestration sits squarely at the intersection of his dual mandate. His AI incubator and Bonvoy Wallet launch signal openness to payment innovation.

7. **NOVA AI for auth rate recovery** | With $26.2B in revenue and millions of cross border transactions, even a 2 to 3% auth rate improvement via smart routing and NOVA AI hard decline recovery (proven 75% at Viva Aerobus) translates to hundreds of millions in recovered revenue annually.

**Sources:**
- [Marriott FY2025 Results](https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-reports-fourth-quarter-and-full-year-2025)
- [Marriott FY2024 Results](https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-reports-fourth-quarter-and-full-year-2024)
- [FreedomPay x Marriott Agreement (Nov 2019)](https://www.prnewswire.com/news-releases/freedompay-announces-an-agreement-with-marriott-international-for-commerce-technology-innovation-300954692.html)
- [Planet x Marriott Case Study](https://www.weareplanet.com/we-helped-marriott-hotels-overcome-their-payment-processing-challenges)
- [Shift4 x Oracle OPERA EMV Certification](https://www.shift4.com/news/shift4-payments-adds-emv-to-certification-with-oracles-opera-property-management-system)
- [Sertifi x Marriott Customer Story](https://corp.sertifi.com/marriott/)
- [Oracle Cloud x Marriott PMS Announcement](https://www.prnewswire.com/news-releases/oracle-cloud-to-help-elevate-property-management-for-marriott-international-302047269.html)
- [Toast x Marriott Restaurant Partnership](https://www.hoteldive.com/news/toast-for-hotel-restaurants-marriott-partnership/652951/)
- [Marriott x Alipay (NFCW)](https://www.nfcw.com/2015/09/09/337651/marriott-hotels-to-accept-alipay/)
- [Marriott x Apple Pay (Retail Dive)](https://www.retaildive.com/ex/mobilecommercedaily/marriott-international-checks-in-apple-pay-for-extended-stay)
- [FTC Action Against Marriott (Oct 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/10/ftc-takes-action-against-marriott-starwood-over-multiple-data-breaches)
- [FTC Consent Order Finalized (Dec 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-finalizes-order-marriott-starwood-requiring-them-implement-robust-data-security-program-address)
- [$52M Marriott Settlement](https://topclassactions.com/lawsuit-settlements/privacy/data-breach/52m-marriott-settlement-to-resolve-data-breach-claims/)
- [Marriott Data Breach Overview (Huntress)](https://www.huntress.com/threat-library/data-breach/marriott-data-breach)
- [Drew Pinto Profile (CIO Dive)](https://www.ciodive.com/news/Marriott-International-C-suite-CTO-change/643645/)
- [Marriott Technology Transformation (PhocusWire)](https://www.phocuswire.com/marriott-technology-transformation-ai-developments)
- [Why Hotel Payments Are Broken (Hospitality Upgrade)](https://www.hospitalityupgrade.com/techtalk/definitely-doug-4-19-24-why-hotel-payments-are-broken-and-costly-and-how-to-fix-them)
- [Hospitality Payment Report (Payrails)](https://www.payrails.com/blog/hospitality-payment-report)
- [Hotel Operations Index 2026](https://www.hotel-online.com/index.php/news/the-2026-hotel-operations-index-progress-pressure-and-the-path-forward)
- [Hotel Payment Fragmentation (Hotel Technology News)](https://hoteltechnologynews.com/2026/02/why-hotel-technology-is-finally-breaking-up-with-fragmented-systems/)
- [DCC Complaints at Marriott (FlyerTalk)](https://www.flyertalk.com/forum/marriott-marriott-bonvoy/2121093-currency-conversion-scam-marriotts-3.html)
- [Marriott Price Inflation (LoyaltyLobby)](https://loyaltylobby.com/2023/01/30/reader-question-why-marriott-allows-hotels-to-misquote-prices-inflate-them-by-15/)
- [Marriott.com Traffic (SimilarWeb)](https://www.similarweb.com/website/marriott.com/)
- [Marriott Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/MAR/marriott/revenue)
- [Marriott Logo](https://companieslogo.com/marriott-international/logo/)
- [Marriott Investor Day Speakers](https://irday.marriottinternational.com/speakers)
- [Marriott Leadership Changes (Jan 2026)](https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-announces-changes-its-continent)
