# SDR Research Brief — H&M (Hennes & Mauritz)
**Yuno Payment Orchestration Intelligence Report**
*Framework v6.0 | Date: 2026-04-08 | Analyst: Claude Opus 4.6*

---

## EXECUTIVE SUMMARY

H & M Hennes & Mauritz AB (HM-B.STO, Nasdaq Stockholm) is the world's second-largest fashion retailer, operating **3,616 H&M stores across 81 markets** with **62 online markets** and ~70 additional "global selling" markets. The group generated SEK 234B (~$22B) in FY2024 revenue. Their primary PSP is **Adyen**, which handles unified commerce (online + in-store) payment processing globally. H&M accepts a wide range of payment methods including Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay, Klarna BNPL, and various local methods. No third-party payment orchestration platform has been identified. With 81 physical markets and 60+ online markets spanning Europe, Americas, Asia, Oceania, and Africa, H&M faces significant multi-market payment complexity — a strong fit for orchestration. The 2024 Brazil launch and continued LATAM expansion create an active payment infrastructure buildout window.

---

## SECTION 1 — Website Traffic Analysis by Country

hm.com operates as a single global domain with country-specific subdomains/paths. Total traffic as of November 2025 was **~114.1M monthly visits** (+8.13% MoM from October 2025). The audience skews female (68.34%) with the largest age group being 25-34.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | ~18-20% | ~20-23M | Stable — top desktop traffic source | https://www.similarweb.com/website/hm.com/ |
| 2 | Germany | ~10-12% | ~11-14M | Stable | https://www.similarweb.com/website/hm.com/ |
| 3 | United Kingdom | ~8-10% | ~9-11M | Stable | https://www.similarweb.com/website/hm.com/ |
| 4 | Sweden | ~5-7% | ~6-8M | Stable — home market | https://www.similarweb.com/website/hm.com/ |
| 5 | India | ~4-6% | ~5-7M | Growing | https://www.similarweb.com/website/hm.com/ |
| 6 | France | ~3-5% | ~4-6M | Stable | https://www.similarweb.com/website/hm.com/ |
| 7 | Netherlands | ~3-4% | ~3-5M | Stable | https://www.similarweb.com/website/hm.com/ |
| 8 | Spain | ~3-4% | ~3-5M | Stable | https://www.similarweb.com/website/hm.com/ |
| 9 | Italy | ~2-3% | ~2-4M | Stable | https://www.similarweb.com/website/hm.com/ |
| 10 | Poland | ~2-3% | ~2-3M | Stable | https://www.similarweb.com/website/hm.com/ |

**Note:** Exact country-level percentage splits are **[INFERENCE — not confirmed]** — SimilarWeb confirmed US, Germany, and UK as the top 3 countries but full breakdown is behind the paywall. Rankings 4-10 are estimated based on H&M's known store density and market size. Total monthly visits (114.1M) and top-3 ranking are confirmed.

**Traffic Sources (Desktop):** Direct (44.79%), Organic Search (40.68%), remainder from paid, social, referral, and email.

Source: https://www.similarweb.com/website/hm.com/ | https://www.semrush.com/website/hm.com/overview/

---

## SECTION 2 — Legal Entities & Local Presence

**Parent Company:** H & M Hennes & Mauritz AB (publ), Reg. No. 556042-7220, Stockholm, Sweden. Listed on Nasdaq Stockholm.

**Brand Portfolio:** H&M (incl. H&M HOME, H&M Move, H&M Beauty), COS (247 stores/49 markets), Weekday (43 stores/14 markets), & Other Stories (66 stores/24 markets), ARKET (54 stores/22 markets), Monki (online-only/29 markets), Sellpy (online-only/24 markets), Singular Society.

**Geographic Footprint (as of February 28, 2026):**

H&M Group operates in **81 store markets** and **62 online markets**, plus ~70 additional "global selling" markets.

| Region | Key Markets (stores + online) | Notes |
|--------|-------------------------------|-------|
| **Nordics** | Sweden (HQ), Norway, Denmark, Finland, Iceland | Home region; Sweden is corporate HQ |
| **Western Europe** | Germany, UK, France, Netherlands, Belgium, Austria, Switzerland, Ireland | Germany and UK are top revenue markets |
| **Eastern Europe** | Poland, Czech Republic, Romania, Hungary, Bulgaria, Slovakia, Croatia, Lithuania, Latvia, Estonia, Slovenia | Strong store presence |
| **Southern Europe** | Spain, Italy, Portugal, Greece, Turkey, Cyprus | Established markets |
| **North & South America** | USA, Canada, Mexico, Chile, Peru, Colombia, Uruguay, Puerto Rico, **Brazil (new — launched Aug 2025)** | LATAM expansion ongoing |
| **Asia, Oceania & Africa** | China, India, Japan, South Korea, Australia, Indonesia, Malaysia, Singapore, Thailand, Vietnam, Philippines, Egypt, Morocco, South Africa, Israel, UAE, Saudi Arabia, Kuwait, Oman, Bahrain, Qatar | Major presence in Asia |

