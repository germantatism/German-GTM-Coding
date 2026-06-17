# BOX | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Box
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/57/Box%2C_Inc._logo.svg
Nombre merchant: Box

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: $50K Card Ceiling
Tittle_Pain Point_2: Germany-Only Direct Debit
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: No PayPal Acceptance
Tittle_Pain Point_5: Manual Enterprise Billing

Desc_Pain Point_1: Card charges capped at $50K. Larger deals must use wire or ACH. With 100K+ orgs and 68% Fortune 500 penetration, the cap forces high-value renewals into slow manual billing.
Desc_Pain Point_2: Direct Debit only in Germany. Netherlands, France, Poland, and 30+ other European markets have zero local bank debit options for subscription billing.
Desc_Pain Point_3: Single processor with no cascade. When a card declines on renewal, there is no alternative acquirer retry. Failed payments churn silently across 100K+ orgs in 180+ countries.
Desc_Pain Point_4: Box explicitly does not accept PayPal. With 435M+ active PayPal accounts globally, this locks out SMB and individual users who prefer PayPal for SaaS subs.
Desc_Pain Point_5: Wire and ACH require Business-level accounts with $1K minimum. Checks need approval. Enterprise invoice reconciliation across 6 currencies is manual and fragmented.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Card processing (Visa/MC/Amex/Discover/JCB)
PSP_2: Wire Transfer / ACH (Business contracted accounts)
PSP_3: Direct Debit (Germany only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: iDEAL
Local_M_3: SEPA Direct Debit
Local_M_4: Pix
Local_M_5: UPI
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: Bancontact
Local_M_9: KakaoPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $1.18B revenue, 100K+ paying organizations across 180+ countries, and 68% Fortune 500 penetration, routing each renewal to the best acquirer per market delivers 3-10% auth uplift on global subscriptions.
Desc_Yuno_Cap2: Automatic cascade when a card decline hits the $50K ceiling or fails on renewal. Instead of losing the subscriber to silent churn, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions retains enterprise ARR.
Desc_Yuno_Cap3: Activates methods Box's global enterprise base demands: PayPal, iDEAL in Netherlands, SEPA DD across Europe (not just Germany), Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, KakaoPay in Korea. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard unifying card processing, wire/ACH invoicing, and German Direct Debit into a single view. Real-time approval monitoring per country, centralized multi-currency reconciliation (6 currencies), and NOVA fraud detection (75% reduction).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Box at a glance:**
- Founded: 2005 by Aaron Levie and Dylan Smith. HQ: Redwood City, California
- Public: NYSE: BOX
- Revenue: $1.18B (FY2026, ending January 31, 2026), up 8% YoY
- Market cap: ~$3.28B (April 2026)
- Operating margin: 28% (FY2026)
- Free cash flow: $313M (FY2026, up 3% YoY)
- Remaining Performance Obligations: $1.469B (+21% YoY)
- Customers: 100,000+ paying organizations
- Enterprise adoption: 68% of Fortune 500 use Box
- Net retention rate: ~104%
- Employees: 2,912 (January 2026, +3.6% YoY)
- Accepted currencies: USD, CAD, GBP, EUR, JPY, AUD (contracted accounts)
- AI strategy: Box AI, intelligent content management
- Products: Box Drive, Box Sign, Box Shield, Box Relay, Box Notes, Box Governance

**Confirmed Payment Stack:**
- Credit cards: Visa, MasterCard, American Express, Discover, JCB (Japan only)
- Wire Transfer: Preferred for Business-level accounts ($1,000 minimum)
- ACH: Available for Business-level contracted accounts ($1,000 minimum)
- Check: Subject to approval and geographic availability
- Direct Debit: Germany only
- Bill.com integration: Payment Network ID 0115981319149676
- Credit card charge limit: $50,000 USD or equivalent
- No PayPal accepted (explicitly stated in help docs)
- No local APMs beyond German Direct Debit
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Evidence):**
- PayPal: Explicitly not accepted. Help docs state "Box does not currently accept PayPal"
- SEPA Direct Debit: Not available despite European enterprise customer base
- Direct Debit limited to Germany only, excluding all other European markets
- Wire/ACH require Business-level contracted accounts with $1,000 minimum
- Credit card cap at $50,000 forces large enterprise deals into manual billing
- No local payment methods for Asia, LATAM, or most of Europe
- JCB only accepted in Japan, no other APAC-specific methods

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest enterprise market)
  Accepted: Visa/MC/Amex/Discover, ACH, Wire, Check
  Missing: PayPal, Apple Pay, Google Pay
  Note: Most complete coverage, but $50K card cap and no failover processor

