# HAPANA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Hapana
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id_s5PAbMc/idJJTbE51F.svg
Nombre merchant: Hapana

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only Dependency
Tittle_Pain Point_2: Franchise Fund Flow Risk
Tittle_Pain Point_3: No LATAM Payment Rails
Tittle_Pain Point_4: Limited APM Coverage
Tittle_Pain Point_5: Cross-Border FX Markup

Desc_Pain Point_1: Stripe is the sole acquirer for $500M+ AUD across 17 countries. Any Stripe outage blocks revenue for 1,000+ fitness clubs and 1M+ members at once.
Desc_Pain Point_2: BFT, Gold's Gym, UFC Gym need complex fund splits across parent, franchisee, and Hapana. Single-PSP setup limits failover for high-stakes flows.
Desc_Pain Point_3: Gold's Gym, UFC Gym, and F45 operate across LatAm. No Pix, OXXO, or Boleto means membership sign-ups blocked in Brazil, Mexico, and Colombia.
Desc_Pain Point_4: Supports BECS (AU/NZ), ACH (US), SEPA DD (EU), Apple Pay, Google Pay. No UPI for India, no Konbini for Japan, no BLIK for Poland expansion.
Desc_Pain Point_5: Sydney entity processes for 17 countries. US, EU, and Asia members pay cross-border interchange on every recurring membership charge, eroding margins.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Connect)
PSP_2: Ezypay
PSP_3: Apple Pay (via Stripe)
PSP_4: Google Pay (via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: UPI
Local_M_4: BLIK
Local_M_5: Konbini
Local_M_6: Boleto
Local_M_7: GCash
Local_M_8: KakaoPay
Local_M_9: PSE
Local_M_10: Naver Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every membership charge to the highest performing acquirer per card BIN, issuer, and country. With $500M+ AUD processed annually across 17 countries, even a 3% auth uplift recovers millions in membership revenue for Hapana and its franchise network.
Desc_Yuno_Cap2: When a recurring membership charge fails on Stripe, Yuno cascades to the next best acquirer in milliseconds. Recovers up to 50% of failed direct debits, cutting involuntary churn for 1M+ gym members and protecting monthly recurring revenue for franchise operators.
Desc_Yuno_Cap3: Unlocks APMs for every market Hapana's fitness brands operate in: Pix in Brazil (Gold's Gym, UFC Gym), OXXO in Mexico, KakaoPay in South Korea (Ezypay expansion), UPI in India, GCash in Philippines. One API, 1,000+ methods, no per-market engineering.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe Connect, Ezypay, and all future PSPs into one view. Real-time auth rate monitoring per franchise location, centralized reconciliation across all countries and currencies, millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Hapana at a glance:**
- Founded: 2014 in Sydney, Australia (originally as OneFitStop)
- CEO/Founder: Jarron Aizen (born South Africa, raised Australia, based in NYC)
- HQ: 276 Pitt St, Level 5, Suite 503, Sydney, NSW 2000, Australia
- Revenue: Strong growth (undisclosed exact figure); processes $500M+ AUD in annual payment volume
- Members on platform: 1M+ fitness club members
- Locations: 1,000+ fitness clubs across 17 countries
- Employees: 80+ globally
- Products: membership management, payment processing, class scheduling, digital analytics, marketing automation, online content, franchise management
- Key clients: BFT (Body Fit Training), Gold's Gym, UFC Gym, KX Pilates, STRONG Pilates, Club Pilates, F45, FS8, Vaura, Air Locker Training, Flex Fitness, Fitstop
- Funding: $17M Series A (Aug 2024, led by OIF Ventures + Bailador); $7.25M (Jan 2026)
- Awards: Jarron Aizen won 2025 Sydney Young Entrepreneur Awards (Fitness category)
- Expansion focus: US and APAC markets; recently entered South Korea with Ezypay

**Confirmed PSPs:**
- Stripe (Connect): primary payment processor; integrated since 2016; processes $500M+ AUD annually
- Stripe Payment Element: added for digital wallets (Apple Pay, Google Pay) and local methods
- Stripe Link: checkout acceleration wallet
- Ezypay: cloud-based direct debit platform; handles recurring DD payments in AU, NZ, South Korea; includes failed payment handling and Tap to Pay terminal
- Apple Pay: via Stripe
- Google Pay: via Stripe
- PayTo: upcoming/planned support (not yet live)
- No payment orchestrator detected

