# Meeting Brief: Yuno <> Suno (Technical Deep Dive)
*Sep 3, 2026 — condensed brief per German's request*

## Header

**Meeting:** Suno + Yuno | Technical Deep Dive
**Date/time:** Thursday, September 3, 2026, 2:00-3:00 PM Colombia Time (COT) / 3:00-4:00 PM Eastern (EDT)
**Link:** meet.google.com/smf-ocwt-wdw
**Organizer:** German Tatis
**Objective:** This is a technical product walkthrough, Jarrett presents. Winning this meeting means the NDA moves forward and a specific date gets locked for the data sprint/sandbox access, both stalled since the Aug 7 call.

### ⚠️ Pre-meeting actions
- **NDA was promised on Aug 7 ("happy to work off yours or send ours over") but was never actually sent.** No NDA thread exists in Gmail. This blocks any data sprint. Send it before or at the top of this call.
- **Reference calls promised Aug 14 were never delivered.** Madden asked for these directly; address this gap in the meeting or right after.
- Madden Titus and Jarrett Falasco have not accepted the calendar invite (status: needsAction). Confirm both are actually joining.
- **Ben Rawstron** was just added as an optional attendee and is unknown to us. Research shows he's a Senior Full Stack Engineer (from Secureframe, compliance/PCI-automation background), his LinkedIn hasn't been updated to Suno yet, meaning a very recent hire. He's likely the person Suno just hired for the "Billing & Subscription" role (renamed "Commerce Platform" on their careers page). Treat him as a technical evaluator, possibly the new billing engineer himself.
- **No AI notetaker on this call.** Madden explicitly banned AI notetakers/recorders on Aug 7; Yuno's own Notetaker joined anyway and recorded the full call, an unresolved trust risk. Turn it off manually before joining.

---

## 1. TL;DR Battle Card

**Five facts to know cold:**
1. Suno's payments team is two people (Madden, Gurwinder) plus a brand-new third hire (likely Ben Rawstron), assembled within the last ~2 months. They are actively building, not maintaining a finished stack.
2. Confirmed stack: Stripe hosted checkout + Radar + 3DS on web, RevenueCat for Apple/Google IAP on mobile, single US legal entity, no orchestrator, and a job posting confirms an in-progress migration to a ledger-based billing model.
3. Suno's new downloads/credits purchase policy goes live today, September 3, adding a metered, pay-as-you-go purchase layer on top of subscriptions on Pro and Premier tiers, a brand-new high-frequency checkout surface.
4. On the Aug 7 call, Gurwinder stated in his own words that he wants out of native Apple/Google subscription orchestration long-term and wants a centralized wallet/token layer across web and app-store payment methods while keeping control of orchestration, this is the Yuno pitch, verbatim, from the buyer himself.
5. Madden accepted the $12M/year business case as conservative on the call ("I think you're underselling yourself"), and named "Stripe has a really bad retry scheduler" as a live pain point in his own words.

**Three hooks, in priority order:**
1. Gurwinder's own ask: a unified token/wallet layer across Stripe (web) and RevenueCat (app stores), so Suno keeps orchestration control instead of being locked into two disconnected systems.
2. The new downloads/credits purchase flow launching today is a fresh, unoptimized checkout surface, an ideal pilot candidate for smart routing and recovery before bad patterns get baked in.
3. Confirmed recurring-payment gaps: Japan/PayPay doesn't support recurring on Stripe (Madden's own words), plus discovery-stage questions on Pix Automatico and UPI Autopay as Suno's Brazil/India volume grows.

**THE objection they will likely raise + the answer:** Given they just hired a dedicated billing engineer and are mid-migration to a new ledger, expect "we're already building this ourselves, why add another vendor." Answer: position Yuno as the layer that sits under their new ledger and unifies Stripe plus RevenueCat, not a replacement for the engineer they just hired, their build gets easier, not redundant.

**The ask:** Get the NDA moving today and lock a specific date for the data sprint. Both stalled after Aug 7, don't let this call end the same way.

**Rapport opener:** The new downloads policy going live the exact day of this meeting is a genuine, low-effort opener, ask how the rollout is going rather than leading with a pitch.

---

## 2. Who Is in the Room

