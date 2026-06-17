# CLOUDFLARE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Cloudflare
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idchmboHEZ/id-eaWS8tS.svg
Nombre merchant: Cloudflare

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-PSP on Stripe
Tittle_Pain Point_2: Flat Retry, Auto-Downgrade
Tittle_Pain Point_3: Zero Regional APMs
Tittle_Pain Point_4: Post-M&A Billing Sprawl
Tittle_Pain Point_5: PayPal Routing Misfires

Desc_Pain Point_1: Entire self-serve revenue flows through Stripe with Zuora for subscription logic. No failover processor. At $2.17B revenue growing 30% YoY, one Stripe outage or approval rate dip puts millions of subscription renewals at risk.
Desc_Pain Point_2: Failed payments get 5 auto-retries over 5 days with no intelligent scheduling, then auto-downgrade to Free plan. Cloudflare states it "does not know why a payment was declined." Flat retry policy leaves recoverable revenue on the table.
Desc_Pain Point_3: Checkout accepts Visa/MC/Amex/Discover/UnionPay/PayPal/Link only. No Pix, iDEAL, UPI, BLIK, or Konbini despite serving 190+ countries. Customers in Brazil, India, and Europe cannot pay with preferred local methods.
Desc_Pain Point_4: Seven acquisitions in 14 months (5 in 2024, Human Native + Astro in Jan 2026). Each entity brings its own billing contracts. No orchestration layer to normalize payment flows across acquired businesses.
Desc_Pain Point_5: Community complaints: PayPal charges linked card instead of PayPal balance. Cards show "declined" but charge goes through. No self-serve refund mechanism. Auth/reconciliation gap creates ops burden.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (self-serve card processing + Link wallet)
PSP_2: Zuora (subscription billing logic)
PSP_3: PayPal (alternative self-serve method)
PSP_4: Citibank (enterprise ACH/Wire, SWIFT: CITIUS33)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: iDEAL
Local_M_3: UPI
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: SPEI
Local_M_7: Konbini
Local_M_8: SEPA Direct Debit
Local_M_9: KakaoPay
Local_M_10: M-Pesa

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $2.17B revenue, 4,298 large customers ($100K+ ARR), and millions of subscriptions across 190+ countries, routing each renewal to the best acquirer per market delivers 3-10% auth uplift on global billing.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a subscription renewal. Instead of a flat 5-retry countdown to auto-downgrade, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions prevents involuntary churn to Free plans at scale.
Desc_Yuno_Cap3: Activates methods Cloudflare's global customer base needs: Pix in Brazil, iDEAL in Netherlands, UPI in India, BLIK in Poland, Konbini in Japan, SEPA DD across Europe, SPEI in Mexico, KakaoPay in Korea. One API, 1,000+ methods. Unlocks self-serve conversion in 190+ countries.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Zuora, PayPal, and Citibank enterprise payments. Real-time approval monitoring per country, centralized reconciliation across 7 recent acquisitions, and NOVA fraud detection (75% reduction) protecting millions of subscription accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Cloudflare at a glance:**
- Founded: 2009. HQ: San Francisco, California
- Public: NYSE: NET
- CEO: Matthew Prince
- Revenue: $2.168B (FY2025), up 29.8% YoY. FY2026 guidance: $2.785-2.795B (28-29% YoY growth)
- Q4 FY2025 revenue: $614.5M, up 33.6% YoY
- Largest deal ever: $42.5M ACV (Q4 2025)
- Large customers ($100K+ ARR): 4,298, up 23% YoY, contributing 73% of Q4 revenue
- New ACV: Grew nearly 50% YoY in Q4
- Gross margin: 74.5% GAAP (FY2025)
- Network: 330+ cities, 190+ countries, 13,000+ interconnections
- Products: CDN, DDoS Protection, Zero Trust, Workers (serverless), R2 (storage), AI Gateway, Pages, DNS, SSL/TLS, WAF, Bot Management, Turnstile
- PCI DSS: Level 1 certified since 2014
- Recent M&A: Human Native (AI data marketplace, Jan 2026), Astro Technology (JS framework, Jan 2026), 5 acquisitions in 2024
- Partnerships: Visa, Mastercard, AmEx (Trusted Agent Protocol for agentic commerce, Oct 2025), Mastercard (SMB cybersecurity, Feb 2026), Coinbase (x402 Foundation, NET Dollar stablecoin)
- Notable customers: Shopify, DoorDash, Canva, Discord, Zendesk, IBM, L'Oreal, Garmin

