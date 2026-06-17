# LYFT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Lyft
=======================================

Logo: https://logo.clearbit.com/lyft.com
Nombre merchant: Lyft

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: EU Payment Gap
Tittle_Pain Point_3: Driver Payout Friction
Tittle_Pain Point_4: Auth Decline Blind Spots
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: Lyft runs Stripe, Braintree, and First Data as separate integrations with no unified orchestration. Terms of service confirm Lyft "may replace its third-party payment processor without notice," signaling a patchwork stack lacking centralized routing or failover logic.
Desc_Pain Point_2: FreeNow acquisition (July 2025) added 9 European countries and 180+ cities overnight, but Lyft lacks local APMs like Giropay, Bancontact, iDEAL, Bizum, and BLIK. FreeNow only accepts cards, PayPal, Apple Pay, and Google Pay today.
Desc_Pain Point_3: Express Pay charges drivers $1.75 per instant payout, yet transfers still fail regularly. Driver forums report missing payouts, failed bank transfers, and delays exceeding 24 hours. On 945M annual rides, payout friction directly impacts driver retention.
Desc_Pain Point_4: Riders report widespread "payment declined" errors even with valid cards. Multiple YouTube guides and support threads document recurring payment failures through 2025 and 2026, suggesting no smart retry or cascade logic across Lyft's three PSPs.
Desc_Pain Point_5: FreeNow processes EUR across 9 countries while Lyft's core runs USD in US and CAD in Canada. On $18.5B gross bookings (2025), unifying settlement across 3 currencies and 11 countries without orchestration creates reconciliation overhead.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Braintree (PayPal)
PSP_3: First Data (Fiserv)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Giropay (Germany)
Local_M_2: Bancontact (Belgium)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Bizum (Spain)
Local_M_5: BLIK (Poland)
Local_M_6: Satispay (Italy)
Local_M_7: MB WAY (Portugal)
Local_M_8: Revolut Pay (UK/EU)
Local_M_9: Venmo (US)
Local_M_10: Interac e-Transfer (Canada)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, Braintree, and First Data. Each ride payment routed to the highest performing processor for that card BIN, issuer, and market. On $18.5B gross bookings across 11 countries, smart routing delivers +3 to 10% auth uplift, recovering hundreds of millions in ride revenue. InDrive achieved 90% approval across 10 markets with Yuno.
Desc_Yuno_Cap2: Automatic cascade across Lyft's three PSPs eliminates single-processor dependency. When Stripe declines, Yuno reroutes to Braintree or First Data in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions, directly reducing the "payment declined" errors riders report.
Desc_Yuno_Cap3: Activates the APMs Lyft and FreeNow still lack: Giropay in Germany, Bancontact in Belgium, iDEAL in Netherlands, Bizum in Spain, BLIK in Poland, Satispay in Italy, and Venmo in the US. One API, 1,000+ payment methods, no custom integration per vendor. Critical for converting Europe's 150K+ FreeNow drivers and millions of riders.
Desc_Yuno_Cap4: One dashboard replacing Lyft's fragmented Stripe + Braintree + First Data settlement across USD, CAD, and EUR. Real-time approval monitoring across all routes, centralized reconciliation for 11 countries, and millisecond anomaly detection. Rappi integrated Yuno with zero implementation friction. McDonald's gained +4.7% auth rate ($3.2M impact) with orchestration.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Lyft at a glance:**
- Rideshare and mobility platform (rides, bikes, scooters, autonomous vehicles)
- Revenue: $6.3B (2025, +9% YoY); Gross Bookings: $18.5B (2025, +15% YoY)
- 945.5M rides in 2025 (all-time high, +14% YoY)
- 51.3M annual active riders (2025, all-time high)
- Net Income: $2.8B (2025); Adjusted EBITDA: $528.8M; Free Cash Flow: $1.12B
- Operates in 11 countries, ~1,000 cities (US, Canada, + 9 European countries via FreeNow)
- NASDAQ: LYFT, market cap ~$7B+
- Founded: 2012, San Francisco. CEO: David Risher (since April 2023)

**Leadership:**
- David Risher: CEO since April 2023. Former Amazon VP. Known for "customer obsession" approach, personally drives for Lyft monthly
- Erin Brewer (Lampert): CFO since July 2023. Architect of cost discipline program. Berkeley Haas MBA
- Kristin Sverchek: President
- No dedicated VP of Payments identified publicly. Payments decisions likely sit under engineering/product leadership

