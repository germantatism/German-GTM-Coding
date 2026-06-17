# HYATT HOTELS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: HYATT HOTELS
=======================================

Logo: https://brandfetch.com/hyatt.com
Nombre merchant: HYATT HOTELS

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Legacy Payment Stack
Tittle_Pain Point_2: Cross Border Auth Losses
Tittle_Pain Point_3: Chargeback & Fraud Burden
Tittle_Pain Point_4: Fragmented Property Pmts
Tittle_Pain Point_5: APM Gap in Growth Markets

Desc_Pain Point_1: Hyatt's payment infrastructure relies on CyberSource (Visa-owned gateway) through Sertifi for contract and event payments across 1,500+ properties. The core PMS is migrating from Oracle Opera V5 to Oracle OPERA Cloud, but payment processing remains tied to legacy gateway architecture. There is no multi-acquirer routing, no real time failover, and no intelligent transaction optimization across the global portfolio.
Desc_Pain Point_2: Hyatt operates 1,500+ properties in 83 countries, serving 63 million World of Hyatt loyalty members booking cross border. A guest in Japan booking a Park Hyatt in Paris processes through a single acquirer path with no BIN-level optimization. Cross-border hotel transactions carry higher decline rates than domestic, and each failed authorization means a lost reservation worth hundreds or thousands of dollars.
Desc_Pain Point_3: The hospitality industry accounts for 55% of all card fraud in the US according to the American Hotel and Lodging Association. Hyatt's 1,500+ properties face $150B in industry-wide annual fraud losses. Friendly fraud represents 71% of chargebacks labeled as fraudulent. Without unified fraud scoring across all properties and PSPs, each hotel fights fraud independently with inconsistent rules and tools.
Desc_Pain Point_4: Hyatt's portfolio spans 37 brands across 83 countries. Each property may process payments through different local acquirers, bank relationships, and regional PSPs depending on the market. There is no single orchestration layer unifying payment data across the global portfolio. Settlement, reconciliation, and reporting happen property by property, not at the enterprise level.
Desc_Pain Point_5: Hyatt is expanding aggressively in Asia Pacific, the Middle East, and Latin America with new properties. Guests in these regions expect local payment methods at booking: Pix in Brazil, UPI in India, Mada in Saudi Arabia, GrabPay in SEA, WeChat Pay and Alipay in China. Hyatt.com accepts Visa, Mastercard, Amex, Discover, and JCB, but offers zero local alternative payment methods at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: CyberSource/Visa (primary gateway via Sertifi)
PSP_2: Oracle Payments (OPERA Cloud PMS integration)
PSP_3: Onyx CenterSource/GroupPay (M&E commissions, 700+ properties)
PSP_4: Local bank acquirers (per property, per country)
PSP_5: Sabre SynXis (CRS booking engine)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: Alipay (China)
Local_M_3: WeChat Pay (China)
Local_M_4: UPI (India)
Local_M_5: Mada (Saudi Arabia)
Local_M_6: GrabPay (SEA)
Local_M_7: Klarna (EU/US BNPL)
Local_M_8: iDEAL (Netherlands)
Local_M_9: SEPA Direct Debit (EU)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover Cascade Retries
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Enterprise Orchestration

