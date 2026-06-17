# BIRD | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Bird
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/bird.co/w/512/h/512/logo
Nombre merchant: Bird

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Checkout Wall
Tittle_Pain Point_2: Zero Local APMs in Europe
Tittle_Pain Point_3: No Failover Architecture
Tittle_Pain Point_4: Post-Bankruptcy Tech Debt
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: Bird accepts only cards, Apple Pay, Google Pay, and PayPal across 20+ countries. Riders in cash-heavy markets like Mexico, Qatar, and Italy cannot pay without a bank card, locking out millions of potential rides.
Desc_Pain Point_2: Bird operates in 20+ European and Middle East countries but offers zero region-specific APMs. No iDEAL in Netherlands, no Bancontact in Belgium, no Sofort in Germany, no BLIK in Poland. 20% of new EU riders chose PayPal when added.
Desc_Pain Point_3: Bird relies on a single payment processor with no automatic cascade. If the primary acquirer goes down, ride starts fail across every market simultaneously. No documented failover or retry logic exists.
Desc_Pain Point_4: After Chapter 11 bankruptcy and $145M acquisition by Third Lane Mobility in 2024, Bird rebuilt under severe cost constraints. Payment infrastructure was not modernized, leaving outdated integrations across 350+ cities.
Desc_Pain Point_5: Bird operates in 20+ countries with localized pricing but settles through centralized USD/EUR corridors. Riders in Qatar, Israel, Mexico, and Japan pay cross-border FX markups on every ride, eroding per-ride margins.

SLIDE 1: PSP TOPOLOGY

PSP_1: Braintree (PayPal)
PSP_2: Apple Pay
PSP_3: Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: BLIK
Local_M_4: Sofort
Local_M_5: OXXO
Local_M_6: Konbini
Local_M_7: SEPA Direct Debit
Local_M_8: Mada
Local_M_9: GrabPay
Local_M_10: DANA

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each ride payment to the highest-performing acquirer for that card BIN, issuer, and country. Bird processes millions of low-ticket microtransactions across 20+ countries. Even a 3% auth rate uplift recovers significant revenue at scale on $200M+ annual GMV.
Desc_Yuno_Cap2: Automatic cascade across multiple acquirers eliminates Bird's single-processor dependency. When the primary acquirer declines, Yuno reroutes in milliseconds. In micromobility, a failed payment means a rider walks away permanently. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Unlock riders across Bird's 20+ country footprint: iDEAL in Netherlands, Bancontact in Belgium, BLIK in Poland, Sofort in Germany, OXXO in Mexico, Konbini in Japan, Mada in Qatar/UAE. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Bird's fragmented Braintree + Apple Pay + Google Pay settlement. Real-time approval rate monitoring across all 350+ cities, centralized reconciliation, instant anomaly detection. Critical post-bankruptcy visibility for Third Lane Mobility leadership.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Bird at a glance:**
- Micromobility operator: e-scooters and e-bikes for short-term rental in 350+ cities
- Revenue: ~$200M TTM (March 2026), down from $240M peak in 2022
- Filed Chapter 11 bankruptcy December 2023; acquired by Third Lane Mobility for $145M in April 2024
- Emerged from bankruptcy September 2024 as anchor brand of Third Lane Mobility Inc.
- Also operates Spin brand (acquired from Ford) as independent subsidiary
- Largest micromobility operator in North America through Bird + Spin combined
- Partnered with Lyft in August 2024 to offer Bird scooters in 25+ US cities via the Lyft app
- Private company (delisted from NYSE September 2023; previously SPAC-listed at $2.5B peak valuation)
- 350+ cities across US, Canada, Europe, Middle East, and Australia

**Countries with operations (from privacy policy):**
- Americas: United States, Mexico, Canada
- Europe: Austria, Belgium, Finland, France, Germany, Hungary, Italy, Netherlands, Portugal, Spain, Switzerland, UK
- Middle East: Israel, Qatar, UAE
- Asia Pacific: Australia, Japan, Korea

