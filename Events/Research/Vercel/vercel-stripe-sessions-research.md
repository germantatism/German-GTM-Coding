# VERCEL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Vercel
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5e/Vercel_logo_black.svg
Nombre merchant: Vercel

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Pro Plans
Tittle_Pain Point_2: Usage Overage Declines
Tittle_Pain Point_3: Global Dev Gap
Tittle_Pain Point_4: Single Acquirer Risk
Tittle_Pain Point_5: v0 Conversion Wall

Desc_Pain Point_1: Pro ($20/user/mo) accepts cards only via Stripe. Prepaid, gift, and virtual cards explicitly rejected. Devs in emerging markets cannot upgrade.
Desc_Pain Point_2: Usage-based compute/bandwidth billing creates unpredictable overages. International cards face higher decline rates on variable charges, silent leakage.
Desc_Pain Point_3: 40M+ devs across 51 countries with 126 PoPs, but zero local APMs. No UPI, no Pix, no SEPA DD. Infrastructure is global; payments are not.
Desc_Pain Point_4: Stripe processes 100% of payments. At $200M+ ARR with 40M devs, any degradation blocks Pro upgrades, Enterprise renewals, and v0 subs globally.
Desc_Pain Point_5: v0 has 4M+ users and a $20/mo tier. Free-to-paid requires an intl credit card, locking out developers where card penetration is under 30%.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Stripe Billing (usage-based)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: SEPA Direct Debit
Local_M_4: BLIK
Local_M_5: iDEAL
Local_M_6: GoPay
Local_M_7: Boleto
Local_M_8: OXXO
Local_M_9: Konbini
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: NOVA Anti-Fraud

Desc_Yuno_Cap1: Route each Pro subscription and usage overage to the optimal acquirer for that card BIN, issuer, and geography. At $200M+ ARR with 82% YoY growth, a 3% auth uplift recovers $6M+ in annual revenue. Every basis point matters at scale.
Desc_Yuno_Cap2: Automatic cascade eliminates Vercel's single-processor dependency. When Stripe declines a renewal or overage charge, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions, protecting recurring revenue for 40M developers.
Desc_Yuno_Cap3: Unlocks payment in every market where Vercel deploys infrastructure: UPI in India, Pix in Brazil, SEPA DD across Europe, BLIK in Poland, iDEAL in Netherlands, OXXO in Mexico, Konbini in Japan. One API, 1,000+ payment methods. Match global infra with global payments.
Desc_Yuno_Cap4: AI-powered fraud engine reducing false positives by up to 75%. Critical for Vercel's usage-based model where legitimate developers get blocked by blunt fraud rules, losing both the developer and their ongoing compute spend.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Vercel at a glance:**
- 40M+ developers, powers 4M+ websites worldwide
- Revenue: $200M ARR (2025), up 82% YoY from $100M (2024). Growth: $70M (April 2025), $100M (June), $150M (September)
- Valuation: $9.3B (Series F, September 2025, $300M raised co-led by Accel + GIC)
- Total funding: ~$863M to date
- Creator of Next.js framework (used by ChatGPT, TikTok, Notion)
- v0: AI code generation product, 4M+ users, $20/mo premium tier
- Pricing: Hobby (free, non-commercial), Pro ($20/user/mo), Enterprise (custom)
- Global CDN: 126 PoPs in 94 cities across 51 countries, 20 compute-capable regions
- CEO: Guillermo Rauch. HQ: San Francisco. ~823 employees
- Enterprise clients include GitHub, Uber, Hulu, Twilio, Shopify

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed via privacy policy and billing documentation)
- Stripe Billing: handles usage-based metering for compute, bandwidth, storage
- March 2026: Stripe became generally available on Vercel Marketplace
- Pro plan: credit/debit card only. Gift cards, prepaid cards, virtual cards explicitly rejected.
- Enterprise: credit card via Stripe, ACH available for Enterprise only
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest developer market)
  Accepted: Visa/MC/Amex (USD), ACH (Enterprise only)
  Missing: Cash App Pay, Venmo
  Note: Primary revenue market. v0 driving strong consumer-like adoption among developers.

