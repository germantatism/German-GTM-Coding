# AMAZON | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Amazon
=======================================

Logo: https://assets.aboutamazon.com/2e/d7/ac71f1f344c39f8949f48fc89e71/amazon-logo-squid-ink-smile-orange.png
Nombre merchant: Amazon

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Outage Vulnerability
Tittle_Pain Point_3: Checkout Decline Loops
Tittle_Pain Point_4: Wallet Ecosystem Gaps
Tittle_Pain Point_5: Cross-Border Auth Loss

Desc_Pain Point_1: Chase Paymentech, Worldpay, Mastercard Gateway across regions with no unified orchestration. Each market runs siloed routing, blocking $588B optimization.
Desc_Pain Point_2: March 2026 outage lasted 5+ hours with 18,000+ reports. Users could not checkout, add gift cards, or switch payment methods. Zero automated failover activated.
Desc_Pain Point_3: "Payment Revision Needed" errors (codes 2063, 2016, 2026) push users to "contact your bank" with no in-flow recovery or APM suggestion. Drives cart abandonment.
Desc_Pain Point_4: Amazon blocks PayPal, Google Pay, Apple Pay on web to protect Amazon Pay. Excludes hundreds of millions of wallet users who prefer their default digital wallet.
Desc_Pain Point_5: International segment ($161.9B) spans 23 marketplaces. Cross-border card transactions face elevated declines from local issuers flagging foreign acquirer BINs.

SLIDE 1: PSP TOPOLOGY

