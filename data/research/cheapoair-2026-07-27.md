# SDR Research Brief — CheapOair (Fareportal)
*Yuno Payment Orchestrator · Framework v8.0 · 2026-07-27*

> Companion to [fareportal-2026-07-23.md](fareportal-2026-07-23.md). This brief is CheapOair-brand-specific and refreshes the stack, leadership, complaints and per-market checkout with a 4-agent deep dig (2025-2026). A CheapOair Business Case (Travel/OTAs, ~$119.7M modeled benefit) was built the same day: `Business Cases/BC sheets - CheapOair.xlsx`.

## EXECUTIVE SUMMARY
CheapOair is Fareportal's US-heavy flagship OTA selling flights across 500+ airlines, ~5.5-6M visits/mo (declining). Its consumer checkout is now CONFIRMED (first-party JS): **CyberSource (Visa) for cards + Google Pay, Braintree for PayPal/Venmo, CardinalCommerce 3DS, Accertify fraud, Akamai edge, and no orchestrator.** That is a two-PSP, multi-BNPL (Affirm + Accrue) stack running in parallel with no routing, failover or unified reconciliation layer. The Yuno wedge is a consumer-side orchestration layer over the existing PSPs: multi-acquirer routing and auth-rate uplift on high-decline air tickets, cross-border cost reduction on Canada (16.81% of traffic) and India (billed from US entities, no local acquiring), local methods where they are missing (Interac in Canada, UPI/RuPay in India), and one reconciliation view to cut the double-charge, refund-delay and dispute volume showing up in complaints and the Quebec class action. Finance-native CEO Amit Singh (ex-Despegar CFO, appointed Aug 2025) and SVP Finance & Fintech Products Manish Kumar Sharma (publicly owns merchant processing) are the buying center.

---

## SECTION 1 — Traffic by Country
**Two readings; both valid, use the one the client shows on the call.**

**A) User's live SimilarWeb view (2026-07-27, used for the Business Case):** 81.08M annual visits.
| Rank | Country | Traffic Share | Change |
|------|---------|---------------|--------|
| 1 | United States | 65.06% | ↓3.20% |
| 2 | Canada | 16.81% | ↓5.72% |
| 3 | India | 1.41% | ↓4.87% |

**B) Free-tool .com-only view (Agent A):** ~5.5-6.9M visits/mo, declining (Semrush Apr→Jun 2026: 5.47M→6.03M→5.87M, -2.63% MoM). US 80.9-84.7% · Canada 2.4-2.5% · India 1.0-1.8% · Saudi Arabia 0.8-1.0% · Argentina/UAE ~0.7-0.9% (UAE and Argentina straddle rank 5-6 depending on tool). Countries 6-10 are paywalled on all free tools. [S1]

The Canada gap (16.81% live view vs ~2.5% .com-only) most likely reflects cheapoair.ca folded into the client's measured view; cheapoair.ca is separately measurable (Hypestat, order-of-magnitude unverified). Either way Canada is a material, cross-border market.

Flags: US-dominant with a real Canada footprint; India, Saudi, Argentina, UAE emerging-market presence = cross-border + local-method signal.

---

## SECTION 2 — Legal Entities
| Country | In Top Traffic? | Local Entity? | Cross-Border Risk | Source |
|---------|-----------------|---------------|-------------------|--------|
| USA | Yes | Fareportal Inc (NYC HQ); RSH Travel Inc / WK Travel Inc consumer entities; app seller "Fareportal, Inc." | Home market | [S2][S3] |
| Canada | Yes (16.81%) | cheapoair.ca storefront; **RSH Travel Inc d/b/a Cheapoair** named in QC suit (US entity, not a CA billing entity) | ⚠️ Likely billed cross-border from US entity | [S4][S5] |
| India | Yes (1.41%) | Fare Portal India Pvt Ltd = Gurgaon dev/ops center only; **no dedicated India storefront** (cheapoair.co.in / in.cheapoair.com / cheapoair.in all dead) → India visitors book on cheapoair.com | ⚠️ Cross-border, US-style checkout | [S3][S6] |
| UK | Regional domain | **No active Fareportal/CheapOair entity on Companies House** (only CHEAPOAIR LTD, dissolved 28-Jan-2025 at a mass-registration address, no evidence of affiliation) → UK likely billed from US | ⚠️ Cross-border | [S7] |
| Mexico | Not in top 3 | **cheapoair.mx storefront EXISTS** (real Spanish "CheapOair.MX", Fareportal CDN) | Spanish storefront live | [S8] |

