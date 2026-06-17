# EVENTBRITE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: EVENTBRITE
=======================================

Logo: https://brandfetch.com/eventbrite.com
Nombre merchant: EVENTBRITE

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi PSP No Orchestration
Tittle_Pain Point_2: Cross Border Ticket Drops
Tittle_Pain Point_3: Limited APM at Checkout
Tittle_Pain Point_4: High Fee Organizer Churn
Tittle_Pain Point_5: Payout Delay Cash Crunch

Desc_Pain Point_1: Eventbrite processes $3B+ in annual gross ticket sales through a fragmented stack of Stripe (US/CA/UK/AU), Adyen (authorization and chargebacks), Braintree (chargebacks), Auth.net (authorization), and PayPal (global fallback). Each PSP operates independently with no routing logic between them. A declined card on Stripe does not cascade to Adyen. There is no intelligent transaction optimization across 258 million annual tickets.
Desc_Pain Point_2: Eventbrite hosts 4.6 million events globally but Eventbrite Payment Processing (EPP) only supports organizers with banks in the US, Canada, UK, and Australia. An event organizer in Germany, Brazil, or Japan must use PayPal as the sole processing option. Attendees buying cross-border tickets process through a single acquirer path with no BIN-level routing, resulting in higher decline rates on international ticket purchases.
Desc_Pain Point_3: Eventbrite checkout accepts Visa, Mastercard, Amex, Apple Pay, and Google Pay globally. But attendees in the Netherlands expect iDEAL (70%+ of Dutch ecommerce). Brazilian fans expect Pix. German buyers expect SEPA Direct Debit or Giropay. Mexican attendees expect OXXO. Zero local alternative payment methods are available at Eventbrite checkout, causing abandonment in every non-US market.
Desc_Pain Point_4: Eventbrite charges 3.7% + $1.79 per paid ticket plus 2.9% payment processing, totaling over 6% per transaction. Fees have increased 11 times since 2007. Organizers are migrating to TicketSpice, TixFox, and Humanitix. Payment cost optimization through smart routing and local acquiring could reduce processing fees, helping Eventbrite retain organizers or improve margins post acquisition.
Desc_Pain Point_5: Eventbrite disburses payouts four days after an event concludes, plus additional bank transfer time. Organizers managing multi-day festivals or recurring events face cash flow gaps. With no unified payment orchestration, settlement reconciliation across Stripe, Adyen, Braintree, and PayPal happens system by system, adding operational overhead and delaying fund availability.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (EPP primary: US, CA, UK, AU)
PSP_2: Adyen (authorization and chargeback processing)
PSP_3: Braintree (chargeback batch processing)
PSP_4: Auth.net (payment authorization)
PSP_5: PayPal (global fallback for non-EPP markets)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: Pix (Brazil)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: OXXO (Mexico)
Local_M_5: Bancontact (Belgium)
Local_M_6: Klarna (EU/US BNPL)
Local_M_7: Boleto (Brazil)
Local_M_8: Giropay (Germany)
Local_M_9: Mercado Pago (LATAM)
Local_M_10: Mada (Saudi Arabia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover Cascade Retries
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Unified Payment Orchestration

Desc_Yuno_Cap1: Route every ticket payment to the optimal acquirer by card BIN, currency, and buyer country in real time. With $3B+ in annual gross ticket sales across 258 million tickets, even a 2% authorization uplift recovers tens of millions in ticket revenue. Smart Routing selects between Stripe, Adyen, and Braintree per transaction instead of static PSP assignment by organizer country. Each recovered decline is a ticket sold and an attendee at the event.
Desc_Yuno_Cap2: When Stripe declines a card or Adyen returns a soft decline, Yuno cascades to the next best processor in milliseconds. A fan buying a $75 concert ticket who hits a payment decline will abandon checkout and the seat goes empty. With Yuno, the transaction retries through an alternative acquirer before the buyer sees a failure. Across 258M annual tickets, failover alone can recover millions in otherwise lost sales.
Desc_Yuno_Cap3: One API activates iDEAL for Dutch attendees, Pix and Boleto for Brazil, SEPA and Giropay for Germany, OXXO for Mexico, Bancontact for Belgium, Klarna for BNPL, Mada for Saudi Arabia, and Mercado Pago for LATAM. Yuno connects 1,000+ local payment methods across 40+ countries. Eventbrite's 4.6M events worldwide get instant local payment access, reducing checkout abandonment in every non-US market.
Desc_Yuno_Cap4: Replace Eventbrite's fragmented stack (Stripe for EPP, Adyen for authorization, Braintree for chargebacks, Auth.net for auth, PayPal as fallback) with a single orchestration layer. Centralized settlement across all PSPs, unified fraud scoring, consolidated chargeback management, and one integration that scales from a Brooklyn comedy show to a Sao Paulo music festival. Real time dashboards across $3B+ in annual ticket volume instead of five disconnected systems.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**EVENTBRITE at a glance:**
- Founded: 2006 in San Francisco by Kevin Hartz, Julia Hartz, and Renaud Visage
- Headquarters: San Francisco, California
- CEO: Julia Hartz (until Bending Spoons acquisition)
- Revenue: ~$295-310M (FY 2025 guidance); Q4 2024 revenue: $76.5M
- Gross ticket sales: $3.0B+ (FY 2025)
- Paid tickets distributed: 258 million (FY 2025); 83 million paid tickets (FY 2024)
- Events hosted: 4.6 million (FY 2025)
- Total tickets issued: 258 million (FY 2025)
- Employees: ~748-1,244 (sources vary)
- Acquired by Bending Spoons (Italy) for $500M all-cash, closed March 10, 2026
- Previously NYSE: EB (delisted post-acquisition)
- IPO price was $1.76B in 2018; acquired at $500M (71% decline)
- Bending Spoons portfolio: also owns Evernote, WeTransfer, Vimeo, komoot, Meetup

**Bending Spoons post-acquisition plans:**
- AI-driven event creation and messaging
- Secondary ticket market system
- Focus on consumer events vs. business events
- Technology overhaul expected
- Historical pattern: feature cuts, price hikes, product optimization for margins

**Confirmed PSPs and payment partners:**

| Provider | Role | Region/Function |
|----------|------|-----------------|
| Stripe | Primary EPP processor, card verification | US, Canada, UK, Australia |
| Adyen | Payment authorization, chargeback batch processing | Global |
| Braintree | Chargeback batch file processing | Global |
| Auth.net (Authorize.net) | Payment card authorization | Global |
| PayPal | Alternative processing for non-EPP markets, digital wallet | Global |
| Amex | Direct card processing | Global |

**Payment methods accepted at checkout:**
- Visa, Mastercard, American Express
- Apple Pay, Google Pay
- PayPal (where EPP unavailable)
- Offline: Check, invoice, at-the-door
- Tap to Pay (in-person): US, CA, UK, AU only
- No local alternative payment methods (no iDEAL, Pix, SEPA, OXXO, Boleto, Klarna)

**Eventbrite Payment Processing (EPP) availability:**
- Direct EPP only in: United States, Canada, United Kingdom, Australia
- All other countries must use PayPal as sole processing option
- EPP uses Stripe to verify and process payments
- Payment processing fee: 2.9% of total order (on top of service fee)
- Service fee: 3.7% + $1.79 per paid ticket (US)

**Key financial metrics:**
- Q4 2024 paid ticket volume: 21.6M
- Q2 2025 paid ticket volume: 19.7M (declined 7% YoY)
- Revenue declining YoY (Q4 2024: 13% decline)
- $100M convertible note financing raised Q2 2025

**Competitive landscape:**
- Ticketmaster/Live Nation (dominant in large-scale events)
- TicketSpice, TixFox, Humanitix (low-fee alternatives)
- Luma, Partiful (social-first event platforms)
- Swapcard, Whova (conference/B2B events)
- Fee-driven churn is Eventbrite's biggest competitive vulnerability

**Key meeting angles:**
1. **$3B+ GMV at stake** | Eventbrite processes $3B+ in annual gross ticket sales through 5 disconnected PSPs. A single orchestration layer unifies Stripe, Adyen, Braintree, Auth.net, and PayPal under intelligent routing, recovering lost sales and reducing processing costs
2. **Post-acquisition transformation** | Bending Spoons acquired Eventbrite to overhaul technology. Payment orchestration is the highest-ROI infrastructure upgrade: it directly recovers revenue (auth uplift), reduces costs (smart routing to cheapest acquirer), and unlocks new markets (local APMs)
3. **Cross-border ticket sales** | 4.6M events globally but EPP only works in 4 countries. Attendees in 180+ countries buy tickets through limited payment options. Yuno enables local acquiring in every market, reducing cross-border decline rates
4. **APM blind spot** | Zero local payment methods at checkout. Dutch attendees (iDEAL), Brazilians (Pix), Germans (SEPA), and Mexicans (OXXO) are forced to use cards or abandon. Yuno's 1,000+ APMs fill every gap
5. **Fee optimization** | Organizers are churning over 6%+ total fees. Smart routing to the cheapest acquirer per transaction reduces Eventbrite's processing cost, enabling either margin improvement or fee reduction to retain organizers
6. **Unified chargeback management** | Eventbrite currently manages chargebacks separately across Adyen and Braintree batch files. Yuno consolidates dispute management and fraud scoring (NOVA, 75% fraud reduction) under one platform
7. **258M tickets = high transaction volume** | At this scale, even fractional authorization improvements translate to millions in recovered revenue annually

**Sources:**
- [Eventbrite Q4 2024 Earnings (Investor Relations)](https://investor.eventbrite.com/press-releases/press-releases-details/2025/Eventbrite-Reports-Fourth-Quarter-2024-Financial-Results/)
- [Eventbrite Q1 2025 Earnings (BusinessWire)](https://www.businesswire.com/news/home/20250508115428/en/Eventbrite-Reports-First-Quarter-2025-Financial-Results)
- [Eventbrite Q3 2025 Earnings (Investor Relations)](https://investor.eventbrite.com/press-releases/press-releases-details/2025/Eventbrite-Reports-Third-Quarter-2025-Financial-Results/)
- [Eventbrite 10-K Annual Report (StockTitan)](https://www.stocktitan.net/sec-filings/EB/10-k-eventbrite-inc-files-annual-report-1eb4f39d73ae.html)
- [Eventbrite Bending Spoons Acquisition (BusinessWire)](https://www.businesswire.com/news/home/20251202408560/en/Eventbrite-Enters-into-Definitive-Agreement-to-Be-Acquired-by-Bending-Spoons-for-Roughly-$500-Million-to-Accelerate-Eventbrites-Next-Phase-of-Growth)
- [Bending Spoons Finalizes Eventbrite Purchase (TicketNews)](https://www.ticketnews.com/2026/03/bending-spoons-finalizes-purchase-of-eventbrite/)
- [Eventbrite Payment Processing (Help Center)](https://www.eventbrite.com/help/en-us/articles/426093/getting-started-with-eventbrite-payment-processing/)
- [Eventbrite Payment Options Comparison (Help Center)](https://www.eventbrite.com/help/en-us/articles/705340/comparing-payment-processing-options/)
- [Eventbrite PayPal Integration (Help Center)](https://www.eventbrite.com/help/en-us/articles/313895/how-to-use-paypal-for-payment-processing-and-payout/)
- [Eventbrite Merchant Agreement (Help Center)](https://www.eventbrite.com/help/en-us/articles/346993/eventbrite-merchant-agreement/)
- [Eventbrite PCI DSS AOC (PDF)](https://cdn.evbstatic.com/s3-s3/security/eventbrite_latest_service_provider_aoc.pdf)
- [Eventbrite Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/EB/eventbrite/revenue)
- [Eventbrite Revenue (StockAnalysis)](https://stockanalysis.com/stocks/eb/revenue/)
- [Bending Spoons Eventbrite Plans (TechCrunch)](https://techcrunch.com/2025/12/02/bending-spoons-agrees-to-buy-eventbrite-for-500m-to-revive-stalled-brand/)
- [Eventbrite Alternatives (Whova)](https://whova.com/blog/eventbrite-alternatives-competitors/)
- [Eventbrite Logo (Brandfetch)](https://brandfetch.com/eventbrite.com)
