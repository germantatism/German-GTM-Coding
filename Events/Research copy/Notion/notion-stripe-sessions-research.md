# NOTION | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Notion
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png
Nombre merchant: Notion

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Self-Serve Wall
Tittle_Pain Point_2: Cross-Border Decline Surge
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: Zero Android Checkout
Tittle_Pain Point_5: Enterprise Invoice Friction

Desc_Pain Point_1: Plus and Business plans accept only cards and Apple Pay. No PayPal, iDEAL, Pix, or UPI. Every missing method is a lost upgrade in a 100M+ user PLG funnel.
Desc_Pain Point_2: LATAM, SEA, and Africa users report cards declined on upgrade. Cross-border auth failures through a single Stripe path block conversions in high-growth emerging markets.
Desc_Pain Point_3: Single Stripe processor with no cascade. Card declines trigger 8 retries over a month on the same processor, then workspace downgrades. No alternative acquirer path.
Desc_Pain Point_4: Android users cannot make payments in the app at all. With 72% global mobile share, this locks out the majority of mobile-first users in emerging markets.
Desc_Pain Point_5: Enterprise contracts need sales-assisted billing with no self-serve wire or local bank transfers. Manual invoicing slows deal velocity on multi-year commitments.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (self-serve card billing)
PSP_2: Apple App Store / Google Play (mobile subs)
PSP_3: SEPA Direct Debit (Europe only, via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: Boleto
Local_M_5: UPI
Local_M_6: BLIK
Local_M_7: GiroPay
Local_M_8: Bancontact
Local_M_9: KakaoPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $600M+ ARR and 100M+ users across 180+ countries, routing each renewal to the best acquirer per market delivers 3-10% auth uplift, translating to $18-60M in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a self-serve renewal. Instead of retrying the same processor 8 times over a month before downgrading, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates methods Notion's global base demands: PayPal, iDEAL in Netherlands, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, KakaoPay in South Korea, GrabPay in SEA. One API, 1,000+ methods. No per-market sprints.
Desc_Yuno_Cap4: One dashboard unifying Stripe card billing, SEPA DD, and mobile app store payments. Real-time approval monitoring per country, centralized reconciliation, and NOVA fraud detection (75% reduction) protecting 4M+ paying organizations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Notion at a glance:**
- Founded: 2013 by Ivan Zhao and Simon Last. HQ: San Francisco, California
- Valuation: $11B (December 2025 employee tender offer)
- Total funding: $418M over 9 rounds
- Key investors: Sequoia Capital, Index Ventures, Coatue Management
- ARR: $600M+ (December 2025 estimate); growing ~50%+ YoY, projected $900M-1B by end of 2026
- Users: 100M+ worldwide (reached in 2024, up 5x from 20M in 2022)
- Paying customers: 4,000,000+ organizations
- Enterprise: ~80% of Fortune 100 and 50%+ of Fortune 500 use Notion
- Employees: ~5,698 (March 2026)
- AI strategy: Notion AI agents and Connectors driving ~50% of ARR growth
- Revenue model: Free, Plus ($10/user/mo annual), Business ($18/user/mo annual), Enterprise (custom)
- IPO: Expected S-1 filing within 18 months; potential 2026-2027 IPO
- Products: Workspace, Wikis, Docs, Projects, AI, Notion Mail, Notion Calendar, Notion Sites

**Confirmed Payment Stack:**
- Stripe: Primary PSP for self-serve credit/debit card billing (Plus and Business plans)
- Stripe Link: Saved card checkout integration
- Apple Pay: Web checkout and iOS in-app payments
- SEPA Direct Debit: Europe-only bank debit (via Stripe, not credit transfer)
- Apple App Store: iOS subscription management
- Google Play Store: Android subscription management (but payments cannot be made in Android app directly)
- No PayPal accepted
- No local APMs beyond SEPA DD
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Evidence):**
- Android app: "Unfortunately, you can't make payments in the Android app at this time"
- SEPA DD is the only non-card method, limited to Europe
- No PayPal, no digital wallets beyond Apple Pay, no local bank transfer methods
- Failed payments retried up to 8 times over one month, then workspace downgraded to Free
- No alternative processor retry path on decline
- Users report being charged even after cancellation on Trustpilot reviews
- SEPA processing locks plan changes until debit fully clears

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market, 80% Fortune 100 adoption)
  Accepted: Visa/MC/Amex, Apple Pay
  Missing: PayPal, Venmo, Google Pay, ACH direct debit
  Note: Most complete coverage, but no failover and no PayPal for 100M+ user base

MARKET 2: Europe (significant knowledge-worker market)
  Accepted: Visa/MC, SEPA DD, Apple Pay
  Missing: iDEAL (Netherlands), GiroPay (Germany), Bancontact (Belgium), BLIK (Poland), Sofort, MB Way
  Note: SEPA DD is the only non-card method. Many local methods still missing across EU markets.

MARKET 3: Brazil / LATAM (fast-growing tech adoption)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of digital payments in Brazil. Card-only checkout blocks growth in LATAM.

MARKET 4: India / South Asia (massive knowledge-worker population)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of digital payments in India. Cross-border card declines are common.

MARKET 5: Japan / APAC (strong productivity-tool market)
  Accepted: Visa/MC (cross-border via Stripe)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: Japan is a top SaaS market. Local payment methods critical for self-serve conversion.

**Key meeting angles:**
1. **$600M+ ARR with card-only self-serve** | Every missing payment method is a lost upgrade in a 100M+ user PLG funnel
2. **Pre-IPO payment optimization window** | With an S-1 expected in 18 months, maximizing conversion and reducing involuntary churn directly impacts the IPO story
3. **Android payment blackout** | Zero in-app payments on 72% of global mobile devices. Massive missed conversion opportunity.
4. **8-retry-then-downgrade model** | Retrying the same failed processor 8 times is inefficient vs. intelligent multi-processor failover
5. **Fortune 100 penetration** | 80% adoption creates enterprise invoicing optimization opportunities
6. **AI-driven ARR surge** | 50%+ growth powered by AI features means payment infrastructure must scale globally
7. **Competitor pressure** | Coda, Microsoft Loop, and Confluence offer broader payment processor flexibility

**Sources:**
- [Notion: Payment Methods Help](https://www.notion.com/help/payment-methods)
- [Notion: Billing Help](https://www.notion.com/help/billing)
- [Notion: Plans, Billing & Payment](https://www.notion.com/help/category/plans-billing-and-payment)
- [Notion: Pricing](https://www.notion.com/pricing)
- [Notion: Invoices Help](https://www.notion.com/help/invoices)
- [Notion: Refunds Help](https://www.notion.com/help/refunds)
- [Trustpilot: Notion Reviews](https://www.trustpilot.com/review/notion.so)
- [SaaStr: Notion at $11B](https://www.saastr.com/notion-and-growing-into-your-10b-valuation-a-masterclass-in-patience/)
- [Sacra: Notion Revenue & Valuation](https://sacra.com/c/notion/)
- [Getlatka: Notion $600M Revenue](https://getlatka.com/companies/notion)
- [Super.so: Notion 100M Users](https://super.so/blog/notion-stats)
- [SQ Magazine: Notion Statistics 2026](https://sqmagazine.co.uk/notion-statistics/)
- [TapTwice: Notion Statistics](https://taptwicedigital.com/stats/notion)
- [Tracxn: Notion Company Profile](https://tracxn.com/d/companies/notion/)
- [Contrary Research: Notion Breakdown](https://research.contrary.com/company/notion)
- [Brandfetch: Notion Logo](https://brandfetch.com/notion.so)
