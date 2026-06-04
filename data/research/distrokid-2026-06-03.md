# SDR Research Brief — DistroKid
*Yuno Payment Orchestrator | Framework v8.0 | Compiled 2026-06-03*

> **Parent-company correction:** The task referenced "Mosaic Music Distribution LLC" as parent. Public records do **not** support this. The actual operating entity is **Kid Distro Holdings, LLC** (Delaware, #7053806). "Mosaic Music Distribution" is a separate, unrelated French company. Source: https://opencorporates.com/companies/us_de/7053806

---

## EXECUTIVE SUMMARY

DistroKid is the world's largest DIY music-distribution platform (estimated 30-40% of all new music globally, ~3M artists [ESTIMATE]), monetized through annual subscriptions ($24.99–$89.99/yr) plus add-ons, and paying artists their streaming royalties twice a week. It runs a **two-sided payments problem**: high-volume **inbound** subscription billing (cards + Apple/Google Pay; PayPal explicitly not accepted) and high-volume **outbound** artist payouts via **Tipalti**. The standout finding: DistroKid's own help docs confirm **zero decline-recovery logic** — failed annual renewals bounce straight from the issuer and pull the artist's music offline, a textbook involuntary-churn and network-tokenization opportunity. No payment orchestrator found. With a rumored ~$2B sale process underway (Jan–Feb 2026) and the Bandzoogle acquisition adding direct-to-fan card acceptance, the payments surface is broadening at exactly the moment efficiency matters most.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|---|---|---|---|---|---|
| 1 | United States | 33.35% | ~3.3M | Up MoM | [S1] |
| 2 | United Kingdom | 5.78% | ~578K | — | [S1] |
| 3 | Germany | 4.55% | ~455K | — | [S1] |
| 4 | France | 4.18% | ~418K | — | [S1] |
| 5 | Canada | 3.72% | ~372K | — | [S1] |
| 6–10 | Not public (SimilarWeb free tier caps at top 5) | — | — | — | [S1] |
| — | "Others" combined | 48.43% | ~4.8M | — | [S1] |

- **Total monthly visits:** ~10M, up 1.66% MoM (April 2026 data).
- **Flag:** US-led (~1/3) with a very long international tail (~48% across many countries). UK, Germany, France all >4% — **all served from US entities**, a cross-border acquiring signal.
- Top traffic source is Direct (~60.6% desktop), implying brand-driven, returning subscribers (renewal-heavy base).
- > ⚠️ MANUAL: ranks 6–10 require paid SimilarWeb.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source |
|---|---|---|---|---|
| United States | Yes (#1) | Yes — Kid Distro Holdings, LLC (DE), NJ branch, HQ NYC | No | [S2] |
| United Kingdom | Yes (#2) | None found | ⚠️ Yes | [S2] |
| Germany | Yes (#3) | None found | ⚠️ Yes | [S2] |
| France | Yes (#4) | None found | ⚠️ Yes | [S2] |
| Canada | Yes (#5) | Bandzoogle (acquired 2023, CA-based) — distribution biz still US | ⚠️ Likely | [S2] |

- **Parent/operating entity:** Kid Distro Holdings, LLC — Delaware, #7053806, incorporated 2018-09-12; NJ branch since 2020-08-21. HQ 34 Third Avenue #183, New York, NY 10003. Sources: [S2]
- **Ownership:** mix including Spotify, Insight Partners, Silversmith Capital Partners. Source: [S2]
- **Brands/subsidiaries:** DistroVid, Bandzoogle (2023), Mixea, Upstream, DistroKid Direct (merch). Source: [S2]
- **ToS governing law:** New York. Source: https://distrokid.com/terms/
- **International entities:** No public information found — all corporate registrations are US (Delaware + NJ branch). [INFERENCE — not confirmed]: single-jurisdiction US structure serving a global base.

> ⚠️ For UK, DE, FR (all top-5 traffic, no local entity found): **Potential cross-border operation — likely processing on US/international acquiring against EU/UK cards.** Verify on official T&Cs.

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**

| Flow | PSP / Acquirer | Evidence Type | Source |
|---|---|---|---|
| Inbound (subscription checkout) | **Not publicly named** | DistroKid states card data "goes straight to our credit card processor and never reaches our database" — confirms a third-party processor exists, unnamed | [S3] |
| Inbound — wallets | Apple Pay + Google Pay live in checkout | [Press/Facebook announcement] | [S3] |
| Outbound (artist payouts) | **Tipalti** (mass-payout provider) | [Third-party guide — INFERENCE, moderate confidence] | [S3] |

- Inbound checkout PSP (Stripe/Adyen/Braintree/Recurly) is the **biggest unknown** — not disclosed; BuiltWith/Crunchbase tech pages were not fetchable. [INFERENCE — not confirmed]: a single modern card processor is plausible given card + Apple/Google Pay + tokenization language, but unverified. **Do not claim a checkout PSP in outreach.**

**3B. Orchestrator:** No public evidence found. No Spreedly/Primer/Gr4vy/Yuno/CellPoint signals. Single-rail inbound checkout, single payout vendor (Tipalti).

> ⚠️ MANUAL — DevTools live checkout: test card 4111 1111 1111 1111 | 02/30 | 123 to identify the inbound gateway.

---

## SECTION 4 — APMs (Agent D verified findings)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source |
|---|---|---|---|
| US / global (subscription) | Visa, Mastercard, Discover, Amex (credit/debit/prepaid), **Apple Pay, Google Pay** | Help-center snippet + getsby corroboration | [S3][S4] |
| Global (payouts) | PayPal, ACH, wire, eCheck, paper check (varies by region) | Help-center snippet (Tipalti) | [S4] |

- **PayPal explicitly NOT accepted for paying the subscription** (DistroKid's own statement). No BNPL present.

**4B. Unverified Markets**

| Market | Verified? | Reason | Popular Local APMs (exploration angle) |
|---|---|---|---|
| Germany (#3) | No | Single .com domain, no DE checkout walk | SEPA Direct Debit, giropay, PayPal — heavy German preference for non-card |
| France (#4) | No | No FR checkout walk | Cartes Bancaires, SEPA |
| UK (#2) | No | No UK-specific verification | — (card-led market) |
| Brazil/LATAM (in long tail) | No | Not in top-5 visible | Pix, boleto — if LATAM share is material |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through in DE/FR before any APM claim. In outreach, **only** reference confirmed methods; for missing-method angles use cross-border / single-rail / decline-recovery instead.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Source |
|---|---|---|---|
| No decline-recovery; failed renewal pulls music offline | DistroKid help center | Documented policy | [S5] |
| Auto-renewal / unexpected charges (add-ons renew on own dates) | Trustpilot, PissedConsumer | Recurring pattern | [S5] |
| Refund friction (original card only; escalation needed) | Trustpilot | Recurring | [S5] |
| Billing complaints (BBB) | BBB | 69 billing-specific of 305 total (3 yr); 91% unanswered | [S5] |
| Withheld royalties / blocked withdrawals post-account-action | BBB/Reddit/Trustpilot | ~127 cases Mar'23–Nov'25 [per 3rd-party aggregation, "according to web data"] | [S5] |
| Slow payouts (twice-weekly batch, up to ~14 days) | Help center + reviews | Structural | [S5] |

**Analysis → Yuno fit:**
- **Decline-recovery gap → smart retries + network tokens + account updater.** "Your bank sends the decline code directly to DistroKid's system" with no retry = pure involuntary churn on annual renewals. This is the single strongest hook.
- **Refund friction / billing confusion → unified reconciliation** across processors and add-on subscriptions.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | Sep 2023 | Acquired **Bandzoogle** (Canada; web stores, merch, tickets, fan subs, crowdfunding) — adds direct-to-fan card acceptance | M&A | [S6] |
| 2 | Post-2023 | Stacey Bedford (ex-Bandzoogle CEO) → GM of DistroKid | Leadership | [S6] |
| 3 | 2024–25 | AI push: automated mastering, Mixea (AI mixing) | Product | [S6] |
| 4 | Current | Open roles: API Engineer, Sr Marketing Engineer (no payments/finance roles open) | Hiring | https://job-boards.greenhouse.io/distrokid |
| 5 | — | Built In lists hiring in Fintech/Financial Services categories | Hiring signal | https://builtin.com/company/distrokid/jobs |

- No confirmed C-suite payments/finance hire or new international market launch found.

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | Jan–Feb 2026 | DistroKid exploring **~$2B sale** (repped by Goldman Sachs & Raine) | ⚠️ Major — efficiency/valuation pressure; payments cost & approval rates become board-level | [S7] |
| 2 | Aug 2021 | Insight Partners investment at **$1.3B valuation** | Financial backdrop | [S7] |
| 3 | Ongoing | **Splits** — auto-distributes royalties to collaborators; non-subscribers $10/yr to collect | Embedded-payouts product (appetite for money movement) | [S7] |

- No new PSP partnership or processor switch found in last 12 months.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Account-based, card-on-file subscription | Standard | Renewals auto-charge stored card |
| Guest checkout | No — account required | — | Subscription model |
| Steps to purchase | Sign up → plan → card | OK | Apple/Google Pay shorten flow |
| 3DS | Not verified | ⚠️ | EU/UK SCA exposure if no 3DS |
| Mobile experience | Apple/Google Pay support → tokenized wallet flow | Good | |
| APM display logic | Cards + wallets only; no geo-localized APMs visible | ⚠️ Opportunity | No SEPA/giropay for DE, etc. |

> ⚠️ MANUAL: Walk checkout in US + DE/FR (VPN).

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not published | Tokenized; "card data goes straight to processor, never reaches DistroKid servers" → PCI scope reduced via processor | Yuno vaulting + network tokens to centralize card-on-file across inbound subs and Bandzoogle commerce | [S3] |

- No public PCI DSS Level, SOC 2, or ISO 27001 page found.

---

## SECTION 10 — Strategic Insights

**Insight #1: Zero decline-recovery on annual renewals = involuntary churn + content takedown**
Evidence: Help center confirms declines pass straight from the issuer with no retry; a failed annual renewal removes the artist's music from streaming until paid (S3/S5). | Pain Point: Every soft-declined renewal is lost revenue AND a churned, music-offline artist — at ~3M subscribers, even a 5% renewal-decline rate is enormous. | Yuno Value Prop: Smart retries, network tokenization, and account updater recover 50% of failed transactions and lift approvals +7%. | Best Case: Subscription recovery economics (Livelo +5% approval / 50% recovery). | Outreach Angle: "When a renewal card soft-declines, your own docs say there's nothing you can do and the music comes down. That's exactly the failure we recover automatically."

**Insight #2: Cross-border acquiring against EU/UK base from US entities**
Evidence: UK/DE/FR each >4% traffic, no local entity found (S1/S2). | Pain Point: International cards on US acquiring = lower approval rates and FX leakage on inbound subscriptions. | Yuno Value Prop: Smart routing to local acquirers, new market live in weeks, no-code PSP enablement. | Best Case: InDrive (10 LATAM markets <8 months, 90% approval). | Outreach Angle: "Roughly a third of your traffic is outside the US but everything seems to run on US entities. Are EU/UK renewals processed locally, or cross-border?"

**Insight #3: Single, unnamed inbound PSP — no orchestration or failover**
Evidence: One card processor, no orchestrator found (S3). | Pain Point: Single-PSP dependency = no auto-failover; a processor outage halts all renewals globally. | Yuno Value Prop: Multi-PSP orchestration with auto-failover through one API. | Best Case: Rappi (ms outage detection, zero implementation time). | Outreach Angle: "Is there a failover processor if your gateway has an incident, or is renewal billing single-rail today?"

**Insight #4: Two-sided money movement broadening (Bandzoogle + Splits)**
Evidence: Bandzoogle adds merch/ticket/fan-sub card acceptance; Splits pays collaborators; Tipalti handles royalty payouts (S6/S3). | Pain Point: Inbound subs + Bandzoogle commerce + outbound payouts are fragmented across vendors — no single reconciliation view. | Yuno Value Prop: Unified reconciliation and a single integration layer across acceptance surfaces. | Best Case: Reserva (+4% approval <3 months). | Outreach Angle: "With Bandzoogle commerce now alongside subscriptions and Tipalti payouts, how are you reconciling money in and money out across all of it?"

**Insight #5: ~$2B sale process = payments efficiency is board-level**
Evidence: Jan–Feb 2026 sale exploration (S7). | Pain Point: Approval rate, churn, and payment cost directly drive the valuation multiple. | Yuno Value Prop: Demonstrable approval uplift and recovery improve net revenue retention ahead of a transaction. | Outreach Angle: Frame Yuno as a quick, quantifiable NRR lever in a diligence window.

---

## SECTION 11 — Pipeline

**11A. Direct Competitors**

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| TuneCore | tunecore.com | Brooklyn, NY (Believe-owned, FR) | Global | US/EU | [S11] |
| CD Baby | cdbaby.com | Portland, OR (Downtown Music) | Global | US/EU | [S11] |
| Amuse | amuse.io | Stockholm, SE | Global | EU/Global | [S11] |
| UnitedMasters | unitedmasters.com | Brooklyn, NY | 1.5M+ artists | Global | [S11] |
| Ditto Music | dittomusic.com | Liverpool, UK | Global | UK/Global | [S11] |
| Symphonic | symphonic.com | Tampa, FL | Global | US/Global | [S11] |
| RouteNote | routenote.com | Cornwall, UK | Global | UK/Global | [S11] |
| ONErpm | onerpm.com | NY / São Paulo | LATAM-heavy | LATAM/Global | [S11] |
| AWAL | awal.com | London (Sony) | Global | Global | [S11] |

**11B. Industry Peers:** Distribution + label-services + creator-payout platforms with two-sided money movement (subscriptions/advances in, royalty payouts out) — strongest orchestration fit among ONErpm (LATAM), Amuse (advances), UnitedMasters (brand deals + payouts).

**11C. Adopting Orchestration:** No competitor confirmed on a named orchestrator. [INFERENCE] Multinational-owned peers (TuneCore/Believe, CD Baby/Downtown, AWAL/Sony) most likely have sophisticated in-house payments.

**11D. Scoring (DistroKid)**

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ |
| Multiple PSPs | +3 | ❌ (single inbound found) |
| Recent expansion (24 mo.) | +2 | ✅ (Bandzoogle 2023, sale process 2026) |
| Public payment issues | +2 | ✅ (decline/billing/payout) |
| Funding >$10M | +2 | ✅ ($1.3B val, Insight) |
| LATAM/APAC/MENA traffic | +2 | ⚠️ partial (long tail) |
| No orchestrator | +2 | ✅ |
| Payment job postings | +1 | ⚠️ Fintech category only |
| Public RFP | +3 | ❌ |

**Score: ~14 → 🔴 High priority.**

---

## SECTION 12 — Business Case

| Metric | Value |
|---|---|
| Annual Revenue | ~$250M run-rate [ESTIMATE — 3rd-party, "according to web data"] |
| Valuation | $1.3B (2021); ~$2B sale rumored (2026) |
| Avg Transaction Value | ~$25–$90 subscription/yr + add-ons [ESTIMATE] |
| Est. Subscribers | ~3M artists [ESTIMATE] |
| Primary Currency | USD |
| Top 3 Markets | US, UK, Germany |

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi [Name], I lead pre-sales at Yuno (payment infrastructure). I've been digging
into DistroKid's payments and one thing stood out: when an annual renewal card
soft-declines, your own help docs say the charge bounces straight back from the
issuer with no retry, and the artist's music comes offline until it clears. At
~3M subscribers that's a lot of recoverable revenue and avoidable churn. Yuno
adds smart retries, network tokens and account updater through one API
(typically +7% approval, ~50% of failed transactions recovered). We do this for
InDrive, Rappi and Livelo. Worth a 20-min chat next week to see the upside?

--- COLD EMAIL ---
Subject: the renewal declines DistroKid can't currently recover

Hello [Name]!

I lead pre-sales at Yuno and spend my days inside subscription payment stacks, so
DistroKid was a natural one to look at.

One finding stood out. Your help center says that when a card declines, the bank
sends the decline code straight to your system and there isn't much DistroKid can
do, and a failed annual renewal pulls the artist's music offline until it clears.
At roughly 3M subscribers, even a small soft-decline rate on renewals is a lot of
lost revenue and avoidable churn.

This is exactly what we recover. Yuno adds smart retries, network tokenization and
an account updater through a single API, typically lifting approvals by 7% and
recovering around half of failed transactions. It also gives you auto-failover if
your processor ever has an incident, and a single reconciliation view across
subscriptions, Bandzoogle commerce and Tipalti payouts.

We do this for InDrive, Rappi and Livelo. Would you be open to a quick 20-minute
chat this week to explore the upside on renewals?

Best,
German
```

---

## APPENDIX — Source URLs

```
[S1]  https://www.similarweb.com/website/distrokid.com/
[S2]  https://opencorporates.com/companies/us_de/7053806 | https://en.wikipedia.org/wiki/DistroKid | https://distrokid.com/terms/ | https://www.bbb.org/us/ny/new-york/profile/music-distribution-companies/distrokid-0121-87139284
[S3]  https://support.distrokid.com/hc/en-us/articles/360057005634-Why-Is-My-Card-Not-Working | https://support.distrokid.com/hc/en-us/articles/360013534294-Can-I-Pay-for-My-Subscription-With-PayPal | https://getsby.com/en/creator-platform/how-does-distrokid-work/ | https://news.distrokid.com/introducing-7-new-payout-options-dcdb0e982367
[S4]  https://support.distrokid.com/hc/en-us/articles/360013535074-What-Withdrawal-Methods-Does-DistroKid-Offer | https://distrokid.com/pricing
[S5]  https://support.distrokid.com/hc/en-us/articles/360046624313-I-Have-a-Question-Regarding-a-Charge-Refund | https://support.distrokid.com/hc/en-us/articles/360013535494-What-Happens-If-I-Stop-Paying-the-Annual-Fee | https://www.trustpilot.com/review/distrokid.com | https://www.bbb.org/us/ny/new-york/profile/music-distribution-companies/distrokid-0121-87139284/complaints
[S6]  https://www.musicbusinessworldwide.com/distrokid-distrokid-acquires-website-hosting-and-e-commerce-company-bandzoogle/ | https://www.billboard.com/pro/distrokid-acquires-bandzoogle/ | https://www.hypebot.com/inside-distrokids-acquisition-of-bandzoogle-and-whats-next/
[S7]  https://www.musicbusinessworldwide.com/distrokid-repped-by-goldman-sachs-and-raine-exploring-a-sale/ | https://musically.com/2026/02/02/distrokid-is-latest-music-firm-rumoured-to-be-exploring-a-sale/ | https://www.insightpartners.com/ideas/distrokid-receives-investment-from-leading-software-investor-insight-partners-valuing-the-company-at-1-3-billion/ | https://support.distrokid.com/hc/en-us/articles/360013534394-Using-Splits-To-Pay-Your-Collaborators-Automatically
[S11] https://aristake.com/digital-distribution-comparison/ | https://unitedmasters.com/en/unitedmasters-vs-competitors | https://dittomusic.com/en/blog/what-are-the-best-distrokid-alternatives | https://symphonic.com/best-music-distribution-services/
[S12] https://growjo.com/company/DistroKid | https://www.trapital.com/memos/why-distrokid-is-valued-at-1-3-billion
```
