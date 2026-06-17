# ASURION | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Asurion
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/asurion.com/w/512/h/512/logo
Nombre merchant: Asurion

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Carrier-Fragmented Billing
Tittle_Pain Point_2: Claims Deductible Friction
Tittle_Pain Point_3: 22-Country Payment Gap
Tittle_Pain Point_4: No Unified Reconciliation
Tittle_Pain Point_5: D&G Integration Complexity

Desc_Pain Point_1: Asurion processes 230M+ customer subscriptions through carrier billing (Verizon, AT&T, T-Mobile) and direct channels. Each carrier has its own payment infrastructure, creating fragmented settlement across dozens of billing systems globally.
Desc_Pain Point_2: When filing insurance claims, customers must pay deductibles via credit card at the moment of claim. In markets like Brazil, Mexico, Japan, and Colombia, low card penetration means customers cannot pay deductibles, delaying or abandoning claims.
Desc_Pain Point_3: Asurion operates in 22 countries across North America, Europe, Asia, and Latin America. Direct-to-consumer products (Home+, Tech Unlimited) require local payment acceptance, but current infrastructure lacks regional APMs.
Desc_Pain Point_4: Asurion processes payments through carrier integrations, Amazon, direct web, and retail partners (Walmart, Best Buy). No single platform reconciles these fragmented streams, creating operational overhead across 23,000 employees.
Desc_Pain Point_5: Asurion is acquiring Domestic & General (12 European markets, $1.32B revenue) in mid-2026. Integrating D&G's UK/European payment infrastructure with Asurion's North American and Asian systems requires a unified orchestration layer.

SLIDE 1: PSP TOPOLOGY

PSP_1: Carrier Billing (Verizon, AT&T, T-Mobile)
PSP_2: PayPal / Venmo (Home+ reimbursements)
PSP_3: Amazon Pay (Marketplace channel)
PSP_4: Credit Card (direct claims)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: Konbini
Local_M_4: SEPA Direct Debit
Local_M_5: BACS Direct Debit
Local_M_6: iDEAL
Local_M_7: Boleto
Local_M_8: UPI
Local_M_9: GCash
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each deductible payment and subscription charge to the best-performing acquirer for that customer's geography and payment method. With 230M+ customers and billions in annual premiums, even a 3% auth rate uplift recovers tens of millions in collected deductibles.
Desc_Yuno_Cap2: Automatic cascade across multiple acquirers protects Asurion's claim deductible collection. When the primary processor declines, Yuno reroutes in milliseconds. A declined deductible delays device replacement and damages the customer experience. Up to 50% soft decline recovery.
Desc_Yuno_Cap3: Accept deductibles and subscriptions locally: Pix/Boleto in Brazil, OXXO in Mexico, Konbini in Japan, SEPA in Europe, UPI in India, PSE in Colombia. One API, 1,000+ payment methods. Critical as Asurion expands direct-to-consumer across 22+ countries.
Desc_Yuno_Cap4: One dashboard unifying Asurion's fragmented carrier billing + Amazon + direct web + retail partner settlement streams. Essential for the Domestic & General integration: centralized reconciliation across 12+ additional European markets, real-time cross-border visibility.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Asurion at a glance:**
- World's largest tech protection and insurance company
- Revenue: $5B-10B annually (private, exact figure undisclosed; some sources report $21.5B)
- 230M+ customers globally, 50%+ with recurring subscriptions
- 23,000 employees across 14 countries
- Private company (owned by institutional investors)
- Headquartered: Nashville, Tennessee
- Products: device insurance, extended warranties, tech support, appliance protection
- Key brands: Asurion, Asurion Home+, Asurion Tech Unlimited, Asurion Tech Care
- Distribution: major US carriers (Verizon, AT&T, T-Mobile), retailers (Amazon, Walmart, Best Buy), direct-to-consumer

**Domestic & General acquisition (closing mid-2026):**
- UK-based appliance care provider, 110+ year legacy
- $1.32B annual revenue
- Operations in 12 European markets + US
- 22M+ appliances under protection
- 25,000+ independent repair engineers
- Partners: Whirlpool, Sky, Hoover-Candy, John Lewis
- Deal value: $2.1B
- Will operate as independent business unit under Asurion

