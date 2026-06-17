# THE REALREAL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: The RealReal
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5e/The_RealReal_logo.svg
Nombre merchant: The RealReal

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: False Decline Epidemic
Tittle_Pain Point_2: BNPL Provider Sprawl
Tittle_Pain Point_3: International Payment Gap
Tittle_Pain Point_4: Consignor Payout Delays
Tittle_Pain Point_5: Single Acquirer Risk

Desc_Pain Point_1: Customers report "credit card declined" errors on Apple Pay and debit cards when neither the bank nor the card issuer blocked the transaction. TikTok and PurseForum threads document repeated order cancellations after payment. For a marketplace with $2.1B GMV and average luxury price points, every false decline is a high value sale lost.
Desc_Pain Point_2: The RealReal integrates Affirm, Afterpay, Klarna, Zip, and Sezzle as separate BNPL providers. Each requires its own contract, reconciliation, and integration maintenance. Five BNPL partners for a single US market creates operational overhead with no unified installment routing or fallback if one provider's approval rate drops.
Desc_Pain Point_3: The RealReal ships to 61 countries but accepts only US payment methods: Visa, MC, Amex, Discover, PayPal, and Affirm. European buyers paying with cards face cross border fees and lower auth rates. No iDEAL for Dutch buyers, no Klarna for EU, no Pix for Brazil, no Alipay for Chinese luxury shoppers. International demand exists but checkout friction blocks it.
Desc_Pain Point_4: Consignors receive payouts monthly with a 15 to 45 day delay after sale. Direct deposit, paper check ($5 fee, 5 to 7 days), or site credit are the only options. No instant payout, no PayPal payout, no Venmo. Competing platforms like Vestiaire Collective offer faster seller payments, making payout speed a consignor retention issue.
Desc_Pain Point_5: The RealReal's payment processing provider is not publicly disclosed, suggesting a single acquirer setup with no multi processor routing. With $692M annual revenue and $2.1B GMV, a single point of payment failure risks significant revenue loss. No evidence of failover routing, cascade retries, or multi acquirer optimization exists.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed Primary Acquirer
PSP_2: PayPal
PSP_3: Affirm
PSP_4: Afterpay (Block)
PSP_5: Klarna

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: Bancontact (Belgium)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: Alipay (China)
Local_M_5: WeChat Pay (China)
Local_M_6: Pix (Brazil)
Local_M_7: Klarna (EU, non US)
Local_M_8: Trustly (Open Banking EU)
Local_M_9: Kakao Pay (South Korea)
Local_M_10: JCB (Japan)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route every transaction to the optimal acquirer by card BIN, issuer, and buyer geography in real time. With $2.1B GMV and average order values in the hundreds, even a 2% authorization uplift recovers tens of millions in annual revenue. Smart Routing eliminates the false declines documented across customer forums by finding the best processing path for each card and transaction profile.
Desc_Yuno_Cap2: When the primary acquirer declines a card or Apple Pay transaction, Yuno cascades to the next viable processor in milliseconds. Customers reporting valid cards declined while the bank approved is a classic single acquirer problem. With Yuno, no buyer sees a false decline while a working route exists. For luxury items with $1,000+ price points, every recovered transaction matters.
Desc_Yuno_Cap3: One API activates iDEAL for Dutch buyers, Bancontact for Belgium, SEPA for the EU, Alipay and WeChat Pay for Chinese luxury shoppers, Pix for Brazil, Kakao Pay for South Korea, and JCB for Japan. The RealReal ships to 61 countries but only accepts US payment rails. Yuno connects 1,000+ payment methods across 40+ countries, turning international shipping into international selling.
Desc_Yuno_Cap4: Replace five separate BNPL integrations (Affirm, Afterpay, Klarna, Zip, Sezzle) plus PayPal and the primary acquirer with a single dashboard. Real time approval rate monitoring across all payment methods. Unified BNPL routing: if Affirm declines, route to Klarna. One reconciliation stream instead of seven. Centralized fraud scoring across card, wallet, and installment transactions on $2.1B in annual GMV.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**The RealReal at a glance:**
- Founded: 2011 by Julie Wainwright
- Headquarters: San Francisco, California
- CEO: Rati Levesque (President & CEO)
- Listed on Nasdaq as REAL (IPO June 2019, raised $300M)
- Revenue: $692.85M (FY2025, +15.4% YoY), $600M (FY2024, +9% YoY)
- Gross Merchandise Value (GMV): ~$2.10B (2025 guidance midpoint)
- 38M+ members
- Nearly 40M items sold since founding
- 17 Luxury Consignment Offices (14 with retail), plus flagship stores
- Achieved positive Adjusted EBITDA and free cash flow for first time in FY2024
- Q4 2024: GMV +12%, revenue +14% vs Q4 2023
- World's largest online marketplace for authenticated luxury resale
- Ships to 61 countries via UPS and DHL Express
- Categories: handbags, watches, jewelry, clothing, shoes, art, home decor
- Authentication: hundreds of in house experts including gemologists and horologists

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| Undisclosed Primary Acquirer | Card processing (Visa, MC, Amex, Discover) | US |
| PayPal | Digital wallet | US |
| Affirm | BNPL (monthly installments, 0% financing) | US |
| Afterpay | BNPL (Pay in 4, 6 or 12 month plans) | US |
| Klarna | BNPL (Pay in 4) | US |
| Zip | BNPL (Pay in 4 over 6 weeks) | US |
| Sezzle | BNPL (4 interest free payments) | US |
| Pay with Moon | Crypto (Bitcoin/USDT via gift cards, indirect) | US |

**No payment orchestrator detected.** Each BNPL provider runs independently. Primary acquirer undisclosed.

