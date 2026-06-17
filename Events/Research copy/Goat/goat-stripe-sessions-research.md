# GOAT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: GOAT
═══════════════════════════════════════

Logo: https://logos-world.net/wp-content/uploads/2022/04/GOAT-Logo.png
Nombre merchant: GOAT

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 170 Countries, No Routing
Tittle_Pain Point_2: FTC Fined $2M for Refunds
Tittle_Pain Point_3: 7+ Payment Partners Siloed
Tittle_Pain Point_4: Seller Payout Bottleneck
Tittle_Pain Point_5: APAC Localization Gaps

Desc_Pain Point_1: GOAT ships to 170 countries and 50M+ members but has no smart routing layer. Each transaction follows a single path through one processor. Failed payments in cross border markets stay failed with no cascade or retry logic.
Desc_Pain Point_2: FTC ordered GOAT to pay $2M+ in December 2024 for shipping violations and deceptive refund practices. Refund requests were rejected or only partially honored. Payment trust is damaged across the platform.
Desc_Pain Point_3: GOAT integrates PayPal, Affirm, Afterpay, Klarna, Alipay, Zip, giropay, Apple Pay, and Google Pay. Dwolla handles ACH payouts. Each operates independently with no unified orchestration or performance monitoring.
Desc_Pain Point_4: Before Dwolla, seller payouts took up to 7 days. Now averaging 2 days via ACH. But 1M+ sellers across 170 countries still lack instant settlement and local payout rails beyond US bank transfers.
Desc_Pain Point_5: GOAT has a Hong Kong hub for APAC but only Alipay covers China. Japan (PayPay, Konbini), Korea (KakaoPay), Southeast Asia (GrabPay, GCash, DANA) have no local payment methods confirmed.

SLIDE 1: PSP TOPOLOGY

PSP_1: PayPal
PSP_2: Affirm
PSP_3: Dwolla (ACH payouts)
PSP_4: Klarna

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: KakaoPay (S. Korea)
Local_M_2: PayPay (Japan)
Local_M_3: Konbini (Japan)
Local_M_4: GrabPay (SEA)
Local_M_5: GCash (Philippines)
Local_M_6: DANA (Indonesia)
Local_M_7: PromptPay (Thailand)
Local_M_8: Pix (Brazil)
Local_M_9: iDEAL (Netherlands)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Across 7+ PSPs
Tittle_Yuno_Cap2: APAC + LATAM APM Activation
Tittle_Yuno_Cap3: Unified Payout Orchestration
Tittle_Yuno_Cap4: Real Time Anomaly Monitors

Desc_Yuno_Cap1: Route each GOAT transaction across PayPal, Affirm, Klarna, Afterpay, and card processors by BIN, issuer, currency, and real time PSP performance. McDonald's achieved +4.7% approval across 18 markets with Yuno. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap2: Activate KakaoPay, PayPay, Konbini, GrabPay, GCash, DANA, PromptPay, Pix, and iDEAL via one API. 1,000+ payment methods, 68+ countries direct. InDrive scaled 10 markets in under 8 months with 90% approval through Yuno.
Desc_Yuno_Cap3: One orchestration layer unifying buyer payments (7+ PSPs) and seller payouts (Dwolla ACH + future local rails) across 170 countries. Single reconciliation dashboard. Rappi (20+ PSPs) cut analyst time by 80% with Yuno.
Desc_Yuno_Cap4: Rappi used Yuno Monitors to cut anomaly response from 10 minutes to milliseconds. For GOAT processing millions of high value sneaker transactions, real time detection prevents checkout errors and fraud before they trigger FTC complaints.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GOAT at a glance:**
- HQ: Los Angeles, CA | CEO: Eddy Lu (co founder) | CTO: Chris To (since March 2024)
- Valuation: $3.7B (Series F, $195M raised, $487M total funding)
- Revenue: ~$248M in 2024
- 50M+ members across 170 countries, 1M+ sellers
- Founded 2015. Merged with Flight Club in 2018.
- Categories: sneakers, apparel, accessories from emerging, contemporary, and iconic brands
- Authentication centers: US (multiple), Hong Kong (APAC hub)
- Business model: buyer pays retail + shipping + authentication fee; seller pays commission
- Investors: Y Combinator, First Round Capital, Andreessen Horowitz

