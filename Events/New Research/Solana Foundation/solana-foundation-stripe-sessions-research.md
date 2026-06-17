# SOLANA FOUNDATION | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Solana Foundation
=======================================

Logo: https://solana.com/branding/solana-logo.svg
Nombre merchant: Solana Foundation

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Network Outage History
Tittle_Pain Point_2: Fiat On/Off-Ramp Gaps
Tittle_Pain Point_3: Cross-Border Settle Lag
Tittle_Pain Point_4: Congestion Tx Failures
Tittle_Pain Point_5: Regional APM Blind Spots

Desc_Pain Point_1: 9+ service disruptions between Oct 2024 and Feb 2025, some 13+ hours, none officially reported. Despite one year stability since Feb 2025, merchant trust lags.
Desc_Pain Point_2: Fiat on/off-ramps rely on third-party providers with varying fees and regional restrictions. Delays, missing webhooks, and settlement failures erode trust.
Desc_Pain Point_3: Despite $1T+ stablecoin volume (2025), cross-border fiat settlement requires bridging blockchain and banking rails. Currency gaps beyond USD/EUR limit adoption.
Desc_Pain Point_4: During congestion peaks, 75%+ of on-chain transactions failed. Fees spike to $10-$50. Merchants face unpredictable costs and completion rates at peak load.
Desc_Pain Point_5: Solana Pay supports USDC/crypto via Shopify but no native fiat methods (Pix, UPI, SEPA, Konbini). Hybrid crypto + fiat checkout needs separate stacks.

SLIDE 1: PSP TOPOLOGY

PSP_1: Solana Pay (native protocol) PSP_2: Modern Treasury (fiat rails: ACH, wire, RTP, FedNow) PSP_3: Helio (Shopify plugin) PSP_4: Circle (USDC issuer)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: Konbini (Japan)
Local_M_5: Boleto (Brazil)
Local_M_6: OXXO (Mexico)
Local_M_7: GrabPay (SE Asia)
Local_M_8: GCash (Philippines)
Local_M_9: M-Pesa (Africa)
Local_M_10: Bizum (Spain)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Hybrid Payment Dashboard

Desc_Yuno_Cap1: Route each merchant transaction to the optimal acquirer by geography, card BIN, and currency. For SDP merchants processing fiat + stablecoin payments, Smart Routing delivers +3-10% auth uplift by selecting the best processor per corridor.
Desc_Yuno_Cap2: When Solana congestion causes failures or Modern Treasury fiat rails experience delays, Yuno cascades to alternative processors in ms. NOVA AI recovers 75% of soft declines. Livelo recovered 50% of failed transactions through Yuno failover.
Desc_Yuno_Cap3: Extend Solana Pay merchants beyond crypto-only to 1,000+ local fiat methods: Pix in Brazil, UPI in India, SEPA in Europe, Konbini in Japan, M-Pesa in Africa. One API enables hybrid checkout globally. InDrive activated 10 markets via Yuno.
Desc_Yuno_Cap4: Unify visibility across Solana Pay crypto settlements, Modern Treasury fiat rails, and card transactions in one dashboard. Monitor approval rates per method and market, detect anomalies, and optimize routing across blockchain and traditional rails.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Solana Foundation at a glance:**
- Non-profit foundation based in Zug, Switzerland
- Dedicated to decentralization, adoption, and security of the Solana ecosystem
- ~453 employees (as of Oct 2025)
- Processed $1T+ in stablecoin volume on Solana in 2025
- Solana Pay: open-source, decentralized payments protocol integrated with Shopify
- Solana Developer Platform (SDP): launched March 2026 with Modern Treasury as payments infrastructure partner
- Early SDP users include Mastercard, Worldpay, and Western Union
- SOL treasury: Foundation holds significant SOL reserves; facilitated $50M+ in discounted token deals
- Solana Pay via Shopify: available to millions of merchants; Helio plugin processed $35M in Solana Mobile Chapter 2 sales

**Confirmed PSPs / Payment Infrastructure:**
- Solana Pay: native open-source payment protocol (USDC default, 100s of crypto tokens supported)
- Modern Treasury: fiat payment rails (ACH, wire, RTP, FedNow) for Solana Developer Platform
- Helio: took ownership of Solana Pay x Shopify plugin (Jan 2024); 0.75% merchant fee
- Circle: USDC issuer; USDC accounts for 55.7% of stablecoin market cap on Solana
- Jupiter: built-in swap aggregator enabling purchases in preferred tokens
- No third-party payment orchestrator detected for fiat merchant payments

**Key Pain Points:**
1. **Network reliability history**: 9+ unreported disruptions Oct 2024 to Feb 2025; some lasting 13+ hours. One year stability since Feb 2025, but merchant trust is still rebuilding
2. **Congestion-driven failures**: During peak activity, 75%+ of transactions failed; fees spiked to $10-$50. Firedancer upgrade (expected 2025) and Frankendancer (9-12% stake, 20% faster) aim to solve this
3. **Fiat on/off-ramp fragmentation**: Third-party providers have varying fees, regional restrictions, settlement failures, and missing webhooks
4. **Crypto-only merchant coverage**: Solana Pay supports USDC/crypto via Shopify but no native fiat local methods. Merchants wanting both must maintain separate stacks
5. **Cross-border settlement complexity**: Blockchain and banking rails operate on separate technology stacks, requiring intermediary solutions for fiat conversion

