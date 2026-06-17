# SKYFIRE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Skyfire
=======================================

Logo: https://skyfire.xyz/wp-content/uploads/2025/04/Group-1410103655.svg
Nombre merchant: Skyfire

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-Rail Dependency
Tittle_Pain Point_2: Stablecoin-Only Limits
Tittle_Pain Point_3: Global Fiat Coverage Gap
Tittle_Pain Point_4: Agent Fraud Exposure
Tittle_Pain Point_5: Merchant Accept Friction

Desc_Pain Point_1: Skyfire relies on USDC on Base as primary settlement rail. Single blockchain dependency creates outage risk with no cascade to alternative chains or fiat rails.
Desc_Pain Point_2: Core agent-to-agent payments settle in USDC only. Markets with stablecoin regulatory restrictions (EU MiCA, India RBI) cannot accept KYAPay natively.
Desc_Pain Point_3: Card and ACH funding in US only. No direct support for Pix (Brazil), UPI (India), SEPA (EU), or mobile wallets across Asia Pacific. Limits adoption globally.
Desc_Pain Point_4: Autonomous agents at scale create novel fraud vectors. KYA identity layer is unproven at volume. No multi-PSP fraud scoring or cross-processor velocity checks.
Desc_Pain Point_5: Merchants must integrate KYAPay to accept agent payments. Low adoption means agents hit checkout walls on most sites, forcing human intervention at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: USDC on Base (Circle) PSP_2: Visa (tokenized credentials via KYAPay) PSP_3: Card/ACH funding (processor undisclosed)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: SEPA Instant (EU)
Local_M_4: Boleto (Brazil)
Local_M_5: iDEAL (Netherlands)
Local_M_6: Bancontact (Belgium)
Local_M_7: GrabPay (SE Asia)
Local_M_8: GCash (Philippines)
Local_M_9: DANA (Indonesia)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing for Agents
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Agent Dashboard

Desc_Yuno_Cap1: Route each AI agent transaction to the optimal acquirer by geography, currency, and merchant acceptance. As Skyfire scales to millions of transactions, Smart Routing delivers +3-10% auth uplift by selecting the best processor per corridor in real time.
Desc_Yuno_Cap2: When USDC on Base faces congestion or Visa tokenization fails, Yuno automatically cascades to alternative rails in milliseconds. NOVA AI recovers 75% of soft declines. Livelo recovered 50% of failed transactions. Zero downtime for autonomous agent commerce.
Desc_Yuno_Cap3: Expand agent payments beyond cards and stablecoins to 1,000+ local methods: Pix in Brazil, UPI in India, SEPA in Europe, GrabPay in SE Asia, iDEAL in Netherlands. One API unlocks every market. InDrive activated 10 markets through Yuno.
Desc_Yuno_Cap4: Replace fragmented visibility across USDC settlements, Visa credentials, and card funding with one real-time dashboard. Monitor agent approval rates, detect fraud patterns, track per-agent spend limits from one control plane.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Skyfire at a glance:**
- Founded: 2023 in San Francisco by Amir Sarhangi (CEO) and Craig DeWitt, both former Ripple executives
- Total Funding: $9.5M over 2 rounds from 18 investors including Coinbase Ventures, a16z CSX, Neuberger Berman, Circle, Gemini, Draper Associates, Ripple
- Exited Beta: March 2025 with enterprise-ready payment network for AI agents
- Product: KYAPay protocol + Know Your Agent (KYA) identity framework for autonomous AI agent commerce
- Visa Partnership: December 2025 demonstration of secure agentic commerce purchase using KYAPay + Visa Intelligent Commerce + Visa Trusted Agent Protocol
- Core Technology: Stablecoin-based (USDC on Base) payment rail for AI agents, paired with KYA compliance layer
- Use Case: AI agents autonomously researching, purchasing, and paying for goods/services without human intervention

**Confirmed PSPs / Payment Infrastructure:**
- USDC on Base blockchain (Circle): primary settlement rail for agent-to-agent transactions
- Visa: tokenized credential access via KYAPay protocol for merchant checkout (demonstrated with Bose.com)
- Card/ACH/Wire funding: agents and enterprises can fund wallets via traditional rails (specific processor not disclosed)
- No third-party payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno integration)

**Key Pain Points:**
1. **Single blockchain dependency**: USDC on Base is the core settlement layer; no multi-chain failover if Base experiences congestion, exploits, or regulatory pressure
2. **Limited fiat payment coverage**: Agent funding supports US cards, ACH, wires, and USDC but lacks direct support for regional methods in LATAM, Asia Pacific, and Europe
3. **Merchant adoption barrier**: KYAPay requires merchant-side integration; most e-commerce sites do not yet accept agent-initiated payments, creating friction
4. **Novel fraud vectors**: Autonomous agents transacting at scale create unprecedented fraud surface area; KYA identity layer is new and untested at volume
5. **Regulatory uncertainty**: No clear legal framework for agent-initiated payments in most jurisdictions; liability for incorrect or fraudulent agent transactions is undefined

**Missing Payment Methods / Regional Gaps:**
- LATAM: Pix, Boleto, Mercado Pago, OXXO, PSE
- Europe: SEPA Instant, iDEAL, Bancontact, Bizum, MBWay, Giropay
- Asia Pacific: UPI, GrabPay, GCash, DANA, LINE Pay, PayPay, KakaoPay
- Global Wallets: PayPal, Google Pay, Apple Pay (beyond Visa tokenization)

