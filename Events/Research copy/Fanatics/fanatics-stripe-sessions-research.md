# FANATICS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Fanatics
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5e/Fanatics_company_logo.svg
Nombre merchant: Fanatics

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Payment Stack
Tittle_Pain Point_2: World Cup Checkout Risk
Tittle_Pain Point_3: Sportsbook Outage Exposure
Tittle_Pain Point_4: Cross-Border Friction
Tittle_Pain Point_5: Collectibles Surcharge Leak

Desc_Pain Point_1: Commerce on Fiserv, Sportsbook on Paysafe, Collect on its own stack. Three divisions, three disconnected payment rails, zero unified visibility across $9B+.
Desc_Pain Point_2: Running all 104 World Cup 2026 stadium retail locations across US, Canada, Mexico. POS must handle USD, CAD, MXN plus tourist currencies at peak volume.
Desc_Pain Point_3: May 2025 fiber cut knocked Sportsbook offline across NY, NJ, CT, PA. Single-provider dependency cost $1M in FanCash refunds and triggered regulatory scrutiny.
Desc_Pain Point_4: Non-US revenue growing 40-50% YoY but checkout lacks local APMs. UK, EU, Australia, Middle East shoppers see card-only; no iDEAL, Afterpay AU, or Mada.
Desc_Pain Point_5: Collect charges 2.9% surcharge on card and Apple Pay up to $1M. Buyers absorb the fee, depressing conversion on high-value collectible auctions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Fiserv (Carat)
PSP_2: Paysafe
PSP_3: PayPal
PSP_4: Apple Pay / Google Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: BLIK
Local_M_6: Mada
Local_M_7: Konbini
Local_M_8: Afterpay AU
Local_M_9: SPEI
Local_M_10: Interac

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every transaction across Fiserv, Paysafe, PayPal by BIN, issuer, and geography. On $13B target revenue in 2026, a 3% auth uplift recovers $390M+ in annual revenue that currently falls through processor blind spots.
Desc_Yuno_Cap2: Automatic cascade eliminates single-point failures like the May 2025 outage. When one processor drops, Yuno reroutes in milliseconds, protecting bets, merchandise, and collectible auctions. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates the APMs Fanatics needs for global scale: OXXO and SPEI for Mexico World Cup venues, Pix for Brazil fans, iDEAL for Netherlands, Interac for Canadian sportsbook launch, Mada for Middle East expansion. One API, 1,000+ payment methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: One dashboard unifying Commerce (Fiserv), Sportsbook (Paysafe), and Collect into a single reconciliation layer. Real-time approval monitoring across three units, centralized FX for 20+ currencies, NOVA fraud engine with 75% fewer false positives.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Fanatics at a glance:**
- Three divisions: Commerce ($6.2B), Collectibles ($1.6B, +40% YoY), Betting & Gaming (~$2B)
- Revenue: $8.1B in 2024, $9B+ in 2025, targeting $13B in 2026
- Valuation: ~$33.5B (Fidelity implied, Nov 2025)
- CEO/Founder: Michael Rubin. Commerce CEO: Andrew Low Ah Kee. CTO: Matthias Spycher (Commerce), Ramana Thumu (parent co, ex-PayPal/eBay)
- IPO: "Not in the cards right now" per Rubin at NRF 2026, but widely expected to provide liquidity for Clearlake, Silver Lake, LionTree
- International: Non-US growing 40-50% YoY; targeting mid-20s% of total revenue by 2027
- Sportsbook: 22 US states, 7-8% market share, Canada expansion imminent, $1B FanCash distribution in 2026
- FIFA World Cup 2026: Exclusive on-site retail licensee for all 104 matches across US, Canada, Mexico

**Confirmed PSPs:**
- Fiserv (Carat): primary commerce processor (confirmed via Fiserv client references)
- Paysafe: sportsbook payment platform (confirmed via Business Wire Nov 2023 press release)
- PayPal: accepted on commerce checkout
- Zip: accepted as BNPL on commerce
- Apple Pay / Google Pay: accepted on commerce and Collect
- FanCash Rewards Card: proprietary stored-value card
- Collect: credit cards with 2.9% surcharge, ACH bank transfers (no surcharge)
- Sportsbook: debit cards, ACH, PayPal, Venmo, Apple Pay (no credit cards)
- No payment orchestrator detected

**Top Market Gap Analysis:**

MARKET 1: United States (primary, all three divisions)
  Accepted: Visa/MC/Amex/Discover, PayPal, Venmo (sportsbook), Apple Pay, Google Pay, Zip, ACH
  Missing: Cash App Pay (57M+ users skewing young sports fan demo)
  Note: Sportsbook does not accept credit cards in any state

MARKET 2: Mexico (World Cup 2026 retail, 16 venues)
  Accepted: Card networks only (in-venue POS)
  Missing: OXXO, SPEI, CoDi, Mercado Pago
  Note: 70%+ of Mexican adults lack credit cards; OXXO vouchers dominate offline payments

