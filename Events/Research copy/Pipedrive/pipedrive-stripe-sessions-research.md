# PIPEDRIVE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Pipedrive
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/4/4f/Pipedrive_Logo.svg
Nombre merchant: Pipedrive

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: PayPal Blocked in UK
Tittle_Pain Point_2: Brazil $10K Monthly Cap
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: SEPA Processing Lock
Tittle_Pain Point_5: Limited APAC Coverage

Desc_Pain Point_1: PayPal unavailable for UK customers, a top European market. UK users forced to cards only, with no wallet or bank debit beyond BACS for subscription billing.
Desc_Pain Point_2: Brazil has a $10K USD monthly cap on local card transfers to international companies per federal law. Larger team subs are blocked by regulation with no workaround.
Desc_Pain Point_3: Single processor with no cascade on decline. With 100K+ customers across 179 countries, every failed renewal without failover is permanent involuntary churn.
Desc_Pain Point_4: SEPA takes up to five working days to process, blocking all billing changes. Customers cannot change plans, add seats, or adjust billing while SEPA clears.
Desc_Pain Point_5: Zero local methods for APAC. No UPI, KakaoPay, GrabPay, or LINE Pay. Card-only checkout in Asia's fastest-growing SMB CRM markets blocks self-serve conversions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit/Debit Cards (Visa/MC/Amex/Discover/JCB/Diners)
PSP_2: PayPal (not available in UK)
PSP_3: SEPA DD / BACS / ACH (regional bank debits)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: iDEAL
Local_M_3: UPI
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: KakaoPay
Local_M_7: GrabPay
Local_M_8: LINE Pay
Local_M_9: Bancontact
Local_M_10: SPEI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With $230M+ projected revenue, 100K+ customers across 179 countries, routing each renewal to the best acquirer per market delivers 3-10% auth uplift on global CRM subscriptions.
Desc_Yuno_Cap2: Automatic cascade when the primary processor declines a subscription renewal. Instead of losing the CRM subscriber to involuntary churn, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions retains ARR.
Desc_Yuno_Cap3: Activates methods Pipedrive's global SMB base demands: Pix in Brazil (bypassing the $10K cap), iDEAL in Netherlands, UPI in India, BLIK in Poland, KakaoPay in Korea, GrabPay in SEA, LINE Pay in Japan. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard unifying card processing, PayPal, SEPA DD, BACS, and ACH into a single view. Real-time approval monitoring per country, centralized reconciliation across EUR/GBP/USD billing, and NOVA fraud detection (75% reduction).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Pipedrive at a glance:**
- Founded: 2010 in Tallinn, Estonia by Timo Rein, Urmas Purde, Ragnar Sass, Martin Henk, Martin Tajur. HQ: New York, USA (operational HQ in Tallinn)
- Ownership: Vista Equity Partners (majority stake since November 2020)
- Valuation: ~$1.5B (at Vista acquisition)
- Total funding: $91.2M in VC prior to Vista; Vista deal valued company at $1.5B
- Key investors: Vista Equity Partners (majority), Bessemer Venture Partners, Insight Partners, Atomico, DTCP, Rembrandt Venture Partners
- Revenue: $207M (2024); projected $230-250M for 2025-2026 (10-15% annual growth)
- Growth: From $12M (2016) to $207M (2024), 1,475% growth in 7 years
- Customers: 100,000+ sales teams across 179 countries
- Employees: ~800-952 across 10 offices
- Offices: Tallinn, Tartu, Lisbon, London, Prague, Dublin, Riga, Berlin, New York, Florida
- Products: CRM, Email Marketing, LeadBooster, Web Visitors, Smart Docs, Projects, Campaigns
- Revenue model: Essential ($14/user/mo), Advanced ($39/user/mo), Professional ($49/user/mo), Power ($64/user/mo), Enterprise ($99/user/mo)

**Confirmed Payment Stack:**
- Credit/debit cards: Visa, MasterCard, American Express, Discover, JCB, Diners Club (North America and UK only)
- PayPal: Accepted (except UK)
- SEPA Direct Debit: Euros, European countries (up to 5 working days processing)
- BACS: British pounds, UK only
- ACH: US dollars, United States only
- Local credit/debit cards: Brazil only
- Billing currencies: EUR (Europe/Turkey), GBP (UK), USD (all other locations)
- No payment orchestrator detected
- No multi-processor failover capability
- No Pix, iDEAL, UPI, or other local APMs

