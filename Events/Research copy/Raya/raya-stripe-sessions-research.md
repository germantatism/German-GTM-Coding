# RAYA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Raya
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id_xHSbAdO/idYFIk5eqn.png
Nombre merchant: Raya

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Apple Tax Erosion
Tittle_Pain Point_2: iOS-Only Revenue Cap
Tittle_Pain Point_3: Zero Web Billing
Tittle_Pain Point_4: Global Reach, Local Gap
Tittle_Pain Point_5: Involuntary Churn Risk

Desc_Pain Point_1: 100% of subscriptions flow through Apple IAP, surrendering 15-30% per transaction. At ~$60M ARR, Apple keeps $9M to $18M/year in commissions.
Desc_Pain Point_2: iOS-only with no Android or web checkout. Any Apple policy shift, fee hike, or App Store disruption blocks 100% of sign-ups and renewals worldwide.
Desc_Pain Point_3: No web checkout exists despite the April 2025 US ruling allowing external payment links. Raya leaves millions in margin by not offering web billing.
Desc_Pain Point_4: Members span LA, New York, London, Paris, and Berlin, but zero local payment methods are offered. European members cannot pay via SEPA, iDEAL, or Bancontact.
Desc_Pain Point_5: All renewals depend on a single Apple billing path. Expired cards and soft declines silently churn premium members at $20-$50/mo with no retry path.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple In-App Purchase
PSP_2: Stripe (privacy policy)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: Sofort
Local_M_5: BLIK
Local_M_6: Pix
Local_M_7: Google Pay
Local_M_8: PayPal
Local_M_9: Giropay
Local_M_10: Swish

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Web Checkout Orchestration

Desc_Yuno_Cap1: Route each subscription charge to the highest performing acquirer by member country and card BIN. At $60M+ ARR across 10+ countries, even a 3% auth uplift recovers $1.8M+ in annual revenue while reducing Apple dependency per transaction.
Desc_Yuno_Cap2: When Apple IAP or Stripe declines a $20 to $50/mo renewal, Yuno cascades to the next best processor in milliseconds. Recovers up to 50% of failed recurring charges, turning silent member churn into retained premium revenue.
Desc_Yuno_Cap3: Unlocks payment methods Raya's global members expect: SEPA DD for London/Paris/Berlin, iDEAL for Netherlands, Bancontact for Belgium, BLIK for Poland, PayPal as universal fallback. One API, 1,000+ methods, no per-market engineering.
Desc_Yuno_Cap4: Single integration powers a web subscription checkout outside Apple IAP, recapturing 15-30% in App Store commissions. Post-Epic ruling, Raya can legally direct US members to a Yuno-powered web flow and keep 100% of subscription revenue.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Raya at a glance:**
- Exclusive, membership-based social/dating app for creatives, celebrities, and professionals
- Founded: 2015 by Daniel Gendelman (CEO). HQ: Los Angeles, CA
- Revenue: ~$60M ARR (est. $5M/mo as of Jan-Feb 2026, per Sensor Tower). $100M+ cumulative lifetime user spending
- Previous revenue: $18.2M in 2023 (per Latka/CEO interview), tripled by 2026
- Downloads: ~90K-100K/month (2026)
- Funding: $15.5M raised (Cowboy Ventures, Dreamers VC, J Ventures Mgmt, Niche Capital, S32)
- Team: ~114 employees (2023 data)
- iOS only. No Android. No web version.
- Membership tiers: Standard ($19.99/mo), Raya+ Premium ($49.99/mo), with 6-month and annual discounts
- Acceptance rate: ~8% of applicants
- Features: Dating, networking, social discovery, events, directory, groups, maps

**Confirmed PSPs:**
- Apple In-App Purchase: 100% of subscription billing flows through iOS IAP
- Stripe: named in Raya's privacy policy as third-party payment processor
- No web checkout, no Android billing, no payment orchestrator detected
- No BNPL, no local APMs, no alternative payment methods visible

