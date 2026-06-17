# NOMAD FINTECH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Nomad Fintech
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idh4I3LNwi/idKKVfIXhE.svg
Nombre merchant: Nomad Fintech

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: FX Spread Margin Erosion
Tittle_Pain Point_2: Single-Acquirer Dependency
Tittle_Pain Point_3: No Routing Optimization
Tittle_Pain Point_4: Limited Payout Rails
Tittle_Pain Point_5: Chargeback Blind Spot

Desc_Pain Point_1: Nomad charges a 2% FX spread on every BRL to USD conversion plus IOF taxes. With 3.5M+ users moving money cross-border, even marginal acquirer-level FX optimization would save millions. No orchestration layer exists to route through the lowest-cost corridor.
Desc_Pain Point_2: Nomad relies on Community Federal Savings Bank for card issuance and Ouribank for FX. If either partner experiences downtime or rate degradation, the entire transaction flow stalls with no automated failover to an alternate acquirer or banking rail.
Desc_Pain Point_3: All remittance and card transactions flow through fixed partner rails with no dynamic routing based on success rates, cost, or corridor performance. There is no real-time decisioning layer optimizing which acquirer or FX provider handles each transaction.
Desc_Pain Point_4: Nomad supports Pix for inbound BRL funding but lacks diversified payout methods across LATAM. No SPEI for Mexico-bound transfers, no local wallet integrations, limiting the platform to a Brazil-US corridor when users travel across the region.
Desc_Pain Point_5: As a program manager (not a bank), Nomad has limited visibility into dispute resolution workflows at Community Federal Savings Bank. Chargebacks on the Visa debit card flow through the partner bank, creating reconciliation delays and cost opacity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Community Federal Savings Bank (Card Issuer)
PSP_2: Ouribank S.A. (FX/Remittance)
PSP_3: Visa (Card Network)
PSP_4: DriveWealth (Investment Clearing)
PSP_5: Apex Clearing (Investment Clearing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SPEI
Local_M_2: OXXO
Local_M_3: CoDi
Local_M_4: Nequi
Local_M_5: PSE (Colombia)
Local_M_6: Mercado Pago Wallet
Local_M_7: RappiPay
Local_M_8: Yape (Peru)
Local_M_9: SEPA Instant
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every cross-border transaction to the optimal acquirer and FX corridor based on real-time cost, approval rate, and corridor performance. With 3.5M+ users and 2% spreads on every conversion, a 3-10% improvement in routing efficiency translates to millions in recovered margin annually.
Desc_Yuno_Cap2: When Ouribank or Community Federal Savings Bank experiences degradation, Yuno cascades to an alternate acquirer or banking rail in milliseconds. Recovers up to 50% of failed transactions, eliminating single-partner dependency that puts the entire remittance flow at risk.
Desc_Yuno_Cap3: Expand beyond the Brazil-US corridor with one API integration. SPEI and OXXO for Mexico, Nequi for Colombia, Yape for Peru, Mercado Pago across LATAM. 1,000+ payment methods unlock regional expansion without building each integration from scratch.
Desc_Yuno_Cap4: Consolidate Community Federal Savings Bank, Ouribank, Visa, and all clearing partners into a single dashboard. Real-time auth rate monitoring, centralized reconciliation, and NOVA anomaly detection (75% fraud reduction) replace fragmented partner-by-partner management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Nomad Fintech at a glance:**
- Founded: 2019 in Sao Paulo, Brazil
- CEO: Lucas Vargas (Co-Founder)
- Founders: Eduardo Haber, Marcos Nader, Gabriel Pinto
- HQ: Sao Paulo, Brazil; US entity: Nomad Fintech, Inc. (Menlo Park, CA)
- Total Funding: $113M across 3 rounds (Series B: $61M in Aug 2023 led by Tiger Global)
- Valuation: R$1.8 billion (~$361M)
- Users: 3.5M+ Brazilians
- Employees: ~203 (as of mid-2024)
- Products: US dollar bank account (FDIC insured up to $250K), Visa debit card, international investments, remittances, Explorer credit card
- Key investors: Tiger Global, Stripes, Monashees, Spark Capital, Propel Ventures, Globo Ventures, Abstract Ventures
- Harvard Business School case study: "Nomad: A License to Bank" (March 2024)

**Confirmed Financial Partners:**
- Community Federal Savings Bank: Issues the Nomad Visa Debit Card, provides FDIC insurance
- Ouribank S.A. Banco Multiplo: Handles foreign exchange transactions and BRL-USD fund transfers
- Visa: Card network for debit and credit cards
- DriveWealth LLC: Holds individual investment accounts (FINRA/SIPC member)
- Apex Clearing Corporation: Alternative investment account custodian (FINRA/SIPC member)
- Nomad Investment Services, Inc (NIS): In-house US broker-dealer (SEC registered, FINRA/SIPC)
- Global DTVM: Brazilian securities distributor partner
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, or Yuno)

