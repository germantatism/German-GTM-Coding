# BETTERME | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: BetterMe
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idlCMOczXe/idV9UD7fK2.svg
Nombre merchant: BetterMe

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Blind Routing
Tittle_Pain Point_2: Subscription Churn Leak
Tittle_Pain Point_3: No Local APMs in LATAM
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: Chargeback & Fraud Surge

Desc_Pain Point_1: Privacy policy confirms Adyen, Checkout.com, PayPal, and "too many to list" PSPs. Without an orchestrator, routing decisions are hardcoded per region with no dynamic optimization based on real-time auth rates.
Desc_Pain Point_2: $75M+ ARR flows through multiple disconnected PSPs. When a renewal fails on one acquirer, there is no automated cascade to a second. Every soft decline is lost revenue from 10M+ monthly active users.
Desc_Pain Point_3: Mexico is a top 3 traffic market with no local entity and no local APMs. No OXXO, no SPEI, no CoDi. 60%+ of Mexicans are unbanked. Cards-only checkout blocks the mass market.
Desc_Pain Point_4: Cyprus-registered entity processes globally. UK and Mexico are top markets with no local acquiring, meaning every transaction carries cross-border interchange markup and lower approval rates.
Desc_Pain Point_5: BBB records 900+ complaints in three years. Trustpilot shows 2.3/5 stars. Users report unauthorized recurring charges and failed cancellations, driving chargebacks that increase processing costs.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: Checkout.com
PSP_3: PayPal
PSP_4: Shopify Payments (Store)
PSP_5: Apple Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: SPEI
Local_M_3: Pix
Local_M_4: Boleto
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: BLIK
Local_M_8: UPI
Local_M_9: SEPA Direct Debit
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge to the best performing acquirer per card BIN, country, and issuer across Adyen, Checkout.com, and PayPal. With $75M+ ARR and 10M+ MAU, a 3-10% auth uplift recovers millions annually without re-integrating any PSP.
Desc_Yuno_Cap2: When a renewal fails on Adyen, Yuno cascades to Checkout.com or an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly cutting involuntary churn across BetterMe's global subscriber base.
Desc_Yuno_Cap3: Unlocks the local methods BetterMe's top markets demand: OXXO/SPEI in Mexico (top 3 traffic), Pix in Brazil, iDEAL in Netherlands, BLIK in Poland, UPI in India. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating Adyen, Checkout.com, PayPal, Shopify Payments, and all unnamed PSPs into one view. Real-time auth rate monitoring, centralized reconciliation, and millisecond anomaly detection via NOVA replaces manual multi-PSP management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**BetterMe at a glance:**
- Founded: 2017 in Kyiv, Ukraine
- CEO: Victoria Repa (Co-Founder)
- HQ: Registered in Cyprus (BetterMe International Limited, HE 417945); US entity: BetterMe, Inc.
- Revenue: ~$75-80M ARR (bootstrapped, no external VC funding beyond initial $5M from Genesis)
- Subscribers: 10M+ monthly active users across iOS and Android
- Downloads: 150M+ lifetime
- Available in 30+ languages, operating across 5 continents
- Employees: ~242-582 (varying reports, 2025-2026)
- Products: BetterMe Health Coaching app, BetterMe Store (Shopify), physical products (pilates kits, yoga mats)
- Pricing: Varies by plan, weekly/monthly/annual subscriptions
- Top markets by traffic: US (#1), UK (#2), Mexico (#3)
- Audience: 69% female, 31% male; largest age group 25-34

**Confirmed PSPs:**
- Adyen: explicitly named in privacy policy as payment processor
- Checkout.com: explicitly named in privacy policy as payment processor
- PayPal: explicitly named in privacy policy; also processes international ACH debits
- Shopify Payments: powers the BetterMe Store (store.betterme.world)
- Apple In-App Purchase: iOS subscription billing
- Google Play Billing: Android subscription billing
- Huawei AppGallery Billing: Huawei device subscriptions
- Apple Pay: accepted on e-commerce store
- Privacy policy states: "Due to the large number of payment processing providers we work with, we cannot list them all"
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, or similar)

