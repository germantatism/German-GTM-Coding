# Project instructions for German Tatis (Yuno GTM)

Distilled 2026-10-06 from German's Claude Code memory: his profile plus every standing rule he has given. Paste into the Claude app Project's custom instructions, or upload as project knowledge if it exceeds the limit. Full context lives in MEMORY_FULL.md.

## Who German is

### Who German is — Account Executive (senior) at Yuno, SDR/outreach workflows
German Tatis (german.tatis@y.uno) is an **Account Executive at Yuno** (more senior role; previously led pre-sales). Yuno is a payment orchestration platform (single API to 1,000+ payment methods, PSPs, fraud tools, 190+ countries).

His workflow centers on outbound sales research and outreach: /research briefs, /builddeck merchant decks on deck.yuno.tools, and a cadence of emails (Email 1 opener, Email 2 deep dive, success case, industry snapshot) tailored to [[reference_buyer_personas]]. His written deliverables follow strict voice rules: no em-dashes, no name dropping in Email 1, tight and senior tone (see [[feedback_email_length_senior]]).

## Standing rules (how German wants Claude to work)

### After completing any code/file changes, automatically git commit and git push without asking the user
After making code or content changes, always commit AND push to the remote automatically. Don't stop at "wrote the files" or "made the edit" — the work isn't done until it's pushed.

**Why:** User explicitly told me on 2026-05-04 that push must happen automatically every time. They were frustrated that after adding SAP merchant to deck.yuno.tools (files written, Supabase row inserted), I stopped without pushing — so the Railway deploy didn't trigger and the new merchant wasn't live. They want this to be the default behavior, not something they have to ask for.

**How to apply:** When you finish a task that modified tracked files, immediately:
1. `git add` the relevant files
2. `git commit` with a descriptive message
3. `git push` to **`main`** (not `master`)

Do all three without asking permission. This applies even when changes touch deploy-sensitive files (CSVs, manifests, generated assets) — that's exactly when push matters most. Only skip the push if the user explicitly says "don't push" or "just stage" first.

**Branch convention for yuno-sales-pitch-maker:** Local branch is `master` but the deploy branch on `origin` is `main`. Always push with `git push origin master:main` (or whatever local branch maps to `main`). Confirmed 2026-05-04: `origin/main` is what Railway deploys to deck.yuno.tools / ss26.yuno.tools. `origin/master` exists but is stale ("Initial commit" only) — do not push there.

### When /business-case skill is activated, always present the slide guide content (slides 4-7) alongside the Excel generation
Always include the "Our Understanding of the Context" slide content (slides 4-7) when running /business-case.

**Why:** The user copies this content directly into the PowerPoint template. The slide guide IS the primary output alongside the Excel file.

**How to apply:** Every time /business-case runs, present SLIDE 4 (Executive Summary), SLIDE 5 (Current Setup Constraints), SLIDE 6 (Payment Stack Overview), and SLIDE 7 (Traffic Map) formatted as copyable text blocks — before or alongside the Excel generation.

### Cuando Magdalena o Samuel Carreño ponen a German en CC en correos a prospectos, German entra al hilo con un reply de estructura fija; plantilla y reglas
Cuando un Sales Strategy Associate (Magdalena Torrealba, Samuel Carreño) manda correos a prospectos con German en CC, German responde dentro de cada hilo para presentarse. Pide "el reply de siempre" y espera un borrador por cada correo sin abrir.

Estructura (inglés, 110 a 130 palabras):
1. Saludo "Hi {nombre},".
2. Intro: "German here, following {Magda/Samu}'s note", su rol (lidera las conversaciones de Yuno con merchants en North America, o globally si el prospecto es de fuera) y por qué escribe directo en vez de quedarse en cc. Si hubo contacto previo, mencionarlo solo con lo verificado.
3. Tesis en dos frases: la del business case si existe; si no, hechos públicos del stack del prospecto.
4. Un solo proof point publicado: inDrive 90% de aprobación en 10 mercados, o McDonald's +4.7%.
5. CTA de 20 a 30 minutos con dos días concretos revisados contra su calendario, en la zona horaria del prospecto, más "happy to move around your calendar".
6. Cierre "Best,".

**Why:** lo aprobó y envió así en 26 hilos de Magdalena el 17-sep-2026 y pidió lo mismo para Samuel el 29-sep-2026.

**How to apply:** buscar `from:{sdr} is:unread in:inbox`, crear cada borrador con create_draft + replyToMessageId, To = prospecto, CC = quien lo copió. Variar la intro y alternar el proof point entre contactos de la misma empresa. Verificar en Gong y Gmail lo que el SDR afirme sobre conversaciones previas antes de repetirlo. Sin links ni guiones. Ver [[feedback_gmail_update_draft_detaches_thread]], [[published-stats-only]], [[project_magdalena_bc_campaigns_sep_2026]], [[project-bounce]].

### Pedidos de datos a clientes = Google Sheet de una sola hoja, campo a la izquierda y respuesta al lado; nada de workbooks de muchas hojas
Cuando German pide armar una solicitud de información para un cliente, el entregable es un Google Sheet de UNA sola hoja: el campo que queremos a la izquierda y al lado el espacio para que el cliente ponga sus números. Lista corta (unas 30 a 40 filas), agrupada por secciones.

**Why:** en Cruz Verde (29-sep-2026) dijo "la mayor cantidad de data posible" y entregué un Excel de 14 hojas y 90 solicitudes; lo mandó a rehacer dos veces: primero a Google Sheets en formato formulario, luego "muuucho más sencillo y en solo un tab". Detallado para él significa cubrir los temas clave (por ejemplo % de rechazos hard vs soft), no un instrumento largo que el cliente no va a llenar.

**How to apply:** empezar por la versión sencilla en Google Sheets y ofrecer el detalle como opción. Sin hojas de instrucciones, prioridades, columnas calculadas ni filas de ejemplo. Vía técnica: [[project-slides-api-token-dead]] (conector de Drive crea el archivo y lo comparte con la service account; Sheets API escribe). Ejemplo: [[project-cruz-verde]], `Deals/Cruz Verde/build/build_data_request_simple.py`.

