# MINDBODY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Mindbody
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idN7yHLkqr/id2mYij2MI.svg
Nombre merchant: Mindbody

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: 100-Country Scale Gap
Tittle_Pain Point_3: LATAM/APAC APM Gaps
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: Post-Merger Complexity

Desc_Pain Point_1: Stripe powers Mindbody Payments in US/Canada, Paysafe handles UK/Europe (since 2006), and region-specific processors cover APAC/UAE. Three separate PSP stacks with no unified routing or real-time optimization layer.
Desc_Pain Point_2: 40,000+ businesses across 100+ countries process payments through Mindbody. Each merchant's auth rate, decline pattern, and retry logic is managed by whichever regional PSP serves that market, with no centralized visibility.
Desc_Pain Point_3: Stripe integration offers BECS in Australia, SEPA/iDEAL in Europe, and Alipay in Asia. But no Pix in Brazil, no OXXO in Mexico, no UPI in India, no BLIK in Poland. Key growth markets lack local payment rails.
Desc_Pain Point_4: US-headquartered platform processing payments for merchants in 100+ countries. Studios and consumers in emerging markets absorb cross-border interchange markup on class bookings and membership charges.
Desc_Pain Point_5: Playlist + EGYM merger creates a $7.5B entity with 88,000+ ClassPass venues, 33,000+ EGYM locations, and 40,000+ Mindbody businesses. Consolidating payment stacks across three brands is a multi-year infrastructure challenge.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (US, Canada, expanding)
PSP_2: Paysafe (UK, Europe)
PSP_3: Apple Pay
PSP_4: Google Pay
PSP_5: Klarna (BNPL)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: UPI
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: Konbini
Local_M_8: Mada
Local_M_9: Mercado Pago
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every class booking, membership charge, and ClassPass transaction to the best performing acquirer per card BIN, country, and issuer. With $800M+ combined revenue and 100K+ venues, a 3-10% auth uplift recovers tens of millions annually.
Desc_Yuno_Cap2: When Stripe declines a membership renewal in the US or Paysafe fails in the UK, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges across all three brands in the Playlist portfolio.
Desc_Yuno_Cap3: Extends beyond BECS, SEPA, iDEAL, and Alipay to the local methods Mindbody's 100-country footprint demands: Pix in Brazil, OXXO/SPEI in Mexico, UPI in India, BLIK in Poland, Konbini in Japan. One API, 1,000+ payment methods, zero engineering sprints.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe, Paysafe, and regional processors across Mindbody, ClassPass, and EGYM into one view. Real-time auth rate monitoring per brand and market, centralized reconciliation, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Mindbody at a glance:**
- Founded: 2001 in San Luis Obispo, CA
- CEO: Fritz Lanman (CEO & Co-Founder of Playlist, parent company)
- Parent company: Playlist (parent brand of Mindbody, Booker, ClassPass)
- Recent merger: Playlist + EGYM merged March 2026, creating $7.5B combined entity
- Investment: $785M new equity from Affinity Partners, Vista Equity Partners, Temasek, L Catterton
- Combined revenue: $800M+ net revenue in 2025 (Playlist + EGYM)
- Mindbody merchants: 40,000+ businesses across 100+ countries
- ClassPass venues: 88,000+ studios globally, millions of subscribers
- EGYM locations: 33,000+ fitness locations, 20,000+ Wellpass employer partners
- Employees: ~2,000+ across the combined entity
- Products: Mindbody (SaaS for studios), Booker (salon software), ClassPass (consumer marketplace), EGYM (gym equipment + corporate wellness)

**Confirmed PSPs:**
- Stripe: powers Mindbody Payments (US, Canada, expanding). Built integrated payments platform on Stripe starting 2020. Uses Stripe Terminal for in-person POS
- Paysafe: payment processing for UK and Europe since 2006. Fully integrated processing solution
- Region-specific processors: for APAC, UAE, and other markets
- Apple Pay, Google Pay: digital wallet options
- Klarna: BNPL offering
- BECS (Australia), SEPA/iDEAL (Europe), Alipay (Asia): local methods via Stripe
- No unified payment orchestrator detected across the multi-PSP stack

**Payment issues documented:**
- BBB complaints: contract enforcement issues, unexpected charges, misleading billing practices
- Trustpilot/SmartCustomer: 1.2/5 stars from 79 reviews; merchants report billing configuration errors
- VAT display issues: incorrect pricing display during checkout (EU compliance risk)
- Disputed payment handling: Mindbody has a dedicated Disputes tool, suggesting significant chargeback volume
- Merchant onboarding: payment setup failures during initial configuration
- PissedConsumer reviews: poor customer service response for billing-related queries

