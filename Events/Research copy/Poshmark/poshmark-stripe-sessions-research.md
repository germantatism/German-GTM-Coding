# POSHMARK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Poshmark
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/50/Poshmark_logo.svg
Nombre merchant: Poshmark

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Failed Global Expansion
Tittle_Pain Point_2: Multi PSP, No Orchestrator
Tittle_Pain Point_3: Seller Payout Friction
Tittle_Pain Point_4: Naver Asia Gap
Tittle_Pain Point_5: Auth Declines at Scale

Desc_Pain Point_1: Poshmark shut down UK, Australia, and India in October 2023 after failing to localize. Now US and Canada only. Each market required separate payment integrations with no unified orchestration layer to scale efficiently.
Desc_Pain Point_2: Poshmark integrates PayPal, Venmo, Affirm, Apple Pay, Google Pay plus cards through multiple processors. Hyperwallet handles payouts. No central orchestration layer routes transactions or manages PSP performance.
Desc_Pain Point_3: Sellers report funds sent to closed accounts, bank verification failures, and 2 to 3 day direct deposit delays. Poshmark uses Hyperwallet for PayPal/Venmo payouts but lacks instant settlement for all sellers.
Desc_Pain Point_4: Naver acquired Poshmark for $1.2B to build global re commerce. Naver dominates Korea and Japan but Poshmark has zero payment infrastructure in Asia. KakaoPay, Naver Pay, Line Pay, PayPay are all missing.
Desc_Pain Point_5: 80M+ registered users, 1.3 star Trustpilot rating. BBB and PissedConsumer report card declines, checkout errors, and denied refunds. No smart routing means every failed transaction stays failed.

SLIDE 1: PSP TOPOLOGY

PSP_1: PayPal/Braintree
PSP_2: Affirm
PSP_3: Hyperwallet
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: KakaoPay (S. Korea)
Local_M_2: Naver Pay (S. Korea)
Local_M_3: Toss (S. Korea)
Local_M_4: PayPay (Japan)
Local_M_5: Line Pay (Japan)
Local_M_6: Konbini (Japan)
Local_M_7: Interac (Canada)
Local_M_8: UPI (India, future)
Local_M_9: iDEAL (Europe, future)
Local_M_10: Pix (LATAM, future)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Across PSPs
Tittle_Yuno_Cap2: Asia Market Activation
Tittle_Yuno_Cap3: Unified Payout Orchestration
Tittle_Yuno_Cap4: Failover + NOVA Recovery

Desc_Yuno_Cap1: Route every Poshmark transaction across PayPal, Affirm, and card processors based on BIN, issuer, and real time PSP performance. No more single path failures. McDonald's achieved +4.7% approval across 18 markets with Yuno Smart Routing.
Desc_Yuno_Cap2: Activate KakaoPay, Naver Pay, Toss, PayPay, Line Pay, and Konbini for Naver's Asia expansion via one API. 1,000+ payment methods, 68+ countries direct. InDrive scaled 10 markets in under 8 months with 90% approval rates through Yuno.
Desc_Yuno_Cap3: One orchestration layer unifying buyer payments and seller payouts across PayPal, Venmo, Hyperwallet, and direct deposit. Single dashboard for reconciliation. Rappi (20+ PSPs) cut analyst time by 80% and implementation time to zero with Yuno.
Desc_Yuno_Cap4: Automatic cascade across PSPs recovers up to 50% of failed transactions. NOVA AI agents recover remaining failures via email/WhatsApp with up to 75% recovery. For 80M+ users, this means millions in recovered GMV per quarter.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Poshmark at a glance:**
- HQ: Redwood City, CA | Parent: Naver Corporation (South Korea) | CEO: Namsun Kim (effective October 2025)
- Acquired by Naver in January 2023 for $1.2B
- Annual sales: ~$1.9B GMV in 2025, with estimated $300M+ commission revenue
- 80M+ registered users
- Currently operates in US and Canada only (closed UK, Australia, India in October 2023)
- Naver is South Korea's largest internet company (search, commerce, AI, fintech)
- CTO: Gautam Golwala (co founder). VP Engineering: Chetan Pungaliya.
- Global resale market: $119B in 2022, projected $219B by 2026
- Business model: 20% commission on sales under $15, otherwise $2.95 flat fee; buyers pay no fees