| Name | Role | Side | Status |
|---|---|---|---|
| Gurwinder Gulati | Payments/billing, ex-Uber (UberOne Membership Payments TL), ex-Netflix Ads Eng | External | Accepted |
| Madden Titus | Payments/fraud, ex-Director Payments & Fraud PM at Disney Streaming, ex-Netflix | External | Needs action |
| Ben Rawstron | Unknown Suno title, Senior Full Stack Engineer (ex-Secureframe) | External, optional | Needs action |
| German Tatis | Account Executive | Internal (Yuno) | Accepted |
| Jarrett Falasco | Sales Engineer, presenting | Internal (Yuno) | Needs action |

**Gurwinder Gulati** (linkedin.com/in/gurwindergulati, confirmed at Suno): ~12 years experience, University of Washington CS, joined Suno late June 2026. Career: UberOne Membership Payments (Tech Lead) → Netflix Ads Engineering → LinkedIn (built a Lucene-based search engine) → Facebook → Hulu. Every company on his resume builds payments in-house, so he defaults to a build bias, but he explicitly told us on Aug 7 he wants to buy the orchestration layer while keeping control. He interrogates API surface and failure modes, not commercial terms.

**Madden Titus** (linkedin.com/in/madden-t-2378aa38, confirmed at Suno): Yale Executive MBA (2022-24), NYC, joined Suno ~Aug 3-4, 2026 (4 days in on the Aug 7 call). Career: Netflix payments/fraud analytics → Disney Streaming, Director of Payments and Fraud Product Management. His own framing walking into the Aug 7 call was "get a global player in as the second one, Adyen, Checkout, a Chase", he's already thinking in orchestration terms.

**Ben Rawstron** (linkedin.com/in/ben-rawstron, profile still shows Secureframe, not yet updated to Suno): Boston University Computer Engineering, NYC. Career: Alarm.com (IoT device engineering) → Secureframe (compliance automation for SOC 2/ISO 27001/PCI), Senior Full Stack Engineer. ⚠️ Unconfirmed, but the timing and location match Suno's own job posting for a "Staff Software Engineer, Billing & Subscription" (since renamed "Commerce Platform" on their careers page), first dedicated billing hire, owns Stripe and RevenueCat integrations end to end, leading a migration to a ledger-based billing model. If this is him, he's the person actually building what Yuno would sit under. Safe opener: ask if he's the one who just picked up billing.

**Relationship timeline:** Not a first meeting. Full history: cold outreach from Feb 2026, LinkedIn thread with Jasper van Rijckevorsel, first live call Aug 7 (34 min, positive, $12M case accepted as conservative), case studies sent Aug 14 (Whop, GoFundMe, Rappi, Mercado Libre), no reply since. This technical session was the explicit next step from Aug 7 and has been pending three weeks.

---

## 3. The Company

Suno, AI music generation, ~$300M ARR and ~2M paid subscribers (reported Feb 2026), $400M Series D at $5.4B valuation (June 2026), reportedly building toward IPO readiness (Music Business Worldwide, July 2026). Single US legal entity, confirmed directly by Madden on Aug 7. Full company and financial detail already covered in the original research brief (`data/research/suno-2026-08-06.md`), not repeated here per the request to keep this brief short and technical.

**Legal context relevant to deal velocity:** UMG and Sony litigation remains unsettled, settlement talks hit an impasse (reported Apr 2026) and claims expanded to over 61,000 alleged infringements (reported May 2026), case now in discovery with trial expected late 2026. Madden already told us this is consuming his legal team's bandwidth for vendor contracting, expect this to still be true. A German court (Munich, Jul 31, 2026) ruled for GEMA and ordered Suno to disclose revenue linked to the infringement, adding a European revenue-reporting burden on top of the US litigation.

---

## 4. Financials (condensed)

$300M ARR, ~2M paid subscribers (Feb 2026) · $400M Series D at $5.4B valuation (Jun 2026) · Pro tier $8/mo, Premier $24/mo per the live pricing page as of Aug 31, 2026 (earlier reporting cited $10/$30, worth a light confirming question, not an assertion). **So what for the call:** they are scaling a subscription business while bolting on a new metered-purchase layer today, both funded and moving fast, but their payments team is two months old and mid-rebuild, timing favors getting in now, before architecture decisions calcify around a single-PSP design.

---

## 5. Payments Money Map

