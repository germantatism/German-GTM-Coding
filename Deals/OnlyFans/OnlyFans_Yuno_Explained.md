# OnlyFans + Yuno: token vault and banking connectivity, explained

Prepared for German Tatis, 9 October 2026. Based on every version of the deck (Samuel's 25-slide content, the 57-slide build, the 28-slide revised deck, the 10 and 15-slide versions, Justo's banking skeleton), the OnlyFans research brief of 8 October 2026, and Yuno's public documentation.

# Part 1. Explained like you are four years old

## The story

OnlyFans is a big website where people called creators make videos and photos. Fans pay to see them. Every year fans pay more than eight billion dollars, and OnlyFans sends most of that money to the creators.

To pay, a fan gives OnlyFans a card. A card number is like a house key: if a bad person copies it, they can get in. So the card number must be kept in a very strong safe. That safe is called a **vault**.

When OnlyFans needs to charge the card, it does not take the key out of the safe. The safe gives OnlyFans a **token** instead. A token is like a toy key with a number painted on it. It looks like a key, it opens the right door when the safe says so, but if a bad person steals it, it opens nothing.

## What OnlyFans wants to build

OnlyFans wants every creator to have one account, like one piggy bank. Behind that piggy bank, the money is really kept in two to five real banks. Why so many? Because once, in 2021, a few banks did not want to work with OnlyFans anymore, and OnlyFans almost had to stop paying creators. If you keep your toys in five boxes and one box gets taken away, you still have four boxes.

They also want:
- **Cards for creators** made by companies called **issuers**, and they want to be able to change issuer the way you change a shoe that does not fit.
- **Stablecoins**, which are digital dollars, so money sitting still can grow a little.
- To start only in the United States.

## The problem

All of this needs lots of secrets: fans' card numbers, creators' bank account numbers, their ID documents, their tax numbers. Today the card numbers live with the companies that charge the cards (processors), and the bank numbers live inside OnlyFans. Two piles of secrets, in two places.

OnlyFans opened a contest called an **RFP** to choose who builds the vault. Yuno arrived late to the contest. The deck is our way of saying "please let us play too."

## What Yuno offers

1. **One safe for every secret.** Cards, bank accounts, IDs, tax numbers, all in one vault.
2. **A messenger (the proxy).** When a bank or a processor needs a real secret, the messenger takes the toy key, swaps it for the real one inside the safe, and delivers it. OnlyFans never touches the real secret.
3. **Wires to every bank (banking connectivity).** Yuno already knows how to talk to banks, card issuers and money rails, so OnlyFans does not have to build each wire itself.
4. **OnlyFans makes the rules.** OnlyFans decides which bank each creator uses. Yuno just follows the rules. And Yuno never holds the money: the banks do.

## Why not someone else

Two other companies, VGS and Basis Theory, sell only the safe. They are good safes. But with them, OnlyFans would have to build all the wires and all the rules by itself. With Yuno, the safe comes with the wires and the rule book.

## What we want now

We want OnlyFans to say: "Yes, Yuno can join the contest," and then to test us in a practice area called a **sandbox**.

# Part 2. From zero to expert

## 2.1 The deal in one page

| Item | What we know |
|---|---|
| Company | OnlyFans, operated by Fenix International Ltd (London, company 10354575); US entity Fenix Internet LLC |
| Trigger | OnlyFans opened a token vault RFP in October 2026. Yuno is late; the goal is to be included |
| Path | Our contact forwards the deck to OnlyFans' Payments Manager, who reads it without us in the room |
| Their design | One creator account; 2 to 5 banks behind it; pluggable card issuers; several bank-transfer providers; stablecoin conversion for yield; US balances first |
| Their main question | Who decides which bank, issuer and rail each creator lands on. Answer: OnlyFans, by rule. Yuno executes |
| What changed on 9 Oct | Juan Pablo (CEO) asked for a short deck (10 to 15 slides) and the term **banking connectivity**, not "banking as a service". OnlyFans said: "I don't want banking as a service. I want to literally work with banks." Justo asked to fold in his banking skeleton and send the same day |
| Deck to send | 15 slides, link: docs.google.com/presentation/d/1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8 (10-slide alternative: 1gUfjfGbSmherHHMgJcPpBsauoNSSBpzEJipT4govY2g) |
| Yuno people | Antoine Cathelin, Head of Trust & Vault (the lead for OnlyFans); Justo Benetti, CRO; Juan Pablo Ortega, CEO; Samuel Vieira prepared the first content |
| History | An earlier OnlyFans opportunity in Salesforce is marked lost (June 2026). No Gong calls recorded |

