# SQUARESPACE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Squarespace
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/57/Squarespace_Logo_2019.svg
Nombre merchant: Squarespace

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Lock-In
Tittle_Pain Point_2: Merchant APM Gap
Tittle_Pain Point_3: Geo-Limited Commerce
Tittle_Pain Point_4: Checkout Abandonment
Tittle_Pain Point_5: Subscription Churn Leak

Desc_Pain Point_1: Squarespace Payments is a Stripe white-label. 100% of card volume routes through one acquirer with no failover. Stripe decline = lost sale for every merchant, no alternative path.
Desc_Pain Point_2: No Pix, no OXXO, no UPI, no GCash for merchants. 27% of revenue is international but zero local APMs in LATAM, APAC, or Africa. Only cards, PayPal, BNPL, and iDEAL.
Desc_Pain Point_3: Squarespace Payments only available in US, UK, and Canada. Merchants in 200+ other countries connect Stripe directly with limited APMs and an uneven experience.
Desc_Pain Point_4: International shoppers hit card declines from cross-border flags and SCA failures in Europe. Each failed checkout is lost GMV the merchant and Squarespace never recover.
Desc_Pain Point_5: 92% subscription revenue, 5.3M subscriptions. Failed renewals have no multi-acquirer retry. Even 1% churn from payment failures erodes millions in annual revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Squarespace Payments)
PSP_2: Stripe (direct connect)
PSP_3: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: UPI
Local_M_4: GCash
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: PSE
Local_M_8: Nequi
Local_M_9: SPEI
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing breaking the single-Stripe dependency. Each payment routed to the best acquirer by BIN, issuer, and market. With 5.3M+ subscriptions and $1.1B+ revenue, a 3% auth uplift recovers $30M+ annually.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Yuno reroutes to the next best acquirer in milliseconds, recovering failed renewals and merchant checkouts. Up to 50% recovery on soft declines, reducing involuntary churn on the 92% subscription model.
Desc_Yuno_Cap3: Activates local APMs for merchants worldwide: Pix in Brazil, OXXO in Mexico, UPI in India, GCash in Philippines, BLIK in Poland, PSE in Colombia, Konbini in Japan. One API, 1,000+ methods. No per-market engineering.
Desc_Yuno_Cap4: One dashboard replacing Stripe-only settlement. Real-time approval monitoring, centralized reconciliation for merchant payouts and platform subscriptions, anomaly detection via NOVA. 75% reduction in payment ops complexity.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Squarespace at a glance:**
- 5.3M+ unique subscriptions, ~3M live websites, 200+ countries and territories
- Revenue: $1.1B+ (2025 estimate), $1.32B annualized run rate (March 2026)
- 92% subscription revenue, 8% commerce/other. ARPUS: ~$228 (up 8-10% YoY)
- 70% annual plans, 30% monthly plans
- Went private Oct 2024: acquired by Permira for $7.2B all-cash
- Founder/CEO Anthony Casalena remains largest shareholder
- International revenue: ~27% (2025), targeting 30% by end of 2026
- 17% market share among simple website builders

**Confirmed PSPs:**
- Stripe: primary acquirer, powers both "Squarespace Payments" (white-label) and direct Stripe connect
- PayPal: secondary processor (PayPal Business + Venmo)
- Square: in-person POS integration (Tap to Pay on iPhone/Android)
- No payment orchestrator detected
- Squarespace Payments = Stripe white-label (same 2.9% + $0.30 fee structure)

**Payment Methods Currently Accepted (Merchant Side):**
- Cards: Visa, Mastercard, Amex, Discover, JCB, Diners Club, UnionPay
- Wallets: Apple Pay, PayPal, Venmo
- BNPL: Afterpay/Clearpay, Klarna
- Bank: ACH (US only), SEPA (Europe), iDEAL (Europe)
- In-person: Square POS, Tap to Pay
- No local APMs for LATAM, APAC, Africa, or Middle East

