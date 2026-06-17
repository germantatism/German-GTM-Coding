# SAPIOM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Sapiom
=======================================

Logo: https://cdn.brandfetch.io/sapiom.ai/w/512/h/512/logo
Nombre merchant: Sapiom

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Micropayment Cost Leakage
Tittle_Pain Point_2: Single Currency Rails
Tittle_Pain Point_3: No Failover on Agent Txns
Tittle_Pain Point_4: Global Agent Billing Gap
Tittle_Pain Point_5: Settlement Reconciliation

Desc_Pain Point_1: Millions of $0.004-$0.08 micro-transactions daily. Small processing fee inefficiencies compound into significant margin erosion at scale across agent purchases.
Desc_Pain Point_2: Agent Wallet operates in USD only. Enterprises in Europe, Japan, and India need local currency billing. USD conversion on micro-transactions adds FX cost.
Desc_Pain Point_3: A failed agent payment (API, compute, LLM) has no cascade to a backup processor. One failure breaks the entire autonomous workflow chain.
Desc_Pain Point_4: Global enterprises cannot fund Agent Wallets locally. No SEPA in Germany, no PIX in Brazil, no UPI in India. This limits non-US enterprise adoption.
Desc_Pain Point_5: 11+ service categories with pay-per-use pricing across millions of micro-transactions require multi-provider settlement and reconciliation at scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Proprietary Agent Wallet (internal)
PSP_2: Undisclosed payment processor

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (Europe)
Local_M_2: PIX (Brazil)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: Konbini (Japan)
Local_M_6: BLIK (Poland)
Local_M_7: Bancontact (Belgium)
Local_M_8: SPEI (Mexico)
Local_M_9: GrabPay (Southeast Asia)
Local_M_10: Alipay (China)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each micro-transaction through the lowest-cost processor for that amount, currency, and geography. With millions of agent-initiated payments daily ranging from $0.004 to $0.08, Smart Routing optimizes processing costs per corridor and can improve margins by 3-10% at scale.
Desc_Yuno_Cap2: When a payment fails mid-workflow, Yuno cascades to a backup acquirer in milliseconds. Up to 50% recovery on soft declines. For autonomous agents, payment continuity equals operational continuity.
Desc_Yuno_Cap3: Let enterprises fund Agent Wallets via their preferred local method: SEPA in Europe, PIX in Brazil, UPI in India, Konbini in Japan, Alipay in China. One API, 1,000+ methods, removing the funding friction that limits Sapiom's global enterprise adoption.
Desc_Yuno_Cap4: One dashboard for wallet top-ups, micro-transaction settlements, vendor payouts, and multi-currency reconciliation. Real-time visibility by service type, geography, and agent with centralized enterprise reporting.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Sapiom at a glance:**
- Execution engine and financial infrastructure platform for AI agents
- Tagline: "Intelligence without access is just a demo"
- Enables AI agents to autonomously purchase software, APIs, data, and compute
- Founded: Summer 2025 by Ilan Zerbib (former Shopify payments engineering director, 5 years)
- Headquarters: San Francisco, CA
- Total funding: $15.75M Seed round (Feb 2026)
- Lead investor: Accel
- Other investors: Okta Ventures, Gradient Ventures, Array Ventures, Menlo Ventures, Anthropic, Coinbase Ventures
- Strategic angels from: Shopify, OpenAI, Vercel, GitHub, Circle, Mercury
- Team size: not disclosed (early-stage startup)
- Revenue: not disclosed (pre-revenue or early revenue)

**Platform services (11+ categories):**
- User Authentication: SMS verification, OTP ($0.015/verification)
- LLM Inference: 400+ language models (per-token pricing)
- AI Search: web queries with citations ($0.006/search)
- Voice & Audio: speech generation, transcription ($0.08/generation)
- Image Generation: text-to-image ($0.004/megapixel)
- Web Extraction: browser automation, scraping ($0.01/extraction)
- Compute: serverless container execution
- Messaging: queue management, task scheduling
- Databases: Redis, vector, search, PostgreSQL
- Filesystem: file storage and serving
- Video: generation, transformation, subtitling

**Integration methods:**
- MCP Server for AI tools
- Skills for coding agents
- SDK (@sapiom/axios) for programmatic access

