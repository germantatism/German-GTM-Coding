# TOGETHER AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Together AI
=======================================

Logo: https://brandfetch.com/together.ai
Nombre merchant: Together AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Global Billing
Tittle_Pain Point_2: Usage Billing Complexity
Tittle_Pain Point_3: Single PSP Dependency
Tittle_Pain Point_4: Enterprise Invoice Gaps
Tittle_Pain Point_5: Cross-Border FX Friction

Desc_Pain Point_1: Together AI serves 450K+ developers globally but relies on third-party payment processor(s) accepting only card-based payments. Developers in markets like India, Brazil, Southeast Asia, and Africa where cards are secondary cannot self-serve onto the platform without international cards.
Desc_Pain Point_2: Per-token, per-minute, and per-image pricing across 200+ models creates complex metered billing. Auto-replenishment charges the stored payment method when balances drop below threshold. Any payment failure on replenishment immediately disrupts active API workloads for the customer.
Desc_Pain Point_3: Together AI uses unnamed third-party payment processor(s) with no confirmed failover. A single processor outage or decline spike blocks account top-ups and auto-replenishments for developers running production AI workloads that depend on continuous API access.
Desc_Pain Point_4: Enterprise customers like Salesforce, Zoom, and SK Telecom likely require invoiced billing, multi-currency settlement, and procurement-friendly payment rails. Scaling from developer self-serve to enterprise contracts demands flexible payment infrastructure beyond card-on-file.
Desc_Pain Point_5: $300M ARR platform billing developers across 100+ countries in USD. International developers face cross-border card fees, issuer fraud blocks on US-originated charges, and 3DS friction that adds steps to the auto-replenishment flow for prepaid balances.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (likely primary, attending Stripe Sessions, standard AI SaaS processor)
PSP_2: Lago (open-source billing/metering platform, deployed on-premise for usage tracking)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: iDEAL
Local_M_5: Boleto
Local_M_6: GCash
Local_M_7: GrabPay
Local_M_8: BLIK
Local_M_9: Konbini
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Auto-Retry
Tittle_Yuno_Cap3: Global Payment Methods
Tittle_Yuno_Cap4: Unified Payment Analytics

Desc_Yuno_Cap1: Per-transaction routing optimizes every prepaid top-up and auto-replenishment based on card BIN, issuer country, and charge amount. With $300M+ ARR from 450K+ developers, even 3% auth uplift on account replenishments prevents API disruptions and recovers significant revenue from failed charges.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor dependency. When the primary processor declines a developer's balance replenishment, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions, preventing API access interruptions for production workloads.
Desc_Yuno_Cap3: One API activates 1,000+ local payment methods for Together AI's global developer base: UPI for Indian AI developers, Pix for Brazil, SEPA DD for European enterprises, GrabPay/GCash for SEA, Konbini for Japan. Developers pay using methods they trust, removing card-only barriers to adoption.
Desc_Yuno_Cap4: NOVA intelligence provides one dashboard across all payment processors. Real-time approval rate monitoring for prepaid and auto-replenishment charges, centralized decline analytics by developer cohort and region, 75% faster fraud detection. Replaces fragmented processor reporting.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Together AI at a glance:**
- Founded: June 2022 by Vipul Ved Prakash (CEO), Ce Zhang (CTO), Chris Re, Percy Liang, Tri Dao (Chief Scientist)
- Headquarters: San Francisco, CA
- Employees: 355 (as of March 2026)
- Revenue: ~$300M annualized (September 2025 estimate via Sacra), up from $130M at end of 2024
- Funding: $533.5M total raised; $305M Series B (February 2025) led by General Catalyst, valuation $3.3B
- Investors: Salesforce Ventures, Nvidia, General Catalyst, Prosperity7, Kleiner Perkins, Coatue, Lux Capital
- Users: 450,000+ AI developers, plus enterprises (Salesforce, Zoom, SK Telecom, Zomato, The Washington Post)
- Products: Serverless Inference (200+ models), Dedicated Inference, GPU Clusters, Fine-Tuning, Agentic Workflows
- Pricing: Pay-as-you-go per million tokens ($0.05 to $7.00), GPU hourly rates ($3.49 to $9.95/hr)
- Available on AWS Marketplace
- Team behind FlashAttention and ThunderKittens (kernel optimization research)

