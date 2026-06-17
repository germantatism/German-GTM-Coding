# QUIZLET | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Quizlet
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/c/c8/Quizlet_Logo_2021.svg
Nombre merchant: Quizlet

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Zero Local APMs Globally
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: App Store Fee Drain
Tittle_Pain Point_4: Single PSP Exposure
Tittle_Pain Point_5: Student Payment Barrier

Desc_Pain Point_1: 60M+ MAU across 130 countries with only cards on web. No Pix, no UPI, no BLIK, no SEPA DD. Students in markets with sub-30% card penetration cannot pay.
Desc_Pain Point_2: $139M ARR processed cross-border from US to 130+ countries. International cards face higher declines from cross-border flags, 3DS friction, and issuer blocks.
Desc_Pain Point_3: Quizlet Plus subscriptions flow through Apple/Google at 15-30% commission. No local APMs on web to pull direct purchases; millions in store fees lost.
Desc_Pain Point_4: No multi-PSP setup detected. A single processor handling $139M ARR across 130 countries creates concentration risk; any outage blocks all revenue.
Desc_Pain Point_5: K-12 and college students use prepaid cards, low-limit debit, or family accounts. Card-only checkout creates friction for a demographic with limited banking.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed Card Processor
PSP_2: Apple App Store
PSP_3: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: BLIK
Local_M_4: SEPA Direct Debit
Local_M_5: iDEAL
Local_M_6: Boleto
Local_M_7: OXXO
Local_M_8: Konbini
Local_M_9: GCash
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge to the highest performing acquirer per card BIN, issuer, and market. With $139M ARR and 60M+ MAU across 130 countries, even a 3% auth uplift translates to $4M+ in recovered annual revenue without touching a single line of product code.
Desc_Yuno_Cap2: When a Quizlet Plus renewal fails on the primary processor, Yuno cascades to the next best acquirer in milliseconds. Recovers up to 50% of soft declines, directly converting failed renewals into retained student subscriptions with zero checkout friction.
Desc_Yuno_Cap3: Unlocks APMs for Quizlet's global student base: Pix in Brazil, UPI in India, BLIK in Poland, SEPA DD across Europe, iDEAL in Netherlands, Konbini in Japan, OXXO in Mexico. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating the card processor, Apple IAP, Google Play, and any future PSPs into one view. Real-time auth rate monitoring per country and plan tier, centralized reconciliation, millisecond anomaly detection via NOVA across 130 countries.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Quizlet at a glance:**
- Founded: 2005 by Andrew Sutherland; publicly launched January 17, 2007
- CEO: Kurt Beidler (appointed July 2024; formerly co-CEO of Zwift)
- Previous CEOs: Matt Glotzbach (2016-2022), Lex Bayer (2022-2024)
- HQ: San Francisco, California; additional office in Denver, Colorado
- Revenue: $139M (2025), up from $80M (2024), 74% YoY growth
- Users: 60M+ monthly active users (2021 figure); 1M+ paying customers
- Study sets: 500M+ user-generated study sets
- Available in: 130 countries, 19 languages
- Employees: ~547 total (138 engineering)
- Valuation: $1B (2020 Series C)
- Funding: $62M total raised (Series C led by General Atlantic, with Union Square Ventures, Costanoa Ventures, Icon Ventures, Owl Ventures)
- Products: Flashcards, Learn mode, Practice Tests, Study Guides, Quizlet Live, Q-Chat (AI tutor, ChatGPT-powered), Course-Powered Quizlet (2025)
- Business model: Freemium (ads + subscriptions)
- Acquisitions: Slader (March 2021), Coconote (February 2026)
- Market penetration: "1 in 2 high school students used Quizlet" (2017)

**Pricing:**
- Quizlet Plus: $7.99/month or $35.99/year
- Quizlet Plus Unlimited: $9.99/month or $44.99/year
- Family Plan: ~$96/year (up to 5 members)
- Teacher Plan: $35.99/year
- Group discounts: 5%+ for 2-9 accounts, higher for larger groups

**Confirmed PSPs:**
- Undisclosed card processor: handles credit/debit card payments on quizlet.com
- Apple App Store: iOS in-app purchases
- Google Play: Android in-app purchases
- Privacy policy references "third-party payment processors" but names no specific company
- Check payments accepted for group orders of 10+ (US banks only)
- No payment orchestrator detected
- No PayPal, no digital wallets, no local APMs on web