**Confirmed Payment Stack:**
- Stripe: Primary PSP for all self-serve billing. Confirmed via "Link" (Stripe's proprietary wallet) in billing docs and job listings referencing Stripe
- Zuora: Subscription billing logic layer (confirmed via job listings: Billing Systems Analyst with Stripe + Zuora + Oracle BRM)
- PayPal: Alternative self-serve payment method
- Link (Stripe): One-click checkout wallet (exclusively available to Stripe merchants)
- Citibank: Enterprise ACH payments and wire transfers (SWIFT: CITIUS33)
- Credit/Debit cards: Visa, Mastercard, Amex, Discover, UnionPay
- Maestro: Explicitly NOT accepted
- Prepaid/gift cards: Typically NOT accepted
- Cryptocurrency: NOT accepted in live checkout (NET Dollar stablecoin initiative in development)
- No payment orchestrator detected
- No multi-processor failover
- No regional APM geo-adaptation in checkout

**Payment Method Gaps (Community Evidence):**
- "Card declined but charge went through" (multiple threads 2023-2025)
- "Cannot pay via PayPal balance, Cloudflare charging my card" (PayPal routing issue)
- "Payment charged but domain purchase failed" (auth/reconciliation gap)
- No self-serve refund mechanism (requires support ticket)
- Flat 5-retry policy over 5 days, then auto-downgrade to Free
- Cloudflare officially states it "does not know why a payment was declined"
- No Pix, iDEAL, UPI, BLIK, Konbini, SEPA DD, or OXXO verified in checkout
- No geo-adapted checkout for any market (no regional domains either)
- No regional APMs surface for non-US IP addresses

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (dominant, ~35-40% of traffic)
  Accepted: Visa/MC/Amex/Discover, PayPal, Link, ACH (enterprise), Wire (enterprise)
  Missing: Venmo (direct), Apple Pay, Google Pay (self-serve)
  Note: Best coverage, but single Stripe processor with no failover

MARKET 2: Europe (UK, Germany, France, significant customer base)
  Accepted: Visa/MC/Amex, PayPal, UnionPay
  Missing: SEPA DD, iDEAL (Netherlands), BLIK (Poland), GiroPay, Bancontact, Sofort, MB Way
  Note: No SEPA DD for recurring subscriptions despite London office and major EU presence

MARKET 3: Brazil / Latin America (high traffic, no local entity confirmed)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix handles 70%+ of Brazilian digital payments. Cross-border card processing adds fees and decline risk. No local entity confirmed.

MARKET 4: India / South Asia (high traffic, no local entity confirmed)
  Accepted: Visa/MC (cross-border)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of Indian digital payments. Cross-border card declines likely impacting self-serve conversion.

MARKET 5: Japan / APAC (high traffic, Singapore office confirmed)
  Accepted: Visa/MC (cross-border)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: Japan is a key market with high CDN traffic. Konbini (convenience store payments) critical for self-serve developer audience.

**Key meeting angles:**
1. **$2.17B revenue, single PSP on Stripe** | Entire self-serve billing depends on one processor. No failover, no routing optimization. Revenue growing 30% YoY amplifies the risk
2. **Flat 5-retry auto-downgrade** | Failed payments get zero intelligent retry logic. "We do not know why a payment was declined." Involuntary churn machine at scale
3. **190+ countries, card-only checkout** | No Pix, UPI, iDEAL, BLIK, or Konbini despite global presence. Free-to-paid conversion constrained in highest-growth markets
4. **Agentic commerce signals payment sophistication** | Visa/Mastercard/AmEx partnership for Trusted Agent Protocol shows the payments team understands infrastructure deeply. Peer-level conversation expected
5. **7 acquisitions in 14 months** | Each acquired entity brings its own billing. Post-M&A consolidation is a classic trigger for payment orchestration evaluation
6. **PayPal/billing auth gaps** | Community confirms charges on wrong method, declined-but-charged errors, no self-serve refunds. Orchestration layer normalizes multi-method management
7. **Enterprise segment exploding** | 4,298 customers at $100K+ ARR (up 23%), contributing 73% of revenue. Enterprise billing complexity (ACH, wire, multi-currency) needs orchestration

**Sources:**
- [Cloudflare: Billing Policy](https://developers.cloudflare.com/billing/billing-policy/)
- [Cloudflare: Create Billing Profile](https://developers.cloudflare.com/billing/create-billing-profile/)
- [Cloudflare: Troubleshoot Failed Payments](https://developers.cloudflare.com/billing/troubleshoot-failed-payments/)
- [Cloudflare: FY2025 Results](https://www.cloudflare.com/press/press-releases/2026/cloudflare-announces-fourth-quarter-and-fiscal-year-2025-financial-results/)
- [Cloudflare: Stripe Support in Workers](https://blog.cloudflare.com/announcing-stripe-support-in-workers/)
- [Cloudflare: Agentic Commerce Partnership](https://www.cloudflare.com/press/press-releases/2025/cloudflare-collaborates-with-leading-payments-companies-to-secure-and-enable-agentic-commerce/)
- [Cloudflare: Human Native Acquisition](https://www.cloudflare.com/press/press-releases/2026/cloudflare-strengthens-content-offering-to-ai-companies-with-acquisition-of-human-native/)
- [Cloudflare: Astro Acquisition](https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-astro-to-accelerate-the-future-of-high-performance-web-development/)
- [Cloudflare: PCI DSS Compliance](https://www.cloudflare.com/trust-hub/compliance-resources/pci-dss/)
- [Cloudflare Community: Card Declined but Charged](https://community.cloudflare.com/t/the-system-shows-that-my-card-was-declined-but-the-charge-actually-went-through-a/889205)
- [Cloudflare Community: PayPal Balance Issue](https://community.cloudflare.com/t/cannot-pay-via-paypal-balance-cloudflare-charging-my-card/315665)
- [Cloudflare Community: Payment Failing](https://community.cloudflare.com/t/payment-failing-cannot-register-new-domain/687809)
- [Cloudflare Job Listing: Billing Systems Analyst](https://job-boards.greenhouse.io/cloudflare/jobs/6819455)
- [Visa: Trusted Agent Protocol](https://investor.visa.com/news/news-details/2025/Visa-Introduces-Trusted-Agent-Protocol-An-Ecosystem-Led-Framework-for-AI-Commerce/default.aspx)
- [FinTech Global: Cloudflare + Mastercard SMB Cybersecurity](https://fintech.global/2026/02/18/cloudflare-and-mastercard-target-smb-cyber-risks/)
- [The Block: Cloudflare x402 Foundation](https://www.theblock.co/post/374726/cloudflare-teams-up-with-visa-mastercard-and-amex-to-lay-payment-rails-for-ai-agents)
- [MacroTrends: Cloudflare Revenue](https://www.macrotrends.net/stocks/charts/NET/cloudflare/revenue)
- [SEC: Cloudflare 10-K FY2024](https://www.sec.gov/Archives/edgar/data/1477333/000147733325000043/cloud-20241231.htm)
- [Brandfetch: Cloudflare Logo](https://brandfetch.com/cloudflare.com)
