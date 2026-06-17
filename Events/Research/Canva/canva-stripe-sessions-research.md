# CANVA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Canva
═════════════���═════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/3/3b/Canva_Logo.svg
Nombre merchant: Canva

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: Cross-Border FX Leakage
Tittle_Pain Point_3: Subscription Churn Risk
Tittle_Pain Point_4: Checkout Decline Spikes
Tittle_Pain Point_5: Reconciliation Complexity

Desc_Pain Point_1: $3.5B ARR flows through Stripe as the sole acquirer. Any Stripe outage or rate change blocks 100% of Pro, Teams, and Enterprise billing across 190 countries.
Desc_Pain Point_2: 85% of 260M users are outside the US. Brazil (12% traffic) and India (5%) generate high volume but cross-border card fees erode margin on every renewal.
Desc_Pain Point_3: 21M paid subscribers renew monthly or yearly. Failed renewals from cross-border declines or expired cards directly reduce net revenue retention at scale.
Desc_Pain Point_4: Trustpilot and forums report cards declined yet funds withdrawn. International users face "transaction declined" errors despite valid cards and funds.
Desc_Pain Point_5: Stripe handles 40+ localized markets with 20+ APMs, yet one dashboard must reconcile cards, wallets, direct debits, and Pix across every currency and method.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Boleto
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: BLIK
Local_M_5: Konbini
Local_M_6: PSE
Local_M_7: Nequi
Local_M_8: Rapipago
Local_M_9: PagoEfectivo
Local_M_10: Mercado Pago

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and local acquirers by card BIN, issuer, and market. With $3.5B ARR and 21M paid subscribers across 190 countries, even a 3% auth uplift translates to $105M+ in recovered annual revenue. InDrive achieved 90% approval via Yuno routing.
Desc_Yuno_Cap2: Automatic cascade eliminates Canva's single Stripe dependency. When Stripe declines a renewal, Yuno reroutes to the next best acquirer in milliseconds, recovering failed subscriptions with zero friction. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Extends Canva's 20+ APMs with Boleto in Brazil, OXXO and SPEI in Mexico, BLIK in Poland, Konbini in Japan, PSE in Colombia. One API, 1,000+ methods. No engineering sprints per market, covering cash and bank transfer methods Canva currently lacks.
Desc_Yuno_Cap4: One dashboard consolidating Stripe, PayPal, Apple IAP, and Google Play settlement streams. Real-time approval monitoring, centralized reconciliation across 40+ markets, NOVA AI recovering 75% of failed renewals via WhatsApp and phone outreach.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Canva at a glance:**
- Founded: 2013, HQ: Sydney, Australia
- Valuation: $42B (August 2025 employee stock sale)
- Revenue: $3.5B (2025), up 35% YoY from $2.7B in 2024
- Monthly Active Users: 260M (2026), 21M paid subscribers
- Employees: 4,500+
- Operates in 190 countries, platform localized in 100 languages
- 95% of Fortune 500 companies use Canva
- IPO delayed to 2027; pivoting core model to AI credits from feature based tiers
- Recent acquisitions (2024 to 2026): Affinity (UK), Leonardo.Ai (AU), MagicBrief (AU), Mango.AI (US), Cavalry (UK), Ortto (AU), Simtheory
- Five startups acquired in Q1 2026 alone
- CEO: Melanie Perkins (Co-Founder), CFO: Damien Singh, CTO: James Humphreys, COO: Cliff Obrecht (Co-Founder)

**Confirmed PSPs:**
- Stripe: primary PSP since founding (confirmed via Stripe case study). Uses Stripe Payments, Billing, and Payments Intelligence Suite. Jointly localized top 40 markets.
- PayPal: secondary (accepted as standalone payment option)
- Apple App Store: mobile IAP (iOS)
- Google Play: mobile IAP (Android)
- No payment orchestrator detected

**Confirmed Payment Methods (extensive):**
- Credit/debit cards (Visa, MC, Amex)
- PayPal
- SEPA Direct Debit (Europe)
- iDEAL (Netherlands)
- Sofort (Germany)
- Pix (Brazil)
- UPI / UPI Autopay (India)
- GCash (Philippines)
- GoPay, OVO, ShopeePay (Indonesia)
- KakaoPay, Naver Pay (South Korea)
- PayPay (Japan)
- MoMo (Vietnam)
- TrueMoney (Thailand)
- Touch 'n Go (Malaysia)
- GrabPay (Malaysia, Singapore, Philippines)
- M-Pesa (Kenya)
- Apple Pay, Google Pay

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (14.38% of traffic)
  Currently offer: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: ACH, Cash App Pay, Venmo (standalone)
  Impact: US is the largest single market; ACH enables enterprise billing at lower cost.

