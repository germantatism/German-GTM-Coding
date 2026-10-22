# HBO Max connections deck · manual edits on the live Google Slides file

Deck: `1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw` ("Deck - Skydance + Yuno · Connections & Payment Methods (Oct 2026)").
The live file has diverged from `gs/deck_spec.json`. A rebuild from the spec would undo everything below.

## German, 22 Oct 2026 (by hand)
- Intro slides 3 to 6 and the closing slide 90 replaced with the Yuno general-deck versions (team slide now before the logo wall); engine `next_steps` slide deleted.
- Cover logo changed from HBO Max to Skydance (group renamed Skydance after the WBD close, 6 Oct 2026); file renamed "Deck - Skydance + Yuno …". Content keeps "HBO Max" (the product whose markets are listed).

## Claude review fixes, 22 Oct 2026 night (Slides API, script in session scratchpad `apply_fixes.py`)
- Cover lockup rebuilt as `yuno | SKYDANCE` (old `yuno + SKYDANCE` group deleted). Closing slide: layout lockup masked with a DARK1 rectangle and rebuilt right-aligned as `yuno | SKYDANCE`.
- White Skydance wordmark PNG hosted on Drive: `14HUjTxhJBEeGXfcbIvfV1MjnpM08DG4d` (anyone-reader), aspect 1000/170 = 5.88. `imageProperties.recolor` cannot be set through the API, hence the white PNG.
- Slide 49 (Netherlands methods) headline shortened to two lines (dropped "available").
- Pix biométrico removed as a recurring method: slide 13 Brazil row now `PIX Automático · NuPay · Smart PIX · Mercado Pago Wallet · Apple Pay · Google Pay · PayPal`; slide 72 headline "3 recurring local methods" and the "Other recurring methods" row without PIX biométrico. `lib.RECURRING_CODES` updated to match.
- Slide 13 Colombia row now shows Daviplata (named in the headline, previously hidden because `short_methods` only surfaces Apple Pay, Google Pay and PayPal among direct methods; NuPay same case).
- Page numbers on the pasted team (5) and logo-wall (6) slides corrected.
- Speaker notes on slides 8 to 14 rewritten without the code-scan / Caio Freitas reference.

## Still open
- Sharing is Yuno-domain reader only; send as PDF or open the link before sharing externally.