**Top Markets Gap Analysis:**

MARKET 1: United States (largest market)
  Offer: Visa/MC/Amex via Stripe, Apple Pay, Google Pay, Klarna
  Missing: ACH Direct Debit, Cash App Pay, Venmo
  Strong coverage with Stripe Terminal for in-person POS

MARKET 2: United Kingdom (second-largest market)
  Offer: Visa/MC via Paysafe, UK Direct Debit
  Missing: Open Banking, PayByBank
  Paysafe relationship since 2006 provides stability but limits innovation

MARKET 3: Australia (key APAC market)
  Offer: Visa/MC, BECS (via Stripe)
  Missing: PayTo, Afterpay (standalone)
  BECS integration shows Mindbody values local payment methods

MARKET 4: Germany (key European market, EGYM HQ)
  Offer: Visa/MC, SEPA, iDEAL via Stripe/Paysafe
  Missing: Giropay
  EGYM merger makes Germany a critical market for payment consolidation

MARKET 5: Brazil (LATAM growth market)
  Offer: Visa/MC via cross-border acquiring
  Missing: Pix, Boleto Bancario
  ClassPass operates in Brazil but with no local APMs. Pix handles 45B+ transactions/year

**Key meeting angles:**
1. **$7.5B merger payment consolidation**: Three brands (Mindbody, ClassPass, EGYM) on different PSP stacks need unified orchestration. Yuno is the single layer that connects them all
2. **Multi-PSP optimization**: Stripe (US/Canada) + Paysafe (UK/Europe) + regional processors. No dynamic routing between them today
3. **100-country scale**: 40,000+ merchants processing payments globally. Each basis point of auth improvement at this scale is worth millions
4. **ClassPass consumer payments**: Millions of subscribers booking classes across 88,000+ venues. Smart Routing directly increases booking conversion
5. **LATAM/APAC expansion**: ClassPass and Mindbody grow in Brazil, Mexico, India, SEA. Local APMs are table stakes for consumer marketplace conversion
6. **Embedded payments revenue**: Mindbody Payments is a revenue center, not just a cost. Higher auth rates = higher take rate = higher embedded fintech revenue

**Sources:**
- [Stripe: How Mindbody Built Integrated Payments](https://stripe.com/customers/mindbody)
- [Stripe Newsroom: Mindbody Partnership](https://stripe.com/newsroom/news/mindbody)
- [Paysafe: Mindbody Customer Story](https://www.paysafe.com/us-en/customer-stories/mindbody/)
- [Mindbody Payment Processing Tools](https://www.mindbodyonline.com/business/payments)
- [Mindbody Payments FAQ](https://support.mindbodyonline.com/s/article/MINDBODY-Payments-account-FAQ-US-Beta?language=en_US)
- [Mindbody Integrated Payments Countries](https://support.mindbodyonline.com/s/article/In-which-countries-does-MINDBODY-offer-integrated-payments?language=en_US)
- [Playlist + EGYM Merger Announcement](https://www.prnewswire.com/news-releases/playlist-and-egym-announce-agreement-to-merge-and-785-million-in-new-equity-investments-bringing-together-global-leaders-in-fitness-and-wellness-technology-302662191.html)
- [Playlist + EGYM Merger Complete](https://www.prnewswire.com/news-releases/playlist-and-egym-complete-merger-to-power-the-worlds-most-comprehensive-fitness-and-wellness-operating-system-302729745.html)
- [TechCrunch: ClassPass Mindbody EGYM $7.5B Merger](https://techcrunch.com/2026/03/31/the-company-behind-classpass-and-mindbody-just-got-a-lot-bigger-with-a-7-5b-merger/)
- [Athletech News: Merger Details](https://athletechnews.com/classpass-mindbody-playlist-egym-merger-7-5-billion-deal/)
- [Mindbody BBB Complaints](https://www.bbb.org/us/ca/san-luis-obispo/profile/computer-software-developers/mindbody-inc-1236-5002899/complaints)
- [Mindbody Processing Rates](https://support.mindbodyonline.com/s/article/What-are-my-MINDBODY-Payments-processing-rates-US-Beta?language=en_US)
- [Brandfetch: Mindbody Logo](https://brandfetch.com/mindbodyonline.com)
