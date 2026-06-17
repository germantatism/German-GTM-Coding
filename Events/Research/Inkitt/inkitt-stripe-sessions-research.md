# INKITT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Inkitt
=======================================

Logo: https://images.seeklogo.com/logo-png/48/1/inkitt-logo-png_seeklogo-483171.png
Nombre merchant: Inkitt

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: IAP Fee Dependency
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: Zero Local APMs
Tittle_Pain Point_4: Payout Fragmentation
Tittle_Pain Point_5: Chargeback Exposure

Desc_Pain Point_1: Galatea runs almost entirely on Apple/Google IAP, surrendering 15 to 30% per transaction. With ~$24M annual app revenue, $3.6M to $7.2M goes to platform fees every year.
Desc_Pain Point_2: Trustpilot reviews report failed charges and users unable to complete purchases. International card declines block conversions across 33M users in 100+ countries.
Desc_Pain Point_3: 33M users globally, yet checkout only accepts cards and PayPal. No Pix, UPI, GCash, BLIK, or any local wallet. Emerging markets are conversion dead zones.
Desc_Pain Point_4: Stripe handles author subscriptions, Tipalti handles royalties, Apple/Google handle consumer billing. Three separate financial streams with no unified view.
Desc_Pain Point_5: Trustpilot flooded with disputed charges, users reporting inability to cancel, unauthorized renewals. High chargeback rates increase processing costs and risk.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple App Store
PSP_2: Google Play
PSP_3: Stripe
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: GCash
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: OXXO
Local_M_7: DANA
Local_M_8: OVO
Local_M_9: Konbini
Local_M_10: iDEAL

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Galatea subscription through the highest performing acquirer per card BIN, issuer, and market. With $24M+ app revenue and 33M users in 100+ countries, even 3% auth uplift recovers $720K+ annually. Web checkout bypasses IAP fees entirely.
Desc_Yuno_Cap2: When Stripe declines a subscription charge, Yuno cascades to alternative acquirers in milliseconds. Up to 50% recovery on failed transactions. NOVA AI re-engages churned readers via WhatsApp/phone, recovering up to 75%.
Desc_Yuno_Cap3: Activate Pix in Brazil, UPI in India, GCash in Philippines, BLIK in Poland, Konbini in Japan, iDEAL in Netherlands. One API, 1,000+ methods. Converts the 70%+ of users in markets where cards are not the default.
Desc_Yuno_Cap4: One dashboard unifying Stripe (author subs), Apple IAP, Google Play, and PayPal into a single view. Real time approval monitoring, centralized reconciliation, millisecond anomaly detection. Replaces three separate payout and billing systems.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Inkitt at a glance:**
- 33M users globally, 100+ countries
- Estimated ~$24M annual app revenue ($2M/month, May 2025 estimate)
- Revenue doubled YoY as of February 2024
- Total funding: $117M across 6 rounds (latest: $37M Series C, Feb 2024)
- Post money valuation: ~$400M
- Products: Inkitt (self publishing platform), Galatea (immersive reading app), Galatea TV (video)
- CEO: Ali Albazaz (Founder)
- VP of Engineering: Pavel Murnikov
- CFO: Jeffrey Nichols
- CMO: Rebecca Sobel
- Founded in Berlin (2013), HQ moved to San Francisco (2022)
- 11M+ app downloads across platforms, ~750K downloads/month
- Galatea is 11th most bestseller generating publisher worldwide

**Confirmed PSPs:**
- Apple App Store: primary consumer billing (iOS IAP)
- Google Play: primary consumer billing (Android IAP)
- Stripe: author subscription payments (confirmed in help center and Facebook community)
- PayPal: accepted for web checkout (confirmed in terms of use)
- Tipalti: author royalty payouts (confirmed in help center)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, HQ in San Francisco)
  Currently offer: Visa/MC via Stripe, PayPal, Apple Pay (via IAP), Google Pay (via IAP)
  Missing: ACH, Cash App Pay, Venmo (outside IAP)
  Web checkout limited to cards and PayPal. Direct web billing could bypass 15 to 30% IAP fees.

