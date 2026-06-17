# GIVEBUTTER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: GiveButter
=======================================

Logo: https://brandfetch.com/givebutter.com
Nombre merchant: GiveButter

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Processing
Tittle_Pain Point_2: Recurring Decline Drain
Tittle_Pain Point_3: Single Acquirer Lock-In
Tittle_Pain Point_4: Zero Global APMs
Tittle_Pain Point_5: Cross-Border Fee Burden

Desc_Pain Point_1: All donations processed exclusively in USD. International donors from 180+ countries absorb bank FX conversion fees, adding 2-4% friction that reduces net donation value and deters repeat giving from non-US supporters.
Desc_Pain Point_2: Nonprofits lose 20-30% of monthly recurring donations to failed card payments. Expired cards, soft declines, and insufficient funds silently erode sustainer programs. No smart retry or failover path beyond Stripe's built-in retries.
Desc_Pain Point_3: Stripe is the sole payment processor via Stripe Express accounts. Any Stripe outage or decline spike blocks 100% of donation flow. No secondary acquirer, no failover routing, no redundancy for $5B+ in cumulative donations.
Desc_Pain Point_4: Despite accepting donors from nearly every country, zero local payment methods outside US-centric options. No Pix, SEPA DD, iDEAL, Bancontact, or bank transfers for international donor bases that prefer non-card rails.
Desc_Pain Point_5: International donors pay bank FX markup plus Stripe's cross-border fee (1%+). A $100 donation from Germany or Brazil can lose $4-6 in fees. Competing platforms like Fundraise Up already offer multi-currency processing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole card acquirer, Stripe Express/Connect)
PSP_2: PayPal (donor payment option)
PSP_3: Venmo (donor payment option, no recurring)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: SEPA Direct Debit
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: BLIK
Local_M_6: Giropay/Sofort
Local_M_7: OXXO
Local_M_8: Boleto
Local_M_9: Konbini
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each donation through the optimal acquirer based on card BIN, geography, and issuer. With $5B+ in cumulative donations processed and recurring programs growing 31% of online revenue, even a 3% auth rate uplift recovers hundreds of thousands in donations that currently fail silently each month.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a card. Yuno reroutes to the next best acquirer in milliseconds, recovering up to 50% of soft declines. For a platform where nonprofits lose 20-30% of monthly donations to failed payments, failover directly protects sustainer revenue and donor retention.
Desc_Yuno_Cap3: Activates the APMs GiveButter's global donors need: Pix in Brazil, SEPA DD in Germany, iDEAL in the Netherlands, BLIK in Poland, Konbini in Japan, UPI in India, OXXO in Mexico. One API, 1,000+ payment methods, instant geo-routing. No engineering sprint per market.
Desc_Yuno_Cap4: One dashboard replacing GiveButter's fragmented Stripe + PayPal + Venmo settlement streams. Real-time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GiveButter at a glance:**
- #1 rated fundraising platform on G2; founded 2016
- $5B+ in cumulative donations processed (as of March 2025)
- Growth: $1B to $2B in 7 months, $2B to $5B in next 7 months
- 70,000+ nonprofits on the platform
- $50M Series A from Bessemer Venture Partners (BVP Forge Fund) + Ardent Venture Partners (April 2024)
- Profitable as of 2024
- CEO: Max Friedman
- Revenue model: Optional donor tips (covers platform fees) or flat 3% platform fee if tips disabled
- Processing fees: 2.9% + $0.30 per transaction (Stripe standard)
- Payouts: 2-3 business day pending, automated nightly payouts available

**Confirmed PSPs:**
- Stripe: Sole card acquirer (Stripe Express / Stripe Connect accounts). Proprietary relationship. All card, ACH, Apple Pay, Google Pay processed through Stripe
- PayPal: Donor-facing payment option (no separate merchant account needed)
- Venmo: Donor-facing (one-time only, no recurring support)
- Cash App Pay: Donor-facing (USD only, US-based supporters only)
- DAFpay (Chariot): Donor-Advised Fund integration
- No payment orchestrator detected

**Accepted Payment Methods:**
- Visa, Mastercard, Amex, JCB, Discover, Diners Club
- PayPal, Venmo, Cash App Pay
- Apple Pay, Google Pay (device/browser dependent)
- ACH bank transfers
- DAFs via Chariot/DAFpay
- Offline: cash, check, in-kind, stock, property
- Text-to-donate, scan-to-donate, tap-to-pay

**International Limitations:**
- Donations processed exclusively in USD
- Donors can give from nearly any country, but all amounts convert to USD
- Organizations must be US-based or have US bank account + EIN/SSN
- Prohibited countries: Iran, North Korea, Libya, Pakistan, Russia, Saudi Arabia, Somalia, Sudan, Syria
- No local payment methods for any international market
- International donors absorb bank FX conversion fees (2-4% typical)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market)
  Accepted: Visa/MC/Amex/Discover/JCB, PayPal, Venmo, Cash App, Apple Pay, Google Pay, ACH
  Missing: Zelle (growing for P2P donations)
  Note: US-centric platform; most comprehensive coverage here

