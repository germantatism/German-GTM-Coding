# SEPHORA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Sephora
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/2/29/Sephora_logo.svg
Nombre merchant: Sephora

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Stack
Tittle_Pain Point_2: Checkout Decline Spiral
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: BNPL Provider Sprawl
Tittle_Pain Point_5: Platform Migration Risk

Desc_Pain Point_1: JPMorgan acquires in store across US and Canada, Adyen processes SEA and APAC online, and each regional site runs its own payment stack. No unified view across 35 markets or 3,400 stores. Reconciliation is manual and market by market.
Desc_Pain Point_2: Sephora community forums are flooded with "payment could not be processed" errors. Multiple pending authorizations appear on cards with no order confirmation. Aggressive fraud filters block loyal Beauty Insiders mid checkout.
Desc_Pain Point_3: Sephora Thailand offers only Visa/MC and PromptPay. Malaysia lacks GrabPay, Touch 'n Go, and FPX. Singapore has no PayNow. The Middle East is missing Tamara and Tabby in most markets. Local wallets are absent where they dominate.
Desc_Pain Point_4: Afterpay in the US, Klarna in the US and UK, Oney 4x in France, Tabby in UAE, Atome in Singapore, each with a separate integration. Every new BNPL partner requires engineering work, a separate contract, and isolated reconciliation.
Desc_Pain Point_5: Sephora is migrating from legacy SAP Commerce to commercetools MACH architecture across all markets. This multi year replatforming means payment integrations must be rebuilt. Any PSP tied to the old stack risks disconnection during transition.

SLIDE 1: PSP TOPOLOGY

PSP_1: JPMorgan Payments
PSP_2: Adyen
PSP_3: Afterpay (Block)
PSP_4: Klarna

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: GrabPay
Local_M_2: Touch 'n Go
Local_M_3: FPX
Local_M_4: PayNow
Local_M_5: DANA
Local_M_6: Tamara
Local_M_7: Tabby
Local_M_8: Mada (online)
Local_M_9: SPEI
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route each transaction to the best performing acquirer by market, card BIN, and issuer in real time. With 250,000+ daily in store transactions through JPMorgan alone, plus Adyen processing across APAC, even a 2% authorization uplift on Sephora's estimated $3.6B e-commerce volume means $72M+ in recovered annual revenue. Smart Routing eliminates the guesswork of static PSP assignments.
Desc_Yuno_Cap2: When JPMorgan declines a US card or Adyen rejects a SEA transaction, Yuno automatically cascades to the next best processor in milliseconds. No customer ever sees a "payment could not be processed" error while a viable route exists. Sephora's community forums are proof that false declines cost loyal Beauty Insiders and revenue alike.
Desc_Yuno_Cap3: One API integration activates GrabPay and Touch 'n Go in Malaysia, DANA in Indonesia, PayNow in Singapore, Tamara and Tabby across the GCC, Konbini in Japan, and SPEI in Mexico. Yuno connects 300+ payment methods across 40+ countries. No per market engineering sprints, no separate contracts, instant geo routing from day one.
Desc_Yuno_Cap4: Replace Sephora's fragmented reconciliation across JPMorgan, Adyen, Afterpay, Klarna, Oney, Tabby, and Atome with a single dashboard. Real time approval rate monitoring, centralized settlement across all 35 markets, and millisecond anomaly detection via Monitors. Perfectly timed for the commercetools migration: one Yuno API replaces dozens of legacy PSP integrations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Sephora at a glance:**
- Founded 1969 in Limoges, France. Owned by LVMH since 1997
- Global CEO: Guillaume Motte. North America CEO: Artemis Patrick (first woman, appointed April 2024)
- 3,400+ stores across 35 markets. ~2,700 freestanding stores, plus Kohl's shop in shops (US)
- Revenue: ~$16B+ global retail sales (2024 est.). E-commerce net sales: ~$3.6B (2025 forecast via sephora.com alone)
- LVMH Selective Retailing division: Sephora delivered double digit growth in revenue and profit in 2024
- US accounts for ~55% of revenues, with 74M+ Beauty Insider loyalty members globally
- Opening ~200 new locations per year. 5 UK stores opened in 2024, targeting 20 by 2027
- Migrating e-commerce platform from SAP Commerce to commercetools (MACH architecture, announced July 2022, multi year rollout)
- Recently adopted SAP S/4 HANA (2024) and Salesforce Commerce Cloud (Europe)
- No dedicated VP/Head of Payments identified publicly. Payments likely falls under CFO Delphine Herve (SVP/CFO, NA) or SVP/GM Ecommerce Nadine Graham

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| JPMorgan Payments | Primary acquirer, in store POS, Tap to Pay on iPhone | US, Canada |
| Adyen | Online acquiring, mPOS, UnionPay SecurePlus | SEA (HK, SG, MY, TH, PH, ID, AU, NZ) |
| Afterpay (Block/Square) | BNPL (4 installments) | US (online, in store, app) |
| Klarna | BNPL (4 installments) | US, UK (online, in store, app) |
| Oney Bank | BNPL (4x installments, EUR 100 to 2,000) | France |
| Tabby | BNPL | UAE, Saudi Arabia |
| Atome | BNPL | Singapore |
| PayPal | Digital wallet + Pay Later | US, select markets |
| Apple Pay | Mobile wallet | US, Canada (Tap to Pay) |
| Google Pay | Mobile wallet | US, Thailand |
| Paze | Card network wallet (Visa/MC/Amex issuer backed) | US |
| Comenity Capital Bank | Sephora branded credit card issuer | US |

