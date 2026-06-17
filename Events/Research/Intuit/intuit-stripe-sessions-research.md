# INTUIT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Intuit
=======================================

Logo: https://companieslogo.com/img/orig/INTU-bfc3f4e4.png
Nombre merchant: Intuit

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US Only Payment Rails
Tittle_Pain Point_2: QB Payments Risk Declines
Tittle_Pain Point_3: No Global Orchestration
Tittle_Pain Point_4: International QB Gaps
Tittle_Pain Point_5: FedNow vs Global Reality

Desc_Pain Point_1: TurboTax only processes cards with US billing addresses. QuickBooks Payments is unavailable in international QuickBooks Online versions. Mailchimp and Credit Karma monetization runs through US centric payment rails. At $18.8B revenue, non US customers are locked out of seamless billing.
Desc_Pain Point_2: QuickBooks community forums document persistent payment declines: ACH payments failing after 10+ years of success, cards declined with "Risk Check" voids by Intuit, and Intuit reserving "the right to decline a credit card transaction with no explanation." SMB customers losing trust in payment reliability.
Desc_Pain Point_3: No payment orchestration platform confirmed across Intuit's product suite. QuickBooks Payments, TurboTax billing, Mailchimp subscriptions, and Credit Karma all appear to run through separate internal stacks. No unified routing or failover between products.
Desc_Pain Point_4: QuickBooks serves users in US (86.5%), Canada (5.5%), UK (3.8%), and Australia as core markets. The "Rest of World" QuickBooks platform has limited payment capabilities. No PIX for Brazil, no iDEAL for Netherlands, no UPI for India. Global SMBs must use third party payment apps.
Desc_Pain Point_5: Intuit completed FedNow certification in April 2026 for instant US payments. But international markets still lack real time payment rails integration. Focusing on US instant payments while global expansion leads with Mailchimp creates a payment infrastructure gap as international revenue grows.

SLIDE 1: PSP TOPOLOGY

PSP_1: Internal (Intuit Payments) PSP_2: Credit/Debit Cards PSP_3: ACH PSP_4: PayPal/Venmo

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: iDEAL (Netherlands)
Local_M_3: BLIK (Poland)
Local_M_4: UPI (India)
Local_M_5: SEPA Instant (Europe)
Local_M_6: Interac (Canada)
Local_M_7: PayPay (Japan)
Local_M_8: Open Banking (UK)
Local_M_9: Boleto (Brazil)
Local_M_10: KakaoPay (South Korea)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each subscription billing and QuickBooks Payments transaction to the optimal acquirer per card BIN, issuer, and geography. With $18.8B in revenue and $8.3B in online ecosystem revenue (up 20%), even a 0.5% auth improvement recovers tens of millions in retained subscriptions. Smart Routing boosts approval 3 to 10%.
Desc_Yuno_Cap2: When a card or ACH payment is declined on QuickBooks, TurboTax, or Mailchimp, Yuno cascades instantly to an alternative processor or method. NOVA AI recovers up to 75% of soft declines, replacing opaque "Risk Check" rejections with intelligent retry. Livelo recovered 50% of failed transactions.
Desc_Yuno_Cap3: Activate PIX in Brazil, iDEAL in Netherlands, UPI in India, SEPA Instant across Europe, and local wallets in emerging markets. One API integration enables QuickBooks international versions to accept local payments natively. InDrive launched 10 LATAM markets in under 8 months with Yuno.
Desc_Yuno_Cap4: Replace siloed payment stacks across QuickBooks Payments, TurboTax billing, Mailchimp subscriptions, and Credit Karma with one real time dashboard. Centralized approval rate monitoring across all four product lines. Millisecond anomaly detection catches payment failures before they cascade during tax season surges or subscription renewal cycles.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Intuit at a glance:**
- NASDAQ: INTU. Global financial technology platform for consumers and small businesses
- FY2025 Total Revenue: $18.8B (up 16% YoY)
- FY2026 Revenue Guidance: $21.0B to $21.2B (up 12 to 13% YoY)
- FY2026 Q2 Revenue: $4.7B (up 17% YoY). Non GAAP EPS $4.15 (up 25%)
- Global Business Solutions Group FY2025: $11.1B (up 16%), of which Online Ecosystem revenue $8.3B (up 20%)
- Consumer Group FY2025: $4.9B (up 10%). TurboTax Live revenue up 47%
- Credit Karma FY2025 Revenue: $2.3B (up 32%)
- QuickBooks Online Accounting revenue up 22% FY2025
- QBO Advanced and Intuit Enterprise Suite online ecosystem revenue up ~40%
- Core markets: US (86.5% of QuickBooks users), Canada (5.5%), UK (3.8%), Australia
- Products: QuickBooks, TurboTax, Credit Karma, Mailchimp, ProConnect, Intuit Enterprise Suite
- ~100M customers globally across all platforms
- FedNow certification completed April 2026

