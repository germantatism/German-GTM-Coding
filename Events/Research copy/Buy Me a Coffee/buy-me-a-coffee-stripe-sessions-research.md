# BUY ME A COFFEE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Buy Me a Coffee
═════════════���═════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5a/Buy_Me_a_Coffee_logo.svg
Nombre merchant: Buy Me a Coffee

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single Dependency
Tittle_Pain Point_2: USD-Only Payouts
Tittle_Pain Point_3: Thin APM Coverage
Tittle_Pain Point_4: Cross-Border FX Friction
Tittle_Pain Point_5: No Failover Path

Desc_Pain Point_1: 100% of card transactions run through Stripe with zero backup. Any outage blocks all tips, memberships, and shop purchases for 1M+ creators globally.
Desc_Pain Point_2: All payouts settle in USD regardless of supporter currency. Non-US creators absorb double FX conversion. This erodes the 95% take rate that defines the brand.
Desc_Pain Point_3: Only cards, PayPal, Apple Pay, Google Pay, UPI (India). No Pix, OXXO, BLIK, GCash. Millions of supporters in cash/wallet markets cannot contribute.
Desc_Pain Point_4: 1% surcharge on international transactions plus Stripe FX fees. 78% of traffic is outside the US, so most transactions incur cross-border markups.
Desc_Pain Point_5: No smart retry when payments fail. Declined cards show a generic error with no cascade to another processor. Supporters abandon, creators lose.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: BLIK
Local_M_4: GCash
Local_M_5: Konbini
Local_M_6: Boleto
Local_M_7: Maya
Local_M_8: PSE
Local_M_9: SEPA Direct Debit
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal by card BIN, issuer, geography. With 1M+ creators and millions of supporters, a 3% auth uplift recovers thousands of tips and memberships. Every failed "coffee" is a creator losing support.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a card. Yuno reroutes to the next best acquirer in milliseconds, turning abandoned tip attempts into completed payments. Up to 50% recovery on soft declines. Critical for one-time donations where the supporter will not return to retry.
Desc_Yuno_Cap3: Activates the APMs Buy Me a Coffee supporters need beyond UPI: Pix in Brazil, OXXO in Mexico, BLIK in Poland, GCash in Philippines, Konbini in Japan, iDEAL in Netherlands, PSE in Colombia. One API, 1,000+ payment methods. Converts cash and wallet users into paying supporters.
Desc_Yuno_Cap4: One dashboard replacing Buy Me a Coffee's fragmented Stripe + PayPal settlement streams. Real-time approval rate monitoring per market, centralized reconciliation, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead for a lean 30-person team.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Buy Me a Coffee at a glance:**
- 1M+ creators across 100+ countries, millions of monthly supporters
- Revenue: ~$4.9M platform revenue (5% fee on all transactions)
- 30-person team (lean operation, payment efficiency is critical)
- Founded by Jijo Sunny and Joseph Sunny (brothers)
- Fee model: 5% platform fee + Stripe's 2.9% + $0.30 per transaction + 0.5% payout fee
- Creators keep 95% of earnings (core brand promise)
- Revenue streams: one-time tips ("coffees"), monthly/annual memberships, digital shop, commissions
- Infrastructure: Stripe (PCI Level 1), AWS hosting, Cloudflare

**Confirmed PSPs:**
- Stripe: sole card acquirer (Stripe Standard Connect for payouts, confirmed in help center and partner directory)
- PayPal: secondary payment option for supporters
- Apple Pay: via Stripe
- Google Pay: via Stripe
- UPI (India): via Stripe
- No payment orchestrator detected

**Supporter Payment Methods Currently Accepted:**
- Credit/debit cards (Visa, MC, Amex)
- PayPal
- Apple Pay
- Google Pay
- UPI (India only)
- Localized pricing (multi-currency display) via Stripe

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (22.2% of traffic)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: Venmo, Cash App Pay, ACH
  Note: Relatively well covered as the home market.

