# Suno & Yuno call, Aug 7 2026 (2:00pm ET / 3:00pm ET actual start ~2:58pm ET) — summary from transcript

Attendees: German Tatis, Justo Benetti, Madden Titus, Gurwinder Gulati, "Yuno Notetaker" (auto-attached). Duration 34:13. Source: Google Meet transcript, https://docs.google.com/document/d/1cbe-_MIYAQHVWdlzXUCAajngZdNQ-J7ilhdCEmc0e7c/edit

## ⚠️ COMPLIANCE FLAG — resolve before any further Suno contact
Madden opened the call stating: "We at Sunno are not allowed to have AI notetakers or recorders on any meeting." Justo replied "No problem, perfect." A "Yuno Notetaker" nonetheless appears in the attendee list and a full verbatim transcript was generated and emailed to German. This is a real trust/compliance risk if Suno discovers it. Flag to Justo immediately; do not forward/reuse this transcript externally.

Note: only a Transcript doc was linked in the meeting-records email (no Video Recording chip, unlike the Aug 6 email which had both). No video was available to review.

## Org facts confirmed live
- Madden: 4 days at Suno (not 5). Gurwinder: ~1.5 months at Suno, prior role in "membership payments" (Uber One, matches research).
- They are literally the entire payments/billing/commerce team; have not yet had a 1:1 with each other.
- Madden's origin story: an ex-colleague in data science reached out ~4 months ago after a "big fraud attack" ~5 months ago (~Mar 2026); Madden advised hiring a fraud ops/data science person, was eventually hired himself. Fraud is "mostly managed" now; current focus is involuntary churn and acquisition.

## Stack confirmed / new intel
- Stripe fully-hosted checkout page, Stripe Radar for fraud, 3DS "fully managed" via Stripe.
- Single US entity confirmed directly by Madden: "I'm pretty confident we only have a US entity."
- NEW: they use RevenueCat to manage Apple/Google IAP subscriptions. RevenueCat's webhook went down THE DAY OF THIS CALL, causing active pain ("causing us a bunch of pain").
- Madden: "there's basically no tech debt... because there's nothing there" (payments infra is greenfield; some subscription/entitlement logic still to unwind).
- Direct confirmation of the core BC thesis: Madden named Japan/PayPay specifically as a live, acknowledged gap: "Stripe doesn't support recurring with that pay method." Also: "Stripe has a really bad retry scheduler" (renewal continuity thesis confirmed in his own words).
- Madden's own pre-meeting mental model walking in: "get a global player in as the second one... adyen, checkout, a Chase" — literally Option A from the Decision Frame slide. Justo's answers (fewer hops, one API vs point solutions) implicitly addressed this without walking the slide by name.
- Gurwinder's technical question: whether smart routing handles vaulting/network tokens/recurring or just exposes raw access. Justo confirmed: vaulting, network tokens, account updater, all in-API; raw + normalized data; "smart 3DS engine" behind 15 different 3DS providers (regional performance varies, weak in LatAm called out).
- Gurwinder's stated product priority: wants OUT of native Apple/Google subscription orchestration long-term; wants a centralized wallet/token layer across web + app-store payment methods while retaining control of orchestration. Direct match to Yuno's pitch.
- German contributed live: Apple ~30%/Google ~15% store fees, and that Suno's iOS price is higher than web (both already verified facts, delivered well).

## The number, said out loud
Justo: "at least adding 12 million a year in subscription revenue, but I think it could be a lot more."
Madden: "I think you're underselling yourself honestly based on everything you were talking about."
Model landed exactly on target; Madden's reaction is that it's likely conservative, not inflated.

## Litigation disclosure (material for deal velocity)
Madden proactively acknowledged the UMG/Sony litigation and said: "our lawyers are pretty heads down on a bunch of stuff too figure out how contracting stuff works." Read: the litigation isn't just legal/financial risk to Suno, it is actively consuming the legal bandwidth needed to sign a new vendor contract. Factor this into timeline expectations.

## Justo's disclosures about other clients (pattern to watch)
In front of Suno, Justo named: OpenAI (active APM/distribution deal work, described tactically), Sora (Yuno is backend for all its transactions), Whop (meeting next week in NY, cited their $3B TPV), Anthropic (took a year to get a meeting), plus Uber, Starlink, GoFundMe as scale references. None of this was in the prepped talk track. Given the prior Riot Games incident (an email shared externally without permission), this is a pattern worth flagging to Justo, not something German controlled in the moment.

## Madden's concrete asks (actionable now)
1. Case studies: "a story of hey, we took a company who was Stripe billing only and we did this with them."
2. White papers, data, anecdotes for his internal pitch.
3. Reference calls (Justo offered these instead of white papers as the better path).

## What did NOT happen
No hard date was set for the technical session with Gurwinder or the two-week data sprint (the brief's stated ask). Close was soft: "we'll send these materials... we'll be in touch," with a loose mention of possibly meeting in NY next week. **This is the most urgent open follow-up: get a specific date on the calendar, don't let it float.**

## Immediate next actions
- [ ] Raise the notetaker/compliance issue with Justo today.
- [ ] Draft and send the case-study / reference-call follow-up Madden asked for.
- [ ] Push for a specific date for the technical session + data sprint kickoff; do not wait for Suno to initiate.
- [ ] Update CRM/pipeline stage to reflect: first live meeting held, quantified case validated ($12M, reaction positive), team is 2 people (Madden + Gurwinder), litigation flagged as a contracting-speed risk.