**Confirmed PSPs:**
- Braintree (PayPal): primary processor (PayPal integration confirmed, Braintree powers PayPal for ride-sharing/micromobility apps)
- Apple Pay: mobile wallet on iOS
- Google Pay: mobile wallet on Android
- PayPal: direct wallet option (added November 2020; 20% adoption among new EU/ME riders)
- No payment orchestrator detected
- Bird Pay (tested 2020 for local business purchases) appears discontinued

**Payment methods accepted:**
- Visa, Mastercard, Amex, Discover (credit/debit)
- Apple Pay, Google Pay
- PayPal
- Cash payments via CVS/7-Eleven in select US cities (Bird Access program only)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Cash (Bird Access in select cities)
  Missing: ACH, Venmo direct, Cash App Pay
  Cash App and Venmo skew toward Bird's young urban demographic.

MARKET 2: Germany
  Currently offer: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: Sofort, SEPA Direct Debit, Giropay
  ~35% credit card penetration. Majority of Germans prefer direct bank payments.

MARKET 3: Netherlands
  Currently offer: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: iDEAL
  iDEAL processes 70%+ of Dutch online payments. Massive blind spot.

MARKET 4: Mexico
  Currently offer: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: OXXO, SPEI
  60%+ of Mexicans lack bank cards. OXXO has 21,000+ convenience stores accepting cash payments.

MARKET 5: Japan
  Currently offer: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: Konbini, PayPay, LINE Pay
  Konbini (convenience store) payments are standard for transport and digital services.

**Key meeting angles:**
1. **Post-bankruptcy rebuild** | Payment infrastructure is legacy from pre-Chapter 11; Third Lane Mobility leadership likely open to modern solutions
2. **Micromobility unit economics** | Every declined ride = $0 revenue and permanent rider churn. Auth rate improvement directly impacts margins
3. **20+ country footprint, zero local APMs** | Massive revenue leakage in EU/ME markets where card penetration is low
4. **Lyft partnership** | Integration with Lyft exposes Bird to Lyft's multi-PSP infrastructure, highlighting Bird's own gaps
5. **Low-ticket, high-frequency model** | Average ride $3-5; Yuno's per-transaction routing maximizes acceptance on millions of micro-payments
6. **Bird Access equity program** | Shows willingness to expand payment access; local APMs are the natural next step

**Sources:**
- [Bird Official Website](https://www.bird.co/)
- [Bird Privacy Policy](https://www.bird.co/privacy/)
- [Bird Help: Accepted Payments](https://help.bird.co/hc/en-us/articles/360031013811-Accepted-forms-of-payment)
- [Bird Blog: PayPal Integration](https://www.bird.co/blog/paypal-bird-new-payment-option-increase-scooter-access/)
- [Bird: Bankruptcy Emergence](https://www.bird.co/blog/bird-successfully-emerges-from-bankruptcy-as-a-stronger-company-and-will-operate-as-the-global-anchor-brand-of-newly-established-third-lane-mobility-inc/)
- [Bird Air 25+ Countries](https://www.bird.co/blog/bird-air-provides-eco-friendly-mobility-25-countries-including-japan/)
- [Bird Logo Guidelines](https://www.bird.co/logo-guidelines/)
- [Brandfetch: Bird Logo](https://brandfetch.com/bird.co)
- [Cassel Salpeter: Bird $145M Sale](https://www.casselsalpeter.com/firm-announcements/cassel-salpeter-co-facilitates-sale-of-bird-global-inc-assets-to-third-lane-mobility-inc-for-145-million-in-micromobility-firms-chapter-11-bankruptcy/)
- [Smart Cities Dive: Bird Reorganizes](https://www.smartcitiesdive.com/news/bird-micromobility-operator-reorganizes-third-lane-mobility-chapter-11-bankruptcy/712525/)
- [Lyft x Bird Partnership](https://www.globenewswire.com/news-release/2024/08/26/2935603/0/en/Lyft-and-Bird-Partner-to-Offer-Bird-Scooter-Rentals-in-the-Lyft-App-in-Over-25-U-S-Cities.html)
- [Bird Global Wikipedia](https://en.wikipedia.org/wiki/Bird_Global)
- [CompaniesMarketCap: Bird Revenue](https://companiesmarketcap.com/bird-global/revenue/)
