# DOLARAPP (ARQ) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: DolarApp
=======================================

Logo: https://asset.brandfetch.io/idHlz-K_6A/idTwwPDjnk.svg
Nombre merchant: DolarApp (ARQ)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Processor Limit
Tittle_Pain Point_2: Card-Only Spend Path
Tittle_Pain Point_3: FX Corridor Gaps
Tittle_Pain Point_4: Stablecoin Offramp Gaps
Tittle_Pain Point_5: Fraud at Scale Risk

Desc_Pain Point_1: Paymentology is the sole card issuer-processor for all DolarApp/ARQ Mastercard transactions across Mexico, Colombia, Argentina, and Brazil. No multi-acquirer routing exists. One Paymentology outage blocks card spending for 2M+ users simultaneously.
Desc_Pain Point_2: International spending is card-only via Mastercard. No support for direct bank-to-bank cross-border transfers, QR payments, or wallet-to-wallet payouts. Users receiving freelance income from U.S./EU employers must convert through card rails rather than direct local payout.
Desc_Pain Point_3: Core corridors are USD/MXN, USD/ARS, USD/BRL, and USD/COP. No EUR/GBP corridors to LatAm exist natively. European freelancers or businesses paying LatAm workers cannot use ARQ for direct EUR payout, limiting the total addressable market.
Desc_Pain Point_4: USDC-to-local currency conversion relies on a single offramp path per country (SPEI in Mexico, Pix in Brazil, CVU in Argentina, PSE in Colombia). If the stablecoin bridge fails, users cannot access local funds. No redundant offramp routing exists.
Desc_Pain Point_5: At $10B+ annualized transaction volume, fraud exposure grows. Cross-border stablecoin transactions face unique risks (wallet compromise, social engineering, unauthorized conversions). No multi-layer fraud orchestration across card, stablecoin, and bank transfer rails is documented.

SLIDE 1: PSP TOPOLOGY

PSP_1: Paymentology (card issuer-processor)
PSP_2: Mastercard (card network)
PSP_3: Circle (USDC stablecoin infrastructure)
PSP_4: SPEI / Pix / CVU / PSE (local rails)
PSP_5: Apple Pay / Google Pay (tokenization)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO (Mexico cash)
Local_M_2: Mercado Pago (LatAm)
Local_M_3: Nequi (Colombia)
Local_M_4: Daviplata (Colombia)
Local_M_5: Boleto (Brazil)
Local_M_6: Open Banking (UK/EU)
Local_M_7: SEPA Instant (EU)
Local_M_8: iDEAL (Netherlands)
Local_M_9: Bancontact (Belgium)
Local_M_10: UPI (India)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each card transaction and currency conversion through the optimal processor by country, amount, and speed. At $10B+ annualized volume across 4 LatAm markets, shifting even 1% of failed transactions to a secondary acquirer recovers significant volume. Smart Routing delivers +3 to 10% auth uplift on cross-border card spend.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor Paymentology dependency. When Paymentology declines a card transaction in Mexico or Brazil, Yuno reroutes instantly through an alternate acquirer. Up to 50% recovery on failed transactions, keeping the fee-free Mastercard experience intact for 2M+ users across 4 countries.
Desc_Yuno_Cap3: Extends ARQ beyond card-only spend: OXXO cash deposits in Mexico, Mercado Pago wallets across LatAm, Nequi and Daviplata in Colombia, Boleto in Brazil, Open Banking and SEPA Instant for European senders. One API, 1,000+ payment methods. Opens EUR/GBP corridors without per-market builds.
Desc_Yuno_Cap4: One dashboard unifying Paymentology card processing, Mastercard network, Circle USDC stablecoin flows, SPEI/Pix/CVU/PSE local rails, and Apple Pay/Google Pay tokenization into a single reconciliation layer. Real-time cross-border monitoring across 4 countries, NOVA fraud engine with 75% fewer false positives across card and stablecoin rails.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**DolarApp (ARQ) at a glance:**
- Founded: 2021 by Fernando Terres (CEO), Zach Garman (CPO), Alvaro Correa (COO)
- Founders previously part of Revolut executive team
- Rebrand: DolarApp rebranded to ARQ in March 2026
- Funding: $70M raised in March 2026 from Sequoia Capital, Founders Fund, and Kaszek
- Revenue: $7.5M (2024 disclosed); growing rapidly with $10B+ annualized transaction volume
- Users: 2M+ customers across Latin America
- Employees: ~50 (as of 2024, expanding post-funding)
- Offices: New York, Mexico City, Buenos Aires, Sao Paulo, Bogota, Krakow, London
- Y Combinator alumnus

**Markets:**
- Mexico (primary): SPEI/CLABE deposits, MXN conversion
- Argentina: CVU/Alias deposits, ARS conversion
- Brazil: Pix deposits, BRL conversion
- Colombia: PSE deposits, COP conversion
- All markets: USD (USDC) and EUR (EURc) digital accounts

