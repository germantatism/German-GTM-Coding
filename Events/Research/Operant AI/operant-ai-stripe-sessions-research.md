# OPERANT AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Operant AI
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idxrn4xr1h/idmN0Gz1UW.svg
Nombre merchant: Operant AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: AWS-Only Billing Lock-In
Tittle_Pain Point_2: Usage Metering Complexity
Tittle_Pain Point_3: No Direct Card Acceptance
Tittle_Pain Point_4: Global Expansion Friction
Tittle_Pain Point_5: Enterprise Invoice Gaps

Desc_Pain Point_1: Operant AI sells through AWS Marketplace, tying all billing to Amazon's infrastructure. This limits pricing flexibility, adds AWS commission on every transaction, and prevents direct customer relationships. No alternate billing channel exists outside the marketplace.
Desc_Pain Point_2: AI Gatekeeper charges per API request ($0.10-$0.50/month depending on contract length). Metering millions of API calls in real-time, converting them to billable units, and reconciling across contract tiers creates operational complexity as the customer base scales.
Desc_Pain Point_3: Enterprise customers who do not use AWS cannot purchase Operant AI directly via credit card, ACH, or wire transfer through a self-serve checkout. The company lacks a direct payment collection layer outside of AWS Marketplace subscriptions.
Desc_Pain Point_4: Operant AI serves global enterprises deploying AI workloads. Customers in Europe, Asia, and LATAM face friction paying through AWS Marketplace in USD only. No local currency billing, no regional payment methods, no localized checkout experience.
Desc_Pain Point_5: Large enterprise deals often require custom invoicing, PO-based billing, net-30/60/90 terms, and multi-entity procurement. AWS Marketplace handles standard subscriptions but lacks flexibility for complex enterprise procurement workflows.

SLIDE 1: PSP TOPOLOGY

PSP_1: AWS Marketplace (Primary Billing)
PSP_2: Stripe (Likely, SaaS standard)
PSP_3: Wire Transfer (Enterprise)
PSP_4: USD Only
PSP_5: No Orchestration Layer

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: UPI
Local_M_5: Pix
Local_M_6: BLIK
Local_M_7: Alipay
Local_M_8: GrabPay
Local_M_9: Konbini
Local_M_10: SPEI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every enterprise subscription and usage-based charge to the optimal acquirer by customer geography, card type, and transaction size. As Operant scales beyond AWS Marketplace to direct sales, smart routing ensures maximum auth rates on self-serve and enterprise payments globally.
Desc_Yuno_Cap2: When a renewal or usage charge fails on the primary processor, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed SaaS payments. For an enterprise security product protecting critical AI infrastructure, payment failures cannot disrupt service continuity.
Desc_Yuno_Cap3: Enable global enterprise procurement with local payment methods: SEPA Direct Debit for European customers, UPI for Indian enterprises, Pix for Brazilian tech companies, Alipay for Chinese firms. One API, 1,000+ methods, removing geographic payment friction from enterprise sales.
Desc_Yuno_Cap4: Consolidate AWS Marketplace billing, direct card payments, wire transfers, and enterprise invoicing into one dashboard. Real-time revenue tracking across all channels, NOVA anomaly detection for subscription fraud, and centralized reconciliation replace fragmented billing management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Operant AI at a glance:**
- Founded: 2020 in San Francisco, California
- CEO: Vrajesh Bhavsar (Co-Founder, ex-Apple, built iOS/macOS Dynamic Tracing, Data Protection, Secure Enclave; ex-Arm ML/AI business unit lead)
- CTO: Dr. Priyanka Tembey (Co-Founder, PhD Georgia Tech, ex-VMware foundational engineer for hybrid cloud)
- CMO: Ashley Roof (Co-Founder)
- Co-Founder: Ashraf Alhashim
- HQ: San Francisco, California
- Total Funding: $13.5M across 2 rounds (Series A: $10M in Sep 2024 led by SineWave Ventures)
- Employees: ~11 (as of Dec 2024, likely growing)
- Revenue: Not disclosed (early-stage)
- Key Investors: Felicis, SineWave Ventures, Alumni Ventures, Calm Ventures, Gaingels
- AWS Marketplace Partner
- Only vendor featured across ALL 5 of Gartner's most critical AI security reports
- Named in Gartner's 2025 Market Guide for API Protection and MCP Gateways

