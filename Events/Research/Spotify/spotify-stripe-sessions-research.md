# SPOTIFY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Spotify
=======================================

Logo: https://storage.googleapis.com/pr-newsroom-wp/1/2023/05/Spotify_Full_Logo_RGB_Green.png
Nombre merchant: Spotify

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 16 PSP Orchestration Tax
Tittle_Pain Point_2: Involuntary Churn Leak
Tittle_Pain Point_3: Cross Border Auth Drag
Tittle_Pain Point_4: UPI/Wallet Fragility
Tittle_Pain Point_5: Emerging Market Gaps

Desc_Pain Point_1: Spotify built a custom Billing API to unify 16 PSPs internally. Every new market, method, or provider means custom engineering. Maintenance cost scales linearly while orchestration platforms solve this with a single integration.
Desc_Pain Point_2: Nearly half of subscription churn is involuntary, caused by failed renewals. With 290M premium subscribers, even 1% involuntary churn equals ~2.9M lost accounts per year and ~€150M+ in lost annual revenue at current ARPU.
Desc_Pain Point_3: Users report cards declined despite sufficient funds, with banks showing no charge attempt from Spotify. Cross border routing in 184 markets creates silent auth failures that erode conversion without clear visibility.
Desc_Pain Point_4: UPI autopay in India and GCash in Philippines show persistent payment failures in community forums. Users report charges debited but Spotify marks payment as failed, indicating PSP reconciliation gaps.
Desc_Pain Point_5: Africa and Southeast Asia grow 20%+ YoY but local APM coverage remains thin. No OXXO in Mexico, no PSE in Colombia, no Nequi confirmed. Cash heavy markets lack digital conversion paths for 460M+ free users.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: PayPal
PSP_3: Klarna
PSP_4: Boku

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: PSE
Local_M_3: Nequi
Local_M_4: Mercado Pago
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Maya
Local_M_8: SPEI
Local_M_9: PhonePe
Local_M_10: RuPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + Recovery
Tittle_Yuno_Cap3: 1,000+ Local Methods
Tittle_Yuno_Cap4: NOVA Fraud Intelligence

Desc_Yuno_Cap1: Per transaction routing across all 16+ PSPs without maintaining a custom Billing API. Each renewal is routed to the highest performing acquirer for that card BIN, issuer, and market. With €15.3B in premium revenue and 290M subscribers, a 3% auth uplift translates to €460M+ in recovered annual revenue. InDrive achieved 90% approval rates across 10 LATAM markets.
Desc_Yuno_Cap2: Automatic cascade across PSPs eliminates silent auth failures. When Adyen declines, Yuno reroutes to the next best acquirer in milliseconds, turning failed renewals into recovered recurring revenue. Up to 50% recovery on failed transactions. Livelo recovered +5% approvals within 3 months.
Desc_Yuno_Cap3: Activates the local APMs Spotify's 460M free users need to convert: OXXO in Mexico, PSE and Nequi in Colombia, BLIK in Poland, Bancontact in Belgium, Maya in Philippines, RuPay and PhonePe in India. One API, 1,000+ methods, instant geo routing. No engineering sprints per market.
Desc_Yuno_Cap4: AI powered fraud scoring replaces fragmented per PSP fraud rules. NOVA analyzes 5,000+ data points per transaction, reducing false declines by up to 75%. For a subscription business with 290M renewals/month, even a 0.5% false decline reduction recovers ~1.45M subscribers monthly. McDonald's uses NOVA across LATAM markets.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Spotify at a glance:**
- 751M MAU (Q4 2025), 290M premium subscribers, available in 184 countries
- Revenue: €17.1B (2025), €15.67B (2024). First full year of profitability in 2024
- Premium revenue: €15.34B (2025), representing ~90% of total revenue
- HQ: Stockholm, Sweden. Listed on NYSE (SPOT)
- CEO: Daniel Ek (co founder). CFO: Christian Luiga
- Price increases: Individual plan raised to $12.99 (2026), $11.99 (2024), from $10.99 (2023)
- 1% churn uptick erodes ~€120M in EBIT, given 32% premium tier gross margin
- Gross margin improved to 31.6% in Q4 2025

