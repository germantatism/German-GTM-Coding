# MOZILLA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Mozilla
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/3/3f/Mozilla_2024_logo.svg
Nombre merchant: Mozilla

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Google Revenue Dependency
Tittle_Pain Point_2: Subscription Geo-Blocks
Tittle_Pain Point_3: Cross-Border Card Decline
Tittle_Pain Point_4: Multi-Channel Reconcile
Tittle_Pain Point_5: Churn on Renewal Failure

Desc_Pain Point_1: 86% of $593M revenue is Google search deals. VPN, Relay, and Monitor subs are the diversification path, but payment friction limits growth in 34 countries.
Desc_Pain Point_2: Mozilla VPN is purchasable in only 34 countries. Stripe Radar blocks unsupported regions. Users in LATAM, Africa, and most of Asia cannot subscribe.
Desc_Pain Point_3: Users report "currency not valid for your country" errors. Cross-border card declines block subscribers. Forums show failed payments despite valid cards.
Desc_Pain Point_4: Four billing channels (Stripe, PayPal, Apple IAP, Google Play IAP) each with independent settlement, reconciliation, and refund workflows. Fragmented data.
Desc_Pain Point_5: VPN subs auto-renew monthly ($9.99) or annually ($4.99/mo). Failed renewals from expired cards or cross-border declines silently churn subscribers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, web subscriptions)
PSP_2: PayPal (secondary, alternative method)
PSP_3: Apple App Store (iOS IAP)
PSP_4: Google Play (Android IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: OXXO (Mexico)
Local_M_3: SPEI (Mexico)
Local_M_4: UPI (India)
Local_M_5: BLIK (Poland)
Local_M_6: Boleto (Brazil)
Local_M_7: Konbini (Japan)
Local_M_8: GCash (Philippines)
Local_M_9: M-Pesa (Kenya)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each VPN, Relay, and Monitor subscription charge to the optimal acquirer by country and card BIN. With subscribers across 34 countries and international card declines reported, smart routing can uplift authorization 3-10%. InDrive achieved 90% approval via Yuno routing.
Desc_Yuno_Cap2: Automatic cascade across acquirers recovers failed renewals instantly. When Stripe declines a cross-border card or PayPal rejects a recurring charge, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions, directly reducing involuntary churn.
Desc_Yuno_Cap3: Activates Pix and Boleto in Brazil, OXXO and SPEI in Mexico, UPI in India, BLIK in Poland, M-Pesa in Africa. One API, 1,000+ methods. Unlocks subscription revenue in LATAM, Asia, and Africa where Mozilla VPN is currently geo-blocked due to payment limitations.
Desc_Yuno_Cap4: One dashboard consolidating Stripe, PayPal, Apple IAP, and Google Play billing. Real-time reconciliation across all four channels, centralized refund management, and NOVA AI recovering 75% of failed renewals. Replaces fragmented multi-channel billing with unified visibility.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Mozilla at a glance:**
- Founded: 2003 (Corporation), 1998 (Project), HQ: San Francisco, CA
- CEO: Anthony Enzor-DeMeo (appointed December 2025), previously Laura Chambers (interim)
- Employees: ~940
- Revenue: $593M (2023 audited); ~86% from Google search royalties
- Structure: Mozilla Corporation (for-profit, wholly owned by Mozilla Foundation, 501(c)(3) nonprofit)
- Firefox market share: <5% globally (down from 30%+ peak)
- Monthly active users: ~150M Firefox desktop
- Strategic pivot: transitioning Firefox into "modern AI browser"

**Products and subscription services:**
- Firefox: core browser, open source, primary distribution channel
- Mozilla VPN: $4.99/mo (annual) or $9.99/mo (monthly), partnership with Mullvad, 500+ servers in 30+ countries, up to 5 devices
- Firefox Relay: email and phone masking service
- Mozilla Monitor (Pro): identity monitoring and data removal
- Thunderbird: email client (community-maintained)
- MDN Web Docs: web developer documentation (free, community resource)
- Pocket: shut down July 2025
- Note: Mozilla plans to scale back investment in VPN, Relay, and Monitor

**Confirmed PSPs:**
- Stripe: primary payment processor for all web subscriptions (confirmed via FxA Subscription Platform docs)
- PayPal: secondary, uses Stripe's subscription infrastructure with "send_invoice" collection method
- Apple IAP: iOS subscriptions managed outside Stripe, state tracked in Firestore
- Google Play IAP: Android subscriptions with Real-Time Developer Notifications
- No payment orchestrator detected

**Payment methods accepted:**
- Credit/debit cards (via Stripe)
- PayPal (Express Checkout Reference Transactions)
- Apple Pay, Google Pay (via Stripe Checkout)
- Link (Stripe's one-click checkout)
- Apple/Google IAP for mobile

**Mozilla VPN country availability (34 countries):**
- Austria, Belgium, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malaysia, Malta, Netherlands, New Zealand, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, Switzerland, UK, US

**NOT available in:**
- All of Latin America (Brazil, Mexico, Colombia, Argentina, Chile, Peru)
- Most of Asia (India, Japan, South Korea, Indonesia, Philippines, Thailand)
- All of Africa
- Middle East

**Payment complaint evidence:**
- Support forum: "the currency of this subscription is not valid for the country associated with your payment"
- Users report money deducted but no subscription created
- Confusion between cancellation and refund processes (30-day guarantee)
- Apple IAP refunds must go through Apple, not Mozilla
- Payment update page lacks options to change credit card details

**Key meeting angles:**
1. **$593M company needs subscription revenue diversification** | 86% Google dependency is existential risk; VPN/Relay/Monitor subscriptions are the alternative, but payment friction limits growth
2. **34-country limit is a payment problem, not a product problem** | Mozilla VPN works globally once installed. The geo-block is driven by Stripe Radar blocking unsupported regions. Payment orchestration can unlock LATAM, Asia, Africa
3. **4 billing channels, zero unified visibility** | Stripe, PayPal, Apple IAP, and Google Play each have independent settlement and reconciliation. Yuno provides one dashboard
4. **Cross-border card declines killing international growth** | Forum complaints show currency mismatches and declined cards. Smart routing solves this by routing to local acquirers
5. **Involuntary churn on subscription renewal** | Failed renewals on $4.99-$9.99/mo plans silently churn subscribers. Failover and NOVA recovery could save thousands of subscriptions monthly
6. **Open-source mission aligns with orchestration transparency** | Mozilla values openness and user control. Yuno's multi-PSP approach gives Mozilla vendor independence, not lock-in
7. **Stripe relationship preserved** | Yuno sits on top of Stripe, adding routing and failover. No migration needed from existing FxA Subscription Platform

**Sources:**
- [Mozilla Foundation Annual Report 2024](https://www.mozilla.org/en-US/foundation/annualreport/2024/)
- [State of Mozilla 2025](https://stateof.mozilla.org/)
- [Mozilla Corporation Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Corporation)
- [FourWeekMBA: How Mozilla Makes $500M+](https://fourweekmba.com/how-does-mozilla-make-money/)
- [Mozilla Subscription Platform Docs](https://mozilla.github.io/ecosystem-platform/tutorials/subscription-platform)
- [Mozilla FxA Subscription Platform Overview](https://mozilla.github.io/ecosystem-platform/relying-parties/reference/sub-plat-overview)
- [Mozilla VPN Countries Available](https://support.mozilla.org/en-US/kb/mozilla-vpn-countries-available-subscribe)
- [Mozilla VPN Billing Help](https://support.mozilla.org/en-US/products/mozilla-vpn/billing-and-subscriptions/manage-billing)
- [Mozilla VPN Wikipedia](https://en.wikipedia.org/wiki/Mozilla_VPN)
- [Security.org: Mozilla VPN Pricing 2026](https://www.security.org/vpn/mozilla/)
- [Mozilla VPN Refund Support](https://support.mozilla.org/en-US/kb/how-do-i-request-refund-mozilla-vpn)
- [Mozilla Support: Payment Issues](https://support.mozilla.org/en-US/questions/1345090)
- [Mozilla Support: Payment Info Update Issues](https://support.mozilla.org/en-US/questions/1302332)
- [GitHub: Mozilla FxA Issues](https://github.com/mozilla/fxa/issues/1071)
- [TechCrunch: Mozilla Downsizes](https://techcrunch.com/2024/02/13/mozilla-downsizes-as-it-refocuses-on-firefox-and-ai-read-the-memo/)
- [TechCrunch: Mozilla New CEO](https://techcrunch.com/2025/12/17/mozillas-new-ceo-says-ai-is-coming-to-firefox-but-will-remain-a-choice/)
- [Wikimedia: Mozilla 2024 Logo](https://commons.wikimedia.org/wiki/File:Mozilla_2024_logo.svg)
