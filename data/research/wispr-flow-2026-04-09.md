# Wispr Flow — SDR Research Brief
**Date:** 2026-04-09
**Prepared for:** Yuno Sales Team

---

## EXECUTIVE SUMMARY

Wispr Flow is an AI-powered voice dictation tool by Wispr AI, Inc. (South San Francisco, CA) that lets users dictate text at 150–184 WPM into any application across Mac, Windows, iOS, and Android. The company has raised **$81M** at a **$700M post-money valuation**, is used inside **270 Fortune 500 companies**, and reports ~$10M revenue with 40% MoM growth. Their payment stack relies on **Stripe** for web/desktop subscriptions and **Apple IAP / Google Play Billing** for mobile — no orchestration layer detected. **Yuno fit is limited**: Wispr Flow is a SaaS subscription business, not a merchant processing consumer payments at checkout. The primary angle would be optimizing cross-border subscription billing as they expand internationally, though this is a weaker fit than typical Yuno ICP targets.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | N/A | N/A | Growing — 100x YoY user base growth | [TechCrunch][S1] |
| 2–10 | Not found | N/A | N/A | N/A | N/A |

No SimilarWeb or Semrush traffic data was found for wispr.ai / wisprflow.ai. Growth proxies from press: 100x YoY user increase, 40% MoM growth, 125 new enterprise customers/week, 270 Fortune 500 companies signed.

> ⚠️ MANUAL: Check SimilarWeb directly for wispr.ai / wisprflow.ai traffic breakdown.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|-------------------|-------------------|---------------------|------------|
| United States | Yes (primary) | Yes — Wispr AI, Inc., 400 Oyster Point Blvd, Ste 212, South San Francisco, CA 94080 | No | [ZoomInfo][S2] |
| Other markets | Unknown | No entities found | Unknown | N/A |

Wispr AI is a US-incorporated company with no confirmed international subsidiaries. Their Nov 2025 funding round mentioned **localization for non-US markets** with region-specific compliance and data residency requirements, suggesting international expansion is planned but early.

> ⚠️ MANUAL: Verify on official T&Cs for any non-US entities.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|---------------|---------------|------------|
| Global (Web/Desktop) | **Stripe** | [Help Center] — Users manage subscriptions via Stripe billing portal; invoices from Stripe | [Wispr Help Center][S3] |
| iOS | **Apple In-App Purchase** | [App Store] — iOS billing through Apple | [App Store][S4] |
| Android | **Google Play Billing** | [Google Play] — Listed on Play Store, Feb 2026 launch | [Google Play][S5] |

### 3B. Orchestrator

No public evidence found of any payment orchestration layer (Spreedly, Primer, Gr4vy, CellPoint, APEXX). Wispr uses Stripe directly for web billing and app store billing for mobile.

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Agent D Findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|---------------------|------------|
| Global (Web) | Credit/debit cards via Stripe (specific brands not displayed) | Help Center — Stripe checkout confirmed | [Wispr Help Center][S3] |
| iOS | Apple Pay / cards via Apple IAP | App Store listing | [App Store][S4] |
| Android | Google Pay / cards via Google Play | Play Store listing | [Google Play][S5] |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|------------------------|---------------------|-------------------|
| Europe | No | No regional domain; single global site | SEPA, iDEAL, Bancontact, Klarna |
| LATAM | No | No regional presence confirmed | Pix, OXXO, Mercado Pago |
| APAC | No | No regional presence confirmed | Alipay, WeChat Pay, GrabPay |

> "Not verified" ≠ "not available." Stripe may enable additional APMs at checkout. MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| No public payment complaints found | Reddit, Trustpilot, G2 | None | N/A | N/A |

