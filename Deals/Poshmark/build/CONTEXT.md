# Poshmark token vault deck · context (23 Oct 2026)

Owner: German Tatis. Request (23 Oct 2026): "make a deck for Poshmark like the one for Token Vault that we did for OnlyFans. It's the same, but adapted to Poshmark's reality. Do a research for Poshmark too to build it well."

## The account (INTERNAL, never on a slide)
- Salesforce / Gong account "Poshmark". Stakeholder: **Adam Clarke, Director of Payments Partnerships and Strategy**. Yuno side: Melissa Pottenger (VP Enterprise Growth NA), Samuel Vieira Tamayo (deal owner), Alejandro Albarracín (met Adam at MRC Vegas on 18 Mar 2026, converted the SQL). NDA (NMDA) signed 6 Apr 2026 via Ivvy Soberay (#legal-latam).
- Demo call 1 Apr 2026 ("Poshmark + Yuno | Demo", Gong 4827770647248792002). Adam: cards are fragmented and "bolted at both locations" between Braintree and Adyen; they recently completed a **40-million-record vault migration from Braintree to Adyen**; Hyperwallet is a payout provider, not a card vault; payouts via Hyperwallet, ACH, Instant Debit; fraud tools Sift, LexisNexis, Iovation. They use network tokens and an account updater; approval rate hit an all-time high of 94.99% the week before. A "payments microservice" was launching in May 2026, so no resources for new projects until H2 2026, tech-debt cleanup in Q3. "Slim team operating payments"; any solution must bring "efficiencies" and "economics". He was "not really sure why I would select one or the other" between a standalone vault and an orchestrator.
- Objections: platform reliability and uptime, data security in sandbox testing, limited budgets after leadership changes.
- Emails: Samuel 19 May 2026 asked for decline mix and transaction numbers for a business case (never received). Samuel 6 Oct 2026 introduced the standalone token vault as one PCI DSS Level 1 vault across Braintree and Adyen, offered a sandbox, noted Bay Area availability. No reply, no agreed next steps as of 23 Oct 2026.
- German's role: he is in SF through November; Poshmark HQ is Redwood City. Coordinate with Samuel and Melissa before sending.

## Source deck
OnlyFans + Yuno | Token Vault, 15 slides, Google Slides `1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8`. Copied on 23 Oct 2026 through German's Drive to:

**Deck - Poshmark + Yuno · Token Vault (Oct 2026)** · `1IzB5Cu6PGBEKGJzVGqc4mWpTNyNjLGmBHYyCTV-a7r8` · owner German, service account shared as writer.

Slide ids are preserved by the copy (same as `onlyfans_vault_source_dump.txt`). The Skydance build (`Deals/Paramount/build/`) is the pattern: gs_lib.py drawing primitives, content.py copy, build_vault_deck.py applies text edits by element id, redraws slide 3 (problem) and slide 7, writes speaker notes, reorders and renumbers.

## Fact bases
- Yuno vault facts: `Deals/OnlyFans/build/yuno_vault_facts.md` (docs.y.uno read 8 Oct 2026, re-checked 22 Oct 2026 for migration, export, stored credentials, Smart Retries).
- Poshmark public facts: `../research/poshmark_payments_2026-10-23.md` (web research, every claim with URL) and `../research/poshmark_live_site_2026-10-23.md` (feature flags and CSP from the poshmark.com bundle).
- Earlier note: `Events/Research/Poshmark/poshmark-stripe-sessions-research.md` (21 Apr 2026). Its "no orchestrator, Braintree and Affirm only" reading predates the Adyen evidence.

## Rules kept from the OnlyFans build
Only CONFIRMED / BETA / PUBLIC claims on slides; OPEN items in notes with an owner; no "+12%" / "20-30%"; house stats 7% uplift / 30% recovered; 460+ processor integrations; "dedicated TRID where the scheme allows it", never "in your name"; competitor pricing only in notes; never name SpaceX, Spike, Ria, Chess.com or other customers' deals; no internal names (Caio, sheet names). Public evidence of the two vaults comes from the web bundle, so the slides never need to quote the demo call; the 40M figure and the 94.99% approval rate stay in speaker notes as "what Adam told us", for German to use or drop.