**Product suite:**
- Digital Dollar Account: USDC-backed, instant peso-to-dollar conversion
- Digital Euro Account: EURc-backed, EUR savings and conversion
- Mastercard Card: Physical and virtual, zero FX fees, up to 4% cashback
- Earnings Account: Up to 4.5% annual yield on savings
- Investments: Stocks and ETFs, zero commission
- Cross-border transfers: Send/receive from U.S. and Europe
- Business accounts: B2B cross-border payment solutions

**Confirmed PSPs / Payment Rails:**
- Paymentology: Card issuer-processor powering all Mastercard transactions (virtual + physical)
- Mastercard: Card network for international spend
- Circle: USDC stablecoin infrastructure (peso-to-USDC and back)
- SPEI: Mexican instant payment system (deposits/withdrawals)
- Pix: Brazilian instant payment system (deposits/withdrawals)
- CVU: Argentine instant transfer system (deposits/withdrawals)
- PSE: Colombian electronic payment system (deposits/withdrawals)
- Apple Pay: Supported via Paymentology tokenization
- Google Pay: Supported via Paymentology tokenization
- 3D Secure: Enabled through Paymentology
- No payment orchestrator detected
- No multi-acquirer routing identified

**Paymentology partnership details:**
- Provides virtual and physical Mastercard card processing
- 3DSecure technology for online transactions
- Apple Pay and Google Pay tokenization
- Scalable card payment program across all 4 LatAm markets
- DolarApp was an early Paymentology client in the region

**Stablecoin infrastructure:**
- USDC (Circle): Core value store, pegged 1:1 to USD
- EURc (Circle): Euro-denominated stablecoin for EUR savings
- Conversion: Instant peso/real/peso colombiano to USDC and back
- On-chain: Stablecoin balances held on blockchain
- Offramp: USDC converted to local currency via SPEI/Pix/CVU/PSE

**$70M funding use (March 2026):**
1. Rebrand from DolarApp to ARQ
2. Team expansion (hiring across all offices)
3. New product verticals: wealth management, local currency high-yield accounts, lending
4. Geographic expansion beyond current 4 markets

**Key Meeting Angles:**
1. **$10B+ volume, single card processor** | Paymentology handles all card transactions with no failover; orchestration adds resilience
2. **Sequoia/Founders Fund backing** | $70M raise signals growth ambition; payment infrastructure needs to scale with it
3. **Card-only international spend** | No bank-to-bank, QR, or wallet-to-wallet cross-border options limits use cases
4. **No EUR/GBP corridors natively** | European freelancers/employers paying LatAm workers is a massive untapped market
5. **Stablecoin offramp single point of failure** | One bridge per country means USDC-to-local conversion has no redundancy
6. **Revolut alumni founding team** | Founders understand payment orchestration from Revolut's multi-PSP architecture
7. **Lending and wealth management expansion** | New product verticals announced with funding require robust payment infrastructure
8. **OXXO and Mercado Pago gaps** | Cash and wallet payment methods in Mexico and LatAm would dramatically expand user base beyond banked population

**Sources:**
- [ARQ $70M Raise (Bloomberg)](https://www.bloomberg.com/news/articles/2026-03-03/sequoia-founders-fund-back-70-million-raise-for-latam-s-arq)
- [ARQ Raises $70M (VentureBurn)](https://ventureburn.com/arq-raises-70m-stablecoin-banking-latin-america/)
- [DolarApp Rebrands to ARQ (LatamRepublic)](https://www.latamrepublic.com/dolarapp-rebrands-as-arq-after-securing-us-70-m-from-sequoia-and-founders-fund/)
- [ARQ $70M Raise (AInvest)](https://www.ainvest.com/news/stablecoin-finance-app-arq-completes-70-million-funding-investment-sequoia-capital-founders-fund-2603-86/)
- [ARQ on Y Combinator](https://www.ycombinator.com/companies/arq)
- [Paymentology x DolarApp Partnership (Paymentology)](https://www.paymentology.com/newsroom/paymentology-and-dolarapp-enable-millions-of-mexicans-to-buy-anywhere-in-usd-fee-free)
- [Paymentology Client Story: DolarApp (Paymentology)](https://www.paymentology.com/client-story-dolarapp)
- [DolarApp Card Processing (IBS Intelligence)](https://ibsintelligence.com/ibsi-news/dolarapp-selects-paymentology-for-card-processing-services/)
- [Buy USDC on DolarApp (Circle)](https://www.usdc.com/learn/how-to-buy-usdc-dolarapp)
- [DolarApp Revenue $7.5M (GetLatka)](https://getlatka.com/companies/dolarapp.com)
- [ARQ Crunchbase Profile](https://www.crunchbase.com/organization/dolarapp)
- [ARQ Official Website](https://www.arqfinance.com/en-MX)
- [DolarApp Official Website](https://www.dolarapp.com/en-MX)
- [ARQ Best Cross-Border Fintech 2026 (ARQ Blog)](https://www.arqfinance.com/en-AR/blog/your-money/mejores-plataformas-fintech-pagos-cross-border-2026)
- [ARQ Rebrand Announcement (ARQ Help Center)](https://help.arqfinance.com/en/articles/13897054-meet-our-new-brand-dolarapp-is-now-arq)
- [DolarApp Logo (Brandfetch)](https://brandfetch.com/dolarapp.com)