**Confirmed PSPs and Payment Infrastructure:**
- Internal (Intuit Payments): QuickBooks Payments is Intuit's own payment processing service. Processes credit cards, debit cards, ACH, Apple Pay, PayPal, Venmo. Card invoice rate: 2.99%, in person swipe: 2.5%, ACH: 1% flat
- Credit/Debit Cards: Visa, Mastercard, Amex, Discover accepted across products. In person: also Samsung Pay, Google Pay via card readers
- ACH Bank Payments: Available for QuickBooks invoice payments in US
- PayPal: Accepted for QuickBooks online payments
- Venmo: Accepted for QuickBooks online payments
- Apple Pay: Accepted for QuickBooks online payments and in person
- Google Pay: In person via card readers
- Samsung Pay: In person via card readers
- TurboTax: Credit/debit cards (US billing address only), "Pay with My Refund" ($40 fee), File Now Pay Later loans ($200 to $6,000)
- FedNow: Intuit certified for FedNow instant payments (April 2026)
- QuickBooks Payments is UNAVAILABLE in international QuickBooks Online versions
- No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Product:**

PRODUCT: QuickBooks Online (US)
  Online Invoices: Visa, Mastercard, Amex, Discover, ACH bank transfer, PayPal, Venmo, Apple Pay
  In Person: Visa, Mastercard, Amex, Discover, Apple Pay, Google Pay, Samsung Pay
  Missing: PIX, iDEAL, BLIK, UPI, SEPA, Boleto, any non US local method

PRODUCT: QuickBooks Online (International: UK, Canada, Australia, RoW)
  Accepted: Third party payment integrations only. QuickBooks Payments NOT available
  Missing: Native payment processing. International users must use Stripe, GoCardless, or other third party integrations

PRODUCT: TurboTax
  Accepted: Visa, Mastercard, Amex, Discover (US billing address only). Pay with My Refund. File Now Pay Later loans
  Missing: PayPal, Apple Pay, any non US card, any international payment method

PRODUCT: Mailchimp (Global)
  Accepted: Credit/debit cards (primary)
  Missing: Local payment methods for international subscribers

PRODUCT: Credit Karma
  Accepted: US focused. Monetized primarily through referral fees, not direct payments
  Missing: N/A (primarily US business model)

**Payment Issues and Incidents:**
- ACH payment declines (2024+): Multiple QuickBooks users report ACH payments suddenly declining after years of successful use. Error messages provide no specific reason. Community forum threads document widespread frustration
- "Risk Check" voids: Intuit voids payments "due to Risk Check" with no explanation provided to merchants. QuickBooks community threads show merchants unable to receive payments from verified customers
- Card decline opacity: "Why are payments being declined? Customer has funds, card number was entered correctly." Forum posts document Intuit declining valid payments with no troubleshooting path
- Intuit reserves right to decline: Official policy states Intuit reserves "the right to decline a credit card transaction with no explanation," creating trust issues with SMB merchants
- Fund holds: QuickBooks users report Intuit holding payment funds without clear release timelines. Forum posts: "Quickbooks will not release my funds, my money"
- International payment limitations: QuickBooks Payments service unavailable outside US. International users must rely on third party payment apps, creating fragmented experience

**Key meeting angles:**
1. **$18.8B revenue, 4 products, siloed payment stacks** | QuickBooks, TurboTax, Mailchimp, and Credit Karma each handle payments differently. No unified orchestration. Yuno could provide a single payment layer across all four product lines, improving auth rates and reducing per product integration costs.
2. **QuickBooks Payments unavailable internationally** | The "Rest of World" QuickBooks platform has no native payment processing. As Intuit expands globally (leading with Mailchimp), international SMBs need local payment methods. Yuno activates PIX, iDEAL, UPI, and 1,000+ methods via one API.
3. **ACH and card declines erode SMB trust** | QuickBooks merchants report valid payments declined with no explanation, funds held without timelines, and "Risk Check" voids. These opaque failures push SMBs to competing platforms. NOVA AI could recover up to 75% of soft declines with intelligent retry.
4. **TurboTax locked to US cards** | TurboTax only accepts cards with US billing addresses. As Intuit considers international tax product expansion, payment infrastructure must support non US cards and local methods. Yuno enables global card acceptance from day one.
5. **FedNow is US only, global needs are now** | FedNow certification is forward looking for US instant payments. But QuickBooks serves UK, Canada, Australia, and growing international markets today. These markets need SEPA Instant, Interac, Open Banking, and local APMs now, not just US real time rails.

