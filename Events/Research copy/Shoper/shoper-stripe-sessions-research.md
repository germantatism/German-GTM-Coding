# SHOPER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Shoper
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id20_Gy3dV/idYNb8qwFZ.svg
Nombre merchant: Shoper

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Stack
Tittle_Pain Point_2: Poland-Locked Checkout
Tittle_Pain Point_3: No Smart Routing Layer
Tittle_Pain Point_4: Cross-Border Auth Gaps
Tittle_Pain Point_5: No Unified Fraud Engine

Desc_Pain Point_1: Merchants juggle PayU, Przelewy24, Tpay, Axepta BNP Paribas, Stripe, and Shoper Payments independently. No orchestration layer unifies routing, reporting, or reconciliation across 6+ PSPs for 20,000+ stores.
Desc_Pain Point_2: Core payment stack built for PLN domestic transactions. Merchants expanding to Germany, Czech Republic, or Western Europe lack native local methods like SEPA DD, Sofort, Bancontact, or Multibanco in their checkout.
Desc_Pain Point_3: Each PSP operates as a siloed integration with no intelligent transaction routing. A declined card on PayU cannot cascade to Stripe or Tpay. Merchants lose sales on every single-attempt failure.
Desc_Pain Point_4: Stripe integration launched July 2025 enables multi-currency cards, but EU shoppers expecting iDEAL, Giropay, or Klarna at checkout still abandon. Card-only cross-border loses 20-40% of local buyers.
Desc_Pain Point_5: Each PSP runs its own fraud rules independently. No centralized fraud scoring across PayU, Stripe, and Przelewy24 transactions. Merchants face inconsistent protection and duplicate chargebacks.

SLIDE 1: PSP TOPOLOGY

PSP_1: PayU (primary Polish gateway, PLN transactions)
PSP_2: Przelewy24 (bank transfers, BLIK, Polish e-wallets)
PSP_3: Stripe (international cards, multi-currency, since July 2025)
PSP_4: Tpay (BLIK on-site, online transfers)
PSP_5: Axepta BNP Paribas (card gateway, split payments)
PSP_6: Shoper Payments (own payment service, 1.69% commission)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: SEPA Direct Debit
Local_M_3: Sofort
Local_M_4: Bancontact
Local_M_5: Giropay
Local_M_6: Multibanco
Local_M_7: Klarna
Local_M_8: EPS
Local_M_9: Trustly
Local_M_10: Swish

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each transaction to the optimal PSP by card BIN, issuer country, and amount. With PLN 21B omnichannel GMV and 20,000+ stores, directing German cards to Stripe while Polish BLIK stays on Tpay delivers 3-10% auth uplift. At this GMV scale, even 3% recovery means hundreds of millions of PLN rescued.
Desc_Yuno_Cap2: Automatic cascade across Shoper's 6 PSPs. When PayU declines a card, Yuno retries through Stripe or Axepta in milliseconds. Up to 50% recovery on failed transactions. No more lost sales from single-attempt processing across 20,000 stores.
Desc_Yuno_Cap3: Activate the European methods Shoper merchants need for cross-border growth: iDEAL (Netherlands), SEPA DD (pan-EU), Sofort and Giropay (Germany), Bancontact (Belgium), Klarna (Nordics), Multibanco (Portugal), Swish (Sweden). One API, 1,000+ methods. No per-market integrations.
Desc_Yuno_Cap4: One dashboard replacing 6 separate PSP admin panels. Unified reporting across PayU, Przelewy24, Tpay, Stripe, Axepta, and Shoper Payments. Centralized reconciliation for PLN 21B GMV, real-time approval rates per country, and NOVA fraud detection (75% reduction) protecting all transactions with a single engine.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Shoper at a glance:**
- Founded: 2005 by Rafal and Krzysztof Krawczyk. HQ: Krakow, Poland (9 Pawia St., 31-154)
- Listed: Warsaw Stock Exchange (WSE: SHO) since July 2021; sWIG80 index member
- IPO valuation: PLN 1.4B (~$350M); offering raised PLN 363M
- Strategic investor: cyber_Folks acquired 49.9% stake for PLN 547.5M (January 2025)
- Revenue 2025: PLN 218M (+13% YoY)
- Adjusted EBITDA 2025: PLN 80M (+21% YoY); margin 36.7%
- Omnichannel GMV 2025: PLN 21B (+45% YoY)
- Q4 2025 omnichannel GMV: PLN 6.5B (+50% YoY)
- Active e-shops: 20,000+ on Shoper platform
- cyber_Folks ecosystem: ~700,000 merchants across Europe (includes PrestaShop)
- Brands: Shoper, Apilo, Sempire
- Employees: 300+ specialists across 4 offices
- Market position: #1 SaaS e-commerce provider in Poland
- Shoper ecosystem accounts for ~1/7 of Allegro ecosystem and 5%+ of entire Polish e-commerce
- Converted from licensed software to SaaS model in 2010
- 80% of new business from word-of-mouth/referrals
- Pricing: Plans from PLN 49/mo to PLN 399/mo
- Key marketplace integrations: Allegro, Amazon, eBay, Empik, OLX

