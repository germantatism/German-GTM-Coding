# HIMS & HERS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: hims & hers
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/HIMS-1e1322ee.png
Nombre merchant: hims & hers

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: FTC Probing Subscriptions
Tittle_Pain Point_2: 6 Countries, Cards Only
Tittle_Pain Point_3: Dual PSP, No Orchestrator
Tittle_Pain Point_4: Subscription Churn at Scale
Tittle_Pain Point_5: Eucalyptus + ZAVA Merge

Desc_Pain Point_1: FTC investigating hims & hers for over a year. Focus: subscription cancellation barriers and misleading advertising. 900+ BBB complaints in 3 years. Trustpilot 2.8 stars. Regulatory risk is mounting.
Desc_Pain Point_2: hims & hers operates in US, UK, Germany, France, Ireland and expanding to Australia and Japan. Only accepts cards and Apple Pay. No SEPA, Open Banking, giropay, Carte Bancaire, or local APMs in any EU market.
Desc_Pain Point_3: Uses both Stripe and Adyen for payment processing but with no orchestration layer between them. No smart routing, no failover cascade, no unified dashboard. Two PSPs operating independently across 6+ countries.
Desc_Pain Point_4: 2.5M+ subscribers with recurring billing. Failed renewals from expired cards, bank declines, and issuer blocks cause involuntary churn. No PSP level retry logic or cascade to recover failed subscription payments.
Desc_Pain Point_5: Acquiring Eucalyptus ($1.15B, AU/UK/DE/JP/CA) and ZAVA (UK/DE/FR/IE). Three separate payment stacks merging across 8+ countries. No unified payment infrastructure to absorb these acquisitions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Adyen
PSP_3: N/A
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: giropay
Local_M_3: Open Banking (UK)
Local_M_4: Carte Bancaire
Local_M_5: iDEAL
Local_M_6: PayPal
Local_M_7: Klarna
Local_M_8: Bancontact
Local_M_9: Konbini (Japan)
Local_M_10: PayPay (Japan)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Stripe + Adyen Orchestration
Tittle_Yuno_Cap2: NOVA AI Subscription Recovery
Tittle_Yuno_Cap3: Global APM Activation
Tittle_Yuno_Cap4: Acquisition Payment Merger

Desc_Yuno_Cap1: Route each subscription renewal across Stripe or Adyen based on card BIN, issuer, country, and real time PSP performance. Automatic failover between both PSPs. McDonald's achieved +4.7% approval across 18 markets with Yuno Smart Routing.
Desc_Yuno_Cap2: NOVA AI agents recover failed subscription payments via email and WhatsApp with up to 75% recovery rate. For 2.5M+ subscribers, NOVA prevents involuntary churn without the dark patterns that triggered the FTC investigation.
Desc_Yuno_Cap3: Activate SEPA, giropay, Open Banking, Carte Bancaire, iDEAL, PayPal, Konbini, PayPay via one API across all 8+ markets. 1,000+ payment methods, 68+ countries direct. InDrive scaled 10 markets in under 8 months with 90% approval.
Desc_Yuno_Cap4: One orchestration layer unifying hims, ZAVA (UK/DE/FR/IE), and Eucalyptus (AU/JP/UK/DE/CA) payment stacks. Single dashboard. Rappi (20+ PSPs) cut analyst time by 80% with Yuno. Reconciliation reduction up to 90%.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**hims & hers at a glance:**
- NYSE: HIMS | HQ: San Francisco, CA | CEO: Andrew Dudum (co founder)
- FY2025 Revenue: $2.35B (up 59% YoY from $1.48B in 2024)
- Q4 2025 Revenue: $617.8M (up 28% YoY)
- FY2025 Net Income: $128M (swing to profitability)
- 2.5M+ subscribers at end of FY2025 (up from 2.2M at end of 2024)
- FY2026 Guidance: $2.7B to $2.9B revenue, $300M to $375M adjusted EBITDA
- 2030 Goals: $6.5B+ revenue, $1.3B adjusted EBITDA
- Operations: US (primary), UK (launched 2019), expanding to Germany, France, Ireland, Australia, Japan, Canada
- Services: telehealth for dermatology, weight loss (GLP 1), sexual health, mental health, hair care
- D2C subscription model: consultations, prescriptions, and products bundled into monthly/quarterly subscriptions

