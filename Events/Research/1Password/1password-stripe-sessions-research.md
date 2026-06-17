# 1PASSWORD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: 1Password
════════════════���══════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/d/d3/1Password_wordmark_blue_2023.svg
Nombre merchant: 1Password

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: USD-Only Billing
Tittle_Pain Point_3: Limited APM Coverage
Tittle_Pain Point_4: Cross-Border FX Fees
Tittle_Pain Point_5: Renewal Churn Risk

Desc_Pain Point_1: Stripe is the sole processor for 1M+ subscriptions across consumer and business segments. Zero acquirer redundancy means every Stripe outage blocks all new sign-ups, upgrades, and renewals globally.
Desc_Pain Point_2: All prices charged in USD regardless of customer location. European, Asian, and LATAM customers absorb FX markups from their banks, inflating the effective price and increasing price sensitivity.
Desc_Pain Point_3: Only credit cards and US ACH accepted. No SEPA DD for Europe, no Pix for Brazil, no UPI for India, no BLIK for Poland. 180,000+ business customers worldwide limited to card-only checkout.
Desc_Pain Point_4: Canadian-domiciled company billing in USD means every non-US customer pays a foreign transaction fee (1.5-3%). With millions of global subscribers, this hidden cost compounds churn pressure.
Desc_Pain Point_5: $400M+ ARR from recurring subscriptions. Card expiration, issuer declines, and failed renewals erode revenue monthly. Stripe's card updater helps, but no multi-acquirer retry path exists for hard failures.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole processor)
PSP_2: Apple App Store (iOS)
PSP_3: Google Play (Android)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: BACS Direct Debit
Local_M_5: BLIK
Local_M_6: iDEAL
Local_M_7: Boleto
Local_M_8: Konbini
Local_M_9: Bancontact
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription charge to the highest-performing acquirer by card BIN, issuer, and country. With $400M+ ARR from 1M+ subscriptions spanning consumers and enterprises globally, even a 3% auth uplift recovers $12M+ in annual revenue without adding a single new customer.
Desc_Yuno_Cap2: Automatic cascade removes 1Password's sole Stripe dependency. When Stripe declines a renewal, Yuno reroutes to the next best acquirer in milliseconds, recovering failed transactions with zero friction. Up to 50% recovery on soft declines across 1M+ active subscriptions.
Desc_Yuno_Cap3: Activates the APMs 1Password's global customer base needs: SEPA DD across Europe, BACS DD in the UK, Pix in Brazil, UPI in India, iDEAL in Netherlands, Konbini in Japan, BLIK in Poland. One API, 1,000+ payment methods. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Stripe card billing, ACH, and app store channels into a unified view. Real-time approval rate monitoring across all markets, centralized reconciliation, millisecond anomaly detection. Full visibility ahead of a potential 2026/2027 IPO.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**1Password at a glance:**
- Password management and identity security platform, founded 2005
- HQ: Toronto, Canada. ~2,900 employees
- Revenue: $400M+ ARR (October 2025), up from $331M in 2024, $250M in 2023
- Valuation: $6.8B (last round). Raised ~$950M total
- 180,000+ business customers, including nearly 1/3 of Fortune 100
- 1M+ total subscriptions (consumer + business)
- 1.3B+ human and machine credentials secured
- CEO: David Faugno. Possible IPO in 2026 or 2027
- 75%+ of revenue from B2B segment. 70% CAGR in $100K+ ARR customers over 3 years
- Gross retention above 90%, free cash flow positive

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed via official Stripe partnership announcement, Nov 2024)
- Stripe Billing: subscription management for 1M+ subscriptions
- Stripe Radar: fraud prevention
- Card Account Updater + Network Tokenization: churn reduction
- Apple App Store: iOS in-app purchases
- Google Play: Android in-app purchases
- No payment orchestrator detected
- No secondary acquirer identified

**Accepted payment methods:**
- Credit/debit cards: Visa, Mastercard, Amex, Discover, Diners Club, UnionPay, JCB
- ACH Direct Debit (US bank accounts only)
- 1Password Gift Cards
- All prices in USD only (no local currency billing)
- Canadian domicile means FX fees for all non-Canadian customers

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, ~60% of revenue estimated)
  Accepted: Visa/MC/Amex/Discover, ACH Direct Debit
  Missing: Cash App Pay, Venmo
  Note: Well served. ACH for enterprise billing is a strong plus

MARKET 2: United Kingdom (major enterprise market)
  Accepted: Visa/MC/Amex, JCB (USD only)
  Missing: BACS Direct Debit, Open Banking, GBP pricing
  Note: UK enterprises expect Direct Debit and local currency billing

MARKET 3: Germany/EU (major enterprise market)
  Accepted: Visa/MC/Amex (USD only)
  Missing: SEPA Direct Debit, Klarna, iDEAL (NL), EUR pricing
  Note: 35% card penetration in Germany. SEPA DD is the B2B standard

MARKET 4: Japan (significant tech market)
  Accepted: Visa/MC/JCB (USD only)
  Missing: Konbini, PayPay, JPY pricing
  Note: Konbini payments are essential for Japanese consumers

MARKET 5: Brazil (growing market)
  Accepted: Visa/MC (USD cross-border)
  Missing: Pix, Boleto, BRL pricing, installments
  Note: Pix handles 70%+ of digital payments. No local currency = significant barrier

**Key meeting angles:**
1. **IPO readiness** | Possible 2026/2027 IPO. Payment infrastructure resilience will face underwriter and analyst scrutiny
2. **1M+ subscription volume** | Massive recurring billing volume with zero acquirer redundancy. Single point of failure
3. **USD-only creates hidden churn** | Every non-US subscriber pays bank FX fees. Local currency + local APMs reduce effective price
4. **Enterprise segment is 75% of revenue** | B2B customers expect SEPA DD, BACS DD, and wire for large contracts
5. **Stripe reciprocal relationship** | Stripe uses 1Password as its password manager. Strong vendor relationship but breeds complacency on diversification
6. **Competitive pressure** | Bitwarden, Dashlane, LastPass all expanding globally. Local payment options become a differentiator in price-sensitive markets

**Sources:**
- [Stripe: 1Password Chooses Stripe Billing](https://stripe.com/newsroom/news/1password-and-stripe)
- [1Password Billing Support](https://support.1password.com/category/billing/)
- [1Password Subscription Management](https://support.1password.com/manage-subscription/)
- [1Password Billing Policy](https://support.1password.com/membership-billing-policy/)
- [1Password Regions](https://support.1password.com/regions/)
- [1Password $400M ARR Press Release](https://1password.com/press/2025/nov/1password-strengthens-leadership-amid-growth-milestone)
- [CNBC: 1Password $400M ARR](https://www.cnbc.com/2025/11/06/ryan-reynolds-backed-1password-tops-400-million-in-arr.html)
- [BetaKit: 1Password ARR Milestone](https://betakit.com/we-could-be-public-today-1password-crosses-400-million-usd-arr-milestone/)
- [Globe and Mail: 1Password IPO](https://www.theglobeandmail.com/business/article-canadian-tech-star-1password-on-track-for-ipo-but-not-likely-in-2025/)
- [1Password Wikipedia](https://en.wikipedia.org/wiki/1Password)
- [Sacra: 1Password Revenue](https://sacra.com/c/1password/)
- [1Password Pricing](https://1password.com/sign-up/)