**Fee Structure & Pain Points:**
- BRL to USD transfers: 1.1% IOF tax + 2% operational spread per transaction
- USD to BRL transfers: 0.38% IOF + 2% spread + $10 flat fee per transaction
- Explorer Credit Card: 3.5% IOF + up to 4% operational rate on international transactions
- Wise comparison: Nomad's FX spreads are higher than competitors like Wise and C6 Bank
- Program manager model: Nomad does not hold a banking license, depends entirely on partner bank (CFSB) for all regulated activities

**Competitive Landscape:**
- Direct competitors: Wise, C6 Bank, Remessa Online, BS2, Revolut
- Differentiation: Full US bank account (not just multi-currency wallet), FDIC insurance, US investment access
- Weakness: Higher fees than Wise, limited to Brazil-US corridor, no LATAM-wide expansion yet

**Top Market Gap Analysis:**

MARKET 1: Brazil (home market, 3.5M+ users)
  Offer: Pix for inbound BRL funding, bank transfer
  Missing: Boleto for account funding, parcelamento (installments)
  Relies on Pix and TED only; no alternative funding methods

MARKET 2: United States (destination market)
  Offer: Visa debit card, ACH via partner bank
  Missing: Venmo, Cash App Pay, Zelle integration
  Limited to traditional card and bank transfer rails

MARKET 3: Mexico (potential expansion)
  Offer: None currently
  Missing: SPEI, OXXO, CoDi
  Massive Brazilian diaspora in Mexico; no local payment rail support

MARKET 4: Colombia (potential expansion)
  Offer: None currently
  Missing: PSE, Nequi, Daviplata
  Growing corridor for Brazilian travelers and remote workers

MARKET 5: Europe (travel destination)
  Offer: Visa card acceptance
  Missing: SEPA Instant, iDEAL, Bancontact
  Nomad card works abroad but no local European payment optimization

**Key meeting angles:**
1. **Program manager vulnerability**: Nomad depends on CFSB and Ouribank with zero failover. Orchestration adds resilience without changing banking partners.
2. **FX margin optimization**: 2% spread on every transaction across 3.5M users. Smart routing to optimal FX corridors directly improves unit economics.
3. **LATAM expansion enabler**: Nomad is Brazil-US only. Adding SPEI, OXXO, Nequi, and Yape via one API unlocks multi-corridor expansion without per-country integrations.
4. **Scale opportunity**: $113M raised, HBS case study, 3.5M users. This is a high-growth fintech that will outgrow its current partner-dependent infrastructure.
5. **Competitor pressure**: Wise, C6 Bank, and Revolut all offer lower fees. Routing optimization helps Nomad compress spreads while protecting margins.

**Sources:**
- [Nomad Official Website](https://www.nomadglobal.com/en)
- [Nomad About Us](https://www.nomadglobal.com/en/about-us)
- [Nomad Legal/Privacy](https://www.nomadglobal.com/en/legal)
- [Nomad Crunchbase Profile](https://www.crunchbase.com/organization/nomad-deb4)
- [Nomad Tracxn Profile](https://tracxn.com/d/companies/nomad/__mxkV1MQ5mH1xoM9Tl0SIHeFCFmXiGAI-I8UmRuyVQ9Y)
- [Nomad Series B: $61M Funding](https://fintech.global/2023/09/22/nomad-secures-61m-in-largest-investment-for-latam-financial-startup-this-year/)
- [Nomad $32M Series A](https://www.bloomberglinea.com/2022/05/16/nomad-a-us-fintech-for-brazilian-users-raises-32m/)
- [Nomad HBS Case Study](https://www.hbs.edu/faculty/Pages/item.aspx?num=65677)
- [Wise: Nomad Bank Review](https://wise.com/us/blog/nomad-bank-account)
- [Nomad Google Play](https://play.google.com/store/apps/details?id=com.nomadfintech.bank.app.android)
- [Brandfetch: Nomad Logo](https://brandfetch.com/nomadglobal.com)
- [Stripes: Nomad Investment](https://www.stripes.co/investments/nomad)
- [LATAM Fintech: Nomad Series A](https://www.latamfintech.co/articles/with-us-20-million-series-a-funding-round-nomad-aims-to-be-brazilians-digital-bank-in-the-u-s)
