# BYTEDANCE / TIKTOK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: ByteDance / TikTok
═══════════════════════════════════════

Logo: https://www.logo.wine/a/logo/TikTok/TikTok-Icon-Logo.wine.svg
Nombre merchant: ByteDance / TikTok

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross Border Decline Tax
Tittle_Pain Point_2: Fragmented 5 PSP Stack
Tittle_Pain Point_3: LATAM APM Blind Spots
Tittle_Pain Point_4: SEA COD Margin Drain
Tittle_Pain Point_5: EU Localization Gap

Desc_Pain Point_1: Card declines are the #1 TikTok Shop complaint. Cross border acquiring across 20+ markets triggers issuer blocks. At $64B GMV, even 1% uplift recovers $640M annually.
Desc_Pain Point_2: Stripe, Adyen, PayPal, Worldpay, and J.P. Morgan operate without an orchestration layer. No unified routing, monitoring, or failover across 20+ countries.
Desc_Pain Point_3: Brazil (#3 by users, 131M) and Mexico (#4, 74M) lack Pix, Boleto, OXXO, and SPEI at checkout. TikTok is now applying for fintech licenses in Brazil to close this gap.
Desc_Pain Point_4: COD dominates Indonesia, Thailand, Vietnam, Malaysia, Philippines. No QRIS, GoPay, OVO, Dana, TrueMoney, or GCash at TikTok Shop checkout in these markets.
Desc_Pain Point_5: TikTok Shop launched in France, Germany, Italy, Spain, Ireland with zero confirmed local APMs. No Carte Bancaire, SEPA DD, Giropay, Bancomat Pay, or Bizum at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Adyen
PSP_3: Worldpay
PSP_4: J.P. Morgan

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: QRIS
Local_M_4: GoPay
Local_M_5: GCash
Local_M_6: TrueMoney
Local_M_7: Carte Bancaire
Local_M_8: SEPA Direct Debit
Local_M_9: KakaoPay
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each TikTok Shop, Coins, and LIVE transaction across Stripe, Adyen, Worldpay, and J.P. Morgan to the best performing acquirer for that card BIN, issuer, and market. At $64B GMV across 20+ countries, a 3% auth uplift translates to $1.9B+ in recovered revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates single PSP dependency. When Stripe declines, Yuno reroutes to Adyen or Worldpay in milliseconds. InDrive achieved 90% approval and 4.5% transaction recovery across 10 LATAM markets using this approach.
Desc_Yuno_Cap3: Activates the APMs TikTok Shop needs: Pix in Brazil (131M users), OXXO in Mexico (74M), QRIS/GoPay in Indonesia (180M), GCash in Philippines, Carte Bancaire in France. One API, 1,000+ methods, no per market engineering sprints.
Desc_Yuno_Cap4: One dashboard replacing TikTok's fragmented Stripe + Adyen + PayPal + Worldpay + J.P. Morgan settlement streams. Centralized reconciliation, real time approval monitoring, millisecond anomaly detection via Monitors across all 20+ markets.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ByteDance / TikTok at a glance:**
- ByteDance: $186B revenue (2025), $155B (2024), ~150,000 employees across 120+ cities
- TikTok platform revenue: ~$23B (2024), ~77% from ads, rest from commerce and in app purchases
- TikTok Shop global GMV: $64.3B (2025), up ~100% YoY from $33B (2024)
- TikTok MAU: 1.9B globally (2025); available in 150+ countries
- TikTok Shop live in 20+ countries: US, UK, Indonesia, Thailand, Vietnam, Malaysia, Philippines, Singapore, South Korea, Mexico, Brazil, France, Germany, Italy, Spain, Ireland, Japan, mainland China
- Revenue streams: TikTok Shop (marketplace commissions), TikTok Coins (virtual currency for LIVE gifts), LIVE Subscriptions/Super Fan ($9.99/mo), advertising, creator payouts
- CEO: Shou Zi Chew (ex CFO ByteDance); USDS Joint Venture (2026): Oracle 15%, MGX 15%, Silver Lake 15%, Michael Dell 35.1%, ByteDance 19.9%
- No dedicated VP/Head of Payments publicly identified. PIPO (Global Payments division) has regional country directors (e.g., Thailand). ByteDance actively hiring "Global Head of Legal, Global Payments"

**Confirmed PSPs:**
- Stripe: tips, creator payments (confirmed via FXC Intelligence, press release)
- Adyen: payment processing (FXC Intelligence report)
- PayPal: US/UK checkout, creator LIVE gift payouts
- Worldpay: payment processing (FXC Intelligence report)
- J.P. Morgan: real time payments infrastructure, 24+ markets, 10x cost reduction, instant settlement
- Payoneer / WorldFirst: cross border seller payout intermediaries
- No payment orchestrator detected (Spreedly, Primer, Gr4vy, CellPoint, APEXX: none found)

**PIPO (Payments Division) Context:**
- PIPO Luxembourg SA: established 2024 for EU payment licensing (after failed Ireland attempt)
- PIPO Europe Limited: 10 Earlsfort Terrace, Dublin 2, Ireland
- TikTok applied for EMI and credit licenses in Brazil (March 2026) to offer payments and lending to 131M Brazilian users
- ByteDance is building centralized payments infrastructure modeled after Douyin (Chinese counterpart)
- Member of The Payments Association EU

---

**Top 5 Markets Gap Analysis:**

MARKET 1: Indonesia (#1 by users, ~180M MAU)
  ✅ Currently offer: Visa/MC cards, COD, local bank installments
  ❌ Missing: QRIS, GoPay, OVO, DANA, ShopeePay, bank transfers
  💡 Digital wallets dominate Indonesian e commerce. GoPay and OVO alone handle hundreds of millions of monthly transactions. COD is expensive operationally; shifting to digital payments is critical.

MARKET 2: United States (#2, ~136M MAU)
  ✅ Currently offer: Visa, MC, Amex, Discover, Apple Pay, Google Pay, PayPal, Venmo, Klarna, Affirm, CC installments (3x 0%), TikTok Balance
  ❌ Missing: Cash App Pay, ACH
  💡 US is well served. Cash App has 57M+ users skewing young, matching TikTok's demographic. ACH could reduce processing costs for subscriptions.

MARKET 3: Brazil (#3, ~131M users)
  ✅ Currently offer: Cards (Visa/MC), PayPal [limited confirmation]
  ❌ Missing: Pix, Boleto, local installment cards (parcelamento)
  💡 Pix processes 45B+ transactions/year and is the dominant digital payment in Brazil. TikTok is actively seeking EMI + credit licenses in Brazil, confirming they know this gap exists. TikTok Shop Brazil reached $46.1M GMV by August 2025.

MARKET 4: Mexico (#4, ~74M MAU)
  ✅ Currently offer: Cards [limited confirmation]
  ❌ Missing: OXXO, SPEI, CoDi, Mercado Pago
  💡 60%+ of Mexican adults are unbanked. OXXO Pay is the primary bridge to digital commerce. Without OXXO, TikTok Shop cannot reach the majority of potential buyers.

MARKET 5: France / Germany / Italy / Spain (EU expansion, 200M+ TikTok MAU across Europe)
  ✅ Currently offer: Cards, likely PayPal
  ❌ Missing: Carte Bancaire (France), Giropay (Germany), SEPA Direct Debit, Bancomat Pay (Italy), Bizum (Spain), PostePay (Italy)
  💡 TikTok Shop launched in these 4 EU markets between December 2024 and March 2025. No confirmed local APMs despite each market having dominant local methods. Carte Bancaire accounts for ~60% of card transactions in France.

---

**Payment Complaint History:**
- Card declines: #1 complaint. "Why is my payment method declined" and "Why is my card declining for TikTok Shop" are among the most searched TikTok discovery topics
- Cross border bank flagging: items shipping from overseas trigger issuer blocks
- Unauthorized charges: multiple reports of charges users did not approve; TikTok covers "Unauthorized Payment" chargebacks for sellers
- Duplicate billing: technical glitches causing double charges reported across multiple platforms
- Chargeback complexity: sellers face $10/chargeback appeal fee, 7 day response window, only 45% win rate industry average
- Refund friction: complex process for both buyers and sellers
- UX issue: "View all" button required to see all payment methods at checkout, reducing BNPL and wallet adoption
- Creator payout delays: January 2025 payout delays during US ban uncertainty
- 3 service incidents in last 90 days (median duration 5h 13m)

---

**Key Meeting Angles:**

1. **$64B GMV with no orchestration** | Five PSPs across 20+ markets with no unified routing layer. At this scale, even marginal approval rate improvement generates hundreds of millions in recovered GMV.

2. **LATAM fintech ambitions** | TikTok applied for EMI + credit licenses in Brazil (March 2026), plans R$200B data center investment. They are building financial services but need the payment rails first. Yuno provides instant LATAM APM coverage while they build.

3. **EU expansion without local methods** | 5 new European markets launched in 6 months with no confirmed local APMs. Carte Bancaire, SEPA DD, Giropay, Bancomat Pay are table stakes in those countries.

4. **SEA COD dependency** | 5 Southeast Asian markets (~380M MAU combined) rely heavily on COD. Failed deliveries, cash handling costs, and margin erosion make digital payment migration essential. QRIS, GoPay, OVO, TrueMoney, GCash are missing.

5. **In house payments transition** | PIPO Luxembourg for EU licensing, J.P. Morgan for real time payments, Brazil fintech applications. Multi year build. Yuno can orchestrate both legacy PSPs and new in house rails during transition.

6. **Card declines are the #1 user complaint** | Cross border acquiring causes issuer blocks. Smart Routing with local acquiring directly solves this. InDrive achieved 90% approval across 10 LATAM markets.

7. **Revenue streams beyond commerce** | TikTok Coins (virtual currency), LIVE gifts, Super Fan subscriptions ($9.99/mo), creator payouts, advertising credits. Each stream has its own payment complexity.

---

**Sources:**
- [FXC Intelligence: TikTok Payments Strategy](https://www.fxcintel.com/research/reports/tiktok-payments-processing-ecommerce-opportunities)
- [TikTok Seller University: Payment Methods](https://seller-us.tiktok.com/university/essay?knowledge_id=4186564050224897&lang=en)
- [Accio: TikTok Shop Payment Methods Guide](https://www.accio.com/blog/the-ultimate-tiktok-shop-payment-methods-guide-what-works-now)
- [PaymentExpert: ByteDance Luxembourg License](https://paymentexpert.com/2024/08/12/bytedance-european-licence-luxembourg/)
- [FintechFutures: TikTok Brazil EMI + Credit License](https://www.fintechfutures.com/regulatory-actions/tiktok-applies-for-emi-and-credit-licences-in-brazil)
- [Vixio: TikTok Enable Instant Payments via J.P. Morgan](https://www.vixio.com/insights/pc-tiktok-enable-instant-account-account-payments-platform)
- [Voz.us: ByteDance J.P. Morgan Partnership](https://voz.us/tiktok-owner-partners-with-j-p-morgan-to-power-its-payments-system/?lang=en)
- [Retail Systems: J.P. Morgan TikTok Payments](https://www.retail-systems.com/rs/JP_Morgan_working_on_TikTok_payments_infrastructure.php)
- [Stripe/TikTok Tips Partnership](https://fintechmagazine.com/financial-services-finserv/tiktok-partners-fintech-firm-stripe-tips-payments)
- [Business of Apps: TikTok Revenue and Stats](https://www.businessofapps.com/data/tik-tok-statistics/)
- [Tubefilter: TikTok $39B International Revenue](https://www.tubefilter.com/2025/04/11/tiktok-us-earnings-bytedance-sale/)
- [ResourceRA: TikTok Shop GMV Statistics](https://resourcera.com/data/social/tiktok-shop-statistics/)
- [MarketMaze: TikTok Shop Doubles GMV](https://www.marketmaze.me/p/tiktok-shop-is-a-global-rocket)
- [Awisee: TikTok Shop Statistics](https://awisee.com/blog/tiktok-shop-statistics/)
- [MarketingLTB: TikTok Shop Statistics](https://marketingltb.com/blog/statistics/tiktok-shop-statistics/)
- [Galileo: TikTok Shop Reshaping LatAm Commerce](https://www.galileo-ft.com/blog/tiktok-shop-latam-commerce-banking-lessons/)
- [Awisee: TikTok Shop Europe Expansion](https://awisee.com/blog/tiktok-shop-expands-in-europe/)
- [Awisee: TikTok Shop LATAM](https://awisee.com/blog/tiktok-shop-in-latin-america/)
- [Wise: TikTok Shop Payment Methods](https://wise.com/gb/blog/how-to-pay-on-tiktok-shop)
- [Chargeflow: TikTok Shop Chargeback Guide](https://www.chargeflow.io/blog/ultimate-tiktok-shop-chargeback-guide)
- [TikTok Seller University: Chargeback Policy](https://seller-us.tiktok.com/university/essay?knowledge_id=7989055607670570&lang=en)
- [TikTok Brand Hub](https://tiktokbrandhub.com/)
- [Payoneer: TikTok Shop FAQ](https://payoneer.custhelp.com/app/answers/detail/a_id/43209/~/tik-tok-shop-faq)
- [DemandSage: TikTok User Statistics](https://www.demandsage.com/tiktok-user-statistics/)
- [World Population Review: TikTok Users by Country](https://worldpopulationreview.com/country-rankings/tiktok-users-by-country)
- [SCMP: ByteDance Overseas Revenue](https://www.scmp.com/tech/big-tech/article/3306161/tiktok-owner-bytedances-overseas-sales-jump-2024-despite-us-hurdles-report)
- [PIPO Luxembourg SA: Payments Association EU](https://www.thepaymentsassociation.eu/membership-directory/corporate/2901734)
- [LifeAtTikTok: Global Head of Legal, Global Payments](https://lifeattiktok.com/search/7522889591839492370)
- [The Org: ByteDance Leadership](https://theorg.com/org/bytedance/teams/leadership-team-1)
- [Glassdoor: ByteDance PIPO Review](https://www.glassdoor.com/Reviews/Employee-Review-ByteDance-E1624196-RVW87043268.htm)
- [ShopiFreaks: TikTok Brazil Fintech Licenses](https://www.shopifreaks.com/tiktok-applies-for-brazilian-fintech-licenses-to-offer-payments-and-lending-to-131-million-local-users/)
- [Logo.wine: TikTok Logo](https://www.logo.wine/logo/TikTok)
