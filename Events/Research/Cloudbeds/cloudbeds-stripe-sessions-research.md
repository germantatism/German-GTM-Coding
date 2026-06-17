# CLOUDBEDS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Cloudbeds
═══════════════════════════════════════

Logo: https://logotyp.us/file/cloudbeds.svg
Nombre merchant: Cloudbeds

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Limited Country Coverage
Tittle_Pain Point_2: Guest APM Blindspot
Tittle_Pain Point_3: Stripe Single-Rail Risk
Tittle_Pain Point_4: Chargeback Exposure
Tittle_Pain Point_5: Cross-Border Guest Declines

Desc_Pain Point_1: Cloudbeds Payments covers only 36 countries, but the platform serves 26,000+ properties across 150 countries. Hotels in 114+ markets have no native payment solution and must rely on legacy gateways like Authorize.net or PayPal Payflow.
Desc_Pain Point_2: International travelers booking hotels need local payment options. No UPI for Indian travelers, no Pix for Brazilian guests, no BLIK for Polish tourists, no GrabPay for Southeast Asian visitors. Guest payment preferences are ignored at checkout.
Desc_Pain Point_3: Cloudbeds Payments is built on Stripe since 2019. Stripe is the sole card acquirer behind the embedded finance platform. Any Stripe disruption blocks payment processing for thousands of properties, with no failover to Adyen or any backup.
Desc_Pain Point_4: Hotels take authorizations months before arrival, creating high chargeback exposure. While 99.96% of Cloudbeds properties see fewer than one chargeback per month, the industry average is 1.5% to 3%, and each dispute costs $25 to $100+ in fees.
Desc_Pain Point_5: International guests booking cross-border face card declines from 3D Secure friction and issuer blocks. Hotels lose direct bookings when payment fails, pushing travelers back to OTAs (which charge 15 to 25% commission).

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Cloudbeds Payments)
PSP_2: Adyen (via Cloudbeds Payments)
PSP_3: Authorize.net
PSP_4: PayPal Payflow Pro

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: BLIK
Local_M_4: GrabPay
Local_M_5: Boleto
Local_M_6: PSE
Local_M_7: Nequi
Local_M_8: M-Pesa
Local_M_9: Dana
Local_M_10: TrueMoney

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, Adyen, and any additional acquirer based on card BIN, issuer, and guest origin country. With 26,000+ properties processing bookings from 150+ countries, routing each transaction to the optimal local acquirer lifts auth rates 3 to 10%, recovering revenue hotels currently lose to silent declines.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a guest card. Yuno reroutes to Adyen or the next best acquirer in milliseconds, turning a failed booking payment into a confirmed reservation. Up to 50% recovery on soft declines. Every recovered transaction is a direct booking saved from OTA leakage.
Desc_Yuno_Cap3: Activates guest-preferred APMs worldwide: UPI for Indian travelers, Pix for Brazilians, BLIK for Polish tourists, GrabPay and Dana for SEA guests, M-Pesa for African travelers, PSE for Colombians. One API, 1,000+ payment methods. Properties accept any traveler's preferred payment with zero integration per market.
Desc_Yuno_Cap4: One dashboard replacing Cloudbeds' fragmented Stripe + Adyen + Authorize.net + PayPal Payflow settlement streams. Real-time approval rate monitoring per property, centralized reconciliation across all gateways and currencies, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead for hotel groups.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Cloudbeds at a glance:**
- 26,000+ properties across 150 countries (hotels, hostels, resorts, motels, serviced apartments)
- Revenue: ~$84.8M (2024 estimate, per Latka). 473% revenue growth over three years
- Total funding: $275M (Series D: $150M led by SoftBank Vision Fund 2, Nov 2021)
- On track for profitability by end of 2025
- 700+ employees across 44 countries
- 90 million bookings analyzed in 2026 State of Independent Hotels Report
- #1 rated PMS by Hotel Tech Report (2021 to 2025), World's Best Hotel PMS (World Travel Awards, 2022)
- Deloitte Technology Fast 500 (2024)

**Confirmed PSPs:**
- Stripe: primary embedded finance partner since 2019. Powers Cloudbeds Payments backend
- Adyen: secondary processor within Cloudbeds Payments PayFac model
- Authorize.net: legacy gateway integration (US, third-party processor agnostic)
- PayPal Payflow Pro: gateway integration (US, CA, AU, NZ)
- Elavon: supported connection
- No payment orchestrator detected

**Cloudbeds Payments Availability (36 Countries):**
- North America: US, Canada, Mexico
- Europe: UK, Germany, France, Spain, Italy, Netherlands, Belgium, Austria, Switzerland, Portugal, Ireland, Finland, and more (most of Europe)
- APAC: Australia, New Zealand, Singapore, Thailand
- NOT available in: most of Latin America (except Mexico), Africa, Middle East, India, Southeast Asia (except Singapore/Thailand)

