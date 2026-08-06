# Slide "Top 20 markets" para Suno (adaptada del deck Anthropic) — contenido final (2026-08-06)

Título: "Stripe does the US and EU very well. Yuno fills the gaps and reinforces those markets."

Columnas: # | Country | Currency live? | $ at stake/yr (est.) | Dominant play | Archetype

| # | Country | Currency live? | $ at stake/yr (est.) | Dominant play | Archetype |
|---|---|---|---|---|---|
| 1 | United States | USD ✓ | $3-5M | Network tokens + account updater + retries; PayPal and Venmo on web | Mature |
| 2 | Brazil | BRL ✓ | $3-5M | Pix Automatico (recurring) + local acquiring + installments | Full-stack |
| 3 | Germany | EUR ✓ | $1.5-3M | PayPal + SEPA DD as recurring rails; SCA tuning | Mature |
| 4 | Russia | RUB ✗ | n/a today | No supported rails (sanctions; RUB not billable) | Not addressable |
| 5 | Indonesia | IDR ✓ | $1.5-3M | QRIS + wallets (OVO, DANA, GoPay) + local cards | Full-stack |
| 6 | India | INR ✓ | $1.5-3M | UPI Autopay mandates on live UPI + RuPay/local card routing | Full-stack |
| 7 | United Kingdom | GBP ✓ | $0.7-1.5M | Cards + Open Banking; retry and token optimization | Mature |
| 8 | Japan | JPY ✓ | $1.5-3M | PayPay + Konbini for acquisition; renewal optimization | Mature |
| 9 | France | EUR ✓ | $0.7-1.5M | Cartes Bancaires domestic routing + PayPal + SEPA DD | Mature |
| 10 | Italy | EUR ✓ | $0.3-0.7M | PayPal + PostePay + SEPA DD | Mature |
| 11 | Republic of Korea | KRW ✓ | $0.7-1.5M | Recurring tokens on live KakaoPay/NaverPay + Toss, Samsung Pay | APM-led |
| 12 | Spain | EUR ✓ | $0.3-0.7M | Bizum + SCA/retry tuning | Mature |
| 13 | Canada | CAD ✓ | $0.3-0.7M | Cards + PayPal; retry optimization | Mature |
| 14 | Turkey | TRY ✓ | $0.7-1.5M | TROY domestic scheme + installments + FX-aware local acquiring | Full-stack |
| 15 | Mexico | MXN ✓ | $0.7-1.5M | Local debit acquiring + SPEI; OXXO for acquisition only | Full-stack |
| 16 | Thailand | THB ✓ | $0.3-0.7M | PromptPay + TrueMoney + local cards | APM-led |
| 17 | Poland | PLN ✓ | $0.3-0.7M | BLIK for acquisition + card retries for renewals | Mature |
| 18 | Ukraine | UAH ✓ | $0.3-0.7M | Local card routing + Apple/Google Pay tokens | Mature |
| 19 | Netherlands | EUR ✓ | $0.3-0.7M | iDEAL first payment, SEPA DD renewals | Mature |
| 20 | Vietnam | VND ✗ | Unlock pending | Enable VND billing first; then MoMo + VietQR + local cards | Full-stack |
| | PORTFOLIO TOTAL | 17 currencies live | **$17-29M/yr** | | |

Panel derecho 1 (PORTFOLIO TOTAL):
- "$17-29M/yr" at stake across the portfolio
- "80%+" of traffic outside the US
- "17" billing currencies already live

Panel derecho 2 (CONCENTRATION):
- TOP 5: "~38%" of traffic (US, RU, BR, DE, JP; SimilarWeb-verified)
- LONG TAIL: "60%+" spread across 100+ countries (the orchestration case)

Panel derecho 3 (ARCHETYPE SPLIT, est.):
- Mature: 11 markets, ~50-55% of value (led by the US)
- Full-stack: 6 markets, ~40% of value (BR, IN, ID, TR, MX, VN)
- APM-led: 2 markets, ~5-10% of value (KR, TH)

Footnote: "Illustrative allocation of the $17-29M/yr portfolio estimate (see decision frame). Traffic shares verified for top 5 (SimilarWeb, Jun 2026); remaining market weights to validate in the data sprint. Recurring-capable rails noted; acquisition-only methods (OXXO, Konbini, BLIK) convert but do not renew on their own. Russia excluded from totals."

Decisiones: Rusia visible pero en gris y fuera de totales (es su tráfico #2, mostrarlo da credibilidad; monetizarlo no es viable). Vietnam con "unlock pending" porque VND no está entre las 17 monedas vivas de Suno. Bandas de $ en vez de cifras falso-precisas; suman ~$26M, consistente con el total $17-29M del decision frame.
