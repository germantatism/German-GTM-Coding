# SDR Research Brief: Appmaking LTD (Cyprus)
*Framework v8.0, 4 agents, accuracy-first | Date: 2026-09-03 | Analyst: Claude for German Tatis (Yuno)*

---

## ENTITY IDENTIFICATION (disambiguation)

"Appmaking Ltd" matches several unrelated entities. This brief covers:

**Appmaking LTD, Limassol, Cyprus** (Reg. HE 437099, VAT CY60022718M). Consumer mobile app publisher ("Certified High-Tech Company" in the Cyprus Register). Address per T&Cs: Promachon Eleftherias 1, 2nd floor, Flat/Office 32, Agios Athanasios, 4103, Limassol, Cyprus. Website: https://appmaking.app/ [S1, S2]

Verified products:
- **AstroSoul: Astro Palm Reader** (Android, `com.astrosouls`, 5M+ installs, palmistry/astrology/tarot) [S4]
- **Atrix: Daily Astrology Guide** (Android, `com.atrixapp`) + **Atrix: Expert Chat & Advice** (iOS, seller "Appmaking LTD", released Dec 2024, last updated 2026-06-18) [S5, S6]
- Site claims "30+ products", "12M+ users", "180+ countries", categories: Spiritual Wellness, AI Stylist, Habit Tracking. Only the apps above are verifiable under this developer account. [INFERENCE — not confirmed]: other products likely live under sibling developer accounts. [S1]

Ruled out (different companies): AppMaking.com (India agency), APPS MAKER LTD (UK, Co. 07391096). No UK, Korean, or Hong Kong "Appmaking Ltd" found.

---

## EXECUTIVE SUMMARY

Appmaking LTD is a small Cyprus-based consumer subscription app publisher (AstroSoul, 5M+ installs; Atrix) whose entire verified monetization runs through Apple App Store and Google Play in-app billing, weekly/monthly subscriptions of $7.99 to $49.99 per item. The key finding: their official privacy policy, hosted on their own CDN and linked from Google Play, was caught mid-draft with the placeholder *"If you purchase directly through our Website, payments may be processed by third-party payment processors [confirm and list: e.g., Solidgate, Stripe, PayPal]"*, meaning they are preparing a direct web checkout and have not locked in a PSP. The Yuno opportunity is the Praktika/Voodoo-style App Store fee-recovery play, timed exactly at their first web PSP decision, reinforced by six years of documented billing and refund complaints. Caveats: no public financials, no named leadership, likely a modest deal size.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| N/A | N/A | No data | No data | N/A | [S3] |

- SimilarWeb shows **no data** for appmaking.app (July 2026): the company is app-first and the website is a corporate shell. [S3]
- App-scale proxies: ~6M total installs, ~50K ratings, top-100 rankings in 10+ countries per AndroidRank/AppBrain (search-snippet data, direct pages blocked, treat as approximate). [S7, S8]
- Company claims distribution in 180+ countries. [S1]
- No per-country traffic or download breakdown found. LATAM/APAC/MENA presence: not verified.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|--------------------|--------------------|--------------------|------------|
| Cyprus | N/A (no traffic data) | Yes (HE 437099, sole known entity) | N/A | [S2] |

- Single known entity worldwide; no subsidiaries or offices found on OpenCorporates, LinkedIn, or their site.
- ⚠️ *Structural note: global app distribution (claimed 180+ countries) from a single Cyprus entity. Today Apple/Google absorb all payment complexity. Any future direct web checkout would, by default, process 100% cross-border from an EU-acquired account, a textbook local-acquiring gap if volume concentrates in the US (reviews are US-priced in USD).*
> ⚠️ MANUAL: Verify entity on official T&Cs (done: appmaking.app/terms-of-use names the Cyprus entity verbatim).

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|----------------|---------------|------------|
| Global (Android) | Google Play in-app billing ("In-app purchases" label, $7.99 to $49.99 per item on AstroSoul; up to $299.99 per item on Atrix) | [Checkout: store listing] | [S4, S5] |
| Global (iOS) | Apple App Store billing ("Payment will be charged to your Apple App Store (iTunes) account or your Google Play account", General Terms §8) | [T&Cs] | [S9, S10] |
| Web (planned, NOT live) | Privacy policy draft placeholder names **Solidgate, Stripe, PayPal** as example processors for direct website purchases. These are template *examples*, NOT confirmed integrations. | [T&Cs, draft placeholder] | [S11] |

