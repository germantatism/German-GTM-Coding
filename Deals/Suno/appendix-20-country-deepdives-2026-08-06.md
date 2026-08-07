# Appendix: 20 Country Deep-Dive Slides for Suno (2026-08-06)

Template matches the Anthropic reference slide (India example) exactly, adapted to Suno with real verified data from tonight's research + the reconciled $12M business case.

## Methodology (state this in the deck's methodology/appendix note)

- Dollar base: the reconciled $12M portfolio total (Slide 8, Decision Frame Slide 12).
- Each country's total is split 65% Audience Expansion / 21% Authorization Uplift / 14% Renewal Continuity, derived from the real observed ratio between APMs Benefit and Cards Benefit in the Excel (proportional allocation, disclosed, not independently modeled per lever per country).
- Blended ARPU: $150/year ($12.50/month), Suno's real derived figure ($300M ARR / 2M subscribers).
- ATV for transaction-count conversions: $12.50.
- Current/with-method conversion rates: estimated by archetype (Full-stack starts lower, Mature starts higher), anchored to Suno's real ~2% registered-to-paid conversion. Labeled as Yuno estimates, TO VALIDATE with Suno's actual data.

---

## MASTER SUMMARY TABLE (all 20, headline numbers)

| # | Country | Suno visits/mo | Total $/mo | Incremental paid subs | Total paid-sub impact | Archetype |
|---|---|---|---|---|---|---|
| 1 | United States | 4.9M | $180K | 9,360 | 14,400 | Full-stack |
| 2 | Germany | 1.2M | $66K | 3,432 | 5,280 | Mature |
| 3 | Brazil | 1.4M | $55K | 2,860 | 4,400 | Full-stack |
| 4 | Japan | 0.80M | $53K | 2,756 | 4,240 | Mature |
| 5 | India | 0.9M | $52K | 2,704 | 4,160 | APM-led |
| 6 | Indonesia | 0.95M | $49K | 2,548 | 3,920 | Full-stack |
| 7 | United Kingdom | 0.85M | $41K | 2,132 | 3,280 | Full-stack |
| 8 | France | 0.75M | $38K | 1,976 | 3,040 | Full-stack |
| 9 | Spain | 0.6M | $37K | 1,924 | 2,960 | APM-led |
| 10 | Italy | 0.6M | $28K | 1,456 | 2,240 | APM-led |
| 11 | Mexico | 0.40M | $25K | 1,300 | 2,000 | Full-stack |
| 12 | Republic of Korea | 0.6M | $23K | 1,196 | 1,840 | Full-stack |
| 13 | Canada | 0.55M | $21K | 1,092 | 1,680 | Mature |
| 14 | Turkey | 0.45M | $21K | 1,092 | 1,680 | Mature |
| 15 | Thailand | 0.35M | $21K | 1,092 | 1,680 | APM-led |
| 16 | Poland | 0.33M | $15K | 780 | 1,200 | Full-stack |
| 17 | Ukraine | 0.28M | $13K | 676 | 1,040 | Full-stack |
| 18 | Argentina | 0.20M | $11K | 572 | 880 | Full-stack |
| 19 | Netherlands | 0.22M | $10K | 520 | 800 | Full-stack |
| 20 | Vietnam | 0.21M | $5K | 260 | 400 | APM-led |

Sum of "Total $/mo" = $764K/mo = $9.17M/yr pay-in levers, matches Slide 8 and the Decision Frame.

---

## PER-COUNTRY DEEP-DIVE SLIDES

### 1. 🇺🇸 United States: Renewal reliability and web-native wallets are the largest lever in the portfolio

**Top stat bar:**
- 93%+ card acceptance baseline / dominant rail today
- ~4.9M Suno monthly visits (SimilarWeb, Jun 2026)
- 9,360 incremental paid subscribers from local-method conversion uplift
- 14,400 total paid-subscriber impact including auth + renewals · ~$180K/mo total

