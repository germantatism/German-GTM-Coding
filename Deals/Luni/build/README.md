# Proposal - Luni + Yuno (build, 2026-10-15)

Deck: https://docs.google.com/presentation/d/1H-YqtBpwkWZ6_JBDLcnSsTMaRnZWsLqVfHxmc-oma6g/edit (copy of "Proposal - FlightHub + Yuno").
Auth: service account `~/.config/gsuite/sa.json` (deck shared with gtm-claude-editor as editor). Deck id in `pid.txt`.

Order of execution (already applied, do not re-run on the same deck):
1. `build_luni.py dry` / `build_luni.py`: texts per element ID (`content_luni.py`), scenario rows and second header in the pricing card (duplicated objects), moves, logos, deletes (Build vs. Buy slides, agenda item 04, stray "$ 0.71" boxes), appendix ranges without dashes. Thumbnails of the changed slides.
2. `fix1_bottom_boxes.py`: pricing slide bottom boxes shortened after the visual review.

- `model.py`: all business case and pricing arithmetic. Change the tranche cut, the rates or the lever assumptions there and regenerate the texts.
- `common.py`: `fmt_requests` keeps regular / bold runs from `**bold**` markup; `two_run` for "big number + small suffix" boxes; `box_req` moves and resizes in points; `image_req` creates an image from a public URL.
- Luni wordmark: teamtailor PNG (black on transparent) inverted and cropped through images.weserv.nl (`filt=negate`); Slides recolor is read-only through the API, so the FlightHub images were replaced, not recolored.

For a one-off text change on the built deck, use the pattern in `fix1_bottom_boxes.py`.
