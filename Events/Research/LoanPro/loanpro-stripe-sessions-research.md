# LOANPRO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: LoanPro
=======================================

Logo: https://brandfetch.com/loanprosoftware.com
Nombre merchant: LoanPro

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US Only Payments
Tittle_Pain Point_2: Multi Processor Complexity
Tittle_Pain Point_3: No Smart Payment Routing
Tittle_Pain Point_4: Card Decline Recovery Gap
Tittle_Pain Point_5: Limited Borrower APMs

Desc_Pain Point_1: LoanPro's Secure Payments is integrated with Authorize.net, LoanPaymentPro, TabaPay, Repay, ACHQ, Actum, VersaPay, and EFT Canada for US and Canadian markets only. No coverage for LATAM, EU, or APAC. As lenders using LoanPro expand internationally with Mastercard Loan on Card, they need payment rails beyond North America.
Desc_Pain Point_2: LoanPro supports multiple payment processors per lender, but each requires separate configuration in Secure Payments. 600+ lenders manage $22B+ annually through this fragmented setup. No unified orchestration layer routes transactions to the optimal processor per borrower profile, card BIN, or geography.
Desc_Pain Point_3: LoanPro lets lenders connect multiple processors but does not intelligently route payments between them. Each processor handles its assigned loan portfolio in a silo. No dynamic routing based on approval rates, cost optimization, or real time processor health. Lenders leave authorization improvements on the table.
Desc_Pain Point_4: When a loan payment is declined on one processor (Authorize.net, TabaPay, Repay), there is no automatic cascade to try the same transaction on an alternative processor. The decline is recorded, and the borrower must retry. With 25M+ loans under management, each failed payment affects portfolio performance and collections.
Desc_Pain Point_5: Borrower payments are limited to bank cards and ACH/EFT. No digital wallets (Apple Pay, Google Pay), no PIX, no SEPA, no UPI, no BLIK. As embedded lending expands into ecommerce and vertical SaaS platforms, borrowers expect to repay loans through the same methods they use for everyday purchases.

SLIDE 1: PSP TOPOLOGY

PSP_1: Authorize.net (Cards) PSP_2: TabaPay (Cards/ACH/RTP) PSP_3: Repay (Cards/ACH) PSP_4: ACHQ/Actum (ACH) PSP_5: VersaPay/EFT Canada

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: UPI (India)
Local_M_4: Apple Pay (Global)
Local_M_5: Google Pay (Global)
Local_M_6: iDEAL (Netherlands)
Local_M_7: BLIK (Poland)
Local_M_8: Open Banking UK
Local_M_9: Boleto (Brazil)
Local_M_10: PayPay (Japan)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each loan repayment to the optimal processor per borrower card BIN, issuer, amount, and geography. With 600+ lenders managing $22B+ annually across Authorize.net, TabaPay, and Repay, even a 1% auth improvement across the portfolio recovers millions in collected payments. Smart Routing boosts approval 3 to 10%.
Desc_Yuno_Cap2: When TabaPay declines a loan payment, Yuno cascades instantly to Repay or Authorize.net before recording a missed payment. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this approach. Each recovered payment improves portfolio delinquency rates and lender revenue.
Desc_Yuno_Cap3: Extend LoanPro beyond cards and ACH with PIX in Brazil, SEPA in EU, UPI in India, and digital wallets globally. One API integration, no per market engineering. As Mastercard Loan on Card launches in 2026 across 200+ countries, borrowers need local repayment methods. InDrive launched 10 LATAM markets in under 8 months with Yuno.
Desc_Yuno_Cap4: Replace siloed processor dashboards with one real time view across Authorize.net, TabaPay, Repay, ACHQ, and future international processors. Monitor approval rates, decline reasons, and recovery metrics per lender, loan type, and geography. Millisecond anomaly detection catches processor issues before they cascade into delinquencies.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**LoanPro at a glance:**
- Founded: 2006 by Rhett Roberts, Ben Roberts, and Lloyd Roberts (started as auto dealership/lending)
- HQ: Farmington, Utah, United States
- Revenue: $24.3M (2025). 221 employees
- Funding: $100M Series A (July 2021, led by FTV Capital)
- Scale: 600+ lender clients managing 25M+ loans and $22B+ annually
- Products: Loan Management System (LMS), Secure Payments, Card Issuing, Origination, Servicing, Collections, Compliance
- Certifications: SOC 2 and PCI-DSS Level 1
- Use Cases: Consumer lending, auto lending, business lending, embedded lending, credit cards, crypto backed lending
- Key Partnerships: Mastercard (Loan on Card, Dec 2025), Thread Bank (embedded finance), TrueNorth (strategic investment)
- Mastercard Loan on Card: Launching 2026. Fixed term installment loans delivered via Mastercard card. Accepted anywhere Mastercard is accepted (200+ countries)

**Confirmed PSPs and Payment Infrastructure:**
- Secure Payments: LoanPro's proprietary payment product. PCI-DSS Level 1 compliant. Separate from LMS to maintain PCI scope isolation
- Authorize.net: Credit and debit card processing (US only)
- LoanPaymentPro: Card processing integration
- TabaPay: Cards, ACH, RTP, FedNow. Competitive advantage in processing credit through debit channels. Plaid integration for bank verification
- Repay: Cards and ACH processing
- ACHQ: ACH/eCheck processing
- Actum: ACH/eCheck processing
- VersaPay: EFT processing
- EFT Canada: Canadian EFT processing
- NACHA file generation: Batch ACH processing
- CPA-005: Canadian batch processing
- Multiple processor support: Lenders can configure multiple processors per loan portfolio
- Payment Profile Portability: Borrower payment profiles transferable between processors
- AutoPay: Automated recurring payments for agents, customers, and automations

