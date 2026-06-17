# VIVENU | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Vivenu
=======================================

Logo: https://seeklogo.com/images/V/vivenu-logo-523755-seeklogo.com.png
Nombre merchant: Vivenu

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single PSP Lock-in
Tittle_Pain Point_2: Global Checkout Gaps
Tittle_Pain Point_3: Peak Sale Downtime Risk
Tittle_Pain Point_4: Resale Payment Friction
Tittle_Pain Point_5: White Label Pay Limits

Desc_Pain Point_1: Vivenu Managed Payments runs exclusively on Stripe. With 1,000+ clients across 50+ countries, a single processor means no failover, no routing optimization, and zero leverage on processing fees at scale.
Desc_Pain Point_2: Operating across 50+ countries but Stripe does not natively support key local methods in growth markets. Fans in Germany (Giropay), Netherlands (iDEAL), Poland (BLIK), Brazil (Pix), and Mexico (OXXO) face card-only checkout.
Desc_Pain Point_3: High-demand on-sales (Grammy Awards, HYROX, StubHub distribution) create extreme volume spikes. Single-processor architecture risks timeout failures during peak loads with no cascade path to a backup PSP.
Desc_Pain Point_4: New StubHub Open Distribution partnership (March 2026) routes 125M fans into vivenu checkout. Cross-border resale transactions across 200+ countries need multi-currency, multi-method support that Stripe alone cannot cover.
Desc_Pain Point_5: As a white-label platform, vivenu's "Own Payments" option supports 8 gateways (Stripe, PayPal, Adyen, Worldline, Shift4, authorize.net, Wallee, Card Connect) but clients must integrate each separately with no unified orchestration layer.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Managed Payments, primary)
PSP_2: PayPal
PSP_3: Adyen (Own Payments option)
PSP_4: Unzer (partner since 2025)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Giropay
Local_M_8: Konbini
Local_M_9: Boleto
Local_M_10: Mada

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every ticket transaction across Stripe, Adyen, PayPal, and Unzer by BIN, issuer, and geography. On $15M+ in annual revenue growing across 50+ countries, a 3-10% auth uplift translates directly into recovered ticket sales that currently fail at Stripe-only checkout.
Desc_Yuno_Cap2: Automatic cascade eliminates single-point-of-failure risk during high-demand on-sales for Grammy Awards, HYROX, and StubHub distribution. When Stripe drops under peak load, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Unlocks the APMs vivenu needs for global ticketing: Pix and Boleto for Brazil, OXXO and SPEI for Mexico, iDEAL for Netherlands, BLIK for Poland, Giropay for Germany, Konbini for Japan, Mada for Middle East. One API, 1,000+ payment methods, zero per-market engineering.
Desc_Yuno_Cap4: One dashboard unifying Stripe Managed Payments, Adyen, PayPal, and Unzer into a single reconciliation layer for 1,000+ clients. Real-time approval monitoring across all white-label deployments, NOVA fraud engine with 75% fewer false positives protecting high-value ticket on-sales.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Vivenu at a glance:**
- White-label ticketing platform founded in 2018, headquartered in Dusseldorf, Germany
- 1,000+ clients across 50+ countries, 500,000+ events per year, 99.99% API uptime
- Estimated annual revenue: ~$15M (as of mid-2025)
- Total funding: $66.6M over 3 rounds (Series B: $50M led by Activant Capital, Nov 2021)
- Investors: Activant Capital, Balderton Capital, Redalpine, Hedosophia, Aurum Fund (San Francisco 49ers family fund)
- Offices: Dusseldorf (HQ), New York, Tampa, Hamburg, Darmstadt
- ~160 employees across 5 continents
- CEO/Co-Founder: Simon Hennes (Forbes 30 Under 30 Europe Technology)
- CTO/Co-Founder: Jens Teichert
- Co-Founder: Simon Weber
- CFO: Tim Mundhenke
- EVP Global Sales: Adam Prowler
- General Counsel: Dirk Neumann

**Key clients:**
- Grammy Awards, Golden Globes, HYROX, Stanford Athletics, Schalke 04
- The Basketball League (TBL), ABA, WABA (250+ teams)
- ECHL (Preferred Primary Ticketing Partner)
- FISU World University Games
- America East Conference

**StubHub Partnership (March 2026):**
- Open Distribution partnership announced March 26, 2026
- Organizers on vivenu can activate StubHub as additional sales channel from dashboard
- Access to StubHub's 125M+ fans across 200+ countries
- Free to use, no exclusive commitment required
- Real-time inventory sync via Distribution API