### In client-facing business cases use the metric the client reported (e.g. Palco ticket promedio $37.09), never a value we derived that contradicts it; raise the discrepancy separately
When a prospect reports a metric (ticket promedio, TPV, volumes), client-facing decks and business cases use that exact number. Do not replace it with a figure we derived from their other data, even if the derivation is arithmetically sound (Palco: Patricio said ticket promedio $37.09; the deck had used $163 = $346M / 2.12M and German said "ojo con eso, reajusta todo").

**Why:** the client recognizes their own number and will reject or distrust a different one; a bigger business case built on a derived ticket looks inflated. Discrepancies are a discovery question, not something to fix silently in the deck.

**How to apply:** use the reported metric everywhere in the deliverable; flag the inconsistency to German in the notes or the summary so he can ask the client; if a lever needs a different basis (e.g. bps on TPV), say explicitly which reported number it uses. See [[palco-ticketing]].

### Always write a shorter version of the Payments Concierge paragraph in email2 — keep it concise
Keep the Payments Concierge paragraph shorter in email2. Don't over-explain it.

**Why:** German finds the full-length version too long and wants it trimmed down.

**How to apply:** When writing email2, condense the Payments Concierge section to 2-3 sentences max instead of the full block. Keep the core idea (AI assistant, natural language queries, proactive alerts) but cut the detail.

### Pattern German likes for replying to a "too expensive / can't justify the cost" rejection, modeled on Sean Calabro's FlightHub reply (oct-2026) and reused for Flair
When a prospect rejects on cost ("breakeven is X, at Y I can't justify it", "the $5-7K range"), German wants the reply built like Sean Calabro's message to Anna-Lena at FlightHub (oct-2026):

1. Appreciate the insight and acknowledge the gap plainly ("that's a ways off from the current proposal").
2. Say we have flexibility in how we structure the commercials, without quoting a new price.
3. Ask for a call to understand how they arrived at their number, and offer to walk through how we arrive at ours.
4. Frame it as getting the full picture on both the cost side and the value side, "so we're all working from the same picture".
5. Restate that we still think it's a great fit for their needs.
6. Close with "this week or next" and offer to include whoever is weighing in on the approval.

Optional opener when the prospect claims near-zero in-house cost: "honestly, I'm surprised your cost comes out that low", then name the hidden costs (dev time per change, manual reconciliation, declines with no second chance) as facts already verified for that account.

**Why:** It keeps the door open and moves the fight from price to the cost model, which is where Yuno wins. Discounting first validates their math.

**How to apply:** Any cost rejection reply (WhatsApp, email). Shorter on WhatsApp. Never quote a new price in the first reply; see [[reference_yuno_pricing_policy]] for room if the call happens. Used on [[project_flair_contacts]] (Lucas, 6-oct-2026) and [[project_flighthub]] (Sean to Anna-Lena).

### All decks render the cover with a top-left lockup (yuno wordmark | merchant logo) and no "Hello {Company} team!" greeting. The lockup is the default.
The cover slide (`src/components/slides/SlideCover.jsx`) renders a compact co-brand lockup in the top-left: Yuno wordmark, vertical separator, merchant logo, all matched to the same height (clamp 20–32px). No "Hello {Company} team!" greeting and no large merchant logo block beneath.

**Why:** User confirmed on 2026-05-11 that this is the preferred cover treatment going forward. Cleaner, more aligned with the Yuno slide design language, lets the GlobeHalo + title carry the visual weight instead of a stacked greeting+logo block.

**How to apply:**
- Do NOT reintroduce the greeting (`Hello {Company} team!`) or the large merchant logo block in any future cover refactor.
- New merchant onboarding only needs the standard logo asset in `public/merchants/{slug}.png` — the cover picks it up automatically via `data.COMPANY_LOGO`.
- Light theme still uses the masked-div fill (theme.accent silhouette); dark theme uses `<img>` directly with the `WHITE_LOGO_FILTER` override for dark-logo merchants in the `DARK_LOGO_MERCHANTS` set.
- Banking mode with the placeholder `Your Bank` still renders Yuno alone without the separator (the `data.MODE === 'banking' && data.COMPANY_NAME === 'Your Bank'` branch suppresses the lockup tail).
- If a merchant logo is unusually wide (e.g. Costco), it's still bounded by `maxWidth: clamp(140px, 14vw, 260px)` in the `coBrandLogo` style so it doesn't dominate the header.

**Reference commit:** `4ab829a` — refactor cover slide to yuno + merchant lockup.

### Every deck content change (slide-overrides.json, business-overviews.json, slide component edits) must be deployed to Neverland/internal-tools, not just pushed to GitHub/Railway
After editing yuno-sales-pitch-maker deck content or slide components, pushing to `main` (GitHub) is NOT enough to make the change visible on `decks.internal-tools.y.uno` (Neverland/Kingdom). That is a separate deploy target from Railway (which auto-deploys deck.yuno.tools on push) and does not always auto-trigger.

**Why:** German explicitly said (2026-08-10) he needs every adjustment he asks for to always be reflected on internal tools, after Magnific/T-Mobile deck fixes were pushed but not visible there.

**How to apply:** After any commit that changes deck content/behavior, explicitly trigger a Kingdom deploy for the `decks` service (ms_id `bbfe08b3-d14d-4f45-8dfc-d427b31bacf2`, env `dev` id `959e071e-7663-42fd-9f34-3dfd303a567b`, kingdom `neverland`, public: false so no tag needed, deploy directly from `main`):

```bash
source ~/.zshenv
curl -s -X POST -H "Authorization: Bearer $KINGDOM_TOKEN" -H "Content-Type: application/json" \
  -d '{"ms_id":"bbfe08b3-d14d-4f45-8dfc-d427b31bacf2","env_id":"959e071e-7663-42fd-9f34-3dfd303a567b","version":"main","use_ci_image":false,"ignore_restrictions":false}' \
  "https://internal-infra.y.uno/kingdom/v1/deployment/create"
```

Poll `GET /kingdom/v1/deployment/get?ms_id=...&env_id=...&limit=1` (response shape is `{"rows":[{status, version_hash, finished_at, ...}], "count"}`, read `rows[0].status`) until `status:"deployed"` (states: starting → preparing → building → created → synchronizing → deployed). Then verify the actual content landed (not just that the build succeeded) by fetching the live JS bundle (`/m/<slug>` → extract `/assets/index-*.js` → curl it) and grepping for a distinctive string from the change — build success does not guarantee the right commit/content shipped.

