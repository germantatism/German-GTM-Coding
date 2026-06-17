# GRAVYTY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Gravyty
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idsPIbXU1a/iduPWYFwkQ.svg
Nombre merchant: Gravyty

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: GravytyPay Single Rail
Tittle_Pain Point_2: Giving Day Volume Spikes
Tittle_Pain Point_3: No Global Donor Methods
Tittle_Pain Point_4: Recurring Gift Churn
Tittle_Pain Point_5: Fragmented Gift Data

Desc_Pain Point_1: GravytyPay is the sole embedded payment processor for all donation forms across 2,750+ institutions. Any outage or decline rate spike blocks giving for universities, nonprofits, and K-12 organizations with no fallback payment rail available.
Desc_Pain Point_2: Giving days concentrate thousands of donations into 24-hour windows. Processing all transactions through a single payment rail during these spikes increases decline rates precisely when donor intent is highest and campaign momentum is critical.
Desc_Pain Point_3: Gravyty serves alumni and donors globally but offers limited payment methods beyond cards. International alumni in Asia, Europe, and Latin America lack local payment options like Alipay, UPI, SEPA, or Pix to make gifts to their alma maters.
Desc_Pain Point_4: Recurring monthly and annual gifts are core to nonprofit revenue. When a donor's card expires or soft-declines, there is no automated cascade to retry via an alternate processor, silently churning recurring donors without notification or recovery.
Desc_Pain Point_5: Gift data must sync to Raiser's Edge, Salesforce, Slate, and other CRMs via separate integrations. Without centralized payment orchestration, reconciling donations across platforms creates manual work for advancement offices managing millions in gifts.

SLIDE 1: PSP TOPOLOGY

PSP_1: GravytyPay (embedded)
PSP_2: Stripe (infrastructure)
PSP_3: CRM Integrations (Salesforce, RE NXT)
PSP_4: Importacular (data transfer)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: UPI
Local_M_4: SEPA Direct Debit
Local_M_5: Pix
Local_M_6: iDEAL
Local_M_7: PayPal
Local_M_8: Apple Pay
Local_M_9: Google Pay
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every donation to the best performing acquirer by card BIN, donor country, and gift amount. With 2,750+ institutions processing giving day campaigns and recurring gifts, a 3% auth uplift recovers thousands of donations that would otherwise fail at checkout.
Desc_Yuno_Cap2: When a donor's card declines during a giving day or recurring gift renewal, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed donations, directly preventing the silent recurring donor churn that erodes nonprofit revenue.
Desc_Yuno_Cap3: Unlocks the payment methods Gravyty's global alumni base needs: Alipay and WeChat Pay for Chinese alumni (350K+ Chinese students graduate from US universities annually), UPI for Indian alumni, SEPA DD for European donors, Pix for Brazilian alumni. One API, 1,000+ payment methods, zero engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard consolidating GravytyPay donations, recurring gifts, giving day campaigns, and peer-to-peer fundraising into one view. Real-time auth rate monitoring across every payment rail, centralized reconciliation replacing manual CRM syncing, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gravyty at a glance:**
- Founded: 2016 (Gravyty AI); merged with Graduway December 2021; merged with Ivy.ai and Ocelot March 2025
- CEO: Daniel Cohen (previously CEO of Graduway)
- Founder: Adam Martel
- Headquarters: United Kingdom (global operations in US, Canada, and Israel)
- US office: Newton, Massachusetts
- Additional offices: Boston, Seattle, Tel Aviv, London
- Employees: 150+ globally (post-merger with Ivy.ai and Ocelot)
- Total funding: $23.8M+ across 5 rounds from 12 investors
- Key investors: K1 Investment Management ($21M), Launchpad Venture Group, Stage 1 Ventures, Venture Capital Fund of New England
- Customers: 2,750+ institutions worldwide (higher education, K-12, nonprofits, healthcare)
- Products: Raise (AI fundraiser enablement), Advance (giving day + online giving platform), Graduway (alumni community), Ivy & Ocelot (AI virtual assistants for enrollment/engagement), Gratavid (personalized video)
- Notable clients: Susan G. Komen, Guiding Eyes for the Blind, and 2,750+ colleges/universities
- CRM integrations: Salesforce, Raiser's Edge NXT, Slate, Ellucian, Team Dynamix
- Recognition: Inc. 5000 List of America's Fastest-Growing Private Companies (2025)
- QuickGive: ultra-fast mobile checkout (10 seconds or less, no login required)

