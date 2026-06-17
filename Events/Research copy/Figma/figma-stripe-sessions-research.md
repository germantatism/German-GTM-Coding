# FIGMA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Figma
════════════════════��══════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg
Nombre merchant: Figma

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP at $1B+ Scale
Tittle_Pain Point_2: Currency Routing Errors
Tittle_Pain Point_3: Hybrid Billing Complexity
Tittle_Pain Point_4: India Checkout Gap
Tittle_Pain Point_5: Card Decline Spiral

Desc_Pain Point_1: 100% of $1.05B revenue flows through Stripe with zero fallback. Post-IPO, any Stripe outage blocks all Pro, Org, and Enterprise billing globally.
Desc_Pain Point_2: Figma Forum confirms "can't pay in USD" errors for international cards. 85% of users are outside the US; cross-border routing friction causes conversion loss.
Desc_Pain Point_3: AI credit usage billing launched March 2026 alongside seat subscriptions. Combining metering with recurring billing strains single PSP infrastructure.
Desc_Pain Point_4: India is #2 traffic market (10% of visits) with a Bengaluru office, but no UPI, RuPay, or INR local acquiring confirmed. Cross-border declines hit hardest here.
Desc_Pain Point_5: Figma Forum shows repeated "Your card has been declined" errors across multiple threads. Users report trying 3+ cards with the same generic decline message.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: N/A
PSP_3: N/A
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: Boleto
Local_M_4: RuPay
Local_M_5: Konbini
Local_M_6: PayPay
Local_M_7: OXXO
Local_M_8: BLIK
Local_M_9: GCash
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and market. With $1.05B revenue and 85% international users across 180+ countries, routing each renewal to the best local acquirer delivers 3 to 10% auth uplift. Livelo achieved +5% approval via Yuno smart routing.
Desc_Yuno_Cap2: Automatic cascade eliminates Figma's 100% Stripe dependency. When Stripe declines a Professional plan renewal, Yuno reroutes instantly to the next best acquirer. Up to 50% recovery on failed transactions. Zero customer friction, zero downtime.
Desc_Yuno_Cap3: Activates the APMs Figma users need: UPI and RuPay in India (#2 market), Pix in Brazil, Konbini and PayPay in Japan, OXXO in Mexico, BLIK in Poland, GCash in Philippines. One API, 1,000+ methods. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard managing Stripe alongside new local acquirers. Real-time approval monitoring across all markets, centralized reconciliation for seat subscriptions and AI credit billing, NOVA AI recovering 75% of failed renewals via automated outreach.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Figma at a glance:**
- Founded: 2012, HQ: San Francisco, CA
- IPO: July 2025 (NYSE: FIG, priced at $33/share, ~$19.3B valuation at IPO)
- Current market cap: ~$10.6B (April 2026, stock at ~$18.92)
- Revenue: $1.05B (FY2025, +41% YoY), FY2026 guide: $1.37B
- Monthly Active Users: 10M+ worldwide, 85% outside the US
- 53% of revenue from non-US markets
- 1,031 customers at $100K+ ARR (up 47% YoY), 11,107 at $10K+ ARR
- 95% of Fortune 500 use Figma
- Products: Figma Design, FigJam, Dev Mode, Figma Make (AI), Figma Sites, Figma Draw, Figma Buzz
- AI credits usage-based billing launched March 2026
- Acquired Weavy (Israel, $200M+, Oct 2025), rebranded as Figma Weave
- Offices: SF, NYC, London, Seattle, Paris, Berlin, Tokyo, Singapore, Sydney, Bengaluru (Nov 2025)
- CEO: Dylan Field (Co-Founder)
- Adobe $20B acquisition blocked Dec 2023 (UK/EU regulators, $1B breakup fee)

**Confirmed PSPs:**
- Stripe: sole PSP (confirmed via Stripe case study, Stripe Payments + Billing + Invoicing + Optimized Checkout Suite)
- Completed billing model re-architecture on Stripe in May 2025
- Finance team managing payments: fewer than 5 people
- No payment orchestrator detected
- No secondary PSP or acquirer found

**Confirmed Payment Methods:**
- Credit card, debit card (Professional plan)
- SEPA Direct Debit (Europe, Professional plan)
- Wire transfer / ACH: Enterprise only via invoice
- PayPal: explicitly NOT available
- 5 currencies confirmed: USD, EUR, GBP, CAD, JPY

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~13% of traffic, ~47% of revenue)
  Currently offer: Visa/MC/Amex, SEPA (EU)
  Missing: ACH (self-serve), PayPal
  Impact: Enterprise ACH only via invoice. Self-serve ACH would reduce card processing costs.

