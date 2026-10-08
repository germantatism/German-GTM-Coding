# -*- coding: utf-8 -*-
"""Product direction slides (source: "DRAFT - Yuno × OnlyFans · Token Vault and banking orchestration",
Google Slides 1uJQwxertVAF2G2yNqvam9DtfSzBNAuCjEGLwotaKUMU, owner m@y.uno, 8 Oct 2026).
Every slide carries the DIRECTION pill and the line "Product direction, not a delivery commitment",
and maps to open items 2, 3 and 6. Placed at the end of Section 06, after "who decides"."""

K = "THE YUNO TOKEN VAULT · PRODUCT DIRECTION"
DISCLAIMER = "Product direction, not a delivery commitment. Rule-based allocation, the US banks and issuers behind the API, and the yield providers are open items 2, 3 and 6 on slide {{slide:owe}}."

SLIDES = {}

# ---------------------------------------------------------------- 1. one creator account, every bank behind it
SLIDES["direction-architecture"] = {
    "id": "direction-architecture", "type": "diagram",
    "kicker": K + " · HOW IT WORKS",
    "headline": "One creator account. Every bank behind it.",
    "tag": ["DIRECTION"],
    "source": DISCLAIMER,
    "boxes": [
        {"id": "creators", "x": 0, "y": 0, "w": 130, "h": 44, "title": "Creators", "body": "Sign up once", "style": "outline"},
        {"id": "of", "x": 145, "y": 0, "w": 275, "h": 44, "title": "OnlyFans", "body": "One account per creator · Sets the rules", "style": "outline"},
        {"id": "orch", "x": 0, "y": 66, "w": 205, "h": 70, "title": "Yuno · orchestration", "body": "Decides where money lives and moves. Opens accounts, runs your rules, routes every transfer, shows every balance in one view.", "style": "blue"},
        {"id": "vault", "x": 215, "y": 66, "w": 205, "h": 70, "title": "Yuno · vault", "body": "Holds the data every provider needs: KYC, tax IDs, bank details, W-9s and cards. Collected once, reused for every provider you add; cards forwarded through the proxy.", "style": "blue"},
        {"id": "banks", "x": 0, "y": 160, "w": 98, "h": 58, "title": "Banks", "body": "2 to 5 per creator", "style": "light"},
        {"id": "issuers", "x": 107, "y": 160, "w": 98, "h": 58, "title": "Card issuers", "body": "Add or swap at any time", "style": "light"},
        {"id": "rails", "x": 215, "y": 160, "w": 98, "h": 58, "title": "Transfer rails", "body": "ACH, wire and RTP", "style": "light"},
        {"id": "ramps", "x": 322, "y": 160, "w": 98, "h": 58, "title": "Stablecoin ramps", "body": "On and off-ramp partners", "style": "light"},
    ],
    "connectors": [
        {"from": "creators", "to": "of"}, {"from": "of", "to": "orch", "label": "rules"}, {"from": "orch", "to": "vault"},
        {"from": "orch", "to": "banks"}, {"from": "orch", "to": "issuers"}, {"from": "vault", "to": "rails"}, {"from": "vault", "to": "ramps"},
    ],
    "side": {"header": "WHAT IT MEANS", "items": [
        {"title": "Yuno never holds the money", "body": "The banks do. Yuno opens the accounts, runs your rules and routes the transfers."},
        {"title": "One platform, both directions", "body": "Fan payments in and creator payouts out run on the same platform, with every balance in one view."},
        {"title": "Collected once", "body": "The vault holds what every provider asks for, so adding a bank or an issuer does not mean asking the creator again."},
    ]},
    "notes": "This is where the product is going, and we label it as direction rather than as a delivery commitment. A creator signs up once. OnlyFans holds one account per creator and sets the rules. Yuno's orchestration decides where the money lives and moves: it opens the accounts, applies your rules, routes every transfer and shows every balance in one view. The vault underneath holds the data every provider needs, collected once and sent to any provider through the proxy. Behind it sit two to five banks per creator, card issuers you can add or swap, ACH and wire rails, and stablecoin on and off-ramp partners. Yuno never holds the money; the banks do. The pieces that are not yet in our public documentation are open items 2, 3 and 6, with owners.",
}

