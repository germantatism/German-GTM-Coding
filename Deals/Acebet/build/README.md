# Proposal - Acebet + Yuno (build, 2026-10-27)

Deck: https://docs.google.com/presentation/d/1htv9kt0QUjbyklQVihkPmTLSWlenPuhZNXHydw79RcQ/edit (Drive copy of "Proposal - Luni + Yuno", Luni folder, owner German).
No business case (German, 27-oct-2026): the divider and the two business case slides go away, agenda becomes 01 Why Yuno / 02 Proposal.
Pricing (German, 27-oct-2026): $10,000 platform fee + 4 tranches per successful transaction, $0.030 / $0.025 / $0.020 / $0.015 (cuts 250K / 500K / 1M), about 2.5 cents average at 700K a month, top tranche at Spreedly's ~1.5 cents. All arithmetic in `model.py`.

Built 27-oct-2026 after German shared the deck with the SA (18 slides). Volume = last 30 days, 678,498 deposits / $22.77M (internal data via German), shown rounded as 680,000; first cut moved to 240,000 so the average lands at $0.025.
Then: `python3 build_acebet.py dry` and `python3 build_acebet.py` (applies once; thumbnails to the scratchpad). Dry-run before sharing with `ACEBET_PID=<Luni deck id>` (same object ids).
Logo: `../acebet-logo.png` (acebet.cc wordmark, white "BET" so it only shows on dark). The build deletes the Luni wordmarks on the cover and close; drop the PNG next to "yuno |" by hand (no public URL for the Slides API).
