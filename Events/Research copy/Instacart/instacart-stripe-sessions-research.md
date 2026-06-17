# INSTACART | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Instacart
═══════════════════════════════════════

Logo: https://c-p.rmcdn.net/5fad7c666514100070f6c76e/4102165/upload-6958c6b6-b750-4fdb-b71a-e18b6f781ed9.svg
Nombre merchant: Instacart

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single Dependency
Tittle_Pain Point_2: International Payment Gap
Tittle_Pain Point_3: Auth Rate Optimization
Tittle_Pain Point_4: Checkout Friction
Tittle_Pain Point_5: Reconciliation Complexity

Desc_Pain Point_1: Stripe processes 100% of $37.2B GTV via Stripe Connect. Zero failover: any Stripe disruption blocks 338.8M annual orders across the marketplace.
Desc_Pain Point_2: Instaleap acquisition adds ~30 countries in LATAM, Europe, Middle East. Current Stripe stack has no local acquiring or APMs for these new markets.
Desc_Pain Point_3: 338.8M orders at $110 avg basket. 1% auth improvement on $37.2B GTV recovers $372M in grocery orders. No multi acquirer routing by BIN or issuer.
Desc_Pain Point_4: No PayPal, Venmo, or Cash App accepted. Only cards, Apple Pay, Google Pay, EBT, Klarna. Millions of US households prefer wallets not supported.
Desc_Pain Point_5: Stripe, Klarna, Chase co brand, EBT/SNAP across 1,500+ retailers. Settlement for marketplace splits, alcohol compliance, and tips compounds ops.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Klarna
PSP_3: Chase (co brand issuer)
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Venmo
Local_M_3: Cash App Pay
Local_M_4: Pix
Local_M_5: OXXO
Local_M_6: PSE
Local_M_7: Nequi
Local_M_8: iDEAL
Local_M_9: BLIK
Local_M_10: Boleto

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each of Instacart's 338.8M annual orders to the optimal acquirer by card BIN, issuer, and geography. With $37.2B GTV and 9 orders per second, even 3% auth uplift translates to $1.1B+ in recovered grocery transactions. ML driven, real time, per transaction.
Desc_Yuno_Cap2: Break Stripe single acquirer dependency. When Stripe declines or experiences latency, Yuno cascades to the next best processor in milliseconds. Up to 50% recovery on soft declines, protecting perishable grocery orders where retry windows are measured in minutes.
Desc_Yuno_Cap3: Unlock Instaleap's 30 new countries with local APMs: Pix in Brazil, OXXO in Mexico, PSE and Nequi in Colombia, iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ methods. Deploy per market in weeks, not quarters of custom Stripe integrations.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Klarna, Chase co brand, and EBT/SNAP flows across 1,500+ retail partners. Real time approval monitoring, centralized reconciliation for marketplace splits and alcohol compliance. Up to 90% reconciliation reduction.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Instacart at a glance:**
- Legal entity: Maplebear Inc. (NASDAQ: CART). IPO September 2023
- FY2024 Revenue: $3.38B (up 11% YoY). FY2025 Revenue: $3.74B (up 11% YoY)
- FY2024 GTV: $33.5B, 294M orders. FY2025 GTV: $37.2B (up 11%), 338.8M orders (up 15%)
- FY2025 GAAP Net Income: $447M. Adjusted EBITDA: $1.09B (up 23%)
- Q4 2025: strongest GTV growth in 3 years (14% YoY), orders up 16%
- ~14.9M monthly active customers. 9 orders completed per second
- Available in US and Canada, reaching 98%+ of North American households
- 1,500+ retail partners, 80,000+ stores
- CEO: Fidji Simo. CTO: Anirban Kundu (ex Uber Delivery). CPO: Daniel Danker. Chief Architect: JJ Zhuang
- Instaleap acquisition (April 2026): adds ~30 countries across LATAM, Europe, Middle East with ~100 retailer relationships
- Chase partnership: Instacart Mastercard co brand credit card + Instacart+ benefits on Chase cards
- $3B+ in stock buybacks authorized