**FreeNow Acquisition (July 2025):**
- Acquired from BMW Group and Mercedes-Benz Mobility for EUR 175M (~$197M)
- Operates in 9 European countries: UK, Ireland, Germany, France, Spain, Italy, Poland, Greece, Austria
- 180+ cities, 150,000+ drivers
- Nearly doubles Lyft's total addressable market to 300B+ personal vehicle trips/year
- FreeNow expected to generate ~EUR 1B top line in 2026
- Current FreeNow payment methods: Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, cash (select markets)
- NO local European APMs supported (no Giropay, Bancontact, iDEAL, Bizum, BLIK, Satispay)

**Canada Market:**
- Rides grew 23% YoY in summer 2025
- Toronto tech hub expansion announced October 2025
- Expanding to Halifax, Regina, Saskatoon (Nova Scotia and Saskatchewan)
- Bikeshare programs in Ontario and Quebec

**Confirmed PSPs:**
- Stripe: Primary processor for rider payments and driver Express Pay (confirmed via Stripe case study and newsroom)
- Braintree (PayPal): Secondary processor (confirmed via Lyft Terms of Service)
- First Data (now Fiserv): Listed in ToS as third processor
- Lyft Terms of Service explicitly states: "All charges are facilitated through third-party payment processors (First Data, Stripe, Inc., Braintree, a division of PayPal, Inc., etc.)"
- No payment orchestrator detected
- Express Pay built with Stripe: 50%+ of all payouts are instant deposits

**Payment Methods Currently Supported:**
- Credit/Debit cards: Visa, Mastercard, Amex, Discover
- Digital wallets: Apple Pay, Google Pay (Android Pay)
- PayPal
- Lyft Cash: prepaid balance loaded at 35,000+ retail locations (Walmart, Walgreens)
- Lyft Direct: debit card for drivers
- Express Pay: instant payout for drivers ($1.75 fee per transfer)
- FreeNow (Europe): Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, cash

**Missing Local Payment Methods (Gap Analysis):**

