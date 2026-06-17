# ATLASSIAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Atlassian
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idm3oijYMB/idVH-7OBfa.svg
Nombre merchant: Atlassian

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Self-Serve Wall
Tittle_Pain Point_2: Cross-Border Decline Spike
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: Billing Engine Migration
Tittle_Pain Point_5: Marketplace Payout Gaps

Desc_Pain Point_1: Monthly Cloud plans accept only credit cards or PayPal. No SEPA DD, iDEAL, or local bank transfers. Users say "not supporting standard methods hinders scaling."
Desc_Pain Point_2: Emerging market users report cards declined on Jira/Confluence upgrades. Banks flag $0/$1 pings as suspicious. OTP handshake failures on recurring subs block renewals.
Desc_Pain Point_3: Stripe is the sole processor for cloud subscriptions. No cascade on card declines. Failed renewals trigger workspace deactivation or forced downgrades to Free.
Desc_Pain Point_4: New billing engine migration underway for 350K+ customers. Payment disruption during cutover risks involuntary churn. Missed payments deactivate workspaces.
Desc_Pain Point_5: "Paid via Atlassian" apps run through Atlassian billing. "Paid via Vendor" forces devs to build their own. Neither supports local APMs for global buyers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (cloud subscriptions, primary)
PSP_2: PayPal (monthly cloud alternative)
PSP_3: ACH Debit (US bank accounts via Stripe)
PSP_4: Wire / Check (enterprise Net-14/Net-30)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: GiroPay
Local_M_8: Boleto
Local_M_9: SPEI
Local_M_10: KakaoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $5.7B+ revenue, 350K+ customers across 200+ countries, and Cloud growing 26% YoY, routing each renewal to the best acquirer per market delivers 3-10% auth uplift on millions of recurring subscriptions.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a Cloud renewal. Instead of deactivating workspaces after a failed retry cycle, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions prevents involuntary downgrades to Free plans.
Desc_Yuno_Cap3: Activates methods Atlassian's global base demands: SEPA DD across Europe, iDEAL in Netherlands, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, SPEI in Mexico, KakaoPay in Korea. One API, 1,000+ methods. No per-market billing sprints.
Desc_Yuno_Cap4: One dashboard unifying Stripe subscriptions, PayPal monthly billing, ACH debits, and enterprise wire transfers. Real-time approval monitoring per country, centralized reconciliation across Cloud + Marketplace, and NOVA fraud detection (75% reduction) protecting 350K+ accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Atlassian at a glance:**
- Founded: 2002 by Mike Cannon-Brookes and Scott Farquhar. HQ: Sydney, Australia (US HQ: San Francisco)
- Public: NASDAQ: TEAM
- Revenue: $5.76B (trailing twelve months ending Dec 2025), up 20.12% YoY. FY2025 total: $5.2B+
- Q2 FY2026 revenue: $1.586B, up 23% YoY
- Cloud revenue: First $1B Cloud quarter in Q2 FY2026, growing 26% YoY
- Free cash flow: $1.4B+ in FY2025
- Customers: 350,000+ across 200+ countries and territories
- Enterprise customers: 55,369 with $10K+ Cloud ARR (Q2 FY2026), up 12% YoY
- 70%+ of Fortune 500 tech companies use Jira
- Products: Jira, Confluence, Bitbucket, Trello, Jira Service Management, Loom, Rovo (AI), Guard, Atlas
- AI users: Rovo surpassed 5M monthly active users in Q2 FY2026
- Marketplace: 6,000+ apps from 1,500+ vendors
- Notable customers: NASA, Tesla, Spotify, Airbnb, AWS, Cisco, Walmart, Reddit, T-Mobile, Mercedes-Benz, Royal Caribbean, Under Armour, ExxonMobil, Cigna Healthcare

**Confirmed Payment Stack:**
- Stripe: Primary PSP for all cloud subscriptions (Jira, Confluence, Bitbucket, Trello, etc.)
- Stripe: Powers ACH Debit for US-based bank accounts (secure bank verification via Stripe)
- PayPal: Alternative for monthly cloud subscriptions
- Wire Transfer: Enterprise orders on Net-14 and Net-30 payment terms (domestic and international)
- ACH Credit: Enterprise payment terms (US)
- Paper Checks: Enterprise payment terms
- Credit/Debit cards: Visa, Mastercard, Amex
- No SEPA Direct Debit for recurring subscriptions
- No iDEAL, GiroPay, Bancontact, or other local European methods
- No local LATAM or APAC payment methods
- No payment orchestrator detected
- No multi-processor failover

