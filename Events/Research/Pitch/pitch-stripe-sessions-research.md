# PITCH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Pitch
=======================================

Logo: https://asset.brandfetch.io/idnDAMblAe/idVOLqSCpT.svg
Nombre merchant: Pitch

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cards-Only Checkout Wall
Tittle_Pain Point_2: No Bank Debit for Subs
Tittle_Pain Point_3: Single Acquirer Risk
Tittle_Pain Point_4: Three-Currency Ceiling
Tittle_Pain Point_5: Renewal Decline Leakage

Desc_Pain Point_1: Pitch accepts only credit and debit cards (Visa/Mastercard) via Stripe. No PayPal, no digital wallets, no local APMs. Teams in markets where cards are secondary (Brazil, India, Poland) cannot subscribe without friction.
Desc_Pain Point_2: Subscription SaaS in Europe relies heavily on SEPA Direct Debit for recurring billing. Pitch, a Berlin-based company with strong EU user base, offers no bank debit option, forcing European teams onto cards with higher churn rates.
Desc_Pain Point_3: Stripe is the sole payment processor for all Pitch subscriptions globally. Any Stripe outage or decline spike blocks 100% of new signups and renewals across all tiers (Plus, Team, Business, Enterprise) with zero fallback.
Desc_Pain Point_4: Billing is locked to USD, EUR, and GBP only. Teams in Japan, Brazil, Mexico, India, South Korea, and dozens of other markets pay in foreign currency, absorbing FX markup that inflates the effective price and increases churn risk.
Desc_Pain Point_5: Failed card payments trigger up to 4 automatic retries over 28 days before downgrading to Free. No cascade to an alternate processor or payment method, meaning each failed renewal relies entirely on the same declining card.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: (none detected)
PSP_3: (none detected)
PSP_4: (none detected)
PSP_5: (none detected)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: BLIK
Local_M_5: Bancontact
Local_M_6: UPI
Local_M_7: Giropay
Local_M_8: Boleto
Local_M_9: Konbini
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge and renewal to the best performing acquirer per card BIN, country, and issuer. For a lean, profitable SaaS with $10M+ ARR and users across 134+ countries, a 3-10% auth uplift directly protects recurring revenue without adding engineering headcount.
Desc_Yuno_Cap2: When Stripe declines a Team or Business subscription renewal, Yuno cascades to an alternate acquirer in milliseconds instead of waiting 28 days of retries on the same failing card. Recovers up to 50% of failed charges, cutting involuntary churn on the core revenue stream.
Desc_Yuno_Cap3: Unlocks the local methods Pitch's 134-country user base demands: SEPA DD in Germany and the EU (Pitch's home market), iDEAL in Netherlands, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, Konbini in Japan. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe and any future processors into one view. Real-time auth rate monitoring across every market, centralized reconciliation for EUR/GBP/USD billing, and millisecond anomaly detection via NOVA to protect a subscription base that funds the entire 40-person operation.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Pitch at a glance:**
- Founded: 2018 in Berlin, Germany (by eight co-founders)
- CEO: Nick Blume (since January 2024); Former CEO/Founder: Christian Reber (stepped down Jan 2024)
- Valuation: Peaked at ~$600M (Series B, May 2021); reset after restructuring in 2024
- Total funding raised: $137M+ across 4 rounds (Seed through Series B)
- Investors: Tiger Global, Lakestar, Index Ventures, Thrive Capital
- Revenue: ~$10M ARR (as of Feb 2025, up ~90% YoY from $4.9M at end of 2023)
- Profitable since mid-2024 after restructuring
- Employees: ~40 (down from 180; laid off ~78% in Jan 2024)
- Restructuring: Returned most unspent venture capital to investors pro rata; current and past employees now own 80% of the company
- Users: 2M+ teams worldwide, 134+ countries, 125,000+ workspaces
- Pricing: Free ($0), Plus ($13-15/mo), Team ($19-23/seat/mo), Business ($25-30/seat/mo), Enterprise (custom)
- Notable customers: Pentagram, Thrive Global, Synthesia, Intercom, Slack, Superhuman, Grammarly, Notion
- Remote-first company, "Made in Germany"

**Confirmed PSPs:**
- Stripe: sole payment processor for all subscription billing (confirmed on Stripe customer case study page and Pitch Help Center)
- Credit card information handled entirely by Stripe; Pitch has no access to card data
- No secondary PSP detected
- No payment orchestrator detected
- No local APMs or digital wallets detected on checkout

