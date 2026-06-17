# DROPBOX | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Dropbox
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/7/78/Dropbox_Icon.svg
Nombre merchant: Dropbox

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Revenue Decline Pressure
Tittle_Pain Point_2: No Payment Failover
Tittle_Pain Point_3: Limited Local Methods
Tittle_Pain Point_4: Cross-Border Auth Friction
Tittle_Pain Point_5: Enterprise Invoice Drag

Desc_Pain Point_1: ARR declined 1.9% to $2.526B. ARPU slipped to $139.68. With 18M+ paying users, even a small auth uplift via multi-processor routing directly reverses revenue contraction.
Desc_Pain Point_2: Braintree is the sole processor with no cascade on decline. When a card fails on renewal for 18M+ subscribers, there is no retry path through an alternative acquirer.
Desc_Pain Point_3: Only cards, PayPal, and direct debit accepted. No Pix, iDEAL, UPI, or BLIK. 700M+ registered users in 180+ countries, but local method absence blocks upgrades.
Desc_Pain Point_4: LATAM, India, and APAC users face cross-border card declines via Braintree. Cards issued outside the US see higher decline rates, impacting conversion in growth markets.
Desc_Pain Point_5: 575K+ Business teams rely on invoicing for large deals. Multi-currency reconciliation is manual. No automated local bank transfer options for enterprise settlement.

SLIDE 1: PSP TOPOLOGY

PSP_1: Braintree / PayPal (primary payment processor)
PSP_2: PayPal (digital wallet option)
PSP_3: Apple App Store / Google Play (mobile subs)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: SEPA Direct Debit
Local_M_7: GiroPay
Local_M_8: Bancontact
Local_M_9: KakaoPay
Local_M_10: SPEI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $2.5B+ revenue, 18M+ paying users across 180+ countries, routing each renewal to the best acquirer per market delivers 3-10% auth uplift. At declining ARR, every recovered transaction counts.
Desc_Yuno_Cap2: Automatic cascade when Braintree declines a subscription renewal. Instead of losing the subscriber to involuntary churn, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions directly reverses ARR contraction.
Desc_Yuno_Cap3: Activates methods Dropbox's global base demands: iDEAL in Netherlands, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, SEPA DD across Europe, SPEI in Mexico, KakaoPay in South Korea. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard unifying Braintree card processing, PayPal wallet, and mobile app store payments. Real-time approval monitoring per country, centralized reconciliation for 575K+ Business teams, and NOVA fraud detection (75% reduction).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Dropbox at a glance:**
- Founded: 2007 by Drew Houston and Arash Ferdowsi. HQ: San Francisco, California
- Public: NASDAQ: DBX
- Revenue: $2.521B (FY2025, ending December 31, 2025), down 1.07% YoY
- Total ARR: $2.526B, down 1.9% YoY (excluding FormSwift: $2.504B, down 0.3%)
- Market cap: ~$5.87B (April 2026)
- Non-GAAP operating margin: 38.2% (Q4 2025, up from 36.9%)
- Paying users: 18.08 million
- Business teams: 575,000+ paying Dropbox Business teams
- Registered users: 700M+ across 180+ countries
- Average revenue per paying user: $139.68
- Employees: 4,023 (February 2026)
- Notable customers: Meta, Humana, StoneX Group, ENEL, Tesco
- Products: Dropbox, Dropbox Business, Dropbox Sign, Dropbox DocSend, Dropbox Replay, Dropbox Dash
- Revenue model: Plus ($11.99/mo), Essentials ($22/mo), Business ($15/user/mo), Business Plus ($24/user/mo), Enterprise (custom)

**Confirmed Payment Stack:**
- Braintree (PayPal): Primary payment processor (historically chose Braintree over Stripe)
- Credit/debit cards: American Express, Discover, MasterCard, Visa
- PayPal: Accepted as a wallet payment option
- Direct Debit: Available in some regions (mentioned in billing docs)
- Apple App Store: iOS subscription management
- Google Play Store: Android subscription management
- Invoicing: Available for Dropbox Business accounts
- No payment orchestrator detected
- No multi-processor failover capability