**Confirmed PSPs:**
- Stripe: Primary processor via "Managed Payments" (including POS card readers)
- PayPal: Accepted as payment method
- Adyen: Available via "Own Payments" integration
- Worldline (Saferpay): Available via "Own Payments"
- Shift4: Available via "Own Payments"
- authorize.net: Available via "Own Payments"
- Wallee: Available via "Own Payments"
- Card Connect: Available via "Own Payments"
- Unzer: Joined as official payment partner (2025)
- No payment orchestrator detected

**Top Market Gap Analysis:**

MARKET 1: Germany (headquarters, major client base)
  Accepted: Cards via Stripe, PayPal
  Missing: Giropay, SOFORT/Klarna, EPS
  Note: Home market with significant event volume; local methods critical for conversion

MARKET 2: United States (expansion market, sports leagues)
  Accepted: Cards, Apple Pay, Google Pay via Stripe
  Missing: Cash App Pay, Venmo, ACH
  Note: Growing US presence with TBL, ECHL, Stanford Athletics, America East

MARKET 3: Netherlands / Benelux (European events)
  Accepted: Cards via Stripe
  Missing: iDEAL, Bancontact
  Note: iDEAL accounts for 60%+ of online payments in Netherlands

MARKET 4: Brazil (potential growth via StubHub distribution)
  Accepted: Cards only
  Missing: Pix, Boleto
  Note: Pix has 150M+ users; essential for any Brazilian ticket sales

MARKET 5: Mexico (potential growth via StubHub distribution)
  Accepted: Cards only
  Missing: OXXO, SPEI, CoDi
  Note: 70%+ of Mexican adults lack credit cards

**Key Meeting Angles:**
1. **StubHub scale urgency** | 125M fans across 200+ countries now flowing into vivenu checkout; Stripe alone cannot handle multi-currency, multi-APM demand at that scale
2. **Single PSP dependency** | All Managed Payments run on Stripe with zero failover; one outage during Grammy or HYROX on-sale could cost millions in lost ticket revenue
3. **White-label gap** | 8 payment gateways available via Own Payments but no orchestration layer to unify them; each client integrates separately
4. **CTO is technical co-founder** | Jens Teichert co-founded vivenu and leads engineering; will understand orchestration architecture and API-first approach
5. **Series B growth mandate** | $66.6M raised to fuel global expansion; payment infrastructure must scale across 50+ countries without per-market engineering
6. **German home market** | Even in their home market, checkout lacks Giropay and local BNPL options
7. **Sports vertical depth** | NFL (49ers investor), ECHL, college athletics all need high-volume, peak-demand payment reliability

**Sources:**
- [vivenu Managed Payments Wiki](https://wiki.vivenu.com/payment)
- [vivenu Own Payments Wiki](https://wiki.vivenu.com/payment/op)
- [vivenu Homepage](https://vivenu.com/)
- [vivenu About Page](https://vivenu.com/about)
- [Unzer x vivenu Partnership](https://www.unzer.com/en/news_unzer-wird-offizieller-zahlungsdienstleister-im-vivenu-oekosystem/)
- [StubHub x vivenu Open Distribution (BusinessWire)](https://www.businesswire.com/news/home/20260326154700/en/StubHub-Opens-Direct-Path-from-Primary-Ticketing-to-125-Million-Fans-Expanding-with-vivenu)
- [StubHub x vivenu (TicketNews)](https://www.ticketnews.com/2026/03/stubhub-expands-open-distribution-push-with-vivenu-partnership/)
- [vivenu $50M Series B (Balderton)](https://www.balderton.com/news/vivenu-raises-50m-series-b-to-disrupt-the-ticketing-industry/)
- [vivenu Crunchbase Profile](https://www.crunchbase.com/organization/vivenu)
- [San Francisco 49ers Investment in vivenu](https://vivenu.com/blog/vivenu-partners-with-the-san-francisco-49ers)
- [vivenu Forbes 30 Under 30](https://vivenu.com/blog/forbes-30-under-30)
- [vivenu ECHL Partnership](https://echl.com/news/2022/12/vivenu-named-preferred-primary-ticketing-partner-of-the-echl)
- [vivenu America East Partnership](https://americaeast.com/news/2024/11/14/ae-vivenu.aspx)
- [vivenu Logo (SeekLogo)](https://seeklogo.com/vector-logo/523755/vivenu)
- [vivenu Brandfetch](https://brandfetch.com/vivenu.com)
- [vivenu Leadership (The Org)](https://theorg.com/org/vivenu/teams/ceo-and-executive-team)
- [vivenu CBInsights](https://www.cbinsights.com/company/vivenu)
- [vivenu US Expansion Blog](https://vivenu.com/blog/vivenu-expanding-to-united-states)
- [vivenu Stanford Athletics Partnership](https://vivenu.com/blog/vivenu-to-team-up-with-stanford-athletics-to-transform-ticketing-and-elevate-the-fan-experience)
- [vivenu POS Card Reader Setup](https://wiki.vivenu.com/pos-setup/card-reader)
