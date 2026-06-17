# DUOLINGO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Duolingo
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/2/2e/Duolingo_logo.svg
Nombre merchant: Duolingo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Emerging Market Friction
Tittle_Pain Point_2: Card-Only Web Checkout
Tittle_Pain Point_3: Single Processor Risk
Tittle_Pain Point_4: Involuntary Sub Churn
Tittle_Pain Point_5: IAP Fee Erosion

Desc_Pain Point_1: 58% of revenue from international markets, but emerging market users face card declines. India (16% of downloads), Brazil (8%), Mexico need local APMs.
Desc_Pain Point_2: Web checkout accepts only Visa/MC/Amex, PayPal, and Apple Pay. No Pix, UPI, BLIK, or bank transfers. 133M MAU but card-only web locks out unbanked.
Desc_Pain Point_3: No confirmed failover across processors. Single-acquirer dependency means any outage or decline spike blocks all web subscription activations and renewals.
Desc_Pain Point_4: 12.2M paid subscribers on recurring billing. Failed charges on Super ($84/yr) and Max ($168/yr) drive involuntary churn. 1% gap equals $10M+ lost annually.
Desc_Pain Point_5: 70%+ of subs via Apple/Google IAP at 15-30% commission. Shifting users to web checkout with local APMs could save tens of millions in fees annually.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (web, inferred)
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: BLIK
Local_M_4: Boleto
Local_M_5: OXXO
Local_M_6: SPEI
Local_M_7: GCash
Local_M_8: M-Pesa
Local_M_9: PSE
Local_M_10: Nequi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing optimized by card BIN, issuer, and market. With $1.04B in annual revenue, 12.2M paid subscribers, and 133M MAU, even a 3% auth uplift translates to $31M+ in recovered annual revenue. Each recovered transaction also retains a learner.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor dependency. When a card decline occurs, Yuno reroutes to the next best acquirer in milliseconds, turning failed Super/Max renewals into retained subscribers. Up to 50% recovery on soft declines with zero learner friction.
Desc_Yuno_Cap3: Unlocks the learners Duolingo cannot convert today: Pix in Brazil (8% of downloads), UPI in India (16% of downloads), OXXO in Mexico, M-Pesa in Africa, BLIK in Poland. One API, 1,000+ payment methods. Shifts IAP-heavy users to web checkout, saving 15-30% in fees.
Desc_Yuno_Cap4: One dashboard consolidating Duolingo's web billing, PayPal, Apple IAP, and Google Play revenue streams. Real-time approval rate monitoring by country, centralized reconciliation, and millisecond anomaly detection via Monitors. Full visibility across all channels.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Duolingo at a glance:**
- 133.1M MAU (Q4 2025), 52.7M DAU, 12.2M paid subscribers
- Revenue: $1.04B (FY2025), the company's first billion-dollar year. Total bookings: $1.16B
- NASDAQ: DUOL. Market cap ~$15B
- Founded 2011 by Luis von Ahn and Severin Hacker (Carnegie Mellon). HQ: Pittsburgh, PA
- Plans: Free, Super ($84/yr or $12.99/mo), Max ($168/yr or $22.99/mo), Family ($119.99/yr)
- Local currency pricing in 40+ countries (India ~$13/yr vs US ~$84/yr for Super)
- Revenue: 42% US, 58% international ($436M international in 2024)
- China became second-largest market by DAU in 2025 (5-6% of business)
- DET (Duolingo English Test) generates additional test revenue globally
- 40%+ YoY growth in DAU and revenue through Q3 2025

**Confirmed PSPs:**
- Stripe: likely primary web processor (inferred from checkout flow patterns; not publicly confirmed)
- PayPal: accepted for web subscriptions
- Apple App Store: major subscription channel (iOS, majority of mobile subs)
- Google Play: Android subscription channel (Google Pay, UPI in India)
- No payment orchestrator detected
- No local APMs confirmed on web checkout

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (13% of downloads, 42% of revenue)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: ACH, Cash App, Venmo (direct)
  Note: Primary revenue market. Well served via cards and wallets.

