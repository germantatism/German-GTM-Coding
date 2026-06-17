# EXPEDIA GROUP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Expedia Group
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/EXPE-afb1e2ef.png
Nombre merchant: Expedia Group

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Brand Stacks
Tittle_Pain Point_2: Cross Border Auth Leakage
Tittle_Pain Point_3: Local APM Coverage Gaps
Tittle_Pain Point_4: Single Acquirer Dependency
Tittle_Pain Point_5: Reconciliation Drag

Desc_Pain Point_1: Six brands (Expedia, Hotels.com, Vrbo, Orbitz, Travelocity, Wotif) on one Adyen backend. 500K daily transactions with no per brand routing.
Desc_Pain Point_2: 37% of revenue is international on $119.5B gross bookings. Cross border declines run 15 to 25% higher, leaking millions in lost travel bookings.
Desc_Pain Point_3: Only cards, PayPal, Apple Pay, Google Pay at global checkout. No Pix in Brazil, no UPI in India, no iDEAL in NL. High value bookings lost.
Desc_Pain Point_4: Adyen handles all pay ins and pay outs across every brand and region. Zero failover: any Adyen disruption freezes 500K daily transactions.
Desc_Pain Point_5: Adyen, Affirm, PayPal, and regional BNPL providers. Multi provider settlement across 6 brands, 70+ countries, multiple currencies compounds ops.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen
PSP_2: PayPal
PSP_3: Affirm
PSP_4: Apple Pay / Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: iDEAL
Local_M_4: BLIK
Local_M_5: Konbini
Local_M_6: KakaoPay
Local_M_7: OXXO
Local_M_8: Boleto
Local_M_9: GCash
Local_M_10: PromptPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each of Expedia's 500K daily transactions to the optimal acquirer by card BIN, issuer, currency, and booking value. With $119.5B in gross bookings and 37% international revenue, even 3% auth uplift recovers hundreds of millions in completed travel bookings annually.
Desc_Yuno_Cap2: Eliminate Adyen single acquirer risk across all 6 consumer brands. When Adyen declines or lags, Yuno cascades to the next best processor in milliseconds. Up to 50% recovery on soft declines, protecting high AOV travel bookings ($200+ average).
Desc_Yuno_Cap3: Activate APMs travelers demand: Pix in Brazil, UPI in India, iDEAL in Netherlands, Konbini in Japan, KakaoPay in Korea, OXXO in Mexico. One API, 1,000+ methods across 200+ countries. Deploy per market in weeks, not quarters of engineering work.
Desc_Yuno_Cap4: One dashboard unifying Adyen, PayPal, Affirm, and regional providers across Expedia, Hotels.com, Vrbo, Orbitz, and more. Real time approval monitoring per brand, centralized reconciliation, millisecond anomaly detection. Up to 90% reconciliation reduction.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Expedia Group at a glance:**
- Brands: Expedia, Hotels.com, Vrbo (41.5% of sales), Orbitz, Travelocity, Wotif, ebookers, Hotwire, CarRentals.com
- FY2024 Revenue: $13.6B (up 6.7% YoY). FY2025 Revenue: $14.7B (up 7.6% YoY)
- FY2024 Gross Bookings: $110.9B. FY2025 Gross Bookings: $119.6B
- FY2025 Booked Room Nights: 415.4M
- 500,000+ transactions per day, processing billions in payments and refunds annually
- Revenue split: ~63% US, ~37% international (international growing 15% vs US 4% in Q3 2025)
- B2B segment growing 26% (Q3 2025), expanding to financial institutions and airlines
- CEO: Ariane Gorin. CTO: Ramana Thumu (since Dec 2024). CFO: Scott Schenkel (since Feb 2025)
- VP Global Payments: Jing Yang (leads end to end payments, formerly Amazon international payments)
- Tech and content spend: $3B+ annually, focus on AI, payments, and self service tooling

**Confirmed PSPs:**
- Adyen: primary acquirer and processor for all brands, pay ins and pay outs (Intelligent Money Movement partnership announced 2025)
- PayPal: accepted at checkout across brands
- Affirm: exclusive US BNPL provider across Expedia, Hotels.com, and Vrbo (multi year deal, Jan 2026)
- Apple Pay / Google Pay: digital wallets on mobile
- FPX (Malaysia), online banking (Thailand): select APAC local methods via Adyen
- No payment orchestrator detected
- Jing Yang previously built payments partnerships at Amazon, now leads payments team of unknown size

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~63% of revenue)
  Accepted: Visa/MC/Amex/Discover/Diners, PayPal, Affirm BNPL, Apple Pay, Google Pay
  Missing: Venmo (standalone), Cash App Pay, ACH
  Note: Affirm exclusivity limits BNPL options. Klarna and Afterpay popular but locked out of Expedia US.

MARKET 2: United Kingdom (key international market)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: Open Banking, PayByBank, Klarna
  Note: UK BNPL regulation tightening; Open Banking growing fast for high value travel purchases.

MARKET 3: Germany (major EU market)
  Accepted: Visa/MC, PayPal
  Missing: Sofort, Giropay successor, SEPA Direct Debit for consumer use
  Note: ~35% card penetration in Germany. Travel bookings average $200+, ideal for bank transfer methods.

MARKET 4: Japan (growing APAC market)
  Accepted: Visa/MC, PayPal
  Missing: Konbini, PayPay, Line Pay
  Note: Japan has 70%+ cash preference for transactions. Without convenience store payments, online conversion suffers.