Kingdom token lasts ~12h now (exp claim in the JWT); if `deployment/create` returns 403 `Token expired`, renew with `bash ~/.claude/plugins/marketplaces/yuno-plugins/yuno/scripts/login.sh kingdom` (Google SSO: opens localhost:8765 in the browser, German clicks Sign-In, 3-min window; run it in background and poll `~/.zshenv`). Kingdom token comes from `$KINGDOM_TOKEN` in `~/.zshenv` (not the `~/.config/yuno-plugin/kingdom-token` file, which may be stale/undecodable even when the env var is valid) — check via `source ~/.zshenv; [[ -n "$KINGDOM_TOKEN" ]]`.

See also [[neverland-migration]] for the broader migration context and [[salesmaker-deploy-branch]] for the Railway side.

### Deck edit requests must apply ONLY to that specific deck, never leak to other decks
When applying a deck edit request (from the Edit button / a person), always make the change they asked for, BUT scope it to **that specific deck only**. It must not alter any other deck.

**Why:** Decks share components (`SlideBase`, slide components, `t()` copy). A naive edit to a shared component changes every deck in that language. German's rule: one person's request must never degrade everyone else's decks.

**How to apply:** Scope by the narrowest identifier that isolates the target deck — `data.COMPANY_SLUG` for a client deck, or a combination like `data.AUDIENCE==='merchant' && data.LANGUAGE==='fr'` for the generic-merchant-in-French deck. In `buildSlides` (SlideViewer.jsx) filter the slide order conditionally; for per-deck copy/data prefer Supabase per-merchant fields over editing shared strings. Example done 2026-07-02: dropped the Integration-as-a-Service slide from ONLY the French generic merchant deck (en/es/pt kept it). If a request truly can't be isolated to one deck in the current architecture, flag it before applying globally. Related: [[project_deck_edit_button]], [[feedback_never_duplicate_decks]].

### Listas y cruces de datos se entregan en Google Sheets (vía conector de Drive), no en Claude Docs ni artifacts
El 5-oct-2026, cuando empecé el cruce Money20/20 × TCL como Claude Doc, German cortó: "pero quiero que me traigas todo en un google sheets".

**Why:** German vive en Google Workspace y comparte estas listas con Susana, Samuel y Sean; un Claude Doc no entra en ese flujo.

**How to apply:** cualquier lista, cruce o tabla de contactos va directo a un Google Sheet. Vía que funciona sin OAuth: `mcp__claude_ai_Google_Drive__create_file` con `contentMimeType: text/csv` y `textContent` (se convierte solo a Sheet; una pestaña). El xlsx en base64 también convierte, pero el parámetro base64 de un workbook de 55 KB (74K chars) supera el límite de salida por turno; usar CSV compacto (< 45 KB) y guardar el xlsx completo en el repo. Ver [[feedback_drive_download_to_disk]] para LEER hojas grandes.

### Para leer un Google Sheet grande completo sin OAuth: download_file_content como xlsx → el harness lo guarda en disco → decodificar base64 con Python y abrir con openpyxl
Descubierto el 5-oct-2026. `mcp__claude_ai_Google_Drive__read_file_content` solo devuelve 5-6 filas de muestra por pestaña en hojas grandes, y gsheets_read / service account / gcloud siguen sin acceso (ver [[project_gsheets_mcp]]).

**How to apply:** llamar `mcp__claude_ai_Google_Drive__download_file_content` con `exportMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`. Cuando el resultado supera el límite de tokens, el harness lo guarda en `~/.claude/projects/<proyecto>/<sesión>/tool-results/mcp-claude_ai_Google_Drive-download_file_content-<ts>.txt` (JSON con `content` en base64). Decodificar con Python (`json.load` → `base64.b64decode` → `.xlsx`) y volcar cada pestaña a TSV con openpyxl. Funcionó con la TCL completa (1.9 MB, 5 pestañas) y con la lista de Money20/20 (1.1 MB, 13 pestañas). Exportar como `text/csv` solo trae la primera pestaña por posición (en la hoja de Money20/20 era "Cadence", no la útil).

Límite relacionado: WebSearch tiene tope de 200 búsquedas por sesión compartido entre todos los subagentes ([[feedback_websearch_budget_shared]]).

### Email 1 (opener) must always use the Yuno description boilerplate, never client name dropping. Name dropping is for Email 2+.
Email 1 always uses the descriptive Yuno boilerplate ("Yuno is a global payment infrastructure platform..."), never the name-dropping variant (GoFundMe, Uber, OpenAI, etc.). Client logos / name dropping is reserved for later emails in the cadence.

**Why:** The first email should establish what Yuno is. Name dropping belongs in follow-up emails where social proof reinforces the initial pitch.

**How to apply:** When writing /email1, always use Variant A (description). When writing /email2 or later cadence emails, name dropping is allowed and encouraged.

### Email 1 and Email 2 must be shorter, denser with value, senior AE tone (same voice)
All Email 1 and Email 2 outreach must keep their existing structure but be shorter and higher-value than the older versions.

**Why:** German is now an Account Executive and more senior (see [[user_german_profile]]); his emails should read tighter and sharper, not junior or padded.

**How to apply:**
- Keep the SAME structure. Email 1: hook → PSP paragraph → APM/local-methods paragraph → one capability paragraph → Yuno boilerplate → CTA. Email 2: opener → 3 titled solution paragraphs → Payments Concierge → client logos → CTA. Keep the SAME persona-tailoring off the base message ([[reference_buyer_personas]]).
- Make each paragraph tighter: 1-2 sentences instead of 3-4. Cut filler and hedging, lead with the insight, drop throat-clearing.
- Every sentence must carry value (a specific finding, number, market, method, or a concrete Yuno outcome). No generic lines.
- Same voice German always uses: warm, peer-to-peer, curious, human, first person, genuine questions. Not corporate.
- Hard rules still apply: no em-dashes or " - " punctuation, no "no small feat", no name dropping in Email 1 (logos start Email 2+), keep Payments Concierge to 2 sentences.
- Net effect: senior AE polish. Shorter, denser, more confident, still the same tone.

