# OnlyFans research A: traffic, entities, PSP stack, PCI

Read 8 Oct 2026. Web searches used: 6 of 6 (standard). Tags: [F] primary (merchant, registry, filing), [E] third-party estimate, [Third-party claim] unsupported assertion. Reuses `ledger_onlyfans.md` (C1, C25, C28, C29, P1, P9, U1 to U4, V9, V10) without re-research.

## 1. Traffic by country and total visits

### 1a. Similarweb, September 2026 (from ledger C28, not re-fetched)
US 42.78%, UK 5.41%, DE 5.32%, CA 5.27%, ES 2.96%. Source: https://www.similarweb.com/website/onlyfans.com/
Ranks 6 to 10: **No public information found.** Similarweb page returned 403 on fetch today (direct and via r.jina.ai). Needs Similarweb Pro login.

### 1b. Semrush, August 2026 (new, different panel) [E]
Page "Last updated: September 17, 2026". Total visits **382.68M (August 2026)**.
1. United States 39.77% (152.2M)
2. Mexico 4.96% (18.99M)
3. United Kingdom 4.64% (17.75M)
4. Canada 3.47% (13.29M)
5. Brazil 3.16% (12.11M)
Ranks 6 to 10: not shown on the public Semrush page. **No public information found.**
Source: https://www.semrush.com/website/onlyfans.com/overview

