# Proposal - Luni + Yuno (Google Slides, 2026-10-15)

Deck: https://docs.google.com/presentation/d/1H-YqtBpwkWZ6_JBDLcnSsTMaRnZWsLqVfHxmc-oma6g/edit
Origin: Drive copy of "Proposal - FlightHub + Yuno" (1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI), Drive folder "Luni" (17670HtkOP0YVqgvOXfLvUH_p1KwaIeBU, My Drive root, same pattern as Línea Directa). 21 slides: Why Yuno (1 to 11), Business Case (12 to 14), Proposal (15 to 16), Appendix (17 to 20), close (21). The FlightHub Build vs. Buy section (3 slides) was removed: at Luni's size an in-house build would cost about the same as Yuno, so the comparison would not help.
Via: service account gtm-claude-editor (shared as editor from the Drive connector). Scripts in build/: model.py (all arithmetic), content_luni.py (text per element ID), build_luni.py (dry / apply), fix1_bottom_boxes.py (second pass), fix2_price_at_40k.py (table at 40K, scenario rows removed), fix3_platform_10k.py (platform $10K), pid.txt (deck id).
Context: BDM intro call 15-oct-2026 with Artsiom Kalianchuk (see luni-meeting-notes-2026-10-15.md). German asked for the usual proposal deck in English, FlightHub as the model, pricing $12K platform + $0.06 / $0.05 tranches, pending boxes for subscriptions engine and reconciliation, and a Cruz Verde style business case.

