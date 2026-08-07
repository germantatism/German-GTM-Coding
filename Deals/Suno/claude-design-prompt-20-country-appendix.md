# Prompt Claude Design: 20 Country Deep-Dive Appendix Slides (2026-08-06)

---

You are adding 20 NEW slides to the existing Google Slides deck "Business Case - Suno + Yuno", as an appendix section after the main deck (insert after the Wave 2 Emerging Markets slide, or as a dedicated "APPENDIX: Country Deep-Dives" section with its own divider). Each of the 20 slides follows the EXACT layout of the reference country-deep-dive slide already shown to you (the India-style slide): flag + title header, a full-width dark blue/purple stat bar with 4 cells, a horizontal row of 3 numbered lever cards separated by a line with circled numbers 1/2/3, a two-column bottom section (left: Payment Method Priority table, right: Base-Case Model box), a "SO WHAT" italic takeaway line, and a small grey footnote at the bottom with page number.

## DESIGN RULES (ABSOLUTE)

1. Use the SAME design system as the rest of the "Business Case - Suno + Yuno" deck: same fonts, same blue/purple color palette, same yuno logo top-right, same page-number bottom-left, same card/box styling used elsewhere in the deck.
2. Layout for each slide, top to bottom:
   - Small country flag emoji top-left, above the title.
   - Title in the deck's blue title style (1-2 lines): "{Country}: {headline}"
   - Full-width dark blue/purple stat bar, 4 cells side by side, each with: a large white/bold number, a label below it, a small sub-caption below that.
   - Below the stat bar, 3 side-by-side lever cards separated by a horizontal line with circled numbers (1, 2, 3) centered on the line. Each card: small caps label, then a large bold "+~X" figure with unit, then a blue "~$X/year" line, then a one-line italic tactic.
   - Two-column row: LEFT = "PAYMENT METHOD PRIORITY" table (columns: Priority chip, Method, Scale/penetration, Role for Suno). RIGHT = "BASE-CASE MODEL" box (Current paid conversion, With-method conversion, Incremental uplift bolded, Blended ARPU, one italic sentence at the bottom).
   - Full-width "SO WHAT" bar (light background, bold "SO WHAT" label, italic sentence).
   - Small grey footnote line at the very bottom: Source + "TO VALIDATE" clause.
3. US English. No em-dashes. No " - " as punctuation. Do not invent or alter any number below; use exactly what is given.
4. If any text overflows its box, shrink font size one step before truncating or dropping content.

## SHARED METHODOLOGY NOTE (put this once, on an appendix divider slide before the 20 country slides)

Divider slide title: "Appendix: Country Deep-Dives"
Body text: "Suno's next 20 markets by combined three-lever opportunity, sized from a business case validated against Suno's own public financials ($300M ARR, 2M paid subscribers, $150/year blended ARPU). 14 markets carry verified per-country data from the underlying model; 6 (Italy, Turkey, Poland, Ukraine, Netherlands, Vietnam) are estimated using the same methodology, proportionally reconciled to the confirmed $12M portfolio total. All figures to be replaced with Suno's actual data in the two-week joint data sprint."

---

## SLIDE 1: 🇺🇸 United States

Title: "United States: Renewal reliability and web-native wallets are the largest lever in the portfolio"

Stat bar (4 cells):
1. "93%+" / "card acceptance baseline" / "dominant rail today"
2. "4.9M" / "Suno monthly visits" / "SimilarWeb, Jun 2026"
3. "9,360" / "Incremental paid subscribers" / "from local-method conversion uplift"
4. "14,400" / "Total paid-subscriber impact" / "including auth + renewals · ~$180K/mo total"

