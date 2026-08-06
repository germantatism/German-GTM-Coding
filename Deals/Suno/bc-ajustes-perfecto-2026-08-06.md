# Suno BC: ajustes para versión "Madden presenta al board" (2026-08-06)

CORRECCIÓN de German (2026-08-06, tarde): el deck NO es de Madden ni va en primera persona de Suno. Sigue siendo el deck de Yuno (German presenta), pero diseñado "robable": estructura y contenido tan board-ready que Madden pueda copiarlo a su formato, ajustarlo y volver. Voz tercera persona ("Suno will...") se mantiene.

Este archivo es el registro; la lista operativa por diapositiva se entregó en chat (misma numeración del Google Slides 1DJVUwerFia3JZ0M66x3tYyKasQlmhf3En1WmY__OrZE).

## Qué se REVIERTE de la lista original
- Voz primera persona: cancelado. Se mantiene "Suno will / By partnering with Yuno".
- Cortar sección Why Yuno / leadership / logos: cancelado; se mantienen (es un deck Yuno). Oficinas (D13) sigue siendo prescindible y tiene el bug "SECTION TITLE"; leadership (D15) puede quedarse.
- Reemplazar el cierre (D36) por "Next steps & decision" del board: se suaviza; el cierre sigue siendo de German pero con next step de piloto/evaluación explícito.
- Portada: mantiene branding Yuno con lockup `yuno | Suno` arriba a la izquierda (regla de covers).

## Qué se MANTIENE íntegro (todo lo factual + estructura robable)
1. Números actualizados: $300M ARR + 2M subs (feb 2026), Serie D $400M+ a $5.4B (jun 2026). Nunca más $200M/$2.45B/$250M.
2. Narrativa en 3 actos de Justo DENTRO del deck Yuno: hoy → modelo propuesto → beneficios → roadmap (agenda: 01 How Suno runs payments today · 02 The proposed model & why Yuno · 03 Business case · 04 Roadmap).
3. Cero claims de "missing methods" sobre lo que ya viven (UPI, KakaoPay, NaverPay, Cash App Pay); usar la cita del help center ("options not yet available with our direct processor...") como evidencia del techo.
4. Quitar Discover (no documentado). Mapa real de métodos + 17 monedas + 36 países en D6. Typo "In-Store"→"In-app". "30% in-app" marcado como supuesto a validar.
5. Quitar Rusia como mercado accionable; eliminar fila Mir/SBP/YooMoney (sanciones; RUB no está en las 17 monedas). Reemplazar por Polonia (PLN vive) y recalcular EMEA.
6. Brasil: agregar Pix (~40% e-comm) + installments; hoy el deck no menciona Pix.
7. Alemania: giropay descontinuado (fin 2024) → Wero/SEPA DD/PayPal/Klarna.
8. APAC: Corea solo net-new (Samsung Pay, Toss; Kakao/Naver ya viven); India → UPI Autopay (UPI ya vive).
9. NA: headline = PayPal ya existe pero solo vía app stores (15-30% fee); habilitarlo en web = margen inmediato. Klarna prescindible.
10. D19: reconciliar $48-52M vs $33-37M en una sola cifra; quitar "202X"; base TPV recalibrada a $300M ARR con split web/IAP como supuesto etiquetado; agregar unit economics (+1pt approval ≈ $3M/año, derivado).
11. Bugs: "gaming" en D10 → consumer subscriptions; números fantasma en D23/27/31/35; "$0.83"/"$1.97" sin "million"; verificación de atribución Livelo/Wingo en D16; "1,500 connections" vs 1,000+/460+ unificar; "7M songs daily" verificar o quitar.
12. Nuevas diapositivas (en voz Yuno): arquitectura hoy vs propuesta (keep Stripe, agregar capa), payouts/creator economy 2026 (Spark + WMG opt-in + overages), economía web vs app store (iOS $10/$30 vs web $8/$24), build vs buy (~22 años eng + ~$5.9M evitados), roadmap 30/60/90 con criterios de éxito.
13. Nada de breach, BBB F ni outage en el deck: va a circular dentro de Suno.

Detalle completo por diapositiva: ver mensaje de chat de esta fecha (sesión Claude 2026-08-06) o reconstruir de este resumen.

## Slides del deck Anthropic (1tog6yCe3-QViNsu9ENEk-ES-sWbSpGDH) a adaptar para Suno
Prioridad alta: decision frame (Stripe-only vs 2do PSP vs orquestación), arquitectura keep-Stripe, waterfall metodológico de 3 levers, tabla top-mercados con arquetipos, slide de 6 data inputs requeridos, sprint de datos de 2 semanas, matriz 2x2 de priorización.
Opcionales: wave-2 emergentes (con twist Suno: los mercados donde los usuarios ya hackean el pago: Nigeria/Ghana/Pakistán/Filipinas documentados), dedicated teams 4 columnas, sprint BD 60 días para mandatos recurrentes (Pix Automático / UPI AutoPay).
NO copiar: bloque huérfano de Mastercard/Agent Pay en la slide "why move now" (artefacto de otro deck); números de Anthropic sin recalcular (ARPU $240/yr vs Suno ~$150/yr blended, WAU de Claude, etc.).
Detalle completo en chat 2026-08-06 (noche).
