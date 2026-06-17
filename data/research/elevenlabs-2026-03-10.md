# ElevenLabs -- Payments Intelligence Report
Date: 2026-03-10
Domain: elevenlabs.io

---

## 1. COMPANY OVERVIEW

- AI voice platform (text-to-speech, voice cloning, dubbing, conversational AI)
- Founded by Mati Staniszewski and Piotr Dabkowski (Polish founders)
- HQ: 169 Madison Avenue, New York City
- European HQ: London
- $330M ARR as of end 2025 (up 175% YoY from $120M in 2024)
- Series D: $500M at $11B valuation (Feb 2026), led by Sequoia Capital -- eyeing IPO
- Revenue split: ~50/50 enterprise vs consumer (Dec 2025), expected 60/40 by Dec 2026
- 41% of Fortune 500 companies use the platform
- Enterprise clients: Deutsche Telekom, Revolut, Washington Post, TIME, Paradox Interactive, HarperCollins

Sources:
- https://www.cnbc.com/2026/02/04/nvidia-backed-ai-startup-elevenlabs-11-billion-valuation.html
- https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/
- https://sacra.com/c/elevenlabs/
- https://en.wikipedia.org/wiki/ElevenLabs

---

## 2. WEBSITE TRAFFIC (SimilarWeb, Jan 2026)

Total traffic trend: +14.25% month-over-month

Top countries by traffic share:
1. United States -- 20.04%
2. India -- 11.72%
3. Brazil -- 4.85%
4-10: Not available without paid SimilarWeb access

Traffic sources:
- Direct: 58.99%
- Organic Search: 2nd largest
- Paid Search: 3rd largest

Audience: 61.47% male, 38.53% female; largest age group 25-34

Sources:
- https://www.similarweb.com/website/elevenlabs.io/
- https://www.semrush.com/website/elevenlabs.io/overview/

---

## 3. LEGAL ENTITIES & OFFICES

Confirmed:
- ElevenLabs, Inc. (Eleven Labs Inc) -- US entity, Delaware-incorporated (Bloomberg ticker: 2285811D:US)
- HQ: 169 Madison Avenue, New York, NY
- European HQ: London (no specific UK Companies House entity confirmed in search)
- Founders are Polish; company has Polish roots but no confirmed Polish entity found

Not found:
- No SEC EDGAR filings (private company, pre-IPO)
- No OpenCorporates or Companies House UK records surfaced in search
- No confirmed subsidiaries beyond US and UK presence

Sources:
- https://en.wikipedia.org/wiki/ElevenLabs
- https://www.bloomberg.com/profile/company/2285811D:US
- https://www.zoominfo.com/c/eleven-labs-inc/566154380
- https://elevenlabs.io/contact-legal
- https://www.cbinsights.com/company/eleven-labs

---

## 4. PSP & PAYMENT STACK

### Primary PSP: Stripe [Press Release] [Checkout] [Third-Party Report]

ElevenLabs uses Stripe as its sole confirmed payment processor:

- Adopted Stripe in 2023 to launch flat-rate subscriptions
- Uses Stripe Optimized Checkout Suite (embedded pre-built Checkout form)
- Stripe Connect for voice actor payouts (Voice Library marketplace)
- Payment methods via Stripe: Apple Pay, Google Pay, Revolut Pay
- Stripe Link accounts for 20% of ElevenLabs payments (auto-fill saved payment info)
- Entire payment stack managed by ONE engineer

Key quote from Stripe case study: ElevenLabs turned to Stripe to handle subscriptions, checkout, and payouts for its global user base.

### Payment Methods Accepted
From help center: credit/debit cards, digital wallets (Apple Pay, Google Pay), Revolut Pay via Stripe

### Payouts Infrastructure
- Voice actors earn revenue through the ElevenLabs Voice Library
- Payouts processed via Stripe Connect
- Payout documentation: https://elevenlabs.io/docs/product-guides/voices/payouts