**Añadido 21-sep-2026 (Appmaking, respuesta a preguntas técnicas de un cliente):** aun cuando el cliente pregunta con nombres de campos de API, German quiere respuestas de 2 o 3 frases por pregunta en lenguaje simple, sin listas de casos, sin "notas para desarrolladores" y sin párrafos de contexto de pricing: sí/no, el mecanismo en una frase y la única limitación que importa. El detalle técnico se lleva a la call. Empezar por la versión corta; rechazó tres versiones largas seguidas.

**Añadido 5-oct-2026 (Genspark, respuesta a Winnie):** cuando el prospecto cuenta algo personal o de contexto (su equipo volcado en NetSuite), German quiere que la respuesta reaccione como persona antes de proponer nada: "Oh wow, I can only imagine the whole team heads down on that right now". Rechazó "Let's pick this up once the dust settles. ... how about the week of October 26th?" por sonar "como robot de AI". Patrón: 1) reacción humana a lo que dijo, 2) pedir igual un rato corto "whenever you can breathe for half an hour", 3) salida fácil. Nada de frases hechas de ventas ("once the dust settles", "pick this up").

**Añadido 5-oct-2026 (Super.com, intro + catch-up a Rick Galasieski para café en Money20/20):** German rechazó la primera versión por "súper tedioso" y con tono de ChatGPT: era un recuento cronológico de todos los contactos previos (quién, cuándo, qué dijo cada uno) en párrafos largos. Lo que quiere en un email de intro/catch-up: 4 párrafos de 1 a 3 frases, backstory en dos frases sin fechas ni citas, un gesto humano (felicitar por la ronda), y el CTA como pregunta corta ("Coffee between sessions Monday or Tuesday?"). Subject corto y casual ("Coffee in Vegas?"), no "Empresa + Yuno, ...". Más friendly y "appealing", menos informe.

### Correos a prospectos que German envía él mismo van sobrios y sin links ni menciones de "sección X del deck"; German agrega el link o adjunto a mano
Al redactar correos que German va a enviar (propuestas, follow-ups), no meter links (Papermark, Drive, deck.y.uno) ni referencias tipo "sección 06, slides 36 y 37". Tampoco listas numeradas de beneficios ni frases de cierre grandilocuentes ("se paga más de diez veces"). Tono plano y corto: qué mando, en qué se basó, la cifra clave, y cómo seguimos.

**Why:** 24-sep-2026, correo de propuesta a Yango: German rechazó la primera versión ("menos allá", "esa vaina de meter links y eso no, yo me encargo de esa parte").

**How to apply:** Borradores de Gmail sin URLs; German pega el link o adjunta el PDF. Mantener [[feedback-email-length-senior]] y [[feedback-no-dashes]]. Ver [[project-yango]].

### Gmail MCP update_draft desprende el borrador del hilo original; para cambiar un borrador de respuesta, recrearlo con create_draft + replyToMessageId
Al usar `mcp__claude_ai_Gmail__update_draft` sobre un borrador creado como respuesta (create_draft con replyToMessageId), Gmail lo desprende del hilo: el resultado devuelve un threadId nuevo igual al messageId y el borrador saldría como correo nuevo, no como reply. Verificado 2026-09-17 con 26 borradores (Magnific, T-Mobile, Best Buy).

**Why:** German quiere los follow-ups siempre dentro del hilo de Magdalena para que el contexto y el CC viajen juntos. Un borrador desprendido rompe eso sin avisar.

**How to apply:**
- Nunca editar un borrador de respuesta con update_draft. Si hay que cambiar el texto, crear uno nuevo con create_draft + replyToMessageId y descartar el viejo con trash_message (no existe delete_draft en el conector).
- Antes de crear, tener el texto final (días propuestos revisados contra el calendario) para no tener que editar.
- Verificar siempre con list_drafts que threadId == threadId del hilo de origen.
- trash_message sobre borradores puede ser bloqueado por el clasificador de auto mode; si pasa, avisar a German para que los descarte a mano en vez de reintentar.

Relacionado: [[feedback_gmail_workflow]].

**Añadido 21-sep-2026:** antes de recrear un borrador (create_draft nuevo + delete_draft del viejo), listar el borrador y comparar: si el `messageId` cambió o el texto difiere de lo que Claude creó, German lo editó a mano en Gmail. En ese caso NO borrarlo: crear el borrador corregido aparte, incluyendo sus ediciones, y avisarle cuál descartar. Pasó con Appmaking (cambió "Attached" por un link y "Jarrett can" por "We can").

**Matiz 21-sep-2026 (mismo día):** German prefiere UN solo borrador en el hilo. Cuando pide cambios sobre un borrador que él editó, recrearlo llevando TODAS sus ediciones (comparar contra el texto real en Gmail) y borrar el anterior; no dejar dos. Ojo con links pegados a mano: pueden venir envueltos en `google.com/url?q=`; dejarlos directos.

### German quiere a Claude siempre dentro de su Gmail (conector claude.ai); leer threads y dejar drafts sin preguntar
German dijo (2026-08-05) que conectar Gmail con Claude es "importantísimo" porque necesita a Claude entrando a su correo siempre.

**Why:** Su workflow de AE vive en el correo: threads de deals (Hostinger, Lululemon, Eventbrite), RFPs, follow-ups. Quiere que Claude opere ahí directamente, no que le pase texto para copiar/pegar.

**How to apply:** Si el conector claude.ai Gmail está autenticado en la sesión, usarlo proactivamente: leer el thread relevante antes de redactar, y dejar el draft creado en Gmail (draft, no enviar sin OK). Si NO está autenticado, avisarle al inicio y darle el paso de claude.ai/settings/connectors. Pendiente al 2026-08-05: German estaba por autorizarlo. Relacionado: [[project_hostinger]] (primer uso previsto: draft en el thread de Hostinger con las respuestas del RFP).

### LinkedIn outreach messages should be a bit shorter than the standard email version
When a persona-tailored outreach message is for LinkedIn (connection message, InMail, LinkedIn DM), make it a bit shorter than the standard email version. Tighten the middle: keep the hook + one crisp Yuno line + the value in one sentence + soft CTA. Full-length structure is fine for email.

**Why:** LinkedIn is read on smaller screens and skimmed; long blocks get ignored. Email tolerates more length.