**Payment Method Gaps (Community Evidence):**
- Community request: "Please support direct debit or PayPal subscriptions" for Bitbucket (unresolved)
- Users report banks blocking $0/$1 verification pings as suspicious
- Many 2026 cards require OTP/app approval for recurring subs, causing silent failures
- Bitbucket auto-downgrades to Free plan on payment decline
- Enterprise customers restricted to wire/check only (no cards on Net-14/Net-30)
- New billing engine migration creating uncertainty for 350K+ customers
- Failed payments after retry cycle deactivate entire workspaces
- No SEPA DD despite massive European customer base
- No Pix, UPI, or emerging market local methods

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest enterprise market)
  Accepted: Visa/MC/Amex, ACH Debit, PayPal, Wire, Check
  Missing: Apple Pay, Google Pay, Venmo (self-serve)
  Note: Best coverage, but single Stripe processor with no failover

MARKET 2: Europe (massive dev community, GDPR-compliant cloud)
  Accepted: Visa/MC/Amex, PayPal, Wire
  Missing: SEPA DD, iDEAL (Netherlands), Bancontact (Belgium), BLIK (Poland), GiroPay (Germany), MB Way
  Note: SEPA DD is the backbone of European subscription billing. Its absence is a critical gap for 200+ country presence.

MARKET 3: Latin America (growing dev/enterprise market)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of Brazilian digital payments. Card-only blocks self-serve upgrades.

MARKET 4: India / South Asia (massive developer population)
  Accepted: Visa/MC (cross-border), PayPal
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of Indian digital payments. OTP requirements cause recurring subscription failures.

MARKET 5: Japan / APAC (strong enterprise adoption)
  Accepted: Visa/MC (cross-border), PayPal
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: APAC dev communities are a growth vector. Local methods essential for self-serve conversion.

**Key meeting angles:**
1. **$5.7B+ revenue, 350K+ customers, single PSP** | Stripe is the sole processor for all cloud subscriptions with zero failover
2. **Billing engine migration risk** | 350K+ customers migrating to new billing. Any payment disruption during cutover drives involuntary churn
3. **Workspace deactivation on failed payment** | No cascade or smart retry. Failed renewals kill access to Jira/Confluence, the tools teams rely on daily
4. **Community demands local methods** | Users explicitly ask for SEPA DD, PayPal for more products, and direct debit. Years of unresolved requests
5. **200+ countries, card-only in most** | Massive global footprint with minimal local payment method coverage
6. **Marketplace monetization opportunity** | 6,000+ apps, "Paid via Atlassian" could benefit from local method activation for global app buyers
7. **Cloud is the growth engine** | 26% YoY Cloud growth depends on frictionless self-serve upgrades. Every payment failure is a lost conversion

**Sources:**
- [Atlassian: Payment Methods and Terms](https://www.atlassian.com/licensing/purchase-licensing/howtopay)
- [Atlassian: Manage Payment Methods](https://support.atlassian.com/subscriptions-and-billing/docs/manage-payment-methods/)
- [Atlassian: Unable to Make Payments](https://support.atlassian.com/subscriptions-and-billing/docs/unable-to-make-payments/)
- [Atlassian: Manage Subscriptions](https://support.atlassian.com/subscriptions-and-billing/docs/manage-subscriptions-and-bills-for-atlassian-cloud-products/)
- [Atlassian: Resolve Guard Payment Issue](https://support.atlassian.com/subscriptions-and-billing/docs/resolve-atlassian-guard-payment-issue/)
- [Atlassian Community: Direct Debit/PayPal Request](https://community.atlassian.com/forums/Bitbucket-questions/Please-support-direct-debit-or-paypal-subscriptions/qaq-p/3041894)
- [Atlassian Community: Credit Card Declined](https://community.atlassian.com/t5/Training-Certification-questions/Credit-card-is-declined-ACP-620/qaq-p/1713901)
- [Atlassian Community: Payment Problem](https://community.atlassian.com/forums/Trello-questions/Problem-with-payment/qaq-p/3184919)
- [Atlassian Community: Subscription Not Renewed](https://community.atlassian.com/t5/Jira-questions/Your-Atlassian-Cloud-subscription-hasn-t-been-renewed/qaq-p/960646)
- [Atlassian Community: Card Declined Trello](https://community.atlassian.com/forums/Trello-questions/Payment-Issue-The-Card-was-declined/qaq-p/2708489)
- [Atlassian Developer: Marketplace Pricing and Billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- [Stripe Newsroom: Atlassian Partnership](https://stripe.com/newsroom/news/atlassian)
- [Atlassian: About Us](https://www.atlassian.com/company)
- [Atlassian: Customers](https://www.atlassian.com/customers)
- [Atlassian: Q4 FY2025 Results](https://www.businesswire.com/news/home/20250807057757/en/Atlassian-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Results)
- [Atlassian: Q2 FY2026 Results](https://www.businesswire.com/news/home/20260205386782/en/Atlassian-Announces-Second-Quarter-Fiscal-Year-2026-Results)
- [MacroTrends: Atlassian Revenue](https://www.macrotrends.net/stocks/charts/TEAM/atlassian/revenue)
- [Brandfetch: Atlassian Logo](https://brandfetch.com/atlassian.com)
