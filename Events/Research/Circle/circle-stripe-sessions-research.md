# CIRCLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Circle
=======================================

Logo: https://asset.brandfetch.io/idXbEMIiHi/idmP2sFJXR.svg
Nombre merchant: Circle

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Coinbase Revenue Share Drag
Tittle_Pain Point_2: Fiat On-Ramp Fragmentation
Tittle_Pain Point_3: Limited Local Fiat Rails
Tittle_Pain Point_4: CPN Partner Onboarding
Tittle_Pain Point_5: Tether Market Share Gap

Desc_Pain Point_1: Circle paid $908M in distribution costs to Coinbase in 2024, roughly 56% of USDC reserve revenue. This single-partner dependency erodes margins on $2.7B revenue. Diversifying fiat collection channels beyond Coinbase reduces distribution concentration and improves unit economics at scale.
Desc_Pain Point_2: Businesses using Circle Mint to mint/redeem USDC need fiat on-ramps in 150+ countries. Each corridor requires local bank rails, compliance checks, and currency conversion. Without unified payment orchestration, each new market means a new banking integration, slowing Circle's corridor expansion.
Desc_Pain Point_3: CPN targets real-time settlement in markets like Brazil, Mexico, and Hong Kong. But local fiat payouts require Pix, SPEI, FPS, and other local rails. Circle currently partners corridor-by-corridor (Thunes, Worldline, RedotPay). No single orchestration layer connects all local payout methods globally.
Desc_Pain Point_4: CPN Managed Payments launched April 2026 with select PSP partners. Scaling from pilot (Veem, Conduit, Alfred Pay, Tazapay) to hundreds of PSPs and banks globally requires each partner to integrate separately. An orchestration layer could accelerate partner onboarding by standardizing fiat-to-USDC flows.
Desc_Pain Point_5: USDC holds ~25% stablecoin market share vs. Tether's ~55%. Despite 72% USDC growth in 2025, Tether launched USAT targeting US institutional dollars. Winning market share requires frictionless fiat entry points. Every failed card auth or missing local method on a mint transaction is a lost USDC inflow.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (fiat card processing for Circle products, confirmed integration)
PSP_2: Circle Mint (institutional USDC minting/redemption, wires + bank transfers)
PSP_3: Coinbase (primary USDC distribution, 56% revenue share)
PSP_4: CPN Partners (Thunes, Worldline, RedotPay, Veem, Conduit, Tazapay)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: SPEI
Local_M_3: UPI
Local_M_4: Mada
Local_M_5: SEPA Instant
Local_M_6: PromptPay
Local_M_7: GCash
Local_M_8: M-Pesa
Local_M_9: BLIK
Local_M_10: Nequi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography on fiat-to-USDC minting flows. With $75.3B USDC in circulation and $11.9T quarterly onchain volume, routing each fiat inflow to the best local acquirer delivers 3-10% authorization uplift on card-funded mint transactions across 150+ countries.
Desc_Yuno_Cap2: Automatic cascade when a fiat-to-USDC card charge is declined. Instead of losing a mint transaction, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions. Each recovered mint increases USDC circulation and reserve income for Circle.
Desc_Yuno_Cap3: Activates local fiat entry points Circle needs for global USDC adoption: Pix in Brazil, SPEI in Mexico, UPI in India, Mada in Saudi Arabia, SEPA Instant in Europe, PromptPay in Thailand, GCash in Philippines, M-Pesa in Africa. One API, 1,000+ methods. Accelerates CPN corridor expansion.
Desc_Yuno_Cap4: One dashboard unifying fiat collection across Stripe, Circle Mint bank rails, Coinbase distribution, and CPN partner corridors. Real-time monitoring of fiat-to-USDC conversion rates per country, centralized compliance tracking, and NOVA fraud detection (75% reduction) protecting institutional mint/redeem flows.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Circle at a glance:**
- Founded: 2013
- HQ: New York City
- CEO & Chairman: Jeremy Allaire
- Public: NYSE: CRCL (IPO June 4, 2025, at $24-$26/share, $6.7B valuation)
- Revenue: $2.7B (FY2025), up 64% YoY
- Q4 2025: $770M revenue, up 77% YoY
- Net Income: $133M (Q4 2025); Net Loss $70M (FY2025, impacted by $424M IPO-related stock comp)
- Adjusted EBITDA: $167M (Q4 2025), up 412% YoY
- USDC in Circulation: $75.3B (year-end 2025), up 72% YoY
- Onchain Transaction Volume: $11.9T (Q4 2025), up 247% YoY; $70T+ cumulative
- Employees: 1,000-5,000 across 18 locations
- Products: USDC stablecoin, EURC (euro stablecoin), Circle Mint, Circle Payments Network (CPN), Programmable Wallets, Developer APIs
- Key Partners: Coinbase (primary distribution, 56% revenue share), Visa, Intuit, Polymarket, Binance, Grab, Nubank, Mercado Libre
- M&A: Interop Labs acquisition (Axelar Network team/IP, December 2025), Centre Consortium (acquired 50% from Coinbase for $210M in shares, 2023)
- FY2026 Guidance: Other revenue $150M-$170M; RLDC margin 38%-40%; adj. opex $570M-$585M
- Competitive Position: #2 stablecoin by market cap (~25% share) vs. Tether USDT (~55%)

