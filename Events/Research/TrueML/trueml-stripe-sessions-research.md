# TRUEML | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: TrueML
=======================================

Logo: https://brandfetch.com/trueml.co
Nombre merchant: TrueML

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card/ACH-Only Recovery
Tittle_Pain Point_2: Single Processor Risk
Tittle_Pain Point_3: Payment Portal Friction
Tittle_Pain Point_4: Multi-Entity Complexity
Tittle_Pain Point_5: Decline Rate Leakage

Desc_Pain Point_1: TrueAccord accepts ACH, debit cards, credit cards, and checks for debt repayment. Consumers in financial distress often lack active credit cards. Missing digital wallets, BNPL arrangements, and local payment methods limits repayment options for 40M+ consumers served.
Desc_Pain Point_2: TrueAccord integrates with Stripe for payment processing, but a single processor dependency means any Stripe outage or decline spike blocks repayment for consumers ready to resolve their debt. In collections, timing is critical: a missed payment window may never reopen.
Desc_Pain Point_3: 98% of consumers resolve debt without human interaction through the self-serve portal. But the payment step still requires entering card or bank details manually. Every friction point in the payment flow reduces the conversion rate from "intent to pay" to "payment completed."
Desc_Pain Point_4: TrueML operates TrueAccord, ERC (Enhanced Recovery Company), and Sentry Credit as separate entities. Each may run different payment integrations, reconciliation systems, and processor relationships, creating operational overhead across a portfolio processing 500K-1M new accounts monthly.
Desc_Pain Point_5: Consumers in debt have higher decline rates from expired cards, insufficient funds, and issuer blocks. Static retry logic cannot adapt to real-time issuer behavior patterns. Each failed payment attempt on a debt account reduces the probability of eventual recovery.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (confirmed integration via Partial.ly/TrueAccord partnership)
PSP_2: ACH direct bank transfers
PSP_3: Check payments (legacy)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Venmo
Local_M_3: Cash App Pay
Local_M_4: Apple Pay
Local_M_5: Google Pay
Local_M_6: Pix
Local_M_7: SEPA Direct Debit
Local_M_8: UPI
Local_M_9: OXXO
Local_M_10: Zelle

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Auto-Retry
Tittle_Yuno_Cap3: Consumer Payment Options
Tittle_Yuno_Cap4: Unified Collections Layer

Desc_Yuno_Cap1: Per-transaction routing optimizes every debt repayment based on card BIN, issuer, and payment amount. With 500K-1M new accounts monthly and collection rates 30-300% above traditional collectors, even 3% auth uplift on repayment attempts translates directly into millions in additional recovery.
Desc_Yuno_Cap2: Automatic cascade across acquirers when Stripe declines a repayment. In debt collection, a consumer ready to pay represents a narrow window. Yuno reroutes to the next best acquirer in milliseconds, recovering up to 50% of failed transactions. Every recovered payment is revenue that would otherwise be lost permanently.
Desc_Yuno_Cap3: One API adds digital wallets (Apple Pay, Google Pay, PayPal, Venmo, Cash App) to the self-serve portal. Consumers in financial distress often have wallet balances when card limits are exhausted. 1,000+ payment methods reduce friction at the critical moment of repayment intent.
Desc_Yuno_Cap4: Single dashboard unifying payment flows across TrueAccord, ERC, and Sentry Credit. Centralized decline analytics, real-time approval rate monitoring per creditor portfolio, and NOVA intelligence with 75% faster fraud detection. One reconciliation view replacing fragmented multi-entity processor reporting.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**TrueML at a glance:**
- Founded: 2013 by Ohad Samet (CEO) and Nadav Samet
- Headquarters: Lenexa, KS
- CEO: Ohad Samet (previously leadership roles at PayPal and Klarna)
- Employees: 224+ (TrueAccord alone as of Dec 2023; group likely larger with ERC and Sentry)
- Funding: $142M raised from 41 investors including PayPal Ventures, Raptor Group, Top Corner Capital, Calm Ventures, CE Innovation Capital
- Active accounts: 26M+
- Consumers served: 40M+ since 2013
- Monthly inflow: 500K to 1M new accounts from creditors
- Collection rates: 30-300% better than traditional debt collectors
- 98% of consumers resolve debt without human interaction
- Clients: PNC, Capital One, Amex, plus BNPL, fintech, telecom, credit unions
- Industry size: Operating in a $20B debt collection industry

**TrueML portfolio companies:**
- TrueAccord: Digital-first third-party debt collection platform (flagship)
- Enhanced Recovery Company (ERC): Tech-enabled debt collection agency (acquired October 2022)
- Sentry Credit: First-party and litigation collection services (acquired May 2025)
- Retain: SaaS product for early-stage recovery using patented ML
- Recover: Full-service debt collection platform

**Confirmed payment stack:**
- Stripe: Confirmed integration (collections from Partial.ly defaulted plans transfer to Stripe balance minus 35% fee)
- ACH: Direct bank transfers for debt repayment
- Debit cards: Accepted for one-time and recurring payments
- Credit cards: Accepted for one-time and recurring payments
- Checks: Legacy payment method still accepted
- Self-serve portal: Digital payment experience, 98% no-human-interaction resolution
- No payment orchestrator detected

