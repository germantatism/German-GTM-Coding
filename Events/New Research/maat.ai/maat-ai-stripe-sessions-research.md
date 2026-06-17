# MAAT.AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: maat.ai
=======================================

Logo: https://cdn.prod.website-files.com/6685a24d657ba36d75fcbee9/6685c10a5fa647954106a881_Logo%20Maatai%20Big.svg
Nombre merchant: maat.ai

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Bottleneck
Tittle_Pain Point_2: LATAM FX Conversion Loss
Tittle_Pain Point_3: Cash Payment Gaps
Tittle_Pain Point_4: B2B Billing Complexity
Tittle_Pain Point_5: Chargeback Fraud Risk

Desc_Pain Point_1: All billing likely flows through one gateway. Any outage or rate hike blocks 100% of recurring revenue from verification clients in Mexico, Canada, LATAM.
Desc_Pain Point_2: Clients in Mexico, Colombia, Brazil, and Canada pay cross-border card fees on every invoice. USD deals billed to MXN clients create FX leakage per transaction.
Desc_Pain Point_3: Many marketplace users in Mexico lack bank accounts. Without OXXO or SPEI, the B2C marketplace launched in 2023 cannot reach 50M+ unbanked Mexican adults.
Desc_Pain Point_4: Per-API-call pricing varies by product (Facial Match, Dextract, Maatch Alive). Mixed enterprise, pay-as-you-go, and marketplace billing adds overhead.
Desc_Pain Point_5: Identity verification SaaS attracts friendly fraud and card-not-present disputes. With ~10 employees, chargeback management consumes disproportionate bandwidth.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (likely, SaaS billing standard)
PSP_2: Conekta (Mexico local acquiring)
PSP_3: PayPal (international fallback)
PSP_4: Not confirmed

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: SPEI
Local_M_3: Boleto
Local_M_4: PSE
Local_M_5: Nequi
Local_M_6: Pix
Local_M_7: CoDi
Local_M_8: Mercado Pago
Local_M_9: Interac (Canada)
Local_M_10: PagoEfectivo

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each transaction to the optimal acquirer by country, currency, and card BIN. For cross-border SaaS billing across Mexico, Canada, and LATAM, smart routing uplifts auth rates 3-10%. InDrive achieved 90% approval via Yuno routing.
Desc_Yuno_Cap2: Automatic cascade ensures zero downtime for subscription renewals. When the primary gateway declines a recurring B2B invoice or marketplace charge, Yuno reroutes to the next acquirer in milliseconds. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates OXXO and SPEI in Mexico, Boleto and Pix in Brazil, PSE and Nequi in Colombia, and Interac in Canada through a single integration. Enables the B2C marketplace to reach unbanked users and enterprise clients preferring local bank transfers. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard consolidating all PSPs, reconciling API billing, enterprise contracts, and marketplace fees across currencies. NOVA AI recovers 75% of failed payments via WhatsApp and phone outreach, critical for a 10-person team.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**maat.ai at a glance:**
- Founded: 2018, HQ: Cuauhtemoc, Mexico City, Mexico
- Founders: Alain Viallix (CEO), Jose Samuel Najar Villagomez, Alexei Stanislawski, Brian Aguirre
- Employees: ~10
- Formerly known as Mati; rebranded to maat.ai
- Valuation: ~$6M (last known)
- Total funding: ~$1M confirmed (investors: Bevos Technologies, CHM Holdings, Holt Xchange, Factory A, Village Capital)
- Raised $13.5M Series A under the Mati brand (Insight Partners, Tribe Capital, Spero Ventures)
- Offices: Mexico City, Montreal, Vancouver
- Revenue: not publicly disclosed

**Products and services:**
- ID PAL: rapid identity verification with background checks
- FACEMATCH: facial recognition comparing photos to identity documents
- MAATCH ALIVE: real-time biometric validation using 27 facial reference points
- DEXTRACT: official document authentication and security validation
- DEXMAATCH: combined facial recognition and document validation
- B2C Marketplace: launched 2023, verified identity community for health, employment, education, entertainment, public services, finance
- API/SDK integration with claimed one-week implementation timelines

**Technology stack:**
- Blockchain, cloud computing, AI, biometrics, cryptography
- End-to-end encryption and role-based access controls
- RegTech and SaaS delivery model

**Confirmed PSPs:**
- No PSP publicly confirmed
- As a Mexican SaaS platform, likely candidates include Stripe, Conekta, or Mercado Pago for local acquiring
- PayPal probable for international B2B billing
- No payment orchestrator detected