**Confirmed Payment/Infrastructure Stack:**
- Stripe: Confirmed integration for fiat card processing
- Circle Mint: Institutional on-ramp for USDC/EURC minting via wire transfers and bank transfers in 185+ countries
- Coinbase: Primary USDC distribution channel ($908M distribution costs in 2024)
- CPN Managed Payments: Launched April 8, 2026. Full-stack platform for PSPs/banks to settle in USDC without holding crypto
- CPN Partners: Thunes, Worldline, RedotPay, Conduit, Alfred Pay, Tazapay, Veem
- Fiat on-ramps: Mexican peso, Brazilian real, Euro confirmed; targeting 20+ blockchain rails
- Circle Payments API: Card payments in 150+ countries
- Programmable Wallets: Enable USDC fiat payments via debit card integration

**Key Business Dynamics:**
- Coinbase Dependency: Coinbase earned ~56% of USDC reserve revenue in 2024. Collaboration Agreement expires August 2026 with auto-renewal
- Revenue Model: Primarily reserve income from USDC reserves invested in short-term US Treasuries and repos
- Distribution Cost Pressure: $908M to Coinbase in 2024 is the primary margin headwind
- Regulatory Advantage: USDC fully MiCA-compliant in EU; Tether delisted from European exchanges
- Competition: Tether USAT targeting US institutional dollars; new stablecoin entrants (Hyperliquid, PayPal PYUSD)
- USDC market cap surged 72% in 2025, outpacing USDT's 32% growth

**Top 5 Fiat Corridor Gaps:**

CORRIDOR 1: Brazil (CPN pilot market)
  Active: CPN partner integration (RedotPay)
  Missing: Direct Pix integration for instant BRL-to-USDC conversion
  Note: Pix handles 70%+ of Brazilian digital payments. Direct Pix on-ramp would accelerate USDC adoption in LATAM's largest economy

CORRIDOR 2: Mexico (CPN pilot market)
  Active: MXN on-ramp via Circle Mint
  Missing: SPEI instant transfer integration at checkout level
  Note: SPEI processes 90%+ of Mexican electronic transfers. Direct integration eliminates intermediary friction

CORRIDOR 3: India (high-growth crypto market)
  Active: Cross-border card processing
  Missing: UPI integration for INR-to-USDC flows
  Note: UPI handles 75%+ of Indian digital payments. 1.3B population with growing crypto interest needs local fiat rails

CORRIDOR 4: Europe (MiCA-compliant, EURC launched)
  Active: EURC stablecoin, SEPA transfers via Circle Mint
  Missing: SEPA Instant for real-time EUR-to-USDC, iDEAL, BLIK
  Note: MiCA compliance gives USDC/EURC regulatory advantage over Tether in EU. Needs frictionless local on-ramps

CORRIDOR 5: Middle East / Africa (emerging stablecoin markets)
  Active: Cross-border card processing
  Missing: Mada (Saudi), M-Pesa (East Africa), Fawry (Egypt)
  Note: Bermuda planning fully onchain national economy with Circle infrastructure. Regional expansion requires local payment rails

