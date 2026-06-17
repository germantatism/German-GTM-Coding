# REDDIT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Reddit
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/58/Reddit_logo_new.svg
Nombre merchant: Reddit

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US Revenue Dependency
Tittle_Pain Point_2: Gold Purchase Friction
Tittle_Pain Point_3: Payout Fee Overhead
Tittle_Pain Point_4: No Local APMs
Tittle_Pain Point_5: Single Processor Risk

Desc_Pain Point_1: 57% of DAU is international but only 18% of revenue comes from outside the US. 68.9M international daily users generating a fraction of domestic ARPU. Payment method gaps block digital goods conversion globally.
Desc_Pain Point_2: Gold purchases limited to credit/debit cards, Apple Pay, Google Pay, and PayPal on desktop. No Pix, no UPI, no SEPA, no local wallets. International users face cross-border card declines on micro-transactions.
Desc_Pain Point_3: Contributor Program payouts via Stripe Connect charge $2.25 + 0.25% per transaction plus 1% currency conversion. Thousands of small creator payouts amplify fees. No multi-rail payout optimization.
Desc_Pain Point_4: Zero local payment methods in any international market. Reddit operates in 23 languages and expanding to 30+ countries, but checkout only accepts cards and PayPal.
Desc_Pain Point_5: Stripe processes 100% of web purchases and 100% of Contributor Program payouts. No secondary acquirer or failover. Any Stripe disruption blocks both user spending and creator earnings simultaneously.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary processor + payouts)
PSP_2: PayPal
PSP_3: Apple App Store (iOS IAP)
PSP_4: Google Play (Android IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: OXXO
Local_M_8: GCash
Local_M_9: Konbini
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Gold purchase and Premium subscription to the highest performing acquirer by card BIN, issuer, and geography. With $2.2B revenue, 121M DAU, and 57% international users, a 3% auth uplift recovers millions in micro-transaction revenue across the global user base.
Desc_Yuno_Cap2: Automatic cascade eliminates Reddit's single Stripe dependency for both purchases and creator payouts. When Stripe declines, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions. Protects both user spending and Contributor Program earnings.
Desc_Yuno_Cap3: Unlocks the 57% international DAU that Reddit cannot monetize: Pix in Brazil, UPI in India, SEPA in Germany/France, iDEAL in Netherlands, BLIK in Poland, OXXO in Mexico, Konbini in Japan. One API, 1,000+ methods. Matches Reddit's 23-language expansion with local payment rails.
Desc_Yuno_Cap4: Single dashboard replacing Reddit's fragmented Stripe + PayPal + Apple IAP + Google Play settlement streams. Real-time per-market revenue analytics, centralized reconciliation of Gold purchases, Premium subscriptions, ad payments, and Contributor payouts. Millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Reddit at a glance:**
- Community platform, NYSE: RDDT (IPO March 2024), HQ San Francisco, California
- Revenue: $2.2B (FY 2025), up 69% YoY. Net income: $530M (first full profitable year). Q4 2025 ad revenue: $690M (+75% YoY)
- 2026 guidance: ~$2.5B+ ad revenue, Q1 2026 revenue ~$600M
- DAU: 121.4M (Q4 2025, +19% YoY). WAU: 471.6M (+24% YoY). MAU: estimated 1.21B (2025)
- International DAU: 68.9M (57% of total), growing 40% YoY. International revenue: 18% of total, growing 71.7% YoY
- Revenue streams: advertising (~93%), data licensing for AI ($140M/year, growing), Reddit Premium ($5.99/mo), Gold digital goods
- AI partnerships: Google ($60M/year data licensing), OpenAI, and others. Total AI licensing ~$400M projected by 2027
- Reddit Answers (AI search): 15M weekly users, up from 1M in 9 months
- Expanding to 30+ countries, machine translation in 23 languages
- Aleph partnership for ad sales in 45+ international markets

**Confirmed PSPs and Partners:**
- Stripe: primary payment processor for web purchases; Stripe Connect for Contributor Program payouts
- PayPal: alternative payment on desktop
- Apple App Store: iOS in-app purchases for Gold and Premium
- Google Play: Android in-app purchases
- Persona: identity verification for Contributor Program
- WeChat Pay: available for desktop Gold purchases (limited markets)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (43% of DAU, ~82% of revenue)
  Supported: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo, ACH
  Note: Highest ARPU market. Core advertising revenue

MARKET 2: United Kingdom (est. 5-7% of international DAU)
  Supported: Credit/debit cards, PayPal
  Missing: Open Banking, Faster Payments, Klarna
  Note: English-language market with high engagement. Zero local methods

MARKET 3: Germany/France (combined est. 8-10% of intl. DAU)
  Supported: Credit cards, PayPal
  Missing: SEPA Direct Debit, Sofort, iDEAL, Bancontact
  Note: Machine translation live in both languages. SEPA is subscription standard in Europe

MARKET 4: Brazil (key growth market, Portuguese translation live)
  Supported: Credit cards (cross-border)
  Missing: Pix, Boleto, local installments
  Note: Pix handles 70%+ of digital payments. Reddit investing in LATAM with Portuguese translation

MARKET 5: India (3rd globally in internet users, Hindi/Tamil translations)
  Supported: Credit cards (cross-border)
  Missing: UPI, RuPay, Paytm, PhonePe, carrier billing
  Note: 75%+ of payments via UPI. Card penetration under 5%. Massive potential for Gold/Premium conversion

**Key issues and vulnerabilities:**
- Massive international user/revenue gap: 57% of DAU but only 18% of revenue
- Gold purchase system redesigned after Coins complexity and regulatory compliance issues (50+ award types discontinued)
- Contributor Program payout fees ($2.25 + 0.25% + 1% FX) eat into small creator earnings
- Payment method change requires cancel and re-subscribe (no seamless switch)
- Account age requirements block new users from purchasing Premium
- AI data licensing revenue concentration risk (regulatory scrutiny, "Data Paradox")
- International ad monetization still early stage via Aleph partnership

**Key meeting angles:**
1. **International revenue gap** | 57% of users, 18% of revenue. Local payment methods directly close the monetization gap for 68.9M international daily users
2. **Stripe confirmed** | Stripe processes both purchases and creator payouts. Single dependency with zero failover for a $2.2B revenue company
3. **30-country expansion** | Reddit actively localizing content into 23+ languages and 30+ countries. Payment localization must match content localization
4. **Gold micro-transactions** | Digital goods purchases are small-ticket, high-volume. Cross-border card declines devastate conversion. Local APMs solve this
5. **Contributor Program scale** | Thousands of creators paid via Stripe Connect. Multi-rail payout optimization reduces $2.25 per-transaction overhead
6. **AI revenue diversification** | $140M data licensing growing to $400M by 2027. Payment infrastructure must support new revenue models beyond ads
7. **First profitable year** | $530M net income in 2025. Protecting margins means reducing payment failures and optimizing international ARPU

**Sources:**
- [Reddit Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Reddit_logo_new.svg)
- [Reddit Statistics 2026 (DemandSage)](https://www.demandsage.com/reddit-statistics/)
- [Reddit Revenue and DAU (KeyGroup)](https://key-g.com/blog/reddit-users-statistics-2025-mau-dau-and-global-data)
- [Reddit Q4 2025 Financials (Resourcera)](https://resourcera.com/data/social/reddit-statistics/)
- [Reddit Gold Help](https://support.reddithelp.com/hc/en-us/articles/17331548463764)
- [Reddit Premium Help](https://support.reddithelp.com/hc/en-us/articles/360043034412)
- [Reddit Contributor Program](https://support.reddithelp.com/hc/en-us/articles/17331620007572)
- [Reddit Contributor Payouts via Stripe](https://support.reddithelp.com/hc/en-us/articles/17331720493972)
- [Reddit Earning Money](https://support.reddithelp.com/hc/en-us/articles/37760672112660)
- [Reddit International Expansion (eMarketer)](https://www.emarketer.com/content/reddit-s-global-expansion-highlights-untapped-international-revenue-potential)
- [Reddit Global Playbook (eMarketer)](https://www.emarketer.com/content/reddit-s-global-playbook-pays-off-with-localized-growth-strategy)
- [Aleph + Reddit 45+ Markets](https://cyprus-mail.com/2025/10/06/aleph-reddit-expand-tie-to-over-45-global-markets/)
- [Reddit AI Data Licensing Revenue](https://www.techbuzz.ai/articles/reddit-bets-ai-search-will-be-its-next-revenue-goldmine)
- [Reddit AI Licensing Deals](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php)
- [Reddit APAC Strategy (Campaign Asia)](https://www.campaignasia.com/article/inside-reddits-strategy-to-court-advertisers-in-asia-pacific/496706)
- [Reddit Strategy Analysis (BrandHistories)](https://brandhistories.com/reddit/analysis)