**1. AUDIENCE EXPANSION:** +~9,360 incremental paid subscribers · ~$1.40M/year · Lead with PayPal and Venmo on web; close the web-vs-app-store price gap
**2. AUTHORIZATION UPLIFT:** +~36,300 recovered card approvals/year · ~$0.45M/year · Network tokens, account updater, BIN-level routing
**3. RENEWAL CONTINUITY:** +~2,020 renewals saved/month · ~$0.30M/year · Smart retries on recurring card failures

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Network tokens + account updater | Card-based renewals | Recurring reliability |
| Must-have | PayPal, Venmo (web) | Mainstream US wallets | Primary web alt to cards |
| Optional | Klarna | Niche for $8-24 subscriptions | Coverage |

**Base-case model:** Current paid conversion ~1.8% · With optimization ~3.5% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** The US is Suno's largest market and its biggest single lever, driven less by missing methods and more by renewal reliability and closing the web-vs-app-store price gap.

**Source:** SimilarWeb (Jun 2026); Suno help center; Yuno business case model. TO VALIDATE: Suno US checkout starts, current paid conversion, decline codes, web-vs-IAP billing split.

---

### 2. 🇩🇪 Germany: PayPal and SEPA Direct Debit turn card-only checkout into a recurring-native one

**Top stat bar:**
- PayPal: dominant German digital wallet, recurring-capable
- ~1.2M Suno monthly visits (SimilarWeb, Jun 2026)
- 3,432 incremental paid subscribers from local-method conversion uplift
- 5,280 total paid-subscriber impact including auth + renewals · ~$66K/mo total

**1. AUDIENCE EXPANSION:** +~3,432 incremental paid subscribers · ~$0.51M/year · Add PayPal and SEPA Direct Debit as primary recurring rails
**2. AUTHORIZATION UPLIFT:** +~13,300 recovered card approvals/year · ~$0.17M/year · Local card routing, cross-border decline recovery
**3. RENEWAL CONTINUITY:** +~740 renewals saved/month · ~$0.11M/year · SCA-aware retry timing, provider fallback

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | PayPal | Leading German digital wallet | Primary recurring rail |
| Must-have | SEPA Direct Debit | EU bank-mandate standard | Recurring rail |
| Optional | Klarna | Invoice/BNPL culture | Coverage |

**Base-case model:** Current paid conversion ~2.5% · With PayPal + SEPA DD ~4.5% · Incremental uplift +2.0pp · Blended ARPU ~$150/year

**So what:** Germany's opportunity is preferred local rails plus SCA-aware recovery logic, not card acceptance, which is already strong.

**Source:** Stripe payment-methods conversion study; Trade.gov; Yuno business case model. TO VALIDATE: Suno Germany checkout starts, current paid conversion, decline codes.

---

### 3. 🇧🇷 Brazil: Suno already has Pix; Pix Automatico for renewals is the missing half

**Top stat bar:**
- 170M+ Pix users / ~40% of Brazilian e-commerce
- ~1.4M Suno monthly visits (SimilarWeb, Jun 2026)
- 2,860 incremental paid subscribers from local-method conversion uplift
- 4,400 total paid-subscriber impact including auth + renewals · ~$55K/mo total

**1. AUDIENCE EXPANSION:** +~2,860 incremental paid subscribers · ~$0.43M/year · Enable Pix Automatico as the subscription-grade recurring rail (Pix itself already live)
**2. AUTHORIZATION UPLIFT:** +~11,090 recovered card approvals/year · ~$0.14M/year · Local card acquiring, installments
**3. RENEWAL CONTINUITY:** +~620 renewals saved/month · ~$0.09M/year · Retries across local processors

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Pix Automatico | 170M+ users; ~40% of e-commerce | Recurring mandate (Pix one-time already live) |
| Must-have | Local card acquiring + installments | Standard Brazilian card behavior | Primary card rail |
| Optional | Google Pay | Coverage | Fallback |

**Base-case model:** Current paid conversion ~1.8% · With Pix Automatico ~4.5% · Incremental uplift +2.7pp · Blended ARPU ~$150/year

**So what:** Brazil is Suno's #3 traffic market and already has Pix live; the real gap is the recurring version of Pix, not Pix itself.

**Source:** BCG/PPRO; SimilarWeb; German (Aug 2026, live-checkout confirmation of Pix). TO VALIDATE: Suno Brazil checkout starts, current paid conversion, decline codes.

---

### 4. 🇯🇵 Japan: high card penetration does not remove the need for local trust rails