Lever 1 AUDIENCE EXPANSION: "+~9,360 incremental paid subscribers" / "~$1.40M/year" / "Lead with PayPal and Venmo on web; close the web-vs-app-store price gap"
Lever 2 AUTHORIZATION UPLIFT: "+~36,300 recovered card approvals/year" / "~$0.45M/year" / "Network tokens, account updater, BIN-level routing"
Lever 3 RENEWAL CONTINUITY: "+~2,020 renewals saved/month" / "~$0.30M/year" / "Smart retries on recurring card failures"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Suno |
| Must-have | Network tokens + account updater | Card-based renewals | Recurring reliability |
| Must-have | PayPal, Venmo (web) | Mainstream US wallets | Primary web alt to cards |
| Optional | Klarna | Niche for $8-24 subscriptions | Coverage |

Base-case model: Current paid conversion ~1.8% | With optimization ~3.5% | Incremental uplift +1.7pp | Blended ARPU ~$150/year
Base-case italic line: "Local methods and renewal reliability move conversion closer to better-monetized subscription benchmarks."

SO WHAT: "The US is Suno's largest market and its biggest single lever, driven less by missing methods and more by renewal reliability and closing the web-vs-app-store price gap."

Footnote: "Source: SimilarWeb (Jun 2026); Suno help center; Yuno business case model. TO VALIDATE: Suno US checkout starts, current paid conversion, decline codes, web-vs-IAP billing split."

---

## SLIDE 2: 🇩🇪 Germany

Title: "Germany: PayPal and SEPA Direct Debit turn card-only checkout into a recurring-native one"

Stat bar: "PayPal" / "dominant German digital wallet" / "recurring-capable" · "1.2M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "3,432" / "Incremental paid subscribers" / "from local-method conversion uplift" · "5,280" / "Total paid-subscriber impact" / "including auth + renewals · ~$66K/mo total"

Lever 1: "+~3,432 incremental paid subscribers" / "~$0.51M/year" / "Add PayPal and SEPA Direct Debit as primary recurring rails"
Lever 2: "+~13,300 recovered card approvals/year" / "~$0.17M/year" / "Local card routing, cross-border decline recovery"
Lever 3: "+~740 renewals saved/month" / "~$0.11M/year" / "SCA-aware retry timing, provider fallback"

Table: Must-have PayPal (Leading German digital wallet / Primary recurring rail) | Must-have SEPA Direct Debit (EU bank-mandate standard / Recurring rail) | Optional Klarna (Invoice/BNPL culture / Coverage)

Base-case: ~2.5% | ~4.5% | +2.0pp | ~$150/year. Italic: "Germany's opportunity is preferred local rails plus recovery logic, not card acceptance, which is already strong."

SO WHAT: "Germany's opportunity is preferred local methods plus recovery logic, not card acceptance, which is already strong."

Footnote: "Source: Stripe payment-methods conversion study; Trade.gov; Yuno business case model. TO VALIDATE: Suno Germany checkout starts, current paid conversion, decline codes."

---

## SLIDE 3: 🇧🇷 Brazil

Title: "Brazil: Suno already has Pix; Pix Automatico for renewals is the missing half"

Stat bar: "170M+" / "Pix users" / "~40% of Brazilian e-commerce" · "1.4M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "2,860" / "Incremental paid subscribers" / "from local-method conversion uplift" · "4,400" / "Total paid-subscriber impact" / "including auth + renewals · ~$55K/mo total"

Lever 1: "+~2,860 incremental paid subscribers" / "~$0.43M/year" / "Enable Pix Automatico as the subscription-grade recurring rail (Pix itself already live)"
Lever 2: "+~11,090 recovered card approvals/year" / "~$0.14M/year" / "Local card acquiring, installments"
Lever 3: "+~620 renewals saved/month" / "~$0.09M/year" / "Retries across local processors"

Table: Must-have Pix Automatico (170M+ users; ~40% of e-commerce / Recurring mandate, Pix one-time already live) | Must-have Local card acquiring + installments (Standard Brazilian card behavior / Primary card rail) | Optional Google Pay (Coverage / Fallback)

Base-case: ~1.8% | ~4.5% | +2.7pp | ~$150/year. Italic: same conversion-benchmark line as others.

SO WHAT: "Brazil is Suno's #3 traffic market and already has Pix live; the real gap is the recurring version of Pix, not Pix itself."

