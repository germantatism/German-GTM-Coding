# YOUTUBE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: YouTube
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg
Nombre merchant: YouTube

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Walled Garden Lock-In
Tittle_Pain Point_2: Cross-Border Declines
Tittle_Pain Point_3: Card-Only Blind Spots
Tittle_Pain Point_4: Involuntary Churn
Tittle_Pain Point_5: Regional Checkout Gaps

Desc_Pain Point_1: 125M+ subscribers route through Google's proprietary stack with zero failover. One outage blocks all renewals, Super Chats, and memberships globally.
Desc_Pain Point_2: Country-match billing since Sept 2025 rejects foreign cards. Users in Turkey, Pakistan, Kenya face "OR-RECR-05" errors, losing converted subs.
Desc_Pain Point_3: 100+ countries served, most accept only Visa/MC. No Pix for Brazil, no UPI for India, no BLIK for Poland, no GCash for Philippines. Billions excluded.
Desc_Pain Point_4: Streaming churn hits 40% annually. YouTube gives 3 days to fix a failed renewal before pausing. No intelligent retry routing or APM fallback to recover.
Desc_Pain Point_5: Premium Lite launched in 22+ countries but payment rails lag. Nigeria, Ghana, Romania lack local checkout methods, capping subscriber growth.

SLIDE 1: PSP TOPOLOGY

PSP_1: Google Payments (in-house)
PSP_2: Apple App Store (iOS IAP)
PSP_3: Google Play Billing (Android IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: GCash
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: OXXO
Local_M_7: KakaoPay
Local_M_8: Maya
Local_M_9: DANA
Local_M_10: OVO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $19.6B subscription revenue and 125M+ paid subs, routing each renewal to the best acquirer per market delivers 3-10% auth uplift, translating to hundreds of millions in recovered revenue.
Desc_Yuno_Cap2: Automatic cascade across acquirers when Google's internal stack declines a renewal. Instead of pausing a subscriber after one failure, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions eliminates involuntary churn at scale.
Desc_Yuno_Cap3: Activates the local rails YouTube's global footprint demands: Pix in Brazil, UPI in India, GCash in Philippines, BLIK in Poland, OXXO in Mexico, KakaoPay in South Korea, DANA/OVO in Indonesia. One API, 1,000+ payment methods. No market-by-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying Google's fragmented billing across web Premium, YouTube TV, Super Chat, memberships, and mobile IAP reconciliation. Real-time approval rate monitoring per market, centralized settlement, and millisecond anomaly detection via NOVA (75% fraud reduction).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**YouTube at a glance:**
- Parent company: Alphabet (Google). YouTube is the #2 website globally
- 2.7B+ monthly active users across 100+ countries (2025)
- Total YouTube revenue: $62.3B (2025), surpassing Disney for the first time
- Subscription revenue (Premium + Music + TV): $19.64B in 2025
- YouTube Premium/Music subscribers: 125M+ paid subscribers (March 2025), up from 100M in Feb 2024
- YouTube TV: ~11M subscribers (Q3 2025), projected to be the largest US pay-TV provider by end of 2026
- YouTube TV revenue projected at $10-11B in 2026
- MoffettNathanson projects combined YouTube ad + subscription revenue to exceed $75B by 2027
- Revenue streams: Ad revenue ($40.36B), Premium/Music subs, YouTube TV, Super Chat (30% take rate), channel memberships, YouTube Shopping

**Confirmed PSPs:**
- Google Payments (in-house): processes all web/desktop Premium, YouTube TV, Super Chat, and membership transactions through Google's proprietary payments infrastructure (Google Payments Center)
- Apple App Store: iOS in-app purchases (15-30% commission)
- Google Play Billing: Android in-app purchases; alternative billing now permitted in US (Oct 2025) and EEA
- No third-party payment orchestrator detected
- No external acquiring partner publicly identified; Google processes internally

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market)
  Accepted: Visa/MC/Amex/Discover, PayPal, Google Pay, Apple Pay
  Missing: ACH Direct Debit, Cash App Pay, Venmo (standalone)
  Note: YouTube TV ($72.99/mo) is US-only and represents $10B+ revenue. Alternative billing now permitted on Android.

