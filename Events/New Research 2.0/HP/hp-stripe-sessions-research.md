# HP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-28*

```
=======================================
DATABASE FIELDS: HP
=======================================

Logo: https://companieslogo.com/img/orig/HPQ-1f7eaeb6.png
Nombre merchant: HP

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Instant Ink Renewal Failures
Tittle_Pain Point_2: Limited LATAM APM Coverage
Tittle_Pain Point_3: No Orchestration Layer
Tittle_Pain Point_4: Asia Local Wallet Gap
Tittle_Pain Point_5: PayPal Cascade Fragility

Desc_Pain Point_1: HP Support forums document repeated "Instant Ink Account Needs Attention" alerts. With 1M+ subscribers and $1B ARR, every failed renewal triggers churn.
Desc_Pain Point_2: HP.com in Brazil and Mexico relies on credit cards. PIX, OXXO, and SPEI are not at checkout. LATAM consumers default to local rails, capping reach.
Desc_Pain Point_3: No payment orchestration platform confirmed for HP.com. Personal Systems, Print, and Instant Ink run on a fragmented stack with no smart routing or failover.
Desc_Pain Point_4: HP sells across Japan, Korea, India, and SE Asia. PayPay, KakaoPay, NaverPay, UPI, and Konbini are absent. Card decline rates inflate cart abandonment.
Desc_Pain Point_5: HP forums show orders declined on card plus PayPal simultaneously. With only card, PayPal, and Klarna, no automatic third option exists when both rails fail.

SLIDE 1: PSP TOPOLOGY

PSP_1: Internal Billing Stack
PSP_2: Credit/Debit Cards (Visa, MC, Amex, Discover)
PSP_3: PayPal + Google Pay
PSP_4: Klarna + Zip (BNPL)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: OXXO (Mexico)
Local_M_4: SPEI (Mexico)
Local_M_5: UPI (India)
Local_M_6: PayPay (Japan)
Local_M_7: Konbini (Japan)
Local_M_8: KakaoPay (South Korea)
Local_M_9: NaverPay (South Korea)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route every Instant Ink renewal and every HP.com order to the optimal acquirer per BIN, issuer, and country. On $55.3B FY2025 revenue, a 3 to 10% auth lift recovers hundreds of millions across Personal Systems, Print, and subscriptions.
Desc_Yuno_Cap2: When a card or PayPal renewal fails, Yuno cascades instantly to a backup acquirer or method. NOVA AI recovers up to 75% of soft declines before the subscriber sees a "Needs Attention" alert. Livelo recovered 50% of failed transactions this way.
Desc_Yuno_Cap3: Activate PIX, OXXO, SPEI, UPI, PayPay, Konbini, and KakaoPay through one API. No per-market engineering. InDrive launched 10 LATAM markets in under 8 months. HP could unlock 50+ markets without rebuilding checkout.
Desc_Yuno_Cap4: Replace HP's siloed billing with one dashboard across Personal Systems, Print, and Instant Ink. Centralized auth-rate monitoring across Americas, EMEA, and Asia. Anomaly detection catches renewal failures before they spike into churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**HP at a glance:**
- NYSE: HPQ. Global leader in PCs, printers, and print subscriptions
- FY2025 (ended October 31, 2025) Net Revenue: $55.3B (up 3.2% YoY)
- Q1 FY2026 Revenue: $14.4B (up 6.9% YoY, up 5.2% in constant currency)
- Q1 FY2026 Non-GAAP diluted EPS: $0.81 (up 9% YoY)
- Personal Systems Q1 FY2026: $10.3B (up 11% YoY). Consumer PS up 16%, Commercial PS up 9%
- Printing Q1 FY2026: $4.2B (down 2% YoY) with 18.3% operating margin
- AI PCs over 35% of PC shipments in Q1 FY2026, up from 30% prior quarter
- Instant Ink subscribers crossed 1M, with consumer subscriptions near $1B ARR
- Consumer Printing FY2025 Q4: down 9% YoY. Q1 FY2026: down 8%
- FY2026 Guidance: Non-GAAP EPS $2.90 to $3.20. FCF $2.8B to $3.0B
- Products: HP laptops and desktops (Pavilion, OMEN, EliteBook, Spectre), HP printers, Instant Ink subscription, HP All-in plans, Smart Tank printers, HP Poly

**Confirmed PSPs and Payment Infrastructure:**
- Internal Billing Stack: HP processes Instant Ink and HP.com transactions through its own billing infrastructure. No external payment orchestrator publicly confirmed
- Credit/Debit Cards (US): Visa, Mastercard, Amex, Discover accepted
- PayPal: Available on HP.com US and key markets including UK, plus PayPal Credit and PayPal Pay in 3 in UK
- Google Pay: Available on HP.com US
- Klarna: Pay in 3 available on HP UK store (interest-free 3 instalment plan)
- Zip (US): BNPL available, splits HP purchases into 4 interest-free payments
- HP Financing: Available US, plus HP.com gift cards
- Direct Debit: Accepted for Instant Ink subscription billing in select countries (IBAN)
- HP Instant Ink Prepaid Card: Allowed as payment method
- No payment orchestration platform confirmed (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: Americas (US, Canada, Brazil, Mexico)
  Accepted: Visa, Mastercard, Amex, Discover, PayPal, Google Pay, Klarna (where available), Zip (US), HP Financing
  Missing: PIX (Brazil, 150M+ users), Boleto (Brazil), OXXO (Mexico, 20K+ stores), SPEI (Mexico), Cash App Pay
  Note: HP relies on international cards in LATAM. No local instant rail (PIX) or cash voucher (Boleto, OXXO) at checkout

REGION: EMEA (UK, Germany, France, Spain, Italy, Switzerland, Nordics)
  Accepted: Credit/Debit cards, PayPal, PayPal Credit, PayPal Pay in 3, Klarna Pay in 3, SEPA Direct Debit (Instant Ink)
  Missing: BLIK (Poland), iDEAL (Netherlands), Bancontact (Belgium), MB Way (Portugal), Trustly (Nordics), Open Banking (UK), Twint (Switzerland)
  Note: Eastern Europe and Nordics severely under-covered for both hardware checkout and Instant Ink

REGION: Asia (Japan, South Korea, India, SE Asia, China)
  Accepted: Credit/Debit cards, PayPal (limited markets)
  Missing: PayPay (Japan, 70M+ users), Konbini cash (Japan, 10% of online purchases), LINE Pay, Rakuten Pay, KakaoPay, NaverPay, Toss, UPI (India, 350M+ users), GrabPay, DANA, GCash, Alipay/WeChat Pay (China)
  Note: Japan and South Korea among HP's top APAC markets but no local wallets supported. India UPI completely absent

**Payment Issues and Incidents:**
- "Instant Ink Account Needs Attention": Recurring HP Support Community thread. Subscribers see warning and lose printing capacity until card is updated. No automatic retry to alternative method
- "Update credit card doesn't work": Multiple users report repeated failures updating expired cards on hpinstantink.com. Customer support manual intervention required
- "Order Declined Using Credit Card And Paypal": HP forum thread documenting both rails failing simultaneously, leaving customer with no third option to complete purchase
- "All Payment Methods Fail": Solved thread where every saved method is rejected. HP advises desktop browser, no VPN, disable autofill. No automatic cascade or fallback
- "Card was charged but site says declined": Forum complaints of double states where card is debited but order marked failed. Manual refund cycle required
- Cannot update payment method: Recurring issue across years. Reflects rigid, single-stack billing vs orchestrated retry logic
- No BNPL on Instant Ink: Subscription billing has no installment option globally. Klarna and Zip live only on hardware checkout in select markets

**Key meeting angles:**
1. **$1B Instant Ink ARR at risk from involuntary churn** | HP just crossed 1M Instant Ink subscribers and consumer subscriptions are nearing $1B annual revenue. HP Support forums are filled with renewal failures and "Account Needs Attention" alerts. NOVA AI could recover up to 75% of soft declines before the subscriber notices.
2. **LATAM and Asia revenue ceiling without local APMs** | HP sells Personal Systems and Print across Brazil, Mexico, Japan, Korea, and India. Yet PIX, OXXO, SPEI, PayPay, KakaoPay, and UPI are absent at checkout. Yuno activates 1,000+ local methods via one API.
3. **AI PC pivot needs a payment stack that scales** | AI PCs already represent 35%+ of HP's quarterly shipments. New consumer demand from emerging markets accelerates with AI PC adoption, but the underlying payment stack has not evolved. Local APM coverage becomes the growth bottleneck.
4. **HP Print sells subscriptions, but its checkout is not subscription-grade** | Adobe, Spotify, and Netflix all moved to orchestration to protect subscription ARR. HP Instant Ink runs on a single stack with no smart routing or failover. Livelo recovered 50% of failed transactions using cascading retries.
5. **FY2026 guidance assumes margin discipline; auth uplift is pure margin** | HP guided FY26 EPS $2.90 to $3.20 with elevated memory costs. A 3 to 10% auth rate improvement on $55B+ revenue is high-margin, low-CAC growth that lands directly in operating margin.

**HP Leadership:**
- Enrique Lores: President and CEO. Leads HP Inc strategy
- Karen Parkhill: EVP and CFO. Oversees financial operations
- Tuan Tran: President, Imaging, Printing & Solutions. Owns Instant Ink and subscription strategy
- Alex Cho: President, Personal Systems. Owns PC and AI PC business
- Anneliese Olson: SVP, Print Category and Online
- No dedicated VP of Payments or Billing identified in public sources

**Recent corporate developments:**
- February 2026: Q1 FY2026 results. Revenue $14.4B (up 6.9%). AI PC mix above 35%
- November 2025: Q4 FY2025 results. Full year revenue $55.3B (up 3.2%)
- January 2026: HP Unveils Intelligent Retail Solutions for unified commerce
- 2025 to 2026: Instant Ink subscribers crossed 1M, all-in plan subscribers up double-digit sequentially
- 2025: Smart Tank printers integrated into HP All-in subscription plans

**Sources:**
- [HP Q1 FY2026 Press Release (HP)](https://www.hp.com/us-en/newsroom/press-releases/2026/hp-inc-reports-fiscal-2026-first-quarter-results.html)
- [HP Q1 FY2026 Earnings PDF (HP)](https://www.hp.com/content/dam/sites/garage-press/press/press-releases/2026/q1-fy26-earnings/HP_Q1_2026_Earnings_Press_Release.pdf)
- [HP FY2025 Results (HP)](https://www.hp.com/us-en/newsroom/press-releases/2025/hp-inc-reports-fiscal-2025-full-year-and-fourth-quarter-results.html)
- [HP Q1 FY2026 Analysis (Futurum)](https://futurumgroup.com/insights/hp-q1-fy-2026-earnings-ai-pc-momentum-memory-costs-temper-outlook/)
- [HP Q4 FY2025 Analysis (Futurum)](https://futurumgroup.com/insights/hp-q4-fy-2025-earnings-rise-on-pc-strength-fy-2026-eps-soft/)
- [HP Q1 2026 Strong Revenue (Insider Monkey)](https://www.insidermonkey.com/blog/hp-inc-hpq-strong-q1-2026-revenue-growth-driven-by-personal-systems-and-ai-pc-adoption-1705040/)
- [HP Statistics 2026 (RequirementsPC)](https://requirementspc.com/hp-statistics/)
- [HP Revenue MacroTrends (MacroTrends)](https://www.macrotrends.net/stocks/charts/HPQ/hp/revenue)
- [HP Instant Ink FAQ (HP)](https://www.hp.com/us-en/printers/instant-ink/faq.html)
- [HP Instant Ink Billing (HP Support)](https://support.hp.com/us-en/document/ish_3259778-1993151-16)
- [HP Instant Ink Billing UK (HP Support)](https://support.hp.com/gb-en/document/ish_3259778-1993151-16)
- [HP Instant Ink Plan Management (HP Support)](https://support.hp.com/us-en/document/ish_7087662-7087709-16)
- [HP Store US Customer Service FAQ (HP)](https://www.hp.com/us-en/shop/cv/customerservicefaq)
- [HP Financing & Consumer Payment Solutions (HP)](https://www.hp.com/us-en/shop/cv/hpfinancing)
- [HP Payment and Financing Options US (HP)](https://www.hp.com/us-en/shop/cv/financing)
- [HP UK Payment Methods (HP)](https://www.hp.com/gb-en/shop/faq.aspx?p=payment-methods)
- [HP Switzerland Payment Methods (HP)](https://www.hp.com/ch-en/shop/faq.aspx?p=payment-methods)
- [HP Setting Up Small Business Payment Options (HP)](https://www.hp.com/us-en/shop/tech-takes/setting-up-small-business-payment-options)
- [Zip BNPL HP Hewlett-Packard (Zip)](https://zip.co/us/store/hp)
- [HP Instant Ink Account Needs Attention (HP Community)](https://h30434.www3.hp.com/t5/Printers-Knowledge-Base/Instant-Ink-Account-needs-attention-or-Update-payment-method/ta-p/7037765)
- [HP Update Credit Card Doesn't Work (HP Community)](https://h30434.www3.hp.com/t5/HP-Instant-Ink/Update-credit-card-doesn-t-work/td-p/8618824)
- [HP Order Declined Card and PayPal (HP Community)](https://h30434.www3.hp.com/t5/Notebook-Software-and-How-To-Questions/Order-Declined-Using-Credit-Card-And-Paypal/td-p/8612405)
- [HP All Payment Methods Fail (HP Community)](https://h30434.www3.hp.com/t5/HP-Instant-Ink/All-Payment-Methods-Fail/td-p/9530937)
- [HP Card Charged but Declined (HP Community)](https://h30434.www3.hp.com/t5/Gaming-Accessories/My-card-was-charged-and-the-site-say-s-it-was-declined/td-p/7927953)
- [HP Cannot Update Payment Method (HP Community)](https://h30434.www3.hp.com/t5/Printer-Setup-Software-Drivers/Cannot-update-payment-method/td-p/7913610)
- [HP Logo (CompaniesLogo)](https://companieslogo.com/HPQ/)
