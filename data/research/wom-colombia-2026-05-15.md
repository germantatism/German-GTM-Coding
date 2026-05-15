# WOM Colombia (Partners Telecom Colombia S.A.S.) — Yuno SDR Research Brief
*Date: 2026-05-15 | Framework v8.0 | Disclaimer: ownership, parallel-proceeding scope, and recharge-checkout PSP identity carry [INFERENCE] flags per web data; assumptions noted inline.*

### EXECUTIVE SUMMARY
WOM Colombia — legally Partners Telecom Colombia S.A.S. (PTC, formerly Avantel) — is Colombia's #3 mobile operator with ~6.4M lines (~6.7% share), a single-country business in active financial recovery. It completed a US Chapter 11 (Delaware, effective Mar 21, 2025) and a Colombian reorganización (SuperSociedades confirmed Jul 17, 2025), was acquired by SUR Holdings in Jan 2025, and turned EBITDA-positive in H1 2025 under a new finance-oriented CEO (Dec 2025). Payment-stack finding: a single confirmed gateway (ePayco) powers postpaid bill pay, with documented duplicate-charge and delayed-crediting complaints and a fragmented domestic rail mix (PSE, Nequi, Daviplata, 20+ cash networks). Main Yuno opportunity: single-PSP redundancy + auth-rate/recovery uplift framed as a cost-efficiency lever for a margin-constrained turnaround.

> ⚠️ BRAND NOTE: Colombia's SIC ordered PTC to stop using the "WOM" brand (resolution Jan 28, 2026); the company is rebranding and operating temporarily as Partners Telecom Colombia / movilPT.co. Address the entity as **Partners Telecom Colombia S.A.S.** in all collateral.

---