**Missing Payment Methods / Regional Gaps:**
- LATAM: Pix, Boleto, Mercado Pago, OXXO, PSE (Solana Pay has no fiat LATAM coverage)
- Europe: SEPA Direct Debit, iDEAL, Bancontact, Bizum, MBWay
- Asia Pacific: UPI, Konbini, PayPay, LINE Pay, GrabPay, GCash, DANA, KakaoPay
- Africa: M-Pesa, Airtel Money, MTN MoMo
- Modern Treasury provides US fiat rails only (ACH, wire, RTP, FedNow); no international fiat coverage

**Key meeting angles:**
1. **Hybrid crypto + fiat opportunity**: Solana Foundation's merchant ecosystem needs both crypto (Solana Pay) and fiat local methods. Yuno bridges this gap with 1,000+ APMs alongside crypto-friendly processors, all through one API.
2. **Developer platform monetization**: The Solana Developer Platform (SDP) onboards enterprises building payment products. Yuno can be offered as the fiat orchestration layer, complementing Modern Treasury's US-only rails with global coverage.
3. **Enterprise trust gap**: Mastercard, Worldpay, and Western Union are early SDP users. These enterprises expect enterprise-grade payment resilience. Yuno's failover and Smart Routing provide the reliability layer blockchain-native rails cannot guarantee alone.
4. **Shopify merchant expansion**: Solana Pay via Shopify reaches millions of merchants. Adding Yuno's local APMs to the Shopify checkout alongside Solana Pay converts crypto-curious merchants into full hybrid payment adopters.
5. **Network congestion failover**: When Solana congestion causes 75%+ transaction failure, Yuno can automatically cascade to fiat rails, ensuring merchants never lose a sale regardless of blockchain network state.
6. **LATAM alignment**: Solana has strong developer presence in LATAM. Yuno has proven LATAM infrastructure (InDrive: 10 markets, 90% approval; Rappi: zero implementation cost). Natural geographic fit.

**Solana Foundation Leadership:**
- Lily Liu: President of Management, Solana Foundation (entrepreneur/investor with CFO background in US, China, and emerging markets)
- Anatoly Yakovenko: Co-Founder of Solana Labs (CEO)
- Raj Gokal: Co-Founder of Solana Labs (COO)
- Dan Albert: Executive Director, Solana Foundation
- Board: Includes representatives from major token deal recipients per Foundation governance structure

**Recent corporate developments:**
- Mar 2026: Solana Developer Platform (SDP) launched with Modern Treasury as payments infrastructure partner
- Mar 2026: Mastercard, Worldpay, Western Union named as early SDP users
- Feb 2025: One year without a major consensus failure (longest stability period in Solana history)
- 2025: Solana processed $1T+ in stablecoin volume
- 2025: Firedancer mainnet launch expected (dual-client architecture for resilience)
- 2025: Frankendancer hybrid client processing blocks 20% faster, accounting for 9-12% of total stake
- 2025: Solana now achieves 99.99% uptime
- Jan 2024: Helio took ownership of Solana Pay x Shopify plugin
- Ongoing: $50M+ in discounted SOL token deals to treasury companies; Foundation holds $430M+ in SOL across partners

**Competitive Context:**
- Stripe launched stablecoin payment support (USDC on Base); competes directly with Solana Pay for crypto commerce
- Stripe x402 protocol enables machine-to-machine payments on blockchain (overlaps with Solana Pay use case)
- PayPal launched PYUSD stablecoin on Solana (Sep 2024); competes for on-chain payment share
- Visa and Mastercard both building on Solana for settlement and tokenization
- Shopify supports both Solana Pay and traditional PSPs (Stripe, PayPal, Shop Pay), giving merchants choice

**Sources:**
- [Solana Foundation Official Website](https://solana.org/)
- [Solana Foundation Branding](https://solana.com/branding)
- [Solana Pay Protocol](https://solanapay.com/)
- [Solana Foundation + Modern Treasury Partnership (BusinessWire)](https://www.businesswire.com/news/home/20260324239645/en/Solana-Foundation-Selects-Modern-Treasury-as-a-Payments-Infrastructure-Partner-for-Solana-Developer-Platform)
- [Modern Treasury + Solana Foundation (Modern Treasury)](https://www.moderntreasury.com/newsroom/press-releases/solana-foundation-selects-modern-treasury-as-a-payments-infrastructure-partner-for-solana-developer)
- [Solana Pay x Shopify Integration (Solana News)](https://solana.com/news/solana-pay-shopify)
- [Helio Solana Pay Shopify Plugin (Helio Docs)](https://docs.hel.io/docs/solana-pay-shopify-plugin)
- [Solana Outage History (StatusGator)](https://statusgator.com/blog/solana-outage-history/)
- [Solana Outages Complete History (Helius)](https://www.helius.dev/blog/solana-outages-complete-history)
- [Solana Network Outages Explained (LeveX)](https://levex.com/en/blog/solana-network-outages-explained)
- [Solana Stablecoins 2026 (Chainstack)](https://chainstack.com/solana-stablecoins-2026/)
- [Solana Ecosystem Roundup March 2026 (Solana News)](https://solana.com/news/solana-ecosystem-roundup-march-2026)
- [Solana Foundation Treasury Deals (The Block)](https://www.theblock.co/post/374029/solana-foundations-many-discounted-token-deals-fuels-sol-treasury-explosion)
- [Solana Foundation Grants and Funding](https://solana.org/grants-funding)
- [Solana Foundation About Page](https://solana.org/about)
- [Solana Foundation LinkedIn](https://www.linkedin.com/company/solana-foundation)