Desc_Yuno_Cap1: Route every reservation payment to the optimal acquirer by guest card BIN, booking currency, and property country in real time. With 1,500+ properties in 83 countries processing cross-border bookings from 63M loyalty members, even a 2% authorization uplift translates to millions in recovered room revenue. Smart Routing selects the best acquirer per transaction instead of routing all payments through CyberSource's single path.
Desc_Yuno_Cap2: When CyberSource declines a cross-border card or a local acquirer returns a soft decline, Yuno cascades to the next best processor in milliseconds. A guest booking a $500/night Grand Hyatt room who hits a payment decline will abandon the reservation. With Yuno, the transaction retries through an alternative acquirer before the guest sees a failure. Every recovered authorization is a room night sold that would otherwise be lost.
Desc_Yuno_Cap3: One API activates Alipay and WeChat Pay for Chinese travelers, UPI for Indian guests, Pix for Brazil, Mada for Saudi Arabia, GrabPay across SEA, iDEAL for the Netherlands, Klarna for BNPL, and SEPA for Europe. Yuno connects 1,000+ local payment methods across 40+ countries. Hyatt guests booking from growth markets can pay with their preferred local method, reducing checkout friction and increasing conversion.
Desc_Yuno_Cap4: Replace Hyatt's fragmented property-by-property payment processing with a single orchestration layer spanning 1,500+ hotels across 83 countries. Real time authorization dashboards, unified fraud scoring powered by NOVA (75% fraud reduction), centralized settlement and reconciliation, and one integration that scales from a Hyatt Place in Dallas to a Park Hyatt in Tokyo. Enterprise-wide payment intelligence instead of 1,500 isolated payment silos.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**HYATT HOTELS at a glance:**
- Founded: 1957 by Jay Pritzker
- Headquarters: Chicago, Illinois
- Chairman & CEO: Mark S. Hoplamazian (CEO since 2006, Chairman since February 2026)
- Revenue: $7.1B (FY 2025, 6.81% YoY growth)
- 2026 outlook: Net income of $235M to $320M (turnaround from $52M loss in 2025)
- NYSE: H
- 1,500+ hotels and all-inclusive properties in 83 countries across 6 continents
- 37 brands across 5 tiers: Luxury, Lifestyle, Inclusive, Classics, Essentials
- 242,000 employees (2026)
- 63 million World of Hyatt loyalty members
- Key brands: Park Hyatt, Grand Hyatt, Hyatt Regency, Andaz, Alila, Thompson Hotels, Miraval, Hyatt Place, Hyatt House, Hyatt Studios
- RevPAR growth target: 1-3% system-wide in 2026
- Strategic loyalty collaboration with American Airlines AAdvantage

**Technology infrastructure:**
- PMS: Migrating from Oracle Opera V5 to Oracle OPERA Cloud across 1,000+ properties (announced September 2024)
- CRS: Sabre SynXis Central Reservation System (for search and booking)
- Oracle Hospitality Integration Platform: 1,000+ pre-integrated business and customer services
- Oracle Cloud Infrastructure (OCI) for centralized data and operations

**Confirmed PSPs and payment partners:**

| Provider | Role | Scope |
|----------|------|-------|
| CyberSource (Visa) | Primary payment gateway via Sertifi integration | 190+ countries, full-service properties |
| Sertifi (by Flywire) | Digital contract and payment collection platform | Brand standard for all North America full-service |
| Onyx CenterSource GroupPay | M&E commission payment automation | 700+ properties (125 owned/managed + 580 franchised) |
| Oracle Payments | Integrated with OPERA Cloud PMS | Global (migrating) |
| Local bank acquirers | Per-property acquiring relationships | 83 countries |
| Sabre SynXis | CRS booking engine with payment processing | Global reservations |

**Payment methods accepted (hyatt.com):**
- Visa, Mastercard, American Express, Discover, JCB
- Some properties accept Apple Pay at restaurants and bars (varies by property)
- No standardized digital wallet support across portfolio
- No local alternative payment methods at online checkout
- Mobile payment acceptance (Google Pay, Samsung Pay) inconsistent across properties

**Hospitality industry payment challenges (context):**
- 55% of all US card fraud occurs in hospitality (AHLA)
- $150B annual fraud losses industry-wide
- 71% of chargebacks labeled "fraud" are actually friendly fraud
- Cross-border hotel bookings carry higher decline rates than domestic
- Hotel chargebacks are uniquely complex: services cannot be returned
- Authorization management is critical: final amounts often differ from initial authorization

**Hyatt GroupPay performance (Onyx CenterSource):**
- Average commission payment time: 46 days from event end date
- Best-performing hotels: 35 days
- 50-75% surge in staff productivity from automation
- Expanded from 125 to 700+ properties in 2025

**Key competitive landscape:**
- Marriott: ~10,000 properties, 130M+ Bonvoy members
- Hilton: ~9,000 properties, 120M+ Honors members, industry-leading Digital Key
- IHG: 100M+ One Rewards members
- Hyatt: Smaller portfolio but premium positioning, strongest loyalty program value per point