MARKET 5: Brazil (emerging travel market)
  Accepted: Visa/MC, PayPal
  Missing: Pix, Boleto, local installment cards
  Note: Pix processed 6.2B+ transactions in March 2025 alone. Without Pix, Expedia loses to Booking.com and local OTAs in Brazil.

**Payment issues documented:**
- Trustpilot rating: 1.3/5 for Expedia UK, with payment processing failures cited repeatedly
- Users report "payment detail went through to the end stage and then failed to process"
- Random charges taken without booking confirmation; duplicate charges on failed attempts
- "Sorry we weren't able to proceed with your booking" error encourages retry while card was already charged
- Charge reversals take 3 to 5 business days on failed bookings, tying up traveler funds
- 1 incident in last 90 days with median 6 hour 57 minute duration

**Key meeting angles:**
1. **$119.5B bookings, one acquirer** | All gross bookings flow through Adyen with zero failover. Risk is enormous for a travel company where bookings are time sensitive.
2. **International revenue growing 4x faster** | 15% international vs 4% US growth. Payment localization is the key unlock for continued expansion.
3. **Payments leader from Amazon** | Jing Yang built Amazon's international payments. She understands multi PSP orchestration and would be a natural champion.
4. **BNPL fragmentation** | Affirm exclusive in US, but no BNPL in APAC, LATAM, or most of EMEA. Yuno can orchestrate BNPL across regions.
5. **High AOV = high recovery value** | Travel bookings average $200+. Recovering even 3% of declined transactions has outsized revenue impact.
6. **B2B white label growing 26%** | Expedia powers travel for financial institutions and airlines. Those partners need localized payment methods too.
7. **Competitor gap** | Booking Holdings uses multiple PSPs and has deeper local APM coverage in Europe and APAC.

**Sources:**
- [Expedia Group FY2024 Results](https://www.expediagroup.com/investors/news-and-events/financial-releases/news/news-details/2025/Expedia-Group-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx)
- [Expedia Group FY2025 Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/EXPE/expedia/revenue)
- [Expedia Group Q2 2025 Results](https://www.expediagroup.com/investors/news-and-events/financial-releases/news/news-details/2025/Expedia-Group-Reports-Second-Quarter-2025-Results/default.aspx)
- [Expedia Revenue and Usage Statistics (Business of Apps)](https://www.businessofapps.com/data/expedia-statistics/)
- [Expedia Statistics (ElectroIQ)](https://electroiq.com/stats/expedia-statistics/)
- [Expedia Statistics 2026 (HotelAgio)](https://hotelagio.com/expedia-statistics/)
- [Expedia Statistics (ExpandedRamblings)](https://expandedramblings.com/index.php/expedia-statistics-facts/)
- [Adyen x Expedia APAC Payments](https://www.adyen.com/knowledge-hub/expedia-group-the-3-things-you-need-to-know-about-delivering-compelling-local-payment-choices-across-apac)
- [Expedia Payment Overhaul with Adyen (Simply Wall St)](https://simplywall.st/stocks/us/consumer-services/nasdaq-expe/expedia-group/news/expedia-payment-overhaul-with-adyen-and-what-it-could-mean-f)
- [Adyen Intelligent Money Movement](https://www.prnewswire.com/news-releases/adyen-launches-intelligent-money-movement-to-unify-enterprise-payments-liquidity-management-and-payouts-302738084.html)
- [Affirm x Expedia Exclusive BNPL (PYMNTS)](https://www.pymnts.com/bnpl/2026/affirm-becomes-expedia-groups-exclusive-bnpl-provider-in-us/)
- [Affirm x Expedia Partnership (Investors)](https://investors.affirm.com/news-releases/news-release-details/expedia-group-and-affirm-deepen-partnership-us-exclusivity-and/)
- [Jing Yang LinkedIn](https://www.linkedin.com/in/jingy/)
- [Jing Yang at Money20/20 Europe](https://europe.money2020.com/agenda/speakers/jing-yang-s102-95034)
- [Expedia and Travel's New Flight Path (JP Morgan)](https://www.jpmorgan.com/payments/payments-unbound/volume-3/trillion-dollar-question)
- [Expedia Group Leadership](https://www.expediagroup.com/who-we-are/leadership/default.aspx)
- [Expedia Group CTO Appointment](https://www.stocktitan.net/news/EXPE/expedia-group-welcomes-ramana-thumu-as-chief-technology-qj4rtb9uch7x.html)
- [Expedia Group B2B Expansion 2025](https://www.expediagroup.com/investors/news-and-events/financial-releases/news/news-details/2025/EXPEDIA-GROUP-EXPANDS-B2B-PLATFORM-AND-LAUNCHES-GENAI-PARTNERSHIPS-TO-ENHANCE-TRAVEL-DISCOVERY/)
- [Expedia Trustpilot UK Reviews](https://www.trustpilot.com/review/www.expedia.co.uk)
- [Expedia Trustpilot US Reviews](https://www.trustpilot.com/review/www.expedia.com)
- [Expedia Payment Help: Stays](https://www.expedia.com/helpcenter/?product=Stays&productId=lodging&articleId=16355)
- [Expedia Payment Help: Flights](https://www.expedia.com/helpcenter/?product=Flights&productId=flight&articleId=16518)
- [Expedia Brand Assets (Newsroom)](https://www.expedia.com/newsroom/media-assets/)
- [Expedia Wikipedia](https://en.wikipedia.org/wiki/Expedia_Group)
- [SimilarWeb Expedia Traffic](https://www.similarweb.com/website/expedia.com/)