MARKET 2: India (#2 YouTube market, 500M+ users)
  Accepted: Visa/MC (locally issued), Google Play balance
  Missing: UPI, RuPay, Paytm, PhonePe, NetBanking
  Note: India requires locally issued payment methods. UPI handles 75%+ of digital payments. Massive subscriber conversion opportunity blocked by card-only checkout.

MARKET 3: Brazil (#3 YouTube market, 150M+ users)
  Accepted: Visa/MC (locally issued), Google Play balance
  Missing: Pix, Boleto, local installment cards
  Note: Pix processes 70%+ of digital payments in Brazil. YouTube Premium Lite launched but without Pix, most Brazilians cannot subscribe via web.

MARKET 4: Indonesia (#4 YouTube market)
  Accepted: Visa/MC, Google Play balance
  Missing: GoPay, DANA, OVO, ShopeePay, QRIS
  Note: Credit card penetration below 5%. Without e-wallets, the vast majority of Indonesian users cannot pay for Premium.

MARKET 5: Philippines
  Accepted: Visa/MC, Google Play balance
  Missing: GCash, Maya, GrabPay
  Note: Credit card penetration ~6%. GCash has 60M+ users. Mobile wallets are the dominant payment method.

**Key policy changes (2025-2026):**
- Sept 2025: YouTube enforced regional restriction clause requiring Premium access mainly from sign-up country
- Oct 2025: Google Play opened alternative billing in the US (Epic Games ruling)
- YouTube Premium Lite ($7.99/mo, ad-free only) expanded to 22+ countries
- YouTube aggressively cancelling subscriptions with country-mismatched billing

**Pain point evidence:**
- "OR-RECR-05" error code is widespread for cross-border payment failures
- Users get only 3-day grace period on failed renewals before pause, 30 days before full cancellation
- Industry streaming churn rate is 40% annually; involuntary churn (payment failures) is a major contributor
- Forum posts document widespread frustration with payment declines across emerging markets
- YouTube Premium payment declines "are rarely about insufficient funds" but rather "card structure, BIN reputation, and recurring billing compatibility" issues

**Key meeting angles:**
1. **Scale of opportunity** | $19.6B subscription revenue with 125M+ paid subs. Even 1% auth improvement = $196M
2. **125M to 250M subscriber path** | Growth comes from emerging markets (India, Brazil, Indonesia, Philippines) where card-only checkout blocks conversion
3. **YouTube TV dominance** | Becoming #1 US pay-TV provider with $10B+ revenue demands payment resilience
4. **Involuntary churn** | 40% industry churn rate with a 3-day grace window. Smart retry routing can save millions of subscriptions
5. **Alternative billing unlocked** | US/EEA alternative billing opens the door to third-party orchestration on mobile
6. **Super Chat/Membership monetization** | Creator economy payments (30% take rate) depend on global payment coverage
7. **Competitor precedent** | Spotify uses Adyen multi-PSP orchestration; Netflix uses multiple acquirers globally

**Sources:**
- [YouTube Help: Accepted Payment Methods](https://support.google.com/youtube/answer/10239146?hl=en)
- [YouTube Premium Restrictions](https://www.youtube.com/premium/restrictions)
- [YouTube Premium Available Locations](https://support.google.com/youtube/answer/6307365?hl=en)
- [YouTube Help: Fix Billing Issues](https://support.google.com/youtube/answer/9972274?hl=en)
- [YouTube Help: Failed/Declined Payments](https://support.google.com/youtube/answer/9971664?hl=en)
- [Google Payments Center](https://support.google.com/paymentscenter/answer/9003590?hl=en)
- [Google Play Alternative Billing APIs](https://developer.android.com/google/play/billing/alternative)
- [Business of Apps: YouTube Statistics 2026](https://www.businessofapps.com/data/youtube-statistics/)
- [DemandSage: YouTube Stats 2026](https://www.demandsage.com/youtube-stats/)
- [Accio: YouTube Premium 125M Subscribers](https://www.accio.com/business/trend-of-youtube-premium-1-year)
- [MediaPost: YouTube TV Biggest Pay TV Provider 2026](https://www.mediapost.com/publications/article/394793/)
- [Cord Cutters News: YouTube TV Q3 2025](https://cordcuttersnews.com/youtube-tv-added-750000-subscribers-in-the-3rd-quarter-of-2025-according-to-a-new-report/)
- [BUVEI: YouTube Premium Payment Declines 2026](https://buvei.com/blog/why-youtube-premium-payments-get-declined-virtual-card-fixes-that-work-in-2026/)
- [Churnkey: Streaming Churn Rates](https://churnkey.co/blog/churn-rates-for-streaming-services/)
- [YouTube Brand Resources](https://www.youtube.com/howyoutubeworks/resources/brand-resources/)