No payment-related complaints were found on Reddit, Trustpilot, G2, or Capterra. This may indicate strong billing practices, a relatively small consumer complaint footprint, or that enterprise clients handle disputes privately.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | June 2025 | $30M Series A led by Menlo Ventures (NEA, 8VC) | Funding | [TechCrunch][S6] |
| 2 | Nov 2025 | $25M raise led by Notable Capital + Steven Bartlett's Flight Fund; $700M valuation | Funding | [TechCrunch][S1] |
| 3 | Dec 2025 | Acquisition of Yapify AI | M&A | [Tracxn][S7] |
| 4 | Dec 2025 | Enterprise expansion into global markets announced | Expansion | [The AI Insider][S8] |
| 5 | Feb 2026 | Android launch — doubles addressable device base | Product | [Wispr Flow][S9] |
| 6 | Ongoing | Year-long partnership with Steven Bartlett / Diary of a CEO (1B+ streams, 35M+ subscribers) | Marketing | [Wispr Flow][S10] |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| — | — | No payment-specific news found | N/A | N/A |

Wispr Flow's news coverage focuses on AI/voice technology and funding. No payment infrastructure changes, PSP partnerships, or payment-related announcements found.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Stripe-hosted checkout (web); app store IAP (mobile) | Standard | PSP-hosted reduces PCI scope |
| Guest checkout | N/A — account required (subscription SaaS) | N/A | Email registration required |
| Steps to purchase | Sign up → 14-day free trial → convert to paid via Stripe | Standard | No credit card required for trial |
| 3DS | Not verified | N/A | Would depend on Stripe's configuration |
| Mobile experience | Native apps on iOS + Android with in-app billing | Good | Separate billing channels per platform |
| APM display logic | No APMs visible on pricing page; Stripe handles at checkout | Unknown | Stripe may offer local methods dynamically |

> ⚠️ MANUAL: Walk checkout in web and mobile to confirm APM options at Stripe checkout.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|-------------------|------------------------------|--------|
| Not certified (not needed) | Fully offloaded to Stripe / app stores | N/A — Wispr doesn't handle card data | [Wispr Docs][S11] |

Wispr holds **SOC 2 Type II** (Feb–May 2025, ACCORP Partners), **ISO 27001:2022** (Sept 2025, Gradient Certification), and **HIPAA** compliance. PCI DSS is unnecessary since Stripe handles all card data.

---

## SECTION 10 — Strategic Insights

### Insight #1: SaaS Subscription Model Limits Yuno Fit
**Evidence:** S3 — Stripe for web, Apple IAP for iOS, Google Play for Android. Simple subscription billing.
**Pain Point:** None confirmed — current stack handles subscription billing adequately.
**Yuno Value Prop:** Limited. Yuno's core value (payment orchestration, smart routing, APM expansion) is designed for merchants with consumer checkout flows, not SaaS subscription billing.
**Best Case:** If Wispr expands aggressively internationally and needs local payment methods for non-card markets.
**Outreach Angle:** Not recommended as a high-priority target — see Insight #5 for the only viable angle.

### Insight #2: Rapid International Expansion Planned
**Evidence:** S8 — Nov 2025 funding earmarked for "localization for non-US markets with region-specific compliance and data residency." Android launch in Feb 2026.
**Pain Point:** As Wispr enters markets where cards-via-Stripe may not be the dominant payment method, conversion rates could suffer.
**Yuno Value Prop:** Yuno could enable local payment methods (Pix in Brazil, UPI in India, SEPA in Europe) without engineering effort.
**Best Case:** Wispr targets LATAM/APAC markets where local APMs drive conversion.
**Outreach Angle:** "As you localize for non-US markets, your Stripe-only checkout may leave conversion on the table in markets where local payment methods dominate."

### Insight #3: Enterprise Scale Creates Billing Complexity
**Evidence:** S1 — 270 Fortune 500 companies, 125 new enterprise/week, $10M revenue growing 40% MoM.
**Pain Point:** Enterprise billing (invoicing, POs, multi-seat licensing) is typically handled differently than consumer subscriptions.
**Yuno Value Prop:** Limited — Yuno doesn't solve enterprise billing/invoicing challenges. This is Stripe Billing or specialized tools like Chargebee/Zuora territory.
**Best Case:** N/A.
**Outreach Angle:** Not applicable.

