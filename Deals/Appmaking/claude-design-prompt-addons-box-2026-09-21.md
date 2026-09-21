# Prompt Claude Design: AppMaking + Yuno, duplicate the pricing slide and price the add-ons (2026-09-21)

Target: the deck **"Proposal - AppMaking + Yuno"** (18 slides, already open in the canvas). **Duplicate slide 13, "The more you process, the less you pay per transaction"**, place the duplicate immediately after it as the new slide 14, and make every change below **on the duplicate only**. Keep its layout, typography, card language and color system exactly as they are; only the bottom-right box changes. Do not touch any other slide.

## Why this changes

On September 21 Tatsiana wrote that reconciliation and network tokens are still marked "Pending" on the pricing slide and asked for a ballpark on both. The duplicate answers that: the token vault is included at no cost, network tokens get a price per event, and reconciliation gets an estimated price. Slide 13 stays in the deck untouched so both versions can be compared side by side.

## Slide 14 (the duplicate): bottom-right box

Today this box reads "PENDING REVIEW · Scope and pricing to be reviewed together once the phase 1 providers are set." with two rows, "Reconciliation · Pending" and "Token vault & network tokens · Pending". Replace its content with:

**Box title** (same small caps bold style as "PENDING REVIEW"): **ADD-ONS**

**Sub-line** next to the title (same grey regular style as today's sub-line): "Estimated pricing. Reconciliation is optional and can be added later."

**Rows** (same row style as the box to its left: label in regular dark text, values in bold Yuno blue, the same treatment as "$14 for every alert"):

| Label | Value |
|---|---|
| Token vault | **Included** |
| Network tokens | **$0.05** per token created · **$0.01** per token update |
| Reconciliation | **$1,500 / month** with 50,000 reconciled transactions included, then **$0.032** per additional transaction |

Only the bolded parts are bold Yuno blue; the connecting words stay regular dark text.

**Fit rules for this box:**
- The box keeps its current position, width and height. Its top and bottom edges stay aligned with the "SUBSCRIPTIONS ENGINE & PRE CHARGEBACK ALERTS" box on its left.
- Title and sub-line share the first line, as they do today. The three rows go underneath, one row per line, at the same font size as the body text of the left box. Never go below that size.
- If a row does not fit on one line, use these shorter wordings instead of wrapping or shrinking: "Network tokens · **$0.05** per token, **$0.01** per update" and "Reconciliation · **$1,500 / month** incl. 50,000 reconciled trx, then **$0.032** each".
- Nothing overlaps and nothing touches the box border. Keep the same inner padding as the left box.

## Slide 14 (the duplicate): bottom-left box

This box was updated by hand in the live Google Slides version on September 18. On the duplicate it must read exactly as follows. If the canvas version differs, bring it to this text, and apply the same sync to slide 13 so both slides match the live deck. This is the only edit allowed on slide 13.

- Title: **SUBSCRIPTIONS ENGINE & PRE CHARGEBACK ALERTS**
- First **3K trx** processed free, then **$0.05** per transaction through the engine
- Ethoca alerts, Mastercard network: $**14 for every alert**
- Verifi RDR: enrolled through your PSP; cases surface in Yuno flagged as pre-dispute

## Everything else on the duplicate stays identical

Title, intro sentence, the TRANSACTION FEE table (flat $8,500 platform fee; $0.14, $0.10, $0.065, $0.05, $0.0425, $0.038, $0.035; all-in $12,000 to $19,000), WHAT IT INCLUDES, WHAT IT MEANS FOR APPMAKING ($11,300, $13,500, $16,000, $93,375, $173,375), FULLY RAMPED $16,000 / month, the note "The tier follows the month's successful transactions and applies to the whole month." and the footer "3-year contract term." Do not move, restyle or renumber any of it. The page number of the duplicate becomes 14 and the following slides shift by one.

## What NOT to do

- Do not edit slide 13 beyond the bottom-left box sync described above. Do not delete it.
- Do not leave the word "Pending" anywhere on the duplicate.
- Do not put a price on the token vault. It is "Included", with no number, no asterisk and no condition.
- Do not add other reconciliation packs, tiers, volume ranges or a per-year total. One line, exactly as written.
- Do not add words like "from", "starting at", "up to", "list price", "minimum" or "discount" to any price. "Estimated pricing" in the sub-line is the only qualifier.
- Do not mention TRID, Visa, Mastercard, token requestor, Solidgate or any PSP in this box.
- Do not add a Verifi price. Verifi RDR stays exactly as written in the bottom-left box.
- Do not add claims about approval rates, savings or comparisons with other vendors.
- Do not change, round or reformat any number on the slide.
- Do not use em-dashes or " - " as punctuation anywhere in the copy. Use "·" or commas.