# ---------------------------------------------------------------- 2. you set the rules, no single bank can cut a creator off
SLIDES["direction-rules"] = {
    "id": "direction-rules", "type": "two_column",
    "kicker": K + " · CONTROL AND RESILIENCE",
    "headline": "You set the rules. No single bank can cut a creator off.",
    "tag": ["DIRECTION"],
    "source": DISCLAIMER,
    "cols": [
        {"header": "YOU SET THE RULES", "items": [
            {"title": "Write the policy once", "body": "Yuno applies it to every creator and logs each decision with the rule that triggered it."},
            {"title": "Spread each creator across 2 to 5 banks", "body": "And cap how much any one bank can hold."},
            {"title": "Send each payout on the cheapest or fastest rail", "body": "Per transfer, by rule, not by code."},
            {"title": "Send new creators to the bank you choose", "body": "Allocation is a setting you own, changeable without a deployment."},
        ]},
        {"header": "NO SINGLE POINT OF FAILURE", "items": [
            {"title": "Backup accounts opened at sign-up", "body": "Yuno opens the backup accounts when the creator signs up, not after an incident."},
            {"title": "Automatic move on a freeze or closure", "body": "If a bank freezes or closes an account, inbound funds and payouts move to the next bank automatically."},
            {"title": "The bank's ledger stays the record of truth", "body": "Yuno reconciles with each bank every day."},
        ]},
    ],
    "bar": "**Why it matters.** In 2021 one group of banks nearly stopped the business. Under this design losing a bank is a reallocation your rules already anticipated, logged decision by decision.",
    "notes": "Two things you asked for, as product direction. First, you set the rules: write the policy once, and Yuno applies it to every creator and logs each decision with the rule that triggered it. Spread each creator across two to five banks, cap how much one bank can hold, send each payout on the cheapest or fastest rail, send new creators to the bank you choose. Second, no single point of failure: backup accounts are opened when the creator signs up, so if a bank freezes or closes an account, inbound funds and payouts move to the next bank automatically. The bank's ledger stays the record of truth and Yuno reconciles with each bank every day. Rule-based allocation across banks and issuers is open item 2; which US banks sit behind the API is open item 3.",
}

# ---------------------------------------------------------------- 3. earn on idle balances, swap issuers freely
SLIDES["direction-yield"] = {
    "id": "direction-yield", "type": "two_column",
    "kicker": K + " · BEYOND THE ACCOUNT",
    "headline": "Earn on idle balances. Swap issuers freely.",
    "tag": ["DIRECTION"],
    "source": DISCLAIMER,
    "cols": [
        {"header": "YIELD ON IDLE BALANCES", "items": [
            {"title": "Treasury-backed balances", "body": "Balances that sit in US T-bills, through Jiko."},
            {"title": "Or convert to stablecoins", "body": "Through Coinbase and Triple-A."},
            {"title": "Your rules decide how much moves and when", "body": "Yuno never holds funds or crypto. The yield rules under the GENIUS Act are still settling, which is why conversion and custody credentials stay portable."},
        ]},
        {"header": "PLUGGABLE ISSUERS", "items": [
            {"title": "Issuers connect like PSPs and banks", "body": "A card issuer connects to Yuno the same way a processor or a bank does."},
            {"title": "No new KYC from the creator", "body": "The vault already holds the creator's verified data, so a new issuer's onboarding can reuse it instead of asking the creator again."},
            {"title": "Swap without a project", "body": "Adding or replacing an issuer is a configuration change on your side."},
        ]},
    ],
    "bar": "**One platform for the full creator money flow.** Fan payments in, balances across banks, payouts and cards out.",
    "notes": "Beyond the account, two parts of your design, as product direction. Yield: idle balances can sit in Treasury-backed accounts through Jiko, or be converted to stablecoins through Coinbase and Triple-A; your rules decide how much moves and when, and Yuno never holds funds or crypto. The stablecoin providers are open item 6. Pluggable issuers: a card issuer connects to Yuno the same way a processor or a bank does, and because the vault already holds the creator's data, a new issuer needs no new KYC and no change to your integration. Showing an issued card to its holder and setting a PIN are not in our documentation today, as the appendix states.",
}
