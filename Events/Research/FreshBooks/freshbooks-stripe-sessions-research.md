# FRESHBOOKS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: FreshBooks
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/e/e3/FreshBooks_Cloud_Accounting_Logo.svg
Nombre merchant: FreshBooks

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Gateway Sprawl
Tittle_Pain Point_2: Limited Int'l APMs
Tittle_Pain Point_3: Legacy WePay Migration
Tittle_Pain Point_4: Cross-Border Decline Rate
Tittle_Pain Point_5: Cash Method Blind Spots

Desc_Pain Point_1: Stripe, PayPal, Braintree, and Authorize.Net run as disconnected gateways. Each has separate fees, dashboards, and settlement timelines across 160+ countries.
Desc_Pain Point_2: Outside US/CA/UK/EU, FreshBooks offers only cards via Stripe. No Pix for Brazil, no UPI for India, no OXXO for Mexico despite acquisitions in DE and MX.
Desc_Pain Point_3: WePay shut down July 2024; cards migrated to Stripe by Jan 2025. Token migration risks include orphaned payment methods and failed recurring charges.
Desc_Pain Point_4: Invoices accepted in 195+ countries and 135+ currencies, but most markets use cross-border Stripe acquiring. International card declines compound for SMBs.
Desc_Pain Point_5: FastBill (Germany) and Facturama (Mexico) acquisitions expand reach, but no Giropay, SOFORT, OXXO, or SPEI confirmed. Local clients invoice in local markets without local rails.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (FreshBooks Payments)
PSP_2: PayPal
PSP_3: Stripe Standard
PSP_4: Braintree

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: SPEI
Local_M_5: Giropay
Local_M_6: BLIK
Local_M_7: iDEAL
Local_M_8: M-Pesa
Local_M_9: GCash
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, PayPal, and Braintree by client location, card BIN, and currency. With 30M+ users in 160+ countries, routing each invoice payment to the best gateway per market delivers 3 to 10% approval uplift for SMB clients.
Desc_Yuno_Cap2: Automatic cascade across FreshBooks' multi-gateway stack. When Stripe declines an invoice payment, Yuno reroutes to PayPal or Braintree in milliseconds. Up to 50% recovery on failed invoice payments. Critical for recurring billing where failed charges cause SMB cash flow gaps.
Desc_Yuno_Cap3: Activates local payment methods for FreshBooks' acquired markets: Giropay in Germany (FastBill), OXXO and SPEI in Mexico (Facturama), Pix in Brazil, UPI in India. One API, 1,000+ methods. SMBs in 160+ countries can pay invoices with local methods.
Desc_Yuno_Cap4: One dashboard unifying Stripe, PayPal, Braintree, and Authorize.Net under a single reconciliation layer. Eliminates multi-gateway accounting complexity for 30M+ users. NOVA AI recovers 75% of failed invoice payments. Instant settlement visibility for SMB cash flow.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**FreshBooks at a glance:**
- Founded: 2003, HQ: Toronto, Canada (legal entity: 2ndSite Inc.)
- Valuation: $1B+ (August 2021, Series E)
- Revenue: estimated $150M to $750M (sources conflict; private company)
- Latest funding: $125M debt facility (March 2025, Morgan Stanley Investment Management)
- Users: 30M+ worldwide across 160+ countries
- Employees: ~400 to 500
- Offices: Toronto (HQ), Raleigh NC (US), Amsterdam (Netherlands), Zagreb (Croatia)
- Acquisitions: FastBill (Germany, Oct 2021), Facturama (Mexico, Sept 2020)
- Products: Invoicing, Accounting, Expenses, Time Tracking, Payments, Payroll, Projects
- Barclays partnership: free FreshBooks accounts for UK small businesses during tax season
- Target market: service-based SMBs (freelancers, consultants, agencies)

**Confirmed Payment Stack:**
- Stripe (FreshBooks Payments): primary processor for US and CA. Replaced WePay in 2024. Credit cards, debit cards, ACH, Apple Pay, Google Pay, Affirm, Afterpay (US only)
- Stripe Standard: international integration supporting SEPA DD (EU), BACS DD (UK), PAD (Canada)
- PayPal: global standalone gateway
- Braintree: supported gateway option for US/CA
- Authorize.Net: supported gateway with +1% surcharge
- WePay/Chase: LEGACY, shut down July 2024, fully migrated to Stripe by Jan 2025
- No third-party payment orchestrator detected

**Confirmed Payment Methods:**
- Credit/debit cards (all major brands)
- ACH bank transfer (US)
- Apple Pay, Google Pay (US/CA)
- SEPA Direct Debit (EU, via Stripe Standard)
- BACS Direct Debit (UK, via Stripe Standard)
- PAD Pre-Authorized Debit (Canada, via Stripe Standard)
- PayPal (global)
- Affirm BNPL (US)
- Afterpay (US only)
- Invoicing in 135+ currencies across 195+ countries

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~40 to 50% of traffic)
  Currently offer: Visa/MC/Amex, ACH, Apple Pay, Google Pay, Affirm, Afterpay, PayPal
  Missing: Venmo (standalone), Cash App Pay
  Impact: Comprehensive US coverage. Minor gaps in alternative wallets.

