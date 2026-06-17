# GITHUB | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: GitHub
=======================================

Logo: https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png
Nombre merchant: GitHub

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: India RBI Recurring Block
Tittle_Pain Point_2: Card-Only Checkout Wall
Tittle_Pain Point_3: Cross-Border Decline Spike
Tittle_Pain Point_4: Single Acquirer Exposure
Tittle_Pain Point_5: Involuntary Sub Churn

Desc_Pain Point_1: RBI mandates block auto-debit on Indian cards, killing Copilot and Pro renewals. GitHub built a temporary one-time payment workaround but developers still churn when banks decline recurring charges.
Desc_Pain Point_2: Only credit cards and PayPal accepted globally. No UPI for India (75%+ of digital payments), no Pix for Brazil, no iDEAL for Netherlands, no BLIK for Poland. Millions of developers locked out.
Desc_Pain Point_3: 180M+ developers in 190+ countries, yet all card transactions route through US-based Stripe acquiring. International issuers decline cross-border charges at 15 to 25pp higher rates than local.
Desc_Pain Point_4: Stripe is the sole payment processor for GitHub billing and Sponsors payouts. Any Stripe outage blocks Copilot, Pro, Teams, Enterprise renewals and creator payouts simultaneously.
Desc_Pain Point_5: With 4.7M paid Copilot subscribers and $2.8B projected revenue, even 5% involuntary churn from failed card payments means $140M+ in lost annual recurring revenue from preventable declines.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Azure Billing (Enterprise)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: iDEAL
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: SEPA Direct Debit
Local_M_7: Bancontact
Local_M_8: Konbini
Local_M_9: GCash
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Copilot and Pro renewal to the optimal acquirer by card BIN, issuer, and country. With $2.8B in projected revenue across 190+ countries, a 3% auth rate uplift from intelligent routing translates to $84M+ in recovered annual revenue for GitHub.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a transaction. Yuno reroutes to the next best acquirer in milliseconds, recovering failed Copilot and Pro renewals without any developer friction. Up to 50% recovery rate on soft declines that currently churn subscribers.
Desc_Yuno_Cap3: Unlocks the methods GitHub developers actually use: UPI for India's 25M+ GitHub users, Pix for Brazil, iDEAL for Netherlands, BLIK for Poland, Konbini for Japan, OXXO for Mexico. One API, 1,000+ payment methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: Single dashboard replacing GitHub's fragmented Stripe billing plus Azure Enterprise plus PayPal settlement streams. Real-time approval rate monitoring, centralized reconciliation, and NOVA anti-fraud reducing false declines by up to 75% across all subscription tiers.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GitHub at a glance:**
- 180M+ registered developers (Feb 2026), up from 100M in early 2025
- 630M+ repositories hosted, 121M new projects added in the last year
- Revenue: $2.8B projected for 2026, 40% YoY growth, with Copilot as the primary growth driver
- Part of Microsoft (acquired 2018 for $7.5B). Reports under Intelligent Cloud segment
- GitHub Copilot: 4.7M paid subscribers (Jan 2026 earnings call), 75% YoY subscriber growth
- Copilot pricing: Free ($0), Pro ($10/mo), Pro+ ($39/mo), Business ($19/user/mo), Enterprise ($39/user/mo)
- GitHub Sponsors: developer-to-developer funding platform, payouts powered by Stripe Connect

**Confirmed PSPs:**
- Stripe: primary processor for all GitHub billing (subscriptions, marketplace, Sponsors payouts). Confirmed via Stripe case study and GitHub Sponsors documentation
- PayPal: secondary option for personal accounts (unmanaged accounts only)
- Azure Billing: available for Enterprise/Organization accounts (Azure Subscription ID linkage)
- No payment orchestrator detected
- Prepaid cards explicitly rejected

**Accepted payment methods (current):**
- Credit cards (Visa, MC, Amex)
- PayPal (personal accounts only)
- ACH (managed accounts only)
- Azure Subscription ID (enterprise only)
- Invoice (managed accounts only)
- NO local APMs in any market

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~30% of developers)
  Accepted: Visa/MC/Amex, PayPal, ACH (enterprise)
  Missing: Cash App Pay, Venmo (direct)
  Note: Core market well served, but ACH restricted to managed accounts limits SMB flexibility.