### No evidence of additional PSPs
No mentions of Adyen, Checkout.com, Worldpay, Braintree, or any other PSP found.

Sources:
- https://stripe.com/en-no/customers/elevenlabs (Stripe case study)
- https://help.elevenlabs.io/hc/en-us/articles/13416538053905-What-kind-of-payment-is-accepted
- https://elevenlabs.io/payouts
- https://help.elevenlabs.io/hc/en-us/sections/24487500797329-Payment-Billing
- https://elevenlabs.io/agents/integrations/stripe

### Payment Orchestration: NONE FOUND

No evidence of any payment orchestration layer (Spreedly, Primer, Gr4vy, CellPoint, or others). Single-PSP setup with Stripe only.

---

## 5. PCI DSS & SECURITY COMPLIANCE

No public PCI DSS compliance statements found for ElevenLabs.

Since they use Stripe's hosted checkout (Optimized Checkout Suite), they likely fall under SAQ A (minimal PCI scope) -- Stripe handles all card data.

No SOC 2 certification page or trust center found in search results. ElevenLabs has a security page but no specific compliance badges surfaced.

Enterprise plans mention "advanced security/compliance" but no specifics publicly available.

Source:
- https://elevenlabs.io/contact-legal (legal contact, no compliance details surfaced)

---

## 6. PRICING & BILLING MODEL

Six tiers:
- Free: 20 min/month, non-commercial
- Starter: $5/month -- commercial rights, instant voice cloning
- Creator: mid-tier for podcasters/YouTubers
- Pro: advanced features, more minutes
- Scale: enterprise-adjacent, large volume
- Business: $1,320/month -- 11,000 min TTS, 13,750 min conversational AI
- Enterprise: custom pricing, dedicated infra, custom SLAs

Billing: monthly or annual. Unused credits roll over up to 2 months on active subscription.

Pricing restructured Jan 2025 (model-aware credits), simplified Aug 2025 (unified credits regardless of model).

Sources:
- https://elevenlabs.io/pricing
- https://flexprice.io/blog/elevenlabs-pricing-breakdown
- https://www.withorb.com/blog/eleven-labs-pricing

---

## 7. YUNO OPPORTUNITY ASSESSMENT

### Single-PSP Risk (HIGH)
ElevenLabs runs 100% on Stripe with no backup PSP or orchestration layer. At $330M ARR and growing, a Stripe outage = full revenue stoppage. One engineer manages the entire payment stack -- fragile.

### Cross-Border Opportunity (HIGH)
- 80% of traffic is outside the US (India 11.72%, Brazil 4.85%, plus unlisted countries)
- Global user base across 190+ countries likely
- Currently only offering cards + Apple Pay + Google Pay + Revolut Pay via Stripe
- Missing local payment methods in key markets (PIX in Brazil, UPI in India, iDEAL in Netherlands, etc.) -- though not confirmed absent, not confirmed present either

### Payout Complexity (MEDIUM)
- Voice Library payouts to creators worldwide via Stripe Connect
- As marketplace grows, multi-rail payout optimization becomes relevant

### IPO Readiness (HIGH)
- Company explicitly eyeing IPO (CEO quote, Feb 2026)
- Pre-IPO companies typically diversify payment infrastructure to reduce vendor concentration risk
- Multi-PSP setup + orchestration = audit-friendly, resilient

### Enterprise Growth (HIGH)
- Revenue mix shifting from 50/50 to 70/30 enterprise by 2027
- Enterprise deals often require payment flexibility (invoicing, custom billing, multi-currency)

---

## 8. KEY CONTACTS & OUTREACH ANGLES

Best angles for outreach:
1. Single-PSP dependency at $330M ARR scale -- one Stripe outage away from zero revenue
2. Cross-border payment optimization -- 80% international traffic, likely missing local APMs in high-growth markets (Brazil, India, LATAM, Europe)
3. IPO readiness -- payment infrastructure diversification as part of pre-IPO hardening
