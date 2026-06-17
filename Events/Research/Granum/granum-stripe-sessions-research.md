# GRANUM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Granum
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idpWE6h5hU/idL9PqZGvK.svg
Nombre merchant: Granum

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only Card Processing
Tittle_Pain Point_2: ACH Transaction Limits
Tittle_Pain Point_3: Slow Payment Reconciliation
Tittle_Pain Point_4: No Failover on Invoices
Tittle_Pain Point_5: Canada Cross-Border Drag

Desc_Pain Point_1: LMN Pay is built exclusively on Stripe Connect. Every credit card, debit card, and digital payment from thousands of landscaping and arborist businesses routes through Stripe as the sole acquirer. Any Stripe rate dip or outage blocks all contractor invoicing.
Desc_Pain Point_2: SingleOps users report ACH transaction limits that cost them recurring customers. High-value landscaping contracts ($10K to $50K+) get blocked when the single payment rail caps transaction amounts, forcing contractors to split invoices or lose deals.
Desc_Pain Point_3: LMN and SingleOps each have separate QuickBooks integrations that frequently break. Users report 6+ months of unresolved sync issues between payment processing and accounting, creating manual reconciliation work that defeats the platform's purpose.
Desc_Pain Point_4: When a landscaper's client invoice payment declines on Stripe, there is no automated cascade to a second processor. The contractor must manually follow up, resend the invoice link, and wait for the client to retry, delaying cash flow by days or weeks.
Desc_Pain Point_5: Granum serves thousands of businesses across the US and Canada. Canadian landscapers paying US-based vendors or receiving cross-border payments absorb FX markups on every transaction with no local acquiring option in Canada.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Connect (LMN Pay)
PSP_2: ACH (bank transfers)
PSP_3: SingleOps Payments
PSP_4: QuickBooks (accounting sync)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Interac (Canada)
Local_M_2: PayPal
Local_M_3: Venmo
Local_M_4: Cash App Pay
Local_M_5: Zelle
Local_M_6: Apple Pay
Local_M_7: Google Pay
Local_M_8: Affirm
Local_M_9: RTP (Real-Time Payments)
Local_M_10: FedNow

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every landscaping invoice payment to the best performing acquirer by card BIN, bank, and contractor location. With thousands of businesses processing through LMN Pay, a 3% auth uplift recovers significant revenue per season across the platform without touching the checkout experience.
Desc_Yuno_Cap2: When a client's card declines on an LMN Pay invoice, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed invoice payments automatically, eliminating the manual follow-up cycle that delays contractor cash flow by days or weeks.
Desc_Yuno_Cap3: Unlocks the payment methods Granum's North American contractor base needs: Interac for Canadian landscapers, PayPal and Venmo for residential clients, Apple Pay and Google Pay for mobile-first checkout, Affirm for large project financing. One API, 1,000+ payment methods, zero engineering sprints per method.
Desc_Yuno_Cap4: Single dashboard consolidating LMN Pay (Stripe Connect), SingleOps Payments, ACH transfers, and QuickBooks accounting data into one view. Real-time auth rate monitoring across all payment rails, centralized reconciliation replacing broken QuickBooks sync, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Granum at a glance:**
- Founded: 2025 (launched October 2025 as parent brand; component companies serving since 2008)
- Component companies: LMN (landscape management), SingleOps (arborist/tree care), Greenius (crew training)
- CEO: Mark Sedgley (20+ years SaaS executive, 9 acquisitions completed)
- Headquarters: 6595 Roswell Rd, Suite G3170, Atlanta, GA 30328
- LMN headquarters: Markham, Ontario, Canada (original LMN)
- Employees: ~240 total
- Funding: $8.6M raised
- Key investors: FTV Capital, Five Elms Capital
- Market: North America (US and Canada)
- Customers: thousands of landscaping and arborist organizations
- Products: LMN (estimating, scheduling, invoicing, LMN Pay), SingleOps (proposals, scheduling, invoicing, payments), Greenius (employee training, safety compliance)
- LMN Pay: powered by Stripe Connect, launched 2026, credit card and ACH/bank transfer acceptance
- Industries served: full-service landscaping, landscape design/build, landscape maintenance, tree care/arborist, snow and ice management
- Recognition: merger of three market-leading platforms into unified green industry software