- **Smoking gun (verbatim from the live privacy policy):** *"If you purchase directly through our Website, payments may be processed by third-party payment processors [confirm and list: e.g., Solidgate, Stripe, PayPal]."* A legal doc caught mid-draft: web checkout is being prepared and the PSP shortlist is literally unfilled. [S11]
- [INFERENCE — not confirmed]: Solidgate is a plausible candidate given the Cyprus quiz-funnel publisher profile; zero confirmation.
- Note: per Yuno rules, PayPal is a wallet/APM, not a PSP; it appears here only because their policy names it.

**3B. Orchestrator**: No public evidence found (searches for Spreedly, Primer, Gr4vy, job listings, source code all empty). No web PSP is live to orchestrate yet.
> ⚠️ MANUAL — DevTools on any web funnel that appears: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Agent D findings)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|----------------|---------------------|------------|
| Global (Android) | Google Play in-app billing only | Live Play listing | [S4] |
| Global (iOS) | Apple in-app billing only | App Store page + iTunes Lookup API + their own General Terms §8 | [S6, S10] |

**4B. Unverified Markets**

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|------------------------|---------------------|---------------------|
| Web (all markets) | Yes | astrosoul.app root is a **GoDaddy parking lander**; atrix-app.com returns empty; candidate funnel domains (astrosoul.io, getastrosoul.com, atrix.app, quiz/web subdomains) do not resolve; support-portal JS bundles contain zero payment SDK code (no Stripe.js/Solidgate/Paddle) | N/A |
| Help center | Yes | appdesk.zendesk.com/hc returns HTTP 403 (not publicly served) | N/A |

> "Not verified" ≠ "not available." The Feb-2024 review pattern (Instagram login, $1 charge, $29 PDF upsell, $19 charge days later) matches a web quiz-funnel purchase, not typical Play IAP behavior. [INFERENCE — not confirmed; no funnel URL located.] MANUAL: VPN walk-through of any ad-driven funnel (TikTok/Meta ads are their named UA channels) before any APM claims.

---

## SECTION 5 — Payment Complaints

All from the AstroSoul Google Play listing [S4]; no company-specific Trustpilot or Reddit threads found.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Refund friction ("run around" over email, "I just want my money back") | Google Play reviews | Recurring; developer replies present | 2023 to Jun 2026 | [S4] |
| Trial-to-subscription surprise charges ($30 auto-charge after 3-day trial; "$14.99+tax weekly") | Google Play reviews | Recurring, high helpful-vote counts (89 to 241) | 2020 to Dec 2024 | [S4] |
| Stacked upsell charges ($1, then $29 PDF, then $19 days later) | Google Play reviews | At least one detailed report | Feb 2024 | [S4] |
| App stopped working while subscription kept billing | Google Play reviews | At least one report | Jun 16, 2026 | [S4] |

**Analysis:** six years of continuous billing-trust complaints. Most are dark-pattern/trial-consent issues (product decisions), but the operational failures (refund workflows, subscription state not matching app access) map to Yuno value: unified subscription billing state, refund/dispute workflows across rails, and real-time payment monitors (Rappi: millisecond detection vs 5 to 10 minutes manual). If they launch a web rail, decline-driven involuntary churn becomes a new problem class that smart routing (+7% approval) and 50% recovery directly address.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Nov to Dec 2024 | Launched Atrix (Android Nov 22, 2024; iOS Dec 2024): second brand, expert chat + daily astrology | New product line | [S5, S6] |
| 2 | 2025 to 2026 | Portfolio expansion into "AI Stylist" and "Habit Tracking" categories; "AI-Native Products" positioning | New verticals | [S1] |
| 3 | Ongoing | Site states products "distributed across platforms **and web**" | Web distribution signal | [S1] |
| 4 | 2026-06-18 | Atrix iOS updated (actively maintained) | Product | [S6] |
| 5 | Ongoing | UA stack named: Snapchat, Adjust, Google, TikTok, Unity, Meta (paid-acquisition growth model) | Growth | [S1] |

- Leadership hires (CTO/CFO/VP Payments): No public information found. No leadership names anywhere public.
- Payment-related job postings: none. Only open role: junior IT Operations Specialist. [S1]
- M&A, public RFPs: No public information found.

---

## SECTION 7 — Payment News