**Confirmed Payment Stack:**
- PayU: Primary Polish payment gateway (PLN-focused, bank transfers, cards)
- Przelewy24: Bank transfers, BLIK integration, Polish e-wallets
- Tpay: BLIK on-site (checkout without leaving store), online transfers, card payments
- Stripe: International payments launched July 2025, multi-currency card support
- Axepta BNP Paribas: Card gateway with split payment capability (min PLN 200)
- Shoper Payments: Own payment service launched 2015 (1.69% commission after 3 months free)
- PayPal: Available through integrations
- BLIK: Available through multiple gateways (Przelewy24, Tpay)
- Apple Pay / Google Pay: Available through select gateways
- No payment orchestrator detected
- No unified routing across PSPs; each gateway operates independently

**Payment Ecosystem Details:**
- Shoper Payments: Own service, 1.69% after introductory period
- PayU: PLN, EUR, USD support
- Tpay: BLIK on-site checkout, returns from admin panel
- Axepta BNP Paribas: Same-day settlements, split payment (card + BLIK or two cards)
- Stripe: Multi-currency, European card brands, digital wallets
- Polish ePlatnosci (PeP): Terminal partnership for physical retail

**Top 5 Markets Gap Analysis:**

MARKET 1: Poland (core market, 90%+ of stores)
  Accepted: BLIK, Przelewy24 bank transfers, PayU, cards, Apple Pay, Google Pay, PayPal
  Missing: Klarna (BNPL growing in Poland), more BNPL options
  Note: Domestic payments well-covered. 54% of Polish e-commerce is BLIK.

MARKET 2: Germany (largest CEE cross-border target)
  Accepted: Visa/MC via Stripe (since July 2025)
  Missing: Sofort, Giropay, SEPA DD, Klarna, PayPal (local), Ratenzahlung
  Note: Germany is Poland's largest trade partner and e-commerce export market. Local methods critical.

MARKET 3: Czech Republic (CEE neighbor expansion)
  Accepted: International cards via Stripe
  Missing: Bank transfers (Czech banks), CSOB, Comgate, GoPay, PayU CZ
  Note: Czech shoppers expect local bank transfer options. Card-only checkout loses buyers.

MARKET 4: Netherlands (Western EU opportunity)
  Accepted: International cards via Stripe
  Missing: iDEAL, Bancontact, SEPA DD
  Note: iDEAL dominates Dutch e-commerce at 60%+ share. Without it, Dutch checkout is broken.

MARKET 5: Nordics / Western Europe (growth frontier)
  Accepted: International cards via Stripe
  Missing: Swish (Sweden), MobilePay (Denmark), Vipps (Norway), Trustly, Klarna
  Note: Nordic markets have 80%+ digital payment adoption. Local wallets are essential.