**Top stat bar:**
- 70M+ PayPay registered users / cashless ratio 42.8% (2024)
- ~0.80M Suno monthly visits (SimilarWeb, Jun 2026)
- 2,756 incremental paid subscribers from local-method conversion uplift
- 4,240 total paid-subscriber impact including auth + renewals · ~$53K/mo total

**1. AUDIENCE EXPANSION:** +~2,756 incremental paid subscribers · ~$0.41M/year · Add PayPay for acquisition, Rakuten Pay for recurring
**2. AUTHORIZATION UPLIFT:** +~10,690 recovered card approvals/year · ~$0.13M/year · Local card routing
**3. RENEWAL CONTINUITY:** +~590 renewals saved/month · ~$0.09M/year · Retry timing on renewals

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | PayPay | 70M+ registered users | Primary acquisition rail |
| Must-have | Rakuten Pay | Recurring-capable wallet | Recurring rail |
| Optional | Konbini | Convenience-store acquisition | Rescue/coverage, not recurring |

**Base-case model:** Current paid conversion ~2.8% · With PayPay + Rakuten Pay ~5% · Incremental uplift +2.2pp · Blended ARPU ~$150/year

**So what:** Japan is a method-trust market; local payment familiarity lifts conversion even where cards already work.

**Source:** PayPay; METI; SimilarWeb. TO VALIDATE: Suno Japan checkout starts, current paid conversion, decline codes.

---

### 5. 🇮🇳 India: UPI is live; UPI Autopay for renewals is the largest remaining audience-expansion lever

**Top stat bar:**
- 504M+ UPI users / 84% of digital retail payments
- ~0.9M Suno monthly visits (SimilarWeb, Jun 2026)
- 2,704 incremental paid subscribers from local-method conversion uplift
- 4,160 total paid-subscriber impact including auth + renewals · ~$52K/mo total

**1. AUDIENCE EXPANSION:** +~2,704 incremental paid subscribers · ~$0.41M/year · UPI Autopay mandates for renewals (UPI one-time already live)
**2. AUTHORIZATION UPLIFT:** +~10,480 recovered card approvals/year · ~$0.13M/year · RuPay and local debit routing
**3. RENEWAL CONTINUITY:** +~580 renewals saved/month · ~$0.09M/year · Smart retries on AutoPay mandate failures

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | UPI Autopay | 504M+ users; 84% of digital retail | Recurring mandate (UPI one-time already live) |
| Must-have | RuPay / local debit | Major local scheme | Local card acceptance |
| Optional | Net banking, wallets | Supplementary | Coverage/fallback |

**Base-case model:** Current paid conversion ~1.2% · With UPI Autopay ~4% · Incremental uplift +2.8pp · Blended ARPU ~$150/year

**So what:** India's monetization path runs through UPI Autopay specifically; the acquisition rail is already there, the renewal rail is not.

**Source:** NPCI; SimilarWeb; Suno help center (UPI confirmed live). TO VALIDATE: Suno India checkout starts, current paid conversion, decline codes.

---

### 6. 🇮🇩 Indonesia: card share under 15% makes wallets the primary path to scale

**Top stat bar:**
- 60M+ QRIS users / 39M merchants
- ~0.95M Suno monthly visits (SimilarWeb, Jun 2026)
- 2,548 incremental paid subscribers from local-method conversion uplift
- 3,920 total paid-subscriber impact including auth + renewals · ~$49K/mo total

**1. AUDIENCE EXPANSION:** +~2,548 incremental paid subscribers · ~$0.38M/year · Add GoPay and DANA as primary wallets
**2. AUTHORIZATION UPLIFT:** +~9,880 recovered card approvals/year · ~$0.12M/year · Local card routing
**3. RENEWAL CONTINUITY:** +~550 renewals saved/month · ~$0.08M/year · Provider redundancy across local PSPs

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | GoPay | Major wallet | Primary acquisition |
| Must-have | DANA | Major wallet | Mobile-first acquisition |
| Optional | QRIS / bank transfer | Mass-adopted trust layer | Coverage |

**Base-case model:** Current paid conversion ~0.8% · With wallets ~3.5% · Incremental uplift +2.7pp · Blended ARPU ~$150/year

