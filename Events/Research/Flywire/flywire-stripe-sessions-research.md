# FLYWIRE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Flywire
=======================================

Logo: https://companieslogo.com/img/orig/FLYW-46489b12.png
Nombre merchant: Flywire

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Visa Policy Revenue Risk
Tittle_Pain Point_2: Banking Partner Lockup
Tittle_Pain Point_3: Travel Payment Friction
Tittle_Pain Point_4: FX Markup Transparency
Tittle_Pain Point_5: Healthcare A/R Delays

Desc_Pain Point_1: Canada and Australia visa policy changes caused a projected 30% revenue decline in those education markets in 2025, triggering 10% workforce cuts. Education is 79% of revenue. Overconcentration in one vertical with government-dependent demand creates structural volatility.
Desc_Pain Point_2: Citibank is the primary banking partner for receivables, FX, global account structures, and outgoing payments. A 15+ year partnership creates deep dependency. No documented multi-bank routing or failover exists if Citi experiences processing issues on any corridor.
Desc_Pain Point_3: 86% of ultra-luxury travelers report payment pain points. Top issues: security concerns (72%), unexpected bank fees, confusing exchange rates, and credit card handling between parties. Sertifi acquisition ($330M) addresses software, but payment rail optimization remains limited.
Desc_Pain Point_4: Payers see converted amounts in local currency, but FX margins are embedded in the rate. User reviews cite "unexpected additional debits" and "confusing currency options." Without transparent multi-source FX routing, Flywire absorbs margin pressure from both clients and payers.
Desc_Pain Point_5: Healthcare payment processing handles in-person, online, and phone payments, but legacy A/R workflows slow cash collection. Hospitals need real-time payment confirmation and multi-channel reconciliation. Current gateway/processor/acquirer unification is partial.

SLIDE 1: PSP TOPOLOGY