### Insight #4: Multi-Platform Billing Fragmentation
**Evidence:** S3, S4, S5 — Three separate billing channels (Stripe, Apple IAP, Google Play) with no unified layer.
**Pain Point:** Revenue reconciliation, analytics, and subscription management across three separate billing systems.
**Yuno Value Prop:** Yuno's single API could theoretically unify reporting, but Yuno doesn't currently specialize in subscription management or app store billing aggregation.
**Best Case:** Minimal — app store billing is mandatory for mobile apps in most cases.
**Outreach Angle:** Not recommended.

### Insight #5: Only Viable Angle — Cross-Border Subscription Optimization
**Evidence:** S8 — International expansion underway. S3 — Stripe-only for web.
**Pain Point:** As user base globalizes, cross-border card declines on subscriptions could increase (especially recurring charges to non-US cards).
**Yuno Value Prop:** Smart routing could optimize approval rates on cross-border recurring charges; local acquiring in key markets could reduce decline rates.
**Best Case:** Wispr processes significant subscription volume from non-US users where local acquiring would improve approval rates.
**Outreach Angle:** "With 40% MoM growth and global expansion, cross-border subscription declines will become a real cost. Local acquiring in your top markets could recover meaningful revenue."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|-----------------|--------|
| Superwhisper | superwhisper.com | N/A | Small | Mac dictation | [Voibe][S12] |
| Otter.ai | otter.ai | Mountain View, CA | 200+ | Meeting transcription | [Voibe][S12] |
| Voibe | getvoibe.com | N/A | Small | Offline dictation | [Voibe][S12] |
| VoiceInk | N/A | N/A | Open source | Mac dictation | [Voibe][S12] |
| Speechify | speechify.com | San Francisco, CA | 200+ | Voice typing | [Speechify][S13] |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| AssemblyAI | assemblyai.com | Speech-to-text API | Global | Voice AI infrastructure | [AssemblyAI][S14] |
| Deepgram | deepgram.com | Speech recognition API | Global | Voice AI infrastructure | [Market research] |
| Rev | rev.com | Transcription services | US | Speech-to-text services | [Market research] |
| Descript | descript.com | Video/audio editing + transcription | US, Global | AI-powered content tools | [Market research] |
| Fireflies.ai | fireflies.ai | Meeting transcription | Global | AI meeting tools | [Market research] |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| No public information found | N/A | N/A | N/A | N/A |

No AI voice/dictation companies were found publicly using payment orchestration. This vertical's simple subscription billing model typically doesn't warrant orchestration.

### 11D. Scoring (Verified Only)

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +0 | No — US-only entity confirmed |
| Multiple PSPs | +3 | Yes — Stripe + Apple IAP + Google Play |
| Recent expansion (24 mo.) | +2 | Yes — Android launch, global expansion planned |
| Public payment issues | +0 | No — none found |
| Funding >$10M | +2 | Yes — $81M total |
| LATAM/APAC/MENA traffic | +0 | Not verified |
| No orchestrator | +2 | Yes — confirmed no orchestrator |
| Payment job postings | +0 | No — hiring ML/product, not payments |
| Public RFP | +0 | No |
| **TOTAL** | **9** | |

**🟡 Medium Priority (9/20)**

### Top 10 Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | Wispr Flow | Target | US (expanding globally) | 9 | 🟡 Medium | $81M funding + global expansion + no orchestrator |

> Note: Score is inflated by the multi-PSP signal (Stripe + app stores), which is standard for any SaaS with mobile apps. True Yuno fit is weaker than the score suggests.

