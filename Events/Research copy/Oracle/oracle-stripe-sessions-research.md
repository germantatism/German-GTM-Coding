# ORACLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Oracle
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg
Nombre merchant: Oracle

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Product PSP Sprawl
Tittle_Pain Point_2: NetSuite Gateway Chaos
Tittle_Pain Point_3: Global Billing Limits
Tittle_Pain Point_4: Hospitality Payment Silos
Tittle_Pain Point_5: $100K Card Ceiling

Desc_Pain Point_1: Oracle Cloud, NetSuite, Hospitality, and Banking each use different PSPs and payment rails. No unified orchestration layer connects Adyen, JPMorgan, Stripe, and internal billing systems.
Desc_Pain Point_2: NetSuite supports 25+ payment gateways (Stripe, Adyen, Worldpay, Braintree, etc.) but each subsidiary configures its own profile. Multi-subsidiary companies manage fragmented PSP configs.
Desc_Pain Point_3: Oracle Cloud billing accepts credit card, debit card, PayPal, and eCheck. Cannot process transactions of $100K+ via card. Local APMs vary by country with no unified coverage map.
Desc_Pain Point_4: Oracle Payments (powered by Adyen) serves 2,550+ organizations across 16,200+ venues in hospitality, restaurants, and sports. US/UK focused with limited LATAM/APAC local method coverage.
Desc_Pain Point_5: Oracle corporate billing rejects virtual cards, prepaid cards, and any card transaction exceeding $99,999.99. Enterprise clients with large invoices must use wire transfers exclusively.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (Oracle Payments)
PSP_2: JPMorgan Chase
PSP_3: Stripe (NetSuite)
PSP_4: Multiple (NetSuite 25+)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: SPEI
Local_M_5: M-Pesa
Local_M_6: GCash
Local_M_7: BLIK
Local_M_8: PSE
Local_M_9: PromptPay
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen, JPMorgan, Stripe, and 25+ NetSuite gateways. With $57.4B annual revenue and cloud growing 27% YoY, routing each SaaS renewal and POS transaction to the best acquirer per market delivers measurable cost savings at massive scale.
Desc_Yuno_Cap2: Automatic cascade across Oracle's fragmented PSP stack. When Adyen declines a hospitality charge or Stripe fails a NetSuite invoice, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery. Critical for 16,200+ venues processing in real time.
Desc_Yuno_Cap3: Extends Oracle's payment reach beyond US/UK: Pix in Brazil, UPI in India, OXXO in Mexico, M-Pesa in Kenya, GCash in Philippines. One API, 1,000+ methods. Oracle Cloud customers in 70+ sovereign regions get local payment options instantly.
Desc_Yuno_Cap4: One dashboard unifying Adyen hospitality payments, JPMorgan ERP integrations, NetSuite multi-gateway configs, and Oracle Cloud billing. Centralized reconciliation, NOVA AI (75% recovery), real-time monitoring across all Oracle business units and 175+ countries.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Oracle at a glance:**
- Founded: 1977, HQ: Austin, TX. Public company (NYSE: ORCL)
- Revenue: $57.4B (FY2025, +8.4% YoY). FY2026 forecast: $67B+ (+17%)
- Cloud revenue: $27B ARR run rate exiting Q4 FY2025
- Cloud Infrastructure (IaaS): $3B/quarter (+52% YoY Q4), accelerating to 70%+ growth FY2026
- Cloud Applications (SaaS): $3.7B/quarter (+12% YoY)
- Strategic SaaS ARR: $9.3B (+20% YoY)
- Remaining Performance Obligations (RPO): $138B
- Capital expenditure: ~$35B planned FY2026 for cloud/AI infrastructure
- Employees: ~160,000+
- Operations: 175+ countries
- Cloud regions: 23 MultiCloud datacenters live, 47 more under construction; 29 Cloud@Customer dedicated datacenters
- More sovereign regions than any major cloud provider
- Key products: Oracle Cloud Infrastructure (OCI), Oracle Cloud Applications (Fusion ERP, HCM, CX), NetSuite (cloud ERP for SMBs), Oracle Hospitality (OPERA, Simphony POS), Oracle Health, Oracle Banking
- CEO: Safra Catz, CTO/Founder: Larry Ellison

**Confirmed PSP/Payment Stack:**
- Adyen: powers Oracle Payments for hospitality, restaurants, sports, entertainment, healthcare (Oct 2025 announcement). 2,550+ orgs, 16,200+ venues
- JPMorgan Chase: expanded partnership for Oracle Fusion Cloud ERP and Simphony POS integrations (AI World 2025)
- NetSuite Payment Gateways (25+ supported): Stripe, Adyen, Worldpay, Braintree, First Data, Global Payments, Heartland, Chase, Elavon, TSYS, Authorize.net, NMI, Shift4, Nuvei, DLocal, Square, Shopify Payments, and more
- Oracle Cloud Billing: credit card, debit card, PayPal, eCheck
- Oracle Banking Payments Cloud Service: ISO 20022 framework, real-time processing
- No unified payment orchestrator across business units

**Confirmed Payment Methods (Oracle Cloud Billing):**
- Credit card (Visa, MC, Amex)
- Debit card
- PayPal
- eCheck
- Virtual cards and prepaid cards: NOT accepted
- Card transactions capped at $99,999.99
- Additional methods available by country (not specified publicly)

