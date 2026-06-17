# PATREON | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Patreon
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/9/94/Patreon_logo.svg
Nombre merchant: Patreon

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Involuntary Churn Drain
Tittle_Pain Point_2: Zero Local APMs
Tittle_Pain Point_3: Single Acquirer Risk
Tittle_Pain Point_4: Cross-Border FX Markup
Tittle_Pain Point_5: Mobile Wallet Gap

Desc_Pain Point_1: Failed payments are the #1 churn driver. Patreon retries 6 times then downgrades to free. Aug 2023 processor issue spiked declines 50%+.
Desc_Pain Point_2: 8M+ patrons across 180+ countries but only cards, PayPal, Apple Pay, Venmo. No Pix, UPI, BLIK, SEPA DD. 59% of traffic outside the US, zero local APMs.
Desc_Pain Point_3: Stripe is the sole card acquirer. Any Stripe disruption blocks 100% of card membership payments. No failover path to reroute if Stripe declines or goes down.
Desc_Pain Point_4: 2.5% FX fee on every cross-border pledge. 72% of traffic is outside the US, so most of 8M patrons absorb markups inflating creator support costs.
Desc_Pain Point_5: No Google Pay despite Android being dominant internationally. No mobile wallets (GCash, Maya, GrabPay) in SEA markets where card penetration is under 10%.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Apple IAP (iOS)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: BLIK
Local_M_5: Google Pay
Local_M_6: Konbini
Local_M_7: Boleto
Local_M_8: GCash
Local_M_9: OXXO
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal based on card BIN, issuer, and geography. With $2B+ in annual creator payouts flowing through the platform, even a 3% auth rate uplift recovers millions in memberships that currently fail silently every month.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a card. Yuno reroutes to the next best acquirer in milliseconds, turning failed renewals into recovered recurring revenue. Up to 50% recovery on soft declines, directly reducing the involuntary churn that cost creators 50%+ spikes in 2023.
Desc_Yuno_Cap3: Activates the APMs Patreon's global patrons need: Pix in Brazil, UPI in India, SEPA DD in Germany, BLIK in Poland, Konbini in Japan, iDEAL in the Netherlands, OXXO in Mexico. One API, 1,000+ payment methods, instant geo-routing. No engineering sprint per market.
Desc_Yuno_Cap4: One dashboard replacing Patreon's fragmented Stripe + PayPal + Apple IAP settlement streams. Real-time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Patreon at a glance:**
- 250,000+ active creators, 8M+ monthly paying patrons, 25M+ paid memberships total
- Platform revenue: $50M to $75M annually; creators earn $2B+ per year on Patreon
- $10B+ cumulative creator payouts since launch
- Valuation: ~$900M to $1.5B (last funding: $155M Series F, Apr 2021)
- IPO positioning: actively exploring public listing, secondary shares trading at ~$13.6/share on Nasdaq Private Market
- 97.5M monthly site visits, 180+ countries, 72% of traffic from outside the US
- New fee structure (Aug 2025): 10% standard platform fee + 2.9% + $0.30 processing fee

**Confirmed PSPs:**
- Stripe: primary card acquirer (confirmed in privacy policy, creator payout docs, help center)
- PayPal: secondary (patron payment option, also used for creator payouts)
- Apple IAP: iOS in-app purchases (Patreon recently enabled web checkout to bypass Apple's 30% fee)
- Payoneer: creator payout option (not patron-facing)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (41% of traffic)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Venmo
  Missing: Google Pay, ACH, Cash App Pay
  Note: No Google Pay despite broad Android usage in the US.

MARKET 2: United Kingdom (6.6%)
  Accepted: Visa/MC, PayPal, Apple Pay
  Missing: Google Pay, Open Banking (Pay by Bank)
  Note: Open Banking adoption surging in UK; natural fit for recurring memberships.

MARKET 3: Germany (4.9%)
  Accepted: Visa/MC, PayPal
  Missing: SEPA Direct Debit, Sofort, Giropay
  Note: ~35% credit card penetration. SEPA DD is the backbone of German subscription billing.

MARKET 4: Japan (4.6%)
  Accepted: Visa/MC, PayPal
  Missing: Konbini, JCB local routing, PayPay, Paidy
  Note: Japan has strong preference for convenience store payments and local wallets.

MARKET 5: Canada (4.3%)
  Accepted: Visa/MC, PayPal, Apple Pay
  Missing: Interac, Google Pay
  Note: Interac Online/Debit is the dominant Canadian payment rail.

**Payment failure history:**
- August 2023: Major payment crisis. Processor partner issue caused 50%+ spike in payment declines, directly reducing creator payouts
- Patreon retries failed payments up to 6 times per month, then downgrades patron to free member
- March 2026: Mass cleanup of long-failed payments; members stuck in decline since pre-2024 were cancelled
- 70% of subscription companies report failed payments negatively impact churn (PYMNTS research)

**Key meeting angles:**
1. **Creator livelihood dependency**: Failed payments directly reduce creator income; Patreon's entire value prop rests on reliable payment flow
2. **IPO readiness**: Payment infrastructure resilience will be scrutinized by underwriters
3. **International growth ceiling**: 72% international traffic but zero local APMs in any market
4. **Involuntary churn reduction**: Smart retries + failover could save millions in lost memberships annually
5. **Apple fee arbitrage**: Patreon already pushing web checkout to avoid Apple's 30% cut; local APMs on web strengthen this strategy
6. **Competitor pressure**: Substack, Buy Me a Coffee, Ko-fi all competing for creators; payment reliability is a differentiator

**Sources:**
- [Patreon Member Payment Options](https://support.patreon.com/hc/en-us/articles/360061439691-What-are-my-members-payment-options)
- [Patreon Payment Processing](https://support.patreon.com/hc/en-us/articles/360024774831-How-payment-processing-works-on-Patreon)
- [Patreon Creator Fees Overview](https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview)
- [Patreon Supported Currencies](https://support.patreon.com/hc/en-us/articles/360039589091-Patreon-s-supported-currencies)
- [Patreon Failed Payment Help](https://support.patreon.com/hc/en-us/articles/203913799-Failed-payment-help)
- [Patreon How Payouts Work](https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work)
- [Patreon Payouts Guide Non-US](https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US)
- [Patreon Using Apple Pay](https://support.patreon.com/hc/en-us/articles/360040486792-Using-Apple-Pay-as-your-payment-method)
- [Patreon Privacy Policy](https://privacy.patreon.com/policies)
- [Patreon Standard Platform Fee Aug 2025](https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025)
- [PYMNTS: Payment Problems for Patreon Creators](https://www.pymnts.com/subscriptions/2023/payment-problems-create-headaches-for-patreon-creators/)
- [Engadget: Patreon Fixing Canceled Payments](https://www.engadget.com/patreon-is-fixing-canceled-payments-and-inaccessible-funds-for-creators-175319787.html)
- [Fueler: Patreon Stats 2026](https://fueler.io/blog/patreon-usage-revenue-valuation-growth-statistics)
- [PremierAlts: Patreon Valuation](https://www.premieralts.com/companies/patreon/valuation)
- [SimilarWeb: patreon.com Traffic](https://www.similarweb.com/website/patreon.com/)
- [TechCrunch: Patreon Web Payments](https://techcrunch.com/2025/05/06/patreons-app-can-now-accept-web-payments-after-u-s-app-store-changes/)
- [Patreon Brand Assets](https://www.patreon.com/brand)