## Client data used (call 15-oct-2026)
- About 40,000 payment attempts in September (Stripe US ~40K at 37%, Stripe France ~1.5K at 68%, third account ~1.5K), blended "a little more than 40%" approval. Deck uses 40,000 attempts at 40% = 16,000 approved payments a month.
- Average ticket $18 (German's number, Artsiom said yes). Approved volume ≈ $288K a month, $3.46M a year.
- Stripe US + Stripe France + Paddle; PayPal US being built in-house; cards, Apple Pay, Google Pay; European cards processed cross-border; 95% subscriptions; new one-time-purchase app at ~$10 AOV.

## Pricing (slide 16), German 15-oct-2026 (v3, same day: platform fee $12,000 -> $10,000; v2 = table at 40,000 successful, scenario rows removed)
| Item | Price | At 40,000 successful / month (both tranches in use) |
|---|---|---|
| Platform fee | $10,000 / month flat (opened at $12,000, lowered the same day) | $10,000 |
| Tranche 1: 0 to 30,000 successful trx | $0.06 / trx | $1,800 |
| Tranche 2: 30,001 to 40,000 | $0.05 / trx | $500 |
| **Total** | | **$12,300 / month, $147,600 / year, $0.31 per successful trx** |
- Today (16,000 successful, 40,000 attempts at 40%): $960 + $10,000 = $10,960 / month, $131,520 / year; stated in the sub-line under the $0.31. At 20,000: $11,200; at 24,000: $11,440.
- v1 had an "As approvals climb" block with three scenario rows (50% / 60% / 40,000) in the left card; German asked to remove it and to show the price at 40K (fix2_price_at_40k.py). Left card = two tranches + note, as in the Línea Directa deck.
- Note under the tranches: "Above 40,000 successful transactions a month, the next tranche is set together as Luni's volume grows" (German gave only two tranches). ⚠️ Confirm or give a third rate.
- No minimum monthly billing shown (German mentioned ~$15K minimums on the call; the fixed $10K is the only floor in the deck). Footer: "Rates locked, tranches reviewed annually as volume grows" (no term stated; FlightHub said 3 years).
- Included (unchanged from FlightHub): +1,000 methods, +450 providers, +50 anti-fraud tools, orchestration & rules engine, smart routing & retries, monitors & auto-failover, PCI token vault, dashboard & insights, KAM + TAM.
- Bottom boxes, both "Pending review", not in the totals: Subscriptions engine (plans, trials, smart retries on failed renewals, past-due recovery; "depending on Luni's interest") and Reconciliation (one view across Stripe US, Stripe France, Paddle and PayPal). No prices.
- Pricing Policy check: Luni is V1 (<25K tx/month) × M4 (software / digital goods). Platform fee list for V1 is $5,000, so $10,000 is above list; pay-ins $0.06 / $0.05 against a $0.10 list and $0.01 floor. Deal size $10,960 / month (today) clears the $10K minimum, with little room below. Subscriptions still "not sellable yet" in the policy draft: confirm with Finance before pricing that box.

## Business case (slides 13 and 14): four levers, FlightHub layout
| Lever | Metric | Conservative | Optimistic | Assumption |
|---|---|---|---|---|
| L1 Approval uplift (routing by geo and card, local route for EU cards, second provider for recoverable declines, no retries on unrecoverable ones) | +10 to +20 pts | $864K | $1.73M | 4,000 to 8,000 more approved payments a month × $18 × 12 |
| L2 Checkout & methods (PayPal, local methods, better checkout) | +2% to +5% | $69K | $173K | on 16,000 approved a month |
| L3 Processing cost (cross-border fees, cheapest provider at equal approval) | 25 to 50 bps | $8.6K | $17K | on $3.46M approved volume |
| L4 Integrations avoided (PayPal US in progress, EU acquirer, local processing, new-market methods) | 3 to 4 integrations | $52K | $113K | 8 to 12 weeks each + 20% to 30% upkeep, $80K per engineer, 3 existing integrations maintained |
| Total | | $0.99M | $2.03M | average $1.51M; L1 = 86% of the average |
- Headline S13: "On 40,000 monthly payment attempts at an $18 ticket, every 10 points of approval are worth about $0.9M a year".
- S14 big number $1.51M "against about $132K to $137K a year on the proposal that follows" (Yuno bill at 16,000 to 24,000 successful, platform $10K). Value / cost ≈ 7x to 15x.
- Why +10 / +20 pts: German said on the call "from 37 we could for sure go beyond 50"; Artsiom expects to "double". Both figures are below his expectation. The assumptions band says part of the measured lift comes from no longer retrying unrecoverable declines, and that everything is recalibrated with the decline breakdown he is sending.

## Changes per slide vs FlightHub
- S1 cover: title for Luni; FlightHub logo (recolored white in Slides) replaced by the Luni wordmark in white (teamtailor PNG inverted through images.weserv.nl, 49×19 pt next to the "yuno |" lockup of the layout).
- S2 agenda: "04. Build vs. Buy" removed. S5: title and "A DEDICATED TEAM FOR LUNI". S11: title, subtitle, bullets 2 and 3 ("Stripe and Paddle stay, Yuno routes across them", "Local routes for European cards and new methods").
- S13, S14: rebuilt as above; the stray "$ 0.71" text boxes deleted. S16: pricing. S17 to S19 (Build vs. Buy) deleted. S21 (close): FlightHub icon replaced by the Luni wordmark. Appendix S18 ranges "4–16%", "8–12%", "20–40" now "4 to 16%" etc. (no dashes rule).
- Untouched: S3, S4, S6 to S10, S12, S15, S17, S19, S20.

## Verification
- Arithmetic (v3): 30,000 × $0.06 = $1,800 ($21,600 / yr); 10,000 × $0.05 = $500 ($6,000); subtotal $2,300 ($27,600); + $10,000 ($120,000) = $12,300 / month, $147,600 / year; $12,300 / 40,000 = $0.3075 → $0.31. Today: 16,000 × $0.06 = $960 + $10,000 = $10,960 (× 12 = $131,520); at 24,000: $11,440 (× 12 = $137,280). L1 4,000 × 18 × 12 = $864,000; 8,000 → $1,728,000. L2 320 × 18 × 12 = $69,120; 800 → $172,800. L3 $3,456,000 × 0.0025 = $8,640; × 0.005 = $17,280. L4 33.6 / 52 × 80,000 = $51,692; 73.2 / 52 × 80,000 = $112,615. Totals $993,452 / $2,030,695 / $1,512,074.
- Forbidden-token scan of the final text: only the standard signature line on the close slide ("German Tatis - Business Development Manager") carries a hyphen.
- Visual QA on thumbnails of slides 1, 2, 5, 11, 13, 14, 16, 21 after the build; second pass on 16 (bottom boxes shortened); third pass on 16 (40K table, scenario rows removed); fourth pass on 16 and 14 (platform $10K), PDF re-exported.
