# OLO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Olo
=======================================

Logo: https://cdn.brandfetch.io/idV7ZwmjhP/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Olo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Dependency
Tittle_Pain Point_2: High Cart Abandonment
Tittle_Pain Point_3: In-Store Payment Gaps
Tittle_Pain Point_4: US-Only Coverage
Tittle_Pain Point_5: Multi-Brand Reconciliation

Desc_Pain Point_1: Olo Pay processes $2.8B in GPV exclusively through Stripe. While the FreedomPay partnership adds in-store processing, digital ordering (the core volume) runs through a single acquirer. For 800+ restaurant brands across 90,000 locations processing 4M+ orders daily, single-acquirer dependency means no fallback when Stripe declines. Every failed transaction is a lost meal order with zero automatic retry.
Desc_Pain Point_2: The average online food ordering cart abandonment rate is nearly 70%. Two of the top reasons are mandatory account creation and complicated checkout. Olo's passwordless Olo Accounts and Apple Pay/Google Pay integration help, but restaurants using Olo still lose significant revenue at checkout. No BNPL option for catering orders ($500 to $5,000+), no PayPal/Venmo despite 90M+ US active accounts.
Desc_Pain Point_3: Olo Pay launched as card-not-present first (digital ordering). In-store expansion via FreedomPay/Stripe partnership announced February 2025 is still early stage. The majority of 90,000 locations still process in-store payments through legacy POS processors disconnected from Olo Pay. No unified view of guest spending across digital and in-store channels for most locations.
Desc_Pain Point_4: Olo operates exclusively in the United States and Canada. As enterprise restaurant brands like Five Guys, Shake Shack, and Wingstop expand internationally, their digital ordering and payment infrastructure cannot follow. No support for local payment methods in international markets where these brands already operate (UK, Europe, Middle East, Asia).
Desc_Pain Point_5: 800+ restaurant brands each with dozens to thousands of locations create massive reconciliation complexity. Each brand may have different fee structures, chargeback policies, and reporting needs. Olo consolidates digital payments, but brands using multiple PSPs for in-store and digital still face fragmented settlement, split reporting, and cross-channel guest identity gaps.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Olo Pay, primary digital)
PSP_2: FreedomPay (in-store gateway)
PSP_3: Legacy POS processors (per-brand)
PSP_4: Third-party marketplaces (DoorDash, Uber Eats)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Venmo
Local_M_3: Klarna
Local_M_4: Afterpay
Local_M_5: Cash App Pay
Local_M_6: Alipay
Local_M_7: WeChat Pay
Local_M_8: iDEAL
Local_M_9: Pix
Local_M_10: Cartes Bancaires

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, FreedomPay, and legacy POS processors for every restaurant order. Each transaction routed to the highest-performing acquirer for that card BIN, issuer, and geography. On $2.8B in GPV across 800+ brands and 90,000 locations, smart routing delivers +3 to 10% authorization uplift on top of Olo Pay's already strong 96.7% auth rate, recovering millions in orders that would otherwise fail at checkout.
Desc_Yuno_Cap2: Automatic cascade across Olo's payment partners eliminates single-acquirer risk on $2.8B in digital ordering volume. When Stripe declines an order, Yuno reroutes to an alternative processor in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For restaurant orders (food being prepared, delivery driver waiting), a failed payment creates waste, delays, and customer churn.
Desc_Yuno_Cap3: Unlocks the payment methods Olo's Stripe-only stack does not offer: PayPal and Venmo (90M+ US active accounts combined), Cash App Pay (57M+ monthly users), Klarna and Afterpay for BNPL on high-value catering orders ($500 to $5,000+), Alipay and WeChat Pay for international brand expansion, iDEAL and Cartes Bancaires for European markets. One API, 1,000+ payment methods for restaurant commerce.
Desc_Yuno_Cap4: One dashboard replacing Olo's Stripe + FreedomPay + legacy POS processor stack. Real-time approval rate monitoring across 800+ brands and 90,000 locations, centralized reconciliation for digital orders, in-store purchases, catering, refunds, and chargebacks, millisecond anomaly detection via Monitors. Reduces the 0.04% chargeback rate further while maintaining the 96.7% authorization rate across all channels and all brands.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Olo at a glance:**
- Model: Open SaaS platform for restaurant digital ordering, payments, and guest engagement
- Products: Olo Ordering (digital ordering), Olo Pay (payments), Olo Engage (marketing/guest data), Olo Loyalty (via Spendgo acquisition)
- Revenue: ~$314M TTM (Q2 2025), up 22% YoY
- Q2 2025 Revenue: $85.7M (+22% YoY)
- Q1 2025 Revenue: $80.7M (+21% YoY)
- FY2024 Revenue: $284.9M (+25% YoY)
- GPV (Gross Payment Volume): $2.8B (FY2024)
- GMV (Gross Merchandise Volume): $29B (FY2024)
- Active Locations: ~90,000 (Q1 2025), growing ~2,000/quarter
- Restaurant Brands: 800+
- Connected Guests: 108M
- Orders per Day: 4M+ average
- Integration Partners: 400+
- Dollar-Based Net Revenue Retention: 111%
- Cash and Investments: $401.8M (Q1 2025)
- Founded: 2005, New York City
- Founder & CEO: Noah Glass (20+ years in foodservice, boards: Portillo's, Share Our Strength, Culinary Institute of America)
- CTO: Jason Ordway
- CFO: Peter Benevides
- CRO: Diego Panama
- COO: Jo Lambert
- CSO: Parrish Chapman (joined May 2025)
- Acquired by Thoma Bravo: September 2025, $2.0B all-cash ($10.25/share, 65% premium)

**Thoma Bravo Acquisition (September 2025):**
- All-cash transaction valued at ~$2.0B
- $10.25 per share (65% premium over $6.20 unaffected price)
- Approved by stockholders September 9, 2025
- Thoma Bravo: $181B+ AUM, largest software-focused PE firm globally
- Noah Glass remains CEO post-acquisition

**Spendgo Acquisition (December 2025):**
- First acquisition under Thoma Bravo ownership
- Spendgo: loyalty and guest engagement platform (founded 2010)
- 120+ restaurant brands using Spendgo loyalty
- Phone-number-based loyalty (low acquisition cost)
- Clients: Cold Stone Creamery, Golden Chick, Captain D's, Shipley Do-Nuts
- Olo Loyalty immediately available; deeper integrations planned early 2026

**Olo Pay Performance Metrics (2024):**
- Authorization Rate: 96.7%
- Fraud Rate: 0.02%
- Chargeback Rate: 0.04%
- Fraudulent Transactions Blocked: $66M+
- Chargeback Fees Saved: $11M+

**Notable Restaurant Brands (using Olo):**
- Five Guys, Shake Shack, Sweetgreen, Wingstop, Applebee's, Chili's, The Cheesecake Factory, Denny's, Lucille's Smokehouse Bar-B-Que, WaBa Grill, and hundreds more

**Case Studies:**
- Lucille's Smokehouse Bar-B-Que: Olo Pay blocked ~6,000 high-risk orders, saving $1.1M. Previously 3.5% of online orders went to chargebacks; now $15 less per chargeback
- WaBa Grill: 30%+ fraud reduction with Olo Pay

**Payments Infrastructure:**
- Stripe: primary payment processor for Olo Pay (digital ordering, card-not-present)
- FreedomPay: payment gateway for in-store (card-present) transactions, announced February 2025
- FreedomPay is processor-agnostic, integrated with 1,000+ POS and payment systems
- Olo Pay launched with Stripe in 2022 for digital payments
- In-store Olo Pay via Stripe + FreedomPay now available for 700+ customers
- EMV-compatible payment terminals with point-to-point encryption
- Self-service kiosks for in-store ordering and payment
- Olo Accounts: passwordless checkout with stored credentials
- Legacy POS processors: still in use at majority of 90,000 locations for in-store

**Payment Methods Supported:**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- Apple Pay
- Google Pay
- Cards on file (stored credentials via Olo Accounts)
- Contactless payments (in-store)

**Payment Methods NOT Supported:**
- PayPal
- Venmo
- Cash App Pay
- Klarna / BNPL
- Afterpay
- Alipay / WeChat Pay
- Samsung Pay (limited)
- Local European, Asian, or Latin American methods

**Geographic Coverage:**
- United States (primary, ~95%+ of volume)
- Canada (limited)
- No international markets

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary, 90,000 locations)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay
  Missing: PayPal (60M+ US active accounts), Venmo (30M+ users), Cash App Pay (57M+ monthly users), Klarna, Afterpay, Affirm
  PayPal, Venmo, and Cash App Pay combined represent 150M+ US digital wallet users not served by Olo Pay's current stack.