**So what:** Indonesia is a mobile-wallet market where card-only checkout structurally under-monetizes existing demand.

**Source:** Bank Indonesia; ASEAN Briefing; SimilarWeb. TO VALIDATE: Suno Indonesia checkout starts, current paid conversion, decline codes.

---

### 7. 🇬🇧 United Kingdom: Open Banking and retry logic compound on an already-strong card base

**Top stat bar:**
- Strong card + Open Banking adoption
- ~0.85M Suno monthly visits (SimilarWeb, Jun 2026)
- 2,132 incremental paid subscribers from local-method conversion uplift
- 3,280 total paid-subscriber impact including auth + renewals · ~$41K/mo total

**1. AUDIENCE EXPANSION:** +~2,132 incremental paid subscribers · ~$0.32M/year · Add Open Banking as a recurring-capable rail
**2. AUTHORIZATION UPLIFT:** +~8,260 recovered card approvals/year · ~$0.10M/year · Token and retry optimization
**3. RENEWAL CONTINUITY:** +~460 renewals saved/month · ~$0.07M/year · Account updater on card renewals

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Open Banking | Growing bank-rail adoption | Recurring-capable alt rail |
| Must-have | Card token/retry optimization | Core rail | Reliability |
| Optional | PayPal | Mainstream | Coverage |

**Base-case model:** Current paid conversion ~3.0% · With Open Banking ~5% · Incremental uplift +2.0pp · Blended ARPU ~$150/year

**So what:** The UK's opportunity is optimization on top of an already-strong base, not new-method acquisition.

**Source:** UK Finance; SimilarWeb. TO VALIDATE: Suno UK checkout starts, current paid conversion, decline codes.

---

### 8. 🇫🇷 France: Cartes Bancaires domestic routing plus PayPal close the gap

**Top stat bar:**
- Cartes Bancaires: dominant domestic card scheme
- ~0.75M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,976 incremental paid subscribers from local-method conversion uplift
- 3,040 total paid-subscriber impact including auth + renewals · ~$38K/mo total

**1. AUDIENCE EXPANSION:** +~1,976 incremental paid subscribers · ~$0.30M/year · Cartes Bancaires domestic routing plus PayPal
**2. AUTHORIZATION UPLIFT:** +~7,660 recovered card approvals/year · ~$0.10M/year · Domestic scheme routing
**3. RENEWAL CONTINUITY:** +~425 renewals saved/month · ~$0.06M/year · SEPA Direct Debit for renewals

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Cartes Bancaires domestic routing | Dominant French scheme | Local card acceptance |
| Must-have | PayPal | Mainstream | Primary alt rail |
| Optional | SEPA Direct Debit | EU standard | Renewal rail |

**Base-case model:** Current paid conversion ~2.5% · With domestic routing ~4.2% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** France's lever is domestic settlement on cards, not new APM acquisition.

**Source:** Banque de France; Stripe; SimilarWeb. TO VALIDATE: Suno France checkout starts, current paid conversion, decline codes.

---

### 9. 🇪🇸 Spain: Bizum is the local APM to test alongside retries

**Top stat bar:**
- 28.8M+ Bizum users (Apr 2025); +82% online YoY
- ~0.6M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,924 incremental paid subscribers from local-method conversion uplift
- 2,960 total paid-subscriber impact including auth + renewals · ~$37K/mo total

**1. AUDIENCE EXPANSION:** +~1,924 incremental paid subscribers · ~$0.29M/year · Add Bizum on mobile checkout
**2. AUTHORIZATION UPLIFT:** +~7,460 recovered card approvals/year · ~$0.09M/year · Local card acceptance
**3. RENEWAL CONTINUITY:** +~415 renewals saved/month · ~$0.06M/year · SCA handling, provider redundancy

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Bizum | 28.8M+ users (Apr 2025) | Primary acquisition rail |
| Must-have | PayPal, cards | Mainstream | Local card acceptance |
| Optional | SEPA Direct Debit | EU recurring | Coverage |

**Base-case model:** Current paid conversion ~2.8% · With Bizum ~4.8% · Incremental uplift +2.0pp · Blended ARPU ~$150/year

**So what:** Spain is a medium-effort European quick win, not a large local-processing gap.

