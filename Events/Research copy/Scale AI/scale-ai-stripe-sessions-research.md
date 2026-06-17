# SCALE AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Scale AI
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idF5mMeONl/id42K0q_R6.svg
Nombre merchant: Scale AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Global Payout Complexity
Tittle_Pain Point_2: Annotator Payment Failures
Tittle_Pain Point_3: Multi-Currency Friction
Tittle_Pain Point_4: No Unified Payout Engine
Tittle_Pain Point_5: Enterprise Billing Gaps

Desc_Pain Point_1: Tens of thousands of annotators across Philippines, Kenya, India, Venezuela, and 30+ countries require weekly payouts. PayPal, Payoneer, and AirTM each carry high cross-border fees and limited local method coverage for emerging markets.
Desc_Pain Point_2: Widespread reports of delayed or missing payments to Remotasks and Outlier contributors. Sudden country bans (Kenya, Nigeria, Pakistan) leave workers without payout resolution. Payment failures damage workforce trust and retention.
Desc_Pain Point_3: $2B revenue flows through enterprise contracts in USD, EUR, and government procurement currencies. Annotator payouts span 30+ local currencies. No centralized FX management creates margin erosion on every cross-border settlement.
Desc_Pain Point_4: Remotasks pays via PayPal/Payoneer/AirTM. Outlier pays via PayPal/AirTM/ACH. Enterprise billing runs separately. Three parallel payout systems with no unified reconciliation, reporting, or fraud detection across the full payment lifecycle.
Desc_Pain Point_5: Enterprise and government contracts use usage-based pricing (per annotation, per task, per API call). Complex billing models spanning subscriptions, usage metering, and milestone-based government invoicing lack a unified commerce layer.

SLIDE 1: PSP TOPOLOGY