**Key leadership (payments relevant):**
- Andrew Dudum, CEO and co founder
- Mo Elshenawy, CTO (joined May 2025): former President and CTO at Cruise (GM's self driving unit). 20+ years leading AI, product, and engineering teams.
- Yemi Okupe, CFO
- Dheerja Kaur, Chief Product Officer (joined July 2025)
- Dan Kenger, Chief Design Officer
- Deb Autor, Chief Policy Officer (joined November 2025)
- No dedicated VP/Head of Payments identified

**Confirmed PSPs and payment infrastructure:**
- Stripe: confirmed as primary payment processor (per official support page and Corepay analysis). Notable because telehealth is typically high risk for payment processing.
- Adyen: confirmed as secondary payment processor (per official support page).
- Credit/debit cards: Visa, Mastercard, Amex, Discover confirmed
- Apple Pay: confirmed (US and UK)
- PayPal: NOT accepted (explicitly stated in support docs)
- Klarna: listed as BNPL partner on Klarna's site, but not confirmed on hims support page
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment methods by market:**

US: Credit/debit cards (Visa, MC, Amex, Discover), Apple Pay

UK: Credit/debit cards, Apple Pay

Germany/France/Ireland: Credit/debit cards (via ZAVA, exact methods TBC)

Australia/Japan/Canada (pending Eucalyptus close): TBC

**Missing local APMs (blind spots across 8+ markets):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | SEPA Direct Debit | Eurozone (DE, FR, IE) | Standard for recurring Euro payments. Critical for subscription billing across EU markets. |
| 2 | giropay | Germany | Popular German online bank transfer. ZAVA operates in Germany. |
| 3 | Open Banking (UK) | UK | Account to account payments. Lower fees than card for recurring subscriptions. |
| 4 | Carte Bancaire | France | Dominant French card network. Local routing improves auth rates. ZAVA operates in France. |
| 5 | iDEAL | Netherlands (future) | 50%+ of Dutch online transactions. Important if expanding into NL. |
| 6 | PayPal | All markets | 400M+ accounts globally. Explicitly not accepted despite being the most requested APM. |
| 7 | Klarna | All markets | Listed on Klarna's site but not confirmed on hims checkout. Major BNPL for health/wellness. |
| 8 | Bancontact | Belgium (future) | 17M+ cards. Important for Benelux expansion. |
| 9 | Konbini | Japan | Convenience store payments. Critical for Eucalyptus Japan launch. |
| 10 | PayPay | Japan | 60M+ users. Dominant QR payment in Japan. |

**Payment complaints and regulatory issues:**
- FTC investigation (ongoing since 2024): probing subscription cancellation barriers and advertising practices. Over a year of document gathering and interviews.
- FDA warning letter (September 2025): product related, but compounds regulatory pressure
- Novo Nordisk partnership termination: cited illegal compounding and deceptive marketing
- BBB: 900+ complaints in 3 years. Subscription billing errors and cancellation runarounds.
- Trustpilot: 2.8 stars from 3,200+ reviews
- PissedConsumer: 1.8 stars
- Common complaints: unauthorized renewals, no advance notice of charges, zero refund policy even for unopened products, difficult cancellation flows
- Refund policy: "all sales and payments are final, irrevocable and not subject to refund"

**Key strategic developments (2025 to 2026):**
1. ZAVA acquisition (June 2025): European telehealth platform in UK, Germany, France, Ireland. 1.3M active customers. 2.3M consultations in 2024. All cash deal.
2. Eucalyptus acquisition (February 2026, $1.15B): Australia, UK, Germany, Japan, Canada. $450M+ ARR. Triple digit YoY growth. Tim Doyle becomes SVP International.
3. Mo Elshenawy CTO hire (May 2025): former Cruise President/CTO. Signals massive technology investment.
4. FY2025 profitability: $128M net income, first profitable year at scale
5. Weight loss / GLP 1 business: major growth driver, also source of regulatory scrutiny
6. 2030 vision: $6.5B+ revenue. Requires global scaling of subscription billing infrastructure.

**Yuno case references for the meeting:**

LIVELO: Subscription platform in Brazil. +5% approval rate, 50% recovery of failed transactions in under 3 months with Yuno. Directly relevant to hims & hers' subscription churn challenge.

INDRIVE: Marketplace scaled 10 LATAM markets in under 8 months. 90% approval rate. 4.5%+ recovery. Shows rapid multi country activation for acquisitions.

RAPPI: 20+ PSPs orchestrated. 80% analyst reduction. Zero implementation time for new providers. Relevant to Stripe + Adyen + ZAVA + Eucalyptus merge.

VIVA AEROBUS: 75% NOVA recovery rate, $300+ per transaction. Shows AI recovery power for high value subscriptions.

**Key meeting angles:**

1. **FTC investigation makes billing transparency urgent**: Over a year of FTC probing on cancellation/billing practices. 900+ BBB complaints. Instead of dark patterns that trap subscribers, Yuno's NOVA AI recovers failed payments proactively. Revenue recovery without regulatory risk.

2. **Stripe + Adyen with no orchestration is wasted potential**: hims already has two world class PSPs but no layer routing between them. Yuno orchestrates both: each renewal routed to whichever processor performs best for that card BIN, issuer, and country. +3 to 10% approval uplift.

3. **Three acquisitions, three payment stacks**: hims core (Stripe/Adyen) + ZAVA (UK/DE/FR/IE, unknown PSP) + Eucalyptus (AU/UK/DE/JP/CA, unknown PSP). Yuno sits on top of all three stacks via single API. Same play as DoorDash merging three stacks.

4. **2.5M+ subscribers = massive recurring billing optimization opportunity**: Every 1% improvement in subscription renewal success at $2.35B revenue = $23.5M recovered. Yuno's smart routing + NOVA AI can deliver 3 to 10% uplift.

5. **International expansion needs local APMs**: Germany (giropay, SEPA), France (Carte Bancaire), UK (Open Banking), Japan (Konbini, PayPay) all need local methods for optimal conversion. Cards only means lost subscribers. Yuno activates 1,000+ methods via one API.

6. **New CTO from Cruise understands platform orchestration**: Mo Elshenawy built autonomous vehicle platforms at GM/Cruise. He understands infrastructure layer thinking. Yuno pitch aligns with his technology worldview.

**Sources:**
- [hims Support: Payment Methods Accepted](https://support.hims.com/hc/en-us/articles/13543925336475-What-payment-methods-are-accepted)
- [hims UK: Payment Methods](https://himsuk.zendesk.com/hc/en-us/articles/16533744467995-which-payment-methods-do-you-accept)
- [hims Support: Payment Information](https://support.hims.com/hc/en-us/sections/360006262372-Payment-Information)
- [hims Support: Refund Policy](https://support.hims.com/hc/en-us/articles/360031526911-What-is-your-refund-policy)
- [hims Payment Processor Revealed (Corepay)](https://corepay.net/articles/who-is-hims-payment-processor/)
- [hims Klarna BNPL](https://www.klarna.com/us/store/30ad9e5d-b490-4e4c-9199-89f9755a341b/hims/pay-with-klarna/)
- [hims & hers FY2024 Financial Results (IR)](https://investors.hims.com/news/news-details/2025/Hims--Hers-Health-Inc.-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/)
- [hims & hers FY2025 Financial Results (IR)](https://investors.hims.com/news/news-details/2026/Hims--Hers-Health-Inc--Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx)
- [hims & hers Q3 2025 Results (IR)](https://investors.hims.com/news/news-details/2025/Hims--Hers-Health-Inc--Reports-Third-Quarter-2025-Financial-Results/default.aspx)
- [hims & hers 2.5M Subscribers (StockTitan)](https://www.stocktitan.net/news/HIMS/hims-hers-health-inc-reports-fourth-quarter-and-full-year-2025-o5uuu4etiv48.html)
- [hims & hers Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/HIMS/hims-hers-health/revenue)
- [hims & hers ZAVA Acquisition (IR)](https://investors.hims.com/news/news-details/2025/Hims--Hers-Announces-Plans-to-Acquire-ZAVA-Accelerating-Major-European-Growth-Across-the-UK-Germany-France-and-Ireland/default.aspx)
- [hims & hers ZAVA (CNBC)](https://www.cnbc.com/2025/06/03/hims-hers-to-acquire-zava-european-telehealth-platform.html)
- [hims & hers ZAVA (BusinessWire)](https://www.businesswire.com/news/home/20250603806947/en/Hims-Hers-Announces-Plans-to-Acquire-ZAVA-Accelerating-Major-European-Growth-Across-the-UK-Germany-France-and-Ireland)
- [hims & hers Eucalyptus Acquisition (IR)](https://investors.hims.com/news/news-details/2026/Hims--Hers-Announces-Agreement-to-Acquire-Eucalyptus-Accelerating-Its-Vision-to-Become-the-Leading-Global-Consumer-Health-Platform/default.aspx)
- [hims & hers Eucalyptus $1.15B (PharmExec)](https://www.pharmexec.com/view/hims-hers-enters-1-billion-agreement-acquire-eucalyptus)
- [hims & hers Eucalyptus (MobiHealthNews)](https://www.mobihealthnews.com/news/hims-hers-plans-acquire-eucalyptus-115b)
- [hims & hers CTO Mo Elshenawy (IR)](https://investors.hims.com/news/news-details/2025/Hims--Hers-Appoints-AI-Expert-and-Former-President-and-CTO-at-Cruise-as-Chief-Technology-Officer/default.aspx)
- [hims & hers Executive Management (IR)](https://investors.hims.com/governance/executive-management/default.aspx)
- [FTC Investigation (Bloomberg)](https://www.bloomberg.com/news/articles/2025-08-14/ftc-probing-complaints-about-hims-ads-cancellation-practices)
- [FTC Consumer Complaints (FTC FOIA)](https://www.ftc.gov/legal-library/browse/frequently-requested-foia-records/hims-hers/foia-2025-02172-him-hers-consumer-complaints)
- [FTC Investigation Impact (Seeking Alpha)](https://seekingalpha.com/news/4485799-hims-and-hers-health-under-investigation-ftc-business-practices)
- [hims & hers Trustpilot](https://www.trustpilot.com/review/hims.com)
- [hims & hers BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/health-and-medical-products/hims-hers-inc-1116-880029/complaints)
- [hims & hers Wikipedia](https://en.wikipedia.org/wiki/Hims_%26_Hers_Health)
- [hims & hers UK Weight Loss (IR)](https://investors.hims.com/news/news-details/2025/Hims--Hers-Brings-Comprehensive-Weight-Loss-Programme-to-the-UK/default.aspx)
- [Yuno Livelo Case Study](https://y.uno/success-cases/livelo)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Platform Overview](https://y.uno/)