Footnote: "Source: BCG/PPRO; SimilarWeb; live-checkout confirmation of Pix (Aug 2026). TO VALIDATE: Suno Brazil checkout starts, current paid conversion, decline codes."

---

## SLIDE 4: 🇯🇵 Japan

Title: "Japan: high card penetration does not remove the need for local trust rails"

Stat bar: "70M+" / "PayPay registered users" / "cashless ratio 42.8% (2024)" · "0.80M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "2,756" / "Incremental paid subscribers" / "from local-method conversion uplift" · "4,240" / "Total paid-subscriber impact" / "including auth + renewals · ~$53K/mo total"

Lever 1: "+~2,756 incremental paid subscribers" / "~$0.41M/year" / "Add PayPay for acquisition, Rakuten Pay for recurring"
Lever 2: "+~10,690 recovered card approvals/year" / "~$0.13M/year" / "Local card routing"
Lever 3: "+~590 renewals saved/month" / "~$0.09M/year" / "Retry timing on renewals"

Table: Must-have PayPay (70M+ registered users / Primary acquisition rail) | Must-have Rakuten Pay (Recurring-capable wallet / Recurring rail) | Optional Konbini (Convenience-store acquisition / Rescue/coverage, not recurring)

Base-case: ~2.8% | ~5% | +2.2pp | ~$150/year.

SO WHAT: "Japan is a method-trust market: local payment familiarity lifts conversion even where cards already work."

Footnote: "Source: PayPay; METI; SimilarWeb. TO VALIDATE: Suno Japan checkout starts, current paid conversion, decline codes."

---

## SLIDE 5: 🇮🇳 India

Title: "India: UPI is live; UPI Autopay for renewals is the largest remaining audience-expansion lever"

Stat bar: "504M+" / "UPI users" / "84% of digital retail payments" · "0.9M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "2,704" / "Incremental paid subscribers" / "from local-method conversion uplift" · "4,160" / "Total paid-subscriber impact" / "including auth + renewals · ~$52K/mo total"

Lever 1: "+~2,704 incremental paid subscribers" / "~$0.41M/year" / "UPI Autopay mandates for renewals (UPI one-time already live)"
Lever 2: "+~10,480 recovered card approvals/year" / "~$0.13M/year" / "RuPay and local debit routing"
Lever 3: "+~580 renewals saved/month" / "~$0.09M/year" / "Smart retries on AutoPay mandate failures"

Table: Must-have UPI Autopay (504M+ users; 84% of digital retail / Recurring mandate, UPI one-time already live) | Must-have RuPay / local debit (Major local scheme / Local card acceptance) | Optional Net banking, wallets (Supplementary / Coverage/fallback)

Base-case: ~1.2% | ~4% | +2.8pp | ~$150/year.

SO WHAT: "India's monetization path runs through UPI Autopay specifically; the acquisition rail is already there, the renewal rail is not."

Footnote: "Source: NPCI; SimilarWeb; Suno help center (UPI confirmed live). TO VALIDATE: Suno India checkout starts, current paid conversion, decline codes."

---

## SLIDE 6: 🇮🇩 Indonesia

Title: "Indonesia: card share under 15% makes wallets the primary path to scale"

Stat bar: "60M+" / "QRIS users" / "39M merchants" · "0.95M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "2,548" / "Incremental paid subscribers" / "from local-method conversion uplift" · "3,920" / "Total paid-subscriber impact" / "including auth + renewals · ~$49K/mo total"

Lever 1: "+~2,548 incremental paid subscribers" / "~$0.38M/year" / "Add GoPay and DANA as primary wallets"
Lever 2: "+~9,880 recovered card approvals/year" / "~$0.12M/year" / "Local card routing"
Lever 3: "+~550 renewals saved/month" / "~$0.08M/year" / "Provider redundancy across local PSPs"

Table: Must-have GoPay (Major wallet / Primary acquisition) | Must-have DANA (Major wallet / Mobile-first acquisition) | Optional QRIS / bank transfer (Mass-adopted trust layer / Coverage)

