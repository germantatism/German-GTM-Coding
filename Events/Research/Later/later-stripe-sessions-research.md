# LATER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Later
=======================================

Logo: https://companieslogo.com/img/orig/later.png
Nombre merchant: Later

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: India Cards Blocked
Tittle_Pain Point_2: No PayPal Acceptance
Tittle_Pain Point_3: Creator Payout Friction
Tittle_Pain Point_4: Single PSP Dependency
Tittle_Pain Point_5: Global Checkout Gaps

Desc_Pain Point_1: Indian bank regulations block recurring credit card charges for subscriptions. Later's help center confirms India based credit cards cannot process automated monthly billing. India is the world's largest creator economy by volume. Thousands of Indian social media managers and agencies cannot subscribe to Later without manual workarounds.
Desc_Pain Point_2: Later does not accept PayPal, Interac, or bank transfers for subscription payments. Only credit and debit cards (Visa, Mastercard, Amex) are accepted. PayPal has 430M+ active accounts globally. Competitors like Hootsuite and Buffer accept PayPal. This limits Later's addressable market for self serve plans.
Desc_Pain Point_3: Mavely powers $2.4B+ annual GMV and has paid $250M+ to 180,000+ creators. Creator payouts at this scale require multi currency disbursement, local payment rails, and real time settlement. As Later expands creator commerce internationally, payout infrastructure becomes a growth bottleneck without local method coverage.
Desc_Pain Point_4: Later processes all subscription billing through a single payment processor with no backup acquirer or orchestration layer. Failed payments retry automatically over a month, but if all retries fail the account is affected. No cascade to an alternative processor exists when the primary PSP declines.
Desc_Pain Point_5: Later serves 6M+ users globally with enterprise clients like Nike, Unilever, and Southwest Airlines. Yet checkout accepts only cards plus Apple Pay and Google Pay for trials only. No PIX for Brazil, no SEPA for EU, no UPI for India, no iDEAL for Netherlands. International enterprise expansion faces payment friction at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (inferred) PSP_2: Credit/Debit Cards (Visa, Mastercard, Amex) PSP_3: Apple Pay (trials only) PSP_4: Google Pay (trials only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal (Global)
Local_M_2: UPI (India)
Local_M_3: PIX (Brazil)
Local_M_4: SEPA Direct Debit (EU)
Local_M_5: iDEAL (Netherlands)
Local_M_6: BLIK (Poland)
Local_M_7: Interac (Canada)
Local_M_8: Bancontact (Belgium)
Local_M_9: Boleto (Brazil)
Local_M_10: PayPay (Japan)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Starter, Growth, and Enterprise subscription renewal to the optimal acquirer per card BIN, issuer, and market. With 6M+ global users and 100%+ enterprise growth in Q1 2026, even a 1% auth rate improvement protects meaningful ARR. Smart Routing boosts approval rates 3 to 10%.
Desc_Yuno_Cap2: When a card renewal fails, Yuno cascades instantly to an alternative acquirer or payment method before the month long retry window runs out. NOVA AI recovers up to 75% of soft declines in real time. Livelo recovered 50% of failed transactions using this exact failover approach, preventing involuntary churn.
Desc_Yuno_Cap3: Activate UPI for India's massive creator economy, PIX in Brazil, SEPA in EU, PayPal globally, and iDEAL in Netherlands. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months with Yuno. Later could unlock subscribers and creators in 50+ markets where cards alone fail.
Desc_Yuno_Cap4: Replace siloed payment visibility with one real time dashboard across Starter, Growth, Scale, and Enterprise subscriptions plus Mavely creator payouts. Monitor approval rates by region as enterprise business doubles. Millisecond anomaly detection catches payment failures before they cascade into subscriber churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Later at a glance:**
- Founded: 2014 (originally Latergramme, then Later; merged with Mavrck in 2022 under Later brand)
- HQ: 53 State Street, Boston, Massachusetts 02109
- Total Funding: ~$270M over 9 rounds. Key backer: Summit Partners (~$500M deployed across multiple rounds)
- Key Funding: $120M from Summit Partners (Dec 2021), $135M investment + Later acquisition (2022), $250M Mavely acquisition (Jan 2025)
- Employees: ~1,900 (as of Jan 2026)
- Users: 6M+ global users across social media management platform
- GMV: $2.4B+ annual run rate through Mavely creator commerce
- Creator Payouts: $250M+ cumulative to 180,000+ creators
- Enterprise Growth: 100%+ YoY in Q1 2026
- Enterprise Clients: Nike, Southwest Airlines, Wayfair, Unilever, Stanley 1913
- G2 Leader: 5th consecutive year in Influencer Marketing Platforms, Social Media Management, and Social Media Analytics
- Products: Social Media Management (scheduling, analytics, social inbox), Influencer Marketing (creator discovery, campaign management), Creator Commerce (Mavely affiliate platform)

**Confirmed PSPs and Payment Infrastructure:**
- Primary PSP: Stripe (inferred from billing infrastructure patterns). Processes all credit/debit card subscriptions
- Credit/Debit Cards: Visa, Mastercard, American Express accepted globally. Primary payment method
- Apple Pay: Available for new trial starts only. Not available for ongoing subscription billing
- Google Pay: Available for new trial starts only. Not available for ongoing subscription billing
- PayPal: NOT accepted. Explicitly stated in Later's help center
- Interac: NOT accepted. Explicitly stated
- Bank Transfers: NOT accepted. Explicitly stated
- Invoice: Available for Enterprise plans only (custom pricing, contact sales)
- iOS Billing: If subscribed through iOS app, Apple handles transactions
- No payment orchestration platform confirmed (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Pricing Structure:**
- Starter: $25/month ($16.67/month billed annually)
- Growth: $45/month (discount billed annually)
- Scale: $82.50/month billed annually (6 Social Sets, 48 profiles, 4 users)
- Enterprise: Custom pricing (contact sales)
- Extra social sets: $11.25/set, Extra users: $3.75/user

**Payment Issues and Incidents:**
- Indian bank recurring payment block: India based credit cards cannot process recurring subscription payments due to Indian banking regulations. Each payment requires manual authorization, incompatible with Later's automated monthly billing. Confirmed in Later's help center
- Failed payment retry logic: After a failed payment, Later retries automatically several times over a month before account action. No manual retry option during this window
- 3DSecure pop up blocks: Credit cards requiring 3DSecure verification depend on browser pop ups. If pop ups are blocked, payment cannot complete. Mandatory for banks in certain regions
- No PayPal fallback: When a card payment fails, subscribers have no alternative payment method. PayPal, the most common global fallback, is explicitly not accepted
- Apple Pay and Google Pay limited to trials: Digital wallets only work for initial trial signup, not ongoing billing. Subscribers who start via Apple Pay must switch to a credit card

**Key meeting angles:**
1. **6M+ users, cards only checkout** | Later serves 6M+ users globally but accepts only credit and debit cards for ongoing subscriptions. PayPal (430M+ accounts) is explicitly not accepted. Apple Pay and Google Pay work for trials only. Yuno activates 1,000+ APMs including PayPal, UPI, PIX, and SEPA through one integration.
2. **India creator economy locked out** | Indian bank regulations block recurring credit card charges for subscriptions. India has the world's largest creator population. Later cannot bill Indian social media managers and agencies automatically. Yuno enables UPI (350M+ users) and local Indian payment methods, unlocking the entire market.
3. **$2.4B GMV needs multi currency payment rails** | Mavely processes $2.4B+ annual GMV across 180,000+ creators and 1,400+ brands. International creator commerce requires local payout methods per region. Yuno's 1,000+ APM network covers every market where creators and brands transact, enabling cross border settlement.
4. **Enterprise business doubled with zero payment innovation** | Later's enterprise segment grew 100%+ in Q1 2026. Nike, Unilever, Southwest Airlines are scaling creator programs. But the billing stack has not evolved beyond cards. Enterprise procurement often requires SEPA, bank transfers, or local methods. Yuno adds these without engineering overhead.
5. **Creator commerce is a payments business** | Later's Mavely acquisition transformed the company from a scheduling tool into a commerce platform. $250M+ in creator payouts, $2.4B+ in GMV. At this scale, payment routing, approval optimization, and local method coverage become core infrastructure. Yuno provides the payment orchestration layer that commerce platforms require.

**Later Leadership:**
- Scott Sutton: CEO. Joined February 2024 from ZoomInfo. Background in operations, finance, multi stage growth
- Mohsin Hussain: CTO. Appointed April 2026 from LiveRamp
- Jose Segrera: CFO. Appointed September 2024
- Jamie Tischart: Chief Information and Technology Officer. Appointed September 2024
- Justin Withers: Chief Growth Officer. Appointed September 2024
- Lyle Stevens: Co-Founder, transitioned from CEO to Chief Strategy Officer (February 2024)

**Recent corporate developments:**
- April 2026: Q1 2026 enterprise business more than doubled YoY. Named G2 Leader for 5th consecutive year
- April 2026: Mohsin Hussain appointed CTO from LiveRamp
- February 2026: Comprehensive rebrand with new logo, visual identity, and brand voice. Launched at SXSW 2026 with "Made You Look" campaign
- January 2026: $2.4B+ annual GMV run rate and $250M+ cumulative creator payouts (one year post Mavely acquisition)
- January 2025: Acquired Mavely for $250M (funded by Summit Partners). Mavely network: 120,000+ creators, $1B+ annual GMV, 1,400+ brands
- AI performance gains: 70% more creators managed per campaign, 40%+ higher engagement, 30%+ savings in creator fees

**Sources:**
- [Later Enterprise Business Doubles (PRNewswire)](https://www.prnewswire.com/news-releases/later-more-than-doubles-enterprise-business-as-influencer-marketing-becomes-a-performance-channel-302741194.html)
- [Later Acquires Mavely $250M (PRNewswire)](https://www.prnewswire.com/news-releases/later-acquires-mavely-for-250-million-unlocking-new-opportunities-for-marketers-and-creators-to-maximize-their-return-on-social-302341591.html)
- [Later $2.4B GMV Milestone (Later Blog)](https://later.com/blog/later-hits-2-4b-gmv-milestone-250m-in-creator-payouts/)
- [Later Accepted Payment Methods (Help Center)](https://help.later.com/hc/en-us/articles/360042493054-Accepted-Payment-Methods)
- [Later Failed Payments FAQ (Help Center)](https://help.later.com/hc/en-us/articles/4409299610519-Failed-Payments-Troubleshooting-FAQ)
- [Later Pricing (Later)](https://later.com/pricing/)
- [Later Pricing 2026 (SaaSPricePulse)](https://www.saaspricepulse.com/tools/later)
- [Later Pricing Breakdown (SocialRails)](https://socialrails.com/blog/later-pricing)
- [Later Leadership Transition (PRNewswire)](https://www.prnewswire.com/news-releases/later-announces-leadership-transition-names-new-ceo-302060687.html)
- [Later Executive Appointments (PRNewswire)](https://www.prnewswire.com/news-releases/later-announces-three-executive-appointments-to-further-accelerate-business-growth-and-product-development-momentum-302236887.html)
- [Later Mavely Deal ROI (RockWater)](https://wearerockwater.com/later-buys-mavely-valuation-and-deal-roi-analysis/)
- [Later About (Later)](https://later.com/about/)
- [Later Funding (Tracxn)](https://tracxn.com/d/companies/later/__tq11uaY0CNPilkXSGYszTnB0ZryfN2FrHZ15J8gIXBU)
- [Later Logo (BrandFetch)](https://brandfetch.com/later.com)
- [Later Logo (SeekLogo)](https://seeklogo.com/vector-logo/619272/later)
- [Summit Partners Later (Summit)](https://www.summitpartners.com/companies/later)