**Consignor payout structure:**
- Commission: 20% to 90% depending on category and item value
- Handbags $7,500+: up to 80% to consignor
- Watches $7,500+: up to 85% to consignor
- Jewelry $750+: up to 70% to consignor
- Payout timing: monthly (e.g., November sale paid December 15)
- Payout methods: direct deposit, paper check ($5 fee, 5 to 7 days), or site credit (+5% bonus)
- No instant payout, no PayPal payout, no Venmo payout
- Loyalty tier bonuses: +5% for net sales over $10,000

**Customer reported payment issues:**
- "Credit card declined" messages when bank did not decline the transaction
- Apple Pay declines on valid cards with no explanation
- Multiple debit cards declined simultaneously on same account
- Advised to "try again in a couple of days" as resolution
- Order cancellations after payment without clear explanation (documented on TikTok)
- Unauthorized purchases on compromised accounts (PayPal fraud cases)
- XCover return guarantee refund disputes (deposits to bank instead of original payment method)
- BBB complaints related to payment and billing issues

**International shipping (61 countries) but US only payments:**
- Ships internationally via UPS Worldwide Expedited and DHL Express
- All duties unpaid (buyer responsible for import taxes/VAT/customs)
- No local payment methods for international buyers
- European, Asian, and LATAM buyers must use US denominated cards or PayPal
- Cross border card transactions have higher decline rates and fees
- Chinese luxury shoppers (massive market) cannot use Alipay or WeChat Pay

**Key meeting angles:**
1. **False decline revenue leak** | Customer forums prove valid cards are being declined. Smart routing across multiple acquirers directly solves this by finding the best processing path for each transaction
2. **Five BNPL providers, zero orchestration** | Affirm, Afterpay, Klarna, Zip, and Sezzle all run independently. If Affirm declines a buyer, there is no automatic cascade to Klarna or Afterpay. Yuno unifies all BNPL under one routing layer
3. **61 countries, US only payments** | The RealReal ships globally but only accepts American payment methods. Chinese, European, and LATAM luxury buyers face checkout friction. One Yuno integration activates Alipay, iDEAL, Pix, and more
4. **$2.1B GMV at luxury price points** | Average order values are in the hundreds to thousands. Every declined transaction represents significant lost revenue. Even a 1% auth rate improvement at this scale is transformative
5. **Consignor payout modernization** | Monthly payouts with 15 to 45 day delays lose consignors to faster platforms. Orchestrated payout routing could enable instant or weekly payouts via multiple rails
6. **First profitable year = infrastructure moment** | The RealReal achieved positive EBITDA and FCF in 2024 for the first time. This is the ideal moment to invest in payment optimization that drives revenue growth
7. **Competitor benchmark** | Vestiaire Collective, StockX, and Poshmark all offer broader payment options. StockX recently added Affirm; Vestiaire offers Klarna across Europe. The RealReal's US only payment stack is a competitive disadvantage

**Sources:**
- [The RealReal FAQ: Payment Methods](https://www.therealreal.com/faq)
- [The RealReal: What Forms of Payment Accepted](https://therealreal.zendesk.com/hc/en-us/articles/230906048-What-forms-of-payment-do-you-accept-)
- [The RealReal: Payment Preference Page](https://www.therealreal.com/payment-preference)
- [The RealReal: Shipping Guidelines](https://www.therealreal.com/shipping)
- [The RealReal: Commission Structure](https://www.therealreal.com/seller/commissions)
- [Affirm x The RealReal](https://www.therealreal.com/sales/affirm-x-trr)
- [Afterpay: The RealReal Store](https://www.afterpay.com/en-US/stores/the-realreal)
- [Klarna: The RealReal Store](https://www.klarna.com/us/store/52fb07ff-338d-49af-be5a-307064977c08/The-RealReal/pay-with-klarna/)
- [Zip: The RealReal Store](https://zip.co/us/store/the-realreal)
- [Sezzle: The RealReal Store](https://sezzle.com/shop/the-realreal/)
- [The RealReal Q4 and Full Year 2024 Results](https://investor.therealreal.com/news-releases/news-release-details/realreal-announces-fourth-quarter-and-full-year-2024-results/)
- [The RealReal Preliminary Q4/FY2024 Results + 2025 Guidance](https://investor.therealreal.com/news-releases/news-release-details/realreal-reports-strong-preliminary-fourth-quarter-and-full-year)
- [The RealReal Revenue (Stock Analysis)](https://stockanalysis.com/stocks/real/revenue/)
- [The RealReal Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/REAL/realreal/revenue)
- [The RealReal Wikipedia](https://en.wikipedia.org/wiki/The_RealReal)
- [The RealReal Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:The_RealReal_logo.svg)
- [The RealReal Commission Guide (TopBubbleIndex)](https://www.topbubbleindex.com/blog/the-realreal-fees/)
- [How The RealReal Reached Profitability (Circular Fashion News)](https://circularfashionnews.substack.com/p/deep-dive-how-did-the-realreal-reach)
- [PYMNTS: Luxury Retailers BNPL Trend](https://www.pymnts.com/news/retail/2026/luxury-retailers-rethink-pricing-as-wealthy-consumers-tighten-budgets/)
- [Twitter/X: The RealReal Payment Decline Complaints](https://x.com/ShelleySullivan/status/1459805752323981318)
- [BBB: The RealReal Complaints](https://www.bbb.org/us/ca/san-francisco/profile/ecommerce/the-realreal-inc-1116-460621/complaints)
- [The RealReal Fees Guide (Vendoo)](https://blog.vendoo.co/luxury-consignment-how-to-sell-with-the-realreal)