Base-case: ~0.8% | ~3.5% | +2.7pp | ~$150/year.

SO WHAT: "Indonesia is a mobile-wallet market where card-only checkout structurally under-monetizes existing demand."

Footnote: "Source: Bank Indonesia; ASEAN Briefing; SimilarWeb. TO VALIDATE: Suno Indonesia checkout starts, current paid conversion, decline codes."

---

## SLIDE 7: 🇬🇧 United Kingdom

Title: "United Kingdom: Open Banking and retry logic compound on an already-strong card base"

Stat bar: "Strong" / "card + Open Banking adoption" / "leading UK rails" · "0.85M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "2,132" / "Incremental paid subscribers" / "from local-method conversion uplift" · "3,280" / "Total paid-subscriber impact" / "including auth + renewals · ~$41K/mo total"

Lever 1: "+~2,132 incremental paid subscribers" / "~$0.32M/year" / "Add Open Banking as a recurring-capable rail"
Lever 2: "+~8,260 recovered card approvals/year" / "~$0.10M/year" / "Token and retry optimization"
Lever 3: "+~460 renewals saved/month" / "~$0.07M/year" / "Account updater on card renewals"

Table: Must-have Open Banking (Growing bank-rail adoption / Recurring-capable alt rail) | Must-have Card token/retry optimization (Core rail / Reliability) | Optional PayPal (Mainstream / Coverage)

Base-case: ~3.0% | ~5% | +2.0pp | ~$150/year.

SO WHAT: "The UK's opportunity is optimization on top of an already-strong base, not new-method acquisition."

Footnote: "Source: UK Finance; SimilarWeb. TO VALIDATE: Suno UK checkout starts, current paid conversion, decline codes."

---

## SLIDE 8: 🇫🇷 France

Title: "France: Cartes Bancaires domestic routing plus PayPal close the gap"

Stat bar: "CB" / "Cartes Bancaires" / "dominant domestic card scheme" · "0.75M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,976" / "Incremental paid subscribers" / "from local-method conversion uplift" · "3,040" / "Total paid-subscriber impact" / "including auth + renewals · ~$38K/mo total"

Lever 1: "+~1,976 incremental paid subscribers" / "~$0.30M/year" / "Cartes Bancaires domestic routing plus PayPal"
Lever 2: "+~7,660 recovered card approvals/year" / "~$0.10M/year" / "Domestic scheme routing"
Lever 3: "+~425 renewals saved/month" / "~$0.06M/year" / "SEPA Direct Debit for renewals"

Table: Must-have Cartes Bancaires domestic routing (Dominant French scheme / Local card acceptance) | Must-have PayPal (Mainstream / Primary alt rail) | Optional SEPA Direct Debit (EU standard / Renewal rail)

Base-case: ~2.5% | ~4.2% | +1.7pp | ~$150/year.

SO WHAT: "France's lever is domestic settlement on cards, not new APM acquisition."

Footnote: "Source: Banque de France; Stripe; SimilarWeb. TO VALIDATE: Suno France checkout starts, current paid conversion, decline codes."

---

## SLIDE 9: 🇪🇸 Spain

Title: "Spain: Bizum is the local APM to test alongside retries"

Stat bar: "28.8M+" / "Bizum users (Apr 2025)" / "+82% online YoY" · "0.6M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,924" / "Incremental paid subscribers" / "from local-method conversion uplift" · "2,960" / "Total paid-subscriber impact" / "including auth + renewals · ~$37K/mo total"

Lever 1: "+~1,924 incremental paid subscribers" / "~$0.29M/year" / "Add Bizum on mobile checkout"
Lever 2: "+~7,460 recovered card approvals/year" / "~$0.09M/year" / "Local card acceptance"
Lever 3: "+~415 renewals saved/month" / "~$0.06M/year" / "SCA handling, provider redundancy"

