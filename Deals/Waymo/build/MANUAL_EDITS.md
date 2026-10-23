# Waymo connections deck · customisations on the live Google Slides file

Current deck (v7, 23 Oct 2026): `1r7g6kFtX8ZENovd3-51qyx9M0369yYLahpwXEGeEHRY` ("Deck - Waymo + Yuno · Connections & Payment Methods (Oct 2026)"), 80 slides.
Previous deck (v6): `1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ`, renamed "OLD, do not use (v6)".

The live file diverges from `gs/deck_spec.json`. After ANY rebuild from the spec: run `vault_slides.py <pid>` (four vault slides, Geist restyle), then the scripts in
`tools/connections/sync/` (`sync_intro.py` + `sync_closing.py` + `fix_team_closing.py` + `fix_team_width.py` + `final_touches.py`) which reproduce the reviewed look from the previous deck.

## Why v7 exists (23 Oct 2026)
- Review found slide 11 speaker notes naming another customer's deck (removed) and Germany without PayPal or Klarna because the y.uno PayPal and Klarna pages omit Germany. `lib.py` now shows a method where a live provider carries it and the scheme serves the country; PayPal also appeared for New Zealand, Taiwan, Venezuela, Panama, Guatemala and the Dominican Republic, Klarna for Mexico. Full rebuild on a fresh template copy.

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
