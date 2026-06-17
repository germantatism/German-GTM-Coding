# FOX CORPORATION | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Fox Corporation
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/2/21/FOX_wordmark.svg
Nombre merchant: Fox Corporation

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: DTC Subscription Friction
Tittle_Pain Point_2: No Google Pay on Fox One
Tittle_Pain Point_3: Tubi Intl Ad Monetization
Tittle_Pain Point_4: Platform Billing Dependency
Tittle_Pain Point_5: FanDuel Option Complexity

Desc_Pain Point_1: Fox One only accepts cards, PayPal, Apple Pay. No BNPL, no local APMs for international viewers. Every abandoned checkout is a lost $240/yr subscriber.
Desc_Pain Point_2: Fox One has Apple Pay but no Google Pay, excluding Android's 75%+ global share. Users must type card details manually, adding friction at conversion.
Desc_Pain Point_3: Tubi has 100M+ MAU across 12 countries. Ad revenue hit $1.1B but intl programmatic yield lags US with no local billing in GBP, AUD, CAD, or MXN.
Desc_Pain Point_4: Fox Nation on Amazon, Roku, Apple pays 15-30% platform fees on $8.99/mo subs. DTC billing avoids the cut but has too few payment options.
Desc_Pain Point_5: Fox holds 18.6% FanDuel call option (~$4.5B, Dec 2030). If exercised, Fox enters iGaming requiring multi-state deposit/withdrawal rails it lacks.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Cards (Visa/MC/Amex/Discover)
PSP_2: PayPal
PSP_3: Apple Pay
PSP_4: Apple/Google/Amazon/Roku (IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Google Pay
Local_M_2: BLIK
Local_M_3: iDEAL
Local_M_4: OXXO
Local_M_5: Open Banking (UK)
Local_M_6: Interac
Local_M_7: Boleto
Local_M_8: SEPA Direct Debit
Local_M_9: Pix
Local_M_10: POLi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route Fox One ($19.99/mo) and Fox Nation ($8.99/mo) subscription payments through the best acquirer per card BIN and market. A 3% auth uplift across millions of subscribers recovers significant recurring revenue and reduces involuntary churn.
Desc_Yuno_Cap2: Automatic cascade eliminates checkout failures for live-event subscribers. When the acquirer declines a Fox One renewal during NFL Sunday, Yuno reroutes in milliseconds, protecting the subscription. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activates the APMs Fox needs for global DTC growth: Google Pay for Android majority, Open Banking for UK Tubi monetization, Interac for Canadian subscribers, OXXO for Mexican viewers, Pix for LatAm expansion. One API, 1,000+ payment methods, zero per-market engineering builds.
Desc_Yuno_Cap4: One dashboard replacing Fox's fragmented billing across DTC, Amazon, Roku, Apple, Google Play. Real-time subscription analytics, centralized reconciliation, NOVA fraud engine with 75% fewer false positives on recurring payments.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Fox Corporation at a glance:**
- Revenue: $16.3B FY2025 (+16.6% YoY); Q2 FY2026 at $5.18B
- Segments: Television ($10.1B), Cable Networks ($5.7B), Tubi ($1.1B+ annual), Fox One (launched Aug 2025)
- Tubi: 100M+ MAU (June 2025), first profitable quarter in Q1 FY2026, 27% revenue growth YoY
- Fox One: $19.99/mo or $199.99/yr, DTC streaming with live Fox News, Fox Sports, Fox Business, entertainment
- Fox Nation: $8.99/mo or $71.88/yr, also available as Amazon Prime Video channel (Feb 2026)
- FanDuel: Fox holds 18.6% call option (~$4.5B strike, exercisable by Dec 2030) plus 2.4% Flutter equity (~4.3M shares)
- CEO: Lachlan K. Murdoch (Executive Chair & CEO)
- COO/President: John P. Nallen
- Tubi Media Group CEO: Paul Cheesbrough (former Fox CTO)
- Tubi CPTO: Mike Bidgoli (Chief Product & Technology Officer, appointed May 2024)
- No dedicated VP/Head of Payments identified at the corporate level

**Confirmed PSPs / Billing:**
- Fox One DTC: Visa, Mastercard, Amex, Discover, PayPal, Apple Pay (confirmed via help.fox.com)
- Fox Nation DTC: same card brands + PayPal
- Fox Nation via Amazon Prime Video: billed through Amazon
- Fox One via Verizon: bundled as a perk with select plans
- Tubi: free / no consumer billing (100% ad-supported AVOD)
- IAP channels: Apple App Store, Google Play, Roku, Amazon Fire TV
- No payment orchestrator detected
- Underlying PSP vendor not publicly disclosed (Fox One built on Tubi Media Group tech stack)

**Top Market Gap Analysis:**

MARKET 1: United States (primary, all services)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay
  Missing: Google Pay, Cash App Pay, Venmo
  Note: No Google Pay on Fox One is a significant gap for Android-majority cord-cutters

MARKET 2: United Kingdom (Tubi active, 40K+ titles)
  Accepted: Cards (via app stores)
  Missing: Open Banking (Pay by Bank), Klarna UK, Google Pay direct
  Note: UK Open Banking adoption surging; Tubi launched UK but no DTC subscription billing there yet

MARKET 3: Canada (Tubi active, Bell Media partnership Oct 2025)
  Accepted: Cards (via app stores)
  Missing: Interac Online, Interac e-Transfer
  Note: Interac dominates Canadian digital payments; critical if Fox One launches in Canada

MARKET 4: Mexico (Tubi active via TV Azteca partnership)
  Accepted: Cards (via app stores)
  Missing: OXXO, SPEI, CoDi, Mercado Pago
  Note: Mexico is Tubi's first LatAm market; 70%+ adults lack credit cards

MARKET 5: Australia (Tubi active since 2019)
  Accepted: Cards (via app stores)
  Missing: POLi, Afterpay AU, BPAY
  Note: Australia is one of Tubi's fastest-growing international markets

**Billing Issues (Fox Nation / Fox One):**
- PissedConsumer: 3,500+ reviews with top complaints being billing issues and poor customer service
- Users report unexpected annual charges when signed up for monthly plans
- Renewal price increases without notification
- Chatbot-only support for billing disputes
- BBB complaints document recurring charge issues and failed cancellations

**Key Meeting Angles:**
1. **Fox One is brand new** | Launched Aug 2025, still building DTC billing infrastructure. Early-stage = low switching cost for orchestration
2. **Tubi monetization upside** | 100M+ MAU generating $1.1B in ads, but advertiser billing in local currencies (GBP, AUD, CAD, MXN) could lift international CPMs
3. **Android gap** | No Google Pay on Fox One excludes the majority of global smartphone users from frictionless checkout
4. **Platform fee arbitrage** | Every Fox Nation subscriber on Amazon/Roku/Apple costs Fox 15-30% in fees. DTC with better APMs reduces that
5. **FanDuel option** | If Fox exercises the 18.6% stake, it enters iGaming payments needing multi-state deposit/withdrawal rails
6. **CPTO has product DNA** | Mike Bidgoli (Tubi CPTO) and Paul Cheesbrough (Tubi Media Group CEO, ex-Fox CTO) are the tech decision-makers
7. **Cord-cutter urgency** | Fox One targets cord-cutters at $20/mo; checkout friction at signup is the single biggest conversion killer

**Sources:**
- [Fox One Payment Methods (help.fox.com)](https://help.fox.com/s/article/What-payment-methods-can-I-use-on-Fox-One)
- [Fox One Billing & Payments FAQ](https://help.fox.com/s/article/Billing-Payments-Discounts-FOX-One-FOX-Nation)
- [Fox Nation Billing & Payment](https://help.fox.com/s/topic/0TO1H000000HHcrWAG/fox-nation-billing-payment)
- [Fox Corporation Executive Team](https://www.foxcorporation.com/management/executive-team/)
- [Fox Corporation Revenue Q2 FY2026](https://thedesk.net/2026/02/fox-fiscal-q1-2026-earnings-report/)
- [Fox Corp Revenue $5.18B (TV News Check)](https://tvnewscheck.com/business/article/fox-corp-revenue-hits-5-18-billion-on-sports-tubi-gains/)
- [Tubi Profitability (The Wrap)](https://www.thewrap.com/fox-corporation-earnings-q1-2026/)
- [Tubi 100M MAU (ppc.land)](https://ppc.land/tubi-surpasses-100-million-users-amid-streaming-advertising-boom/)
- [Tubi Statistics 2026 (Business of Apps)](https://www.businessofapps.com/data/tubi-statistics/)
- [Fox One Launch (Deadline)](https://deadline.com/2025/08/fox-corp-launches-fox-one-streaming-1236486461/)
- [Fox One Wikipedia](https://en.wikipedia.org/wiki/Fox_One)
- [Fox One on Amazon Prime Video](https://www.aboutamazon.com/news/entertainment/fox-one-news-sports-entertainment-prime-video-subscription)
- [Fox Nation on Amazon Prime Video](https://nation.foxnews.com/)
- [Tubi UK Expansion (StreamTV Insider)](https://www.streamtvinsider.com/video/foxs-tubi-eyes-uk-expansion-hires-david-salmon-lead-international-efforts)
- [Tubi LatAm Expansion (TechCrunch)](https://techcrunch.com/2022/08/11/fox-owned-tubi-expands-its-free-streaming-service-to-five-latin-american-countries/)
- [Tubi CPTO Mike Bidgoli Appointment](https://corporate.tubitv.com/press/tubi-appoints-mike-bidgoli-as-chief-product-technology-officer/)
- [Fox Tubi Media Group (NextTV)](https://www.nexttv.com/news/fox-forms-tubi-media-group-puts-cto-paul-cheesbrough-in-charge-of-new-digital-unit)
- [Fox FanDuel Option (Covers)](https://www.covers.com/industry/fox-ownership-option-continues-to-loom-over-fanduel-april-2-2026)
- [Fox FanDuel Stake (Sportico)](https://www.sportico.com/business/sales/2025/flutter-purchase-fanduel-stake-value-cost-1234861636/)
- [Fox BBB Complaints](https://www.bbb.org/us/ny/new-york/profile/tv-stations/fox-corporation-0121-7020/complaints)
- [Fox Nation PissedConsumer](https://fox-nation.pissedconsumer.com/review.html)
- [FOX Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:FOX_wordmark.svg)
- [Fox Programmatic Advertising](https://www.foxadvertising.com/programmatic/)
- [Fox FY2025 Earnings (SEC)](https://www.sec.gov/Archives/edgar/data/1754301/000162828025037611/foxq42025earningsrelease.htm)
