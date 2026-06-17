# ADOBE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Adobe
=======================================

Logo: https://companieslogo.com/img/orig/ADBE-fb158b30.png
Nombre merchant: Adobe

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Subscription Decline Churn
Tittle_Pain Point_2: Limited Local Payment Rails
Tittle_Pain Point_3: No Orchestration Layer
Tittle_Pain Point_4: APAC Payment Gap at $3.4B
Tittle_Pain Point_5: PayPal Fallback Fragility

Desc_Pain Point_1: Adobe community forums document persistent subscription billing failures. Users report cards declined across Creative Cloud, Document Cloud, and Experience Cloud with messages like "There is an issue with your payment details." Failed renewals trigger service suspension, driving involuntary churn on $25.2B ARR.
Desc_Pain Point_2: Credit cards accepted in all markets. SEPA Direct Debit available in 8 EU countries only. PayPal in ~24 countries. No PIX, no BLIK, no UPI, no PayPay, no KakaoPay. Regions generating $9.65B in revenue (EMEA + Asia) have minimal local payment method coverage.
Desc_Pain Point_3: No payment orchestration platform confirmed for Adobe's subscription billing. Creative Cloud, Document Cloud, and Experience Cloud appear to run through a single internal billing stack. No smart routing between acquirers, no automatic failover when a processor declines a renewal.
Desc_Pain Point_4: Asia revenue reached $3.36B in FY2025. Markets like Japan, South Korea, India, and Southeast Asia rely on credit cards for Adobe subscriptions. PayPay (70M+ users in Japan), KakaoPay (South Korea), UPI (India) are all absent. High credit card decline rates in these markets cap subscriber growth.
Desc_Pain Point_5: Users report "PayPal service is down, please choose a different payment method" during checkout. When both card and PayPal fail simultaneously, subscribers have no third option. No automatic cascade between payment methods. Each failed renewal risks permanent subscriber loss.

SLIDE 1: PSP TOPOLOGY

PSP_1: Internal Billing Stack PSP_2: Credit/Debit Cards PSP_3: PayPal PSP_4: SEPA Direct Debit (EU)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: BLIK (Poland)
Local_M_3: iDEAL (Netherlands)
Local_M_4: UPI (India)
Local_M_5: PayPay (Japan)
Local_M_6: KakaoPay (South Korea)
Local_M_7: NaverPay (South Korea)
Local_M_8: GrabPay (SE Asia)
Local_M_9: Boleto (Brazil)
Local_M_10: Trustly (Nordics)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Creative Cloud, Document Cloud, and Experience Cloud subscription renewal to the optimal acquirer per card BIN, issuer, and market. With $25.2B ARR and millions of monthly renewals, even a 0.5% auth improvement recovers over $100M in retained subscriptions. Smart Routing boosts approval 3 to 10%.
Desc_Yuno_Cap2: When a card or PayPal renewal fails, Yuno cascades instantly to an alternative acquirer or payment method. NOVA AI recovers up to 75% of soft declines, preventing involuntary churn before the subscriber even notices. Livelo recovered 50% of failed transactions with this exact approach.
Desc_Yuno_Cap3: Activate PIX in Brazil, BLIK in Poland, iDEAL in Netherlands, UPI in India, PayPay in Japan, and KakaoPay in South Korea. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months using Yuno's single connection. Adobe could unlock subscribers in 50+ markets.
Desc_Yuno_Cap4: Replace Adobe's siloed billing infrastructure with one real time dashboard across Creative Cloud, Document Cloud, and Experience Cloud. Centralized approval rate monitoring for Americas ($14.1B), EMEA ($6.3B), and Asia ($3.4B). Millisecond anomaly detection catches renewal failures before they cascade into churn spikes.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Adobe at a glance:**
- NASDAQ: ADBE. Global leader in creative, document, and digital experience software
- FY2025 (ended November 28, 2025) Total Revenue: $23.77B (up 11% YoY, record)
- FY2025 Total ARR (Annualized Recurring Revenue): $25.20B (up 11.5% YoY)
- Q4 FY2025 Revenue: $6.19B (up 10% YoY, record quarter)
- Q1 FY2026 (ended February 27, 2026) Revenue: $6.40B (up 12% YoY, record)
- Q1 FY2026: AI first ARR tripled
- FY2026 Revenue Guidance: $25.9B to $26.1B. Total ARR growth ~10.2% YoY
- FY2025 GAAP EPS: $16.70. Non GAAP EPS: $20.94
- Digital Media FY2025 Revenue: $17.65B (up 11% YoY, 86.86% of total)
- Digital Experience FY2025 Revenue: ~$5.8B to $5.9B
- Revenue by Region FY2025: Americas $14.12B, EMEA $6.29B, Asia $3.36B
- Products: Creative Cloud (Photoshop, Illustrator, Premiere Pro, etc.), Document Cloud (Acrobat, Sign), Experience Cloud, Firefly AI, Adobe Commerce (Magento)