Table: Must-have Bizum (28.8M+ users, Apr 2025 / Primary acquisition rail) | Must-have PayPal, cards (Mainstream / Local card acceptance) | Optional SEPA Direct Debit (EU recurring / Coverage)

Base-case: ~2.8% | ~4.8% | +2.0pp | ~$150/year.

SO WHAT: "Spain is a medium-effort European quick win, not a large local-processing gap."

Footnote: "Source: Stripe; Bank of Spain; SimilarWeb. TO VALIDATE: Suno Spain checkout starts, current paid conversion, decline codes."

---

## SLIDE 10: 🇮🇹 Italy

Title: "Italy: PayPal and SEPA Direct Debit make card-only checkout suboptimal"

Stat bar: "PayPal" / "leading Italian digital wallet" / "primary alt rail" · "0.6M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,456" / "Incremental paid subscribers" / "from local-method conversion uplift" · "2,240" / "Total paid-subscriber impact" / "including auth + renewals · ~$28K/mo total"

Lever 1: "+~1,456 incremental paid subscribers" / "~$0.22M/year" / "Add PayPal and SEPA Direct Debit"
Lever 2: "+~5,650 recovered card approvals/year" / "~$0.07M/year" / "Local card routing"
Lever 3: "+~310 renewals saved/month" / "~$0.05M/year" / "SEPA-driven renewal reliability"

Table: Must-have PayPal (Leading Italian wallet / Primary recurring rail) | Must-have SEPA Direct Debit (EU standard / Recurring rail) | Optional PostePay (Local prepaid card culture / Coverage)

Base-case: ~2.3% | ~4.0% | +1.7pp | ~$150/year.

SO WHAT: "Italy mirrors Germany's playbook at smaller scale: preferred local rails plus recurring reliability."

Footnote: "Source: Banca d'Italia; Stripe; SimilarWeb. TO VALIDATE: Suno Italy checkout starts, current paid conversion, decline codes."

---

## SLIDE 11: 🇲🇽 Mexico

Title: "Mexico: cross-border card decline and local debit gap suppress conversion together"

Stat bar: "Local" / "debit + SPEI + Mercado Pago" / "leading e-commerce methods" · "0.40M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,300" / "Incremental paid subscribers" / "from local-method conversion uplift" · "2,000" / "Total paid-subscriber impact" / "including auth + renewals · ~$25K/mo total"

Lever 1: "+~1,300 incremental paid subscribers" / "~$0.20M/year" / "Mercado Pago Suscripciones plus local debit acquiring"
Lever 2: "+~5,040 recovered card approvals/year" / "~$0.06M/year" / "Local acquiring, reduce issuer declines"
Lever 3: "+~280 renewals saved/month" / "~$0.04M/year" / "Retries across local processors"

Table: Must-have Local debit / domestic cards (Leading e-commerce method / Primary acquisition + recurring rail) | Must-have Mercado Pago Suscripciones (Recurring-capable wallet / Recurring rail) | Optional SPEI, Apple/Google Pay (Bank-transfer/wallet trust layer / Coverage)

Base-case: ~1.5% | ~4.0% | +2.5pp | ~$150/year.

SO WHAT: "Mexico combines local payment-method coverage with meaningful card-approval upside."

Footnote: "Source: PPRO; PCMI; SimilarWeb. TO VALIDATE: Suno Mexico checkout starts, current paid conversion, decline codes."

---

## SLIDE 12: 🇰🇷 Republic of Korea

Title: "Republic of Korea: recurring tokens on already-live wallets are the unlock"

Stat bar: "Live" / "KakaoPay and NaverPay" / "already live at Suno checkout" · "0.6M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,196" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,840" / "Total paid-subscriber impact" / "including auth + renewals · ~$23K/mo total"

Lever 1: "+~1,196 incremental paid subscribers" / "~$0.18M/year" / "Add Toss and Samsung Pay; enable recurring tokens on live KakaoPay/NaverPay"
Lever 2: "+~4,640 recovered card approvals/year" / "~$0.06M/year" / "Local card uplift"
Lever 3: "+~260 renewals saved/month" / "~$0.04M/year" / "Subscription retry and token management"

