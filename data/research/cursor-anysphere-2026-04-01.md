# Cursor (Anysphere Inc.) — Payments Intelligence Report
*Framework v8.0 | Research Date: 2026-04-01*

---

## EXECUTIVE SUMMARY

Cursor is an AI-powered code editor built by **Anysphere Inc.**, a San Francisco-based startup founded in 2022 by four MIT graduates (Michael Truell, Sualeh Asif, Aman Sanger, Arvid Lunnemark). Cursor is a VS Code fork enhanced with AI-native features (code generation, multi-file editing, agentic debugging). The company reached **$1B+ ARR by late 2025** — the fastest SaaS company in history to hit $100M ARR (Jan 2025, ~20 months post-launch) — and was valued at **$29.3B** as of November 2025. Cursor operates a pure **SaaS subscription model** (credit-based, $0–$200/user/month) with 1M+ daily active users. Payment infrastructure appears to rely on **Stripe** for billing/subscriptions. No public evidence of payment orchestration, multi-PSP strategy, or complex payment infrastructure. The Yuno opportunity here is **limited** — Cursor is a developer tool, not a merchant or marketplace processing end-consumer payments. The primary payment need is recurring subscription billing.

---

## SECTION 1 — EXPANSION (Last 24 Months)

### New Markets & Enterprise Push

