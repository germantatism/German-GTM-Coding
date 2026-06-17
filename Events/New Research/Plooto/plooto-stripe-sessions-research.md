# PLOOTO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Plooto
=======================================

Logo: https://asset.brandfetch.io/idPYWkpfCz/idExPOuL_n.svg
Nombre merchant: Plooto

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Slow Settlement Cycles
Tittle_Pain Point_2: Limited Intl Pay Methods
Tittle_Pain Point_3: No Real-Time Rails
Tittle_Pain Point_4: Card Fee Compression
Tittle_Pain Point_5: Single-Rail FX Routing

Desc_Pain Point_1: Standard EFT/ACH payments take 3 to 5 business days to settle. Competing platforms like Melio and Wise offer same-day or instant options. Slow settlement strains supplier relationships and blocks early payment discounts for 12,000+ business customers.
Desc_Pain Point_2: International payments cover 30+ countries but rely on a single cross-border rail per corridor. No Pix for Brazil, no UPI for India, no SEPA Instant for Europe. Vendors in those markets receive slow wire-equivalent transfers instead of local methods.
Desc_Pain Point_3: Plooto Instant exists for domestic payments but international transactions have no real-time option. Businesses paying overseas vendors must wait days while competitors offer near-instant cross-border settlement via local rails.
Desc_Pain Point_4: Pay by Card charges 2.9% for Visa/MC and 3.2% for Amex. Competitors like Bill.com and Melio offer free ACH with card surcharges below 2.5%. High card fees erode the working capital benefit that Pay by Card is designed to provide.
Desc_Pain Point_5: All international payments route through a single FX provider. No ability to compare rates across multiple corridors or route through the cheapest rail per currency pair, leaving margin on the table for every cross-border transaction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Visa (Pay by Card partner)
PSP_2: EFT/ACH direct bank rails
PSP_3: Cross-border wire network
PSP_4: Interac (Canada domestic)
PSP_5: (single FX provider, undisclosed)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Instant
Local_M_4: SPEI
Local_M_5: iDEAL
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: OXXO
Local_M_9: PayNow (Singapore)
Local_M_10: PromptPay (Thailand)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every cross-border payment through the optimal rail per currency pair, corridor, and amount. With 12,000+ businesses processing international AP/AR and 516% three-year revenue growth, optimizing FX routing across corridors saves basis points on every transaction at scale.
Desc_Yuno_Cap2: When an EFT/ACH payment or cross-border transfer fails, Yuno cascades to an alternate rail or processor in milliseconds. Recovers up to 50% of failed transactions, ensuring vendor payments clear on time and preserving early payment discount windows.
Desc_Yuno_Cap3: Unlocks instant local settlement in markets Plooto's 30+ country network demands: Pix in Brazil (real-time), UPI in India (instant), SEPA Instant in Europe (10-second settlement), SPEI in Mexico. One API, 1,000+ payment methods, transforming 3-5 day wire transfers into same-day local payouts.
Desc_Yuno_Cap4: Single dashboard consolidating Visa card payments, EFT/ACH domestic rails, and cross-border corridors into one view. Real-time monitoring of settlement success rates across every country, centralized FX reconciliation, and NOVA anomaly detection to flag failed or delayed payments before they impact vendor relationships.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Plooto at a glance:**
- Founded: 2015 in Toronto, Canada (325 Front Street West)
- Co-Founders: Hamed Abbasi (departed March 2024), Serguei Kloubkov (CTO, departed)
- Leadership changes in 2024: Both co-founders departed; new executive leadership from PayPal and Xero alumni
- Total funding raised: $26.4M CAD ($20M USD Series B led by Centana Growth Partners, Dec 2022; $8M CAD Series A led by FINTOP Capital, 2021)
- Revenue: Estimated $8-15M ARR range (Deloitte Fast 500 eligibility floor is $5M+)
- Revenue growth: 516% three-year growth (2021-2024)
- Customers: 12,000+ businesses (up from ~8,500 in late 2022)
- Employees: ~112 (as of Jan 2026)
- Recognition: Back-to-back Deloitte Fast 50 Canada (2023, 2024, 2025); Deloitte Fast 500 North America (ranked 233rd in 2025)
- Integrations: QuickBooks, Xero, NetSuite
- Products: AP automation, AR automation, Pay by Card, Plooto Instant, International Payments
- Visa partnership: Pay by Card launched Oct 2024 in collaboration with Visa
- Plooto Network: 150,000+ vendors and suppliers

**Confirmed Payment Infrastructure:**
- Visa: Official partner for Pay by Card feature (2.9% Visa/MC, 3.2% Amex)
- EFT (Canada) / ACH (US): Core domestic payment rails
- Cross-border wire network: International payments to 30+ countries in 25+ currencies
- Interac: Canadian domestic instant payment option
- Pre-funded accounts: Available in USD and CAD
- No payment orchestrator detected
- No disclosed third-party PSP for card processing (may use Stripe or similar under the hood)

**Payment methods offered:**
- Outgoing: EFT (Canada), ACH (US), check, wire transfer, Pay by Card (credit card to vendor via EFT/ACH/check)
- Incoming: PAD (Pre-Authorized Debit), credit card
- International: Cross-border payments to 30+ countries, 25+ currencies, from CAD or USD
- Fees: Cross-border $10/txn (Grow/Pro) or $19/txn (Go); no FX transfer fee; card 2.9% (Visa/MC) or 3.2% (Amex)