**How to apply:** Same persona angle and grounding as always (see [[reference_buyer_personas]]), just condensed. Keep no-dashes, no-name-drop-in-opener rules. Default to the shorter form whenever the channel is LinkedIn/Sales Navigator; keep full length only when German says it's for email.

### Meeting briefs — agenda y open questions SIEMPRE al final (ahí arranca German a tomar notas); TL;DR battle card al inicio
En todo meeting brief para German: la **agenda de la llamada y las open/discovery questions van SIEMPRE como últimas secciones** del documento. Razón: German toma notas a partir de la agenda, así que todo el contenido de estudio va antes y la zona de trabajo en vivo queda al final, con espacio de notas ("Notes: ___") bajo cada bloque de agenda y cada pregunta.

**Why:** German lee el brief de arriba hacia abajo antes de la reunión y usa el final del doc como su hoja de notas durante la llamada.

**How to apply:** Estructura v2: (1) header con logística + objetivo + action flags, (2) TL;DR battle card de 1 página, (3) quién está en la sala, (4) la empresa (incl. subsidiarias/estructura corporativa), (5) payments money map, (6) top markets, (7) news & signals con fechas, (8) cómo vender Yuno + landmines, (9) "Be ready for" (qué te pueden preguntar a ti, con respuestas listas), y de últimas SIEMPRE (10) agenda con espacio de notas y (11) discovery questions con espacio de notas, + checklist post-meeting. Ver [[project-meeting-brief-skill]].

### Never create a duplicate deck/merchant; if it already exists, just say so
NEVER duplicate a deck/merchant. If a merchant already exists (in `public/merchants.csv`, `src/data/merchants.generated.js`, `public/merchants/{slug}.png`, or Supabase), STOP and just tell the user it already exists. Do not rebuild, do not overwrite the logo, do not add a second row.

**Why:** In the super.com /builddeck run, the Supabase existing-merchant check returned "Invalid API key" so I never confirmed existence, AND I skipped checking the local files. super-com already existed (CSV, manifest, logo). I created duplicate CSV + manifest entries and overwrote the original logo, which the user flagged. Had to git revert.

**How to apply:** In /builddeck pre-flight, the existing-merchant check must include LOCAL files, not only Supabase: `grep` the slug in `public/merchants.csv`, `merchants.generated.js`, and `ls public/merchants/{slug}.png`. If the Supabase key lookup fails, the local grep is the authoritative fallback, never assume "not found" on a failed API call. If found anywhere, stop and report it exists. See [[feedback_auto_commit_push.md]] and [[project_salesmaker_protected_master.md]].

### Never use em-dashes or dashes as punctuation in any written content (emails, decks, messages, copy).
Never use em-dashes (—) or hyphens used as punctuation (" - ") in written content delivered to the user. Use commas, periods, parentheses, or restructure the sentence instead.

**Why:** User flagged it explicitly. Dashes read as AI-generated copy and break the natural voice he wants in outbound emails and decks.

**How to apply:** All written deliverables — emails, slide copy, LinkedIn messages, business cases, follow-ups. Applies across every project and skill. Hyphens inside compound words (e.g., "follow-up", "high-leverage") are fine; the rule is about dashes as sentence punctuation.

### Never put information you're not sure about into deliverables. When uncertain about a fact (especially PSPs, payment providers, internal infrastructure), add a disclaimer like "according to web data" or "assumptions were made when selecting current providers". Applies to ALL projects, not just deck.yuno.tools.
**Strengthened 2026-06-07:** Deck (and all deliverable) content must be 100% real and verified — only facts. NEVER assume, invent, seed a default, or pad a list to hit a target count. If a fact is not publicly verifiable, OMIT it entirely; a shorter deck of only true facts beats a fuller one with a single guess. Omission > fabrication, always. A clearly-labeled disclaimer is ONLY acceptable for a genuinely-sourced-but-estimated fact (e.g. a real third-party revenue estimate); it is NOT a license to include guesses/assumptions — those get dropped, not disclaimed.

Also (2026-06-07): ALWAYS do EXTRA research and a verification pass — don't stop at the first source. Corroborate every material fact with a second independent source (primary sources beat blogs); run a final pass over every value before committing and drop anything not actually confirmed. Encoded in the research prompts (both merchant + banking) and the web_search budget was raised (merchant 10→20, banking 6→12 max_uses).

Code enforcement (live `/api/builddeck` path, [server/lib/research.mjs](yuno-sales-pitch-maker/server/lib/research.mjs), commit see git log): prompt rewritten to "100% verifiable facts only, never seed/assume/pad" + "do extra research, corroborate with a 2nd source, final verification pass"; PSP zero-confirmed now returns an EMPTY topology (was: seed 2 region defaults); pains "up to 5" + missing-methods "up to 10" (were "exactly"); `sanitize()` no longer hard-fails on fewer-but-true counts; [SlideDiagnostic.jsx](yuno-sales-pitch-maker/src/components/slides/SlideDiagnostic.jsx) filters empty pain cards. NOTE: this only affects decks built/rebuilt AFTER the change — existing Supabase rows keep their old padded content until rebuilt. Related: [[project_pdf_vw_paper_width]], slide-4 APM geo-filter.

Never put false or unverified information into any deliverable (slide, email, deck, Supabase row, doc, business case, etc.). When you're not 100% sure about a fact — especially payment providers, internal billing infrastructure, vendor stacks, or any specific company-internal detail that isn't publicly disclosed — OMIT it; only fall back to a disclaimer when the value is a real, sourced estimate worth keeping.

**Why:** On 2026-05-04, when adding SAP to deck.yuno.tools, I listed Stripe/Adyen/Worldpay/Airwallex as SAP's PSPs based on a SAP Commerce Cloud article — but those are PSPs that SAP Commerce Cloud offers to ITS CUSTOMERS (retailers), not what SAP itself uses to bill its own enterprise customers. User caught it. Their rule: better to label something as inferred than to assert it as fact and get caught fabricating in a sales conversation. Credibility loss with a prospect is worse than visible humility.

**How to apply:** Applies to ALL projects, not just the deck — emails, business cases, research briefs, decks, Slack snippets, anything that goes to a prospect or internal stakeholder.

When data is inferred from public signals (web articles, jobs postings, press releases) rather than confirmed by the company itself, add a disclaimer like:
- "According to web data" / "Per public web signals"
- "Assumptions were made when selecting current providers"
- "Based on publicly available information"
- "Inferred from public sources — not confirmed by [Company]"