**Confirmed PSPs & billing infrastructure:**
- Proprietary "Agent's Wallet" system for managing agent spending
- Pay-per-use model with no subscriptions or minimums
- Transparent per-action pricing
- Underlying payment processor not publicly disclosed
- No payment orchestrator detected
- Built on Node.js/Next.js ecosystem

**Named partners:**
- Anchor, Blaxel, Polsia, Anything, name.com, Linkup, Prelude, Yugabyte

**Target market:**
- Vibe-coding platforms (Lovable, Bolt, etc.)
- Enterprises deploying autonomous AI agents
- Any application requiring AI agents to access paid services

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, largest AI/enterprise market)
  Currently offer: USD wallet funding (method unknown)
  Missing: ACH Direct Debit for enterprise wallet top-ups, automated wire transfers
  US enterprises managing thousands of AI agents need bulk wallet funding via ACH, not manual card charges.

MARKET 2: Europe (major enterprise AI market: UK, Germany, France, Netherlands)
  Currently offer: USD billing only
  Missing: SEPA Direct Debit, iDEAL, Bancontact, EUR invoicing
  European enterprises deploying AI agents need EUR-denominated billing and SEPA for recurring wallet top-ups.

MARKET 3: Asia Pacific (Japan, Singapore, India, growing AI adoption)
  Currently offer: USD billing only
  Missing: UPI (India), Konbini (Japan), PayNow (Singapore), local invoicing
  APAC enterprises represent a massive AI agent deployment opportunity but require local currency billing.

MARKET 4: Latin America (growing developer and AI ecosystem)
  Currently offer: USD billing only
  Missing: PIX (Brazil), SPEI (Mexico), PSE (Colombia)
  LATAM developers building with vibe-coding tools need local currency options to fund agent wallets.

MARKET 5: China (largest AI market outside US)
  Currently offer: USD billing only
  Missing: Alipay, WeChat Pay, UnionPay, CNY invoicing
  Chinese enterprises deploying AI agents cannot easily fund USD wallets. Local payment methods are essential for market entry.

**Key meeting angles:**
1. **Payment company at its core** | Sapiom IS a payment infrastructure company for AI agents. They deeply understand payment orchestration value and may want Yuno as their underlying multi-provider layer.
2. **Micropayment scale** | Millions of $0.004-$0.08 transactions daily require optimized routing to minimize per-transaction costs. Smart Routing is purpose-built for this.
3. **Ex-Shopify payments DNA** | Founder Ilan Zerbib led Shopify's payments engineering. He understands multi-provider orchestration and will appreciate Yuno's architecture.
4. **Anthropic as investor** | Anthropic (Claude AI) is a strategic investor. Sapiom is positioned at the intersection of AI and payments, a natural Yuno partnership.
5. **Global enterprise ambition** | Sapiom targets enterprise AI deployments worldwide. Local payment methods are the unlock for non-US market expansion.
6. **Wallet funding bottleneck** | Every enterprise client must fund Agent Wallets. Making this seamless across geographies and payment methods directly drives Sapiom's growth.

**Sources:**
- [Sapiom Homepage](https://www.sapiom.ai/)
- [TechCrunch: Sapiom Raises $15M](https://techcrunch.com/2026/02/05/sapiom-raises-15m-to-help-ai-agents-buy-their-own-tech-tools/)
- [TechBuzz: Sapiom Payment Rails for AI Agents](https://www.techbuzz.ai/articles/sapiom-lands-15m-to-build-payment-rails-for-ai-agents)
- [The AI Insider: Sapiom Seed Round](https://theaiinsider.tech/2026/02/12/sapiom-raises-15m-seed-round-to-build-financial-infrastructure-for-ai-agents/)
- [Sapiom Blog: Funding Announcement](https://www.sapiom.ai/blog/sapiom-raises-15-75m-to-give-ai-agents-trusted-access-to-the-api-economy)
- [CryptoRank: Sapiom AI Agents Payments](https://cryptorank.io/news/feed/598ec-sapiom-ai-agents-payments-funding)
- [Sapiom Crunchbase](https://www.crunchbase.com/organization/sapiom)
- [Yahoo Finance: Sapiom $15M](https://finance.yahoo.com/news/sapiom-raises-15m-help-ai-235342135.html)
- [TechJuice: Shopify for Robots](https://www.techjuice.pk/the-shopify-for-robots-ex-exec-raises-millions-for-agents-to-handle-their-own-bills/)