**Key leadership (payments relevant):**
- Eddy Lu, CEO and co founder
- Chris To, CTO (since March 2024): oversees technology strategy, product development, engineering expansion, mobile optimization
- Matt Cohen, Chief Revenue Officer
- Sen Sugano, brand strategy and global marketing
- No dedicated VP/Head of Payments identified

**Confirmed PSPs and payment infrastructure:**
- PayPal: confirmed as buyer payment method across markets
- Affirm: BNPL partner. 30% increase in average order values since integration. Monthly payments or 4 interest free payments.
- Afterpay: BNPL. Pay in 4 installments.
- Klarna: BNPL option. Region dependent availability.
- Alipay: confirmed for China/Chinese consumer transactions
- Zip: BNPL. Pay in 4 installments.
- giropay: confirmed for German market
- Apple Pay, Google Pay: digital wallets confirmed
- Dwolla: ACH API for US seller payouts. Integrated in 10 days. Reduced payout time from 7 days to 2 days. 50% increase in bank transfer payouts. 80% reduction in cashout support tickets.
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment methods by context:**

General: Credit/debit cards, PayPal, Affirm, Afterpay, Alipay, Apple Pay, giropay, Google Pay, Klarna, Zip

Auctions: Cards, Apple Pay, Google Pay only (no Affirm, Afterpay, Alipay, Zip)

Drops: Cards, Apple Pay, Google Pay, PayPal only (no BNPL, no Alipay)

Guest Checkout: Cards, Apple Pay, PayPal, Affirm, Afterpay, Alipay, Klarna

**Missing local APMs (blind spots across 170 countries):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | KakaoPay | South Korea | 37M+ users. Sneaker culture is massive in Korea. GOAT ships there but no local payment. |
| 2 | PayPay | Japan | 60M+ users. Dominant QR payment. Japan is a top sneaker market globally. |
| 3 | Konbini | Japan | Convenience store payments. Critical for cash preferring Japanese sneakerheads. |
| 4 | GrabPay | Southeast Asia | Leading super app wallet across SEA markets. GOAT has APAC hub in HK. |
| 5 | GCash | Philippines | 80M+ users. Dominant mobile wallet in Philippines. |
| 6 | DANA | Indonesia | 150M+ users. Leading Indonesian digital wallet. |
| 7 | PromptPay | Thailand | National payment system. Critical for Thai market. |
| 8 | Pix | Brazil | 70%+ of Brazilian digital payments. LATAM sneaker market is growing fast. |
| 9 | iDEAL | Netherlands | 50%+ of Dutch online transactions. Key European sneaker market. |
| 10 | Bancontact | Belgium | 17M+ cards. Important Benelux market. |

**Payment complaints and regulatory issues:**
- FTC settlement (December 2024): $2M+ fine for shipping violations and deceptive refund practices
- FTC findings: 37% of "Instant" orders shipped late, 16% of "Next Day" orders late. Refund requests rejected or only partially honored.
- BBB complaints: undelivered orders, denied refunds, partial credits instead of full refunds
- Trustpilot: mixed reviews with payment and refund complaints recurring
- Pre Dwolla: seller payouts took up to 7 days. Sacrificing 2 to 3% margins on third party payment flows.

**Key strategic developments (2025 to 2026):**
1. CTO Chris To (March 2024): scaling engineering, mobile optimization, automating operations for international growth
2. APAC expansion: Hong Kong authentication hub serving Asia Pacific markets
3. Beyond sneakers: expanding into apparel, accessories, and lifestyle categories
4. High value authentication marketplace: average order values boosted 30% with Affirm integration
5. FTC compliance overhaul: required to honor buyer protection policies going forward

**Yuno case references for the meeting:**

INDRIVE: Marketplace scaled 10 LATAM markets in under 8 months. 90% approval rate. 4.5%+ recovery. Similar multi country expansion challenge to GOAT's 170 country footprint.

MCDONALD'S: +4.7% approval across 18 markets with Smart Routing. Shows routing impact at scale across diverse geographies.

RAPPI: 20+ PSPs orchestrated via Yuno. Zero implementation time for new providers. 80% analyst reduction. Directly relevant to GOAT's 7+ PSP orchestration needs.

WINGO: 14% approval rate increase across 10+ countries. Demonstrates rapid multi country activation.

**Key meeting angles:**

