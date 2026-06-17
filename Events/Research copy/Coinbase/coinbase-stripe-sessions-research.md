# COINBASE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Coinbase
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/3/3f/Coinbase.svg
Nombre merchant: Coinbase

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fiat On-Ramp Fee Burden
Tittle_Pain Point_2: Single-Rail ACH Dependency
Tittle_Pain Point_3: Fraud & Phishing Surge
Tittle_Pain Point_4: LatAm/Asia APM Gap
Tittle_Pain Point_5: Commerce Checkout Limits

Desc_Pain Point_1: Debit card deposits cost 3.99% per transaction. On a $1,000 BTC buy, $39.90 goes to processing. Competitors like Kraken and Binance offer cheaper instant options, creating direct conversion leakage across 120M monthly users.
Desc_Pain Point_2: ACH via Plaid is the primary free deposit rail for U.S. users. Any Plaid outage or bank integration failure blocks deposits for all ACH users simultaneously, with no failover path during volatile market windows when deposit demand peaks.
Desc_Pain Point_3: May 2025 insider breach exposed 69,461 customers. Push payment fraud is now the top threat to retail crypto users. Total compliance fines exceed $181M (Ireland, UK). Fragmented fraud tooling across card, ACH, and crypto rails multiplies exposure.
Desc_Pain Point_4: Coinbase operates in 115 countries but lacks native Pix (Brazil), UPI (India), SPEI (Mexico), and other local rails. India fiat on-ramp is still "planned for 2026." Without local APMs, each new market launch relies on costly card-only deposit flows.
Desc_Pain Point_5: Coinbase Commerce accepts only crypto payments. Merchants wanting fiat + crypto checkout must integrate separate processors. This limits Commerce adoption to crypto-native buyers and excludes the 95%+ of consumers who still pay with traditional methods.

SLIDE 1: PSP TOPOLOGY

PSP_1: Plaid (ACH bank linking)
PSP_2: Marqeta (Coinbase Card issuer processor)
PSP_3: Visa (Coinbase Card network)
PSP_4: Stripe (fiat-to-crypto onramp, Wallet)
PSP_5: PayPal (fiat deposits)
PSP_6: Pathward N.A. (card issuing bank)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: SPEI (Mexico)
Local_M_4: OXXO (Mexico)
Local_M_5: PSE (Colombia)
Local_M_6: Open Banking (UK/EU)
Local_M_7: BLIK (Poland)
Local_M_8: Boleto (Brazil)
Local_M_9: Nequi (Colombia)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each fiat deposit through the optimal rail by amount, speed, and geography. A $1,000 debit card purchase at 3.99% ($39.90 fee) could route to a lower-cost acquirer or instant bank transfer instead. At $7.2B annual revenue and $425B quarterly trading volume, even basis-point savings translate to tens of millions recovered.
Desc_Yuno_Cap2: Automatic cascade eliminates Coinbase's single-rail Plaid dependency for ACH. When Plaid drops a bank connection or ACH fails during market volatility spikes, Yuno reroutes to an alternative payment initiator in milliseconds. Up to 50% recovery on failed transactions, protecting deposit conversion exactly when it matters most.
Desc_Yuno_Cap3: Activates the local rails Coinbase needs for global fiat on-ramp expansion: Pix in Brazil, UPI in India, SPEI and OXXO in Mexico, PSE and Nequi in Colombia, Open Banking in UK/EU, BLIK in Poland, GrabPay in Southeast Asia. One API, 1,000+ payment methods, no per-market engineering builds. Turns 115 countries from card-only into full local coverage.
Desc_Yuno_Cap4: One dashboard unifying Plaid ACH, Marqeta card issuance, Visa debit, Stripe onramp, PayPal deposits, and Coinbase Commerce crypto payments into a single reconciliation layer. Real-time deposit monitoring, centralized compliance reporting across jurisdictions, NOVA fraud engine with 75% fewer false positives across all payment rails simultaneously.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Coinbase at a glance:**
- Founded: 2012 by Brian Armstrong and Fred Ehrsam in San Francisco
- Public: COIN on Nasdaq (direct listing April 2021)
- Revenue: $7.2B FY2025 (+9% YoY); Q1 2025 alone generated $2B
- Subscription & Services Revenue: $2.8B FY2025 (+23% YoY), 5.5x higher than prior cycle peak
- Q4 2025 Revenue: $1.78B (EPS $0.66, missed analyst expectations of $1.05)
- Q1 2026 Forecast: $550M to $630M subscription and services revenue
- Trading Volume: $425B per quarter (Q2 2025)
- Users: 120M monthly users, 8.7M monthly transacting users
- Employees: ~4,300
- Market Share: 60 to 65% of U.S. crypto exchange volume, ~6.9% global
- Countries: 115 supported, 103 with active trading