**Source:** Stripe; Bank of Spain; SimilarWeb. TO VALIDATE: Suno Spain checkout starts, current paid conversion, decline codes.

---

### 10. 🇮🇹 Italy: PayPal and SEPA Direct Debit make card-only checkout suboptimal

**Top stat bar:**
- PayPal: leading Italian digital wallet
- ~0.6M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,456 incremental paid subscribers from local-method conversion uplift
- 2,240 total paid-subscriber impact including auth + renewals · ~$28K/mo total

**1. AUDIENCE EXPANSION:** +~1,456 incremental paid subscribers · ~$0.22M/year · Add PayPal and SEPA Direct Debit
**2. AUTHORIZATION UPLIFT:** +~5,650 recovered card approvals/year · ~$0.07M/year · Local card routing
**3. RENEWAL CONTINUITY:** +~310 renewals saved/month · ~$0.05M/year · SEPA-driven renewal reliability

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | PayPal | Leading Italian wallet | Primary recurring rail |
| Must-have | SEPA Direct Debit | EU standard | Recurring rail |
| Optional | PostePay | Local prepaid card culture | Coverage |

**Base-case model:** Current paid conversion ~2.3% · With PayPal + SEPA DD ~4.0% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** Italy mirrors Germany's playbook at smaller scale: preferred local rails plus recurring reliability.

**Source:** Banca d'Italia; Stripe; SimilarWeb. TO VALIDATE: Suno Italy checkout starts, current paid conversion, decline codes.

---

### 11. 🇲🇽 Mexico: cross-border card decline and local debit gap suppress conversion together

**Top stat bar:**
- Local debit cards + SPEI + Mercado Pago: leading e-commerce methods
- ~0.40M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,300 incremental paid subscribers from local-method conversion uplift
- 2,000 total paid-subscriber impact including auth + renewals · ~$25K/mo total

**1. AUDIENCE EXPANSION:** +~1,300 incremental paid subscribers · ~$0.20M/year · Mercado Pago Suscripciones plus local debit acquiring
**2. AUTHORIZATION UPLIFT:** +~5,040 recovered card approvals/year · ~$0.06M/year · Local acquiring, reduce issuer declines
**3. RENEWAL CONTINUITY:** +~280 renewals saved/month · ~$0.04M/year · Retries across local processors

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Local debit / domestic cards | Leading e-commerce method | Primary acquisition + recurring rail |
| Must-have | Mercado Pago Suscripciones | Recurring-capable wallet | Recurring rail |
| Optional | SPEI, Apple/Google Pay | Bank-transfer/wallet trust layer | Coverage |

**Base-case model:** Current paid conversion ~1.5% · With local methods ~4.0% · Incremental uplift +2.5pp · Blended ARPU ~$150/year

**So what:** Mexico combines local payment-method coverage with meaningful card-approval upside.

**Source:** PPRO; PCMI; SimilarWeb. TO VALIDATE: Suno Mexico checkout starts, current paid conversion, decline codes.

---

### 12. 🇰🇷 Republic of Korea: recurring tokens on already-live wallets are the unlock

**Top stat bar:**
- KakaoPay and NaverPay: already live at Suno checkout
- ~0.6M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,196 incremental paid subscribers from local-method conversion uplift
- 1,840 total paid-subscriber impact including auth + renewals · ~$23K/mo total

**1. AUDIENCE EXPANSION:** +~1,196 incremental paid subscribers · ~$0.18M/year · Add Toss and Samsung Pay; enable recurring tokens on live KakaoPay/NaverPay
**2. AUTHORIZATION UPLIFT:** +~4,640 recovered card approvals/year · ~$0.06M/year · Local card uplift
**3. RENEWAL CONTINUITY:** +~260 renewals saved/month · ~$0.04M/year · Subscription retry and token management

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Toss | Major easy-pay platform | Net-new acquisition rail |
| Must-have | Samsung Pay | Mainstream mobile wallet | Net-new acquisition rail |
| Optional | Recurring tokens on KakaoPay/NaverPay | Already live at Suno | Depth on existing rails |

**Base-case model:** Current paid conversion ~2.0% · With Toss + Samsung Pay ~4.0% · Incremental uplift +2.0pp · Blended ARPU ~$150/year

