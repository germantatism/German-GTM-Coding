# WARNER BROS. DISCOVERY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Warner Bros. Discovery
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/a/a2/Warner_Bros._Discovery.svg
Nombre merchant: Warner Bros. Discovery

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Subscriber Churn Bleed
Tittle_Pain Point_2: ARPU Erosion
Tittle_Pain Point_3: Checkout Friction Global
Tittle_Pain Point_4: Single-Acquirer Fragility
Tittle_Pain Point_5: M&A Payment Complexity

Desc_Pain Point_1: Max posted 17% annual churn; failed payments drive up to 32% of cancellations. At 131.6M subs and $2.8B revenue, 1% churn recovery unlocks $28M+ annually.
Desc_Pain Point_2: Streaming ARPU dropped 9% YoY in Q4 2025 as Max enters lower-ARPU markets. Without local acquiring and smart routing, cross-border costs erode margins further.
Desc_Pain Point_3: Max accepts only Visa, MC, and PayPal in most markets. In 100+ countries, millions lack credit cards. No UPI in India, no BLIK in Poland means lost sign-ups.
Desc_Pain Point_4: Max has no visible multi-PSP strategy. Any acquirer outage blocks subscription renewals globally, risking mass involuntary churn during billing cycles.
Desc_Pain Point_5: Paramount Skydance deal ($110.9B, closing Q3 2026) merges Max, Paramount+, and Discovery+ billing. Without orchestration, three payment stacks create chaos.

SLIDE 1: PSP TOPOLOGY