**Products:**
- Coinbase Exchange: Spot trading (retail + advanced), 250+ assets
- Coinbase Prime: Institutional prime brokerage, custody, OTC desk
- Coinbase Card: Visa debit card (issued by Pathward N.A., powered by Marqeta), up to 4% crypto rewards
- Coinbase Commerce: Onchain payment protocol for merchants (crypto-only)
- Coinbase Wallet: Self-custody wallet with Stripe fiat-to-crypto onramp
- Coinbase Developer Platform: APIs for onramp/offramp, payments, Base L2
- Base: Ethereum L2 blockchain (launched 2023), 150M+ x402 protocol transactions since May 2025
- USDC Partnership: Co-creator with Circle, $300M+ quarterly revenue from USDC

**Confirmed PSPs / Payment Rails:**
- Plaid: Bank verification and ACH initiation for U.S. users
- Marqeta: Issuer processor powering Coinbase Card
- Pathward N.A.: Issuing bank for Coinbase Card (Member FDIC)
- Visa: Card network for Coinbase Card, accepted at 80M+ merchant locations
- Stripe: Powers fiat-to-crypto onramp in Coinbase Wallet (credit card, Apple Pay)
- PayPal: Fiat deposit option for U.S. users
- Apple Pay / Google Pay: Supported for crypto purchases
- ACH / Fedwire: Free deposits (ACH), institutional wire transfers
- SWIFT: International wire transfers for Coinbase Prime institutional clients
- SEPA: EUR deposits for European users (EUR 0.15 fee)
- Faster Payments: GBP deposits for UK users
- No payment orchestrator detected

**Fee Structure:**
- ACH deposits: Free (3 to 5 day settlement)
- Debit card: 3.99% instant purchase fee
- SEPA: EUR 0.15 deposit fee
- Wire transfer: Variable (institutional)
- USDC onramp/offramp: 0% fees for developers
- Trading fees: Maker/taker model, varies by volume tier

**Key Security/Compliance Issues:**
- May 2025 insider data breach: Bribed overseas support agents exposed data of 69,461 users
- Ireland Central Bank fine: EUR 21.5M for failing to monitor EUR 176B in transactions
- UK FCA fine: GBP 3.5M for high-risk customer onboarding failures
- Total fines: $181M+ across jurisdictions
- Push payment fraud: Largest single threat to retail crypto users
- Phishing: Sophisticated social engineering attacks surging in 2025/2026

**2026 Strategic Priorities (per CEO Brian Armstrong):**
1. "Everything Exchange": Global all-in-one platform for crypto, equities, commodities
2. Stablecoin scaling: USDC as core revenue driver ($9T stablecoin payments in 2025, +87% YoY)
3. Onchain activity: Grow Base L2, developer tools, x402 agent payments
4. India fiat on-ramp: INR deposit capability planned for 2026
5. MiCA license: Enables regulated services across all 27 EU member states
6. AI agent payments: x402 protocol joined Linux Foundation with Google, Stripe, AWS support