> ⚠️ MANUAL: verify per-market billing entity on each storefront's T&Cs clause 1. RSH Travel / WK Travel are US consumer entities; no confirmed CA/UK/IN local billing entity.

---

## SECTION 3 — Payment Stack (CONFIRMED via first-party checkout JS)

**3A. PSPs / gateways / fraud**
| Layer | Vendor | Role | Confidence | Evidence |
|-------|--------|------|-----------|----------|
| Card gateway / PSP | **CyberSource (Visa)** | Cards + Google Pay (`Gateway:"cybersource", GatewayMerchantId:"007100", MerchantName:"CheapOair"`) | High | [A1] |
| Wallet PSP | **Braintree (PayPal)** | PayPal + Venmo (prod tokenization key, `CheapOair_instant`) | High | [A1] |
| 3-D Secure | **CardinalCommerce (Visa)** | Consumer auth / 3DS | High | [A3] |
| Anti-fraud | **Accertify (Amex)** | Device intel / fraud (consent string in live checkout) | High | [A3] |
| Anti-fraud (2019) | **Fraud.net** | ML scoring (SVP testimonial); current status unclear | Med | [A4] |
| Fraud ops | **In-house Gurgaon team** | Manual review | High | [A5] |
| Edge / bot mgmt | **Akamai** | CDN + bot management (the 403 blocker) | High | live headers |
| Card issuing (co-brand) | **Synchrony Bank** | CheapOair Credit Card + Visa/Visa Signature (issuing, NOT acquiring) | High | [S9] |
| Acquiring bank behind CyberSource | **No public info found** | — | — | Agent A |
| **Orchestrator** | **None found** | — | — | JS sweep + [S10] |

**3B. Orchestrator:** No public evidence found. Sweep for Spreedly/Primer/Gr4vy/CellPoint/APEXX returned nothing; checkout JS shows no orchestrator. Supplier side IS orchestrated (Amadeus Outpayce B2B Wallet, Jan 2026) and Fareportal even markets "payment orchestration" via Enterprise Solutions (Apr 2026) — so the wedge is the **consumer** side, not "you lack orchestration."
> ⚠️ MANUAL — real-browser DevTools on cheapoair.com checkout to read the acquirer + 3DS flow (test card 4111 1111 1111 1111 | 02/30 | 123).

---

## SECTION 4 — APMs

**4A. Confirmed / research-verified**
| Market | Methods (live) | Source |
|--------|----------------|--------|
| US (cheapoair.com) | Visa/MC/Amex/Discover, PayPal + Venmo (Braintree), Apple Pay + Google Pay (CyberSource), Paze, Affirm BNPL, Accrue Savings; T&Cs reference unnamed "non credit/debit card payment methods" | [A1][S11][S12] |
| Canada (cheapoair.ca) | Cards + **Affirm CONFIRMED** on .ca homepage (2023 Affirm.js modal); PayBright absorbed by Affirm | [S4][S13] |
| UK (cheapoair.co.uk) | **CARD-ONLY confirmed**: "We accept Debit cards and Credit cards online… Payment must be made in full with a valid credit or debit card." No wallet/BNPL named. | [S14] |

**4B. Unverified markets (do NOT treat as gaps)**
| Market | Attempted? | Reason | Popular local APMs (context only) |
|--------|-----------|--------|-----------------------------------|
| India (on .com) | Yes | US-style card checkout, INR display only; from archived JS not live | UPI, RuPay, Net Banking, Paytm/PhonePe |
| Canada | Yes | .ca 2026 is a JS shell; Interac not observed (≠ absent) | Interac / e-Transfer |
| Mexico (cheapoair.mx) | Yes | JS shell, no payment strings captured | OXXO, SPEI, MSI installments, Mercado Pago |
| UAE | Yes | cheapoair.ae is a parked page (not a storefront) | Tabby, Tamara, mada, Apple Pay |