MARKET 2: Canada (~15 to 20% of traffic, HQ)
  Currently offer: Visa/MC, PAD, Apple Pay, Google Pay, PayPal
  Missing: Interac e-Transfer
  Impact: Interac is Canada's dominant P2P/B2B payment rail. Adding it would accelerate invoice collection.

MARKET 3: United Kingdom (~5 to 8% of traffic, Barclays partnership)
  Currently offer: Visa/MC, BACS Direct Debit, PayPal
  Missing: Open Banking (PayByBank), Faster Payments
  Impact: Open Banking reduces card fees and increases instant settlement for UK SMB invoices.

MARKET 4: Germany (~2 to 4% of traffic, FastBill acquisition)
  Currently offer: Visa/MC, SEPA Direct Debit
  Missing: Giropay, SOFORT/Klarna, EPS
  Impact: FastBill serves German SMBs but no German-specific local rails beyond SEPA confirmed.

MARKET 5: Mexico (Facturama acquisition)
  Currently offer: Credit/debit cards, PayPal
  Missing: OXXO, SPEI, CoDi
  Impact: Facturama handles Mexican e-invoicing but no local payment rails for collecting invoice payments.

**Payment complaint evidence:**
- Capterra/NerdWallet: bank feed connection failures and duplicate transactions among top complaints
- Multiple reviews cite difficulty managing multi-gateway settings
- WePay to Stripe migration caused confusion about stored payment methods (2024 to 2025)
- International users report higher decline rates on cross-border transactions
- CardFellow review notes Authorize.Net integration adds +1% surcharge, creating hidden fee complaints

**Key meeting angles:**
1. **Multi-gateway sprawl without orchestration** | Stripe + PayPal + Braintree + Authorize.Net with no unified routing or failover
2. **WePay migration aftermath** | Recent PSP migration (2024) shows willingness to evolve payment stack; orchestration is the logical next step
3. **Acquired markets lack local rails** | FastBill (Germany) and Facturama (Mexico) serve local SMBs but with no local APMs like Giropay or OXXO
4. **30M+ users, 160+ countries** | Scale demands automated routing across gateways, not manual per-gateway configuration
5. **SMB cash flow dependency** | Failed invoice payments directly impact freelancer and SMB cash flow. Recovery rates matter more here than in enterprise
6. **Barclays UK partnership** | UK expansion with Barclays creates opportunity to add Open Banking payment rails
7. **$125M debt facility (March 2025)** | Fresh capital for growth; payment infrastructure optimization is a high-leverage investment

**Sources:**
- [FreshBooks Support: Stripe Payments](https://support.freshbooks.com/hc/en-us/articles/24999759052429)
- [FreshBooks Support: Stripe Standard](https://support.freshbooks.com/hc/en-us/articles/216579858)
- [FreshBooks Support: WePay to Stripe Migration](https://support.freshbooks.com/hc/en-us/articles/22060878896013)
- [FreshBooks Support: Online Payment Settings](https://support.freshbooks.com/hc/en-us/articles/217544777)
- [FreshBooks Support: Stripe Standard Fees](https://support.freshbooks.com/hc/en-us/articles/360035569211)
- [FreshBooks Partner: Stripe](https://www.freshbooks.com/partner/stripe)
- [FreshBooks Press: Releases](https://www.freshbooks.com/press/releases)
- [FreshBooks Press: Facturama Acquisition](https://www.freshbooks.com/press/releases/freshbooks-acquires-mexico-based-e-invoicing-company-facturama-further-expanding-its-international-presence)
- [BetaKit: FreshBooks Stripe Partnership](https://betakit.com/freshbooks-expands-stripe-partnership-with-new-embedded-payments-offering/)
- [BetaKit: FastBill Acquisition](https://betakit.com/freshbooks-acquires-germanys-fastbill-as-it-pursues-global-expansion/)
- [CardFellow: FreshBooks Payments Review](https://www.cardfellow.com/blog/freshbooks-payments-review)
- [TechCrunch: FreshBooks $1B Valuation](https://techcrunch.com/2021/08/09/freshbooks-secures-130-75m/)
- [Tracxn: FreshBooks Profile](https://tracxn.com/d/companies/freshbooks/__FodOJN0CRJhaeEA3kDg_7oh4plQTHkBD2AVaxCN8TKw)
- [ExpandedRamblings: FreshBooks Statistics](https://expandedramblings.com/index.php/freshbooks/)
- [Capterra: FreshBooks Reviews](https://www.capterra.com/p/142390/FreshBooks/reviews/)