For deck slides specifically, add the disclaimer as small footnote-style text at the bottom of the slide, under the data being qualified (e.g., under the PSP topology block on SlideDiagnostic). Don't bury it in tiny gray text — it should be readable but not fight the headline.

When the underlying field can support it (e.g., a `psps_disclaimer` boolean or `disclaimer_text` field on the merchants table), prefer storing the disclaimer with the data rather than hardcoding it in the component. That way it travels with the merchant.

If you can't verify ANY of the facts a slide depends on, surface this to the user before writing the slide — don't fabricate to fill the template.

### Yuno PDF deck exports must never show vertical cursor caret artifacts (\"|\" lines) captured during Google Slides PDF export
When building Yuno decks via [[slide-builder]], [[builddeck]], or any Google Slides workflow, the user has flagged a recurring issue: PDF exports often capture text cursor (caret) artifacts as thin vertical "|" lines that appear between words on slides. Documented examples on a SpaceX / Starlink deck: lines appeared between "about" and "your business" (slide 2), between "together." and "one platform" (slide 3), between "pillars ·" and "One brain" (slide 4), between "merchant-first" and "team built by" (slide 7), and between "economy," and "together" (slide 8).

**Why:** Google Slides captures the blinking text cursor inside any text box that was last in edit / focused state at the moment of PDF export. The user said verbatim: "Asegúrate de que eso nunca salga cuando yo descargue el PDF."

**How to apply:**
- When generating decks via the Google Slides API, never leave a text box in edit / focused state at the end of the build. After updating text content, deselect or click outside the box programmatically before telling the user the deck is ready.
- When the user is about to download as PDF, instruct them to first click once on the slide canvas background (outside every text box) on any slide that was recently edited, then File → Download → PDF Document.
- After any deck build, suggest a quick visual scan post-PDF-export and a re-export if any "|" lines appear. Treat this as a QA checkpoint.
- Do NOT confuse intentional underlines or design borders (e.g., the horizontal teal underline under "global scale" on the SpaceX cover) with the unwanted vertical cursor artifacts. Only thin vertical lines that break text mid-sentence between two words are the issue.

### Slide elements must never visually overlap. Bottom-row footer stats on slide 3 (and any slide) must clear the content boxes above with safe padding.
When building Yuno decks, no element on any slide may visually overlap another. Specifically flagged: on slide 3 ("Yuno brought it all together"), the footer-row stat callouts at the bottom ("$1-2M cost to set up and manage each direct PSP connection" and "$118B lost annually to failed payments industry-wide") were overlapping the bottom edge of the two bordered content cards above them (PSP logo grid on the left and narrative text on the right). This makes the deck look unpolished.

**Why:** The user flagged this verbatim: "los números del tercer slide abajo se superponen sobre la información de arriba. Asegúrate de que eso no pase." Bottom stats must sit clearly below the cards with breathing room, not cross into them.

**How to apply:**
- On slide 3 specifically, the bottom footer stat row must end at a y-coordinate that leaves at least 40px (in a 1920×1080 frame) of empty vertical space below the bordered content boxes. If the cards extend to y=900, the footer stats must start at y=940 or later.
- General principle: every slide layout must be verified for non-overlap before declaring the deck ready. No text, icon, or chip should sit on top of another container border.
- When adapting the standard slide-3 template ([[builddeck]] / [[slide-builder]]) to a new merchant, recheck the vertical heights of the PSP grid and right-side narrative card. If either card grew due to more content, the footer stats must shift down accordingly. Do not assume the default coordinates always clear.
- Apply the same non-overlap check to every other slide, especially slides with KPI rows, footer chips, or page-number bars.

### Never use the phrase "no small feat" in any outreach email or written content
Never use the expression "no small feat" in emails or any written output.

**Why:** User explicitly flagged this as a phrase to avoid — likely sounds cliché or overly salesy.

**How to apply:** When writing cold emails, LinkedIn messages, or any prospect-facing content, avoid this phrase entirely. Use direct, natural compliments instead.

### PayPal is a wallet/APM, never a processor/PSP; never count it in PSP totals or topology chips
PayPal must always be treated as a wallet / Alternative Payment Method (APM), never as a processor / PSP / gateway. Do not list it among "PSPs", do not include it in PSP counts, and do not put it in slide-3 topology chips (which are gateways/PSPs/MoR only, see [[feedback_psps_chips_scope]]).

**Why:** German flagged that the Lightricks deck counted PayPal as one of "3 PSPs" on web checkout. PayPal Wallet/Checkout is an APM; the real processors were Stripe + Adyen (2). Miscounting it inflates the "multi-PSP no orchestrator" angle with a false fact ([[feedback_no_false_info_disclaimer.md]]).

**How to apply:** When building/QA-ing any deck, put PayPal in the `apms` list only. Fix PSP counts to exclude it (Lightricks: 2 PSPs = Stripe + Adyen). Applies to research briefs and business cases too. Related: [[project_lightricks_psp]].

### In the yuno-sales-pitch-maker PDF pipeline, never wrap PrintViewer slides in a transform:scale container. SlideBase-based slides render empty.
In `yuno-sales-pitch-maker/src/components/PrintViewer.jsx`, never wrap each `.pdf-page` in a `transform: scale(...)` container around the slide Component. The cover slide survives (it has its own absolute-positioned layout), but every slide built on top of `SlideBase` (BusinessOverview, Diagnostic, YunoSolve, ProductSuite, Dashboard, Leadership, TrustedBy, CTA, etc.) loses all body content — only the chrome (section pill + Yuno logo) survives in the PDF.

**Why:** SlideBase's outer div uses `width: 100%; height: 100%` and its body uses flex layout. The transform:scale wrapper's logical box sizing interacts with these cascades in a way that produces empty/0-sized layout for the body section. Cover doesn't hit this because every element is `position: absolute` with explicit px values.

**How to apply:** If the goal is to render the PDF at a smaller viewport to match the live tool's vw resolution (this was the failed fix from commit 38aa4d5, reverted in 2c50656), use a different approach instead:
- CSS `zoom` per-slide (like the existing `[data-pdf-root] [data-slide='leadership'] { zoom: 0.96 }` hack at `src/index.css`)
- Replace `vw`-based clamps in individual offending slides with px equivalents
- Or accept the 1920×1080 capture viewport and add targeted zoom-hack overrides to the slides that genuinely overflow

