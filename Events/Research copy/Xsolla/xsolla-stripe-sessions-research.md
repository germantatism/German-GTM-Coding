# XSOLLA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Xsolla
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/f/fb/Xsolla_New_Logo.svg
Nombre merchant: Xsolla

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Adyen Single Acquirer
Tittle_Pain Point_2: MoR Fee Pressure
Tittle_Pain Point_3: Chargeback Escalation
Tittle_Pain Point_4: Auth Rate Blind Spots
Tittle_Pain Point_5: PSP Mode Complexity

Desc_Pain Point_1: Xsolla's new PSP mode relies entirely on Adyen as global acquirer. No redundancy: if Adyen declines or experiences downtime, zero failover exists for card transactions across 200+ markets.
Desc_Pain Point_2: MoR model charges 5% of revenue vs. PSP at lower rates. Game studios migrating to PSP mode lose Xsolla's tax/compliance layer but gain no multi-acquirer routing or intelligent optimization.
Desc_Pain Point_3: Game developers face Visa Fraud Monitoring when chargeback rates exceed 1%. Xsolla auto-blocks accounts on chargeback, penalizing legitimate players. Fines reach $10K/month per card scheme.
Desc_Pain Point_4: 1,000+ payment methods across 200+ regions but no transparent per-method authorization reporting. Developers cannot see which APMs underperform or which acquirer routes leak revenue.
Desc_Pain Point_5: New PSP mode requires developers to manage taxes, compliance, fraud, and end-user support independently. Studios must rebuild what the MoR handled, adding cost and operational risk.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (primary acquirer)
PSP_2: PayPal
PSP_3: Mercado Pago (Brazil)
PSP_4: Xsolla Pay Station (proprietary)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Dana (Indonesia)
Local_M_2: TrueMoney (Thailand)
Local_M_3: Toss (South Korea)
Local_M_4: PhonePe (India)
Local_M_5: Nequi (Colombia)
Local_M_6: Yape (Peru)
Local_M_7: CoDi (Mexico)
Local_M_8: Rapipago (Argentina)
Local_M_9: LINE Pay (Japan)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each gaming transaction across multiple acquirers by card BIN, issuer, country, and game genre risk profile. With $522B global gaming market and 3.6B players, even a 3% auth uplift on Xsolla's 1,500+ studios translates to massive recovered revenue per title.
Desc_Yuno_Cap2: Automatic cascade eliminates Xsolla's single Adyen dependency. When Adyen declines a card, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions. Critical for high-volume game launches and in-game purchase spikes.
Desc_Yuno_Cap3: Fills gaps across Xsolla's 200+ markets: Dana in Indonesia, PhonePe in India, Toss in South Korea, Nequi in Colombia, Yape in Peru. One API, 1,000+ methods. Complements Xsolla's existing APMs with deeper local coverage where it matters most.
Desc_Yuno_Cap4: Single dashboard spanning Xsolla's Adyen + PayPal + Mercado Pago + Pay Station stack. Real-time per-method authorization analytics, centralized reconciliation across all providers and currencies. NOVA anti-fraud reduces chargebacks 75%, keeping studios off Visa monitoring programs.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Xsolla at a glance:**
- Gaming commerce platform, private company, HQ Sherman Oaks, California. Founded 2005 by Aleksandr Agapitov
- Revenue: ~$100M (2021 disclosed); private, no recent public figures. Estimated significantly higher by 2026
- Serves 1,500+ game developers globally across 200+ geographies, 160+ currencies
- Products: Pay Station (checkout), Merchant of Record, PSP mode (launched Aug 2025), Anti-Fraud, Game Store, Partner Network
- Supports 1,000+ local payment methods across 130+ countries
- Strategic partnership with Adyen (Aug 2025) for global acquiring in PSP mode
- Key clients: Epic Games, Roblox, Ubisoft, PUBG, Valve, Twitch
- 2021 controversy: AI-based layoffs of 150 employees, negative public perception
- Gaming market context: $522.5B global (2025), growing at 7.25% CAGR to $691.3B by 2029

**Confirmed PSPs and Partners:**
- Adyen: primary global acquirer for PSP mode, card processing across 200+ markets
- PayPal: alternative payment option across multiple game studios
- Mercado Pago: recurring billing in Brazil
- Xsolla Pay Station: proprietary checkout UI with 1,000+ methods
- ShopeePay: Malaysia, Singapore, Thailand
- FPX: Malaysia bank transfers
- Affirm: US and Canada BNPL
- Bizum (Spain), Swish (Sweden), Satispay (Italy): European local methods
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest gaming market, $55B+)
  Supported: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Affirm, Pay by Bank
  Missing: Cash App Pay, Venmo standalone, ACH for subscriptions
  Note: Largest market for PC/console D2C web stores