MARKET 2: Philippines (large romance/fiction reader base)
  Currently offer: Visa/MC via Stripe (web), Apple/Google IAP
  Missing: GCash, Maya, GrabPay
  Credit card penetration ~6%. Without mobile wallets, vast majority cannot pay for Galatea on web.

MARKET 3: India (large English reading market)
  Currently offer: Visa/MC via Stripe (web), Apple/Google IAP
  Missing: UPI, RuPay, Paytm, PhonePe
  75%+ of Indian digital payments use UPI. Massive untapped fiction reading audience.

MARKET 4: Brazil (growing LATAM market for digital reading)
  Currently offer: Visa/MC via Stripe (web), Apple/Google IAP
  Missing: Pix, Boleto
  Pix handles 70%+ of Brazilian digital payments. Without it, web conversion is minimal.

MARKET 5: Germany (Inkitt's founding country, strong reading culture)
  Currently offer: Visa/MC via Stripe (web), PayPal, Apple/Google IAP
  Missing: SEPA Direct Debit, Sofort, Giropay
  ~35% card penetration. SEPA DD is standard for German subscription billing.

**Payment issues documented:**
- Trustpilot reviews report Galatea charging $69.99 without delivering service
- Users describe deceptive billing: displayed as $4.99/month but charged $48.99/year at checkout
- Multiple reports of inability to cancel subscriptions
- Users report unauthorized charges continuing after cancellation
- No prorated refunds offered; customers resort to credit card disputes

**Key meeting angles:**
1. **IAP fee arbitrage** | Galatea is heavily app store dependent. Web checkout with local APMs bypasses 15 to 30% fees on ~$24M revenue
2. **33M users, zero local APMs** | Massive global base with only cards and PayPal. Local methods could unlock emerging markets
3. **Chargeback crisis** | Trustpilot is full of billing disputes. Smart routing and better UX reduce chargebacks
4. **Revenue doubling** | Fast growth = need for scalable payment infrastructure before it breaks
5. **Payout unification** | Stripe + Tipalti + Apple + Google = four separate financial systems
6. **Competitor precedent** | Scribd uses 4 PSPs (Stripe, Adyen, Braintree, EBANX). Wattpad uses multi PSP. Galatea is behind
7. **Berlin roots, global ambitions** | Founded in Germany with strong European presence; SEPA/iDEAL would capture EU readers

**Sources:**
- [Inkitt $37M Series C (TechCrunch)](https://techcrunch.com/2024/02/26/inkitt-ai-publishing-37-million/)
- [Inkitt Revenue Data (Growjo)](https://growjo.com/company/Inkitt)
- [Inkitt Crunchbase Profile](https://www.crunchbase.com/organization/inkitt)
- [Galatea Royalty Payments via Tipalti](https://inkitt.zendesk.com/hc/en-us/articles/12756836931090-Galatea-Royalty-Payments-through-Tipalti)
- [Inkitt Author Subscription Payouts](https://inkitt.zendesk.com/hc/en-us/articles/12234449953938-Managing-My-Author-Subscription-Payouts)
- [Inkitt Author Subscription Terms](https://www.inkitt.com/author-subscriptions-terms)
- [Galatea Trustpilot Reviews](https://www.trustpilot.com/review/getgalatea.com)
- [Inkitt Trustpilot Reviews](https://www.trustpilot.com/review/www.inkitt.com)
- [Galatea Terms of Use](https://galatea.com/terms)
- [Inkitt Leadership (The Org)](https://theorg.com/org/inkitt/teams/leadership-team)
- [Inkitt Facebook: Stripe Question](https://www.facebook.com/groups/webnovelfanpage/posts/1690345321746672/)
- [Galatea App Store](https://apps.apple.com/us/app/galatea-books-audiobooks/id1380362212)
- [Galatea Google Play](https://play.google.com/store/apps/details?id=com.colt)
- [SimilarWeb: Galatea App Stats](https://www.similarweb.com/app/google-play/com.colt/statistics/)
- [Inkitt Logo (Seeklogo)](https://seeklogo.com/vector-logo/483171/inkitt)