MARKET 2: United States (catering, $500-$5,000+ orders)
  Currently offer: Credit/debit cards only
  Missing: BNPL (Klarna, Afterpay, Affirm), ACH/bank transfer, corporate billing
  High-value catering orders are natural BNPL candidates. Corporate catering often requires invoice-based payment not supported by cards-only checkout.

MARKET 3: United Kingdom (Five Guys, Shake Shack, Wingstop expansion)
  Currently offer: Not available (US-only platform)
  Missing: Open Banking, Klarna, PayPal, Cartes Bancaires, Apple Pay UK
  Five Guys has 150+ UK locations. Shake Shack has 20+ UK locations. Wingstop has 50+ UK locations. These brands need local UK payment methods.

MARKET 4: Europe (enterprise brand expansion)
  Currently offer: Not available
  Missing: iDEAL (Netherlands), Bancontact (Belgium), Cartes Bancaires (France), Bizum (Spain), Klarna, SEPA
  Enterprise restaurant brands are expanding across Europe. Local APMs are required for each market.

MARKET 5: Middle East / Asia (Five Guys, Shake Shack global presence)
  Currently offer: Not available
  Missing: Mada (Saudi Arabia), UPI (India), GrabPay (Southeast Asia), Alipay, WeChat Pay
  Five Guys has locations in Saudi Arabia, UAE, and across Asia. Shake Shack operates in Japan, South Korea, Hong Kong, and the Middle East.