> "Not verified" ≠ "not available." MANUAL: VPN + real browser checkout per market before any APM claim. India (UPI) and Canada (Interac) are the strongest upside but must be walked live first.

---

## SECTION 5 — Payment Complaints (fresh 2025-2026)
| Issue | Platform | Volume / recency | Source |
|-------|----------|------------------|--------|
| Double charges, refund delays, hidden fees | **PissedConsumer** | **1.5/5, 613 reviews**; Jul 2026 "amount deducted twice," Jun 2026 refund weeks past promise, Apr 2026 billing error $982.50 | [S15] |
| Price changed at booking, quoted 4 different refund amounts, cancellation fees despite insurance | **SiteJabber** | 3.1/5, 14,844 reviews; Mar/May/Dec 2025 | [S16] |
| Hidden charges, cancellation fees inside 24h window, refund refusals | **Reviews.io** | **1.2/5, 201 reviews, 4% recommend**; 2025-2026 | [S17] |
| (rating not retrievable — bot-blocked) | Trustpilot | ~1,533-1,554 reviews | [S18] |
| Charged MORE than displayed "Final Total Price" | **Quebec Superior Court class action** | *RSH Travel Inc d/b/a Cheapoair*, No. 500-06-001050-208, filed ~Mar 2020, class from Mar 2017, **$20M punitive**; 2025-26 status unverified | [S5] |
| False-urgency tactics | **NY AG settlement** | $2.6M (2022) | [S19] |

Analysis: the recurring pattern (price-at-payment mismatch, double charges, chargebacks, 60-90 day refunds) maps directly to Yuno's unified reconciliation, single transaction view across CyberSource/Braintree/Affirm/Accrue, dispute tooling and consistent charge/settle logic. High dispute volume also pressures acquirer relationships, where multi-acquirer routing helps.

---

## SECTION 6 — Expansion & Corporate
| # | Date | Development | Source |
|---|------|-------------|--------|
| 1 | Apr 24 2025 | Frontier NDC API integration | [S20] |
| 2 | **Aug 28 2025** | **Amit Singh appointed President** (later CEO & President); ex-Despegar CFO, ex-Wall Street | [S21] |
| 3 | Jan 21 2026 | Amadeus Outpayce B2B Wallet (supplier settlement) | [S22] |
| 4 | Apr 30 2026 | Fareportal Enterprise Solutions launch — markets "payment orchestration" (B2B) | [S23] |
| 5 | May 26 2026 | Sabre partnership expansion, "agentic AI orchestrating end-to-end shopping" + NDC | [S24] |

**Leadership / buying center (verified on official leadership page):**
- **Amit Singh — CEO & President** (finance-native, ex-Despegar CFO). [S25]
- **Gary Starr — CFO.** [S25]
- **Manish Kumar Sharma — SVP, Finance & Fintech Products** — publicly owns **merchant processing + virtual-card processing**. This is the payments owner. [S25][S26]
- Yuvraj Datta — Chief Supply & Revenue Officer; Naveen Gunti — Chief AI & Technology Officer; Sam S. Jain — Founder & Exec Chairman.
- ⚠️ **Tom Spagnola (prior champion) is NO LONGER on the current official leadership page**; supplier relations now rolls up to Yuvraj Datta. Confirm his status before outreach.
- ~3,102 employees (India-heavy). No payments job postings confirmable (Naukri/LinkedIn access-blocked; ~29-39 open Fareportal Gurgaon roles indexed).

---

## SECTION 7 — Payment News (last 12 mo)
No NEW consumer PSP/method partnership or removal found Jul 2025→Jul 2026. Existing rails all predate the window: Affirm (Apr 2019, both brands), PayBright/Affirm CA (May 2022), Accrue Savings (Jun 2023), Synchrony co-brand cards. iOS app actively shipped (v4.281.0, Jul 10 2026; 4.77★, 264k ratings; description claims "no booking or credit card fees"). Sezzle and Zip are user-side virtual-card workarounds, NOT native CheapOair integrations. [S12][S15]