**Key meeting angles:**
1. **$2.7B revenue, 64% growth** | Circle is scaling fast but $908M Coinbase distribution costs erode margins. Diversifying fiat collection channels reduces dependency and improves unit economics
2. **CPN Managed Payments launch** | Just launched April 2026 with select partners. Orchestration layer could accelerate partner onboarding by standardizing fiat-to-USDC settlement flows globally
3. **$75.3B USDC in circulation** | Every failed fiat-to-USDC transaction is lost circulation. Smart routing on mint flows maximizes fiat inflow conversion across 150+ countries
4. **Tether USAT competitive threat** | New US-regulated competitor targeting institutional dollars. Circle needs frictionless local fiat entry points in every market to defend and grow market share
5. **CPN corridor expansion** | Targeting 20+ blockchain rails globally. Each corridor needs local fiat payout methods (Pix, SPEI, UPI, M-Pesa). Orchestration connects all rails through one API
6. **MiCA regulatory advantage** | USDC is MiCA-compliant; Tether is not. European market opportunity requires SEPA Instant, iDEAL, BLIK, and other local methods for frictionless EUR-to-USDC conversion
7. **Enterprise partnerships accelerating** | Visa, Intuit, Grab, Nubank, Mercado Libre integrations show institutional momentum. Each partner integration benefits from optimized fiat collection rails

**Sources:**
- [Circle: Q4 & FY2025 Financial Results](https://www.circle.com/pressroom/circle-reports-fourth-quarter-and-full-fiscal-year-2025-financial-results)
- [Circle: CPN Managed Payments Launch](https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement)
- [Circle: Payments Use Case](https://www.circle.com/use-case/payments)
- [Circle: CPN Network Partners](https://www.circle.com/blog/circle-payments-network-partners-grow-with-circle)
- [Circle: CPN Field Guide](https://www.circle.com/blog/circle-payments-network-cpn-a-concise-field-guide-for-prospective-network-participants)
- [Circle: Circle Mint Institutional On-Ramp](https://www.circle.com/blog/circle-mint-delivers-a-powerful-institutional-onramp-to-usdc-and-eurc)
- [Circle: Programmable Wallets + Debit Cards](https://www.circle.com/blog/how-programmable-wallets-with-debit-cards-can-enable-usdc-payments)
- [Circle: Wikipedia](https://en.wikipedia.org/wiki/Circle_Internet_Group)
- [BusinessWire: Circle FY2025 Results](https://www.businesswire.com/news/home/20260225882643/en/Circle-Reports-Fourth-Quarter-and-Full-Fiscal-Year-2025-Financial-Results)
- [The Block: CPN Managed Payments](https://www.theblock.co/post/396727/circle-rolls-out-usdc-payments-platform-that-lets-users-pay-without-holding-stablecoins)
- [JPMorgan: USDC Outpaces Tether Onchain](https://www.theblock.co/post/377031/jpmorgan-circle-usdc-stablecoin-tether-usdt-onchain-growth)
- [CoinDesk: Tether and Circle Dominance Tested](https://www.coindesk.com/opinion/2025/10/11/tether-and-circle-s-dominance-is-being-put-to-the-test)
- [Decrypt: Tether Stablecoin Dominance](https://decrypt.co/365049/tether-stablecoin-dominance-over-circle-usdc-major-crypto-hacks)
- [SiliconAngle: Circle Acquisition Talks](https://siliconangle.com/2025/05/19/report-circle-potentially-acquired-coinbase-ripple-5b/)
- [Aurpay: Circle Coinbase $908M Deal](https://aurpay.net/aurspace/circle-coinbase-partnership/)
- [CoinDesk: Tether USAT Threat](https://www.coindesk.com/business/2026/01/27/circle-faces-first-major-threat-for-institutional-dollars-from-tether-s-usat)
- [Brandfetch: Circle Logo](https://brandfetch.com/circle.com)
- [Quartr: Circle Q4 2025 Summary](https://quartr.com/events/circle-internet-group-inc-crcl-q4-2025_FVLFgRKH)