**Products:**
- AI Gatekeeper: Runtime protection for AI applications and agents across Kubernetes, hybrid, and private clouds
- Agent Protector: Real-time agentic AI security (launched Feb 2026), first solution for shadow agent discovery + secure dev enclaves + zero trust enforcement
- MCP Gateway: Enterprise-grade runtime defense for MCP-connected AI applications (launched Jun 2025)
- API Threat Protection: Runtime defense for API endpoints

**Pricing (AWS Marketplace):**
- 1-month contract: $0.50 per API request per month
- 12-month contract: $0.25/month (up to 96% savings)
- 24-month contract: $0.20/month (up to 98% savings)
- 36-month contract: $0.10/month (up to 99% savings)
- 7-day free trial available
- Pay-as-you-go and annual commitment models

**Competitive Landscape:**
- Competitors: Protect AI, Robust Intelligence, HiddenLayer, Calypso AI
- Differentiation: Only vendor in all 5 Gartner AI security reports; runtime defense (not just scanning); covers AI + APIs + MCP + Agents
- Strength: Deep technical founders (Apple, VMware, Google pedigree), Gartner recognition, AWS partnership
- Weakness: Very early stage (~11 employees), no disclosed enterprise logos, AWS-dependent billing

**Key meeting angles:**
1. **AWS billing dependency**: All revenue flows through AWS Marketplace commissions. Direct billing capability adds margin and customer ownership.
2. **Early stage = right time**: With only 11 employees and Series A, Operant is building its payment infrastructure now. Orchestration from day one prevents technical debt.
3. **Global enterprise AI buyers**: AI security customers are global (US, EU, Asia). Local payment methods remove friction from enterprise procurement.
4. **Usage-based complexity**: Per-API-request billing across contract tiers needs robust metering and reconciliation. Payment orchestration simplifies multi-tier billing.
5. **Gartner momentum**: Featured in all 5 Gartner AI security reports means rapid enterprise pipeline growth. Payment infrastructure must scale ahead of demand.
6. **Founder pedigree**: Apple Secure Enclave + VMware hybrid cloud founders understand infrastructure. They will appreciate a well-architected payment layer.

**Sources:**
- [Operant AI Official Website](https://www.operant.ai/)
- [Operant AI About Page](https://www.operant.ai/company/about)
- [Operant AI Agent Protector Launch](https://www.globenewswire.com/news-release/2026/02/05/3233044/0/en/Operant-AI-Launches-Agent-Protector-The-First-Real-Time-Agentic-Security-Solution-Enabling-Safe-AI-Agent-Innovation-at-Scale.html)
- [Operant AI Gatekeeper Launch](https://www.globenewswire.com/news-release/2025/04/16/3062605/0/en/Operant-AI-Announces-AI-Gatekeeper-to-Supercharge-Runtime-Protection-for-AI-Agents-and-AI-Applications.html)
- [Operant AI MCP Gateway Launch](https://www.globenewswire.com/news-release/2025/06/16/3099877/0/en/Operant-AI-Launches-MCP-Gateway-Enterprise-Grade-Runtime-Defense-for-MCP-Connected-AI-Applications.html)
- [Operant AI $10M Series A](https://www.globenewswire.com/news-release/2024/09/12/2945058/0/en/Operant-AI-Secures-10M-Series-A-to-Protect-the-Modern-Cloud-Across-APIs-Applications-and-AI.html)
- [Operant AI Gartner Recognition](https://www.operant.ai/art-kubed/operant-ai-featured-in-gartners-2025-market-guide-for-api-protection-and-innovation-report-mcp-gateways)
- [Operant AI AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-4uz4qpfa6cymq)
- [Operant AI on AWS Marketplace (Blog)](https://www.operant.ai/art-kubed/operant-ai-on-aws-marketplace)
- [SiliconANGLE: Agent Protector Launch](https://siliconangle.com/2026/02/05/operant-ai-debuts-agent-protector-secure-autonomous-ai-agents-scale/)
- [Pulse2: CEO Vrajesh Bhavsar Interview](https://pulse2.com/operant-ai-profile-vrajesh-bhavsar-interview/)
- [Operant AI Crunchbase](https://www.crunchbase.com/organization/operant-ai)
- [Operant AI Tracxn](https://tracxn.com/d/companies/operant-ai/__ei9GBSPqL_n7OUu-qQX8ay9wSRQWkT215htbu1Ey50M)