---

## SECTION 8 — Checkout Audit
| Dimension | Finding |
|-----------|---------|
| Checkout type | Single Fareportal platform across all domains; currency-only localization; Akamai 403 to bots |
| Methods (US) | Cards + PayPal/Venmo + Apple/Google Pay + Paze + Affirm + Accrue |
| Methods (UK) | **Card-only** (confirmed T&Cs); no wallet/BNPL named |
| Methods (Canada) | Cards + Affirm (confirmed); Interac not observed |
| Methods (India) | US-style card checkout on .com, INR display only |
| 3DS | CardinalCommerce (confirmed) |
| Multi-currency | Yes (USD, CAD, GBP, INR, MXN displays) |
| Biggest UX pain | Charged amount exceeding displayed final price (litigated) + double charges + slow refunds |

> ⚠️ MANUAL: walk US, Canada and India checkouts in a real browser with local IPs.

---

## SECTION 9 — PCI DSS
No public PCI/security page found. [INFERENCE] Card-heavy air ticketing at ~6M visits/mo → almost certainly PCI DSS Level 1, undocumented. Yuno reduces PCI scope via a portable vault + network tokenization. [S3]

---

## SECTION 10 — Strategic Insights

**Insight #1: Two consumer PSPs, zero orchestration.**
Evidence: S3 (CyberSource + Braintree confirmed, no orchestrator). Pain: cards on CyberSource and PayPal/Venmo on Braintree run in parallel with no routing, no cross-processor failover, split reconciliation. Yuno value: one orchestration layer over both PSPs, +7% approval on high-decline air tickets, 50% recovery. Best case: NYT / Newfold (already had PSPs, optimized the rest). Angle: "Your supplier side is orchestrated on Outpayce and you sell orchestration through Enterprise Solutions. Is the consumer checkout, CyberSource for cards and Braintree for PayPal, routed to the best acquirer per market?"

**Insight #2: Canada (16.81%) and India billed cross-border from US entities.**
Evidence: S4, S5, S7 (no CA/UK/IN billing entity). Pain: cross-border MDR and no local acquiring on a big Canada base. Yuno value: local acquiring + cross-border MDR reduction. Best case: inDrive (10 markets < 8 months). Angle: local acquiring for Canada without standing up a Canadian entity.

**Insight #3: India is a US-style card checkout in a UPI-first market.**
Evidence: S6 (no India storefront; .com card checkout). Pain: Indian buyers want UPI/RuPay/net banking; card-only leaks conversion. Yuno value: add local methods in weeks. Angle: bring India a local, high-approval way to pay (verify live first).

**Insight #4: Litigated price-at-payment mismatch + heavy dispute volume.**
Evidence: S5 (class action), S15-S17 (1.2-1.5/5 payment complaints, fresh Jul 2026). Pain: double charges, chargebacks, 60-90 day refunds erode trust and acquirer standing. Yuno value: unified reconciliation, single transaction view, dispute tooling, consistent charge logic. Angle: cut the double-charge and refund friction visible in complaints and the Quebec suit.

**Insight #5: Finance-native buying center.**
Evidence: S21, S25, S26 (Amit Singh ex-Despegar CFO CEO; Manish Kumar Sharma owns merchant processing). Pain: a CEO who ran an OTA's finances knows payment economics cold. Yuno value: speak auth-rate, MDR and reconciliation in their language. Angle: lead with the P&L, not the tech.

---

## SECTION 11 — Pipeline (OTA peers)
| Company | HQ | Note | Source |
|---------|-----|------|--------|
| eDreams ODIGEO | Madrid | Flight-led OTA, 7M+ Prime subs; closest EU analog | [S27] |
| lastminute.com | Chiasso/Amsterdam | Flight + package OTA | [S28] |
| Hopper | Montreal | AI/fintech-heavy travel | [S28] |
| Kiwi.com | Brno CZ | Virtual-interlining budget OTA; IXOPAY orchestration **unverified-current** | [S29] |
| Expedia / Booking / Trip.com | US / US / CN | Scale peers, in-house payments | [S30] |
| MakeMyTrip | Gurgaon | India leader (same talent market) | [S30] |

