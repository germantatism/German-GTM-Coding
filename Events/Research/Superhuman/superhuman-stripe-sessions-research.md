# SUPERHUMAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Superhuman
=======================================

Logo: https://asset.brandfetch.io/idS3X5lclB/idWKtXF5-I.svg
Nombre merchant: Superhuman

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Checkout Wall
Tittle_Pain Point_2: Country Mismatch Blocks
Tittle_Pain Point_3: Single Acquirer Exposure
Tittle_Pain Point_4: Zero APM Coverage
Tittle_Pain Point_5: Post-Merger Billing Chaos

Desc_Pain Point_1: Only Visa, MC, Amex, and Discover accepted. No PayPal, no wallets, no local methods. For a $700M+ ARR suite (with Grammarly) serving 40M daily users globally, card-only checkout locks out millions in low card-penetration markets.
Desc_Pain Point_2: Payments declined when billing country does not match the card issuer country. International users routinely blocked at checkout due to rigid country-matching rules, creating friction across every non-US market.
Desc_Pain Point_3: Stripe is the sole payment processor for all Superhuman Mail subscriptions. Any Stripe incident blocks new signups and renewals across Starter, Business, and Enterprise tiers with zero failover path.
Desc_Pain Point_4: No UPI for India (regional rupee pricing offered but no local rails), no SEPA for Europe, no Pix for Brazil, no Konbini for Japan. Three currencies supported but zero local payment methods in any market.
Desc_Pain Point_5: Grammarly acquisition created parallel billing systems. Superhuman Mail billed separately from the Superhuman Suite. Subscription management split across Grammarly and Superhuman accounts, complicating reconciliation.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Apple App Store (mobile)
PSP_3: Google Play (mobile)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: SEPA Direct Debit
Local_M_3: iDEAL
Local_M_4: Pix
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: PayPal
Local_M_8: Konbini
Local_M_9: GCash
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the optimal acquirer by card BIN, issuer, and market. With 40M+ DAU across the Superhuman Suite and $700M+ combined ARR, a 3% auth uplift from intelligent routing recovers $21M+ in annual revenue across all subscription tiers.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Yuno reroutes to the next best acquirer in milliseconds, recovering failed renewals without user friction. Up to 50% recovery on soft declines, turning country-mismatch blocks and cross-border failures into completed payments.
Desc_Yuno_Cap3: Unlocks the methods Superhuman's global users need: UPI for India (where INR pricing already exists), SEPA DD for Europe, Pix for Brazil, iDEAL for Netherlands. One API, 1,000+ payment methods, zero per-market engineering. Removes the card-only barrier in every market.
Desc_Yuno_Cap4: Single dashboard unifying Superhuman Mail and Grammarly Suite billing into one reconciliation stream. Real-time approval monitoring, centralized settlement across Stripe plus App Store plus Play Store, and NOVA anti-fraud reducing false declines by up to 75%.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Superhuman at a glance:**
- Founded 2014, HQ San Francisco. CEO/Founder: Rahul Vohra
- Acquired by Grammarly July 2025. Grammarly rebranded as Superhuman in October 2025
- Pre-acquisition: ~70K paying customers, $35 to $36.5M ARR (June 2025)
- Post-acquisition (Superhuman Suite): 40M+ DAU, $700M+ combined ARR (Grammarly + Superhuman Mail + Coda)
- Previous valuation: $825M (2021). Acquisition estimated at $300 to $500M
- Total funding raised: $118M+ from a16z, IVP, Tiger Global
- Superhuman Suite tiers: Free, Pro ($25/mo annual), Enterprise (custom)
- Superhuman Mail standalone: Starter ($30/mo), Business ($40/mo), Enterprise (custom)
- Available on iOS, Android, macOS, Windows, and web

**Confirmed PSPs:**
- Stripe, Inc. and affiliates: sole payment processor (confirmed in Superhuman Terms of Service: "Superhuman uses Stripe, Inc. and its affiliates as its payment service provider")
- Apple App Store: mobile IAP (iOS)
- Google Play: mobile IAP (Android)
- No payment orchestrator detected
- No PayPal, no wallets, no local APMs

