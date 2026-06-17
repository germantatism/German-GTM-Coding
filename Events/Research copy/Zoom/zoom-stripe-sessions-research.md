# ZOOM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Zoom
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/2/2a/Zoom_Communications_Logo.svg
Nombre merchant: Zoom

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Involuntary Churn Drain
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: Cross-Border FX Markup
Tittle_Pain Point_5: Manual Rollout Bottleneck

Desc_Pain Point_1: Stripe, Zuora, and PayPal run as disconnected systems. No unified routing, no centralized approval monitoring, no single reconciliation dashboard for $4.87B in revenue.
Desc_Pain Point_2: Zoom retries declines via Stripe but has no multi-acquirer failover. Each soft decline with no backup route is a lost seat license and recurring revenue gone forever.
Desc_Pain Point_3: 300M+ users in 180+ countries but only a handful of local APMs added recently. Mexico, Colombia, Turkey, Thailand, and Egypt still have zero local coverage.
Desc_Pain Point_4: Enterprise customers in 18+ currencies absorb FX fees on every renewal. Without local acquiring, cross-border interchange inflates the true cost per seat globally.
Desc_Pain Point_5: Zoom adds roughly one new payment method per month via Stripe. Scoping, compliance, and engineering per method limits speed for 180+ countries.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Zuora (billing/subscription)
PSP_4: Apple App Store
PSP_5: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: PSE
Local_M_3: Boleto
Local_M_4: SPEI
Local_M_5: Nequi
Local_M_6: TrueMoney
Local_M_7: Fawry
Local_M_8: Bizum
Local_M_9: Bancontact
Local_M_10: Dana

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, PayPal, and additional acquirers by BIN, issuer, and geography. With $4.87B revenue and 504,900 customers, a 3% auth uplift on seat renewals recovers tens of millions in ARR per year.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Yuno reroutes to the next best acquirer in milliseconds, turning failed seat renewals into recovered revenue. Up to 50% recovery on soft declines, directly reducing involuntary churn.
Desc_Yuno_Cap3: Activates APMs Zoom has not yet reached: OXXO and SPEI in Mexico, PSE in Colombia, Boleto in Brazil, TrueMoney in Thailand, Fawry in Egypt, Bizum in Spain. One API, 1,000+ methods, instant geo-routing. No month-by-month rollout.
Desc_Yuno_Cap4: One dashboard replacing Zoom's fragmented Stripe + PayPal + Zuora streams. Real-time approval monitoring, centralized reconciliation across providers and currencies, anomaly detection via NOVA. 75% reduction in payment ops overhead.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Zoom at a glance:**
- 300M+ daily meeting participants, 504,900 business customers, 180+ countries
- Revenue: $4.87B (FY2026, ended Jan 2026), up 4.4% YoY. Gross margin 77%
- 2,278+ enterprise customers contributing $100K+ annually
- 70% of Fortune 100, 50%+ of Fortune 500 use Zoom
- 3.3 trillion annual meeting minutes, 45B+ annual webinar minutes
- Market share: 55.9% of global video conferencing (vs. Microsoft Teams at 32.3%)
- ~8,484 employees. Public company (NASDAQ: ZM)

**Confirmed PSPs:**
- Stripe: primary card acquirer (confirmed via Stripe case study page, Zoom support docs, and marketplace integration)
- Zuora: subscription billing and management platform (confirmed, Zoom adopted Zuora in 2015)
- PayPal: secondary payment option for subscriptions and events
- Apple App Store: iOS mobile purchases
- Google Play: Android mobile purchases
- No payment orchestrator detected

**Payment Methods Currently Accepted:**
- Global: Visa, Mastercard, Amex, Discover, JCB, PayPal, Apple Pay, Google Pay
- US: ACH, Klarna
- Europe (15 countries): Klarna
- SEPA Zone: SEPA Direct Debit
- Netherlands: iDEAL
- Poland: Przelewy24 (P24) / BLIK
- Japan: Furikomi
- India: UPI
- Philippines: GCash
- South Korea: KakaoPay
- Vietnam: MoMo Pay
- Brazil: Pix
- Manual: wire/bank transfer, EFT, checks ($250+ monthly minimum)

**Top Markets by Customer Distribution:**
- United States: 69.1% of enterprise customers (121,263)
- Germany: 7.5% (13,172)
- United Kingdom: 6.6% (11,663)
- Japan: significant market (Furikomi added)
- India: growing rapidly (UPI added)
- Brazil: key LATAM market (Pix added)

**Key Stripe Case Study Insights:**
- Zoom rolls out approximately one new payment method per month through Stripe
- iDEAL displaced 20% of international credit card transactions in the Netherlands since launch
- P24 reaches 72% of Polish online shoppers
- Stripe Adaptive Acceptance used for payment retry optimization
- Stripe Sigma for data analytics, Stripe Radar for fraud

**Payment Issues Documented:**
- Community forums show recurring "payment declined" complaints, especially from international users
- Cross-border card transactions trigger security blocks frequently
- Users report browser-specific payment failures
- BIN selection and recurring billing support are common failure causes
- No multi-acquirer failover exists; all card declines depend on Stripe retry logic alone

**Key Meeting Angles:**
1. **Orchestration gap**: Stripe + Zuora + PayPal with no unified routing layer. Yuno sits on top of all three
2. **Scale = massive uplift**: At $4.87B revenue, even 1% auth improvement = $48M+ recovered
3. **Linear APM rollout**: One method/month is too slow for 180+ countries. Yuno activates 1,000+ via single API
4. **iDEAL proof point**: 20% card displacement in Netherlands proves local APMs convert. Now replicate across 20+ markets
5. **Enterprise retention**: Involuntary churn from declined renewals directly impacts net revenue retention, a metric Wall Street watches closely
6. **LATAM + APAC white space**: Mexico, Colombia, Thailand, Egypt, Turkey have zero local coverage despite user presence

**Sources:**
- [Stripe Case Study: Zoom](https://stripe.com/customers/zoom)
- [Zoom Payment Methods Support](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0061567)
- [Zoom Billing and Account Support](https://support.zoom.com/hc/en/billing-and-account?id=billing_and_account)
- [Zoom Investor Relations](https://investors.zoom.us/)
- [Zoom FY2025 Financial Results](https://www.globenewswire.com/news-release/2025/02/24/3031536/0/en/Zoom-Communications-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results.html)
- [MacroTrends: Zoom Revenue](https://www.macrotrends.net/stocks/charts/ZM/zoom-communications/revenue)
- [DemandSage: Zoom Statistics 2026](https://www.demandsage.com/zoom-statistics/)
- [6sense: Zoom Market Share](https://6sense.com/tech/video-conferencing/zoom-market-share)
- [Zoom Community: Declined Payments](https://community.zoom.com/t5/Billing-Account-Management/SOLVED-Declined-payments/m-p/152220)
- [Zoom Community: Payment Not Going Through](https://community.zoom.com/t5/Billing-Account-Management/Payment-not-Going-Through/m-p/831)
- [Payments by Stripe for Zoom Marketplace](https://marketplace.zoom.us/apps/cO9EIkTfQ3q695Y89jbSGg)
- [Wikimedia: Zoom Communications Logo](https://commons.wikimedia.org/wiki/File:Zoom_Communications_Logo.svg)
