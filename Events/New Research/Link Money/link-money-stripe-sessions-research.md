# LINK MONEY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Link Money
=======================================

Logo: https://brandfetch.com/link.money
Nombre merchant: Link Money

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US Only Coverage
Tittle_Pain Point_2: No Card Fallback Layer
Tittle_Pain Point_3: Limited APM Ecosystem
Tittle_Pain Point_4: Merchant Adoption Friction
Tittle_Pain Point_5: No Multi Acquirer Routing

Desc_Pain Point_1: Link Money operates exclusively in the US market with connections to 3,400+ US banks. No coverage in Europe (SEPA, Open Banking UK), Latin America (PIX, PSE), or Asia Pacific. As merchants using Link Money expand internationally, they need a parallel payment infrastructure for non US markets.
Desc_Pain Point_2: Link Money provides Pay by Bank as a card alternative, reducing processing fees by 70 to 80%. But when a bank authentication fails or a customer's bank is not in the 3,400+ network, there is no automatic cascade to a card payment or alternative method. The transaction is simply lost.
Desc_Pain Point_3: Link Money focuses on ACH and A2A bank payments only. No digital wallets (Apple Pay, Google Pay), no BNPL, no local payment methods beyond US bank accounts. Merchants need a full payment stack alongside Pay by Bank, requiring a separate integration for every additional payment method.
Desc_Pain Point_4: With only 37 employees and $30M total funding, Link Money serves as a specialized component in the merchant payment stack. Merchants must separately integrate Link Money for A2A plus a card PSP (Stripe, Adyen) plus wallets plus local methods. Each integration adds engineering cost and operational complexity.
Desc_Pain Point_5: Link Money routes all transactions through its single ACH connection. No smart routing between multiple bank rails, no optimization of which bank connection to use for each transaction. As transaction volume grows, merchants cannot optimize for speed, cost, or success rate across different bank networks.

SLIDE 1: PSP TOPOLOGY

PSP_1: Link Money (Pay by Bank / ACH) PSP_2: 3,400+ US Bank Connections PSP_3: Radial (Integration Partner) PSP_4: Mastercard Start Path (Accelerator)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Instant (EU)
Local_M_2: Open Banking UK
Local_M_3: PIX (Brazil)
Local_M_4: UPI (India)
Local_M_5: iDEAL (Netherlands)
Local_M_6: BLIK (Poland)
Local_M_7: PayPay (Japan)
Local_M_8: Apple Pay (Global)
Local_M_9: Google Pay (Global)
Local_M_10: Boleto (Brazil)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Pay by Bank transaction to the optimal bank connection or acquirer per customer BIN, issuer, and market. When Link Money merchants process thousands of A2A payments, even a 1% improvement in bank authentication success recovers meaningful revenue. Smart Routing boosts approval rates 3 to 10%.
Desc_Yuno_Cap2: When a bank authentication fails or a customer's bank is not supported, Yuno cascades instantly to a card payment, digital wallet, or alternative method. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this exact failover, turning lost A2A attempts into completed payments.
Desc_Yuno_Cap3: Extend Link Money's US bank coverage with PIX in Brazil, SEPA in EU, UPI in India, iDEAL in Netherlands, and Open Banking UK. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months with Yuno. Link Money merchants could accept payments in 50+ countries alongside Pay by Bank.
Desc_Yuno_Cap4: Unify Link Money Pay by Bank data with card, wallet, and local payment method performance into one real time dashboard. Compare A2A success rates against card approval rates by merchant and region. Track the 70 to 80% fee savings from bank payments alongside total payment mix optimization.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Link Money at a glance:**
- Legal Name: Link Financial Technologies, Inc. (dba Link Money)
- Founded: 2021. HQ: San Francisco, California
- Co-Founders: Eric Shoykhet (CEO) and Edward Lando
- Total Funding: $30M over 2 rounds. Seed: $10M (Tiger Global, Amplo). Series A: $20M (Valar Ventures, Amplo)
- Employees: ~37 (as of January 2026)
- Bank Coverage: 3,400+ US banks, 90%+ of US banked population
- Market Focus: US only (no international operations confirmed)
- Products: Pay by Bank, AccountVerify, Dynamic Links, Indicators, Payouts
- Key Partnership: Radial (bpostgroup company) for enterprise ecommerce merchants
- Accelerator: Mastercard Start Path Open Banking (selected 2024)
- Value Proposition: Reduce merchant processing fees by 70 to 80% vs cards. 0.5% subscription failure rate vs higher card rates

**Confirmed PSPs and Payment Infrastructure:**
- Link Money is itself a PSP/payment method (Pay by Bank via ACH/A2A)
- US bank connections: 3,400+ banks covering 90%+ of banked population
- Authentication: Bank app login (password, Face ID, fingerprint)
- Real time funds guarantee via proprietary AI/ML model
- Same day settlement to 95% of US accounts (payouts)
- Integration: SDK for web and mobile (JavaScript, iOS, Android)
- Partners: Radial (enterprise ecommerce), Optty (payments platform)
- Mastercard Start Path Open Banking accelerator participant
- Nacha compliant for account verification
- FDX standards compliant