No public information found. No funding, acquisition, or PSP partnership news for Appmaking LTD in 2025 to 2026. No 🟢/🔴 events to flag.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | 100% app-store IAP (verified); no live web checkout found | N/A | Privacy policy drafts a future direct-website purchase flow [S11] |
| Guest checkout | N/A (IAP) | N/A | |
| Steps to purchase | In-app paywall after onboarding; reviews describe forced trial signup before content | Poor (per reviews) | "Can't receive any info until you sign up for the Free Trial" [S4] |
| 3DS | Not found | N/A | Apple/Google handle auth today |
| Mobile experience | App-native | N/A | |
| APM display logic | N/A | N/A | Apple/Google billing only |

Pricing verified on Play: AstroSoul weekly $7.99 with 3-day free trial, monthly $24.99, 3-month $29.99; Atrix IAP items up to $299.99. [S4, S5]

> ⚠️ MANUAL: Walk any ad-driven web funnel from TikTok/Meta ads in top markets; that is where a hidden web checkout would live.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|--------------------|------------------------------|--------|
| No certification published | "We don't collect or store payment data" (privacy policy); Apple/Google handle all card data today | If/when web checkout launches: Yuno SDK with hosted fields keeps them at SAQ-A scope while enabling multi-PSP routing and Yuno's PCI-compliant vault from day one | [S11] |

---

## SECTION 10 — Strategic Insights

**Insight #1: The web-checkout PSP decision is open right now, in writing.**
Evidence: Section 3, privacy policy placeholder "[confirm and list: e.g., Solidgate, Stripe, PayPal]" [S11]. | Pain Point: about to make a single-PSP choice that locks in one approval rate, one market footprint, and a migration project for every future addition. | Yuno Value Prop: start orchestrated instead of single-PSP; one integration, PSPs enabled no-code, new market live in weeks. | Best Case: Praktika BC template (App Store fee recovery via web). | Outreach Angle: "Before you fill in that PSP shortlist, see what starting orchestrated looks like."

**Insight #2: 100% of revenue pays the 15 to 30% app-store toll.**
Evidence: Sections 3 and 8, all billing via Apple/Google per their own T&Cs [S9, S10]; verified subscription price points [S4]. | Pain Point: platform fee on every weekly/monthly renewal across 5M+ installs. | Yuno Value Prop: web checkout rail with orchestration recovers most of the fee delta; standard fee-recovery business case. | Best Case: Praktika ($6.5M / 32.6% ARR template), Voodoo Stripe-MoR web rail precedent. | Outreach Angle: fee-recovery math on their own published price points.

**Insight #3: Six years of billing-trust complaints are a churn and dispute problem Yuno reduces.**
Evidence: Section 5, Play reviews 2020 to Jun 2026 [S4]. | Pain Point: refund run-arounds, subscription state mismatches, chargeback exposure. | Yuno Value Prop: unified billing operations, refunds and disputes across rails, real-time monitors. | Best Case: Rappi (80% less analyst resolution time). | Outreach Angle: secondary proof point, use carefully (their complaints are partly product dark patterns, do not lead with this).

**Insight #4: Global distribution, single Cyprus entity: any web rail is cross-border by default.**
Evidence: Sections 1 and 2 [S1, S2]. | Pain Point: EU-acquired card processing for a likely US-heavy audience depresses approval rates from day one. | Yuno Value Prop: routing to local acquiring where volume justifies it, plus local APMs across 180+ claimed countries. | Best Case: InDrive (10 markets in under 8 months, 90% approval). | Outreach Angle: "one integration now, local rails when volume justifies them."

**Insight #5 (qualifier): thin, hard-to-reach account.**
Evidence: Sections 6 and 12; no leadership names, no funding, no financials. | Implication: low-cost outreach only (LinkedIn company page, info@appmaking.app, hr@appmaking.app); do not invest in a custom deck until a human responds. Deal size likely modest; fits an SDR-motion tier, not a strategic pursuit.

---

## SECTION 11 — Pipeline

**11A. Direct Competitors** (astrology / spiritual-wellness subscription apps)

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|----|-----------|-----------------|--------|
| Nebula | Not fetched | Not found ([INFERENCE — not confirmed]: OBRIO / Genesis group, Ukraine) | 15M+ downloads | Global | [S12, S13] |
| Co-Star | Not fetched | Not found | 20M+ downloads | Global, US-heavy | [S12, S13] |
| The Pattern | Not fetched | Not found | 5M+ downloads | Global | [S12, S13] |
| Sanctuary | Not fetched | Not found | 2M+ downloads | Global | [S12, S13] |
| CHANI | Not fetched | Not found | 500K+ downloads | Global | [S12] |
| Zodiac Touch | Not fetched | Not found | 3M+ downloads | Global | [S12] |
| AstroSage | Not fetched | India | 25M+ downloads | India, web + apps | [S12] |
| AstroYogi | Not fetched | India | 10M+ downloads | India, web + apps | [S12] |