**Payments leadership:**
- Sandra Alzetta: VP, Global Head of Commerce and Customer Service (formerly VP, Global Head of Payments). 27 years at Visa before joining Spotify in 2019. Key quote: "We want to make sure that our users are able to pay in the way that feels natural to them."
- Andy Wiggan: Head of Payments and Conversion. 15+ years across fintech/payments, previously at GoCardless. Now at Mangopay (left Spotify).
- Payments is a strategic priority, not buried in engineering. Sandra reports to senior leadership and oversees 184 country payment operations.

**Confirmed PSPs (16 total, 4 primary identified):**
- Adyen: Primary PSP since 2015. Full stack acquirer handling subscriptions, local currencies, and regional methods across 60+ countries. Adyen case study confirms Spotify as a marquee client.
- PayPal: Secondary PSP, added 2011. Available in select markets.
- Klarna: European BNPL, added 2013. Users get Premium now and pay later with 30 day settlement window.
- Boku: Carrier billing, added 2013. Enables mobile operator billing in markets with low card penetration.
- Sofort: European bank transfers (now Klarna Group), added 2013.
- Google Play / Apple App Store: Mobile IAP channels.
- Additional PSPs: Spotify's internal Billing API interfaces with 16 PSPs total (Nordic APIs, 2016 data). The full list is not publicly disclosed.
- No third party payment orchestrator detected. Spotify built a custom internal orchestration layer (Billing API + Checkout API).

**Payment architecture (Nordic APIs source):**
- Checkout API: Manages communication between Payment Backend and client apps. State machine guiding variable checkout workflows per market.
- Billing API: Intermediary between Payment Backend and 16 PSPs. Abstracts varying provider logic into standardized JSON calls.
- Anomaly detection system: Built on top of Billing API data, monitoring payment trends to detect provider outages and local issues (bank holidays, etc.).
- Evolution: Credit/debit cards only (2008) > PayPal (2011) > Boku, Sofort, Klarna, Google IAP, Facebook payments (2013) > Adyen partnership for 250+ methods and 150+ currencies (2015) > ~40 methods across 60 markets (2016).

**Top 5 Markets (traffic share + payment analysis):**

MARKET 1: United States (27.3% of traffic, ~65M users)
  Confirmed methods: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay
  Gap: No Venmo standalone, no Cash App Pay, no ACH for subscriptions

MARKET 2: Brazil (4.7% of traffic, est. ~35M users)
  Confirmed methods: Credit/debit cards, Pix (added June 2023), Boleto bancario, gift cards
  Gap: Pix is prepaid only (no recurring), no Mercado Pago

MARKET 3: United Kingdom (4.6% of traffic)
  Confirmed methods: Visa/MC/Amex, PayPal, Klarna
  Gap: No Open Banking payments (Truelayer/GoCardless style)

MARKET 4: Mexico (4.5% of traffic, est. ~34M users)
  Confirmed methods: Credit/debit cards, carrier billing
  Gap: No OXXO, no SPEI, no Mercado Pago confirmed online

MARKET 5: India (3.8% of traffic, est. ~28M users)
  Confirmed methods: UPI, net banking, credit/debit cards
  Gap: UPI autopay failures widely reported. No RuPay, no PhonePe, no Paytm confirmed

**Payment complaints and outage history:**
- April 2025: Major 3 hour outage affecting millions in North America (Fortune)
- September 2024: Large outage, 40,000+ users affected in US
- Community forums show persistent "Payment failed" complaints across regions
- India UPI: Users report UPI autopay charged but Spotify marks payment as failed (reconciliation gap)
- Philippines GCash: Multiple community threads about GCash not appearing as option or payments failing
- Indonesia: Credit/debit cards NOT supported, only GoPay, Dana, and carrier billing
- Cross border: Users report cards declined despite bank showing no charge attempt from Spotify
- Renewal failures: Users report autopay failing even with valid, funded cards

