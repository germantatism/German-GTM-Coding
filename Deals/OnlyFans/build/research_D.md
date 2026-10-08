# OnlyFans: accepted payment methods (Research Agent D)

Date: 8 Oct 2026. Method: official pages read through the text reader https://r.jina.ai/<url> (onlyfans.com blocks direct fetches). 4 web searches used. Builds on ledger rows P1 to P18 and V1 to V9 in `ledger_onlyfans.md`; new facts are tagged D1 onward.

Rule applied: only what a source states. Where OnlyFans does not name a method, this file says "not named on official pages", never "not accepted".

## 1. Pay-in (fan side)

| Market/Domain | Page Fetched | APMs Confirmed | PSP Signals | Source URL |
|---|---|---|---|---|
| Global, onlyfans.com (single domain) | Help: "How do I make a payment on OnlyFans?" | Payment cards only, worded as "OnlyFans accepts the majority of payment cards". Prerequisites: accepted Terms, verified email, "added a valid payment card", "completed any additional onboarding steps based on where you live". No card brand list on the page | "Payment providers may charge currency conversion fees." All prices charged in USD | https://onlyfans.com/help/258/272/275 |
| Global | Help: "How do I use the OnlyFans Wallet?" | OnlyFans Wallet (stored value, "Wallet Credits"). Funds added in the "Your Cards" section; wallet used by default when balance suffices; "Make wallet primary method for rebills" option | Wallet is funded through the cards section, so top-ups ride the card rail (inference from page wording) | https://onlyfans.com/help/258/272/277 |
| Global | Terms of Service | Payment card and Wallet Credits. "if you attempt a purchase that costs more than the total amount of your remaining Wallet Credits, your payment card will be charged the full amount"; "Wallet Credits are subject to a maximum amount as indicated"; non-refundable | "All Fan Payments will be received and processed by a third-party payment provider we approve."; "We may change which third-party payment providers process Fan Payments."; provider takes "periodic payments" for Subscriptions and "immediate payments" otherwise. No provider named | https://onlyfans.com/terms |
| Global | Help: "How do I tip a creator?" | Fan selects "the Payment method you want to use" (methods not enumerated) | None | https://onlyfans.com/help/258/272/273 |
| Global | Help: tip and daily limits (D1) | n/a. New users: max tip $100, rising to $200 after 4 months; new users may spend up to $500 per day; limits "set automatically by OnlyFans", changes via support@onlyfans.com | Velocity limits are risk controls set by OnlyFans | https://onlyfans.com/help/258/272/274 ; https://onlyfans.com/help/258/272/278 |
| Global | Help: tax and "jurisdiction charge" (D2) | n/a. Sales or indirect tax and a separate "jurisdiction charge" may be added "depending on where you live", shown before confirmation | Location-based pricing logic at checkout | https://onlyfans.com/help/258/272/279 ; https://onlyfans.com/help/258/272/280 |
| Global | Help: "Does OnlyFans have an App?" (D3) | "No. OnlyFans does not have an App." Web only (add to home screen) | No app store billing channel; all pay-in is web checkout | https://onlyfans.com/help/179/180/182 |
| Global | Help: refunds (D4) | n/a. Subscriptions, tips, streams, paid posts and paid messages "non-refundable unless there has been a violation" of the Terms | None | https://onlyfans.com/help/258/282/285 |
| Global | Help: card statement descriptor | Already in ledger P8 ("OnlyFans", "OF", "OnlyFans.com") | Already in ledger | https://onlyfans.com/help/258/272/276 |
| Card brands, 3DS, wallets (Apple Pay, Google Pay, PayPal), prepaid, gift cards | Third-party blog only | NOT VERIFIED on official pages. Third parties claim Visa, Mastercard, Maestro, Discover with mandatory 3D Secure, and list PayPal, Apple Pay, Google Pay, gift cards, crypto as unavailable. No OnlyFans page names a brand, a 3DS rule, or a digital wallet | n/a | https://www.solcard.cc/blog/onlyfans-payment-methods (third party, ledger P7 already covers) |
| UK, Germany, Brazil, Mexico, India | Language and country variants of the Help Center | NOT VERIFIED: no regional help exists. https://onlyfans.com/de/help , /pt/help and /es/help return "Sorry, this page is not available". `?lang=de` and `?lang=pt` return the same English content as the global page. The help copy says onboarding steps, tax and jurisdiction charges vary "based on where you live" but no page lists a country-specific payment method | None | https://onlyfans.com/help/258/272/275?lang=pt ; https://onlyfans.com/help?lang=de |

