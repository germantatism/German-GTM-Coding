# Meeting Brief: Yuno <> Acebet (Oct 27, 2026) · v2

- **When:** Tuesday Oct 27, 2026, 11:00 to 11:25 PT (25 minutes)
- **Link:** meet.google.com/xpe-rihd-ybf · phone +1 423-707-2717, PIN 570917024
- **Organizer:** Melissa Pottenger (Yuno) · **Lead:** German Tatis

**Objective:** Confirm Boris's orchestration plan across Breeze, Coinflow and a third PSP. Show that Yuno already runs Coinflow in production and can add Breeze and a third provider behind one integration. Leave with a technical working session booked this week and the KYC/KYB pack started.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed (never state in the call) · ❓ ask in discovery.

> ⚠️ **PRE-MEETING ACTIONS**
>
> 1. **Ask the integrations squad about Coinflow health.** The Coinflow api-int QA suite in #qa-reports-api-int has failed every morning this week, with 20 to 21 of 64 tests failing on 20 to 27 Oct. Get a one-line status before promising anything on Coinflow. Internal only.
> 2. **Ask how long a Breeze connector would take.** Breeze is not in Yuno's provider catalog (docs.y.uno provider list). Do not give a timeline on the call without a number from integrations.
> 3. **Legal pre-check still applies.** Golden Frog Inc. holds an Anjouan licence. Both Breeze and Coinflow act as merchant of record, which may change what Yuno's KYC has to cover ⚠️. Post a heads-up in #salesops-legal.
> 4. **Boris still has not accepted the invite.** Ask Melissa to confirm he will attend and to share his surname and company email.
> 5. **Roles:** German leads end to end. Melissa opens with 30 seconds on why she connected us. Sean handles the senior close if needed. Justo covers partners and commercial questions.

---

# STUDY ZONE

## 0. New context from Melissa (27-Oct, 10:28)

| What Melissa said | What it means for the call |
|---|---|
| Boris is **one of the founders** of Acebet | ✅ A decision maker is in the room. Skip the "who decides" questions and go straight to the plan |
| Acebet is "a large gaming operator **going live with Coinflow**" | Coinflow is not live yet. ❓ Ask the go-live date and what Coinflow covers (cards, wallets, ACH, crypto) |
| They are **evaluating gateways** and asked for an intro to Yuno | Inbound interest. They want to be sold a solution, not convinced the problem exists |
| They do **about $20M GMV today** | ❓ Ask per month or per year. Do not assume. It changes the pricing tier entirely |
| They want to **orchestrate across Breeze, Coinflow and potentially another PSP** | They have already decided to orchestrate. The question is build it themselves or use Yuno |
| **Breeze and Coinflow are MoR providers**, similar to Xsolla or Coda | Both providers take merchant-of-record liability. Yuno would route between MoRs, not acquirers |

**What we know about each provider**

| Provider | What it is | Status with Yuno |
|---|---|---|
| **Coinflow** | Chicago-based payments company. Takes cards and wallets and settles in stablecoins, with chargeback indemnification. $25M Series A in Oct-2025 led by Pantera Capital (blockworks.co) | ✅ **In Yuno's provider catalog** (COINFLOW, docs.y.uno). ✅ **Live in production** with Whop (crypto, US) and Felix Pago (card account-funding). ✅ Partner contract signed, partner manager Melissa Pottenger. ✅ Partner sheet lists Coinflow as accepting **gambling in the US**: Card, Apple Pay, Google Pay, Cash App Pay, ACH, Wire, Crypto. ✅ Coinflow chargeback protection is built into Yuno's iOS SDK (v2.5.0 changelog) |
| **Breeze** | Merchant of record for games and apps, founded 2022. Handles payments, fraud, chargebacks, tax and compliance through one API, fiat and crypto. Third-party profiles claim over $1B processed a year ⚠️ unverified | ⚠️ **Not in Yuno's provider catalog.** It would be a new connection. ✅ The "breeze" key in Acebet's code is this provider (cards, Amex, Apple Pay, Google Pay, ACH, instant bank on acebet.cc) |
| **Third PSP candidates** | Partner sheet entries that are signed and accept US gambling | ✅ **Checkout.com** (cards, Apple Pay, Google Pay, PayPal, Venmo, ACH, SEPA, Klarna, card and bank payouts; partner manager Melissa). ✅ **CoinsPaid** (crypto). Coda Payment is an MoR in the sheet but flagged as not accepting gambling, and its contract is unsigned |

**So what for the call:** we are not pitching orchestration as an idea. Boris has already chosen it. Our edge is that one of his two providers already runs live on Yuno. The open risks are Breeze, which needs building, and licence and KYC appetite.