**Oracle Payments (Hospitality, via Adyen):**
- Credit/debit cards
- Apple Pay, Samsung Pay, Google Pay
- Contactless payments
- Focus: US and UK

**NetSuite (customer configured):**
- Depends on which of 25+ gateways the customer selects
- Adyen integration supports iDEAL, Klarna, Google Pay, and "many others" per Adyen docs
- Multi-subsidiary companies can configure different gateways per subsidiary

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, largest revenue contributor)
  Currently offer: Visa/MC/Amex, PayPal, eCheck, Apple Pay, Google Pay, Samsung Pay
  Missing: ACH direct (Oracle Cloud billing), RTP/FedNow
  Impact: Enterprise billing over $100K cannot use cards. ACH/RTP would enable large invoice payments.

MARKET 2: United Kingdom (Oracle Payments live)
  Currently offer: Cards, contactless, Apple Pay, Google Pay (via Adyen)
  Missing: Open Banking (PayByBank), Faster Payments
  Impact: Open Banking enables instant, low-cost enterprise invoice payments bypassing card fees.

MARKET 3: India (sovereign cloud region, OCI expanding)
  Currently offer: Credit/debit cards
  Missing: UPI, RuPay, NetBanking, Paytm
  Impact: India UPI handles 80%+ of digital payments. Oracle Cloud subscriptions in India lack the dominant payment method.

MARKET 4: Brazil (sovereign cloud region)
  Currently offer: Credit/debit cards
  Missing: Pix, Boleto
  Impact: Pix processes 40%+ of Brazilian online transactions. Oracle Cloud and NetSuite customers in Brazil need local rails.

MARKET 5: Japan (cloud region)
  Currently offer: Credit/debit cards
  Missing: Konbini, PayPay, Line Pay
  Impact: Konbini (convenience store payments) is critical for Japanese enterprise software billing.

**Key meeting angles:**
1. **$57.4B revenue company with no unified payment orchestration** | Each business unit (Cloud, NetSuite, Hospitality, Banking) operates separate payment stacks
2. **Adyen hospitality partnership is US/UK only** | 2,550+ orgs, 16,200+ venues but limited LATAM/APAC local method coverage
3. **NetSuite 25+ gateway fragmentation** | Multi-subsidiary companies configure separate payment profiles per gateway per subsidiary. Orchestration unifies this instantly.
4. **Oracle Cloud billing $100K ceiling** | Enterprise clients with large cloud bills cannot pay by card. Orchestration can route to bank transfer rails automatically.
5. **70+ sovereign cloud regions** | Oracle operates more sovereign regions than any competitor. Each region needs local payment method coverage.
6. **JPMorgan partnership expanding** | ERP and POS payment integrations growing; adding Yuno orchestration on top amplifies the value
7. **$35B capex FY2026** | Massive infrastructure investment signals growth phase where payment optimization matters

**Sources:**
- [Oracle: Payments (Hospitality)](https://www.oracle.com/industries/payments/)
- [Oracle News: Enterprises Adopt Oracle Payments Powered by Adyen](https://www.oracle.com/news/announcement/enterprises-rapidly-adopt-oracle-payments-powered-by-adyen-to-offer-seamless-customer-experiences-2025-10-23/)
- [JPMorgan: Oracle Partnership Expansion](https://www.jpmorgan.com/payments/newsroom/oracle-partnership-expansion-erp-integrations)
- [Oracle: Billing and Cost Management](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingoverview.htm)
- [Oracle: Available Payment Options](https://supportrenewalshelp.oracle.com/app/answers/detail/a_id/1217)
- [Oracle: My Oracle Billing FAQs](https://www.oracle.com/corporate/invoicing/faqs/)
- [NetSuite: Payment Gateway Docs](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_3803057063.html)
- [NetSuite: Payment Processing Profiles](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1572588.html)
- [Adyen Docs: NetSuite Integration](https://docs.adyen.com/plugins/netsuite)
- [Adyen: NetSuite Payments Bundle](https://www.adyen.com/partners/netsuite)
- [NetSuite: Payment Orchestration Article](https://www.netsuite.com/portal/resource/articles/accounting/payment-orchestration.shtml)
- [Oracle Investor Relations: FY2025 Q4 Results](https://investor.oracle.com/investor-news/news-details/2025/Oracle-Announces-Fiscal-2025-Fourth-Quarter-and-Fiscal-Full-Year-Financial-Results/default.aspx)
- [Oracle Investor Relations: FY2026 Q2 Results](https://investor.oracle.com/investor-news/news-details/2025/Oracle-Announces-Fiscal-Year-2026-Second-Quarter-Financial-Results/default.aspx)
- [Futurum: Oracle Q4 FY2025 Results](https://futurumgroup.com/insights/oracle-delivers-q4-fy-2025-results-with-27-cloud-growth-rpo-hits-138-billion/)
- [Constellation Research: Oracle Cloud Revenue](https://www.constellationr.com/blog-news/insights/oracle-cloud-s-annual-revenue-run-rate-exiting-q4-nears-27-billion)
- [SensePass: NetSuite Payment Gateway Guide](https://sensepass.com/netsuite-payment-gateway-integration-guide/)
- [BrokenRubik: NetSuite Payment Gateways](https://www.brokenrubik.com/blog/netsuite-payment-gateways)