**Payment Pain Points:**
1. $2.8B GPV running exclusively through Stripe with no fallback processor
2. No PayPal, Venmo, or Cash App Pay despite 150M+ US digital wallet users
3. No BNPL for high-value catering orders ($500-$5,000+)
4. In-store Olo Pay via FreedomPay still early stage; most locations on legacy processors
5. US-only coverage while enterprise brands expand globally
6. 70% cart abandonment in digital ordering; limited payment options contribute
7. Multi-brand reconciliation complexity across 800+ brands
8. No smart routing to optimize auth rates beyond Stripe's native capabilities
9. Legacy POS processors disconnected from Olo Pay create guest identity gaps
10. Fraud blocked $66M+ in 2024, but fraudsters adapt; multi-acquirer data improves detection

**Key Meeting Angles:**
1. **$2.8B GPV, single acquirer**: Every digital restaurant order flows through Stripe. Yuno adds multi-acquirer routing without replacing Stripe, providing failover on 4M+ daily orders
2. **PayPal and Venmo are missing**: 150M+ US digital wallet users cannot pay with their preferred method. Yuno activates PayPal, Venmo, Cash App Pay, and 1,000+ methods via one API
3. **Catering BNPL opportunity**: Corporate and event catering ($500-$5,000+ orders) are natural BNPL candidates. Klarna and Afterpay increase conversion and AOV for high-ticket orders
4. **96.7% auth rate can go higher**: Olo Pay already achieves industry-leading auth rates. Yuno's smart routing (+3-10% uplift) applied to $2.8B GPV means tens of millions in recovered orders. McDonald's gained +4.7% auth rate with Yuno
5. **International expansion path**: Five Guys, Shake Shack, Wingstop operate globally. Yuno provides the multi-market payment layer these brands need outside the US. InDrive achieved 90% approval across 10 markets with Yuno
6. **Post-Thoma Bravo growth mandate**: $2B acquisition with PE backing means aggressive growth targets. Payment optimization is a direct revenue lever
7. **Spendgo + payments convergence**: Loyalty programs tied to payment methods increase guest engagement. Yuno's unified orchestration enables loyalty tracking across all payment channels
8. **CEO founded the company in 2005**: Noah Glass has 20+ years of restaurant technology vision. He serves on the Portillo's board and the Culinary Institute of America, understanding both the business and the consumer side deeply

**Sources:**
- [Olo Homepage](https://www.olo.com/)
- [Olo Pay](https://www.olo.com/pay)
- [Olo Pay Solution Suite](https://www.olo.com/solutions/pay)
- [Olo About Us](https://www.olo.com/about-us)
- [Olo + FreedomPay + Stripe Partnership](https://www.businesswire.com/news/home/20250204262840/en/Olo-Announces-Partnership-with-FreedomPay-and-Deeper-Collaboration-with-Stripe-to-Accelerate-Adoption-of-In-store-Payments-for-Enterprise-Restaurants)
- [Olo Investor Relations](https://investors.olo.com/overview/default.aspx)
- [Olo FY2024 Financial Results](https://investors.olo.com/news/news-details/2025/Olo-Announces-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx)
- [Olo Q1 2025 Financial Results](https://www.businesswire.com/news/home/20250507249420/en/Olo-Announces-First-Quarter-2025-Financial-Results)
- [Thoma Bravo Acquires Olo](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-olo)
- [Olo Acquires Spendgo](https://www.businesswire.com/news/home/20251222826702/en/Olo-Completes-Acquisition-of-Spendgo-to-Expand-Platform-with-Loyalty-Solution)
- [Olo Wikipedia](https://en.wikipedia.org/wiki/Olo_(online_ordering))
- [Swipesum: What Is Olo](https://www.swipesum.com/insights/what-is-olo)
- [Restaurant Business: Olo Customer-Facing App](https://www.restaurantbusinessonline.com/technology/olo-launching-customer-facing-ordering-app)
- [Restaurant Business: Olo In-Store Payments](https://www.restaurantbusinessonline.com/technology/olo-takes-big-step-toward-digitizing-more-premise-transactions)
- [Olo Case Study: Lucille's Smokehouse](https://www.olo.com/case-studies/lucilles-smokehouse-bar-b-que)
- [Olo Case Study: WaBa Grill](https://www.olo.com/case-studies/waba-grill)
- [Olo Fraud Trends Blog](https://www.olo.com/blog/fraud-trends-every-restaurant-should-know-about)
- [Food On Demand: Olo Thoma Bravo](https://foodondemand.com/07072025/olo-to-be-acquired-by-thoma-bravo-in-2b-all-cash-deal/)
- [Thoma Bravo: Behind the Deal with Noah Glass](https://www.thomabravo.com/behind-the-deal/the-future-of-restaurants-in-an-ai-world-hudson-smith-with-olo-founder-noah-glass)
