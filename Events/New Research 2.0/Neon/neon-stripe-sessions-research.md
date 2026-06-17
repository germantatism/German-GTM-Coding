# Neon | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-28*

```
=======================================
DATABASE FIELDS: Neon
=======================================

Logo: https://neon.com/favicon/favicon.svg
Nombre merchant: Neon

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: India Billing Failure
Tittle_Pain Point_2: Card-Only Self-Service
Tittle_Pain Point_3: AWS Marketplace Removed
Tittle_Pain Point_4: No Smart Routing
Tittle_Pain Point_5: AI Agent Volume Strain

Desc_Pain Point_1: Neon docs state Indian customers cannot set up autopay due to RBI eMandate. Failed payments require manual support tickets and invoice links.
Desc_Pain Point_2: Neon billing runs on Stripe Checkout with cards only. No SEPA, iDEAL, PIX, UPI, or PayPay on self-service plans. Local-rail markets are blocked.
Desc_Pain Point_3: Neon dropped AWS Marketplace self-service billing. Customers cannot co-term Neon with AWS commits. Azure stays, but AWS path now forces cards or invoice.
Desc_Pain Point_4: With Stripe as sole acquirer, there is no smart routing per BIN, issuer, or country. Each card decline ends the renewal. No automatic cascade exists.
Desc_Pain Point_5: 80%+ of Neon databases are provisioned by AI agents. Each agent project triggers a $5 minimum. A single decline cascades into mass agent suspension.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Checkout (Self-Service)
PSP_2: Azure Marketplace Billing
PSP_3: Manual Invoice (Enterprise)
PSP_4: Cards Only (Visa, MC, Amex)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI (India)
Local_M_2: RuPay (India)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BLIK (Poland)
Local_M_6: PIX (Brazil)
Local_M_7: Boleto (Brazil)
Local_M_8: PayPay (Japan)
Local_M_9: Konbini (Japan)
Local_M_10: Alipay/WeChat Pay (China + APAC)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: India eMandate Coverage

Desc_Yuno_Cap1: Route every Launch, Scale, and Agent plan renewal to the optimal acquirer per BIN, issuer, and country. With AI agents driving 80%+ of project creation and a $5/month minimum per project, even a 3 to 10% auth lift compounds across millions of micro-tenants under Databricks.
Desc_Yuno_Cap2: When a Stripe renewal fails, Yuno cascades instantly to a backup acquirer or method. NOVA AI recovers up to 75% of soft declines before a developer or AI agent sees a database suspension. Livelo recovered 50% of failed transactions this way.
Desc_Yuno_Cap3: Activate UPI and RuPay (India), SEPA Direct Debit (EU), iDEAL, BLIK, PIX, Boleto, PayPay, Konbini, and Alipay through one API. Open the Indian developer market that today cannot autopay. Open EU enterprise that wants SEPA on Scale plans.
Desc_Yuno_Cap4: Yuno integrates RBI-compliant eMandate flows, removing the manual invoice loop Indian customers face today. Indian developers can autopay Neon Launch, Scale, and Agent plans without breaking RBI rules. Critical for Databricks's APAC growth and for Neon's AI agent thesis.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Neon at a glance:**
- Serverless Postgres database. Founded 2021 by Nikita Shamgunov, Heikki Linnakangas, Stas Kelvich
- Acquired by Databricks for ~$1B announced May 14, 2025. Closed 2025
- Core innovation: Postgres branching (database branches like git branches), instant scale-to-zero, copy-on-write storage
- Plans: Free, Launch, Scale, Agent (custom for AI agent platforms), Enterprise
- $5 per month minimum on paid plans
- Pricing post-acquisition: compute -15 to 25%, storage from $1.75 to $0.35 per GB-month, Free plan compute doubled to 100 CU-hours/month
- 80%+ of databases on Neon are provisioned automatically by AI agents (not humans)
- Strategic role at Databricks: power Lakebase and operational data layer for AI agent systems
- Distribution: direct (neon.com), Azure Marketplace (eligible for MACC). AWS Marketplace billing discontinued

**Confirmed PSPs and Payment Infrastructure:**
- Stripe Checkout: Confirmed primary billing engine for self-service plans (Free, Launch, Scale)
- Azure Marketplace: Charges go through Microsoft Azure subscription, eligible for MACC
- AWS Marketplace: No longer supported for self-service plans
- Manual invoice: Used for Enterprise and for Indian customers (post-eMandate failure)
- Cards: Visa, Mastercard, Amex via Stripe Checkout
- No PayPal, no SEPA, no iDEAL, no UPI, no PIX confirmed for self-service billing
- No payment orchestration platform (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: Americas (US, Canada, Brazil, Mexico)
  Accepted: Visa, Mastercard, Amex via Stripe
  Missing: PIX (Brazil), Boleto, OXXO, SPEI, ACH, Cash App Pay
  Note: Self-service developer base in LATAM blocked from local rails

REGION: EMEA
  Accepted: Visa, Mastercard, Amex via Stripe
  Missing: SEPA Direct Debit, iDEAL (Netherlands), BLIK (Poland), Bancontact, Trustly (Nordics), Open Banking (UK)
  Note: EU enterprise procurement standards favor SEPA. No SEPA path forces card or invoice

REGION: Asia (India, Japan, Korea, SE Asia, China)
  Accepted: Visa, Mastercard, Amex (subject to RBI restrictions in India)
  Missing: UPI (India, 350M+ users), RuPay, eMandate-compliant flows, PayPay (Japan), Konbini, KakaoPay, NaverPay, Alipay, WeChat Pay
  Note: India explicitly blocked from autopay by Neon's billing stack. Major friction for the largest developer market in APAC

**Payment Issues and Incidents:**
- India eMandate failure: Neon docs state "Customers in India cannot set up automatic monthly payments." On payment failure, customers must contact support and pay manually via an invoice link. RBI eMandate (rule on recurring card payments) is not implemented in Neon's Stripe Checkout flow
- AWS Marketplace removed: Self-service Neon plans were de-listed from AWS Marketplace. Customers committing AWS spend can no longer co-term Neon. Forces card or invoice procurement
- Cards-only on self-service: No SEPA, no PayPal, no UPI on Launch and Scale plans. Limits Neon's reach in markets where local rails are the default
- Stripe single point of failure: With Stripe as sole acquirer, a single issuer-level decline kills the renewal. No automatic cascade. For AI agent volumes (80%+ of projects), this becomes operationally critical
- $5/month minimum compounds: Every paid project carries a $5 minimum even if usage is lower. Across thousands of agent-provisioned tenants, every billing failure cascades into project suspensions

**Key meeting angles:**
1. **India is the AI agent market and Neon's billing locks it out** | India produces a massive share of global developers and AI agent workloads. Neon docs explicitly state Indian customers cannot autopay. Yuno enables RBI-compliant eMandate flows so Databricks can monetize India agentic volume cleanly.
2. **80%+ of databases are agent-provisioned, billing must be 80%+ resilient** | Each AI agent creates Postgres branches at machine speed. A single Stripe issuer block cascades into thousands of suspended agent tenants. NOVA AI recovers up to 75% of soft declines before agents see failures.
3. **Single PSP risk on Databricks's newest platform layer** | Neon is now part of Databricks's Lakebase strategy. A Stripe outage hits Databricks's reported revenue. Multi-PSP orchestration is a board-level operational hedge.
4. **Self-service global expansion needs local rails** | Stripe-only cards forces every EU, LATAM, and APAC developer onto international card rails. Yuno opens SEPA, iDEAL, BLIK, PIX, UPI, and PayPay through one API. InDrive launched 10 LATAM markets in under 8 months.
5. **Enterprise procurement wants AWS Marketplace and SEPA** | Removing AWS Marketplace fragmented procurement for committed AWS customers. Yuno's orchestration layer enables Neon to keep Stripe and add invoice + SEPA + UPI without rebuilding Stripe Checkout.

**Neon Leadership (post-acquisition):**
- Nikita Shamgunov: Co-founder and CEO, Neon
- Heikki Linnakangas: Co-founder, Postgres core contributor
- Stas Kelvich: Co-founder
- Ali Ghodsi: CEO, Databricks (parent)
- Reynold Xin: Co-founder and Chief Architect, Databricks
- Acquisition rationale: Databricks bought Neon for technology plus talent, particularly Postgres and AI agent expertise

**Recent corporate developments:**
- May 14, 2025: Databricks announced acquisition of Neon for ~$1B
- Late 2025: Compute costs dropped 15 to 25% across tiers. Storage from $1.75 to $0.35 per GB-month. Free plan doubled compute allowance
- 2025: AWS Marketplace self-service plans discontinued
- 2025 to 2026: Azure Marketplace remains (MACC-eligible)
- 2026: Databricks Lakebase strategy actively positions Neon as serverless Postgres for AI agents
- Ongoing: Agent Plan launched for AI agent platforms provisioning thousands of databases

**Sources:**
- [Databricks Agrees to Acquire Neon (Databricks)](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)
- [Databricks and Neon Blog (Databricks)](https://www.databricks.com/blog/databricks-neon)
- [Databricks Acquires Neon Press Release (PRNewswire)](https://www.prnewswire.com/news-releases/databricks-agrees-to-acquire-neon-to-deliver-serverless-postgres-for-developers--ai-agents-302454992.html)
- [Databricks Acquires Neon Analysis (TheCubeResearch)](https://thecuberesearch.com/databricks-acquires-neon-to-power-serverless-postgres-at-scale-for-the-ai-native-era/)
- [Databricks Neon Acquisition Talent (LeadGenius)](https://www.leadgenius.com/resources/databricks-didnt-just-buy-neon-for-the-tech----they-bought-the-talent)
- [Databricks Agentic AI New Persona (Futurum)](https://futurumgroup.com/insights/databricks-takes-on-agentic-ai-itself-as-a-new-user-persona-with-neon-acquisition/)
- [Databricks Acquires Neon Techzine (Techzine)](https://www.techzine.eu/news/analytics/131385/databricks-acquires-neon-serverless-postgres-database-for-ai-agents/)
- [Neon Pricing (Neon)](https://neon.com/pricing)
- [Neon Manage Billing (Neon)](https://neon.com/docs/introduction/manage-billing)
- [Neon Plans and Billing (Neon)](https://neon.com/docs/introduction/about-billing)
- [Neon Plans (Neon)](https://neon.com/docs/introduction/plans)
- [Neon AWS Marketplace (Neon)](https://neon.com/docs/introduction/billing-aws-marketplace)
- [Neon Azure Marketplace (Neon)](https://neon.com/docs/introduction/billing-azure-marketplace)
- [Neon Monitor Usage (Neon)](https://neon.com/docs/introduction/monitor-usage)
- [Neon New Usage-Based Pricing Blog (Neon)](https://neon.com/blog/new-usage-based-pricing)
- [Neon Pricing 2026 Breakdown (Vela)](https://vela.simplyblock.io/articles/neon-serverless-postgres-pricing-2026/)
- [Neon Database Review 2026 (Autonoma)](https://getautonoma.com/blog/neon-database)
- [Neon AWS Marketplace Pricing Drop (Vantage)](https://www.vantage.sh/blog/neon-acquisition-new-pricing)
- [RBI eMandate Stripe India (Chargebee)](https://www.chargebee.com/docs/payments/2.0/kb/billing/what-are-the-new-stripe-india-rbi-emandate-changes)
- [RBI Recurring Card Payments (Razorpay)](https://razorpay.com/blog/business-banking/rbi-guidelines-and-making-international-expenses/)
