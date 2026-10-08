# OnlyFans research B: complaints, payments news, checkout UX

Prepared 8 Oct 2026. Window: Oct 2025 to Oct 2026 unless stated. Rules: every claim has a URL; "No public information found" where searches came back empty; inference marked [INFERENCE, not confirmed]. Reddit could not be searched from this environment (the search tool refuses reddit.com), so Reddit volume is unmeasured. OnlyFans pages read through r.jina.ai (server-side text reader), as in ledger_onlyfans.md.

## 1. Payment complaints, last 12 months

### 1a. Frequency signal
| Source | What was found | Date range | URL |
|---|---|---|---|
| Trustpilot, onlyfans.com | 4,122 reviews total, TrustScore 1.2/5 (read 8 Oct 2026). Keyword filter "payment" surfaced 19 reviews on the first results page; 10 of them fall inside Oct 2025 to Oct 2026, and most of those are content-quality or creator-scam complaints, not processing failures | Mar 2025 to Oct 2026 | https://www.trustpilot.com/review/onlyfans.com ; https://www.trustpilot.com/review/onlyfans.com?search=payment |
| BBB, Fenix Internet (Fort Lauderdale) | 78 complaints in the last 3 years; "Not BBB Accredited"; no per-type breakdown or 12-month count was readable | 3 years to Oct 2026 | https://www.bbb.org/us/fl/fort-lauderdale/profile/web-design/fenix-internet-0633-90602738/complaints |
| Reddit | Not measurable (domain blocked for the search tool) | n/a | n/a |

Read: public payment-processing complaints are a thin, low-frequency signal (a handful of Trustpilot reviews a year). Most negative volume is about content value, refunds for content, and account bans. Do not describe declines as "systemic" or "high volume" on a slide on this evidence.

### 1b. Classified reviews inside the window (verbatim snippets, Trustpilot)
| Class | Date | Reviewer | Quote | URL |
|---|---|---|---|---|
| Declines / checkout error | 24 Nov 2025 | Malcolm Jones, "Unable to pay for subscriptions" | "the payment isn't taken. This a continual problem with this site" | https://www.trustpilot.com/review/onlyfans.com?search=payment |
| Declines | 26 Dec 2025 | Eric Carter, "Site sucks now" | "No proper payment transaction (mails) and also the card declines" | same |
| Unwanted renewal (recurring billing friction) | 15 Mar 2026 | James Staney, "Pay for a trial period and before I..." | "before I could cancel they withdrew the full payment for the next month" | same |
| Refund friction | 2 Jun 2026 | Stefan Nickolov, "Absolutely bad support" | "you have problem with a payment and they decline to pay you back" | same |
| Refund friction | 25 Sep 2026 | Emanuele, "Really something to avoid" | "I paid for a subscription that I can't even use" ... "I also asked for a refund and...haven't received any response" | https://www.trustpilot.com/review/onlyfans.com |
| Unauthorised charge claim | 31 Aug 2026 | Alex Stuart, "AVOID THIS COMPANY" | "they started taking money from my bank account via direct debit, despite me never knowingly authorising them" | same |
| Refund friction (content dispute) | 2 Oct 2026 | AP | "Only after I had paid was I told: 'this is not ur custom'" | same |

Outside the window but relevant (for context only, do not present as current):
| Class | Date | Quote | URL |
|---|---|---|---|
| Double charge, no refund | 3 Jun 2025 | "Taking payments after error...don't refund double payment" (Y B) | https://www.trustpilot.com/review/onlyfans.com?search=payment |
| Chargeback hits creator balance | 11 Apr 2025 | "Unjustified chargeback ... the amount was reversed, and my balance was reduced" (Anette Belori) | same |
| Payment methods disabled / account action | 8 Apr 2025, 22 Mar 2025 | "your team disabled payment methods and kick you off"; "after I submit a picture and payment verification I was banned" | same |
| Multiple renewals same day | undated in snippet | Search summary: one user "renewed ten times on the same day ... totaling $210". Could not confirm the date or the review page; treat as unverified | https://www.trustpilot.com/review/onlyfans.com |

