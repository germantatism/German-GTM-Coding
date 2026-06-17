# TWITCH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Twitch
═══════════════════════════════════════

Logo: https://brand.twitch.tv/assets/logos/svg/glitch-logo-purple.svg
Nombre merchant: Twitch

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Local APM Desert
Tittle_Pain Point_2: Auth Rate Bleed
Tittle_Pain Point_3: Single Acquirer Risk
Tittle_Pain Point_4: Subscription Churn Gap
Tittle_Pain Point_5: FX Cost Drag

Desc_Pain Point_1: 240M+ MAU across 150+ countries yet only cards, PayPal, and Amazon Pay accepted. Brazil (17M users) has no Pix; India has no UPI. Users request local methods.
Desc_Pain Point_2: Cross-border card transactions from 64% non-US users trigger issuer declines. Local banks reject international charges; prepaid cards fail at checkout.
Desc_Pain Point_3: Xsolla is the sole processor with no failover. March 2026 checkout incident blocked all subscription and Bits purchases for nearly an hour.
Desc_Pain Point_4: Failed recurring charges on subs cause involuntary churn. With $1.05B in subscription revenue, even 1% recovery gap equals $10M+ lost annually.
Desc_Pain Point_5: USD settlement for 64% international users adds FX markup on every transaction. Local pricing in 40+ countries but no local acquiring to cut fees.

SLIDE 1: PSP TOPOLOGY

PSP_1: Xsolla
PSP_2: Amazon Pay
PSP_3: PayPal
PSP_4: Apple App Store
PSP_5: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: BLIK
Local_M_4: Boleto
Local_M_5: OXXO
Local_M_6: SPEI
Local_M_7: GCash
Local_M_8: RuPay
Local_M_9: Maya
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Xsolla, Amazon Pay, and PayPal. Each subscription renewal routed to the highest performing processor for that card BIN, issuer, and market. With $1.9B in revenue and 240M+ MAU, even a 3% auth uplift translates to $31M+ in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates Twitch's single-processor dependency on Xsolla. When a decline occurs, Yuno reroutes to the next best acquirer in milliseconds, turning failed sub renewals into recovered revenue with zero viewer friction. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activates the APMs Twitch's global community demands: Pix in Brazil (17M users), UPI in India, BLIK in Poland, GCash in Philippines, OXXO in Mexico, PSE in Colombia. One API, 1,000+ payment methods, instant geo-routing. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Twitch's fragmented Xsolla + Amazon Pay + PayPal + App Store settlement streams. Real-time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Twitch at a glance:**
- 240M+ MAU (2026), 35M+ DAU, 150+ countries
- Revenue: $1.9B (2025), up 5.6% YoY. Subscriptions = 58% ($1.05B), Ads = 33% ($600M), Bits/other = 9%
- Owned by Amazon (acquired 2014 for $970M)
- 7.3M+ paid subscribers across Tier 1/2/3 and Turbo
- 72% of content consumed is gaming; expanding into Just Chatting, music, sports
- Local subscription pricing active in 40+ countries
- 64% of users are outside the United States

**Confirmed PSPs:**
- Xsolla: primary payment processor (subscription billing, Bits, Turbo via Xsolla Pay Station)
- Amazon Pay: integrated via parent company (card + Amazon balance)
- PayPal: secondary option for subs and Bits
- Apple App Store / Google Play: mobile IAP for iOS and Android
- Paysafecard: available via Xsolla in select European markets
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (36% of users, 93M)
  Accepted: Visa/MC/Amex/Discover, PayPal, Amazon Pay, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo (direct), ACH
  Note: Core market well served, but Cash App's 57M users skew young and match Twitch demographics perfectly.

MARKET 2: Brazil (6.6%, 17M users)
  Accepted: Visa/MC via Xsolla, PayPal
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazil digital payments. Users request Pix on forums. Massive conversion gap.

MARKET 3: Germany (6.6%, 16.8M users)
  Accepted: Visa/MC, PayPal, Paysafecard, Sofort (limited via Xsolla)
  Missing: SEPA Direct Debit, Giropay
  Note: Only 35% credit card penetration. SEPA DD is the German subscription billing backbone.

MARKET 4: Russia (4.1%, 10.5M users)
  Accepted: Visa/MC (limited due to sanctions), Xsolla local cards
  Missing: MIR, SBP, YooMoney
  Note: International card restrictions post-sanctions make local methods critical.

MARKET 5: Mexico (3.6%, 9.2M users)
  Accepted: Visa/MC via Xsolla
  Missing: OXXO, SPEI, CoDi
  Note: 63% of Mexicans are unbanked. OXXO processes 5.5M+ daily cash transactions. Without it, most cannot pay.

**Payment outage history:**
- March 31, 2026: "Identified Checkout Issues" incident lasting ~56 minutes
- September 2024: Payment partner issue delayed creator payouts (acknowledged by @TwitchSupport)
- "Payment Declined" errors are common enough to generate multiple third-party troubleshooting guides and TikTok tutorials

**Key meeting angles:**
1. **Amazon parent, startup payments** | Despite Amazon's fintech muscle, Twitch runs on Xsolla with no orchestration layer
2. **Revenue at scale** | $1.9B in revenue; even small auth rate improvements yield 8-figure gains
3. **64% international, minimal APMs** | Local pricing without local payment methods is a half-measure
4. **Brazil gap** | 17M users, zero Pix support. Pix is 70%+ of digital payments in Brazil.
5. **Subscription churn** | Involuntary churn from failed renewals is the silent revenue killer for a platform with 7.3M+ paid subs
6. **Xsolla single dependency** | No failover means any Xsolla outage halts 100% of web purchases
7. **Competitor precedent** | YouTube (Adyen multi-PSP), Discord (Stripe), Spotify (Adyen + local acquiring)

**Sources:**
- [Twitch Brand Assets (Logo)](https://brand.twitch.com/)
- [Twitch Help: Payout Details FAQ](https://help.twitch.tv/s/article/payout-details-faq)
- [Twitch Help: Failed Payments](https://help.twitch.tv/s/article/failed-payments)
- [Twitch Help: Local Sub Price Countries](https://help.twitch.tv/s/article/local-sub-price-countries)
- [Twitch Terms of Sale](https://legal.twitch.com/en/legal/terms-of-sale/)
- [Xsolla Partner Spotlight: Twitch](https://xsolla.com/stories/twitch)
- [Twitch UserVoice: Expanding Payment Methods India](https://twitch.uservoice.com/forums/929338-purchase-management/suggestions/43276860)
- [Twitch UserVoice: Change Payment Processor](https://twitch.uservoice.com/forums/929338-purchase-management/suggestions/47609756)
- [DemandSage: Twitch Statistics 2026](https://www.demandsage.com/twitch-users/)
- [Business of Apps: Twitch Revenue and Usage Statistics 2026](https://www.businessofapps.com/data/twitch-statistics/)
- [World Population Review: Twitch Users by Country](https://worldpopulationreview.com/country-rankings/twitch-users-by-country)
- [The Social Shepherd: Twitch Statistics 2026](https://thesocialshepherd.com/blog/twitch-statistics)
- [Twitch Status: Incident History](https://status.twitch.com/history)
- [Twitch Support: Payment Partner Issue (X/Twitter)](https://x.com/TwitchSupport/status/1835728981926047815)
- [Getsby: Twitch Payment Methods](https://getsby.com/en/which-payment-methods-are-available-for-twitch-tv/)
