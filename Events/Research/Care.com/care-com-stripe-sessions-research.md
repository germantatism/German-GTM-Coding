# CARE.COM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Care.com
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/3/3f/Care.com_Logo.svg
Nombre merchant: Care.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: FTC Fined $8.5M for Billing
Tittle_Pain Point_2: 16 Countries, Cards Only
Tittle_Pain Point_3: Subscription Churn Crisis
Tittle_Pain Point_4: No PSP Redundancy
Tittle_Pain Point_5: HomePay Payout Complexity

Desc_Pain Point_1: FTC fined Care.com $8.5M for deceptive subscription billing. 194,207 consumers received refunds. Cancellation flows designed to impede users. 73% of Trustpilot reviews are 1 star. Billing trust is broken.
Desc_Pain Point_2: Care.com operates in 16+ countries (US, Canada, UK, Germany, France, Nordics, Benelux, ANZ) but only accepts Visa, Mastercard, Amex, Discover. No local European APMs despite major EU presence.
Desc_Pain Point_3: Subscription model with monthly, quarterly, and annual plans. Users report unauthorized charges after cancellation, billing years later. Involuntary churn from failed card payments has no PSP level retry logic.
Desc_Pain Point_4: No confirmed backup PSP or payment orchestrator. A single processor handles subscriptions across 16+ countries. Any outage halts all recurring billing globally with no cascade or failover path.
Desc_Pain Point_5: HomePay processes payroll for nanny/caregiver employers across tax jurisdictions. Payroll tax calculations, direct deposits, and compliance across US states add reconciliation layers with no unified payment dashboard.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe [INFERENCE]
PSP_2: N/A
PSP_3: N/A
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: Giropay/EPS
Local_M_5: Carte Bancaire
Local_M_6: Open Banking (UK)
Local_M_7: Swish (Sweden)
Local_M_8: MobilePay (Denmark)
Local_M_9: PayPal
Local_M_10: Apple Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Subscription Routing
Tittle_Yuno_Cap2: NOVA AI Recovery
Tittle_Yuno_Cap3: Pan European APM Activation
Tittle_Yuno_Cap4: Unified Billing Dashboard

Desc_Yuno_Cap1: Route each Care.com subscription renewal across the best performing processor for that card BIN, issuer, and country. Failed renewals automatically cascade to backup PSPs. Livelo (subscriptions, Brazil) achieved +5% approval and 50% recovery in under 3 months with Yuno.
Desc_Yuno_Cap2: NOVA AI agents recover failed subscription payments via email and WhatsApp with up to 75% recovery rate. For Care.com's subscription model across 16+ countries, NOVA prevents involuntary churn before it becomes a cancellation or FTC complaint.
Desc_Yuno_Cap3: Activate iDEAL, SEPA, Bancontact, Carte Bancaire, Swish, MobilePay, and Open Banking via one API across all 16+ Care.com markets. 1,000+ payment methods, no engineering sprints per country. InDrive scaled 10 markets in under 8 months with 90% approval.
Desc_Yuno_Cap4: One dashboard reconciling Care.com subscriptions, HomePay payroll, and enterprise billing across all markets. Rappi (20+ PSPs) cut analyst time by 80% with Yuno. Reconciliation reduction up to 90%. Single source of truth for every transaction.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Care.com at a glance:**
- HQ: Dallas, TX | Offices: New York, Shelton, Berlin | CEO: Brad E. Wilson
- Acquired by IAC in February 2020 for $500M. Sold to Pacific Avenue Capital Partners in March 2026 for $320M (closing H1 2026).
- FY2025 Revenue: $347M with $47M Adjusted EBITDA (IAC reporting)
- Largest online marketplace for finding family care and care jobs, serving a $400B market
- Operations in 16+ countries: US, Canada, UK, Germany, Austria, Switzerland, France, Spain, Belgium, Netherlands, Ireland, Australia, New Zealand, Sweden, Finland, Denmark, Norway
- European operations via Care.com Europe GmbH (Munich) and Betreut.de (Berlin)
- Enterprise clients include Google, Facebook, Starbucks, BestBuy
- Services: childcare, senior care, pet care, housekeeping, tutoring, special needs care
- HomePay: nanny/household payroll and tax service

**Key leadership (payments relevant):**
- Brad E. Wilson, CEO (since June 2023)
- Amit Goyal, CTO (appointed March 2024): 20+ years leading technology and product teams, building large scale distributed platforms
- Elizabeth Sartin, Chief Product Officer
- Naaz Nichols, Chief Customer Experience Officer
- No dedicated VP/Head of Payments identified