Table: Must-have Toss (Major easy-pay platform / Net-new acquisition rail) | Must-have Samsung Pay (Mainstream mobile wallet / Net-new acquisition rail) | Optional Recurring tokens on KakaoPay/NaverPay (Already live at Suno / Depth on existing rails)

Base-case: ~2.0% | ~4.0% | +2.0pp | ~$150/year.

SO WHAT: "Korea is not a card-access problem or even a first-method problem, since two wallets are already live; it is a depth and recurring-token problem."

Footnote: "Source: KISDI; Antom; SimilarWeb; Suno help center (KakaoPay/NaverPay confirmed live). TO VALIDATE: Suno Korea checkout starts, current paid conversion, decline codes."

---

## SLIDE 13: 🇨🇦 Canada

Title: "Canada: retry and token optimization on an already-strong card base"

Stat bar: "Cards" / "+ PayPal" / "dominant rails" · "0.55M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,092" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,680" / "Total paid-subscriber impact" / "including auth + renewals · ~$21K/mo total"

Lever 1: "+~1,092 incremental paid subscribers" / "~$0.16M/year" / "PayPal depth, Interac coverage"
Lever 2: "+~4,230 recovered card approvals/year" / "~$0.05M/year" / "Retry optimization"
Lever 3: "+~235 renewals saved/month" / "~$0.04M/year" / "Account updater on renewals"

Table: Must-have Cards + PayPal (Dominant rails / Core reliability) | Optional Interac (Local bank-debit rail / Coverage)

Base-case: ~2.8% | ~4.5% | +1.7pp | ~$150/year.

SO WHAT: "Canada is a low-effort optimization market riding on the US playbook."

Footnote: "Source: SimilarWeb; Yuno business case model. TO VALIDATE: Suno Canada checkout starts, current paid conversion, decline codes."

---

## SLIDE 14: 🇹🇷 Turkey

Title: "Turkey: domestic scheme and FX-aware processing matter more than global cards"

Stat bar: "67M+" / "TROY cards" / "20% of card transactions" · "0.45M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,092" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,680" / "Total paid-subscriber impact" / "including auth + renewals · ~$21K/mo total"

Lever 1: "+~1,092 incremental paid subscribers" / "~$0.16M/year" / "TROY domestic scheme, installments"
Lever 2: "+~4,230 recovered card approvals/year" / "~$0.05M/year" / "FX-aware local acquiring"
Lever 3: "+~235 renewals saved/month" / "~$0.04M/year" / "Provider redundancy and retry logic"

Table: Must-have TROY (domestic scheme) (67M cards; 20% of card txns / Primary acquisition + recurring rail) | Must-have Local installments (Mainstream Turkish behavior / Conversion driver) | Optional Papara, BKM/FAST (Local wallet layer / Coverage)

Base-case: ~1.8% | ~4.2% | +2.4pp | ~$150/year.

SO WHAT: "Turkey is a localization market where domestic card behavior, FX-friendly processing and retries combine."

Footnote: "Source: BKM; Daily Sabah; SimilarWeb. TO VALIDATE: Suno Turkey checkout starts, current paid conversion, decline codes."

---

## SLIDE 15: 🇹🇭 Thailand

Title: "Thailand: PromptPay-adjacent wallets are the dominant local behavior to support"

Stat bar: "PromptPay" / "dominant Thai payment behavior" / "bank-linked" · "0.35M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "1,092" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,680" / "Total paid-subscriber impact" / "including auth + renewals · ~$21K/mo total"

Lever 1: "+~1,092 incremental paid subscribers" / "~$0.16M/year" / "Add TrueMoney and Rabbit LINE Pay (recurring-capable wallets)"
Lever 2: "+~4,230 recovered card approvals/year" / "~$0.05M/year" / "Local card routing"
Lever 3: "+~235 renewals saved/month" / "~$0.04M/year" / "Provider redundancy"