**Key leadership (payments relevant):**
- Namsun Kim, CEO (October 2025): former Naver President of Investments. Focused on global expansion.
- Gautam Golwala, CTO and co founder: leads technology since 2011
- Chetan Pungaliya, VP of Engineering
- No dedicated VP/Head of Payments identified

**Confirmed PSPs and payment infrastructure:**
- PayPal/Braintree: PayPal and Venmo accepted as buyer payment methods. Confirmed in official support and X/Twitter.
- Affirm: BNPL partner since 2022. Monthly payments or 4 interest free payments on items $50+.
- Hyperwallet (PayPal): processes seller payouts via Instant Transfer, PayPal, and Venmo redemption.
- Apple Pay and Google Pay: confirmed as buyer payment methods.
- Credit/debit cards: Visa, Mastercard, Amex, Discover confirmed.
- Seller payouts: direct deposit (2 to 3 business days), check by mail, balance spending, Venmo, PayPal.
- No payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment methods by market:**

US: Credit/debit cards, Apple Pay, Google Pay, PayPal, PayPal Pay Later, Venmo, Affirm, Poshmark Gift Cards

Canada: Credit/debit cards, Apple Pay, Google Pay (PayPal/Venmo/Affirm availability not confirmed for CA)

**Missing local APMs (blind spots for Naver expansion):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | KakaoPay | South Korea | 37M+ users. Dominant mobile payment. Essential for Naver's home market commerce. |
| 2 | Naver Pay | South Korea | Naver's own payment system with 30M+ users. Parent company's fintech product. |
| 3 | Toss | South Korea | 22M+ users. Leading Korean fintech super app. |
| 4 | PayPay | Japan | 60M+ users. Dominant QR code payment in Japan. Naver has major Japan presence via LINE. |
| 5 | Line Pay | Japan | 40M+ users. Part of Naver's LINE ecosystem. Natural integration for Poshmark. |
| 6 | Konbini | Japan | Convenience store payments. Critical for cash preferring Japanese consumers. |
| 7 | Interac | Canada | National debit network used by most Canadian bank account holders. Not confirmed on Poshmark CA. |
| 8 | UPI | India (future) | 10B+ monthly transactions. Non negotiable for any India re entry. |
| 9 | iDEAL | Europe (future) | 50%+ of Dutch online transactions. Critical for European expansion. |
| 10 | Pix | LATAM (future) | 70%+ of Brazilian digital payments. Largest LATAM market for re commerce. |

**Payment complaints and issues:**
- Trustpilot: 1.3 stars from 2,800+ reviews
- PissedConsumer: 9,400+ reviews, majority negative
- BBB: complaints about denied refunds, checkout errors, billing disputes
- Seller payouts: funds sent to closed accounts, bank verification failures
- Card declines at checkout with no retry or alternative routing
- Refund processing takes up to 1 full billing cycle

**Key strategic developments (2025 to 2026):**
1. CEO transition (October 2025): Namsun Kim (Naver investments chief) becomes CEO. Signals stronger Naver integration and global expansion push.
2. Market consolidation (October 2023): closed UK, Australia, India. Refocused on US and Canada core markets.
3. Naver synergy: leveraging Naver's technology in AI, search, and commerce. Social shopping and livestream commerce features.
4. Re commerce growth: global market projected $219B by 2026. Poshmark positioned as leading social marketplace.
5. Naver Pay and LINE Pay ecosystem: parent company operates major fintech platforms across Korea and Japan.

**Yuno case references for the meeting:**

INDRIVE: Mobility marketplace scaled 10 LATAM markets in under 8 months. 90% approval rate. 4.5%+ recovery. Similar multi market expansion challenge to Poshmark's Naver ambitions.

MCDONALD'S: +4.7% approval across 18 markets with Yuno Smart Routing. Shows multi market routing impact at scale.

RAPPI: 20+ payment providers orchestrated via Yuno. Zero implementation time for new providers. 80% analyst reduction. Relevant to Poshmark's multi PSP reconciliation needs.

WINGO: 14% approval rate increase, 10+ countries. Demonstrates rapid multi country activation.

**Key meeting angles:**

1. **Naver expansion demands payment orchestration**: Naver acquired Poshmark for $1.2B to go global. But Poshmark failed in UK/Australia/India partly due to localization. Yuno activates 1,000+ payment methods across 68+ countries via one API, making re expansion possible without building per market integrations.