## 1. TL;DR Battle Card

**Five facts to know cold**

1. ✅ **Boris is a co-founder** and wants to orchestrate across Breeze, Coinflow and possibly a third PSP. Both providers are merchants of record.
2. ✅ **Coinflow already runs on Yuno in production** (Whop, Felix Pago), and the partner sheet marks it as accepting US gambling. **Breeze is not in Yuno's catalog yet.**
3. ✅ **About $20M GMV today** ❓ period unknown. US sweepstakes site acebet.cc has about 6.7M visits a month (94% US). The real-money site acebet.co has about 371K (Germany 62%). SimilarWeb, Sep-2026.
4. ✅ **Three entities.** Golden Frog Inc. (Anjouan licence 15831) runs acebet.co. 51 Plus One Ltd (Cyprus) manages payments. Trey Mark Services Ltd (Cyprus) runs acebet.cc.
5. ✅ **Payouts are the public pain.** About 60% of 105 Trustpilot reviews are about withdrawal delays, blocked cash-outs or KYC loops.

**Three hooks, in priority order**

1. **"Coinflow is already live on Yuno."** Going live with Coinflow through Yuno means one integration that then reaches Breeze and the third PSP too, instead of a second direct build.
2. **Routing and failover between MoRs.** Send each transaction to the MoR most likely to approve it, at the best cost. Retry on the other when one declines or goes down.
3. **One view of payouts and reconciliation** across Breeze, Coinflow and crypto, with real-time monitoring.

**The objection he will raise:** "Why not just build the switch between Breeze and Coinflow ourselves?"
**The answer:** "You can build the first switch in a sprint. Then it needs retries, failover, decline-code mapping, reporting, reconciliation and a third provider. That's the part that never ends. With Yuno, Coinflow is already done, and every provider after it is configuration, not code."

**The ask:** a technical working session this week with Yuno solutions, to map Breeze, Coinflow and the third PSP. The KYC/KYB pack starts in parallel.

**Rapport opener:** "Congrats on going live with Coinflow. What made you pick them?" Or: "Slot Battles is a different idea. How has it landed since April?"

## 2. Who Is in the Room

| Name | Role | Side | Status / history |
|---|---|---|---|
| Boris (surname unknown), borissaidme@gmail.com | **Co-founder** (per Melissa, 27-Oct) | Acebet | Invite "needs action". No prior meeting, email or Slack trace ✅ |
| Melissa Pottenger | Organizer; partner manager for Coinflow and Checkout.com | Yuno | Accepted. Booked the meeting on 26-Oct and supplied the context in section 0 |
| Sean Calabro | Head of North America | Yuno | Accepted. Forwarded the invite to German on 26-Oct with "if you can join" |
| Justo Benetti | Commercial | Yuno | Accepted |
| German Tatis | Senior AE, **leads the call** | Yuno | Accepted |

**Boris, profile.** Co-founder of Acebet, per Melissa ✅. No public profile could be built: Acebet names no executives, and searches by email handle and by "Boris" with each Acebet entity returned nothing. Without a surname, LinkedIn cannot be searched.

- ⚠️ **How to read him:** a founder who has already picked two merchants of record and decided to orchestrate. He knows payments, wants specifics, and will judge Yuno on how concrete it is. Talk providers, routing rules and timelines, not vision.
- ❓ Get his surname, which entity he signs for, and who runs payments engineering day to day.

**Intro path.** Boris asked for an intro to Yuno while evaluating gateways, and Melissa booked it ✅. Melissa manages the Coinflow partnership, so the intro may have come through Coinflow ⚠️ (ask Melissa before the call).

**Relationship timeline.**

- No prior meeting with any attendee of this call exists on the calendar. The calendar was searched by Boris's email, by "Boris" and by "Acebet" for 2025 to 2026, and the only hit is this invite ✅.
- No Gmail threads with Boris or any Acebet, Golden Frog, Trey Mark or 51 Plus One address. No Slack mentions. No Gong CRM account ✅.
- **Implication:** first meeting, but inbound and warm. They have received no Yuno material.

**Other known contacts in the account:** none. Acebet publishes no leadership, and no payments job postings were found on LinkedIn or Pentasia ✅.

---

## 3. The Company

