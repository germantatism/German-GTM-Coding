# SDR Research Brief — Fareportal (CheapOair, OneTravel)
*Yuno Payment Orchestrator · Framework v8.0 · 2026-07-23*

## EXECUTIVE SUMMARY
Fareportal is a New York based travel technology company (founder held by Sam Jain, ~3,500 staff, large Gurgaon India center) that runs the online travel agencies CheapOair (US heavy) and OneTravel (India heavy and growing fast), plus Travelong and other brands, selling flights across 500+ airlines. It is a card heavy, multi currency, multi brand OTA with a fragmented consumer pay-in stack (major cards, PayPal, Apple Pay, Affirm BNPL, Accrue Savings) across US, Canada, UK, UAE and India, and no publicly confirmed consumer side acquirer or orchestrator. Notably, Fareportal already orchestrates the supplier side (it contracted Amadeus Outpayce B2B Wallet virtual cards in Jan 2026) and even markets "payment orchestration" as a B2B product, so the Yuno wedge is not "you lack orchestration," it is consolidate and optimize the consumer side acquiring: multi acquirer routing and auth rate uplift on high decline air tickets, local methods for OneTravel's India heavy base, and fewer disputes and chargebacks on a business already facing a class action over charged amounts exceeding the displayed final price.

---

## SECTION 1 — Traffic by Country
**cheapoair.com** ~6.9M visits/mo (down ~2.2% MoM). **onetravel.com** ~1.48M visits/mo (up ~72% MoM, roughly doubled YoY).

| Brand | Rank | Country | Traffic Share | Source |
|-------|------|---------|---------------|--------|
| CheapOair | 1 | United States | 84.73% | [S1] |
| CheapOair | 2 | Canada | 2.48% | [S1] |
| CheapOair | 3 | India | 0.96% | [S1] |
| CheapOair | 4 | Saudi Arabia | 0.79% | [S1] |
| CheapOair | 5 | Argentina | 0.64% | [S1] |
| OneTravel | 1 | India | 45.79% | [S2] |
| OneTravel | 2 | United States | 33.88% | [S2] |
| OneTravel | 3 | Canada | 6.64% | [S2] |
| OneTravel | 4 | Venezuela | 1.67% | [S2] |
| OneTravel | 5 | Germany | 1.13% | [S2] |

Flags: two very different footprints under one owner. CheapOair is US dominant, OneTravel is India dominant (46%) and the fastest growing brand. India, Saudi, Argentina and Venezuela presence = strong emerging market, cross border, local method signal.

---