**Confirmed stack, live and unchanged since Aug 7:**
- **Web:** Stripe fully-hosted checkout, Stripe Radar for fraud, 3DS fully managed via Stripe.
- **Mobile app stores:** RevenueCat manages Apple and Google IAP subscriptions. RevenueCat's webhook went down the day of the Aug 7 call, causing active pain, a live redundancy argument.
- **Legal entity:** single US entity, confirmed directly by Madden.
- **Currencies:** 17 confirmed (USD, AUD, BRL, CAD, EUR, GBP, IDR, INR, JPY, KRW, MXN, NOK, PLN, SEK, THB, TRY, UAH).
- **No orchestrator.** A recent Suno job posting (since renamed from "Billing & Subscription" to "Commerce Platform") confirms an in-progress migration to a ledger-based billing model, owning Stripe and RevenueCat integrations end to end. This is Ben Rawstron's likely role.

**New as of today:** Suno's updated downloads policy (effective Sep 3) introduces purchasable add-on credits on Pro and Premier tiers on top of the flat subscription, a metered, high-frequency, small-ticket purchase flow layered onto existing billing, live the same day as this meeting.

**Confirmed gaps, in their own words or verified:**
- Japan/PayPay: Stripe doesn't support recurring with that method (Madden, Aug 7, direct quote).
- Involuntary churn: "Stripe has a really bad retry scheduler" (Madden, Aug 7, direct quote), matches the core recovery thesis of the business case.
- Pix is live in Brazil per German's own account intel (not documented in Suno's public help center), but no confirmation of Pix Automatico (recurring Pix), worth a direct discovery question rather than an assertion.
- UPI Autopay (recurring UPI in India) status unconfirmed, same treatment, ask rather than assert.

**Gurwinder's technical requirements, stated directly on Aug 7:** does smart routing handle vaulting, network tokens, and recurring natively, or just expose raw access. He wants a centralized wallet/token layer across web and app-store methods while retaining orchestration control. Jarrett should have concrete, specific answers ready on vaulting, network tokens, account updater, and the 3DS engine (15+ regional providers, LatAm coverage was flagged as comparatively weaker on Aug 7, be ready to acknowledge honestly rather than oversell).

---

## 6. News & Signals

| Date | Item | Source |
|---|---|---|
| Sep 3, 2026 | **Downloads/ToS policy update goes live, same day as this meeting.** Free tier capped at 7 lifetime downloads, Pro 20/month, Premier 60/month, no rollover, purchasable add-on credits on Pro/Premier. | suno.com/pricing, musicbusinessworldwide.com |
| Aug 21, 2026 | Blog post on artist profiles/identity on platform | suno.com/blog |
| Aug 13, 2026 | Studio 2.0 launched (browser DAW, Premier-exclusive, unlimited downloads outside the cap) | suno.com/blog |
| Aug 12, 2026 | Licensing partnership announced with BMG (second licensor after the Warner settlement) | suno.com/blog, variety.com |
| Aug 10, 2026 | Downloads policy update first announced (effective Sep 3) | suno.com/blog, musicbusinessworldwide.com |
| Aug 6, 2026 | Responsible-AI post: audio watermarking, fingerprinting, tighter download policy | digitalmusicnews.com, variety.com |
| Jul 31, 2026 | Munich court rules for GEMA, orders Suno to disclose infringement-linked revenue, judgment not final | twobirds.com, variety.com |
| May 2026 | UMG/Sony expand claims to 61,000+ alleged infringements | digitalmusicnews.com |
| Apr 2026 | UMG settlement talks hit an impasse over fees/equity | digitalmusicnews.com |

No news found in the last 7 days beyond the scheduled Sep 3 policy launch itself, that launch is the opener.

---

## 9. Selling Yuno Here

**Core frame:** Suno is actively assembling a payments org and rebuilding their billing architecture right now, not defending a finished system. Position Yuno as the orchestration layer that sits under their new ledger and unifies Stripe (web) and RevenueCat (app stores) into the single token/wallet layer Gurwinder already asked for, not a replacement for the engineer they just hired to build it.

**Hooks with proof points:**
- Gurwinder's own stated want (unified wallet/token layer, retained orchestration control), lead with his words back to him.
- Involuntary churn / retry recovery, tied directly to his colleague Madden's "bad retry scheduler" quote. Proof points: Livelo (+5% approval, 50% recovery).
- New downloads/credits flow launching today as a live pilot candidate for smart routing before patterns calcify. Proof point: Reserva (+4% approval in under 3 months, fast to show results).
- Real-time monitoring vs. manual, relevant to a two-person team that can't staff 24/7 payments ops. Proof point: Rappi (zero implementation time, 80% less analyst resolution time).
- Case studies already sent Aug 14 (Whop, GoFundMe, Rappi, Mercado Libre), Jarrett should reference these as already-delivered, not resend them cold.

