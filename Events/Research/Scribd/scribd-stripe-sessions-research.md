# SCRIBD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Scribd
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/2/26/Scribd_logo_%28new%29.svg
Nombre merchant: Scribd

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Stack
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: LATAM Localization Gap
Tittle_Pain Point_4: Single Routing Logic
Tittle_Pain Point_5: Reconciliation Drag

Desc_Pain Point_1: Four PSPs (Stripe, Adyen, Braintree, EBANX) across Scribd, Everand, SlideShare, and Fable with no unified orchestration. Each product line manages its own billing logic.
Desc_Pain Point_2: Users report "error processing your payment" on valid cards. Cross border declines hit 50%+ international base. India (#1 traffic) has zero local APMs.
Desc_Pain Point_3: EBANX covers LATAM cards but Pix, OXXO, and Boleto remain absent from checkout. Brazil is 6.5% of traffic with no instant payment option.
Desc_Pain Point_4: No smart routing across Stripe, Adyen, and Braintree. Each transaction hits one fixed PSP regardless of BIN, issuer, or real time performance data.
Desc_Pain Point_5: Four PSPs plus Apple and Google IAP create six settlement streams. Payments team manually reconciles across providers, currencies, and billing cycles.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Adyen
PSP_3: Braintree
PSP_4: EBANX

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: Boleto
Local_M_5: BLIK
Local_M_6: GoPay
Local_M_7: DANA
Local_M_8: OVO
Local_M_9: QRIS
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Scribd/Everand renewal across Stripe, Adyen, Braintree, and EBANX in real time. ML selects the best acquirer per BIN, issuer, and market. With $166M ARR and 1M+ subscribers across 100+ countries, even 3% uplift recovers $5M+ annually.
Desc_Yuno_Cap2: When Stripe declines a renewal, Yuno cascades to Adyen or Braintree in milliseconds. Up to 50% recovery on failed transactions. NOVA AI re-engages churned subscribers via WhatsApp/phone, recovering up to 75%.
Desc_Yuno_Cap3: Activate Pix in Brazil (6.5% traffic), UPI in India (#1 market, 12.3%), OXXO in Mexico, QRIS/GoPay in Indonesia (8%). One API, 1,000+ methods, instant geo-routing. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Scribd's fragmented Stripe + Adyen + Braintree + EBANX + Apple IAP + Google Play streams. Real time approval monitoring, centralized reconciliation, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Scribd at a glance:**
- Revenue: $166.8M (2024), up from $133.3M (2023), ~25% YoY growth
- 1M+ paying subscribers across 100+ countries
- 100M+ monthly active users across Scribd, Everand, SlideShare platforms
- Products: Scribd (document sharing), Everand (ebooks/audiobooks subscription), SlideShare (presentations), Fable (social reading, acquired 2025)
- Subscription pricing: Standard $11.99/mo, Plus $16.99/mo, Deluxe $28.99/mo (US only)
- CEO: Nick Grimminck (former CFO, promoted to CEO)
- Board: Padma Warrior (ex CTO Cisco, founder of Fable)
- Actively hiring Staff Backend Engineer, Payments & Billing (Denver, posted Feb 2026)
- 50%+ of subscriber base is outside the United States

**Confirmed PSPs:**
- Stripe: primary card processor (confirmed in Help Center, privacy policy)
- Adyen: secondary card processor (confirmed in Help Center)
- Braintree: tertiary processor (confirmed in Help Center)
- EBANX: LATAM cross border processor (confirmed in Help Center)
- Apple App Store: iOS IAP
- Google Play: Android IAP
- No payment orchestrator detected
- Job posting confirms: "integrates with multiple providers including Stripe, Adyen, and Braintree while supporting international currencies"

**Top 5 Markets Gap Analysis:**

MARKET 1: India (12.34% of traffic, #1 market)
  Currently offer: Visa/MC via Stripe/Adyen, PayPal
  Missing: UPI, RuPay, Paytm, PhonePe
  75%+ of Indian digital payments use UPI. Without it, Scribd loses the majority of potential conversions in its largest traffic market.

MARKET 2: United States (9.11% of traffic)
  Currently offer: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: ACH, Cash App Pay, Venmo
  US market is well covered but missing younger demographic wallets.

MARKET 3: Indonesia (8.06% of traffic)
  Currently offer: Visa/MC via Stripe/Adyen
  Missing: QRIS, GoPay, OVO, DANA
  Credit card penetration in Indonesia is ~5%. Without e-wallets, 95% of potential users cannot pay.

MARKET 4: Brazil (6.47% of traffic)
  Currently offer: Visa/MC via EBANX, PayPal
  Missing: Pix, Boleto
  Pix processes 70%+ of Brazilian digital payments. Everand recently launched LATAM plans but still lacks the #1 payment method.

MARKET 5: Peru (4.7% of traffic)
  Currently offer: Visa/MC via EBANX
  Missing: PagoEfectivo, Yape
  Cash and mobile wallet dominant market. Without local options, subscription conversion is severely limited.

**Payment issues documented:**
- Trustpilot reviews report "Oops! There was an error processing your payment" on valid cards
- Users unable to update payment methods after card changes
- Reports of charges continuing after cancellation
- Support acknowledges backlog in resolving payment related tickets

**Key meeting angles:**
1. **Payments hiring = pain signal** | Staff Backend Engineer Payments & Billing posted Feb 2026, proving internal investment in fixing payment infrastructure
2. **4 PSPs, zero orchestration** | Stripe, Adyen, Braintree, EBANX all running independently with no routing optimization
3. **India paradox** | #1 traffic market with zero local APMs. UPI adoption would unlock massive conversion lift
4. **Indonesia blind spot** | 8% of traffic, 5% card penetration, no e-wallets supported
5. **LATAM expansion timing** | Everand just launched in 20+ LATAM countries. Pix/OXXO/Boleto would accelerate adoption
6. **Multi-product complexity** | Scribd + Everand + SlideShare + Fable each need unified billing
7. **Competitor precedent** | Spotify (multi PSP via Adyen), Netflix (multi acquirer strategy)

**Sources:**
- [Scribd Payment Methods Help Center](https://support.scribd.com/hc/en-us/articles/210134006-Payment-methods)
- [Scribd Country Availability](https://support.scribd.com/hc/en-us/articles/210135206-In-what-countries-are-Scribd-Everand-and-Slideshare-available)
- [Scribd EU MAU Report](https://support.scribd.com/hc/en-us/articles/24001072212500-Average-Monthly-Active-Users-in-the-EU)
- [Scribd Revenue Data (GetLatka)](https://getlatka.com/companies/scribd)
- [Scribd Statistics 2025](https://expandedramblings.com/index.php/scribd-facts-statistics/)
- [Scribd Staff Backend Engineer Job](https://jobs.ashbyhq.com/scribd/5a880357-30b4-4393-b89a-034543c26cd3)
- [Scribd Leadership Expansion PR](https://www.prnewswire.com/news-releases/scribd-redefines-executive-leadership-team-with-four-additions-dedicated-to-enhancing-product-technology-operational-efficiency-and-people-301428040.html)
- [Scribd Trustpilot Reviews](https://www.trustpilot.com/review/www.scribd.com)
- [SimilarWeb: Scribd Traffic](https://www.similarweb.com/website/scribd.com/)
- [Everand Plans (August 2025)](https://support.scribd.com/hc/en-us/articles/29859144648596-Plus-Standard-and-Deluxe-plans-on-Everand-August-2025)
- [Scribd Wikipedia](https://en.wikipedia.org/wiki/Scribd)
- [Scribd Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Scribd_logo_(new).svg)
