# Wix — Full Output Summary
Research date: 2026-03-11 | Consolidated: 2026-03-13

---

## 1. EXECUTIVE SUMMARY

- Wix.com Ltd. (NASDAQ: WIX) — website building and commerce platform, $1.76B revenue FY2024, 260M+ registered users
- Operates Wix Payments, its own proprietary PSP layer, built on Stripe and PayPal as underlying processors
- Multi-PSP without orchestration architecture: two confirmed PSPs with no smart routing or vendor-neutral layer
- Active expansion: 11 new European markets (Dec 2025), Wix Capital, Wix Checking
- Yuno opportunity: at the platform level — orchestrate Stripe/PayPal to improve approval rates, unify reconciliation, accelerate market expansion

---

## 2. COMPANY KEY DATA

| Data Point | Value |
|------------|-------|
| Revenue FY2024 | $1.76B (+12.74% YoY) |
| Q4 FY2025 Revenue | $524M (+14% YoY) |
| Registered users | 260M+ |
| Monthly visits | ~40M |
| Top traffic | US (23%), UK (7.3%), India (6%) |
| Ticker | NASDAQ: WIX |
| HQ | Tel Aviv, Israel |
| Legal entities | US, UK, India, Brazil, Germany, Canada, Japan, Netherlands, Ireland, Lithuania, Poland, Ukraine, Singapore |
| PCI DSS | Level 1 (merchant + service provider) |
| Certifications | ISO 27001, 27017, 27032, 27035 |

---

## 3. PAYMENT STACK

### Confirmed PSPs
- Wix Payments (proprietary layer) built on:
  - **Stripe** (primary processor, European expansion base)
  - **PayPal** (second processor, integrated Jul 2025)
- 60+ third-party PSPs available in marketplace (Braintree, Square, Nuvei, Elavon, Authorize.net, MercadoPago, Razorpay, etc.)

### Orchestrator
- **None detected** — No public evidence of Spreedly, Primer, Gr4vy, CellPoint, or Yuno

### Verified APMs
- US: Apple Pay, Google Pay, Affirm, Afterpay, Klarna, PayPal Pay Later, Venmo
- Brazil: PIX, Boleto, Installments (parcelamento)
- Netherlands: iDEAL
- UK: Clearpay, Klarna, PaidBy Bank
- Germany: Klarna (Pay Now/Later/Slice)
- Japan: Paidy, Rakuten Pay (via KOMOJU)

### Critical Limitation
- Recurring/subscriptions: cards only — no APMs (no PIX, no iDEAL, no wallets for recurring billing)

---

## 4. RECENT DEVELOPMENTS (2025-2026)

1. **Dec 2025** — Wix Payments expanded to 11 European markets via Stripe (UK, Germany, Italy, Spain, Netherlands, Austria, Belgium, Finland, Lithuania, Portugal, Switzerland)
2. **Jul 2025** — PayPal becomes second processor within Wix Payments; PayPal Pay Later and Venmo integrated
3. **Aug 2025** — Financial Services Suite launched: Wix Checking + Wix Capital
4. **Jun 2025** — Base44 acquisition ($80M) — AI platform
5. **May 2025** — Hour One acquisition — AI media creation
6. **2025** — Stripe Agentic Commerce Suite integration
7. **2025** — Choice Inc. partnership for ACH payments in US
8. **2025** — $250M private placement (Durable Capital Partners)

---

## 5. IDENTIFIED PAIN POINTS

| # | Pain Point | Evidence |
|---|-----------|----------|
| 1 | Multi-PSP without orchestration | Stripe + PayPal under Wix Payments with no smart routing |
| 2 | European expansion = cross-border complexity | 11 new markets, each with local regulatory requirements and acquiring costs |
| 3 | Subscriptions card-only | No APMs in recurring billing = high churn in APM-preference markets |
| 4 | India without Wix Payments | #3 traffic market but no native payment infrastructure |
| 5 | PSP marketplace fragmentation | 60+ PSPs available but no intelligence layer optimizing routing |

---

## 6. OUTREACH ANGLES

### Angle 1: Multi-PSP without orchestration (primary)
- "You've brought PayPal and Stripe under the Wix Payments umbrella — the next step is routing between them intelligently"
- Success case: Rappi — 80% reduction in analyst resolution time

### Angle 2: European expansion
- "With 11 new European markets, the cost of cross-border vs local acquiring is now a meaningful P&L line"
- Success case: InDrive — 10 LATAM markets in <8 months, 90% approval rate

