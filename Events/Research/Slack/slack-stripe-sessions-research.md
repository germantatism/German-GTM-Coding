# SLACK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Slack
=======================================

Logo: https://a.slack-edge.com/80588/marketing/img/icons/icon_slack_hash_colored.png
Nombre merchant: Slack

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Global Billing
Tittle_Pain Point_2: Invoice Manual Overhead
Tittle_Pain Point_3: APAC Payment Gaps
Tittle_Pain Point_4: Auth Rate Plateau
Tittle_Pain Point_5: Failed Payment Churn

Desc_Pain Point_1: Slack accepts cards and US ACH only. No SEPA, BACS, Konbini, or local transfers for 40%+ international users. Germany, Japan, Brazil buyers face friction.
Desc_Pain Point_2: Self-serve invoices need annual billing and 58+ seats (Pro) or 28+ (Business+). Smaller workspaces cannot invoice, forcing manual payment reconciliation.
Desc_Pain Point_3: Japan is Slack's #2 market, yet no Konbini, PayPay, or bank transfer. APAC is 40% of new users in 2026 but checkout offers zero local methods beyond cards.
Desc_Pain Point_4: Slack cites 99% auth via Stripe, but 1% on millions of enterprise subscriptions is significant lost revenue. No multi-acquirer routing to push rates higher.
Desc_Pain Point_5: Failed payments trigger workspace downgrades. Help docs guide users to retry the same card. No automated retry across alternative processors to recover revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary global processor) PSP_2: ACH via Stripe PSP_3: Apple Pay (US/Canada only, rolling out)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (EU)
Local_M_2: BACS Direct Debit (UK)
Local_M_3: Konbini (Japan)
Local_M_4: PayPay (Japan)
Local_M_5: Boleto (Brazil)
Local_M_6: Pix (Brazil)
Local_M_7: iDEAL (Netherlands)
Local_M_8: Bancontact (Belgium)
Local_M_9: UPI (India)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Billing Dashboard

Desc_Yuno_Cap1: Route each subscription renewal to the optimal acquirer by card BIN, issuer, and currency. With 47M+ daily users across 150+ countries, even 0.5% auth uplift recovers millions in annual revenue. Smart Routing delivers +3-10% improvement.
Desc_Yuno_Cap2: When Stripe declines a renewal or experiences downtime, Yuno cascades automatically to alternative processors in milliseconds. NOVA AI recovers 75% of soft declines before they trigger workspace downgrades. Livelo recovered 50% of failed transactions with Yuno failover.
Desc_Yuno_Cap3: Unlock SEPA Direct Debit for EU enterprises, BACS for UK, Konbini and PayPay for Japan (Slack's #2 market), Pix and Boleto for Brazil, UPI for India. One API integration activates every local method across all of Slack's global markets. InDrive deployed 10 markets through Yuno.
Desc_Yuno_Cap4: Replace single-processor visibility with a centralized dashboard spanning every acquirer, method, and market. Monitor subscription auth rates per region, track failed payment recovery in real time, and detect anomalies before they cascade into churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Slack at a glance:**
- Owned by Salesforce (acquired July 2021 for $27.7B)
- 47.2M daily active users, 79M monthly active users (2026)
- Revenue: $2.3B in latest fiscal year under Salesforce (14% YoY growth); Salesforce CEO projects $3B for 2026
- 215,000+ organizations use Slack; 77% of Fortune 100
- Second-largest market: Japan; Europe and APAC account for nearly 40% of new users in 2026
- Net revenue retention rate: 132%
- Average revenue per user (ARPU): $425/year; Enterprise Grid clients average $1,100+/seat
- Enterprise customers include Amazon, IBM, HSBC, Uber, Airbnb, Target

**Confirmed PSPs:**
- Stripe: primary global payment processor for all subscription billing
- ACH bank debiting (US only, via Stripe)
- Apple Pay: rolling out for US and Canadian workspaces
- Self-serve invoice payments via check or direct deposit (for qualifying workspaces)
- No multi-PSP setup detected; Stripe is single-provider for card processing
- No third-party payment orchestrator detected (no Spreedly, Primer, Gr4vy, or Yuno)

**Supported Payment Methods (as of 2026):**
- Credit cards: Visa, Mastercard, American Express, JCB, Maestro, Discover, Diners
- ACH bank transfer (US only)
- Apple Pay (US/Canada, gradual rollout)
- Self-serve invoices (check or direct deposit, annual billing only, minimum seat thresholds)
- No debit card explicit support outside credit card networks
- No wire transfers listed as supported

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market, HQ in San Francisco)
  Offer: Visa, MC, Amex, Discover, JCB, Maestro, Diners, ACH bank transfer, Apple Pay
  Missing: PayPal, Venmo, Cash App Pay
  Why it matters: ACH covers enterprise bank payments; Apple Pay rollout is partial. PayPal has 430M+ global accounts and is a preferred method for many SMBs.

MARKET 2: Japan (second-largest market, fastest growing)
  Offer: Visa, MC, Amex, JCB, Maestro credit cards only
  Missing: Konbini (7-Eleven, Lawson, FamilyMart), PayPay (63M+ users), LINE Pay, Rakuten Pay, bank transfer (furikomi)
  Why it matters: Japan is Slack's biggest growth market. Konbini is used by millions who prefer cash-based payment. PayPay dominates mobile payments. Cards-only checkout leaves significant conversion on the table.

MARKET 3: United Kingdom (major enterprise market)
  Offer: Visa, MC, Amex, JCB, Maestro credit cards only
  Missing: BACS Direct Debit, Open Banking, PayPal, Google Pay, Apple Pay (not available in UK)
  Why it matters: BACS is the standard for recurring B2B payments in the UK. Enterprise procurement teams expect direct debit options for SaaS subscriptions.