**Payment issues documented:**
- BBB complaints about unauthorized charges, especially involving minors
- Users report difficulty canceling subscriptions; "Manage Subscription" option sometimes missing
- Continued billing after cancellation attempts reported
- Payment form rejecting valid credit card information
- Payments won't process despite multiple attempts
- Non-refundable policy except where required by law
- 7-day free trial auto-converts to paid (annual plans only)

**Top Markets Gap Analysis:**

MARKET 1: United States (largest market by traffic)
  Offer: Visa/MC/Amex, check (groups only)
  Missing: ACH Direct Debit, PayPal, Cash App Pay, Venmo, Apple Pay, Google Pay
  #1 market. No digital wallets at all on web. Students heavily use Cash App and Venmo.

MARKET 2: United Kingdom (second largest by traffic)
  Offer: Visa/MC (cross-border from US entity)
  Missing: Open Banking, PayByBank, PayPal
  All UK transactions are cross-border. No local acquiring.

MARKET 3: Poland (third largest by traffic)
  Offer: Visa/MC (cross-border from US entity)
  Missing: BLIK, Przelewy24, PayPal
  BLIK processed 2.5B+ transactions in 2024. 80%+ of Polish online payments use BLIK. Students without international cards cannot pay.

MARKET 4: Brazil (Portuguese content, large student population)
  Offer: Visa/MC (cross-border from US entity)
  Missing: Pix, Boleto, local installments
  Pix handles 70%+ of digital payments. 60M+ students in Brazil. Without Pix, mass adoption is blocked.

MARKET 5: India (19 languages supported, English learning demand)
  Offer: Visa/MC (cross-border from US entity)
  Missing: UPI, RuPay, Paytm, PhonePe
  UPI processes 14B+ transactions/month. 75%+ of Indian digital payments use UPI. Student demographic has near-zero international card access.

**Key meeting angles:**
1. **Student demographic = payment diversity**: K-12 and college students disproportionately lack international credit cards. Local APMs unlock the addressable market.
2. **130 countries, zero local APMs**: Cards-only checkout in 130 countries means Quizlet is leaving conversion on the table in every non-US market.
3. **74% revenue growth demands infrastructure**: $80M to $139M in one year. Payment infrastructure must scale with this trajectory or become a bottleneck.
4. **Poland surprise**: Third-largest traffic market. BLIK is essential and completely absent.
5. **AI investment moment**: Q-Chat (ChatGPT), Course-Powered Quizlet (2025), Coconote acquisition (2026). Heavy product investment; payment infrastructure must match.
6. **App store fee arbitrage**: Local APMs on web pull students to direct channel, avoiding 15-30% Apple/Google commissions.
7. **Competitor precedent**: Duolingo accepts PayPal, Google Pay, and multiple local methods. Quizlet's web checkout is comparatively bare.

**Sources:**
- [Quizlet Privacy Policy](https://quizlet.com/privacy)
- [Quizlet Billing Help](https://help.quizlet.com/hc/en-us/categories/360001598931-Billing)
- [Quizlet Payment Methods Help](https://help.quizlet.com/hc/en-us/sections/360008104172-Payment-methods)
- [Quizlet Subscriptions Help](https://help.quizlet.com/hc/en-us/sections/360004125931-Subscriptions)
- [Quizlet Terms of Service](https://quizlet.com/tos)
- [Quizlet Wikipedia](https://en.wikipedia.org/wiki/Quizlet)
- [Quizlet Revenue (GetLatka)](https://getlatka.com/companies/quizlet)
- [Quizlet BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/social-media-marketing/quizlet-inc-1116-463039/complaints)
- [TechCrunch: Quizlet $1B Valuation](https://techcrunch.com/2020/05/13/quizlet-valued-at-1-billion-as-it-raises-millions-during-a-global-pandemic/)
- [Quizlet Plus Pricing](https://quizlet.com/upgrade)
- [Quizlet Refund Policy](https://help.quizlet.com/hc/en-us/articles/360031214952-Requesting-a-refund-if-you-paid-on-the-website)
- [SimilarWeb: Quizlet Traffic](https://www.similarweb.com/website/quizlet.com/)
- [Semrush: Quizlet Traffic](https://www.semrush.com/website/quizlet.com/overview/)
- [Wikimedia: Quizlet Logo](https://commons.wikimedia.org/wiki/File:Quizlet_Logo_2021.svg)