**Confirmed PSPs:**
- Stripe Connect: exclusive payment processor for LMN Pay (confirmed via press release and product page)
- ACH / Direct Bank Transfer: supported for invoice payments
- SingleOps Payments: separate payment processing for arborist platform (details limited)
- QuickBooks: accounting integration (not a PSP but key financial sync)
- No payment orchestrator detected
- No digital wallets detected (no Apple Pay, Google Pay)
- No Canadian local payment methods (no Interac)

**Payment issues documented:**
- ACH transaction limits: SingleOps limits high ACH transactions, causing lost recurring customers
- Forced annual contracts: SingleOps requires year-long commitment with no exit clause
- QuickBooks sync failures: users report 6+ months of unresolved sync issues between SingleOps and QuickBooks
- Desktop/mobile sync: scheduling not syncing between platforms, 3-week response time for generic support
- Hidden fees: LMN charged $97 extra without acknowledgement for Greenius addon
- Cancellation fees: LMN charges 30-day cancellation usage fee
- Clunky interface: reviewers note rigidity and lack of flexibility for non-standard projects
- Slow payment processing: SingleOps users report slow payment processing and confusing invoice listings

**Key meeting angles:**
1. **LMN Pay is Stripe-only**: Just launched on Stripe Connect; perfect timing to layer orchestration before scale locks them into single-acquirer dependency
2. **Seasonal cash flow criticality**: Landscaping is seasonal (spring/summer peaks); failed invoice payments during peak season have outsized revenue impact
3. **Canadian gap**: LMN originated in Canada (Markham, ON); thousands of Canadian landscapers need Interac and CAD-optimized acquiring
4. **Two disconnected payment systems**: LMN Pay and SingleOps Payments run independently; orchestration unifies them under one dashboard
5. **Large contract values**: Landscaping/arborist contracts range $10K to $100K+; ACH limits and card decline rates have material dollar impact per failure
6. **QuickBooks reconciliation fix**: NOVA provides real-time reconciliation that replaces the broken QuickBooks sync plaguing both LMN and SingleOps users

**Sources:**
- [Granum Official Website](https://granum.com/)
- [Granum Launch Press Release (PRNewswire)](https://www.prnewswire.com/news-releases/lmn-singleops-and-greenius-unite-as-granum-the-leading-software-partner-for-landscapers--arborists-302577883.html)
- [Granum Launches LMN Pay Powered by Stripe (PRNewswire)](https://www.prnewswire.com/news-releases/granum-launches-new-lmn-pay-experience-powered-by-stripe-302717695.html)
- [LMN Pay Powered by Stripe](https://granum.com/lmn/lmn-pay-powered-by-stripe/)
- [LMN Pay Product Page](https://granum.com/lmn/lmn-pay/)
- [Granum About / Company](https://granum.com/about/company/)
- [Granum on Five Elms Capital](https://www.fiveelms.com/company/granum/)
- [Granum on FTV Capital](https://ftvcapital.com/portfolio-item/granum/)
- [Granum PitchBook Profile](https://pitchbook.com/profiles/company/172773-91)
- [LMN Reviews (Capterra)](https://www.capterra.com/p/142064/LMN/reviews/)
- [SingleOps Reviews (Capterra)](https://www.capterra.com/p/176935/SingleOps/reviews/)
- [LMN Reviews (G2)](https://www.g2.com/products/lmn/reviews)
- [Granum ZoomInfo](https://www.zoominfo.com/c/granum-llc/5000599205)
- [LMN by Granum Launches Stripe Platform (Landscape Management)](https://www.landscapemanagement.net/lmn-by-granum-launches-new-financial-infrastructure-platform-in-partnership-with-stripe/)
- [Granum Launch (Yahoo Finance)](https://finance.yahoo.com/news/lmn-singleops-greenius-unite-granum-100000492.html)