**Pricing plans:**
- Go: Starting plan with basic AP/AR
- Grow: $32/month (popular plan, 30-day free trial)
- Grow Unlimited: $59/month
- Pro/Accountant plans: From $9/month
- Enterprise: Custom pricing

**Key pain points and gaps:**
- Settlement speed: 3-5 business days standard; competitors offer same-day
- International coverage: 30+ countries but via slow wire-equivalent rails, not local instant methods
- No local payment methods in any international market (no Pix, UPI, SEPA Instant)
- Card fees higher than competitors (2.9% vs. sub-2.5% at Melio/Bill.com)
- Single FX provider for all corridors; no multi-rail routing
- Leadership instability: Both co-founders departed in 2024

**Top Markets Gap Analysis:**

MARKET 1: Canada (primary market)
  Offer: EFT, Interac, PAD, Pay by Card
  Missing: Interac e-Transfer for business AR, instant settlement
  3-5 day EFT settlement is the norm; instant domestic option exists but limited

MARKET 2: United States (secondary market)
  Offer: ACH, wire, Pay by Card
  Missing: RTP/FedNow, same-day ACH at scale
  US market is growth focus but rails are slow

MARKET 3: United Kingdom (international corridor)
  Offer: Cross-border wire in GBP
  Missing: Faster Payments, Open Banking, BACS DD
  UK payments clear in days; Faster Payments would be instant

MARKET 4: India (international corridor)
  Offer: Cross-border wire in INR
  Missing: UPI, NEFT, IMPS
  UPI processes billions of transactions monthly; wire is unnecessarily slow

MARKET 5: Europe (international corridor)
  Offer: Cross-border wire in EUR
  Missing: SEPA Instant, SEPA DD, iDEAL, BLIK
  SEPA Instant settles in 10 seconds; Plooto's wire takes days

**Key meeting angles:**
1. **Speed is the battleground**: Plooto's 3-5 day settlement loses to Melio, Wise, and Bill.com on speed. Local payment methods via Yuno convert wire-speed transfers into instant local payouts.
2. **International growth enabler**: 30+ countries served but only via slow wires. Pix, UPI, SEPA Instant via Yuno transform international AP from a cost center into a competitive advantage.
3. **516% growth trajectory**: Rapid revenue growth means payment infrastructure bottlenecks will compound. Orchestration prevents growing pains.
4. **Visa partnership leverage**: Pay by Card partnership with Visa shows willingness to partner on payment innovation. Yuno orchestration is the logical next step.
5. **Competitor pressure**: Bill.com (public, $1B+ revenue), Melio (acquired by Xero), and Wise (global) all offer faster, cheaper international payments. Plooto needs better rails to compete.
6. **12,000+ businesses**: Each customer processes multiple payments monthly. Even small improvements in success rates and settlement speed multiply across the entire customer base.

**Sources:**
- [Plooto Official Website](https://www.plooto.com/)
- [Plooto International Payments](https://www.plooto.com/features/international-business-payments)
- [Plooto Pay by Card Feature](https://www.plooto.com/features/pay-by-card)
- [Plooto Pricing](https://www.plooto.com/pricing)
- [Plooto Pay by Card Launch - BusinessWire](https://www.businesswire.com/news/home/20241024208198/en/Plooto-Launches-Pay-by-Card-Unlocking-Instant-Access-to-Short-term-Financing-for-SMBs)
- [Plooto Series B $20M - BusinessWire](https://www.businesswire.com/news/home/20221213005316/en/Payments-Automation-Platform-Plooto-Raises-%2420M-USD-%2427M-CAD-in-Series-B-Funding-Led-by-Centana-Growth-Partners)
- [Plooto Deloitte Fast 50 2024](https://www.plooto.com/newsroom/plooto-wins-the-deloitte-technology-fast-50-canada-award-for-the-second-year-in-a-row)
- [Plooto Leadership Change - BusinessWire](https://www.businesswire.com/news/home/20240304515720/en/Plooto-Announces-Change-In-Executive-Leadership)
- [Why Centana Invested in Plooto](https://www.centana.com/2023/03/30/why-centana-invested-in-plooto/)
- [Plooto: Killing the Paper Invoice - Fintech Observer](https://fintechobserver.substack.com/p/plooto-killing-the-paper-invoice)
- [Plooto - Scotiabank Digital Banking Lab](https://www.ivey.uwo.ca/scotiabank-digital-banking-lab/canada-fintech/payments-money-transfer/plooto/)
- [Melio vs Plooto vs Bill.com - LedgerFi](https://www.ledgerfi.co/resources/melio-vs.-plooto-vs.-bill-com-which-is-best-for-you)
- [Best Plooto Alternatives - Venn](https://www.venn.ca/resources/best-plooto-alternatives-for-canadian-businesses)
- [Plooto International Payments - Wise Guide](https://wise.com/ca/blog/plooto-international-payments-canada)
- [Brandfetch: Plooto Logo](https://brandfetch.com/plooto.com)