### SECTION 1 — Traffic by Country
| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source |
|---|---|---|---|---|---|
| 1 | Colombia | 89.8% (desktop) | ~581K total (Apr 2026) | -10.6% MoM | [SimilarWeb](https://www.similarweb.com/website/wom.co/) |
| 2 | United States | 2.75% | — | n/a | [SimilarWeb](https://www.similarweb.com/website/wom.co/) |
| 3 | Chile | 2.44% | — | n/a | [SimilarWeb](https://www.similarweb.com/website/wom.co/) |

Single-country (Colombia) operator. Distinct legal entity from **wom.cl** (WOM Chile / WOM SpA), which is separately owned by a creditor group (Amundi/BlackRock/Man GLG/Moneda) — do not conflate. No LATAM cross-border footprint; opportunity is depth-in-market, not multi-country.

---

### SECTION 2 — Legal Entities
| Country | In Top Traffic? | Local Entity? | Cross-Border Risk? | Source |
|---|---|---|---|---|
| Colombia | ✅ | ✅ Partners Telecom Colombia S.A.S. (ex-Avantel) | No — domestic operator | [SuperSociedades](https://www.supersociedades.gov.co/noticias-supersociedades/-/asset_publisher/atwl/content/superintendencia-de-sociedades-confirma-el-acuerdo-de-reorganizaci%C3%B3n-de-partners-telecom-colombia-s.a.s.) |

Ownership: acquired by **SUR Holdings** (US/UK consortium — Alexey Reznikovich, Vitaliy Podolskiy, Mat Travizano, Stan Chudnovsky) from Novator Partners, Jan 2025. ([El Tiempo](https://www.eltiempo.com/economia/empresas/wom-colombia-es-adquirida-por-sur-holdings-para-garantizar-su-crecimiento-en-el-pais-3417639), [DCD](https://www.datacenterdynamics.com/en/news/sur-holdings-acquires-colombias-wom/)). No cross-border acquiring angle — pitch is domestic auth-rate and redundancy, not local-entity gaps.

> ⚠️ MANUAL: Verify processing entity on official T&Cs (wom.co/tyc) once accessible.

---

### SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**
| Country | PSP / Acquirer | Evidence Type | Source |
|---|---|---|---|
| Colombia | **ePayco** (postpaid bill pay) | [Press Release] [Checkout] — dedicated co-branded subdomain `pagosexpress-wom.epayco.com` | [ePayco WOM portal](https://pagosexpress-wom.epayco.com/), [Scribd mirror](https://www.scribd.com/document/775166415/Paga-tus-facturas-WOM-con-ePayco-facil-y-seguro) |
| Colombia | Recharge-flow PSP | Not confirmed — JS-rendered/blocked checkout | [INFERENCE — not confirmed] likely same ePayco integration |

**3B. Orchestrator:** No public evidence found of Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno. WOM Colombia runs a fragmented domestic stack with **single confirmed gateway (ePayco)** and no orchestration layer.

> ⚠️ MANUAL — DevTools test card 4111 1111 1111 1111 | 02/30 | 123 to confirm the recharge-flow processor.

---

### SECTION 4 — APMs (Agent D)

**4A. Confirmed APMs**
| Market | APMs Confirmed | Source |
|---|---|---|
| Colombia (bill pay) | PSE; Visa, Mastercard, American Express, Codensa; Nequi; Daviplata; bank agreements (Bancolombia, Davivienda, BBVA, Banco de Bogotá); cash (Efecty, Baloto, Éxito, SuperGiros) | [Selectra factura](https://selectra.com.co/empresas/wom/factura/pagar), [Nequi help center](https://ayuda.nequi.com.co/hc/es/articles/33954890040973) |
| Colombia (online recharge) | Debit/credit card, PSE (web guest flow); Nequi, Daviplata (Mi WOM app) | [Selectra recargas](https://selectra.com.co/empresas/wom/recargas) |

**4B. Unverified**
| Market | Verification Attempted? | Reason | Notes |
|---|---|---|---|
| wom.co live checkout | Yes | ECONNREFUSED / bot-block from research environment | APMs confirmed via 3rd-party sources, not live page |
| Recharge-flow native PSP | Yes | JS-rendered, no PSP name surfaced | Manual VPN walk-through needed |

> "Not verified" ≠ "not available." Never claim WOM lacks a method in outreach.

---

### SECTION 5 — Payment Complaints
| Issue Type | Platform | Frequency | Source |
|---|---|---|---|
| Duplicate recharges (dedicated complaint form exists) | wom.co | Structural — own intake form | [wom.co duplicate form](https://www.wom.co/form/recharge/duplicate) |
| Recharge not credited / delayed (24–48h on wallets & cash) | Selectra / forums | Recurring | [Selectra recargas](https://selectra.com.co/empresas/wom/recargas) |
| Unauthorized / unrecognized charges (~$20,999 COP) | Laneros forum | Multiple posts | [Laneros](https://www.laneros.com/temas/wom-colombia-foro-oficial.242165/page-1193) |
| Overbilling, refund never received | Apple App Store (Mi WOM 2.6★) | Multiple reviews | [App Store Mi WOM](https://apps.apple.com/co/app/mi-wom/id1598372244) |
| Refund friction — 15-business-day PQR window, no instant refund | Selectra / wom.co PQR | Structural | [Selectra PQR](https://selectra.com.co/empresas/wom/pqr) |

**Pattern → Yuno fit:** Duplicate charges and delayed crediting map to real-time monitoring + automated retry/recovery; refund friction maps to centralized reconciliation and faster dispute handling.

---

### SECTION 6 — Expansion & Corporate Developments
| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | 2026-01-28 | SIC orders cessation of "WOM" brand; rebrand underway | Brand/legal | [Telesemana](https://www.telesemana.com/) / [El Colombiano](https://www.elcolombiano.com/) |
| 2 | 2025-12-04 | Gyorgy Zsembery appointed CEO (financial-services background) | Leadership | [La República](https://www.larepublica.co/) |
| 3 | 2025-07-17 | SuperSociedades confirms reorganization (~COP $3.22T, 85.92% creditor approval) | Restructuring | [Infobae](https://www.infobae.com/colombia/2025/07/17/wom-no-desaparecera-superintendencia-de-sociedades-aprobo-su-reorganizacion-e-hizo-varias-aclaraciones-a-los-usuarios/) |
| 4 | 2025 H1 | First EBITDA-positive period in company history (+COP $60B H1) | Financial | [El Tiempo](https://www.eltiempo.com/economia/empresas/wom-lanza-plan-movil-ilimitado-por-29-900-pesos-para-competir-en-colombia-tras-su-salvamento-3478123) |
| 5 | 2025-03-21 | US Chapter 11 plan effective (Delaware, Case 24-10628) | Restructuring | [Kroll WOM](https://cases.ra.kroll.com/wom/Home-Index) |
| 6 | 2025-02-06 | CEO Ramiro Lafarga announces departure | Leadership | [La República](https://www.larepublica.co/) |
| 7 | 2025-01 | SUR Holdings acquires WOM Colombia from Novator Partners | M&A | [DCD](https://www.datacenterdynamics.com/en/news/sur-holdings-acquires-colombias-wom/) |

---

### SECTION 7 — Payment News
| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | Ongoing | ePayco powers WOM bill payment via co-branded portal | 🟢 Single confirmed PSP relationship | [ePayco WOM](https://pagosexpress-wom.epayco.com/) |
| 2 | 2026 | Rebrand from "WOM" → Partners Telecom Colombia / movilPT.co | Domain/checkout branding change | [El Colombiano](https://www.elcolombiano.com/) |

No new PSP partnership or removal announced. ePayco relationship appears established/ongoing (no 🔴 removal found).

---

### SECTION 8 — Checkout Audit
| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Hosted redirect (ePayco) for bill pay; JS-rendered recharge flow | Mixed | Not live-verified — env blocked |
| Guest checkout | ✅ Web recharge: phone number + amount, no registration | Good | [Selectra](https://selectra.com.co/empresas/wom/recargas) |
| Steps to purchase | Recharge COP $1K–$100K, credited <1 min (cards/PSE) | Good | Wallet/cash recharges 24–48h |
| 3DS | Not found | — | Manual check needed |
| Mobile experience | Mi WOM app requires login (OTP); post-update instability reported | Negative | [App Store](https://apps.apple.com/co/app/mi-wom/id1598372244) |
| APM display logic | Cash offline-only; cards/PSE/wallets online | Adequate | [Selectra](https://selectra.com.co/empresas/wom/factura/pagar) |

> ⚠️ MANUAL: Walk recharge + bill-pay checkout via Colombia VPN.

---

### SECTION 9 — PCI DSS
| PCI DSS Level | Card Data Handling | Recommended Yuno Integration | Source |
|---|---|---|---|
| Not found | [INFERENCE — not confirmed] Hosted ePayco redirect likely offloads PCI scope to ePayco | Yuno hosted fields / SDK to keep PCI scope minimal while adding redundancy | n/a |

---

### SECTION 10 — Strategic Insights

**Insight #1: Single-PSP dependency on ePayco**
Evidence: §3 — only ePayco confirmed across bill pay; no redundancy or orchestration found. | Pain Point: A single gateway means any ePayco outage directly halts collections for ~6M subscribers, with no failover to recover declined or interrupted payments. | Yuno Value Prop: Multi-PSP failover + smart routing across local Colombian acquirers, +7% approval uplift, 50% transaction recovery. | Best Case: Rappi (LATAM scale, ms-level monitoring). | Outreach Angle: "Running collections for 6M subscribers through a single gateway leaves revenue exposed the moment that provider has a bad day — orchestration adds the fallback layer without re-engineering."

**Insight #2: Cost-efficiency turnaround under finance-led leadership**
Evidence: §6 — EBITDA turned positive H1 2025; new CEO Gyorgy Zsembery has a financial-services background; company under reorganization plan. | Pain Point: Margin pressure in a Claro/Tigo-Movistar duopoly; every point of approval rate and every bps of MDR matters in a turnaround. | Yuno Value Prop: Routing optimization to the cheapest/best-performing local processor, MDR renegotiation leverage via 450+ providers. | Best Case: Livelo (+5% approval, 50% recovery). | Outreach Angle: "For a CEO with a finance background steering a turnaround, payments is one of the fastest levers — recovered transactions drop straight to EBITDA."

**Insight #3: Duplicate-charge & delayed-crediting complaints**
Evidence: §5 — dedicated duplicate-recharge form, unauthorized-charge forum reports, refund friction (15-business-day PQR). | Pain Point: Manual reconciliation across PSE, wallets, and 20+ cash networks creates duplicate-charge and crediting-delay incidents that drive churn and support cost. | Yuno Value Prop: Real-time monitoring + centralized reconciliation across all rails; proactive alerts before revenue is lost. | Best Case: Rappi (80% less analyst resolution time). | Outreach Angle: "You already run a dedicated duplicate-recharge complaint form — that's the kind of friction a single reconciliation layer across all your rails removes."

**Insight #4: Fragmented domestic rail mix, no orchestration**
Evidence: §3–4 — PSE, cards, Nequi, Daviplata, 20+ cash networks, all managed separately. | Pain Point: No unified view of payment performance across rails; adding/optimizing methods needs engineering. | Yuno Value Prop: One API across every Colombian method, no-code enablement, single performance dashboard. | Best Case: InDrive (fast PSP/APM activation). | Outreach Angle: "With this many rails stitched together, a single orchestration layer turns weeks of integration work into a toggle."

---

### SECTION 11 — Pipeline

**11A. Direct Competitors (Colombian mobile market, CRC Sep 2025)**
| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| Claro Colombia | claro.com.co | Mexico (América Móvil) | 42.1M lines (44%) | Colombia | [El Colombiano](https://www.elcolombiano.com/) |
| Tigo-Movistar (merged) | tigo.com.co | Luxembourg (Millicom) | 41.2M lines (43%) | Colombia | [BNamericas](https://www.bnamericas.com/) |
| Virgin Mobile Colombia | virginmobile.co | MVNO | 3.2M lines | Colombia | [El Colombiano](https://www.elcolombiano.com/) |
| Móvil Éxito | movilexito.com | Grupo Éxito MVNO | 2.2M lines | Colombia | [El Colombiano](https://www.elcolombiano.com/) |
| ETB | etb.com | Bogotá | 227K lines | Colombia | [El Colombiano](https://www.elcolombiano.com/) |

**11B. Industry Peers (LATAM challenger telcos / MVNOs)**
| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| WOM Chile | wom.cl | Mobile | Chile | Same brand origin, separate owner | [df.cl](https://www.df.cl/) |
| Entel | entel.cl | Mobile | Chile, Peru | Challenger telco | [Crunchbase](https://www.crunchbase.com/) |
| VTR Móvil | vtr.com | Mobile | Chile | Challenger | Not found |
| Virgin Mobile LATAM | virginmobile.com | MVNO | Multi-LATAM | Asset-light challenger | Not found |

**11C. Adopting Orchestration:** No public evidence found among WOM Colombia or listed peers.

**11D. Scoring (WOM Colombia)**
| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | 0 | ❌ Single-country (Colombia) |
| Multiple PSPs | 0 | ❌ Single confirmed (ePayco) |
| Recent expansion (24 mo.) | +2 | ✅ Ownership change, new CEO, 5G rollout |
| Public payment issues | +2 | ✅ Duplicate charges, refund friction |
| Funding >$10M | +2 | ✅ SUR Holdings injection >COP $400B |
| LATAM/APAC/MENA traffic | +2 | ✅ Colombia (LATAM) |
| No orchestrator | +2 | ✅ None found |
| Payment job postings | 0 | None found |
| Public RFP | 0 | None found |
| **Total** | **10** | 🟡 Medium |

**Top Pipeline (this account + adjacent):**
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | WOM Colombia / PTC | Target | Colombia | 10 | 🟡 Medium | Single PSP + turnaround cost mode |
| 2 | ETB | Peer telco | Colombia | n/a | Watch | State-owned, fragmented stack [INFERENCE] |
| 3 | Virgin Mobile Colombia | Peer MVNO | Colombia | n/a | Watch | Asset-light, recharge-heavy [INFERENCE] |

Pipeline summary: 1 primary target (Medium), constrained by single-country footprint and reorganization-limited procurement. Strongest vertical: Colombian challenger telcos with recharge/bill-pay-heavy single-PSP stacks.

---

### SECTION 12 — Business Case
| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| Not found (WOM Colombia-specific; 2024 net loss ~COP $1.3T, EBITDA +COP $60B H1 2025) — [Infobae](https://www.infobae.com/colombia/2025/07/17/wom-no-desaparecera-superintendencia-de-sociedades-aprobo-su-reorganizacion-e-hizo-varias-aclaraciones-a-los-usuarios/) | [INFERENCE] Low-ticket (recharges COP $1K–$100K) | High volume — ~6.4M subscribers paying recharges/bills monthly [CRC] | COP | Colombia (single market) |

---

### SECTION 13 — Outreach
*(Verified findings only. Entity addressed as Partners Telecom Colombia. No unconfirmed APM claims.)*

```
--- LINKEDIN MESSAGE ---
Hi [First Name] — congrats on the turnaround. Going EBITDA-positive in H1 2025 while still inside a reorganization is a genuinely hard thing to pull off.

One area I'd love to compare notes on: payments. From the outside it looks like collections for your ~6M subscribers run through a single gateway, with no failover layer if that provider has a bad day. We built Yuno precisely for that — multi-PSP redundancy and smart routing across local Colombian acquirers (PSE, cards, wallets) through one API, no re-engineering.

In a turnaround, the math is simple: recovered transactions drop straight to EBITDA. We've delivered +5% approval and 50% recovery for Livelo, and for Rappi we cut payment-analyst resolution time by 80% with real-time monitoring.

Worth 20 minutes next week to walk through where the quick wins would be? Open Tuesday or Thursday.

— German, Yuno

--- COLD EMAIL ---
Subject: Recovered payments → straight to EBITDA at Partners Telecom

Hi [First Name],

Congrats on turning EBITDA-positive in H1 — impressive while still executing the reorganization.

A quick outside observation on payments: collections for ~6M subscribers appear to run through a single gateway, with no fallback if it goes down. You also operate a dedicated duplicate-recharge complaint form, which usually signals reconciliation friction across the many rails you support (PSE, Nequi, Daviplata, cards, cash networks).

That's exactly what Yuno solves. We're a payment orchestrator: one API → 1,000+ payment methods, 450+ processors and 50+ fraud tools. The relevant levers for a turnaround:

• Smart routing across local Colombian acquirers → +7% approval uplift on average
• Multi-PSP failover so a single outage never stops collections
• 50% recovery on soft declines, plus one reconciliation view across every rail

Proof points: Livelo (+5% approval, 50% recovery), Rappi (80% less payment-analyst resolution time), InDrive (10 LATAM markets live in under 8 months).

In a margin-constrained turnaround, every recovered transaction is incremental EBITDA. Worth 20 minutes next week to size the opportunity? I have Tuesday or Thursday open.

— German
Yuno
```

---

### APPENDIX — Source URLs
```
[S1] https://www.similarweb.com/website/wom.co/
[S2] https://www.supersociedades.gov.co/noticias-supersociedades/-/asset_publisher/atwl/content/superintendencia-de-sociedades-confirma-el-acuerdo-de-reorganizaci%C3%B3n-de-partners-telecom-colombia-s.a.s.
[S3] https://cases.ra.kroll.com/wom/Home-Index
[S4] https://www.datacenterdynamics.com/en/news/sur-holdings-acquires-colombias-wom/
[S5] https://www.eltiempo.com/economia/empresas/wom-colombia-es-adquirida-por-sur-holdings-para-garantizar-su-crecimiento-en-el-pais-3417639
[S6] https://www.infobae.com/colombia/2025/07/17/wom-no-desaparecera-superintendencia-de-sociedades-aprobo-su-reorganizacion-e-hizo-varias-aclaraciones-a-los-usuarios/
[S7] https://pagosexpress-wom.epayco.com/
[S8] https://www.scribd.com/document/775166415/Paga-tus-facturas-WOM-con-ePayco-facil-y-seguro
[S9] https://selectra.com.co/empresas/wom/factura/pagar
[S10] https://selectra.com.co/empresas/wom/recargas
[S11] https://ayuda.nequi.com.co/hc/es/articles/33954890040973
[S12] https://www.wom.co/form/recharge/duplicate
[S13] https://www.laneros.com/temas/wom-colombia-foro-oficial.242165/page-1193
[S14] https://apps.apple.com/co/app/mi-wom/id1598372244
[S15] https://www.eltiempo.com/economia/empresas/wom-lanza-plan-movil-ilimitado-por-29-900-pesos-para-competir-en-colombia-tras-su-salvamento-3478123
[S16] https://www.larepublica.co/empresas/wom-colombia-fue-adquirida-por-sur-holdings-y-continuara-operando-en-el-pais-4037018
[S17] https://www.hklaw.com/en/news/pressreleases/2025/07/holland-knight-advises-partners-telecom-colombia-in-reorganization
```
