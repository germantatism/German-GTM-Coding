# Feedback de Justo sobre la PPT Suno + plan de ejecución (2026-08-06 noche)

Feedback crudo de Justo, organizado en 9 items y 3 bloques de ejecución. Meeting: mañana 2pm CO.

## Los 9 items del feedback

1. Mostrar qué métodos de pago soportan SUSCRIPCIÓN (recurrente) vs solo pago único.
2. Slide 5: mostrar cómo hace Stripe los métodos locales hoy: UPI = Stripe → EBANX/Razorpay → UPI; Pix = Stripe → EBANX → Pix (capas de agregación debajo).
3. NUEVA slide: el flujo con Yuno es DIRECTO a EBANX, Razorpay, dLocal (diagrama comparando hops).
4. Revisar/verificar los métodos de pago relevantes en cada mercado del deck.
5. Antes del exec summary (slide 4): mostrar lo que sabemos del negocio: industria, competidores, TAM; después bajar a sus website visits.
6. Slide 6: hablar de que los tokens de tarjeta viven DENTRO de Stripe (fricción de portabilidad).
7. Slides 7 y 8 (las nuevas A y B): mucho texto, pasar a bullets.
8. Slide de Scopely mostrando lo que tienen (proof point con material oficial interno).
9. Cambiar logo (⚠️ confirmar con Justo cuál: ¿logo de Suno en portada o versión del logo Yuno?).

## Plan de ejecución

### Paso 0: inputs que faltan (esta noche, German/Justo)
- [ ] Justo confirma el wording exacto de la cadena Stripe→agregador para UPI/Pix (es conocimiento de industria; en el deck impreso va formulado con cuidado porque Gurwinder/Madden pueden conocer el detalle técnico).
- [ ] Conseguir el material oficial de Scopely (slide aprobada / case interno; buscar en Glean o pedir a enablement). NUNCA inventar cifras de Scopely.
- [ ] Confirmar qué logo hay que cambiar.
- [ ] Verificación rápida de soporte recurrente por método (Pix Automático sí, UPI Autopay sí, SEPA DD sí, PayPal billing agreements sí, Klarna sí, OXXO no [voucher], SPEI pago único [domiciliación aparte], KakaoPay/NaverPay/PayPay: verificar).

### Paso 1: contenido nuevo (Claude armará el copy, German revisa)
- NUEVA "Industry context" (va ANTES del exec summary): mercado AI music ($1.98B narrow / $5.55B broad, 2026), Suno ~69% del tráfico de la categoría (AITools) y líder por un orden de magnitud sobre Udio/Mureka/ElevenLabs Music, tráfico de la categoría contrayéndose = la era de la monetización; remate: "y esto vemos en su funnel: ~23M visitas/mes". Todo con fuente (research 2026-08-06).
- NUEVA "Local rails: today vs direct" (el flujo de Justo): izquierda: Suno → Stripe → capa de agregación → UPI/Pix (más hops = más costo, menos visibilidad de declines); derecha: Suno → Yuno → directo EBANX / Razorpay / dLocal / acquirers locales (menos hops, términos comerciales directos, decline data completa). Va en "The proposed model" junto a la arquitectura.
- NUEVA "Scopely" (pendiente material oficial).
- Columna/flag "subscription-grade" en la tabla de métodos por mercado (item 1+4).

### Paso 2: ediciones a slides existentes
- Slide 5: bullet nuevo sobre agregación de métodos locales bajo Stripe [wording confirmado por Justo].
- Slide 6: bullet de tokens: "Card credentials are tokenized inside the current processor; adding or switching providers requires managed token migration. An orchestration vault makes tokens provider-agnostic." (formulado como fricción, no como imposibilidad).
- Slides 7 y 8 (2026 flows + web vs stores): pasar los párrafos a bullets de máx. 8-10 palabras.
- Logo: swap cuando Justo confirme cuál.
- Re-verificar listas de métodos por mercado contra checkout real (Pix ya confirmado por German).

### Paso 3: segundo prompt a Claude Design
Cuando el Paso 0 esté resuelto, Claude genera el prompt v2 (mismas reglas: no tocar diseño existente, solo texto + slides nuevas en el design system).

### Orden por impacto si falta tiempo antes de la call
1. Bullets en 7-8 (rápido, es lo que más se ve).
2. Industry context antes del exec summary (todo el contenido ya existe en el research).
3. Slide de flujo directo (el argumento más nuevo).
4. Tokens en slide 6 (una línea).
5. Logo.
6. Scopely y columna recurrente (pueden llegar en la v2 post-call).
