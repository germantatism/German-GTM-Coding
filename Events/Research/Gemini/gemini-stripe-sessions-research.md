# GEMINI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Gemini
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/e/e0/Gemini_%28digital_currency_exchange%29_logo.svg
Nombre merchant: Gemini

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fiat On-Ramp Friction
Tittle_Pain Point_2: EU/UK/AU Market Exit
Tittle_Pain Point_3: Debit Card Fee Burden
Tittle_Pain Point_4: ACH Hold Window
Tittle_Pain Point_5: Single-Rail Dependency

Desc_Pain Point_1: Debit card deposits cost 3.49%, PayPal 2.50%. Free ACH takes 4-5 days. Users wanting instant access pay a steep premium or wait a week, killing conversion.
Desc_Pain Point_2: Exited UK, EU, Australia on April 6, 2026, cut 25% of staff. No local rails (Open Banking, SEPA, BPAY) made unit economics unsustainable. Only US and SG remain.
Desc_Pain Point_3: Every debit card buy carries 3.49% fee. On $1,000 BTC purchase, $34.90 goes to processing. Coinbase and Kraken offer cheaper instant deposits, creating leakage.
Desc_Pain Point_4: ACH deposits lock funds 4-5 days before crypto withdrawal. In volatile markets, users buy but cannot move funds out, triggering tickets and eroding trust.
Desc_Pain Point_5: Plaid handles bank linking and payment initiation for all fiat rails. Any Plaid downtime blocks deposits for all ACH users with no fallback route.

SLIDE 1: PSP TOPOLOGY

PSP_1: Plaid (bank linking / ACH)
PSP_2: PayPal
PSP_3: Apple Pay / Google Pay
PSP_4: Mastercard (Credit Card program)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Open Banking (UK/EU)
Local_M_2: SEPA Instant
Local_M_3: Pix
Local_M_4: OXXO
Local_M_5: PayNow (SG)
Local_M_6: FPS (UK)
Local_M_7: UPI
Local_M_8: BLIK
Local_M_9: Interac
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each fiat deposit through the optimal rail by amount, speed, and geography. A $500 debit card buy at 3.49% could route to a lower-cost acquirer, recovering margin on $52.7B annual trading volume. Basis-point savings at scale equal millions recovered.
Desc_Yuno_Cap2: Automatic cascade eliminates Plaid single-rail dependency. When Plaid drops a bank connection or ACH fails, Yuno reroutes to an alternative initiator in milliseconds, keeping deposits live during volatile windows. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates local rails for Singapore (PayNow) and future re-entry: Open Banking for UK/EU, Pix for Brazil, UPI for India, Interac for Canada. One API, 1,000+ payment methods, no per-market engineering builds required.
Desc_Yuno_Cap4: One dashboard unifying Plaid ACH, debit cards, PayPal, Apple Pay, Google Pay, and Credit Card settlement. Real-time deposit monitoring, NYDFS/CFTC compliance reporting, NOVA fraud engine with 75% fewer false positives.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gemini at a glance:**
- Founded: 2014 by Cameron and Tyler Winklevoss
- IPO: September 12, 2025, Nasdaq (GEMI) at $28/share, raised $425M, valued at $3.3B
- Revenue: $179.6M FY2025 (+26% YoY); Q3 2025 revenue up 52% QoQ
- Net Loss: $582.8M in 2025 (vs $158.5M in 2024), driven by restructuring and EU/UK/AU exit costs
- Trading Volume: $52.7B FY2025; institutional volume $21.5B in H1 alone (87% of total)
- Assets on Platform: $21B+ (as of IPO filing)
- Products: Spot exchange (147 assets, 420 markets), Gemini Credit Card (Mastercard, $1.2B tx volume), Gemini Pay (via Flexa), Gemini Staking (ETH, SOL, MON), Gemini Predictions (CFTC-licensed DCM)
- Gemini Credit Card: $0 annual fee, up to 4% crypto cashback, $1.2B transaction volume in FY2025, 115% services revenue surge
- CTO: Pravjit Tiwana (departing as of April 2026)
- Markets: US (primary) and Singapore only, after exiting UK/EU/AU on April 6, 2026
- Staff: Cut 25% as part of restructuring (Feb 2026)
- SEC Settlement: Reached in principle to resolve Gemini Earn lawsuit
- Prediction Markets: Gemini Predictions launched with CFTC DCM license, 330% volume growth MoM in early 2026

**Confirmed PSPs / Payment Rails:**
- Plaid: bank linking, ACH initiation, Open Banking (was used for UK/EU, now US-only)
- PayPal: fiat deposits (US only, 2.50% fee)
- Debit Cards: 3.49% fee (likely processed via a card acquirer, not publicly disclosed)
- Apple Pay: supported for crypto purchases (short withdrawal hold)
- Google Pay: supported for crypto purchases (short withdrawal hold)
- ACH: free deposits via linked bank, 4-5 day hold
- Wire Transfers: free deposit (bank may charge), $25 withdrawal fee
- FAST: supported for SGD in Singapore
- Flexa: crypto payment network for Gemini Pay (in-store crypto spending)
- Mastercard: partner for Gemini Credit Card
- No payment orchestrator detected

**Deposit/Withdrawal Limits:**
- ACH: $5,000/day, $30,000/month deposits; $100,000/day withdrawals
- Debit card: limits set per account (3.49% fee)
- Wire: no stated limit (institutional-grade)
- Crypto: 10 free withdrawals/month, then dynamic network fees