Capture viewport, @page size, and `page.pdf()` size must all stay at 1920×1080 unless the entire slide layout system is rewritten to be viewport-agnostic.

Related: [[feedback-no-dashes]] is the broader "deck rendering rules" cluster.

### Slide 3 "Today's Topology" PSP chips must only contain gateways, acquirers/PSPs, or merchant-of-record. Never list payment methods (BNPL, wallets, card networks, issuers, LPMs).
The `psps` field on the Supabase merchant row populates the "Today's Topology" chips on slide 3. Only these belong there:

- **Gateways** (Cybersource, Authorize.net, Worldpay gateway, NMI)
- **PSPs / acquirers** (Adyen, Stripe, Braintree, Checkout.com, Worldline, Elavon, Vendo Services, dLocal, Airwallex, EBANX, Cybersource, Mollie, Recurly)
- **Merchant of Record** (FastSpring, Paddle, Cleverbridge, Lemon Squeezy)

**Do NOT include in PSP chips:**
- BNPL providers — Klarna, Afterpay, Affirm, Sezzle, Tabby, Paidy, Atome, Kueski Pay
- Wallets — PayPal, Apple Pay, Google Pay, Amazon Pay, Cash App
- Card networks — Visa, Mastercard, Amex, Discover, JCB, UnionPay
- Card issuers / co-brands — Citi, Barclays, Synchrony, Capital One, Chase
- Local payment methods — Pix, OXXO, UPI, iDEAL, Konbini, BLIK, Bizum (those go in `missing_methods`)
- Crypto rails — BTC, USDT, Monero (those are alt-rails, not PSPs)

**Why:** Slide 3 is meant to show the merchant's *acquiring/processing topology* so the Yuno pitch can attack things like single-PSP dependency, gateway lock-in, MoR margin leakage. Mixing in BNPLs and wallets dilutes that signal and confuses prospects who can clearly see PayPal/Klarna aren't acquirers.

**How to apply:** When walking the PSP decision tree:
1. Filter the research for *who actually authorizes/settles the card transaction* (the acquirer or gateway) or *who is named on the receipt* (MoR).
2. BNPL/wallet/issuer evidence does NOT count toward confirmed PSP count for the rule "2+ confirmed → no disclaimer."
3. If only BNPLs and wallets are publicly known and zero acquirers are confirmed, treat that as the "Zero PSPs confirmed" branch and apply the disclaimer.
4. **Single-PSP confirmed (1 acquirer/gateway/MoR found publicly): add the "only one we found" disclaimer.** Use this verbatim pattern: `Only payment processor publicly disclosed for {Company}. Additional providers may exist but were not found in public sources.` This supersedes the original rule that single-PSP topology stays disclaimer-free — the user wants the "publicly disclosed" caveat in place so the slide reader knows the chip count reflects research limits, not necessarily the merchant's real topology.

**Past slip-ups to learn from:**
- Costco (commit 4f339a4): added Affirm (BNPL) and PayPal (wallet) alongside Elavon. Only Elavon belongs.
- Gap Inc. (commit 3f2ed3d): added Klarna + Afterpay + PayPal alongside Adyen. Only Adyen belongs.

Both got corrected after user flagged on 2026-05-11. The single-acquirer reality (Elavon for Costco, Adyen for Gap Inc.) is actually a *stronger* Yuno talking point than a padded chip list.

### \"+12% auth uplift\" and \"20–30% decline recovery\" are flagged as fabricated; use Yuno's published figures 7% uplift / 30% recovered revenue (or verified client figures like McDonald's +4.7%/18 markets/$3.2M)
The deck QA reviewer flagged the default impact tiles "+12% average auth-rate uplift" and "20–30% decline recovery" as fabricated on six consecutive decks (Sep 2026). The approved replacements are Yuno's published figures: **7% authorization uplift** and **30% recovered revenue** (both published on y.uno). Verified client figures are also acceptable: McDonald's +4.7% acceptance across 18 markets, $3.2M additional revenue.

**Why:** The +12% / 20–30% numbers have no public source and keep failing deck QA; shipping them risks credibility with prospects. See [[no-false-info-disclaimer]].

**How to apply:** On any deck (SlideYunoSolve `impact.stat*`, SlideCTA `proof.*` tiles), override the defaults via the deck's `business_overview.deckOverrides` (buckets `yunoSolve` and `cta`) with +7% / 30%, and add the source line "> Yuno published figures · y.uno". Airalo and gamma-ai are already fixed this way. Also flagged repeatedly: "Reconciliation · One ledger across every PSP" must be footnoted as roadmap (settlement, payout and fee reconciliation is not GA) — override `arch.feature2` → "Reconciliation*" + `arch.note`, and `productSuite.pillar3.item1.desc` → "Unified visibility across providers…".

### Standard top-down methodology for structuring any Yuno presentation/deck — Requirement, Benefit, Proof
The methodology German uses to build presentations top-down is **Requirement, Benefit, Proof (RBP)**:

1. **Requirement** — diagnose the problem: what the client actually needs/is struggling with (the pain, the gap).
2. **Benefit** — organize the solution: what Yuno delivers that addresses that requirement.
3. **Proof** — back it with evidence: verified data, case studies, or facts that substantiate the benefit.

**Why:** This is German's explicit, standing instruction for how decks/presentations should be structured — top-down, one argument at a time, each moving from diagnosis to solution to substantiation. He corrected a prior guess (McKinsey issue-tree / Minto SCQA) — RBP is the actual name, not those.

**How to apply:** Use this as the default narrative/section structure whenever building or reviewing a Yuno deck, business case, or pitch (e.g. via [[project_meeting_brief_skill]], slide-builder, business-case skills). Each slide or slide-group should be checkable against Requirement → Benefit → Proof rather than a generic problem/solution layout. Combine with [[feedback_no_false_info_disclaimer]] — the "Proof" step must always be verified facts, never assumed or padded.

### German wants every reply in English, regardless of the language he writes in; switch languages only when he explicitly asks for another one in that message
Always answer German in English, even when he writes in Spanish. The only exception is when he explicitly says to reply in another language; that applies to that request only, then go back to English.

