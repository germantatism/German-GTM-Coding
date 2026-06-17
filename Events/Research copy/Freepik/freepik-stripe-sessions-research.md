# FREEPIK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
════════════���══════════════════════════
DATABASE FIELDS: Freepik
═══════════��═══════════════════════════

Logo: https://commons.wikimedia.org/wiki/Special:Redirect/file/FREEPIK_logo.svg
Nombre merchant: Freepik

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: EUR-Only Checkout Wall
Tittle_Pain Point_2: Cross-Border Card Blocks
Tittle_Pain Point_3: No Local APMs in Asia
Tittle_Pain Point_4: Renewal Failure Churn
Tittle_Pain Point_5: Limited PSP Redundancy

Desc_Pain Point_1: All plans charged in EUR only. 80M+ monthly users in 100+ countries absorb FX conversion fees and bank markups on every transaction. Users in India, Brazil, and Southeast Asia pay 3-5% extra just to subscribe.
Desc_Pain Point_2: Spain-based billing triggers international transaction blocks from banks worldwide. Support docs confirm most failed payments come from cards without international/recurring flags enabled. High friction for 40% of new users from Asia.
Desc_Pain Point_3: India is Freepik's #1 traffic source with millions of monthly users. Zero local payment methods: no UPI, no RuPay, no Paytm. 75%+ of Indian digital payments use UPI, yet Freepik only accepts cards and PayPal.
Desc_Pain Point_4: Failed renewals auto-retry 3 times over 21 days then cancel. With 800K+ paid subscribers on recurring billing, every percentage point of renewal failure directly translates to involuntary churn and lost ARR.
Desc_Pain Point_5: Credit cards, PayPal, Google Pay, and Apple Pay accepted but no indication of multi-acquirer routing or failover. A single card processing pipeline means no competitive routing across providers for authorization optimization.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card Processor (undisclosed)
PSP_2: PayPal
PSP_3: Google Pay
PSP_4: Apple Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: BLIK
Local_M_4: GCash
Local_M_5: GrabPay
Local_M_6: DANA
Local_M_7: Boleto
Local_M_8: Konbini
Local_M_9: OXXO
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing optimizes every subscription charge based on card BIN, issuer country, and plan tier. With 800K+ paid subscribers and 80M monthly users across 100+ countries, even a 3% auth uplift on renewals recovers substantial recurring revenue from cross-border declines.
Desc_Yuno_Cap2: Automatic cascade replaces Freepik's single-pipe card processing. When the primary acquirer declines a renewal, Yuno reroutes to the next best processor in milliseconds. Prevents the 21-day retry-then-cancel cycle that drives involuntary churn. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates the APMs Freepik's top markets need: UPI for India (#1 traffic source), Pix for Brazil (#3 market), GCash and GrabPay for Southeast Asia, BLIK for Poland. One API, 1,000+ payment methods. Converts free users who cannot pay with cards today.
Desc_Yuno_Cap4: One dashboard unifying card processing, PayPal, Google Pay, and Apple Pay data. Real-time approval monitoring across all subscription tiers and geographies, centralized reconciliation for Freepik + Flaticon + Slidesgo + Videvo revenue streams. NOVA intelligence delivers 75% faster anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Freepik at a glance:**
- 80M+ monthly users, 800K+ paid subscribers, 100+ countries
- Revenue: estimated $250M to $300M (2025); $69.95M confirmed (2021), rapid growth since EQT acquisition
- Products: Freepik (stock content + AI generation), Flaticon (icons), Slidesgo (presentations), Videvo (video), Magnific.ai (AI upscaling)
- AI scale: 3M AI images and 200K videos generated daily
- 8M+ US monthly users downloading 10M+ assets/month
- Asia = 40% of new user growth (India is #1 traffic source)
- CEO: Joaquin Cuenca Abela (Co-Founder); Co-Founders: Pablo Blanes, Alejandro Sanchez Blanes
- HQ: Malaga, Spain. ~1,600 employees across 6 continents
- Owned by EQT (majority stake acquired May 2020 for 250M+ EUR)
- 21,000+ content collaborators in 100+ countries
- Freemium model: free tier with limits, paid tiers from Essential to Pro
- Charges in EUR only; international/recurring card features required

**Confirmed PSPs:**
- Card processor: not publicly named (likely Stripe or Adyen based on Spain/EU SaaS patterns)
- PayPal: secondary payment option
- Google Pay: accepted
- Apple Pay: accepted (requires international + recurring enabled cards)
- Contributor payouts via PayPal and Payoneer (bank transfer for SEPA countries)
- No payment orchestrator detected

**Payment challenges identified:**
- EUR-only billing forces FX conversion costs on 70%+ of users (majority outside Europe)
- Spain-based billing triggers "international transaction" blocks from non-EU banks
- Support explicitly states: "most failed payments are caused by cards that do not have international/recurring features enabled"
- Auto-retry cycle: 3 retries over 21 days, then auto-cancellation
- No local payment methods in top markets: India (#1), Brazil (#3), Southeast Asia

**Top 5 Markets Gap Analysis:**

MARKET 1: India (#1 traffic source, millions of monthly users)
  Accepted: Visa/MC, PayPal, Google Pay, Apple Pay
  Missing: UPI, RuPay, Paytm, PhonePe, net banking
  75%+ of Indian digital payments use UPI. Massive free-to-paid conversion opportunity blocked.

MARKET 2: United States (8M+ monthly users)
  Accepted: Visa/MC/Amex, PayPal, Google Pay, Apple Pay
  Missing: ACH, Affirm/Klarna BNPL, Cash App Pay
  Well-covered for cards; BNPL would reduce friction on annual plan upgrades.

MARKET 3: Brazil (top 3 market by traffic)
  Accepted: Visa/MC, PayPal
  Missing: Pix, Boleto, local installment cards
  Pix handles 70%+ of Brazilian digital payments. EUR pricing adds further FX barrier.

MARKET 4: Indonesia/Philippines/Thailand (fast-growing SEA markets)
  Accepted: Visa/MC, PayPal
  Missing: GCash, GrabPay, DANA, OVO, PromptPay
  Card penetration under 10% in most SEA markets. Mobile wallets are dominant.

MARKET 5: Poland/Germany/Spain (European core)
  Accepted: Visa/MC, PayPal, Google Pay, Apple Pay
  Missing: BLIK (Poland), SEPA DD (recurring), Bancontact (Belgium), Bizum (Spain)
  BLIK covers 70%+ of Polish online payments. SEPA DD ideal for annual subscriptions.

**Key meeting angles:**
1. **India opportunity** | #1 traffic source with zero local payment methods; UPI activation alone could unlock massive conversion
2. **EUR-only pricing wall** | 70%+ of users outside Europe absorb FX fees on every transaction
3. **Cross-border decline pattern** | Spain-based billing systematically triggers international card blocks globally
4. **800K subscriber base** | Large recurring revenue pool where auth rate optimization has direct ARR impact
5. **AI-driven growth surge** | 3M AI images/day means rapidly growing transaction volume that needs scalable payment infra
6. **EQT growth mandate** | PE ownership means aggressive growth KPIs; payment conversion is low-hanging fruit
7. **Multi-product portfolio** | Freepik + Flaticon + Slidesgo + Videvo need unified payment orchestration

**Sources:**
- [Freepik Help: Payment Methods](https://support.freepik.com/s/article/Payment-methods?language=en_US)
- [Freepik Help: Payment Methods Accepted](https://support.freepik.com/s/article/Payment-methods-accepted-by-Freepik?language=en_US)
- [Freepik Help: Rejected and Declined Payments](https://support.freepik.com/s/article/Rejected-and-declined-payments?language=en_US)
- [Freepik Help: Billing Information](https://support.freepik.com/s/article/Billing-information?language=en_US)
- [Freepik Pricing](https://www.freepik.com/pricing)
- [Freepik AI Docs: Payment Methods](https://www.freepik.com/ai/docs/payment-methods)
- [Tech.eu: Europe's Quiet AI Giant Freepik](https://tech.eu/2025/06/24/europes-quiet-ai-giant-freepik-is-moving-fast-and-taking-market-share/)
- [EQT Portfolio: Freepik](https://eqtgroup.com/about/current-portfolio/freepik)
- [EQT Acquires Freepik](https://eqtgroup.com/news/2020/eqt-acquires-freepik-company-the-global-leading-freemium-provider-of-digital-visual-content/)
- [BusinessWire: Freepik Record Year](https://www.businesswire.com/news/home/20231220808411/en/)
- [Similarweb: Freepik Traffic](https://www.similarweb.com/website/freepik.com/)
- [Freepik Logo](https://commons.wikimedia.org/wiki/File:FREEPIK_logo.svg)
- [Tracxn: Freepik Profile](https://tracxn.com/d/companies/freepik)