**So what:** Korea is not a card-access problem or even a first-method problem, since two wallets are already live; it is a depth and recurring-token problem.

**Source:** KISDI; Antom; SimilarWeb; Suno help center (KakaoPay/NaverPay confirmed live). TO VALIDATE: Suno Korea checkout starts, current paid conversion, decline codes.

---

### 13. 🇨🇦 Canada: retry and token optimization on an already-strong card base

**Top stat bar:**
- Cards + PayPal: dominant rails
- ~0.55M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,092 incremental paid subscribers from local-method conversion uplift
- 1,680 total paid-subscriber impact including auth + renewals · ~$21K/mo total

**1. AUDIENCE EXPANSION:** +~1,092 incremental paid subscribers · ~$0.16M/year · PayPal depth, Interac coverage
**2. AUTHORIZATION UPLIFT:** +~4,230 recovered card approvals/year · ~$0.05M/year · Retry optimization
**3. RENEWAL CONTINUITY:** +~235 renewals saved/month · ~$0.04M/year · Account updater on renewals

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Cards + PayPal | Dominant rails | Core reliability |
| Optional | Interac | Local bank-debit rail | Coverage |

**Base-case model:** Current paid conversion ~2.8% · With optimization ~4.5% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** Canada is a low-effort optimization market riding on the US playbook.

**Source:** SimilarWeb; Yuno business case model. TO VALIDATE: Suno Canada checkout starts, current paid conversion, decline codes.

---

### 14. 🇹🇷 Turkey: domestic scheme and FX-aware processing matter more than global cards

**Top stat bar:**
- 67M+ TROY cards / 20% of card transactions
- ~0.45M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,092 incremental paid subscribers from local-method conversion uplift
- 1,680 total paid-subscriber impact including auth + renewals · ~$21K/mo total

**1. AUDIENCE EXPANSION:** +~1,092 incremental paid subscribers · ~$0.16M/year · TROY domestic scheme, installments
**2. AUTHORIZATION UPLIFT:** +~4,230 recovered card approvals/year · ~$0.05M/year · FX-aware local acquiring
**3. RENEWAL CONTINUITY:** +~235 renewals saved/month · ~$0.04M/year · Provider redundancy and retry logic

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | TROY (domestic scheme) | 67M cards; 20% of card txns | Primary acquisition + recurring rail |
| Must-have | Local installments | Mainstream Turkish behavior | Conversion driver |
| Optional | Papara, BKM/FAST | Local wallet layer | Coverage |

**Base-case model:** Current paid conversion ~1.8% · With TROY + installments ~4.2% · Incremental uplift +2.4pp · Blended ARPU ~$150/year

**So what:** Turkey is a localization market where domestic card behavior, FX-friendly processing and retries combine.

**Source:** BKM; Daily Sabah; SimilarWeb. TO VALIDATE: Suno Turkey checkout starts, current paid conversion, decline codes.

---

### 15. 🇹🇭 Thailand: PromptPay-adjacent wallets are the dominant local behavior to support

**Top stat bar:**
- PromptPay: dominant Thai payment behavior (bank-linked)
- ~0.35M Suno monthly visits (SimilarWeb, Jun 2026)
- 1,092 incremental paid subscribers from local-method conversion uplift
- 1,680 total paid-subscriber impact including auth + renewals · ~$21K/mo total

**1. AUDIENCE EXPANSION:** +~1,092 incremental paid subscribers · ~$0.16M/year · Add TrueMoney and Rabbit LINE Pay (recurring-capable wallets)
**2. AUTHORIZATION UPLIFT:** +~4,230 recovered card approvals/year · ~$0.05M/year · Local card routing
**3. RENEWAL CONTINUITY:** +~235 renewals saved/month · ~$0.04M/year · Provider redundancy

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | TrueMoney | Major Thai wallet | Recurring-capable acquisition |
| Must-have | Rabbit LINE Pay | Major Thai wallet | Recurring-capable acquisition |
| Optional | Local cards | Coverage | Fallback |

**Base-case model:** Current paid conversion ~1.5% · With wallets ~3.8% · Incremental uplift +2.3pp · Blended ARPU ~$150/year

