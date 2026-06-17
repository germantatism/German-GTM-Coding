# PEACOCK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Peacock
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/d/d3/NBCUniversal_Peacock_Logo.svg
Nombre merchant: Peacock

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US-Only Payment Wall
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: Fragmented Billing
Tittle_Pain Point_4: Involuntary Churn
Tittle_Pain Point_5: No Failover Layer

Desc_Pain Point_1: Requires a US-issued card to subscribe. International users in SkyShowtime markets (20+ countries) who want the full library cannot pay directly.
Desc_Pain Point_2: 44M paid subscribers billed via cards and PayPal with no local acquiring. Cross-border card attempts from expats and travelers face issuer declines.
Desc_Pain Point_3: Billing split across 5+ channels (direct, Apple, Google, Roku, Amazon, Xfinity) with no unified view. Reconciliation gaps create churn blind spots.
Desc_Pain Point_4: Failed recurring card charges on $5.4B annual revenue cause silent subscriber loss. Each 1% recovery improvement equals $54M+ in annual revenue saved.
Desc_Pain Point_5: Single payment processor for direct billing with no cascade. Any processor outage halts all web and app subscription activations and renewals.

SLIDE 1: PSP TOPOLOGY

PSP_1: Comcast Internal Billing
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play
PSP_5: Roku Pay
PSP_6: Amazon IAP

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: BLIK
Local_M_5: Pix
Local_M_6: Sofort/Klarna
Local_M_7: Giropay
Local_M_8: Swish
Local_M_9: Multibanco
Local_M_10: Przelewy24

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple acquirers optimized by card BIN, issuer, and region. With $5.4B in annual revenue and 44M subscribers, even a 3% auth uplift on direct billing translates to $50M+ in recovered annual revenue from reduced declines alone.
Desc_Yuno_Cap2: Automatic cascade eliminates Peacock's single-processor dependency. When a card decline occurs, Yuno reroutes to the next best acquirer in milliseconds, turning failed renewals into recovered subscriptions. Up to 50% recovery on soft declines with zero subscriber friction.
Desc_Yuno_Cap3: Unlocks international expansion without a US-card requirement: SEPA DD in Europe, iDEAL in Netherlands, BLIK in Poland, Bancontact in Belgium, Sofort in Germany. One API, 1,000+ payment methods. Enables Peacock to monetize SkyShowtime markets directly.
Desc_Yuno_Cap4: One dashboard consolidating Peacock's fragmented billing across direct, Apple, Google, Roku, Amazon, and Xfinity channels. Real-time approval rate monitoring, centralized reconciliation, and millisecond anomaly detection via Monitors across all revenue streams.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Peacock at a glance:**
- 44M paid subscribers (Q4 2025), up 22% YoY
- Revenue: $5.4B (2025), up from $4.9B (2024). 16% YoY growth in Q1 2025
- Owned by NBCUniversal (Comcast subsidiary)
- Adjusted EBITDA loss narrowing: ($215M) in Q1 2025 vs ($639M) Q1 2024 (66% improvement)
- Plans: Premium ($7.99/mo), Premium Plus ($13.99/mo), bundles with Apple TV+ ($14.99/$19.99/mo)
- Content: NBC originals, Universal films, Premier League, NFL Sunday Night Football, WWE, NBA on NBC
- Comcast co-CEO Mike Cavanagh: "Domestic is our path." Focused on US profitability, not global expansion
- SkyShowtime JV (with Paramount) distributes Peacock content in 20+ European markets

**Confirmed PSPs:**
- Comcast/NBCUniversal internal billing: primary for direct subscribers (credit/debit cards)
- PayPal: secondary direct payment option
- Apple Pay: accepted for web/mobile
- Apple App Store / Google Play / Roku / Amazon: third-party IAP channels
- Xfinity bundled billing for Comcast cable subscribers
- No payment orchestrator detected
- Bank statement descriptors: PEACOCKTV, NBCUNIVERSAL PEACOCK, PEACOCK-PREMIUM, PMT-PEACOCK

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary, 44M subscribers)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay, Gift Cards
  Missing: ACH, Venmo (direct), Cash App Pay
  Note: Core market adequately served via cards/PayPal; mobile wallet gaps among younger demographics.