## 2.2 OnlyFans, the business

| Metric | Value | Source |
|---|---|---|
| Net revenue, year to 30 Nov 2025 | $1.55B (up 10%) | FY2025 accounts, filed 20 Sep 2026 |
| Paid to creators that year | $6.3B | Reporting on the FY2025 accounts |
| Paid to creators since 2016 | More than $30B | Same |
| Active creators / active fan accounts | 2.5M / 132M | Same |
| Employees | 47 | Accounts |
| Revenue by region | US $965M · UK and Europe $347M · rest of world $241M | Accounts, note 4 |
| Pricing | Everything in USD; OnlyFans keeps 20% of each fan payment | Terms of Service |
| Ownership | Architect Capital bought about 16% for $535M at a $3.15B valuation (May 2026). Its founder, James Sagan, joined the board on 8 May 2026 and plans "financial products for creators" | Bloomberg, Companies House, Dealroom |
| People | CEO Keily Blair; CFO Lee Taylor (director since 2021) | Companies House |

**How they take payments today (public facts only).**
- Fans pay with a card or an OnlyFans Wallet, on the web only. There is no app.
- The Terms say payments are processed by "a third-party payment provider we approve", and that OnlyFans "may change which third-party payment providers process Fan Payments".
- The audited accounts show money due from several "Payment Service Providers" ($134.9M), but no provider is named anywhere official. CCBill, Stripe, Merrick and Harris are only third-party claims.
- The Privacy Policy says OnlyFans does "not receive your full payment card number". So the cards live with the processors.
- OnlyFans does store creators' bank account details for direct-transfer payouts, plus ID documents and tax data, for up to 7 years.
- Payouts depend on where the creator lives. Outside the US they go by bank wire. There is a $20 minimum, a 7-day pending period (21 days in some countries) and 3 to 5 business days to pay.
- No orchestrator, no vault vendor and no PCI attestation are public.

**Why multiple banks matter to them.** In August 2021, OnlyFans announced a ban on explicit content because, in the founder's words, "the short answer is banks": BNY Mellon, Metro Bank and JPMorgan were rejecting transfers and closing accounts. The ban was reversed six days later. In 2024, CEO Keily Blair said a bank rejected her personally because of OnlyFans. Their design (2 to 5 banks per creator) is the structural answer. Handle this history with care: do not bring it up in front of them unless they do.

## 2.3 Payments vocabulary you must own