**Confirmed PSPs / payment methods:**
- GravytyPay: embedded payment processing (no external gateways)
- Stripe: likely underlying infrastructure (attending Stripe Sessions)
- Credit/debit cards: accepted on all donation forms
- Recurring gifts: supported for monthly/annual donations
- Matching gifts: integrated via Double the Donation / 360MatchPro
- Donor advised funds: supported
- No digital wallets detected (no Apple Pay, Google Pay)
- No international local payment methods detected
- No PayPal detected

**Payment architecture:**
- GravytyPay embeds payment processing directly into Advance donation forms
- No external gateway required (built-in processing)
- 150+ integrations available for CRM data flow
- Importacular used for data transfer to RE NXT and other non-Salesforce CRMs
- Real-time analytics on giving campaigns

**Key meeting angles:**
1. **2,750+ institutions = massive donation volume**: Every giving day, homecoming, and GivingTuesday campaign processes through a single payment rail; multi-acquirer routing prevents decline spikes
2. **Global alumni base**: Universities have alumni worldwide; Chinese, Indian, and European alumni need local payment methods to donate to US institutions
3. **Recurring gift protection**: Monthly donors are the most valuable nonprofit revenue; failover on recurring charges prevents silent donor churn
4. **GravytyPay is embedded**: The payment processor is built into the platform, making orchestration a natural layer to add without disrupting the giving experience
5. **Post-merger scale**: Three mergers (Graduway, Gratavid, Ivy.ai/Ocelot) created a 2,750+ customer platform; payment infrastructure must match this scale
6. **Giving day peaks**: Concentrated 24-hour campaigns need burst processing capacity with intelligent routing to maintain auth rates during spikes

**Sources:**
- [Gravyty Official Website](https://gravyty.com)
- [Gravyty Products Overview](https://gravyty.com/products/)
- [Gravyty Advance (Giving Day Platform)](https://gravyty.com/advance/)
- [Gravyty Advance Online Donation Forms](https://gravyty.com/blog/advance-online-donation-forms/)
- [Gravyty Fundraising AI](https://gravyty.com/products/fundraising-ai/)
- [Gravyty Raise (AI Donor Engagement)](https://gravyty.com/raise/)
- [Gravyty Nonprofit Fundraising Software](https://gravyty.com/products/nonprofit-fundraising-software/)
- [Gravyty What is Gravyty](https://gravyty.com/blog/what-is-gravyty/)
- [Graduway and Gravyty Merger (K1 Capital)](https://k1.com/graduway-and-gravyty-announce-merger/)
- [Gravyty, Ivy.ai, Ocelot Unite (PRWeb)](https://www.prweb.com/releases/gravyty-ivyai-and-ocelot-unite-to-transform-student-and-alumni-engagement-302397399.html)
- [Gravyty Launches Ivy & Ocelot (PRNewswire)](https://www.prnewswire.com/news-releases/gravyty-launches-ivy--ocelot-higher-educations-most-trusted-ai-assistant-302594268.html)
- [Gravyty Inc. 5000](https://gravyty.com/blog/gravyty-ivy-ai-and-ocelot-inc-5000/)
- [Gravyty Tracxn Profile](https://tracxn.com/d/companies/gravyty/__hmMa-F94Xofb4za3dj1WBBycDJtvgbsyIGEEribSzBY)
- [Gravyty CBInsights](https://www.cbinsights.com/company/gravyty-technologies)
- [Gravyty Crunchbase](https://www.crunchbase.com/organization/gravyty)
- [Gravyty PitchBook Profile](https://pitchbook.com/profiles/company/162967-15)
- [K1 Invests $21M in Gravyty (PrivSource)](https://www.privsource.com/acquisitions/deal/k1-investment-management-invests-21m-in-gravyty-3ASlmG)
- [Gravyty Brandfetch Logo](https://brandfetch.com/graduway.com)
- [Gravyty Raise Review (SmartThoughts)](https://www.smartthoughts.net/post/gravyty-raise-ai-review-associations)