### Angle 3: Subscription billing APM gap
- "In markets like Brazil and the Netherlands, your subscription flows are likely running card-only"
- Success case: Livelo — +5% approval rate, 50% transaction recovery

### Angle 4: India without native coverage
- "India is your #3 traffic market globally but Wix Payments doesn't cover it"
- Success case: Orchestration to deliver native experience via UPI/NetBanking

### Angle 5: PSP Plugin API = orchestration-ready
- "You've already built the multi-PSP infrastructure — orchestration is the missing intelligence layer"

---

## 7. PROSPECT SCORE

**16 points — HIGH PRIORITY**

| Signal | Pts | Verified |
|--------|-----|----------|
| Operates in 3+ countries | +3 | Yes |
| Uses multiple PSPs | +3 | Yes |
| Recent expansion | +2 | Yes |
| Public payment issues | +2 | Yes |
| Recent funding (>$10M) | +2 | Yes |
| High traffic in LATAM/APAC | +2 | Yes |
| No known orchestrator | +2 | Yes |

---

## 8. OUTREACH OUTPUTS

### 8A. LinkedIn Connection Request

Hi [Name],

Noticed Wix just expanded Wix Payments into 11 European markets through Stripe — and recently brought PayPal under the Wix Payments umbrella as a second underlying processor.

That's a smart consolidation move. The next question most platforms at that scale start asking is: how do you route intelligently between Stripe and PayPal based on BIN, cost, and approval probability — rather than statically?

I work with platforms like Rappi and Uber that ran multi-PSP setups without orchestration and found meaningful approval rate gaps between their PSPs by region. Adding a routing layer above Stripe and PayPal cut Rappi's reconciliation time by 80%.

Given Wix's further EMEA and APAC expansion plans, this feels like the right moment. Would love to share what that looks like in practice.

Would Thursday at 11am work for a 25-minute call?

German Tatis
Yuno — Payment Orchestration

---

### 8B. Cold Email

Subject: Wix Payments — routing between Stripe and PayPal

Hi [Name],

Saw the Q4 announcement — Wix Payments expanded to 11 European markets via Stripe, and PayPal is now the second processor under the Wix Payments umbrella. Strong infrastructure move.

The pattern we see at that inflection point: two confirmed PSP dependencies (Stripe + PayPal) with no smart routing between them. Each transaction goes to a default provider regardless of BIN, market, or approval probability — which means approval rate and acquiring cost improvements are being left on the table across your merchant base.

At Yuno, we sit above PSPs like Stripe and PayPal and route each transaction to the best processor in real time. Rappi deployed this and cut reconciliation time by 80% with zero implementation downtime. Uber and GoFundMe use the same layer globally.

For Wix, the math is straightforward: even a 1-2% approval rate improvement across your merchant transaction volume moves significant revenue.

Would next Wednesday at 11am work for a 25-minute conversation?

Best regards,
German

---

## 9. CUSTOMER COMPLAINTS (Trustpilot)

| Issue | Frequency |
|-------|-----------|
| Auto-renewal without adequate warning | High |
| Refunds denied (14-day cutoff) | High |
| Approved refunds with slow processing | Moderate |
| Add-on charges with no refund path | Moderate |
| Slow dispute resolution | Moderate |

---

## 10. COMPETITORS & PIPELINE

### Direct Competitors
1. Shopify (built own routing — validates the category)
2. Squarespace (single PSP: Stripe)
3. Webflow (no native payments)
4. GoDaddy (GoDaddy Payments)
5. Hostinger/Zyro

### Industry peers with similar orchestration needs
1. BigCommerce — multi-PSP open SaaS
2. WooCommerce — fragmented PSP ecosystem
3. Ecwid (Lightspeed)
4. PrestaShop
5. Shift4Shop

---

## 11. MANUAL FOLLOW-UPS

- [ ] Verify full top-10 traffic breakdown via SimilarWeb Pro
- [ ] DevTools: test card on merchant store US, Brazil, Germany to identify processor
- [ ] Checkout walkthrough on Wix demo store (US, Germany, Brazil)
- [ ] VPN checkout test in Mexico, India, Singapore to verify APMs
- [ ] Verify Wix payment-related job postings
- [ ] Verify complete subsidiary list in 20-F Exhibit 8.1

---

*Full source: data/research/wix-2026-03-11.md (449 lines, 13 sections + URL appendix)*
