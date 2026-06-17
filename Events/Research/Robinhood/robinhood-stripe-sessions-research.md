# ROBINHOOD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Robinhood
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/b/b9/Robinhood_%28company%29_logo.svg
Nombre merchant: Robinhood

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Entity Fragmentation
Tittle_Pain Point_2: Instant Deposit Cost Drag
Tittle_Pain Point_3: EU/Asia Payment Gap
Tittle_Pain Point_4: Crypto Withdrawal Delays
Tittle_Pain Point_5: Card Single-Rail Risk

Desc_Pain Point_1: Galileo powers banking, Sutton Bank holds deposits, Coastal Community issues the Gold Card, and Bitstamp runs institutional crypto. Four separate payment stacks with no unified orchestration layer create reconciliation silos across $4.5B in annual revenue.
Desc_Pain Point_2: Instant deposits via ACH cost up to 1.75% (minimum $2). On $68B in net deposits (2025 record), instant transfer fees eat into margin. Competitors offering free instant deposits pressure Robinhood to absorb or reduce this cost.
Desc_Pain Point_3: Robinhood expanded from 3 to 30 countries in 2025, but deposit rails remain U.S. centric. European users lack SEPA Instant, Open Banking, and iDEAL. Asia Pacific markets (Singapore, Indonesia) have no local payment rails like PayNow or GoPay activated.
Desc_Pain Point_4: Crypto deposits from external wallets can take 1 to 5 business days to become tradeable. Users transferring BTC or ETH to Robinhood face hold periods that competitors like Coinbase and Kraken do not impose, causing conversion loss.
Desc_Pain Point_5: The Gold Card routes through a single Visa path via Coastal Community Bank. No multi-acquirer routing means every soft decline on the 3% cashback card is a lost transaction with no retry, impacting 4.2M Gold subscribers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Galileo (banking/payment processor)
PSP_2: Sutton Bank (deposit accounts)
PSP_3: Coastal Community Bank (Gold Card issuer)
PSP_4: Visa (card network)
PSP_5: Bitstamp (institutional crypto)
PSP_6: Plaid (bank linking)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Instant (EU)
Local_M_2: Open Banking (UK/EU)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Bancontact (Belgium)
Local_M_5: BLIK (Poland)
Local_M_6: PayNow (Singapore)
Local_M_7: GoPay (Indonesia)
Local_M_8: Pix (Brazil)
Local_M_9: SPEI (Mexico)
Local_M_10: UPI (India)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each deposit and card transaction through the optimal rail by amount, speed, and geography. With $68B in net deposits and 27M funded customers, shifting even 10% of instant deposits from 1.75% ACH to lower-cost bank transfers recovers millions annually. Smart Routing delivers +3 to 10% auth uplift on Gold Card transactions.
Desc_Yuno_Cap2: Automatic cascade eliminates single-bank card dependency. When Coastal Community Bank declines a Gold Card transaction, Yuno reroutes instantly through an alternate acquirer. Up to 50% recovery on failed transactions, protecting the 3% cashback experience for 4.2M Gold subscribers.
Desc_Yuno_Cap3: Activates the local deposit rails Robinhood needs for 30-country expansion: SEPA Instant and Open Banking for EU, iDEAL for Netherlands, Bancontact for Belgium, PayNow for Singapore, GoPay for Indonesia, Pix for Brazil. One API, 1,000+ payment methods, no per-market builds required.
Desc_Yuno_Cap4: One dashboard unifying Galileo banking, Sutton Bank deposits, Coastal Community Gold Card, Visa network, Bitstamp institutional crypto, and Plaid ACH into a single reconciliation layer. Real-time transaction monitoring across all entities, NOVA fraud engine with 75% fewer false positives across every payment rail.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Robinhood at a glance:**
- Founded: 2013 by Vlad Tenev and Baiju Bhatt in Menlo Park, CA
- Public: HOOD on Nasdaq (IPO July 2021 at $38/share)
- Revenue: $4.5B FY2025 (record, +52% YoY); Q4 2025: $1.28B (record)
- Net Income: Record diluted EPS of $2.05 in 2025 ($0.66 in Q4)
- Net Deposits: $68B in 2025 (record), $16B in Q4
- Funded Customers: 27.0M (+7% YoY)
- Gold Subscribers: 4.2M (record, +58% YoY)
- Average Revenue Per User: $191 (+16% YoY)
- Employees: ~4,000+
- Markets: 30 countries (expanded from 3 in 2025), including entire EU

**Key 2025/2026 milestones:**
- Bitstamp acquisition: Completed June 2025 for $200M. Brings 50+ global crypto licenses, institutional client base, and crypto-as-a-service infrastructure
- EU expansion: Full EU/EEA access across 30 countries, crypto trading + US ETF access
- UK launch: Stock trading launched 2024
- Asia Pacific: Singapore as regional base, acquired PT Buana Capital Sekuritas (Indonesia)
- Robinhood Ledger: Institutional crypto platform using Bitstamp for smart order routing
- 2026 plans: Stock Tokens, Layer 2 blockchain, perpetual futures in EU, Money Market Funds

