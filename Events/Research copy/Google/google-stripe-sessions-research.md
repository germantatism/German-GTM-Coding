# GOOGLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Google
=======================================

Logo: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
Nombre merchant: Google

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Billing Error Churn
Tittle_Pain Point_2: Fragmented Stacks
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: Regulatory Fracture
Tittle_Pain Point_5: Cross-Border Decline

Desc_Pain Point_1: 32.3% of Google Play cancellations are involuntary billing errors, double the App Store rate. With $52B+ in Play revenue and 325M paid subscribers, even 1% recovery unlocks hundreds of millions.
Desc_Pain Point_2: Google operates separate billing rails for Play, YouTube Premium, Google One, Workspace, and Cloud. Each stack has its own PSP mix, reconciliation, and reporting with no unified view.
Desc_Pain Point_3: Google Play supports 290+ methods but key APMs remain absent in top markets. No BLIK subscriptions in Poland, no Konbini in Japan, no Nequi in Colombia, no Fawry in Egypt.
Desc_Pain Point_4: Epic v. Google injunction (Oct 2025) forces third party billing in the US. EU DMA mandates the same. Google must now manage multi-PSP flows it never had to orchestrate before.
Desc_Pain Point_5: India (95% Android) and Brazil (81% Android) drive massive Play downloads but card auth rates lag. RBI auto-debit rules and cross-border FX markups inflate involuntary churn.

SLIDE 1: PSP TOPOLOGY

PSP_1: Google Play Billing (In-house)
PSP_2: Adyen
PSP_3: Stripe
PSP_4: Braintree (PayPal)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: BLIK (subscriptions)
Local_M_2: Konbini
Local_M_3: Fawry
Local_M_4: Nequi
Local_M_5: MoMo
Local_M_6: SPEI
Local_M_7: Boleto (subscriptions)
Local_M_8: PhonePe
Local_M_9: Maya
Local_M_10: Efecty (subscriptions)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the highest performing processor by card BIN, issuer, and country. With $52B+ in annual Google Play revenue and 325M+ paid subscribers across YouTube Premium, Google One, and Play, a 3% auth uplift translates to $1.5B+ in recovered annual revenue. AI powered decisioning optimizes every transaction.
Desc_Yuno_Cap2: Automatic cascade across processors when the primary rail declines. Grace periods recover 57% more renewals, but Yuno adds instant failover to a backup PSP before the grace window even starts. Up to 50% recovery on soft declines, turning involuntary churn into retained subscribers.
Desc_Yuno_Cap3: Activates the APMs Google Play still lacks for subscriptions: BLIK in Poland, Konbini in Japan, Fawry in Egypt, Nequi in Colombia, PhonePe in India, Maya in Philippines, SPEI in Mexico. One API, 1,000+ payment methods, instant geo-routing. Zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Google's fragmented Play Billing + Adyen + Stripe + Braintree settlement streams across Play, YouTube Premium, Google One, and Workspace. Real-time approval rate monitoring, centralized reconciliation, millisecond anomaly detection via Monitors across all providers and 200+ countries.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Google / Alphabet at a glance:**
- Alphabet FY2025 revenue: $402.8B (up 15% YoY), net income $132.2B
- Google Services revenue: $95.9B in Q4 2025 (up 14% YoY), includes Play, YouTube, Subscriptions, Devices
- Google subscriptions, platforms, and devices: $13.6B in Q4 2025 (up 17% YoY)
- YouTube total revenue (ads + subscriptions): exceeded $60B for full year 2025
- YouTube subscription business: ~$20B annual run rate (Music, Premium, TV, NFL Sunday Ticket)
- YouTube Music + Premium: 125M paid subscribers (March 2025), adding ~2M per month
- Google Play Store revenue: $52.3B in 2025 (up from $46.7B in 2024)
- Google paid consumer subscribers: exceeded 325M across Google One, YouTube Premium, and other services
- Google One and YouTube Premium identified as key growth drivers for subscription segment
- Geographic split (2024): US 48.7% ($170.5B), EMEA 29.2% ($102.1B), APAC 16.2% ($56.8B), Americas ex-US 5.8% ($20.4B)

