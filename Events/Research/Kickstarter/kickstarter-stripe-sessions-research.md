# KICKSTARTER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Kickstarter
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/b/b5/Kickstarter_logo.svg
Nombre merchant: Kickstarter

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single PSP Lock-in
Tittle_Pain Point_2: 3-5% Pledge Failure Rate
Tittle_Pain Point_3: Card-Only Global Checkout
Tittle_Pain Point_4: Cross-Border Decline Spike
Tittle_Pain Point_5: Late Pledge Leakage

Desc_Pain Point_1: Kickstarter runs 100% of payment processing through Stripe since 2014. On $9.4B+ in total pledges and record 2025 volume, a single processor means no routing optimization, no failover, and zero leverage on processing fees at scale.
Desc_Pain Point_2: Industry data shows 1-5% of campaign pledges fail at charge time, averaging ~3%. On a $46.7M campaign (eufyMake, largest ever), that is $1.4M+ in lost pledges. Creators have only 7 days to recover failed payments before backers are dropped.
Desc_Pain Point_3: Backers from 24.9M accounts worldwide can only pay with cards and Apple Pay. No Pix (Brazil), no iDEAL (Netherlands), no BLIK (Poland), no Konbini (Japan). Only German backers get SEPA direct debit, and only for German projects under EUR250.
Desc_Pain Point_4: International backers frequently face card declines from issuer fraud algorithms flagging cross-border crowdfunding charges. Stripe Radar blocks some legitimate payments it deems high risk, further increasing the drop rate on global pledges.
Desc_Pain Point_5: Late pledges (post-campaign contributions) grew 30% YoY in 2025 and are a key revenue driver. But the same card-only, single-processor limitations apply, leaving international late-pledge revenue on the table.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole processor since 2014)
PSP_2: Stripe Connect (creator payouts)
PSP_3: Stripe Radar (fraud)
PSP_4: Apple Pay (mobile app)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: iDEAL
Local_M_3: BLIK
Local_M_4: Konbini
Local_M_5: Bancontact
Local_M_6: OXXO
Local_M_7: Giropay
Local_M_8: Boleto
Local_M_9: Line Pay
Local_M_10: PayPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every pledge by BIN, issuer, and geography to the optimal processor. On record-breaking 2025 pledge volume across 25M backers worldwide, a 3-10% auth uplift recovers millions in pledges that currently fail at Stripe-only checkout, directly boosting creator success rates.
Desc_Yuno_Cap2: Automatic cascade catches the 3-5% of pledges that fail at charge time. When Stripe declines a legitimate international backer, Yuno reroutes through an alternative processor in milliseconds instead of waiting 7 days for manual card updates. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates the APMs Kickstarter needs for true global crowdfunding: Pix for Brazil, iDEAL for Netherlands, BLIK for Poland, Konbini for Japan, Bancontact for Belgium, OXXO for Mexico. One API, 1,000+ payment methods, turning card-declined backers into funded pledges.
Desc_Yuno_Cap4: One dashboard layered over Stripe Connect, providing real-time approval monitoring across all creator campaigns and geographies. NOVA fraud engine with 75% fewer false positives replaces Stripe Radar's overly aggressive blocking that currently kills legitimate international pledges.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Kickstarter at a glance:**
- World's premier crowdfunding platform for creative projects, founded April 2009
- Public Benefit Corporation (PBC), headquartered in Brooklyn, NY
- Unionized workforce (Kickstarter United); 4-day workweek; ~376 employees across 6 continents
- 2025: Biggest year in company history (revenue + pledge volume records)
- $9.41B total pledged to date (as of 2026)
- 686,810 projects launched; 292,605 successfully funded (42.74% success rate)
- 24.98M total backers; 8.7M+ repeat backers
- Top categories: Games ($2.85B), Technology ($2.00B), Design ($1.94B)
- Largest campaign ever: eufyMake 3D printer by Anker, $46.7M
- CEO: Everette Taylor (appointed Sept 2022, former CMO at Artsy)
- CTO: Mahesh Guruswamy (20+ years in software, former Head of Engineering at Mosaic)
- Named one of Time Magazine's 100 Most Influential Companies
- Revenue was down 20% YoY when Taylor took over; has grown every year since

**Creator countries supported:**
- Australia, Austria, Belgium, Canada, Denmark, France, Germany, Greece, Hong Kong, Ireland, Italy, Japan, Luxembourg, Mexico, Netherlands, New Zealand, Norway, Poland, Singapore, Slovenia, Spain, Sweden, Switzerland, UK, US

**Confirmed PSPs / Payment Methods:**
- Stripe: Sole payment processor since 2014 (Stripe Payments + Stripe Connect for payouts)
- Stripe Radar: Fraud detection (ML-based)
- Stripe Optimized Checkout Suite: Adopted 2023
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- Apple Pay: Available in Kickstarter iOS app
- SEPA direct debit: Only for German backers pledging to German projects under EUR250
- Google Pay: Not confirmed
- PayPal: NOT accepted
- No payment orchestrator detected

**Payment fee structure:**
- Kickstarter: 5% platform fee on successfully funded projects
- Stripe: ~3-5% variable card processing fee
- Total: ~8-10% of funds raised goes to fees