Note: Similarweb and Semrush disagree on country order (Semrush has Mexico #2 and Brazil #5; Similarweb Sept top 5 has neither MX nor BR). Germany absent from Semrush top 5. Do not mix panels on one slide.

### 1c. Older data points [E]
- OFStats: 305.5M visits Dec 2025; US 48.96%, UK 5.97%, MX 5.62%, DE 4.53%, CA 4.48%, other 30.44%. https://ofstats.net/
- Semrush search snippet (Jan 2026 country data): US 39.96%, UK 5.48%, MX 4.23%, DE 3.46%, BR 3.11%; snippet also says 414M visits in June 2026. https://www.semrush.com/website/onlyfans.com/overview (snippet; page now shows Aug 2026)

### 1d. Candidate rank 6 to 10 countries
Union of all panels above: Germany, Spain, Brazil, Mexico (depending on panel). Anything beyond that (France, Italy, Australia, etc.) = **No public information found**. [INFERENCE — not confirmed] ranks 6 to 10 in Similarweb likely include MX and BR, given they appear in top 5 on Semrush and OFStats.

### 1e. Regional domains
No OnlyFans regional ccTLDs found. Semrush returns many unaffiliated lookalike domains (onlyfan.com, only-fans.me, only-fans.uk, onlyfansleaks.tv); these are NOT OnlyFans properties. `start.onlyfans.com` is a subdomain used by the May 2026 brief's Similarweb citation.

## 2. Legal entities

### 2a. Subsidiaries per Fenix group accounts FY ended 30 Nov 2025 [F] (new)
Source: Fenix International Limited, group accounts made up to 30 Nov 2025, filed 20 Sep 2026, note 15 "Subsidiaries", p. 39 of PDF:
https://find-and-update.company-information.service.gov.uk/company/10354575/filing-history/MzU0NTkyNjUxNGFkaXF6a2N4/document?format=pdf&download=0

| Entity | Registered office | % held direct |
|---|---|---|
| Fenix Internet LLC | 501 Silverside Road, Suite 87, Wilmington, Delaware, USA 19809 | 100 |
| Delivery Code Limited (UK 08662491) | 9th Floor, 107 Cheapside, London EC2V 6DN | 100 |
| Fenix US INC | 501 Silverside Road, Suite 87, Wilmington, Delaware, USA 19809 | 100 |
| HPS Poland Spolka z ograniczona odpowiedzialnoscia | ul. Prwna 15/1 (as printed), 30-527 Krakow, Poland | 75 |
| OF World LLC | 501 Silverside Road, Suite 87, Wilmington, Delaware, USA 19809 | 100 |
| OF Media Productions Limited (UK 15555739) | 9th Floor, 107 Cheapside, London EC2V 6DN | 100 |

Same filing, related parties (note 27, p. 43): HPS Poland is shown with amounts related to "payments for management charges" [F, read from scan; exact figures not transcribed]. [INFERENCE — not confirmed] HPS Poland is a service/tech center, not a payments licence entity.

Other facts from the same filing [F]:
- Revenue by geography FY2025 ($000): USA 965,447; UK and Europe 346,771; Rest of World 241,091; total 1,553,309 (FY2024: 909,062 / 283,705 / 220,327 / 1,413,094). Note 4, p. 33.
- Employees: group average 47 (company 37). Note 5, p. 33.
- "Amounts due from Payment Service Providers" $134.9M at 30 Nov 2025 (FY2024 $119.3M), less provisions $3.46M "relate to timing differences on refunds and chargebacks". Note 16, p. 40. Confirms plural PSPs in the accounts but names none.
- Sales tax and VAT liability about $161M (2025) noted in note 28 (scan, figures approximate).
- Controlling party note 29: L. Radvinsky ultimate controlling party at year end; he "passed away on 20 March 2026", control vested in K. Chudnovsky as sole trustee of the LR Fenix Trust (scan reading; verify wording before use).

Companies House name search found no other "Fenix International" related companies (results unrelated). https://find-and-update.company-information.service.gov.uk/search/companies?q=fenix+international

### 2b. Local entity per traffic country
| Country | Local entity? | Source |
|---|---|---|
| United States | Yes: Fenix Internet LLC, Fenix US INC, OF World LLC (Delaware) | Accounts note 15 (above) |
| United Kingdom | Yes: Fenix International Ltd (HQ), Delivery Code Ltd, OF Media Productions Ltd | Accounts note 15; C1 |
| Germany | No entity in subsidiary list | Accounts note 15 (complete list at 30 Nov 2025) |
| Canada | No | Accounts note 15 |
| Spain | No | Accounts note 15 |
| Mexico | No | Accounts note 15 |
| Brazil | No | Accounts note 15 |
| Ranks 6 to 10 (unknown) | None outside US, UK, Poland in the group | Accounts note 15 |
Poland (75% HPS Poland) is the only non-UK/US entity; Poland is not in any top 5 traffic list.

LinkedIn/OpenCorporates not separately searched (budget); the audited subsidiary list is the stronger source.

## 3. PSP stack

| Claim | Tag | Source |
|---|---|---|
| Terms: payments processed by "a third-party payment provider we approve" (no name) | [F] | ledger P1, https://onlyfans.com/terms |
| Accounts show receivables from "Payment Service Providers" (plural), $134.9M | [F] | Accounts note 16, link above |
| Stripe, CCBill, Merrick, Harris used to "distribute transaction volume and keep chargeback ratios within acceptable limits" | [Third-party claim] | https://paymentcloudinc.com/blog/onlyfans-payment-processor-guide/ (summarising Corepay and SecureGlobalPay) |
| CCBill descriptors on statements | [Third-party claim] | ledger P9 |
| Adyen, Checkout.com, Worldpay, Braintree | No public information found linking any of them to OnlyFans | Search "OnlyFans payment gateway PSP Stripe Adyen Checkout.com Worldpay Braintree" |
| Orchestrators Spreedly, Primer, Gr4vy, CellPoint, APEXX | No public information found | Search "OnlyFans payment orchestration Spreedly Primer Gr4vy CellPoint APEXX" (results only generic Gr4vy/Spreedly pages) |

No [Checkout], [Source Code], [Job Listing] or [Press Release] evidence found. New since May 2026: only the [F] confirmation of plural PSPs in FY2025 accounts; no PSP named anywhere primary.

## 4. PCI DSS
- No public certification, AOC, ROC or security page found. Privacy policy and Transparency Center contain no PCI statement (ledger V9).
- Search "OnlyFans PCI DSS compliance security certification" returned only content-farm blogs asserting PCI compliance and tokenization, e.g. https://www.cgaa.org/article/is-onlyfans-safe-for-credit-cards [Third-party claim, Low, Omit].
- [INFERENCE — not confirmed] With $1.55B revenue (FY2025) on card volume, OnlyFans would fall in PCI Level 1 by transaction count; scope depends on whether its PSPs host card capture.