MARKET 2: Brazil (11.92% of traffic)
  Currently offer: Pix, credit/debit cards
  Missing: Boleto Bancario, local installment cards
  Impact: Boleto covers unbanked population. 30M+ Canva users in Brazil; cash methods expand reach.

MARKET 3: Indonesia (5.9% of traffic)
  Currently offer: GoPay, OVO, ShopeePay
  Missing: QRIS, DANA
  Impact: QRIS is the national QR standard covering all wallets. DANA has 180M+ users.

MARKET 4: Mexico (5.57% of traffic)
  Currently offer: Credit/debit cards
  Missing: OXXO, SPEI
  Impact: OXXO reaches 60%+ of Mexican population via cash. SPEI enables instant bank transfers.

MARKET 5: India (5.26% of traffic)
  Currently offer: UPI, UPI Autopay, credit/debit cards
  Missing: RuPay, Paytm Wallet, PhonePe Wallet
  Impact: RuPay cards are 60%+ of Indian debit cards. Wallet options expand beyond UPI.

**Payment complaint evidence:**
- Trustpilot (1,547 reviews, 1.8 avg on PissedConsumer): unauthorized charges, difficulty canceling subscriptions
- March 2026: user reported card declined twice yet Canva withdrew funds from bank account
- Quora threads: "Why does Canva say transaction declined even though you put in your correct banking information?"
- Canva help center acknowledges cards must be "activated for online and international purchases" suggesting cross-border decline patterns

**Key meeting angles:**
1. **$42B pre-IPO company with single PSP dependency** | $3.5B ARR through one acquirer creates material concentration risk ahead of 2027 IPO
2. **260M users, 190 countries, but gaps in cash and bank transfer methods** | No OXXO in Mexico (#4 market), no Boleto in Brazil (#2 market)
3. **AI credit model transition** | Moving from subscriptions to usage-based AI credits adds billing complexity; orchestration simplifies mixed models
4. **Aggressive M&A integration** | 5 acquisitions in Q1 2026; each acquired company may bring different payment stacks needing consolidation
5. **Subscription churn at scale** | 21M paid subscribers; even 1% improvement in failed renewal recovery = 210K saved subscriptions
6. **Competitor precedent** | Figma (Stripe only), Adobe (multi-PSP); Canva could leapfrog both with orchestration
7. **Stripe relationship preserved** | Yuno sits on top of Stripe, not replacing it. Adds routing intelligence and failover without migration risk

**Sources:**
- [Stripe: Canva Case Study](https://stripe.com/customers/canva)
- [Canva Help: Payment Options](https://www.canva.com/help/payment-options/)
- [Canva Help: Global Payment Methods](https://www.canva.com/help/global-payment-methods/)
- [Canva Help: Pay Using Pix](https://www.canva.com/help/pay-pix/)
- [Canva Help: Pay Using UPI](https://www.canva.com/help/pay-via-upi/)
- [Canva Help: Pay Using iDEAL](https://www.canva.com/help/article/pay-ideal/)
- [Canva Help: Pay Using GCash](https://www.canva.com/help/pay-gcash/)
- [Canva Help: Failed Payments](https://www.canva.com/help/failed-payments/)
- [DemandSage: Canva Statistics 2026](https://www.demandsage.com/canva-statistics/)
- [Backlinko: Canva Users](https://backlinko.com/canva-users)
- [SaaStr: Canva $3.3B ARR](https://www.saastr.com/the-next-great-b2b-ipo-canva-crosses-3-3-billion-arr-42-billion-valuation/)
- [Capital Brief: Canva IPO Delayed to 2027](https://www.capitalbrief.com/article/scoop-cliff-obrecht-confirms-canva-is-now-working-towards-an-ipo-next-year-in-2027-cb530c42-3b29-4793-a7b9-e86f79af7812/)
- [Canva Create 2026: Five Acquisitions](https://www.shashi.co/2026/04/canva-create-2026-what-five.html)
- [Trustpilot: Canva Reviews](https://ca.trustpilot.com/review/canva.com)
- [PissedConsumer: Canva Complaints](https://canva.pissedconsumer.com/complaints/RT-P.html)
- [SpreadThoughts: Canva Users by Country](https://www.spreadthoughts.com/canva-users-by-country-statistics-insights/)
- [TSG Invest: Canva $42B Valuation](https://tsginvest.com/canva/)
