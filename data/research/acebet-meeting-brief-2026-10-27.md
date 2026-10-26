# Meeting Brief: Yuno <> Acebet (Oct 27, 2026)

- **When:** Tuesday Oct 27, 2026, 11:00 to 11:25 PT (25 minutes)
- **Link:** meet.google.com/xpe-rihd-ybf · phone +1 423-707-2717, PIN 570917024
- **Organizer:** Melissa Pottenger (Yuno)

**Objective:** Learn who Boris is and which Acebet entity he speaks for. Map how deposits and payouts run today. Leave with a booked 30-minute working session with Yuno solutions and a KYC/KYB pack (entities, licences, UBOs) moving in parallel.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed (never state in the call) · 🔍 ask in discovery.

> ⚠️ **PRE-MEETING ACTIONS**
>
> 1. **Boris has not accepted the invite.** borissaidme@gmail.com shows "needs action". Ask Melissa to confirm he is attending and get his surname, title and company email.
> 2. **Boris is unidentified.** No surname, no LinkedIn match, no public link to Acebet, Golden Frog Inc., 51 Plus One Ltd or Trey Mark Services. Ask Melissa where the lead came from (inbound form, event, referral).
> 3. **Legal pre-check.** The operating licence is Anjouan. Yuno legal precedent requires the contracting entity to match the KYC'd entity and the licence holder. Post a heads-up in #salesops-legal before the call so there is an answer on appetite before a second meeting.
> 4. **Agree roles with Sean and Justo.** Suggested split: Melissa or Sean intros, German runs discovery, Justo covers commercial and partners questions.
> 5. **No company-email domain** exists for Acebet in Gmail or Calendar, so there is no email history to build on.

---

# STUDY ZONE

## 1. TL;DR Battle Card

**Five facts to know cold**

1. ✅ **Two brands, three entities.** acebet.co is the international real-money crypto plus fiat casino and sportsbook, owned by Golden Frog Inc. under Anjouan licence 15831. Payments run through its Cyprus subsidiary, 51 Plus One Ltd. acebet.cc is a US sweepstakes casino run by Trey Mark Services Limited (Cyprus) on the same codebase.
2. ✅ **The US sweepstakes site is the volume.** About 6.7M visits for acebet.cc (94% US) against about 371K for acebet.co (Germany 62%, US 19%, Spain 7%, France 4%, Canada 2%). SimilarWeb, Sep-2026.
3. ✅ **Hand-wired cashier with no orchestrator.** Their code shows 13 rail identifiers: Fireblocks and Mesh for crypto, separate rails for cards, Interac, PIX and open banking, Revolut and Wise via peer.xyz, Kinguin gift cards, Zen, PayPal and MassPay payouts, LatAm and India payouts, and Whop rails on the US site. Each provider has its own hosted redirect and its own fee notice.
4. ✅ **Payouts are the public pain.** About 60% of 105 Trustpilot reviews read are about withdrawal delays, blocked cash-outs or KYC loops. Operator pages promise three different payout timelines.
5. ✅ **Young and product-led.** They launched in November 2025, added the US sweepstakes site in January 2026 and launched PvP Slot Battles in April 2026. Payout rails for LatAm and India are already in the code ahead of the traffic.

**Three hooks, in priority order**

1. **Payouts.** Route SEPA, card payouts, LatAm bank transfers and crypto through one layer with real-time monitoring. Aim at the "up to 10 business days" cases and the conflicting SLAs.
2. **One integration instead of thirteen.** Each new method or market stops being a new contract, a new redirect and a new fee notice. Routing and failover come with it.
3. **Fiat and stablecoins in one flow.** They already settle in USDT and USDC on six chains each. Yuno's Stablecoins product can remove the third-party on-ramp step and its player-paid fees.

**The objection they will raise:** "We built our own cashier. It works, and we can add rails ourselves."

**The answer:** "You have built a lot, and fast. The question is what the next ten rails cost. Yuno sits on top of the providers you already contracted, so nothing gets ripped out. You get routing, retries and monitoring across all of them, and the engineers who maintain redirects go back to building product like Slot Battles."

**The ask:** a 30-minute working session this week with Yuno solutions, plus the KYC/KYB pack started in parallel (entity, licences, UBOs).

**Rapport opener:** "Congrats on Slot Battles. A PvP format on slots is a genuinely different idea. How has it landed since April?" ✅ The launch was 4-Apr-2026, and the operator claimed 1,300 players in its first weeks.

---

## 2. Who Is in the Room