**Pipeline Summary:** 1 company analyzed. Medium priority on paper, but **low practical fit** for Yuno's core value proposition. Wispr Flow is a SaaS subscription business, not a merchant with consumer checkout flows. The only viable angle is cross-border subscription optimization as they expand internationally.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|---------------|
| ~$10M (Oct 2025), growing 40% MoM | $12–$15/month (Pro); $10/user/month (Team) | ~800K–1M subscription charges/year **[INFERENCE — not confirmed]** | USD | US (confirmed); international expansion planned |

---

## SECTION 13 — Outreach (Verified Findings Only)

> ⚠️ **Honest assessment:** Wispr Flow is a weak Yuno ICP fit. They are a SaaS subscription business using Stripe + app store billing. The outreach below uses the only viable angle (cross-border subscription optimization during international expansion) but expectations should be managed accordingly.

### 13A. LinkedIn Message

```
--- LINKEDIN MESSAGE ---
Hi [Name],

Congrats on the momentum at Wispr Flow — 270 Fortune 500 companies and the Android launch is impressive growth.

I noticed you're expanding into non-US markets with localization and data residency as priorities. As your subscriber base goes global, cross-border recurring charges through Stripe alone can see elevated decline rates — especially in markets where local acquiring significantly outperforms.

At Yuno, we connect to 300+ payment providers through a single API, enabling local acquiring in 40+ countries. Companies like InDrive went live in 10 LATAM markets in under 8 months and hit 90% approval rates.

Would it make sense to chat about how local payment routing could support your international rollout? Happy to share what we've seen with other fast-scaling SaaS companies.

How does [day] at [time] look?
--- END ---
```

### 13B. Cold Email

```
--- COLD EMAIL ---
Subject: Wispr Flow's global expansion — a payments blind spot?

Hi [Name],

With Wispr Flow now in 270 Fortune 500 companies and actively localizing for international markets, you're entering a phase where your Stripe-only billing setup may start showing cracks.

Cross-border recurring charges — especially to non-US cards — see measurably higher decline rates than locally acquired transactions. For a subscription business growing 40% month over month, even a 2–3% decline rate improvement translates to meaningful recovered revenue.

Yuno connects to 300+ payment providers via a single API, enabling local acquiring in 40+ countries with no-code PSP enablement. InDrive went live in 10 LATAM markets in under 8 months with 90% approval rates. Livelo saw +5% approval uplift and 50% transaction recovery.

Worth a 15-minute call to see if this applies to Wispr's international roadmap?

Best,
[Your Name]
--- END ---
```

---

## APPENDIX — Source URLs

```
[S1] https://techcrunch.com/2025/11/20/as-its-voice-dectation-app-takes-off-wispr-secures-25m-from-notable-capital/
[S2] https://www.zoominfo.com/c/wispr-ai-inc/559959743
[S3] https://docs.wisprflow.ai/articles/4516677216-how-do-i-download-your-wispr-flow-invoices
[S4] https://apps.apple.com/us/app/wispr-flow-ai-voice-dictation/id6497229487
[S5] https://play.google.com/store/apps/details?id=com.wispr.flowapp
[S6] https://techcrunch.com/2025/06/24/wispr-flow-raises-30m-from-menlo-ventures-for-its-ai-powered-dictation-app/
[S7] https://tracxn.com/d/companies/wisprflow/__XTPty9fIPUjngX0uMeYcKZnHJVG4WCoPwSamLLI2QjE
[S8] https://theaiinsider.tech/2025/12/05/wispr-accelerates-growth-with-new-funding-as-voice-ai-platform-expands-into-enterprise-and-global-markets/
[S9] https://wisprflow.ai/android
[S10] https://wisprflow.ai/new-funding
[S11] https://docs.wisprflow.ai/articles/6939510703-compliance-certifications-standards
[S12] https://www.getvoibe.com/blog/wispr-flow-alternatives/
[S13] https://speechify.com/blog/alternatives-to-wispr-flow/
[S14] https://www.assemblyai.com/blog/voice-ai-in-2026-series-1
```
