# HEALTHSPAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Healthspan
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idM3tIH3_a/idZ-UEA4Fo.svg
Nombre merchant: Healthspan

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: CyberSource Lock-In
Tittle_Pain Point_2: Subscription Card Churn
Tittle_Pain Point_3: No Local EU/APAC Methods
Tittle_Pain Point_4: CBD Payment Restrictions
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: CyberSource is the primary payment gateway for all Healthspan ecommerce across UK, Ireland, Australia, and New Zealand. With 500,000 active customers and 92% DTC revenue, any acquirer issue blocks supplement purchases across four markets with limited fallback.
Desc_Pain Point_2: Subscribe & Save is Healthspan's core retention engine, but it only accepts credit/debit cards. When a subscriber's card expires or soft-declines, there is no automated cascade to an alternate processor, silently churning recurring customers and leaking monthly revenue.
Desc_Pain Point_3: Healthspan ships to Europe and Rest of World but offers only cards and PayPal at checkout. No iDEAL for Dutch customers, no BLIK for Poland, no Bancontact for Belgium, no POLi for Australia/NZ, no Konbini for potential Asian markets.
Desc_Pain Point_4: CBD product purchases are automatically restricted from certain payment methods (eWallets blocked). This forces CBD buyers to use cards only, reducing conversion for a high-margin product category that already faces regulatory payment friction.
Desc_Pain Point_5: International Subscribe & Save orders charge GBP prices to customers in Ireland (EUR), Australia (AUD), and New Zealand (NZD). Subscribers absorb cross-border FX markups on every recurring shipment, increasing effective price and churn risk.

SLIDE 1: PSP TOPOLOGY

PSP_1: CyberSource (primary gateway)
PSP_2: PayPal
PSP_3: Apple Pay
PSP_4: Visa / Mastercard
PSP_5: tradeit (ecommerce platform)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: BLIK
Local_M_3: Bancontact
Local_M_4: SEPA Direct Debit
Local_M_5: POLi (Australia/NZ)
Local_M_6: Klarna
Local_M_7: Afterpay
Local_M_8: Google Pay
Local_M_9: Open Banking (UK)
Local_M_10: Giropay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every supplement purchase and subscription renewal to the best performing acquirer by card BIN, customer country, and order value. With $92M+ in annual revenue and 500,000 active customers, a 3% auth uplift recovers significant revenue without touching the checkout experience.
Desc_Yuno_Cap2: When a Subscribe & Save card renewal declines, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly cutting the involuntary subscription churn that erodes Healthspan's core DTC retention model.
Desc_Yuno_Cap3: Unlocks the local methods Healthspan's international footprint demands: iDEAL for Netherlands, Bancontact for Belgium, BLIK for Poland, SEPA DD for EU subscriptions, POLi for Australia/NZ, Klarna/Afterpay for BNPL checkout, Open Banking for UK direct debits. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating CyberSource card processing, PayPal, Apple Pay, and new local payment methods across UK, Ireland, Australia, and New Zealand into one view. Real-time auth monitoring, centralized reconciliation with Microsoft Dynamics Navision, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Healthspan at a glance:**
- Founded: 1996 by Derek Coates
- CEO: Martin Talbot
- Headquarters: Healthspan House, The Grange, St. Peter Port, Guernsey GY1 2QH (Channel Islands)
- Parent company: Orkla Health (Orkla ASA, Norway) since March 2022
- Acquisition price: GBP 65M (cash and debt-free basis) + up to GBP 20M earn-out
- Revenue: ~$92.3M (2026); ~GBP 50M turnover (at time of acquisition)
- Employees: ~121 to 193 (varies by source)
- Active customers: ~500,000
- DTC share: 92% of sales direct-to-consumer online
- Products: 400+ vitamins, minerals, supplements, CBD oil, skincare, sports nutrition, pet health
- Brands: Healthspan (main), Healthspan Elite (sports/performance)
- Markets: UK (primary), Ireland, Australia, New Zealand, Europe (shipping), Rest of World (shipping)
- Does NOT ship to: USA or Canada
- Distribution centers: 3 (Great Britain, Ireland, New Zealand)
- Awards: Feefo Platinum Trusted Service Award (7 consecutive years as of 2026)
- UK delivery: 10 working days; Europe: 14 days; Rest of World: 21 days
- Ecommerce platform: tradeit by Red Technology (migrated from Sitecore)