MARKET 2: China ($45B+ gaming market)
  Supported: WeChat Pay, Alipay, UnionPay
  Missing: Douyin Pay, Huawei Pay
  Note: Regulatory complexity limits direct reach; most revenue via local publishers

MARKET 3: Japan ($20B+ gaming market)
  Supported: Konbini, MerPay (added 2025), credit cards
  Missing: LINE Pay, PayPay, Rakuten Pay
  Note: Cash-on-delivery and convenience store payments still dominant for gaming

MARKET 4: Brazil ($3B+ gaming market)
  Supported: Mercado Pago (recurring billing added 2025), credit cards
  Missing: Pix (real-time), Boleto for lower-income gamers
  Note: Pix processes 70%+ of Brazilian digital payments; critical gap for gaming

MARKET 5: India ($3B+ gaming market, 500M+ gamers)
  Supported: Basic card payments, UPI via Adyen
  Missing: PhonePe, Paytm, RuPay, carrier billing depth
  Note: 75%+ of payments via UPI; mobile gaming dominates with low ARPU

**Key competitive vulnerabilities:**
- Adyen single-acquirer dependency in PSP mode creates concentration risk
- MoR model at 5% revenue share is expensive vs. Stripe (2.9% + $0.30) or direct Adyen integration
- 2021 AI layoffs scandal damaged employer brand and developer trust
- BBB complaints about unauthorized charges and account blocking without evidence
- FastSpring, Paddle, Stripe, and Appcharge all competing for gaming D2C payments
- PSP mode launched Aug 2025 is immature vs. established orchestrators
- No transparent per-method auth rate dashboard for developers

**Key meeting angles:**
1. **Adyen single dependency** | New PSP mode routes 100% of cards through Adyen with zero failover. Yuno adds multi-acquirer resilience
2. **1,500 studios, one orchestration gap** | Massive developer base but no intelligent routing between Adyen, PayPal, Mercado Pago
3. **Chargeback crisis** | Gaming has high fraud rates. NOVA anti-fraud at 75% chargeback reduction keeps studios off Visa monitoring
4. **MoR to PSP migration** | Studios moving to PSP need the routing intelligence that Xsolla MoR never provided
5. **LATAM gaming explosion** | Brazil, Mexico, Colombia growing fast. Pix, OXXO, Nequi are table stakes Xsolla partially covers
6. **Auth rate visibility** | 1,000+ methods but no per-route performance analytics. Yuno provides real-time optimization dashboards
7. **Competitor pressure** | FastSpring and Paddle offer MoR + better rates. Xsolla needs orchestration differentiation

**Sources:**
- [Xsolla Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Xsolla_New_Logo.svg)
- [Xsolla + Adyen Partnership (BusinessWire)](https://www.businesswire.com/news/home/20250814871369/en/)
- [Xsolla + Adyen Blog](https://xsolla.com/blog/xsolla-and-adyen-partner-to-power-global-game-payments)
- [Xsolla PSP Product Page](https://xsolla.com/payment-service-provider)
- [Xsolla Wikipedia](https://en.wikipedia.org/wiki/Xsolla)
- [Xsolla Supported Countries](https://developers.xsolla.com/dev-resources/references/supported-countries/)
- [Xsolla 1,000+ Payment Methods](https://80.lv/articles/xsolla-now-supports-over-1-000-local-payment-methods-across-200-regions)
- [Xsolla Payment Expansion (Games Press)](https://www.gamespress.com/XSOLLA-LAUNCHES-GLOBAL-PAYMENT-EXPANSION-ACROSS-ASIA-EUROPE-AND-THE-AM)
- [Xsolla State of Play Q3 2025](https://xsolla.com/the-xsolla-report)
- [Xsolla BBB Complaints](https://www.bbb.org/us/ca/sherman-oaks/profile/video-game-services/xsolla-usa-inc-1216-1004824/complaints)
- [Xsolla MoR vs PSP Blog](https://xsolla.com/blog/choose-the-right-payment-partner-mor-vs-psp)
- [Xsolla Anti-Fraud](https://xsolla.com/anti-fraud)
- [Xsolla Chargeback Docs](https://developers.xsolla.com/payment-ui-and-flow/anti-fraud/chargeback/)
- [7 Best Xsolla Competitors 2026 (FastSpring)](https://fastspring.com/blog/xsolla-competitors/)
- [Xsolla Trustpilot Reviews](https://www.trustpilot.com/review/secure.xsolla.com)