**Payment challenges identified:**
- Limited payment methods: Only cards, ACH, and checks; no digital wallets (PayPal, Venmo, Cash App, Apple Pay, Google Pay)
- Consumers in financial distress often lack active credit/debit cards
- Single processor dependency creates risk for time-sensitive debt repayments
- Multi-entity payment infrastructure across TrueAccord, ERC, and Sentry Credit
- Higher-than-average decline rates from financially distressed consumer card profiles
- Manual card/bank entry friction in self-serve portal reduces payment conversion
- Each failed repayment attempt reduces probability of future recovery
- 500K-1M new accounts/month creates massive payment processing volume

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary and likely sole market)
  Accepted: Visa/MC/Amex/Discover, ACH, debit cards, checks
  Missing: PayPal, Venmo, Cash App Pay, Apple Pay, Google Pay, Zelle
  Digital wallets critical for financially distressed consumers who may have wallet balances but no active cards.

MARKET 2: Digital Wallet Ecosystem (US consumers)
  Accepted: Card-on-file, ACH
  Missing: PayPal, Venmo, Cash App, Apple Pay, Google Pay
  56% of US consumers use digital wallets. Distressed consumers more likely to have wallet balances than card credit.

MARKET 3: Underbanked/Unbanked Consumers (US)
  Accepted: Debit cards, checks
  Missing: Cash-based methods (retail pay points), prepaid card paths, mobile money
  7M+ US households are unbanked. Cash-based repayment options would expand recoverable accounts.

MARKET 4: BNPL/Fintech Creditor Portfolios (cross-border consumers)
  Accepted: US cards and ACH only
  Missing: SEPA DD, Pix, UPI, local methods
  BNPL clients like Klarna serve global consumers; cross-border debt recovery needs local payment rails.

MARKET 5: Future International Expansion
  Accepted: None currently outside US
  Missing: SEPA DD, Pix, UPI, OXXO, BLIK, local bank transfers
  $20B global industry. If TrueML expands internationally, local payment infrastructure is prerequisite.

**Key meeting angles:**
1. **Revenue-per-payment is everything** | In debt collection, every successful payment is direct revenue; smart routing optimization has outsized ROI vs. typical commerce
2. **Time-critical windows** | Consumers ready to pay represent a narrow behavioral window; failover ensures the payment succeeds on the first attempt
3. **40M+ consumers, 98% digital** | Massive self-serve payment volume through the portal; adding wallets and reducing friction directly increases recovery rates
4. **PayPal Ventures investor** | PayPal already invested in TrueML; payment infrastructure improvement aligns with investor thesis
5. **Multi-entity consolidation** | TrueAccord + ERC + Sentry Credit need unified payment orchestration across all three collection operations
6. **Distressed consumer profiles** | Higher decline rates require smarter routing; ML-driven routing adapts to issuer patterns for this specific consumer segment
7. **CEO from payments** | Ohad Samet spent years at PayPal and Klarna; speaks the language of payment optimization natively

**Sources:**
- [TrueML Homepage](https://trueml.co/)
- [TrueAccord Homepage](https://www.trueaccord.com/)
- [TrueAccord for Consumers](https://consumers.trueaccord.com/)
- [TrueAccord Payment Terms](https://www.trueaccord.com/payment-terms)
- [TrueAccord Payment Plan Terms of Service](https://www.trueaccord.com/payment-plan-terms-of-service/)
- [TrueAccord How It Works](https://www.trueaccord.com/product/how-it-works)
- [TrueAccord Self-Serve Portal eBook](https://pages.trueaccord.com/SelfServePortaleBook.html)
- [TrueAccord Blog: Self-Serve Consumer Experience](https://blog.trueaccord.com/2024/10/the-trueaccord-difference-for-a-better-self-serve-consumer-experience/)
- [Retain ML Blog](https://blog.getretain.com/how-retain-uses-machine-learning-for-digital-debt-collection/)
- [TrueML Acquires ERC (PRNewswire)](https://www.prnewswire.com/news-releases/trueml-acquires-erc-recovery-business-301640209.html)
- [TrueAccord Acquires Sentry Credit](https://www.prweb.com/releases/trueaccord-accelerates-growth-with-acquisition-of-sentry-credit-302448199.html)
- [Ohad Samet CEO Profile (Fintech Leaders)](https://fintechleaders.substack.com/p/ohad-samet-ceo-and-co-founder-of)
- [TrueML Globy Podcast: 26M Active Accounts](https://gogloby.io/podcast/ohad-samet/)
- [TenOneTen Ventures: TrueML Portfolio](https://www.tenoneten.com/portfolio/trueml)
- [Not Boring: TrueAccord Unsexiness as Moat](https://www.notboring.co/p/trueaccord-unsexiness-as-a-moat)
- [TrueML Crunchbase](https://www.crunchbase.com/organization/trueml)
- [TrueAccord 40M Consumers Served](https://blog.trueaccord.com/2022/07/trueaccord-digitally-serves-20-million-consumers-on-path-to-financial-health/amp/)
