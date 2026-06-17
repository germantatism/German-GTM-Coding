# DOCUSIGN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Docusign
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idTPIoZi1S/idpkMVnDOi.svg
Nombre merchant: Docusign

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 6-Gateway Fragmentation
Tittle_Pain Point_2: Card-Heavy Checkout Bias
Tittle_Pain Point_3: Cross-Border Latency
Tittle_Pain Point_4: No Routing or Failover
Tittle_Pain Point_5: Renewal Billing Friction

Desc_Pain Point_1: Six gateways (Stripe, Braintree, Cybersource, Authorize.net, Elavon, Zuora) run independently. Own API, fees, and reporting. No unified view across 1M+ customers.
Desc_Pain Point_2: ACH is USD-only, SEPA is EUR-only. No Pix, UPI, Boleto, or BLIK. Agreements stall when signers in emerging markets cannot pay at the moment of signing.
Desc_Pain Point_3: APAC users face cross-border latency. Authorize.net is US-centric. International signers face higher fees and lower approval rates on cross-border cards.
Desc_Pain Point_4: Six gateways, zero orchestration. If Stripe declines an agreement payment, no cascade to Braintree or Cybersource. Signer sees a failure, deal stalls.
Desc_Pain Point_5: Community reports renewal charges on expired cards, failed payments not communicated, cancellation requests not honored. $350M IAM ARR at risk from billing friction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (payment gateway)
PSP_2: Braintree (payment gateway)
PSP_3: Cybersource (payment gateway)
PSP_4: Authorize.net (payment gateway)
PSP_5: Elavon (payment gateway)
PSP_6: Zuora (subscription billing gateway)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: Boleto
Local_M_4: BLIK
Local_M_5: SPEI
Local_M_6: iDEAL
Local_M_7: Bancontact
Local_M_8: KakaoPay
Local_M_9: GrabPay
Local_M_10: M-Pesa

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, geography, and cost across Stripe, Braintree, Cybersource, Elavon, and Authorize.net simultaneously. With $3.2B revenue and 1M+ customers globally, routing each agreement payment to the best acquirer per market delivers 3-10% auth uplift.
Desc_Yuno_Cap2: Automatic cascade when the primary gateway declines a payment in an agreement. Instead of showing a failure that stalls the deal, Yuno retries through the next best processor in milliseconds. Up to 50% recovery turns declines into signed, paid agreements.
Desc_Yuno_Cap3: Activates methods Docusign's global signers need: Pix in Brazil, UPI in India, SPEI in Mexico, iDEAL in Netherlands, BLIK in Poland, Bancontact in Belgium, KakaoPay in Korea, M-Pesa in Africa. One API, 1,000+ methods. Pay at the moment of signing, anywhere.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Braintree, Cybersource, Authorize.net, Elavon, and Zuora. Real-time approval monitoring per country, centralized reconciliation across all agreement payments, and NOVA fraud detection (75% reduction) protecting 1B+ users worldwide.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Docusign at a glance:**
- Founded: 2003. HQ: San Francisco, California
- Public: NASDAQ: DOCU
- CEO: Allan Thygesen
- Revenue: $3.22B (FY2026 guidance), up 8% YoY. FY2025: $2.977B
- Q3 FY2026 revenue: $818.4M, up 8% YoY. Subscription revenue: $801M, up 9% YoY
- IAM ARR: $350M+ (FY2026 Q4 earnings disclosure)
- IAM customers: 25,000+
- Total customers: 1M+, with 1B+ users globally
- E-signature market share: ~55-67% (dominant global leader)
- Products: eSignature, Intelligent Agreement Management (IAM), CLM, Notary, ID Verification, Navigator, Maestro
- Key partners: Microsoft, Salesforce, Oracle, SAP
- Notable customers: Walmart, T-Mobile, Unilever, Bank of America, Morgan Stanley, Salesforce
- Geographic distribution: 80% US, 5% Canada, 4.5% UK, remainder global
- Enterprise focus: Expanding IAM into large enterprise segment in 2026

**Confirmed Payment Stack:**
- Stripe: Primary payment gateway for Docusign Payments
- Braintree: Payment gateway (PayPal-owned, supports PayPal/Venmo)
- Cybersource: Payment gateway (Visa-owned)
- Authorize.net: Payment gateway (more US-centric)
- Elavon: Payment gateway (US Bancorp subsidiary)
- Zuora: Subscription billing gateway
- Credit/Debit cards: Visa, Mastercard, Amex, Discover
- ACH: Bank transfer (USD only)
- SEPA: Bank transfer (EUR only)
- Apple Pay: Supported
- Google Pay: Supported (not in all regions)
- PayPal: Via Braintree gateway
- No payment orchestrator detected
- No cross-gateway failover or routing
- 1-2% processing fee on top of gateway rates