**Landmines, what NOT to say:**
- No AI notetaker or recorder joins this call, full stop.
- Don't suggest replacing the work of the engineer they just hired, frame as infrastructure under the rebuild.
- Don't repeat the Aug 7 pattern of naming other clients (OpenAI, Sora, Whop's TPV, Anthropic) unprompted, flag to Justo if it comes up again.
- Don't raise the UMG/Sony litigation or the Nov 2025 data breach unprompted, sensitive, let Suno raise it.
- Don't assert Pix Automatico or UPI Autopay are missing, ask instead.

---

## 10. Be Ready For

| They may ask | Ready answer |
|---|---|
| Does your vaulting expose raw access or handle tokens/network tokens/account updater natively? | Full in-API vaulting, network tokens, and account updater; both raw and normalized data available (confirm this is still accurate with Jarrett before the call) |
| How does your 3DS engine perform across regions, especially LatAm? | Smart 3DS engine spanning 15+ regional providers; LatAm performance is comparatively weaker, be honest about this rather than oversell |
| Can Yuno sit under a ledger-based billing rebuild already in progress? | Yes, Yuno integrates via API regardless of the underlying ledger model, no need to rip out Stripe or pause the rebuild |
| Can you unify web (Stripe) and native IAP (RevenueCat/Apple/Google) under one token layer? | Yes, this is the exact capability Gurwinder asked about on Aug 7, confirm the specific demo is ready before this call |
| What's implementation timeline for a two-person, newly-formed payments team? | Reference Rappi's zero-implementation-time case; give a realistic timeline given their current bandwidth |
| What's your PCI/security posture? | Standard Yuno PCI DSS answer; Ben Rawstron's Secureframe background (compliance automation) means expect a sharper-than-usual compliance question |
| Where's the NDA? | Address directly and get it moving today |

---

## 11. Agenda (60 minutes)

| Time | Block | Notes |
|---|---|---|
| 0:00-0:05 | Intros, confirm attendee roles, quick NDA status check | ____ |
| 0:05-0:15 | Recap Aug 7 outcomes, ask what's changed on their side (ledger migration, new hire) | ____ |
| 0:15-0:40 | Jarrett product walkthrough: vaulting, tokens, account updater, 3DS, smart routing, retries | ____ |
| 0:40-0:55 | Technical Q&A / discovery | ____ |
| 0:55-1:00 | Next steps: NDA, data sprint date, reference calls | ____ |

---

## 12. Discovery Questions

1. Since Aug 7, where has the ledger-based billing migration landed, and does the new hire lock in architecture decisions we should design around? Notes: ____
2. The new downloads/credits purchase flow launched today, is that running on Stripe already, or is this the right moment to pilot an alternate rail specifically on it? Notes: ____
3. On the recurring gaps we flagged (Japan/PayPay, Pix Automatico, UPI Autopay), which markets are actually driving volume today so we prioritize correctly? Notes: ____
4. Where do things stand on the NDA, do you want to work off Yuno's template or send yours? Notes: ____
5. Can we lock a specific date for the data sprint and sandbox access today, rather than leaving it open again? Notes: ____

---

## 13. Post-Meeting Checklist

- Send recap email same day
- Follow up explicitly on the NDA and the still-undelivered reference calls
- Lock the data sprint date in the calendar, don't let it go soft again
- Update memory with confirmed titles (Gurwinder, Madden, and whether Ben Rawstron is the new billing/commerce hire)

---

## Appendix — Sources

```
Deals/Suno/call-transcript-summary-2026-08-07.md (internal, Aug 7 call)
suno.com/pricing
suno.com/blog
musicbusinessworldwide.com (downloads policy, UMG impasse, Sony/UMG claims expansion)
variety.com (BMG deal, GEMA ruling)
digitalmusicnews.com (responsible-AI post, litigation updates)
twobirds.com (GEMA/Munich court ruling)
help.suno.com (currencies, payment methods)
linkedin.com/in/gurwindergulati
linkedin.com/in/madden-t-2378aa38
linkedin.com/in/ben-rawstron
Suno careers page (Commerce Platform / Billing & Subscription role)
data/research/suno-2026-08-06.md (full account research, not repeated here)
```