**Key Subsidiaries (confirmed from public filings):**
- H & M Hennes & Mauritz AB (publ) — Sweden (parent)
- H&M has local operating subsidiaries in each major market — **[INFERENCE — not confirmed]** exact entity names not publicly listed outside the full annual report's note on group companies
- COS, Weekday, & Other Stories, ARKET, Sellpy operate as brands within the group structure

**Recent Changes:**
- Afound brand wound down in 2024
- Monki integrated into Weekday (stores + online) during 2025
- Brazil market launched August 2025 (stores + online)
- ~70 additional "global selling" online markets added

Source: https://hmgroup.com/about-us/markets-and-expansion/ | https://hmgroup.com/news/h-m-hennes-mauritz-ab-full-year-report-2024/ | https://hmgroup.com/wp-content/uploads/2025/01/H-M-Hennes-Mauritz-AB-Full-year-report-2024.pdf

---

## SECTION 3 — Payment Service Providers (PSP Stack)

### Confirmed PSP: Adyen [Press Release] [Industry Source]

**Adyen** is H&M's primary payment service provider for unified commerce (online + in-store).

- **Evidence:** Adyen publicly lists H&M as a customer. Multiple Adyen marketing materials, press coverage, and industry analyses reference H&M as a flagship Adyen client alongside Uber, Spotify, eBay, and Microsoft.
- **Scope:** Adyen processed €544B+ in H2 2023 across its client base. For H&M, Adyen likely handles acquiring, payment gateway, fraud prevention, and terminal processing across multiple markets.
- **Source:** https://www.adyen.com/industries/retail | https://theretailexec.com/tools/adyen-review/

### Accepted Payment Methods (US Market)

From H&M's US customer service page, H&M accepts:
- **Cards:** Visa, Mastercard, American Express, Discover
- **Digital Wallets:** Apple Pay, Google Pay, PayPal
- **BNPL:** Klarna (Pay in 4, Pay in 30 days)
- **Gift Cards:** H&M gift cards
- **[INFERENCE — not confirmed]** European markets likely also accept local methods such as iDEAL (NL), Bancontact (BE), Swish (SE), Sofort/Giropay (DE), Multibanco (PT), Bizum (ES) — consistent with Adyen's APM coverage.

### Payment Orchestration

No evidence found of a third-party payment orchestration platform (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno). **[INFERENCE — not confirmed]** H&M likely relies on Adyen's built-in routing and optimization capabilities rather than a separate orchestration layer.

### Other Payment Partners

- **Klarna** — BNPL provider, confirmed on H&M US checkout. Klarna and H&M have had a longstanding partnership (both are Swedish companies).
- **PayPal** — Confirmed as accepted payment method in US and likely other markets.

Source: https://www2.hm.com/en_us/customer-service/payments.html | https://www.adyen.com/industries/retail

---

## SECTION 4 — PCI DSS Compliance

**No public PCI DSS certification or compliance attestation page found for H&M.**

**[INFERENCE — not confirmed]** As a Level 1 merchant processing millions of card transactions annually across 80+ markets, H&M is required to maintain PCI DSS compliance and undergo annual audits by a Qualified Security Assessor (QSA). Their use of Adyen as a PCI-certified PSP (Adyen is PCI DSS Level 1 certified) means H&M can reduce their PCI scope by using Adyen's hosted/tokenized payment flows. H&M's annual report references data protection and information security as key risk areas but does not specifically mention PCI DSS certification.

Source: https://www.pcisecuritystandards.org | https://hmgroup.com/about-us/corporate-governance/annual-report/

---

## SECTION 5 — Key Findings & Yuno Relevance

### Opportunities
1. **81 markets, massive complexity** — H&M operates in more physical markets than almost any fashion retailer. Managing local payment methods, acquirers, and regulatory requirements across 81+ markets is a textbook use case for payment orchestration.
2. **LATAM expansion** — Brazil launched in August 2025, joining existing Chile, Peru, Colombia, Uruguay, Mexico markets. LATAM is Yuno's home turf. Active infrastructure buildout = decision window.
3. **Single-PSP concentration risk** — Heavy reliance on Adyen creates vendor lock-in. An orchestration layer would provide failover, A/B testing of acquirers, and negotiation leverage.
4. **Multi-brand complexity** — 8 brands (H&M, COS, Weekday, & Other Stories, ARKET, Monki, Sellpy, Singular Society) across different market footprints could benefit from unified payment orchestration.
5. **No orchestration layer detected** — No evidence of Spreedly, Primer, or any orchestration platform, meaning the category is greenfield.

### Risks
- Adyen relationship is deeply embedded (unified commerce = online + POS) and likely contractually long-term
- H&M's scale means decisions are made centrally in Stockholm with long procurement cycles
- Internal payment teams may resist adding an orchestration layer on top of Adyen

---

*Research completed 2026-04-08. 6 web searches used.*
