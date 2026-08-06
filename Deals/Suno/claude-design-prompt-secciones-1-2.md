# Prompt para Claude Design: Suno BC, secciones 1 y 2 (2026-08-06)

Copia enviada a Claude Design. Alcance: slides 1 a 17 + 4 slides nuevas. Business case (18-36) queda para una fase posterior.

---

You are editing an existing Google Slides deck: "Business Case - Suno + Yuno" (36 slides). This pass covers ONLY Section 1 (context, slides 1-7) and Section 2 (Why Yuno, slides 8-17), plus four NEW slides. Do NOT touch slides 18-36 (the Business Case section); we will handle those in a later pass.

## NON-NEGOTIABLE RULES

1. DO NOT change the design of any existing slide: no changes to layouts, colors, fonts, logos, backgrounds, image positions, or slide masters. Existing slides get TEXT AND DATA replacements only, exactly as specified below.
2. The ONLY design work allowed is the four NEW slides, and they must follow the deck's existing design system (same fonts, colors, header style, footer style, section labels).
3. US English. Never use em-dashes or " - " as punctuation. Never use the phrase "no small feat".
4. Never invent numbers. Every figure below is verified; if you need a figure that is not provided, leave a [TO VALIDATE] placeholder instead of inventing one.
5. Keep all existing source footnotes; add the new ones specified.

## EXISTING SLIDES: TEXT REPLACEMENTS

### Slide 1 (cover)
- Replace the title "POWERING SEAMLESS GLOBAL MONEY MOVEMENT" with: "Suno's Payment Infrastructure: Today, the Proposed Model, and What It Unlocks".
- Everything else stays exactly as is.

### Slide 2 (agenda)
- Replace the three agenda items with four:
  01. HOW SUNO RUNS PAYMENTS TODAY
  02. THE PROPOSED MODEL & WHY YUNO
  03. BUSINESS CASE
  04. ROADMAP & NEXT STEPS
- Keep the layout; if the design only fits three lines cleanly, merge 03 and 04 into "03. BUSINESS CASE & ROADMAP".

### Slide 3 (section divider)
- Replace "Our understanding of the context" with "How Suno runs payments today".

### Slide 4 (Executive Summary)
- Replace the company description paragraph with: "AI music generation platform. $300M ARR and 2M+ paying subscribers (Feb 2026). $400M+ Series D at a $5.4B valuation (Jun 2026). 100M+ users since launch. The US is ~19% of traffic; 80%+ is international, led by Brazil, Germany and Japan."
- Delete "7 million songs created daily" and "recently closed a $250M Series C at a $2.45B valuation. $200M+ ARR" wherever they appear.
- Replace "Top markets: US, India, and Brazil." with nothing (covered by the new description).
- In KEY CHALLENGES, replace these bullets:
  - "IAP - so fully dependent on store regulations (30% MDRs)." becomes: "In-app billing depends on store rules: Apple 30% (15% after year one), Google 15%. iOS pricing already carries the markup: Pro $10 vs $8 on web."
  - "Missing local payment methods in top markets" becomes: "Local payment method coverage is capped by what a single processor supports. Suno's own help center: 'Options not yet available with our direct processor may be available on mobile.'"
  - "Cross-border processing friction in markets outside USA" becomes: "Cross-border processing from a single US entity in markets like Brazil, Germany and Japan".
  - Keep the "Single dependency on Stripe" and "No smart routing" bullets as they are.