Classes with no public evidence found in the window: 3DS failures (as a complaint, see 1c), payout delays (No public information found in Trustpilot/BBB results for Oct 2025 to Oct 2026; the Jan 2026 article in 2a asserts "payout delays" generally without data).

### 1c. Re-verification of the May 2026 brief's complaint rows (data/research/onlyfans-2026-05-11.md, section 5)
The May brief labelled these "2024 to 2026". Publication dates read today say otherwise:
| Source | Actual date | Status |
|---|---|---|
| https://pupuweb.com/solved-fix-onlyfans-transactions-error/ | Published 12 Apr 2021 | Old how-to; not evidence of a current pattern |
| https://medium.com/@mindyrosenghan/why-your-3d-secure-card-is-declined-by-onlyfans-system-7617e9e67c74 | Published 12 Nov 2022 | Old; SEO explainer, not a complaint |
| https://vocal.media/01/my-card-is-3-d-secure-but-only-fans-keeps-declining-my-card-why-does-only-fans-keep-declining-my-card | No date shown | SEO explainer, not a complaint |
| https://evertry.co/blog/how-to-subscribe-to-onlyfans-when-your-card-doesnt-work/ | Published 4 Jul 2025 | Vendor blog; country-decline claim (BR, IN, NG, EG, ZA) is the vendor's assertion, not complaint data |
Recommendation: drop "systemic 3DS declines, 2024 to 2026" framing. A current, sourced statement is only: a 3DS-capable card is required (see section 3) and some fans report declines (two Trustpilot reviews, Nov and Dec 2025).

## 2. Payments news, Oct 2025 to Oct 2026

| Flag | Date | Item | URL |
|---|---|---|---|
| 🟢 (investor, not a PSP) | 8 May 2026 | Architect Capital buys about 16% for $535M at a $3.15B valuation; commitment to build financial services for creators "often underserved by traditional financial institutions and products". Already in ledger rows C14 to C16, C24 | https://cryptobriefing.com/architect-capital-onlyfans-stake-3b-valuation/ ; https://www.riverfronttimes.com/onlyfans-just-closed-a-535-million-deal-that-could-finally-fix-the-banking-problem-nobody-talks-about/ ; https://www.netinfluencer.com/onlyfans-valued-at-3-15b-usd-as-parent-company-sells-16-percent-stake-to-architect-capital/ |
| Context | 31 Jan 2026 (pre-deal analysis, Pallavi Madhiraju) | "OnlyFans has long operated in a gray zone with major banks and card networks ... resulting in payout delays, service friction, and reputational hurdles." Speculates Architect "could enable a direct buildout of proprietary payment networks, onboarding tools, or escrow mechanisms" and cites a "2028 IPO target". Opinion, not company statement | https://business-news-today.com/?p=256908 |
| Name conflict to resolve | 2026 | Crypto Briefing summary names Architect Capital's founder and CEO as Julian Zegelman; the ledger (C15, Dealroom and Companies House) names James Sagan as founder and CEO and the new Fenix director. Do not print a founder name until checked against Architect's own site | https://cryptobriefing.com/architect-capital-onlyfans-stake-3b-valuation/ ; ledger C15 |
| Creator card / banking product | n/a | No public information found of an OnlyFans-branded creator card, bank account, or debit product launched Oct 2025 to Oct 2026 | searches 8 Oct 2026 |
| Stablecoin / crypto payments | n/a | No public information found of OnlyFans accepting or paying out in stablecoins. Historic crypto context only (ledger C32) | searches 8 Oct 2026 |
| New PSP / acquirer partnership | n/a | No public information found | searches 8 Oct 2026 |
| 🔴 PSP removal | n/a | No public information found | searches 8 Oct 2026 |
| Token vault RFP | n/a | No public information found | searches 8 Oct 2026 |
| Payments hiring | n/a | No public information found; a targeted search for "head of payments", processor or tokenization news returned nothing on OnlyFans. Consistent with ledger C31 (careers page unavailable) | searches 8 Oct 2026 |
| Search noise to ignore | 2026 | A result claiming 2026 "tiered subscriptions" and PayPal or Venmo integration came from a spam page on a university subdomain (demo2.ccps.virginia.edu); not a source | n/a |

