# LIFE360 | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Life360
=======================================

Logo: https://companieslogo.com/img/orig/LIF-6048e0bc.png
Nombre merchant: Life360

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 7 Day Grace Period Risk
Tittle_Pain Point_2: App Store Revenue Leakage
Tittle_Pain Point_3: No Local Payment Rails
Tittle_Pain Point_4: Brazil Growth, No PIX
Tittle_Pain Point_5: Hardware + Sub Split Billing

Desc_Pain Point_1: Life360 gives subscribers only 7 days to update billing after a card decline before terminating the subscription. With 2.8M paying circles at $7.99 to $24.99 per month, each terminated subscription is lost recurring revenue. No automatic failover to an alternative payment method or acquirer exists during this grace window.
Desc_Pain Point_2: Life360 subscriptions are split across Apple App Store, Google Play, and direct web billing. App store channels take 15 to 30% commission on every subscription dollar. With $489.5M revenue (58% US subscription + 12% international subscription), migrating even 10% of app store subscribers to direct billing recovers millions.
Desc_Pain Point_3: Life360 operates in 180+ countries with 95.8M MAU. Subscription checkout accepts only credit/debit cards and app store payments. No SEPA for EU, no iDEAL for Netherlands, no BLIK for Poland, no UPI for India, no Boleto for Brazil. International subscription revenue is only 12% of total despite global user reach.
Desc_Pain Point_4: Brazil is Life360's second largest international market at 3.95% of users. PIX has 150M+ active users and processes more digital payments than cards in Brazil. Life360 does not accept PIX for subscriptions. Converting free Brazilian MAU to paid circles requires the dominant local payment method.
Desc_Pain Point_5: Life360 sells hardware (Tile trackers, Jiobit GPS) plus software subscriptions across separate billing systems. Hardware revenue is 11% of total ($53.8M). Tile Premium and Life360 Gold/Platinum have different payment flows. No unified payment orchestration across hardware purchases and subscription renewals.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple App Store (iOS) PSP_2: Google Play Store (Android) PSP_3: Direct Web Billing (Credit/Debit Cards) PSP_4: Third-party Payment Processor (unconfirmed)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BLIK (Poland)
Local_M_6: Boleto (Brazil)
Local_M_7: Bancontact (Belgium)
Local_M_8: PayPay (Japan)
Local_M_9: KakaoPay (South Korea)
Local_M_10: MB Way (Portugal)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Gold, Platinum, and Tile Premium renewal to the optimal acquirer per card BIN, issuer, and market. With $489.5M revenue and 2.8M paying circles, even a 0.5% auth improvement recovers meaningful subscription revenue. Smart Routing boosts approval rates 3 to 10% across all direct billing channels.
Desc_Yuno_Cap2: When a card renewal fails, Yuno cascades instantly to an alternative acquirer or payment method before the 7 day grace period expires. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this approach. Each recovered subscription protects $96 to $300 in annual revenue per circle.
Desc_Yuno_Cap3: Activate PIX in Brazil (3.95% of users), SEPA in EU, UPI in India, iDEAL in Netherlands, and BLIK in Poland. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months with Yuno. Life360 could convert free international MAU to paying circles by accepting how they actually pay.
Desc_Yuno_Cap4: Unify hardware sales (Tile, Jiobit) and subscription billing (Gold, Platinum, Tile Premium) into one real time dashboard. Monitor approval rates across direct web, app store bypass, and international markets. Track the 7 day grace window recovery rate. Millisecond anomaly detection catches decline spikes before they cascade.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Life360 at a glance:**
- Founded: 2008. HQ: San Francisco, California
- Public: Nasdaq (LIF) and ASX (360). Dual listed
- FY2025 Revenue: $489.5M (up 32% YoY). First full year profitability in company history
- FY2025 Net Income: $150.8M ($32M+ excluding one time non cash tax benefit)
- FY2025 Adjusted EBITDA: $93.2M (19% margin)
- AMR (Annualized Monthly Revenue): $478.0M (up 30% YoY as of Dec 31, 2025)
- MAU: 95.8M (up 20% YoY as of Dec 31, 2025)
- Paying Circles: 2.8M (record 576K net additions in 2025)
- Active Devices: 10.8M monthly active Tile devices
- Revenue Mix FY2025: US subscription 58%, International subscription 12%, Hardware subscription 5%, Other revenue (data/advertising) 14%, Hardware sales 11%
- 2026 Guidance: Adjusted EBITDA $128M to $138M (~20% margin). Long term targets: 150M MAU, $1B+ revenue, 35% EBITDA margin
- Markets: 180+ countries. US 60.24%, Brazil 3.95%, UK 3.54%, Australia 2.93%, Mexico 2.54%
- Products: Life360 app (family location, safety), Tile (Bluetooth trackers), Jiobit (GPS devices), advertising/data partnerships

