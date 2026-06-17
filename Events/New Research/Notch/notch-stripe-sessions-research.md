# NOTCH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Notch
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id2FLhKf2C/idgHix8MpR.svg
Nombre merchant: Notch

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-PSP Lock-In
Tittle_Pain Point_2: B2B Payment Friction
Tittle_Pain Point_3: No Cross-Border Rails
Tittle_Pain Point_4: Manual Retry on Declines
Tittle_Pain Point_5: Reconciliation Fragmented

Desc_Pain Point_1: Notch recently partnered with Adyen as its primary payment processor. Running all B2B transactions through a single acquirer means no fallback if Adyen experiences degradation, and no ability to benchmark auth rates against alternative processors.
Desc_Pain Point_2: Food and beverage distributors still rely heavily on cash on delivery (COD) and paper checks. Notch supports credit cards and EFT/ACH, but lacks instant bank transfer options, real-time pay-by-bank, and digital wallet acceptance that could accelerate collections.
Desc_Pain Point_3: Notch serves Canadian and US markets but has no local payment rails for international expansion. No SEPA for European distributors, no Pix for Brazilian suppliers, no SPEI for Mexican operations. Global food supply chains need multi-currency settlement.
Desc_Pain Point_4: Notch automatically retries declined payments, but routing stays on Adyen. Without cascading to an alternate acquirer on failure, the retry hits the same processor and issuer, limiting recovery rates on B2B card payments where ticket sizes are high.
Desc_Pain Point_5: Despite Rutter integrations with QuickBooks, NetSuite, Xero, and Dynamics 365, payment data from Adyen and ERP invoice data live in separate systems. No unified payment-to-invoice matching dashboard exists across all payment types in real time.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (Primary Processor)
PSP_2: Visa (Card Network)
PSP_3: Mastercard (Card Network)
PSP_4: American Express (Card Network)
PSP_5: Rutter (Integration Layer)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Interac e-Transfer (Canada)
Local_M_2: Pay by Bank (Open Banking)
Local_M_3: SEPA Direct Debit
Local_M_4: Pix
Local_M_5: SPEI
Local_M_6: iDEAL
Local_M_7: Bancontact
Local_M_8: BLIK
Local_M_9: PayPal (B2B)
Local_M_10: Boleto Bancario

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every B2B payment to the best-performing acquirer by card BIN, industry vertical, and transaction size. Food and beverage distributors process high-ticket invoices where a 3-10% auth rate uplift on Adyen versus an alternate acquirer directly accelerates cash flow for Notch's customers.
Desc_Yuno_Cap2: When a high-value distributor payment fails on Adyen, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed B2B transactions. For wholesale invoices averaging thousands of dollars, every recovered payment significantly reduces Days Sales Outstanding.
Desc_Yuno_Cap3: Unlock the local payment methods global food supply chains demand: Interac e-Transfer in Canada, SEPA Direct Debit in Europe, Pix in Brazil, SPEI in Mexico. One API, 1,000+ payment methods, zero engineering sprints per market as Notch expands internationally.
Desc_Yuno_Cap4: Consolidate Adyen, ERP integrations, and all future PSPs into one real-time dashboard. NOVA anomaly detection (75% fraud reduction) flags suspicious B2B transactions, while centralized reconciliation auto-matches payments to invoices across QuickBooks, NetSuite, and Xero.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Notch at a glance:**
- Founded: 2015 in Toronto, Canada (originally as ChefHero, pivoted to AR automation)
- CEO: Jordan Huck (Co-Founder)
- CTO: Diego Dominguez Ferrera (Co-Founder)
- HQ: Toronto, Ontario, Canada
- Total Funding: ~$32.6M across 3 rounds ($10M led by Portage in Jan 2023)
- Employees: ~47 (as of Jan 2026)
- Revenue: Estimated $10-50M range
- Key Investors: Portage, Golden Ventures, Math Ventures, Accomplice, Precursor Ventures, Garage Capital, Plexo Capital, Compass Digital Ventures, Gaingels, Agman
- Target Market: Food and beverage industry (manufacturers, distributors, restaurants, suppliers)

**Confirmed PSPs and Partners:**
- Adyen: Primary payment processor (partnership announced Feb 2025)
- Visa, Mastercard, American Express: Accepted card networks
- EFT and ACH: Electronic funds transfer and automated clearing house
- PAD (Pre-Authorized Debit): Supplier-initiated pull payments
- Rutter: Unified API for accounting integrations (QuickBooks Online, QuickBooks Desktop, NetSuite, Xero, Dynamics 365)
- WISK.ai: Strategic partnership for restaurant operations
- Fidelio: Partnership for F&B manufacturers and distributors
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, or Yuno)