MARKET 2: United Kingdom (top international donor base)
  Accepted: Visa/MC (via Stripe), PayPal
  Missing: Open Banking (Pay by Bank), Direct Debit, Apple Pay (UK config)
  Note: UK donors face FX conversion to USD. Open Banking growing fast for recurring giving.

MARKET 3: Canada (significant donor base)
  Accepted: Visa/MC, PayPal
  Missing: Interac, local bank transfers
  Note: Canadian donors pay FX fees. Interac is dominant Canadian payment rail.

MARKET 4: Germany / EU (growing diaspora giving)
  Accepted: Visa/MC, PayPal
  Missing: SEPA Direct Debit, Sofort, Giropay, iDEAL, Bancontact
  Note: ~35% card penetration in Germany. SEPA DD is backbone of European subscription/recurring billing.

MARKET 5: Brazil / LATAM (diaspora giving)
  Accepted: Visa/MC, PayPal
  Missing: Pix, Boleto, OXXO, PSE, local debit networks
  Note: Pix processes 4B+ monthly transactions in Brazil. Essential for any Brazilian donor reach.

**Recurring Donation Pain Points:**
- Nonprofits lose 20-30% of monthly donations to failed payments (industry average)
- Monthly giving = 31% of all online nonprofit revenue, growing YoY
- Expired cards, soft declines, insufficient funds are primary failure drivers
- No smart retry logic beyond Stripe's default behavior
- Venmo does not support recurring plans (forces donors to one-time only)
- Card updater services help but do not solve soft declines or issuer blocks

**Competitive Landscape:**
- Fundraise Up: Multi-currency support, AI-powered conversion optimization
- Donorbox: Lower processing fees (2.2% + $0.30 for 501c3s), multi-currency
- Classy/GoFundMe Pro: Enterprise features, peer-to-peer strength
- Every Action: Large nonprofit CRM with integrated payments
- GiveButter differentiates on free pricing model + UX, but lags on international payment infrastructure

**Key meeting angles:**
1. **Recurring revenue protection**: 20-30% of monthly donations fail. Smart routing + failover could recover significant sustainer revenue
2. **International donor ceiling**: $5B+ processed but USD-only. Global diaspora giving blocked by lack of local APMs and FX friction
3. **Single processor risk**: 100% dependency on Stripe. One outage blocks all donation flow for 70,000+ nonprofits
4. **Competitive gap**: Fundraise Up and Donorbox already offer multi-currency. GiveButter risks losing international-focused nonprofits
5. **Growth trajectory**: $1B to $5B in 14 months. Infrastructure must scale. Orchestration prevents single-point-of-failure at scale
6. **Recurring giving growth**: Monthly giving is 31% of online revenue and growing. Failed payment recovery directly protects this growth engine

**Sources:**
- [GiveButter Payment Processing](https://givebutter.com/nonprofit-payment-processing)
- [GiveButter Payment Methods Configuration](https://help.givebutter.com/en/articles/1726573-how-to-configure-payment-methods-on-givebutter)
- [GiveButter Supported Countries & Currencies](https://help.givebutter.com/en/articles/1726542-supported-countries-and-currencies-on-givebutter)
- [GiveButter Pricing](https://givebutter.com/pricing)
- [GiveButter ACH Donations](https://givebutter.com/features/ach-donations)
- [GiveButter Recurring Donations](https://givebutter.com/features/recurring-donations)
- [GiveButter $5B Milestone Press Release](https://www.prnewswire.com/news-releases/givebutter-surpasses-5-billion-in-donations-processed-demonstrating-explosive-growth-in-nonprofit-fundraising-302394860.html)
- [TechCrunch: GiveButter Turning a Profit](https://techcrunch.com/2024/04/27/deal-dive-givebutter-is-turning-a-profit-making-tech-for-nonprofits/)
- [GiveButter $50M Investment Announcement](https://givebutter.com/blog/givebutter-receives-50m-investment)
- [GiveButter Stripe Connect Help](https://help.givebutter.com/en/articles/10401823-how-to-add-and-edit-your-payout-information-with-stripe-connect)
- [GiveButter Stripe Partner Directory](https://stripe.partners/directory/givebutter)
- [NonProfit Times: GiveButter PE Investment](https://thenonprofittimes.com/npt_articles/givebutter-gets-50m-private-equity-investment/)
- [Charity Engine: Recurring Giving Stats](https://blog.charityengine.net/recurring-giving-statistics)
- [Double the Donation: Payment Processing for Nonprofits](https://doublethedonation.com/payment-processing-for-nonprofits/)
- [GiveButter Brand Assets](https://brandfetch.com/givebutter.com)