PSP_1: Citibank (banking, FX, receivables)
PSP_2: Visa / Mastercard (card networks)
PSP_3: American Express (card network)
PSP_4: Discover Global Network (card network)
PSP_5: Sertifi (travel payment software)
PSP_6: Local banking partners (240 countries)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: Alipay (China)
Local_M_4: WeChat Pay (China)
Local_M_5: OXXO (Mexico)
Local_M_6: SPEI (Mexico)
Local_M_7: Nequi (Colombia)
Local_M_8: GCash (Philippines)
Local_M_9: BLIK (Poland)
Local_M_10: Open Banking (UK/EU)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each tuition, healthcare, and travel payment through the optimal banking partner and FX source by corridor, amount, and speed. At $37.5B+ annual payment volume across 240 countries, selecting the best rate and processor per transaction recovers margin on every cross-border payment. Smart Routing delivers +3 to 10% auth uplift.
Desc_Yuno_Cap2: Automatic cascade eliminates Citibank single-partner dependency. When Citi's corridor fails or FX rate is uncompetitive, Yuno reroutes to the next best banking partner instantly. Up to 50% recovery on failed transactions, protecting tuition payment deadlines where delays mean student enrollment risk.
Desc_Yuno_Cap3: Activates the local payment rails students and travelers actually use: UPI for Indian students (largest int'l student population), Pix for Brazilians, Alipay/WeChat Pay for Chinese students, OXXO/SPEI for Mexicans, GCash for Filipinos, Open Banking for UK/EU payers. One API, 1,000+ methods, no per-corridor builds.
Desc_Yuno_Cap4: One dashboard unifying Citibank receivables, card network processing (Visa, Mastercard, Amex, Discover), Sertifi travel software, healthcare A/R, and 240-country banking network into a single reconciliation layer. Real-time payment monitoring across education, healthcare, and travel verticals. NOVA fraud engine with 75% fewer false positives.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Flywire at a glance:**
- Founded: 2009 by Iker Marcaide in Boston, MA (originally as peerTransfer)
- Public: FLYW on Nasdaq (IPO May 2021)
- Revenue: $623M FY2025; Q4 2025: $157.5M (+34% YoY)
- Total Payment Volume: $37.5B+ FY2025 (Q1: $8.4B, Q2: $5.9B, Q3: $13.9B, Q4: $9.3B)
- Clients: 750+ new customer wins in 2025 across 52 countries, 4,000+ total clients
- New Sales Pipeline: +35% YoY growth in 2025
- Revenue Churn: Sub-1% in Education and Travel verticals
- Employees: ~1,400
- Countries: 240+ (payments), 140+ currencies
- Adjusted EBITDA: Growing, with 150 to 350 bps margin expansion guided for 2026

**2026 Guidance:**
- Revenue (less ancillary services): 15% to 21% growth (FX neutral)
- Adjusted EBITDA margin: 150 to 350 bps expansion
- Q1 2026 earnings: Scheduled May 5, 2026

**Verticals and revenue mix:**
- Education: ~79% of revenue. U.S. higher education, international student payments, study abroad
- Healthcare: Hospital/health system payment processing (in-person, online, phone)
- Travel: Ultra-luxury, hospitality (accelerated by Sertifi acquisition)
- B2B: Cross-border business payments

**Key acquisitions:**
- Sertifi (Feb 2025): $330M. Hospitality payment software, 20,000+ hotel locations. $35 to $40M annual revenue
- StudyLink (Nov 2024): $38.8M. Australian higher education payments
- WPM (Dec 2021): UK education payments
- Cohort Go (Jul 2022): Australian student financial services

**Confirmed PSPs / Payment Rails:**
- Citibank: Primary banking partner for 15+ years. Receivables, FX, global account structures, outgoing payments. Named 2025 Partner of the Year
- Visa: Card acceptance for tuition, healthcare, travel payments
- Mastercard: Card acceptance across verticals
- American Express: Card acceptance (Platinum Sponsor at Flywire Fusion)
- Discover Global Network: Card acceptance (Silver Sponsor)
- Sertifi: Travel/hospitality payment software (now owned by Flywire)
- Local banking partners: Network across 240 countries for settlement
- Bank transfers: SEPA, wire transfers, local bank payments per jurisdiction
- E-wallets: Select markets
- No payment orchestrator detected
- No multi-bank routing identified

**Payer payment methods:**
- International credit/debit cards (Visa, MC, Amex, Discover)
- Bank transfers (SEPA, wire, local bank transfer)
- Online bill payment
- E-wallets (select markets)
- Payment options vary by country/corridor

**Pain points detail:**

1. **Visa policy vulnerability**: Canada announced international student enrollment caps in 2024/2025. Australia tightened visa rules. Both caused projected 30% revenue decline in those education markets, triggering 10% workforce reduction. Single-vertical concentration amplifies regulatory risk.

2. **Citibank concentration**: 15-year partnership means deep integration but also deep dependency. FX rates, receivables processing, and global accounts all flow through Citi. No documented alternative banking partners for failover if Citi has corridor-specific issues.

3. **Travel payment pain**: Sertifi acquisition adds software layer for hospitality, but payer-side experience still has friction. 86% of travelers report payment pain points. Security (72%), hidden fees, and FX confusion are top complaints. Payment rail optimization vs. just software integration is the gap.

4. **FX transparency pressure**: Flywire embeds FX margin in conversion rates shown to payers. As competitors (Wise, Karbon) offer real exchange rates with transparent markups, Flywire faces margin compression. Smart routing across multiple FX providers would maintain competitive rates.

5. **Healthcare A/R complexity**: Healthcare combines gateway, processor, and acquirer functions, but patient payment fragmentation (in-person, online, phone, third-party insurance) creates reconciliation challenges. Real-time payment confirmation across channels remains an operational gap.

**Key Meeting Angles:**
1. **$623M revenue, Citibank-dependent** | 15-year banking partnership handles FX, receivables, and settlement with no multi-bank routing
2. **79% education revenue, visa policy risk** | Canada/Australia disruptions prove the danger of single-vertical concentration
3. **240 countries, limited local APMs** | Indian students (UPI), Chinese students (Alipay), Brazilian students (Pix) lack native payment options
4. **$330M Sertifi bet on travel** | Hospitality software acquired, but payment rail optimization across 20,000 hotels is the next frontier
5. **86% of travelers report payment friction** | Smart routing and local APMs directly address the #1 payer complaint
6. **FX margin under pressure** | Multi-source FX routing maintains competitive rates vs. Wise and transparent-fee competitors
7. **Healthcare A/R modernization** | Unified orchestration across in-person, online, and phone payments accelerates cash collection
8. **750 new clients in 2025** | Rapid client acquisition demands scalable payment infrastructure across all verticals

**Sources:**
- [Flywire Q4 & FY2025 Results (Flywire)](https://www.flywire.com/news/flywire-reports-fourth-quarter-and-fiscal-year-2025-financial-results)
- [Flywire FY2025 Results (GlobeNewsWire)](https://www.globenewswire.com/news-release/2026/02/24/3244013/0/en/Flywire-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results.html)
- [Flywire Q1 2025 Results (Investor Relations)](https://ir.flywire.com/news-releases/news-release-details/flywire-reports-first-quarter-2025-financial-results/)
- [Flywire Q3 2025 Results (GlobeNewsWire)](https://www.globenewswire.com/news-release/2025/11/04/3180829/0/en/Flywire-Reports-Third-Quarter-2025-Financial-Results.html)
- [Flywire Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/FLYW/flywire/revenue)
- [Flywire Acquires Sertifi (Flywire)](https://www.flywire.com/news/flywire-acquires-sertifi-to-accelerate-travel-business)
- [Flywire Sertifi $330M (PYMNTS)](https://www.pymnts.com/acquisitions/2025/flywire-pays-330-million-dollars-hospitality-payments-platform-sertifi/)
- [Flywire StudyLink Acquisition (Payments Dive)](https://www.paymentsdive.com/news/flywire-scoops-up-australian-firm-studylink-education-payments-acquisition/699364/)
- [Flywire WPM Acquisition (Flywire)](https://www.flywire.com/news/flywire-acquires-wpm)
- [Flywire Cross-Border Technology (FinTech Magazine)](https://fintechmagazine.com/company-reports/flywire-how-tech-powers-frictionless-cross-border-payments)
- [Citibank x Flywire Partnership (Partnerbase)](https://www.partnerbase.com/citibank/flywire)
- [Flywire Payment Compliance (Flywire)](https://www.flywire.com/resources/how-to-solve-payment-and-data-compliance-challenges-across-complex-industries)
- [Flywire 2026 Payment Predictions (Flywire)](https://www.flywire.com/resources/2026-payment-predictions)
- [Flywire International Payments 101 (Flywire)](https://www.flywire.com/resources/international-payments-101)
- [Flywire Platform (Flywire)](https://www.flywire.com/platform)
- [Flywire Global Payment Network (Flywire)](https://www.flywire.com/platform/global-payment-network)
- [Flywire Healthcare Solutions (Flywire)](https://www.flywire.com/industries/healthcare/solution/payment-services)
- [Flywire G2 Reviews (G2)](https://www.g2.com/products/flywire/reviews)
- [Flywire Trustpilot Reviews (Trustpilot)](https://www.trustpilot.com/review/www.flywire.com)
- [Flywire Logo (CompaniesLogo)](https://companieslogo.com/flywire/logo/)