**Product Suite:**
- Notch Invoice Manager: End-to-end invoice automation with OCR scanning
- Notch Order Manager: Order-to-payment workflow
- Notch AP Manager: Accounts payable for restaurants
- Notch AR Manager: Accounts receivable for distributors
- Customer Payment Portal: Self-service payment collection
- Payment Processing: Credit cards, EFT, ACH with surcharging capability

**Key Performance Metrics (from website):**
- 3x faster payment collection
- 80% customer payments automated online
- 70% less time spent on admin
- PCI compliant payment storage

**Competitive Landscape:**
- Direct competitors: Bill.com, Melio, Tipalti, Stampli
- Differentiation: Purpose-built for food and beverage industry, not horizontal SaaS
- Weakness: Single-PSP dependency (Adyen only), no cross-border payment rails, limited to North America

**Top Market Gap Analysis:**

MARKET 1: Canada (home market)
  Offer: Credit cards (Visa/MC/Amex), EFT, PAD
  Missing: Interac e-Transfer, Pay by Bank (Open Banking)
  Canadian B2B payments still heavily check-based; Interac e-Transfer is the fastest growing domestic rail

MARKET 2: United States (expansion market)
  Offer: Credit cards, ACH
  Missing: Real-time payments (RTP/FedNow), Zelle Business, Pay by Bank
  ACH is slow for B2B; RTP and FedNow enable instant settlement

MARKET 3: Europe (potential expansion)
  Offer: None currently
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BLIK
  European F&B distribution runs on SEPA; no support means no European entry

MARKET 4: Latin America (supply chain corridor)
  Offer: None currently
  Missing: Pix, Boleto, SPEI, OXXO
  Global food supply chains increasingly source from LATAM; no local payment support

MARKET 5: UK (potential expansion)
  Offer: None currently
  Missing: Faster Payments, Open Banking, BACS Direct Debit
  UK F&B distribution is a large market with distinct local payment rails

**Key meeting angles:**
1. **Adyen single-PSP risk**: Notch just partnered with Adyen (Feb 2025) but has no fallback. Orchestration adds resilience without disrupting the new partnership.
2. **B2B high-ticket recovery**: Food distributors process large invoices. A single failed $10K+ payment that cascades to a second acquirer pays for itself many times over.
3. **Global food supply chain**: Notch is North America only. Adding SEPA, Pix, and SPEI via one API enables international expansion for their distributor customers.
4. **COD displacement**: Notch's mission is moving F&B from cash/checks to digital. More payment methods (Interac, Pay by Bank, wallets) accelerate that migration.
5. **Pivot momentum**: ChefHero to Notch pivot shows adaptability. The team has proven willingness to rebuild around a better payment infrastructure thesis.

**Sources:**
- [Notch Official Website](https://www.notch.financial/)
- [Notch Payment Processing Software](https://www.notch.financial/products/payment-processing-software)
- [Notch AR Automation](https://www.notch.financial/solutions/accounts-receivable-automation)
- [Notch Adyen Partnership](https://notch.financial/press-releases/notch-adyen-partnership/)
- [Notch Rutter Case Study](https://www.rutter.com/case-studies/notch-financial)
- [Notch Fidelio Partnership](https://www.notch.financial/press-releases/fidelio-and-notch-announce-partnership-to-revolutionize-accounts-receivable-processes-for-distributors)
- [Notch WISK.ai Partnership](https://www.notch.financial/press-releases/notch-financial-wisk-ai-announce-strategic-partnership)
- [Notch $10M Funding (Portage)](https://www.notch.financial/press-releases/notch-announces-funding-led-by-portage)
- [Notch $13.7M BetaKit](https://betakit.com/after-navigating-major-changes-to-restaurant-industry-notch-closes-13-7-million-cad-to-fuel-pivot-to-fintech/)
- [Notch Tracxn Profile](https://tracxn.com/d/companies/notch/__EC5lPj0NBuczO8TBnxmSIujDU4FV9V0hbLf_k3NIti8)
- [Notch Crunchbase Profile](https://www.crunchbase.com/organization/notch-financial)
- [Notch GetApp Profile](https://www.getapp.com/finance-accounting-software/a/notch/)
- [This Week in Fintech: Adyen + Notch](https://www.thisweekinfintech.com/live-from-toronto-adyens-head-of-canada-sander-meijers-and-notchs-ceo-jordan-huck-on-building-for-canadian-businesses/)
- [Brandfetch: Notch Logo](https://brandfetch.com/notch.financial)