PSP_1: Visa / Mastercard (direct)
PSP_2: PayPal
PSP_3: Apple App Store (iOS)
PSP_4: Google Play (Android)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI (India)
Local_M_2: BLIK (Poland)
Local_M_3: GCash (Philippines)
Local_M_4: DANA (Indonesia)
Local_M_5: GrabPay (SE Asia)
Local_M_6: KakaoPay (South Korea)
Local_M_7: Konbini (Japan)
Local_M_8: MoMo (Vietnam)
Local_M_9: PromptPay (Thailand)
Local_M_10: Nequi (Colombia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each of Max's 131.6M subscription renewals to the highest-performing acquirer per card BIN, issuer, and market. With $2.8B in streaming revenue and ARPU under pressure, even a 3% auth-rate uplift on cross-border transactions recovers $84M+ in annual recurring revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor dependency. When the primary acquirer declines a renewal, Yuno reroutes in milliseconds to the next best processor. Up to 50% recovery on failed transactions, directly cutting involuntary churn.
Desc_Yuno_Cap3: Activates APMs Max needs globally: UPI in India, BLIK in Poland, GCash in Philippines, DANA in Indonesia, GrabPay in SE Asia, KakaoPay in South Korea, Konbini in Japan. One API, 1,000+ methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying Max, Discovery+, and post-merger Paramount+ billing into a single reconciliation layer. Real-time approval monitoring across 100+ markets, centralized subscriber lifecycle management, NOVA engine for anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Warner Bros. Discovery at a glance:**
- Revenue: $37.3B total (FY 2025), streaming revenue $2.8B (+5% YoY)
- Streaming subscribers: 131.6M (Q4 2025), +15M added in 2025, targeting 150M by end of 2026
- Streaming profit: $1.3B anticipated for FY 2025 (up from $677M in 2024, $103M in 2023)
- Operating Income: $738M (FY 2025), vs. $10B+ operating loss in 2024
- Net Income: $749M (FY 2025), vs. $11.5B net loss in 2024
- CEO: David Zaslav. Streaming CEO: JB Perrette. CTO: Avi Saxena
- Employees: ~35,000 globally
- Headquarters: New York City
- Key brands: HBO, Max, Discovery+, Warner Bros. Pictures, CNN, TNT, TBS, DC Studios

**Paramount Skydance Acquisition (closing Q3 2026):**
- Deal value: $110.9B enterprise value ($81B equity), $31/share all-cash
- Shareholder vote: April 23, 2026 (WBD Board unanimously recommends FOR)
- Combined entity will merge Max + Paramount+ + Discovery+ streaming platforms
- WBD was splitting into Warner Bros. (studios + streaming) and Discovery Global (networks) before deal
- Netflix originally bid $82.7B ($27.75/share) but withdrew February 2026
- Post-merger payment infrastructure consolidation will be critical

**Confirmed PSPs and payment infrastructure:**
- Direct billing: Visa, Mastercard, American Express (US/select markets), PayPal
- Regional methods: Bancontact (Belgium), Cartes Bancaires (France), iDEAL (Netherlands), Klarna (Sweden)
- Brazil: Pix accepted (via third-party integration), Mercado Pago integration, Nubank partnership (included in Nubank+ plans)
- Mobile IAP: Apple App Store, Google Play, Amazon Appstore, Roku
- Telco/cable bundling: Available through AT&T, Comcast, and other distributors
- No payment orchestrator detected
- No multi-acquirer routing identified
- No public information on primary payment gateway (Stripe/Adyen/Braintree)

**Max global footprint (100+ countries):**
- United States (core market, 57M domestic subscribers)
- Latin America: Brazil, Mexico, Argentina, Colombia, Chile + Caribbean nations
- Europe: Nordics, Iberia, Central/Eastern Europe, France, Belgium, Netherlands, Poland
- January 2026: Germany, Italy, Switzerland launched
- March 2026: UK and Ireland launched (completing European rollout)
- Asia-Pacific: Australia (March 2025), SE Asia (Malaysia, Indonesia, Thailand, Singapore, Philippines, Hong Kong, Taiwan)
- Post-Soviet: Armenia, Georgia, Kazakhstan, Kyrgyzstan, Tajikistan (July 2025)
- Pacific Islands: Bhutan, Fiji, Maldives, Samoa, Tonga + others

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (57M domestic subscribers, core market)
  Currently offer: Visa/MC/Amex, PayPal, Apple Pay (via App Store), Google Pay
  Missing: ACH Direct Debit, Cash App Pay, Venmo direct
  Note: Well-served but heavy IAP reliance gives Apple/Google 15 to 30% commission cut.

MARKET 2: Brazil (largest LatAm streaming market)
  Currently offer: Visa/MC, Pix (via third-party), Mercado Pago, Nubank partnership
  Missing: Boleto Bancario, local installment cards (parcelamento)
  Note: Pix handles 70%+ of digital payments. Integration exists but not native/optimized.

MARKET 3: Europe (Germany, Italy, UK launched 2026)
  Currently offer: Visa/MC, PayPal, iDEAL (NL), Bancontact (BE), Klarna (SE), Cartes Bancaires (FR)
  Missing: SEPA Direct Debit (crucial for German subscriptions), Sofort, BLIK (Poland)
  Note: SEPA DD is the backbone of subscription billing in Germany. Without it, conversion suffers.

MARKET 4: Southeast Asia (Malaysia, Indonesia, Thailand, Philippines, Singapore)
  Currently offer: Visa/MC (credit card only in most markets)
  Missing: GCash, Maya, GrabPay, DANA, OVO, PromptPay, TrueMoney
  Note: Credit card penetration below 10% in Indonesia and Philippines. Mobile wallets are the primary payment rail.

MARKET 5: India (massive addressable market, not yet launched)
  Currently offer: Not available (anticipated future launch)
  Missing: UPI (75%+ of Indian digital payments), RuPay, Paytm, PhonePe
  Note: India represents 1.4B+ population with exploding OTT adoption. UPI is mandatory for any subscription service.

**Churn and payment performance:**
- Annual churn rate: 17% (April 2023 to March 2024 period)
- Premium streamer average monthly churn: 4.1% (industry benchmark)
- Involuntary churn: accounts for 18 to 32% of total cancellations in streaming
- Disney+/Hulu/Max bundle: 80% retention rate after 3 months (outperforming Netflix)
- ARPU declined 9% YoY in Q4 2025 due to expansion into lower-ARPU international markets
- WBD discontinued ARPU reporting after Q4 2025

**Key meeting angles:**
1. **131.6M subscribers, $2.8B revenue** | At this scale, even basis-point auth-rate improvements translate to millions in recovered revenue
2. **Paramount merger** | Consolidating Max + Paramount+ + Discovery+ payment stacks is a once-in-a-decade infrastructure challenge
3. **17% churn rate** | Involuntary churn from failed payments represents the lowest-hanging recovery opportunity
4. **ARPU pressure** | Smart routing and local acquiring in international markets preserves margin per subscriber
5. **SE Asia + India** | Credit card penetration below 10%; without local APMs, Max cannot convert these massive markets
6. **IAP fee arbitrage** | Routing web/app subscribers through local APMs instead of Apple/Google IAP saves 15 to 30% in commission
7. **Europe 2026 rollout** | Germany (SEPA DD), UK, Italy launches need optimized local payment rails from day one
8. **Competitor precedent** | Netflix (Adyen, multi-PSP), Disney+ (multi-gateway), Spotify (Adyen + local APMs in 180+ markets)

**Sources:**
- [WBD Q4 2025 Earnings Report](https://www.wbd.com/news/warner-bros-discovery-reports-fourth-quarter-and-full-year-2025-results)
- [WBD Q3 2025 Earnings Report](https://www.wbd.com/news/warner-bros-discovery-reports-third-quarter-2025-results)
- [WBD Q1 2025 Earnings Report](https://www.wbd.com/news/warner-bros-discovery-reports-first-quarter-2025-results)
- [WBD Leadership Page](https://www.wbd.com/leadership)
- [Variety: HBO Max 132M Subscribers](https://variety.com/2026/film/news/hbo-max-subscribers-132-million-warner-bros-discovery-earnings-1236673104/)
- [Streamable: WBD Q4 2025 131.6M Subs, $2.8B Streaming Revenue](https://thestreamable.com/warner-bros-discovery-q4-2025-earnings-report)
- [Hollywood Reporter: WBD Q1 2025 Adds 5.3M Subs](https://www.hollywoodreporter.com/business/business-news/warner-bros-discovery-q1-2025-earnings-streaming-growth-1236210369/)
- [Variety: WBD Q2 2025 Profit, Max Expansion](https://variety.com/2025/tv/news/warner-bros-discovery-q2-profit-hbo-max-expansion-minecraft-1236481308/)
- [StreamTV Insider: WBD Pegs 2026 as Major Growth Year](https://www.streamtvinsider.com/content/warner-bros-discovery-pegs-2026-major-growth-year-hbo-max-globally)
- [WBD Press: Max UK and Ireland Launch](https://press.wbd.com/us/media-release/hbo-max-now-streaming-uk-and-ireland-major-international-expansion)
- [WBD Press: Max July 2025 Global Expansion](https://press.wbd.com/us/media-release/hbo-max/hbo-max-accelerates-global-growth-strategy-july-expansion-multiple-new-markets)
- [Deadline: Max UK, Germany, Italy Launch Dates](https://deadline.com/2025/12/hbo-max-germany-italy-2026-launch-date-january-1236634223/)
- [WBD: Paramount Skydance Shareholder Vote April 23](https://www.wbd.com/news/warner-bros-discovery-sets-shareholder-meeting-date-april-23-2026-approve-transaction)
- [Paramount: WBD Acquisition Announcement](https://www.prnewswire.com/news-releases/paramount-to-acquire-warner-bros-discovery-to-form-next-generation-global-media-and-entertainment-company-302699998.html)
- [NPR: WBD Split Announced](https://www.npr.org/2025/06/09/nx-s1-5428176/warner-bros-discovery-split-hbo-max-zaslav)
- [Britannica Money: Paramount Wins WBD After Netflix Drops](https://www.britannica.com/money/netflix-paramount-skydance-battle-for-warner-bros)
- [WBD Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Warner_Bros._Discovery.svg)
- [HBO Max Help: Payment Methods](https://help.hbomax.com/us/Answer/Detail/000002525)
- [HBO Max Help: Billing & Subscription](https://help.hbomax.com/us/Category/Detail/Billing_Subscription)
- [HBO Max Help: Plans](https://help.hbomax.com/plans)
- [Mercado Pago x HBO Max Brazil](https://www.mercadopago.com.br/ajuda/18136)
- [Churnkey: Streaming Churn Rates](https://churnkey.co/blog/churn-rates-for-streaming-services/)
- [BroadbandTV News: US Streaming Churn Surge](https://www.broadbandtvnews.com/2025/08/20/us-streaming-platforms-shift-focus-to-retention-as-churn-rates-surge/)
- [Deadline: WBD Post-Split Leadership](https://deadline.com/2025/07/warner-bros-discovery-separates-new-leadership-1236472293/)
