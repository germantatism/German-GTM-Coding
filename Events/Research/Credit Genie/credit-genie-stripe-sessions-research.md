# CREDIT GENIE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Credit Genie
=======================================

Logo: https://asset.brandfetch.io/idJqL_W48O/idosPFcCeP.svg
Nombre merchant: Credit Genie

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: ACH-Only Disbursement Lag
Tittle_Pain Point_2: High Decline on Repayments
Tittle_Pain Point_3: Subscription Fee Leakage
Tittle_Pain Point_4: No Real-Time Pay Rails
Tittle_Pain Point_5: Single-Market Limitation

Desc_Pain Point_1: Standard cash advance disbursements via ACH take 1-3 business days. Express ACH costs users $5.99; instant debit card transfer costs $12.99. High delivery fees erode the value proposition of $5-$150 no-interest advances. Faster, cheaper disbursement rails would improve retention and NPS.
Desc_Pain Point_2: Repayment is auto-debited from linked bank accounts on estimated payday. Insufficient funds trigger failed ACH pulls, postponed payments, and split repayment attempts. Each failed debit costs processing fees and extends the collection cycle. No intelligent retry timing or alternate payment rail cascade.
Desc_Pain Point_3: Credit Genie charges $4.99/month (or $3.49 biweekly) as a bank connection fee. Users report being charged even after attempting cancellation. Trustpilot complaints cite unauthorized charges and difficulty stopping recurring billing. Failed subscription charges create churn and reputational damage.
Desc_Pain Point_4: The platform relies on ACH and debit card rails for both disbursement and collection. No support for RTP (Real Time Payments), FedNow, or push-to-card networks beyond basic debit. As competitors like EarnIn and Dave offer instant $250-$1,000 advances, Credit Genie's $150 max with slow rails falls behind.
Desc_Pain Point_5: Credit Genie operates in 46 US states only (unavailable in CT, MD, NV, HI, DC). No international expansion. As a US-only fintech with sub-$1M revenue scaling to $270M valuation, payment infrastructure must support rapid growth without adding PSP integration complexity for each new product line.

SLIDE 1: PSP TOPOLOGY

PSP_1: ACH Network (primary disbursement and repayment rail)
PSP_2: Debit Card Networks (instant disbursement via linked debit)
PSP_3: Plaid (bank account connection and verification)
PSP_4: TransUnion (credit data and identity verification)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: RTP (Real Time Payments)
Local_M_2: FedNow
Local_M_3: Push-to-Card (Visa Direct)
Local_M_4: Apple Pay
Local_M_5: Google Pay
Local_M_6: PayPal
Local_M_7: Venmo
Local_M_8: Cash App Pay
Local_M_9: Zelle
Local_M_10: Credit Card (for subscriptions)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by bank, account type, and funding timing. With $4.99 recurring subscription charges and $5-$150 cash advance repayments debited from consumer bank accounts, routing each ACH pull to optimal timing windows based on deposit patterns delivers higher first-attempt success rates on collections.
Desc_Yuno_Cap2: Automatic cascade when an ACH repayment pull fails due to insufficient funds. Instead of postponing and splitting payments (current approach), Yuno retries through alternate rails or optimal timing windows. Up to 50% recovery on failed transactions reduces write-offs and improves unit economics on micro-lending.
Desc_Yuno_Cap3: Adds payment rails Credit Genie users need: RTP and FedNow for instant disbursement without $12.99 fees, Apple Pay and Google Pay for frictionless subscription payments, Venmo and Cash App Pay for Gen Z users. One API, 1,000+ methods. Modernizes the payment experience for financial wellness users.
Desc_Yuno_Cap4: One dashboard unifying ACH disbursements, debit card transfers, subscription billing, and repayment collection. Real-time monitoring of collection success rates by bank and timing, centralized reconciliation of advances plus fees plus repayments, and NOVA fraud detection (75% reduction) protecting against advance fraud and identity theft.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Credit Genie at a glance:**
- Founded: 2019, Conshohocken, Pennsylvania
- HQ: Conshohocken, PA (near Philadelphia)
- Founder & CEO: Ed Harycki (former founder of Swift Capital, acquired by PayPal in 2017/2018; ex-Barclays Capital, ex-MBNA America)
- Revenue: ~$963.6K (2023)
- Valuation: $270M (as of January 2025)
- Funding: $47.8M total over 4 rounds
- Latest Round: $33.8M (January 28, 2025)
- Key Investors: Khosla Ventures, Tippet Venture Partners, Gabriel Investments, First Round Capital, Sutter Hill Ventures, Protagonist
- Employees: 113 (as of January 2026)
- Products: Cash Boost (cash advances $5-$150), Debt Relief services, Credit Monitoring, Financial Wellness tools
- App: iOS and Android
- Market: US only (46 states; unavailable in CT, MD, NV, HI, DC)
- Team Background: Leaders from PayPal, Square, Cash App
- Technology: AWS Serverless (Amplify, DynamoDB, S3, Lambda, KMS), Plaid, TransUnion