**Failed payment data:**
- 1-5% of pledges fail at charge time (industry average ~3%)
- Backers get 7 days + email reminders every 48 hours to fix
- Direct outreach recovers ~20-30% of errored backers
- Stripe Radar occasionally blocks legitimate international payments
- Post-campaign pledge managers (BackerKit, CrowdOx) used to recover additional failed payments

**Top Market Gap Analysis:**

MARKET 1: United States (largest backer + creator base)
  Accepted: Cards, Apple Pay
  Missing: Cash App Pay, Venmo, PayPal
  Note: PayPal is explicitly NOT supported despite being the world's largest digital wallet

MARKET 2: Germany (SEPA available, major creator market)
  Accepted: Cards, Apple Pay, SEPA direct debit (limited)
  Missing: Giropay, Klarna DE, full SEPA for all projects
  Note: SEPA only available for German-to-German pledges under EUR250

MARKET 3: Japan (supported creator country)
  Accepted: Cards, Apple Pay
  Missing: Konbini, PayPay, Line Pay, Rakuten Pay
  Note: Japan is a major market for games/tech Kickstarter categories

MARKET 4: Netherlands / Benelux (supported creator countries)
  Accepted: Cards, Apple Pay
  Missing: iDEAL, Bancontact
  Note: iDEAL accounts for 60%+ of Dutch online payments

MARKET 5: Brazil (large backer community, not a creator country)
  Accepted: International cards only
  Missing: Pix, Boleto
  Note: Brazilian backers face high cross-border decline rates

**Key Meeting Angles:**
1. **Record year, record leakage** | 2025 was Kickstarter's biggest year ever, but 3-5% of pledges still fail. On $9.4B+ cumulative, that is hundreds of millions in lifetime lost pledges
2. **Stripe sole dependency** | 100% of processing runs through Stripe since 2014 with zero failover or routing optimization
3. **25M backers, card-only** | Nearly 25M backers worldwide but checkout offers only cards + Apple Pay. Missing local methods for every non-US market
4. **CTO understands platform scale** | Mahesh Guruswamy has 20+ years in software engineering; will grasp orchestration architecture immediately
5. **Late pledges growth** | 30% YoY growth on post-campaign pledges, but same payment limitations apply to this high-margin revenue stream
6. **PayPal gap is strategic** | Kickstarter explicitly does not accept PayPal, the world's largest digital wallet. Orchestration could enable it alongside cards
7. **PBC mission alignment** | As a Public Benefit Corporation, improving global payment access directly serves Kickstarter's mission to help creators everywhere

**Sources:**
- [Kickstarter Fees (Help Center)](https://help.kickstarter.com/hc/en-us/articles/115005028634-What-are-the-fees)
- [Kickstarter Payment Methods (Help Center)](https://help.kickstarter.com/hc/en-us/articles/115005066433-What-forms-of-payment-can-I-use-to-make-a-pledge)
- [Kickstarter x Stripe Case Study](https://stripe.com/customers/kickstarter)
- [Kickstarter Adopts Stripe (Stonemaier Games)](https://stonemaiergames.com/kickstarter-adopts-stripe-payment-system-what-does-this-mean-for-creators-and-backers/)
- [Kickstarter Apple Pay Announcement](https://www.kickstarter.com/blog/introducing-apple-pay-to-the-kickstarter-app)
- [Kickstarter Making Payments Easier Blog](https://www.kickstarter.com/blog/making-payments-easier-for-creators-and-backers)
- [Kickstarter Wikipedia](https://en.wikipedia.org/wiki/Kickstarter)
- [Kickstarter Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Kickstarter_logo.svg)
- [Kickstarter Stats 2026 (SearchLogistics)](https://www.searchlogistics.com/learn/statistics/kickstarter-stats-facts/)
- [Kickstarter Statistics (ExpandedRamblings)](https://expandedramblings.com/index.php/kickstarter-statistics/)
- [Kickstarter Biggest Year (Entrepreneur)](https://www.entrepreneur.com/leadership/kickstarter-was-in-decline-then-it-had-its-biggest-year/502023)
- [Everette Taylor 2025 Record Year (Threads)](https://www.threads.com/@everette/post/DTAwHKiEbaJ/)
- [Everette Taylor CEO Announcement](https://www.kickstarter.com/blog/announcing-kickstarters-new-ceo-everette-taylor)
- [Mahesh Guruswamy CTO Announcement](https://updates.kickstarter.com/mahesh-guruswamy-kickstarters-new-cto/)
- [Kickstarter Fees Guide (Creators)](https://updates.kickstarter.com/kickstarter-fees-a-comprehensive-guide-for-creators/)
- [Failed Payments Recovery (BackerKit)](https://www.backerkit.com/blog/guides/post-campaign-guide/dealing-with-failed-payments/)
- [Failed Credit Cards Recovery (LaunchBoom)](https://www.launchboom.com/blog/failed-credit-cards-on-kickstarter-and-how-to-fix-them-a70b592d79ca/)
- [Kickstarter Payment Methods Guide (PhotonPay)](https://www.photonpay.com/hk/blog/article/kickstarter-payment-methods?lang=en)
- [Kickstarter Crunchbase](https://www.crunchbase.com/organization/kickstarter)
- [Everette Taylor (Semafor Interview)](https://www.semafor.com/article/04/23/2025/i-dont-know-any-ceos-like-me-five-questions-for-kickstarters-everette-taylor)