2. **Korea and Japan are the obvious next markets**: Naver dominates both. KakaoPay, Naver Pay, Toss, PayPay, Line Pay, Konbini are all missing from Poshmark. Yuno enables all of them through a single integration.

3. **Multiple PSPs with no orchestrator**: PayPal, Affirm, Hyperwallet, Apple Pay, Google Pay all operating independently. No smart routing, no failover, no unified dashboard. Yuno provides the orchestration layer.

4. **Seller payout issues erode marketplace trust**: Funds to closed accounts, verification failures, 2 to 3 day delays. Yuno's unified payout orchestration provides single dashboard reconciliation across all payout methods.

5. **1.3 star Trustpilot rating signals payment UX problems**: Card declines, checkout errors, and refund denials dominate complaints. Smart routing and failover directly reduce these issues.

6. **InDrive parallel**: InDrive (marketplace, multi country) achieved 90% approval scaling 10 markets in 8 months with Yuno. Poshmark needs the same playbook for Naver's Asia expansion.

**Sources:**
- [Poshmark Support: Payment Methods](https://support.poshmark.com/s/article/284791087?language=en_US)
- [Poshmark Support: How to Get Paid](https://poshmark.com/posh_guide/how_to_get_paid)
- [Poshmark Support: Venmo Payment Method](https://support.poshmark.com/s/article/venmo-payment-method?language=en_US)
- [Poshmark Support: Redeem Earnings via Venmo and PayPal](https://support.poshmark.com/s/article/redeem-earnings-via-Venmo-and-PayPal?language=en_US)
- [Poshmark Support X/Twitter: Payment Methods](https://x.com/PoshmarkSupport/status/1851671854181945376)
- [Poshmark Getting Paid Guide (PoshPowerSeller)](https://poshpowerseller.com/poshmark-getting-paid-direct-deposit-and-checks)
- [Poshmark Seller Payment Guide (Closo)](https://closo.co/blogs/community/how-does-poshmark-pay-sellers-complete-guide-2025)
- [Affirm and Poshmark Partnership (Affirm IR)](https://investors.affirm.com/news-releases/news-release-details/affirm-and-poshmark-expand-partnership)
- [Naver Acquires Poshmark (PR Newswire)](https://www.prnewswire.com/news-releases/naver-completes-acquisition-of-poshmark-301714299.html)
- [Naver Poshmark $1.2B (TechCrunch)](https://techcrunch.com/2022/10/03/naver-agrees-to-acquire-fashion-marketplace-poshmark-for-1-2b/)
- [Poshmark CEO Transition (PR Newswire)](https://www.prnewswire.com/news-releases/poshmark-inc-announces-chief-executive-officer-transition-302525526.html)
- [Poshmark Global Expansion (Yahoo Finance)](https://finance.yahoo.com/news/poshmark-ceo-naver-acquisition-212136138.html)
- [Poshmark Closes UK/Australia/India (ValueAddedResource)](https://www.valueaddedresource.net/poshmark-closes-uk-australia-india-marketplaces/)
- [Poshmark Revenue (ecdb)](https://ecdb.com/resources/sample-data/retailer/poshmark)
- [Poshmark Business Model (SimiCart)](https://simicart.com/blog/poshmark-business-model/)
- [Poshmark Engineering](https://poshmark.com/engineering)
- [Poshmark Leadership (Comparably)](https://www.comparably.com/companies/poshmark/executive-team)
- [Poshmark Trustpilot Reviews](https://www.trustpilot.com/review/poshmark.com)
- [Poshmark PissedConsumer](https://poshmark.pissedconsumer.com/review.html)
- [Poshmark BBB Complaints](https://www.bbb.org/us/ca/redwood-city/profile/consignment-clothes/poshmarkcom-1116-442251/complaints)
- [Poshmark Wikipedia](https://en.wikipedia.org/wiki/Poshmark)
- [Naver Poshmark Acquisition (PYMNTS)](https://www.pymnts.com/acquisitions/2023/naver-completes-acquisition-poshmark-aims-grow-globally/)
- [Naver Poshmark (Modern Retail)](https://www.modernretail.co/technology/unpacked-what-to-know-about-poshmarks-new-owner-south-korean-search-giant-naver/)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Wingo Case Study](https://y.uno/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner)
- [Yuno Platform Overview](https://y.uno/)
