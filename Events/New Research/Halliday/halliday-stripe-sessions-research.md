# HALLIDAY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Halliday
=======================================

Logo: https://cdn.brandfetch.io/halliday.xyz/w/512/h/512/logo
Nombre merchant: Halliday

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Onramp Routing Blind Spots
Tittle_Pain Point_2: Fiat Settlement Fragmented
Tittle_Pain Point_3: No Failover on Card Txns
Tittle_Pain Point_4: Regional Method Gaps
Tittle_Pain Point_5: Cross-Border FX Leakage

Desc_Pain Point_1: Routes onramps via Stripe, Transak, MoonPay with no orchestration. Suboptimal acquirer selection across 35+ clients leaves 3-10% auth uplift unrealized.
Desc_Pain Point_2: Three onramp providers settle into separate accounts with different timelines and currencies. Manual reconciliation grows unsustainable at scale.
Desc_Pain Point_3: When Stripe declines a card onramp, no cascade to Transak or MoonPay exists. User drops off. Each failed onramp is a lost user for 35+ client dApps.
Desc_Pain Point_4: Only cards and ACH. Users in Europe (SEPA), Southeast Asia (GrabPay), LATAM (PIX, PSE) cannot onramp with preferred methods, capping global adoption.
Desc_Pain Point_5: USD-only settlement globally. Users in EUR, GBP, JPY, BRL absorb FX on every onramp. Competitors with local currency settlement gain advantage.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Transak
PSP_3: MoonPay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: PIX
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: GrabPay
Local_M_6: GCash
Local_M_7: PSE
Local_M_8: Konbini
Local_M_9: BLIK
Local_M_10: Sofort

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each fiat onramp to the best-performing acquirer by card BIN, issuer, and geography. With 35+ client dApps processing cross-chain purchases globally, a 3% auth uplift translates into thousands of additional successful onramps monthly and higher platform stickiness.
Desc_Yuno_Cap2: When Stripe declines a credit card onramp, Yuno automatically cascades to Transak or MoonPay in milliseconds. Up to 50% recovery on soft declines means fewer drop-offs at the critical fiat-to-crypto conversion step, directly protecting Halliday's per-transaction revenue.
Desc_Yuno_Cap3: Unlock onramps globally: SEPA for EU, PIX for Brazil, GrabPay for SEA, Konbini for Japan. One API, 1,000+ methods, zero engineering sprints per market. More local methods means more successful onramps for every client chain and higher end-user conversion.
Desc_Yuno_Cap4: One dashboard consolidating Halliday's fiat onramp volume across Stripe, Transak, and MoonPay. Real-time approval monitoring per geography and onramp provider, centralized reconciliation, and granular analytics on conversion rates by chain, token, and payment method.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Halliday at a glance:**
- Web3 payments infrastructure company: unified fiat onramps, cross-chain swaps, and bridging
- Founded: 2022, headquartered in San Francisco (185 Berry Street) with presence in New York
- Total funding: $26M ($6M Seed + $20M Series A led by a16z crypto, March 2025)
- CEO: Griffin Dunaif (Stanford); Co-founder: Akshay Malhotra
- Team from Stanford, Harvard, Penn with experience at Meta, Netflix, Samsung
- Employees across 4 continents (North America, Europe, Asia)
- Named to The Generalist's Future 50 Startups (August 2025)
- 35+ production clients including ApeChain, Avalanche Core Wallet, Story Protocol, Shrapnel, DeFi Kingdoms, Metis
- Upcoming integrations: Frax Finance, Lens Labs
- Non-custodial by design: Halliday never takes custody of user funds

**Core product:**
- Halliday Payments: single interface linking onchain commerce with fiat (credit cards, ACH) and crypto (tokens from any chain)
- Intelligent routing through best onramps, swaps, and bridges based on geography, payment method, and latency
- Workflow Protocol: abstracts multi-chain, multi-bridge orchestrations for developers
- Implementation: 7-line code UI, embedded modal, headless SDK, or direct API
- Supports any token on any chain, including custom bridge/DEX routing

**Confirmed PSPs:**
- Stripe: fiat onramp for credit card payments
- Transak: fiat-to-crypto onramp partner
- MoonPay: fiat-to-crypto onramp partner
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States
  Currently offer: Credit cards (Visa/MC/Amex), ACH
  Missing: Apple Pay, Google Pay for onramps
  US crypto buyers increasingly expect mobile wallet onramps for faster conversion.

MARKET 2: Europe (Germany, Netherlands, France)
  Currently offer: International credit cards (USD settlement)
  Missing: SEPA Direct Debit, iDEAL, Bancontact, Sofort, BLIK
  35% card penetration in Germany. European DeFi users strongly prefer bank-based methods for larger onramp amounts.

MARKET 3: Southeast Asia (Thailand, Singapore, Indonesia)
  Currently offer: International credit cards
  Missing: GrabPay, GCash, ShopeePay, bank transfer
  Mobile wallets dominate payments in SEA. Forcing credit card onramps excludes the majority of potential DeFi users.

MARKET 4: Latin America (Brazil, Colombia, Mexico)
  Currently offer: International credit cards
  Missing: PIX, PSE, OXXO, SPEI
  PIX processes 44B+ transactions per year in Brazil. Crypto adoption in LATAM is among the highest globally but card penetration is low.

MARKET 5: Japan
  Currently offer: International credit cards
  Missing: Konbini, bank transfer (furikomi), PayPay
  Japan has a highly active crypto market but strong preference for local payment methods. Card-only onramps miss a significant user segment.

**Key meeting angles:**
1. **Onramp conversion at risk** | Every failed card payment is a lost crypto buyer for Halliday's 35+ clients. Smart retry logic directly protects per-transaction revenue
2. **Multi-PSP complexity** | Three onramp providers (Stripe, Transak, MoonPay) with no unified orchestration. Yuno consolidates into one dashboard
3. **Global expansion blocked** | Credit card-only onramps exclude users in Europe, LATAM, and Asia where local methods dominate
4. **a16z backing** | $26M raised with strong investor network. Growth-stage company actively scaling payment infrastructure
5. **Non-custodial model** | Yuno's orchestration layer fits Halliday's architecture since it routes payments without touching user funds
6. **Competitive pressure** | Competing onramp providers like Ramp, Wyre replacements, and Alchemy Pay offer localized payment methods

**Sources:**
- [Halliday Official Website](https://halliday.xyz/)
- [Halliday Documentation](https://docs.halliday.xyz/)
- [a16z Crypto: Investing in Halliday](https://a16zcrypto.com/posts/article/investing-in-halliday-2/)
- [Fortune: Halliday Raises $20M](https://fortune.com/crypto/2025/03/18/blockchain-payments-company-halliday-fundraising-andreessen-horowitz/)
- [SiliconANGLE: Halliday $20M Series A](https://siliconangle.com/2025/03/19/halliday-raises-20m-build-ai-driven-blockchain-agents-away-smart-contracts/)
- [Fintech Futures: Halliday $20M Series A](https://www.fintechfutures.com/venture-capital-funding/blockchain-start-up-halliday-lands-20m-series-a-led-by-andreessen-horowitz)
- [Crypto-Fundraising: Halliday Profile](https://crypto-fundraising.info/projects/halliday/)
- [CBInsights: Halliday](https://www.cbinsights.com/company/halliday)
- [Alchemy: Halliday DApp](https://www.alchemy.com/dapps/halliday)
- [Brandfetch: Halliday Logo](https://brandfetch.com/halliday.xyz)
