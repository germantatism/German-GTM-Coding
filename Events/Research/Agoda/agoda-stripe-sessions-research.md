# AGODA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Agoda
═══════════════════════════════════════

Logo: https://seeklogo.com/images/A/agoda-logo-3D3D2ECE77-seeklogo.com.png
Nombre merchant: Agoda

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: PSP Fragmentation
Tittle_Pain Point_2: Cross-Border Auth Leakage
Tittle_Pain Point_3: SEA Wallet Gaps
Tittle_Pain Point_4: FX Cost Hemorrhage
Tittle_Pain Point_5: Fraud and Double-Charge Incidents

Desc_Pain Point_1: At least 4 PSPs (Adyen, Antom, Juspay, J.P. Morgan) plus app store IAP channels, each with separate dashboards, settlement files, and reconciliation logic. Juspay case study confirms "complex reconciliation across multiple currencies and PSPs with incompatible settlement file formats." Every new market or method adds another integration sprint.
Desc_Pain Point_2: 190+ countries with massive cross-border card volume. Agoda's Head of FinTech Jibran Bugvi called FX "a killer" for emerging market travelers. Local banks regularly decline international charges, and prepaid/debit cards from SEA markets fail at checkout. No public auth-rate metric disclosed, signaling room to improve.
Desc_Pain Point_3: Agoda operates across Thailand, Indonesia, Philippines, Vietnam, and Malaysia, yet core checkout still lists only 5 card networks plus PayPal. Regional wallets (GrabPay, DANA, OVO, ShopeePay, PromptPay, TrueMoney) are absent from the main help page. Some wallets are available only through Juspay in limited markets (VNPay, PayPay, LINE Pay), leaving large swaths of SEA travelers without their preferred method.
Desc_Pain Point_4: J.P. Morgan case study shows Agoda expanded from 14 to 27 settlement currencies to reduce FX exposure, with manual settlement consuming "up to 30 work hours per month." Cross-border FX markup hits every transaction where the traveler's currency differs from the property's currency. Australian travelers report a hidden 5% foreign transaction fee on AUD bookings.
Desc_Pain Point_5: Consumer complaint sites document repeated double-charge incidents (credit cards billed twice for the same reservation), currency conversion errors (charged in USD instead of local THB), and overcharges up to 30% above displayed rates. Slow refund resolution erodes trust and increases chargeback risk.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: Antom (Ant International)
PSP_3: Juspay
PSP_4: J.P. Morgan

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: GrabPay
Local_M_2: DANA
Local_M_3: OVO
Local_M_4: ShopeePay
Local_M_5: PromptPay
Local_M_6: TrueMoney
Local_M_7: GoPay
Local_M_8: Pix
Local_M_9: BLIK
Local_M_10: KakaoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & NOVA AI Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen, Antom, and additional acquirers based on card BIN, issuer country, and historical performance. With estimated revenue of $1B to $5B and 190+ country coverage, even a 3% auth uplift from intelligent routing translates to tens of millions in recovered bookings annually. InDrive achieved 90% approval rates across 10 markets with this approach.
Desc_Yuno_Cap2: Automatic cascade eliminates single-PSP dependency. When Adyen declines a Thai traveler's debit card, Yuno reroutes to a local acquirer in milliseconds. Up to 50% recovery on soft declines via standard failover. NOVA AI pushes recovery to 75% on hard declines, matching Viva Aerobus results. Zero customer friction, zero abandoned bookings.
Desc_Yuno_Cap3: Activates the SEA wallets Agoda travelers demand but cannot use today: GrabPay (SG/MY/PH/TH), DANA and OVO (Indonesia), PromptPay and TrueMoney (Thailand), ShopeePay (region-wide), GoPay (Indonesia). One API, 1,000+ payment methods, 300+ processors, 200+ countries. No multi-month engineering sprints per market.
Desc_Yuno_Cap4: One dashboard replacing Agoda's fragmented Adyen + Antom + Juspay + J.P. Morgan settlement streams. Real-time approval rate monitoring, centralized reconciliation across all providers and 27+ currencies, millisecond anomaly detection. Eliminates the "30 work hours per month" manual settlement burden documented in the J.P. Morgan case study.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Agoda at a glance:**
- Subsidiary of Booking Holdings (NYSE: BKNG). Parent revenue: $23.7B (FY2024, +11.2% YoY). Parent gross bookings: $165.6B
- Agoda estimated revenue: $1B to $5B annually (standalone figures not publicly broken out)
- 4.5M+ properties listed across 190+ countries
- 20% market share in APAC online accommodation
- Headquarters: Singapore. ~7,000 employees
- CEO: Omri Morgenshtern (since 2022, at Agoda since 2014 via Qlika acquisition)
- CTO: Idan Zalzberg (since 2014)
- Head of FinTech & Business Initiatives: Jibran Bugvi (quoted in Juspay and Antom case studies)
- VP Commercial Finance: Darren Makarem (quoted in Adyen press release)
- September 2025: ~50 layoffs in Singapore office