- Replace "OVER 1,500 INSTANT PAYMENT CONNECTIONS" with "1,000+ PAYMENT METHODS · 460+ INTEGRATIONS · ONE API" (must match slide 9's figures).

### Slide 5 (current setup constraints)
- Replace "$250M raised to grow globally" with "$400M+ Series D raised to grow globally".
- Replace "a Head of International Markets just hired" with "a Head of International Markets on board since Sept 2025".
- Replace "$200M+ in annual recurring revenue at risk" with "$300M in annual recurring revenue at risk".
- Replace the entire "DEPENDENT ON STRIPE CONNECTIONS" box (title and body) with:
  Title: "THREE BILLING RAILS, ZERO UNIFIED VIEW"
  Body: "Web billing runs on Stripe, iOS on Apple in-app purchase, Android on Google Play: three disconnected systems with no unified reconciliation and no single source of truth on payment performance."

### Slide 6 (payment stack)
- Replace "Visa, Mastercard, Amex, and Discover handle most online volume across your operations" with "Visa, Mastercard and Amex handle most online volume across Suno's operations". If a Discover logo appears on this slide, remove that one logo; change nothing else visually.
- Replace "In-Store payment processing relies on the Apple and Play Store which means high discount rates.. Estimated 30% of sales happen in-app." with: "In-app payment processing relies on the Apple App Store and Google Play at 15-30% store fees. In-app share of sales: [TO VALIDATE with Suno data]."
- Replace the "APM INTEGRATION OPPORTUNITY" body text with: "Live today: 17 billing currencies across 36 countries, all through one processor. Korea: Korean Card, KakaoPay, NaverPay. India: UPI. Some regions: Apple Pay, Google Pay, Cash App Pay, stablecoin. PayPal is reachable only through the app stores. Deepening local methods in high-volume markets reduces cost and expands the paid base."
- Add footnote: "Source: Suno help center (accepted payment methods), Aug 2026."

### Slide 7 (traffic map)
- Update the five main traffic labels to: US 19.2% · Russia 5.41% · Brazil 4.97% · Germany 4.72% · Japan 3.93%.
- Delete any other percentage labels on the map (text deletion only; keep the map design).
- Add footnote: "Source: SimilarWeb, June 2026, share of web visits."

### Slide 8 (section divider "Why Yuno?")
- Replace "Why Yuno?" with "The proposed model".

### Slide 9 (Yuno stats)
- No changes.

### Slide 10 (why Yuno is the right partner)
- Replace "Engineered for the high-concurrency spikes of gaming." with "Engineered for high-concurrency consumer subscription renewals and viral launch spikes."
- No other changes.

### Slide 11 (product suite)
- Text stays identical. Bold these four module names only: "Payouts", "Subscription management", "Network tokens and account updater", "Monitors & auto-failover". No layout changes.

### Slide 12 (competitive advantage table)
- Replace the column header "WHAT GLOBAL PSPS MISS" with "SINGLE-PSP SETUP (TODAY)".
- Replace the column header "ADVANTAGE" with "ORCHESTRATED SETUP (PROPOSED)".
- Row content stays the same.

### Slide 13 (global presence)
- Fix the placeholder: replace "SECTION TITLE" with "WHY YUNO?". Nothing else.

### Slide 14 (logos)
- No changes.

### Slide 15 (leadership)
- No changes.

### Slide 16 (credentials)
- Attribution must be unambiguous: inDrive = "Expanded to 11 countries in 8 months, 90% approval rates". Rappi = "Cuts new provider implementation time to zero". Livelo = "+5% approval uplift · 50% transaction recovery". Wingo = keep the "+14% increase in approval rates" claim ONLY if it belongs to Wingo's official post; if the floating stats cannot be attributed cleanly, attach "50% transaction recovery / 5% approval uplift" to Livelo and remove the unattributed number.

### Slide 17 (partner to scale Suno)
- No changes.

## NEW SLIDES TO DESIGN (match the deck's design system)

### NEW SLIDE A: "What 2026 adds to the stack" (insert after slide 6)
Section label: HOW SUNO RUNS PAYMENTS TODAY.
Title: "2026 adds new money flows on top of the same single rail"
Four blocks:
1. "LICENSED-MODEL RELAUNCH (WARNER DEAL)" body: "Paid tiers get monthly download caps with the ability to pay for more. A new consumption-purchase layer lands on top of subscriptions."
2. "CREATOR PAYOUTS ARE ALREADY LIVE" body: "The Spark program pays cash grants to independent artists today. Opt-in artist licensing under the Warner deal implies recurring artist compensation flows."
3. "INTERNATIONAL PUSH" body: "A dedicated Head of International Markets is driving expansion, on a stack that bills every market cross-border from one US entity."
4. "MORE PAID CONVERSION PRESSURE" body: "Free-tier downloads end in 2026, deliberately pushing more users toward paid, meaning more transaction volume through the same rail."
Footnote: "Sources: Warner Music Group and Suno partnership announcement (Nov 2025); Suno Spark announcement (Jun 2026)."

### NEW SLIDE B: "Web vs app store economics" (insert after New Slide A)
Section label: HOW SUNO RUNS PAYMENTS TODAY.
Title: "Every subscription that moves from the app stores to web keeps 15-30% more revenue"
Left block, "TODAY": "Same plans, two prices. Pro: $10 on iOS vs $8 on web. Premier: $30 on iOS vs $24 on web. iOS pricing already absorbs the store fee. PayPal is only reachable via the app stores, so that volume pays the store fee too."
Right block, "THE LEVER": "Grow the web billing share: a faster web checkout, local payment methods per market, and external purchase flows where rules allow them (US post-Epic ruling, EU DMA). Each point of billing mix shifted to web saves 15-30% on that revenue."
Footnote: "Source: Apple App Store and suno.com/pricing, verified Aug 2026."

### NEW SLIDE C: "The decision frame" (insert right after slide 8, the new "The proposed model" divider)
Section label: THE PROPOSED MODEL.
Title: "A second PSP fixes one gap. Orchestration fixes all four."
Table: 4 rows (the gaps) by 3 columns (the options).
Column headers: "TODAY: Stripe only" · "OPTION A: add a second PSP directly" · "OPTION B: add an orchestration layer".
Row 1 "Local methods capped by one processor's catalog": Today: "Limited to the native method list; Suno's help center already points users to mobile when a method is unavailable" / Option A: "Better, but still capped by the second provider's list; two integrations to build and maintain" / Option B: "One integration opens 1,000+ methods and local PSPs per market".
Row 2 "Cross-border card declines (Brazil, Germany, Japan billed from a US entity)": Today: "Cross-border routing only" / Option A: "Partial: local acquiring where the second PSP has it" / Option B: "Routes each market to its best-performing local acquirer".
Row 3 "Renewal failures at 2M+ subscribers": Today: "Single provider, no cross-provider retry" / Option A: "No retries BETWEEN the two providers" / Option B: "Cross-PSP smart retries, network tokens, account updater".
Row 4 "Three disconnected billing rails and payouts arriving in 2026": Today: "No unified view" / Option A: "Now four systems to reconcile" / Option B: "One dashboard, unified reconciliation, payouts through the same API".
Bottom line: "Option A adds a second integration and fixes one gap. Option B adds one integration and addresses all four."

### NEW SLIDE D: "Proposed architecture" (insert after New Slide C)
Section label: THE PROPOSED MODEL.
Title: "Keep Stripe direct. Add the orchestration layer alongside it. Zero infra risk, full upside."
Diagram (build in the deck's design system): a "Yuno Orchestration Layer" band on top; below it two branches: left box "Stripe (direct)" labeled "Existing integration preserved: global card processing, markets where Stripe performs well, fallback path. No migration needed, stays as is." Right box "Local PSPs and methods" labeled "New via one API: local payment methods per market, local acquiring and domestic scheme routing, cross-PSP smart retries, payouts, single dashboard and unified reconciliation."
Bottom line: "Nothing is ripped out. Stripe stays live as the safety net; the layer adds redundancy, local rails and recovery around it."

## SEQUENCE AFTER THIS PASS
Section 1: cover, agenda, divider, exec summary (4), constraints (5), stack (6), NEW A (2026 flows), NEW B (web vs stores), traffic map (7).
Section 2: divider "The proposed model" (8), NEW C (decision frame), NEW D (architecture), Yuno stats (9), why partner (10), suite (11), advantage table (12), presence (13), logos (14), leadership (15), credentials (16), partner to scale (17).
Slides 18-36 remain untouched in this pass.
