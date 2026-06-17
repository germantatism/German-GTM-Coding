# URBAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Urban
=======================================

Logo: https://cdn.brandfetch.io/idPjMIq8Kl/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Urban

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: No BNPL for Wellness
Tittle_Pain Point_3: Therapist Payout Friction
Tittle_Pain Point_4: Limited International APMs
Tittle_Pain Point_5: Gift Card Stack Disconnect

Desc_Pain Point_1: Urban runs payments through Braintree (PayPal), Checkout.com, and Shopify across different flows. App bookings process through Braintree or Checkout.com, while gift card purchases route through Shopify. No unified orchestration layer connects these three processors. Each transaction goes to a single PSP with no fallback, no smart routing, and no cross-processor optimization across 1.3M+ treatments delivered.
Desc_Pain Point_2: Wellness treatments range from 60 to 150+ GBP per session. Premium packages (couples massage, multi-session plans, corporate wellness) can reach 500+ GBP. Urban offers no buy-now-pay-later option despite Klarna being live on Google Pay in the UK since February 2026. Without BNPL, price-sensitive customers delay or skip bookings rather than splitting the cost across installments.
Desc_Pain Point_3: Urban operates a marketplace model with 4,000+ self-employed therapists who receive payouts after each treatment. The platform takes over 30% commission. Therapists report commission increases without corresponding price reductions for customers. Payment timing, transparency, and cost optimization at the platform level directly impact therapist retention and satisfaction.
Desc_Pain Point_4: Urban operates in the UK (London, Manchester, Birmingham, Liverpool, Edinburgh, Glasgow, Coventry) and Paris. UK and French consumers increasingly expect local payment methods: Open Banking via Pay by Bank, Cartes Bancaires for French customers, Klarna for BNPL, and iDEAL for Dutch tourists in London. Urban's current stack supports only cards and PayPal with limited wallet support.
Desc_Pain Point_5: Gift cards and corporate vouchers process through Shopify, completely separate from the Braintree/Checkout.com booking flow. No unified reconciliation between gift card purchases and treatment redemptions. Corporate gifting (bulk orders of 10+) is a growing revenue line but runs on disconnected payment infrastructure, creating operational complexity and limited spend tracking.

SLIDE 1: PSP TOPOLOGY

PSP_1: Braintree / PayPal (app bookings)
PSP_2: Checkout.com (app bookings)
PSP_3: Shopify (gift cards / vouchers)
PSP_4: Apple Pay (via Checkout.com)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Klarna
Local_M_2: Clearpay (Afterpay UK)
Local_M_3: Open Banking / Pay by Bank
Local_M_4: Cartes Bancaires
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: Google Pay
Local_M_8: Revolut Pay
Local_M_9: Alipay
Local_M_10: WeChat Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Braintree, Checkout.com, and Shopify for every wellness booking and gift card purchase. Each transaction routed to the highest-performing processor for that card BIN, issuer, and market. Across 250,000+ clients booking 1.3M+ treatments in the UK and France, smart routing delivers +3 to 10% authorization uplift, recovering revenue on declined bookings that would otherwise be lost to a single-processor decline.
Desc_Yuno_Cap2: Automatic cascade across Urban's multiple PSPs eliminates single-processor dependency per transaction. When Braintree declines a treatment booking, Yuno reroutes to Checkout.com in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For time-sensitive bookings (therapist arriving in 60 minutes), a failed payment means a cancelled appointment and lost revenue for both Urban and the therapist.
Desc_Yuno_Cap3: Activates the payment methods UK and French wellness consumers expect: Klarna for BNPL on premium treatments (60 to 150+ GBP), Clearpay for younger demographics, Open Banking / Pay by Bank for lower fees, Cartes Bancaires for French customers in Paris, iDEAL for Dutch tourists in London, Revolut Pay for the UK's 9M+ Revolut users, Alipay and WeChat Pay for Chinese tourists seeking wellness services. One API, 1,000+ payment methods.
Desc_Yuno_Cap4: One dashboard replacing Urban's fragmented Braintree + Checkout.com + Shopify stack. Real-time approval rate monitoring across all booking flows and gift card channels, centralized reconciliation for treatments, refunds, gift card redemptions, and therapist payouts, millisecond anomaly detection via Monitors. Unifies the corporate gifting revenue line with the consumer booking flow under a single payment intelligence layer.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Urban at a glance:**
- Model: On-demand wellness marketplace connecting consumers with self-employed therapists for at-home treatments
- Services: 50+ treatments including massage (deep tissue, sports, Swedish), facials, manicures, nails, waxing, lashes, osteopathy, physiotherapy
- Treatments Delivered: 1.3M+
- Clients: 250,000+
- Therapists: 4,000+ self-employed practitioners (vetted, insured, qualified)
- Five-Star Reviews: 500,000+
- Average Rating: 4.92
- Total Funding: $41M across 7 rounds from 42 investors
- Key Investors: BNF Capital, Accelerated Digital Ventures (ADV), Passion Capital, Felix Capital, Firestartr
- Series B: $10M (2019), led by ADV
- Seedrs Crowdfund: 5.9M GBP (2020), tripled the 2M GBP target, 800+ investors, pre-money valuation 42.8M GBP
- Current Valuation: ~37.4M GBP
- Founded: 2014, London, UK (originally as "Urban Massage," rebranded to "Urban" in 2018)
- Co-Founders: Jack Tang (original CEO), Giles Williams (CTO)
- CEO: Charmain Manning (appointed April 2023; joined as CFO July 2020; background at Pearson and Financial Times)
- CTO: Giles Williams (Co-Founder)
- Award: Best Beauty Treatments Booking App 2025 (LUXlife Magazine)
- Operating Cities: London, South East, Manchester, Birmingham, Liverpool, Coventry, Edinburgh, Glasgow (UK) + Paris (France)
- Commission: 30%+ taken from therapist earnings

