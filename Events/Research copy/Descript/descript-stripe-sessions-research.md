# DESCRIPT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════���═══════════════
DATABASE FIELDS: Descript
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/0/04/Descript_%28Icon%29.svg
Nombre merchant: Descript

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Billing
Tittle_Pain Point_2: Card-Only Checkout
Tittle_Pain Point_3: AI Credit Overage Risk
Tittle_Pain Point_4: Single Acquirer Lock
Tittle_Pain Point_5: Global Creator Barrier

Desc_Pain Point_1: USD-only billing. Stripe auto-converts at bank FX rates, adding markups to every charge for 1.5M+ users. Churn compounds on $16 to $50/mo plans.
Desc_Pain Point_2: Only cards and Stripe Link accepted. No PayPal, no bank transfers, no local wallets. Creators where card penetration is under 30% cannot subscribe.
Desc_Pain Point_3: 2025 pricing overhaul added metered AI credit top-ups. Variable-amount charges on international cards face higher decline rates, unpredictable loss.
Desc_Pain Point_4: Stripe is the sole processor. At ~$100M ARR with 1.5M users, any degradation blocks all signups, renewals, and AI credit purchases globally.
Desc_Pain Point_5: Not every country is Stripe-supported. Creators in excluded markets are locked out. Video/podcast creation is global; Descript's payments are not.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Stripe Link (wallet)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: SEPA Direct Debit
Local_M_4: PayPal
Local_M_5: BLIK
Local_M_6: iDEAL
Local_M_7: Boleto
Local_M_8: OXXO
Local_M_9: Konbini
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal and AI credit purchase to the optimal acquirer for that card BIN and geography. At ~$100M ARR with 75% YoY growth, a 3% auth uplift recovers $3M+ annually. Smart Routing optimizes both recurring and metered charges.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a creator's payment. Yuno reroutes to the next best processor in milliseconds. For a creator mid-edit on a deadline, a failed AI credit purchase means lost productivity and potential churn. Up to 50% recovery rate.
Desc_Yuno_Cap3: Opens Descript to the global creator economy: UPI in India, Pix in Brazil, SEPA DD across Europe, BLIK in Poland, iDEAL in Netherlands, OXXO in Mexico, PayPal for users who prefer it. One API, 1,000+ payment methods. No engineering effort per market.
Desc_Yuno_Cap4: One dashboard unifying subscription billing and AI credit metering across all processors and geographies. Real-time approval rate monitoring, centralized reconciliation for the new media minutes + AI credits model, and instant anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Descript at a glance:**
- 1.5M+ active users, 12-15% conversion to paid plans
- Revenue: ~$100M ARR (2026), up from $55M ARR (late 2024), ~75% YoY growth
- AI-powered video/audio/podcast editor with text-based editing, transcription, screen recording
- Pricing (2026): Free, Hobbyist ($16/mo annual), Creator ($24/mo annual), Business ($50/mo annual), Enterprise (custom)
- September 2025 pricing overhaul replaced "transcription hours" with "media minutes" and introduced metered AI credit top-ups
- Total funding: $104M. Series C: $50M (November 2022) led by OpenAI Startup Fund, with a16z, Redpoint, Spark Capital
- Estimated valuation: $550M to $650M (private, based on 5-6x ARR multiple)
- 188 employees (March 2026). HQ: San Francisco
- CEO: Andrew Mason (founder of Groupon)
- OpenAI is an investor and strategic partner

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed in help docs: "Stripe is Descript's payments processor")
- Stripe Link: accepted as payment method alongside credit cards
- Invoice billing: Enterprise plans only, supports ACH transfer
- Bills in USD only. Stripe auto-converts international currencies.
- Not every country supported by Stripe is available
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market, HQ)
  Accepted: Visa/MC/Amex, Stripe Link
  Missing: ACH (non-Enterprise), PayPal, Cash App Pay
  Note: Primary revenue market. Creators, podcasters, YouTubers are core users.

MARKET 2: India (large creator economy)
  Accepted: Visa/MC (international USD)
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: India's creator economy is booming. YouTube India is the #1 market by users. Descript's target audience exists but cannot pay.

MARKET 3: Brazil (growing creator market)
  Accepted: Visa/MC (USD)
  Missing: Pix, Boleto, local installment cards
  Note: Brazil has one of the largest YouTube/podcast communities in LATAM. Pix handles 70%+ of digital payments.

MARKET 4: Europe (UK, Germany, France)
  Accepted: Visa/MC/Amex (USD)
  Missing: SEPA Direct Debit, iDEAL, BLIK, Sofort, Bancontact
  Note: European podcasters and video creators are a growing segment. SEPA DD is standard for subscription billing.

MARKET 5: Japan/Asia Pacific
  Accepted: Visa/MC (USD)
  Missing: Konbini, PayPay, Line Pay, GrabPay
  Note: Japan's podcast market is emerging. Konbini is essential for Japanese digital subscriptions.

**Key meeting angles:**
1. **Creator economy payments** | 1.5M creators, 75% growth, but card-only checkout filters out the global creator base
2. **OpenAI-backed** | Strategic investor validates AI-first approach. Payment infrastructure should match the AI ambition.
3. **AI credits model** | September 2025 overhaul added metered AI credits. Variable charges face higher international decline rates.
4. **PayPal absence is notable** | A creator tool that doesn't accept PayPal misses a massive user preference segment
5. **USD-only billing** | Every international creator pays FX markup. Local currency billing reduces friction and churn.
6. **Enterprise growth** | Custom pricing and invoice/ACH for Enterprise. Multi-currency, multi-method support accelerates global Enterprise deals.
7. **Groupon founder's DNA** | CEO Andrew Mason understands marketplaces and payments from Groupon experience. Payments conversation has executive relevance.

**Sources:**
- [Descript Help: Payment Methods](https://help.descript.com/hc/en-us/articles/10255834199437-Manage-and-update-your-payment-method)
- [Descript Help: How Billing Works](https://help.descript.com/hc/en-us/articles/10255874128397-How-billing-works-in-Descript)
- [Descript Pricing](https://www.descript.com/pricing)
- [Descript Privacy Policy](https://www.descript.com/privacy)
- [Descript Security](https://www.descript.com/security)
- [Descript Terms of Service](https://www.descript.com/terms)
- [Descript Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Descript_(Icon).svg)
- [Sacra: Descript Revenue & Funding](https://sacra.com/c/descript/)
- [Tracxn: Descript Company Profile](https://tracxn.com/d/companies/descript/__vF948CDG-Kh3N00CfMczYLzLCnpIqW3JvPsaCVEZfPU)
- [Crunchbase: Descript](https://www.crunchbase.com/organization/descript)
- [Growjo: Descript Revenue & Competitors](https://growjo.com/company/Descript)
- [Miracuves: Descript Revenue Model 2026](https://miracuves.com/blog/descript-clone-revenue-model/)
- [Tekpon: Descript Pricing 2026](https://tekpon.com/software/descript/pricing/)
- [MeetGeek: Descript Pricing Review 2026](https://meetgeek.ai/blog/descript-pricing)
- [CostBench: Descript Pricing](https://costbench.com/software/ai-video-generators/descript/)