**Confirmed PSPs and payment partners:**
- Adyen: primary acquirer since 2015. Provides local acquiring, Real Time Account Updater, alternative payment methods (ATM bank transfers, convenience store payments). Press release March 2019
- Antom (Ant International): partner since 2014. Started with Alipay wallets, expanded to global payments. Provides Antom Shield (AI fraud prevention), payment orchestration, A+ Rewards marketing tool
- Juspay: payment orchestration layer. Connects VNPay (Vietnam), PayPay (Japan), LINE Pay (Taiwan), Apple Pay, UPI. Enables fallback routing across 3 PSPs and 7 APMs in 29 countries
- J.P. Morgan: settlement bank. 27 currency accounts across 12 branches globally (APAC, UK, US, Canada). Virtual card self-issuance program
- Mastercard: B2B payment partnership (January 2026) for supplier/property payments

**Payment methods currently confirmed on Agoda:**
- Cards: Visa, Mastercard, American Express, JCB, Carte Bleue
- Wallets: PayPal, Alipay (via Antom), VNPay (Vietnam, via Juspay), PayPay (Japan, via Juspay), LINE Pay (Taiwan, via Juspay), Apple Pay (via Juspay), GCash (Philippines, limited)
- Bank transfers: select Indonesian banks (BNI, CIMB Niaga, Mandiri)
- Other: convenience store payments (select markets), UPI (India, via Juspay), Pay at Hotel (cash/card on arrival)

**Top 5 Markets Gap Analysis:**