MARKET 2: India (6.5%)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay, UPI
  Missing: RuPay, Paytm Wallet, PhonePe
  Note: UPI is live, which is ahead of most competitors. But RuPay and wallet coverage still missing.

MARKET 3: United Kingdom (5.5%)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: Open Banking (Pay by Bank), Amex UK routing
  Note: Open Banking would reduce card processing costs on recurring memberships.

MARKET 4: Spain (3.1%)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: Bizum, SEPA DD, Sofort
  Note: Bizum is Spain's dominant P2P payment method with 25M+ users.

MARKET 5: France (3.0%)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: Carte Bancaire local routing, SEPA DD
  Note: Carte Bancaire is France's domestic card network; local routing reduces interchange.

**Payment challenges:**
- Card declines reported by supporters even with sufficient funds
- International transactions trigger fraud alerts from banks
- Not available in many African and Asian countries (creators must use alternatives like Ko-fi)
- USD-only payouts force non-US creators to absorb FX conversion twice
- No smart retry or failover when payments fail
- 1% international surcharge on 78% of total traffic

**Key meeting angles:**
1. **Lean team, big scale**: 30 employees managing 1M+ creators and millions of supporters. Payment orchestration automates what they cannot staff manually.
2. **95% creator promise**: Brand identity built on low fees, but hidden FX and cross-border costs erode this for non-US creators.
3. **One-time payments need first-try success**: Unlike subscriptions, a failed "coffee" payment means the supporter walks away. No retry opportunity.
4. **India proof point**: Already has UPI. Shows willingness to add local APMs. Natural expansion to Pix, OXXO, BLIK.
5. **Competitor landscape**: Ko-fi (zero fees), Patreon (bigger), GitHub Sponsors. Payment coverage is a differentiator.
6. **78% international traffic**: The platform is fundamentally global, but payment infrastructure is US-centric.

**Sources:**
- [Buy Me a Coffee FAQ](https://help.buymeacoffee.com/en/articles/4539170-frequently-asked-questions)
- [Buy Me a Coffee Stripe Express Payouts](https://help.buymeacoffee.com/en/articles/9770774-understanding-your-payouts-on-buy-me-a-coffee-through-stripe-express)
- [Buy Me a Coffee Payment Charges](https://help.buymeacoffee.com/en/articles/8105744-how-to-calculate-charges-on-your-payment)
- [Buy Me a Coffee Supported Countries](https://help.buymeacoffee.com/en/articles/6258038-supported-countries-for-payouts-on-buy-me-a-coffee)
- [Buy Me a Coffee Multi-Currency](https://help.buymeacoffee.com/en/articles/8837323-multiple-currency-shopping-on-buy-me-a-coffee)
- [Buy Me a Coffee How to Make a Payment](https://help.buymeacoffee.com/en/articles/7982732-how-to-make-a-payment)
- [Buy Me a Coffee Payout Setup](https://help.buymeacoffee.com/en/articles/10025793-how-do-you-set-up-payouts-on-your-buy-me-a-coffee-page)
- [Stripe Partner Directory: Buy Me a Coffee](https://stripe.partners/directory/buy-me-a-coffee)
- [Buy Me a Coffee Pricing 2026 (SchoolMaker)](https://www.schoolmaker.com/blog/buy-me-a-coffee-pricing)
- [Buy Me a Coffee Review (InfluencerMarketingHub)](https://influencermarketinghub.com/buy-me-a-coffee/)
- [Growjo: Buy Me a Coffee Revenue](https://growjo.com/company/Buy_me_a_coffee)
- [Getlatka: Buy Me a Coffee $4.9M Revenue](https://getlatka.com/companies/buymeacoffee.com)
- [SimilarWeb: buymeacoffee.com Traffic](https://www.similarweb.com/website/buymeacoffee.com/)
- [Buy Me a Coffee Brand Assets](https://buymeacoffee.com/brand)
- [Buy Me a Coffee Not Available in Your Country (Medium)](https://medium.com/write-a-catalyst/what-to-do-when-buy-me-a-coffee-is-not-available-in-your-country-f6c2b25d91ae)