PSP_1: Chase Paymentech PSP_2: Worldpay PSP_3: Mastercard Gateway PSP_4: Amazon Pay (proprietary)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Google Pay
Local_M_3: Apple Pay (web)
Local_M_4: Bizum (Spain)
Local_M_5: Bancontact (Belgium)
Local_M_6: iDEAL (Netherlands)
Local_M_7: MBWay (Portugal)
Local_M_8: Mercado Pago (LATAM)
Local_M_9: DANA (Indonesia)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each of Amazon's billions of annual transactions to the optimal acquirer per card BIN, issuer, and market. With $588B in e-commerce revenue, even a 1% auth uplift recovers $5.8B in lost sales. Real-time processor performance analysis per corridor.
Desc_Yuno_Cap2: Automatic cascade across Chase Paymentech, Worldpay, and Mastercard Gateway. When one acquirer declines or goes down (March 2026 outage), Yuno reroutes in ms. NOVA AI recovers 75% of soft declines. Livelo recovered 50% of failed transactions.
Desc_Yuno_Cap3: Activate missing wallets across all 23 Amazon marketplaces: PayPal, Google Pay, Apple Pay on web; Bizum in Spain, iDEAL in Netherlands, Bancontact in Belgium, DANA in Indonesia, GrabPay in SE Asia. One API, zero per-market engineering.
Desc_Yuno_Cap4: Replace Amazon's siloed regional stacks with one real-time dashboard. Centralized approval monitoring across Chase Paymentech, Worldpay, Mastercard Gateway. ms anomaly detection catches issues like the March 2026 outage before they reach users.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Amazon at a glance:**
- NASDAQ: AMZN. World's largest e-commerce company
- FY2025 Revenue: $716.9B total ($426.3B North America, $161.9B International, $128.7B AWS)
- 23 marketplace websites operating across 20+ countries
- 2.0 to 2.3B monthly visits on amazon.com alone; combined global traffic exceeds 4 to 5B monthly visits
- 3P marketplace sellers account for approximately $300B in GMV
- Amazon operates a fully proprietary payment stack and acts as its own orchestrator
- AWS "Cognitive Payments Director" confirms in-house AI routing on AWS Bedrock
- Worldpay (Amazon Pay's primary acquirer) acquired by Global Payments for $24.5B in January 2026

**Confirmed PSPs:**
- Chase Paymentech (now Chase Payment Solutions): primary US acquirer, processes $1T+ annually
- Worldpay: first acquirer for Amazon Pay, now under Global Payments ownership
- Mastercard Gateway: adopted via Amazon Payment Services for 9 MEA countries
- Amazon Pay: proprietary PSP with 110M+ UPI users in India
- Regional banking partners: Axis Bank, RBL Bank, Yes Bank (India UPI), IDFC FIRST Bank (BNPL via Axio)
- BNPL partners: Affirm (US), Paidy (Japan), Afterpay and Zip (Australia), Amazon Pay Later (India)
- No third-party payment orchestrator detected (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States ($426.3B North America revenue, ~2.0 to 2.3B monthly visits)
  Offer: Visa, MC, Amex, Discover, JCB, Diners Club; Amazon Store Card; prepaid gift cards; FSA/HSA; EBT/SNAP; ACH checking account; Affirm BNPL
  Missing: PayPal, Google Pay, Apple Pay (web), Venmo, Cash App Pay
  Why it matters: PayPal has 430M+ active accounts globally. Google Pay and Apple Pay dominate mobile wallet usage. Amazon deliberately blocks these to promote Amazon Pay, but this creates friction for users whose default wallet is excluded.

MARKET 2: Germany ($40.9B revenue, ~407 to 512M monthly visits on amazon.de)
  Offer: Visa, MC, Amex; Amazon Visa; SEPA Direct Debit; Kauf auf Rechnung (Pay by Invoice); Monthly Invoice (DE, AT, DK, NO, FI, SE, CH)
  Missing: PayPal (explicitly not accepted), Giropay (discontinued but successor), Klarna
  Why it matters: PayPal is the most popular online payment method in Germany (used by 57% of online shoppers). Explicit exclusion is a major friction point.

MARKET 3: United Kingdom ($37.86B revenue, ~370 to 487M monthly visits on amazon.co.uk)
  Offer: Visa, MC, Amex; debit cards; Pay by Bank (open banking redirect); SEPA Direct Debit (EUR)
  Missing: PayPal, Google Pay, Apple Pay (web), Klarna
  Why it matters: Open banking adoption is growing but PayPal remains dominant for UK online payments. Missing major wallets limits checkout conversion.

MARKET 4: Japan ($27.4B revenue, ~525 to 743M monthly visits on amazon.co.jp)
  Offer: Visa, MC, Amex, JCB, Diners; Konbini (7-Eleven, Lawson, FamilyMart, MiniStop); ATM/Pay-easy; Internet Banking; E-Money (Edy, Mobile Suica); Carrier Billing (docomo, au, SoftBank, Y!mobile); Paidy BNPL; Pay ID
  Missing: LINE Pay, Rakuten Pay, PayPay, Merpay
  Why it matters: PayPay has 63M+ users in Japan. LINE Pay and Rakuten Pay are top mobile wallets. Amazon offers deep local payment integration but excludes competing mobile wallets.

MARKET 5: Brazil ($1.2% traffic share, growing rapidly; amazon.com.br)
  Offer: Visa, MC, Elo, Amex; Visa/Elo debit; Pix (QR code, 30-min window, Automatic Pix for Prime); Boleto Bancario (1-day expiry)
  Missing: Mercado Pago, PicPay, Google Pay, Nubank direct integration
  Why it matters: Mercado Pago is the most used digital wallet in Brazil with 50M+ users. Amazon has strong local APM coverage with Pix and Boleto but blocks competing fintech wallets.

**Outage and incident history:**
- March 5, 2026: Major outage lasting 5+ hours starting at 1:55 PM ET. Over 18,000 user reports. Users could not see product prices, complete checkout, add gift cards, pay for orders, or switch payment methods. Amazon Fresh and Whole Foods also affected. No automated failover.
- October 2025: AWS global outage affected US-EAST-1 region with significant API errors and connectivity issues. Amazon Pay and other services dependent on AWS infrastructure were impacted.
- Recurring "Payment Revision Needed" errors: Error codes 2063, 2016, 2021, 2023, 2026, 2027, 2028, 2029, 2040, 2041, 2043, 2044, 2047, 2048, 7035. So common that multiple third-party troubleshooting guides exist.
- Double charges: Recurring complaints on Trustpilot and consumer forums about authorization hold patterns creating duplicate charges.
- FTC scrutiny: $2.5B settlement related to refund practices; ongoing regulatory attention on chargebacks and consumer protection.

**Key meeting angles:**
1. **Worldpay ownership change** | Worldpay (Amazon Pay's primary acquirer) now under Global Payments. Contract renegotiation window creates openness to evaluating alternatives.
2. **Outage resilience** | March 2026 outage (5+ hours, 18K+ reports) exposed zero-failover architecture. Yuno's automatic cascade would have prevented revenue loss during downtime.
3. **LATAM acceleration** | Amazon expanding to Colombia and Chile with plans for 10 new markets. Yuno has proven LATAM infrastructure (InDrive: 10 markets, 90% approval; Rappi: zero implementation cost).
4. **Wallet exclusion strategy risk** | Blocking PayPal, Google Pay, Apple Pay preserves Amazon Pay but causes measurable checkout friction for hundreds of millions of wallet users.
5. **Amazon Payment Services as competitor** | APS operates in 9 MENA countries with Mastercard Gateway. Yuno competes for MENA merchants who want multi-PSP flexibility vs. Amazon's single-provider lock-in.
6. **3P seller opportunity** | ~$300B GMV from 3P sellers who also sell on Shopify, Walmart, eBay. These sellers need multi-channel payment orchestration outside Amazon's walled garden.
7. **AI orchestration parallel** | AWS published "Cognitive Payments Director" on Bedrock. Amazon is thinking about AI-driven routing, Yuno already delivers it in production.

**Amazon Payments team:**
- Processes billions of dollars annually, millions of transactions daily, across 50+ payment methods
- Payment Service Provider Program (PSPP) team actively hiring Software Development Engineers
- Amazon Pay India CEO: Vikas Bansal
- Doug Herrington leads global retail operations
- No dedicated external-facing VP of Payments identified in public sources

**Recent corporate developments:**
- Sep 2025: Acquired Axio (formerly Capital Float) for ~$150 to 200M; Indian NBFC powering Amazon Pay Later for 10M+ customers
- Jan 2026: Worldpay acquired by Global Payments for $24.5B; Amazon Pay's primary acquirer under new ownership
- Jan 2026: Amazon Pay launches Fixed Deposits product in India (multi-bank comparison)
- Dec 2025: Amazon Pay introduces biometric authentication for UPI (fingerprint/face) up to INR 5,000 on Android
- 2025: Global Partner Program launched, opening PSP ecosystem for cross-border sellers
- 2025: Mastercard + Amazon Payment Services multi-year MEA partnership (9 countries)
- 2025: Amazon Pay In-Store Payments expanded to major US/UK retail chains; 20% increase in merchant adoption
- 2025: Amazon Pay plans expansion to 10 new markets (LATAM, SE Asia focus)
- 2025 to 2026: 23 marketplace websites operational; recent additions include Ireland, Belgium, South Africa, Nigeria, Colombia

**IMPORTANT NOTE:** Amazon operates a fully proprietary payment stack and effectively acts as its own orchestrator. This is NOT a traditional prospect for payment orchestration sales. The primary opportunities are: (1) Amazon's 3P marketplace sellers who sell across platforms, (2) Amazon's competitive peer set (Coupang, SHEIN, Temu) that lacks payment orchestration, (3) Merchants evaluating Amazon Payment Services in MENA where Yuno competes.

**Sources:**
- [Amazon Official Logo (Press Center)](https://press.aboutamazon.com/logos)
- [Amazon US Payment Methods](https://www.amazon.com/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon UK Payment Methods](https://www.amazon.co.uk/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon DE Payment Methods](https://www.amazon.de/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon JP Payment Methods](https://www.amazon.co.jp/-/en/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon IN Payment Methods](https://www.amazon.in/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon BR Payment Methods](https://www.amazon.com.br/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon MX Payment Methods](https://www.amazon.com.mx/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Amazon AU Payment Methods](https://www.amazon.com.au/gp/help/customer/display.html?nodeId=GFBWMNXEPYVJAY9A)
- [Chase Paymentech as Amazon acquirer (Quora)](https://www.quora.com/Which-company-handles-Amazons-credit-card-processing)
- [Worldpay enables Amazon Pay (Finextra)](https://www.finextra.com/newsarticle/33565/worldpay-becomes-first-acquirer-to-enable-amazon-pay)
- [Amazon Revenue by Region (Bullfincher)](https://bullfincher.io/companies/amazoncom/revenue-by-geography)
- [Amazon Q4 2025 Earnings (Digital Commerce 360)](https://www.digitalcommerce360.com/article/amazon-sales/)
- [Mastercard + Amazon Payment Services MEA (FinTech Magazine)](https://fintechmagazine.com/articles/mastercard-and-amazon-payment-services-ink-mea-deal)
- [AWS Agentic Payments Blog](https://aws.amazon.com/blogs/industries/agentic-payments-the-next-evolution-in-the-payments-value-chain/)
- [Amazon PSPP Job Posting (Amazon.jobs)](https://www.amazon.jobs/en-gb/jobs/2116384/software-development-engineer-payment-service-provider-program-pspp)
- [Amazon Pay India UPI (AboutAmazon.in)](https://www.aboutamazon.in/news/retail/how-urban-india-pays)
- [Amazon Axio Acquisition (AboutAmazon.in)](https://www.aboutamazon.in/news/company-news/amazon-acquires-axio)
- [Amazon Global Marketplaces Guide (EasyParser)](https://easyparser.com/blog/amazon-global-marketplaces-2025-complete-guide)
- [Amazon March 2026 Outage (Tom's Guide)](https://www.tomsguide.com/computing/live/amazon-is-down-live-outage-report-as-users-cant-check-out-see-product-reviews-and-more)
- [AWS October 2025 Outage (CNN)](https://www.cnn.com/business/live-news/amazon-tech-outage-10-20-25-intl)
- [Amazon Payment Revision Error (Izoate)](https://www.izoate.com/blog/how-to-fix-amazon-error-2063-2026-prime-video-payment-failed-solution/)
- [Amazon FTC Settlement (FTC)](https://www.ftc.gov/enforcement/refunds/amazon-refunds)
- [Amazon Chargebacks (Justt)](https://justt.ai/blog/amazon-chargebacks/)
- [Amazon No PayPal (SlashGear)](https://www.slashgear.com/1943009/why-amazon-does-not-accept-paypal-and-what-you-can-use-instead/)
- [PayPal on Amazon (PayPal)](https://www.paypal.com/us/cshelp/article/how-do-i-make-payments-with-paypal-on-amazon-help595)
- [Amazon Pay India Statistics (Inc42)](https://inc42.com/features/can-amazon-pay-turn-scale-into-fintech-dominance/)
- [Amazon Subsidiaries (LexChart)](https://lexchart.com/amazon-subsidiaries-2025/)
- [Amazon LATAM Expansion (MerchantSpring)](https://resources.merchantspring.io/blog/amazon-expansion-in-latam-opportunities-risks-strategy)
- [Worldpay Acquired by Global Payments (Digital Transactions)](https://www.digitaltransactions.net/how-top-u-s-acquirers-ranking-changed-following-acquisitions/)
- [Amazon Pay Statistics (CoinLaw)](https://coinlaw.io/amazon-pay-statistics/)
- [Trustpilot Amazon Reviews](https://www.trustpilot.com/review/www.amazon.com)