**Accepted payment methods (current):**
- Credit/debit cards: Visa, Mastercard, American Express, Discover
- Regional pricing in EUR, GBP, INR (currency only, not local payment rails)
- Apple Pay / Google Pay (only through App Store/Play Store, not direct checkout)
- NO PayPal, NO SEPA, NO UPI, NO local APMs

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~60% of user base)
  Accepted: Visa/MC/Amex/Discover
  Missing: PayPal, ACH, Cash App Pay
  Note: Core market well served by cards. PayPal absence notable for a consumer/prosumer product.

MARKET 2: United Kingdom (~10%)
  Accepted: Visa/MC/Amex (GBP pricing)
  Missing: Open Banking, PayPal
  Note: GBP pricing available but no UK-native methods. Open Banking adoption growing rapidly for subscriptions.

MARKET 3: India (INR pricing available)
  Accepted: Visa/MC (INR pricing)
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: Superhuman offers INR pricing but zero Indian payment rails. 75%+ of Indian digital payments use UPI. Massive gap between pricing localization and payment localization.

MARKET 4: Europe / EU (EUR pricing available)
  Accepted: Visa/MC/Amex (EUR pricing)
  Missing: SEPA Direct Debit, iDEAL (NL), BLIK (PL), Bancontact (BE), Sofort
  Note: EUR pricing exists but no European payment methods. SEPA DD is the backbone of EU subscription billing.

MARKET 5: Canada / Australia (~8% combined)
  Accepted: Visa/MC/Amex (USD pricing)
  Missing: Interac (Canada), BPAY (Australia)
  Note: No local currency or methods for two significant English-speaking markets.

**Key meeting angles:**
1. **Post-merger payment unification** | Grammarly acquisition created parallel billing. Yuno orchestration layer unifies Superhuman Mail + Suite billing into one stream.
2. **40M DAU scale** | Combined suite has massive global reach. Card-only checkout at this scale means millions in unreachable revenue in low card-penetration markets.
3. **India pricing gap** | INR pricing shows intent to localize, but without UPI the pricing is symbolic. Adding local rails converts intent into revenue.
4. **Stripe single dependency** | All $700M+ ARR routes through one PSP. At this scale, failover is a board-level risk.
5. **Country mismatch friction** | Documented billing country vs card country blocks. Smart Routing eliminates this by routing to local acquirers.
6. **Enterprise billing complexity** | Enterprise customers need invoicing, PO, and ACH. Current card-only setup limits enterprise deal velocity.

**Sources:**
- [Superhuman Terms of Service (Stripe confirmation)](https://superhuman.com/legal/terms)
- [Superhuman Pricing Plans](https://superhuman.com/plans)
- [Superhuman Billing Help Center](https://help.superhuman.com/hc/en-us/categories/38445127077651-Billing)
- [Superhuman Receipts and Invoices](https://help.superhuman.com/hc/en-us/articles/38456121262355-Receipts-and-Invoices)
- [Superhuman Media Assets](https://superhuman.com/media-assets)
- [Grammarly: Superhuman Billing FAQs](https://support.grammarly.com/hc/en-us/articles/40875737663885-Superhuman-billing-and-subscription-management-FAQs)
- [Grammarly: Country Mismatch Error](https://support.grammarly.com/hc/en-us/articles/14034418233997)
- [Grammarly Acquires Superhuman (TechCrunch)](https://techcrunch.com/2025/07/01/grammarly-acquires-ai-email-client-superhuman/)
- [Superhuman Blog: Grammarly Acquisition](https://blog.superhuman.com/superhuman-is-being-acquired-by-grammarly/)
- [Sacra: Superhuman Revenue & Valuation](https://sacra.com/c/superhuman/)
- [Contrary Research: Superhuman Breakdown](https://research.contrary.com/company/superhuman)
- [The Split: Superhuman $700M ARR](https://www.thespl.it/p/inside-the-new-superhuman-700m-arr)
- [Superhuman Wikipedia](https://en.wikipedia.org/wiki/Superhuman_(email_client))
