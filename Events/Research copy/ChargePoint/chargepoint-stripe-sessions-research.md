# CHARGEPOINT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ChargePoint
=======================================

Logo: https://companieslogo.com/img/orig/CHPT_BIG-1c7accca.png?t=1752312076
Nombre merchant: ChargePoint

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Pay Channels
Tittle_Pain Point_2: EU Compliance Pressure
Tittle_Pain Point_3: Contactless Auth Failures
Tittle_Pain Point_4: Multi-Currency Complexity
Tittle_Pain Point_5: Roaming Reconciliation

Desc_Pain Point_1: App, RFID, contactless NFC, phone, PayPal, Apple Pay, Google Pay on separate rails. No unified processor across 16 EU countries plus NA.
Desc_Pain Point_2: EU AFIR mandates contactless card acceptance at all public chargers. EMV terminal rollout at scale with no unified multi-acquirer strategy.
Desc_Pain Point_3: Tap-to-charge at roadside stations faces high decline rates from issuer velocity checks, low-value blocks, and cross-border processing.
Desc_Pain Point_4: 16 EU countries plus US and Canada means 10+ settlement currencies. FX on $5 to $50 session charges erodes margins across 1.3M+ ports.
Desc_Pain Point_5: OCPI roaming lets other networks charge at ChargePoint stations. Multi-network, multi-operator settlement creates reconciliation chaos.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed card processor (contactless NFC)
PSP_2: PayPal
PSP_3: Apple Pay
PSP_4: Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: BLIK
Local_M_4: Swish
Local_M_5: MobilePay
Local_M_6: Vipps
Local_M_7: SEPA Direct Debit
Local_M_8: Sofort
Local_M_9: EPS
Local_M_10: Pix

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each charging session payment to the best acquirer for that card, currency, and country. With $162M subscription revenue and 1.3M+ ports across 18 countries, a 3% auth uplift directly reduces failed session starts and driver frustration.
Desc_Yuno_Cap2: When a contactless tap-to-charge is declined, Yuno cascades to the next acquirer in milliseconds. Drivers charge their EVs on first tap, not after app fallback. Up to 50% of failed contactless auths recovered automatically.
Desc_Yuno_Cap3: Activates the local APMs that EV drivers in each market prefer: iDEAL in Netherlands, Bancontact in Belgium, BLIK in Poland, Swish in Sweden, MobilePay in Denmark, Vipps in Norway, EPS in Austria. One API, 1,000+ methods, EU AFIR compliance ready.
Desc_Yuno_Cap4: Single dashboard unifying ChargePoint's contactless NFC, app, RFID, PayPal, Apple Pay, Google Pay, and roaming partner settlement streams. Real-time monitoring across all 18 countries, centralized multi-currency reconciliation, anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ChargePoint at a glance:**
- Founded 2007, HQ Campbell, CA. Public: NYSE CHPT
- FY2026 (ended Jan 31, 2026): subscription revenue $162M (up 13% YoY)
- FY2025 total revenue: $417.1M. Subscription revenue: $144.3M (up 20% YoY)
- 1.3M+ connected charging ports worldwide (public and private)
- Operations: US, Canada, and 16 European countries (Germany, UK, France, Netherlands, Spain, Italy, Sweden, Norway, Denmark, Poland, Czech Republic, Portugal, Belgium, Austria, Switzerland, Ireland)
- Partnership with Eaton for integrated EV charging + power management
- Cloud subscription SaaS model: hardware + software + services
- Industry first: payment terminal meeting OCPI standards and EU AFIR regulations
- CEO: Rick Wilmer (appointed 2024)

