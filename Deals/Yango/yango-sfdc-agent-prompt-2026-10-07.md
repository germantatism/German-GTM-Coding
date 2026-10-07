# Prompt for a Salesforce agent · Yango (Col, Pe, Bol, Ven) · 2026-10-07

Copy everything below the line into the agent. Fill `[LEAD SOURCE]` first.

---

You have write access to Yuno's Salesforce (yuno.lightning.force.com). Create and advance ONE opportunity exactly as specified. Do not invent values. If a field below does not exist or a value is rejected, leave it and report the exact error. Report every step and finish with the opportunity URL.

## A. Pre-checks (stop and report if any fails)
1. Account = "Yango", Id 001Hu00003QIh8UIAT (https://yuno.lightning.force.com/lightning/r/Account/001Hu00003QIh8UIAT/view). Never use "Yango Deli Israel" (001Ps00001YsGJyIAN).
2. Opportunity 006Ps00000wENTCIA4 (owner Piotr Sierpinski) must already be Closed. If it is still open, stop and report; do not create a second open opp on the account.
3. If an open opportunity named "Yango (Col, Pe, Bol, Ven)" already exists on the account, stop and report its URL.

## B. Create the opportunity
- Create it from the Contact, not from the Account page (BDMs cannot use "New Opportunity" on the Account). Open Contact Javier Patiño under the Yango account and use Opportunity > New. If the Contact does not exist, create it first: First name Javier, Last name Patiño, Title "Head of Operations, Colombia", Email jpatino@yango-team.com, Account Yango.
- Opportunity Name: Yango (Col, Pe, Bol, Ven)
- Record type / opportunity type: New Merchant (merchant deal, not partner)
- Owner (BDM): German Tatis
- SDR: German Tatis
- KAM / Account Manager: Maria Jose Pineda
- Lead Source: [LEAD SOURCE]  (set it before anything else; Set Pricing is blocked without it)
- Stage at creation: Meeting Booked
- Close Date and Contract Signed Date: 2026-12-31
- Forecast Category: Pipeline
- Amount / TAR: 285660 USD (annual, full four-country volume)
- MRR (if the field exists): 23805 USD
- Currency: USD
- Countries / markets: Colombia, Peru, Bolivia, Venezuela
- Industry / vertical: Mobility, ride-hailing super-app (Dubai HQ, LatAm operations run from Colombia)
- Business Proposal Link: https://deck.y.uno/yangobclatam
- Decision Maker: Konstantin, Head of Payments, Yango HQ (surname not known)
- Competitors / incumbents (if the field exists): PayU, Unlimit, Inswitch (pay-ins); Cobre (payouts Colombia); Monnet (payouts Peru)
- Description / Deal Comments: paste section F
- Next Steps: paste section G
- Blockers: paste section H

## C. Contact roles (attach to the opportunity; create Contacts under the Yango account if missing)
| Name | Title | Email | Role | Primary |
|---|---|---|---|---|
| Javier Patiño | Head of Operations, Colombia | jpatino@yango-team.com | Champion | yes |
| Alejandro Sanabria Cárdenas | Finance Manager | pcardenas@yango-team.com | Economic Buyer | no |
| Luis Alejandro Montealegre Díaz | Ops Manager, Colombia | lmontealegre@yango-team.com | Influencer | no |
Do not create contacts for Konstantin or Sergey Solyakov (HQ): no email on record.

## D. Advance the stage
Move Meeting Booked → Discovery → Demo/BP, one step at a time. Stop at Demo/BP. Do NOT set Proposal Sent by hand: it is set automatically when Finance approves the pricing.
Stage evidence if asked: first meeting May 2026; discovery call 2026-08-19 (Gong "Yango + Yuno"); business case sent 2026-09-04 (opened by Javier 2026-09-16); proposal sent by WhatsApp 2026-09-30 and presented to Yango HQ by the Colombia team on 2026-10-01.

## E. Set Pricing (click the Set Pricing button while in Demo/BP and submit exactly this)
Volume basis (Yango data, August 2026, per month):
| Country | Approved recharge volume / month | Transactions / month | Average ticket |
|---|---|---|---|
| Colombia | 1,929,598 USD | 551,314 | 3.50 USD |
| Peru | 1,796,096 USD | 561,280 | 3.20 USD |
| Bolivia | 2,747,371 USD | 1,831,581 | 1.50 USD |
| Venezuela | 831,960 USD | 297,129 | 2.80 USD |
| Total | 7,305,025 USD | 3,241,304 | 2.25 USD blended |

Fees:
- Platform fee (monthly fee): 12,000 USD per month (144,000 USD per year), billed annually upfront.
- Transaction fee: percentage of approved recharge volume, ONE pooled stream for the four countries, tiered:
  - 0.25% on the first 1,500,000 USD per month
  - 0.20% from 1,500,000 to 3,000,000 USD
  - 0.15% from 3,000,000 to 4,500,000 USD
  - 0.10% above 4,500,000 USD
- Fixed fee per transaction: none
- Minimum guaranteed / monthly minimum: 0 (none)
- Setup fee: none
- Credit months: 0
- Declined transactions and card verification (binding) attempts: not charged
- Network tokens (add-on): 0.05 USD per token created, 0.01 USD per lifecycle update
- Reconciliation (add-on): 2,000 USD per month per 500,000 transactions plus 0.0003 USD per transaction
- Nova: not quoted (pending review)
- Contract term: 3 years, USD
If the pricing form cannot represent a percentage-of-volume tier, enter the platform fee, put the four tiers verbatim in the pricing notes or comments field, and report that the tiers could not be entered as structured fields.

Expected billing from these fees (for the MRR / ARR fields and the Finance note):
| Rollout step | Monthly total |
|---|---|
| Colombia only | 16,609 USD |
| Colombia + Peru | 19,839 USD |
| + Bolivia | 22,973 USD |
| + Venezuela (full volume) | 23,805 USD per month = 285,660 USD per year = 0.0073 USD per recharge = 0.33% of volume |
Transaction fee at full volume: 11,805 USD per month. Platform fee: 12,000 USD per month.

Note for Finance (paste into the pricing comments):
"Segment V4 x M1 (mobility). Strategic merchant: 3.24M tx/month. Pay-in tiers equal 0.0056 / 0.0045 / 0.0034 / 0.0023 USD per transaction at the 2.25 USD blended ticket, below the 0.01 USD policy minimum (red zone, needs Global Controller/CFO + CRO). Network tokens 0.05/0.01 vs minimum 0.20/0.04 (red). Reconciliation 0.0003 USD/tx vs minimum 0.0085 (red). Platform fee 12,000 vs V4 list 16,000 (yellow). 3-year term (yellow). Card verification not charged: policy marks it pending, please confirm. Rationale: average ticket 1.50 to 3.50 USD makes any fixed per-transaction fee unviable (the client's Finance Manager asked for variable pricing on 2026-08-19); incumbents charge 2.4% (240 bps); card-rail business case 3.21M USD per year is 11.2x the annual cost of 285,660 USD."

## F. Description / Deal Comments (paste verbatim)
Yango consolidates driver top-up (recharge) collection across Colombia, Peru, Bolivia and Venezuela onto one platform. Yuno sits on the collection side only, complementing Cobre (payouts in Colombia, 120k+ drivers via Fast Pay) and Monnet (payouts in Peru). Root cause found on the 2026-08-19 discovery call: card binding succeeds only 68 to 70% because Yango's acquirers have no local presence and banks block the small verification charges as foreign; once bound, transactions approve at 90 to 92%. Pitch: zero-cost card verification plus smart routing with multi-provider fallback to fix binding, plus local payment methods per market. Incumbents: PayU (cards), Unlimit (2.4% flat, global master agreement), Inswitch (2.4% + COP 150); PayRetailers formerly. Business case sent 2026-09-04 (https://deck.y.uno/yangobclatam, opened by Javier 2026-09-16): 87.7M USD per year in cashless recharges, 38.9M transactions, card-rail case 3.21M USD per year (2.33M acceptance + 0.88M MDR), 10.7M USD identified in total. Final proposal sent by WhatsApp on 2026-09-30: 12,000 USD monthly platform fee plus 0.25/0.20/0.15/0.10% of approved recharge volume pooled across the four countries, no minimum, no fixed per-transaction fee, declines and card verification free; 23,805 USD per month (285,660 USD per year) at full volume. Javier Patiño said the proposal "hace mucho sentido"; the Colombia team presented it to HQ on 2026-10-01. HQ decision owners: Konstantin (Head of Payments) and Sergey Solyakov (Integrations, Dubai). Yango wants one contract and one platform, partly to minimise taxable movements under Colombia's 4x1000 tax, and may expand scope beyond LatAm. Reference case they cited: inDrive. Yuno team: German Tatis (BDM), Maria Jose Pineda (KAM), Justo Benetti (CRO, in cc); Piotr Sierpinski (EMEA) is in parallel contact with Yango's Russian HQ.

## G. Next Steps (paste verbatim)
1. Get HQ feedback on the proposal presented internally on 2026-10-01 and secure the meeting with Konstantin and Sergey Solyakov.
2. Submit Set Pricing and obtain Finance sign-off on the red-zone items (pay-in tiers below 0.01 USD/tx, network tokens, reconciliation).
3. Align with Piotr Sierpinski and Maria (GM EMEA) on the Russian-HQ channel so Yango hears one Yuno voice.
4. Close the remaining data gaps: binding rate per country, live payment methods per country, ticket confirmation for Peru, Bolivia and Venezuela.

## H. Blockers (paste verbatim)
Pricing below policy minimum (CFO + CRO approval required). HQ decision pending since 2026-10-01 with no date committed. Average ticket of 1.50 to 3.50 USD rules out any fixed per-transaction fee.

## I. Report back
Return: opportunity Id and URL; final stage; the pricing record status (should read pending Finance approval); every field you could not fill and why; every validation error verbatim; whether the three contact roles were attached.