PSP_1: PayPal (annotator payouts, Remotasks and Outlier)
PSP_2: Payoneer (annotator payouts, cross-border disbursements)
PSP_3: AirTM (annotator payouts, emerging market coverage)
PSP_4: ACH (US-based contributor payouts, Outlier)
PSP_5: Enterprise invoicing (government contracts, custom billing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: M-Pesa
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: GCash
Local_M_5: GrabPay
Local_M_6: SEPA Direct Debit
Local_M_7: Boleto
Local_M_8: BLIK
Local_M_9: OPay
Local_M_10: Dana

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each payout by contributor country, currency, and amount to the lowest-cost rail. With $2B revenue and tens of thousands of annotators across 30+ countries, intelligent routing per market delivers significant cost savings on cross-border fees. Filipino workers get GCash, Kenyan contributors get M-Pesa, Indian annotators get UPI.
Desc_Yuno_Cap2: Automatic cascade when PayPal or Payoneer fails a payout. Instead of leaving contributors without payment for days, Yuno retries through the next available rail in milliseconds. Up to 50% recovery on failed disbursements. No more mass non-payment incidents that damage workforce trust.
Desc_Yuno_Cap3: Activate the local payout methods Scale's global workforce needs: M-Pesa (Kenya), UPI (India), GCash (Philippines), Pix (Brazil), OPay (Nigeria), Dana (Indonesia), BLIK (Poland). One API, 1,000+ methods. Pay annotators in their preferred local method, not just PayPal.
Desc_Yuno_Cap4: One dashboard unifying Remotasks payouts, Outlier disbursements, enterprise billing, and government contract invoicing. Real-time payout monitoring per country, centralized reconciliation across all contributor platforms, and NOVA fraud detection (75% reduction) protecting against fraudulent accounts and duplicate payouts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Scale AI at a glance:**
- Founded: 2016 by Alexandr Wang and Lucy Guo. HQ: San Francisco, California
- CEO: Jason Droege (Interim CEO since June 2025; former Uber Eats founder). Alexandr Wang departed to join Meta.
- Valuation: $29B (June 2025, following Meta investment)
- Total funding: ~$15.9B over 9 rounds from 61 investors
- Largest round: Series G, $14.3B (June 2025, Meta's 49% non-voting stake)
- Key investors: Meta (49% non-voting), Tiger Global, Founders Fund, Index Ventures, Accel, Y Combinator
- Revenue: ~$2B (2025 estimate, up from $870M in 2024)
- Employees: ~500 core staff (plus tens of thousands of gig annotators globally)
- Enterprise clients: 400+ enterprise clients, ~1,000 total customers
- Notable clients: OpenAI, Meta, Google, Microsoft, Anthropic, U.S. Department of Defense, Toyota, General Motors
- Government contracts: $250M DoD BPA, $100M CDAO OTA, $99M Army R&D contract
- Products: Scale Data Engine, Scale GenAI Platform, Scale Donovan (defense), Scale Labs (research)
- Subsidiaries: Remotasks (computer vision annotation), Outlier (LLM training data)
- Y Combinator alumnus (S16)
- Pricing: Pay-as-go (2c/image, 6c/annotation) to custom enterprise contracts

**Confirmed Payment Stack:**
- PayPal: Primary payout method for Remotasks and Outlier contributors
- Payoneer: Secondary payout for Remotasks (cross-border disbursements)
- AirTM: Alternative payout for both Remotasks and Outlier (emerging market coverage)
- ACH: US-based contributor payouts for Outlier
- Enterprise invoicing: Custom billing for enterprise and government contracts
- Usage-based billing: Per annotation, per task, per API call pricing
- Government procurement: Milestone-based invoicing for DoD/Army contracts
- No payment orchestrator detected
- No unified payout system across subsidiaries
- Payout schedule: Weekly (Remotasks and Outlier), with reported delays

**Payment Challenges (Documented Evidence):**
- Inc. Magazine: "Accusations of Mass Non-Payment" against Outlier AI
- Washington Post: Remotasks workers in Philippines reporting low pay and missing payments
- Rest of World: Remotasks dropping entire countries (Kenya, Nigeria, Pakistan) without explanation
- Annotator pay dropped to less than 1 cent per task in some markets due to oversupply
- Late payments described as "commonplace" across contributor base
- Workers report receiving "only a few percent of promised compensation"
- Sudden account suspensions via automated quality scoring systems
- PayPal/Payoneer cross-border fees erode already-low annotator wages
- No local mobile money support (M-Pesa, GCash, UPI) despite heavy emerging market workforce

**Annotator Workforce Geography:**
- Philippines: Remotasks primary market (computer vision tasks)
- Kenya: Former Remotasks market (terminated 2024)
- Nigeria: Former Remotasks market (terminated 2024)
- Pakistan: Former Remotasks market (terminated 2024)
- India: Remotasks expansion market
- Venezuela: Remotasks expansion market
- US/Europe: Outlier contributors (LLM training, higher-pay roles)

**Top 5 Markets Gap Analysis:**

MARKET 1: Philippines (largest annotator workforce)
  Accepted: PayPal, Payoneer, AirTM
  Missing: GCash, Maya, bank transfers (BDO, BPI), InstaPay
  Note: GCash has 90M+ users in Philippines. PayPal fees eat 3-5% of already-low wages.

MARKET 2: India (growing annotator base)
  Accepted: PayPal, Payoneer, AirTM
  Missing: UPI, Paytm, bank transfers (IMPS/NEFT), PhonePe
  Note: UPI handles 75%+ of digital payments in India. PayPal India has withdrawal limitations.

MARKET 3: Kenya / East Africa (terminated but critical for re-entry)
  Accepted: Previously PayPal, AirTM
  Missing: M-Pesa, Airtel Money, bank transfers, mobile money
  Note: M-Pesa is the dominant payment method in Kenya. 83% of adults use mobile money.

MARKET 4: United States (enterprise clients + Outlier contributors)
  Accepted: ACH, PayPal, enterprise invoicing
  Missing: Unified billing platform, real-time payouts, Zelle
  Note: Enterprise contracts ($100M+ DoD) require sophisticated billing. US contributors expect instant ACH.

MARKET 5: Latin America (Venezuela, Brazil expansion)
  Accepted: PayPal, AirTM
  Missing: Pix (Brazil), Mercado Pago, OXXO (Mexico), PSE (Colombia), Nequi
  Note: AirTM popular in Venezuela but Pix dominates Brazil. LATAM expansion needs local rails.

**Key meeting angles:**
1. **$2B revenue with fragmented payout infrastructure** | Three separate payout systems (Remotasks/Outlier/Enterprise) with zero orchestration.
2. **Workforce trust crisis** | Mass non-payment accusations and country bans. Reliable, local-method payouts rebuild annotator trust and retention.
3. **Emerging market workers, Western payout rails** | Filipino, Indian, and African annotators forced through PayPal/Payoneer. Local methods (GCash, UPI, M-Pesa) eliminate 3-5% cross-border fees.
4. **$29B company with payout reputational risk** | Inc., Washington Post, and Rest of World coverage of payment failures. Payment orchestration is infrastructure insurance.
5. **Government contract complexity** | $250M DoD BPA, $100M CDAO, $99M Army. Usage-based, milestone-based, and subscription billing need unified commerce.
6. **Meta partnership amplifies scale** | 49% Meta stake accelerates demand. Annotator workforce and payout volume will grow dramatically.
7. **Competitor pressure** | Surge AI, Labelbox, and Prolific all improving contributor payment experiences to attract talent away from Scale.

**Sources:**
- [Scale AI: Official Website](https://scale.com/)
- [Scale AI: About](https://scale.com/about)
- [Scale AI: Careers](https://scale.com/careers)
- [Scale AI: $100M DoD Deal](https://scale.com/blog/scale-ai-inks-100m-deal)
- [Scale AI: Next Phase (Meta Deal)](https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution)
- [Scale AI: Government Contracts](https://scale.com/contracts)
- [Wikipedia: Scale AI](https://en.wikipedia.org/wiki/Scale_AI)
- [CNBC: Wang Departure to Meta](https://www.cnbc.com/2025/06/12/scale-ai-founder-wang-announces-exit-for-meta-part-of-14-billion-deal.html)
- [CNBC: Meta $14B Scale AI Bet](https://www.cnbc.com/2025/06/10/zuckerberg-makes-metas-biggest-bet-on-ai-14-billion-scale-ai-deal.html)
- [Fortune: Alexandr Wang Meta Deal](https://fortune.com/2025/06/14/self-made-billionaire-college-dropout-alexandr-wang-signs-14-3-billion-deal-to-bolster-metas-ai-efforts-theres-a-huge-premium-to-naivete/)
- [Fortune: Inside Rise of Scale AI](https://fortune.com/2025/06/22/inside-rise-scale-alexandr-wang-meta-zuckerberg-14-billion-deal-acquihire-ai-supremacy-race/)
- [TechCrunch: Scale AI Meta Confirmation](https://techcrunch.com/2025/06/13/scale-ai-confirms-significant-investment-from-meta-says-ceo-alexandr-wang-is-leaving/)
- [FedScoop: Scale AI $250M DoD Contract](https://fedscoop.com/scale-ai-awarded-250m-ai-contract-by-department-of-defense/)
- [GovConWire: $99M Army Contract](https://www.govconwire.com/articles/scale-ai-99m-army-contract-rd-services)
- [Nextgov: Pentagon $200M AI Contracts](https://www.nextgov.com/acquisition/2025/07/pentagon-awards-multiple-companies-200m-contracts-ai-tools/406698/)
- [GetLatka: Scale AI Revenue](https://getlatka.com/companies/scale)
- [Sacra: Scale AI Revenue and Valuation](https://sacra.com/c/scale-ai/)
- [TSG Invest: Scale AI $29B Valuation](https://tsginvest.com/scale-ai/)
- [AI Funding Tracker: Scale AI Sales-Led Growth](https://aifundingtracker.com/scale-ai-sales-led-growth-strategy/)
- [Fueler: Scale AI Statistics 2026](https://fueler.io/blog/scale-ai-usage-revenue-valuation-growth-statistics)
- [Inc.: Outlier AI Mass Non-Payment Accusations](https://www.inc.com/sam-blum/its-a-scam-accusations-of-mass-non-payment-grow-against-scale-ais-subsidiary-outlier-ai.html)
- [Washington Post: Remotasks Philippines Low Pay](https://www.washingtonpost.com/world/2023/08/28/scale-ai-remotasks-philippines-artificial-intelligence/)
- [Rest of World: Remotasks Banning Workers](https://restofworld.org/2024/scale-ai-remotasks-banned-workers/)
- [Contrary Research: Scale AI](https://research.contrary.com/company/scale)
- [Crunchbase: Scale AI](https://www.crunchbase.com/organization/scale-2)
- [Y Combinator: Scale AI](https://www.ycombinator.com/companies/scale-ai)
- [Brandfetch: Scale AI Logo](https://brandfetch.com/scale.ai)