Table: Must-have TrueMoney (Major Thai wallet / Recurring-capable acquisition) | Must-have Rabbit LINE Pay (Major Thai wallet / Recurring-capable acquisition) | Optional Local cards (Coverage / Fallback)

Base-case: ~1.5% | ~3.8% | +2.3pp | ~$150/year.

SO WHAT: "Thailand needs wallet depth more than card optimization; PromptPay itself is a bank-transfer rail, not a subscription-grade mandate, so wallets carry the recurring load."

Footnote: "Source: Bank of Thailand; Stripe; SimilarWeb. TO VALIDATE: Suno Thailand checkout starts, current paid conversion, decline codes."

---

## SLIDE 16: 🇵🇱 Poland

Title: "Poland: card retries carry more weight than BLIK for a subscription business"

Stat bar: "BLIK" / "dominant Polish payment method" / "acquisition-only, not recurring" · "0.33M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "780" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,200" / "Total paid-subscriber impact" / "including auth + renewals · ~$15K/mo total"

Lever 1: "+~780 incremental paid subscribers" / "~$0.12M/year" / "BLIK for first payment/acquisition (non-recurring, note caveat)"
Lever 2: "+~3,020 recovered card approvals/year" / "~$0.04M/year" / "Local card acquiring"
Lever 3: "+~170 renewals saved/month" / "~$0.03M/year" / "Card retries carry all renewals since BLIK does not support subscriptions"

Table: Must-have Card retries for renewals (Core recurring rail / Renewal reliability) | Optional BLIK (Dominant Polish method / Acquisition-only, not recurring)

Base-case: ~1.8% | ~3.5% | +1.7pp | ~$150/year.

SO WHAT: "Poland is a smaller market where the subscription model itself constrains the APM opportunity; renewal reliability on cards does most of the work."

Footnote: "Source: NBP; PPRO; SimilarWeb. TO VALIDATE: Suno Poland checkout starts, current paid conversion, decline codes."

---

## SLIDE 17: 🇺🇦 Ukraine

Title: "Ukraine: local card routing and wallet tokens compound on an already-billable market"

Stat bar: "UAH" / "already a live Suno billing currency" / "confirmed" · "0.28M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "676" / "Incremental paid subscribers" / "from local-method conversion uplift" · "1,040" / "Total paid-subscriber impact" / "including auth + renewals · ~$13K/mo total"

Lever 1: "+~676 incremental paid subscribers" / "~$0.10M/year" / "Local card routing depth"
Lever 2: "+~2,620 recovered card approvals/year" / "~$0.03M/year" / "Apple/Google Pay tokens"
Lever 3: "+~150 renewals saved/month" / "~$0.02M/year" / "Retry logic on card renewals"

Table: Must-have Local card routing (Core rail / Approval uplift) | Optional Apple Pay, Google Pay (Mainstream tokens / Coverage) | Optional Privat24, LiqPay (Local bank rails / Future depth)

Base-case: ~1.5% | ~3.2% | +1.7pp | ~$150/year.

SO WHAT: "Ukraine is already billable in UAH; the opportunity is pure processing depth, not new-currency enablement."

Footnote: "Source: NBU; SimilarWeb; Suno help center (UAH confirmed live currency). TO VALIDATE: Suno Ukraine checkout starts, current paid conversion, decline codes."

---

## SLIDE 18: 🇦🇷 Argentina

Title: "Argentina: Mercado Pago Suscripciones plus local processing unlock a high-friction market"

Stat bar: "Mercado Pago" / "dominant Argentine digital wallet" / "recurring-capable" · "0.20M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "572" / "Incremental paid subscribers" / "from local-method conversion uplift" · "880" / "Total paid-subscriber impact" / "including auth + renewals · ~$11K/mo total"

Lever 1: "+~572 incremental paid subscribers" / "~$0.09M/year" / "Mercado Pago Suscripciones (recurring)"
Lever 2: "+~2,220 recovered card approvals/year" / "~$0.03M/year" / "Local card acquiring"
Lever 3: "+~120 renewals saved/month" / "~$0.02M/year" / "Installments and retries"