| Name | Role | Side | Status / history |
|---|---|---|---|
| Boris (surname unknown), borissaidme@gmail.com | Unknown 🔍 | Acebet (assumed) | Invite "needs action". No prior meeting, email or Slack trace ✅ |
| Melissa Pottenger | Organizer | Yuno | Accepted. Booked the meeting on 26-Oct |
| Sean Calabro | Head of North America | Yuno | Accepted. Forwarded the invite to German on 26-Oct with "if you can join" |
| Justo Benetti | Commercial | Yuno | Accepted |
| German Tatis | Senior AE | Yuno | Accepted |

**Boris, profile.** No profile could be built. Searches for the email handle, for "Boris" with Acebet, Golden Frog, 51 Plus One or Trey Mark, the Acebet LinkedIn company page (which shows four people, one named without a title) and press items all returned nothing. Acebet publishes no executives. LinkedIn was not opened directly because there is no surname to search on.

- ⚠️ **How to read him:** a personal Gmail on a commercial call usually means a founder, an owner-operator, or an outside payments consultant or agency. Do not assume which. Open with "tell me about your role at Acebet" and calibrate from there.
- 🔍 Get his surname, role, his entity (Golden Frog, 51 Plus One or Trey Mark), and who else owns payments and engineering.

**Intro path.** The meeting came through Melissa Pottenger. The lead source is unknown 🔍 (ask Melissa before the call).

**Relationship timeline.**

- No prior meeting with any attendee of this call exists on the calendar. The calendar was searched by Boris's email, by "Boris" and by "Acebet" for 2025 to 2026, and the only hit is this invite ✅.
- No Gmail threads with Boris or any Acebet, Golden Frog, Trey Mark or 51 Plus One address. No Slack mentions. No Gong CRM account ✅.
- **Implication:** first-meeting framing. They have received no Yuno material. Every fact we show is new to them.

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

**Orchestrator status:** none found in the code of either site. Each provider has its own key, hosted redirect ("Your payment will be processed through [provider name]") and fee notice ✅. ⚠️ Reads as in-house method selection by region.

**Providers by function** (from the acebet.co code snapshot of 3-Oct-2026 and the live acebet.cc code; vendor identities behind short keys are ⚠️ unless the page names the vendor)

| Function | Providers |
|---|---|
| Crypto deposits and custody | Fireblocks ✅; Mesh ("meshconnect") ⚠️; wallet connect (Phantom, Solflare, Coinbase Wallet, Trust, Ledger and others) ✅ |
| Fiat-to-crypto on-ramp | Swapped.com ✅ |
| Cards, Interac, PIX, Open Banking | "paytech" (BASIC_CARD, INTERAC, PIX, Open Banking) ⚠️ vendor unconfirmed |
| US cards, wallets, ACH | "breeze" (Visa, Mastercard, Amex, Apple Pay, Google Pay, ACH, instant bank transfer) ⚠️ vendor unconfirmed |
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
| Germany | 62% | Bank-led market (SEPA, open banking) with PayPal and Sofort/Klarna popular ⚠️ (general market knowledge) | 🔍 Confirm whether German players get the sweepstakes tenant or real money. That decides which rails matter |
| United States | 19% (.co) plus 94% of acebet.cc | Cards and ACH; high decline rates for gaming-coded transactions ⚠️ | The volume market. Ask about card approval rates on Gold Coin purchases |
| Spain | 7% | Cards and Bizum ⚠️ | 🔍 Ask whether Spain is served on real money |
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

**Core frame:** "You have built more payment coverage in a year than most operators build in three. Yuno makes that coverage work as one system: routing, failover, payouts and monitoring across all of it, through one integration on top of the providers you already have."

**Hooks with proof points** (published Yuno results only)

1. **Payouts and monitoring.** Rappi detects payment anomalies in milliseconds instead of 5 to 10 minutes manually, with 80% less analyst resolution time. Livelo recovered 50% of failed transactions.
2. **One integration, faster markets.** inDrive reached about 90% approval and went live in 11 new countries in under eight months on one integration (y.uno).
3. **Approvals and recovery.** Up to 7% approval uplift and 30% recovered revenue (y.uno).
4. **Stablecoins and crypto.** Yuno lists Crypto as a vertical "bridging fiat and crypto rails" for exchanges, on-ramps and Web3 platforms, and sells a Stablecoins product (y.uno).
5. **Gaming logos.** Garena, Moon Active and NetEase appear on y.uno. Whop is a Yuno customer logo too ⚠️. Do not mention that Whop appears in Acebet's code.

**Landmines (what NOT to say)**

- Do not say "you don't have X" for any method or market.
- Do not mention their licence quality, restricted-country conflicts, Trustpilot scores or the thegamehaus delisting.
- Do not quote prices, MDRs or timelines for go-live before legal has cleared the entities.
- Do not promise acquiring for gambling in any specific country. Partner appetite for Anjouan-licensed operators is unconfirmed.
- Do not reveal that we inspected their site code. Use "from what is visible on your site".
- Do not use unpublished stats.

