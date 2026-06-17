# DISTROKID | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: DistroKid
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/4/40/Logo_of_DistroKid.svg
Nombre merchant: DistroKid

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Global Card Rejection
Tittle_Pain Point_2: Zero Local APMs
Tittle_Pain Point_3: Single Processor Risk
Tittle_Pain Point_4: Subscription Churn
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: Artists in Africa, India, and LatAm face systematic card declines. Nigerian banks block international recurring charges. India's RBI rejects auto-debits.
Desc_Pain Point_2: Only Visa/MC/Amex/Discover, Apple Pay, and Google Pay accepted. No Pix, UPI, M-Pesa, OXXO, or bank transfers. Card-only checkout locks out unbanked artists.
Desc_Pain Point_3: Single card processor with no failover cascade. Any outage halts activations. Artists whose renewals fail risk music removal from all platforms.
Desc_Pain Point_4: Annual billing means one failed charge can remove an artist's entire catalog. DistroKid warns before takedown, but a single payment failure is catastrophic.
Desc_Pain Point_5: USD-only pricing across all markets. Artists in 150+ countries pay FX conversion fees on every renewal. No local currency pricing to reduce friction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card Processor (undisclosed)
PSP_2: Apple Pay
PSP_3: Google Pay
PSP_4: Tipalti (payouts only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: M-Pesa
Local_M_4: OXXO
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: PSE
Local_M_8: SPEI
Local_M_9: GCash
Local_M_10: Nequi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing optimized by card BIN, issuer, and country. With $97M+ revenue and 2M+ artists paying annual subscriptions, even a 5% auth uplift translates to $4.8M+ in recovered annual revenue and thousands of artists retained.
Desc_Yuno_Cap2: Automatic cascade when the primary processor declines. Yuno reroutes to the next best acquirer in milliseconds, preventing the catastrophic outcome of artists losing their catalog on streaming platforms due to a single failed renewal. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Unlocks the artists DistroKid cannot reach today: Pix in Brazil, UPI in India (where card declines are endemic), M-Pesa in Kenya, OXXO in Mexico, Boleto in Brazil. One API, 1,000+ payment methods. Removes the card-only barrier for the global creator economy.
Desc_Yuno_Cap4: One dashboard consolidating DistroKid's subscription billing and Tipalti payout streams. Real-time approval rate monitoring by country, centralized reconciliation, and millisecond anomaly detection via Monitors. Full visibility into where artists are blocked.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**DistroKid at a glance:**
- 2M+ registered artists, handles 30-40% of all new music releases globally
- Revenue: $97.2M (2024), subscription-based annual model
- Exploring $2B sale (Goldman Sachs + Raine advising, as of Jan 2026). Up from $1.3B valuation in 2021
- Founded by Philip Kaplan (2013). Now run by President Phil Bauer (Kaplan transitioned to Chairman in Jan 2024)
- Pricing: Musician ($24.99/yr), Musician Plus ($39.99/yr), Ultimate ($89.99/yr)
- Takes 0% of artist royalties (subscription-only model)
- Distributes to Spotify, Apple Music, TikTok, YouTube Music, Amazon, Pandora, Deezer, TIDAL, 150+ platforms
- Launched DistroKid Direct (merchandise platform) in 2025

**Confirmed PSPs:**
- Card processor: undisclosed (likely Stripe or Braintree based on tech stack signals, but not confirmed)
- Apple Pay: accepted for subscription payments
- Google Pay: accepted for subscription payments
- Tipalti: handles all artist payouts (PayPal, ACH, wire, eCheck, paper check)
- No PayPal for subscriptions (explicitly stated)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary HQ market)
  Accepted: Visa/MC/Amex/Discover, Apple Pay, Google Pay
  Missing: PayPal, ACH direct, Cash App, Venmo
  Note: US market adequately served via cards/wallets, though PayPal exclusion is unusual.

MARKET 2: India (massive independent music market)
  Accepted: Visa/MC (international-enabled only)
  Missing: UPI, RuPay, Paytm, PhonePe, net banking
  Note: RBI mandate blocks auto-recurring charges above Rs 5,000 on most cards. "Almost every Indian artist has had payments fail." UPI handles 75%+ of digital payments.