**Market context (LATAM identity verification):**
- Online fraud in LATAM expected to exceed $20B by 2028
- 1 in 5 online transactions in LATAM falsely flagged as fraud (highest globally)
- Mexico's Fintech Law mandates digital onboarding and KYC/AML standards
- Identity theft and synthetic identities are among fastest-growing financial crimes in Mexico
- 50M+ unbanked adults in Mexico lack traditional payment access
- Competitors: Incode, Veriff, Sumsub, Trulioo, FacePhi, IDmission

**Top market gap analysis:**

MARKET 1: Mexico (primary market)
  Likely offer: credit/debit cards, bank transfer
  Missing: OXXO (cash, 60%+ population reach), SPEI (instant bank transfer), CoDi (QR-based)
  Impact: B2C marketplace cannot monetize unbanked users without cash-based payment options.

MARKET 2: Canada (office in Montreal & Vancouver)
  Likely offer: credit/debit cards
  Missing: Interac e-Transfer (dominant Canadian payment method)
  Impact: Canadian enterprise clients expect Interac; absence adds friction to B2B billing.

MARKET 3: Colombia (LATAM expansion target)
  Likely offer: credit/debit cards
  Missing: PSE (bank transfer), Nequi (mobile wallet), Efecty (cash)
  Impact: PSE covers 85%+ of Colombian online banking; missing it blocks enterprise adoption.

MARKET 4: Brazil (LATAM expansion target)
  Likely offer: credit/debit cards
  Missing: Pix (instant payment), Boleto (cash voucher)
  Impact: Pix processes 50B+ transactions/year in Brazil; essential for any LATAM expansion.

MARKET 5: Peru (LATAM expansion target)
  Likely offer: credit/debit cards
  Missing: PagoEfectivo (cash/bank), Yape (mobile wallet)
  Impact: Cash-based methods reach 60%+ of Peruvian population.

**Key meeting angles:**
1. **Tiny team, huge operational leverage needed** | 10 employees cannot dedicate headcount to payment ops, collections, or chargeback management; Yuno automates all three
2. **B2C marketplace launched 2023 needs local methods** | Without OXXO, SPEI, and CoDi, the identity marketplace cannot reach Mexico's 50M+ unbanked adults
3. **Cross-border SaaS billing across 3 countries** | Mexico, Canada, and expanding LATAM means FX leakage on every invoice without local acquiring
4. **High-risk vertical (identity/KYC)** | Fraud and chargeback rates are elevated in verification SaaS; smart routing and failover reduce false declines
5. **$13.5M Series A funding** | Capital available to invest in payment infrastructure that supports growth
6. **Competitive pressure from well-funded rivals** | Incode ($220M+), Veriff ($100M+), Sumsub ($65M+) all have sophisticated payment stacks; maat.ai needs parity
7. **Stripe relationship preserved** | Yuno sits on top of existing PSPs, not replacing them; adds routing intelligence without migration risk

**Sources:**
- [maat.ai Official Website](https://www.maatai.com/)
- [maat.ai LinkedIn](https://www.linkedin.com/company/maat-ai/)
- [maat.ai Crunchbase](https://www.crunchbase.com/organization/maat-ai)
- [Mati TechCrunch: Reshapes Online Trust](https://techcrunch.com/2020/11/17/mati-reshapes-online-trust-and-reputation-with-a-plaid-like-api/)
- [Mati TechCrunch: Spero Ventures Invests](https://techcrunch.com/2020/05/26/omidyar-backed-spero-ventures-invests-in-mexico-citys-mati-a-startup-pitching-id-verification/)
- [LexLatin: maat.ai Investment](https://lexlatin.com/noticias/fintech-mexicana-maatai-recibe-inversion-desarrollo-nuevos-productos)
- [Legal Paradox: maat.ai Fintech Profile](https://www.legalparadox.com/fintech/maatai)
- [America Digital: maat.ai Marketplace Launch](https://mx.america-digital.com/digital-identity-maat-ai-launches-new-marketplace/?lang=en)
- [Holt Xchange: maat.ai](https://holtxchange.com/maat-ai/)
- [CBInsights: maat.ai](https://www.cbinsights.com/company/maatai)
- [MIT Solve: Mati](https://solve.mit.edu/solutions/5689)
- [Sumsub: Digital Identity in LATAM](https://sumsub.com/blog/digital-identity-id-verification-latin-america/)
- [Signzy: Best KYC Platforms Mexico 2026](https://www.signzy.com/blogs/best-kyc-verification-platforms-mexico)