**Billing details:**
- Accepted: Credit cards (Visa, Mastercard) and debit cards (Visa, Mastercard)
- Alternative methods: Only available for Enterprise subscriptions (30+ seats) via manual contact
- Currencies: EUR (EU + non-EU Europe), GBP (UK), USD (US + rest of world)
- Currency cannot be changed within the app; requires starting a new subscription
- Failed payments: Automatic retry up to 4 times over 28 days; then downgraded to Free plan
- No PayPal, no Apple Pay, no Google Pay, no bank transfers on self-serve plans

**Key payment gaps identified:**
- Cards-only strategy for a product with global ambitions and a Berlin home base
- SEPA Direct Debit absence is notable for a German company billing EU teams
- No local methods in any market despite 134-country presence
- Failed payment recovery relies on retrying the same card; no cascade or alternate processor
- Three-currency limitation forces FX markup on teams in Asia, LATAM, Middle East
- Competitors like Canva accept Pix, UPI, and dozens of local methods globally

**Top Markets Gap Analysis:**

MARKET 1: Germany / DACH (home market, Berlin HQ)
  Offer: Visa/MC via Stripe (EUR billing)
  Missing: SEPA Direct Debit, Giropay/Sofort
  ~35% card penetration in Germany; SEPA DD is standard for subscription billing

MARKET 2: United States (USD billing)
  Offer: Visa/MC via Stripe
  Missing: ACH Direct Debit, Apple Pay, Google Pay
  US teams on annual plans could benefit from bank debit option

MARKET 3: United Kingdom (GBP billing)
  Offer: Visa/MC via Stripe
  Missing: Open Banking, PayByBank, Apple Pay
  UK moving aggressively toward open banking payments

MARKET 4: Brazil (global user base)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: Pix, Boleto
  Pix processes 45B+ transactions/year; primary payment method for digital services

MARKET 5: India (global user base)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: UPI, Netbanking, Paytm
  UPI has 500M+ users; most SaaS purchases in India use UPI

**Key meeting angles:**
1. **Cards-only in card-averse markets**: Berlin-based company with 134-country footprint but only accepts Visa/MC. SEPA DD alone could lift conversion meaningfully in the home market.
2. **Post-restructuring efficiency**: 40-person team needs max revenue per engineer. Yuno adds 1,000+ APMs via single integration instead of per-method engineering sprints.
3. **Involuntary churn protection**: 4 retries over 28 days on the same card is the only recovery mechanism. Failover to alternate acquirer recovers up to 50% of those declines.
4. **Competitive gap vs Canva**: Canva accepts Pix, UPI, iDEAL, and dozens of local methods. Pitch's cards-only approach puts it at a conversion disadvantage in every non-US/EU market.
5. **Profitable and growing**: 90% YoY ARR growth means payment conversion lift has immediate bottom-line impact on a profitable business.
6. **Enterprise upside**: Enterprise plan already negotiates alternative payment methods manually. Automating this with Yuno creates a scalable path.

**Sources:**
- [Pitch Rolls Out Globally with Stripe - Stripe Customer Story](https://stripe.com/customers/pitch)
- [Guide to Billing at Pitch - Help Center](https://help.pitch.com/en/articles/4540282-guide-to-billing-at-pitch)
- [Manage a Paid Subscription - Pitch Help Center](https://help.pitch.com/en/articles/4645938-manage-a-paid-subscription)
- [Pitch Pricing Page](https://pitch.com/pricing/us)
- [Pitch About Page](https://pitch.com/about)
- [Pitch Revenue, Funding & Analysis - Sacra](https://sacra.com/c/pitch/)
- [Pitch Switches CEO, Lays Off Two-Thirds - TechCrunch](https://techcrunch.com/2024/01/08/pitch-christian-reber-venture-funding/)
- [Pitch Series B $85M at $600M Valuation - TechCrunch](https://techcrunch.com/2021/05/20/pitch-a-platform-for-making-and-sharing-presentations-raises-85m-on-a-600m-valuation/)
- [Pitch vs Figma Slides](https://pitch.com/pitch-vs-figma-slides)
- [Pitch Layoffs Analysis - SunsetHQ](https://www.sunsethq.com/layoff-tracker/pitch)
- [Pitch - Crunchbase](https://www.crunchbase.com/organization/pitch-5b94)
- [Pitch - Tracxn](https://tracxn.com/d/companies/pitch/__BbgI_p33m_w39hexTQlrkQDmVVVoWvh-WDX3JO9yKe4)
- [Pitch Raises EUR 69.5M - Silicon Canals](https://siliconcanals.com/pitch-raises-69-5m/)
- [Brandfetch: Pitch Logo](https://brandfetch.com/pitch.com)
