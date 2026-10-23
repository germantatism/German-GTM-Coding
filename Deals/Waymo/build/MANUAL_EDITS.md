# Waymo connections deck · customisations on the live Google Slides file

Current deck (v8, 23 Oct 2026): `1NvO73rW7fvS2cZ-q9qsrWSnJsvQ0GvolXzYTIAw1Lb8` ("Deck - Waymo + Yuno · Connections & Payment Methods (Oct 2026)"), 79 slides.
Previous decks: v7 `1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY` and v6 `1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ`, renamed "OLD, do not use". The v6 copy stays as the reference the sync clones from.

The live file diverges from `gs/deck_spec.json`. After ANY rebuild from the spec: run `vault_slides.py <pid>` (four vault slides, Geist restyle), then the scripts in
`tools/connections/sync/post_build_waymo.py <new_pid>` (one script: intro kickers, $100B+, Moonactive, team slide, closing, next-steps removal, divider and vault wording, cover wordmark), which reproduces the reviewed look from the v6 reference deck.

## Why v7 exists (23 Oct 2026)
- Review found slide 11 speaker notes naming another customer's deck (removed) and Germany without PayPal or Klarna because the y.uno PayPal and Klarna pages omit Germany. `lib.py` now shows a method where a live provider carries it and the scheme serves the country; PayPal also appeared for New Zealand, Taiwan, Venezuela, Panama, Guatemala and the Dominican Republic, Klarna for Mexico. Full rebuild on a fresh template copy.

## Why v8 exists (23 Oct 2026)
- German: add the ride-hailing gap connections rated 8+ for South Korea, Japan, Taiwan, Hong Kong, Malaysia, Spain, Canada, Singapore, Indonesia, Germany, Argentina, Israel and the UAE and show them as "in homologation". `lib.HOMOLOGATING_EXTRA` adds them as Homologating rows (providers and methods) and replaces any lower tier the same name had (in code, signed, on request): NHN KCP, KG Inicis, Toss Payments, NICE Payments and Korean domestic cards via a local PG; GMO and JCB; LINE Pay; AlipayHK, Adyen and Global Payments for Hong Kong; DuitNow QR; Redsys; Moneris; AllinPay and PayNow; Midtrans (already homologating); Payone; Payway; Cal and Isracard; Magnati. Headlines say "more connections in homologation" where methods are included. Not real integration status: a commercial framing German chose.

## Customisations the sync re-applies (German's reviewed version)
- Intro: kickers removed ("THE YUNO STORY", "ABOUT YUNO · PLATFORM", "WHY YUNO?"), "$30B+" → "$100B+", Kraken → Moonactive (white PNG on Drive `1DVDaujX4mYhF79wDLsiXmiafHtOdbKuB`), page numbers 5 and 6.
- Team slide "Run by builders from top payments companies" (ten people incl. Antoine Cathelin, Head of Trust & Vault) cloned element by element; placed before the logo wall.
- Dividers: agenda line "03 CONNECTIONS AND PAYMENT METHODS IN TARGET MARKETS", no subtitle lines, "The Token Vault" capitalised, section 03 title "Connections and payment methods in target markets".
- Vault slides: problem slide market rows without years (London / Tokyo, Munich / Singapore, Toronto); summary slide without the INCLUDED pill, "Tokenization", "One token on both PSPs (and future)"; versus slide without the footer line.
- Closing: "Let's grow together", German's contact lines, `yuno | WAYMO` lockup (cloned from v6, layout graphics included); engine next-steps slide deleted. Cover Waymo wordmark sized as in v6.
- Speaker notes: no other customer named; second-PSP source worded "shared by Waymo with Yuno, October 2026".

## Limits
- `imageProperties.recolor` and `brightness` cannot be set through the Slides API and `replaceImage` drops them: logos that must render white on dark need a white PNG (recipe: download, PIL white + alpha, upload via Drive MCP, share with the service account, SA sets anyone-reader).
- Cloned text boxes are created with a transparent fill only when `shapeBackgroundFill.propertyState` is honoured (NOT_RENDERED first); name and role boxes on the team slide are widened 22% to avoid wrapping.
