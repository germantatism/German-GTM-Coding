# XERO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Xero
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/en/9/9f/Xero_software_logo.svg
Nombre merchant: Xero

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: US Market Payment Gap
Tittle_Pain Point_3: Reconciliation Drag
Tittle_Pain Point_4: Cross-Border Cost Bleed
Tittle_Pain Point_5: Melio Integration Risk

Desc_Pain Point_1: Stripe, GoCardless, PayPal, and Melio operate as disconnected rails. Each PSP has its own dashboard, fee structure, and settlement timeline across 180+ countries.
Desc_Pain Point_2: US is the #1 growth priority but Xero lacked native bill pay until the $2.5B Melio acquisition. International bill payments planned for 2026, not yet live.
Desc_Pain Point_3: Xero Central forums document Stripe and GoCardless reconciliation problems. Multi-PSP settlement across AUD, NZD, GBP, USD creates complexity for 4.6M subs.
Desc_Pain Point_4: AU (58% revenue) and NZ (12%) are domestic, but UK (21%) and US (9%) involve cross-border processing. FX markup on every non-local transaction compounds.
Desc_Pain Point_5: Melio ($2.5B, Oct 2025) processes $30B yearly on its own stack. Integrating Melio's rails with Xero's Stripe/GoCardless creates orchestration complexity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: GoCardless
PSP_3: PayPal
PSP_4: Melio (acquired)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: SPEI
Local_M_5: BLIK
Local_M_6: M-Pesa
Local_M_7: GCash
Local_M_8: Konbini
Local_M_9: PSE
Local_M_10: PromptPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, GoCardless, Melio, and PayPal by market, currency, and payment type. With NZ$2.1B revenue and 4.6M subscribers, routing each invoice payment to the best PSP per corridor delivers 3 to 10% cost savings.
Desc_Yuno_Cap2: Automatic cascade across Xero's multi-PSP stack. When a GoCardless direct debit fails, Yuno reroutes to Stripe card or PayPal in milliseconds. Up to 50% recovery on failed invoice payments. Eliminates manual retry workflows documented in Xero Central forums.
Desc_Yuno_Cap3: Extends Xero beyond AU/NZ/UK/US into global markets: Pix in Brazil, UPI in India, OXXO in Mexico, M-Pesa in Kenya, GCash in Philippines. One API, 1,000+ methods. Accelerates international bill payments launch planned for 2026.
Desc_Yuno_Cap4: One dashboard unifying Stripe, GoCardless, PayPal, and Melio under a single reconciliation layer. Eliminates the Stripe sync issues documented in Xero Central. Real-time monitoring, NOVA AI (75% recovery), and automated settlement matching for 4.6M subscribers.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Xero at a glance:**
- Founded: 2006, HQ: Wellington, New Zealand. Public company (ASX: XRO)
- Revenue: NZ$2.1B (FY2025, +23% YoY), equivalent to ~US$1.23B
- H1 FY2026: NZ$1.19B operating revenue (+20% YoY)
- Subscribers: 4.59M (H1 FY2026, +10% YoY)
- Subscriber breakdown: AU/NZ 2.6M, International 1.9M (UK 900K+, North America 400K+)
- Revenue by market: Australia 58%, UK 21%, NZ 12%, North America 9%
- Products: Accounting, Payroll, Payments, Tax, Projects, Analytics
- Strategy: "Win the 3x3" (accounting, payroll, payments across US, UK, Australia)
- Major acquisition: Melio ($2.5B, completed Oct 2025) for US bill pay
- Melio stats: 80K customers, $30B payment volume in FY25, $153M revenue
- Offices: NZ, Australia, UK, US, Canada, South Africa, Singapore
- Operates in 180+ countries
- Market share: 32.8% UK (#1), 30% AU (#1), 6.66% global accounting

**Confirmed PSPs:**
- Stripe: primary card payment processor (integrated into Xero invoice Pay Now buttons). Credit card, debit card, Apple Pay, Google Pay
- GoCardless: direct debit processor (BACS UK, SEPA EU, PAD Canada, ACH US). Being acquired by Mollie
- PayPal: standalone payment option for invoices
- Melio: US bill pay ($2.5B acquisition, processes ACH, cards, checks for outbound AP)
- No third-party payment orchestrator detected

**Confirmed Payment Methods:**
- Credit/debit cards (via Stripe)
- Apple Pay, Google Pay (via Stripe)
- BACS Direct Debit (UK, via GoCardless)
- SEPA Direct Debit (EU, via GoCardless)
- PAD Pre-Authorized Debit (Canada, via GoCardless)
- ACH Direct Debit (US, via GoCardless/Melio)
- PayPal
- Tap to Pay (in-person, US)

**Top 5 Markets Gap Analysis:**

MARKET 1: Australia (58% of revenue, 1.7M+ subscribers)
  Currently offer: Visa/MC, Apple Pay, Google Pay, BECS Direct Debit
  Missing: PayTo (NPP real-time), BPAY
  Impact: PayTo is the next-gen Australian direct debit. BPAY is used by 90%+ of Australian bill payers.

MARKET 2: United Kingdom (21% of revenue, 900K+ subscribers)
  Currently offer: Visa/MC, BACS Direct Debit, Apple Pay, Google Pay
  Missing: Open Banking (PayByBank), Faster Payments
  Impact: Open Banking bypasses card fees entirely. Growing rapidly for invoice and subscription payments in UK.

MARKET 3: New Zealand (12% of revenue, 500K+ subscribers)
  Currently offer: Visa/MC, direct debit
  Missing: POLi, Account2Account
  Impact: POLi is NZ's dominant online bank transfer method. Low card penetration makes bank transfers critical.

MARKET 4: United States (9% of revenue, 400K+ subscribers, Melio)
  Currently offer: ACH, cards, checks (via Melio), Stripe cards, Apple Pay
  Missing: Venmo, Cash App Pay, RTP/FedNow
  Impact: Melio fills AP gap but outbound international payments still limited. RTP enables instant settlement.

MARKET 5: South Africa (office confirmed)
  Currently offer: Cards (via Stripe)
  Missing: EFT, Instant EFT (Ozow/Peach), SnapScan
  Impact: SA has low card penetration. EFT is the dominant payment method for business invoices.

**Payment complaint evidence:**
- Xero Central: "Stripe and Xero reconciliation problems" documented in community forums
- Xero Central: "GoCardless automated payments problem" threads
- GoCardless App Store reviews: accounts closed without explanation, disrupting business operations
- Currency mismatch errors when GoCardless bank currency differs from invoice currency
- Multi-PSP reconciliation complexity across Stripe, GoCardless, and PayPal

**Key meeting angles:**
1. **$2.5B Melio integration creates orchestration need** | Merging Melio's payment stack with existing Stripe/GoCardless/PayPal demands a unified layer
2. **GoCardless being acquired by Mollie** | PSP ownership change creates vendor uncertainty for 4.6M subscribers relying on direct debit rails
3. **US market is #1 growth priority** | "Win the 3x3" strategy targets US but international bill payments still not live
4. **Multi-PSP reconciliation pain documented** | Xero Central forums show real Stripe/GoCardless sync issues that an orchestration layer solves
5. **4.6M subscribers across 180+ countries** | Scale demands automated routing, not manual PSP-by-PSP configuration
6. **Payments is one of three strategic pillars** | Xero explicitly names payments as a core strategic focus alongside accounting and payroll
7. **International expansion bottleneck** | AU/NZ/UK strong but rest of world has minimal local payment rail coverage

**Sources:**
- [Xero: Accept Payments](https://www.xero.com/us/accounting-software/accept-payments/)
- [Xero: Stripe Partnership](https://www.xero.com/us/partnerships/stripe/)
- [Xero: Payment Apps Marketplace](https://apps.xero.com/us/function/payments)
- [Xero: Media Factsheet](https://www.xero.com/us/media/factsheet/)
- [Xero: Media Downloads](https://www.xero.com/us/media/downloads/)
- [Xero Central: Fix Payment Service Issues](https://central.xero.com/s/article/Fix-problems-with-payment-services)
- [Xero Central: Stripe Reconciliation Problems](https://central.xero.com/s/question/0D53m00005qPQQSCA4/stripe-and-xero-reconciliation-problems)
- [Xero Central: GoCardless Payments Problem](https://central.xero.com/s/question/0D53m00009ESYDACA5/gocardless-automated-payments-problem)
- [Xero: Melio Acquisition PR](https://www.prnewswire.com/news-releases/xero-to-acquire-melio-a-leading-us-smb-bill-pay-solution-to-accelerate-global-growth-302490268.html)
- [Xero Blog: Melio Acquisition](https://blog.xero.com/news-events/xero-to-acquire-melio/)
- [CPA Practice Advisor: Xero Completes Melio Acquisition](https://www.cpapracticeadvisor.com/2025/10/15/xero-acquires-payments-platform-melio-for-2-5b/170967/)
- [FinTech Magazine: Xero 23% Revenue Surge](https://fintechmagazine.com/articles/xero-reports-23-revenue-surge-as-platform-strategy-pays-off)
- [CompaniesMarketCap: Xero Revenue](https://companiesmarketcap.com/aud/xero/revenue/)
- [Alpha Partners: Xero 1M AU/NZ Subscribers](https://www.alphapartners.co/blog/xero-reaches-1-million-subscribers-in-new-zealand-and-australia)
- [6Sense: Xero Market Share](https://6sense.com/tech/accounting/xero-market-share)
- [Xero Wikipedia](https://en.wikipedia.org/wiki/Xero_(company))
