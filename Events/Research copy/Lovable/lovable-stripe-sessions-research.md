# LOVABLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Lovable
═══════════════════════════════════════

Logo: https://cdn.prod.website-files.com/67302d9e6b5a3ea4e25913c5/67302d9e6b5a3ea4e2591488_lovable-logo.svg
Nombre merchant: Lovable

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Link Wallet Dependency
Tittle_Pain Point_2: LATAM Creator Gap
Tittle_Pain Point_3: Hyper-Scale Billing Risk
Tittle_Pain Point_4: Single Processor Lock
Tittle_Pain Point_5: APAC Checkout Friction

Desc_Pain Point_1: 58% of volume runs through Link (Stripe wallet). One wallet controls most of $400M ARR. Any Link issue or policy change is existential risk.
Desc_Pain Point_2: Brazil is the #1 traffic source but has no Pix, Boleto, or OXXO. LATAM devs need USD cards, killing conversion where penetration is under 30%.
Desc_Pain Point_3: $0 to $400M ARR in 16 months. AI credits generate thousands of micro-charges daily. Each failed $1 to $50 charge is direct lost revenue at scale.
Desc_Pain Point_4: Stripe is the sole processor. At $400M ARR across 150+ countries, any incident blocks subscriptions, credit purchases, and Cloud billing.
Desc_Pain Point_5: India, Indonesia, Philippines use Lovable but have zero local APMs. No UPI, no GoPay, no GCash. Users without intl cards cannot pay.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Stripe Link (consumer wallet)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: BLIK
Local_M_4: Boleto
Local_M_5: OXXO
Local_M_6: GoPay
Local_M_7: GCash
Local_M_8: iDEAL
Local_M_9: Konbini
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription and credit purchase to the highest-performing acquirer for that card BIN and geography. At $400M ARR and hyper-growth trajectory, a 3% auth uplift recovers $12M+ annually. Smart Routing optimizes every micro-charge in real time.
Desc_Yuno_Cap2: Automatic cascade eliminates Lovable's total dependency on a single processor. When Stripe declines, Yuno reroutes to the next best acquirer in milliseconds. At 100,000+ new projects daily, even minutes of downtime mean thousands of lost credit purchases.
Desc_Yuno_Cap3: Unlocks the markets where Lovable's builders live: Pix in Brazil, UPI in India, BLIK in Poland, OXXO in Mexico, GCash in Philippines, iDEAL in Netherlands, Konbini in Japan. One API, 1,000+ payment methods. No engineering sprints per country.
Desc_Yuno_Cap4: One dashboard consolidating Stripe + Link into a unified view. Real-time monitoring of approval rates across all 150+ countries, centralized reconciliation for subscription + usage-based + Cloud billing, and anomaly detection that catches revenue leaks instantly.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Lovable at a glance:**
- $400M ARR (February 2026), up from $200M (November 2025), $100M (July 2025)
- 8M+ users (February 2026), 100,000+ new projects created daily
- 6M+ daily visits to Lovable-built sites and apps
- Fastest SaaS company to reach $100M ARR (8 months from launch)
- Founded: November 2024 (Stockholm, Sweden). Opening offices in Boston and SF.
- Pricing: Free (5 daily credits), Starter ($20/mo), Launch ($50/mo), Scale ($100/mo), Enterprise (custom)
- Usage-based credit system for AI code generation
- Valuation: $6.6B (Series B, December 2025, $330M raised by CapitalG + Menlo Ventures)
- Total funding: $530M+ (Series A: $200M at $1.8B led by Accel, July 2025)
- 146 employees as of February 2026
- Clients include Klarna, Delivery Hero, HCA Healthcare

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed via Stripe case study and official documentation)
- Stripe Link: handles 58% of payment volume (Stripe's consumer wallet)
- Stripe Billing: usage-based billing for Lovable Cloud and Lovable AI
- No secondary processor or payment orchestrator detected
- Accepts payments in 150+ countries across 125+ local payment methods (via Stripe)

**Top 5 Markets Gap Analysis:**

MARKET 1: Brazil (core audience per Semrush traffic data)
  Accepted: Visa/MC via Stripe, Link wallet
  Missing: Pix, Boleto, local installment cards
  Note: Lovable.dev's #1 audience country. Pix handles 70%+ of Brazilian digital payments. Massive conversion opportunity.

MARKET 2: United States (second largest market)
  Accepted: Visa/MC/Amex, Link, Apple Pay, Google Pay (via Stripe)
  Missing: ACH for subscriptions, Cash App Pay
  Note: Strong developer adoption. Link wallet dominance (58%) may mask underlying payment diversity needs.

MARKET 3: India (fast-growing developer market)
  Accepted: Visa/MC (international)
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: India's developer community is among the fastest adopters of AI coding tools. UPI is essential for conversion.

MARKET 4: Europe (Stockholm HQ, strong presence)
  Accepted: Visa/MC, Link
  Missing: SEPA Direct Debit, iDEAL (NL), BLIK (PL), Bancontact (BE), Sofort (DE)
  Note: European developers are a natural market for a Stockholm-based company. SEPA DD critical for subscription billing.

MARKET 5: Mexico/Colombia (LATAM expansion)
  Accepted: Visa/MC (USD)
  Missing: OXXO, SPEI (MX), PSE (CO)
  Note: Growing vibe-coding community across LATAM. Cash-based methods like OXXO are essential.

**Key meeting angles:**
1. **Fastest-growing SaaS ever** | $0 to $400M ARR in 16 months. Payment infrastructure must match this trajectory.
2. **Link wallet concentration risk** | 58% of volume through one wallet. Diversification is a business continuity imperative.
3. **Brazil is audience #1** | Largest traffic source has no local APMs. Pix activation alone could materially lift conversion.
4. **100K projects/day** | Each project is a potential credit purchase. Failed payments at this volume compound into millions in lost revenue.
5. **$6.6B valuation, IPO trajectory** | At this scale, payment resilience and multi-processor redundancy become board-level concerns.
6. **Vibe coding ecosystem** | Every app built on Lovable may need payments. Yuno integration in the Lovable ecosystem could drive adoption.

**Sources:**
- [Stripe Customer Story: Lovable](https://stripe.com/customers/lovable)
- [Stripe Newsroom: Lovable and Stripe](https://stripe.com/newsroom/news/lovable-and-stripe)
- [Lovable Pricing](https://lovable.dev/pricing)
- [Lovable Blog: One Year of Lovable](https://lovable.dev/blog/one-year-of-lovable)
- [Lovable Brand Assets](https://lovable.dev/brand)
- [Lovable Docs: Stripe Integration](https://docs.lovable.dev/integrations/stripe)
- [Lovable Series B Announcement](https://lovable.dev/blog/series-b)
- [TechCrunch: Lovable $330M Series B](https://techcrunch.com/2025/12/18/vibe-coding-startup-lovable-raises-330m-at-a-6-6b-valuation/)
- [Bloomberg: Lovable $400M ARR](https://www.bloomberg.com/news/articles/2026-03-12/vibe-coding-startup-lovable-hits-400-million-recurring-revenue)
- [CNBC: Lovable $6.6B Valuation](https://www.cnbc.com/2025/12/16/ai-startup-lovables-round-values-it-at-6point6-billion-sources.html)
- [Sacra: Lovable Revenue & Funding](https://sacra.com/c/lovable/)
- [Semrush: Lovable.dev Traffic Analytics](https://www.semrush.com/website/lovable.dev/overview/)
- [GetLatka: Lovable Revenue](https://getlatka.com/companies/lovable.dev)
- [Panto: Lovable Statistics 2026](https://www.getpanto.ai/blog/lovable-statistics)
