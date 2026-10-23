# HBO Max connections deck · manual edits on the live Google Slides file

Current deck (v2, 23 Oct 2026): `1vULwizzS9eoNpyOYCOEfxGDkZegRp_9bmPgPhUAy2zo` ("Deck - Skydance + Yuno · Connections & Payment Methods (Oct 2026)"), 91 slides.
Previous deck (v1): `1TyFXKt2OfoBLHGn8T1xX_Z1Uic_5ZYeeGUb8g_n0jrw`, renamed "OLD, do not use (v1)".

The live file diverges from `gs/deck_spec.json`. After ANY rebuild from the spec, re-apply the customisations below with the scripts in `tools/connections/sync/`
(`sync_hbo.py` + `sync_hbo2.py` for intro, team, closing, cover and next-steps removal; `final_touches.py` for the Moonactive logo and team box widths;
`hbo_cover_fix2.py` for the white Skydance cover logo; `hbo_text_edits.py` for the overview rows and the Netherlands headline).

## Why v2 exists (23 Oct 2026)
- The y.uno/integrations PayPal and Klarna pages omit countries the schemes serve (Germany, New Zealand, Taiwan, Venezuela, Panama, Guatemala, Dominican Republic for PayPal; Germany, Mexico and several European markets for Klarna). `lib.py` now shows the method where a live provider carries it and the scheme serves the country. Germany and seven other European markets gained PayPal and/or Klarna rows, so the deck was rebuilt on a fresh template copy.

## Customisations re-applied on v2 (same content as German's hand edits on v1)
- Intro: "THE YUNO STORY" and "ABOUT YUNO · PLATFORM" kickers removed, "$30B+" changed to "$100B+", "WHY YUNO?" kicker removed from the logo wall, Kraken replaced by Moonactive (white PNG on Drive `1DVDaujX4mYhF79wDLsiXmiafHtOdbKuB`, anyone-reader), page numbers 5 and 6 fixed.
- Team slide: the Yuno general-deck version ("Run by builders from top payments companies", ten people incl. Antoine Cathelin, Head of Trust & Vault) cloned element by element from v1, placed before the logo wall.
- Closing: "Let's grow together" with German's contact lines and the `yuno | SKYDANCE` lockup, cloned from v1 (layout graphics included); engine next-steps slide deleted.
- Cover: presenter line "Yuno · October 2026", lockup `yuno | SKYDANCE` (bar + white Skydance wordmark; the Skydance PNG is black on transparent and needs recolor, which the API cannot set, so the white asset from the closing slide is reused).
- Overview rows: Brazil shows NuPay, Colombia shows Daviplata (both are direct recurring methods the overview logic hides). Netherlands methods headline shortened to two lines.
- Speaker notes credit the code scan as "Yuno integration code scan and repo inventory (internal, October 2026)" (generator default).

## Still open
- Sharing is Yuno-domain reader only; send as PDF or open the link before sharing externally.
- `imageProperties.recolor` and `brightness` cannot be set through the Slides API; `replaceImage` drops them. Logos that must render white on dark need a white PNG.