[INFERENCE, not confirmed] With Architect's stated aim of creator financial products, any new payout, card or wallet product would add stored bank and card credentials, which is the vault angle; nothing public confirms a build or vendor.

## 3. Checkout UX (public sources only)

| Attribute | Finding | Source type | URL |
|---|---|---|---|
| Checkout type | Account-based, on-site. Prerequisites: accepted Terms, verified email, "added a valid payment card", "completed any additional onboarding steps based on where you live" | OnlyFans Help Center [F] | https://onlyfans.com/help/258/272/275 |
| Guest checkout | None: payment requires an account with verified email and a card on file (same page). [INFERENCE, not confirmed] no guest path exists | [F] | https://onlyfans.com/help/258/272/275 |
| Mobile vs app | "No. OnlyFans does not have an App." Users are told to add onlyfans.com to the home screen. So all checkout is web, incl. mobile web (ledger C29: 84.1% mobile web visits) | [F] | https://onlyfans.com/help/179/180/182 |
| Currency | "All prices appear, and are charged, in USD. Payment providers may charge currency conversion fees." | [F] | https://onlyfans.com/help/258/272/275 |
| Stored card and wallet | "Your Cards" section; Wallet top-up lets fans pay "without making a credit card transaction every time"; wallet used by default; "Make wallet primary method for rebills" | [F] | https://onlyfans.com/help/258/272/277 |
| Tips UX | "clicking 'Send Tip', entering the amount, and selecting the Payment method" | [F] | https://onlyfans.com/help/258/272/273 |
| Velocity limits | New users: max tip $100, rising to $200 after 4 months; "New users may spend up to $500 per day"; limits "set automatically by OnlyFans", changes by email to support | [F] | https://onlyfans.com/help/258/272/274 ; https://onlyfans.com/help/258/272/278 |
| Tax and jurisdiction charge | Sales or indirect tax and a separate "jurisdiction charge" may apply by location; exact amount shown and must be confirmed before processing | [F] | https://onlyfans.com/help/258/272/279 ; https://onlyfans.com/help/258/272/280 |
| 3DS | Third party (SolCard, card issuer, published 3 Aug 2026): OnlyFans "requires it on every card, every time"; adding a card triggers "a small verification charge and a step-up authentication prompt". OnlyFans' own help pages do not state the 3DS rule | [E], issuer with a commercial interest | https://www.solcard.cc/blog/onlyfans-payment-methods |
| Accepted brands | Third party: Visa, Mastercard, Maestro, Discover with 3DS. OnlyFans says only "the majority of payment cards" | [E] / [F] | https://www.solcard.cc/blog/onlyfans-payment-methods ; https://onlyfans.com/help/258/272/275 |
| Wallets (Apple Pay, Google Pay, Samsung Pay) | Not offered, per third party; PayPal not offered | [E] | https://www.solcard.cc/blog/onlyfans-payment-methods |
| BNPL | No public information found. [INFERENCE, not confirmed] none, given cards-only reporting | n/a | n/a |
| APMs / geo logic | No local APMs reported (no bank transfer, no crypto, no official gift card) per third party. The only geo-logic stated by OnlyFans is location-based onboarding steps, tax and jurisdiction charges | [E] / [F] | https://www.solcard.cc/blog/onlyfans-payment-methods ; https://onlyfans.com/help/258/272/275 |
| Prepaid cards | Retail prepaid gift cards "are not enrolled in 3D Secure, so they are declined"; reloadable prepaid "usually" works if 3DS enrolled; SolCard says its own Virtual card "is often declined by the issuing bank for this kind of merchant" | [E] | https://www.solcard.cc/blog/onlyfans-payment-methods |
| Known UX issues | Issuer declines on adult merchants (SolCard), renewals dependent on a fresh card charge unless wallet is primary (SolCard), plus the two Trustpilot decline reviews in 1b | [E] | as above |

Not verified by us: a live checkout walk-through (needs an age-verified account). Treat 3DS, wallets and brand list as third-party claims.