**Payment Methods Currently Accepted:**
- Cards: Visa, Mastercard, Amex, Discover, regional cards
- Wallets: Apple Pay, Google Pay, Samsung Pay
- BNPL: Affirm, other BNPL options
- Regional: OXXO (Mexico), SEPA (Europe), Interac (Canada), Cartes Bancaires (France)
- Channels: Pay by Link, Tap to Pay (mobile POS), integrated terminals, manual entry (Card Not Present)
- Guest billing: Pix for Cloudbeds subscription billing (Brazil, manual only)

**Top Markets by Region (Hotel Performance Data):**
- Latin America: led all regions with 4.6% TRevPAR increase. Highest F&B revenue per room ($97.51)
- North America: stable performance, strong direct booking trends
- Europe: recovery continues, strong summer seasonality
- Asia Pacific: stalled YoY, lowest ancillary revenue ($43.90 F&B/room)
- Key countries: US, Mexico, Brazil, Colombia, Spain, Portugal, UK, Australia, Thailand

**Payment Issues in Hospitality:**
- Hotels take authorizations months before arrival, increasing chargeback exposure
- Cross-border card declines push guests to OTAs (15 to 25% commission vs. 2 to 3% card processing)
- 3D Secure / SCA compliance adds friction for European guests
- Manual reconciliation across multiple gateways wastes front desk staff time
- Legacy gateways (Authorize.net, PayPal Payflow) lack smart routing and failover
- Cloudbeds reports 15% revenue uplift for users on Cloudbeds Payments vs. off-platform processing

**Key Meeting Angles:**
1. **Direct booking conversion**: Every payment failure on the booking engine pushes the guest to Booking.com or Expedia (15 to 25% commission). Multi-acquirer failover saves direct bookings
2. **Traveler origin routing**: A hotel in Mexico receives guests from 50+ countries. Smart routing by card origin maximizes auth rates per guest nationality
3. **LATAM is their growth leader**: Latin America outperforms all other regions. Local APMs (Pix, PSE, Nequi, SPEI) would accelerate direct bookings in the fastest-growing market
4. **Stripe dependency**: Built entirely on Stripe since 2019. Yuno adds orchestration on top without replacing Stripe, reducing single-point-of-failure risk
5. **Scale opportunity**: 26,000+ properties. Platform-level orchestration improves payments for every property simultaneously
6. **OTA fee arbitrage**: $1 saved in OTA commission per booking x millions of bookings = massive hotel revenue recovery
7. **Profitability timeline**: Approaching profitability. Payment optimization directly improves unit economics

**Sources:**
- [Cloudbeds Payments](https://www.cloudbeds.com/payments/)
- [Cloudbeds: Payment Processing Gateways Supported](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/207142527-Payment-Processing-Gateways-Currently-Supported)
- [Cloudbeds: Payments Countries and Requirements](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/18785525247899-Apply-for-Cloudbeds-Payments-account-countries-requirements)
- [Cloudbeds: Payments FAQ](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/360057381933-Cloudbeds-Payments-Frequently-Asked-Questions)
- [Cloudbeds: Payments Terms (Stripe)](https://www.cloudbeds.com/terms/cloudbeds-payments/stripe/)
- [Cloudbeds Expands to 36 Countries](https://www.cloudbeds.com/articles/cloudbeds-expands-proprietary-payment-solution-to-more-than-36-countries/)
- [Stripe Case Study: Cloudbeds](https://stripe.com/customers/cloudbeds)
- [Cloudbeds: 2026 State of Independent Hotels Report](https://www.cloudbeds.com/hospitality-industry-report/)
- [Cloudbeds: Hotel Market Pulse Fall 2025](https://www.cloudbeds.com/articles/market-pulse/)
- [Cloudbeds: Redefining Hotel Payments](https://www.cloudbeds.com/articles/redefining-hotel-payments/)
- [Cloudbeds: Hotel Chargebacks Guide](https://www.cloudbeds.com/articles/hotel-chargebacks/)
- [Cloudbeds: $150M Funding Announcement](https://www.cloudbeds.com/articles/cloudbeds-raises-150m-in-funding-to-support-rapid-company-growth/)
- [Merchant Cost Consulting: Cloudbeds Payment Processing](https://merchantcostconsulting.com/lower-credit-card-processing-fees/cloudbeds-payment-processing/)
- [GetLatka: Cloudbeds Revenue](https://getlatka.com/companies/cloudbeds)
- [Cloudbeds Media Kit](https://www.cloudbeds.com/media-kit/)
