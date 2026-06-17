# KRISP AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Krisp AI
=======================================

Logo: https://companieslogo.com/img/orig/krisp-ai.png
Nombre merchant: Krisp AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card Decline Retry Gap
Tittle_Pain Point_2: No Local Payment Rails
Tittle_Pain Point_3: Single PSP Dependency
Tittle_Pain Point_4: India Expansion Pay Gap
Tittle_Pain Point_5: Enterprise Invoice Friction

Desc_Pain Point_1: When a recurring payment fails on Stripe, Krisp retries only 3 times over 10 days. If all attempts fail the subscription is cancelled automatically. With $37.7M in revenue and a growing call center AI product, each lost renewal erodes ARR. No failover to an alternative acquirer or payment method exists.
Desc_Pain Point_2: Krisp accepts Visa, Mastercard, Amex, and PayPal globally. No PIX for Brazil, no BLIK for Poland, no UPI for India, no iDEAL for Netherlands. As the platform expands into 80+ language markets with AI Live Interpreter, potential enterprise and pro subscribers in these regions face checkout friction.
Desc_Pain Point_3: Krisp processes all subscription payments through Stripe as its sole PSP. No backup acquirer, no orchestration layer, no automatic cascade when Stripe declines a transaction. A single processor outage or regional decline spike affects the entire subscriber base with no recovery path.
Desc_Pain Point_4: Krisp appointed a Chief Growth Officer to lead India expansion in January 2026. India has 350M+ UPI users, yet Krisp accepts only credit cards and PayPal. Enterprise BPM customers like Movate and Concentrix operate large Indian teams. UPI and local wallets are missing for seat based billing.
Desc_Pain Point_5: Invoice payments are available only for Enterprise plans and require manual coordination with an account executive. Business plan customers at $30 per seat have no invoice option. Call Center AI requires 40+ seats minimum but must pay via credit card, creating procurement friction for large deployments.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe PSP_2: Credit/Debit Cards (Visa, Mastercard, Amex) PSP_3: PayPal PSP_4: Invoice (Enterprise only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: UPI (India)
Local_M_3: BLIK (Poland)
Local_M_4: iDEAL (Netherlands)
Local_M_5: Bancontact (Belgium)
Local_M_6: SEPA Direct Debit (EU)
Local_M_7: PayPay (Japan)
Local_M_8: KakaoPay (South Korea)
Local_M_9: GrabPay (SE Asia)
Local_M_10: Boleto (Brazil)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Pro, Business, and Call Center AI renewal to the optimal acquirer per card BIN, issuer, and market. With $37.7M in revenue and enterprise contracts for 40+ seat deployments, even a 1% auth improvement recovers meaningful ARR. Smart Routing boosts approval rates 3 to 10%.
Desc_Yuno_Cap2: When Stripe declines a card renewal, Yuno cascades instantly to an alternative acquirer or payment method before the 10 day retry window begins. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this same failover approach, preventing involuntary churn.
Desc_Yuno_Cap3: Activate UPI in India for the BPM expansion, PIX in Brazil, BLIK in Poland, iDEAL in Netherlands, and PayPay in Japan. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months with Yuno. Krisp could unlock enterprise subscribers across 80+ language markets it already supports.
Desc_Yuno_Cap4: Replace single PSP visibility with one real time dashboard across Pro, Business, Call Center AI, and Enterprise subscriptions. Monitor approval rates by region as Krisp expands into India and Southeast Asia. Millisecond anomaly detection catches renewal failures before subscriptions cancel automatically after 10 days.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Krisp AI at a glance:**
- Founded: 2017 in Yerevan, Armenia. HQ: 2150 Shattuck Ave, Penthouse 1300, Berkeley, California 94704
- Co-Founders: Davit Baghdasaryan (CEO) and Artavazd Minasyan (CTO)
- Revenue: $37.7M (2025), up from $30M prior year. 343 employees
- Total Funding: $15.5M over 3 rounds. Series A: $9M (Feb 2021, led by RTP Global)
- Key Investors: RTP Global, CM Ventures, S16VC, Storm Ventures, TechNexus Venture Collaborative
- Scale: 200M+ devices deployed, 4T+ minutes of voice processed, 75B+ minutes per month
- Products: AI Meeting Assistant, Call Center AI, AI Voice SDK
- Enterprise Customers: Siemens, Autodesk, Sony, Cisco, Okta, TTEC, Concentrix, Cognizant, Discord, Twilio, RingCentral, Vonage, Zoho, Aircall
- January 2026: Appointed Vimal Nair as Chief Growth Officer to lead India expansion
- April 2026: Strategic partnership with Movate for global CX delivery with AI voice solutions

**Confirmed PSPs and Payment Infrastructure:**
- Stripe: Primary PSP for all credit/debit card subscription billing. Auto renewable subscriptions with 3 retry attempts on days 2, 5, and 10 after a failed payment. Subscription cancelled if all retries fail
- Credit/Debit Cards: Visa, Mastercard, American Express accepted globally
- PayPal: Added December 2020. Initially for Personal Pro plan. Available as upgrade payment option
- Invoice: Available for Enterprise plans only. Requires coordination with account executive
- No payment orchestration platform confirmed (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Pricing Structure:**
- Free Trial: 7 days
- Core: $16/month ($8/month billed annually)
- Advanced: $30/month ($15/month billed annually)
- Call Center Core: Starting $10/agent/month (annual, 40 seat minimum)
- Call Center Advanced: Custom pricing
- Voice AI SDK: Application based (Early Stage and Enterprise tiers)

**Payment Issues and Incidents:**
- Recurring payment declined: Stripe retries 3 times over 10 days (day 2, 5, 10). If all fail, subscription cancelled automatically. No manual retry option during this window
- Single PSP risk: All payments routed through Stripe. No backup processor. Regional Stripe outages or issuer level decline spikes have no fallback
- No local payment methods: Enterprise customers in India (major BPM market) limited to credit cards. UPI with 350M+ users not available. Same gap in Brazil (no PIX), Poland (no BLIK), Netherlands (no iDEAL)
- Invoice friction: Business plan ($30/seat) requires credit card even for large team deployments. Only Enterprise gets invoice option. Creates procurement barriers for mid market deals

**Key meeting angles:**
1. **$37.7M ARR with single PSP risk** | Krisp routes all subscription revenue through Stripe with no backup acquirer. Three retry attempts over 10 days, then automatic cancellation. NOVA AI could recover up to 75% of those soft declines before the subscription is lost. At $37.7M and growing, each percentage point of involuntary churn is material.
2. **India expansion blocked by payment coverage** | Krisp hired a Chief Growth Officer in January 2026 to lead India expansion. The BPM sector is the target. But Indian enterprises and call centers face credit card only checkout. UPI processes 350M+ users. Yuno activates UPI, Paytm, and local wallets via one API integration.
3. **80+ language markets, 2 payment methods** | Krisp AI Live Interpreter supports 80+ languages for real time translation. Yet payment acceptance is limited to cards and PayPal globally. Markets like Brazil, Poland, Japan, and South Korea have dominant local methods that Krisp cannot accept. Yuno connects 1,000+ APMs through a single integration.
4. **Call Center AI needs enterprise grade billing** | Call Center AI requires 40+ seat minimums. Large BPO clients (Concentrix, TTEC, Cognizant) operate globally. Multi currency billing, local payment methods per region, and invoice reconciliation become critical. Yuno provides a unified dashboard across all payment rails.
5. **Voice AI SDK monetization opportunity** | Krisp offers a Voice AI SDK for developers embedding noise cancellation and accent conversion. As SDK partners scale globally, their end users need local payment methods. Yuno as the payment layer enables Krisp to offer embedded payments across all SDK partner markets.

**Krisp AI Leadership:**
- Davit Baghdasaryan: Co-Founder and CEO. Serial entrepreneur, leads company strategy
- Artavazd Minasyan: Co-Founder and CTO. Leads technology and AI development
- Vimal Nair: Chief Growth Officer. Appointed January 2026 to lead India expansion. 20+ years enterprise tech experience
- No dedicated VP of Payments or Billing identified in public sources

**Recent corporate developments:**
- January 2026: Vimal Nair appointed Chief Growth Officer for India expansion
- April 2026: Strategic partnership with Movate for AI powered voice solutions in global CX
- 2025: Revenue reached $37.7M with 343 person team
- 2025: VIVA (Voice Isolation for Voice Agents) launched. Processes audio in under 20ms, boosts accuracy 3.5x, cuts dropped calls ~50%
- 2025: AI Voice Translation v2.0 with synchronous mode, 80+ languages
- Call Center AI platform launched combining noise cancellation, accent conversion, live interpreter, and agent assist

**Sources:**
- [Krisp Revenue $37.7M (GetLatka)](https://getlatka.com/companies/krisp.ai)
- [Krisp About Us (Krisp)](https://krisp.ai/about-us/)
- [Krisp Pricing Plans (Krisp)](https://krisp.ai/pricing/)
- [Krisp Supported Payment Methods (Help)](https://help.krisp.ai/hc/en-us/articles/4404136935314-Supported-payment-methods-at-Krisp)
- [Krisp Recurring Payment Declined (Help)](https://help.krisp.ai/hc/en-us/articles/11384908133404-My-recurring-payment-was-declined-When-will-the-next-attempt-be)
- [Krisp Pay with PayPal Announcement (What's New)](https://whatsnew.krisp.ai/announcements/pay-with-paypal-1)
- [Krisp Subscription Info (Help)](https://help.krisp.ai/hc/en-us/articles/5626527210908-How-Krisp-subscription-works)
- [Krisp Funding (Crunchbase)](https://www.crunchbase.com/organization/krisp-af3e)
- [Krisp Company Profile (Tracxn)](https://tracxn.com/d/companies/krisp-technologies/__rd-xYlpOUB0k7qLEd6Z8tY5DRc_8-Oerl1lBjUa6Wkc)
- [Krisp India Expansion (Krisp Blog)](https://krisp.ai/blog/vimal-nair-as-chief-growth-officer-to-lead-india-expansion/)
- [Krisp Movate Partnership (PRNewswire)](https://www.prnewswire.com/in/news-releases/movate-and-krisp-announce-strategic-partnership-to-transform-global-cx-delivery-with-ai-powered-voice-solutions-302672315.html)
- [Krisp AI Wiki (AIWiki)](https://aiwiki.ai/wiki/krisp_ai)
- [Krisp Contact Center (Krisp)](https://krisp.ai/contact-center/)
- [Krisp Logo (SeekLogo)](https://seeklogo.com/vector-logo/476183/krisp)
- [Krisp Customers (Krisp)](https://krisp.ai/customers/)