**Confirmed PSPs:**
- Stripe: sole payment processor via Stripe Connect since 2012. Processes 100% of $37.2B GTV
- Stripe Payments: powers cards, Apple Pay, Google Pay acceptance
- Stripe Data Pipeline: feeds Instacart's AI analytics on payment performance
- Stripe Network Tokens + Card Account Updater: used for card lifecycle management
- Klarna: BNPL partner since 2022 (Pay in 4 interest free)
- Chase / Mastercard: co brand credit card issuer (not acquirer)
- EBT/SNAP: government benefit card acceptance at participating stores
- No payment orchestrator detected
- Actively hiring Senior Software Engineer II, Payments (processes $100M+ daily, focus on auth optimization, cost optimization, new payment methods)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~95% of GTV)
  Accepted: Visa/MC/Amex/Discover, Apple Pay, Google Pay, Klarna, EBT/SNAP, Instacart Mastercard
  Missing: PayPal, Venmo, Cash App Pay, ACH
  Note: Instacart explicitly does not accept PayPal, Venmo, or Cash App. PayPal has 400M+ accounts, Venmo 90M+ users. Significant checkout friction for wallet preferring customers.

MARKET 2: Canada (~5% of GTV)
  Accepted: Visa/MC/Amex, Apple Pay, Google Pay
  Missing: Interac Online, PayPal (Canada)
  Note: Interac is the dominant debit network in Canada. Without it, debit card users face cross border routing fees.

MARKET 3: Latin America (via Instaleap, ~30 countries coming)
  Accepted: Not yet launched (Instaleap handles separately)
  Missing: Pix, Boleto (Brazil), OXXO, SPEI (Mexico), PSE, Nequi (Colombia), Rapipago (Argentina)
  Note: Instaleap powers 100M+ transactions for Cencosud, SPAR, others. Current payment infra is fragmented across local providers.

MARKET 4: Europe (via Instaleap)
  Accepted: Not yet launched (Instaleap handles separately)
  Missing: iDEAL (NL), BLIK (PL), Sofort (DE), Open Banking (UK), Carte Bancaire (FR)
  Note: Instaleap serves Continente and Jeronimo Martins in Portugal/Europe. Local APMs critical for grocery e commerce conversion.

MARKET 5: Middle East (via Instaleap)
  Accepted: Not yet launched (Instaleap handles separately)
  Missing: Mada (Saudi), Fawry (Egypt), KNet (Kuwait)
  Note: Instaleap serves Lulu in the Middle East. Cash on delivery still common; digital payment localization is essential.

**Payment issues documented:**
- Instacart Zendesk help article: "Why is my purchase being declined?" documents systematic decline issues
- Users report debit cards declined despite sufficient funds; pre authorization holds exceeding order total
- Shoppers report Instacart payment card declined at stores, requiring out of pocket payment
- No PayPal/Venmo acceptance is a documented user complaint
- Payment method limitations restrict the addressable market (wallet only households)
- Job posting confirms focus on "optimizing payment costs" and "improving payment success rates"

**Key meeting angles:**
1. **$37.2B GTV, one processor** | 100% of transaction volume flows through Stripe with zero failover. A single Stripe incident could freeze 9 orders per second.
2. **Instaleap = 30 new countries overnight** | Acquisition brings LATAM, Europe, and Middle East markets. Stripe alone cannot provide local acquiring and APMs for all 30 countries efficiently.
3. **Payments team actively building** | Hiring Sr SE II Payments focused on auth optimization, cost reduction, and new methods. Yuno accelerates this roadmap by years.
4. **$372M auth recovery opportunity** | 1% improvement on $37.2B GTV. Multi acquirer routing, smart retries, and failover can deliver 3 to 10%.
5. **Grocery = high frequency, time sensitive** | Failed grocery payments cannot wait for retry. Perishable orders need instant failover or the customer goes to a competitor.
6. **Wallet gap** | No PayPal (400M+ users), no Venmo (90M+ users), no Cash App. Yuno enables wallet acceptance without rebuilding checkout.
7. **Chase partnership creates co brand complexity** | Instacart Mastercard + Klarna + EBT + Stripe. Yuno's unified dashboard simplifies multi provider reconciliation.