MARKET 2: Europe (significant enterprise base)
  Accepted: Visa/MC/Amex, Wire (contracted), Direct Debit (Germany only)
  Missing: iDEAL (Netherlands), SEPA DD (pan-European), Bancontact (Belgium), BLIK (Poland), GiroPay, Sofort
  Note: Direct Debit exclusively in Germany. Zero bank debit options in 30+ other European markets.

MARKET 3: Japan / APAC (JCB card acceptance signals market)
  Accepted: Visa/MC/Amex, JCB (Japan only), Wire (contracted)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: JCB acceptance shows Japan focus, but no local methods. APAC enterprise market underserved.

MARKET 4: Brazil / LATAM (growing enterprise cloud market)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of digital payments in Brazil. Card-only blocks LATAM expansion.

MARKET 5: India / South Asia (enterprise digital transformation market)
  Accepted: Visa/MC (cross-border)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of Indian digital payments. Cross-border card declines common.

**Key meeting angles:**
1. **$1.18B revenue with $50K card ceiling** | Forces high-value deals into slow wire/ACH workflows. Intelligent routing removes this bottleneck.
2. **68% Fortune 500 penetration** | Massive enterprise base with manual multi-currency reconciliation across 6 currencies
3. **Germany-only Direct Debit** | The only local method Box offers, excluding the entire rest of Europe from bank debit payments
4. **No PayPal explicitly** | Help docs confirm PayPal is not accepted. Locks out 435M+ global PayPal users from self-serve plans.
5. **$1.469B RPO growing 21%** | Remaining performance obligations signal strong renewal pipeline that payment optimization protects
6. **$313M free cash flow** | Profitable company with budget to invest in payment infrastructure modernization
7. **Competitor pressure** | Dropbox, Google Drive, Microsoft OneDrive, and SharePoint offer broader payment options

**Sources:**
- [Box Support: Payment Methods Accepted](https://support.box.com/hc/en-us/articles/360044193453-Payment-Methods-Accepted-by-Box)
- [Box Support: Updating Credit Card](https://support.box.com/hc/en-us/articles/360043694254-Updating-your-Credit-Card-Information)
- [Box: About Us](https://www.box.com/about-us)
- [Box: Customers](https://www.box.com/customers)
- [Box: FAQ](https://www.box.com/about-us/faq)
- [Box Investor Relations: Q4 FY2025 Results](https://www.boxinvestorrelations.com/news-and-media/news/press-release-details/2025/Box-Reports-Fourth-Quarter-and-Fiscal-2025-Financial-Results/)
- [Box Investor Relations: Q3 FY2026 Results](https://www.boxinvestorrelations.com/news-and-media/news/press-release-details/2025/Box-Reports-Third-Quarter-Fiscal-2026-Financial-Results/)
- [Box Investor Relations: Q4 FY2026 Results](https://finance.yahoo.com/news/box-reports-fourth-quarter-fiscal-210500019.html)
- [StockAnalysis: BOX Revenue](https://stockanalysis.com/stocks/box/revenue/)
- [StockAnalysis: BOX Employees](https://stockanalysis.com/stocks/box/employees/)
- [Stock Titan: Box 10-K Annual Report](https://www.stocktitan.net/sec-filings/BOX/10-k-box-inc-files-annual-report-4a4b882ac9a5.html)
- [MacroTrends: Box Revenue](https://www.macrotrends.net/stocks/charts/BOX/box/revenue)
- [Brandfetch: Box Logo](https://brandfetch.com/box.com)