**Payments Infrastructure:**
- Braintree (PayPal): primary payment processor for app bookings
- Checkout.com: secondary payment processor for app bookings
- Shopify: gift card and voucher purchases
- Apple Pay: supported via Checkout.com on iOS
- AMEX: supported via Checkout.com on iOS
- PayPal: supported via Braintree
- No unified payment orchestration across Braintree, Checkout.com, and Shopify
- No smart routing between processors
- Tokenized card storage (Urban does not hold full card details)
- Gift cards: 16-digit codes, valid 12 months, redeemable across multiple bookings

**Payment Methods Supported:**
- Credit/debit cards: Visa, Mastercard, Amex
- PayPal (via Braintree)
- Apple Pay (via Checkout.com on iOS)
- Gift cards / vouchers (via Shopify)

**Payment Methods NOT Supported:**
- Google Pay
- Klarna / BNPL
- Clearpay (Afterpay UK)
- Open Banking / Pay by Bank
- Cartes Bancaires (France)
- Revolut Pay
- Alipay / WeChat Pay
- iDEAL / Bancontact

**Corporate Gifting:**
- Bulk orders of 10+ gift cards with personalized messages
- Physical card option available
- Growing B2B revenue line (employers buying wellness gifts for teams)
- Processed through Shopify, separate from main booking flow

**Top 5 Markets Gap Analysis:**

MARKET 1: London and South East (primary market, largest volume)
  Currently offer: Visa/MC/Amex, PayPal, Apple Pay
  Missing: Klarna, Clearpay, Google Pay, Open Banking, Revolut Pay
  London has 9M+ Revolut users in the UK. Klarna is now on Google Pay UK since February 2026. Open Banking reduces processing fees. Premium treatments (100-150+ GBP) are natural BNPL candidates.

MARKET 2: Paris, France (international expansion market)
  Currently offer: Visa/MC, PayPal, Apple Pay
  Missing: Cartes Bancaires (dominant French card network), Bancontact, PayLib, Alma (French BNPL)
  Cartes Bancaires processes 60%+ of French card transactions. Not offering it means higher decline rates on French-issued cards.

MARKET 3: Manchester, Birmingham, Liverpool, Coventry (UK regional cities)
  Currently offer: Visa/MC, PayPal, Apple Pay
  Missing: Klarna, Clearpay, Google Pay, Open Banking
  Regional UK consumers are more price-sensitive. BNPL increases booking conversion for 80-150 GBP treatments.

MARKET 4: Edinburgh, Glasgow (Scotland)
  Currently offer: Visa/MC, PayPal, Apple Pay
  Missing: Klarna, Clearpay, Google Pay, Open Banking
  Scottish consumers have high BNPL adoption rates. Klarna and Clearpay are expected at checkout.

MARKET 5: Tourist Clientele in London (international visitors)
  Currently offer: Visa/MC, PayPal
  Missing: Alipay (1.3B+ users), WeChat Pay (900M+ users), UPI (India), iDEAL (Netherlands), Bancontact (Belgium)
  London hosts 20M+ international visitors annually. Chinese, Indian, and European tourists booking wellness treatments need their local wallets.