| Term | Meaning, in one or two sentences |
|---|---|
| PAN | The full card number. The single most sensitive piece of card data |
| PCI DSS | The card industry's security standard. Level 1 is the strictest, required at high volume. Whoever stores PANs must be certified |
| SAQ A | The lightest PCI self-assessment for a merchant, possible when card data is captured by a certified provider's hosted fields and never touches the merchant's systems |
| Tokenization | Replacing a sensitive value with a meaningless substitute (a token) that only the vault can map back |
| Token vault | The certified system that stores the real values and issues the tokens |
| Detokenization | Turning a token back into the real value, inside the vault, only for an authorised use |
| Proxy (forward proxy) | The vault sends a request to a third party on the merchant's behalf, swapping tokens for real values on the way, so the merchant never sees them |
| Processor / PSP / acquirer | The companies that run card payments for a merchant. PayPal counts as a wallet, not a processor, in our house rules |
| Network token | A token issued by Visa, Mastercard or Amex themselves to replace the PAN. Survives card reissue and usually improves approval rates |
| Cryptogram | A one-time code generated for each network-token payment, proving the token is used legitimately |
| Token Requestor ID (TRID) | The registration with a card network that owns the network tokens. Whoever holds it controls portability, which is why a vault buyer asks "whose name is it in?" |
| PAR (Payment Account Reference) | A reference that links a PAN, its network tokens and wallet tokens to the same underlying account. One fan stays one fan across card, wallet and reissue |
| Account updater | A service that refreshes stored cards when the bank reissues them (new number or expiry) |
| CIT / MIT | Customer-initiated vs merchant-initiated transaction. Subscription renewals are MITs and need the network transaction ID of the first charge |
| NTID | Network transaction ID. The reference that chains recurring payments; losing it on migration can break renewals |
| 3DS | Card authentication step (the bank's challenge). Yuno can run it standalone and return the result for any acquirer |
| ACH, same-day ACH, wire, RTP | US bank transfer rails: ACH is batch and cheap, same-day ACH is faster, wire is immediate and expensive, RTP is real-time |
| Issuer | A company that issues cards (to creators, here). "Pluggable issuers" means they can be added or swapped |
| Stablecoin | A digital token pegged to the dollar. The GENIUS Act (July 2025) bars issuers from paying holders interest or yield; how platforms can offer rewards is still being settled by regulators |
| Banking connectivity | Yuno's term for connecting a platform to banks: entities, onboarding on a named bank connection, accounts, transfers. Use it instead of "banking as a service" with OnlyFans |

## 2.4 What a token vault buyer evaluates

1. **Storage and capture.** Is it PCI DSS Level 1? Does capture keep the merchant at SAQ A?
2. **Data beyond cards.** Can it hold bank accounts, identity documents and tax IDs, not only cards?
3. **Network tokens.** Which networks, whose TRID, cryptograms, account updater, PAR.
4. **The proxy.** Can it send stored data to any destination, with allowlists, mutual TLS and audit logs?
5. **Portability and exit.** Can I take my data and tokens out, under what conditions, and with the NTIDs?
6. **Resilience.** Uptime commitment, what happens if the vault goes down, subprocessors.
7. **Control.** Who in my company can see or use each field (access by role), retention, audit.
8. **What sits above the vault.** Who builds the provider connections, the routing rules and the payouts.

## 2.5 The Yuno answer, capability by capability

| Capability | What Yuno offers | Status to be honest about |
|---|---|---|
| Card vault | PCI DSS Level 1 (v4.0), SOC 2 Type 2, ISO 27001, ISO 27701, Visa Service Provider. SDK enrollment keeps most merchants at SAQ A. Zero-amount verification optional | Documented |
| One token, any processor | A vaulted token works on every processor connected; 460+ processor integrations | Documented |
| Network tokens | Visa, Mastercard and American Express per docs; cryptograms for Visa and Mastercard; network token import process | Docs say Amex, but internal engineering says Amex is still in certification. Confirm per network before a sandbox test |
| Account updater | Visa and Mastercard, asynchronous; the vaulted token and fingerprint stay the same | Documented. Amex and Discover updater not in docs |
| NTID for recurring | Stored on the token and sent on every MIT, whichever provider is used | Documented. Capturing a new NTID through the proxy is not documented |
| Proxy | Forward proxy to any HTTPS host on your allowlist; mutual TLS; bodies not stored; audit record per call; limits: 20 tokens per request, 1 MB, 30 s (120 s by header), TLS 1.2+ | In beta, enabled per organization. Outbound only; no inbound proxy; no custom code |
| Data beyond cards | Bank details via the enroll API; entity and KYC data via the banking API (returned masked) | Custom tables per column (the schema slide) appear on the vault product page; no public API reference yet |
| Banking connectivity | Entities, onboarding on a named bank connection (`yuno_connection_id`), accounts with routing numbers, ACH, same-day ACH, wire and RTP, with webhooks | Documented API. Which US banks are connected, and one creator on several banks, still to confirm |
| Rules for banks | Today OnlyFans names the bank on each onboarding call. Rule-based allocation across banks and issuers is product direction | Card routing rules are a mature product; bank rules are roadmap |
| Exit | Documented export: written request, recipient's PCI attestation, PGP file over SFTP | The documented file has no NTIDs or network tokens |
| SLA | 99.90% monthly availability, critical incidents answered within 5 minutes (y.uno/sla) | Contract figure and vault-outage design come with the RFP answer |
| Yield and issuers | Jiko (Treasury bills), Coinbase and Triple-A (stablecoins); issuers connected like processors and banks | Named in Justo's skeleton. Confirm they are real connections before sending |

## 2.6 Yuno versus VGS and Basis Theory

The one sentence: **a standalone vault stores the credential; OnlyFans' design also needs the layer that connects it to banks, issuers and processors, and Yuno brings both.**

| Area | Who leads | Why |
|---|---|---|
| Card vault at PCI Level 1 | Level | All three have one |
| Network token depth | VGS and Basis Theory | VGS says it is connected to all four networks; Basis Theory creates the TRID for the merchant |
| Personal data token types | VGS and Basis Theory | Aliases and token types for bank, SSN and tax data |
| Issued-card display and PIN | VGS and Basis Theory | Card display tools; PIN setting documented at Basis Theory (Lithic, Marqeta) |
| Proxy with custom code | VGS and Basis Theory | Inbound and outbound routes, serverless code |
| Rules for where each request goes | Yuno | VGS: "does not make routing decisions for you". Basis Theory: vault "independent of any payment processor or orchestration layer" |
| Provider connections built for you | Yuno | 460+ integrations vs proxy requests the merchant writes |
| Bank accounts and transfers by API | Yuno | Neither vault offers an accounts or transfers API |
| Payouts and split payments | Yuno | Via partners or not offered at the vaults |

Tally: Yuno leads on 4, level on 1, they lead on 4. Being honest about their strengths is part of the pitch, because a vault buyer distrusts any vendor that claims to win everything. Their public prices (Basis Theory $995 a month for 20,000 tokens; VGS from $1,000 a month) stay out of the slides.

## 2.7 The 15-slide deck, slide by slide

| # | Slide | The point you make |
|---|---|---|
| 1 | Cover: "One vault, every bank behind it" | We are here for the vault and the banks behind it |
| 2 | Executive summary | Their need, the challenge, the decision, and what we propose, on one page |
| 3 | Integrated vault vs standalone | Same vault basics; Yuno adds the connections, so far less to build |
| 4 | How it works | Their systems hold tokens only; the vault stores; the proxy delivers to any provider |
| 5 | Vault only or with services | They can buy just the vault (what the RFP asks) and add services later on the same tokens |
| 6 | The vault you design | Tables, columns, protection and retention per column |
| 7 | Access per role | Who sees what, for people and services, with an access log |
| 8 | Network tokens and PAR | One fan across card, wallet and reissue; requestor model confirmed in writing |
| 9 | The proxy request | Exactly what their engineers send and what the provider receives |
| 10 | Portability and exit | Switch processor and keep the cards; leave Yuno with a documented export |
| 11 | Banking connectivity | One creator account; vault plus Yuno connect to banks, issuers, rails, stablecoin ramps; Yuno never holds the money |
| 12 | Rules and resilience | OnlyFans decides by rule; backup banks; failover; balances in one view |
| 13 | Issuers and yield | Swap issuers without re-KYC; yield via Treasury bills or stablecoins |
| 14 | Clients | Social proof |
| 15 | Next steps | Intro call, deep dive, sandbox proof, RFP answer, phase 1; Antoine as lead |

**Talk track in 60 seconds.** "You opened an RFP for a vault. Your design needs more than a vault: one creator account with several banks, issuers and rails behind it, and a rule you control for where each creator lands. Yuno gives you a PCI Level 1 vault for cards, bank, identity and tax data, a proxy to any provider, and banking connectivity to your banks, with OnlyFans setting the rules and the banks holding the money. You can start with the vault alone. Include us in the RFP, and test us in the sandbox."

## 2.8 Questions they will ask, and how to answer

| Question | Answer |
|---|---|
| Whose name are the network tokens registered in? | Our API reference says Yuno holds the requestor ID; registration under OnlyFans per network will be confirmed in writing with the RFP. Do not promise it until Antoine confirms |
| Do you support Amex network tokens? | In our docs, yes; activation is confirmed per network before phase 1 |
| Which US banks are connected today? | Open item. We name them in writing with the RFP response |
| Can one creator have accounts at several banks? | That is exactly what the sandbox proof tests: one creator, two banking connections |
| What happens if the vault goes down? | Provider failover is a routing feature (Monitors). The vault-outage design comes with the RFP answer |
| What is in the export file? | Cardholder name, card number, expiry and the Yuno token. NTIDs and network tokens are not in the documented file; we scope them in writing |
| Does the proxy change our SAQ? | Capture stays in our hosted fields and the proxy resolves data inside Yuno's PCI environment, so per our docs your scope does not change. Your QSA confirms your SAQ |
| Can we show a creator their issued card or set a PIN? | Not documented today. That is a strength of the standalone vaults; say so |
| Can you run our custom code on stored data? | Not today. Basis Theory (Reactors) and VGS (Compute) can |
| Who are your subprocessors? | Provided in writing with the security pack |
| What does it cost? | Commercial offer comes with the RFP response; check the Finance pricing policy before quoting anything |

## 2.9 Open items before sending, and what never to say

**Confirm with Antoine or Justo:**
- The token requestor ID wording (slides 8 and 10).
- Jiko, Coinbase and Triple-A as real connections (slide 13).
- Backup accounts at signup, automatic failover between banks, daily reconciliation (slide 12).
- The schema and access demo (slides 6 and 7), and "bank, identity and tax data in one vault" (slide 3).

**Never say or show:**
- "Banking as a service." Say banking connectivity.
- "+12% authorization uplift" or "20 to 30% decline recovery". The only Yuno-wide figures are up to 7% approval uplift and 30% recovered revenue.
- 99.99% uptime. The published SLA is 99.90%.
- That OnlyFans lacks a payment method, or that a specific processor (Stripe, CCBill) is theirs. None is confirmed.
- Anything about a previous vault evaluation with another customer.

## 2.10 Where everything lives

| What | Where |
|---|---|
| 15-slide deck | Google Slides 1hrBLCFxPXXAyNR73j46JH12ZtMZGPglRnFeaGBxjKk8 |
| 10-slide deck | Google Slides 1gUfjfGbSmherHHMgJcPpBsauoNSSBpzEJipT4govY2g |
| 57-slide technical build | Google Slides 1_W9Xr8MWsNcv-y3I2baUFl1WUMnvVxxyrLCjKu3t5js |
| OnlyFans research brief | data/research/onlyfans-2026-10-08.md |
| Evidence ledger (110 sourced rows) | Deals/OnlyFans/build/ledger_onlyfans.md |
| Yuno vault fact base | Deals/OnlyFans/build/yuno_vault_facts.md |
| Buyer question register | Deals/OnlyFans/build/gap_register.md |
| VGS and Basis Theory comparison | Deals/OnlyFans/build/vs_standalone_vault.md |
| Changes for Samuel | Deals/OnlyFans/build/CHANGES_FOR_SAMUEL.md |