MARKET 3: United Kingdom (fanatics.co.uk, growing football merchandise)
  Accepted: Cards, PayPal
  Missing: Open Banking (Pay by Bank), Klarna UK
  Note: UK is largest international commerce market for Fanatics

MARKET 4: Canada (sportsbook launch imminent, commerce active)
  Accepted: Cards, PayPal
  Missing: Interac Online, Interac e-Transfer
  Note: Interac dominates Canadian digital payments; critical for sportsbook deposits

MARKET 5: Australia & New Zealand (fastest-growing int'l markets)
  Accepted: Cards, PayPal
  Missing: Afterpay AU/NZ (originated in AU, huge adoption), POLi
  Note: Afterpay has 3.6M+ AU users; natural fit for sports merchandise

**Sportsbook Outage History:**
- May 2025: Major outage from fiber optic cable cut. New York, NJ, CT, PA users locked out of accounts, bets, and withdrawals. Fanatics paid $1M in FanCash compensation. Triggered public backlash and regulatory attention.
- BBB complaints document sudden account closures with balances of $600+, no prior warning, no payout of winnings.

**Key Meeting Angles:**
1. **World Cup urgency** | 104 stadium retail locations across 3 countries need multi-currency, multi-APM POS by June 2026
2. **Three stacks, one problem** | Commerce, Sportsbook, and Collect each run separate PSPs; no unified view of $13B in transactions
3. **Canada sportsbook launch** | Interac is table-stakes for Canadian deposits; Paysafe alone won't cover it
4. **CTO has fintech DNA** | Ramana Thumu (ex-PayPal, ex-eBay) understands orchestration; Matthias Spycher leads Commerce tech
5. **Collectibles conversion** | Removing the 2.9% card surcharge via lower-cost routing could lift auction conversion significantly
6. **IPO readiness** | Payment infrastructure consolidation is a narrative investors and underwriters will scrutinize
7. **$13B target** | 2026 revenue goal demands higher auth rates; even 1% improvement = $130M in recovered revenue

**Sources:**
- [Fanatics Payment Guide](https://www.fanatics.com/play-hard-pay-smart-payment-guide/ch-4891)
- [Fanatics Payment FAQ](https://www.fanatics.com/what-payment-methods-do-you-accept/ch-2689)
- [Fanatics Collect Payment Methods](https://help.fanaticscollect.com/hc/en-us/articles/20108383117085-Accepted-payment-methods)
- [Fanatics Commerce Leadership](https://www.fanaticsinc.com/commerce-leadership)
- [Fanatics Inc Leadership](https://www.fanaticsinc.com/leadership)
- [Paysafe x Fanatics Sportsbook Press Release](https://www.businesswire.com/news/home/20231113600099/en/Paysafe-Provides-Fanatics-Sportsbook-With-All-Inclusive-Payment-Solution)
- [Fiserv Carat Platform](https://www.carat.fiserv.com/en-us/)
- [Sportico: Fanatics Revenue $8.1B](https://www.sportico.com/business/finance/2025/fanatics-2024-sales-rise-1234824898/)
- [Sacra: Fanatics Revenue & Valuation](https://sacra.com/c/fanatics/)
- [Fanatics FIFA World Cup 2026 PR](https://investor.fanatics.com/news/news-details/2025/Fanatics-to-Exclusively-Operate-FIFA-World-Cup-2026-Stadium-and-Fan-Festival-Retail-Experiences-2025-N3517G-gOY/default.aspx)
- [CNBC: Fanatics FIFA Deal](https://www.cnbc.com/2025/12/04/2026-fifa-world-cup-fanatics-merchandising-deal.html)
- [Fanatics Sportsbook Outage $1M Payout](https://sccgmanagement.com/sccg-news/2025/5/1/fanatics-sportsbook-outage-triggers-backlash-and-1m-payout/)
- [Fanatics BBB Complaints](https://www.bbb.org/us/fl/jacksonville/profile/online-gaming/fanatics-betting-and-gaming-0403-236024747/complaints)
- [Yogonet: Fanatics 2026 Strategy](https://www.yogonet.com/international/news/2025/09/26/115547-fanatics-2026-strategy-sportsbook-expansion-stadium-retail-and-digital-innovation)
- [Fanatics Canada Sportsbook Expansion](https://www.fanaticsinc.com/news/canadian-gaming-business-fanatics-sportsbook-intends-to-make-canada-part-of-international-expansion)
- [Fanatics Middle East Expansion](https://www.fanaticsinc.com/press-releases/fanatics-continues-global-development-with-expansion-into-middle-east)
- [Fanatics Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Fanatics_company_logo.svg)
- [Deadspin: Betting 40% Revenue by 2027](https://deadspin.com/legal-betting/sports-betting-could-become-40-of-fanatics-revenue-by-2027/)
- [Michael Rubin NRF 2026](https://awfulannouncing.com/lifestyle/michael-rubin-fanatics-ipo-public.html)