## SECTION 2 — Legal Entities
| Country | In Top Traffic? | Local Entity? | Cross-Border Risk | Source |
|---------|-----------------|---------------|-------------------|--------|
| USA | Yes (both) | Fareportal Inc (NYC HQ); RSH Travel / WK Travel consumer entities | Home market | [S3] |
| India | Yes (OneTravel #1) | Fare Portal India Pvt Ltd (Gurgaon, est. 2009) | Ops/dev center; consumer billing entity for India buyers not confirmed | [S3][S4] |
| Canada | Yes | CheapOair.ca / OneTravel.ca storefronts (RSH Travel named in QC suit) | CAD storefront | [S5] |
| UK / UAE | Regional domains referenced | Not verified | ⚠️ Potential cross-border operation, no local entity confirmed | [S3] |

Other offices: New York, Las Vegas, Canada, India, UK, Mexico, Ukraine. Brands: CheapOair, OneTravel, Travelong, FareBuzz, Fareportal Media Group, others.
> MANUAL: verify per-market billing entity on each storefront's T&Cs.

---

## SECTION 3 — Payment Stack

**3A. Consumer pay-in methods (confirmed / indicated, NOT processors)**
| Method | Evidence | Source |
|--------|----------|--------|
| Major cards (Visa, Mastercard, Amex, UnionPay on OneTravel) | Checkout snippets / press | [S6][S7] |
| PayPal | Press / snippet | [S6][S7] |
| Apple Pay (since 2016), Android Pay | Press release | [S6] |
| Affirm BNPL (3/6/12 mo), both CheapOair and OneTravel | Fareportal press + official BNPL pages | [S8][S7] |
| Accrue Savings "Save Now, Buy Later" | Fareportal/Accrue press (Jun 2023) | [S9] |

Note: Sezzle and Zip appear only on those providers' own store-directory / virtual-card pages, NOT confirmed as native CheapOair integrations. Do not assert them.

**3B. Processor / Orchestrator**
- Consumer side PSP / acquirer: **No public evidence found** (all Fareportal domains return 403 bot protection, so source-level checkout inspection was blocked).
- Supplier side: **Amadeus Outpayce B2B Wallet** (virtual card supplier settlement) contracted Jan 2026. [S10]
- Fareportal markets its own "payment orchestration" inside Fareportal Enterprise Solutions (B2B product, Apr 2026). [S11]
- Consumer side orchestrator: **No public evidence found.** This is the wedge: supplier settlement and B2B are handled, consumer acquiring is unconfirmed and likely fragmented.
> MANUAL — DevTools on cheapoair.com / onetravel.com checkout (bypass 403 via real browser): test card 4111 1111 1111 1111 | 02/30 | 123 to reveal the acquirer/PSP and 3DS flow.

---

## SECTION 4 — APMs (verified)

**4A. Confirmed / strongly indicated**
| Market | Methods | Source |
|--------|---------|--------|
| US (both brands) | Cards, PayPal, Apple Pay, Android Pay, Affirm, Accrue Savings | [S6][S7][S8][S9] |
| US OneTravel | + UnionPay, Amex named in checkout snippet | [S7] |

**4B. Unverified markets (do NOT treat as gaps)**
| Market | Attempted? | Reason | Popular local APMs (opportunity) |
|--------|-----------|--------|----------------------------------|
| India (OneTravel #1 market) | Yes | Domain 403 | UPI, RuPay, netbanking, Paytm/PhonePe wallets |
| Canada (.ca) | Yes | Domain 403 | Interac |
| UK / UAE | Yes | Not reachable | Open banking (UK); Mada, local cards (UAE) |

> "Not verified" is not "not available." MANUAL: VPN + real browser checkout walk-through per market before any APM claim. The India angle for OneTravel is the strongest opportunity but must be verified live first.

---

## SECTION 5 — Payment Complaints
| Issue | Platform | Volume / Note | Source |
|-------|----------|---------------|--------|
| Charged MORE than displayed "Final Total Price" (class action) | Quebec Superior Court | Filed 2020, class from Mar 2017, ~$20M punitive sought; names CheapOair.ca/.com + OneTravel.ca/.com | [S5] |
| Refund delays, unexpected/unexplained fees | BBB (Fareportal Inc) | 1,421 complaints in 3 yrs, 809 in last 12 mo; refunds stated 60 to 90 days; "post-ticketing services fee" | [S12] |
| Duplicate charges leading to chargebacks | BBB / news | Documented duplicate charge resolved via bank chargeback | [S12] |
| Overcharging, double charges, refund friction | OneTravel PissedConsumer | 1.6 stars, ~18% would recommend | [S13] |

Analysis: the recurring pattern (price-at-payment mismatch, duplicate charges, chargebacks, slow refunds) maps directly to Yuno's reconciliation, single view of the transaction across acquirers/BNPL, dispute tooling, and consistent charge/settle logic. High chargeback volume also pressures acquirer relationships, where multi acquirer routing helps.

---

## SECTION 6 — Expansion & Corporate
| # | Date | Development | Source |
|---|------|-------------|--------|
| 1 | Apr 24 2025 | Frontier Airlines NDC API integration | [S14] |
| 2 | Jan 21 2026 | Amadeus partnership; adopts Outpayce B2B Wallet (virtual card supplier settlement) | [S10] |
| 3 | Apr 30 2026 | Launches Fareportal Enterprise Solutions (B2B), markets "payment orchestration" | [S11] |
| 4 | May 26 2026 | Expands Sabre partnership; "agentic AI orchestrating end-to-end shopping" + NDC | [S15] |

Leadership: no named CFO / Head of Payments found. Yuvraj Datta (Chief Supply and Revenue Officer) and Nipun Joshi (AVP Product and AI Experiences) are the payments-adjacent execs quoted. Founder/Exec Chairman: Sam Jain. Large in-house India engineering base implies a build-vs-buy bias to pre-empt.

---

## SECTION 7 — Payment News
| # | Date | Headline | Relevance | Source |
|---|------|----------|-----------|--------|
| 1 | Jan 2026 | Fareportal adopts Amadeus Outpayce B2B Wallet | Supplier-side already orchestrated; frames a "consolidate consumer side too" pitch | [S10] |
| 2 | Apr 2026 | Fareportal Enterprise Solutions markets "payment orchestration" | They speak the orchestration language; position Yuno as the consumer-acquiring engine | [S11] |

---

## SECTION 8 — Checkout Audit
| Dimension | Finding |
|-----------|---------|
| Checkout type | Hosted OTA flight checkout across cheapoair.com / onetravel.com + .ca; 403 blocked source inspection |
| Guest checkout | Not verified (403) |
| Methods shown | Cards, PayPal, Apple Pay, Affirm, Accrue (US); India/UK/UAE not verified |
| 3DS | Not verified |
| Multi-currency | Yes (USD, CAD storefronts confirmed via class action) |
| Biggest UX pain | Charged amount exceeding displayed final price (litigated), plus post-ticketing fees |

> MANUAL: walk CheapOair (US) and OneTravel (India) checkouts in a real browser.

---

## SECTION 9 — PCI DSS
No public PCI or security page found. [INFERENCE] Given card-heavy air ticketing at 6.9M monthly visits, Fareportal is almost certainly PCI DSS Level 1, but this is undocumented. Yuno can reduce PCI scope via a portable vault and network tokenization. [S3]

---

## SECTION 10 — Strategic Insights

**Insight #1: Supplier side is orchestrated, consumer side is not.**
Evidence: S10 (Amadeus Outpayce), S11 (they market orchestration), S3 (no consumer PSP/orchestrator confirmed). Pain: consumer acquiring likely stitched per market/brand with no unified routing. Yuno value: one consumer-side orchestration layer across brands, markets and methods, with multi acquirer routing and +7% auth uplift. Best case: NYT / Newfold (already orchestrate, optimized the rest). Angle: "You orchestrate supplier settlement with Outpayce and sell orchestration to partners. The open question is whether the consumer checkout, across CheapOair and OneTravel and every currency, is routed to the best acquirer per market."

**Insight #2: OneTravel is 46% India and growing ~72% MoM, on a likely card-centric checkout.**
Evidence: S2 (India traffic), S4 (Gurgaon entity). Pain: India buyers strongly prefer UPI, RuPay, netbanking and wallets; a card/PayPal-only flow leaks conversion. Yuno value: add local methods and local acquiring in weeks. Best case: inDrive (10 markets in under 8 months). Angle: bring OneTravel's fastest growing market a local, high-approval way to pay (verify current India methods live first).

**Insight #3: Litigated price-at-payment mismatch + heavy dispute volume.**
Evidence: S5 (class action), S12 (1,421 BBB complaints). Pain: charge/settle inconsistency, duplicate charges, chargebacks, 60 to 90 day refunds erode trust and acquirer standing. Yuno value: unified reconciliation, single transaction view across acquirers and BNPL, dispute tooling, consistent charge logic. Angle: cut the duplicate-charge and reconciliation issues showing up in complaints and litigation.

**Insight #4: Multi-currency, multi-brand, multi-BNPL with no consumer orchestrator.**
Evidence: S3, S6 to S9. Pain: Affirm + Accrue + PayPal + cards across US/CA/UK/UAE/India, no single control plane. Yuno value: unify acquiring, APMs, BNPL and fraud under one API and one reconciliation layer. Angle: consolidate the stack before adding more markets and methods.

---

## SECTION 11 — Pipeline (OTA peers)
| Company | HQ | Size | Orchestration flag | Source |
|---------|-----|------|--------------------|--------|
| Expedia Group | Seattle US | ~$13B rev | In-house payments platform | [S16] |
| Booking Holdings | Norwalk US | ~$150B cap | In-house | [S16] |
| Trip.com Group | Shanghai | ~$30B cap | APAC scale | [S16] |
| eDreams ODIGEO | Barcelona | Mid-cap public | Orchestration-adjacent | [S16] |
| Kiwi.com | Brno CZ | Private | **Confirmed orchestrated (IXOPAY + legacy ZOOZ, 12 acquirers)** | [S16] |
| Hopper | Montreal | ~$5B val | Fintech ancillary model | [S16] |
| Despegar | Buenos Aires | Public | LATAM leader | [S16] |
| MakeMyTrip | Gurgaon IN | ~$8B cap | India leader (same talent market) | [S16] |
| Almosafer / Wego | Riyadh / Dubai | Regional | MENA peers | [S16] |

Reference peers for the pitch: Kiwi.com (confirmed orchestrator) and eDreams (orchestration-adjacent) show "OTAs your size already orchestrate consumer acquiring."

**11D. Scoring (verified)**
| Signal | Pts | Verified |
|--------|-----|----------|
| Operates in 3+ countries | +3 | Yes (US, CA, UK, India, UAE) |
| Multiple PSPs | +0 | Not verified (no PSP named; multiple methods/BNPL yes) |
| Recent expansion (24 mo.) | +2 | Yes (Sabre, Amadeus, Enterprise Solutions, Frontier) |
| Public payment issues | +2 | Yes (class action + BBB volume) |
| Revenue scale (funding proxy) | +2 | Yes (~$460M+ net rev, billions in bookings) |
| Emerging-market traffic (India/MENA/LATAM) | +2 | Yes |
| No consumer orchestrator | +1 | Consumer side unconfirmed; supplier side orchestrated |
| Payment job postings | +0 | Not verified |
| Public RFP | +0 | No |
| **Total** | **12** | **🔴 High** |

Pipeline summary: strong OTA vertical fit, best comparable is Kiwi.com (confirmed orchestrator). Strongest wedge region: India (OneTravel).

---

## SECTION 12 — Business Case
| Annual Revenue (est.) | Gross bookings | Avg ticket | Primary currency | Top markets |
|-----------------------|----------------|------------|------------------|-------------|
| ~$460M to $487M net (aggregator ESTIMATE, low confidence) | "Billions" (CheapOair ~$3.5B in 2014, dated; current not disclosed) | Not found (air ticket, typically a few hundred USD) | USD (also CAD, INR, others) | US, India, Canada |

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi [Name], I have been following Fareportal's payments moves, the Outpayce wallet for supplier settlement and the "payment orchestration" you now offer through Enterprise Solutions. You clearly think about payments as infrastructure. The one piece that usually stays fragmented is the consumer checkout: across CheapOair and OneTravel, US and Canada and India, cards plus PayPal plus Affirm plus Accrue, routed through whatever acquirer each market defaults to. Yuno is a consumer-side orchestration layer that routes each transaction to the best acquirer per market for higher approval on air tickets, adds local methods (relevant given OneTravel is now mostly India), and unifies reconciliation so the duplicate-charge and refund issues get easier to control. inDrive went live in 10 markets in under 8 months with us; Kiwi.com runs a similar orchestrated model in your space. Worth 20 minutes to compare against your current consumer setup? Tuesday or Thursday works.

--- COLD EMAIL ---
Subject: CheapOair + OneTravel: the consumer side of your payments stack

Hi [Name],

You have already orchestrated the hard part most OTAs ignore: supplier settlement, now on Amadeus Outpayce, and you even sell payment orchestration through Enterprise Solutions. The piece that usually stays stitched together is the consumer checkout.

Across CheapOair (US heavy) and OneTravel (now ~46% India and growing fast), in USD, CAD and INR, with cards, PayPal, Apple Pay, Affirm and Accrue, each market tends to run on whatever acquirer it defaulted to, with no single routing or reconciliation layer. On air tickets, that means avoidable declines, and it shows up downstream as the duplicate charges, slow refunds and disputes in your complaint volume.

Yuno is a consumer-side orchestration layer: one API that routes each transaction to the best acquirer per market (about +7% approval in our base), adds local methods where your buyers are (UPI and netbanking matter for OneTravel's India base), and unifies reconciliation and disputes across brands, currencies and BNPL providers. It complements Outpayce rather than touching it.

inDrive went live in 10 markets in under 8 months with us, and Kiwi.com runs an orchestrated model in your exact vertical.

Worth 20 minutes to map your consumer acquiring by market and see the auth-rate upside? I have Tuesday or Thursday afternoon.

[Signature]
```

---

## APPENDIX — Sources
```
[S1]  https://www.similarweb.com/website/cheapoair.com/
[S2]  https://www.semrush.com/website/onetravel.com/overview/
[S3]  https://www.fareportal.com/ · https://en.everybodywiki.com/Fareportal
[S4]  https://www.tofler.in/fare-portal-india-private-limited/company/U72900DL2005PTC134394
[S5]  https://topclassactions.com/lawsuit-settlements/money/fees/cheapoair-facing-a-class-action-lawsuit-over-charging-customers-more-than-the-final-price/
[S6]  https://www.pymnts.com/apple-pay-tracker/2016/cheapoair-apple-pay-acceptance/
[S7]  https://www.onetravel.com/flights/book-now-pay-later
[S8]  https://www.fareportal.com/2019/04/29/pay-for-your-flights-over-time-on-cheapoair-com-and-onetravel-com-with-affirm/ · https://www.cheapoair.com/flights/book-now-pay-later-flights
[S9]  https://www.globenewswire.com/news-release/2023/06/13/2687326/0/en/Fareportal-and-Save-Now-Buy-Later-Platform-Accrue-Savings-Announce-Partnership.html
[S10] https://amadeus.com/en/newsroom/press-releases/fareportal-partnership-amadeus-innovation-travel
[S11] https://www.prweb.com/releases/fareportal-announces-launch-of-fareportal-enterprise-solutions-enabling-partners-to-own-and-scale-travel-offerings-302758710.html
[S12] https://www.bbb.org/us/ny/new-york/profile/travel-agency/fareportal-inc-0121-89212/complaints
[S13] https://onetravel.pissedconsumer.com/review.html
[S14] https://news.flyfrontier.com/fareportal-and-frontier-airlines-launch-ndc-api-to-offer-travelers-more-personalized-options/
[S15] https://www.prweb.com/releases/fareportal-expands-long-term-partnership-with-sabre-to-accelerate-global-growth-and-ai-driven-distribution-302780866.html
[S16] https://silviglobaltechnology.com/blog/best-otas-in-2026/ · https://mize.tech/blog/online-travel-agencies-market-share-across-the-world/
```