MARKET 4: Germany (strong enterprise market in EU)
  Offer: Visa, MC, Amex, JCB, Maestro credit cards only
  Missing: SEPA Direct Debit, Giropay, PayPal, Klarna
  Why it matters: SEPA Direct Debit is the standard recurring payment method for B2B in Europe. PayPal is used by 57% of German online shoppers. Cards-only billing creates procurement friction for enterprise accounts.

MARKET 5: Brazil (growing LATAM market)
  Offer: Visa, MC, Amex, JCB, Maestro credit cards only
  Missing: Pix, Boleto Bancario, Mercado Pago
  Why it matters: Pix processes 4B+ transactions monthly in Brazil. Boleto is essential for B2B billing. Credit card penetration in Brazil is lower than US/EU, making local methods critical for conversion.

**Billing and Payment Challenges:**
- Early Slack history: company leaders recognized payments were mission critical but fraught with complexity
- Relied on manual processes for invoice generation (time consuming, error prone)
- Needed to simplify checkout flow and eliminate unnecessary steps weighing on conversion and auth rates
- Stripe helped set up and optimize payments in 15 countries
- Shorter checkout page (Payment Element + Address Element) increased paid plan conversion by 3.1%
- Failed or late payments still trigger workspace downgrades; recovery relies on users manually retrying same card
- Data residency: all Slack data resides on AWS in the US, creating concerns for customers with strict data sovereignty requirements

**Key meeting angles:**
1. **Japan growth vs. payment coverage gap**: Japan is Slack's #2 market and fastest growing, yet zero local payment methods are offered. Yuno activates Konbini, PayPay, LINE Pay, and bank transfers without any Slack engineering.
2. **Single-PSP risk**: Slack runs 100% of billing through Stripe. Any Stripe outage or rate change impacts the entire revenue stream. Multi-PSP orchestration through Yuno adds resilience and negotiating leverage.
3. **Enterprise SEPA/BACS gap**: 40% of new users are in Europe and APAC. Enterprise procurement in UK (BACS) and EU (SEPA) expects direct debit for SaaS subscriptions. Missing these creates friction in six-figure enterprise deals.
4. **Failed payment recovery**: When subscriptions fail, workspaces downgrade. Yuno's NOVA recovers 75% of soft declines automatically, preventing involuntary churn before users even notice.
5. **Salesforce Commerce Cloud alignment**: Salesforce (Slack's parent) already integrates with multiple PSPs (Adyen, Stripe, Cybersource, Braintree) via Commerce Cloud. Yuno orchestration aligns with Salesforce's existing multi-PSP philosophy.
6. **$3B revenue protection**: At projected $3B revenue and 132% net retention, even 1% improvement in payment success translates to $30M+ in protected annual recurring revenue.

**Slack Leadership:**
- Denise Dresser: CEO of Slack (since 2024)
- Marc Benioff: Salesforce CEO (Slack's parent company)
- Stewart Butterfield: Slack co-founder (departed Salesforce January 2023)
- Jonathan Gan: mentioned in Stripe case study for accounting and revenue operations

**Recent corporate developments:**
- Apr 2026: Salesforce CEO projects Slack revenue to reach $3B in 2026
- Jun 2025: Updates to Slack plan pricing; Business+ price increased; new Enterprise+ plan launched
- 2025: Slack AI features expanded across all paid plans
- 2025: Slack Connect contributed $260M in revenue from paid features
- 2025: App integrations and ecosystem partnerships generated $180M (up 20% YoY)
- 2025: Europe and APAC accounted for nearly 40% of new users
- 2024: Denise Dresser appointed CEO of Slack
- Ongoing: 215,000+ organizations; 77% of Fortune 100 adoption

**Sources:**
- [Slack Uses Stripe Case Study (Stripe)](https://stripe.com/customers/slack)
- [Slack Deploys Stripe Globally (Stripe Newsroom)](https://stripe.com/newsroom/stories/slack)
- [Slack Supported Payment Methods (Slack Help)](https://slack.com/help/articles/360002038947-Supported-payment-methods)
- [Slack Failed or Late Payments (Slack Help)](https://slack.com/help/articles/115004492008-Failed-or-late-payments)
- [Slack Plan and Billing Management (Slack Help)](https://slack.com/help/articles/218915087-Manage-your-Slack-plan-and-billing-details)
- [Slack Pricing Plans (Slack)](https://slack.com/pricing)
- [Slack Statistics 2026 (DemandSage)](https://www.demandsage.com/slack-statistics/)
- [Slack Revenue and Usage Statistics 2026 (Business of Apps)](https://www.businessofapps.com/data/slack-statistics/)
- [Slack in 2026 Statistics (Fueler)](https://fueler.io/blog/slack-usage-revenue-valuation-growth-statistics)
- [Salesforce CEO: Slack Revenue $3B (247 Wall St)](https://247wallst.com/investing/2026/04/01/salesforce-ceo-benioff-slack-revenue-expected-to-hit-3-billion-this-year/)
- [Salesforce Slack Acquisition FAQ (Salesforce)](https://www.salesforce.com/news/stories/faq-salesforce-completes-slack-acquisition/)
- [Slack Statistics 2025 (SQ Magazine)](https://sqmagazine.co.uk/slack-statistics/)
- [Slack Media Kit (Slack)](https://slack.com/media-kit)
- [Slack Vendor Details (Slack Help)](https://slack.com/intl/en-gb/help/articles/115005855543-Vendor-and-payment-details-for-Slack)
