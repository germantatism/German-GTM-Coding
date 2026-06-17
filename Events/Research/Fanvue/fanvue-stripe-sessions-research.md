# FANVUE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Fanvue
═══════════════════════════════════════

Logo: https://brandfetch.com/fanvue.com
Nombre merchant: Fanvue

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Limited Card Networks
Tittle_Pain Point_2: 3DS Friction Wall
Tittle_Pain Point_3: Zero LATAM/APAC APMs
Tittle_Pain Point_4: Fragmented PSP Stack
Tittle_Pain Point_5: High-Risk Acquirer Cost

Desc_Pain Point_1: Only Visa and Mastercard accepted. No Amex, Discover, JCB. 17M+ MAU globally, but excluding major card networks means lost conversions at checkout.
Desc_Pain Point_2: 3DS mandatory on nearly all payments. Fans get ~2 min to verify or it fails. German banks need separate auth apps. Extra friction kills impulse buys.
Desc_Pain Point_3: Only Pix (Brazil) as local APM. No UPI for India, GCash for Philippines, OXXO for Mexico. Top traffic markets have zero local wallet coverage.
Desc_Pain Point_4: Four processors (Primer, OnlineIPS, Axcess PS, TotalProcessing) with no orchestration. No routing, no centralized analytics, no automated failover.
Desc_Pain Point_5: High-risk classification by card networks means higher fees, stricter compliance, fewer acquirers. Without smart routing Fanvue cannot optimize across 4 PSPs.

SLIDE 1: PSP TOPOLOGY

PSP_1: Primer
PSP_2: OnlineIPS
PSP_3: Axcess PS
PSP_4: TotalProcessing

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: GCash
Local_M_3: OXXO
Local_M_4: PSE
Local_M_5: Konbini
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: Maya
Local_M_9: SEPA Direct Debit
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Fanvue's 4 processors (Primer, OnlineIPS, Axcess PS, TotalProcessing). Each subscription and tip routed to the highest-performing acquirer for that card BIN, issuer, and market. With $100M ARR and 17M+ MAU, a 3% auth uplift recovers $3M+ annually.
Desc_Yuno_Cap2: Automatic cascade across all 4 PSPs. When one acquirer declines (common in high-risk), Yuno reroutes in milliseconds to the next best option. Up to 50% recovery on soft declines, critical for a vertical with elevated decline rates.
Desc_Yuno_Cap3: Activates the APMs Fanvue's global fans demand: UPI in India, GCash in Philippines, OXXO in Mexico, PSE in Colombia, Konbini in Japan, BLIK in Poland, iDEAL in Netherlands. One API, 1,000+ payment methods. Extends beyond the single Pix integration currently live.
Desc_Yuno_Cap4: One dashboard replacing 4 fragmented processor integrations. Real-time approval rates per PSP per market, centralized reconciliation, anomaly detection via NOVA. 75% ops reduction. Single view of $100M+ annual volume.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Fanvue at a glance:**
- 17M+ monthly active users, 250,000+ creators, 20,000+ new creators joining monthly
- Revenue: $100M ARR (Jan 2026), up from $40M at end of 2024 (450% YoY growth)
- Scaled from $300K/month (late 2023) to $10M+/month (end 2025)
- Funding: $22M Series A (Jan 2026) for international expansion and AI product development
- Founded 2020, London UK (Shift Holdings LTD). US subsidiary: Fanvue LLC (Dover, Delaware)
- Commission: 15% month 1, 20% month 2+ (creators keep 80-85%)
- AI creators account for ~15% of platform revenue, top AI creators earning $20K+/month
- 93% of creators use at least one AI tool (analytics, voice, content)

**Confirmed PSPs (fan-facing card processing):**
- Primer: payment orchestration/processing partner
- OnlineIPS: card processing partner
- Axcess PS: card processing partner
- TotalProcessing: card processing partner
- All confirmed PCI DSS compliant per Fanvue Terms & Conditions
- MassPay: creator payout partner (100+ countries, crypto/bank/card)
- Cosmo: alternative payout eWallet for restricted banking regions