1. **170 countries, 7+ PSPs, zero orchestration**: GOAT has PayPal, Affirm, Afterpay, Klarna, Alipay, Zip, giropay, Apple Pay, Google Pay, and Dwolla all operating independently. No smart routing, no failover, no unified dashboard. Yuno provides the orchestration layer to route each transaction through the best performing path.

2. **FTC fine makes payment reliability urgent**: $2M+ for shipping/refund violations. Any further payment errors increase regulatory scrutiny. Yuno's real time monitors detect anomalies in milliseconds before they become customer complaints or FTC issues.

3. **APAC is the growth frontier but payment localization is missing**: GOAT has a Hong Kong hub but only Alipay covers China. Japan, Korea, and Southeast Asia need KakaoPay, PayPay, Konbini, GrabPay, GCash, DANA. Yuno activates all via one API.

4. **High AOV marketplace means high stakes per failed transaction**: Sneakers sell for $200 to $2,000+. Every failed payment is significant revenue lost. Smart routing + failover recovers up to 50% of failures. NOVA AI recovers up to 75%.

5. **Seller payout orchestration**: 1M+ sellers across 170 countries. Dwolla handles US ACH but international seller payouts need local rails. Yuno provides unified payout orchestration.

6. **InDrive parallel**: marketplace, multi country, high volume. InDrive achieved 90% approval scaling 10 markets in 8 months with Yuno.

**Sources:**
- [GOAT Support: Payment Methods](https://support.goat.com/hc/en-us/articles/115004610327-What-payment-options-do-you-accept)
- [GOAT Support: Auction Payment Methods](https://support.goat.com/hc/en-us/articles/16596121279757-Are-all-payment-methods-accepted-during-an-Auction)
- [GOAT Support: Drop Payment Methods](https://support.goat.com/hc/en-us/articles/25250528295309-Are-all-payment-methods-accepted-during-a-Drop)
- [GOAT Support: Guest Checkout Payment](https://support.goat.com/hc/en-us/articles/10340211575181-What-Payment-methods-are-available-for-Guest-Checkout)
- [GOAT Affirm Testimonial](https://www.affirm.com/business/blog/goat-testimonial)
- [GOAT + Affirm: 30% AOV Boost (Retail TouchPoints)](https://www.retailtouchpoints.com/features/retail-success-stories/goat-boosts-average-order-values-30-with-affirm-payments)
- [GOAT Dwolla ACH Payouts Case Study](https://www.dwolla.com/case-studies/goat-ach-payouts/)
- [GOAT Dwolla Automation](https://www.dwolla.com/updates/goat-saved-by-automating-funds-flow/)
- [GOAT Group Valuation $3.7B (PR)](https://www.goatgroup.com/news/goat-group-valuation-more-than-doubles-to-3-7-billion-after-closing-series-f-funding-round-of-195-million)
- [GOAT Group Revenue (Latka)](https://getlatka.com/companies/goatgroup.com)
- [GOAT Group Profile (Tracxn)](https://tracxn.com/d/companies/goat-group/__H8BlxgLbU_-e-rrAVi0RGn8xQGzvXOq27PUXdW8XpLI)
- [GOAT Group Business Breakdown (Contrary Research)](https://research.contrary.com/company/goat)
- [GOAT Group Leadership (Comparably)](https://www.comparably.com/companies/goat-group-28154/executive-team)
- [GOAT Group Leadership (The Org)](https://theorg.com/org/goat-group/teams/leadership-team-1)
- [FTC GOAT Settlement Dec 2024](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-order-requires-online-retailer-goat-pay-more-2-million-consumers-mail-order-rule-violations)
- [FTC GOAT Penalty (Hunton)](https://www.hunton.com/hunton-retail-law-resource/ftc-penalizes-goat-2-million-for-shipping-and-return-violations)
- [FTC GOAT (PYMNTS)](https://www.pymnts.com/news/regulation/2024/ftc-orders-goat-to-pay-2-million-alleging-shipping-violations/)
- [GOAT BBB Complaints](https://www.bbb.org/us/ca/los-angeles/profile/online-retailer/goat-1216-704262/complaints)
- [GOAT Shipping International](https://support.goat.com/hc/en-us/articles/360056429792-What-international-shipping-models-does-GOAT-use-)
- [GOAT Shipping Costs](https://support.goat.com/hc/en-us/articles/115004770608-How-much-does-shipping-cost)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Wingo Case Study](https://y.uno/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner)
- [Yuno Platform Overview](https://y.uno/)