**11D. Scoring (verified)**
| Signal | Pts | Verified |
|--------|-----|----------|
| Operates in 3+ countries | +3 | Yes (US, CA, UK, IN, MX) |
| Multiple PSPs | +3 | **Yes — CyberSource + Braintree confirmed** |
| Recent expansion (24 mo.) | +2 | Yes (Amadeus, Sabre, Enterprise Solutions, Frontier) |
| Public payment issues | +2 | Yes (class action + 1.2-1.5/5 complaints) |
| Revenue scale | +2 | Yes (~$487M+ Fareportal) |
| Emerging-market traffic | +2 | Yes (India/MENA/LATAM) |
| No consumer orchestrator | +2 | **Yes — confirmed** |
| Payment job postings | +0 | Not confirmable |
| Public RFP | +0 | No |
| **Total** | **16** | **🔴 High** |

---

## SECTION 12 — Business Case
| Annual Revenue (est.) | Modeled TPV | Avg ticket | Primary currency | Top markets |
|-----------------------|-------------|------------|------------------|-------------|
| ~$487.5M Fareportal consolidated (Zippia est.; $1B+ per Seamless) | ~$1.8B modeled | US domestic $427.69 (BTS Q1 2026); blended higher (international skew) | USD (also CAD, INR, GBP, MXN) | US, Canada, India |

Full model: `Business Cases/BC sheets - CheapOair.xlsx` — **~$119.7M modeled annual benefit** (TPV acceptance uplift $55.9M + fee renegotiation $9.0M + new APM TPV growth $53.9M + engineering savings $0.89M) across NA (US, Canada) + APAC (India). Take rate 0.10 (Travel/OTAs, conservative), conversion 0.06.

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi [Name], I have been following CheapOair's payments setup. You already orchestrate the supplier side on Amadeus Outpayce and even sell orchestration through Enterprise Solutions. The piece that usually stays fragmented is the consumer checkout: cards on CyberSource, PayPal and Venmo on Braintree, plus Affirm and Accrue, all running in parallel with no routing or failover across them. Yuno is a consumer-side orchestration layer that sits over your existing PSPs: it routes each transaction to the best acquirer per market for higher approval on air tickets, reduces cross-border cost on Canada, and unifies reconciliation so the double-charge and refund issues in your reviews get easier to control. inDrive went live in 10 markets in under 8 months with us. Worth 20 minutes to compare against your current consumer setup? Tuesday or Thursday works.

--- COLD EMAIL ---
Subject: CheapOair's consumer checkout: CyberSource + Braintree, no layer on top

Hi [Name],

You have orchestrated the hard part most OTAs ignore: supplier settlement, now on Amadeus Outpayce, and you sell payment orchestration through Enterprise Solutions. The piece that usually stays stitched together is the consumer checkout.

CheapOair runs cards on CyberSource and PayPal and Venmo on Braintree, with Affirm and Accrue on top, each rail operating in parallel with no routing, no cross-processor failover and split reconciliation. On air tickets that means avoidable declines, and downstream it shows up as the double charges, slow refunds and disputes across your review sites and the Quebec pricing case.

Yuno is a consumer-side orchestration layer that sits over your current PSPs: one API that routes each transaction to the best acquirer per market (about +7% approval in our base), reduces cross-border cost on markets like Canada that bill from your US entity, adds local methods where your buyers are, and unifies reconciliation and disputes across brands, currencies and BNPL. It complements Outpayce rather than touching it.

inDrive went live in 10 markets in under 8 months with us. Worth 20 minutes to map your consumer acquiring by market and see the auth-rate upside? I have Tuesday or Thursday afternoon.