**Confirmed PSPs and Billing Infrastructure:**
- Google Play Billing: proprietary in-house system, supports 290+ forms of payment globally
- Adyen: integrated as PSP for Google Pay API processing (official documentation confirms)
- Stripe: integrated as PSP for Google Pay API (official documentation confirms)
- Braintree (PayPal): integrated as PSP for Google Pay API (official documentation confirms)
- Checkout.com: listed as supported PSP for Google Pay integrations
- Cybersource: listed as supported PSP for Google Pay integrations
- Square: listed as supported PSP for Google Pay integrations
- No payment orchestrator detected across any Google property
- Google Wallet available in 146 countries for tap to pay

**Leadership (Payments):**
- Jenny Cheng: former VP/GM of Google Wallet, recently moved to VP/GM of Merchant Shopping. Expanded Google Wallet to 90+ countries
- Sameer Samat: President, Android Ecosystem (Play Store, WearOS, TV, Automotive). Formerly helped start Google Commerce team
- Kunal Rana: Director of Merchant Services, Google Pay (appointed June 2024)
- Ashwin Samuel: Head of Analytics, Payments at Google (team of 70+ analysts and data scientists)
- No single VP of Payments role identified post Caesar Sengupta departure (left April 2021)

**Google Pay / Wallet evolution:**
- Google Pay standalone app shut down in US on June 4, 2024. Functionality consolidated into Google Wallet
- Google Wallet now used 5x more than the old Pay app was in the US
- Google Wallet available in 146 countries with varying payment method support
- Google Pay remains active as standalone app in India and Singapore

**Top 5 Markets Gap Analysis:**