## 2. Payouts (creator side)

| Market/Domain | Page Fetched | Methods Confirmed | PSP Signals | Source URL |
|---|---|---|---|---|
| Global | Help: "How do I get paid my earnings on OnlyFans?" | Method "will depend on where you live"; minimum $20 "for most payout methods"; manual "Request withdrawal" or automatic Monthly, Weekly or Daily "if available". Methods not enumerated | Already in ledger P11 | https://onlyfans.com/help/196/244/245 |
| Global, outside US | Help: "Why is my payment delayed?" (D5) | Bank wire transfer named explicitly: "For bank wire transfers (outside US), please ask your bank to provide you with your Destination Trace ID" | Delays attributed to "the payment provider which is outside OnlyFans' control"; escalation to payments@onlyfans.com | https://onlyfans.com/help/196/244/248 |
| Global | Help: "Why am I being charged a fee by my bank on payments from OnlyFans?" (D6) | Bank and e-wallet named as payout destination types: payout sent in USD "to your payment method"; "Your bank or e-wallet provider may charge you currency conversion or other fees" | USD-only payout, FX borne by creator | https://onlyfans.com/help/196/244/251 |
| Global | Terms of Service | "Payout Options by direct bank transfer" (data stored by OnlyFans) and Payout Options registered "with a payment provider" (data not stored); "e-wallet provider charges" referenced | Split between direct bank rail and third-party payout providers, none named | https://onlyfans.com/terms |
| Global | Help: "Can I become an OnlyFans Creator where I live?" (D7) | Country eligibility list sits behind login in the "Add Bank" section and "is updated regularly"; not public | NOT VERIFIED: country list requires a logged-in account | https://onlyfans.com/help/196/197/201 |
| Global | Help: "Payout percentages" | Creators receive 80%, OnlyFans retains 20% (matches ledger P3) | None | https://onlyfans.com/help/196/197/287 |
| Named payout providers (Paxum, Skrill, Cosmo Payment, ePayments), ACH, SEPA | Third-party blogs; Paxum site search | NOT VERIFIED on official pages. Third parties cite ACH (US), international wire, SEPA, Paxum. A search restricted to paxum.com, cosmopayment.com and skrill.com returned no page naming OnlyFans | n/a | https://www.sirency.com/onlyfans-payment-methods ; https://scrile.com/blog/how-does-onlyfans-pay-you (third party, ledger P14 already covers) |

## 3. Proposed new ledger rows

| ID | Fact | Source | Tag | Use in brief |
|---|---|---|---|---|
| D1 | Velocity limits: tip max $100 for new users, $200 after 4 months; new users up to $500 per day; set automatically by OnlyFans | help/258/272/274 ; help/258/272/278 | [F] | Yes |
| D2 | Location-based indirect tax and a separate "jurisdiction charge" added at checkout | help/258/272/279 ; help/258/272/280 | [F] | Yes |
| D3 | No app; web-only checkout | help/179/180/182 | [F] | Yes |
| D4 | All fan purchases non-refundable unless Terms violated | help/258/282/285 | [F] | Notes only |
| D5 | Outside-US payouts by bank wire, traced by Destination Trace ID; delays attributed to the payment provider | help/196/244/248 | [F] | Yes |
| D6 | Payout destinations described as bank or e-wallet, paid in USD | help/196/244/251 ; terms | [F] | Yes |
| D7 | Creator-eligible country list only visible in logged-in "Add Bank" section | help/196/197/201 | [F] | Notes only |
| D8 | Terms: "We may change which third-party payment providers process Fan Payments." | terms | [F] | Yes (multi-provider flexibility written into the contract) |

All official URLs above were read via https://r.jina.ai/ on 8 Oct 2026.