**Key Meeting Angles:**
1. **$7.2B revenue, fragmented payment stack** | Six+ payment providers with no orchestration layer means reconciliation, fraud detection, and routing happen in silos
2. **3.99% debit card fee is a conversion killer** | Smart routing to cheaper rails would recover millions across 120M monthly users
3. **Plaid single-rail risk** | ACH is the primary free deposit method; any Plaid outage blocks all U.S. bank deposits during peak trading moments
4. **115 countries, card-only in most** | Local APMs (Pix, UPI, SPEI) would unlock native deposit flows in Coinbase's fastest-growing markets
5. **$181M+ in compliance fines** | Unified orchestration with centralized fraud/compliance monitoring reduces multi-jurisdictional regulatory exposure
6. **Commerce is crypto-only** | Fiat + crypto checkout orchestration would dramatically expand Coinbase Commerce merchant adoption
7. **Stripe partnership as wedge** | Already integrating Stripe for Wallet onramp; orchestration conversation is natural extension
8. **India on-ramp gap** | UPI activation through Yuno could accelerate India fiat launch timeline vs. building in-house

**Sources:**
- [Coinbase Q4 2025 Earnings (Investor Relations)](https://investor.coinbase.com/news/news-details/2026/Coinbase-Delivers-on-Q4-Financial-Outlook-Doubles-Total-Trading-Volume-and-Crypto-Trading-Volume-Market-Share-in-2025/default.aspx)
- [Coinbase Revenue 2020-2025 (MacroTrends)](https://www.macrotrends.net/stocks/charts/COIN/coinbase-global/revenue)
- [Coinbase Usage and Trading Statistics (Backlinko)](https://backlinko.com/coinbase-users)
- [Coinbase Statistics 2026 (CoinLaw)](https://coinlaw.io/coinbase-statistics/)
- [Coinbase Users Statistics (DemandSage)](https://www.demandsage.com/coinbase-users-statistics/)
- [Coinbase + Stripe Partnership (Coinbase Blog)](https://www.coinbase.com/blog/coinbase-stripe-team-up-to-increase-global-adoption-of-crypto)
- [Coinbase x402 Joins Linux Foundation (CoinDesk)](https://www.coindesk.com/tech/2026/04/02/coinbase-s-ai-payments-system-joins-linux-foundation-gathers-support-from-google-stripe-aws-and-others)
- [Marqeta Powers Coinbase Card (Marqeta)](https://www.marqeta.com/blog/marqeta-powers-coinbase-card)
- [Coinbase Card (Coinbase)](https://www.coinbase.com/card)
- [Coinbase Insider Breach (Blockaid)](https://www.blockaid.io/blog/the-coinbase-customer-support-scam-breaking-down-cryptos-growing-multibillion-dollar-push-payment-fraud-problem)
- [Coinbase EUR 21.5M Fine (OneSafe)](https://www.onesafe.io/blog/the-evolving-landscape-of-crypto-compliance-lessons-from-coinbases-21-5-million-fine)
- [Coinbase 2026 Focus (LiveBitcoinNews)](https://www.livebitcoinnews.com/coinbase-sets-2026-focus-on-a-global-all-in-one-exchange-across-crypto-and-markets/)
- [Coinbase Supported Countries (DataWallet)](https://www.datawallet.com/crypto/coinbase-countries)
- [Coinbase International Payments (Coinbase Blog)](https://www.coinbase.com/blog/coinbase-expands-international-payments-options-for-institutional-customers)
- [Coinbase Payment Methods (Coinbase Help)](https://help.coinbase.com/en/exchange/trading-and-funding/adding-a-payment-method)
- [Coinbase Fees 2026 (BitDegree)](https://www.bitdegree.org/crypto/tutorials/coinbase-fees)
- [Coinbase Payments (Coinbase Blog)](https://www.coinbase.com/blog/powering-the-future-of-ecommerce-introducing-coinbase-payments)
- [Coinbase Prime Funding (Coinbase Help)](https://help.coinbase.com/en/prime/trading-and-funding/funding-your-account-with-usd)
- [Coinbase Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Coinbase.svg)
- [Plaid ACH Verification (Coinbase Help)](https://help.coinbase.com/en/exchange/funding/verifying-a-us-bank-with-plaid)