MARKET 1: India (95% Android, 19.1B annual Play downloads, #1 by volume)
  Accepted: Visa/MC, UPI (all providers), netbanking, carrier billing, gift cards, debit cards
  Missing: PhonePe direct billing, RuPay for subscriptions, auto-debit compliant recurring (RBI mandate issues)
  Insight: RBI regulations cause banks to decline automatic card charges for recurring payments. PayTM UPI handles deprecated by NPCI order. Massive involuntary churn from regulatory friction.

MARKET 2: Brazil (81% Android, 9B+ annual Play downloads, #2 by volume)
  Accepted: Visa/MC/Elo credit cards, Pix (one-time only), Mercado Pago, PicPay, PayPal, gift cards
  Missing: Pix for subscriptions, Boleto for subscriptions, local installment cards (parcelado)
  Insight: Pix processes 6.2B+ monthly transactions (March 2025) but Google Play only supports it for one-time purchases. No recurring Pix support means subscription apps lose the #1 payment method in Brazil.

MARKET 3: United States (#1 by revenue, ~$2B in H1 2024 alone)
  Accepted: Visa/MC/Amex/Discover, PayPal, Cash App Pay, Google Play balance, gift cards, carrier billing
  Missing: ACH direct debit, Venmo direct (only via PayPal), buy now pay later options
  Insight: Epic v. Google injunction (upheld July 2025) now allows third party billing. Google must accept alternative PSPs from Oct 29, 2025. Service fee reduced to 9-20% range.

MARKET 4: Indonesia (90%+ Android, top 5 by downloads)
  Accepted: Visa/MC, Dana, Doku, GoPay, OVO, ShopeePay, cash at convenience stores, gift cards
  Missing: QRIS direct (works via e-wallets but no native QRIS checkout), LinkAja, carrier billing (not confirmed)
  Insight: E-wallets cover 96% of Indonesian consumers via QRIS interoperability. Google Play integrates the top 5 wallets but subscription support is limited.

MARKET 5: Japan (#2 by revenue globally, $421M in H1 2024)
  Accepted: Visa/MC/JCB/Amex, carrier billing (NTT Docomo, au, SoftBank), gift cards, Google Play balance
  Missing: Konbini direct payment, PayPay, Rakuten Pay, LINE Pay
  Insight: Konbini (convenience store) payments are critical for unbanked/underbanked Japanese users. Google Play only supports gift card purchases at convenience stores, not direct konbini billing.

**Additional Markets of Note:**

MEXICO: Mercado Pago accepted, carrier billing available. Missing: OXXO for subscriptions, SPEI direct.
COLOMBIA: PSE enabled September 2025 (one-time only), Efecty (one-time only). Missing: Nequi, PSE for subscriptions.
POLAND: BLIK accepted for purchases. Missing: BLIK for recurring subscriptions.
GERMANY: PayPal, carrier billing. Missing: SEPA Direct Debit native, Giropay.
TURKEY: Carrier billing. Missing: local bank transfers, iyzico wallet integration.

**Billing Error and Churn Data:**
- 32.3% of all Google Play cancellations are involuntary billing errors (RevenueCat 2026 State of Subscription Apps, 115,000+ apps, $16B+ tracked revenue)
- This is more than double the App Store's 15.2% involuntary cancellation rate
- Grace periods improve recovery by 57%, account hold adds 35% more recovery and 8% less involuntary churn
- Combining grace period + account hold triples decline recovery from ~10% to 33%
- A subscriber surviving the 1st monthly renewal has 73-82% chance of reaching the 3rd
- Once a monthly subscriber churns, only ~20% return within a year; annual subscribers only ~5%
- Emerging markets show highest initial billing friction but converge by 3rd renewal cycle

**Regulatory and Competitive Landscape:**
- Epic v. Google: Ninth Circuit upheld antitrust injunction (Sept 12, 2025). Effective Oct 29, 2025, Google cannot require Play Billing for apps on Play Store
- Proposed Epic/Google settlement (Nov 2025): 9-20% service fee, alternative app stores allowed globally
- EU DMA: Google designated as gatekeeper, must allow third party billing and alternative app stores
- UK CMA: secured commitments from Google for fair competition in 2025
- Google Play now must manage multi-PSP ecosystem it previously controlled end to end
- Over 67 outages affected Google Play users in the past ~2 years (StatusGator)
- Last acknowledged outage: Jan 3, 2026; detected outage: Feb 10, 2026
- Google Pay API had Android LoadPaymentData issues affecting significant user subset

**Key meeting angles:**
1. **Subscription churn crisis** | 32.3% involuntary billing errors on Play vs 15.2% on iOS. At $52B+ revenue, recovery is worth billions
2. **Regulatory disruption** | Epic injunction + DMA force multi-PSP management Google never built for. Yuno was designed for exactly this
3. **325M subscriber base** | YouTube Premium, Google One, and Play subscriptions all need optimized recurring billing across 200+ countries
4. **India/Brazil paradox** | Highest Android adoption, highest download volumes, but recurring payment infrastructure lags massively
5. **Fragmented billing stacks** | Play, YouTube, Workspace, Cloud each run separate billing. No unified orchestration layer
6. **$60B YouTube opportunity** | YouTube's subscription business alone is $20B annually, and subscription billing errors directly erode that growth
7. **Competitor precedent** | Spotify (multi-PSP via Adyen), Netflix (multi-PSP + local methods), Apple (investing in APM expansion)

**Yuno Reference Cases:**

InDrive: Achieved 90% payment approval rate. Expanded into 10 Latin American countries in under 8 months. Access to 300+ payment methods through single API. Smart Routing and real-time monitoring via unified checkout.

Rappi: Cut new provider implementation time to near zero. Reduced payment issue response time from minutes to seconds. AI smart routing decreased transaction failures. Analysts spend 80% less time resolving disruptions. Monitors auto-redirect traffic during provider outages.

McDonald's: Streamlined multi-country payment operations through Yuno orchestration. Integrated PSPs to expand payment options. Improved authorization rates and user experience across markets.

**Sources:**
- [Alphabet FY2025 Earnings (SEC Filing)](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm)
- [Alphabet FY2024 Earnings (SEC Filing)](https://www.sec.gov/Archives/edgar/data/1652044/000165204425000010/googexhibit991q42024.htm)
- [Alphabet Revenue by Geography (StockAnalysis)](https://stockanalysis.com/stocks/googl/metrics/revenue-by-geography/)
- [Google Play Revenue Guide (HubiFi)](https://www.hubifi.com/blog/google-play-revenue-guide)
- [Google Play Store Statistics 2026 (SQ Magazine)](https://sqmagazine.co.uk/google-play-store-statistics/)
- [Google Play Accepted Payments: Brazil](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DBR)
- [Google Play Accepted Payments: India](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DIN)
- [Google Play Accepted Payments: Mexico](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DMX)
- [Google Play Accepted Payments: Indonesia](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DID)
- [Google Play Accepted Payments: Colombia](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DCO)
- [Google Play Accepted Payments: Japan](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DJP)
- [Google Play Accepted Payments: Poland](https://support.google.com/googleplay/answer/2651410?hl=en&co=GENIE.CountryCode%3DPL)
- [Google Play Accepted Payments: Ultimate List (Beebom)](https://beebom.com/accepted-payment-methods-google-play-store-ultimate-list/)
- [Google Play Billing Error Churn (RevenueCat)](https://www.revenuecat.com/blog/growth/google-play-billing-error-churn-how-to-fix/)
- [Google Play Billing Errors Double iOS (Android Headlines)](https://www.androidheadlines.com/2025/10/google-play-store-subscription-billing-errors-double-ios-rate.html)
- [Google Play Billing Declined Rates (RevenueCat Community)](https://community.revenuecat.com/general-questions-7/huge-payment-declined-rate-on-google-play-store-5069)
- [Google Play Alternative Billing / Epic Injunction (Play Console Help)](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en)
- [Epic v. Google Injunction Upheld (NeonPay)](https://www.neonpay.com/blog/epic-v-google-appeals-court-upholds-injunction-alternative-payments-on-the-way)
- [Google Play US Billing Policy Update (Android Headlines)](https://www.androidheadlines.com/2025/10/google-play-store-alternative-third-party-billing-us-ruling-epic-games.html)
- [Google Pay PSP Integrations (Google Developers Blog)](https://developers.googleblog.com/en/easily-connect-google-pay-with-your-preferred-payment-processor/)
- [Google Pay App Shutdown (TechCrunch)](https://techcrunch.com/2024/02/23/google-is-sunsetting-the-google-pay-app-in-the-us-later-this-year/)
- [Google Wallet Countries (Android Metro)](https://www.androidmetro.com/2024/04/google-wallet-available-countries.html)
- [Jenny Cheng VP/GM Google Wallet (NMI Podcast)](https://www.nmi.com/resources/podcasts/nmis-payment-playbook-podcast-episode-15-jenny-cheng-vp-and-gm-of-google-wallet/)
- [Kunal Rana Director Google Pay (HR Today)](https://hrtoday.in/kunal-rana-appointed-as-director-merchant-services-google-pay-at-google/)
- [YouTube Subscriptions $60B (TechCrunch)](https://techcrunch.com/2026/02/05/googles-subscriptions-rise-in-q4-as-youtube-pulls-60b-in-yearly-revenue/)
- [YouTube Premium 125M Subscribers (Accio)](https://www.accio.com/business/trend-of-youtube-premium-1-year)
- [App Downloads by Country (AppTweak)](https://www.apptweak.com/en/reports/app-downloads-by-country)
- [Top Google Play Markets by Revenue (Statista)](https://www.statista.com/statistics/1496829/gp-top-app-markets-by-revenue/)
- [Google Play Status Dashboard](https://status.play.google.com/)
- [Google Pay API Status Dashboard](https://developers.google.com/pay/api/status)
- [Google Brand Resource Center](https://about.google/brand-resource-center/brand-elements/)
- [Yuno: Payment Orchestration Platform](https://y.uno/)
- [InDrive + Yuno Success Case](https://y.uno/success-cases/indrive)
- [Rappi + Yuno Success Case](https://y.uno/success-cases/rappi)
- [Yuno Success Cases Overview](https://y.uno/success-cases)
- [Pix 6.2B Monthly Transactions (WooshPay)](https://www.wooshpay.com/resources/knowledge/2025/11/24/brazil-payment-methods-ecosystem-pix-on-top-local-cards-still-critical-boleto-not-dead/)
- [India Android Market Share (Google Play Stats)](https://ripenapps.com/blog/google-play-store-statistics/)
- [Google PSE Colombia (MobileTime LATAM)](https://mobiletime.la/noticias/03/09/2025/google-play-habilita-pse-en-colombia/)
- [Indonesia E-Wallets 96% Coverage (Transfi)](https://www.transfi.com/blog/indonesias-e-wallets-ovo-gopay-dana-explained)