| Event | Date | Details | Source |
|-------|------|---------|--------|
| Enterprise waitlist demand | Feb 2025 | 4,000–5,000 companies requested enterprise access | [Contrary Research](https://research.contrary.com/company/cursor) |
| Enterprise plan launched | 2025 | SCIM 2.0, audit logs, pooled credits, SSO, RBAC | [Cursor Pricing](https://cursor.com/terms/pricing) |
| Teams plan launched | 2025 | $40/user/month, centralized billing, shared chats | [Cursor Pricing](https://cursor.com/terms/pricing) |
| Credit-based billing migration | Jun 2025 | Switched from request-based to credit-based billing model | [FinTech Weekly](https://www.fintechweekly.com/magazine/articles/cursor-pricing-change-user-backlash-refund) |
| Bugbot launch | Jul 2025 | GitHub-integrated debugging add-on, $40/user/month | [Wikipedia — Anysphere](https://en.wikipedia.org/wiki/Anysphere) |

### M&A Activity

| Target | Date | Deal Size | Strategic Rationale | Source |
|--------|------|-----------|---------------------|--------|
| Supermaven | ~2024–2025 | Not disclosed | Fast code completion technology (acquired talent + IP) | [Crunchbase](https://news.crunchbase.com/venture/cursor-financing-ai-coding-automation/) |
| Koala | Jul 2025 | Not disclosed | Enterprise sales team talent acquisition | [Contrary Research](https://research.contrary.com/company/cursor) |
| Graphite | Dec 2025 | ~$290M (est.) | Code review platform; end-to-end dev workflow | [TechFundingNews](https://techfundingnews.com/anysphere-soars-to-29-3b-valuation-with-2-3b-funding-redefining-the-future-of-coding/) |
| Streamfold | Mar 2026 | Not disclosed | Unknown — recent acquisition | [Tracxn](https://tracxn.com/d/companies/anysphere/__boMTRCeqvEyO5l8MfmRisI6Gmrw7Hjta62sJbpUI4uc) |

### Leadership Changes

| Name | Role | Date | Details | Source |
|------|------|------|---------|--------|
| Arvid Lunnemark | Co-founder & CTO | Oct 2025 (departure) | Left to found Integrous Research (AI safety lab) | [Wikipedia — Anysphere](https://en.wikipedia.org/wiki/Anysphere) |

No public information found on: VP Payments hires, payment-related job postings, or public RFPs related to payment infrastructure.

---

## SECTION 2 — FINANCIALS

### Revenue & Growth

| Metric | Value | Date | Source |
|--------|-------|------|--------|
| ARR | $100M | Jan 2025 | [TechCrunch](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/) |
| ARR | $500M | Jun 2025 | [TechCrunch](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/) |
| ARR | $1B+ | Late 2025 | [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) |
| YoY ARR growth | ~9,900% | 2025 | [GetLatka](https://getlatka.com/companies/cursor.com) |
| Daily active users | 1M+ | Dec 2025 | [GetLatka](https://getlatka.com/companies/cursor.com) |
| Paid customers (enterprise) | 50,000+ | Late 2025 | [GetLatka](https://getlatka.com/companies/cursor.com) |

### Funding Rounds

| Round | Date | Amount | Valuation | Lead Investors | Source |
|-------|------|--------|-----------|----------------|--------|
| Seed | Oct 2023 | $8M | Not disclosed | OpenAI Startup Fund | [Crunchbase](https://news.crunchbase.com/ai/anysphere-cursor-venture-funding-thrive/) |
| Series A | 2024 | $60M | $400M | Andreessen Horowitz | [Wikipedia — Anysphere](https://en.wikipedia.org/wiki/Anysphere) |
| Series B | Nov 2024 | $100M (est.) | $2.5B | Thrive Capital, a16z | [Contrary Research](https://research.contrary.com/company/cursor) |
| Series C | Jun 2025 | $900M | $9.9B | Thrive Capital, a16z, Accel, DST Global | [TechCrunch](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/) |
| Series D | Nov 2025 | $2.3B | $29.3B | Accel, Coatue; strategic: Google, NVIDIA | [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) |

**Total funding raised**: ~$3.4B+

### Subscription Pricing (Average Transaction Values)

| Plan | Price | Billing | Key Features |
|------|-------|---------|--------------|
| Hobby | $0/month | Free | Limited completions, limited agent requests |
| Pro | $20/month ($16/mo annual) | Monthly/Annual | Extended agent, frontier models, $20 credit pool |
| Pro+ | $60/month | Monthly | 3x usage credits |
| Ultra | $200/month | Monthly | 20x usage, priority features |
| Teams | $40/user/month | Per-seat | SSO, RBAC, centralized billing |
| Enterprise | Custom | Custom | SCIM, audit logs, pooled credits |

Source: [Cursor Pricing](https://cursor.com/terms/pricing) | [LowCode Agency](https://www.lowcode.agency/blog/cursor-ai-pricing) | [Dev.to](https://dev.to/rahulxsingh/cursor-pricing-in-2026-hobby-pro-pro-ultra-teams-and-enterprise-plans-explained-4b89)

### Payment Infrastructure

- **Primary PSP**: Stripe (confirmed via billing page and community forums)
- **Payment methods accepted**: Credit/debit cards, Alipay. Community requests for additional methods (e.g., PayPal, regional methods) are unresolved.
- **No evidence of**: payment orchestration, multi-PSP strategy, smart routing, or dedicated payments team.

Sources: [Cursor Billing Docs](https://cursor.com/docs/account/billing) | [Cursor Forum](https://forum.cursor.com/t/cursor-payment-method-to-know/33674) | [Cursor Forum — Payment Methods](https://forum.cursor.com/t/add-some-reasonable-payment-methods/91777)

---

## SECTION 3 — COMPETITORS

### A. Direct Competitors (AI Code Editors / AI Coding Assistants)

| # | Company | Website | HQ | Est. Size | Key Markets | Funding / Valuation | Payment Orchestration? | Source |
|---|---------|---------|-----|-----------|-------------|---------------------|----------------------|--------|
| 1 | **GitHub Copilot** (Microsoft) | github.com/features/copilot | San Francisco, CA | Part of Microsoft (228K+ employees) | Global | N/A (Microsoft subsidiary) | No — Microsoft billing | [GitHub](https://github.com/features/copilot) |
| 2 | **Windsurf** (fka Codeium, now Cognition) | windsurf.com | San Francisco, CA | ~150 (pre-acquisition) | Global | $1.25B val (Aug 2024); acquired by Cognition for ~$250M (Dec 2025) | No public evidence | [CBInsights](https://www.cbinsights.com/company/exafunction/financials) |
| 3 | **Claude Code** (Anthropic) | claude.ai | San Francisco, CA | ~1,000+ | Global | Anthropic valued at $60B+ | No — Stripe billing | [Anthropic](https://www.anthropic.com) |
| 4 | **Tabnine** | tabnine.com | Tel Aviv, Israel | ~200 | Global (enterprise focus) | $55M+ total funding | No public evidence | [Tabnine](https://www.tabnine.com) |
| 5 | **Replit** | replit.com | San Francisco, CA | ~200 | Global | $1.16B valuation (2023); $100M ARR by mid-2025 | No public evidence | [Replit](https://replit.com) |
| 6 | **Zed** | zed.dev | San Francisco, CA | ~30 | Global | Seed-stage | No public evidence | [Zed](https://zed.dev) |
| 7 | **Continue.dev** | continue.dev | San Francisco, CA | ~20 | Global (open-source) | Seed-stage | N/A (open source) | [Continue](https://continue.dev) |
| 8 | **Devin** (Cognition AI) | cognition.ai | San Francisco, CA | ~100 | Global | $2B valuation (2025 est.) | No public evidence | [Cognition](https://cognition.ai) |

### B. Industry Peers (Developer Tools with Similar SaaS/Subscription Business Models)

| # | Company | Website | HQ | Est. Size | Key Markets | Funding / Valuation | Payment Orchestration? | Source |
|---|---------|---------|-----|-----------|-------------|---------------------|----------------------|--------|
| 1 | **Vercel** | vercel.com | San Francisco, CA | ~500 | Global | $3.5B valuation (2024) | No public evidence | [Vercel](https://vercel.com) |
| 2 | **Supabase** | supabase.com | San Francisco, CA | ~200 | Global | $2B valuation (2025) | No public evidence | [Supabase](https://supabase.com) |
| 3 | **Figma** (Adobe) | figma.com | San Francisco, CA | ~1,500 | Global | Acquired by Adobe attempt ($20B, blocked); independent at ~$12.5B | No public evidence | [Figma](https://figma.com) |
| 4 | **Notion** | notion.so | San Francisco, CA | ~500 | Global | $10B valuation (2024) | No public evidence | [Notion](https://notion.so) |
| 5 | **Linear** | linear.app | San Francisco, CA | ~80 | Global | $400M valuation (2022) | No public evidence | [Linear](https://linear.app) |
| 6 | **Railway** | railway.app | San Francisco, CA | ~50 | Global | Series A | No public evidence | [Railway](https://railway.app) |
| 7 | **Lovable** | lovable.dev | Stockholm, Sweden | ~50 | Global | $100M ARR in 8 months (2025) | No public evidence | [Lovable](https://lovable.dev) |

---

## SECTION 4 — PAYMENT OPPORTUNITY ASSESSMENT

### Payment Complexity Score: LOW

**Rationale**: Cursor is a pure SaaS subscription product with straightforward recurring billing. Key observations:

1. **Single PSP (Stripe)**: All billing runs through Stripe. No multi-PSP complexity.
2. **Limited payment methods**: Cards + Alipay only. Users have requested PayPal and regional methods but these remain unserved.
3. **No marketplace/platform payments**: Cursor does not process payments on behalf of third parties.
4. **No cross-border payment complexity**: Subscriptions are billed in USD globally.
5. **Growth-driven pain points (potential)**: At $1B+ ARR and 1M+ DAUs across global markets, Cursor may eventually face:
   - High churn from failed recurring payments (involuntary churn / card declines)
   - Demand for local payment methods in non-US markets (e.g., SEPA, Boleto, UPI, iDEAL)
   - Enterprise procurement requirements for local invoicing/billing entities
   - FX optimization on international subscriptions

### Signals to Monitor

- Job postings for payments/billing engineering roles
- Expansion of payment method support beyond cards + Alipay
- Enterprise billing complexity as 50K+ business customers scale
- Potential IPO (frequently discussed) which would increase financial transparency

---

## SOURCES

- [TechCrunch — Anysphere $9.9B valuation](https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/)
- [CNBC — $2.3B Series D at $29.3B](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html)
- [Crunchbase — Anysphere funding](https://news.crunchbase.com/ai/anysphere-cursor-venture-funding-thrive/)
- [TechFundingNews — Series D details](https://techfundingnews.com/anysphere-soars-to-29-3b-valuation-with-2-3b-funding-redefining-the-future-of-coding/)
- [Wikipedia — Anysphere](https://en.wikipedia.org/wiki/Anysphere)
- [Contrary Research — Cursor breakdown](https://research.contrary.com/company/cursor)
- [GetLatka — Cursor financials](https://getlatka.com/companies/cursor.com)
- [Cursor Pricing Policy](https://cursor.com/terms/pricing)
- [Cursor Billing Docs](https://cursor.com/docs/account/billing)
- [Cursor Forum — Payment methods](https://forum.cursor.com/t/add-some-reasonable-payment-methods/91777)
- [FinTech Weekly — Pricing backlash](https://www.fintechweekly.com/magazine/articles/cursor-pricing-change-user-backlash-refund)
- [Tracxn — Anysphere profile](https://tracxn.com/d/companies/anysphere/__boMTRCeqvEyO5l8MfmRisI6Gmrw7Hjta62sJbpUI4uc)
- [Sacra — Codeium/Windsurf revenue](https://sacra.com/c/codeium/)
- [CBInsights — Windsurf financials](https://www.cbinsights.com/company/exafunction/financials)
- [Summit Ventures — Anysphere](https://www.summit-ventures.net/company/anysphere/)
- [AccessIPOs — Anysphere IPO analysis](https://accessipos.com/anysphere-cursor-stock-ipo/)
- [MVP.vc — Anysphere analysis](https://www.mvp.vc/company-initations/anysphere)