**EU/UK/AU Exit Details:**
- Feb 5, 2026: Announced exit from UK, EU/EEA, Australia
- March 5, 2026: Accounts moved to withdrawal-only mode
- April 6, 2026: All accounts closed
- Reason: Unsustainable unit economics, refocus on US and prediction markets
- Previously held: MiFID II license (Malta), E-Money license (Ireland), VASP registrations (Italy, France, Greece)
- Customer migration: Partnership with eToro for account transfers

**Key Meeting Angles:**
1. **Post-IPO efficiency pressure** | $582.8M net loss in 2025 puts intense focus on reducing processing costs per transaction
2. **Fiat on-ramp is the bottleneck** | 3.49% debit card fees and 4-5 day ACH holds are the #1 source of user friction and support tickets
3. **Prediction markets growth** | 330% MoM volume growth in Gemini Predictions creates new settlement demands that need reliable instant rails
4. **CTO transition** | Pravjit Tiwana departing creates a window for infrastructure decisions with new tech leadership
5. **Credit Card as wedge** | $1.2B in Gemini Credit Card transaction volume means Gemini is already a payments company, not just an exchange
6. **Singapore is the international lifeline** | PayNow and FAST are table-stakes for Singaporean depositors; Yuno activates both instantly
7. **Re-entry optionality** | If Gemini ever re-enters EU/UK/AU, an orchestration layer with 1,000+ local APMs avoids the same unit-economics trap that caused the exit

**Sources:**
- [Gemini IPO at $28/share (CNBC)](https://www.cnbc.com/2025/09/11/winklevoss-founded-crypto-exchange-gemini-prices-ipo.html)
- [Gemini Nasdaq Debut (CNBC)](https://www.cnbc.com/2025/09/12/gemini-the-winklevoss-crypto-exchange-pops-in-nasdaq-debut.html)
- [Gemini Revenue $179.6M (Yahoo Finance)](https://finance.yahoo.com/markets/crypto/articles/gemini-revenue-grows-180-million-223900349.html)
- [Gemini Q3 Revenue +52% (Yahoo Finance)](https://finance.yahoo.com/news/gemini-crypto-exchange-q3-revenue-050631308.html)
- [Gemini GEMI Earnings Miss (CoinDesk)](https://www.coindesk.com/business/2025/11/11/gemini-slumps-after-missing-earnings-estimates-in-first-report-since-ipo)
- [Gemini IPO Raises $433M (Bloomberg)](https://www.bloomberg.com/news/articles/2025-09-09/crypto-exchange-gemini-raises-us-ipo-target-to-433-3-million)
- [Gemini Exits UK/EU/AU (CoinDesk)](https://www.coindesk.com/markets/2026/02/05/gemini-to-exit-u-k-eu-and-australia-reduce-staff-and-focus-on-u-s-and-prediction-markets)
- [Gemini Account Closures FAQ (Gemini Support)](https://support.gemini.com/hc/en-us/articles/46255474469275-Gemini-closing-accounts-in-the-UK-EU-and-Australia-Everything-you-need-to-know)
- [Gemini Exits UK/EU/AU (Bloomberg)](https://www.bloomberg.com/news/articles/2026-02-05/gemini-to-shutter-uk-eu-australia-customer-accounts)
- [Gemini eToro Migration (Finance Magnates)](https://www.financemagnates.com/fintech/gemini-accounts-in-the-uk-eu-and-australia-can-be-transferred-to-etoro-ahead-of-closure/)
- [Gemini Supported Payment Methods (Gemini Support)](https://support.gemini.com/hc/en-us/articles/4402719030171-What-payment-methods-are-supported)
- [Gemini Debit Card Fees (Gemini Support)](https://support.gemini.com/hc/en-us/articles/9767473757723-What-are-the-limits-and-fees-of-using-a-debit-card-on-the-Gemini-exchange)
- [Gemini Credit Card (Gemini)](https://www.gemini.com/credit-card)
- [Gemini Credit Card Review (CryptoNews)](https://cryptonews.com/reviews/gemini-credit-card-review/)
- [Gemini Predictions Launch (Gemini Blog)](https://www.gemini.com/blog/gemini-predictions-tm-is-now-live)
- [Gemini Prediction Markets (Finance Magnates)](https://www.financemagnates.com/cryptocurrency/exchange/gemini-breaks-into-prediction-markets-after-5-year-wait-challenging-kalshi-and-polymarket/)
- [Gemini CTO Pravjit Tiwana Appointment](https://www.gemini.com/blog/we-welcome-pravjit-tiwana-as-our-chief-technology-officer)
- [Gemini CTO Departing (The Block)](https://www.theblock.co/post/261804/gemini-cto-pravjit-tiwana-leaving-company-bloomberg)
- [Gemini SEC Settlement (CoinMarketCap)](https://coinmarketcap.com/academy/article/sec-reaches-settlement-with-gemini-trust-over-earn-program-reuters-reports)
- [Gemini Staking (Gemini)](https://www.gemini.com/staking)
- [Gemini EU Staking/Perpetuals Launch (CoinDesk)](https://www.coindesk.com/business/2025/09/05/crypto-exchange-gemini-expands-eu-offering-with-staking-perpetuals)
- [Gemini Exchange Review (CryptoSlate)](https://cryptoslate.com/crypto-exchanges/gemini-exchange-review/)
- [Gemini Shareholder Letter Q4 2025](https://investors.gemini.com/static-files/bf86769a-ca14-4f92-aa25-d9aa4e073dc0)
- [Gemini Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Gemini_(digital_currency_exchange)_logo.svg)
- [Gemini Crypto Statistics 2025 (CoinLaw)](https://coinlaw.io/gemini-crypto-exchange-statistics/)