**Confirmed payment stack:**
- Third-party payment processor(s): Not named in ToS, likely Stripe (attending Stripe Sessions, standard for AI SaaS)
- Lago: Open-source billing/metering platform deployed on-premise for usage tracking across serverless, dedicated, GPU clusters, and fine-tuning
- Prepaid balance model with auto-replenishment when balance drops below threshold
- All fees non-refundable per ToS
- No payment orchestrator detected
- Enterprise likely invoiced separately for Salesforce/Zoom/SK Telecom-class accounts

**Payment challenges identified:**
- Card-only acceptance limits self-serve adoption in non-card-dominant markets
- Auto-replenishment failures disrupt active production AI workloads immediately
- Complex metered billing (per-token, per-minute, per-image) across 200+ models
- Cross-border card fees and issuer fraud blocks on USD charges from international developers
- Enterprise accounts need invoiced billing, multi-currency settlement, procurement-friendly rails
- No confirmed processor failover for a $300M+ ARR platform
- 450K+ developer global base spans markets with vastly different payment preferences

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, AI developer community)
  Accepted: Credit/debit cards via payment processor
  Missing: ACH Direct Debit, PayPal
  Well-served by cards, but ACH would benefit enterprise/high-volume developer accounts.

MARKET 2: India (massive AI developer community, Zomato is a customer)
  Accepted: International cards
  Missing: UPI, RuPay, net banking, Paytm
  75%+ of Indian digital payments use UPI. Most Indian developers lack international cards for US-originated charges.

MARKET 3: Europe (enterprise customers, GDPR-conscious market)
  Accepted: International cards
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BLIK, Giropay
  SEPA DD preferred for recurring API billing. Enterprise procurement often requires local invoicing.

MARKET 4: Brazil (growing AI adoption market)
  Accepted: International cards
  Missing: Pix, Boleto, local installment cards
  Pix handles 70%+ of Brazil digital payments. Brazilian developers face card issuer blocks on US charges.

MARKET 5: Southeast Asia (SK Telecom customer, growing AI hub)
  Accepted: International cards
  Missing: GrabPay, GCash, DANA, ShopeePay, PromptPay
  Mobile wallets dominant in SEA. Developer self-serve capped at international card holders.

**Key meeting angles:**
1. **$300M ARR at scale** | Every basis point of payment conversion directly impacts a $300M+ revenue stream
2. **450K developer self-serve** | Massive volume of prepaid top-ups and auto-replenishments that benefit from smart routing
3. **Auto-replenishment critical path** | Failed payment = instant API disruption for production workloads; failover prevents this
4. **Global developer base, card-only** | Developers in India, Brazil, SEA cannot self-serve without international cards
5. **Enterprise scaling** | Moving from developer self-serve to Salesforce/Zoom-class enterprise contracts needs flexible payment rails
6. **$3.3B valuation pressure** | Investors expect infrastructure maturity; payment orchestration is part of that story
7. **Competitor comparison** | OpenAI, Anthropic, and Google Cloud offer broader payment options for API billing

**Sources:**
- [Together AI Homepage](https://www.together.ai)
- [Together AI Pricing](https://www.together.ai/pricing)
- [Together AI About Us](https://www.together.ai/about-us)
- [Together AI Terms of Service](https://www.together.ai/terms-of-service)
- [Together AI $305M Series B Announcement](https://www.together.ai/blog/together-ai-announcing-305m-series-b)
- [Sacra: Together AI Revenue & Valuation](https://sacra.com/c/together-ai/)
- [Together AI Valuation $3.3B (Crunchbase News)](https://news.crunchbase.com/cloud/together-ai-valuation-jump-general-catalyst-nvda/)
- [Together AI Billing Docs](https://docs.together.ai/docs/gpu-clusters-billing)
- [Lago Customers (Together AI mentioned)](https://www.getlago.com/customers/together-ai)
- [TapTwice: Together AI Statistics](https://taptwicedigital.com/stats/together-ai)
- [Vipul Ved Prakash (CEO) LinkedIn](https://www.linkedin.com/in/vipulved/)
