# Autodesk · orchestration and vault deck · context (26 Oct 2026)

Owner: German Tatis. Request (26 Oct 2026): a Google Slides deck of at most 12 slides, in the style of the Carry1st, OnlyFans, Waymo and Higgsfield decks, that answers one question for Justo: why Autodesk should include Yuno in its token vault and payment orchestration RFP. Orchestration and vaulting first, then "a bit beyond". Every solution slide tailored to Autodesk. One "how things stand today" slide, which German decides to keep or drop. Clear and concise.

## The account (INTERNAL, never on a slide)
- RFP intel: German heard on 19 Oct 2026 (industry conversations, Money20/20 Vegas) that Autodesk is preparing an RFP for token vault plus payment orchestration. On 23 Oct 2026 Austin Clark (VGS, Global Director Sales and Partnerships) confirmed by email that Autodesk is running the process under strict RFP rules and an NDA with VGS, and recommended cold outreach to Autodesk "without mentioning VGS". German forwarded to Sean. Never name VGS or the source anywhere ([[feedback_never_expose_backchannel_source]]).
- Outreach so far (all unanswered as of 26 Oct 2026): Jeong Sohn, Catherine Winfield (follow-up 23 Oct, Sean in cc), Chelsea Hall (follow-up 23 Oct), Neil O'Connor, Sebastian Goodwin, Thierry Carel, Brandon Hillstead, Raji Arasu. dev.patel@autodesk.com bounced (blocked). Addresses are guessed first.last@autodesk.com.
- No Yuno activity in Gong, Slack or Drive before 19 Oct 2026. Salesforce account 001Ps00001Ti0MUIAZ exists (owner unchecked).
- German is based in San Francisco through November; Autodesk HQ is One Market.

## Source deck and build
- Base: OnlyFans + Yuno | Token Vault, 15 slides, Google Slides `1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8`, copied on 26 Oct 2026 through German's Drive to **Autodesk + Yuno · Orchestration and Vault (Oct 2026)** · `1H0NFvyWIPy6tGDQi7E_910v08y2Sokf_vkvvrF9o6-s` · owner German, service account gtm-claude-editor@ shared as writer. Slide ids preserved by the copy.
- Pattern: Deals/Poshmark/build (gs_lib.py primitives, content.py copy, build script applies text edits by element id, redraws bodies, draws new slides from the chrome of an existing one, writes notes, reorders and renumbers).
- Final order (12): cover · executive summary · how things stand today (optional) · one vendor for both halves · orchestration architecture · renewals routing · vault cards · portability · beyond the RFP · proven (house) · trusted by (house) · next steps.
- Dropped from the OnlyFans base: network tokens detail, personal data, your design, proxy how it works, proxy controls, versus VGS/Basis Theory, team.

## Fact bases
- Autodesk public facts: `data/research/autodesk-2026-10-19.md` (FY26 10-K, Terms and Payments pages per country from Wayback snapshots Mar to Oct 2026, Online Purchase Terms Dec 2025). Contact map: `data/research/autodesk-contacts-2026-10-19.md`.
- Yuno vault facts: `Deals/OnlyFans/build/yuno_vault_facts.md` (docs.y.uno, read 8 and 22 Oct 2026). y.uno vault page and subscriptions page re-read 26 Oct 2026.

## Rules kept
Only verified claims on slides (published stats: up to 7% uplift, 30% recovered revenue, 1,000+ methods, 190+ countries, 460+ processor integrations on the vault page); no "+12%" or "20-30%"; "dedicated TRID where the scheme allows it", never "in your name"; no dashes as punctuation; USD only; no customer deal names (SpaceX, Chess.com, Spike, Ria); no internal names; Digital River, Adyen-in-Australia and the complaint threads are inferences and stay out of the deck; the renewal complaints are never quoted.