**Payment capabilities documented:**
- BECS Direct Debit (Australia, New Zealand)
- ACH Debit (United States)
- SEPA Direct Debit (Europe)
- Credit/debit card processing via Stripe
- Apple Pay, Google Pay, Link (Stripe wallet)
- Secure hosted payment pages for tokenization
- Multi-currency support
- Refund processing
- Automated billing cycles with failed payment retries
- 43.2% increase in fitness locations since Stripe partnership

**Top Markets Gap Analysis:**

MARKET 1: Australia (home market, largest concentration)
  Offer: BECS Direct Debit, Visa/MC, Apple Pay, Google Pay
  Missing: PayTo (planned but not live), AfterPay/Zip BNPL
  BECS is well-served. PayTo will modernize real-time direct debits.

MARKET 2: United States (active expansion, Fitstop partnership)
  Offer: ACH Debit, Visa/MC, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo
  US is the strategic expansion priority. ACH covers core needs.

MARKET 3: South Korea (new Ezypay expansion market)
  Offer: Ezypay direct debit, Visa/MC
  Missing: KakaoPay, Naver Pay, Samsung Pay, Toss
  Korea's digital wallet penetration exceeds 60%. Card-only is insufficient for gym members.

MARKET 4: Brazil (Gold's Gym, UFC Gym presence)
  Offer: Visa/MC (cross-border only via Stripe)
  Missing: Pix, Boleto, local debit cards
  Pix handles 70%+ of digital payments. Gym memberships are a natural fit for recurring Pix.

MARKET 5: Mexico (UFC Gym, F45 presence)
  Offer: Visa/MC (cross-border only via Stripe)
  Missing: OXXO, SPEI, CoDi
  60%+ unbanked population. OXXO processes 55M+ transactions/month. Essential for mass-market gym access.

**Key meeting angles:**
1. **Single PSP concentration risk**: $500M+ AUD flowing through Stripe alone. Any Stripe incident blocks the entire franchise network.
2. **LATAM fitness expansion**: Gold's Gym, UFC Gym, F45 all operate in LatAm. No local APMs means lost membership sign-ups at scale.
3. **South Korea entry**: Ezypay partnership opened Korea, but no KakaoPay/Naver Pay support leaves a wallet gap.
4. **Franchise fund flow complexity**: BFT, Gold's, UFC require parent/franchisee/platform splits. Multi-PSP orchestration ensures fund flows never fail.
5. **Fresh capital, global ambitions**: $7.25M raised Jan 2026 specifically for global expansion and next-gen platform. Payment infrastructure is the enabler.
6. **Recurring revenue sensitivity**: Gym memberships are 100% recurring. Every failed direct debit is an immediate revenue loss and member churn risk.
7. **Platform revenue model**: Hapana takes a cut of every payment processed. Higher auth rates = more revenue for Hapana itself.

**Sources:**
- [Stripe Case Study: Hapana](https://stripe.com/customers/hapana)
- [Hapana Payment Integrations](https://www.hapana.com/integrations/payment-collections)
- [Hapana $17M Funding](https://www.hapana.com/blog/hapana-investment-software)
- [Hapana $7.25M Funding](https://www.hapana.com/blog/hapana-raises-7-25m-platform-growth)
- [Hapana Gym Payment Software](https://www.hapana.com/blog/gym-payment-software)
- [Hapana Privacy Policy](https://www.hapana.com/privacy-policy)
- [Hapana Ezypay Integration](https://www.ezypay.com/partnerdirectory/hapana)
- [Ezypay + Hapana South Korea Expansion](https://activemgmt.com.au/exciting-news-ezypay-and-hapana-expand-into-south-korea/)
- [Flex Fitness + Ezypay + Hapana NZ](https://ezypay.prowly.com/430561-flex-fitness-selects-ezypay-and-hapana-to-power-operations-across-new-zealand)
- [Hapana Crunchbase](https://www.crunchbase.com/organization/onefitstop)
- [Hapana Fitstop US Expansion](https://insider.fitt.co/press-release/hapana-to-drive-fitstops-ambitious-us-expansion-strategy/)
- [BusinessNewsAustralia: Hapana](https://www.businessnewsaustralia.com/articles/how-fitness-studio-software-hapana-became-a-behind-the-scenes-trainer-to-booming-brands.html)
- [Brandfetch: Hapana Logo](https://brandfetch.com/hapana.com)