**11B. Industry Peers** (consumer subscription app publishers)

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| Bending Spoons | bendingspoons.com | App roll-up | Global | IAP fee leakage in own S-1; already in Yuno AI-apps batch | Internal Yuno research + [S14] |
| Lightricks | lightricks.com | Photo/video apps | Global | 3 PSPs, no orchestrator; already researched | Internal Yuno research |
| Replika (Luka Inc.) | replika.com | AI companion | Global | Single web PSP (Stripe) + IAP; already researched | Internal Yuno research |
| Babbel | babbel.com | Language learning | EU/US | Multi-PSP, no orchestrator; already researched | Internal Yuno research |
| Voodoo | voodoo.io | Games/apps publisher | Global | Stripe-MoR web rail for US iOS (Jun 2025): the exact motion Appmaking is drafting | Internal Yuno research |
| Calm | calm.com | Meditation subscription | US/global | Same subscription-app monetization shape | [S14] |
| Headspace | headspace.com | Meditation subscription | US/global | Same subscription-app monetization shape | [S14] |
| Praktika | praktika.ai | AI language tutor | Global | 100% IAP, fee-recovery BC template; already researched | Internal Yuno research |

**11C. Adopting Orchestration**: none publicly confirmed in this vertical this session. No public information found.

**11D. Scoring — Appmaking LTD** (verified only):

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ Global app-store distribution; top-100 rankings in 10+ countries [S7]; claims 180+ countries [S1] |
| Multiple PSPs | 0 | ❌ IAP-only verified; web PSPs unconfirmed draft |
| Recent expansion (24 mo.) | +2 | ✅ Atrix launched Nov/Dec 2024, new categories [S5, S6] |
| Public payment issues | +2 | ✅ Play reviews 2020 to Jun 2026 [S4] |
| Funding >$10M | 0 | ❌ No public information found |
| LATAM/APAC/MENA traffic | 0 | ❌ Not verified (no traffic data) |
| No orchestrator | +2 | ✅ No public evidence of any orchestrator or live web PSP |
| Payment job postings | 0 | ❌ None found |
| Public RFP | 0 | ❌ None found |

**Total: 9 → 🟡 Medium (7 to 11).** The score understates timing: the open PSP shortlist in their own privacy policy is a rare live buying signal. Treat as Medium priority, low-cost outreach, high urgency window.

**Top 10 Pipeline** (from 11A/11B; scores indicative, full scoring not run per company):

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | Bending Spoons | Peer | Global | Prior: High | 🔴 | IAP fee leakage in own S-1, IPO catalyst (already in batch) |
| 2 | Nebula (OBRIO) | Competitor | Global | Not scored | 🟡 | 15M+ downloads, aggressive web-to-app funnels [INFERENCE] |
| 3 | Babbel | Peer | EU/US | Prior: High (16) | 🔴 | Multi-PSP, no orchestrator (already researched) |
| 4 | Sanctuary | Competitor | US | Not scored | 🟡 | Hybrid subscription + pay-per-minute astrologer payments |
| 5 | Co-Star | Competitor | US/global | Not scored | 🟡 | 20M+ downloads, paid tier |
| 6 | The Pattern | Competitor | US/global | Not scored | 🟡 | $14.99/mo paywall at 5M+ downloads |
| 7 | AstroYogi | Competitor | India | Not scored | 🟡 | Live astrologer payments, web + app, India APM complexity |
| 8 | AstroSage | Competitor | India | Not scored | 🟢 | 25M+ downloads but free/Vedic-tools heavy |
| 9 | Calm | Peer | US/global | Not scored | 🟢 | Large subscription base, stack unknown |
| 10 | Headspace | Peer | US/global | Not scored | 🟢 | Large subscription base, stack unknown |

Pipeline Summary: 16 companies surfaced, 2 already-researched high-priority peers reinforced. Strongest vertical: consumer subscription apps (astrology/wellness) in US + India; the astrology cluster (Nebula, Sanctuary, Co-Star, The Pattern) is unresearched whitespace.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|----------------|
| Not found (Cyprus filings not public; no Crunchbase) | Verified price points: $7.99/wk, $24.99/mo, $29.99/3-mo (AstroSoul); items to $299.99 (Atrix) [S4, S5]. Peer benchmark $9.99/wk (Nebula) [S13] | Not found | USD (US-storefront pricing) | Not verified; US-heavy [INFERENCE from USD reviews, not confirmed] |