**Products and Features:**
- Pay by Bank: Core product. Customers pay directly from bank account at checkout. No card details needed
- AccountVerify: Bank account verification for Nacha compliance and KYC
- Dynamic Links: No code payment links shared via SMS or email
- Indicators: Fraud prevention and risk assessment tools
- Payouts: Same day settlement to merchant sellers and partners

**Payment Positioning and Market Context:**
- Link Money is a payment method provider, not a traditional merchant billing company
- Their merchants integrate Link Money alongside existing card PSPs (Stripe, Adyen, etc.)
- Pay by Bank sits as one option in a merchant's checkout alongside cards and wallets
- Key differentiator: 70 to 80% lower fees than card processing
- Subscription use case: 0.5% failure rate for direct debit vs higher card decline rates
- Fraud: ACH fraud at 0.08 basis points (8 cents per $10,000)
- US merchants pay 10x more in processing fees than European counterparts

**Key meeting angles:**
1. **US only coverage limits merchant growth** | Link Money connects to 3,400+ US banks but has zero international coverage. As merchants grow globally, they need PIX in Brazil, SEPA in EU, UPI in India, and Open Banking UK. Yuno provides 1,000+ payment methods across 50+ countries through a single API. Link Money merchants get global reach without building separate integrations per market.
2. **No fallback when bank auth fails** | When a Pay by Bank authentication fails or a bank is outside the 3,400 network, the transaction drops. No cascade to a card or alternative method. Yuno's failover engine catches these failures and routes them to the next best payment option. NOVA recovers up to 75% of soft declines automatically.
3. **Payment orchestration complements A2A** | Link Money excels at reducing card processing fees by 70 to 80%. But merchants still need cards, wallets, BNPL, and local methods for full coverage. Yuno orchestrates all payment methods including A2A into one unified flow. Smart Routing optimizes which method to present per customer, maximizing conversion and minimizing cost.
4. **Radial partnership shows enterprise demand** | Link Money partnered with Radial to bring Pay by Bank to enterprise ecommerce brands. These same enterprise merchants need multi acquirer routing, international coverage, and unified reporting. Yuno provides the orchestration layer that makes Pay by Bank work alongside every other payment method at enterprise scale.
5. **Open banking is growing, orchestration is the unlock** | A2A payments projected to reach $5.7T by 2029. Mastercard selected Link Money for Start Path. The US market is early. As open banking scales, merchants need one platform to manage A2A alongside cards, wallets, and local methods. Yuno is that platform.

**Link Money Leadership:**
- Eric Shoykhet: Co-Founder and CEO. Also founded Atom Finance. Collectively raised $100M across ventures
- Edward Lando: Co-Founder
- Rohit Mehtani: Chief Product Officer
- Syed Khalid: Chief Compliance Officer
- Amrit Patra: VP of Engineering

**Recent corporate developments:**
- 2024: Selected for Mastercard Start Path Open Banking accelerator
- 2024: Partnership with Radial for enterprise ecommerce Pay by Bank
- 2024: Partnership with Optty payments platform
- 2023: Raised $30M total ($20M Series A from Valar Ventures)
- Focus: US market open banking adoption for merchants seeking card fee reduction
- Market context: A2A payments projected to reach $5.7T globally by 2029

**Sources:**
- [Link Money Website (link.money)](https://link.money/)
- [Link Money About (link.money)](https://link.money/about)
- [Link Money Blog: Problems Pay by Bank Solves (link.money)](https://link.money/blog/what-problems-link-money-pay-by-bank-solves-and-why-merchants-should-care)
- [Link Money Pay by Bank vs ACH (link.money)](https://link.money/blog/pay-by-bank-vs-ach-direct-debit-what-is-best-for-my-business)
- [Link Raises $30M (TechCrunch)](https://techcrunch.com/2023/01/19/link-raises-30m-to-help-merchants-accept-direct-bank-payments/)
- [Link Money Funding (Crunchbase)](https://www.crunchbase.com/organization/link-financial)
- [Radial Link Money Partnership (BusinessWire)](https://www.businesswire.com/news/home/20240213680383/en/Radial-and-Link-Money-Partner-to-Introduce-Pay-by-Bank-a-Secure-and-Cost-Effective-Payment-Solution-for-Global-Merchants)
- [Radial Link Money Partnership (PYMNTS)](https://www.pymnts.com/partnerships/2024/radial-and-link-money-partner-on-pay-by-bank-offering/)
- [Mastercard Start Path Open Banking (Mastercard)](https://www.mastercard.com/global/en/innovation/partner-with-us/start-path/open-finance.html)
- [Link Money Optty Partnership (Finovate)](https://finovate.com/open-banking-firm-link-money-teams-up-with-payments-platform-optty/)
- [Link Money on Omdia (Omdia)](https://omdia.tech.informa.com/om029970/on-the-radar-link-money-utilizes-open-banking-to-enable-a2a-payments-for-us-merchants)
- [Link Money Profile (CBInsights)](https://www.cbinsights.com/company/link-3)
- [A2A Payments $5.7T by 2029 (Retail Banker)](https://www.retailbankerinternational.com/sponsored/a2a-banking-to-reach-5-7-trillion-in-2029-what-it-means-for-fintechs-and-challengers/)
- [McKinsey US Open Banking A2A (McKinsey)](https://www.mckinsey.com/industries/financial-services/our-insights/the-role-of-us-open-banking-in-catalyzing-the-adoption-of-a2a-payments)
