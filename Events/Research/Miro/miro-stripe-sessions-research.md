# MIRO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Miro
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idAnDTFapY/idG6vYsJPg.svg
Nombre merchant: Miro

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Checkout Wall
Tittle_Pain Point_2: Cross-Border Decline Spike
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: Enterprise Invoice Friction
Tittle_Pain Point_5: Marketplace Monetization Gap

Desc_Pain Point_1: Self-serve plans accept only credit cards. No PayPal, iDEAL, SEPA, or bank transfers. Users state it is "the sole reason stopping me from upgrading."
Desc_Pain Point_2: Philippine, LATAM, and emerging market users report multiple cards declined on upgrade. Cross-border auth failures block conversions in growth markets.
Desc_Pain Point_3: Single processor for self-serve subs with no cascade. When a card declines, no retry through an alternative acquirer. Failed renewals churn silently.
Desc_Pain Point_4: Enterprise invoices ($15K+) cannot use credit cards. Only wire or ACH, adding 30-day terms and manual reconciliation on Fortune 100 contracts.
Desc_Pain Point_5: Marketplace has no native monetization. Developers must self-integrate Stripe or Salable. Fragmented billing across 60M+ users limits platform revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (self-serve billing)
PSP_2: Bank Wire / ACH (enterprise invoicing)
PSP_3: Stripe (Marketplace developer payments)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: iDEAL
Local_M_3: SEPA Direct Debit
Local_M_4: GiroPay
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: Pix
Local_M_8: UPI
Local_M_9: Bancontact
Local_M_10: KakaoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $500M ARR and 100M+ users globally, routing each renewal to the best acquirer per market delivers 3-10% auth uplift, translating to $15-50M in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a self-serve renewal. Instead of silently churning a subscriber, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions turns involuntary churn into retained ARR.
Desc_Yuno_Cap3: Activates methods Miro's global base demands: PayPal, iDEAL in Netherlands, SEPA DD across Europe, Pix in Brazil, UPI in India, BLIK in Poland, Bancontact in Belgium, KakaoPay in South Korea. One API, 1,000+ methods. No per-market sprints.
Desc_Yuno_Cap4: One dashboard unifying self-serve Stripe billing, enterprise wire/ACH invoicing, and Marketplace payouts. Real-time approval monitoring per country, centralized reconciliation, and NOVA fraud detection (75% reduction) protecting 130K+ paying accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Miro at a glance:**
- Founded: 2011 (as RealtimeBoard, renamed Miro in 2019). HQ: San Francisco, CA (founded in Perm, Russia)
- Valuation: $17.5B (January 2022, Series C)
- Total funding: $476M over 4 rounds
- Key investors: ICONIQ Capital (led Series B and C), Accel, Atlassian, Dragoneer, GIC, Salesforce Ventures, TCV
- ARR: ~$500M (2026 estimate); Sacra estimated $665M ARR in 2024
- Users: 100M+ worldwide (end of 2025, up from 90M earlier in 2025)
- Paying organizations: 130,000+ paying customers, 250,000+ total organizations
- Enterprise: 99% of Fortune 100 companies use Miro; 20 Fortune 100 contracts worth $1M+ ARR each
- Notable customers: Best Buy, Deloitte, Dell, Shopify, Yamaha, Walt Disney, Ubisoft, PepsiCo, DocuSign, Macy's
- Forbes Cloud 100 (2025)
- User retention: 90%+; average session duration ~45 minutes
- Collaborative whiteboard market: $3.17B (2025), projected 20.85% CAGR through 2030
- Revenue model: Free, Starter ($8/user/mo annual), Business ($16/user/mo annual), Enterprise (custom)
- Data residency: EU, US, and Australia
- Canvas 2026 events: San Francisco, London, Sydney, Tokyo (global reach)

**Confirmed Payment Stack:**
- Stripe: Primary PSP for self-serve credit card billing (Starter and Business plans)
- Stripe: Powers Marketplace developer monetization (Miro + Stripe integration documented)
- Bank Wire (US and international): Enterprise plan invoicing
- ACH: US bank transfers for Enterprise
- Paper Checks: Accepted for Enterprise (mentioned in help docs)
- Salable: Alternative Marketplace monetization platform
- No PayPal, no local APMs, no digital wallets accepted
- No payment orchestrator detected
- Enterprise invoices $15K+ cannot be paid by credit card