**Payment Pain Points:**
1. Three separate PSPs (Braintree, Checkout.com, Shopify) with no orchestration
2. No BNPL for premium wellness treatments (60-150+ GBP per session)
3. No Google Pay support despite being the UK's second-largest mobile wallet
4. No Cartes Bancaires for French market (Paris), causing higher decline rates
5. Gift card and corporate voucher payments disconnected from booking payments
6. 30%+ commission to Urban means processing cost optimization directly impacts margins
7. No smart routing between Braintree and Checkout.com
8. Therapist payout friction (commission complaints, transparency issues)
9. No Open Banking / Pay by Bank (lower fees than card processing)
10. App payment issues reported post-December 2025 update (booking failures)

**Key Meeting Angles:**
1. **1.3M+ treatments, three PSPs, no orchestration**: Braintree, Checkout.com, and Shopify operate independently. Yuno unifies all PSPs under one routing layer with real-time optimization
2. **BNPL unlocks wellness spending**: Premium treatments (100-150+ GBP) and multi-session packages are natural BNPL candidates. Klarna on Google Pay UK launched February 2026. Yuno activates Klarna and Clearpay via one API
3. **Paris expansion needs Cartes Bancaires**: 60%+ of French card transactions run on Cartes Bancaires. Without it, Urban's Paris authorization rates suffer. Yuno's 1,000+ APMs via single API includes all French payment methods
4. **Gift card revenue unification**: Corporate gifting is growing but runs on Shopify, disconnected from Braintree/Checkout.com. Yuno provides a single reconciliation layer across all channels
5. **Therapist marketplace economics**: 30%+ commission means every basis point in processing cost matters. Smart routing optimizes cost per transaction. InDrive achieved 90% approval across 10 markets with Yuno
6. **London tourist market**: 20M+ international visitors annually. Alipay, WeChat Pay, and iDEAL via Yuno serve tourists booking wellness treatments. McDonald's gained +4.7% auth rate with Yuno
7. **CEO has finance DNA**: Charmain Manning was CFO before becoming CEO. She understands payment economics, processing costs, and margin optimization deeply
8. **Award-winning platform scaling**: Best Beauty Treatments Booking App 2025. As Urban expands to new UK cities and European markets, payment infrastructure must scale. Yuno provides the multi-market payment layer

**Sources:**
- [Urban Homepage](https://urban.co/en-gb)
- [Urban Privacy Policy (PSP details)](https://urban.co/en-gb/privacy-policy)
- [Urban How It Works](https://urban.co/en-gb/how-it-works)
- [Urban Gift Cards](https://urban.co/en-gb/gifts)
- [Urban Corporate Gifting](https://urban.co/en-gb/gifts/corporate-gifting)
- [TechCrunch: Urban Series B ($10M)](https://techcrunch.com/2019/05/14/urban-series-b/)
- [EU-Startups: Urban Series B](https://www.eu-startups.com/2019/05/london-based-wellness-app-urban-closes-e9-million-series-b-for-its-on-demand-massage-and-beauty-services/)
- [Seedrs: Urban Crowdfunding Campaign](https://www.seedrs.com/urban)
- [Crowdfund Insider: Urban Overfunding](https://www.crowdfundinsider.com/2020/08/166001-overfunding-wellness-app-urban-quickly-surpasses-2-million-funding-target-through-seedrs-campaign/)
- [EU-Startups: Urban Seedrs 6.5M EUR](https://www.eu-startups.com/2020/09/british-wellness-app-urban-raises-e6-5-million-tripling-crowdfunding-target/)
- [Maddyness: Meet Urban](https://www.maddyness.com/uk/2024/03/30/meet-urban-the-app-bringing-a-human-touch-to-city-life/)
- [TechRound: Charmain Manning CEO](https://techround.co.uk/women-in-startups-tech/46-charmain-manning-ceo-at-urban/)
- [Trustpilot: Urban Reviews](https://uk.trustpilot.com/review/urban.co)
- [Britain Reviews: Urban Massage](https://britainreviews.co.uk/services/urban-massage-reviews)
- [CB Insights: Urban Financials](https://www.cbinsights.com/company/urban-massage/people)
- [Tracxn: Urban Profile](https://tracxn.com/d/companies/urban/__hIehRvPhZbFzLD3NUtK3dmXVCEUYdyvqSaLUqEbw_VY)
- [Google Play: Urban App](https://play.google.com/store/apps/details?id=com.urbanmassage.Massage&hl=en_GB)
- [Bdaily: Urban Liverpool Expansion](https://bdaily.co.uk/articles/2024/03/06/innovative-wellness-app-announces-significant-expansion-plans-across-liverpool)