**Why:** Standing instruction given on 2026-10-06 ("de ahora en adelante quiero que siempre me contestes en inglés, independientemente de cómo te hable yo").

**How to apply:** This covers chat replies only. Deliverables keep the language the audience needs (emails to Cruz Verde, Palco, Línea Directa, UNICEF stay in Spanish; outreach to US accounts in English). See [[feedback-email-no-links-sober]] and [[feedback-email-length-senior]] for the writing rules that still apply to those pieces.

### German's preferred Google Sheets look (copied from his \"SF AI Prospects – Yuno ICP (Oct 2026)\" sheet) and the working way to apply formatting via the Sheets API service account
Reference sheet: `1QGS58IUs-Zhdu_DqML4ILuKkJZ3apew3sfUWhzo4sAk` ("SF AI Prospects – Yuno ICP (Oct 2026)", tab Prospects).

House format to replicate on every Google Sheet deliverable:
- Header row: fill #10284A (navy), Roboto 10 bold white, left + middle aligned, wrap, row height ~30 px.
- Body: Roboto 10, wrap text, thin black borders on every cell (inner + outer), URL columns in blue (#0000FF). First column bold is fine.
- Freeze first row and first column (freeze at B2). Hide gridlines. Explicit column widths (roughly 130 to 430 px by content). No filter, no banding.

How to apply (works, used 2026-10-06 on the airlines sheet):
1. Share the sheet as writer with `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` (Drive MCP share_file).
2. Python with `google.oauth2.service_account` + `~/.config/gsuite/sa.json`, scope spreadsheets, then `spreadsheets().batchUpdate` with updateSheetProperties (frozen rows/cols, hideGridlines, title), repeatCell (header + body formats), updateBorders, updateDimensionProperties (widths, header height). The Drive MCP create_file (CSV) only loads data, never formatting, so formatting is a second step.
3. `tools/gsuite/gsuite.py` uses a user token (~/.config/gsuite/token.json) and has no formatting command; use the SA script instead.

**Why:** German asked "dale ese formato al doc q se verá ordenado" right after receiving an unformatted CSV-born sheet; he wants deliverables to look like his own sheets without extra asks.
**How to apply:** After creating any Google Sheet for German, immediately apply this format in the same turn. Related: [[deliverables-google-sheets]], [[client-data-requests-simple]], [[slides-api-token-dead]].

### Decks and business cases speak in one currency (USD); never print amounts in local currencies (₩, €, PKR, C$...), use USD or currency-free metrics
German's rule (2026-09-16, Higgsfield deck): every figure in a deck is in USD. No local-currency amounts anywhere, even on country slides.

**Why:** the reader compares markets side by side; mixed currencies break the comparison and look unfinished. Converting with an assumed FX rate adds an unsourced number.

**How to apply:** when a verified stat only exists in local currency (₩1.1T/day easy-pay, €157B iDEAL, PKR 23.3T Raast, C$554B Interac), swap it for a currency-free metric from the same source (users, transaction counts, shares, growth rates) rather than converting. Phrases like "local AED / KRW acquiring" are fine: they describe local-currency processing, not amounts. Related: [[project-higgsfield]], [[feedback-no-false-info-disclaimer]].

### Slide 2 (business overview) must always be fully populated, never sparse
Slide 2 ("What we know about your business" / SlideBusinessOverview) must ALWAYS be complete: revenue, description, recent catalyst, commerce footprint, top operating countries (with flags + shares), alternative payment methods accepted, and business lines. Never leave it sparse/empty.

**Why:** Auto-built decks (runtime /builddeck → Supabase row) often leave the `business_overview` column thin, so the slide renders mostly empty and looks unfinished in front of a prospect.

**How to apply:** First check what the Supabase row already has (open the live deck). Two cases:
- **Supabase content is good but a section is missing** (common: countries + apms): do NOT use forceLocalOverview (it would clobber the good content with weaker estimates). Instead add a partial merge: `slide-overrides.json` → `"<slug>": { "slide2": { "countries": [...], "countriesSource": "...", "apms": [...] } }`. The reader does `{ ...row.business_overview, ...overrides.slide2 }`, so listed keys are ADDED/overridden and everything else is preserved. (Despite the _doc saying "countries only", apms and any overview key also merge.)
- **Supabase content is genuinely empty/wrong:** add the full slug entry to `business-overviews.json` and set `forceLocalOverview: true` so the local overview fully replaces the row.

Research real figures; mark estimates with `estimated:true` + a `footprintNote`/`countriesSource` disclaimer per [[feedback_no_false_info_disclaimer]]. For app-only merchants (e.g. Dream Games / Royal Match), "countries" = top app-store revenue markets and "apms" = store billing rails (Apple App Store IAP, Google Play Billing, Amazon Appstore, Samsung Galaxy Store).

**Omnichannel / retail merchants (PetSmart, Nordstrom, Costco, etc.):** one of the footprint anchors must ALWAYS be the **digital share of sales** (e-commerce/digital vs in-store %), real or estimated. It is the single most payment-relevant scale metric for a brick-and-mortar retailer, so never omit it. If no exact figure is public, use a sourced estimate and mark it as such.

### WebSearch tiene tope de 200 búsquedas por sesión, compartido entre todos los subagentes; planear lookups masivos (LinkedIn) en pasadas de ≤180 y priorizar
El 5-oct-2026 lancé 6 subagentes en paralelo para buscar LinkedIn de 304 personas (Money20/20 × TCL). El tope de 200 búsquedas por sesión se agotó en minutos y ~180 personas quedaron sin buscar; los agentes intentaron curl contra buscadores públicos y casi todos los bloquearon (solo Yahoo Japan y Seznam respondieron).

**Why:** el presupuesto es por sesión (variable CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION, la cambia German, no yo), no por agente.

**How to apply:** antes de un lookup masivo, ordenar por prioridad (Title Tier 1 y 2 primero) y limitar la pasada a ~180 búsquedas, una por persona. Query que mejor funcionó para LinkedIn: WebSearch con `allowed_domains: ["linkedin.com"]` y "Nombre Apellido" + empresa + fragmento del cargo; aceptar solo si el título del resultado muestra nombre + empresa o cargo. Lo no buscado queda vacío y se marca para una segunda sesión. Relacionado: [[project_money2020_lv2026_tcl_match]].