**Confirmed PSPs / payment methods:**
- CyberSource: primary payment gateway (confirmed via Red Technology case study)
- PayPal: accepted for one-time purchases (NOT accepted for Subscribe & Save)
- Apple Pay: accepted at checkout
- Visa / Mastercard: accepted (97% UK ecommerce penetration)
- Subscribe & Save: credit/debit cards ONLY (no PayPal, no direct debit, no standing order, no cheque)
- CBD restrictions: eWallet payments automatically blocked for CBD product category
- No Google Pay detected
- No Open Banking / Pay by Bank detected
- No BNPL (Klarna, Afterpay) detected
- No payment orchestrator detected
- Attending Stripe Sessions (possible evaluation of Stripe as additional/replacement processor)

**Payment issues documented:**
- Subscription cancellation: cannot cancel online, must call; must cancel 72 hours before dispatch
- Misleading subscriptions: consumers report being signed up without clear warnings
- Pre-authorization holds: customer reported card pre-auth of GBP 38.75 that lasted 15 days (bank-side)
- Missing order records: customer paid EUR 30.99 but website showed no order; customer service could not find record
- Address re-entry: customers must re-enter billing/delivery address every order; website refuses to accept it
- Limited refund/change options: website changes reported but not implemented
- Trustpilot: generally positive (Feefo Platinum), but billing and subscription complaints exist
- Reviews.io: mixed reviews focusing on subscription management frustration

**Technology stack:**
- Ecommerce: tradeit by Red Technology
- ERP: Microsoft Dynamics Navision
- Address validation: Loqate
- Promotions: Qixol
- Reviews: Feefo
- Analytics: Google Analytics Enhanced eCommerce, Google Tag Manager
- Frontend: PWA, jQuery, Emotion, yepnope.js
- Security: X-XSS-Protection

**Key meeting angles:**
1. **Orkla scale opportunity**: Orkla Health (parent) operates across Nordic countries and Europe; payment orchestration could extend across the entire Orkla portfolio
2. **Subscribe & Save is card-only**: Core retention engine locked to credit/debit cards; adding SEPA DD, Open Banking, and local methods would reduce churn and expand subscriber base
3. **CBD payment friction**: High-margin CBD products blocked from eWallets; orchestration can route CBD payments to processors that accept the category
4. **Four-market expansion**: UK, Ireland, Australia, NZ each need local payment optimization; single CyberSource gateway does not provide local acquiring in each market
5. **DTC at 92%**: Almost all revenue flows through the website; checkout conversion improvements have outsized revenue impact
6. **Stripe Sessions = PSP evaluation**: Attending Stripe Sessions while using CyberSource signals they are evaluating Stripe as an additional or replacement processor; orchestration makes the transition seamless

**Sources:**
- [Healthspan UK Official Website](https://www.healthspan.co.uk/)
- [Healthspan About Us](https://www.healthspan.co.uk/about-us/)
- [Healthspan Wikipedia](https://en.wikipedia.org/wiki/Healthspan_(company))
- [Healthspan FAQs](https://www.healthspan.co.uk/faqs/)
- [Healthspan Subscribe & Save Policy](https://www.healthspan.co.uk/subscribe-and-save-policy/)
- [Healthspan Delivery Information](https://www.healthspan.co.uk/delivery-information/)
- [Healthspan Terms and Conditions](https://www.healthspan.co.uk/terms-and-conditions/)
- [Healthspan Credit Card Security](https://www.healthspan.co.uk/how-does-healthspan-ensure-credit-card-security/)
- [Healthspan UK Ecommerce Case Study (Red Technology)](https://www.redtechnology.com/customers/healthspan-uk/)
- [Healthspan International Rollout to Australia (Red Technology)](https://www.redtechnology.com/news-and-insights/healthspans-international-ecommerce-rollout-reaches-australia/)
- [Orkla Health Acquires Healthspan](https://www.orkla.com/media/press-releases/2022/orkla-health-acquires-healthspan/)
- [Orkla Healthspan Acquisition (NutraIngredients)](https://www.nutraingredients.com/Article/2022/03/09/orkla-expands-health-care-proposition-with-healthspan-acquisition/)
- [Orkla Healthspan GBP 65M (Bailiwick Express)](https://www.bailiwickexpress.com/business-ge/orkla-health-purchases-healthspan-65m/)
- [Healthspan Trustpilot Reviews](https://uk.trustpilot.com/review/www.healthspan.co.uk)
- [Healthspan Reviews.io](https://www.reviews.io/company-reviews/store/healthspan)
- [Healthspan PitchBook Profile](https://pitchbook.com/profiles/company/131446-99)
- [Healthspan ZoomInfo](https://www.zoominfo.com/c/healthspan-ltd/27936418)
- [Healthspan Logo (Brandfetch)](https://brandfetch.com/healthspan.co.uk)
- [Healthspan Customer Reviews (Feefo)](https://www.healthspan.co.uk/about-us/reviews/)
- [EcommerceDB Healthspan Revenue](https://ecommercedb.com/store/healthspan.co.uk)