**Confirmed PSPs and Payment Infrastructure:**
- Internal Billing Stack: Adobe processes subscription billing through its own infrastructure. No external payment orchestrator publicly confirmed
- Credit/Debit Cards: Visa, Mastercard, Amex, Discover accepted globally. Primary payment method in all markets
- PayPal: Available in ~24 countries including US, Canada, Mexico, UK, Brazil, South Korea, Singapore, Thailand, Malaysia, Indonesia, Philippines, and major EU countries (Austria, Belgium, Czech Republic, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Poland, Portugal, Spain)
- SEPA Direct Debit: Available in 8 EU countries (Austria, Belgium, France, Germany, Ireland, Italy, Netherlands, Spain). Takes up to 48 hours to process
- Purchase Orders: Available for phone orders of $2,500+ (US only)
- Wire Transfer: Mentioned as available but no country specific details confirmed
- Adobe Commerce (Magento): Separate product. Integrates with Braintree (bundled since 2.4.0), Adyen (plugin), and Adobe Payment Services. Supports Apple Pay, Google Pay, Venmo, ACH, and local methods via these integrations
- No Apple Pay, Google Pay, or BNPL for Adobe subscription billing
- No payment orchestration platform confirmed for subscription billing (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: Americas ($14.12B revenue)
  Accepted: Visa, Mastercard, Amex, Discover, PayPal (US, Canada, Mexico, Brazil)
  Missing: PIX (Brazil, 150M+ users), Boleto (Brazil), Cash App Pay, Venmo, Apple Pay, any BNPL
  Note: Brazil has PayPal but no PIX for subscription billing

REGION: EMEA ($6.29B revenue)
  Accepted: Visa, Mastercard, PayPal (major EU + UK), SEPA Direct Debit (8 countries)
  Missing: BLIK (Poland, even though PayPal is available in Poland), iDEAL (Netherlands, even though SEPA is available), Bancontact (Belgium), MB Way (Portugal), Trustly (Nordics), Open Banking (UK)
  Note: SEPA covers only 8 of 30+ European markets. Major gaps in Eastern Europe and Nordics

REGION: Asia ($3.36B revenue)
  Accepted: Visa, Mastercard, PayPal (South Korea, Singapore, Thailand, Malaysia, Indonesia, Philippines)
  Missing: PayPay (Japan, 70M+ users), LINE Pay (Japan), Rakuten Pay (Japan), KakaoPay (South Korea), NaverPay (South Korea), UPI (India, 350M+ users), GrabPay (SE Asia), DANA (Indonesia), GCash (Philippines)
  Note: Japan, Adobe's largest Asian market, has no local wallet for subscription billing despite PayPay's 70M user base

**Payment Issues and Incidents:**
- "There is an issue with your payment details" error: Persistent subscription billing error. Users report cards and PayPal both failing. Adobe advises updating billing information, but users confirm details are correct. Service suspended during payment resolution
- "Unable to pay using any credit card": Adobe community thread where user reports all credit cards declined for new subscription purchase. Multiple cards from different banks all rejected. No specific error code or reason provided
- "Payment method failed, but card was charged": Users report Adobe charging their card but marking the payment as failed. Subscription remains suspended. Requires manual support intervention to resolve billing discrepancy
- "PayPal service is down, please choose a different payment method": Error appears during checkout even when PayPal is operational. Eliminates the primary fallback for card failures, leaving subscribers with no alternative
- Renewal failures cause involuntary churn: Failed automatic renewals suspend Adobe services (Photoshop, Illustrator, Acrobat, etc.). Creative professionals lose access to tools during active projects. Adobe provides guides for retrying failed payments but no automatic fallback
- No BNPL for subscription billing: Adobe Creative Cloud All Apps costs $59.99/month or $659.88/year. No installment option for annual plans. High annual cost without BNPL creates a barrier for individual creators and SMBs

**Key meeting angles:**
1. **$25.2B ARR at risk from involuntary churn** | Every failed subscription renewal is lost recurring revenue. Adobe community forums show persistent payment failures across cards and PayPal with no automatic fallback. NOVA AI could recover up to 75% of soft declines before the subscriber even sees a suspension notice.
2. **EMEA and Asia generate $9.65B with minimal local APMs** | EMEA ($6.29B) and Asia ($3.36B) combined represent 40.6% of Adobe's revenue. Yet local payment methods are largely absent: no BLIK, no iDEAL standalone, no PayPay, no KakaoPay, no UPI. Yuno activates 1,000+ local methods via one API.
3. **Adobe Commerce knows orchestration, subscription billing does not** | Adobe Commerce (Magento) integrates with Adyen, Braintree, Apple Pay, Google Pay, and local methods for its merchants. But Adobe's own subscription billing stack lacks these same capabilities. The technology Adobe sells to merchants exceeds what it uses internally.
4. **Japan and South Korea: $1B+ markets, zero local wallets** | Japan and South Korea are among Adobe's top Asian revenue markets. PayPay (70M users) and KakaoPay are not accepted for Creative Cloud billing. Subscribers in these markets must use international credit cards, increasing decline rates and churn.
5. **AI first ARR tripled, payment stack stays static** | Q1 FY2026 saw AI first ARR triple. Firefly AI is driving new subscriber acquisition globally. But the payment infrastructure accepting these new subscribers has not evolved. As AI accelerates growth in emerging markets, local payment coverage becomes the growth bottleneck.

**Adobe Leadership:**
- Shantanu Narayen: Chairman and CEO. Leads strategic direction since 2007
- Dan Durn: EVP and CFO. Oversees financial operations and billing infrastructure
- David Wadhwani: President, Digital Media Business. Leads Creative Cloud and Document Cloud
- Anil Chakravarthy: President, Digital Experience Business. Leads Experience Cloud
- Abhay Parasnis: Former EVP and CTO. Departed 2023
- No dedicated VP of Payments or Billing identified in public sources
- Scott Belsky: EVP and Chief Strategy Officer. Oversees product strategy and creator ecosystem

**Recent corporate developments:**
- March 2026: Q1 FY2026 results. Revenue $6.40B (up 12%, record). AI first ARR tripled. Exceeded guidance
- December 2025: Q4 FY2025 results. Revenue $6.19B (up 10%, record). Full year $23.77B. ARR $25.2B
- FY2026 Guidance: Revenue $25.9B to $26.1B. Non GAAP EPS $23.30 to $23.50. ARR growth 10.2%
- FY2025: Digital Media revenue $17.65B (11% growth). Creative Cloud and Document Cloud ARR acceleration
- Adobe Firefly: Generative AI integrated across Creative Cloud. Driving new subscriber acquisition
- Adobe Commerce: Magento platform with Braintree bundled (since 2.4.0) and Adyen plugin integration
- SEPA Direct Debit: Available in 8 EU countries for subscription billing
- PayPal: Available in ~24 countries for subscription billing

**Sources:**
- [Adobe FY2025 Record Revenue (Adobe News)](https://news.adobe.com/news/2025/12/122025-q4earnings)
- [Adobe Q4 FY2025 Earnings (BusinessWire)](https://www.businesswire.com/news/home/20251210150605/en/Adobe-Reports-Record-Q4-and-FY2025-Revenue)
- [Adobe Q1 FY2026 Record Results (BusinessWire)](https://www.businesswire.com/news/home/20260312749997/en/Adobe-Delivers-Record-Q1-Results)
- [Adobe Q4 FY2025 Analysis (Futurum)](https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/)
- [Adobe Revenue by Region (Bullfincher)](https://bullfincher.io/companies/adobe/overview)
- [Adobe Revenue by Segment (Bullfincher)](https://bullfincher.io/companies/adobe/revenue-by-segment)
- [Adobe Creative Cloud Statistics (ElectroIQ)](https://electroiq.com/stats/adobe-creative-cloud-statistics/)
- [Adobe Statistics 2025 (Analyzify)](https://analyzify.com/statsup/adobe)
- [Adobe Online Order Payment FAQ (HelpX)](https://helpx.adobe.com/x-productkb/policy-pricing/adobe-stores-online-order-payment-faq.html)
- [Adobe Update Payment Information (HelpX)](https://helpx.adobe.com/account/individual/billing-and-payments/payment-methods/update-payment-information.html)
- [Adobe SEPA Payments (HelpX)](https://helpx.adobe.com/manage-account/using/buy-with-sepa.html)
- [Adobe Payment Methods for Teams (HelpX)](https://helpx.adobe.com/enterprise/kb/payment-methods-available-for-CCT.html)
- [Adobe Retry Failed Payments (HelpX)](https://helpx.adobe.com/account/individual/billing-and-payments/payment-and-billing-issues/retry-failed-or-missed-payment.html)
- [Adobe Fix Failed Payment (HelpX)](https://helpx.adobe.com/manage-account/kb/video/how-to-fix-a-failed-or-missed-payment-for-your-adobe-subscription.html)
- [Adobe Payment Refused (Community Forum)](https://community.adobe.com/t5/account-payment-plan-discussions/adobe-creative-cloud-payment-refused/m-p/14057664)
- [Adobe Unable to Pay Credit Card (Community Forum)](https://community.adobe.com/t5/account-payment-plan-discussions/unable-to-pay-using-any-credit-card/td-p/13783047)
- [Adobe Payment Details Issue (Community Forum)](https://community.adobe.com/t5/download-install-discussions/quot-there-is-an-issue-with-your-payment-details-quot/td-p/10212682)
- [Adobe Payment Failed but Charged (Community Forum)](https://community.adobe.com/t5/account-payment-plan-discussions/payment-method-failed-but-card-was-charged/m-p/13356373)
- [Buy Adobe with PayPal (ProDesignTools)](https://prodesigntools.com/pay-adobe-with-paypal-not-credit-card.html)
- [Adobe Commerce Payments Overview (Experience League)](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/payments/payments)
- [Adobe Commerce Payment Services (Adobe)](https://business.adobe.com/resources/payment-services.html)
- [Adyen for Adobe Commerce (Adyen)](https://www.adyen.com/partners/adobe-commerce)
- [Adyen Adobe Commerce Plugin (Docs)](https://docs.adyen.com/plugins/adobe-commerce)
- [Braintree for Adobe Commerce (Experience League)](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/payments/braintree)
- [Adobe Licensing Changes 2025 (Licenseware)](https://licenseware.io/adobe-licensing-pricing-changes-comprehensive-analysis-of-2025-updates/)
- [Adobe Logo (CompaniesLogo)](https://companieslogo.com/adobe/logo/)