---

## 10. Be Ready For

| They may ask | Ready answer |
|---|---|
| "Can you onboard us with an Anjouan licence?" | "Our compliance team reviews every gaming merchant by entity and licence. I'll take your entity details back today and come back with a clear answer, rather than guess on the call." Do not say yes or no. |
| "How much does it cost?" | "Pricing depends on volume, markets and which providers you bring. Once we see your mix we'll send a proposal. Our model is a platform fee plus a per-transaction fee." Do not quote numbers. Consult the Finance pricing policy afterwards. |
| "Do we have to replace our providers?" | "No. Yuno connects to the providers you already contract with. You add or switch providers from the dashboard without new engineering work." |
| "How long does integration take?" | "One API or SDK integration on your side. inDrive went live in 11 new countries in under eight months on that single integration. Your timeline depends on how many rails you move first." |
| "Do you have acquirers that take gaming?" | "We work with high-risk and gaming partners. Which ones fit depends on licence and market, so that's part of the review we'd run with you." |
| "PCI and card data?" | "Our hosted checkout and SDK keep card data out of your scope. Cards are tokenized in Yuno's vault and can be reused for payouts and repeat deposits." |
| "Do you do payouts?" | "Yes. Yuno has a Payouts product, and routing and monitoring cover payouts as well as pay-ins." |
| "Do you support crypto or stablecoins?" | "Yes. Yuno bridges fiat and crypto rails and offers stablecoin settlement. We'd map that against how Fireblocks and your wallets work today." |
| "Who else in gaming uses you?" | "Garena, Moon Active and NetEase are public names. Others we can discuss under NDA." |
| "Why not build routing ourselves?" | "You can, and you've shown you build fast. The trade-off is that every new rule, retry and monitor is your team's time forever. We give you that layer on day one so your engineers stay on product." |

---

# LIVE ZONE

## 11. Agenda (25 minutes)

| Minute | Block | Owner | Notes |
|---|---|---|---|
| 0 to 3 | Intros. Boris's role, entity and who else owns payments | Melissa / Sean | Notes: ____ |
| 3 to 13 | Discovery: today's cashier, volumes, payouts, markets (questions 1 to 8) | German | Notes: ____ |
| 13 to 20 | Yuno in one breath: one integration, routing and failover, payouts with monitoring, stablecoins. Proof points | German | Notes: ____ |
| 20 to 23 | Their questions | All | Notes: ____ |
| 23 to 25 | Next step: 30-minute working session this week plus the KYC/KYB pack | Sean / Justo | Notes: ____ |

## 12. Discovery Questions

1. What is your role at Acebet, and which entity do you work for: Golden Frog, 51 Plus One or Trey Mark? Who else owns payments and engineering?<br>Notes: ____
2. Is acebet.cc in scope for this conversation, or only the real-money site? Which entity would sign with a payments partner, and which licences does it hold?<br>Notes: ____
3. How is the cashier built today? Do you choose providers by method and region in-house, or does a provider host the cashier for you? Can you walk me through the main card and bank providers?<br>Notes: ____
4. Roughly what monthly deposit volume do you process, and how does it split between fiat and crypto, and between the US sweepstakes site and the real-money site?<br>Notes: ____
5. What card approval rates do you see by country, especially the US, Germany and Canada?<br>Notes: ____
6. Payouts: volume, average size, rails (SEPA, card payouts, bank transfers, crypto), the target timeline per rail, and how many need manual review?<br>Notes: ____
7. Which markets come next, and what blocks launching them? How long did the last new rail take your team?<br>Notes: ____
8. Where do KYC and fraud hurt most today, with Sumsub and Sift in place? False declines or re-verification?<br>Notes: ____
9. What would a payments partner have to prove in the first 90 days for this to be worth it?<br>Notes: ____

## 13. Post-Meeting Checklist

- [ ] Recap email to Boris the same day: what we heard, the two or three priorities, the proposed working-session slots, and the KYC/KYB document list.
- [ ] Post entity, licence and UBO details in #salesops-legal for a pre-check (Golden Frog Inc., 51 Plus One Ltd, Trey Mark Services Ltd).
- [ ] Ask Payments Concierge which partners accept Anjouan-licensed operators for EU and Canadian cards and for US sweepstakes.
- [ ] Create the Salesforce opportunity and log the outcome and new facts.
- [ ] Book the working session with solutions.
- [ ] Update memory (project_acebet) and the research brief with new facts.

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

*Google Doc: https://docs.google.com/document/d/18ufiAJlRHgtFg20E_bk_GkbGgrLUU1JSft5tNT_P6MA/edit*