MARKET 2: India (~14%, 25M+ developers, largest international base)
  Accepted: Visa/MC (recurring blocked by RBI), PayPal (limited)
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: RBI recurring payment mandates block auto-debit. GitHub built a one-time payment workaround but developers still churn. Community forums flooded with complaints.

MARKET 3: Brazil (~5%, growing fast)
  Accepted: Visa/MC (cross-border), PayPal
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of digital payments in Brazil. Zero local payment support for the country's developer community.

MARKET 4: Germany/Europe (~8% combined)
  Accepted: Visa/MC, PayPal
  Missing: SEPA Direct Debit, iDEAL (NL), BLIK (PL), Bancontact (BE), Sofort
  Note: Credit card penetration in Germany is ~35%. SEPA DD is the standard for subscription billing in the Eurozone.

MARKET 5: Japan (~4%)
  Accepted: Visa/MC, PayPal
  Missing: Konbini, PayPay, carrier billing
  Note: Cash-preference culture with 20%+ of online payments at convenience stores (Konbini). PayPay has 60M+ users.

**India payment crisis (documented):**
- RBI regulations on recurring online transactions block auto-debit for Indian-issued cards
- GitHub community discussions #170516, #67932, #30737, #45195 document widespread payment failures
- Workarounds: international virtual cards (HDFC Forex Card, Niyo Global), Apple Pay via iOS app
- GitHub created temporary one-time payment option but the structural problem persists
- Developers report 2+ week support response times with services suspended during the wait

**Key meeting angles:**
1. **India developer crisis** | 25M+ developers, the largest international market, systematically blocked from paying by RBI regulations. UPI integration solves this instantly.
2. **Copilot revenue at risk** | 4.7M paid subs growing 75% YoY. Every percentage of involuntary churn from card failures costs tens of millions.
3. **Microsoft parent precedent** | Microsoft uses Adyen as primary processor. GitHub on Stripe alone creates a gap in the Microsoft payments strategy.
4. **Single point of failure** | Stripe is the sole processor for all of GitHub's $2.8B revenue stream. No failover, no redundancy.
5. **Developer audience alignment** | GitHub's users are the most technically demanding audience. Payment friction directly contradicts the platform's developer-experience mission.
6. **Sponsors payout dependency** | Creator economy payouts also route through Stripe Connect, compounding the single-processor risk.

**Sources:**
- [GitHub Supported Payment Methods](https://docs.github.com/en/billing/reference/supported-payment-methods)
- [GitHub Billing Documentation](https://docs.github.com/en/billing)
- [GitHub One-Time Payments India](https://docs.github.com/en/billing/managing-the-plan-for-your-github-account/one-time-payments-for-customers-in-india)
- [GitHub Sponsors Stripe FAQ](https://github.com/orgs/community/discussions/153919)
- [GitHub Sponsors Additional Terms](https://docs.github.com/en/site-policy/github-terms/github-sponsors-additional-terms)
- [Stripe Case Study: GitHub](https://stripe.com/customers/github)
- [GitHub Blog: Sponsors with Stripe Connect](https://github.blog/2019-09-10-accelerating-the-github-sponsors-beta-with-stripe-connect/)
- [GitHub Community: India Payment Issues #170516](https://github.com/orgs/community/discussions/170516)
- [GitHub Community: Payment Issues India #67932](https://github.com/orgs/community/discussions/67932)
- [GitHub Community: Debit Card India #30737](https://github.com/orgs/community/discussions/30737)
- [GitHub Copilot Plans & Pricing](https://github.com/features/copilot/plans)
- [GitHub Troubleshooting Declined Cards](https://docs.github.com/en/billing/managing-your-github-billing-settings/troubleshooting-a-declined-credit-card-charge)
- [Kinsta: GitHub Statistics 2026](https://kinsta.com/blog/github-statistics/)
- [Fueler: GitHub Revenue & Growth 2026](https://fueler.io/blog/github-usage-revenue-valuation-growth-statistics)
- [GetPanto: GitHub Copilot Statistics 2026](https://www.getpanto.ai/blog/github-copilot-statistics)