**Payment Method Gaps (Evidence):**
- PayPal explicitly unavailable in UK
- Brazil $10,000 USD monthly cap on local card transfers to international companies (federal law)
- SEPA requires up to 5 working days, blocking billing changes during processing
- Diners Club only in North America and UK
- No local APMs for APAC markets (India, Japan, Korea, SEA)
- No local APMs for LATAM beyond Brazilian local cards
- No iDEAL for Netherlands, no Bancontact for Belgium
- Only account administrators with billing access can modify payment methods

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (HQ, largest CRM market)
  Accepted: Visa/MC/Amex/Discover/JCB/Diners, PayPal, ACH
  Missing: Apple Pay, Google Pay, Venmo
  Note: Best coverage with PayPal and ACH. But no failover processor.

MARKET 2: Europe / EMEA (operational HQ in Tallinn, 6 EU offices)
  Accepted: Visa/MC/Amex, PayPal (not UK), SEPA DD, BACS (UK only)
  Missing: iDEAL (Netherlands), Bancontact (Belgium), BLIK (Poland), GiroPay (Germany), Sofort, MB Way
  Note: SEPA DD is good but 5-day lock is friction. PayPal absent in UK is a gap. No iDEAL in Netherlands.

MARKET 3: Brazil / LATAM (local card support shows focus)
  Accepted: Visa/MC, Local credit/debit cards (Brazil only)
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Note: $10K monthly cap on local cards blocks larger teams. Pix bypasses this cap and processes 70%+ of Brazilian digital payments.

MARKET 4: India / South Asia (growing SMB CRM market)
  Accepted: Visa/MC (cross-border)
  Missing: UPI, RuPay, Paytm, NetBanking
  Note: UPI handles 75%+ of Indian digital payments. Zero local methods in a massive SMB market.

MARKET 5: Japan / APAC (CRM growth region)
  Accepted: Visa/MC, JCB
  Missing: Konbini, PayPay, KakaoPay, LINE Pay, GrabPay, PromptPay
  Note: JCB acceptance is positive for Japan, but no local methods for broader APAC. Korea, SEA completely unserved.

**Key meeting angles:**
1. **Vista portfolio optimization** | Vista Equity Partners owns majority. Payment efficiency and auth uplift directly improve portfolio returns and IPO readiness.
2. **PayPal blocked in UK** | One of the largest European CRM markets with no wallet option. BACS is the only non-card alternative.
3. **Brazil $10K cap** | Federal law caps local card payments at $10K/month. Larger Brazilian sales teams literally cannot pay. Pix via orchestration solves this.
4. **100K+ customers in 179 countries** | Global SMB base with limited local methods. Each unlocked method drives self-serve conversions.
5. **SEPA 5-day lock** | Billing changes blocked during SEPA processing. Creates friction during team scaling moments.
6. **CRM market competition** | Salesforce, HubSpot, and Zoho offer broader payment options. Payment flexibility is a competitive differentiator.
7. **$230M+ revenue with growth trajectory** | 10-15% annual growth. Payment optimization directly accelerates the path to profitability and potential IPO.

**Sources:**
- [Pipedrive: Accepted Payment Methods](https://support.pipedrive.com/en/article/what-are-the-accepted-payment-methods-for-pipedrive)
- [Pipedrive: How to Start Paying](https://support.pipedrive.com/en/article/how-can-i-start-paying-for-pipedrive)
- [Pipedrive: Billing Category](https://support.pipedrive.com/en/category/billing)
- [Pipedrive: Brazil Local Card Payments](https://support.pipedrive.com/en/article/paying-for-pipedrive-with-a-local-credit-card-brazil)
- [Pipedrive: Billing Troubleshooting](https://support.pipedrive.com/en/article/billing-troubleshooting)
- [Pipedrive: Update Billing Details](https://support.pipedrive.com/en/article/how-can-i-update-my-billing-details-in-pipedrive)
- [Pipedrive: Pricing](https://www.pipedrive.com/en/pricing)
- [Pipedrive: Vista Equity Partners Investment](https://www.pipedrive.com/en/blog/vista-equity-partners-make-majority-investment-pipedrive)
- [TechCrunch: Pipedrive Vista Investment](https://techcrunch.com/2020/11/12/european-unicorns-are-no-longer-a-pipe-dream/)
- [PitchBook: Vista Pipedrive Deal](https://pitchbook.com/newsletter/vista-to-take-control-of-pipedrive-in-15b-deal)
- [Wikipedia: Pipedrive](https://en.wikipedia.org/wiki/Pipedrive)
- [BoostStash: Pipedrive Revenue 2025](https://www.booststash.com/pipedrive-revenue-2025/)
- [ElectroIQ: Pipedrive Statistics](https://electroiq.com/stats/pipedrive-statistics/)
- [Getlatka: Pipedrive Revenue](https://getlatka.com/companies/pipedrive)
- [Pipedrive Community: Ordering & Payment](https://community.pipedrive.com/discussion/17332/ordering-payment-method)
- [Brandfetch: Pipedrive Logo](https://brandfetch.com/pipedrive.com)