**Payment Method Gaps (Evidence):**
- No local APMs beyond cards, PayPal, and basic direct debit
- No Pix, iDEAL, UPI, BLIK, Boleto, or other regional methods
- Direct debit availability limited by region (not universally available)
- Changes to billing date only apply to teams paying by credit card, PayPal, or direct debit
- No SEPA Direct Debit explicitly mentioned as an option
- Mobile subscribers locked into App Store/Play Store payment rails
- Enterprise invoicing available but lacks local bank transfer automation

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market by user count)
  Accepted: Visa/MC/Amex/Discover, PayPal, Direct Debit
  Missing: Apple Pay, Google Pay, Venmo, ACH direct
  Note: Most complete coverage with PayPal. But no failover processor on card declines.

MARKET 2: United Kingdom (2nd largest market, 2,076 companies)
  Accepted: Visa/MC, PayPal, Direct Debit
  Missing: Open Banking, Faster Payments
  Note: Direct Debit availability in UK is a positive. But lacks modern open banking options.

MARKET 3: Europe (significant presence, major markets)
  Accepted: Visa/MC, PayPal
  Missing: iDEAL (Netherlands), GiroPay (Germany), SEPA DD, Bancontact (Belgium), BLIK (Poland), Sofort, MB Way
  Note: PayPal helps in Europe, but dominant local methods like iDEAL and SEPA DD are absent. 266 companies in Netherlands alone.

MARKET 4: Brazil / LATAM (192+ companies, growing market)
  Accepted: Visa/MC (cross-border), PayPal
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: Pix processes 70%+ of Brazilian digital payments. PayPal helps but Pix absence is critical.

MARKET 5: India / APAC (497+ companies in India alone)
  Accepted: Visa/MC (cross-border), PayPal
  Missing: UPI, RuPay, Paytm, GrabPay, KakaoPay, LINE Pay
  Note: UPI handles 75%+ of Indian digital payments. 497 companies in India signals untapped potential.

**Key meeting angles:**
1. **$2.5B revenue in decline** | ARR dropped 1.9%. Payment optimization that recovers failed transactions and activates local methods directly reverses contraction.
2. **18M+ paying users with single processor** | Braintree handles all card processing with no failover. Every failed renewal is permanent churn.
3. **700M registered users, 18M paying** | 2.6% conversion rate. Local payment methods in emerging markets unlock upgrades from the 97.4% free tier.
4. **PayPal accepted but not enough** | PayPal is a positive differentiator vs. competitors, but iDEAL, Pix, UPI, and BLIK are essential in their respective markets.
5. **575K+ Business teams** | Enterprise invoicing optimization across multi-currency reconciliation accelerates cash collection.
6. **38.2% operating margin** | Highly profitable company with financial capacity to invest in payment infrastructure
7. **Competitor pressure** | Google Drive, Box, Microsoft OneDrive, and iCloud offer alternative storage with varying payment flexibility

**Sources:**
- [Dropbox Help: Change Billing Information](https://help.dropbox.com/billing/change-information)
- [Dropbox Help: Billing](https://help.dropbox.com/billing)
- [Dropbox Help: Invoices and Receipts](https://help.dropbox.com/billing/invoices-receipts)
- [Dropbox Help: Dropbox Sign Payment Methods](https://help.dropbox.com/billing/dropbox-sign-accepted-payment-method)
- [Dropbox Help: Find Credit Card Charge](https://help.dropbox.com/billing/find-credit-card-charge)
- [Dropbox Forum: Payment Method](https://www.dropboxforum.com/discussions/101001018/payment-method/512750)
- [Dropbox: Q4 FY2025 Results](https://investors.dropbox.com/news-releases/news-release-details/dropbox-announces-fourth-quarter-and-fiscal-2025-results)
- [MacroTrends: Dropbox Revenue](https://www.macrotrends.net/stocks/charts/DBX/dropbox/revenue)
- [Backlinko: Dropbox Usage and Revenue Stats 2026](https://backlinko.com/dropbox-users)
- [SQ Magazine: Dropbox Statistics 2026](https://sqmagazine.co.uk/dropbox-statistics/)
- [Expanding Ramblings: Dropbox Statistics](https://expandedramblings.com/index.php/dropbox-statistics/)
- [Quora: Why Dropbox Chose Braintree Over Stripe](https://www.quora.com/Why-did-Dropbox-choose-Braintree-over-Stripe)
- [Dropbox: Customer Success Stories](https://www.dropbox.com/business/customers)
- [Brandfetch: Dropbox Logo](https://brandfetch.com/dropbox.com)