**Key meeting angles:**
1. **Enterprise-wide payment orchestration** | Hyatt operates 1,500+ properties across 83 countries with no unified payment layer. Each property processes payments independently through local acquirers. Yuno provides one orchestration layer spanning the entire portfolio
2. **Cross-border booking conversion** | 63M loyalty members booking globally through hyatt.com. Cross-border transactions decline more often than domestic. Smart Routing optimizes each booking payment by card BIN and destination country, recovering lost reservations
3. **Fraud reduction at scale** | 55% of US card fraud hits hospitality. Hyatt's properties fight fraud property by property with inconsistent tools. Yuno's NOVA provides unified fraud scoring across 1,500+ properties, cutting fraud by up to 75%
4. **Growth market expansion** | Hyatt is expanding in Asia Pacific, Middle East, and LATAM. Guests in these regions expect Alipay, WeChat Pay, UPI, Pix, and Mada at checkout. Yuno's 1,000+ APMs unlock local payment access for every new market
5. **Oracle OPERA Cloud migration** | Hyatt is already modernizing its tech stack with Oracle OPERA Cloud. This is the ideal moment to modernize payments alongside PMS migration. Yuno integrates as a payment orchestration layer complementing Oracle's hospitality platform
6. **$7.1B revenue at stake** | Every declined booking is a lost room night. With average Hyatt room rates in the hundreds, a 2% authorization uplift across the global portfolio translates to significant annual revenue recovery
7. **Competitive pressure** | Hilton leads in digital checkout innovation. Marriott has 10x the properties. Hyatt competes on experience and loyalty. Payment orchestration gives Hyatt a frictionless booking advantage that competitors lack

**Sources:**
- [Hyatt Q4 & FY2025 Earnings (Newsroom)](https://newsroom.hyatt.com/Q4-FullYear-2025-Earnings)
- [Hyatt Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/H/hyatt-hotels/revenue)
- [Hyatt + Sertifi Partnership (Hotel Management)](https://www.hotelmanagement.net/tech/hyatt-hotels-closes-deals-250-percent-faster)
- [Hyatt Broadens Payment Platform to Franchised Properties (Hotel Management)](https://www.hotelmanagement.net/tech/hyatt-broadens-roll-out-payment-platform-franchised-properties)
- [Hyatt + Onyx CenterSource GroupPay Expansion (BusinessWire)](https://www.businesswire.com/news/home/20251002060234/en/Onyx-CenterSource-and-Hyatt-Expand-GroupPay-to-Over-700-Properties-Accelerating-ME-Commission-Payments)
- [Hyatt Selects Oracle OPERA Cloud (Oracle)](https://www.oracle.com/news/announcement/hyatt-selects-oracle-opera-cloud-as-property-management-system-for-its-global-properties-2024-09-17/)
- [Hyatt + Sabre SynXis CRS (Newsroom)](https://newsroom.hyatt.com/news-releases?item=124401)
- [Mark Hoplamazian Chairman & CEO (Newsroom)](https://newsroom.hyatt.com/mark-s-hoplamazian)
- [Hyatt Leadership Change (Yahoo Finance)](https://finance.yahoo.com/news/investors-reacting-hyatt-hotels-h-160600723.html)
- [World of Hyatt Program Overview](https://world.hyatt.com/content/gp/en/program-overview.html)
- [Hyatt Payment FAQ](https://www.hyatt.com/help/faqs/payment-and-cancellation)
- [Hyatt Brands Explained (NerdWallet)](https://www.nerdwallet.com/travel/learn/the-guide-to-world-of-hyatt-brands)
- [Hospitality Fraud Statistics (AHLA via Sertifi)](https://corp.sertifi.com/blog/posts/hospitality-payment-chargeback-statistics-you-need-to-know-and-how-to-respond-to-them/)
- [Hospitality Chargebacks (Payrails)](https://www.payrails.com/blog/chargebacks-travel-hospitality)
- [Hyatt Logo (Brandfetch)](https://brandfetch.com/hyatt.com)
