# ANCESTRY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Ancestry
═══════════════════════════════════════

Logo: https://logos-world.net/wp-content/uploads/2021/02/Ancestry-Logo.png
Nombre merchant: Ancestry

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Checkout
Tittle_Pain Point_2: Cross-Border Decline Rate
Tittle_Pain Point_3: No Acquirer Redundancy
Tittle_Pain Point_4: UK Payment Gaps
Tittle_Pain Point_5: Renewal Revenue Leakage

Desc_Pain Point_1: 3.6M+ subscribers limited to Visa, Mastercard, Amex, and Discover. No PayPal in the UK, no SEPA DD in Europe, no Pix in Brazil, no UPI in India. Card-only checkout in 128 DNA-kit countries blocks non-card buyers.
Desc_Pain Point_2: Country-specific sites in 8 markets but subscriptions route through centralized billing. International cards face higher issuer decline rates on cross-border transactions, directly reducing DNA kit conversions.
Desc_Pain Point_3: No multi-acquirer failover path detected. With $1B+ annual revenue from 3.6M recurring subscribers, any processor outage blocks all renewals and new sign-ups simultaneously across every market.
Desc_Pain Point_4: Ancestry UK accepts only Visa, Mastercard, and Barclaycard. No PayPal, no Apple Pay, no BACS Direct Debit, no Open Banking. UK is a top-3 market being underserved with the fewest payment options.
Desc_Pain Point_5: High-value annual subscriptions ($240-$540/year) with recurring billing. Each failed renewal means losing a full year of revenue. Card expiration, issuer blocks, and SCA failures compound involuntary churn.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card processor (Stripe or legacy)
PSP_2: PayPal (US only)
PSP_3: Apple App Store (iOS)
PSP_4: Google Play (Android)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: BACS Direct Debit
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: iDEAL
Local_M_6: Boleto
Local_M_7: Bancontact
Local_M_8: BLIK
Local_M_9: Konbini
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription charge and DNA kit purchase to the highest-performing acquirer by card BIN, issuer, and country. With $1B+ annual revenue from 3.6M subscribers across 128 countries, even a 3% auth uplift recovers $30M+ annually without a single new subscriber.
Desc_Yuno_Cap2: Automatic cascade removes single-processor dependency. When the primary acquirer declines a renewal or DNA kit purchase, Yuno reroutes in milliseconds. Up to 50% recovery on soft declines, protecting high-value annual subscriptions worth $240-$540 each.
Desc_Yuno_Cap3: Activates the APMs Ancestry's global customer base needs: BACS DD in the UK, SEPA DD across Europe, Pix in Brazil, UPI in India, iDEAL in Netherlands, Konbini in Japan. One API, 1,000+ payment methods. No engineering effort per market.
Desc_Yuno_Cap4: One dashboard consolidating card billing, PayPal (US), and app store channels across 8 country-specific sites into a unified view. Real-time approval rate monitoring per market, centralized reconciliation, millisecond anomaly detection. IPO-ready infrastructure.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Ancestry at a glance:**
- Largest for-profit genealogy company in the world. Founded 1983, based in Lehi, Utah
- Revenue: $1B+ annually. 3.6M+ paying subscribers
- 25M+ DNA test users across 128 countries
- Owned by Blackstone (acquired Dec 2020 for $4.7B). GIC (Singapore) holds minority stake
- IPO or sale actively being explored. Banks pitched in Sep 2025. Potential $10B valuation
- CEO: Howard Hochhauser (since Feb 2025, previously CFO/COO)
- ~1,800 employees
- Country-specific sites: US, UK, Australia, Canada, France, Germany, Italy, Mexico, Sweden
- Products: Subscription records access, DNA test kits, family tree builder, AncestryHealth (discontinued)

**Confirmed PSPs and payment methods:**
- US: Visa, Mastercard, Amex, Discover, PayPal, debit cards
- UK: Visa, Mastercard, Barclaycard, debit cards only. No PayPal, no Amex, no Apple Pay
- Australia: Cards (details limited)
- Zip (BNPL) partnership detected for US market
- Apple App Store and Google Play for mobile subscriptions
- Specific card processor not publicly confirmed (likely Stripe or Braintree based on scale)
- No payment orchestrator detected