**Confirmed PSPs and Payment Infrastructure:**
- Apple App Store: Primary subscription channel for iOS users. Apple handles billing and takes 15 to 30% commission
- Google Play Store: Primary subscription channel for Android users. Google handles billing
- Direct Web Billing: Available at life360.com. Accepts major credit and debit cards
- Third-Party Payment Processor: Terms of service reference a third party payment processor but do not name it
- Tile hardware purchases: Sold through life360.com/tile and retail (27,000+ stores)
- No payment orchestration platform confirmed
- No PayPal, no digital wallets (beyond app store), no local payment methods confirmed for direct billing

**Pricing Structure:**
- Free: Basic location sharing, 2 day location history
- Silver: $7.99/month
- Gold: $14.99/month ($99.99/year). 30 day location history, Driver Reports, Emergency Dispatch, ID Theft Protection
- Platinum: $24.99/month ($199.99/year). Tile Starter Pack, credit monitoring, towing, stolen funds reimbursement up to $1M
- Tile Premium: Separate subscription for extended Tile features
- All paid plans include 7 day free trial

**Payment Issues and Incidents:**
- 7 day grace period: If Life360 cannot charge the card on file, subscriber has only 7 days to update billing before subscription termination. No automatic retry to alternative methods
- App store billing fragmentation: Subscribers who signed up via iOS must manage billing through Apple. Those via Android through Google Play. Those via web through Life360.com. Creates confusion and limits payment method flexibility
- Card update errors: Users report app glitches when trying to update payment methods. Support suggests clearing cache or reinstalling the app
- Refund complaints: BBB and complaint boards show recurring unauthorized charge issues and difficulty canceling subscriptions
- No fallback payment: When a card fails, no alternative payment method (PayPal, bank debit, local method) is offered during the 7 day grace window

**Key meeting angles:**
1. **$489.5M revenue, 12% international despite 40% international MAU** | 40% of Life360's 95.8M MAU are outside the US, but international subscription revenue is only 12% of total. The gap between free international users and paying circles is a conversion problem. Local payment methods are the unlock: PIX in Brazil, SEPA in EU, UPI in India.
2. **2.8M paying circles with a 7 day cliff** | When a card declines, Life360 gives subscribers just 7 days before termination. No failover to an alternative acquirer, no cascade to a backup payment method. NOVA AI recovers up to 75% of soft declines instantly. Each saved circle protects $96 to $300 in annual subscription revenue.
3. **App store bypass opportunity** | Apple and Google take 15 to 30% of every subscription dollar. With US subscription at 58% of $489.5M ($284M), even shifting 10% to direct billing through Yuno saves $4M to $8.5M annually. Yuno enables direct web checkout with 1,000+ APMs, reducing app store dependency.
4. **Brazil: 3.8M MAU, zero local payments** | Brazil is Life360's second largest international market. PIX dominates digital payments with 150M+ users. Life360 cannot accept PIX for subscriptions. Yuno activates PIX, Boleto, and local Brazilian methods through one API. Converting even 5% of Brazilian free users to paid circles at $99.99/year adds meaningful ARR.
5. **Hardware + subscription convergence** | Tile hardware, Jiobit GPS, and Life360 subscriptions run on separate billing rails. As Life360 launches GPS pet trackers and elder care devices in 2025 to 2026, unified payment orchestration becomes essential. Yuno provides one dashboard for hardware commerce and subscription renewal across all regions.

