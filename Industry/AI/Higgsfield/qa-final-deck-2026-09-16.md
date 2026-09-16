# QA pre-envío: HiggsfieldAI_Yuno_SEPT 2026 (deck final de German)

**Deck revisado:** https://docs.google.com/presentation/d/1LQarKMJTA7qh_sDFT_9CYwc9QP_78GtxpZlgmSb8fRQ/edit
**Fecha:** 2026-09-16 (el deck cambió durante la revisión: 52 → 55 slides; se quitó el gráfico de burbujas de OpenAI y se agregaron 4 slides después de Thank You)
**Método:** lectura completa vía Slides API (2,253 elementos de texto), escaneos automáticos (monedas, em-dashes, tokens del deck de OpenAI, tipos numéricos), diff contra el deck construido el mismo día, y 4 agentes de QA visual sobre renders 1600x900.
**Veredicto:** NO enviar todavía. 8 bloqueantes, ~12 importantes, ~25 menores. Los números del modelo (hero, palancas, 20 países, ranking) están correctos salvo los puntos listados.

## Bloqueantes (números o texto incorrectos, contenido de otra empresa, notas internas visibles)

| # | Slide | Qué está mal | Corrección |
|---|---|---|---|
| B1 | S03 Executive summary | "~$6.1M  MAU" (signo $ sobre usuarios); "~25M/year" sin $; "~$21M/  year" y "~$4M/ year" con espacios | "~6.1M MAU", "~$25M/year", "~$21M/year", "~$4M/year" |
| B2 | S06 Proposed architecture | Texto heredado del deck de OpenAI: "Authorization uplift limited to Adyen's own routing" en las dos columnas; "Local payment methods in all 20 markets" (son 18); "(Stripe → Adyen → Dlocal" sin cerrar; cierre "— Adyen, local PSPs, retries, and LPMs included"; "New integration – single API" | Columna Stripe: "Global card processing (US, EU, Australia) at 95.6% authorization / Link, Klarna, Affirm and Adaptive Pricing stay as they are / Stripe Connect payouts for Higgsfield Earn continue / Fallback if Yuno is ever unavailable / No migration needed: stays as-is". Columna Yuno: "Local payment methods in all 18 markets / Cross-PSP smart retries (Stripe → Adyen → local acquirer) / Local acquiring + domestic scheme routing / Issuer-aware smart routing across 30+ PSPs and local acquirers / Single dashboard for every attempt across every route". Cierre: "Stripe stays live as your safety net. Yuno adds the orchestration layer around it: local PSPs, retries and local methods included." |
| B3 | S11 Methodology bridge | "~$0.11/month" (falta la M); "Across Higgsfield's 20 priority markets" bajo 6.1M MAU | "~$0.11M/month"; "Across the 18 addressable markets (~12M global)" |
| B4 | S16 Revenue comparison | Tarjeta Yuno con cifras de OpenAI: "Cross-PSP retry unlocks full Lever 3 ($110–120M/yr)", "Multi-acquirer routing maximizes Lever 2 ($120–145M/yr)"; viñeta duplicada "No cross-PSP retry (Lever 3 mostly lost)"; "Yuno ARR is ~4x the Adyen-only ARR —" | "Includes Adyen + Stripe + 30 local PSPs per market / Cross-PSP retry unlocks full Lever 3 (~$2.8M/yr) / Multi-acquirer routing maximizes Lever 2 (~$1.3M/yr) / 100% of the addressable opportunity"; cierre "Yuno captures ~4x the second-PSP outcome because orchestration unlocks all three levers, not just partial LPM coverage." |
| B5 | S22 How to read the numbers | Columna "Caveats & positioning language" escrita para el equipo de Yuno: "ask Higgsfield to validate", "should be A/B validated", "(model in appendix files)", "Never state that Higgsfield lacks a method". Falta el caveat de estructura (top 20 / 18 modelados / US baseline / Rusia excluida) | Retitular "CAVEATS" y reescribir en voz cliente: "MAU is triangulated and shown as ranges; to be validated against Higgsfield funnel data" · "Sensitivity (Yuno model): 16M MAU ~$34M/yr; +3.5pp EM uplift ~$58M; +1.0pp ~$15M" · "Conversion uplift anchored on Stripe-published examples; to be A/B validated per market" · "Levers are sized sequentially, not independently" · "Top 20 by traffic, 18 modeled: the US stays on Stripe (upside on its own slide, outside the base case); Russia excluded under sanctions" · "Methods live today: cards (Visa, Mastercard, Amex, JCB), Apple Pay, bank payments; Stripe materials add Link, Klarna, Affirm, Pix, Kakao Pay, Naver Pay, PayCo, WeChat Pay" |
| B6 | S52 a S55 (después de Thank You) | S52 y S53 son el mismo slide duplicado (uno con marco Yuno, otro sin). S54 y S55 usan otra tipografía (título negro, sin regla izquierda). S55 tiene nota interna visible en el pie ("Illustrative mockup in test mode... verify higgsfield.ai/pricing before sending") y banner "You are in testing environment". S54 afirma "THE BRIDGE · BUILT BY YUNO · LIVE" y "Also live: Stripe Proxy" | Decidir si van: si sí, borrar el duplicado, moverlos antes de Thank You (o al appendix), unificar estilo, quitar la nota interna y el banner de test, y confirmar con Producto que el bridge de Stripe Billing y Stripe Proxy están en GA antes de escribir "LIVE" |
| B7 | S05, S06, S08 (x2), S16, S20 | Em-dashes en títulos y cierres (regla del deck: ninguno) | S05 "Stripe alone leaks revenue at four points. A second PSP only fixes one"; S08 "Yuno commits dedicated teams across every region, not just software" y "REGIONAL PRESENCE: Local teams across the Americas, EMEA and APAC: São Paulo · ..."; S20 "...across four regions, not just integration" |
| B8 | S20 BD sprint | Cabeceras de columna del deck de OpenAI ("CHINA / SINGAPORE", "ASIA-PACIFIC") no corresponden al contenido (India/Pakistán/Indonesia/Vietnam bajo "ASIA-PACIFIC"; Corea/Japón/China bajo "CHINA / SINGAPORE"); logos de GrabPay, Touch 'n Go, GCash, Maya, PSE, Nequi, Meeza, M-Pesa (wallets fuera del top 20) | Cabeceras: LATIN AMERICA · SOUTH & SE ASIA · EAST ASIA · EUROPE / MENA; logos alineados con los wallets nombrados (UPI/Paytm/PhonePe, QRIS/GoPay, MoMo, Kakao Pay/PayPay/Alipay, PayPal/iDEAL/Bizum, Tabby) |

