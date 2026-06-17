# LATAM Airlines | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: LATAM Airlines
=======================================

Logo: https://images.seeklogo.com/logo-png/28/1/latam-airlines-logo-png_seeklogo-287010.png
Nombre merchant: LATAM Airlines

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border Decline Surge
Tittle_Pain Point_2: Checkout Conversion Collapse
Tittle_Pain Point_3: Missing Local Payment Rails
Tittle_Pain Point_4: Refund & Double-Charge Chaos
Tittle_Pain Point_5: Multi-Market PSP Complexity

Desc_Pain Point_1: LATAM operates across 7+ countries, each with distinct card networks and issuer behavior. Regional card decline rates hit 15% to 25%, with Brazil alone at 5% fraud-related declines (double the global average). Cross-border transactions from Chilean or Peruvian cards to foreign acquirers trigger elevated false declines, leaking revenue on every international route sale.
Desc_Pain Point_2: FlyerTalk and TripAdvisor forums document years of persistent payment failures at checkout: "The operation was not completed, please try again later." Users report trying 8+ times across multiple devices, browsers, and cards. The payment page freezes at step 4 of 6, forcing travelers to abandon or book through third parties like Expedia at higher fares. Phone bookings add $35 to $40 surcharges per passenger.
Desc_Pain Point_3: LATAM accepts Visa, Mastercard, Amex, Diners Club, Hipercard, Elo, PayPal, SafetyPay, and PSE (Colombia). Missing from checkout: Pix (170M+ Brazilian users), Mercado Pago (Latin America's largest wallet), OXXO (Mexico cash vouchers), Nequi (Colombia), Webpay (Chile domestic), and MACH (Chile). In Brazil, where credit card penetration is under 35%, the absence of Pix alone excludes a massive buyer segment.
Desc_Pain Point_4: Consumer complaints document repeated double-charge incidents where cards are billed twice for a single booking. One documented 2024 case: LATAM charged $77 and $722, refunded both, then recharged both amounts months later without authorization. FlyerTalk users describe "nearly a year, almost 100 emails, zero accountability." Slow refund processing and unauthorized recharges erode customer trust and inflate chargeback ratios.
Desc_Pain Point_5: LATAM must manage separate PSP integrations, settlement files, and reconciliation logic across Brazil, Chile, Colombia, Peru, Ecuador, Argentina, and the US. SafetyPay handles bank transfers in select markets, PSE covers Colombia, and card acquiring varies by country. Each new market or payment method requires a dedicated integration sprint, slowing expansion and creating operational overhead for a 43,000-employee organization.

SLIDE 1: PSP TOPOLOGY

PSP_1: SafetyPay
PSP_2: PSE (Colombia)
PSP_3: Card acquiring (country-specific, unconfirmed primary gateway)
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: Mercado Pago
Local_M_3: OXXO
Local_M_4: Nequi
Local_M_5: Webpay (Chile)
Local_M_6: MACH (Chile)
Local_M_7: Yape (Peru)
Local_M_8: PagoEfectivo (Peru)
Local_M_9: Rapipago (Argentina)
Local_M_10: Efecty (Colombia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & NOVA AI Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple acquirers based on card BIN, issuer country, and historical approval performance. With $13B in annual revenue and 82M passengers across 7+ countries, even a 3% auth uplift from intelligent routing translates to hundreds of millions in recovered ticket sales. Wingo Airlines achieved +14% authorization improvement with this exact approach. InDrive reached 90% approval across 10 LATAM markets.
Desc_Yuno_Cap2: Automatic cascade across acquirers eliminates the single-point failures that plague LATAM's checkout today. When a Chilean traveler's card gets declined by one processor, Yuno reroutes to a local acquirer in milliseconds. 50% recovery on soft declines via standard failover. NOVA AI pushes recovery to 75% on hard declines, matching Viva Aerobus airline results. Zero customer friction, zero abandoned bookings.
Desc_Yuno_Cap3: Activates the payment methods LATAM's passengers demand but cannot use today: Pix (Brazil, 170M+ users), Mercado Pago (region-wide), OXXO (Mexico), Nequi (Colombia), Yape (Peru), Webpay and MACH (Chile). One API, 1,000+ payment methods, 300+ processors, 200+ countries. No multi-month engineering sprints per market. Rappi achieved zero-effort implementation across its LATAM footprint.
Desc_Yuno_Cap4: One dashboard replacing LATAM's fragmented SafetyPay + PSE + country-specific card acquirer patchwork. Real-time approval rate monitoring, centralized reconciliation across all 7+ country operations and multiple currencies, millisecond anomaly detection. Eliminates duplicated PSP management overhead for a team already running a $13B revenue operation across the continent.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**LATAM Airlines at a glance:**
- Largest airline group in South America, one of the largest globally by passengers transported
- Revenue: $13.03B (FY2024, +10.6% YoY). Net income: $977M (nearly doubled from prior year)
- Record 82 million passengers carried in 2024. 15.1% capacity expansion YoY
- Operating margin: 12.7% (highest in company history)
- Q2 2025 revenue: $3.28B (+8.2% YoY). Q3 2025 revenue: $3.86B (+17.3% YoY)
- Headquarters: Santiago, Chile. ~43,000 employees
- Ticker: SNSE: LTM. Emerged from Chapter 11 bankruptcy in November 2022
- CEO: Roberto Alvo (since March 2020, joined LAN Airlines in 2001)
- Chief Information & Digital Officer: Juliana Rios (20+ years in finance/airline tech, former Banco Santander executive)
- Operations across Chile, Brazil, Colombia, Peru, Ecuador, Argentina, and international routes to US, Europe, Oceania
- Fleet modernization: receiving first Embraer E195-E2 aircraft in late 2025
- 100% migrated to Google Cloud. AI-driven "70/50/2 Project": 70% of customer service via conversational AI, 50% proactive interactions within 2 years
- Named to FTE Airline Digital Transformation Power List Americas 2024 and 2025
- Selected GitLab Ultimate and Duo Enterprise for consolidated software toolchain

**Confirmed PSPs and payment partners:**
- SafetyPay: bank transfer platform available in select Latin American markets (Brazil, Peru, Ecuador confirmed)
- PSE (Pagos Seguros en Linea): Colombian online banking payment rail integrated for Colombia market
- PayPal: available as checkout option across markets
- LATAM Wallet: proprietary digital wallet for refunds, rewards, and ticket purchases. Can be loaded via bank transfer or cash (Brazil, Peru, Ecuador). No maintenance fees. Combines with credit card at checkout
- Card acquiring: country-specific arrangements (primary gateway not publicly disclosed). Accepts Visa, Mastercard, American Express, Diners Club (Brazil, Chile, Colombia, Ecuador, Argentina), Hipercard and Elo (Brazil only)

**Payment methods currently confirmed:**
- Cards: Visa, Mastercard, American Express, Diners Club, Hipercard (Brazil), Elo (Brazil)
- Wallets: PayPal, LATAM Wallet (proprietary)
- Bank transfers: SafetyPay (select countries), PSE (Colombia)
- Other: Cash loading for LATAM Wallet (Brazil, Peru, Ecuador)

**Top 5 Markets Gap Analysis:**

MARKET 1: Brazil (LATAM's largest domestic market)
  Currently offer: Visa/MC/Amex/Diners/Hipercard/Elo, SafetyPay, PayPal, LATAM Wallet
  Missing: Pix, Mercado Pago, Boleto Bancario (for non-banked), PicPay
  Note: Pix processed $346B+ in transactions and has 170M+ registered users. It is Brazil's dominant payment rail. Its absence from LATAM's checkout is a critical gap. Credit card penetration is under 35% in Brazil.

MARKET 2: Chile (LATAM's home market)
  Currently offer: Visa/MC/Amex/Diners, PayPal, LATAM Wallet
  Missing: Webpay (domestic debit rail), MACH (digital wallet), Mercado Pago, Khipu
  Note: Webpay is Chile's national debit payment system used by most domestic online shoppers. MACH is a popular fintech wallet among younger Chilean consumers.

MARKET 3: Colombia (3rd largest LATAM market)
  Currently offer: Visa/MC/Amex/Diners, PSE, PayPal, LATAM Wallet
  Missing: Nequi (16M+ users), Daviplata, Efecty (cash voucher), Bancolombia QR
  Note: Nequi is Colombia's fastest-growing digital wallet with 16M+ users. Cash-based methods like Efecty serve the 40%+ unbanked population.

MARKET 4: Peru (key domestic operation)
  Currently offer: Visa/MC/Amex/Diners, SafetyPay, PayPal, LATAM Wallet
  Missing: Yape (15M+ users), PagoEfectivo, BCP mobile banking, BBVA wallet
  Note: Yape dominates Peru's digital payment landscape with 15M+ users. PagoEfectivo enables cash/bank payments for the unbanked segment.

MARKET 5: Mexico (international route market)
  Currently offer: Visa/MC/Amex, PayPal
  Missing: OXXO (cash vouchers), SPEI (instant bank transfer), Mercado Pago, CoDi
  Note: OXXO vouchers serve 20M+ users who pay for online purchases at 20,000+ convenience stores. SPEI is Mexico's real-time bank transfer system. These are essential for reaching Mexico's large unbanked population.

**Pain point evidence (sourced):**

1. Cross-Border Decline Surge: Rapyd research documents LATAM regional card decline rates of 15% to 25%, with Brazil fraud-related declines at 5% (double the global 2.6% average). Nearly 20% of LATAM e-commerce revenue is lost to fraud and false declines. Cross-border card-not-present transactions from regional issuers trigger elevated rejection rates at foreign acquirers. Source: rapyd.net/blog/payment-processing-decline-rates-in-latam/

2. Checkout Conversion Collapse: FlyerTalk forum documents multi-year persistent payment failures. Users report "The operation was not completed, please try again later" errors, checkout freezing at step 4 of 6, multiple failed attempts across devices and browsers. TripAdvisor threads spanning 7+ years document the same recurring payment failures. Phone booking surcharges of $35 to $40 per passenger. Source: flyertalk.com/forum/latam-latam-pass/2068363, tripadvisor.com/ShowTopic-g1-i10702-k9502817

3. Double-Charge and Refund Failures: FlyerTalk 2025 complaint documents LATAM charging $77 and $722, issuing refunds, then recharging both amounts months later without authorization. Customer spent "nearly a year, almost 100 emails" with "zero accountability, zero explanations, zero solutions." Cases closed with no resolution. Source: flyertalk.com/forum/latam-latam-pass/2185465-latam-airlines-unjustified-charges-denials

4. PSP Fragmentation Overhead: LATAM manages separate payment integrations across 7+ countries with country-specific card acquiring, SafetyPay for bank transfers, PSE for Colombia, and PayPal as an overlay. Each market has different card networks (Elo/Hipercard in Brazil, Diners in select countries). The CellPoint Digital airline payments analysis confirms that LATAM airlines face "complexity from managing multiple payment providers across diverse regulatory environments." Source: cellpointdigital.com/articles/blog/latam-payment-trends-2024

5. Regional Fraud Exposure: Cybersource Global eCommerce Payments & Fraud Report estimates online fraud costs airlines 1.2% of annual revenue (over $10B industry-wide). LATAM's cross-border routes across high-fraud markets (Brazil ranks among the top globally) make it particularly exposed. Card testing is the #1 fraud threat in Latin America. Source: cybersource.com/content/dam/documents/campaign/fraud-report/global-fraud-report-2024.pdf

**Key meeting angles:**

1. **Airline-proven results** | Wingo Airlines achieved +14% authorization improvement with Yuno's Smart Routing. Viva Aerobus achieved 75% hard-decline recovery with NOVA AI. Both are Latin American airlines operating in similar markets to LATAM. This is not theoretical: these are proven airline results in LATAM's own region.

2. **Pix gap is the biggest revenue leak** | Brazil is LATAM Airlines' largest domestic market. Pix has 170M+ registered users and processes over $346B annually. Its absence from LATAM's checkout forces Brazilian travelers to use credit cards (under 35% penetration) or abandon. Yuno activates Pix through a single API alongside 1,000+ other methods.

3. **Checkout failure is a brand crisis** | 7+ years of documented payment failures on FlyerTalk and TripAdvisor. Travelers forced to third-party OTAs at higher prices, or phone bookings with $35 to $40 surcharges. Yuno's failover routing eliminates single-processor dependency, automatically cascading to a backup acquirer when the primary fails.

4. **$13B revenue, massive recovery opportunity** | At 15% to 25% regional decline rates, even a 3% improvement on LATAM's ticket volume represents hundreds of millions in recovered revenue. Smart Routing + NOVA AI + Failover together target the full decline funnel.

5. **Digital transformation leadership** | CIO Juliana Rios leads a cloud-first, AI-driven technology strategy (Google Cloud migration complete, GitLab for dev toolchain, 70/50/2 AI project). Payment orchestration fits naturally into this modernization agenda. Rios has 20+ years in finance/airline tech and previously led retail strategy at Banco Santander.

6. **Regional wallet activation** | Nequi (Colombia, 16M users), Yape (Peru, 15M users), OXXO (Mexico, 20M+ users), Mercado Pago (region-wide). LATAM's current checkout misses the dominant payment method in nearly every market it serves. One Yuno integration activates all of them simultaneously.

**Sources:**
- [LATAM Airlines Payment Methods Help Page](https://www.latamairlines.com/us/en/help-center/faq/purchases/asistance/available-payment-methods)
- [LATAM Wallet Digital Experience](https://www.latamairlines.com/us/en/experience/digital/latam-wallet)
- [LATAM Airlines FY2024 Results (Travel and Tour World)](https://www.travelandtourworld.com/news/article/latam-airlines-delivers-a-strong-2024-reporting-977-million-in-net-profit-transporting-a-record-82-million-passengers-increasing-revenue-to-13-03-billion-and-achieving-a-12-7-operating-margin-wi/)
- [LATAM Airlines Q3 2025 Earnings Release](https://s205.q4cdn.com/986550758/files/doc_financials/2025/q3/Earning-Release-Q325-ENG.pdf)
- [LATAM Airlines Executive Management](https://ir.latam.com/English/governance/executive-management/default.aspx)
- [Juliana Rios, CIO/CDO LATAM Airlines (LinkedIn)](https://cl.linkedin.com/in/juliana-rios-a22388)
- [FTE Airline Digital Transformation Power List Americas 2025](https://www.futuretravelexperience.com/2025/07/united-southwest-alaska-latam-delta-air-canada-more-among-fte-airline-digital-transformation-power-list-americas-2025/)
- [FlyerTalk: LATAM Payment Failures](https://www.flyertalk.com/forum/latam-latam-pass/2068363-no-credit-debit-cards-working-website.html)
- [FlyerTalk: LATAM Unjustified Charges](https://www.flyertalk.com/forum/latam-latam-pass/2185465-latam-airlines-unjustified-charges-denials.html)
- [TripAdvisor: LATAM Website Problems](https://www.tripadvisor.com/ShowTopic-g1-i10702-k9502817-o70-New_LATAM_ex_LAN_website_problems-Air_Travel.html)
- [Rapyd: Payment Decline Rates in LATAM](https://www.rapyd.net/blog/payment-processing-decline-rates-in-latam/)
- [Cybersource Global Fraud Report 2024](https://www.cybersource.com/content/dam/documents/campaign/fraud-report/global-fraud-report-2024.pdf)
- [CellPoint Digital: LATAM Payment Trends 2024](https://cellpointdigital.com/articles/blog/latam-payment-trends-2024)
- [PSE LATAM Airlines Payments Guide](https://taxreceipts.icnareliefcanada.ca/pro-voice/pse-latam-airlines-your-guide-to-payments-in-english-1764811222)
- [LATAM Airlines Logo (Seeklogo)](https://seeklogo.com/vector-logo/287010/latam-airlines)