**No payment orchestrator detected.** Each market runs its own PSP integration.

**Top Markets Gap Analysis:**

MARKET 1: United States (~55% of revenue, 430+ stores)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Paze, Afterpay, Klarna, Sephora Visa Card
  Missing: ACH, Venmo (standalone), Cash App Pay
  Insight: 250,000+ daily transactions processed via JPMorgan. 7% basket size increase from Tap to Pay. 25% of in store transactions now mobile.

MARKET 2: France (EUR 1.66B revenue, home market)
  Accepted: Visa/MC, Oney 4x, Carte Bancaire (via Visa/MC cobadge)
  Missing: Bancontact (Belgium cross border), iDEAL (Netherlands cross border), PayPal (not confirmed)
  Insight: Oney limited to EUR 100 to 2,000 and not available on mobile app or Click & Collect. Payment friction on lower basket sizes.

MARKET 3: Southeast Asia (7 markets, 200+ stores, Adyen processed)
  Thailand: Visa/MC, PromptPay, Google Pay, COD
  Singapore: Visa/MC, Amex, PayPal, Atome
  Malaysia: Visa/MC, PayPal only
  Philippines: Visa/MC, Amex, GCash, Online Banking
  Missing: GrabPay (MY, TH, PH), Touch 'n Go (MY), FPX (MY), DANA (ID), ShopeePay, PayNow (SG), LINE Pay (TH)
  Insight: Credit card penetration under 10% in PH, ID, TH. Without wallets, vast majority of consumers cannot pay online.

MARKET 4: Middle East (UAE, Saudi Arabia, strong market share)
  Accepted: Visa/MC, Mada (SA), COD, Tabby (UAE)
  Missing: Tamara (SA BNPL), Apple Pay (checkout), STC Pay (SA), Benefit Pay (Bahrain)
  Insight: Mada has 93% card market share in Saudi Arabia. BNPL adoption growing fast with Tabby and Tamara at ~10M users each across GCC.

MARKET 5: Brazil (sephora.com.br)
  Accepted: Visa/MC, Pix, local installment cards
  Missing: Boleto (unconfirmed), PIX QR deeplink, PicPay, Mercado Pago
  Insight: Pix handles 70%+ of Brazilian digital payments. Sephora Brazil does offer Pix, but broader local wallet coverage is thin.

MARKET 6: Mexico (sephora.com.mx)
  Accepted: Visa/MC, Amex, PayPal, OXXO
  Missing: SPEI, Mercado Pago, CoDi
  Insight: OXXO is offered for cash payments. SPEI (instant bank transfer) not available despite being Mexico's fastest growing payment rail.

MARKET 7: India (sephora.in)
  Accepted: Visa/MC, UPI, PhonePe, Amazon Pay, Ola Money, Airtel Money, Net Banking, ICICI PayLater, HDFC FlexiPay, COD
  Insight: India is the most locally adapted Sephora market for payments. Strong UPI and wallet coverage.

MARKET 8: South Korea (sephora.kr, re-entered via partnership)
  Accepted: Visa/MC, Naver Pay, Kakao Pay, Payco, bank transfer, mobile pay
  Insight: Korea is also well localized. 93.6% cashless economy.

**Payment outage and checkout error history:**
- "Payment could not be processed" is the most common support thread topic in the Beauty Insider Community
- Customers report multiple pending authorizations (up to 9 holds) with no order completion
- PayPal login loops and "almost done" screen freezes documented in Aug 2024
- Address validation rejections blocking repeat customers with verified addresses (2024, continuing into 2025)
- Gift card authentication failures rising in 2025 due to aggressive anti fraud filters
- App checkout errors preventing PayPal use entirely (Aug 2024, lasted over a week)

**Key meeting angles:**
1. **commercetools migration = payment reset** | Sephora is rebuilding its entire commerce stack on MACH. A payment orchestrator is the natural complement: one API instead of rebuilding each PSP integration per market
2. **35 markets, zero orchestration** | JPMorgan in NA, Adyen in SEA, plus 6+ BNPL partners. No unified routing, no failover, no cross provider analytics
3. **SEA wallet desert** | Malaysia accepts only Visa/MC and PayPal online. GrabPay, Touch 'n Go, FPX are all missing. Under 10% card penetration means Sephora is invisible to most online shoppers
4. **False decline epidemic** | Community forums document years of authorization failures. Smart routing and cascade retries directly solve this
5. **BNPL consolidation** | 6 different BNPL integrations across markets. Yuno's single API approach replaces fragmented contracts with unified access
6. **250K daily transactions** | JPMorgan processes a quarter million transactions daily for Sephora. Even small auth rate improvements at this scale translate to tens of millions in revenue
7. **Competitor precedent** | Ulta Beauty, L'Oreal e-commerce, and other LVMH brands (Le Bon Marche, DFS) face the same multi market payment fragmentation

