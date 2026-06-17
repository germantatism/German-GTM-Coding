# PUZZLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Puzzle
=======================================

Logo: https://asset.brandfetch.io/idJc8WLOzU/idIlyYcnMa.png
Nombre merchant: Puzzle

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Billing
Tittle_Pain Point_2: Single Processor Risk
Tittle_Pain Point_3: No International Rails
Tittle_Pain Point_4: Startup Churn Pressure
Tittle_Pain Point_5: Invoice Payment Gaps

Desc_Pain Point_1: Puzzle only supports USD for all billing and cost features. As startups using Puzzle expand globally, the platform cannot process subscriptions in local currencies. International customers bear FX conversion fees on every monthly charge.
Desc_Pain Point_2: Stripe is the sole payment processor for all Puzzle subscriptions. Any Stripe degradation blocks revenue collection from the entire customer base growing at 15% month over month. No backup processor exists for billing continuity.
Desc_Pain Point_3: Puzzle is only available in the United States. As the platform eyes international expansion, it has zero local payment methods for non-U.S. markets. No SEPA, Pix, UPI, or iDEAL for global startups needing AI accounting.
Desc_Pain Point_4: Startups have high churn rates. Failed card payments on $79 to $199/month subscriptions cause involuntary churn. Without smart retry logic or failover routing, every decline risks losing a customer permanently.
Desc_Pain Point_5: Puzzle recommends Stripe for invoicing but cannot receive payments directly. This creates a split workflow where accounting lives in Puzzle but payment collection requires a separate Stripe dashboard. No unified payment view exists.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary billing processor and invoicing partner)
PSP_2: Plaid (bank connections for 12,000+ institutions)
PSP_3: ACH (via bank integrations)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (EU)
Local_M_2: Pix (Brazil)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BLIK (Poland)
Local_M_6: Bancontact (Belgium)
Local_M_7: KakaoPay (South Korea)
Local_M_8: PayPay (Japan)
Local_M_9: Boleto (Brazil)
Local_M_10: OXXO (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription payment to the optimal acquirer by card BIN and geography. With 15% monthly customer growth, every recovered decline compounds revenue. Smart routing delivers 3% to 10% auth uplift, turning failed charges into retained customers.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines a $79 or $199 subscription, Yuno reroutes in milliseconds to a backup processor. Up to 50% recovery on failed transactions, directly reducing involuntary churn across the customer base.
Desc_Yuno_Cap3: Activates the APMs international markets need when Puzzle expands beyond the U.S.: SEPA DD across Europe, Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland, Boleto in Brazil. One API, 1,000+ methods, zero per-market builds.
Desc_Yuno_Cap4: One dashboard unifying Stripe billing, Plaid bank connections, and subscription management. Real-time monitoring across Starter, Growth, and Enterprise plans. NOVA fraud engine with 75% fewer false positives. Centralized analytics for all payment flows.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Puzzle at a glance:**
- Founded: 2019 by Sasha Orloff (CEO) and John Cwikla (CTO)
- Headquarters: San Francisco, California
- Employees: 91 (as of January 2026)
- Funding: $66.5M total raised over 3 rounds from 14 investors
  - Series A: $30M led by S32 and XYZ Capital
  - Participation: General Catalyst, FOG Ventures, Felicis, Kapor Capital, Sterling Road, Born Ventures, Soma Capital, Alumni Ventures, Gaingels
  - 50+ CFO and operator angel investors
- Customer Growth: 15% new customer growth month-over-month
- Available: United States only

**Products:**
- AI Accounting Software: AI-native general ledger rebuilt from scratch
- Puzzlebot: Intelligent assistant auto-categorizing up to 90-98% of transactions
- Automated Revenue Recognition: Native Stripe integration for accrual accounting
- Month-End Close Automation: 85-95% of repetitive bookkeeping automated
- Burn Rate & Runway Tracking: Real-time financial health monitoring
- ASC 718 / SBC Reporting: Stock-based compensation compliance

**Pricing:**
- Starter Plan: $79/month (entity-based, no per-user fees)
- Growth Plan: $199/month
- Enterprise Plan: Custom pricing
- No per-user fees; unlimited view-only guests

**Integrations:**
- Payments: Stripe (native, primary)
- Banking: Mercury, Brex, Ramp, Meow, Every + 12,000 banks via Plaid
- Payroll: Gusto, Rippling, Every, Central, Deel
- Expenses: Brex, Ramp, Meow, Bill.com
- Other: QuickBooks (migration), custom APIs

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary billing processor and native invoicing integration
- Plaid: Bank account connections for 12,000+ institutions
- ACH: Via bank integrations
- Puzzle cannot receive payments directly (recommends Stripe)
- No payment orchestrator detected
- No international/local APMs detected

**Key Limitations:**
- USD only: No multi-currency support (on roadmap)
- U.S. only: Platform only available in the United States
- No multi-entity support: Single entity only
- No direct payment receipt: Must use Stripe separately for invoicing
- No international tax compliance: US-focused tax handling only

**Competitive Landscape:**
- QuickBooks: 62% market share, default for U.S. small businesses
- Xero: Cloud-native, strong international presence, 1,000+ integrations
- FreshBooks: Small business accounting with invoicing
- Wave: Free accounting for micro-businesses
- Bench (closed): Was a major competitor, shut down in late 2024
- Pilot: Bookkeeping service for startups

**Key Meeting Angles:**
1. **15% monthly growth, single-processor risk** | Rapid customer growth flowing through Stripe alone. Failover routing prevents involuntary churn from card declines on $79-$199 subscriptions.
2. **$66.5M raised, U.S.-only platform** | Well-funded AI accounting with zero international payment rails. Expansion beyond the U.S. requires multi-currency billing and local APMs.
3. **Stripe-native, Stripe-dependent** | Built natively on Stripe but no diversification. Orchestration adds resilience without replacing the core Stripe integration.
4. **Involuntary churn reduction** | SaaS subscription models lose 3-5% of revenue to failed payments monthly. Smart routing and retries recover up to 50% of those losses.
5. **85-95% automation, 0% payment flexibility** | AI automates bookkeeping brilliantly but payment collection remains rigid and single-rail.
6. **Accounting firms as multiplier** | Puzzle's partner-only model means each accounting firm brings dozens of startup clients. Payment infrastructure must scale with this network effect.

**Sources:**
- [Puzzle Official Website](https://puzzle.io)
- [Puzzle Pricing](https://puzzle.io/pricing)
- [Puzzle Integrations](https://puzzle.io/integrations)
- [Puzzle About Page](https://puzzle.io/about)
- [Puzzle $30M Fundraise](https://puzzle.io/blog/puzzle-raises-an-additional-30m-to-fuel-a-new-era-of-ai-powered-accounting)
- [Puzzle Stripe Integration](https://puzzle.io/partners/stripe)
- [Puzzle Mercury Integration](https://puzzle.io/partners/mercury)
- [Puzzle Brex Integration](https://puzzle.io/partners/brex)
- [Puzzle Help: Stripe FAQ](https://help.puzzle.io/en/articles/9426187-faq-stripe)
- [Puzzle Help: Accounts Receivable](https://help.puzzle.io/en/articles/9359018-faq-accounts-receivable)
- [Puzzle Help: Invoicing](https://help.puzzle.io/en/articles/10246150-invoicing-in-puzzle)
- [Puzzle Help: Integrations FAQ](https://help.puzzle.io/en/articles/9155896-faq-integrations)
- [Puzzle Help: Pricing FAQ](https://help.puzzle.io/en/articles/8891734-faq-pricing)
- [Puzzle Review (Tofu Blog)](https://www.gotofu.com/blog/puzzle-io-review)
- [Puzzle Tracxn Profile](https://tracxn.com/d/companies/puzzle/__S4yCZBnPr-mpGqg7hbrU72aQdTnrSDtmsEqXuDcw_v8)
- [Puzzle Brandfetch Logo](https://brandfetch.com/puzzlefinancial.com)
- [Puzzle QuickBooks Alternatives](https://puzzle.io/blog/quickbooks-alternatives-for-startups)
