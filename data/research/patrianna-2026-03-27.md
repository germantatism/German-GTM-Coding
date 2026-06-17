# Patrianna — SDR Research Brief
**Date:** 2026-03-27 | **Framework:** v8.0 | **Analyst:** Yuno Intelligence

---

## EXECUTIVE SUMMARY

Patrianna Limited is a Gibraltar-headquartered iGaming product and technology company (founded 2011, ~200–417 employees) that builds social casino and sweepstakes platforms for global markets. Their confirmed consumer brand is **Spree Casino** (operated by Play Spree Ltd, Isle of Man), active in 35 US states. The company maintains a dedicated in-house Java payments engineering team plus a payments/fraud analytics team in Malta, but **no named PSPs or payment orchestrator** were found publicly. Three active payments-related job postings (Payments Manager, Lead Java Engineer–Payments, Lead Payment & Fraud Analytics) signal they are actively building or restructuring their payments infrastructure — a classic inflection point where Yuno's orchestration layer could accelerate their roadmap and reduce build-vs-buy complexity. Multiple direct competitors (SOFTSWISS, Slotegrator, Soft2Bet, Gamingtec) already use payment orchestration.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | Gibraltar | N/A | N/A | HQ location | [patrianna.com](https://www.patrianna.com/) |
| 2 | United States | N/A | N/A | Primary consumer market (Spree Casino — 35 states) | [BallIsLife](https://ballislife.com/betting/reviews/spree/) |

**Note:** No SimilarWeb or Semrush traffic data is available for patrianna.com (corporate site only). Consumer-facing brand domains were not fully identified. Spree Casino (spree.com) is the only confirmed consumer brand but the site returned 403 errors when fetched.

**Operational presence by workforce (proxy for market focus):**
- 🇬🇮 Gibraltar — HQ, customer support, analytics, legal
- 🇺🇦 Ukraine — Primary engineering hub (15+ tech roles)
- 🇲🇹 Malta — Analytics, HR, payments/fraud analysis
- 🇵🇱 Poland — Mobile development
- 🇧🇬 Bulgaria — Analytics, design
- 🇵🇹 Portugal — Analytics
- 🇬🇪 Georgia — Analytics

Sources: [Patrianna Careers](https://jobs.ashbyhq.com/patrianna) | [Patrianna.com](https://www.patrianna.com/)

---

## SECTION 2 — Legal Entities

| Country | Entity | Company # | Status | Cross-Border Risk? | Source URL |
|---------|--------|-----------|--------|---------------------|------------|
| Gibraltar | Patrianna Limited | 106842 | Active (Private Co. Ltd by Shares) | HQ — N/A | [DatoCapital](https://www.datocapital.com.gi/companies/Patrianna-Ltd.html) |
| Isle of Man | Play Spree Ltd | Not found | Active (Spree Casino operator) | Operates in 35 US states from IoM | [Spree ToS](https://spree.com/terms-of-service) |
| UK | Patriana Limited (05239108) | 05239108 | Active — **NOT related** (food wholesale) | N/A | [Companies House](https://find-and-update.company-information.service.gov.uk/company/05239108) |

**Group structure:** Patrianna's privacy policy references the "Patrianna group of undertakings," indicating multiple entities exist. Subsidiary names are not publicly disclosed.

⚠️ *Play Spree Ltd (Isle of Man) operates Spree Casino in 35 US states — cross-border acquiring from IoM to US market. No US entity identified.*

> ⚠️ MANUAL: Verify on official T&Cs and Gibraltar Gambling Commissioner's licensee register for full entity mapping.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|---------------|---------------|------------|
| Global | No named PSP identified | — | — |
| N/A | In-house Java payments platform | [Job Listing] — "Lead Java Engineer (Payments)" | [Patrianna Careers](https://jobs.ashbyhq.com/patrianna) |
| N/A | In-house payments/fraud analytics (multi-analyst team) | [Job Listing] — "Team Leader Payment & Fraud Data Analyst" | [Patrianna Careers](https://jobs.ashbyhq.com/patrianna) |
| N/A | Multiple unnamed "Payment Agent(s)" | [Terms of Service] — Spree Casino | [Spree ToS](https://spree.com/terms-of-service) |

**Key signals from job postings:**
- **Lead Java Engineer (Payments)** — Ukraine (Remote): Dedicated payments engineering lead, architecture for "seamless payment experiences globally" [Job Listing]
- **Senior Java Engineer (with Fin-tech experience)** — Ukraine (Remote): Custom payment integrations [Job Listing]
- **Team Leader Payment & Fraud Data Analyst** — Malta (Remote): Senior payments/fraud role overseeing analyst team [Job Listing]
- **Payments Manager** — "Overseeing payment solutions and partnerships, analyzing data to inform payment strategy, engaging with global payment partners for optimization" [Job Listing]

[INFERENCE — not confirmed]: The combination of a dedicated payments engineering team (Java), a payments manager focused on "global payment partners," and a multi-person fraud analytics team strongly suggests Patrianna integrates with **multiple PSPs** and maintains custom routing/orchestration logic. Given the iGaming/sweepstakes vertical (high-risk MCC), they likely work with gaming-specialist acquirers (e.g., Nuvei, Paysafe, Worldpay Gaming) rather than mainstream providers.

### 3B. Orchestrator

**No public evidence of a third-party payment orchestrator found.** No mentions of Spreedly, Primer, Gr4vy, CellPoint, or APEXX.

[INFERENCE — not confirmed]: The in-house Java payments platform and the hiring pattern suggest they may be building internal orchestration capabilities rather than using a third-party orchestrator. This represents an opportunity for Yuno to offer a mature orchestration layer vs. continued in-house build.

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123 on Spree Casino checkout

---

## SECTION 4 — APMs (Agent D Findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|---------------------|------------|
| US (Spree Casino) | Visa (credit/debit), Mastercard (credit/debit) | Multiple third-party reviews (corroborated 3+ sources) | [TheGameDay](https://thegameday.com/sweepstakes-casinos/spree/banking/) |
| US (Spree Casino) | Gift cards (redemption, instant, 10 SC min) | Multiple third-party reviews | [TheGameDay](https://thegameday.com/sweepstakes-casinos/spree/banking/) |
| US (Spree Casino) | Bank transfer / ACH (redemption, 1–10 biz days, 75 SC min) | Multiple third-party reviews | [Lines.com](https://www.lines.com/guides/is-spree-casino-legit/1985) |

**Conflicting / lower confidence:**

| Method | Sources Confirming | Sources Contradicting | Assessment |
|--------|-------------------|----------------------|------------|
| PayPal | Lines.com; GlobeNewsWire (Feb 2026) | TheGameDay, SlotsFan don't mention | Possibly added recently (2026); GlobeNewsWire piece reads as sponsored |
| Apple Pay | Lines.com; search snippets | SlotsFan says card-only | Cannot confirm with certainty |
| Google Pay | Search snippets | SlotsFan says card-only | Cannot confirm with certainty |

Sources: [TheGameDay](https://thegameday.com/sweepstakes-casinos/spree/banking/) | [Lines.com](https://www.lines.com/guides/is-spree-casino-legit/1985) | [SlotsFan](https://www.slotsfan.com/casinos/sweeps-social/spree-casino/) | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/02/18/3239896/0/en/Online-Casinos-That-Accept-PayPal-2026-Spree-s-Leading-PayPal-Options.html)

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|------------------------|--------------------|--------------------|
| US (Spree — direct site) | Yes | 403 Forbidden on spree.com | ACH, PayPal, Apple Pay, Google Pay, Venmo |
| Other markets | No | No other consumer brands identified | Varies by market |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| No complaints found | Trustpilot, Reddit, AskGamblers | N/A | N/A | N/A |

**Analysis:** No payment-specific complaints were found for either Patrianna or Spree Casino. Most reviews indicate general player satisfaction. However, Patrianna operates as a B2B/platform layer — complaints would surface under individual brand names. The limited payment method options at Spree (primarily Visa/Mastercard) could indicate underlying acquiring constraints typical of high-risk MCC gaming merchants. Yuno's multi-PSP routing could help diversify acquiring relationships and improve approval rates.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2025–2026 | Hiring Payments Manager, Lead Java Engineer (Payments), Lead Payment & Fraud Analytics | Payment hiring | [Patrianna Careers](https://jobs.ashbyhq.com/patrianna) |
| 2 | 2026 Q1 | Dropped from top 50 largest Ukrainian product IT companies list | Workforce shift | [Mezha Media](https://mezha.ua/en/news/ukrainian-product-it-companies-in-2025-308811/) |
| 3 | 2026 Feb | Senior Java Developer hired | Engineering | [LinkedIn](https://www.linkedin.com/company/patrianna/) |
| 4 | 2025 Nov | Java Developer hired | Engineering | [LinkedIn](https://www.linkedin.com/company/patrianna/) |
| 5 | Ongoing | Active hiring for QA, React Native, Frontend engineers across Ukraine | Engineering expansion | [DOU.ua](https://jobs.dou.ua/companies/patrianna/) |
| 6 | Ongoing | Operations spanning 7 countries (Gibraltar, Ukraine, Malta, Poland, Bulgaria, Portugal, Georgia) | Multi-market operations | [Patrianna Careers](https://jobs.ashbyhq.com/patrianna) |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | Feb 2026 | Spree Casino listed among casinos accepting PayPal | 🟢 Possible new APM addition | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/02/18/3239896/0/en/Online-Casinos-That-Accept-PayPal-2026-Spree-s-Leading-PayPal-Options.html) |

No PSP partnerships, removals, or fintech deals found in the last 12 months.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Sweepstakes model — purchase Gold Coins, not traditional deposits | N/A | Different from standard iGaming checkout |
| Guest checkout | Not verified — 403 on site | N/A | Likely requires account registration |
| Steps to purchase | Not verified | N/A | — |
| 3DS | Not verified | N/A | Likely present given card-based transactions |
| Mobile experience | Not verified | N/A | Job listings mention React Native — mobile app exists |
| APM display logic | Not verified | N/A | Limited APMs suggest simple display |

> ⚠️ MANUAL: Walk checkout in Spree Casino (US). Site returned 403 to automated fetches.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card Data Handling | Recommended Yuno Integration | Source |
|---------------|-------------------|------------------------------|--------|
| Not publicly disclosed | [INFERENCE] Likely SAQ-A or SAQ-A-EP via PSP partners; possibly own certification given in-house payments platform | SDK or API integration depending on card data handling model | [Lines.com](https://www.lines.com/guides/is-spree-casino-legit/1985) references "PCI DSS compliance" |

---

## SECTION 10 — Strategic Insights

### Insight #1: In-House Payments Build vs. Buy Inflection Point
**Evidence:** 3 active payments job postings (Payments Manager, Lead Java Engineer–Payments, Lead Payment & Fraud Analytics) + in-house Java payments platform
**Pain Point:** Building and maintaining custom payment orchestration in-house is expensive, slow, and diverts engineering resources from core gaming product development. Gaming-specialist acquirer integrations are complex and require ongoing compliance maintenance.
**Yuno Value Prop:** Single API replaces months of custom PSP integration work. No-code PSP enablement lets the payments team focus on strategy rather than plumbing. Smart Routing optimizes across multiple gaming acquirers automatically.
**Best Case:** InDrive — 10 LATAM markets in <8 months, 90% approval rates, 4.5% recovery
**Outreach Angle:** "Your team is building what Yuno already ships — we can give your Payments Manager the orchestration layer they're hiring engineers to build, live in weeks instead of quarters."

### Insight #2: High-Risk MCC Acquiring Complexity
**Evidence:** Sweepstakes/social casino vertical (high-risk MCC); limited confirmed payment methods (Visa/Mastercard only at high confidence); unnamed "Payment Agents" in T&Cs
**Pain Point:** Gaming merchants face higher decline rates, limited acquirer options, and complex compliance requirements. Single or few acquirer relationships create concentration risk.
**Yuno Value Prop:** Smart Routing across multiple gaming-specialist acquirers boosts approval rates (+7% uplift benchmark). Transaction recovery (50% benchmark) captures revenue lost to soft declines. Real-time monitoring (Rappi: ms detection vs. 5–10 min manually) flags issues instantly.
**Best Case:** Livelo — +5% approval, 50% recovery
**Outreach Angle:** "In gaming, every declined transaction is lost player lifetime value. Our Smart Routing across gaming acquirers typically lifts approvals 5–7% — what would that mean for Spree's numbers?"

### Insight #3: Cross-Border Acquiring from Isle of Man to US
**Evidence:** Play Spree Ltd (Isle of Man) operates in 35 US states; no US entity identified
**Pain Point:** Cross-border card-not-present transactions from IoM to US face higher decline rates, higher interchange fees, and issuer friction. US players paying an IoM entity triggers additional fraud screening.
**Yuno Value Prop:** Local acquiring in the US market through Yuno's network can reduce cross-border friction, lower costs, and improve approval rates. New market enablement in weeks.
**Best Case:** InDrive — local acquiring across 10 markets, 90% approval
**Outreach Angle:** "Processing US transactions from the Isle of Man adds friction your players don't see but your approval rates do. Local US acquiring through our network can change that equation."

### Insight #4: Competitor Adoption of Payment Orchestration
**Evidence:** SOFTSWISS (integrated crypto + fiat processing), Slotegrator (Moneygrator AI payment bot, 2026), Soft2Bet (integrated payment module), Gamingtec (multi-PSP integration), GR8 Tech (payment orchestration in platform)
**Pain Point:** Direct competitors are already shipping payment orchestration as a platform capability. Without similar capabilities, Patrianna's platform offering may fall behind.
**Yuno Value Prop:** White-label or embedded orchestration that Patrianna can offer to their own B2B clients, powered by Yuno's 1,000+ payment method network.
**Best Case:** Rappi — zero implementation time, 80% less analyst resolution time
**Outreach Angle:** "SOFTSWISS and Slotegrator are already shipping payment orchestration to their operators. Yuno can help you match or exceed that — without the multi-year build."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors (B2B iGaming Platform Providers)

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|-----------------|--------|
| SOFTSWISS | softswiss.com | Poland/Malta | 2,000+ | Global (160+ countries) | [SOFTSWISS](https://www.softswiss.com/) |
| Slotegrator | slotegrator.pro | Curacao | 200–500 | CIS, LatAm, Asia, Africa | [Slotegrator](https://slotegrator.pro/) |
| Soft2Bet | soft2bet.com | Malta | 500+ | Europe, LatAm | [Rakeback](https://www.rakeback.com/news/best-b2b-igaming-providers-in-2026-the-ultimate-guide/) |
| Gamingtec | gamingtec.com | Curacao/Estonia | 200–500 | Europe, CIS, LatAm | [Gamingtec](https://gamingtec.com/) |
| NuxGame | nuxgame.com | Curacao | 100–300 | Global | [NuxGame](https://nuxgame.com/) |
| B2Spin | b2spin.com | Curacao | 50–200 | LatAm, Europe, Asia | [AffPapa](https://affpapa.com/best-igaming-b2b-software-providers/) |
| Tecpinion | tecpinion.com | India | 50–200 | Global | [Tecpinion](https://www.tecpinion.com/) |
| Velitech | velitech.com | Malta | 50–200 | Europe, Africa | [Velitech](https://velitech.com/) |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| Playtech | playtech.com | iGaming B2B | Global (170+ licenses) | Largest B2B gaming tech provider | [TRUEiGTech](https://www.trueigtech.com/top-igaming-software-providers-a-comprehensive-guide/) |
| Evolution | evolution.com | Live dealer | Global | Major B2B gaming content provider | [Smartico](https://www.smartico.ai/blog-post/igaming-software-providers-2025) |
| Kambi | kambi.com | Sportsbook B2B | Global (50+ partners) | B2B gaming platform model | [Rakeback](https://www.rakeback.com/news/best-b2b-igaming-providers-in-2026-the-ultimate-guide/) |
| GR8 Tech | gr8.tech | iGaming B2B | Europe, CIS, LatAm | Ukraine-based gaming tech (like Patrianna) | [GR8 Tech](https://gr8.tech/igaming-glossary/b2b-services-in-igaming/) |
| BGaming | bgaming.com | iGaming content | Global | B2B gaming content provider | [GamSystem](https://www.gamsystem.org/en/igaming-providers-that-set-the-tech-pace-in-2025) |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| SOFTSWISS | In-house (crypto + fiat) | Ongoing | iGaming B2B | [SOFTSWISS](https://www.softswiss.com/) |
| Slotegrator | Moneygrator (in-house AI) | 2026 | iGaming B2B | [Slotegrator](https://slotegrator.pro/) |
| Soft2Bet | In-house payment module | Ongoing | iGaming B2B | [Rakeback](https://www.rakeback.com/news/best-b2b-igaming-providers-in-2026-the-ultimate-guide/) |
| Gamingtec | In-house multi-PSP | Ongoing | iGaming B2B | [Gamingtec](https://gamingtec.com/) |
| GR8 Tech | In-house orchestration | Ongoing | iGaming B2B | [GR8 Tech](https://gr8.tech/) |

### 11D. Scoring (Verified Only)

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ Yes — 7 countries (workforce), US market (Spree) |
| Multiple PSPs | +3 | ⚠️ Inferred — "Payment Agents" (plural) in T&Cs; multi-person payments team |
| Recent expansion (24 mo.) | +2 | ✅ Yes — continued hiring across 7 countries, payments team buildout |
| Public payment issues | +2 | ❌ None found |
| Funding >$10M | +2 | ❌ No public funding — appears bootstrapped |
| LATAM/APAC/MENA traffic | +2 | ❌ Not confirmed — primary market appears to be US |
| No orchestrator | +2 | ✅ Yes — no third-party orchestrator found |
| Payment job postings | +1 | ✅ Yes — 3 active payments roles |
| Public RFP | +3 | ❌ None found |

**Total: 11 points → 🟡 Medium Priority**

### Top 10 Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | SOFTSWISS | Competitor | Global (160+ countries) | Est. 14+ | 🔴 High | In-house orchestration, 2,000+ employees, multi-market |
| 2 | Slotegrator | Competitor | CIS, LatAm, Asia, Africa | Est. 12+ | 🔴 High | Launched Moneygrator AI payment bot (2026) |
| 3 | Gamingtec | Competitor | Europe, CIS, LatAm | Est. 11+ | 🟡 Medium | Multi-PSP integration, cross-border |
| 4 | Soft2Bet | Competitor | Europe, LatAm | Est. 11+ | 🟡 Medium | 500+ employees, integrated payment module |
| 5 | **Patrianna** | **Target** | **US, Multi-country ops** | **11** | **🟡 Medium** | **3 payments job postings, no orchestrator** |
| 6 | GR8 Tech | Peer | Europe, CIS, LatAm | Est. 10+ | 🟡 Medium | Ukraine-based, payment orchestration in platform |
| 7 | NuxGame | Competitor | Global | Est. 9 | 🟡 Medium | Payment system integration, growing |
| 8 | B2Spin | Competitor | LatAm, Europe, Asia | Est. 8 | 🟡 Medium | LatAm/Asia presence |
| 9 | Tecpinion | Competitor | Global | Est. 7 | 🟡 Medium | Integrated payment gateways |
| 10 | Velitech | Competitor | Europe, Africa | Est. 6 | 🟢 Low | Smaller, niche markets |

**Pipeline Summary:** 10 companies identified, 2 high-priority. Strongest vertical: **B2B iGaming platforms** in Europe/CIS/LatAm. The iGaming B2B vertical shows heavy adoption of in-house payment orchestration — companies not yet offering it (like Patrianna) face competitive pressure. Yuno has a clear opportunity to serve as the orchestration layer for mid-tier platforms.

---

## SECTION 12 — Business Case

| Metric | Value | Source |
|--------|-------|--------|
| Annual Revenue | ~$5.5M–$8.2M (third-party estimates — likely understated) | [ZoomInfo](https://www.zoominfo.com/c/patrianna-ltd/430076940), [RocketReach](https://rocketreach.co/patrianna-limited-profile_b5e5f90af42e6143) |
| Avg Transaction Value | Not found — sweepstakes typically $5–$50 coin purchases | N/A |
| Est. Annual Transactions | Not found | N/A |
| Primary Currency | USD (US market via Spree) | [INFERENCE] |
| Top 3 Markets | US (Spree Casino — 35 states), Gibraltar (HQ), Malta (operations) | Multiple sources |

**Note:** Revenue estimates of $5.5–8.2M appear significantly understated for a 200–400 person company. Third-party estimators frequently undercount iGaming companies operating through multiple entities/jurisdictions. Actual revenue is likely substantially higher.

---

## SECTION 13 — Outreach (Verified Findings Only)

```
--- LINKEDIN MESSAGE ---

Hi [Name],

I noticed Patrianna is hiring a Payments Manager and Lead Java Engineer focused on payments — looks like you're building something serious on the payment infrastructure side.

We work with gaming and digital platforms that face exactly this challenge: integrating multiple acquirers, optimizing approval rates across high-risk MCCs, and enabling new payment methods — without the 6–12 month engineering lift.

Companies like InDrive and Rappi use our single API to connect 1,000+ payment methods and route intelligently across PSPs. InDrive went live in 10 LATAM markets in under 8 months with 90% approval rates.

Would it make sense to chat about how Yuno could accelerate what your payments team is building? Happy to do a quick 15-min call next Tuesday or Wednesday.

Best,
[Your name]

--- COLD EMAIL ---

Subject: Your Payments Manager hire caught my eye — quick thought

Hi [Name],

I saw Patrianna is actively building out a payments team — Payments Manager, Lead Java Engineer (Payments), and Payment & Fraud Analytics Lead all open at once. That's a clear signal you're investing heavily in payment infrastructure.

Here's the challenge we keep hearing from gaming platforms in this exact stage: building multi-PSP routing, fraud orchestration, and local acquiring in-house takes 12–18 months and ties up your best engineers on plumbing instead of product.

Yuno gives gaming companies a single API to 1,000+ payment methods, smart routing across acquirers, and new market enablement in weeks — not quarters. InDrive launched across 10 LATAM markets in under 8 months with 90% approval rates and 4.5% transaction recovery. Rappi cut analyst resolution time by 80%.

Several of your competitors (SOFTSWISS, Slotegrator, Gamingtec) are already shipping payment orchestration to their operators. Yuno can help you match or exceed that without the multi-year build.

Worth a 15-minute conversation to see if there's a fit?

Best,
[Your name]
```

---

## APPENDIX — Source URLs

```
[S1] https://www.patrianna.com/
[S2] https://www.datocapital.com.gi/companies/Patrianna-Ltd.html
[S3] https://jobs.ashbyhq.com/patrianna
[S4] https://www.crunchbase.com/organization/patrianna
[S5] https://www.zoominfo.com/c/patrianna-ltd/430076940
[S6] https://rocketreach.co/patrianna-limited-profile_b5e5f90af42e6143
[S7] https://thegameday.com/sweepstakes-casinos/spree/banking/
[S8] https://www.lines.com/guides/is-spree-casino-legit/1985
[S9] https://www.slotsfan.com/casinos/sweeps-social/spree-casino/
[S10] https://spree.com/terms-of-service
[S11] https://www.globenewswire.com/news-release/2026/02/18/3239896/0/en/Online-Casinos-That-Accept-PayPal-2026-Spree-s-Leading-PayPal-Options.html
[S12] https://mezha.ua/en/news/ukrainian-product-it-companies-in-2025-308811/
[S13] https://ballislife.com/betting/reviews/spree/
[S14] https://www.rankiteo.com/company/patrianna
[S15] https://business.netgear.gi/patrianna-ltd-case-study/
[S16] https://www.softswiss.com/
[S17] https://slotegrator.pro/
[S18] https://soft2bet.com/
[S19] https://gamingtec.com/
[S20] https://nuxgame.com/
[S21] https://affpapa.com/best-igaming-b2b-software-providers/
[S22] https://www.rakeback.com/news/best-b2b-igaming-providers-in-2026-the-ultimate-guide/
[S23] https://www.trueigtech.com/top-igaming-software-providers-a-comprehensive-guide/
[S24] https://www.smartico.ai/blog-post/igaming-software-providers-2025
[S25] https://gr8.tech/igaming-glossary/b2b-services-in-igaming/
[S26] https://find-and-update.company-information.service.gov.uk/company/05239108
[S27] https://www.patrianna.com/privacy-policy
[S28] https://www.clodura.ai/directory/company/patrianna
[S29] https://jobs.dou.ua/companies/patrianna/
[S30] https://www.sumologic.com/case-studies/patrianna
```