MARKET 3: Nigeria (largest African music market)
  Accepted: Visa/MC (international-enabled only)
  Missing: Bank transfer, M-Pesa, Flutterwave, Paystack local methods
  Note: Nigerian banks have stopped supporting international payments on naira cards. Virtual USD cards (EverTry, etc.) are the only workaround.

MARKET 4: Brazil (major music export market)
  Accepted: Visa/MC (international-enabled only)
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazil digital payments. Artists must use international Visa/MC to subscribe.

MARKET 5: Mexico (growing Latin music market)
  Accepted: Visa/MC (international-enabled only)
  Missing: OXXO, SPEI, CoDi
  Note: 63% unbanked population. Without cash-based methods like OXXO, most independent Mexican artists cannot pay.

**Payment issues documented:**
- Card decline is the single most common support issue (dedicated Help Center article, multiple YouTube troubleshooting videos)
- African artists face near-total payment blockage due to local bank restrictions on international recurring charges
- Indian artists face systematic declines due to RBI auto-debit mandate
- Failed annual renewal = music removed from all streaming platforms (catastrophic consequence)
- "Leave a Legacy" add-on exists specifically to protect against payment failure takedowns ($29.99/song one-time)

**Key meeting angles:**
1. **$2B sale imminent** | Goldman Sachs + Raine advising. Payment infrastructure will be under buyer scrutiny
2. **Card-only global platform** | 2M+ artists in 150+ countries, but only cards accepted. Massive creator exclusion
3. **India payment wall** | RBI mandate + local bank restrictions = systematic card declines for Indian artists
4. **Africa lockout** | Nigerian banks blocking international recurring charges entirely
5. **Catastrophic failure stakes** | One failed annual charge = entire music catalog pulled from Spotify, Apple Music, etc.
6. **Creator economy growth** | 30-40% of all new releases globally. Music distribution is a payments business at scale
7. **Competitor precedent** | TuneCore (PayPal + local methods), CD Baby (PayPal + multiple options)

**Sources:**
- [DistroKid Official Logo](https://distrokid.com/logo/)
- [DistroKid Help: Why Is My Card Not Working](https://support.distrokid.com/hc/en-us/articles/360057005634)
- [DistroKid Help: Withdrawal Methods](https://support.distrokid.com/hc/en-us/articles/360013535074)
- [DistroKid Help: Can I Pay With PayPal](https://support.distrokid.com/hc/en-us/articles/360013534294)
- [DistroKid Help: Billing Questions](https://support.distrokid.com/hc/en-us/sections/4407873147027)
- [DistroKid Help: Country Availability](https://support.distrokid.com/hc/en-us/articles/360013648113)
- [DistroKid Plans and Pricing](https://distrokid.com/pricing/)
- [DistroKid Wikipedia](https://en.wikipedia.org/wiki/DistroKid)
- [MBW: DistroKid Exploring Sale](https://www.musicbusinessworldwide.com/distrokid-repped-by-goldman-sachs-and-raine-exploring-a-sale/)
- [SpitFireHipHop: DistroKid $2B Sale](https://spitfirehiphop.com/corporate-corner/revenue-monetization/2026/04/distrokids-2-billion-sale-talks-show-why-independent-artists-need-an-exit-strategy/)
- [EverTry: How to Pay for DistroKid in Africa](https://evertry.co/blog/how-to-pay-for-distrokid-in-africa-a-step-by-step-guide/)
- [DireNote Media: Why Distributors Let Down Indian Artists](https://blog.direnotemedia.com/2025/07/why-global-music-distributors-often-let.html)
- [Expanded Ramblings: DistroKid Statistics 2025](https://expandedramblings.com/index.php/distrokid/)
- [Rewarble: DistroKid Payment Methods](https://rewarble.com/insight/distrokid-payment-methods)
- [RexiusRecords: DistroKid Withdrawal Methods](https://www.rexiusrecords.com/transfer-money-distrokid/)
- [ALERA: DistroKid Pricing 2026](https://www.alera.fm/blog/distrokid-pricing-2026-every-plan-fee-hidden-cost)