**Life360 Leadership:**
- Lauren Antonoff: CEO (promoted from COO). Joined Life360 in 2023. Oversees product, design, engineering, sales, marketing, CX
- Chris Hulls: Co-Founder and Executive Chairman. Led company as CEO for ~20 years
- Justin Moore: CTO. Leads engineering strategy, infrastructure, and innovation
- Mike Zeman: CMO. Leads business and brand growth globally
- Heather Houston: Chief People Officer
- No dedicated VP of Payments or Billing identified in public sources

**Recent corporate developments:**
- March 2026: Q4 and FY2025 results. Revenue $489.5M (32% growth). First profitable full year. 95.8M MAU. 2.8M paying circles
- 2026 Guidance: EBITDA $128M to $138M. Long term: 150M MAU, $1B revenue, 35% EBITDA margin
- 2025: Advertising/data revenue surged 90% to $68.4M. Uber partnership for airport ride offers
- 2025: Agreed to acquire Nativo (ad tech) for ~$120M
- 2025: CEO transition from Chris Hulls to Lauren Antonoff
- FY2025: International subscription growth accelerating. ANZ MAU up 28% YoY to 3.2M
- Hardware: New Tile lineup complete. GPS pet tracker (Jiobit) and elder care device planned for 2025 to 2026

**Sources:**
- [Life360 Q4 FY2025 Results (Investors)](https://investors.life360.com/news-releases/news-release-details/life360-reports-record-q4-2025-results)
- [Life360 Q4 FY2025 Results (GlobeNewsWire)](https://www.globenewswire.com/news-release/2026/03/02/3247854/0/en/Life360-Reports-Record-Q4-2025-Results.html)
- [Life360 Q3 2025 Results (Investors)](https://investors.life360.com/news-releases/news-release-details/life360-reports-record-q3-2025-results)
- [Life360 FY25 Slides (Investing.com)](https://www.investing.com/news/company-news/life360-fy25-slides-profitability-milestone-reached-revenue-up-32-93CH-4536516)
- [Life360 $489.5M Revenue (StockTitan)](https://www.stocktitan.net/sec-filings/LIF/ars-life360-inc-sec-filing-58a4355716d0.html)
- [Life360 Data Analysis (LocaChange)](https://www.locachange.com/location-changer/life360-data-analysis/)
- [Life360 Acquires Tile (PRNewswire)](https://www.prnewswire.com/news-releases/life360-to-acquire-tile-creating-the-world-leader-in-finding-and-location-solutions-301430364.html)
- [Life360 Pricing (Life360)](https://www.life360.com/plans-pricing)
- [Life360 Membership Plans (PhoneLocator360)](https://phonelocator360.com/blog/location-trackers-reviews/how-much-does-life-360-cost-pricing-explained)
- [Life360 Update Billing (Support)](https://support.life360.com/hc/en-us/articles/23053412005527-Update-Membership-Billing-Information)
- [Life360 Management (Investors)](https://investors.life360.com/corporate-governance/management)
- [Life360 CEO Transition (Life360 Blog)](https://www.life360.com/blog/life360-ceo-transition-chris-hulls)
- [Life360 Unpacking Growth (BeyondSPX)](https://beyondspx.com/quote/LIFX/life360-unpacking-growth-profitability-and-the-path-to-family-safety-dominance-lifx)
- [Life360 Wikipedia](https://en.wikipedia.org/wiki/Life360)
- [Life360 Logo (CompaniesLogo)](https://companieslogo.com/life360/logo/)