**So what:** Thailand needs wallet depth more than card optimization; PromptPay itself is a bank-transfer rail, not a subscription-grade mandate, so wallets carry the recurring load.

**Source:** Bank of Thailand; Stripe; SimilarWeb. TO VALIDATE: Suno Thailand checkout starts, current paid conversion, decline codes.

---

### 16. 🇵🇱 Poland: card retries carry more weight than BLIK for a subscription business

**Top stat bar:**
- BLIK: dominant Polish payment method (acquisition-only, not recurring)
- ~0.33M Suno monthly visits (SimilarWeb, Jun 2026)
- 780 incremental paid subscribers from local-method conversion uplift
- 1,200 total paid-subscriber impact including auth + renewals · ~$15K/mo total

**1. AUDIENCE EXPANSION:** +~780 incremental paid subscribers · ~$0.12M/year · BLIK for first payment/acquisition (non-recurring, note caveat)
**2. AUTHORIZATION UPLIFT:** +~3,020 recovered card approvals/year · ~$0.04M/year · Local card acquiring
**3. RENEWAL CONTINUITY:** +~170 renewals saved/month · ~$0.03M/year · Card retries carry all renewals since BLIK does not support subscriptions

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Card retries for renewals | Core recurring rail | Renewal reliability |
| Optional | BLIK | Dominant Polish method | Acquisition-only, not recurring |

**Base-case model:** Current paid conversion ~1.8% · With optimization ~3.5% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** Poland is a smaller market where the subscription model itself constrains the APM opportunity; renewal reliability on cards does most of the work.

**Source:** NBP; PPRO; SimilarWeb. TO VALIDATE: Suno Poland checkout starts, current paid conversion, decline codes.

---

### 17. 🇺🇦 Ukraine: local card routing and wallet tokens compound on an already-billable market

**Top stat bar:**
- UAH already a live Suno billing currency
- ~0.28M Suno monthly visits (SimilarWeb, Jun 2026)
- 676 incremental paid subscribers from local-method conversion uplift
- 1,040 total paid-subscriber impact including auth + renewals · ~$13K/mo total

**1. AUDIENCE EXPANSION:** +~676 incremental paid subscribers · ~$0.10M/year · Local card routing depth
**2. AUTHORIZATION UPLIFT:** +~2,620 recovered card approvals/year · ~$0.03M/year · Apple/Google Pay tokens
**3. RENEWAL CONTINUITY:** +~150 renewals saved/month · ~$0.02M/year · Retry logic on card renewals

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Local card routing | Core rail | Approval uplift |
| Optional | Apple Pay, Google Pay | Mainstream tokens | Coverage |
| Optional | Privat24, LiqPay | Local bank rails | Future depth |

**Base-case model:** Current paid conversion ~1.5% · With optimization ~3.2% · Incremental uplift +1.7pp · Blended ARPU ~$150/year

**So what:** Ukraine is already billable in UAH; the opportunity is pure processing depth, not new-currency enablement.

**Source:** NBU; SimilarWeb; Suno help center (UAH confirmed live currency). TO VALIDATE: Suno Ukraine checkout starts, current paid conversion, decline codes.

---

### 18. 🇦🇷 Argentina: Mercado Pago Suscripciones plus local processing unlock a high-friction market

**Top stat bar:**
- Mercado Pago: dominant Argentine digital wallet
- ~0.20M Suno monthly visits (SimilarWeb, Jun 2026)
- 572 incremental paid subscribers from local-method conversion uplift
- 880 total paid-subscriber impact including auth + renewals · ~$11K/mo total

**1. AUDIENCE EXPANSION:** +~572 incremental paid subscribers · ~$0.09M/year · Mercado Pago Suscripciones (recurring)
**2. AUTHORIZATION UPLIFT:** +~2,220 recovered card approvals/year · ~$0.03M/year · Local card acquiring
**3. RENEWAL CONTINUITY:** +~120 renewals saved/month · ~$0.02M/year · Installments and retries

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | Mercado Pago Suscripciones | Dominant Argentine wallet, recurring-capable | Primary recurring rail |
| Must-have | Local card acquiring | Standard behavior | Approval uplift |
| Optional | Google Pay | Coverage | Fallback |

