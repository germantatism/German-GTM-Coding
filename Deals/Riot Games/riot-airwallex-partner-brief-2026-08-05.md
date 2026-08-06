# Riot Games: brief para la reunión con Airwallex

**Fecha:** 2026-08-05
**Contexto:** Airwallex está en conversaciones activas con Riot Games y avanzando bien. Objetivo de la reunión: contarles qué sacamos de nuestro call con Riot (2026-07-31, Andreas Borngraeber) y construir un plan conjunto para que nos ayuden a entrar.

---

## TL;DR (30 segundos)

Tuvimos call directo con Andreas Borngraeber, el arquitecto de todo el stack de payments de Riot (intro del CSO Abhi Ramprasad). Conclusión: el middle tier in-house de Riot es intocable hoy, el propio CEO lo construyó cuando era CFO y hay trauma histórico con vendors third-party. PERO Andreas dejó una puerta abierta explícita: cuando Riot entre a physical goods / mail order (merch con shipping), ve a Yuno como capa complementaria, no como reemplazo. Timeline: meses a 1-2 años. Todo pasa por RFP formal de 10-12 vendors. La jugada con Airwallex: ellos mueven fondos, nosotros somos capa técnica, cero overlap; si su thread en Riot conecta con el proyecto comercial nuevo, podemos entrar juntos como propuesta combinada.

---

## Lo que le cuentas a Airwallex del call

**Quién es Andreas Borngraeber**
- Construyó todo el stack de payments de Riot; hoy lidera un proyecto confidencial en el espacio "commercial" (no pudo dar detalles, pero es la persona a seguir).
- Basado en Dubai (no en LA ni Europa). Alemán, background de finanzas (payments, treasury, management accounting, rol tipo CFO en gaming antes de Riot).
- Llegó a nosotros por intro del Chief Strategy Officer (Abhi Ramprasad), así que tenemos air cover de C-level.

**Cómo funciona payments en Riot hoy**
- Middle tier propio construido ~2015: hub central de integración para todas las relaciones con PSPs. Fallback PSPs, dynamic routing, todo ya construido in-house.
- Postura PCI deliberadamente liviana: hosted payment fields, las tarjetas viven en el PSP, tokens hasheados atados a cada PSP. No quieren exposición SAQ-D.
- Operación por juego/región: prueban PSPs en juegos pequeños y le dan el negocio de cada región al PSP que mejor performa. Failover automático al fallback cuando suben los declines.
- Solo digital goods (skins, champions), card-not-present. No hay flujo de shipping/address/warehouse hoy.

**Por qué el core está cerrado**
- Dos traumas con third parties: el colapso de su primer vendor de pagos en el launch de LoL (2008-09, terminaron construyendo su propio shop y payments API en 6 semanas) y un middle layer coreano que escaló mal y tuvo un incidente serio de seguridad que casi les cuesta un evento mayor. Seguridad y "healthy paranoia" es cultura, especialmente en payments.
- El CEO actual era el CFO que vivió todo eso. Frase textual de Andreas: "as long as our CEO is CEO, there won't be a way in" (para reemplazar el middle layer).
- Nota de manejo: la historia del incidente de seguridad compartirla como "trauma histórico con vendors", sin detalles, porque Andreas fue candid sin NDA.

**La puerta abierta (lo importante)**
- Physical goods / mail order: merch con dirección, validación de address, inventario en warehouse, capture al momento del envío (regulación US), returns amarrados al payment y refunds. Su stack actual no cubre nada de ese flujo y Andreas lo sabe.
- Cita textual: "what I believe could work in a complementary way once you go into mail order. So that's why I basically offered to talk."
- Timeline: "not tomorrow", un par de meses a 1-2 años, depende de cómo avancen "those projects" (probablemente el proyecto comercial que él lidera).
- Proceso de compra: siempre RFP. Comparan 10-12 vendors, lista de criterios actuales y futuros, 3 rondas de negociación. Nunca venta directa.
- Le interesó nuestra capa de AI (leyó la documentación de Payments Concierge por su cuenta; AI es hot topic en Riot). Quedamos en ping cada pocos meses.

---

## El ángulo conjunto Yuno + Airwallex

- **Cero overlap entre nosotros:** Andreas validó en el call que Yuno es capa técnica pura, sin funds flow, sin MoR, sin licencias bancarias. Airwallex es exactamente lo contrario: acquiring, FX, payouts, licencias. Somos complementarios por diseño.
- **El modelo de Riot nos favorece a ambos:** su middle tier trata a los PSPs como vendors intercambiables que entran por RFP. Airwallex encaja como PSP/acquirer dentro de ese modelo hoy. Yuno no compite ahí; nuestra entrada es el flujo nuevo de physical goods donde el middle tier no llega.
- **La propuesta combinada para el RFP que viene:** Yuno orquesta el flujo completo de mail order (address, capture on ship, returns, refunds, ledger) y Airwallex procesa y mueve los fondos. Llegamos al RFP como stack pre-integrado en lugar de dos vendors sueltos entre 10-12.
- **Por qué les conviene a ellos:** si su conversación con Riot toca el proyecto comercial nuevo, meternos en la jugada les da una historia end-to-end que ningún PSP solo puede contar, y nosotros les damos contexto de primera mano del decision maker técnico (Andreas) y del sponsor C-level (Abhi, CSO).

---

## Plan conjunto a proponer

1. **Intercambio de mapa de cuenta:** nosotros ponemos sobre la mesa a Andreas (arquitecto, Dubai, proyecto comercial) y la intro del CSO; ellos nos cuentan con quién hablan, qué use case y en qué etapa van.
2. **Alinear narrativa:** ninguno de los dos pitcha "reemplazar el middle tier". La historia conjunta es el flujo nuevo (physical goods / commercial) donde Riot no tiene nada construido.
3. **Cadencia coordinada:** Andreas nos invitó a hacerle ping cada pocos meses. Coordinar esos toques con los avances de Airwallex para que las dos conversaciones se refuercen en lugar de cruzarse.
4. **Trigger del RFP:** el que primero detecte que se abre el RFP de physical goods avisa al otro. Objetivo: entrar como propuesta combinada desde la primera ronda.

---

## Preguntas para hacerle a Airwallex (zona de notas)

- ¿Con quién exactamente están hablando en Riot? ¿Equipo, seniority, geografía? ¿Se cruza con Andreas o con el proyecto comercial?
- ¿Qué use case están vendiendo? (acquiring regional, payouts a esports/creators, FX/treasury, algo del lado commercial nuevo)
- ¿En qué etapa están? ¿Ya pasaron por un RFP de Riot o van hacia uno?
- ¿Han escuchado algo del proyecto de physical goods / merch / mail order?
- ¿Estarían dispuestos a presentarnos con su contacto o a incluirnos en la narrativa cuando toque orquestación?
- ¿Qué necesitan de nosotros para que la propuesta combinada les sume en su propio deal?

**Notas:**