MARKET 2: India (~10% of traffic, 11.6M monthly visits)
  Currently offer: Visa/MC (cross-border through Stripe)
  Missing: UPI, RuPay, Paytm, PhonePe, NetBanking
  Impact: UPI handles 80%+ of Indian digital payments. Bengaluru office opened Nov 2025 but no local payment entity confirmed.

MARKET 3: Russia (~9% of traffic)
  Currently offer: Limited (sanctions complexity)
  Missing: Mir, SBP (System of Fast Payments)
  Impact: Sanctions era constraints limit payment routing. Material traffic with no confirmed local options.

MARKET 4: Germany (confirmed office)
  Currently offer: SEPA Direct Debit, credit cards
  Missing: Klarna, Giropay
  Impact: SEPA covers basics; Klarna would add BNPL for annual plan upgrades.

MARKET 5: Brazil (Portuguese localization live)
  Currently offer: Credit/debit cards (cross-border)
  Missing: Pix, Boleto Bancario
  Impact: Pix handles 70%+ of Brazilian digital payments. Full Portuguese UI but no local payment rails confirmed.

**Payment complaint evidence:**
- Figma Forum: "Your card has been declined" errors across multiple threads (2024 to 2026)
- Figma Forum: "Can't pay in USD" currency routing error for international users
- Figma Forum: inability to update payment method without contacting support
- Trustpilot: unexpected seat upgrade charges, dark pattern on downgrade flow, post-cancellation billing
- Figma support acknowledges "most declines are generic" and cannot determine exact reason

**Key meeting angles:**
1. **$1B+ SaaS on a single PSP post-IPO** | Zero redundancy for 100% of revenue creates material risk flagged in public company reporting
2. **85% international users, 53% international revenue** | Cross-border acquiring costs and decline rates compound at this scale
3. **India is #2 market with zero local APMs** | Bengaluru office opened Nov 2025 but no UPI, no RuPay, no INR local acquiring
4. **Currency routing errors confirmed** | Forum threads prove international checkout friction exists today
5. **AI billing complexity** | Hybrid subscription + usage-based model launched March 2026 strains single-PSP billing infrastructure
6. **Sub-5 person finance team** | Lean team managing $1B+ in payments needs automation, not more manual processes
7. **Competitor gap** | Canva already has 20+ APMs via Stripe; Figma lags significantly in local method coverage

**Sources:**
- [Stripe: Figma Case Study](https://stripe.com/customers/figma)
- [Figma Help: Manage Payment Details](https://help.figma.com/hc/en-us/articles/360040532093)
- [Figma Help: Pay for Figma](https://help.figma.com/hc/en-us/articles/10278790616215)
- [Figma Help: Billing Guide](https://help.figma.com/hc/en-us/articles/29717597009431)
- [Figma Forum: Card Declined](https://forum.figma.com/report-a-problem-6/the-card-was-declined-48598)
- [Figma Forum: Can't Pay in USD](https://forum.figma.com/report-a-problem-6/your-payment-method-s-address-is-in-a-country-that-can-t-pay-in-usd-please-use-a-different-payment-method-48965)
- [Figma Forum: Payment/Billing Address](https://forum.figma.com/report-a-problem-6/problems-with-payment-and-billing-address-43883)
- [Trustpilot: Figma Reviews](https://www.trustpilot.com/review/figma.com)
- [Figma Investor Relations: Q4 2025 Earnings](https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx)
- [Fortune: Figma IPO](https://fortune.com/2025/07/02/figma-ipo-s-1-filing-growth-profitability-dual-class-share-structure-dylan-field-nyse-fig/)
- [TechCrunch: Figma India Office](https://techcrunch.com/2025/11/12/figma-bets-on-india-to-expand-beyond-design/)
- [Fueler: Figma Statistics 2026](https://fueler.io/blog/figma-usage-revenue-valuation-growth-statistics)
- [SQ Magazine: Figma Statistics 2026](https://sqmagazine.co.uk/figma-statistics/)
- [Sacra: Figma Revenue](https://sacra.com/c/figma/)