**Key meeting angles:**
1. **Infrastructure layer opportunity**: Skyfire is building the "Stripe for AI agents" but lacks multi-PSP orchestration. Yuno can be the routing and failover layer underneath KYAPay, ensuring every agent transaction reaches the optimal processor.
2. **Global expansion bottleneck**: As agentic commerce scales globally (Asia Pacific = 24.5% of agentic commerce revenue in 2025), Skyfire needs local payment method coverage it does not have. Yuno's 1,000+ APMs solve this instantly.
3. **Visa partnership as entry point**: Skyfire already works with Visa for tokenized credentials. Yuno integrates with Visa and hundreds of other processors, making it a natural orchestration layer beneath the KYAPay protocol.
4. **Fraud and trust gap**: 87% of financial institutions cite trust as the biggest barrier to agentic payment adoption. Yuno's cross-processor fraud scoring and velocity checks add the risk layer Skyfire needs.
5. **Ripple DNA, payment orchestration gap**: Founders built cross-border payments at Ripple but Skyfire lacks multi-acquirer routing intelligence. Yuno fills the exact gap between Skyfire's identity/wallet layer and the diverse global acquirer landscape.

**Skyfire Leadership:**
- Amir Sarhangi: CEO and Co-Founder (former Ripple VP of Product and Services; founded Jibe Mobile)
- Craig DeWitt: Co-Founder (former Ripple Senior Director of Product)
- Benjamin Vivo-Wachter: VP of Business Development
- Hieu Ta: VP of Engineering

**Recent corporate developments:**
- Dec 2025: Demonstrated secure agentic commerce purchase with Visa Intelligent Commerce on Bose.com
- Oct 2024: Raised additional $1M; Coinbase Ventures and a16z CSX joined cap table
- Aug 2024: Launched with $8.5M seed funding from Neuberger Berman, Inception Capital, Arrington Capital, and others
- Mar 2025: Exited Beta with enterprise-ready features including programmatic wallets, payment controls, and enterprise-grade capabilities
- Jun 2025: Launched open KYAPay Protocol with Agent Checkout for fully autonomous transactions
- Integrations: Apify, BuildShip, CarbonArc, and growing ecosystem of AI agent platforms

**Competitive Context:**
- Stripe launched x402 protocol for AI agent payments using USDC on Base (direct competitor to KYAPay)
- Crossmint offers AI agent virtual cards as alternative to stablecoin-based approach
- Mastercard launched Agentic Commerce standards for secure agent transactions
- Market is early: Forrester and eMarketer both identify 2026 as inflection year for agentic payments

**Sources:**
- [Skyfire Official Website](https://skyfire.xyz/)
- [Skyfire KYAPay and KYA Framework (Stellagent)](https://stellagent.ai/insights/skyfire-kyapay-know-your-agent)
- [Skyfire Launches AI Agent Checkout (PYMNTS)](https://www.pymnts.com/artificial-intelligence-2/2025/skyfire-launches-ai-agent-checkout-to-enable-fully-autonomous-transactions/)
- [Skyfire + Visa Intelligent Commerce (BusinessWire)](https://www.businesswire.com/news/home/20251218520399/en/Skyfire-Demonstrates-Secure-Agentic-Commerce-Purchase-Using-the-KYAPay-Protocol-and-Visa-Intelligent-Commerce)
- [Visa Partners Complete Secure AI Transactions (Visa)](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-partners-complete-secure-agentic-transactions.html)
- [Skyfire Exits Beta (BusinessWire)](https://www.businesswire.com/news/home/20250306938250/en/Skyfire-Exits-Beta-with-Enterprise-Ready-Payment-Network-for-AI-Agents)
- [Skyfire $8.5M Launch (SiliconANGLE)](https://siliconangle.com/2024/08/21/ai-payment-processing-startup-skyfire-launches-8-5m-funding/)
- [Coinbase + a16z Fund Skyfire (The Block)](https://www.theblock.co/post/322742/coinbase-ventures-and-a16zs-csx-bring-skyfires-total-funding-raised-to-9-5-million)
- [Skyfire TechCrunch Profile](https://techcrunch.com/2024/08/21/skyfire-lets-ai-agents-spend-your-money/)
- [Skyfire KYAPay Protocol Launch (BusinessWire)](https://www.businesswire.com/news/home/20250626772489/en/Skyfire-Launches-Open-KYAPay-Protocol-With-Agent-Checkout)
- [Skyfire Apify Integration (Apify Docs)](https://docs.apify.com/platform/integrations/skyfire)
- [Agentic Payments 2026 (Fenwick)](https://www.fenwick.com/insights/publications/is-2026-the-year-of-agentic-payments)
- [Mastercard Agentic Commerce Standards](https://www.mastercard.com/global/en/news-and-trends/stories/2026/agentic-commerce-standards.html)
- [Stripe x402 Protocol (Stripe Docs)](https://docs.stripe.com/payments/machine/x402)
- [Skyfire Crunchbase Profile](https://www.crunchbase.com/organization/skyfire-systems)
- [Skyfire Tracxn Profile](https://tracxn.com/d/companies/skyfire/__-gSNwLdAbLR2EH3jQO5ja24BZ2dqjmKWC_BS3-4pf1s)