**Sources:**
- [Stripe x Instacart Case Study](https://stripe.com/customers/instacart)
- [Instacart FY2024 Results (Grocery Dive)](https://www.grocerydive.com/news/instacart-reports-mixed-fourth-quarter-results/740976/)
- [Instacart FY2025 Results (Progressive Grocer)](https://progressivegrocer.com/instacart-ends-2025-high-note)
- [Instacart FY2025 Shareholder Letter](https://investors.instacart.com/static-files/8a93ec81-cbef-4c62-9817-9ed532089aa3)
- [Instacart Revenue (Business of Apps)](https://www.businessofapps.com/data/instacart-statistics/)
- [Instacart Statistics (ElectroIQ)](https://electroiq.com/stats/instacart-statistics/)
- [Instacart Statistics (Zippia)](https://www.zippia.com/advice/instacart-statistics/)
- [Instacart Statistics (ExpandedRamblings)](https://expandedramblings.com/index.php/instacart-statistics-facts/)
- [Instacart Instaleap Acquisition (TechCrunch)](https://techcrunch.com/2026/04/14/instacart-acquires-instaleap-to-expand-its-enterprise-platform-internationally/)
- [Instacart Instaleap Acquisition (Press Release)](https://investors.instacart.com/news-releases/news-release-details/instacart-acquires-instaleap-accelerate-global-expansion-its)
- [Instacart Instaleap (Bloomberg)](https://www.bloomberg.com/news/articles/2026-04-14/instacart-buys-grocery-tech-firm-instaleap-in-international-push)
- [Instacart Canada Expansion](https://www.instacart.com/company/updates/expanding-our-footprint-to-reach-90-of-canadian-households/)
- [Instacart International Plans (Grocery Dive)](https://www.grocerydive.com/news/instacart-plans-to-expand-globally/600827/)
- [Instacart x Klarna Partnership](https://www.instacart.com/company/instacart-retail/instacart-and-klarna-partner-to-offer-consumers-more-flexible-ways-to-pay)
- [Instacart x Chase Mastercard](https://salestechstar.com/sales-engagement/instacart-and-chase-launch-new-instacart-mastercard-credit-card-unlocking-new-rewards/)
- [Chase Co Brand Instacart+ Benefits](https://www.nerdwallet.com/credit-cards/news/chase-adds-instacart-benefits-to-some-credit-cards)
- [Instacart Payment Methods (Docs)](https://docs.instacart.com/storefront/learn_about_your_storefront/payments/payment_methods/)
- [Instacart EBT SNAP](https://www.instacart.com/ebt-snap)
- [Instacart Help: Payment Decline](https://instacart-branchapp.zendesk.com/hc/en-us/articles/40049839248923-Why-is-my-purchase-being-declined)
- [Instacart Payment Methods Guide](https://instacartpromocodes.com/instacart-payment-methods-guide/)
- [Instacart Sr SE II Payments Job](https://jobs.generalcatalyst.com/companies/instacart/jobs/51583036-senior-software-engineer-ii-payments)
- [Instacart CTO Appointment](https://www.instacart.com/company/updates/joining-our-table-meet-chief-technology-officer-anirban-kundu)
- [Instacart Leadership Team](https://www.clay.com/dossier/instacart-executives)
- [Instacart Logo Brand Guide](https://heyitsinstacart.com/logo/)
- [Instacart Wikipedia](https://en.wikipedia.org/wiki/Instacart)