MARKET 2: India (large developer community)
  Accepted: Visa/MC (international USD)
  Missing: UPI, RuPay, NetBanking, Paytm
  Note: India is a major Next.js developer market. GIC (Singapore sovereign fund) co-led Series F, signaling Asia expansion focus.

MARKET 3: Europe (London, Frankfurt, Amsterdam PoPs)
  Accepted: Visa/MC/Amex (USD)
  Missing: SEPA Direct Debit, iDEAL, BLIK, Sofort, Bancontact
  Note: European developers are core Next.js users. SEPA DD is standard for SaaS subscriptions in EU.

MARKET 4: Brazil (growing developer market)
  Accepted: Visa/MC (USD)
  Missing: Pix, Boleto, local installment cards
  Note: Next.js adoption growing across LATAM. Pix covers 70%+ of digital payments in Brazil.

MARKET 5: Japan/Asia Pacific (Tokyo, Sydney, Singapore PoPs)
  Accepted: Visa/MC (USD)
  Missing: Konbini, PayPay, Line Pay, GrabPay
  Note: Tokyo PoP serves strong Japanese developer community. Konbini payments are essential for Japan.

**Key meeting angles:**
1. **$9.3B infrastructure company** | Vercel deploys globally but collects payment like a US-only startup. 126 PoPs, zero local APMs.
2. **v0 is a new revenue engine** | 4M+ users, $20/mo premium. Consumer-like product needs consumer payment methods.
3. **GIC co-led Series F** | Singapore sovereign wealth fund signals Asia expansion. Payment methods must follow.
4. **Usage-based billing at scale** | Compute/bandwidth overages on variable amounts face higher international decline rates.
5. **Explicit card restrictions** | Prepaid, gift, and virtual cards rejected. This filters out developers in cash-heavy markets.
6. **Stripe Marketplace GA** | March 2026 Stripe GA on Vercel Marketplace deepens the relationship but also the dependency.
7. **Next.js ecosystem** | Powers ChatGPT, TikTok, Notion. The framework's global adoption outpaces Vercel's payment reach.

**Sources:**
- [Vercel Privacy Policy](https://vercel.com/legal/privacy-policy)
- [Vercel Pricing](https://vercel.com/pricing)
- [Vercel Pro Plan Billing FAQ](https://vercel.com/docs/accounts/plans/pro/billing)
- [Vercel Enterprise Billing FAQ](https://vercel.com/docs/plans/enterprise/billing)
- [Vercel Brand Assets](https://vercel.com/geist/brands)
- [Vercel Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Vercel_logo_black.svg)
- [Vercel Global Regions](https://vercel.com/docs/regions)
- [Vercel Blog: Series F](https://vercel.com/blog/series-f)
- [Vercel Changelog: Stripe GA on Marketplace](https://vercel.com/changelog/stripe-is-now-generally-available-on-the-marketplace-and-v0)
- [Sacra: Vercel Revenue & Valuation](https://sacra.com/c/vercel/)
- [GetLatka: Vercel Revenue](https://getlatka.com/companies/vercel)
- [TapTwice: Vercel Statistics](https://taptwicedigital.com/stats/vercel)
- [SaaStr: Vercel's Path to $9.3B](https://www.saastr.com/how-vercel-hit-9-3b-and-replit-hit-3b-after-a-decade-the-long-paths-to-ai-overnight-success/)
- [Shipper: Vercel & v0 Statistics](https://shipper.now/vercel-v0-stats/)
- [Feature Asia: Vercel $300M with Asia Backing](https://feature-asia.com/feature/spotlight/feature-asia-vercel-300m-funding/)
- [SchematicHQ: Vercel Pricing Explained](https://schematichq.com/blog/vercel-pricing)
