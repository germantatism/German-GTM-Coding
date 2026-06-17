# DISCORD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Discord
═══════════════════════════════════════

Logo: https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d718355f9c89eb0fd350_Logo.svg
Nombre merchant: Discord

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Localization Debt
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: Checkout Friction
Tittle_Pain Point_4: Single Point of Failure
Tittle_Pain Point_5: Cross-Border Cost

Desc_Pain Point_1: 17 currencies localized but zero local APMs accepted. Users in Brazil, India, Philippines openly request Pix, UPI, GCash on community forums.
Desc_Pain Point_2: Cross-border card declines hit 200M+ global users. Local banks refuse international transactions; prepaid cards systematically rejected at checkout.
Desc_Pain Point_3: Only 6 payment methods for 200M+ MAU across 150+ countries. India's 42M users have zero local options: no UPI, no RuPay, no way to pay.
Desc_Pain Point_4: Stripe is the sole card acquirer with no failover. Any Stripe outage blocks 100% of web/desktop Nitro, Boost, and Shop transactions globally.
Desc_Pain Point_5: USD settlement across 17 local currency markets adds FX markup on every transaction. 72% of users outside the US pay cross-border fees.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: GCash
Local_M_4: BLIK
Local_M_5: Konbini
Local_M_6: Boleto
Local_M_7: RuPay
Local_M_8: OXXO
Local_M_9: Maya
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal. Each Nitro renewal routed to the highest performing processor for that card BIN, issuer, and market. With $725M ARR and 200M+ MAU across 150+ countries, even a 3% auth uplift translates to $21M+ in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates Discord's single Stripe dependency. When Stripe declines, Yuno reroutes to the next best acquirer in milliseconds, turning failed Nitro renewals into recovered recurring revenue with zero customer friction. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates the APMs Discord users demand: Pix in Brazil (52M users), UPI in India (42M users), GCash in Philippines, BLIK in Poland, Konbini in Japan, OXXO in Mexico. One API, 1,000+ payment methods, instant geo-routing. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Discord's fragmented Stripe + PayPal + Apple IAP + Google Play settlement streams. Real-time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Discord at a glance:**
- 200M+ MAU (2025), 690M+ registered users, 150+ countries
- Revenue: $725M ARR (end 2024), ~29% YoY growth, positive EBITDA 5 consecutive quarters
- IPO filed January 2026 (Goldman Sachs + JPMorgan). Targeting $15B to $20B valuation
- New CEO: Humam Sakhnini (ex PayPal, appointed April 2025)
- Revenue streams: Nitro ($2.99 to $9.99/mo, ~7.3M subscribers), Server Boosts, Quests (ads), Shop/Orbs, Creator Program (10% cut)
- 72% of users are international; Asia Pacific = 34% of base
- No dedicated VP/Head of Payments identified. Likely under VP Engineering (Thomas Jacques) or CTO (Stan Vishnevskiy)

**Confirmed PSPs:**
- Stripe: primary (named in Privacy Policy, powers creator payouts)
- PayPal: secondary (named in Privacy Policy)
- Apple App Store: mobile IAP (iOS)
- Google Play: mobile IAP (Android)
- No payment orchestrator detected
- Actively hiring Sr. Software Engineer, Payments

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (28.4% of traffic)
  ✅ Currently offer: Visa/MC/Amex/Discover, PayPal, Venmo (via PayPal), Apple Pay, Google Pay
  ❌ Missing: ACH, Cash App Pay
  💡 Cash App has 57M+ users skewing young. Discord's exact demographic.

MARKET 2: Brazil (6.5%, 52M users)
  ✅ Currently offer: Visa/MC, PayPal, Paysafecard (BRL pricing available)
  ❌ Missing: Pix, Boleto, local installment cards
  💡 Pix handles 70%+ of digital payments in Brazil. Community posts explicitly demand it.

MARKET 3: India (5.3%, 42M users, NO localized pricing)
  ✅ Currently offer: Visa/MC, PayPal (USD only)
  ❌ Missing: UPI, RuPay, Paytm, PhonePe. Also no INR pricing.
  💡 75%+ of Indian digital payments use UPI. Community posts state "many Indians are unable to buy Nitro."

MARKET 4: Philippines (3.8%)
  ✅ Currently offer: Visa/MC, PayPal (PHP pricing available)
  ❌ Missing: GCash, Maya, GrabPay
  💡 Credit card penetration ~6%. GCash has 60M+ users. Without mobile wallets, vast majority can't pay.

MARKET 5: Germany (3.3%, 26M users)
  ✅ Currently offer: Visa/MC, PayPal, Paysafecard (EUR pricing)
  ❌ Missing: SEPA Direct Debit, Sofort
  💡 ~35% credit card penetration. SEPA DD is the backbone of German subscription billing.

**Payment outage history:**
- Multiple payment related incidents documented on discordstatus.com
- "Unable to Confirm Payment Method" error is so common it has multiple third party troubleshooting guides

**Key meeting angles:**
1. **IPO urgency** | Payment infrastructure under underwriter scrutiny right now
2. **New CEO from PayPal** | Humam Sakhnini has fintech DNA; payments is a natural executive conversation
3. **Localization paradox** | 17 currencies, ZERO local APMs in any market
4. **India black hole** | 42M users, no INR pricing, no local APMs
5. **Building vs. buying** | Actively hiring payments engineers; Yuno saves years of internal build
6. **IAP fee arbitrage** | Local APMs on web reduce Apple/Google 15 to 30% fees
7. **Competitor precedent** | Spotify (Adyen multi PSP), Roblox (multi PSP), Steam (100+ methods)

**Sources:**
- [Discord Privacy Policy](https://discord.com/privacy)
- [Discord Branding (Logo)](https://discord.com/branding)
- [Discord Billing FAQ](https://support.discord.com/hc/en-us/articles/360017693772)
- [Discord Localized Pricing](https://support.discord.com/hc/en-us/articles/4407269525911)
- [Discord Paid Services Terms](https://discord.com/terms/paid-services-terms)
- [Discord Status](https://discordstatus.com/history)
- [Discord Sr. SE Payments Job](https://discord.com/jobs/8452933002)
- [Discord Community: Pix Brazil](https://support.discord.com/hc/en-us/community/posts/20393408384407)
- [Discord Community: UPI India](https://support.discord.com/hc/en-us/community/posts/4420206869399)
- [Discord Community: Indian Payment](https://support.discord.com/hc/en-us/community/posts/1500001341081)
- [Discord Failed Payment Support](https://support.discord.com/hc/en-us/articles/28561299065623)
- [DemandSage: Discord Stats 2026](https://www.demandsage.com/discord-statistics/)
- [World Population Review: Discord Users](https://worldpopulationreview.com/country-rankings/discord-users-by-country)
- [Accio: Discord IPO Filing](https://www.accio.com/blog/discord-ipo-filing-shows-path-to-725m-revenue-growth)
- [Discord Press: New CEO](https://discord.com/press-releases/discord-appoints-new-ceo-humam-sakhnini)
