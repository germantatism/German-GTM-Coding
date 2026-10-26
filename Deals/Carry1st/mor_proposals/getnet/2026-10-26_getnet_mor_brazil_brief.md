# Getnet Brazil · MoR cross-border commercial proposal · deep brief

Received 26-oct-2026 22:31 UTC from Igor Leite (Enterprises & Global Clients, Getnet Brasil, igor.leite@getnet.net, WhatsApp +55 11 99311-8121), thread "MoR Proposal Getnet Brazil" (Gmail threadId 1a17a576a929da1d). CC on his side: Fabrice Mendez, Elbenetton Farias, Juan Anton, Francisco Perez Perez, Gabriel Pires, Luiz Perri. PDF: `2026-10-26_Getnet_Commercial_Proposal_MoR_Brazil.pdf` (8 pages, "Commercial Proposal MoR - Brazil", file name "Commercial Proposal - MoR Brazil y.uno.pdf"). Merchant = Carry1st Shop (never named to Getnet; Cordel has not cleared Getnet, only Mercado Pago).

Igor's framing in the email: "a more standard offer as we don't have detailed information about the merchant". He asks for the merchant's name and transaction details to rework it with his finance team, and offers a call.

## TL;DR

* Brazil only, cross-border MoR (Getnet's Brazilian entity collects in BRL, hedges daily, remits abroad). Mexico "soon, with delays" per Fabrice (22-oct). Getnet is licensed only in Spain, Portugal, Brazil, Mexico, Argentina, Chile and Uruguay (page 7), so Colombia and Bolivia are out of reach even later.
* Card pricing is a flat installment grid, not a small-ticket price: 1x Visa and Mastercard 4.0%, Elo 4.5%, Amex 5.0%, plus 1.0 point per extra installment up to 12x (15.0% to 16.0%).
* On top of MDR: 1.5% FX service fee on every remittance over spot, and IOF 3.5% on transactions (0.38% on refunds). Ad valorem all-in on a 1x Visa or Mastercard sale is about 9% before per-transaction fees.
* The hidden cost at a $5 to $10 ticket is the per-transaction gateway stack in BRL: 0.14 (payment) + 0.31 (antifraud) + 0.20 (reconciliation) + 0.02 (vault) + 0.14 (ABU) + 0.15 (3DS) + 0.07 (tokenization) = BRL 1.03 if everything is taken. At a BRL 25 ticket the full stack is 4.1% by itself.
* Pix is "available" but has no price in the document. Debit cards are "available" but have no rate. Hipercard is not in the grid (text says "all local credit card schemes").
* Nothing German asked for on 23-oct about timing arrived: no onboarding timeline, no KYC list, no go-live ETA. The MoR governance route (formal acceptance, risk areas, committee, contract) is described with no dates. Proposal valid until 30-nov-2026, three days after Black Friday.
* Minimum annual volume, average ticket and MCC are all "TBD", and the conditions say fees change if the card brand does not validate the MCC. The numbers are not underwritten for gaming yet.
* Page 5 still carries a Temu co-brand lockup in the header: this is Getnet's recycled standard cross-border template, which confirms Igor's "standard offer" line. Internal note only.

## Page by page

### Page 1 · cover
"Commercial Proposal MoR - Brazil".

### Page 2 · Payment Processing (header "Commercial offer | CROSSBORDER")

| Item | Price / fee | Comment |
|---|---|---|
| Service fee | 1.50% | Each foreign exchange transaction + spot rate |
| Implementation fee | BRL 0 | Technical implementation |
| Minimum volume | TBD | Per year |
| Average ticket | TBD | Per transaction |
| MCC | TBD | |
| Term of partnership | 1 year | |
| Chargeback | Scheme cost passed through | "When such event occurs, the cost charged by the respective card scheme is passed on the merchant" |

### Page 3 · Gateway Services (all per transaction, BRL)

| Item | BRL per transaction |
|---|---|
| Payment transaction (credit, debit and Pix) | 0.14 |
| Antifraud | 0.31 |
| Reconciliation | 0.20 |
| Vault | 0.02 |
| ABU (account updater) | 0.14 |
| 3DS | 0.15 |
| Tokenization | 0.07 |
| Full stack | 1.03 |

Not stated: which lines are mandatory under the MoR model (antifraud is the likely one, since Getnet carries the risk as merchant of record) and whether a merchant can bring its own vault, tokens, 3DS and reconciliation.

### Page 4 · Acquiring Fees (MDR by brand and installments, "Share: TBD")

| Installments | Visa | Mastercard | Elo | Amex |
|---|---|---|---|---|
| 1x | 4.0% | 4.0% | 4.5% | 5.0% |
| 2x | 5.0% | 5.0% | 5.5% | 6.0% |
| 3x | 6.0% | 6.0% | 6.5% | 7.0% |
| 6x | 9.0% | 9.0% | 9.5% | 10.0% |
| 12x | 15.0% | 15.0% | 15.5% | 16.0% |

Linear: +1.0 point per extra installment, every brand. Hipercard not in the grid. Debit not in the grid. Pix not in the grid.

### Page 5 · Important Information | Disclaimer
* IOF: transactions 3.5%, refund 0.38%.
* Payment methods available: all local credit card schemes (with installments), all local debit cards and Pix.
* FX structure: automatic daily hedge, guaranteed FX rate.
* FX settlement: T+7, and "FX transaction will only be executed after the funds have been settled".
* FX reference: spot USD rate. FX applied to all payment options and to reversals if funds were already remitted abroad.
* Header shows the Temu x Getnet lockup (recycled template).

### Page 6 · Commercial Conditions
* Valid until 30-nov-2026; Getnet may then ratify or change conditions.
* Confidential between the parties.
* "Getnet receivables shall be settled in a Santander account."
* Acceptance formalization, responsibilities, implementation schedule, tests and interfaces "will be defined and agreed between the parties" (no dates).
* Partnership 12 months, may be extended if both agree.
* Rates were composed from "costs, transaction volumes, mix, flags and average market products reported" (none were reported, so these are defaults).
* If the MCC is not validated by the brand, "the MCC and consequently the fees will be exchanged".
* Prices subject to review with economic and market changes.
* Adherence by signing a contract.
* MoR governance: after formal acceptance, internal approval by the risk areas, then committee deliberation for contract signing; "we need the updated governance documents".

### Page 7 · Legal disclaimer
Licensed territories: Spain, Portugal, Brazil, Mexico, Argentina, Chile and Uruguay. Services offered only to entities located in those territories; offshore entities operating within them are served.

### Page 8 · Closing
Confidentiality and IP notice, "©Getnet 2024".

## What it costs at Carry1st's tickets

Basis: 1x Visa or Mastercard sale. FX fee and IOF apply to the remitted amount (net of MDR), so the gross-basis figures below are marginally overstated. BRL tickets use an illustrative 5.0 BRL per USD (mid-2026 references cluster at 5.0 to 5.1; replace with the rate of the day, the proposal does not quote one).

Ad valorem: 4.0% MDR + 1.5% FX fee + 3.5% IOF = about 9.0% (Elo 9.5%, Amex 10.0%).

| Ticket | Gateway, payment only (BRL 0.14) | Gateway, payment + antifraud (BRL 0.45) | Gateway, full stack (BRL 1.03) |
|---|---|---|---|
| $5 median (BRL 25) | 0.6% | 1.8% | 4.1% |
| $10 average (BRL 50) | 0.3% | 0.9% | 2.1% |

All-in on a 1x Visa or Mastercard sale:

| Ticket | Payment only | Payment + antifraud | Full stack |
|---|---|---|---|
| $5 median | about 9.6% | about 10.8% | about 13.1% |
| $10 average | about 9.3% | about 9.9% | about 11.1% |

At the run rate in the business case (450K transactions and $4.5M a month):

| Line | Monthly, BRL | Monthly, USD at 5.0 | Share of TPV |
|---|---|---|---|
| Gateway, payment only | 63,000 | 12,600 | 0.28% |
| Gateway, payment + antifraud | 202,500 | 40,500 | 0.90% |
| Gateway, full stack | 463,500 | 92,700 | 2.06% |
| Ad valorem 9.0% (if 100% 1x Visa/MC) | | 405,000 | 9.0% |

Pix: no MDR quoted. On the document alone a Pix sale costs BRL 0.14 gateway + 1.5% FX + 3.5% IOF plus whatever Pix fee Getnet adds. With Pix at 42% of Brazilian online purchases this is the biggest hole in the quote.

Comparison basis warning: the Carry1st model carries EBANX at 4.5% all-in (ESTIMATE, range 3 to 6%). Before comparing, align what each quote includes: MDR only, MDR + FX, or MDR + FX + IOF + per-transaction fees. Getnet ex-IOF and ex-gateway is 5.5% on 1x Visa/MC.

## Reading for the deal

1. Getnet fits as a Brazil-only second MoR behind EBANX, never as the primary for five markets. Colombia and Bolivia are outside its licences; Argentina is licensed but the MoR product is not there; Mexico is delayed.
2. The cards all-in looks roughly double the EBANX estimate on a like-for-like basis, but the quote is explicitly a default. Igor offered to rework it with finance once he has volumes, ticket and MCC. The $4 to 5M a month and 400K to 500K transactions should move the MDR and the per-transaction lines.
3. The gateway stack is where Yuno's value shows. Vault, tokenization, 3DS, reconciliation, account updater and antifraud routing are all things Carry1st gets through Yuno across every provider. Taking Getnet's payment line only (BRL 0.14) instead of the full stack (BRL 1.03) is worth about $80K a month at run rate, which covers Yuno's $21K a month several times over. Use it internally; confirm first which lines Getnet makes mandatory under MoR.
4. Installments are irrelevant for $10 top-ups and expensive on the grid (12x at 15%). Recommend 1x only, or a cap at 3x for gift cards.
5. Cash cycle is unclear. The document only gives FX settlement at T+7 after domestic settlement. Brazilian credit card receivables settle D+30 by default unless anticipated, so a credit card sale could reach Carry1st around five weeks later. Debit and Pix should be faster. This is a question, not a finding.
6. Black Friday risk is real. Fabrice said pricing by "end of next week" and Igor delivered on Monday, which is a good sign, but the governance chain (acceptance, risk areas, committee, contract, governance documents) has no lead time attached and the proposal expires on 30-nov.
7. The minimum annual volume is TBD. Do not accept a minimum on a market that Carry1st itself cannot forecast yet ("slow burn or rocket ship").
8. MCC: Getnet has not committed to a gaming or digital goods MCC. The conditions let them reprice if the brand rejects the MCC. Get the MCC in writing before any comparison is final.

## What is missing against German's 23-oct ask

| Asked | Delivered |
|---|---|
| Pricing that works with small tickets ($10 average, $5 median) | No. Default grid plus per-transaction fees that punish small tickets |
| Cards including Elo and Hipercard | Elo priced at +0.5 pt. Hipercard not in the grid, only "all local credit card schemes" |
| Pix | Listed as available, not priced |
| Onboarding timeline including KYC | Not provided |
| Go-live ETA | Not provided |

## Questions for Getnet (send after the team review)

1. Pix: MDR or fixed fee, settlement timing, and whether the 1.5% FX fee and IOF apply the same way.
2. Debit card rate (not in the grid) and Hipercard confirmation and rate.
3. Which gateway lines are mandatory under MoR. Can the merchant bring its own vault, network tokens, 3DS and reconciliation through its orchestration layer, paying only the BRL 0.14 payment line.
4. Domestic settlement terms by method (credit D+30 or anticipated, debit, Pix) before the T+7 FX leg; anticipation cost if any.
5. Onboarding: governance document list, KYC steps, risk and committee lead time, and a realistic go-live date for a late-November start.
6. Minimum annual volume: the number, and the consequence of missing it.
7. MCC Getnet would assign to game top-ups and gift cards, and the fee impact if the brand reclassifies.
8. Confirm the 1.5% service fee and the 3.5% IOF apply to the net remitted amount, and whether IOF is 3.5% under this MoR structure.
9. Volume pricing: MDR and per-transaction fees at $4 to 5M a month and a $10 ticket.
10. Chargebacks under MoR: fixed fee per dispute, dispute handling, and liability split.
11. Settlement currency options (USD only?) and how the guaranteed daily rate is set against spot.
12. "Receivables settled in a Santander account": whose account, and does the merchant need one.
13. Integration path: API or SDK, and whether Yuno's existing Getnet Brazil connection covers the MoR cross-border product or needs a new connection.

## Next steps

* Thank Igor and tell him we will socialize it with the team (draft in Gmail, 26-oct).
* Ask Cordel for the green light to name Carry1st to Getnet, as he did for Mercado Pago.
* Send the anonymized inputs now (gaming and digital goods, $10 average and $5 median ticket, Brazil first, $4 to 5M a month by end 2027) so finance can rework the grid in parallel.
* Build the comparison once Mercado Pago, PagSeguro and the merchant's EBANX quote are in (`../mor_proposals_comparison.md`).