## Importantes (el cliente lo nota)

| # | Slide | Qué está mal | Corrección |
|---|---|---|---|
| M1 | S02 Industry context | Único slide con estadísticas de terceros sin línea de fuente. "Google folded Veo into Gemini" es impreciso (Veo vive en Gemini y en Flow) | Añadir línea de fuentes 7pt (Fortune Business Insights Aug 2026; The Business Research Company; PR Newswire Aug 17 2026; Stripe customer story; Kuaishou Q1/Q2 2026; PYMNTS Sep 8 2026; ContentGrip/FT Aug 18 2026; TechCrunch Mar 24 2026); "Google ships Veo inside Gemini and Flow" |
| M2 | S04 Speed to market | Título "Outside the US and EU, paid AI-video subscribers are near zero" contradice el 75% de ingresos fuera de EE. UU. | "Outside the US and EU, localized AI-video checkout does not exist yet. This is a greenfield race, and first mover takes it" |
| M3 | S07 Proposed model | Tile "20-30% decline recovery" (cifra no publicada, marcada antes como fabricada); chip "Reconciliations" sin nota de roadmap; "RISK CONDITIONS + FRAUD & RISK"; "+1,000" vs "1,000+" | "30% recovered revenue on failed payments (published)"; nota "*Reconciliation: confirm GA status"; "FRAUD & RISK"; "1,000+" en ambos |
| M4 | S14 Bubble chart | Etiqueta "Ned" (Países Bajos truncado); India solapa Brasil y sale del borde superior; etiqueta Vietnam sobre México; Japón (#18 tráfico) en banda Medium mientras Vietnam/Países Bajos/EAU (#14-16) en Low; fuente 6.8pt | "Netherlands"; reacomodar India/Brasil/Vietnam; bajar Japón a Low; fuente 8pt |
| M5 | S48 Lever 2 methodology | Línea del ejemplo con estilos mezclados (20pt bold hasta "×", resto 11pt); "25% cross-border decline" contradice la fórmula "avoidable decline gap"; flechas rojas/amarillas fuera de paleta; "0.685 partial year" sobre una cifra mensual | Una sola tipografía; "25% avoidable decline gap"; flechas azul marca; mover el 0.685 a la línea anualizada o llamarlo "ramp factor" |
| M6 | S50 Lever 3 methodology | "Recovered renewals × ARPU. Each saved renewal extends customer LTV by another month" contradice los tiles (6.6K × $20 ≠ $0.61M); "~38% default... anything beyond is incremental" junto a "40% rescued" se lee como +2pp | "Recovered renewals × remaining subscriber value ($120 EM / $150 DM) × 0.78 incrementality"; aclarar que el 40% aplica a renovaciones que siguen fallando tras los reintentos de Stripe |
| M7 | S34 Canada | "Interac e-Transfers in 2024 ($554B)": son dólares canadienses (deck solo USD) | "Interac e-Transfer transactions in 2024 (Interac)" |
| M8 | S24 India | Tile 3 "~30K" vs palanca "+~30.1K" (tile 4 31.5K se construye con 30.1K) | Tile 3 "~30.1K" |
| M9 | S27 South Korea | "≈60% of population; Pay apps 54.9% of easy-pay use" a dos líneas y con "≈" | "~60% of population; 54.9% of easy-pay use" |
| M10 | S38 UAE | Caption del tile 1 en 12pt bold (resto 11pt regular) | 11pt regular |
| M11 | S43 Ranking | Filas 19-20 corridas 7pt a la izquierda; fila total con estilos mezclados; "of Lever 1 MRR" y la fuente en Calibri; "~$1.8M /mo" con espacio | Alinear x=56/87/195/267/339/416/634; un estilo en la fila total; Titillium Web; "~$1.8M/mo" |
| M12 | S19 Data sprint | "an Higgsfield-validated forecast" | "a Higgsfield-validated forecast" |

## Menores (pulido)

- S05: kicker "STRATEGIC CONTEXT THE DECISION FRAME" sin separador (" · "); elemento oculto duplicado "FOUR PAYMENT-FRICTION GAPS" (x=74, y=357); tres cifras "30" distintas ("30 PSPs", "30+ local PSPs per market", "30 local acquirers").
- S08: "apms" en minúscula; "REGIONAL PRESENCE:Local" sin espacio.
- S09: última fila de archetype split pegada al borde inferior de la tarjeta.
- S10: cabecera "WHY THIS MATTERS" duplicada; "Localize early" repetido tres veces; nota 8pt pegada al borde.
- S11: apóstrofes curvos y rectos mezclados; "~90K new + retained users" (son 83K nuevos + 7K recuperados; los 27K de renovaciones no están) → "new + recovered subscribers".
- S12: rangos con guion corto "4–12 weeks" vs "4 to 12" en el cuerpo.
- S16: regla inferior sobresale bajo la tarjeta azul.
- S17: círculos 5 y 6 con relleno claro (1-4 sólidos).
- S20: "...on Higgsfield's behalf, PayPal, iDEAL, Bizum and Satispay enablement in Europe included" (cláusula colgante); kicker igual al de S19 sin indicar secuencia.
- S22: "Levers are NOT additive" mientras el deck suma 21 + 1.3 + 2.8 → "sized sequentially, not independently".
- S23: "· TO VALIDATE:" en la línea de fuente se lee como to-do interno → "Data to validate with Higgsfield:" (aplica a los 20 slides país).
- S30 Indonesia: cuerpo desplazado +2pt x / +3pt y respecto a los vecinos.
- S39 China y S42 Pakistan: celdas de la tabla a dos líneas ("1.41B MAU; e-wallets 65% of e-com", "60M + 59M registered; 29M + 20M active", "742M Raast transactions in Q3 FY26 (SBP)"); "92% of retail digital" sin sustantivo.
- S40 Japan: línea de fuente en x=54 (resto x=46).
- S49 divisor Lever 3: subtítulo desplazado ~10px respecto a los divisores de Lever 1 y 2.
- S02: "OpenAI shut down the Sora app" es un hecho con fuente (TechCrunch, 24 mar 2026) y contexto competitivo, no un residuo; mantenerlo es defendible, pero es la única mención a OpenAI del deck.

## Lo que sí está bien

- Los 20 slides país: cifras iguales al modelo, tile 4 = L1 + L2 en todos, banderas correctas, US como upside fuera del hero, Rusia excluida, sin monedas distintas de USD (salvo Canadá, M7).
- Ranking (S43): suma de usuarios 82.4K ≈ 83K, MRR $1.80M, MAU 6.06M, top 3 47% y top 10 78% correctos.
- S09 top 20, S10 wave 2, S12, S13, S15, S17, S18, S21, S44 a S47, S51: sin hallazgos de fondo.
- Sin "ChatGPT", "WAU", "Claude", "Grok" en ninguno de los 55 slides; sin países fuera del top 20 en tablas (los de S10 son la wave 2, correcto).
