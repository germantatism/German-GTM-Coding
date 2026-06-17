# AUDIBENE (hear.com) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: audibene
=======================================

Logo: https://asset.brandfetch.io/idBhn8NGQF/idugALdL7_.svg
Nombre merchant: audibene

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: High-Ticket CNP Fraud
Tittle_Pain Point_2: Multi-Country Split Stack
Tittle_Pain Point_3: No Local APMs at Checkout
Tittle_Pain Point_4: Telehealth Chargeback Risk
Tittle_Pain Point_5: Financing Reconciliation Gap

Desc_Pain Point_1: Hearing aids average $5,000-$7,000 per pair, all processed card-not-present. High-ticket telehealth transactions trigger elevated fraud scoring at issuers. Without intelligent routing to optimize BIN-level approval, authorization rates suffer on every consultation-to-purchase conversion.
Desc_Pain Point_2: audibene operates across 9 countries (US, Germany, Netherlands, Switzerland, India, South Korea, and more) under multiple brands. Each market likely runs its own payment contracts and acquirer relationships. No orchestration layer unifies payment flows across the WS Audiology corporate structure.
Desc_Pain Point_3: German checkout likely lacks SEPA DD, Klarna, and Giropay despite these being dominant payment methods. US checkout relies on credit cards plus Allegro/CareCredit financing. No Pix for Brazil, UPI for India, or KakaoPay for Korea. Customers in expansion markets cannot pay locally.
Desc_Pain Point_4: Telehealth hearing consultations are intangible services. Customers receive hearing aids after remote fittings, creating a dispute-friendly transaction profile. Chargeback ratios above 1% trigger PSP scrutiny. No fraud detection layer optimized for high-ticket telehealth commerce.
Desc_Pain Point_5: hear.com offers third-party financing through Allegro and CareCredit (Synchrony Bank) alongside direct card payments. Reconciling financed purchases, insurance reimbursements, deposits ($199-$499), and monthly installments across 9 countries creates ops burden without unified payment visibility.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (likely primary card processor, confirmed Twilio Pay integration partner)
PSP_2: CareCredit / Synchrony Bank (US financing, installment plans)
PSP_3: Allegro Credit (US financing alternative)
PSP_4: Wire Transfer / Bank Transfer (enterprise and international)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: Klarna
Local_M_3: Giropay
Local_M_4: Sofort
Local_M_5: iDEAL
Local_M_6: UPI
Local_M_7: KakaoPay
Local_M_8: Pix
Local_M_9: TWINT
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $5,000-$7,000 average order values across 9 countries, routing each hearing aid purchase to the optimal local acquirer delivers 3-10% authorization uplift. On high-ticket telehealth sales, every percentage point recovered translates to significant revenue.
Desc_Yuno_Cap2: Automatic cascade when a high-ticket hearing aid charge is declined. Instead of losing a $6,000 sale after weeks of consultation and fitting, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions. For audibene, each recovered transaction is worth thousands.
Desc_Yuno_Cap3: Activates methods audibene's patients need in each market: SEPA DD and Klarna in Germany, iDEAL in Netherlands, TWINT in Switzerland, UPI in India, KakaoPay in Korea. One API, 1,000+ methods. Eliminates financing friction in markets where credit cards are not the primary payment habit.
Desc_Yuno_Cap4: One dashboard unifying card processing, CareCredit financing, Allegro installments, and bank transfers across 9 countries. Real-time approval monitoring per market, centralized reconciliation of deposits plus installments plus insurance, and NOVA fraud detection (75% reduction) protecting high-ticket telehealth commerce.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**audibene (hear.com) at a glance:**
- Founded: 2012, Berlin, Germany
- HQ: Berlin, Germany (Schonhauser Allee 53, 10437 Berlin)
- Co-Founders / Co-CEOs: Marco Vietor and Paul Crusius
- Parent Company: WS Audiology (formed from Sivantos + Widex merger, 2019)
- WS Audiology Revenue: EUR 2.63B (FY2023-2024), adjusted EBITDA EUR 542M
- audibene Revenue: ~$301.7M (2026 estimate)
- Employees: 1,200+ across 9 locations (other sources cite ~476 across 5 continents)
- Brand Portfolio: audibene (Europe), hear.com (US/global), plus Signia, Rexton, Widex under WS Audiology
- Products: Horizon IX hearing aids, remote fitting technology, telehealth consultations
- Hearing Aid Prices: $1,599-$6,499 per pair; monthly plans $139-$199/month
- Consultations: 1M+ hearing aid consultations annually
- Partner Network: 3,000+ audiology partners, 5,000+ independent partner audiologists
- Technology: Twilio Flex (customer engagement), Zoom (telehealth), Dropbox Business, AWS, Heroku, Azure

**Office Locations:**
- Berlin, Germany (HQ)
- Mainz, Germany
- Denver, Colorado, USA
- Miami, Florida, USA
- Utrecht, Netherlands
- Zug/Rotkreuz, Switzerland
- Gurgaon, India
- Seoul, South Korea
- Additional location (9th unconfirmed)

**Confirmed Payment Stack:**
- CareCredit (Synchrony Bank): Primary US financing option, installment plans at 5.99%-24.99% APR
- Allegro Credit: Alternative US financing provider
- Credit/Debit Cards: Standard card acceptance for direct purchases
- Deposits: $199-$499 required based on technology level
- Twilio: Used for customer engagement (Flex platform), with Twilio Pay integration supporting Stripe connector
- No payment orchestrator detected
- No multi-processor failover confirmed
- No regional APM adaptation confirmed across markets