**Base-case model:** Current paid conversion ~1.2% · With Mercado Pago ~3.5% · Incremental uplift +2.3pp · Blended ARPU ~$150/year

**So what:** Argentina combines high inflation-driven card friction with a dominant wallet that already supports recurring billing.

**Source:** PCMI; Adyen; dLocal; SimilarWeb. TO VALIDATE: Suno Argentina checkout starts, current paid conversion, decline codes.

---

### 19. 🇳🇱 Netherlands: iDEAL for first payment, SEPA Direct Debit for renewals

**Top stat bar:**
- iDEAL: dominant Dutch online payment method
- ~0.22M Suno monthly visits (SimilarWeb, Jun 2026)
- 520 incremental paid subscribers from local-method conversion uplift
- 800 total paid-subscriber impact including auth + renewals · ~$10K/mo total

**1. AUDIENCE EXPANSION:** +~520 incremental paid subscribers · ~$0.08M/year · iDEAL for first payment, converting into SEPA Direct Debit mandate
**2. AUTHORIZATION UPLIFT:** +~2,020 recovered card approvals/year · ~$0.03M/year · Local card uplift
**3. RENEWAL CONTINUITY:** +~110 renewals saved/month · ~$0.02M/year · SEPA-driven renewal reliability

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Must-have | iDEAL | Dominant Dutch method | Primary acquisition rail |
| Must-have | SEPA Direct Debit | EU standard | Renewal rail after iDEAL mandate |
| Optional | Apple/Google Pay | Coverage | Fallback |

**Base-case model:** Current paid conversion ~2.5% · With iDEAL + SEPA DD ~4.3% · Incremental uplift +1.8pp · Blended ARPU ~$150/year

**So what:** The Netherlands is a small, high-conversion market once the iDEAL-to-SEPA-DD handoff is built correctly.

**Source:** Dutch Payments Association; Stripe; SimilarWeb. TO VALIDATE: Suno Netherlands checkout starts, current paid conversion, decline codes.

---

### 20. 🇻🇳 Vietnam: enabling VND billing unlocks MoMo and VietQR

**Top stat bar:**
- MoMo: 30M+ users; QR payments grew 471% YoY
- ~0.21M Suno monthly visits (SimilarWeb, Jun 2026)
- 260 incremental paid subscribers from local-method conversion uplift
- 400 total paid-subscriber impact including auth + renewals · ~$5K/mo total

**1. AUDIENCE EXPANSION:** +~260 incremental paid subscribers · ~$0.04M/year · Enable VND billing first, then MoMo
**2. AUTHORIZATION UPLIFT:** +~1,010 recovered card approvals/year · ~$0.01M/year · Local card routing
**3. RENEWAL CONTINUITY:** +~56 renewals saved/month · ~$0.01M/year · Retry logic once VND billing is live

**Payment method priority:**
| Priority | Method | Scale/penetration | Role for Suno |
|---|---|---|---|
| Prerequisite | Enable VND billing | Not yet a Suno billing currency | Unlocks everything below |
| Must-have | MoMo | 30M+ users | Primary acquisition rail once VND is live |
| Optional | VietQR, local cards | Coverage | Fallback |

**Base-case model:** Current paid conversion ~0.8% (USD-only friction today) · With VND + MoMo ~2.8% · Incremental uplift +2.0pp · Blended ARPU ~$150/year

**So what:** Vietnam is the one market on this list where the first step is not a payment method at all, it is currency enablement; everything else follows from that.

**Source:** GAJRC; market reports; SimilarWeb; Suno help center (VND not in the 17 live currencies). TO VALIDATE: Suno Vietnam checkout starts, current paid conversion, decline codes.

---

## Closing note for the appendix cover slide

"Suno's next 20 markets by combined three-lever opportunity, sized from a business case validated against Suno's own public financials ($300M ARR, 2M paid subscribers, $150/year blended ARPU). 14 markets carry verified per-country data from the underlying model; 6 (Italy, Turkey, Poland, Ukraine, Netherlands, Vietnam) are estimated using the same methodology, proportionally reconciled to the confirmed $12M portfolio total. All figures to be replaced with Suno's actual data in the two-week joint data sprint."