**Fan Payment Methods Currently Accepted:**
- Visa (credit/debit)
- Mastercard (credit/debit)
- Apple Pay
- Google Pay
- Pix (Brazil only)
- Crypto (via Fanvue wallet)
- NOT accepted: Amex, Discover, PayPal, Zelle, Cash App, bank transfers

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~30% of traffic)
  Accepted: Visa/MC, Apple Pay, Google Pay
  Missing: Amex, Discover, PayPal, Cash App Pay, ACH
  Note: No Amex or Discover excludes millions of US cardholders.

MARKET 2: United Kingdom (~15%)
  Accepted: Visa/MC, Apple Pay, Google Pay
  Missing: Open Banking, PayPal, Amex
  Note: UK base market for the company. Open Banking would reduce card fees.

MARKET 3: Mexico (~8%)
  Accepted: Visa/MC
  Missing: OXXO, SPEI, Mercado Pago
  Note: 70%+ of Mexicans lack credit cards. OXXO cash payments are essential.

MARKET 4: India (~7%)
  Accepted: Visa/MC
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: 75%+ of Indian digital payments use UPI. Card-only checkout excludes the vast majority.

MARKET 5: Germany (~5%)
  Accepted: Visa/MC, Apple Pay, Google Pay
  Missing: SEPA DD, Sofort, Giropay
  Note: German Sparkasse banks require separate 3DS app, causing extra friction.

**Payment challenges specific to Fanvue:**
- High-risk merchant category means elevated decline rates from card issuers
- 3D Secure mandatory on nearly all transactions (adds friction, causes timeouts)
- 4 separate PSPs with no unified routing or failover logic
- Only Visa/MC accepted for cards (no Amex, Discover, JCB)
- Only Pix as a local payment method (single market: Brazil)

**Key meeting angles:**
1. **Explosive growth, fragile payment stack**: $100M ARR on 4 unorchestrated PSPs
2. **High-risk vertical needs smart routing**: Elevated decline rates make failover and intelligent retry critical
3. **Series A expansion**: $22M raised for international growth, but payment coverage does not match the ambition
4. **3DS friction**: Mandatory verification on every transaction kills impulse purchases
5. **India + Mexico opportunity**: Top traffic markets with zero local payment methods
6. **Competitor race**: OnlyFans, Fansly, Passes all competing; payment UX is a differentiator
7. **AI creator monetization**: 15% of revenue from AI creators, growing fast, needs seamless global checkout

**Sources:**
- [Fanvue Payment Methods](https://help.fanvue.com/en/articles/7860539-payment-methods-on-fanvue)
- [Fanvue Payment Issues](https://help.fanvue.com/en/articles/7860518-for-fans-issues-with-adding-a-card-or-making-a-payment)
- [Fanvue Payout Methods](https://help.fanvue.com/en/articles/9508853-payout-methods-available-on-fanvue)
- [Fanvue MassPay eWallet](https://help.fanvue.com/en/articles/9508784-masspay-ewallet-everything-you-need-to-know)
- [Fanvue Creator Earnings & Payouts](https://legal.fanvue.com/creator-earnings-payouts)
- [Fanvue Terms & Conditions (PSP disclosure)](https://legal.fanvue.com/terms-conditions)
- [Fanvue $22M Series A / $100M ARR (BusinessWire)](https://www.businesswire.com/news/home/20260112458975/en/)
- [Fanvue Payout Methods Guide (fanvuemodels.com)](https://fanvuemodels.com/blog/fanvue-payout-methods)
- [Fanvue Review 2026](https://slobodskyi.com/monetize/memberships/fanvue)
- [Fanvue ARR 450% Growth (ARR Club)](https://www.arr.club/signal/fanvue-memo-2026-01-25-26)
- [Sacra: Fanvue Revenue](https://sacra.com/c/fanvue/)
- [Semrush: fanvue.com Traffic](https://www.semrush.com/website/fanvue.com/overview/)
- [Fanvue About Page](https://landing.fanvue.com/about)