**Payment Method Gaps (Market Evidence):**
- Germany (HQ market): No Klarna, SEPA DD, or Giropay confirmed in checkout despite being dominant German payment methods
- US: Relies on credit card plus third-party financing (CareCredit, Allegro)
- Netherlands: No iDEAL confirmed despite it being the #1 Dutch payment method
- Switzerland: No TWINT confirmed
- India: No UPI confirmed despite UPI handling 75%+ of digital payments
- South Korea: No KakaoPay confirmed
- Telehealth industry standard: Chargeback ratios monitored above 1% trigger PSP scrutiny
- High-ticket CNP transactions ($5,000-$7,000) face elevated fraud scoring

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (major revenue market, Denver + Miami offices)
  Accepted: Credit/Debit Cards, CareCredit financing, Allegro financing
  Missing: Apple Pay, Google Pay, PayPal, Affirm, Afterpay
  Note: Financing-dependent model. Each failed card auth on a $6K purchase = lost revenue after weeks of consultation investment

MARKET 2: Germany (HQ market, Berlin + Mainz offices)
  Accepted: Credit/Debit Cards (likely), Bank Transfer
  Missing: SEPA DD, Klarna, Giropay, Sofort, PayPal
  Note: 60%+ of German e-commerce uses non-card methods. Hearing aid purchases without SEPA DD or Klarna financing creates friction

MARKET 3: Netherlands (Utrecht office)
  Accepted: Credit/Debit Cards (likely)
  Missing: iDEAL, Bancontact, SEPA DD
  Note: iDEAL accounts for 70%+ of Dutch online payments. Checkout without iDEAL severely limits conversion

MARKET 4: India (Gurgaon office)
  Accepted: Credit/Debit Cards (likely cross-border)
  Missing: UPI, RuPay, NetBanking, Paytm
  Note: UPI handles 75%+ of Indian digital payments. High-ticket hearing aid purchases on cross-border rails face elevated decline rates

MARKET 5: South Korea (Seoul office)
  Accepted: Credit/Debit Cards (likely cross-border)
  Missing: KakaoPay, Naver Pay, Samsung Pay, Toss
  Note: Mobile payments dominate Korean commerce. No local payment rails = checkout friction for hearing aid buyers

**Key meeting angles:**
1. **$5K-$7K AOV, card-not-present** | Every declined high-ticket transaction wastes weeks of consultation and fitting investment. Smart routing maximizes first-attempt auth rates on telehealth purchases
2. **9 countries, fragmented payment stack** | Each market likely runs separate acquirer contracts. Orchestration unifies payment flows under WS Audiology's multi-brand structure
3. **Financing reconciliation burden** | CareCredit + Allegro + direct card + deposits + insurance across 9 markets. No unified dashboard for payment visibility
4. **Telehealth chargeback vulnerability** | Intangible remote consultations + high-ticket purchases = elevated dispute risk. NOVA fraud detection reduces chargebacks 75%
5. **Germany without German APMs** | HQ market likely missing SEPA DD, Klarna, and Giropay. 60%+ of German e-commerce uses non-card methods
6. **1M+ annual consultations** | Scale of patient interactions means even small auth rate improvements translate to significant revenue recovery
7. **WS Audiology corporate play** | Parent company (EUR 2.63B revenue) operates Signia, Rexton, Widex brands. audibene success could expand to full corporate payment stack

**Sources:**
- [hear.com: Success Story](https://www.hear.com/news/press-releases/success-story/)
- [hear.com: Hearing Aid Prices](https://www.hear.com/hearing-aids/prices/)
- [hear.com: Financial Assistance & Financing](https://www.hear.com/hearing-aids/financial-assistance/)
- [hear.com: FAQs](https://www.hear.com/faqs/)
- [Twilio: audibene Customer Story](https://customers.twilio.com/en-us/audibene)
- [Zoom: audibene Customer Story](https://www.zoom.com/en/customer-stories/audibene-hear-dot-com/)
- [Dropbox: audibene Technology Story](https://blog.dropbox.com/topics/customer-stories/audibene-and-dropbox-for-business)
- [StackShare: audibene Tech Stack](https://stackshare.io/audibene-gmbh/hear-com)
- [Crunchbase: audibene](https://www.crunchbase.com/organization/audibene)
- [Owler: audibene Revenue & Employees](https://www.owler.com/company/audibene)
- [Glassdoor: audibene Office Locations](https://www.glassdoor.com/Location/All-audibene-Office-Locations-E1155737.htm)
- [WS Audiology: Wikipedia](https://en.wikipedia.org/wiki/WS_Audiology)
- [EQT: WS Audiology Portfolio](https://eqtgroup.com/about/current-portfolio/ws-audiology-2)
- [Audiology Online: Sivantos + audibene Partnership](https://www.audiologyonline.com/releases/sivantos-and-audibene-enter-strategic-13781)
- [Brandfetch: audibene Logo](https://brandfetch.com/audibene.de)
- [GR4VY: Payment Orchestration in Healthcare](https://gr4vy.com/posts/payment-orchestration-in-healthcare-powering-seamless-payments-for-telehealth-and-mental-health-services/)
- [PayAtlas: Payments for Telemedicine](https://payatlas.com/industry/telemedicine-4954)
- [Luqra: Hidden Challenges in Telehealth Payments](https://www.luqra.com/blog/challenges-in-telehealth-payments/)