MARKET 2: India (16% of downloads, #1 by downloads)
  Accepted: Google Play (UPI, cards), Apple IAP
  Missing: UPI on web, RuPay, Paytm, PhonePe, net banking (web)
  Note: Duolingo charges ~$13/yr in India vs $84/yr in US. UPI works via Google Play but NOT on web checkout. Massive conversion opportunity on web.

MARKET 3: Brazil (8% of downloads)
  Accepted: Visa/MC (international), Apple/Google IAP
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazil digital payments. Without Pix on web, users are forced into IAP (15-30% commission hit).

MARKET 4: Mexico (major LatAm market)
  Accepted: Visa/MC (international), Apple/Google IAP
  Missing: OXXO, SPEI, CoDi
  Note: 63% unbanked. OXXO processes 5.5M+ daily cash transactions. Without cash methods, unbanked learners cannot subscribe via web.

MARKET 5: China (#2 by DAU, 5-6% of business)
  Accepted: Apple IAP (China), Android stores (Huawei, Xiaomi)
  Missing: Alipay, WeChat Pay (on web)
  Note: Fastest-growing market. 100% IAP dependency means 30% commission on every subscription. Local web checkout would be transformative.

**Payment issues documented:**
- Failed renewals and payment declines frequently reported in support forums and JustAnswer
- Subscription "not recognized" after payment is a known issue
- VPN-based pricing arbitrage is widely documented (users buy from cheaper countries)
- Google Play UPI issues in India (users instructed to update UPI ID)
- Web checkout has fewer payment options than mobile IAP channels

**Key meeting angles:**
1. **$1B revenue, basic payments** | First billion-dollar year but no payment orchestration, no multi-PSP failover
2. **IAP fee arbitrage** | 70%+ of subs through Apple/Google at 15-30% commission. Local web APMs could recapture tens of millions
3. **India #1 by downloads** | 16% of downloads, but UPI only works via Google Play, not web. Web conversion opportunity is enormous
4. **58% international revenue** | Majority of revenue from international markets with minimal local payment coverage
5. **China fastest-growing** | #2 by DAU with 100% IAP dependency. No Alipay/WeChat Pay on web
6. **12.2M paid subs, recurring billing** | Involuntary churn from failed charges is a direct revenue drain at billion-dollar scale
7. **Competitor precedent** | Babbel (multi-PSP, local methods), Rosetta Stone (multi-PSP, enterprise billing)

**Sources:**
- [Duolingo Brand Guidelines (Logos)](https://design.duolingo.com/identity/logos)
- [Duolingo Help: Update Payment Method](https://support.duolingo.com/hc/en-us/articles/4403782693901)
- [Duolingo Investors: Q3 2025 Earnings](https://investors.duolingo.com/news-releases/news-release-details/duolingo-surpasses-50-million-daily-active-users-grows-dau-36)
- [Duolingo Investors: Q1 2025 Shareholder Letter](https://investors.duolingo.com/static-files/01420520-3377-4985-887b-55ed3c1e4fc5)
- [Duolingo 2025 10-K: 130M MAUs](https://www.stocktitan.net/sec-filings/DUOL/ars-duolingo-inc-sec-filing-557c0f359430.html)
- [Business of Apps: Duolingo Statistics 2026](https://www.businessofapps.com/data/duolingo-statistics/)
- [Expanded Ramblings: Duolingo Statistics 2026](https://expandedramblings.com/index.php/duolingo-facts-statistics/)
- [ElectroIQ: Duolingo Statistics 2025](https://electroiq.com/stats/duolingo-statistics/)
- [Duolingo Blog: 2025 Language Report](https://blog.duolingo.com/2025-duolingo-language-report/)
- [Class Central: Duolingo 2025 Review](https://www.classcentral.com/report/duolingo-2025/)
- [TMTPOST: Duolingo Expands in China](https://en.tmtpost.com/post/7707729)
- [CheckThat: Duolingo Pricing 2026](https://checkthat.ai/brands/duolingo/pricing)
- [PureVPN: Get Duolingo Cheaper 2026](https://www.purevpn.com/blog/how-to-get-duolingo-cheaper/)
- [Analyzify: Duolingo Statistics 2025](https://analyzify.com/statsup/duolingo)