**Confirmed PSPs and payment infrastructure:**
- No PSP publicly confirmed in official documentation. Care.com support pages mention credit/debit card payments only.
- Stripe [INFERENCE]: StackShare lists Care.com's tech stack but does not explicitly confirm Stripe. Given the subscription model and IAC portfolio patterns, Stripe is a likely processor.
- HomePay: separate payroll processing system for caregiver employer payments, tax filings, and direct deposits
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment methods confirmed:**
- Credit cards: Visa, Mastercard, Amex, Discover
- NOT confirmed: Apple Pay, Google Pay, PayPal, SEPA, iDEAL, or any European local APMs
- HomePay: direct deposit for caregiver payroll

**Missing local APMs (blind spots across 16+ markets):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | SEPA Direct Debit | Eurozone (DE, FR, NL, BE, AT, ES) | Standard for recurring Euro payments. Critical for subscription billing across Care.com's 10+ EU markets. |
| 2 | iDEAL | Netherlands | 50%+ of Dutch online transactions. Care.com operates care.com/nl-nl. |
| 3 | Bancontact | Belgium | 17M+ cards. Care.com operates both care.com/fr-be and care.com/nl-be. |
| 4 | Giropay/EPS | Germany/Austria | Popular online bank transfer. Betreut.de and betreut.at serve these markets. |
| 5 | Carte Bancaire | France | Dominant card network. Local routing via CB improves auth rates for care.com/fr-fr. |
| 6 | Open Banking (UK) | UK | Account to account payments. Lower fees than card for recurring subscriptions at care.com/en-gb. |
| 7 | Swish | Sweden | 8M+ users in Sweden. Dominant mobile payment. Care.com operates care.com/sv-se. |
| 8 | MobilePay | Denmark | Leading Danish mobile payment app. Care.com operates care.com/da-dk. |
| 9 | PayPal | All markets | 400M+ active accounts globally. Not confirmed as a payment option for subscriptions. |
| 10 | Apple Pay | All markets | Standard digital wallet. Not confirmed on Care.com checkout. |

**Payment complaints and regulatory issues:**
- FTC settlement (August 2024): $8.5M fine for deceptive subscription practices. 194,207 consumers received refunds.
- FTC findings: cancellation process designed to impede users with multi page questionnaires, confusing language, warnings, and upsell offers
- Trustpilot: 2.3/5 stars from 4,600+ reviews. 73% are 1 star.
- PissedConsumer: 1.4 star rating from 642 reviews. 5% likely to recommend.
- BBB complaints: unauthorized charges, billing after cancellation, denied refunds
- Users report being charged years after cancellation
- Recurring theme: subscription billing system lacks transparency and customer control

**Key strategic developments (2025 to 2026):**
1. Sale to Pacific Avenue Capital Partners (March 2026): $320M all cash transaction. PE ownership typically drives payment optimization and cost reduction.
2. Brand refresh (June 2025): expanded from childcare to broader caregiving platform (senior care, pet care, home help, camp searches)
3. HomePay growth: nanny/household payroll service expanding as care costs rise
4. Enterprise segment: Google, Facebook, Starbucks, BestBuy offer Care.com as employee benefit
5. PE ownership transition: new owner will likely scrutinize payment costs, conversion rates, and subscription billing efficiency

**Yuno case references for the meeting:**

LIVELO: Subscription platform in Brazil. +5% approval rate, 50% recovery of failed transactions in under 3 months with Yuno. Directly relevant to Care.com's subscription billing challenges.

INDRIVE: Marketplace scaled 10 LATAM markets in under 8 months. 90% approval rate. 4.5%+ recovery. Similar multi country marketplace model.

RAPPI: 20+ payment providers. Analyst time reduced 80%. New provider implementation time reduced to zero. Relevant to Care.com's multi market reconciliation needs.

VIVA AEROBUS: 75% NOVA recovery rate, $300+ per transaction. Shows AI recovery power for high value failed transactions.

**Key meeting angles:**

1. **FTC fine makes billing optimization urgent**: $8.5M settlement for deceptive billing. The new PE owner will demand clean, transparent subscription management. Yuno's orchestration provides retry logic that recovers revenue without the dark patterns that triggered FTC action.

