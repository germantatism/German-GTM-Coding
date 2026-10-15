# Proposal - Luni + Yuno (build, 2026-10-15)

Deck: https://docs.google.com/presentation/d/1H-YqtBpwkWZ6_JBDLcnSsTMaRnZWsLqVfHxmc-oma6g/edit (copy of "Proposal - FlightHub + Yuno").
Auth: service account `~/.config/gsuite/sa.json` (deck shared with gtm-claude-editor as editor). Deck id in `pid.txt`.

Order of execution (already applied, do not re-run on the same deck):
1. `build_luni.py dry` / `build_luni.py`: texts per element ID (`content_luni.py`), scenario rows and second header in the pricing card (duplicated objects), moves, logos, deletes (Build vs. Buy slides, agenda item 04, stray "$ 0.71" boxes), appendix ranges without dashes. Thumbnails of the changed slides.
2. `fix1_bottom_boxes.py`: pricing slide bottom boxes shortened after the visual review.
3. `fix2_price_at_40k.py` (German, same day): scenario block removed from the left card; 'What it means for Luni' table at 40,000 successful with one row per tranche ($14,300 / month, $0.36 per trx); today's bill kept in the sub-line.
4. `fix3_platform_10k.py` (German, same day): platform fee $12,000 -> $10,000 on the pricing slide (header, terms, table: $12,300 / month at 40,000, $0.31 per trx, today $10,960) and the cost line on Total Impact.
5. `fix4_bc_conservative.py` (German, same day): business case about 20% more conservative (+8 / +16 pts, +2% / +4%, 20 / 40 bps, 2 to 3 integrations; totals $0.80M / $1.21M / $1.62M). Re-applies every S13 / S14 text from `content_luni.T`.
6. `fix5_no_token_vault.py` (German, same day): 'PCI token vault · Included' row removed from 'What the rate covers' (rows below move up) and from the header sentence.

- `model.py`: all business case and pricing arithmetic. Change the tranche cut, the rates or the lever assumptions there and regenerate the texts.
- `common.py`: `fmt_requests` keeps regular / bold runs from `**bold**` markup; `two_run` for "big number + small suffix" boxes; `box_req` moves and resizes in points; `image_req` creates an image from a public URL.
- Luni wordmark: teamtailor PNG (black on transparent) inverted and cropped through images.weserv.nl (`filt=negate`); Slides recolor is read-only through the API, so the FlightHub images were replaced, not recolored.

For a one-off text change on the built deck, use the pattern in `fix1_bottom_boxes.py`.