MARKET 2: United Kingdom (SkyShowtime/NOW distribution)
  Accepted: Via Sky/NOW subscription only (no direct Peacock billing)
  Missing: Direct billing, SEPA DD, Open Banking, Faster Payments
  Note: 20M+ Sky customers accessed Peacock content until Jan 2024 shutdown. No direct payment path exists.

MARKET 3: Germany (SkyShowtime territory)
  Accepted: Via Sky/WOW only (no direct billing)
  Missing: SEPA DD, Sofort, Giropay, PayPal direct
  Note: Only 35% credit card penetration. Without SEPA DD, direct subscriber acquisition is impossible.

MARKET 4: Italy (SkyShowtime territory)
  Accepted: Via Sky only
  Missing: PostePay, Bancomat Pay, SEPA DD, Satispay
  Note: 80%+ of Italian digital payments use debit/prepaid. No direct billing pathway.

MARKET 5: Netherlands (SkyShowtime territory)
  Accepted: Via SkyShowtime only
  Missing: iDEAL, SEPA DD, Bancontact
  Note: iDEAL handles 70%+ of Dutch e-commerce. Without it, direct billing is blocked for the majority.

**Payment issues documented:**
- "Failed payment" and "payment declined by bank" messages documented in Peacock Help Center
- US-card requirement blocks all international direct subscribers
- Third-party billing reconciliation issues: users charged via Apple/Google but Peacock fails to recognize the subscription
- Separate billing descriptors for Premium vs Premium Plus confuse subscribers

**Key meeting angles:**
1. **$5.4B revenue, basic payments** | Peacock processes billions with no orchestration layer or failover
2. **US-only wall** | Requires US-issued card, blocking all international direct subscribers
3. **SkyShowtime monetization** | Peacock content reaches 20+ European countries but Comcast gets JV revenue share, not direct billing
4. **Involuntary churn at scale** | 44M subs on recurring billing; failed charges = silent revenue drain
5. **Sports-driven growth** | NBA, NFL, Premier League drive spiky traffic; payment infrastructure must handle surges
6. **Fragmented billing** | 6+ billing channels (direct, Apple, Google, Roku, Amazon, Xfinity) with no unified dashboard
7. **Competitor precedent** | Disney+ (multi-PSP global), Netflix (Adyen global), HBO Max (multi-acquirer)

**Sources:**
- [Peacock Help: Payment Methods](https://www.peacocktv.com/help/article/payment-methods)
- [Peacock Help: Change Payment Method](https://www.peacocktv.com/help/article/how-do-i-change-my-payment-method)
- [Peacock Help: Third-Party In-App Billing](https://www.peacocktv.com/help/article/third-party-in-app-billing)
- [Peacock Help: Where Is Peacock Available](https://www.peacocktv.com/help/article/where-is-peacock-available)
- [Peacock Terms of Use](https://www.peacocktv.com/terms)
- [Deadline: Peacock Hits 44M Subscribers](https://deadline.com/2026/01/comcast-earnings-peacock-boosts-subscribers-nba-deal-widens-losses-1236700887/)
- [Hollywood Reporter: Peacock Stuck at 41M](https://www.hollywoodreporter.com/business/business-news/comcast-q2-2025-earnings-peacock-subscribers-versant-news-1236334135/)
- [Hollywood Reporter: Peacock Not Going Global](https://www.hollywoodreporter.com/business/business-news/mike-cavanagh-peacock-domestic-1236520525/)
- [The Desk: Comcast Peacock Focused on US](https://thedesk.net/2026/03/comcast-peacock-focused-on-us/)
- [Evoca: Peacock Statistics 2026](https://evoca.tv/peacock-statistics/)
- [Zippia: 40+ Peacock Statistics 2026](https://www.zippia.com/advice/peacock-statistics/)
- [Comcast Corporate: Peacock European Rollout](https://corporate.comcast.com/press/releases/peacock-european-rollout-continues-on-sky)
- [Sky Group: Peacock European Rollout](https://www.skygroup.sky/article/peacock-european-rollout-begins-on-sky)
- [Wikipedia: Peacock Streaming Service](https://en.wikipedia.org/wiki/Peacock_(streaming_service))
- [Bank Statement: Peacock Charge Descriptors](https://yourbankstatementconverter.com/blog/what-does-peacock-show-up-as-on-the-bank-statement/)
- [StatesCard: Pay for Peacock Outside US](https://www.statescard.com/us-streaming/pay-for-peacock)