2. **PE ownership = payment cost scrutiny**: Pacific Avenue Capital Partners acquiring for $320M. PE firms optimize unit economics immediately. Yuno's smart routing reduces processing costs while improving approval rates.

3. **16+ country subscription billing without local APMs**: Care.com charges European subscribers with international card processing instead of local methods like SEPA, iDEAL, Swish. This means higher decline rates, higher fees, and worse UX. Yuno activates all local methods via one API.

4. **NOVA AI replaces dark patterns**: Instead of making cancellation hard (FTC violation), NOVA AI recovers failed payments proactively via email/WhatsApp. Revenue recovery without regulatory risk.

5. **Subscription peer already on Yuno**: Livelo (subscription platform) achieved +5% approval and 50% recovery in under 3 months. Care.com's subscription model is directly comparable.

6. **HomePay + subscriptions + enterprise = reconciliation nightmare**: Three revenue streams across 16+ countries with no unified payment dashboard. Yuno provides single source of truth.

**Sources:**
- [Care.com Wikipedia](https://en.wikipedia.org/wiki/Care.com)
- [Care.com About / Corporate](https://www.care.com/about/)
- [Care.com Europe GmbH Portal](https://www.care.com/en-ie/portals)
- [Care.com UK Portal](https://www.care.com/en-gb/portals)
- [Care.com Help Center: Payments](https://help.care.com/families/s/topic/0TO5Y000009m2uMWAQ/payments?language=en_US)
- [Care.com Help Center: Refund Policy](https://help.care.com/families/s/article/what-is-the-care-com-refund-policy-for-families?language=en_US)
- [Care.com HomePay](https://www.care.com/homepay)
- [Care.com Plans and Pricing](https://www.care.com/app/vhp/plans-and-pricing)
- [IAC Q2 2025 Earnings (Care.com segment)](https://ir.iac.com/static-files/84f3b67e-1299-4561-b33d-f9310e16127a)
- [IAC Q3 2025 Earnings](https://ir.iac.com/static-files/e2666073-0141-41f8-a45d-77ea800a65be)
- [Pacific Avenue Capital Acquires Care.com (PR Newswire)](https://www.prnewswire.com/news-releases/pacific-avenue-capital-partners-to-acquire-iacs-carecom-302701509.html)
- [IAC Sells Care.com $320M (StockTitan)](https://www.stocktitan.net/news/IAC/pacific-avenue-capital-partners-to-acquire-iac-s-care-flflvkdg28uu.html)
- [Care.com Sale $320M (Pulse2)](https://pulse2.com/iac-320-million-sale-of-care-com-to-pacific-avenue-capital-partners/)
- [Care.com CTO Amit Goyal (BusinessWire)](https://www.businesswire.com/news/home/20240501593089/en/Care.com-Names-Amit-Goyal-Chief-Technology-Officer)
- [Care.com Executive Team Expansion (BusinessWire)](https://www.businesswire.com/news/home/20230927495727/en/Care.com-Builds-out-Executive-Team-With-CMO-CPO-and-CXO-Appointments)
- [FTC Care.com Settlement (FTC)](https://www.ftc.gov/enforcement/refunds/carecom-refunds)
- [FTC Care.com Action (FTC Press)](https://www.ftc.gov/news-events/news/press-releases/2024/08/ftc-takes-action-against-carecom-deceiving-caregivers-about-wages-availability-jobs-its-site)
- [FTC $8.1M Refunds (FTC Press)](https://www.ftc.gov/news-events/news/press-releases/2025/06/ftc-sends-more-81-million-consumers-harmed-carecoms-deceptive-claims-about-earnings-job-listings)
- [Care.com FTC Settlement (Courthouse News)](https://www.courthousenews.com/federal-trade-commission-announces-over-8-million-payout-from-online-caregiver-marketplace/)
- [Care.com Trustpilot Reviews](https://www.trustpilot.com/review/care.com)
- [Care.com PissedConsumer](https://care-com.pissedconsumer.com/review.html)
- [Care.com BBB Complaints](https://www.bbb.org/us/tx/dallas/profile/caregiver-resources/carecom-0875-91350147/complaints)
- [Care.com StackShare Tech Stack](https://stackshare.io/care-com/care-com)
- [Care.com Tracxn Profile](https://tracxn.com/d/companies/carecom/__ZmJ10WS9N-7BRQvThP-CgLQDYqQ5G2j1q9CPl1LG60I)
- [Yuno Livelo Case Study](https://y.uno/success-cases/livelo)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Platform Overview](https://y.uno/)