BC framing: with no revenue data, anchor on the fee-recovery template (Praktika model) using their published price points and 5M+ install base. Yuno pricing anchor: $50K processed free, then $0.05 per transaction.

---

## SECTION 13 — Outreach (verified findings only)

No named decision-makers exist publicly. Channels: LinkedIn company page, info@appmaking.app. Persona unknown; the messages below assume a founder/GM reader.

--- LINKEDIN MESSAGE ---

Hi [Name], I work with consumer app publishers at Yuno. Two things stood out about Appmaking: AstroSoul's monetization runs entirely through Apple and Google billing today, and your own public policies already contemplate direct website payments, with the processor shortlist still open. That first web checkout decision is worth getting right. A single PSP means one approval rate, one market footprint, and a migration project every time you add a payment method. Yuno is one API connecting 1,000+ payment methods and PSPs, with smart routing that lifts approvals ~7% and recovers up to 50% of failed transactions. It's how InDrive went live across 10 markets in under 8 months at 90% approval, and why Rappi runs payment ops on us. Worth 20 minutes before you lock in the web stack? I can do Tuesday or Wednesday afternoon.

--- COLD EMAIL ---

Subject: Before you fill in that web-payments shortlist

Hi [Name],

Your published payments terms already contemplate purchases directly through your website, alongside the Apple and Google billing that carries AstroSoul's 5M+ installs today. That tells me the web checkout decision is on your desk right now.

It's the highest-leverage payments choice you'll make: web checkout removes the 15 to 30% store fee from every $7.99 weekly and $24.99 monthly renewal, but a single-processor launch caps your approval rate and locks your roadmap to one vendor across the 180+ countries you distribute in.

Yuno is a payment orchestration platform: one API and one integration that connects 1,000+ payment methods, processors, and fraud tools. Smart routing lifts approval rates ~7%, failed-transaction recovery saves up to 50% of declines, and new processors or markets go live in weeks without code. You start orchestrated instead of migrating to orchestration later.

I put together fee-recovery math on your published price points. Worth 20 minutes this week to walk through it?

Best,
German Tatis
Yuno

---

## APPENDIX — Source URLs

```
[S1]  https://appmaking.app/
[S2]  https://appmaking.app/terms-of-use
[S3]  https://www.similarweb.com/website/appmaking.app/
[S4]  https://play.google.com/store/apps/details?id=com.astrosouls&hl=en_US
[S5]  https://play.google.com/store/apps/details?id=com.atrixapp&hl=en_US
[S6]  https://apps.apple.com/us/app/atrix-expert-chat-advice/id6737768525
[S7]  https://www.androidrank.appspot.com/developer?id=8888427613446085618
[S8]  https://www.appbrain.com/app/astrosoul-astro-palm-reader/com.astrosouls
[S9]  https://appmakingpub.b-cdn.net/Appmaking%20General%20Terms.html
[S10] https://play.google.com/store/apps/dev?id=8888427613446085618
[S11] https://appmakingpub.b-cdn.net/Appmaking%20Privacy%20Policy.html
[S12] https://www.apptunix.com/blog/top-horoscope-apps/
[S13] https://unstar.app/blog/co-star-sanctuary-pattern-nebula-stellium-astrology-apps-ranked-2026
[S14] https://en.wikipedia.org/wiki/Calm_(company) ; https://en.wikipedia.org/wiki/Headspace_(company) ; https://en.wikipedia.org/wiki/Bending_Spoons
Also: https://appmaking.app/privacy-policy · https://support.astrosoul.app/ · https://www.linkedin.com/company/appmaking-ltd
Ruled-out entities: https://find-and-update.company-information.service.gov.uk/company/07391096 (APPS MAKER LTD, UK) · https://in.linkedin.com/company/appmaking (AppMaking.com, India)
```

*Integrity notes: AppBrain/AndroidRank blocked direct fetch (403/TLS); their figures are search-snippet approximations. The "$30/week" figure appears only in user reviews and is unverified; verified pricing is the Play-listing set above. Solidgate/Stripe/PayPal are draft examples in their privacy policy, never confirmed integrations. No live web checkout exists on any domain checked as of 2026-09-03.*