**Confirmed Payment Stack:**
- Plaid: Bank account connection and verification (core infrastructure)
- ACH Network: Primary rail for both cash advance disbursement and repayment collection
- Debit Card Networks: Instant disbursement option (Visa/MC debit rails), $12.99 fee
- Express ACH: Same-day/next-day option, $5.99 fee
- TransUnion: Credit data integration for eligibility assessment
- Bank Connection Fee: $4.99/month or $3.49 biweekly recurring charge
- AWS KMS + CloudHSM: FIPS 140-2 validated encryption for financial data
- No payment orchestrator detected
- No RTP or FedNow support detected
- No Apple Pay, Google Pay, or wallet payments

**Payment/Business Pain Points (User Evidence):**
- Trustpilot: Multiple complaints of unauthorized recurring $4.99 charges
- Users report being charged bank connection fees even after account deletion attempts
- "Deleting the app doesn't stop fees" noted in multiple reviews
- APR equivalent: 130%-4,687% depending on advance amount and fee structure
- Maximum advance: $150 (vs. competitors at $250-$1,000)
- Repayment relies on auto-debit from linked bank; insufficient funds = failed collection
- LendEdu review 2026: "High Fees and Low Advances, Better Alternatives Available"
- No customer service phone number readily available; Zendesk-only support

**Competitive Landscape:**
- Brigit: Up to $250 advances, $8.99-$14.99/month
- Dave: Up to $500 advances
- EarnIn: Up to $1,000/pay period, free
- MoneyLion: Up to $500 with Instacash
- Empower: Up to $250
- Credit Genie's $150 max and $4.99 fee structure is among the least competitive

**Key meeting angles:**
1. **PayPal DNA, payment-first founder** | CEO Ed Harycki sold Swift Capital to PayPal. Understands payment infrastructure deeply. Peer-level conversation about orchestration and routing optimization
2. **ACH collection failures** | Auto-debit repayments fail on insufficient funds. No intelligent retry or cascade. Each failed pull = processing cost + extended collection cycle + potential write-off
3. **$270M valuation, scaling fast** | From $963K revenue to $270M valuation with $47.8M funding. Payment infrastructure must scale with growth. Orchestration prevents PSP integration debt as products expand
4. **Instant disbursement cost** | $12.99 for instant debit, $5.99 for express ACH. RTP/FedNow rails through Yuno could reduce disbursement costs while maintaining speed, improving unit economics
5. **Subscription billing complaints** | Trustpilot filled with unauthorized charge complaints. Better subscription payment management (Apple Pay, Google Pay) reduces friction and improves user trust
6. **Khosla + First Round backed** | Tier-1 VCs expect infrastructure sophistication. Payment orchestration signals maturity to investors and supports Series C positioning
7. **Debt relief services expansion** | Beyond cash advances, Credit Genie negotiates with creditors and manages repayment plans. Multi-party payment flows (consumer, creditor, servicer) need orchestration

**Sources:**
- [Credit Genie: Homepage](https://www.creditgenie.com/)
- [Credit Genie: About](https://www.creditgenie.com/about)
- [Credit Genie: Cash Boost](https://www.creditgenie.com/cash-boost)
- [Credit Genie: Terms and Conditions](https://www.creditgenie.com/terms-and-conditions)
- [Credit Genie: Contact Us](https://creditgenie.com/contact-us)
- [AWS Blog: Credit Genie MVP to Growth](https://aws.amazon.com/blogs/mobile/fintech-startup-creditgenie-ultimate-speed-from-mvp-to-growth/)
- [Alex Kates: Scaling Credit Genie with AWS Serverless](https://www.alexkates.dev/blog/how-we-scaled-the-credit-genie-platform-with-aws-serverless)
- [Crunchbase: Credit Genie](https://www.crunchbase.com/organization/creditly-corp)
- [PitchBook: Credit Genie 2026](https://pitchbook.com/profiles/company/489043-63)
- [GetLatka: Credit Genie Revenue](https://getlatka.com/companies/creditgenie.com)
- [PremierAlts: Credit Genie Valuation $270M](https://www.premieralts.com/companies/credit-genie/valuation)
- [Trustpilot: Credit Genie Reviews](https://www.trustpilot.com/review/creditgenie.com)
- [LendEdu: Credit Genie Review 2026](https://lendedu.com/blog/credit-genie-app-review/)
- [Finder: Credit Genie Review](https://www.finder.com/cash-advance-apps/credit-genie-review)
- [OverdraftApps: Credit Genie Review](https://overdraftapps.com/credit-genie-review/)
- [FinTech Global: Credit Genie $10M Funding](https://fintech.global/2023/10/24/credit-genie-bags-10m-funding-to-redefine-behavioural-finance-with-ai/)
- [The Org: Ed Harycki](https://theorg.com/org/credit-genie/org-chart/ed-harycki)
- [Brandfetch: Credit Genie Logo](https://brandfetch.com/creditgenie.com)
- [CBInsights: Credit Genie](https://www.cbinsights.com/company/creditly)