**Subscription tiers (US pricing):**
- Discovery: $24.99/mo or $19.99/mo (annual)
- World Explorer: $39.99/mo or $29.99/mo (annual)
- All Access: $59.99/mo or $44.99/mo (annual)
- DNA kits: $99-$199 one-time purchase

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, majority of revenue)
  Accepted: Visa/MC/Amex/Discover, PayPal, debit cards, Zip (BNPL)
  Missing: ACH, Cash App Pay, Venmo
  Note: Best served market. PayPal and BNPL available

MARKET 2: United Kingdom (top international market)
  Accepted: Visa, Mastercard, Barclaycard, debit cards ONLY
  Missing: PayPal, Apple Pay, Google Pay, BACS DD, Open Banking, Amex
  Note: Severely underserved. Fewest payment options of any Ancestry market

MARKET 3: Australia (dedicated site ancestry.com.au)
  Accepted: Cards (limited data)
  Missing: BECS Direct Debit, PayTo, POLi, Afterpay
  Note: Australian consumers expect BNPL and direct debit for subscriptions

MARKET 4: Germany/France (dedicated sites)
  Accepted: Cards (likely Visa/MC only)
  Missing: SEPA DD, Sofort, Giropay, iDEAL (NL), Bancontact (BE)
  Note: Only ~35% card penetration in Germany. SEPA DD is essential for European subscriptions

MARKET 5: Mexico (dedicated site)
  Accepted: Cards
  Missing: OXXO, SPEI, Mercado Pago
  Note: 70% of Mexicans lack credit cards. Cash-based payment options essential

**Key meeting angles:**
1. **Blackstone IPO exit** | Active IPO exploration at $10B valuation. Payment infrastructure modernization directly impacts listing narrative
2. **DNA kit conversion** | 128-country DNA distribution but card-only payment. Each missed conversion is a lost lifetime subscriber
3. **UK market paradox** | Top international market with the fewest payment options. No PayPal, no wallets, no Direct Debit
4. **Annual subscription economics** | $240-$540/year plans mean each failed renewal loses substantial recurring revenue
5. **Genealogy tourism model** | Users start with DNA kit (one-time), convert to subscriber (recurring). Both transactions need optimization
6. **Private equity efficiency** | Blackstone owns the company. Payment optimization is a direct lever on EBITDA ahead of exit

**Sources:**
- [Ancestry Wikipedia](https://en.wikipedia.org/wiki/Ancestry.com)
- [Ancestry Subscription Pricing](https://www.ancestry.com/offers/subscribe)
- [Ancestry Payment Update Support](https://support.ancestry.com/s/article/Viewing-and-Updating-Payment-Information)
- [Ancestry UK Payment Methods](https://www.whoacceptsit.com/companies/ancestry-uk/3124/)
- [Ancestry Corporate Logo Library](https://www.ancestry.com/corporate/logos-library)
- [Blackstone Explores $10B Exit](https://finance.yahoo.com/news/blackstone-explores-10b-ipo-sale-205507101.html)
- [Reuters: Blackstone Weighs Ancestry Options](https://finance.yahoo.com/news/exclusive-blackstone-weighs-options-ancestry-100126389.html)
- [Blackstone Acquisition of Ancestry](https://www.blackstone.com/news/press/blackstone-completes-acquisition-of-ancestry-leading-online-family-history-business-for-4-7-billion/)
- [Ancestry IPO Overview (Capital.com)](https://capital.com/en-int/learn/ipo/ancestry-com-ipo)
- [Ancestry Revenue (CompWorth)](https://compworth.com/company/ancestry)
- [Zip BNPL at Ancestry](https://zip.co/us/store/ancestry)
- [Ancestry Australia Billing](https://support.ancestry.com.au/s/article/Finding-Your-Ancestry-Billing-Provider)