**Product suite:**
- Robinhood Investing: Commission-free stocks, ETFs, options, crypto
- Robinhood Crypto: 20+ digital currencies, staking
- Robinhood Gold: Premium subscription ($5/mo), 4.5% APY, 3% Gold Card cashback
- Gold Card: Visa credit card issued by Coastal Community Bank, 3% cashback on everything
- Robinhood Cash Card: Debit card via Sutton Bank
- Robinhood Checking & Savings: 3% APY, powered by Galileo
- Robinhood Clearing: In-house clearing (self-clearing broker-dealer since 2018)
- Bitstamp: Institutional crypto exchange (50+ licenses, 14-year track record)

**Confirmed PSPs / Payment Rails:**
- Galileo Financial Technologies (SoFi-owned): Payment processor for banking/checking products
- Sutton Bank: Deposit account custodian (FDIC insured up to $250K)
- Coastal Community Bank: Issuing bank for Gold Card (Visa)
- Visa: Card network for Gold Card and Cash Card
- Plaid: Bank account linking for ACH deposits
- ACH/Fedwire: Primary deposit/withdrawal rails
- Bitstamp: Institutional crypto infrastructure, smart order routing
- Robinhood Securities: In-house clearing broker
- No payment orchestrator detected

**Deposit Methods & Fees:**
- ACH standard: Free, 1 to 5 business days
- Instant bank transfer: Free for select banks (minutes)
- Instant ACH: Up to 1.75% fee ($2 minimum)
- Debit card deposit: Up to 1.75% fee ($2 minimum), $3,000/day cap
- Wire transfer (incoming): Free
- Wire transfer (outgoing): $25 fee
- Crypto transfers: 1 to 5 business day hold

**Key Meeting Angles:**
1. **$4.5B revenue, four payment stacks** | Galileo, Sutton Bank, Coastal Community, and Bitstamp each operate independently with no unified orchestration
2. **30-country expansion, U.S.-only rails** | SEPA Instant, Open Banking, and Asia Pacific APMs needed to match global footprint
3. **$68B net deposits at 1.75% instant fee** | Smart routing to cheaper rails directly improves deposit margin
4. **4.2M Gold subscribers at risk** | Single-acquirer card routing means every soft decline loses a premium customer transaction
5. **Bitstamp integration opportunity** | Unified payment orchestration across retail and institutional crypto simplifies the merger tech stack
6. **Indonesia/Singapore entry** | Local APMs (GoPay, PayNow) are table-stakes for Asia Pacific retail investors
7. **Clearing in-house, payments outsourced** | Robinhood built its own clearing; payment orchestration is the next logical infrastructure play
8. **Competitor pressure** | Coinbase (120M users, lower fees), SoFi (same-day funding), Revolut (EU-native rails)

**Sources:**
- [Robinhood Q4 & FY2025 Results (Investor Relations)](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-fourth-quarter-and-full-year-2025-results)
- [Robinhood Revenue 2020-2025 (MacroTrends)](https://www.macrotrends.net/stocks/charts/HOOD/robinhood-markets/revenue)
- [Robinhood Record 2025 (InvestmentNews)](https://www.investmentnews.com/equities/robinhood-caps-record-2025-with-q4-revenue-surge-but-shares-fall-on-investor-concerns/265225)
- [Robinhood Bitstamp Acquisition (CNBC)](https://www.cnbc.com/2025/06/02/robinhood-bitstamp-crypto.html)
- [Robinhood Completes Bitstamp Acquisition (Robinhood Newsroom)](https://robinhood.com/us/en/newsroom/robinhood-completes-acquisition-of-bitstamp/)
- [Robinhood 2026 Crypto Expansion (KuCoin)](https://www.kucoin.com/news/flash/robinhood-unveils-2026-crypto-expansion-plan-with-global-access-and-layer-2-network)
- [Robinhood Stock Tokens, L2, EU Expansion (Robinhood Newsroom)](https://newsroom.aboutrobinhood.com/robinhood-launches-stock-tokens-reveals-layer-2-blockchain-and-expands-crypto-suite-in-eu-and-us-with-perpetual-futures-and-staking/)
- [Robinhood Gold Card (Robinhood)](https://robinhood.com/creditcard/)
- [Robinhood Gold Card FAQ (Robinhood)](https://robinhood.com/us/en/support/articles/robinhood-gold-card-faq/)
- [Robinhood Deposit Methods (Robinhood)](https://robinhood.com/us/en/support/articles/deposit-money-into-your-robinhood-account/)
- [Robinhood Transfer Fees (Robinhood)](https://robinhood.com/us/en/support/articles/are-there-fees-for-transfers/)
- [Galileo x Robinhood Partnership (PRNewswire)](https://www.prnewswire.com/news-releases/galileo-and-robinhood-partner-on-robinhood-checking--savings-300764680.html)
- [Robinhood Clearing (Robinhood)](https://robinhood.com/us/en/support/articles/whats-clearing-by-robinhood/)
- [Robinhood Cash Card / Sutton Bank (Robinhood)](https://www.robinhoodcashcard.com/)
- [Robinhood EU Crypto Expansion (Payment Expert)](https://paymentexpert.com/2025/06/30/robinhoods-latest-crypto-includes-access-to-us-etfs/)
- [Robinhood Supported Countries (Neobanque)](https://neobanque.ch/blog/where-is-robinhood-available-supported-countries/)
- [Robinhood Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Robinhood_(company)_logo.svg)
- [Robinhood 2026 Outlook (Yahoo Finance)](https://finance.yahoo.com/news/products-diversification-crypto-drive-hood-121400670.html)