[Signature]
```

---

## APPENDIX — Sources
```
[S1]  https://www.semrush.com/website/cheapoair.com/overview/ · https://hypestat.com/info/cheapoair.com · https://www.similarweb.com/website/cheapoair.com/
[S2]  https://itunes.apple.com/search?term=cheapoair&entity=software&country=us (seller "Fareportal, Inc.")
[S3]  https://www.fareportal.com/
[S4]  http://web.archive.org/web/20230105045433/https://www.cheapoair.ca/
[S5]  https://ca.topclassactions.com/lawsuit-settlements/lawsuit-news/cheapoair-facing-a-class-action-lawsuit-over-charging-customers-more-than-the-final-price/
[S6]  Wayback availability/CDX: no snapshots for cheapoair.co.in / in.cheapoair.com; cheapoair.in last archived 2012
[S7]  https://find-and-update.company-information.service.gov.uk/search?q=cheapoair (CHEAPOAIR LTD 15847020, dissolved 28-Jan-2025)
[S8]  http://web.archive.org/web/20260605232318/https://www.cheapoair.mx/
[S9]  https://www.synchrony.com/contenthub/newsroom/cheapoair-and-onetravel-launch-new-travel-rewards-credit-cards.html · https://www.nerdwallet.com/credit-cards/learn/cheapoair-credit-card
[S10] Orchestrator sweep (Spreedly/Primer/Gr4vy/CellPoint/APEXX) — no link found
[S11] http://web.archive.org/web/20260417221609/https://www.cheapoair.com/info/generaltermsandconditions/
[S12] https://apps.apple.com/us/app/cheapoair-cheap-flight-deals/id436858222
[S13] https://www.travelpress.com/cheapoair-ca-paybright-unveil-new-partnership/
[S14] http://web.archive.org/web/20260410171507/https://www.cheapoair.co.uk/faq/payments.asp · http://web.archive.org/web/20260313231239/https://www.cheapoair.co.uk/info/generaltermsandconditions/
[S15] https://cheapoair.pissedconsumer.com/review.html
[S16] https://www.smartcustomer.com/reviews/cheapoair.com
[S17] https://www.reviews.io/company-reviews/store/cheapoair
[S18] https://www.trustpilot.com/review/www.cheapoair.com
[S19] https://topclassactions.com/lawsuit-settlements/lawsuit-news/cheapoair-com-onetravel-com-owner-to-pay-2-6m-following-ag-investigation/
[S20] https://news.flyfrontier.com/fareportal-and-frontier-airlines-launch-ndc-api-to-offer-travelers-more-personalized-options/
[S21] https://www.prnewswire.com/news-releases/fareportal-inc-appoints-amit-singh-as-president-302541147.html
[S22] https://amadeus.com/en/newsroom/press-releases/fareportal-partnership-amadeus-innovation-travel
[S23] https://www.prweb.com/releases/fareportal-announces-launch-of-fareportal-enterprise-solutions-enabling-partners-to-own-and-scale-travel-offerings-302758710.html
[S24] https://www.prweb.com/releases/fareportal-expands-long-term-partnership-with-sabre-to-accelerate-global-growth-and-ai-driven-distribution-302780866.html
[S25] https://www.fareportal.com/leadership/
[S26] https://www.linkedin.com/in/sharmacpa/ · https://theorg.com/org/fareportal
[S27] https://en.wikipedia.org/wiki/EDreams_ODIGEO · https://www.edreamsodigeo.com/our-brands/
[S28] https://portersfiveforce.com/blogs/competitors/lastminute
[S29] https://en.wikipedia.org/wiki/IXOPAY
[S30] https://mize.tech/blog/online-travel-agencies-market-share-across-the-world/

Addendum (checkout JS, confirmed stack):
[A1] Wayback COA checkout JS: web.archive.org/web/20260626225207/https://www.cheapoair.com/air/paymentoption.bundle.8e517cea72796b9c65a1.js
[A3] Wayback COA _air_payment (Cardinal/Accertify strings): web.archive.org/web/20250624211940/https://www.cheapoair.com/air/iln/desktop/en-us/2.2.821/_air_payment
[A4] Fraud.net case study (Fareportal SVP): fraud.net/resources/case-study-fareportal-travel-agency/
[A5] OneTravel privacy policy (in-house fraud): web.archive.org/web/20260411083819/https://www.onetravel.com/info/privacy-policy/
```