**Payment Infrastructure Details:**
- US and Canada only. No international payment processing confirmed
- Payment methods: Bank cards (credit/debit), ACH, EFT (Canada)
- No digital wallets, no BNPL, no local international methods
- Payment Application Waterfall: Controls how payments are distributed across loan components (principal, interest, fees)
- Payment Match Calculator: Helps borrowers understand payment amounts
- Payment Return Actions: Automated handling of returned/failed payments

**Key meeting angles:**
1. **$22B+ managed with no smart routing** | 600+ lenders process $22B+ annually through LoanPro's Secure Payments with multiple processors (Authorize.net, TabaPay, Repay) configured in silos. No dynamic routing between them. Yuno's Smart Routing directs each payment to the optimal processor, boosting approval 3 to 10% and recovering millions in loan collections.
2. **Mastercard Loan on Card needs global payment rails** | LoanPro and Mastercard launch Loan on Card in 2026, delivering installment loans via Mastercard to 200+ countries. But LoanPro's payment infrastructure is US and Canada only. Yuno provides 1,000+ payment methods across 50+ countries, enabling borrowers worldwide to repay through local rails.
3. **Failed payments drive delinquency** | When a card or ACH payment fails on one processor, LoanPro records the miss with no cascade to an alternative. With 25M+ loans, each failed repayment increases delinquency and reduces lender revenue. NOVA AI recovers up to 75% of soft declines instantly by routing to the next available processor.
4. **Embedded lending demands embedded payments** | LoanPro powers lending for vertical SaaS (construction, restaurants, ecommerce) and fintech platforms. These embedded experiences require embedded payment flexibility: wallets, BNPL, local methods. Yuno adds 1,000+ APMs alongside LoanPro's existing card and ACH rails through one API.
5. **600+ lenders, one orchestration opportunity** | Every LoanPro lender manages processors independently. Yuno provides unified orchestration across all processors with one dashboard for approval rates, decline analysis, and cost optimization. The value multiplies across 600+ lenders and $22B+ in annual volume.

**LoanPro Leadership:**
- Rhett Roberts: Founder and CEO
- Ben Roberts: Co-Founder and Chief Customer Relations Officer
- Lloyd Roberts: Co-Founder and Chief Revenue Officer
- Cesar Olea: Chief Technology Officer
- Andy Morrise: Chief Operating Officer
- Colin Terry: Chief Product Officer
- Colton Pond: Chief Marketing Officer (joined 2023, fintech veteran)
- Jeri Larsen: Chief Customer Officer
- Jer Wood: President of Credit Sponsorship (joined Feb 2024, former bank president)

**Recent corporate developments:**
- December 2025: Mastercard and LoanPro partnership for Loan on Card. Launching 2026. Fixed term installment loans via Mastercard card, accepted anywhere Mastercard is accepted
- August 2023: Strategic minority equity investment in TrueNorth (global financial technology services)
- July 2021: $100M Series A from FTV Capital
- 2025: Revenue at $24.3M with 221 employees
- 2025: Thread Bank partnership for embedded lending
- Platform: 600+ lenders, 25M+ loans, $22B+ managed annually
- Compliance: SOC 2 and PCI-DSS Level 1 certified

**Sources:**
- [LoanPro Revenue $24.3M (GetLatka)](https://getlatka.com/companies/loanpro.io)
- [LoanPro Website (LoanPro)](https://www.loanpro.io/)
- [LoanPro Payments (LoanPro)](https://www.loanpro.io/payments/)
- [LoanPro Payment Processing Overview (Help)](https://help.loanpro.io/en_US/payment-processing/payment-processing-overview)
- [LoanPro Secure Payments (Help)](https://help.loanpro.io/secure-payments/secure-payments-overview)
- [LoanPro Card Processors (Help)](https://help.loanpro.io/article/ndoaz9d0pt-processors-debit-credit-card)
- [LoanPro TabaPay Integration (Help)](https://help.loanpro.io/individual-processors/tabapay)
- [LoanPro Multiple Processors (Help)](https://help.loanpro.io/article/r4nq05oqnb-using-multiple-payment-processors)
- [Mastercard LoanPro Partnership (Mastercard)](https://www.mastercard.com/us/en/news-and-trends/press/2025/december/mastercard-and-loanpro-announce-partnership-to-modernize-lending.html)
- [Mastercard LoanPro Partnership (BusinessWire)](https://www.businesswire.com/news/home/20251216985410/en/Mastercard-and-LoanPro-Announce-Partnership-to-Modernize-Lending)
- [LoanPro Loan on Card Blog (LoanPro)](https://www.loanpro.io/blog/loan-on-card-a-new-way-to-deliver-credit/)
- [LoanPro Funding (Crunchbase)](https://www.crunchbase.com/organization/loanpro-software)
- [LoanPro Company Profile (Tracxn)](https://tracxn.com/d/companies/loanpro/__9iOrWHFaivxHVO6pHJSPpUrW-ZZ8iT-edieAq2HTKgk)
- [LoanPro CMO Announcement (PRNewswire)](https://www.prnewswire.com/news-releases/loanpro-welcomes-fintech-industry-veteran-as-chief-marketing-officer-to-continue-to-accelerate-growth-301906485.html)
- [LoanPro TrueNorth Investment (LoanPro)](https://www.loanpro.io/blog/loanpro-announces-strategic-minority-equity-investment-in-truenorth/)
- [Thread Bank LoanPro Partnership (ThePaypers)](https://thepaypers.com/fintech/news/thread-bank-partners-with-loanpro-for-embedded-lending)
- [LoanPro Brand Guidelines (PDF)](https://www.loanpro.io/wp-content/uploads/2020/10/LoanPro_Branding_Guidelines.pdf)