**Payment Method Gaps (Evidence):**
- ACH limited to USD only; no multi-currency bank transfers
- SEPA limited to EUR only; no broader European local methods
- No Pix, Boleto for Brazil
- No UPI for India
- No BLIK, iDEAL, Bancontact for European markets
- No M-Pesa for Africa
- No SPEI/OXXO for Mexico
- Authorize.net is US-centric with limited international support
- APAC faces cross-border latency issues
- Google Pay not available in all regions
- Local gateway partnerships (e.g., Alipay) require custom API configurations
- Community complaints about failed renewal payments and billing errors
- No automatic retry or cascade between the 6 supported gateways

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (80% of customers)
  Accepted: Visa/MC/Amex/Discover, ACH, Apple Pay, Google Pay, PayPal
  Missing: Venmo (direct), Cash App Pay
  Note: Best coverage, but no failover between Stripe, Braintree, Cybersource, Authorize.net, Elavon

MARKET 2: Europe (significant enterprise base)
  Accepted: Visa/MC, SEPA (EUR only), Apple Pay, PayPal (via Braintree)
  Missing: iDEAL (Netherlands), BLIK (Poland), Bancontact (Belgium), GiroPay, MB Way, Sofort
  Note: SEPA covers basic EUR transfers but local methods critical for agreement completion

MARKET 3: Latin America (growing e-signature adoption)
  Accepted: Visa/MC (cross-border)
  Missing: Pix, Boleto, OXXO, SPEI, PSE, Nequi
  Note: Pix handles 70%+ of Brazilian digital payments. Agreements stall when signers cannot pay locally.

MARKET 4: Asia Pacific (expansion market, latency issues)
  Accepted: Visa/MC (cross-border), Apple Pay
  Missing: UPI, Alipay, WeChat Pay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: Cross-border latency already an issue. Adding local payment methods reduces friction and improves conversion.

MARKET 5: Middle East / Africa
  Accepted: Visa/MC (cross-border)
  Missing: M-Pesa, Fawry, STC Pay, mada, MTN Mobile Money
  Note: Mobile money dominates Sub-Saharan Africa. Agreements requiring payment cannot close without local methods.

**Key meeting angles:**
1. **$3.2B revenue, 6 gateways, zero orchestration** | Stripe, Braintree, Cybersource, Authorize.net, Elavon, and Zuora all run independently
2. **Payment at the moment of signing** | Docusign's core value prop is closing agreements instantly. A declined payment breaks that promise
3. **1B+ users, card-heavy checkout** | ACH is USD-only, SEPA is EUR-only. Most of the world has no local payment option at signing
4. **IAM is the growth engine** | $350M ARR on IAM platform. Payment friction in agreements directly impacts expansion revenue
5. **55-67% e-signature market share** | Dominant position means every payment failure affects the global standard for digital agreements
6. **Enterprise push in 2026** | IAM targeting large enterprise. Complex B2B payments need wire, local methods, and multi-currency support
7. **APAC latency + payment gaps** | Cross-border performance issues compounded by missing local payment methods in highest-growth regions

**Sources:**
- [Docusign: Payments Product Page](https://www.docusign.com/products/payments)
- [Docusign: Payments Blog](https://www.docusign.com/blog/docusignpayments)
- [Docusign: Supported Payment Gateways](https://support.docusign.com/s/document-item?language=en_US&bundleId=juu1573854950452&topicId=oph1573854895655.html)
- [Docusign: Managing Payment Gateways](https://support.docusign.com/en/guides/managing-payment-gateways)
- [Docusign: Payment Fields FAQ](https://support.docusign.com/s/articles/DocuSign-Payments-FAQ?language=en_US)
- [Docusign: Billing FAQ](https://support.docusign.com/s/articles/DocuSign-Billing-FAQ?language=en_US)
- [Docusign: Stripe Integration](https://www.docusign.com/integrations/stripe)
- [Docusign: IAM Platform Overview](https://www.docusign.com/blog/docusign-iam-overview-intelligent-agreement-management)
- [Docusign: IAM Pricing](https://ecom.docusign.com/plans-and-pricing/iam)
- [Docusign Community: Cancel Auto-Renewal Billing Issue](https://community.docusign.com/esignature-111/urgent-cancel-auto-renewal-and-stop-billing-issue-22985)
- [Docusign Community: Billing Error](https://community.docusign.com/esignature-111/billing-error-4589)
- [Cybersource: DocuSign Partnership](https://www.cybersource.com/en-us/why-cybersource/partners/partner-marketplace/business-operations/docusign.html)
- [eSignGlobal: DocuSign Supported Gateways](https://www.esignglobal.com/blog/docusign-payments-supported-gateways-stripe-paypal)
- [Docusign: Q3 FY2026 Results](https://investor.docusign.com/investors/press-releases/press-release-details/2025/Docusign-Announces-Third-Quarter-Fiscal-2026-Financial-Results/default.aspx)
- [MacroTrends: Docusign Revenue](https://www.macrotrends.net/stocks/charts/DOCU/docusign/revenue)
- [CRN Asia: Docusign Enterprise IAM Strategy](https://www.crnasia.com/news/2026/artificial-intelligence/docusign-eager-to-target-enterprise-customers-in-next-phase)
- [6Sense: DocuSign Market Share](https://6sense.com/tech/digital-signatures/docusign-market-share)
- [Brandfetch: Docusign Logo](https://brandfetch.com/docusign.com)