**Key meeting angles:**
1. **PLN 21B GMV with 6 unorchestrated PSPs** | Each gateway is a silo. No routing, no failover, no unified fraud. Massive efficiency opportunity.
2. **Cross-border is the growth play** | Stripe added July 2025, but cards alone miss 60%+ of German/Dutch/Nordic shoppers who prefer local methods.
3. **700K merchant ecosystem via cyber_Folks** | PrestaShop + Shoper creates one of Europe's largest SaaS e-commerce groups. Payment orchestration scales across the entire fleet.
4. **"Operating system for e-commerce" vision** | Shoper's own words. Payment orchestration is the missing layer to make this real across borders.
5. **BLIK success proves local method power** | 54% of Polish e-commerce uses BLIK. Shoper merchants need the same local method coverage in every target market.
6. **Record profitability enables investment** | 36.7% EBITDA margin, dividend payer. Financial capacity to invest in payment infrastructure.
7. **Competitor pressure** | Shopify offers Shop Pay globally; WooCommerce merchants can add any gateway. Shoper merchants need parity for cross-border.

**Sources:**
- [Shoper Investor Relations: About Us](https://investors.shoper.pl/en/about-us)
- [Shoper: Stripe International Payments Launch](https://investors.shoper.pl/en/press-office/shoper-wprowadza-dla-wszystkich-sprzedawcow-miedzynarodowe-platnosci-stripe)
- [Shoper: Tpay Partnership](https://investors.shoper.pl/en/press-office/tpay-shoper)
- [Shoper: Axepta BNP Paribas Integration](https://investors.shoper.pl/en/press-office/shoper-rozwija-oferte-platnosci-bramka-platnicza-axepta-bnp-paribas-juz-dostepna-dla-klientow-spolki)
- [Shoper: ePlatnosci Terminal Partnership](https://investors.shoper.pl/en/press-office/shoper-i-eplatnosci)
- [Shoper: Q1 2025 Financial Results](https://investors.shoper.pl/en/press-office/wyniki-finansowe-q1-2025---komunikat)
- [Shoper: Q4 2025 Financial Results](https://investors.shoper.pl/en/press-office/wyniki-finansowe-q4-2025---komunikat)
- [Shoper: cyber_Folks Acquisition](https://investors.shoper.pl/en/press-office/cyber-folks-nabywa-49-9-akcji-shopera)
- [Shoper: Record Year PLN 4B GMV](https://investors.shoper.pl/en/press-office/shoper-podsumowuje-rekordowy-rok-juz-4-mld-zl-gmv)
- [Shoper: Shoplo Acquisition](https://investors.shoper.pl/en/press-office/shoper-przejmuje-shoplo-i-zwieksza-udzial-w-rynku)
- [Shoper: IPO on Warsaw Stock Exchange](https://investors.shoper.pl/en/press-office/shoper-zadebiutowal-na-rynku-glownym-gieldy-papierow-wartosciowych)
- [Shoper: Financial Results Q1 2024](https://investors.shoper.pl/en/press-office/rekordowa-rentownosc-shopera-w-q1-2024-sklepy-shoper-napedzaja-polski-rynek-e-commerce)
- [E-Commerce News EU: Shoper Launches Own Payment System](https://ecommercenews.eu/polish-ecommerce-platform-shoper-launches-its-own-payment-system/)
- [PayU Poland: Shoper Integration](https://poland.payu.com/our-solutions/payments-for-e-commerce/shoper/)
- [Robert Ditrych: Shoper IPO Deep Dive](https://robertditrych.substack.com/p/shoper-ipo-deep-dive-on-polish-shopify)
- [Kubang Pasu Capital: Shoper Analysis](https://kubangpasucapital.substack.com/p/shoper-sa-the-shopify-of-poland-trading)
- [Asttero: Shoper Review 2024](https://www.asttero.com/en/blog/post/shoper-review-2024)
- [Fenige: Shoper Features](https://www.fenige.com/blog/shoper-what-is-it-and-what-features-does-it-offer)
- [Brandfetch: Shoper Logo](https://brandfetch.com/shoper.pl)
- [Poland Insight: cyber_Folks Acquires Shoper](https://polandinsight.com/cyber_folks-to-acquire-49-9-stake-in-shoper-s-a-for-pln-547-5-million-22573/)
- [StoreleadsApp: Shoper Poland Report](https://storeleads.app/reports/shoper/PL/top-stores)