**Key meeting angles:**
1. **Custom orchestration cost** | Spotify built and maintains a Billing API for 16 PSPs internally. This is engineering overhead a platform like Yuno eliminates with a single integration.
2. **Involuntary churn at scale** | With 290M subscribers, even micro improvements in renewal auth rates translate to massive revenue recovery. Industry data shows ~50% of subscription churn is involuntary (failed payments).
3. **Pix is prepaid only** | Brazil (Spotify's #2 market) added Pix but only for prepaid/one time purchases. No recurring Pix support. Yuno's Pix recurring capability could unlock Brazil's largest payment method for subscriptions.
4. **India reconciliation gap** | UPI autopay charges users but Spotify marks payment failed. This suggests a PSP level reconciliation issue that Smart Routing and real time monitoring would surface and resolve.
5. **460M free to paid conversion** | 461M free users who could convert to paid. Local APMs (OXXO, PSE, BLIK, Bancontact) remove payment friction in markets where card penetration is low.
6. **Sandra Alzetta (ex Visa, 27 years)** | Head of Payments understands orchestration deeply. Conversation can be technical and strategic.
7. **Price increases + churn risk** | Three consecutive price hikes (2023, 2024, 2026). Each hike amplifies churn risk. Payment optimization becomes critical retention infrastructure.

**Sources:**
- [Spotify Support: Payment Methods](https://support.spotify.com/us/article/payment-methods/)
- [PYMNTS: Spotify How Users Pay](https://www.pymnts.com/news/payment-methods/2025/spotify-says-how-users-pay-as-important-as-what-they-play)
- [Adyen: Spotify Case Study](https://www.adyen.com/en_GB/knowledge-hub/spotify)
- [Nordic APIs: Spotify Internal Payment APIs](https://nordicapis.com/the-brilliance-of-spotify-internal-apis-to-mitigate-payments/)
- [Spotify Newsroom: Pix in Brazil](https://newsroom.spotify.com/2023-06-13/spotify-brazil-expands-payment-methods-with-pix/)
- [Spotify Newsroom: Logo and Brand Assets](https://newsroom.spotify.com/media-kit/logo-and-brand-assets/)
- [Sandra Alzetta: The Org](https://theorg.com/org/spotify/org-chart/sandra-alzetta)
- [Sandra Alzetta: LinkedIn](https://www.linkedin.com/in/sandraalzetta/)
- [Adyen: Andy Wiggan Insights](https://www.adyen.com/knowledge-hub/5-insights-from-andy-wiggan-head-of-payments-spotify)
- [Fortune: Spotify April 2025 Outage](https://fortune.com/2025/04/16/spotify-not-working-down-outage/)
- [Spotify Community: UPI Failures](https://community.spotify.com/t5/Subscriptions/UPI-Autopay-charged-me-but-Spotify-says-payment-failed/td-p/6597871)
- [Spotify Community: GCash Issues](https://community.spotify.com/t5/Subscriptions/GCash-payments-keep-failing/td-p/6399186)
- [Spotify Community: Indonesia Cards Not Supported](https://community.spotify.com/t5/Subscriptions/Credit-Debit-card-is-not-supported-for-Indonesia-as-a-payment/td-p/5333655)
- [Spotify Community: Payment Failed](https://community.spotify.com/t5/Subscriptions/Payment-failed/td-p/6362884)
- [DemandSage: Spotify Stats 2026](https://www.demandsage.com/spotify-stats/)
- [Business of Apps: Spotify Statistics 2026](https://www.businessofapps.com/data/spotify-statistics/)
- [Fast Company: Adyen IPO / Spotify Client](https://www.fastcompany.com/40577258/adyen-payments-processor-for-spotify-and-uber-plans-to-ipo-in-june)
- [Spotify Support: UPI Payments India](https://support.spotify.com/in-en/article/paying-for-spotify-with-upi/)
- [Spotify Support: Klarna Payments](https://support.spotify.com/de-en/article/klarna-payments/)
- [Spotify Support: Carrier Billing](https://support.spotify.com/id-en/article/mobile-billing-payments/)
- [CNBC: Spotify Price Hike 2026](https://www.cnbc.com/2026/01/15/spotify-subscription-price-premium-us.html)
- [Revology Analytics: Spotify Price Rise Analysis](https://www.revologyanalytics.com/articles-insights/an-rgm-deep-dive-into-spotifys-latest-price-rise)
- [FF News: Sandra Alzetta Paytech Magazine](https://ffnews.com/thought-leader/the-paytech-magazine/the-paytech-magazine-issue-17/exclusive-optimising-the-payments-stream-sandra-alzetta-spotify-in-the-paytech-magazine/)
- [Wikipedia: Spotify](https://en.wikipedia.org/wiki/Spotify)