**Intuit Leadership:**
- Sasan Goodarzi: CEO (since 2019). Former EVP of Small Business Group
- Sandeep Aujla: CFO (since 2023). Previously SVP and Chief Accounting Officer
- Alex Chriss: Former EVP and GM of Small Business and Self Employed Group. Left to become CEO of PayPal (September 2023)
- Nhung Ho: EVP and Chief Product and Technology Officer. Leads AI and product strategy
- Marianna Tessel: EVP and Chief Technology Officer
- David Zaslavsky: SVP and GM of Payments and Capital. Directly oversees QuickBooks Payments, lending, and payment strategy
- No external payment orchestration vendor identified

**Recent corporate developments:**
- April 2026: Intuit completed FedNow Service certification for instant payments
- February 2026: Q2 FY2026 results. Revenue $4.7B (up 17%). Intuit Enterprise Suite contracts up nearly 50% QoQ
- November 2025: Q1 FY2026 results. Strong start, reiterating full year guidance
- August 2025: FY2025 results. Revenue $18.8B (up 16%). Set FY2026 guidance for $21.0B to $21.2B
- FY2025: Online Ecosystem revenue $8.3B (up 20%). TurboTax Live revenue up 47%. Credit Karma $2.3B (up 32%)
- Strategy: "AI driven expert platform" positioning. Intuit Assist AI across all products
- International: Leading global expansion with Mailchimp, then bringing QuickBooks ecosystem
- Core markets focus: US, UK, Canada, Australia with "Rest of World" platform for other markets

**Sources:**
- [Intuit FY2025 Full Year Results (Investor Relations)](https://investors.intuit.com/news-events/press-releases/detail/1266/intuit-reports-strong-fourth-quarter-and-full-year-fiscal-2025-results-sets-fiscal-2026-guidance-with-double-digit-revenue-growth-and-continued-operating-margin-expansion)
- [Intuit Q1 FY2026 Results (Investor Relations)](https://investors.intuit.com/news-events/press-releases/detail/1286/intuit-reports-strong-first-quarter-results-and-reiterates-full-year-guidance)
- [Intuit Q2 FY2026 Results (Investor Relations)](https://investors.intuit.com/news-events/press-releases/detail/1307/intuit-reports-strong-second-quarter-results-and-reiterates-full-year-guidance)
- [Intuit FedNow Certification (BusinessWire)](https://www.businesswire.com/news/home/20260409118272/en/Intuit-Completes-FedNow-Service-Certification-to-Accelerate-Instant-Payments-for-Small-and-Mid-Market-Businesses)
- [QuickBooks Payments (Intuit)](https://quickbooks.intuit.com/payments/)
- [QuickBooks Payments Overview (Intuit)](https://quickbooks.intuit.com/payments/overview/)
- [QuickBooks Payments Rates (Intuit)](https://quickbooks.intuit.com/payments/payment-rates/)
- [QuickBooks Payment Methods (Method)](https://www.method.me/blog/how-does-quickbooks-payments-work/)
- [TurboTax Payment Methods (Intuit Support)](https://ttlc.intuit.com/turbotax-support/en-us/help-article/intuit-account-billing/forms-payment-turbotax-online-accept/L7MiM0ehb_US_en_US)
- [TurboTax File Now Pay Later (Intuit)](https://turbotax.intuit.com/file-now-pay-later/)
- [QuickBooks Payment Rejected Forum](https://quickbooks.intuit.com/learn-support/en-us/payments/payment-rejected-i-don-t-know-why/00/1487714)
- [QuickBooks Payment Declined Forum](https://quickbooks.intuit.com/learn-support/en-us/payments/payment-declined/00/1128405)
- [QuickBooks ACH Decline Forum](https://quickbooks.intuit.com/learn-support/en-us/reports-and-accounting/my-customers-are-unable-to-pay-their-invoices-with-ach-link-on/00/1369934)
- [QuickBooks Risk Check Void Forum](https://quickbooks.intuit.com/learn-support/en-us/reports-and-accounting/why-vendors-payment-declined-by-qb/00/1489814)
- [QuickBooks Fund Hold Forum](https://quickbooks.intuit.com/learn-support/en-us/payments/quickbooks-will-not-release-my-funds-my-money/00/1490096)
- [QuickBooks Declining Cards Forum](https://quickbooks.intuit.com/learn-support/en-us/payments/quickbooks-online-declining-credit-card-payments/00/1436667)
- [QuickBooks Market Share 2026 (AceCloud)](https://www.acecloudhosting.com/blog/quickbooks-market-share/)
- [Intuit Global Expansion Mailchimp QuickBooks (Intuit Blog)](https://www.intuit.com/blog/news-social/an-update-on-fueling-small-businesses-globally-with-mailchimp-and-quickbooks/)
- [Intuit Wikipedia](https://en.wikipedia.org/wiki/Intuit)
- [Intuit AI QuickBooks Updates (Fintech News)](https://fintechnews.am/fintech-usa/54428/intuit-ai-quickbooks-global-updates/)
- [Intuit Logo (CompaniesLogo)](https://companieslogo.com/intuit/logo/)
