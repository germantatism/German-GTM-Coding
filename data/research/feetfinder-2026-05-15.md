# FeetFinder (feetfinder.com) — Yuno SDR Research Brief
*Date: 2026-05-15 | Framework v8.0 | Disclaimer: revenue, user counts, valuation and commission % are third-party estimates or self-reported marketing claims, not audited. First-party site (checkout/T&Cs) returned HTTP 403 to research — PSP/APM findings are sourced from FeetFinder's official X account + consistent third-party reporting, per web data. Inference flags inline.*

### EXECUTIVE SUMMARY
FeetFinder is a US-based, bootstrapped creator marketplace for feet photos/videos — an adult-adjacent, high-risk payments vertical (founder/CEO Patrick Nielson; est. ~$8.5M annual revenue, third-party estimate). Its payment stack is concentrated on a single high-risk specialist processor, **Segpay** (confirmed via FeetFinder's own X/Twitter post), with **Paxum** for non-US payouts and PayPal routed through Segpay — no orchestration layer or acquirer redundancy found. The dominant public pain is creator payout delays/withholding plus chargeback reversal and European buyer declines, which combine into a textbook orchestration narrative: failover, decline recovery, descriptor control, and payout reliability. Gating constraint for Yuno: acquirer/compliance appetite for adult content must be qualified internally before pursuit.

> ⚠️ INTERNAL: This is a high-risk adult-adjacent merchant. Confirm Yuno's underwriting/acquirer appetite for this MCC before investing cycles. Brief is accuracy-graded; treat growth/financial figures as unaudited.

---

### SECTION 1 — Traffic by Country
| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|---|---|---|---|---|---|
| 1 | United States | 39.56% (desktop) | ~2.1M total site visits (Feb 2026) | Direct-dominant (44.5%) | [SimilarWeb](https://www.similarweb.com/website/feetfinder.com/) |
| 2 | United Kingdom | 8.17% | — | n/a | [SimilarWeb](https://www.similarweb.com/website/feetfinder.com/) |
| 3 | Germany | 7.51% | — | n/a | [SimilarWeb](https://www.similarweb.com/website/feetfinder.com/) |
| 4+ | Canada (cited core market) | Not found (paywalled) | — | n/a | [Semrush](https://www.semrush.com/website/feetfinder.com/overview/) |

Full ranked top-10 with absolute visits is behind SimilarWeb/Semrush login — only top-3 shares confirmed. US/UK/Germany concentration with material non-US share = cross-border acquiring relevance from a single US entity.

---

### SECTION 2 — Legal Entities
| Country | In Top Traffic? | Local Entity? | Cross-Border Risk? | Source |
|---|---|---|---|---|
| US | ✅ | ✅ "Feetfinder", Mercer Island WA; registered agent Carson City NV | n/a (home) | [Creditsafe](https://www.creditsafe.com/business-index/en-us/company/feetfinder-us149682718), [BBB](https://www.bbb.org/us/nv/carson-city/profile/adult-entertainment/feetfinder-1166-90041984) |
| UK | ✅ (8.17%) | ❌ Not found | ⚠️ Cross-border — served from US entity | [SimilarWeb](https://www.similarweb.com/website/feetfinder.com/) |
| Germany | ✅ (7.51%) | ❌ Not found | ⚠️ Cross-border — served from US entity | [SimilarWeb](https://www.similarweb.com/website/feetfinder.com/) |

⚠️ *UK and Germany are top-3 traffic markets with no local entity found — buyers there are likely processed cross-border on a US-acquired, high-risk MCC, a known driver of issuer declines.* Entity type (LLC vs Corp) and exact incorporation date ambiguous (Creditsafe shows 2025/26 registration vs. 2019/20 product origin). "Dinny Samaniego (CEO)" / "Lebron Jordan (Owner)" appear only on data aggregators — [INFERENCE — not confirmed], treat as noise; founder/CEO is Patrick Nielson.

> ⚠️ MANUAL: Verify processing entity and acquirer geography on official T&Cs.

---

### SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**
| Region | PSP / Acquirer | Evidence Type | Source |
|---|---|---|---|
| US (buyers) | **Segpay** (high-risk adult specialist, PCI-DSS) | [Press/Review — FeetFinder official X account] | [x.com/FeetFinder](https://x.com/FeetFinder/status/1488257130062757888), [Footly safety review](https://www.tryfootly.com/blog/is-feetfinder-safe-2026) |
| Global | PayPal — enabled *via the Segpay partnership* (Feb 2022), not direct | [Press — FeetFinder official X] | [x.com/FeetFinder](https://x.com/FeetFinder/status/1488605844191133696) |
| Non-US (payouts) | **Paxum**; US payouts via Segpay; aggregated through **MassPay** | [Press/Review — multiple consistent guides] | [Ecommerce Fastlane](https://ecommercefastlane.com/how-to-make-money-on-feetfinder/) |

Cards confirmed: Visa, Mastercard, Discover, prepaid cards ([Rewarble](https://rewarble.com/insight/what-is-feetfinder-and-how-does-it-work)). Amex, Apple Pay, Google Pay, crypto/USDT — **not confirmed** (not asserting absence; first-party checkout was 403-blocked). Billing descriptor is discreet but reported **not customizable** (competitor differentiator). The "CCBILL*FOOTLY" descriptor seen in some sources belongs to competitor **Footly, not FeetFinder** — excluded to avoid false attribution.

**3B. Orchestrator:** No public evidence found (Spreedly, Primer, Gr4vy, CellPoint, APEXX, Yuno). Single buyer-side processor (Segpay) with no apparent acquirer redundancy or routing layer.

> ⚠️ MANUAL — DevTools test card 4111 1111 1111 1111 | 02/30 | 123 (requires account/age-gate pass via VPN).

---

### SECTION 4 — APMs (Agent D)

**4A. Confirmed**
| Market | Methods Confirmed | Source |
|---|---|---|
| Global (buyers) | Visa, Mastercard, Discover, prepaid cards, PayPal (via Segpay) | [x.com/FeetFinder](https://x.com/FeetFinder/status/1488257130062757888), [Rewarble](https://rewarble.com/insight/what-is-feetfinder-and-how-does-it-work) |
| Creators (payouts) | Segpay (US), Paxum (non-US), weekly, $30 min threshold | [Ecommerce Fastlane](https://ecommercefastlane.com/how-to-make-money-on-feetfinder/) |

**4B. Unverified**
| Market | Attempted? | Reason | Notes |
|---|---|---|---|
| feetfinder.com checkout/FAQ | Yes | HTTP 403 bot-block; help subdomain ECONNREFUSED | Methods cross-confirmed via X + 3rd-party, not live page |
| Amex / Apple Pay / Google Pay / crypto | Yes | Not surfaced in any source | Not asserting absence — manual VPN walk needed |

> "Not verified" ≠ "not available." Never claim FeetFinder lacks a method in outreach.

---

### SECTION 5 — Payment Complaints
| Issue Type | Platform | Frequency | Date Range | Source |
|---|---|---|---|---|
| Creator payout delays (advertised weekly, actual 2–6 weeks) | Footly / StartupBooted | #1 documented issue | 2025–2026 | [Footly income](https://www.tryfootly.com/blog/feetfinder-income-real-creator-earnings-2026) |
| Withheld earnings / payout-triggered account suspensions | PissedConsumer (1.6★) | Multiple named cases | Aug 2024–Mar 2025 | [PissedConsumer](https://feetfinder.pissedconsumer.com/review.html) |
| Chargebacks reverse creator earnings; no merchant-side dispute shield | JustAnswer / forums | Recurring | 2025 | [JustAnswer](https://www.justanswer.com/south-africa-law/ri36i-legal-action-against-website-feetfinder.html) |
| Subscription auto-renewal charged w/o warning; refund requests ignored | Trustpilot (1.6★) / PissedConsumer | Recurring | 2025–Mar 2026 | [PissedConsumer](https://feetfinder.pissedconsumer.com/review.html) |
| European buyers unable to complete subscription payment | Trustpilot corpus | Reported | 2025–2026 | [INFERENCE — single-acquirer/issuer decline] [SimilarWeb context](https://www.similarweb.com/website/feetfinder.com/) |

**Pattern → Yuno fit:** payout delays/withholding ↔ orchestrated payout reliability + reconciliation; chargeback reversals ↔ dispute automation/fraud tooling; European declines ↔ smart routing + local acquiring + retry/cascade; non-customizable descriptor ↔ descriptor control. (Trustpilot specifics are lower-confidence — page 403-blocked, snippet-only.)

---

### SECTION 6 — Expansion & Corporate Developments
| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | Ongoing | Self-reported 8M verified users, $100M+ cumulative buyer spend, 12.5M items sold (marketing claim) | Growth (unaudited) | [Ecommerce Fastlane](https://ecommercefastlane.com/feet-pics-statistics/) |
| 2 | 2026 | Creator growth slowing; competitors (Footly, FunWithFeet) attacking on fees/payout speed | Competitive | [Footly](https://www.tryfootly.com/blog/why-creators-are-leaving-feetfinder-for-footly-2026) |
| 3 | Ongoing | No native iOS/Android app — 2+ yrs unable to meet Apple/Google adult-content policy; 100% web CNP | Distribution constraint | [Arceus X](https://arceusx.net/feetfinder-app-download/) |
| 4 | n/a | Bootstrapped — no external funding raised | Financial | [Crunchbase listing](https://www.crunchbase.com/organization/feetfinder) (corroborated, page 403) |

No confirmed payments/engineering job postings, no funding round, no new-market or leadership events in last 24 months.

---

### SECTION 7 — Payment News
| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | Feb 2022 | "In partnership with @segpay … approved to begin using @PayPal to process payments" | 🟢 Confirms Segpay primary processor + PayPal enablement | [x.com/FeetFinder](https://x.com/FeetFinder/status/1488257130062757888) |

No PSP partnership/removal, de-risking event, or funding in 2025–2026 found. Last confirmed processor event is the 2022 Segpay→PayPal enablement.

---

### SECTION 8 — Checkout Audit
| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Web-only, recurring subscription + prepaid credits/coins system | — | No native app (adult policy); 100% CNP |
| Guest checkout | Membership is subscription-based, no one-time guest model | Friction | [Footly fees](https://www.tryfootly.com/blog/feetfinder-fees-explained-hidden-costs-2026) |
| Steps to purchase | Subscribe ($4.99/mo basic, $14.99/mo premium) → buy credits ($10+) → spend internally | Adequate | [Rewarble](https://rewarble.com/insight/what-is-feetfinder-and-how-does-it-work) |
| 3DS | Not found | — | Manual check needed |
| Mobile experience | Mobile web/PWA only; no official app | Constrained | [Arceus X](https://arceusx.net/feetfinder-app-download/) |
| Descriptor | Discreet but reported not customizable | Negative vs. competitors | [Footly](https://www.tryfootly.com/blog/is-feetfinder-safe-2026) |

> ⚠️ MANUAL: Walk checkout via VPN + age-gated account.

---

### SECTION 9 — PCI DSS
| PCI DSS | Card Data Handling | Recommended Yuno Integration | Source |
|---|---|---|---|
| Compliance via processor (Segpay PCI-DSS); FeetFinder does not store card data | Tokenized/encrypted at Segpay | Yuno hosted fields/SDK to keep PCI scope at processor while adding routing/redundancy | [Footly](https://www.tryfootly.com/blog/is-feetfinder-safe-2026) |

---

### SECTION 10 — Strategic Insights

**Insight #1: Single high-risk acquirer (Segpay) concentration**
Evidence: §3 — only Segpay confirmed buyer-side (per FeetFinder's own X post), no redundancy/orchestration. | Pain Point: In adult MCC, acquirer de-risking or an outage means revenue stops with zero failover; all volume rides one processor. | Yuno Value Prop: Multi-PSP failover + smart routing across high-risk-capable acquirers, +7% approval uplift, 50% soft-decline recovery. | Best Case: Rappi (volume + ms-level monitoring). | Outreach Angle: "Running 100% of card volume through one high-risk processor in this vertical is the single biggest revenue risk you carry — orchestration is the redundancy layer, not a rip-and-replace."

**Insight #2: Cross-border European decline leakage**
Evidence: §1–2 + §5 — UK 8% / Germany 7.5% of traffic, no local entity; European buyers report payment failures. | Pain Point: Cross-border high-risk MCC = elevated issuer declines and lost subscriptions in top-3 markets. | Yuno Value Prop: Local acquiring + retry/cascade routing to recover EU declines. | Best Case: Livelo (+5% approval, 50% recovery). | Outreach Angle: "Your #2 and #3 markets are UK and Germany — exactly where a US-acquired high-risk MCC leaks the most approvals. That's recoverable."

**Insight #3: Payout reliability is the #1 public complaint**
Evidence: §5 — payout delays/withholding dominate creator reviews (PissedConsumer 1.6★); chargebacks claw back creator earnings. | Pain Point: Payout layer (MassPay→Segpay/Paxum) drives churn to Footly/FunWithFeet; no merchant-side dispute shield. | Yuno Value Prop: Pay-ins and payouts through one API with reconciliation and faster method/location-based payouts; centralized dispute/fraud tooling. | Best Case: Rappi (80% less analyst resolution time). | Outreach Angle: "Creators are leaving over payout speed and chargeback clawbacks — fixing the payout + dispute layer is a retention play, not just a payments one."

**Insight #4: Lean bootstrapped team, greenfield vertical**
Evidence: §6 — bootstrapped, ~$8.5M est. revenue, minimal payments engineering; no peer in the vertical uses orchestration. | Pain Point: Limited in-house payments resource to build redundancy/routing. | Yuno Value Prop: Orchestration substitutes for payments headcount; no-code PSP enablement. | Best Case: InDrive (fast multi-PSP activation). | Outreach Angle: "You don't need a payments team to get acquirer redundancy and decline recovery — that's what the orchestration layer is for."

---

### SECTION 11 — Pipeline

**11A. Direct Competitors**
| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| FunWithFeet | funwithfeet.com | Not found | ~469K visits/mo | US/UK | [Semrush](https://www.semrush.com/website/feetfinder.com/competitors/) |
| Snifffr | snifffr.com | Not found | ~817K visits/mo | US/UK | [Footly platforms](https://www.tryfootly.com/blog/where-to-sell-feet-pics-best-platforms-2026) |
| Feetify | feetify.com | Not found | ~139K visits/mo | Global | [Footly](https://www.tryfootly.com/blog/where-to-sell-feet-pics-best-platforms-2026) |
| Footly | tryfootly.com | Not found | Newer entrant | US | [Footly](https://www.tryfootly.com/blog/is-feetfinder-safe-2026) |
| DollarFeet | dollarfeet.com | Not found | Not found | US/Global | [JustAlternativeTo](https://www.justalternativeto.com/dollarfeet/) |
| InstaFeet | instafeet.com | Not found | Not found | US | [Stage and Cinema](https://stageandcinema.com/2026/05/03/best-sites-to-sell-feet-pics-2026/) |

**11B. Industry Peers (creator / adult-adjacent monetization)**
| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| OnlyFans | onlyfans.com | Creator subscription | Global | $7.22B FY24 gross, high-risk processors | [Variety](https://variety.com/2025/digital/news/onlyfans-fiscal-2024-revenue-earnings-1236495750/) |
| Fansly | fansly.com | Creator subscription | Global | CCBill/PayPal | [Wikipedia](https://en.wikipedia.org/wiki/Fansly) |
| ManyVids | manyvids.com | Adult creator e-comm | Global | High-risk specialists | [Creatorhero](https://www.creatorhero.com/blog/onlyfans-alternatives-) |
| JustForFans | justfor.fans | Adult creator | Global | CCBill + crypto | [Corepay](https://corepay.net/articles/which-payment-processor-does-just-for-fans-use/) |
| LoyalFans | loyalfans.com | Creator subscription | Global/EU | EU acquirer relationships | [Supercreator](https://www.supercreator.app/guides/onlyfans-alternatives) |
| Fanvue | fanvue.com | AI-creator | UK/Global | Fast payouts | [Fanvue](https://www.fanvue.com/) |
| Patreon | patreon.com | Mainstream creator | Global | Lower-risk (Stripe/PayPal) | [Creatorhero](https://www.creatorhero.com/blog/onlyfans-alternatives-) |

**11C. Adopting Orchestration:** None found. The vertical universally uses high-risk specialists (Segpay, CCBill, Verotel, Epoch, Paxum) + crypto; **no orchestration adoption found across the entire set** — greenfield, gated by acquirer compliance.

**11D. Scoring (FeetFinder)**
| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ US/UK/Germany via traffic |
| Multiple PSPs | 0 | ❌ Single buyer-side (Segpay); Paxum is payout-side |
| Recent expansion (24 mo.) | 0 | ❌ No confirmed corporate event |
| Public payment issues | +2 | ✅ Payout delays, chargebacks, declines |
| Funding >$10M | 0 | ❌ Bootstrapped |
| LATAM/APAC/MENA traffic | 0 | ❌ US/UK/DE-dominant |
| No orchestrator | +2 | ✅ None found |
| Payment job postings | 0 | None found |
| Public RFP | 0 | None found |
| **Total** | **7** | 🟡 Medium (low end) |

**Top Pipeline (this account + adjacent):**
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | FeetFinder | Target | US/UK/DE | 7 | 🟡 Medium | Single high-risk acquirer, payout pain |
| 2 | Fansly | Peer | Global | n/a | Watch | CCBill single-stack [INFERENCE] |
| 3 | JustForFans | Peer | Global | n/a | Watch | CCBill + crypto, multi-rail [INFERENCE] |

Pipeline summary: 1 primary target (Medium, low end). Score is understated relative to the qualitative fit — single high-risk acquirer + cross-border decline + payout pain is a strong orchestration narrative. Strongest vertical: adult-adjacent creator marketplaces, **gated by Yuno acquirer/compliance appetite for this MCC.**

---

### SECTION 12 — Business Case
| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| ~$8.47M est. (third-party, [Prospeo](https://prospeo.io/c/feetfinder-revenue) — unaudited) | Subscription $4.99–$14.99/mo + $10+ credit packs ([Rewarble](https://rewarble.com/insight/what-is-feetfinder-and-how-does-it-work)) | Not disclosed; ~20% platform commission (disputed vs. marketed 10%) | USD | US, UK, Germany |

---

### SECTION 13 — Outreach
*(Verified findings only — Segpay confirmed via FeetFinder's own X post. No unconfirmed APM claims. Internal acquirer-appetite caveat applies before sending.)*

```
--- LINKEDIN MESSAGE ---
Hi Patrick — I run pre-sales at Yuno (payment orchestration) and have spent time looking at how high-risk creator marketplaces handle payments.

One thing stood out: from your own announcement, FeetFinder's card volume runs through Segpay. In this vertical, a single acquirer is the biggest single point of failure — if it has a bad day or tightens underwriting, there's no fallback and the revenue just stops. Your #2 and #3 markets being the UK and Germany makes it sharper, since a US-acquired high-risk MCC is exactly where European approvals leak.

Yuno sits above your existing processor, not instead of it: smart routing and multi-PSP failover, decline recovery (we typically see +7% approval and ~50% recovery on soft declines), plus pay-ins and payouts through one API with reconciliation — relevant given how much of the creator feedback is about payout speed.

We've done this for Livelo (+5% approval, 50% recovery) and Rappi (real-time monitoring, 80% less analyst time). Worth 20 minutes next week to map where the recoverable revenue is? Open Tuesday or Thursday.

— German, Yuno

--- COLD EMAIL ---
Subject: Segpay is your single point of failure — the fix isn't a migration

Hi Patrick,

From FeetFinder's own announcement, card volume runs through Segpay. In a high-risk vertical that's the biggest risk you carry: one acquirer, no failover. If underwriting tightens or it goes down, revenue stops with nothing to route to.

Two compounding signals from the outside:
• UK and Germany are your #2 and #3 markets — a US-acquired high-risk MCC is precisely where European approvals get declined and lost.
• Creator feedback skews heavily to payout speed and chargeback clawbacks — a payout + dispute problem, not just an acceptance one.

Yuno is a payment orchestrator. We sit above your current processor (no rip-and-replace): one API → 1,000+ methods, 450+ processors, 50+ fraud tools, with:
• Smart routing + multi-PSP failover so one acquirer is never the whole business
• +7% approval uplift and ~50% recovery on soft declines on average
• Pay-ins and payouts through the same API, with centralized reconciliation

Proof: Livelo (+5% approval, 50% recovery), Rappi (80% less payment-analyst resolution time), InDrive (fast multi-PSP activation).

Worth 20 minutes next week to size the recoverable revenue? I have Tuesday or Thursday open.

— German
Yuno
```

---

### APPENDIX — Source URLs
```
[S1] https://www.similarweb.com/website/feetfinder.com/
[S2] https://www.semrush.com/website/feetfinder.com/overview/
[S3] https://x.com/FeetFinder/status/1488257130062757888
[S4] https://x.com/FeetFinder/status/1488605844191133696
[S5] https://www.tryfootly.com/blog/is-feetfinder-safe-2026
[S6] https://rewarble.com/insight/what-is-feetfinder-and-how-does-it-work
[S7] https://ecommercefastlane.com/how-to-make-money-on-feetfinder/
[S8] https://feetfinder.pissedconsumer.com/review.html
[S9] https://www.tryfootly.com/blog/feetfinder-income-real-creator-earnings-2026
[S10] https://www.tryfootly.com/blog/feetfinder-fees-explained-hidden-costs-2026
[S11] https://www.tryfootly.com/blog/why-creators-are-leaving-feetfinder-for-footly-2026
[S12] https://arceusx.net/feetfinder-app-download/
[S13] https://www.creditsafe.com/business-index/en-us/company/feetfinder-us149682718
[S14] https://prospeo.io/c/feetfinder-revenue
[S15] https://variety.com/2025/digital/news/onlyfans-fiscal-2024-revenue-earnings-1236495750/
[S16] https://corepay.net/articles/which-payment-processor-does-just-for-fans-use/
[S17] https://medium.com/authority-magazine/patrick-nielson-of-feetfinder-5-things-i-wish-someone-told-me-before-i-became-a-founder-b7bbbc8c21d
```