**Payment issues documented:**
- BBB: 900+ complaints in three years, many about unauthorized charges and billing after cancellation
- Trustpilot: 2.3/5 stars across ~4,800 reviews
- Apple Community forums: multiple threads calling BetterMe a "scam" due to billing practices
- Xolvie (Sikayetvar) complaints from Turkey, Belgium, and other international markets
- Users report weekly charges of $8+ without explicit consent
- Cancellation flow involves multiple "are you sure" prompts and discount offers, making cancellation difficult
- Refund requests frequently denied or only partially honored (50% refund)

**Top Markets Gap Analysis:**

MARKET 1: United States (largest traffic source)
  Offer: Visa/MC/Amex via Adyen/Checkout.com, PayPal, Apple Pay
  Missing: ACH Direct Debit, Cash App Pay, Venmo
  No native debit option for subscription billing

MARKET 2: United Kingdom (second largest)
  Offer: Visa/MC via Adyen/Checkout.com, PayPal
  Missing: Open Banking payments, PayByBank
  No local UK entity detected; cross-border acquiring risk

MARKET 3: Mexico (third largest)
  Offer: Visa/MC via cross-border acquiring
  Missing: OXXO, SPEI, CoDi
  No local entity; 60%+ unbanked population. OXXO processes 55M+ transactions/month

MARKET 4: Brazil (Portuguese content available)
  Offer: Visa/MC via cross-border acquiring
  Missing: Pix, Boleto Bancario
  Pix handles 45B+ transactions/year in Brazil

MARKET 5: Germany (localized content)
  Offer: Visa/MC via Adyen/Checkout.com, PayPal
  Missing: SEPA Direct Debit, Giropay
  ~35% credit card penetration; SEPA DD standard for subscriptions in DACH

**Key meeting angles:**
1. **Multi-PSP chaos without orchestration**: Adyen + Checkout.com + PayPal + unnamed others with no central routing layer = suboptimal auth rates and zero visibility
2. **LATAM activation**: Mexico is top 3 traffic but zero local APMs and no local entity. OXXO/SPEI alone could unlock mass-market conversion
3. **Chargeback reduction**: 900+ BBB complaints drive disputes. Better retry logic and routing reduces failed charges that trigger complaints
4. **Cross-border drag**: Cyprus entity processing for UK/Mexico/Brazil means every transaction carries FX markup and lower approval rates
5. **Bootstrapped margin focus**: No VC funding means every basis point of payment cost matters. Smart Routing optimization directly hits the bottom line
6. **Scale opportunity**: 150M+ downloads, 10M+ MAU, $75M+ ARR with growing physical product store on Shopify

**Sources:**
- [BetterMe Privacy Policy](https://betterme.world/en/privacy-policy)
- [BetterMe Subscription Terms](https://betterme.world/en/subscription-terms)
- [BetterMe Terms and Conditions](https://betterme.world/en/terms)
- [BetterMe Store FAQ](https://store.betterme.world/pages/faq)
- [BetterMe BBB Complaints](https://www.bbb.org/us/ga/cumming/profile/mobile-apps/betterme-0443-91842647/complaints)
- [BetterMe Trustpilot Reviews](https://www.trustpilot.com/review/betterme.world)
- [BetterMe Xolvie Complaints](https://www.sikayetvar.com/en/betterme-us)
- [Sifted: BetterMe Bootstrapped Ukrainian Health App](https://sifted.eu/articles/betterme-bootstrapped-health-app-ukraine)
- [Partnerkin: Interview with Victoria Repa](https://partnerkin.com/en/blog/interviews/interview-with-victoria-repa)
- [BetterMe Wikipedia](https://en.wikipedia.org/wiki/BetterMe)
- [BetterMe Tracxn Profile](https://tracxn.com/d/companies/betterme/__utaEHIwUpMzGj-dwDPlxoFOzD3m8BpN0sTqmbFJpNxQ)
- [Brandfetch: BetterMe Logo](https://brandfetch.com/betterme.world)