Table: Must-have Mercado Pago Suscripciones (Dominant Argentine wallet, recurring-capable / Primary recurring rail) | Must-have Local card acquiring (Standard behavior / Approval uplift) | Optional Google Pay (Coverage / Fallback)

Base-case: ~1.2% | ~3.5% | +2.3pp | ~$150/year.

SO WHAT: "Argentina combines high inflation-driven card friction with a dominant wallet that already supports recurring billing."

Footnote: "Source: PCMI; Adyen; dLocal; SimilarWeb. TO VALIDATE: Suno Argentina checkout starts, current paid conversion, decline codes."

---

## SLIDE 19: 🇳🇱 Netherlands

Title: "Netherlands: iDEAL for first payment, SEPA Direct Debit for renewals"

Stat bar: "iDEAL" / "dominant Dutch online payment method" / "confirmed leader" · "0.22M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "520" / "Incremental paid subscribers" / "from local-method conversion uplift" · "800" / "Total paid-subscriber impact" / "including auth + renewals · ~$10K/mo total"

Lever 1: "+~520 incremental paid subscribers" / "~$0.08M/year" / "iDEAL for first payment, converting into SEPA Direct Debit mandate"
Lever 2: "+~2,020 recovered card approvals/year" / "~$0.03M/year" / "Local card uplift"
Lever 3: "+~110 renewals saved/month" / "~$0.02M/year" / "SEPA-driven renewal reliability"

Table: Must-have iDEAL (Dominant Dutch method / Primary acquisition rail) | Must-have SEPA Direct Debit (EU standard / Renewal rail after iDEAL mandate) | Optional Apple/Google Pay (Coverage / Fallback)

Base-case: ~2.5% | ~4.3% | +1.8pp | ~$150/year.

SO WHAT: "The Netherlands is a small, high-conversion market once the iDEAL-to-SEPA-DD handoff is built correctly."

Footnote: "Source: Dutch Payments Association; Stripe; SimilarWeb. TO VALIDATE: Suno Netherlands checkout starts, current paid conversion, decline codes."

---

## SLIDE 20: 🇻🇳 Vietnam

Title: "Vietnam: enabling VND billing unlocks MoMo and VietQR"

Stat bar: "30M+" / "MoMo users" / "QR payments grew 471% YoY" · "0.21M" / "Suno monthly visits" / "SimilarWeb, Jun 2026" · "260" / "Incremental paid subscribers" / "from local-method conversion uplift" · "400" / "Total paid-subscriber impact" / "including auth + renewals · ~$5K/mo total"

Lever 1: "+~260 incremental paid subscribers" / "~$0.04M/year" / "Enable VND billing first, then MoMo"
Lever 2: "+~1,010 recovered card approvals/year" / "~$0.01M/year" / "Local card routing"
Lever 3: "+~56 renewals saved/month" / "~$0.01M/year" / "Retry logic once VND billing is live"

Table: Prerequisite Enable VND billing (Not yet a Suno billing currency / Unlocks everything below) | Must-have MoMo (30M+ users / Primary acquisition rail once VND is live) | Optional VietQR, local cards (Coverage / Fallback)

Base-case: ~0.8% (USD-only friction today) | ~2.8% | +2.0pp | ~$150/year.

SO WHAT: "Vietnam is the one market on this list where the first step is not a payment method at all, it is currency enablement; everything else follows from that."

Footnote: "Source: GAJRC; market reports; SimilarWeb; Suno help center (VND not in the 17 live currencies). TO VALIDATE: Suno Vietnam checkout starts, current paid conversion, decline codes."

---

## WHAT NOT TO DO
- Do not modify any other slide in the deck outside this new appendix section.
- Do not invent or round any number differently than given above.
- Do not add country flags as full graphics if the deck's design system does not already use them elsewhere; emoji flags are acceptable per the reference slide shown.
- Keep all 20 slides visually identical to each other in layout, differing only in content.