MARKET 1: Thailand (Agoda's home turf, #1 inbound market)
  Currently offer: Visa/MC/Amex/JCB, PayPal, Pay at Hotel
  Missing: PromptPay, TrueMoney, Rabbit LINE Pay, mobile banking apps
  Note: PromptPay is Thailand's government-backed real-time payment rail used by 70M+ accounts. Its absence from Agoda's checkout is a major friction point for domestic Thai travelers.

MARKET 2: Indonesia (largest SEA e-wallet market)
  Currently offer: Visa/MC, bank transfers (BNI/CIMB/Mandiri), convenience store payments
  Missing: GoPay, DANA, OVO, ShopeePay, QRIS
  Note: Credit card penetration under 5%. 78% of Indonesian digital transactions use e-wallets. Agoda introduced bank transfers but skipped the dominant wallets entirely.

MARKET 3: Philippines (high-growth travel market)
  Currently offer: Visa/MC, GCash (limited availability), PayPal
  Missing: Maya, GrabPay, ShopeePay, BPI/BDO online banking
  Note: Credit card penetration ~6%. GCash has 60M+ users. Maya (formerly PayMaya) is the second-largest wallet. Without broad wallet coverage, most Filipino travelers cannot pay online.

MARKET 4: Japan (#1 inbound tourist destination on Agoda)
  Currently offer: Visa/MC/JCB, PayPay (via Juspay)
  Missing: Konbini, Carrier billing, PayPay broader rollout, Rakuten Pay
  Note: PayPay integration exists through Juspay but was only announced in May 2024, suggesting limited rollout. Konbini (convenience store) payments are standard for Japanese e-commerce.

MARKET 5: South Korea (top 5 Agoda inbound market)
  Currently offer: Visa/MC, PayPal
  Missing: KakaoPay, Naver Pay, Toss, Samsung Pay, local card networks (BC Card, Lotte Card)
  Note: KakaoPay has 37M+ users in a country of 52M. Korean travelers booking via Agoda have extremely limited local payment options.

**Pain point evidence (sourced):**

1. PSP Fragmentation: Juspay case study documents "fragmented payment flows across Southeast Asia and Middle East" with "lengthy integration timelines for new payment methods (weeks or months of development)" and "complex reconciliation across multiple currencies and PSPs with incompatible settlement file formats." Source: juspay.io/customer-stories/agoda

2. FX and Cross-Border Costs: J.P. Morgan case study documents manual settlement consuming "up to 30 work hours per month" before automation, with expansion from 14 to 27 settlement currencies needed to manage FX exposure. Jibran Bugvi (Head of FinTech) stated "FX is a killer" for emerging market travelers. Source: jpmorgan.com/insights/payments/commercial-cards/agoda-virtual-card-program, knowledge.antom.com/agoda-antom-shaping-tomorrows-travel-payments

3. Double Charges and Payment Errors: Consumer complaint platform Xolvie documents multiple 2024 and 2025 incidents: credit cards charged twice for single reservations, currency conversion errors (charged USD instead of THB), overcharges up to 30% above displayed rates, and slow refund processing. Source: sikayetvar.com/en/agoda-us

4. System Outages: Monitoring sites document recurring Agoda payment failures including "unable to proceed to payment" errors (April 2025), search function outages (December 2024), and geographic clusters of reports from Thailand, Australia, and the US. Source: outagedown.com/web/agoda.com, updownradar.com/status/agoda.com

5. Fraud Exposure: Travel vertical experiences elevated fraud rates per Antom case study. TripAdvisor forums document unauthorized transactions on credit cards used with Agoda. Agoda uses Antom Shield for fraud monitoring but cross-border card-not-present transactions remain high risk. Source: tripadvisor.com forums, knowledge.antom.com

**Key meeting angles:**

1. **Orchestration already in play** | Agoda already uses Juspay for orchestration across 3 PSPs and 29 countries. This proves they believe in the orchestration model. Yuno offers 300+ processors (vs. Juspay's limited network), 1,000+ APMs, and proven enterprise results (McDonald's +4.7%, Wingo +14%).

2. **SEA wallet gap is revenue leakage** | Agoda's core market is SEA, where credit card penetration is below 10% in most countries. Without GrabPay, DANA, OVO, PromptPay, and ShopeePay, millions of potential bookings die at checkout. Yuno activates all of these through a single API.

3. **FX cost reduction** | Agoda expanded to 27 settlement currencies to manage FX exposure. Yuno's local acquiring across 200+ countries routes transactions through domestic rails, eliminating cross-border interchange and FX markups at the processor level.

4. **Booking Holdings context** | Sister brand Booking.com partnered with Antom in January 2025 to add 40+ new payment methods across 8 Asian markets. Agoda should match or exceed this APM coverage in its home territory.

5. **NOVA AI recovery** | With Agoda's massive cross-border volume, even small auth rate improvements translate to significant revenue. NOVA AI's 75% hard-decline recovery rate (proven at Viva Aerobus) applied to Agoda's multi-billion-dollar booking volume represents a substantial revenue recovery opportunity.

6. **Consolidation play** | Replace the Adyen + Antom + Juspay + J.P. Morgan patchwork with one orchestration layer. Reduce operational burden, eliminate the 30-hour/month manual settlement bottleneck, and gain unified real-time analytics across all processors.

7. **Head of FinTech is the buyer** | Jibran Bugvi owns payment infrastructure decisions and has publicly discussed payment pain points. He is the primary contact for a Yuno conversation.

**Sources:**
- [Adyen Press Release: Agoda Partnership (2019)](https://www.adyen.com/press-and-media/agoda-partners-with-adyen-to-improve-payment-experience-for-customers)
- [Antom: Agoda Shaping Tomorrow's Travel Payments](https://knowledge.antom.com/agoda-antom-shaping-tomorrows-travel-payments)
- [Juspay: Agoda Case Study](https://juspay.io/customer-stories/agoda)
- [J.P. Morgan: Agoda Virtual Card Program](https://www.jpmorgan.com/insights/payments/commercial-cards/agoda-virtual-card-program)
- [Agoda Press: PayPay Partnership (2024)](https://www.agoda.com/press/agoda-partners-with-paypay-to-enhance-travel-payment-options-in-japan/)
- [Agoda Press: Alternative Payments Indonesia](https://www.agoda.com/press/alternative-payment-indonesia/)
- [Agoda: How Do I Pay](https://www.agoda.com/info/how-do-i-pay-for-my-booking.html)
- [Agoda Press: Leadership](https://www.agoda.com/press/leadership/)
- [Xolvie: Agoda Payment Complaints](https://www.sikayetvar.com/en/agoda-us)
- [Payment Expert: Andrew Smith on Agoda Innovations](https://paymentexpert.com/2024/04/16/andrew-smith-agodas-innovations/)
- [Booking Holdings FY2024 Earnings](https://www.bookingholdings.com/wp-content/uploads/2024/02/BKNG-Earnings-Release-Final.pdf)
- [BusinessWire: Booking.com and Antom Partnership (2025)](https://www.businesswire.com/news/home/20250114445080/en/Booking.com-and-Antom-Partner-to-Expand-Local-Payment-Options-Across-Asia)
- [WalletBoat: Agoda Foreign Transaction Fee](https://www.walletboat.com/lifestyle/agodas-5-foreign-fee-how-to-avoid-it/)
- [Agoda Logo (Seeklogo)](https://seeklogo.com/vector-logo/309548/agoda)
- [Brandfetch: Agoda Brand Assets](https://brandfetch.com/agoda.com)