**Squarespace Payments Availability:**
- US, UK, Canada only (as of April 2026)
- Merchants in all other countries must connect Stripe directly
- Rolling out to more countries "soon" per Squarespace documentation

**Top Markets:**
- United States: 76.9% of Squarespace stores (286,350), 58.8% of website traffic
- United Kingdom: 6.7% of stores (25,057), 7.8% of traffic
- Australia: 5.1% of stores (19,176), 6.0% of traffic
- Canada: 3.5% of stores (13,021), 5.7% of traffic
- France: 1.8% of traffic
- International: 27% of revenue, growing toward 30%

**Payment Issues Documented:**
- Cross-border card declines common for international shoppers
- SCA authentication failures in EEA countries cause checkout drops
- Merchants report postal code mismatches when customers travel internationally
- No multi-acquirer failover: Stripe decline = terminal failure
- Subscription payment failures have dedicated troubleshooting guide
- Forum complaints about Stripe being removed as direct option in favor of Squarespace Payments

**Key Meeting Angles:**
1. **Platform-level impact**: Yuno would improve payments for millions of Squarespace merchants simultaneously
2. **Permira PE ownership**: Private equity focuses on margin improvement. Multi-acquirer routing directly improves net revenue
3. **International growth mandate**: Targeting 30% non-US revenue by 2026 requires local APMs in new markets
4. **White-label opportunity**: Squarespace already white-labels Stripe. Yuno orchestration could sit behind the same Squarespace Payments brand
5. **Subscription economics**: 92% subscription model means every failed renewal compounds. Failover protects the entire revenue base
6. **Merchant enablement**: Adding Pix, OXXO, UPI to Squarespace stores unlocks new buyer segments for merchants, increasing GMV and platform fees

**Sources:**
- [Squarespace: Connect a Payment Processor](https://support.squarespace.com/hc/en-us/articles/235161188-Connect-a-payment-processor)
- [Squarespace: Accepted Payment Methods](https://support.squarespace.com/hc/en-us/articles/206541017-What-payment-methods-can-I-accept-with-Squarespace-Commerce)
- [Squarespace: Getting Started with Squarespace Payments](https://support.squarespace.com/hc/en-us/articles/19848492736269-Getting-started-with-Squarespace-Payments)
- [Squarespace: Payments Availability](https://support.squarespace.com/hc/en-us/articles/33482360045069-Squarespace-Payments-availability)
- [Squarespace: Supported Countries and Currencies](https://support.squarespace.com/hc/en-us/articles/205811248-Supported-countries-and-currencies-for-Squarespace-Commerce)
- [Squarespace: Stripe FAQ](https://support.squarespace.com/hc/en-us/articles/205811418-Stripe-FAQ)
- [Squarespace: Tips for International Merchants](https://support.squarespace.com/hc/en-us/articles/206540837-Tips-for-merchants-outside-the-US)
- [Squarespace: Troubleshooting Checkout Issues](https://support.squarespace.com/hc/en-us/articles/205815238-Troubleshooting-checkout-issues)
- [Squarespace: Failed Customer Payments](https://support.squarespace.com/hc/en-us/articles/218953057-Failed-customer-payments)
- [Permira Completes Acquisition of Squarespace](https://www.squarespace.com/press-releases/2024/10/17/permira-completes-acquisition-of-squarespace)
- [TechCrunch: Permira Squarespace Acquisition](https://techcrunch.com/2024/10/17/permira-completes-squarespace-acquisition-after-upping-bid-to-7-2b/)
- [Backlinko: Squarespace Subscriber and Revenue Statistics 2026](https://backlinko.com/squarespace-users)
- [WiserReview: Squarespace Statistics 2026](https://wiserreview.com/blog/squarespace-statistics/)
- [Colorlib: Squarespace Statistics 2026](https://colorlib.com/wp/squarespace-statistics/)
- [SimilarWeb: squarespace.com Traffic](https://www.similarweb.com/website/squarespace.com/)
- [SparkPlugin: Squarespace Payments vs Stripe](https://www.sparkplugin.com/blog/squarespace-payments-vs-stripe)