MARKET 1: Germany (FreeNow's largest EU market)
  Currently offer: Cards, PayPal, Apple Pay, Google Pay
  Missing: Giropay, SEPA Direct Debit, Klarna, PayPal Pay Later
  Giropay and SEPA dominate German online payments. 58% of Germans prefer bank-based payments over cards.

MARKET 2: Spain (FreeNow market)
  Currently offer: Cards, PayPal, Apple Pay, Google Pay
  Missing: Bizum, Redsys direct debit
  Bizum has 25M+ users in Spain (54% of the population). Essential for mobile-first rideshare.

MARKET 3: Poland (FreeNow market)
  Currently offer: Cards, PayPal, Apple Pay, Google Pay
  Missing: BLIK, Przelewy24
  BLIK processes 60%+ of Polish e-commerce transactions. 17M+ active users.

MARKET 4: Netherlands (FreeNow potential expansion)
  Currently offer: Cards, PayPal, Apple Pay, Google Pay
  Missing: iDEAL, Tikkie
  iDEAL has 70% market share for Dutch online payments. Essential for any digital commerce.

MARKET 5: United States (core market)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Lyft Cash
  Missing: Venmo, Cash App Pay, Affirm
  Venmo has 90M+ US users. Cash App has 57M+ users. Significant overlap with Lyft rider demographics.

MARKET 6: Belgium (FreeNow potential)
  Currently offer: Cards, PayPal
  Missing: Bancontact, Payconiq
  Bancontact processes 80%+ of Belgian debit card transactions and is the dominant online payment method.

**Payment Pain Points (documented):**
1. Rider payment declines: Multiple YouTube guides in 2025/2026 specifically for "How to fix payment failed on Lyft"
2. Server-side payment failures: Lyft support acknowledges "server issues" causing payment method update failures
3. Express Pay failures: Drivers report missing payouts, failed instant transfers, and delays beyond 24 hours
4. Express Pay $1.75 fee: Charged on every instant payout, creating friction for Lyft's 945M annual rides
5. Card verification failures: Riders unable to add or update payment methods due to server glitches
6. No smart retry: Declined transactions show generic "card declined" with no automatic cascade to alternate PSP
7. FreeNow cash limit: EUR 220 max per trip via app payment, limiting premium ride bookings

**Key Meeting Angles:**
1. **FreeNow = Immediate EU payment gap**: 9 countries, 180+ cities, 150K+ drivers, but zero local European APMs. Yuno activates Giropay, Bancontact, iDEAL, Bizum, BLIK via single API
2. **$18.5B gross bookings without orchestration**: Running Stripe + Braintree + First Data separately is exactly the problem Yuno solves. McDonald's gained +4.7% auth rate ($3.2M impact) with Yuno
3. **Driver payout optimization**: 945M rides/year, 50%+ instant payouts, yet Express Pay failures persist. Unified orchestration improves reliability
4. **Auth decline epidemic**: Rider-facing payment failures documented across forums, YouTube, and TikTok. Smart routing + failover eliminates single-PSP dependency
5. **11-country reconciliation**: USD + CAD + EUR settlement across 3 separate PSPs creates massive operational overhead. One dashboard, one API
6. **Autonomous vehicle payments**: Risher says "2026 will be the year of the AV." New modalities require flexible, orchestrated payment infrastructure
7. **FreeNow EUR 1B target**: Growing European revenue demands local payment method coverage to maximize conversion

**Sources:**
- [Lyft Terms of Service (PSP disclosure)](https://www.lyft.com/terms)
- [Stripe Customer: Lyft Case Study](https://stripe.com/customers/lyft)
- [Stripe Newsroom: Lyft and Stripe](https://stripe.com/newsroom/stories/lyft-and-stripe)
- [Lyft Full-Year 2025 Financial Results](https://investor.lyft.com/news-events/press-releases/detail/191/lyft-reports-record-q4-and-full-year-2025-results)
- [Lyft Full-Year 2024 Financial Results](https://investor.lyft.com/news-events/press-releases/detail/103/lyft-reports-record-q4-and-full-year-2024-results)
- [Lyft Q1 2025 Financial Results](https://investor.lyft.com/news-events/press-releases/detail/99/lyft-reports-strong-q1-2025-financial-results)
- [Lyft Goes Global: FreeNow Acquisition Complete](https://investor.lyft.com/news-events/press-releases/detail/96/lyft-goes-global-freenow-acquisition-complete)
- [Lyft Blog: FreeNow Acquisition](https://www.lyft.com/blog/posts/lyft-goes-global-freenow-acquisition-complete)
- [CNBC: Lyft Toronto Tech Hub](https://www.cnbc.com/2025/10/16/lyft-to-open-toronto-tech-hub-deepening-push-beyond-us-market.html)
- [TechCrunch: Lyft to Buy FreeNow for $197M](https://techcrunch.com/2025/04/16/lyft-to-buy-taxi-app-freenow-for-197m-to-enter-europe/)
- [Lyft Blog: Expanding to Nova Scotia and Saskatchewan](https://www.lyft.com/blog/posts/lyft-is-arriving-in-nova-scotia-and-saskatchewan)
- [FreeNow: Payment Methods](https://support.free-now.com/hc/en-gb/articles/22331201929234-What-payment-methods-are-available-and-how-do-I-set-them-up)
- [Lyft Help: How to Add Payment Info](https://help.lyft.com/hc/en-us/all/articles/115013080408-How-to-add-or-update-payment-info)
- [Lyft Help: Express Pay](https://help.lyft.com/hc/en-us/all/articles/115012923167-Express-Pay)
- [Lyft Blog: Cash Payment Option](https://www.lyft.com/blog/posts/a-new-payment-option-for-the-millions-of-people-who-are-cash-preferred)
- [YouTube: How to Fix Payment Failed on Lyft 2025](https://www.youtube.com/watch?v=I1nAvaGFGtY)
- [YouTube: Resolve Repeated Payment Declines on Lyft 2026](https://www.youtube.com/watch?v=9GTHSio56Xo)
- [Business of Apps: Lyft Statistics 2026](https://www.businessofapps.com/data/lyft-statistics/)
- [Seeking Alpha: Lyft Scaling Up Globally](https://seekingalpha.com/article/4824141-lyft-scaling-up-globally)
- [Motley Fool: What Lyft Needs to Prove in 2026](https://www.fool.com/investing/2025/12/13/what-lyft-needs-to-prove-in-2026/)
- [Paylosophy: Payment Gateways for Uber/Airbnb/Lyft](https://paylosophy.com/payment-gateways-companies-like-airbnb-uber-use/)
- [Lyft Executive Team](https://investor.lyft.com/company-information/executive-team)