**Confirmed PSPs / Payment Infrastructure:**
- Contactless NFC card processor: undisclosed (handles tap-to-charge at stations)
- PayPal: named as accepted payment method
- Apple Pay, Google Pay: digital wallet options
- ChargePoint RFID cards: proprietary network cards
- Toll-free phone payment: backup for drivers without app/card
- EMV chip reader: optional for specific grant/regulatory compliance
- OCPI roaming: cross-network charging via partner apps and RFID
- No payment orchestrator detected
- New drivers restricted from digital wallets for first 90 days

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market by ports)
  OK Currently offer: Credit/debit contactless, Apple Pay, Google Pay, PayPal, ChargePoint RFID
  Missing: ACH for fleet billing, Cash App Pay
  Note: Strong coverage but fleet operators need enterprise billing options

MARKET 2: Germany (largest EU EV market)
  OK Currently offer: Contactless NFC, ChargePoint app
  Missing: SEPA Direct Debit, Sofort, GiroPay
  Note: ~35% credit card penetration. Many German EV drivers prefer bank-based methods

MARKET 3: Netherlands (highest EV density in EU)
  OK Currently offer: Contactless NFC, ChargePoint app
  Missing: iDEAL (75%+ of Dutch online payments)
  Note: iDEAL dominates; without it, app top-up and account funding face friction

MARKET 4: Norway/Sweden/Denmark (Nordic EV leaders)
  OK Currently offer: Contactless NFC, ChargePoint app
  Missing: Vipps (Norway), Swish (Sweden), MobilePay (Denmark)
  Note: Nordic mobile wallets have 80%+ penetration. Card-only charging creates needless friction

MARKET 5: Poland (fast-growing EU EV market)
  OK Currently offer: Contactless NFC, ChargePoint app
  Missing: BLIK (70%+ of Polish digital payments), Przelewy24
  Note: BLIK is the dominant mobile payment method in Poland

**Key meeting angles:**
1. **EU AFIR compliance** | Mandatory contactless at all public chargers requires robust multi-acquirer processing across 16 countries
2. **Roadside reliability** | Failed tap-to-charge at highway stations creates range anxiety and brand damage
3. **Subscription revenue growth** | $162M recurring revenue depends on driver satisfaction at the point of charge
4. **Roaming settlement** | OCPI cross-network charging needs unified reconciliation across multiple operators and currencies
5. **Fleet billing complexity** | Enterprise fleet customers need local billing options beyond consumer card rails
6. **90-day wallet restriction** | New driver onboarding friction from digital wallet lockout period could be eliminated with local APMs

**Sources:**
- [ChargePoint Payment Methods FAQ](https://www.chargepoint.com/drivers/support/faqs/what-payment-methods-can-i-use)
- [ChargePoint Business Payment FAQ](https://www.chargepoint.com/businesses/payment-methods-faq)
- [ChargePoint Payment Terminal (OCPI/EU)](https://www.chargepoint.com/about/news/chargepoint-releases-first-terminal-meet-new-ev-charging-payment-standards)
- [ChargePoint PayPal Acceptance](https://www.chargepoint.com/about/news/chargepoint-now-accepts-paypal)
- [ChargePoint FY2026 Q3 Results](https://investors.chargepoint.com/news/news-details/2025/ChargePoint-Reports-Third-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx)
- [ChargePoint FY2026 Full Year Results](https://www.businesswire.com/news/home/20260304399865/en/ChargePoint-Reports-Fourth-Quarter-and-Full-Fiscal-Year-2026-Financial-Results)
- [ChargePoint FY2025 Results](https://www.chargepoint.com/about/news/chargepoint-reports-fourth-quarter-and-full-fiscal-year-2025-financial-results)
- [ChargePoint Europe Expansion](https://www.chargepoint.com/about/news/chargepoint-leads-charge-across-europe-strategic-acquisitions-pioneering-rd-facilities)
- [Paythru + Adyen EV Charging Platform](https://thepaypers.com/payments/news/paythru-partners-with-adyen-to-launch-ev-charging-payment-platform)
- [ChargePoint Tap to Charge](https://www.chargepoint.com/resources/setting-and-using-tap-charge)
- [ChargePoint Logo](https://companieslogo.com/chargepoint/logo/)
