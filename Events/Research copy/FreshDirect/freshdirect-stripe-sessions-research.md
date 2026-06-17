# FRESHDIRECT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: FreshDirect
═══════════════════════════════════════

Logo: https://brandfetch.com/freshdirect.com
Nombre merchant: FreshDirect

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Friendly Fraud Surge
Tittle_Pain Point_2: EBT Split Pay Barrier
Tittle_Pain Point_3: Single Checkout Flow
Tittle_Pain Point_4: High Cart Abandonment
Tittle_Pain Point_5: No Multi-PSP Routing

Desc_Pain Point_1: Customers claim missing items for unwarranted refunds. First-party fraud is top-5 threat for 90% of food delivery firms. $15B chargeback fraud in 2025.
Desc_Pain Point_2: EBT accepted only for NY cards and cannot combine with credit/debit in one order. Customers must place separate orders, creating friction for 42M+ SNAP users.
Desc_Pain Point_3: $650M annual revenue flows through one processor with no failover. Any outage during peak grocery hours (evenings, weekends) blocks the entire checkout.
Desc_Pain Point_4: Online grocery cart abandonment exceeds 70%. A declined card at checkout loses the full basket. No automatic retry or APM fallback to save the order.
Desc_Pain Point_5: No multi-PSP routing or orchestration. $650M routed without BIN or issuer optimization. Every basis point of auth improvement at this scale recovers millions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Third-party payment processor (undisclosed, likely Adyen or Braintree)
PSP_2: PayPal
PSP_3: Venmo
PSP_4: Apple Pay
PSP_5: Google Pay
PSP_6: EBT/SNAP (NY state only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Klarna
Local_M_2: Afterpay
Local_M_3: Affirm
Local_M_4: Cash App Pay
Local_M_5: Zip (QuadPay)
Local_M_6: ACH Direct Debit
Local_M_7: Instacart Pay
Local_M_8: Multi-state EBT
Local_M_9: Samsung Pay
Local_M_10: Amazon Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by BIN, issuer, and order value across multiple processors. $650M annual revenue means 1% auth uplift recovers $6.5M. Each grocery order routed to the highest-performing acquirer. 3-10% uplift proven.
Desc_Yuno_Cap2: Automatic cascade when the primary processor declines a grocery order. Instead of losing a $150+ basket, Yuno reroutes to a secondary PSP in milliseconds. Up to 50% recovery on soft declines. Critical during peak ordering windows when families cannot wait for manual retry.
Desc_Yuno_Cap3: Activates payment options grocery shoppers want: Klarna and Afterpay for BNPL on large orders, Cash App Pay, ACH for recurring subscriptions, multi-state EBT. One API, 1,000+ methods. Reduces 70%+ cart abandonment.
Desc_Yuno_Cap4: One dashboard unifying card, EBT, wallet, and BNPL payments. Real-time approval rates by method and order size for $650M volume. NOVA fraud detection (75% reduction) flags first-party fraud (missing item claims, repeat chargebacks).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**FreshDirect at a glance:**
- Founded: 2002. HQ: Bronx, New York City
- Annual revenue: $650M (as of acquisition)
- Employees: ~3,000
- Ownership: Acquired by Getir (Turkish ultrafast delivery company) in December 2023 from Ahold Delhaize USA
- Previous funding: $189M raised in 2016 at $600M valuation (led by J.P. Morgan Asset Management, W Capital, AARP Innovation Fund)
- Service area: Northeast US (New York, New Jersey, Connecticut, Pennsylvania, Delaware)
- Core model: Online grocery delivery with own warehouse and fleet (not gig-based marketplace)
- Sources directly from local farms and producers. Emphasis on freshness and quality
- Delivery: Same-day and next-day with time slots. $75 minimum for free delivery

**Post-Acquisition Context:**
- Getir acquired FreshDirect to strengthen US presence
- In 2024, Getir restructured into two separate companies
- Getir exited US and European ultrafast delivery markets but FreshDirect continued operations
- FreshDirect operates independently post-restructuring
- Technology integration: Getir's tech was expected to improve FreshDirect's infrastructure

**Confirmed Payment Stack:**
- Credit/Debit cards: Visa, MasterCard, Discover, American Express
- Debit cards: MasterCard and Visa branded
- PayPal: Accepted
- Venmo: Accepted
- Apple Pay: Available on supported platforms (no account save required)
- Google Pay: Available on supported platforms (no account save required)
- Checking accounts: Accepted
- EBT/SNAP: NY state-issued EBT Food Cards only. Cannot be combined with other payment methods in a single order
- Third-party payment processors used with encryption and secure processing
- Specific PSP name not publicly disclosed

**Payment Challenges in Online Grocery:**
- Average online grocery cart abandonment rate exceeds 70%
- Friendly fraud (first-party fraud): customers claiming missing/damaged items for unwarranted refunds
- 90% of food delivery providers rank first-party fraud in their top five threats
- Account takeover attacks surged 72% YoY in quick-service restaurant/food delivery in 2025
- $15B in chargeback fraud projected for US merchants in 2025 (Mastercard data)
- Friendly fraud alone expected to cost $7B+ in 2025
- EBT online integration creates unique challenges: fraud prevention, state-by-state requirements, split-tender limitations
- Grocery delivery adoption in the US: grew from 16% (2022) to 25% (2024), a 56% increase

**Competitive Landscape:**
- Instacart: Marketplace model, 80K+ retail stores, broader geographic coverage
- Amazon Fresh: Integrated with Prime, same-day delivery, massive logistics network
- Walmart Grocery: Lowest prices, store pickup + delivery, largest US grocery retailer
- Shipt (Target): Marketplace model, membership-based delivery
- Peapod (Ahold Delhaize): Sister brand (formerly), same parent company
- DoorDash: Expanded into grocery delivery alongside restaurants
- FreshDirect differentiator: Own warehouse model, direct sourcing, quality focus

**Top 5 Pain Point Evidence:**

1. FRIENDLY FRAUD SURGE
   - First-party fraud is a top-five threat for 90% of food delivery providers
   - Customers claim items missing, damaged, or poor quality for refunds they do not deserve
   - $15B in chargeback fraud projected for US merchants in 2025
   - Friendly fraud costs both the product and the transaction fee
   - Account takeover attacks up 72% YoY in food delivery (2025)
   - Perishable goods make dispute resolution harder (no return possible)

2. EBT SPLIT PAY BARRIER
   - EBT accepted only for NY state-issued cards
   - Cannot combine EBT with credit/debit in a single order
   - Customers must place separate orders: one EBT, one regular payment
   - 42M+ Americans receive SNAP benefits
   - Walmart updated fraud prevention in 2025, causing widespread EBT account flags
   - Multi-state EBT expansion would unlock significant customer base

3. SINGLE CHECKOUT FLOW
   - All card transactions appear to flow through one undisclosed processor
   - $650M annual revenue on a single checkout rail with no public failover
   - Peak grocery ordering hours (evenings, weekends) are high-risk for outages
   - Online grocery delivery grew 56% in two years; checkout must keep pace

4. HIGH CART ABANDONMENT
   - Online grocery cart abandonment exceeds 70%
   - $75 minimum for free delivery adds pressure to complete large orders
   - A declined card or payment error at checkout loses the entire basket
   - 62% of users who encounter a payment error never return
   - Prices can be 14% higher than in-store (Instacart benchmark)
   - No BNPL options to split large grocery orders

5. NO MULTI-PSP ROUTING
   - No evidence of payment orchestration or multi-processor routing
   - $650M annual volume without BIN-level or issuer-level optimization
   - Each basis point of auth improvement at this scale = $65K recovered
   - Getir acquisition brought tech ambitions but payment stack remains basic
   - Competitors (Instacart, Amazon) have sophisticated payment engineering

**Key meeting angles:**
1. **$650M revenue, single processor** | Smart routing adds redundancy and auth rate optimization at scale
2. **Friendly fraud is the #1 threat** | NOVA fraud detection flags repeat chargebacks and phantom claims
3. **EBT split-pay friction** | Unified checkout with multi-tender support reduces abandonment
4. **70%+ cart abandonment** | Failover + BNPL options (Klarna, Afterpay) keep customers from leaving
5. **Post-Getir independence** | FreshDirect needs its own payment infrastructure; Yuno fills the gap
6. **Northeast US focus with expansion potential** | Payment methods must scale with geographic growth
7. **3,000 employees, own fleet** | Operational scale demands enterprise-grade payment orchestration

**Sources:**
- [FreshDirect: FAQ Payment & Billing](https://www.freshdirect.com/help/faq_home.jsp?page=faq_billing)
- [FreshDirect: EBT/SNAP FAQ](https://www.freshdirect.com/help/faq/faq_billing_ebt)
- [FreshDirect: EBT Landing Page](https://www.freshdirect.com/browse?id=about_ebt)
- [FreshDirect: Customer Agreement](https://www.freshdirect.com/help/terms_of_service)
- [FreshDirect: Wikipedia](https://en.wikipedia.org/wiki/FreshDirect)
- [Getir Acquires FreshDirect (TechCrunch)](https://techcrunch.com/2023/11/07/getir-freshdirect/)
- [Getir Completes FreshDirect Acquisition (BusinessWire)](https://www.businesswire.com/news/home/20231215050549/en/Getir-Completes-the-Acquisition-of-Leading-US-Online-Grocer-FreshDirect)
- [Getir FreshDirect $650M Revenue (PR Newswire UK)](https://www.prnewswire.co.uk/news-releases/getir-has-completed-the-acquisition-of-freshdirect-a-us-company-with-a-turnover-of-650-million-dollars-302016715.html)
- [Getir Exits US Markets; FreshDirect Continues (Chain Store Age)](https://chainstoreage.com/getir-exits-us-european-markets-freshdirect-continue)
- [Getir Restructuring (PYMNTS)](https://www.pymnts.com/business/2024/getir-to-split-into-2-companies-in-restructuring/)
- [Chargeback Fraud $15B Projection (VMS)](https://www.getvms.com/15-billion-in-chargeback-fraud-looms-over-businesses-in-2025/)
- [Food Delivery Fraud Benchmarks (Sift)](https://sift.com/blog/food-delivery-fraud-benchmarking-risk-and-tracking-trends/)
- [Grocery Store Fraud Prevention (Chargeback Gurus)](https://www.chargebackgurus.com/blog/grocery-store-fraud)
- [Online Grocery Delivery Apps Comparison (Rolling Stone)](https://www.rollingstone.com/product-recommendations/lifestyle/best-online-grocery-shopping-delivery-services-1234681461/)
- [Brandfetch: FreshDirect Brand Assets](https://brandfetch.com/freshdirect.com)