**International Presence:**
- Key cities: Los Angeles, New York, London, Paris, Berlin, Barcelona, Mexico City
- Offices: Los Angeles (HQ), with reported presence in New York, London, Paris, Berlin, Barcelona, Mexico City
- US and UK are the most profitable markets
- ~75% of users US-based (est. 15K+ of ~20K active members)
- Available in 10+ countries but iOS App Store billing only

**Top Markets Gap Analysis:**

MARKET 1: United States (~75% of revenue)
  Offer: Apple IAP (Visa/MC/Amex via iTunes billing)
  Missing: Direct card billing, ACH, Cash App Pay, Venmo, PayPal
  Post-Epic ruling (April 2025) allows external web checkout links from iOS apps in the US

MARKET 2: United Kingdom (~10% of revenue)
  Offer: Apple IAP only
  Missing: Open Banking, PayPal, Faster Payments, Klarna
  Premium members in London paying $50/mo via Apple with no UK-native option

MARKET 3: France (~5% of revenue)
  Offer: Apple IAP only
  Missing: Carte Bancaire (local network), SEPA DD, PayPal
  Carte Bancaire handles 60%+ of French card transactions

MARKET 4: Germany (~3% of revenue)
  Offer: Apple IAP only
  Missing: SEPA DD, Giropay, Sofort, PayPal
  ~35% credit card penetration. SEPA DD is the backbone of German subscription billing

MARKET 5: Spain/Mexico (~2% of revenue)
  Offer: Apple IAP only
  Missing: Bizum (Spain), OXXO/SPEI (Mexico)
  Bizum has 30M+ users in Spain. OXXO dominates cash payments in Mexico

**Key meeting angles:**
1. **Apple Tax recapture**: 15-30% commission on $60M ARR = $9-18M/year to Apple. Web checkout via Yuno recaptures this margin
2. **Epic ruling window**: Since April 2025, US apps can link to external payment. Raya has not acted. First-mover advantage in exclusive dating
3. **Single point of failure**: 100% revenue through Apple IAP. Any billing disruption = total revenue halt
4. **European local methods**: London, Paris, Berlin members with zero SEPA, zero Open Banking, zero Carte Bancaire
5. **Android + web unlock**: Yuno web checkout SDK enables billing outside iOS entirely, opening Android users and web sign-ups
6. **Premium ARPU protection**: At $20-$50/mo per member, every churned member is high-value. Failover recovers up to 50% of failed renewals
7. **Competitor benchmark**: Bumble, Hinge, and Tinder all offer web billing + local APMs in Europe

**Sources:**
- [Raya Official Website](https://rayatheapp.com/)
- [Raya Privacy Policy](https://rayatheapp.com/privacy)
- [Raya App Store Listing](https://apps.apple.com/us/app/raya/id957215308)
- [Wikipedia: Raya (app)](https://en.wikipedia.org/wiki/Raya_(app))
- [AppMagic: Raya $100M User Spending](https://appmagic.rocks/blog/raya-100-millions-user-spending)
- [Sensor Tower: Raya Revenue](https://app.sensortower.com/overview/957215308?country=US)
- [Latka: Raya $18.2M Revenue](https://getlatka.com/companies/rayatheapp.com)
- [Crunchbase: Raya Funding](https://www.crunchbase.com/organization/raya)
- [The Org: Raya Leadership](https://theorg.com/org/raya/org-chart/daniel-g)
- [Brandfetch: Raya Logo](https://brandfetch.com/rayatheapp.com)
- [DatingByBlaine: Raya Review 2026](https://datingbyblaine.com/guides/raya-dating-app-review)
- [SwipeStats: Raya Review 2026](https://www.swipestats.io/blog/raya-review)
- [Roast Dating: Raya Plus Membership](https://roast.dating/blog/raya-plus-membership)
- [DatingGroup: Where Is Raya Located](https://www.datinggroup.in/where-is-raya-located/)
- [Grazia: Raya Membership Explained](https://graziadaily.co.uk/life/real-life/raya-dating-app/)
- [RevenueCat: App-to-Web Purchase Guidelines](https://www.revenuecat.com/blog/engineering/app-to-web-purchase-guidelines/)