**Sources:**
- [Sephora Payment Methods (US)](https://www.sephora.com/beauty/payment-methods)
- [Sephora BNPL FAQ](https://www.sephora.com/beauty/shop-now-pay-later-faq)
- [Sephora Billing & Payment Options](https://www.sephora.com/beauty/billing-payment-options)
- [Sephora Thailand Payment Methods](https://sephorath.zendesk.com/hc/en-us/articles/360020256672)
- [Sephora Singapore Payment Methods](https://sephorasg.zendesk.com/hc/en-us/articles/360029890651)
- [Sephora Philippines Payment Methods](https://sephoraph.zendesk.com/hc/en-us/articles/360029601992)
- [Sephora Malaysia Payment Methods](https://sephoramy.zendesk.com/hc/en-us/articles/360029891851)
- [Sephora Korea Payment Methods](https://sephorakr.zendesk.com/hc/en-us/articles/360035281531)
- [Sephora India Payment FAQ](https://sephora.in/page/faqs-payment)
- [Sephora Mexico Payment Methods](https://www.sephora.com.mx/pages/faq-payment.html)
- [Sephora Brazil Payment Methods](https://www.sephora.com.br/formas-de-pagamento.html)
- [Sephora France CGV (Oney 4x)](https://www.sephora.fr/cgv.html)
- [Sephora UK Payment Methods](https://www.sephora.co.uk/help-centre/Payment/payment%20methods)
- [Adyen: Sephora SEA UnionPay SecurePlus](https://www.adyen.com/press-and-media/sephora-sea-digital-partners-with-adyen-to-offer-unionpay-secureplus-to-customers)
- [Adyen: Sephora Malaysia mPOS](https://www.adyen.com/press-and-media/sephora-malaysia-unveils-best-in-class-customer-experience-with-adyens-in-person-payments-solution)
- [JPMorgan: Sephora Tap to Pay on iPhone](https://www.jpmorgan.com/about-us/corporate-news/2023/jpm-payments-enables-tap-to-pay-on-iphone-for-us-merchants-starting-with-sephora)
- [JPMorgan: Sephora Omnichannel Experience](https://www.jpmorgan.com/insights/payments/acquiring-and-e-commerce/sephora-omnichannel-experience)
- [JPMorgan: Sephora Canada Tap to Pay](https://www.jpmorgan.com/about-us/corporate-news/2024/tap-to-pay-on-iphone-canada-expansion)
- [Afterpay x Sephora Partnership (July 2022)](https://www.businesswire.com/news/home/20220713005007/en/Afterpay-and-Sephora-Partner)
- [Sephora + commercetools Partnership](https://newsroom.sephora.com/sephora-elevates-the-future-of-commerce-partners-with-commercetools-as-next-generation-commerce-solution/)
- [Sephora MACH Architecture (Retail TouchPoints)](https://www.retailtouchpoints.com/topics/digital-commerce/e-commerce-experience/sephora-commercetools-ecommerce-mach-headless)
- [Salesforce: Sephora Europe](https://investor.salesforce.com/press-releases/press-release-details/2018/Sephora-Selects-Salesforce-to-Power-Digital-Shopping-Experiences-in-Europe/)
- [Glossy: Sephora 2024 Record Earnings](https://www.glossy.co/beauty/inside-sephoras-2024-record-earnings-sephoria-wins-and-global-growth/)
- [LVMH 2024 Annual Results](https://www.lvmh.com/en/publications/lvmh-achieves-a-solid-performance-despite-an-unfavorable-global-economic-environment)
- [Sephora Wikipedia](https://en.wikipedia.org/wiki/Sephora)
- [Sephora Americas Leadership](https://newsroom.sephora.com/sephora-americas-leadership/)
- [Sephora Community: Payment Errors](https://community.sephora.com/t5/Customer-Support/Problems-checking-out-on-app-amp-website/m-p/6479444)
- [Sephora Community: Authorization Failures](https://community.sephora.com/t5/Customer-Support/Unsuccessful-authorization-again/m-p/6358727)
- [Sephora Community: Checkout Errors](https://community.sephora.com/t5/Customer-Support/HELP-online-order-checkout-errors/m-p/6970196)
- [Sephora UAE Payment Methods](https://ae.arabiccoupon.com/en/article/discover-the-payment-methods-available-from-sephora)
- [Sephora Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Sephora_logo.svg)