**Payment Method Gaps (Community Evidence):**
- PayPal: Requested repeatedly in community forums; NOT accepted. Users state "credit cards are complicated, old-fashioned, very expensive and can be physically stolen or lost"
- iDEAL: Dutch users requesting their dominant local payment method
- GiroPay: German users requesting local bank transfer option
- SEPA Direct Debit: European users requesting subscription-friendly bank debit
- Community thread spans 2+ years with no resolution
- User quote: "It is the sole reason stopping me from upgrading"
- Sept 2025: Users reported multiple Philippine bank credit cards declined when upgrading to Business plan
- Users report trying "6 cards from different countries without success"

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest enterprise market)
  Accepted: Visa/MC/Amex, ACH, Wire, Check (Enterprise only)
  Missing: PayPal, Venmo, Apple Pay, Google Pay (self-serve)
  Note: 99% Fortune 100 adoption but self-serve only accepts cards

MARKET 2: Europe / EU (significant enterprise base)
  Accepted: Visa/MC, Wire (Enterprise)
  Missing: iDEAL (Netherlands), GiroPay (Germany), SEPA DD, Bancontact (Belgium), BLIK (Poland), Sofort
  Note: SEPA DD is the backbone of European subscription billing. Its absence blocks B2B adoption.

MARKET 3: Brazil / LATAM
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, PSE
  Note: Pix processes 70%+ of digital payments in Brazil. Card-only checkout blocks growth in LATAM.

MARKET 4: India / South Asia
  Accepted: Visa/MC (cross-border)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of digital payments in India. Cross-border card declines common.

MARKET 5: Japan / APAC
  Accepted: Visa/MC (cross-border)
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay
  Note: Japan is a key market (Canvas Tokyo event). Local payment methods critical for self-serve conversion.

**Key meeting angles:**
1. **$500M ARR with card-only self-serve** | Every missing payment method is a lost upgrade in a 100M+ user funnel
2. **Fortune 100 penetration** | 99% adoption, 20 contracts at $1M+ ARR. Enterprise invoice optimization accelerates cash flow.
3. **Cross-border decline wall** | Philippine, LATAM, and APAC users cannot upgrade despite wanting to pay
4. **Community screaming for PayPal/local methods** | 2+ year unresolved request thread. Direct evidence of lost revenue.
5. **Marketplace monetization opportunity** | 60M+ users accessing third-party apps with no native payment layer
6. **PLG to enterprise conversion** | Self-serve checkout friction blocks the free-to-paid upgrade path that drives Miro's growth model
7. **Competitor pressure** | Figma (backed by Adobe), Canva, and Lucidspark offer broader payment options

**Sources:**
- [Miro: Payment Options Help](https://help.miro.com/hc/en-us/articles/360010961020-Payment-options-invoicing-and-automated-payments)
- [Miro: Enterprise Plan Payment](https://help.miro.com/hc/en-us/articles/8798149412626-How-to-pay-for-Enterprise-Plan)
- [Miro: Billing and Payments](https://help.miro.com/hc/en-us/sections/4408892705938-Billing-and-payments)
- [Miro Community: Billing Alternatives Request](https://community.miro.com/wish-list-32/billing-alternatives-to-credit-card-paypal-girppay-ideal-bank-account-etc-13502)
- [Miro Community: Payment Method Issues](https://community.miro.com/ask-the-community-45/an-issue-with-payment-method-16424)
- [Miro Community: Payment Problems](https://community.miro.com/ask-the-community-45/payment-problems-10525)
- [Miro Community: PayPal Request](https://community.miro.com/ideas/payment-via-paypal-137)
- [Miro Developer Docs: Monetization with Stripe](https://developers.miro.com/docs/monetization-with-miro-stripe)
- [Miro Developer Docs: Marketplace](https://developers.miro.com/docs/miro-marketplace)
- [Miro: Customers Page](https://miro.com/customers/)
- [Miro: Forbes Cloud 100 2025](https://miro.com/newsroom/miro-is-named-to-the-2025-forbes-cloud-100/)
- [Miro: Pricing](https://miro.com/pricing/)
- [Fueler: Miro 2026 Statistics](https://fueler.io/blog/miro-usage-revenue-valuation-growth-statistics)
- [Sacra: Miro Revenue & Valuation](https://sacra.com/c/miro/)
- [TechCrunch: Miro $17.5B Valuation](https://techcrunch.com/2022/01/05/visual-collaboration-company-miro-valued-at-17-5b-following-400m-in-new-funding/)
- [Contrary Research: Miro Breakdown](https://research.contrary.com/company/miro)
- [Brandfetch: Miro Logo](https://brandfetch.com/miro.com)