**Geographic operations:**
- Americas: US, Canada, Brazil, Mexico, Colombia, Peru, Chile (via Claro/America Movil)
- Europe: UK, France (expanding with D&G to 12+ markets)
- Asia: Japan (60M users via NTT Docomo, KDDI), China, Singapore
- Operations in 22 countries total through carrier partnerships

**Confirmed PSPs / payment methods:**
- Carrier billing: primary channel (premiums bundled in phone bills via Verizon, AT&T, T-Mobile, Claro, NTT Docomo, KDDI)
- Credit card: direct deductible payments at claim time
- PayPal, Venmo: Home+ fast claims reimbursements (announced 2024)
- Direct-to-debit: Home+ reimbursement option
- Amazon: marketplace protection plan billing through Amazon
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market)
  Currently offer: Carrier billing, credit card, PayPal, Venmo
  Missing: ACH Direct Debit, Cash App Pay
  Home+ and Tech Unlimited DTC products could benefit from ACH for recurring billing.

MARKET 2: Japan (60M users)
  Currently offer: Carrier billing (NTT Docomo, KDDI)
  Missing: Konbini, PayPay, bank transfer (furikomi)
  Direct-to-consumer expansion requires local payment acceptance beyond carrier billing.

MARKET 3: Brazil (Claro partnership)
  Currently offer: Carrier billing (Claro Brazil)
  Missing: Pix, Boleto
  Pix handles 70%+ of digital payments. DTC and claims deductibles need local methods.

MARKET 4: Mexico (Claro partnership)
  Currently offer: Carrier billing (Claro Mexico)
  Missing: OXXO, SPEI
  60%+ unbanked. OXXO is essential for deductible collection in non-carrier channels.

MARKET 5: United Kingdom (D&G acquisition)
  Currently offer: D&G's existing UK payment infrastructure
  Missing: Unified orchestration with Asurion's systems, Open Banking
  Post-acquisition, UK/European payment systems must integrate with global Asurion infrastructure.

**Key meeting angles:**
1. **D&G acquisition** | Mid-2026 close creates immediate need for unified payment orchestration across 12+ new European markets
2. **230M customers** | Massive recurring subscription base where every failed payment = customer coverage gap
3. **Deductible friction** | Claims deductible collection in low-card markets (Brazil, Mexico, Japan) directly impacts customer satisfaction
4. **DTC expansion** | Home+ and Tech Unlimited are growing direct-to-consumer, requiring payment infrastructure beyond carrier billing
5. **Carrier dependency** | Diversifying beyond carrier billing is strategic priority as Asurion builds direct customer relationships
6. **Global complexity** | 22 countries, multiple carrier partners, Amazon, Walmart, direct web. No single reconciliation layer exists

**Sources:**
- [Asurion Official Website](https://www.asurion.com/)
- [Asurion Claims](https://www.asurion.com/claims/)
- [Asurion Home+ Reimbursements via PayPal/Venmo](https://www.asurion.com/press-releases/asurion-home-launches-fast-claims-reimbursements-through-paypal-venmo-and-more/)
- [Asurion Q1 2025 Partnerships](https://www.asurion.com/press-releases/asurion-growth-q1-2025/)
- [Asurion D&G Acquisition](https://www.asurion.com/press-releases/asurion-acquires-domestic-and-general/)
- [CVC: Asurion D&G Announcement](https://www.cvc.com/media/news/2025/asurion-to-acquire-domestic-general-establishing-a-global-leader-in-technology-and-appliance-care-committed-to-excellence-in-customer-service/)
- [Asurion Wikipedia](https://en.wikipedia.org/wiki/Asurion)
- [Asurion Brazil Expansion](https://www.asurion.com/press-releases/asurion-expands-services-latin-america-entrance-brazil-telecommunications-market/)
- [Asurion Latin America (Claro)](https://www.asurion.com/press-releases/asurion-expands-into-latin-america/)
- [Asurion Japan (JETRO)](https://www.jetro.go.jp/en/invest/investment_environment/success_stories/asurion.html)
- [Brandfetch: Asurion Logo](https://brandfetch.com/asurion.com)
- [Nashville Post: D&G Revenue](https://www.nashvillepost.com/business/m_and_a/asurion-to-acquire-u-k-company-with-1-32b-in-revenue/article_581ff121-28c1-460b-b8ac-15c8c14d1f2d.html)
- [Finsur: Asurion D&G Deal Value](https://www.finsur.co.uk/p/asurion-acquires-d-and-g-21bn-for)
