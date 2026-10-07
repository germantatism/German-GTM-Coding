# Yango (Col, Pe, Bol, Ven) · Salesforce opportunity spec (2026-10-07)

**Status:** opp NOT yet created. Claude has no write path into Salesforce from Claude Code (no Salesforce connector, no API credentials in `.env`, no browser). Everything below is paste-ready. Script that creates it once credentials exist: `Deals/Yango/build/create_sfdc_opp.py`.

**Context from Slack today (7-oct, 08:30 PDT):** Piotr Sierpinski is closing his own Yango opp (https://yuno.lightning.force.com/lightning/r/Opportunity/006Ps00000wENTCIA4/view) and wrote "feel free to open yours". Confirm his is Closed before creating, so the account has one open opp.

---

## 1. How to create it (Yuno rules, per Felipe Triboni / RevOps)

1. BDMs cannot use "New Opportunity" from the Account page (that button is KAM-only). Create it from a **Contact** (Contact > Opportunity > New) or by converting a Lead with "Convert to Deal".
2. Use Contact **Javier Patiño** under the Yango account. If he does not exist as a Contact yet, create him first (section 5).
3. Set **Lead Source** right away: Salesforce blocks Set Pricing without it.
4. Stage flow: Meeting Booked → Discovery → **Demo/BP** → Proposal Sent → Negotiation → Contracting → Closed Won. You cannot move it to Proposal Sent by hand: hit **Set Pricing** while in Demo/BP, Finance approves under the Pricing tab, and the opp moves to Proposal Sent automatically.
5. Fill "Guidance for Success" fields as you go (Deal Comments, Next Steps, Blockers, Business Proposal Link, Decision Maker, Forecast Category, Contract Signed Date). Business Proposal Link is mandatory before Contracting.

## 2. Header fields

| Field | Value |
|---|---|
| Opportunity Name | Yango (Col, Pe, Bol, Ven) |
| Account | Yango · `001Hu00003QIh8UIAT` · https://yuno.lightning.force.com/lightning/r/Account/001Hu00003QIh8UIAT/view (NOT "Yango Deli Israel" `001Ps00001YsGJyIAN`) |
| Opportunity type / record type | New Merchant (merchant, not partner) |
| Owner (BDM) | German Tatis |
| SDR | German Tatis (self-sourced; same pattern as Flair) |
| KAM / Account Manager | Maria Jose Pineda |
| Stage at creation | Meeting Booked, then advance to Discovery and Demo/BP (all three already happened: first call May 2026, discovery call 19-aug, business case 4-sep, proposal ~30-sep) |
| Lead Source | ⚠️ German to pick (not recorded in repo or memory) |
| Close Date / Contract Signed Date | 2026-12-31 (assumption: Q4 2026; HQ has had the proposal since 1-oct) |
| Forecast Category | Pipeline until HQ answers; move to Best Case when Konstantin/Sergey engage |
| Amount / TAR | $285,660 per year (full four-country volume) |
| MRR at full volume | $23,805 |
| Currency | USD |
| Industry / vertical | Mobility · ride-hailing super-app (Dubai HQ, LatAm ops from Colombia) |
| Countries | Colombia, Peru, Bolivia, Venezuela |
| Product scope | Pay-in orchestration for driver top-ups (cards + local methods), zero-cost card verification + smart routing to fix card binding; token vault; monitors; reporting. Payouts stay with Cobre (CO) and Monnet (PE) |
| Business Proposal Link | deck.y.uno/yangobclatam (Papermark). Source deck: Google Slides `1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw` "Business Case Yango + Yuno" (39 slides, section 06 · Proposal). Local PDF: `Deals/Yango/Business Case Yango + Yuno_Sept2026 copy.pdf` |
| Competitors / incumbents | PayU, Unlimit (2.4% flat), Inswitch (2.4% + COP 150) on pay-ins; Cobre (payouts CO), Monnet (payouts PE); PayRetailers formerly. Reference case they cited: inDrive |
| Decision Maker | Konstantin (HQ Head of Payments, owns CO/PE/BO/Africa decision). Surname unknown |

## 3. Set Pricing (the FINAL proposal, deck 24-sep, sent by WhatsApp ~30-sep, presented to HQ 1-oct)

Volume basis (Yango data, Aug 2026, monthly):

| Country | Approved recharges / mo | Transactions / mo | Ticket |
|---|---|---|---|
| Colombia | $1,929,598 | 551,314 | $3.50 |
| Peru | $1,796,096 | 561,280 | $3.20 |
| Bolivia | $2,747,371 | 1,831,581 | $1.50 |
| Venezuela | $831,960 | 297,129 | $2.80 |
| **Total** | **$7,305,025** | **3,241,304** | $2.25 |

Pricing to submit:

| Item | Value |
|---|---|
| Platform fee | $12,000 / month ($144,000 / year) |
| Transaction fee | % of approved recharge volume, one pooled stream for the four countries, tranches: **0.25%** ($0 to $1.5M/mo) · **0.20%** ($1.5M to $3M) · **0.15%** ($3M to $4.5M) · **0.10%** (> $4.5M) |
| Fixed per-tx fee | none |
| Monthly minimum | none |
| Setup fee | none |
| Declines / card verification (binding) | not charged |
| Network tokens (add-on) | $0.05 per token created, $0.01 per lifecycle update |
| Reconciliation (add-on) | $2,000 / month per 500K tx + $0.0003 / tx |
| Nova | not quoted |
| Term | 3 years, USD, platform fee annual upfront, usage monthly in arrears |

What it yields (verified with `Deals/Yango/build/yango_pricing_model.py`, FINAL section):

| Rollout step | Total / month |
|---|---|
| Colombia | $16,609 |
| + Peru | $19,839 |
| + Bolivia | $22,973 |
| + Venezuela (full) | **$23,805** → $285,660 / year, $0.0073 per recharge, 0.33% of volume |

Set Pricing gotcha (Felipe, 3-oct): if the opp already has products from an earlier pricing, the flow keeps the old fees and ignores what you type. This is a new opp so it should not apply; if it does, ask Felipe to set the fees directly on the opp.

## 4. Pricing Policy zones (internal, declare in the Finance submission)

Segment V4 (1M to 5M tx/mo) × M1 (mobility). Yango is a strategic merchant (3.24M tx/mo ≥ 1.2M), which is the only case where red zone is a deliberate decision.

| Item | Proposal | Policy reference | Zone |
|---|---|---|---|
| Pay-in tranches | 0.25 / 0.20 / 0.15 / 0.10% = $0.0056 / $0.0045 / $0.0034 / $0.0023 per tx at $2.25 ticket | Doc minimum $0.01 / tx | 🔴 Red: Global Controller/CFO + CRO, SLA 5 business days |
| Platform fee | $12,000 | V4 list $16,000, min $4,000 | 🟡 Yellow at most (RevOps/Sales Ops/GM, 2 business days) |
| Network tokens | $0.05 / $0.01 | min $0.20 / $0.04 | 🔴 Red |
| Reconciliation | $0.0003 / tx | min $1,500 + $0.0085 / tx | 🔴 Red (10x below) |
| Term 3 years | | long terms | 🟡 Yellow |
| Card verification not charged | | "PENDING if counts as tx" in policy | ⚠️ confirm with Finance |

Minimum price is never customer-facing. Justification for the ask: ticket $1.50 to $3.50 makes any fixed per-tx fee unviable (Alejandro asked for variable pricing on the 19-aug call); incumbents charge 240 bps; card-rail business case $3.21M/yr is 11.2x the annual cost.

## 5. Contacts to attach (Opportunity Contact Roles)

| Name | Title | Email | Role |
|---|---|---|---|
| Javier Patiño | Head of Operations, Colombia | jpatino@yango-team.com (also jpatino@yango.com) | Champion, primary contact since May 2026 |
| Alejandro Sanabria Cárdenas | Finance Manager | pcardenas@yango-team.com | Finance / economic buyer (asked for variable pricing) |
| Luis Alejandro Montealegre Díaz | Ops Manager, Colombia (ex-Rappi) | lmontealegre@yango-team.com | Influencer |
| Konstantin (surname unknown) | Head of Payments, HQ | unknown | Decision maker |
| Sergey Solyakov | Integrations, HQ Dubai · linkedin.com/in/sergey-solyakov/ | unknown | Decision maker / technical |

Yuno side: German Tatis (BDM), Maria Jose Pineda (KAM), Justo Benetti (CRO, in cc of the thread), Piotr Sierpinski (EMEA, in parallel with Yango's Russian HQ; his manager Maria, GM EMEA, is reviewing all deals).

## 6. Deal Comments (paste)

Yango consolidates driver top-up (recharge) collection across Colombia, Peru, Bolivia and Venezuela onto one platform; Yuno sits on the collection side only, complementing Cobre (payouts CO) and Monnet (payouts PE). Root cause found on the 19-aug discovery call: card binding succeeds only 68 to 70% because acquirers have no local presence; once bound, transactions approve at 90 to 92%. Pitch: zero-cost card verification + smart routing to fix binding, plus local methods per market. Business case (deck sent 4-sep, Papermark deck.y.uno/yangobclatam, opened by Javier 16-sep): $87.7M/yr cashless recharges, 38.9M tx, card-rail case $3.21M/yr, $10.7M identified in total. Final proposal (variable % of approved volume + $12K platform fee, $23.8K/mo at full volume) sent by WhatsApp ~30-sep; Javier said it "hace mucho sentido" and the Colombia team presented it to HQ on 1-oct. HQ decision owners: Konstantin (payments) and Sergey Solyakov (integrations). Incumbents: PayU, Unlimit, Inswitch (pay-ins). Scope may expand beyond LatAm (Yango wants a global solution).

## 7. Next Steps (paste)

1. HQ feedback on the proposal (presented internally 1-oct); push for the meeting with Konstantin and Sergey.
2. Submit Set Pricing and get Finance sign-off on the red-zone items (pay-in % below $0.01/tx, tokens, reconciliation).
3. Align with Piotr Sierpinski / Maria (GM EMEA) on the Russian-HQ channel so Yango hears one Yuno voice.
4. Close the data gaps for the final model: per-country binding rates, live payment methods per country, Peru/Bolivia/Venezuela ticket confirmation.

## 8. Blockers (paste)

Pricing below policy minimum (requires CFO + CRO). HQ decision pending since 1-oct, no date committed. Ticket size ($1.50 to $3.50) rules out any fixed per-tx fee.

## 9. After the opp exists

- Update the Deal Status GTM tracker row for Yango (currently "Demo" with a stale comment that says the proposal was not sent) to the Salesforce stage.
- Add the opp URL to `project_yango` memory and to this file.