**What they do.** Crypto-native online casino and sportsbook, "built by crypto-native gamblers" and launched in 2025 ✅. It offers casino content through Hub88 (Evolution, Pragmatic Play, Hacksaw, Nolimit City, BGaming, Play'n GO, NetEnt and others), a sportsbook through Betby, in-house "Originals" and PvP Slot Battles. Login works by account or crypto wallet (Phantom, Solflare, Coinbase Wallet, Trust) ✅. A separate US sweepstakes site (Gold Coins and Sweeps Coins) runs in 39 states ✅.

| Metric | Value | Source |
|---|---|---|
| Launch | Nov-2025 (acebet.co); LinkedIn page says founded 2024 | mightytips.com; linkedin.com/company/acebet |
| Monthly visits, acebet.co | ~371K, -11.4% MoM (Sep-2026) [ESTIMATE] | SimilarWeb |
| Monthly visits, acebet.cc | ~6.7M, -11.3% MoM (Sep-2026) [ESTIMATE] | SimilarWeb |
| Top markets, acebet.co | Germany 62%, US 19%, Spain 7%, France 4%, Canada 2% | SimilarWeb |
| Headcount | 51 to 200 self-declared; 4 visible on LinkedIn | LinkedIn |
| Game library | 2,000+ casino games, 35+ sports, esports | review sites |
| Trustpilot | acebet.com 2.7 (433 reviews); acebet.co 2.2 (80 reviews, unclaimed) | trustpilot.com |
| Platform | Proprietary multi-tenant Next.js build ⚠️; no SOFTSWISS, Altenar, BetConstruct or Digitain strings | site code |

**Corporate structure and subsidiaries**

| Entity | Jurisdiction | Role | Source |
|---|---|---|---|
| Golden Frog Inc., reg. 15831 | Anjouan, Union of Comoros | Owner and operator of acebet.co; "authorized to conduct online gaming operations by the Anjouan Offshore Financial Authority" ✅ | acebet.co footer (Wayback 3-Oct-2026) |
| 51 Plus One Ltd, Strovolos, Nicosia | Cyprus | "Financial transactions are managed by 51 Plus One Ltd". The FAQ calls it "our subsidiary" ✅ | acebet.co licensing page |
| Trey Mark Services Limited, HE481956, Nicosia | Cyprus | Owner and operator of acebet.cc and acebet.gg (US sweepstakes). The FAQ says "Trey Mark Holdings Ltd." ✅ | acebet.cc |
| German sweepstakes tenant (Trey Mark Holdings Ltd, AMOE address in Offenbach) | Germany (address) | Free-to-play sweepstakes variant found in the acebet.co code ✅. ⚠️ This probably explains the 62% German traffic | acebet.co code |
| Golden Frog Ltd., Mutsamudu, Anjouan | Anjouan | Data controller per the privacy policy, which also says data is "controlled by Golden Frog in the United States". The pages are inconsistent | privacy policy |

- The licence and registration numbers are the same (15831). The Anjouan register could not confirm it because the page is client-rendered ✅.
- A 22-Apr-2026 article says the Central Bank of the Comoros does not recognise such offshore licences ✅ (briefglance.com).
- The T&Cs restrict the US, UK, Netherlands, Switzerland, Cyprus, Cayman Islands and Comoros, and a representation clause adds Germany, Spain, France, Austria and Australia. Those are three of the top four traffic markets ✅. Do not raise this in the call. It is a legal question for Yuno, not a talking point.

**Leadership and strategy themes.** No executives are named anywhere ✅. Themes visible from the product: speed of launch (three products in six months), crypto-first identity, US access through the sweepstakes model, and markets built into code ahead of traffic (Interac, PIX, SEPA, ACH, IMPS, payouts in AR, CL, CO, MX and PE) ✅.

---

## 4. Financials

Acebet is private and offshore. No revenue, profit, funding, investors or valuation is public ✅. A 10-year trajectory does not exist because the company launched in November 2025.

| Item | Value | Basis and source |
|---|---|---|
| Revenue, last full year | Not public | n/a |
| Funding | None found | Crunchbase-style searches returned nothing |
| Traffic, combined | ~7.1M monthly visits (Sep-2026), both sites down about 11% MoM | SimilarWeb [ESTIMATE] |
| Margin proxy | acebet.cc affiliate programme pays 30% to 45% revenue share, hybrid CPA, monthly negative-balance reset | acebet.cc/affiliate-program |
| Ticket size proxies | Lowest acebet.cc package $5; redemption cap $9,500 per day; withdrawal limit $9,000 per transaction | acebet.cc FAQ; AskGamblers [Review Site] |
| Payment cost borne by players | Swapped.com on-ramp fees of 1.75% (Visa) to 6.7% (e-wallets); an "additional fee imposed by our payment provider at checkout" | sportsgambler.com; acebet.co code |

**Category context (US sweepstakes, where the volume sits).** Eilers & Krejcik estimate about $14.3B in Gold Coin sales in 2025 and $4B to $5B net operator revenue, as cited by Track360 [weak source]. California's ban took effect on 1-Jan-2026, and some reports put California at nearly 20% of sector revenue. Oklahoma's ban takes effect on 1-Nov-2026, and lines.com reports sector revenue down about $1B in 2026 from the ban wave.

**So what for the call:** traffic is falling on both sites and the US sweepstakes market is shrinking state by state. Conversion per visit and cost per transaction therefore matter more each month. Frame Yuno around approvals, payout speed and fee pass-through, not around growth they might not have.

---

## 5. Competitive Landscape

Acebet competes in two arenas: crypto-first real-money casinos (acebet.co) and US sweepstakes casinos (acebet.cc).

| Competitor | Segment | Est. market share (source · basis) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Stake | Crypto casino | ~45% of tracked on-chain deposits among 24 operators, Q2-2026 (Tanzanite via VIP-Grinders · deposit-volume share) | $5.11B deposits Q2-2026; $4.7B GGR 2024 [media-reported] | Category leader, sponsorships, Curacao | Praxis Tech orchestrator since Nov-2025 ✅ |
| Roobet | Crypto casino | ~11% to 12.5% (DappRadar · 24-hour deposit snapshot) | $1.18B deposits Q2-2026, -46% QoQ (Tanzanite) | Streamer-led marketing | Not found |
| Shuffle | Crypto casino | ~10% to 11% (DappRadar · 24-hour deposit snapshot) | $578M deposits Q2-2026, +10% QoQ (Tanzanite) | Token airdrops for loyalty; founded 2024 | MoonPay on-ramp ✅ |
| BC.Game | Crypto casino | ~6% to 9% (DappRadar · 24-hour deposit snapshot) | $432M deposits Q2-2026 (Tanzanite) | Anjouan; 40 fiat currencies; PIX, UPI, Interac | Not found |
| Rollbit | Crypto casino | No estimate available | $152M deposits Q2-2026, -22% QoQ (Tanzanite) | Moved toward trading products | Not found |
| Gamdom | Crypto casino | No estimate available | 26 deposit methods, 23 languages (AskGamblers) | Curacao; crypto-only withdrawals | PayPal, Trustly, Skrill deposits |
| Rainbet | Crypto casino | No estimate available | Founded 2025; SimilarWeb lists it as an Acebet audience-affinity site | Anjouan, the closest licence peer | MoonPay on-ramp, PIX, Interac ✅ |
| VGW (Chumba, LuckyLand, Global Poker) | US sweepstakes | VGW plus RSI (Pulsz) ~45% combined (tech-insider.org · basis not stated) | About A$7.3B FY2025 revenue (Track360, reported, unaudited) | Largest sweepstakes group | Not found |
| Pulsz (Rush Street Interactive) | US sweepstakes | Included in the combined ~45% above | RSI is listed; Pulsz revenue not broken out | Backed by a regulated US operator | Not found |
| Stake.us | US sweepstakes | No estimate available | Track360 "category leader" tier | Same brand as the crypto leader | Not found |
| McLuck | US sweepstakes | No estimate available | Track360 "category leader" tier | Big slots catalogue | Not found |
| Crown Coins Casino | US sweepstakes | No estimate available | Exited Tennessee after a cease-and-desist (Track360) | Mobile-first | Not found |

Caveats: the deposit-share figures cover only operators that on-chain trackers can label, so they are not revenue share. The DappRadar figures are single-day snapshots and swing with activity. The sweepstakes share figure comes from one article with no stated method.

**Where Acebet sits.** acebet.co is a small player in crypto casinos. Its ~371K visits are a fraction of the leaders, and no deposit-share estimate exists for it. acebet.cc's ~6.7M visits put it in the mid tier of US sweepstakes ⚠️ (by traffic only, no revenue data).

**For the call:** Stake, the category leader, moved onto an orchestrator (Praxis) in November 2025. "Your largest competitor already orchestrates" is a factual peer signal you can use. Do not name Praxis as a competitor to beat unless Boris raises it.

---

## 6. Payments Money Map

**Orchestrator status:** none today. Boris plans to orchestrate across Breeze, Coinflow and a third PSP ✅ (per Melissa). None found in the code of either site. Each provider has its own key, hosted redirect ("Your payment will be processed through [provider name]") and fee notice ✅. ⚠️ Reads as in-house method selection by region.

**Providers by function** (from the acebet.co code snapshot of 3-Oct-2026 and the live acebet.cc code; vendor identities behind short keys are ⚠️ unless the page names the vendor)

| Function | Providers |
|---|---|
| Crypto deposits and custody | Fireblocks ✅; Mesh ("meshconnect") ⚠️; wallet connect (Phantom, Solflare, Coinbase Wallet, Trust, Ledger and others) ✅ |
| Fiat-to-crypto on-ramp | Swapped.com ✅ |
| Cards, Interac, PIX, Open Banking | "paytech" (BASIC_CARD, INTERAC, PIX, Open Banking) ⚠️ vendor unconfirmed |
| US cards, wallets, ACH | **Breeze**, merchant of record (Visa, Mastercard, Amex, Apple Pay, Google Pay, ACH, instant bank transfer) ✅ confirmed by Melissa |
| Going live | **Coinflow**, merchant of record ✅ per Melissa |
| Instant bank (EU/UK) | peer.xyz for Revolut and Wise ✅ |
| Other deposit rails | Kinguin gift cards ✅; Zen, paycom, memepay, skindeck, des (USD) ⚠️ |
| Payouts | MassPay, PayPal, "cdn-software" (USD); SEPA, Visa Payout, Mastercard Payout ✅; "tx-tech" bank transfers in AR, CL, CO, MX, PE, plus card and IMPS ⚠️ |
| US sweepstakes extras | Whop ACH, Venmo and PayPal rails ✅ |
| KYC / fraud | Sumsub ✅; Sift ✅ |
| Content | Hub88 and ALEA aggregators; Betby sportsbook ✅ |

**Fraud and 3DS:** 3DS posture not verified. Sift is in the code. KYC is usually triggered at first withdrawal and has taken about 7 business days in one user report ✅.

**Hiring signals:** none (no payments roles on LinkedIn or Pentasia) ✅.

**Peer context:** Stake uses Praxis Tech (since Nov-2025). Shuffle, Rainbet and Cloudbet use the MoonPay on-ramp. No peer evidence of Spreedly, Primer or Gr4vy ✅.

**Methods by market** (confirmed in operator pages or code only; the live cashier could not be walked because of a Cloudflare challenge and the login wall)

| Market | Methods confirmed |
|---|---|
| Global (acebet.co) | Visa, Mastercard, Apple Pay, Google Pay, Revolut, Wise, Kinguin gift cards; 20+ cryptos including USDT and USDC on six chains each, PYUSD, DAI |
| Canada | Interac |
| Brazil | PIX |
| EU | SEPA, Open Banking |
| AR, CL, CO, MX, PE | Bank-transfer payout keys only |
| India | IMPS payout key only |
| US (acebet.cc) | Visa, Mastercard, Amex, Google Pay, Apple Pay, ACH, instant bank transfer, crypto; redemptions to Visa, Mastercard, ACH, bank transfer, crypto |

**Framing rules for this account**

- Never say they lack a method. Not verified does not mean not available.
- Never mention the licence, the restricted-country conflicts or Trustpilot scores in a judgmental way. Use "players care most about payout speed" rather than "your reviews are bad".
- Do not show that we read their code. Say "from what is visible on your site" and ask them to confirm providers.
- PayPal is a wallet, not a PSP.

---

## 7. Top Markets

| Market | Share of acebet.co visits | Payment behaviour | For the call |
|---|---|---|---|
| Germany | 62% | Bank-led market (SEPA, open banking) with PayPal and Sofort/Klarna popular ⚠️ (general market knowledge) | ❓ Confirm whether German players get the sweepstakes tenant or real money. That decides which rails matter |
| United States | 19% (.co) plus 94% of acebet.cc | Cards and ACH; high decline rates for gaming-coded transactions ⚠️ | The volume market. Ask about card approval rates on Gold Coin purchases |
| Spain | 7% | Cards and Bizum ⚠️ | ❓ Ask whether Spain is served on real money |
| Canada | 2% | Interac confirmed in their code ✅ | Interac is already live. Ask how it performs versus cards |
| Brazil | 1.2% of acebet.cc | PIX confirmed in code ✅ | Possible expansion lever. Ask about plans |

---

## 8. News & Signals (newest first)

| Date | Item | Use |
|---|---|---|
| 1-Nov-2026 (upcoming) | Oklahoma sweepstakes ban takes effect (Track360) | ⚠️ Ask whether acebet.cc is affected. Do not assert |
| Oct-2026 | acebet.cc runs October slot challenges with 75 to 250 SC prizes (next.io); promo code ALARM offers 10 free SC plus a 200% purchase bonus (fantasyalarm.com) | Shows active US acquisition spend |
| 16-Oct-2026 | thegamehaus.com: "Acebet.cc is no longer recommended" (no reason given) | Internal context only |
| Q2-2026 | Crypto casino deposits: Stake $5.11B (-10% QoQ), Roobet -46%, Rollbit -22%, Shuffle +10% (Tanzanite via VIP-Grinders) | Category is consolidating |
| 2026 | US sweepstakes revenue reported down about $1B on state bans (lines.com) | Pressure on the US business |
| 22-Apr-2026 | Coverage of Slot Battles calls the Anjouan licence "highly problematic" (briefglance.com) | Internal risk context only |
| 4-Apr-2026 | PvP Slot Battles launch; 1,300 players and 22,000 rounds in the first weeks (operator claim) | Rapport opener |
| 1-Jan-2026 | California ban on dual-currency sweepstakes takes effect (Track360) | ⚠️ acebet.cc's excluded-state list does not include California. Leave to legal, do not raise |
| 25-Jan-2026 | Reported GlobeNewswire release for the acebet.cc US launch (could not be verified) | Context |
| Nov-2025 | acebet.co launch | Context |

Nothing from the last 7 days that works as a rapport opener.

---

## 9. Selling Yuno Here

**Core frame:** "You've already decided to run more than one merchant of record. Yuno is the layer that makes that work: one integration, Coinflow already live on it, Breeze and a third provider added as configuration, with routing, failover, payouts and reporting across all of them."

**Hooks with proof points** (published Yuno results only)

1. **Coinflow is already live on Yuno.** Production traffic for Whop and Felix Pago. Name Whop only if asked for references, and check with Melissa first ⚠️.
2. **Approvals and recovery.** Up to 7% approval uplift and 30% recovered revenue (y.uno).
3. **Speed to add providers and markets.** inDrive reached about 90% approval and went live in 11 new countries in under eight months on one integration (y.uno).
4. **Monitoring.** Rappi detects payment anomalies in milliseconds instead of 5 to 10 minutes manually, with 80% less analyst resolution time.
5. **Stablecoins and crypto.** Yuno bridges fiat and crypto rails and sells a Stablecoins product (y.uno). Coinflow settles in stablecoins.

**Landmines (what NOT to say)**

- Do not say Breeze is "supported" or give a timeline for it. It is not in the catalog.
- Do not say Yuno is an MoR or takes chargeback liability. Breeze and Coinflow do that.
- Do not quote prices or MDRs. The GMV period is unknown and legal has not cleared the entities.
- Do not mention the Anjouan licence, the restricted-country conflicts, Trustpilot scores or reviewer delistings.
- Do not reveal that we read their site code. Say "from what is visible on your site".
- Do not mention the Coinflow QA failures or name other Yuno merchants beyond the public logos without checking.
- Do not say "you don't have X" about any method or market.

## 10. Be Ready For

| He may ask | Ready answer |
|---|---|
| "Do you already integrate Coinflow?" | "Yes. Coinflow is in our catalog and live in production with other merchants today. You'd be connecting to something that already runs." |
| "Do you integrate Breeze?" | "Not yet. It's not one of our live connectors. Let me get you a firm timeline from our integrations team rather than guess. That's one of the outputs of the working session." |
| "What would you suggest as the third PSP?" | "It depends on what you want it to fix: cards approval, a market or payouts. Our partner network has providers that accept gaming in the US, and we'd map options against your volume in the working session." Do not name partners as committed. |
| "Can you route between two MoRs?" | "Yes. Each MoR is a connection in Yuno. Rules decide which one gets each payment, by country, method, card type, amount or approval history, with automatic fallback to the other." |
| "How much does it cost?" | "It depends on volume and mix. Is the $20M monthly or annual? Once we have that and the provider split, we'll send a proposal. The model is a platform fee plus a per-transaction fee." No numbers. |
| "How long to go live?" | "One integration on your side. Because Coinflow is already a Yuno connector, that piece is configuration. Breeze depends on the build, which we'll confirm." |
| "Can you onboard us given our licence?" | "Compliance reviews every gaming merchant by entity and licence. Send me the entity details and I'll come back with a clear answer." Do not say yes or no. |
| "Do you do payouts?" | "Yes. Yuno has a Payouts product, and routing and monitoring cover payouts as well as pay-ins." |
| "PCI and card data?" | "Our hosted checkout and SDK keep card data out of your scope. Cards are tokenized in Yuno's vault." |
| "Who else in gaming uses you?" | "Garena, Moon Active and NetEase are public names. Others we can discuss under NDA." |
| "Why not build the switch ourselves?" | "You can build version one. Retries, failover, decline mapping, reporting, reconciliation and every new provider after that are the part that never ends. We give you that on day one." |

---

# LIVE ZONE

## 11. Call Plan: German Leads

**Goal of the 25 minutes:** confirm the plan, prove Yuno fits it, and book the working session. Talk 30% of the time, listen 70%.

**1. Open (minute 0 to 3).** Melissa takes 30 seconds to introduce. Then you say:
> "Thanks Boris. Melissa gave us the headline: you're going live with Coinflow, you already work with Breeze, and you want to orchestrate across both and maybe a third PSP. I'd like to spend most of the time on your plan, show you where Yuno fits, and agree whether a deeper technical session makes sense. Does that work?"

Then the rapport opener: "Congrats on going live with Coinflow. What made you pick them?"

**2. Discovery (minute 3 to 12).** Ask the five must-ask questions below in order. Write the answers in the Notes column. If he gives a long answer, let him finish.

**3. Position Yuno (minute 12 to 19).** Three points only, tied to what he said:
> "First, Coinflow is already a live connector on Yuno, so that piece is configuration, not a build."
> "Second, Yuno routes each payment to whichever MoR is most likely to approve it at the best cost, and falls back automatically when one declines or goes down."
> "Third, you get one view of payments, payouts and reconciliation across Breeze, Coinflow and crypto, with monitoring that catches problems in milliseconds."

Be straight about Breeze: "Breeze isn't a live connector yet. I'll get you a firm timeline from our integrations team."

**4. Handle his questions (minute 19 to 22).** Use the Be Ready For table. If you don't know, say "Let me confirm and come back today."

**5. Close (minute 22 to 25).**
> "Here's what I'd suggest: a 45-minute technical session this week with our solutions team. We'd map how Breeze, Coinflow and a third provider would sit behind Yuno, and what go-live looks like. In parallel, we'll send our KYC list so compliance isn't the long pole. Does Thursday or Friday work?"

Get a date before hanging up. Confirm who from his side joins.

**Say this**

- "You've already decided to orchestrate. We make that decision cheaper to run."
- "Coinflow is already live on Yuno."
- "Configuration, not code, for every provider after the first."
- "Let me confirm and come back today." (whenever unsure)

**Don't say this**

- Anything that promises Breeze support or a timeline.
- Any price, MDR or discount.
- Anything about their licence, reviews or what we saw in their code.
- "Yuno is an MoR" or "we take the chargeback risk".
- Unpublished stats or merchant names beyond Garena, Moon Active and NetEase.

**If the call goes sideways**

- **He wants a price now:** "Happy to. I need the GMV period and the split by provider first. I'll send a range within 48 hours of the session."
- **He's only shopping for a third PSP:** "We can help with that too. Our partner network covers gaming in the US. Orchestration is what lets you switch between them without new code each time."
- **He asks about licence or compliance:** "Our compliance team reviews every gaming merchant. Send me the entity details and I'll come back with an answer."

## 12. Agenda (25 minutes)

| Minute | Block | Owner | Notes |
|---|---|---|---|
| 0 to 3 | Melissa intro (30 seconds). German frames the call and asks the opener | Melissa, German | Notes: ____ |
| 3 to 12 | Five must-ask questions | German | Notes: ____ |
| 12 to 19 | Three Yuno points: Coinflow live, routing and failover across MoRs, one view of payouts and reporting | German | Notes: ____ |
| 19 to 22 | His questions | German (Justo on partners and commercial) | Notes: ____ |
| 22 to 25 | Close: technical session this week plus KYC pack. Get a date | German (Sean backs up) | Notes: ____ |

## 13. Discovery Questions

**Must-ask (in this order)**

1. "Walk me through the plan: what does Breeze handle today, what will Coinflow handle, and what's the third PSP for?"<br>Notes: ____
2. "When does Coinflow go live, and are you integrating it directly or waiting to do it through an orchestrator?"<br>Notes: ____
3. "Is the $20M GMV per month or per year, and how does it split between the US sweepstakes site, the real-money site and crypto?"<br>Notes: ____
4. "How do you want to route between Breeze and Coinflow: by country, payment method, card type, approval rates or cost?"<br>Notes: ____
5. "What does success look like in 90 days, and who besides you is involved in choosing the gateway?"<br>Notes: ____

**If time allows**

6. "Which entity would sign with us: Golden Frog, 51 Plus One or Trey Mark?"<br>Notes: ____
7. "What approval rates do you see today on Breeze, and where do you lose the most?"<br>Notes: ____
8. "How do payouts work today, and are they in scope for the orchestration?"<br>Notes: ____
9. "Which other gateways are you evaluating, and when do you want to decide?"<br>Notes: ____

## 14. Post-Meeting Checklist

- [ ] Recap email to Boris the same day: his plan in his words, the three Yuno points, the session date and the KYC/KYB list.
- [ ] Ask integrations for a Breeze connector estimate and the current Coinflow status.
- [ ] Post entities, licence and the MoR model in #salesops-legal for a pre-check (Golden Frog Inc., 51 Plus One Ltd, Trey Mark Services Ltd).
- [ ] Ask Melissa and Justo about third-PSP options (Checkout.com, CoinsPaid) for US gambling.
- [ ] Pricing: run the GMV figure through the Finance pricing policy before any number goes out.
- [ ] Create the Salesforce opportunity and log the outcome.
- [ ] Update memory (project_acebet) and the research brief.

---

## Appendix: Sources

- Meeting invite: Google Calendar event "Yuno <> Acebet", 27-Oct-2026; Gmail forward from Sean Calabro, 26-Oct-2026
- Full research brief: data/research/acebet-2026-10-26.md (every source URL listed there)
- https://web.archive.org/web/20261003012735/https://acebet.co/
- https://web.archive.org/web/20260422185930/https://acebet.co/policies/licensing
- https://web.archive.org/web/20260130031420/http://acebet.com/policies/terms-of-service
- https://web.archive.org/web/20260128131925/http://acebet.com/policies/privacy-policy
- https://acebet.cc/ · https://acebet.cc/affiliate-program
- https://www.similarweb.com/website/acebet.co/ · https://www.similarweb.com/website/acebet.cc/
- https://www.trustpilot.com/review/acebet.com · https://www.trustpilot.com/review/acebet.co
- https://www.askgamblers.com/online-casinos/reviews/acebet-casino
- https://www.linkedin.com/company/acebet
- https://briefglance.com/articles/acebets-pvp-slot-battles-innovation-on-a-shaky-regulatory-foundation
- https://www.sportsgambler.com/review/acebet/ · https://www.thespike.gg/reviews/acebet-co · https://www.mightytips.com/bookmakers/acebet/
- https://thegamehaus.com/igaming/reviews/acebet-cc/
- https://next.io/win/us/acebet-cc-casino-challenges-to-win-rewards-in-october-2026/
- https://www.fantasyalarm.com/articles/promotions/acebet-promo-code-bonus/196376
- https://www.vip-grinders.com/research/crypto-casino-market-report/
- https://dappradar.com/narratives/gambling/page/3/?cur=BTC
- https://bitquery.io/investigations/on-chain-casino-stake-market-share
- https://track360.io/blog/crypto-gambling-statistics-2026
- https://track360.io/blog/sweepstakes-casino-market-report-2026-size-growth-operators
- https://track360.io/blog/vgw-sweepstakes-operator-group-portfolio-analysis-2026
- https://tech-insider.org/de/igt-us-sweepstakes-operator-tech-stack-disclosure-analysis-de-d174/
- https://www.lines.com/sweepstakes-casino-revenue-down-1b-in-2026-ban-wave
- https://www.askgamblers.com/online-casinos/reviews/bc-game-casino · https://www.askgamblers.com/online-casinos/reviews/rainbet-casino · https://www.askgamblers.com/online-casinos/reviews/shuffle-casino · https://www.askgamblers.com/online-casinos/reviews/gamdom-casino
- https://praxis.tech/ · https://partnerkin.com/en/b2b/payment-orchestration/
- https://www.y.uno/
- Melissa Pottenger context message, 27-Oct-2026 10:28
- https://docs.y.uno/reference/api-enums (provider list, COINFLOW) · https://docs.y.uno/changelog/ios (Coinflow chargeback protection)
- Slack #partnerships--sales, Payments Concierge partner sheet answers 22-Oct and 27-Oct-2026 · #product-tech Coinflow tickets (Whop 3-Mar-2026, Felix Pago 25-Feb-2026) · #qa-reports-api-int Coinflow suite 20 to 27-Oct-2026
- https://blockworks.co/news/coinflow-raise-stablecoin-payments
- https://thegrid.id/profiles/breeze · https://assetstore.unity.com/packages/sdk/breeze-payment-sdk-7562841


*Google Doc v2 (current): https://docs.google.com/document/d/1AIvBmnjJSLBt99ir6r_gmu48ojjp9oXJwQ2ZououPf4/edit · v1 renamed OLD: 18ufiAJlRHgtFg20E_bk_GkbGgrLUU1JSft5tNT_P6MA*
