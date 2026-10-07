# German Tatis · Full Claude memory export

Exported 2026-10-06 from Claude Code (project GTMCoding). 151 memories: 1 user, 35 feedback, 10 reference, 105 project.

Each entry keeps its original slug (useful when a memory links to another with `[[slug]]`), its one-line description and the full body. Dates inside entries are absolute. Everything here was true when written; verify anything time-sensitive before acting on it.

## Index

### Who German is
- **user_german_profile** · Who German is — Account Executive (senior) at Yuno, SDR/outreach workflows

### Standing rules (how German wants Claude to work)
- **Always commit and push automatically** · After completing any code/file changes, automatically git commit and git push without asking the user
- **Always include slide content in business-case** · When /business-case skill is activated, always present the slide guide content (slides 4-7) alongside the Excel generation
- **feedback-cc-handoff-reply-pattern** · Cuando Magdalena o Samuel Carreño ponen a German en CC en correos a prospectos, German entra al hilo con un reply de estructura fija; plantilla y reglas
- **feedback-client-data-requests-simple** · Pedidos de datos a clientes = Google Sheet de una sola hoja, campo a la izquierda y respuesta al lado; nada de workbooks de muchas hojas
- **client-reported-metrics** · In client-facing business cases use the metric the client reported (e.g. Palco ticket promedio $37.09), never a value we derived that contradicts it; raise the discrepancy separately
- **Payments Concierge shorter in email2** · Always write a shorter version of the Payments Concierge paragraph in email2 — keep it concise
- **feedback_cost_objection_reply_pattern** · Pattern German likes for replying to a "too expensive / can't justify the cost" rejection, modeled on Sean Calabro's FlightHub reply (oct-2026) and reused for Flair
- **Cover slide uses yuno + merchant lockup** · All decks render the cover with a top-left lockup (yuno wordmark | merchant logo) and no "Hello {Company} team!" greeting. The lockup is the default.
- **deck-changes-deploy-neverland** · Every deck content change (slide-overrides.json, business-overviews.json, slide component edits) must be deployed to Neverland/internal-tools, not just pushed to GitHub/Railway
- **feedback_deck_edits_scoped** · Deck edit requests must apply ONLY to that specific deck, never leak to other decks
- **feedback_deliverables_google_sheets** · Listas y cruces de datos se entregan en Google Sheets (vía conector de Drive), no en Claude Docs ni artifacts
- **feedback_drive_download_to_disk** · Para leer un Google Sheet grande completo sin OAuth: download_file_content como xlsx → el harness lo guarda en disco → decodificar base64 con Python y abrir con openpyxl
- **Email 1 — no name dropping** · Email 1 (opener) must always use the Yuno description boilerplate, never client name dropping. Name dropping is for Email 2+.
- **feedback_email_length_senior** · Email 1 and Email 2 must be shorter, denser with value, senior AE tone (same voice)
- **feedback-email-no-links-sober** · Correos a prospectos que German envía él mismo van sobrios y sin links ni menciones de "sección X del deck"; German agrega el link o adjunto a mano
- **feedback_gmail_update_draft_detaches_thread** · Gmail MCP update_draft desprende el borrador del hilo original; para cambiar un borrador de respuesta, recrearlo con create_draft + replyToMessageId
- **gmail-workflow-central** · German quiere a Claude siempre dentro de su Gmail (conector claude.ai); leer threads y dejar drafts sin preguntar
- **feedback_linkedin_shorter** · LinkedIn outreach messages should be a bit shorter than the standard email version
- **feedback-meeting-brief-structure** · Meeting briefs — agenda y open questions SIEMPRE al final (ahí arranca German a tomar notas); TL;DR battle card al inicio
- **feedback_never_duplicate_decks** · Never create a duplicate deck/merchant; if it already exists, just say so
- **feedback-no-dashes** · Never use em-dashes or dashes as punctuation in any written content (emails, decks, messages, copy).
- **Never put false info — disclaimer when uncertain** · Never put information you're not sure about into deliverables. When uncertain about a fact (especially PSPs, payment providers, internal infrastructure), add a disclaimer like "according to web data" or "assumptions were made when selecting current providers". Applies to ALL projects, not just deck.yuno.tools.
- **no-pdf-cursor-artifacts** · Yuno PDF deck exports must never show vertical cursor caret artifacts (\"|\" lines) captured during Google Slides PDF export
- **no-slide-overlap** · Slide elements must never visually overlap. Bottom-row footer stats on slide 3 (and any slide) must clear the content boxes above with safe padding.
- **Never use "no small feat** · Never use the phrase "no small feat" in any outreach email or written content
- **feedback_paypal_not_processor** · PayPal is a wallet/APM, never a processor/PSP; never count it in PSP totals or topology chips
- **feedback-pdf-no-transform-scale** · In the yuno-sales-pitch-maker PDF pipeline, never wrap PrintViewer slides in a transform:scale container. SlideBase-based slides render empty.
- **PSP chips = gateways/PSPs/MoR only** · Slide 3 "Today's Topology" PSP chips must only contain gateways, acquirers/PSPs, or merchant-of-record. Never list payment methods (BNPL, wallets, card networks, issuers, LPMs).
- **published-stats-only** · \"+12% auth uplift\" and \"20–30% decline recovery\" are flagged as fabricated; use Yuno's published figures 7% uplift / 30% recovered revenue (or verified client figures like McDonald's +4.7%/18 markets/$3.2M)
- **rbp-methodology** · Standard top-down methodology for structuring any Yuno presentation/deck — Requirement, Benefit, Proof
- **feedback-reply-in-english** · German wants every reply in English, regardless of the language he writes in; switch languages only when he explicitly asks for another one in that message
- **sheet-house-format** · German's preferred Google Sheets look (copied from his \"SF AI Prospects – Yuno ICP (Oct 2026)\" sheet) and the working way to apply formatting via the Sheets API service account
- **feedback-single-currency-usd** · Decks and business cases speak in one currency (USD); never print amounts in local currencies (₩, €, PKR, C$...), use USD or currency-free metrics
- **feedback_slide2_always_complete** · Slide 2 (business overview) must always be fully populated, never sparse
- **feedback_websearch_budget_shared** · WebSearch tiene tope de 200 búsquedas por sesión, compartido entre todos los subagentes; planear lookups masivos (LinkedIn) en pasadas de ≤180 y priorizar

### Reference material (positioning, pricing, personas, tools)
- **reference_buyer_personas** · Yuno's 13 buyer personas — tailor any outreach/email to the persona German names
- **reference_colombia_processors** · Procesadores de tarjetas en Colombia verificados el 29-sep-2026 (tarifas públicas, qué está conectado a Yuno, Bre-B recurrente, DRUO); no existe dato público de aprobación por procesador
- **reference-money2020-vegas-2026-supercar-event** · Evento de Yuno y PayPal en Money20/20 Las Vegas 2026: 'Payments Unlocked: An exclusive supercar experience' en SpeedVegas; invite Luma luma.com/10q4wvgc; usar para invitar a prospectos que van a Vegas
- **rfp-training-guide** · Google Doc \"Payments & Yuno: Guía de Entrenamiento\" (glosario + productos + RFPs + call Riot) para entrenar a German en terminología técnica de payments
- **reference-salesops-legal** · Canal Slack #salesops-legal (C07QPMCDMUH) = donde German pide NDAs y documentos legales; contacto Ivvy Soberay; formato y tono de sus mensajes
- **reference-subscriptions-stats** · Where the Yuno Subscriptions engine stats come from (launch deck sep-2026, Reface 26.49 pp case via Payments Concierge), what is live vs roadmap, and Jarrett's gap list; use before quoting any subs number externally
- **yuno-agents-platform** · Cómo funciona la plataforma interna Yuno Agents (ai.agents.y.uno): owner + admins por agente, transferencia de ownership vía equipo plataforma en #yuno-agents, Personal vs Service, Private/Public
- **reference_yuno_positioning** · Official Yuno one-liner positioning / pitch to use in decks, emails, and deliverables
- **yuno-pricing** · Yuno's standard product pricing model — $50K processed free, then $0.05 per transaction
- **yuno-pricing-policy** · Yuno Products Pricing Policy (Finance, Laura Galan): list/minimum price por producto, zonas de aprobación green/yellow/red, segmentación V1-V5 x M1-M4, tranches vs tiers, credits, MMG, billing terms. Consultar SIEMPRE al construir propuestas o quotes

### Accounts, deals and ongoing work
- **project_ai_apps_batch_2026_06_17** · Batch of 5 AI/consumer-app SDR research briefs (2026-06-17) pending next steps (decks/outreach)
- **airalo-deck** · Airalo deck fix pass 2026-09-09 — thesis is \"orchestration is in, coverage is not\" (Stripe + partial orchestration layer confirmed); revenue ~$150M FY2023 Forbes; BeyondOne proof slide slug-scoped after The Solve
- **airlines-targeted-list** · Google Sheet \"Airlines Targeted · Oct 2025 to Oct 2026\" (37 airlines, leads, head of payments, last contact) built 2026-10-06 from Gmail, Calendar, NORAM/TCL/Recovery sheets; CSV copy in repo
- **allegiant-signed** · Allegiant Air signed with Yuno (German confirmed 2026-10-06) and acquired Sun Country; deal was run by Samuel Vieira and Adam Mawdesley after German's Aug to Nov 2025 outreach
- **project-american-red-cross** · American Red Cross — call inbound 2-sep-2026 (Susana SDR) con Carlos Carneiro (Merchant Services, seniority sin confirmar); sin recap ni follow-up después; brief en data/research/american-red-cross-meeting-brief-2026-09-02.md
- **project-anthropic-shaa** · Anthropic / Shaa (shaa@anthropic.com), hilo de Magdalena "Yuno's Subscription Engine for Anthropic" (Gmail 1a0a68b971b71667); Justo y Magda sin respuesta; German entra por email 6-oct tras WhatsApp
- **project-appmaking** · Appmaking/Wowmaking (Cyprus app group, AstroSoul/Atrix) — demo done 2026-09-04, live Solidgate vs Truegate bake-off on web funnel, next step tech deep dive + proposal
- **project-arrive** · Arrive (Arrive Recommerce, arrive.com) — Amit Chhabra (Chief Architect for Payments) call 29-oct-2026 vía Susi; Debbie Guerra (Head of Payments) va a Money20/20 Vegas; pedido de intro para café en borrador
- **project_babbel** · Babbel (Lesson Nine GmbH) — multi-PSP (Adyen+Stripe) no orchestrator; orchestration + churn-recovery angle
- **project_bending_spoons_psp** · Bending Spoons payment stack + Yuno angle (research 2026-06-17)
- **project-bounce** · Bounce (luggage storage, bounce.com): campaña de Samuel Carreño 28-sep-2026 a 11 contactos con German en CC; 11 replies en borrador Gmail 29-sep; contacto previo real = correo a Léa Brutkiewicz oct-2025 que declinó sin dar razón; stack Stripe Connect
- **project_british_airways** · British Airways web deck (/m/british-airways, vertical merchant, 11 slides): edición de texto 21-sep-2026 aplicada solo en Supabase; dónde vive cada campo; pendientes visuales (detalle 01 slide 4 recortado, Expected Impact +12%/20–30% intacto)
- **business-case-tripadvisor-deck** · New standalone \"Business Case TripAdvisor\" report deck in yuno-sales-pitch-maker (slug business-case-tripadvisor), ported from an external PDF; deployed live
- **project_cambly** · Cambly online English tutoring — Stripe+EBANX, local APMs only in Brazil; BC focused on missing APMs per market
- **cellpoint-whitelabel-deal** · CellPoint Digital (no \"Sellpoint\") — pivot 1-sep de full white-label ($50k) a propuesta liviana de APM connectivity ($15k/mes + rev-share 50/50 O integration fee $500)
- **project_chai_ai_psp** · Chai AI (Chai Research) payment stack + Yuno angle (research 2026-06-17)
- **project-chess-com** · Chess.com / Sean Walkinshaw (Sr PM Payments & Pricing, Texas): infra work late Q1 2027, vault first (Basis Theory), shortlist Yuno/Checkout.com/Stripe/Global Payments; touch base Dec-2026; one-pager Yuno vs Basis Theory sent 8-sep
- **project-cobrana** · Cobrana (Perú, cobros por WhatsApp sobre Kashio, 2 fundadores) — intro vía Isabella Ponce; calls 21 y 24-ago-2026 con Gabriel Shimabuko; sin seguimiento desde entonces; brief en data/research/cobrana-meeting-brief-2026-08-21.md
- **project-cruz-verde** · Cruz Verde Colombia (droguerías, Femsa) — Andrés Guzmán (Ecommerce), Michael Vargas (coordina), Sandra P. Vargas, Adriana Buitrago (lleva el NDA); Mercado Pago único, ~60% PSE, 100K tx/mes; propuesta v1 24-sep $13,750/mes; NDA: los 5 documentos de Yuno ENTREGADOS (formulario firmado por JPO vía DocuSign y enviado por JP Pantoja 5-oct en hilo aparte); Michael pidió a Adriana crear el NDA 5-oct; esperando borrador de NDA de CV; info del BC (xlsx 29-sep) sin respuesta; propuesta v2 (tiers, pesos, BC sin L4/L5) SIGUE PENDIENTE de Yuno; correo de pendientes en BORRADOR 6-oct
- **project-curology** · Curology deck — slide 2 lives in Supabase business_overview column (precedence over local JSON); card-only checkout is the lead angle
- **project_deck_edit_button** · Self-serve \"Editar deck\" button feature — flow, files, and pending one-time setup
- **project_deck_languages** · yuno-sales-pitch-maker supports 4 deck languages (en/es/pt/fr) and how to add more
- **project_deck_override_layer** · Per-deck copy override layer — how any vertical-deck slide text is edited live via Supabase, no deploy
- **project_deck_tools_handover** · Deck tools (yuno-sales-pitch-maker + Neverland + deck counter) are being handed over to Magdalena Torrealba and Yamin Lahmeur (Sep 2026); they will replicate the tool in a new repo/Supabase and own it. Handover doc lives in docs/HANDOVER.md and as an artifact.
- **project-doordash-aj-tus** · DoorDash — A.J. Tus (Head of Payments & FinTech Partnerships) es la puerta; respondió una sola vez (sep-2025) y derivó a Alodie Taveras; German lo contactó él mismo el 5-oct-2026 para Money20/20 (borrador de Claude eliminado)
- **doTERRA uses Cybersource** · doTERRA's PSP is Cybersource, relevant for any outreach or BC referencing their payment stack
- **project_eve_events_agent** · Agente "Eve" en Yuno Agents (ai.agents.y.uno) para buscar eventos gratis en SF, registrar a German y avisarle por correo; hoja de Google "SF Events Feed · Eve" como puente con el playbook
- **eventbrite-bakeoff** · Eventbrite orchestrator eval — call 2026-08-04 hecho: Paul Pasion en su ÚLTIMA SEMANA en Eventbrite (confirmado 2026-08-11, antes se estimaba ~08-18), decisores = Noe/Giacomo/Filippo (Bending Spoons Milán, ya en CC directo); MNDA + materiales custom antes del vie 2026-08-14; Justo en Milán fin de agosto
- **eventbrite-deck** · Eventbrite en 2 formatos: Deck.pptx (29 slides, con ⚠VERIFY pendientes) + deck web /builddeck (23 slides, 13 custom slug-scoped, SOLO claims documentados); deadline 2026-08-14
- **project_experian** · Experian (DataCrédito Colombia) deal; Carlos Falla (PM) + Cristian Vargas (Midatacrédito) + Milena Olaya (operaciones); prioridades 29-sep = débito a cuentas (Davivienda, Grupo Aval), alternativa a PayU en tarjetas, Bre-B tokenizable; implementación desde abril 2027; follow-up 29-sep en borrador Gmail; conciliación con Milena por agendar
- **project_fanduel** · FanDuel deck + research — US
- **project-fareportal** · Fareportal (CheapOair/OneTravel) deal state, Tom Spagnola champion, Manish Kumar Sharma owns payments budget, 2027 supplier window opened July 2026
- **project_fc_barcelona** · FC Barcelona — licitación de sistemas de pagos pendiente desde nov-2025; Yuno homologado en portal de proveedores + NDA mutuo firmado (ene-2026); Àlex Castelló (Sistemes de Pagaments i Blockchain) y Arnau Alcaraz (compras) son los contactos; pliego pospuesto 3 veces; sin respuesta desde 17-jun-2026
- **project_flair_contacts** · Flair Airlines buying committee + meeting context for Yuno orchestration pitch
- **project_flighthub** · FlightHub (Montreal OTA) — Anna-Lena Schlenner contraparte; Nick Hart CFO; sin network tokens = hook; volúmenes REALES 3-sep (500-800K tx/mes, 80-92%, ~$800 CAD); presencial 22-sep HECHO (Will, todo es precio); deck final 24 slides $10K + tranches; respuestas Jarrett retries/disputes 22-sep; borrador post-presencial en Gmail pidiendo call 23-sep; ver bloques 22-sep
- **gamma-deck** · Gamma (never \"Gamma AI\", slug gamma-ai) deck fix 2026-09-09 — Stripe sole PSP (public case study), never rip-and-replace framing; India 10.8% largest market, Gamma reported 22% revenue lift from UPI; OpenAI logo on proof wall
- **project-gcloud-cli** · Google Cloud CLI instalada en la Mac de German (22-sep-2026) con Python 3.12 vía uv; proyecto GCP gtm-claude-tools-260922 en su Gmail personal para las integraciones de Sheets/Slides/Docs
- **project-genspark** · Genspark AI (MainFunc) — Winnie Wei (Head of Finance) único contacto; Stripe único; RESPONDIÓ 5-oct: esta semana no (SF Tech Week), equipo volcado en implementar NetSuite; respuesta de German en borrador proponiendo presencial semana del 26-oct
- **project-godaddy** · GoDaddy — Sunil Joshi (Director PM Payments, SF) respondió a la campaña BC de Magdalena; café presencial en SF por agendar
- **gofundme-marketplace** · GoFundMe is Yuno's first live Marketplace-solution merchant (Feb 2026) — Stripe+Adyen+Tabapay, splits+recipients+transfers; PayPal marketplace in build; the reference for platform deals
- **project-gopuff** · Gopuff deck — Stripe (payouts) + Forage (EBT/FSA-HSA) confirmed, consumer acquirer unknown; slide 2 lives in Supabase business_overview column
- **project_gsheets_mcp** · Google Sheets editing is wired up via the gdrive MCP server — how to use it and where the config lives
- **project_hbo_max** · HBO Max / Warner Bros. Discovery — ya orquestan con Spreedly (+ Adyen, Checkout.com, iyzico como SDKs separados); Ashwyn Singhal (Sr Director Product Payments, NYC) = decisor global, Karime Velazquez (Payments Manager LATAM, CDMX, ex-PPRO) = puerta LatAm; BC $15M/año enviado 20-ago sin respuesta; follow-up in-person ENVIADO 17-sep-2026
- **headshots-con-camisa-yuno** · Pipeline tools/swap_shirt.py para poner la camiseta negra Yuno a fotos de equipo (Headshots/); bloqueado 22-sep-2026 por falta de API key de modelo de imagen
- **project_hertz** · Hertz account state — single-PSP Stripe angle, 13 active leads, John March dropped
- **project-higgsfield** · Higgsfield AI research brief 2026-09-16 (supersedes 2026-03-27); Stripe-only at $700M annualized revenue, India/Korea/Brazil cross-border, payment roles open, score 14 High
- **project_hostinger** · Hostinger (hosting, Lituania) — demo HECHA 24-sep-2026: Paulius quiere empezar por INDIA (Razorpay+BillDesk bajo una integración, 2º mercado) y vault-as-a-service aparte; ~2M tokens, NTs bajo su propio TRID; billing sigue in-house; 3 correos ENVIADOS tras la demo (recap 24-sep, redline NDA 24-sep, token migration de Dirk 25-sep) SIN respuesta; NDA mutuo con redline de Ivvy en manos de Hostinger, sin envelope nuevo; India prometida por escrito en \"a few days\" pero interno ~8-oct; FUP de German en borrador Gmail 30-sep (India kick-off 1-oct, NDA, working session 13/14-oct); ⚠️ el hilo de la demo estaba en la Papelera y se restauró el 30-sep
- **project_lightricks_psp** · Lightricks payment stack + Yuno angle (research 2026-06-17)
- **project-linea-directa** · Línea Directa (Colombia, Grupo Elede; venta directa de moda) — inbound vía Susana Awad; Luis Paternina (Dir. Tesorería) + Jesús Cubides; 300K tx/mes CO + 25K PE; llamada 30-sep HECHA; propuesta Google Slides 30-sep (20 slides, sin BC): platform $7.5K + compromiso $7.5K (125K tx) = mínimo $15K/mes, $0.06/$0.05 = $25,250/mes a 325K; pendiente enviarla y confirmar Dale
- **localiza-andre-aires** · Localiza re-engagement — André Aires, LinkedIn group message with Alejandro after missed H1 call
- **lucky-agent-yuno-agents** · Lucky" = agente creado en la plataforma Yuno Agents (2026-09-09); deal strategist BD entre discovery call y demo; produce MEDDIC doc + account plan desde transcripts/Granola + research
- **project-lululemon** · Lululemon account — Eric Mei (PM Payments) sole contact; NA PSP assessment is the door; Mexico company-operated (direct) since Sept 2024, lululemon.mx
- **project_magdalena_bc_campaigns_sep_2026** · Campañas de business case de Magdalena (Magnific/Freepik, T-Mobile, Best Buy) donde German va en CC; 26 follow-ups ENVIADAS 17-sep 17:07-17:15 UTC (antes decía en borrador) desde 2026-09-17, cero respuestas
- **project_mcafee_psp** · McAfee payments research — MoR (Digital River) collapse + in-house billing build = lead angle
- **project-meeting-brief-skill** · Skill nuevo de meeting briefs (v2) en construcción — plantilla basada en el brief de Riot optimizada; ejemplo demo en Google Doc; pendiente escribir el skill
- **milo-intro-routine** · Rutina cloud \"Milo Intro-Reply (Gmail)\" (trig_01SW3DdQ2gYYkPgpGLkp6ujf) corre cada hora L-V 8am-6pm COT; ejecuta Milo/intro-reply-single.md del repo GitHub; Gmail conectado a nivel claude.ai
- **project_money2020_lv2026_tcl_match** · Money20/20 Las Vegas 2026 (18-21 oct): cruce de la lista de asistentes de Susana contra la TCL; Google Sheet entregado 5-oct; segunda pasada de LinkedIn pendiente
- **project-money2020-must-talk-list** · Money20/20 Las Vegas 2026 (18-21 oct): lista 'sí o sí' de German cruzando asistentes × TCL × deals propios × dueños internos; quién NO tocar porque ya tiene dueño en Yuno
- **neverland-migration** · Decks app DEPLOYED live en Neverland (decks.internal-tools.y.uno, 2026-07-30); service-role key OK (2026-08-03); Railway sigue como dominio de prospectos; pendiente ANTHROPIC_API_KEY + export Railway + OAuth SecOps
- **project_neverland_pdf_export_broken** · PDF export (/api/pdf/:slug) fails on Neverland (decks.internal-tools.y.uno) with a browser-level connection error, while it works fine on Railway
- **nyt-gus-jacobs** · LinkedIn outreach to Gus Jacobs at The New York Times; NYT already orchestrates payments
- **palco-ticketing** · Palco (ex Palco4, pal.co) white-label ticketing ES+LatAm; deal ACTIVO: demo 9-sep + deep dive 15-sep hechos; reunión de PROPUESTA lun 21-sep 11:00 COT con Patricio+Alfonso+Fernando (+Miguel tentativo); resumen completo en Deals/Palco/palco-deal-summary-2026-09-16.md; TPV $457M, aprobación MX 56-60%; cuentas de procesamiento son de sus clientes
- **patreon-kritika** · Patreon outreach — Kritika Rooney-Cespedes (Head of Payment Ops); warm but slow, moving to email
- **project_pdf_vw_paper_width** · Why deck PDFs overflowed vs the live link, and the 1440px-page fix
- **project-peacock** · Peacock / NBCUniversal account state (Brendan Callinan silent since Jul-2026), verified stack (Spreedly vault + Adyen), current prices post 18-ago-2026, and the Subscriptions one-pager review of 18-sep-2026
- **project-pedidosya** · PedidosYa (PeYa): oportunidad B2B de Collections con Belén Casaret (cobro de deuda de partners, conciliación de 15 bancos, pago en el portal de vendors); 1ª llamada 29-sep-2026 hecha, deep dive con Fanny propuesto 8 o 9-oct; stack Spreedly + dLocal, split Uber/SSW
- **project_perplexity_psp** · Perplexity AI payment stack + Yuno angle (research 2026-06-17)
- **project-pipeline-sync** · Pipeline Sync Apps Script (TCL Final List -> Deal Status GTM cada 15 min); manual + fuente en Lists & ICP/Pipeline Sync; owner Magdalena Torrealba
- **project_polymarket_psp** · Polymarket's primary payment processor is MoonPay (fiat on-ramp)
- **project_praktika_psp** · Praktika AI language app — 100% Apple/Google IAP, zero web checkout; App Store fee-recovery BC
- **railway-stale-sep-2026** · deck.yuno.tools (Railway) dejó de publicar commits de main desde ~8-sep-2026; bundle vivo index-DahtyNRA.js tiene agosto pero no septiembre; Neverland es el target real
- **railway-watchdog-routine** · Watchdog de deck.yuno.tools reescrito 2026-08-03 en modo SILENCIOSO (solo Gmail draft, NUNCA calendario/push) tras ~65 falsas alarmas; el sandbox cloud no alcanza deck.yuno.tools (curl exit 56)
- **project_replika_psp** · Replika (Luka Inc) payment stack + Yuno angle (research 2026-06-17)
- **project-riot-games** · Riot Games — call 2026-07-31 con Andreas Borngraeber hecho; core middle tier CERRADO (CEO ex-CFO), puerta abierta = physical goods/mail order en 1-2 años vía RFP; jugada activa = entrar junto a Airwallex
- **project_salesmaker_protected_master** · yuno-sales-pitch-maker — deploy branch is main (Railway auto-deploys); master is a protected, unused decoy
- **samuel-knowledge-transfer** · Prompt sent to Samuel Vieira's Claude (Oct 2026) to brain-dump its payments/RFP/research training; German will paste the output back for ingestion
- **sean-calabro-manager** · Sean Calabro, nuevo Head of North America de German (ex-Worldpay); su estilo de gestion, expectativas y estructura de trabajo del equipo
- **project-sf-relocation-fall-2026** · German, Samuel Vieira y Joaquin Mann viven en San Francisco del 28-sep al 4-nov-2026 (Airbnb aprobado por Justo y Sean el 17-sep); planear reuniones presenciales Bay Area y horarios PT
- **project-sf-trip-budget-sheet** · Google Sheet del presupuesto día a día del viaje de German a San Francisco (28-sep → 4-nov-2026), supuestos clave y cómo regenerarlo
- **project-sf-trip-playbook** · Playbook del viaje a SF (28-sep a 4-nov-2026) con pestaña Interactive Calendar; cómo se construye, reglas que pidió German y hallazgos verificados de eventos y precios
- **project_skydance** · Skydance = nombre del grupo Paramount + Warner Bros. Discovery desde el cierre del 6-oct-2026 (David Ellison CEO, Ynon Kreiz co-CEO); incluye Paramount+ y HBO Max. Cuenta Paramount en Salesforce: OPP / LOST, la trabajan Alejandro Albarracín + Samuel Carreño; bloqueo = integración con Recurly. HBO Max es la cuenta de German
- **project-slides-api-token-dead** · Google Slides API token (~/.config/yuno-slides/token.json) dead since 2026-09-18: its GCP project 304613953104 was deleted; engine.py edits fail with 403 until re-auth
- **project_stripe_tour_berlin_event** · Stripe Tour Berlin event deck build — batched roster of ~100 companies, progress tracker
- **project_stripe_tour_paris_event** · Stripe Tour Paris event playlist build — progress and remaining companies
- **project_stubhub** · StubHub (STUB) research — global ticket marketplace, payout pain, no orchestrator, high-fit ICP
- **project-suno-jasper** · Suno account — full outreach history (LinkedIn + email campaign), research brief, and live meeting state as of 2026-08-06.
- **supabase-deck-down-sep-2026** · El proyecto Supabase del deck tool (mlwiosgalwsroisdkytl) dejó de resolver el 30-sep-2026; vive en la org de Isabella Ponce
- **project_supabase_service_key_location** · Where the Supabase service-role key for /builddeck upserts is stored
- **project_super_contacts** · Super.com (Yuno target) key contacts and relationship history for outreach
- **project_tango_live** · Tango Live (tango.me) research — live-streaming/gifting, web top-up already bypasses app-store fee, dual-sided orchestration play
- **project_tcl_agent** · Target Company List (TCL) build — German's AE outbound list of ~695 companies being enriched into a full sourced schema in Google Sheets
- **project_tcl_final_list_misaligned** · En la TCL (Google Sheet), la pestaña Final List tiene columnas desalineadas desde Insight 3 hasta Confidence; usar TCL_v2 para rating, tier, SF status y stakeholders
- **project_thinkific** · Thinkific (Vancouver, TSX THNC, Thinkific Payments = Stripe en 36 países, cero LatAm/India) — Darren (VP Product) solo le contesta a Justo; 4 FUPs sin respuesta; 23-sep-2026 reorganización (96 puestos, foco Plus + FCF); research 24-sep contra prioridades Skool + mensaje para Justo en Deals/Thinkific
- **project_thrivecart** · ThriveCart research brief — checkout platform building payments in-house; embed-Yuno angle not merchant sale
- **project-tiendamia** · Tiendamia (marketplace cross-border LatAm, HQ Miami; AR/BR/CR/EC/PE/UY) — intro call vie 25-sep-2026 9:00 COT agendada por Pedro Ferrer (SDR) con Salvador Boidi; Yuno ya les hizo demo en feb-2024 (Cybersource Uruguay)
- **project-unicef-colombia** · UNICEF Colombia, inbound; demos 21 y 29-sep hechas, follow-up 29-sep ENVIADO sin respuesta; propuesta Google Slides armada 2-oct, pricing v6 del 6-oct (platform $7K + 0.28%/0.24% por transacción aprobada, corte 100K trx + suscripciones $0.015 por trx enviada con las primeras 50K gratis = $14,500/mes; facturación mínima $10K), SIN enviar; stack Credibanco iPay, Redeban, Wompi, Nuvei, débitos batch 3 bancos
- **universal-psp-and-naming** · Universal Destinations (theme parks) deck — internal name \"Universal\" only, single bank-acquirer PSP topology (Chase or BofA) with disclaimer
- **project_us_qsr_retail_batch** · US QSR/fast-casual/retail batch (45 brands) added to TCL + enriched 2026-07-27; mostly weak Yuno fit (US-only)
- **project-vix** · ViX (TelevisaUnivision) deal history — decision-maker structure, Recurly conflict, Mastercard POP interest, Yuno<>Stripe co-sell prep
- **project_voodoo_psp** · Voodoo (mobile games + BeReal) payment stack and Yuno angle
- **warby-parker-eben** · Warby Parker / Eben Timko (Product Manager); blocker original \"solo US y Canadá\"; re-engagement jul-2026 sin respuesta; 3er toque sep-2026 con ángulo growth (tiendas + Intelligent Eyewear)
- **project-yango** · Yango deal — driver-recharge payments across LatAm, Aug 19 2026 discovery call findings, key contacts, and BC data gaps
- **yuno-sales-deck-skill** · Local skill .claude/skills/yuno-sales-deck (Samuel Vieira's package, 2026-09-17) adapted to German; builds research-backed .pptx sales decks with pptxgenjs + deck_qa.py; where it lives, what was changed, pending QA fixes on Anthropic/Higgsfield decks
- **project-yuno-vs-stripe-subscriptions** · Ongoing initiative to build a side-by-side Yuno Subscriptions vs Stripe Billing comparison; German will keep feeding info and send a not-yet-ready presentation
- **project-zoom-drew-curhan** · Drew Curhan, Payments Lead en Zoom (basado en Santa Barbara, CA); 3 emails fríos feb-mar 2026 sin respuesta; 4-oct-2026 German pasa a ángulo networking casual desde SF

---

# Who German is

## user_german_profile
*Who German is — Account Executive (senior) at Yuno, SDR/outreach workflows*  
*type: user · last updated 2026-07-01*

German Tatis (german.tatis@y.uno) is an **Account Executive at Yuno** (more senior role; previously led pre-sales). Yuno is a payment orchestration platform (single API to 1,000+ payment methods, PSPs, fraud tools, 190+ countries).

His workflow centers on outbound sales research and outreach: /research briefs, /builddeck merchant decks on deck.yuno.tools, and a cadence of emails (Email 1 opener, Email 2 deep dive, success case, industry snapshot) tailored to [[reference_buyer_personas]]. His written deliverables follow strict voice rules: no em-dashes, no name dropping in Email 1, tight and senior tone (see [[feedback_email_length_senior]]).

---

# Standing rules (how German wants Claude to work)

## Always commit and push automatically
*After completing any code/file changes, automatically git commit and git push without asking the user*  
*type: feedback · last updated 2026-05-04*

After making code or content changes, always commit AND push to the remote automatically. Don't stop at "wrote the files" or "made the edit" — the work isn't done until it's pushed.

**Why:** User explicitly told me on 2026-05-04 that push must happen automatically every time. They were frustrated that after adding SAP merchant to deck.yuno.tools (files written, Supabase row inserted), I stopped without pushing — so the Railway deploy didn't trigger and the new merchant wasn't live. They want this to be the default behavior, not something they have to ask for.

**How to apply:** When you finish a task that modified tracked files, immediately:
1. `git add` the relevant files
2. `git commit` with a descriptive message
3. `git push` to **`main`** (not `master`)

Do all three without asking permission. This applies even when changes touch deploy-sensitive files (CSVs, manifests, generated assets) — that's exactly when push matters most. Only skip the push if the user explicitly says "don't push" or "just stage" first.

**Branch convention for yuno-sales-pitch-maker:** Local branch is `master` but the deploy branch on `origin` is `main`. Always push with `git push origin master:main` (or whatever local branch maps to `main`). Confirmed 2026-05-04: `origin/main` is what Railway deploys to deck.yuno.tools / ss26.yuno.tools. `origin/master` exists but is stale ("Initial commit" only) — do not push there.

## Always include slide content in business-case
*When /business-case skill is activated, always present the slide guide content (slides 4-7) alongside the Excel generation*  
*type: feedback · last updated 2026-03-30*

Always include the "Our Understanding of the Context" slide content (slides 4-7) when running /business-case.

**Why:** The user copies this content directly into the PowerPoint template. The slide guide IS the primary output alongside the Excel file.

**How to apply:** Every time /business-case runs, present SLIDE 4 (Executive Summary), SLIDE 5 (Current Setup Constraints), SLIDE 6 (Payment Stack Overview), and SLIDE 7 (Traffic Map) formatted as copyable text blocks — before or alongside the Excel generation.

## feedback-cc-handoff-reply-pattern
*Cuando Magdalena o Samuel Carreño ponen a German en CC en correos a prospectos, German entra al hilo con un reply de estructura fija; plantilla y reglas*  
*type: feedback · last updated 2026-09-29*

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

## feedback-client-data-requests-simple
*Pedidos de datos a clientes = Google Sheet de una sola hoja, campo a la izquierda y respuesta al lado; nada de workbooks de muchas hojas*  
*type: feedback · last updated 2026-09-29*

Cuando German pide armar una solicitud de información para un cliente, el entregable es un Google Sheet de UNA sola hoja: el campo que queremos a la izquierda y al lado el espacio para que el cliente ponga sus números. Lista corta (unas 30 a 40 filas), agrupada por secciones.

**Why:** en Cruz Verde (29-sep-2026) dijo "la mayor cantidad de data posible" y entregué un Excel de 14 hojas y 90 solicitudes; lo mandó a rehacer dos veces: primero a Google Sheets en formato formulario, luego "muuucho más sencillo y en solo un tab". Detallado para él significa cubrir los temas clave (por ejemplo % de rechazos hard vs soft), no un instrumento largo que el cliente no va a llenar.

**How to apply:** empezar por la versión sencilla en Google Sheets y ofrecer el detalle como opción. Sin hojas de instrucciones, prioridades, columnas calculadas ni filas de ejemplo. Vía técnica: [[project-slides-api-token-dead]] (conector de Drive crea el archivo y lo comparte con la service account; Sheets API escribe). Ejemplo: [[project-cruz-verde]], `Deals/Cruz Verde/build/build_data_request_simple.py`.

## client-reported-metrics
*In client-facing business cases use the metric the client reported (e.g. Palco ticket promedio $37.09), never a value we derived that contradicts it; raise the discrepancy separately*  
*type: feedback · last updated 2026-09-16*

When a prospect reports a metric (ticket promedio, TPV, volumes), client-facing decks and business cases use that exact number. Do not replace it with a figure we derived from their other data, even if the derivation is arithmetically sound (Palco: Patricio said ticket promedio $37.09; the deck had used $163 = $346M / 2.12M and German said "ojo con eso, reajusta todo").

**Why:** the client recognizes their own number and will reject or distrust a different one; a bigger business case built on a derived ticket looks inflated. Discrepancies are a discovery question, not something to fix silently in the deck.

**How to apply:** use the reported metric everywhere in the deliverable; flag the inconsistency to German in the notes or the summary so he can ask the client; if a lever needs a different basis (e.g. bps on TPV), say explicitly which reported number it uses. See [[palco-ticketing]].

## Payments Concierge shorter in email2
*Always write a shorter version of the Payments Concierge paragraph in email2 — keep it concise*  
*type: feedback · last updated 2026-04-08*

Keep the Payments Concierge paragraph shorter in email2. Don't over-explain it.

**Why:** German finds the full-length version too long and wants it trimmed down.

**How to apply:** When writing email2, condense the Payments Concierge section to 2-3 sentences max instead of the full block. Keep the core idea (AI assistant, natural language queries, proactive alerts) but cut the detail.

## feedback_cost_objection_reply_pattern
*Pattern German likes for replying to a "too expensive / can't justify the cost" rejection, modeled on Sean Calabro's FlightHub reply (oct-2026) and reused for Flair*  
*type: feedback · last updated 2026-10-06*

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

## Cover slide uses yuno + merchant lockup
*All decks render the cover with a top-left lockup (yuno wordmark | merchant logo) and no "Hello {Company} team!" greeting. The lockup is the default.*  
*type: feedback · last updated 2026-05-11*

The cover slide (`src/components/slides/SlideCover.jsx`) renders a compact co-brand lockup in the top-left: Yuno wordmark, vertical separator, merchant logo, all matched to the same height (clamp 20–32px). No "Hello {Company} team!" greeting and no large merchant logo block beneath.

**Why:** User confirmed on 2026-05-11 that this is the preferred cover treatment going forward. Cleaner, more aligned with the Yuno slide design language, lets the GlobeHalo + title carry the visual weight instead of a stacked greeting+logo block.

**How to apply:**
- Do NOT reintroduce the greeting (`Hello {Company} team!`) or the large merchant logo block in any future cover refactor.
- New merchant onboarding only needs the standard logo asset in `public/merchants/{slug}.png` — the cover picks it up automatically via `data.COMPANY_LOGO`.
- Light theme still uses the masked-div fill (theme.accent silhouette); dark theme uses `<img>` directly with the `WHITE_LOGO_FILTER` override for dark-logo merchants in the `DARK_LOGO_MERCHANTS` set.
- Banking mode with the placeholder `Your Bank` still renders Yuno alone without the separator (the `data.MODE === 'banking' && data.COMPANY_NAME === 'Your Bank'` branch suppresses the lockup tail).
- If a merchant logo is unusually wide (e.g. Costco), it's still bounded by `maxWidth: clamp(140px, 14vw, 260px)` in the `coBrandLogo` style so it doesn't dominate the header.

**Reference commit:** `4ab829a` — refactor cover slide to yuno + merchant lockup.

## deck-changes-deploy-neverland
*Every deck content change (slide-overrides.json, business-overviews.json, slide component edits) must be deployed to Neverland/internal-tools, not just pushed to GitHub/Railway*  
*type: feedback · last updated 2026-09-14*

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

## feedback_deck_edits_scoped
*Deck edit requests must apply ONLY to that specific deck, never leak to other decks*  
*type: feedback · last updated 2026-07-02*

When applying a deck edit request (from the Edit button / a person), always make the change they asked for, BUT scope it to **that specific deck only**. It must not alter any other deck.

**Why:** Decks share components (`SlideBase`, slide components, `t()` copy). A naive edit to a shared component changes every deck in that language. German's rule: one person's request must never degrade everyone else's decks.

**How to apply:** Scope by the narrowest identifier that isolates the target deck — `data.COMPANY_SLUG` for a client deck, or a combination like `data.AUDIENCE==='merchant' && data.LANGUAGE==='fr'` for the generic-merchant-in-French deck. In `buildSlides` (SlideViewer.jsx) filter the slide order conditionally; for per-deck copy/data prefer Supabase per-merchant fields over editing shared strings. Example done 2026-07-02: dropped the Integration-as-a-Service slide from ONLY the French generic merchant deck (en/es/pt kept it). If a request truly can't be isolated to one deck in the current architecture, flag it before applying globally. Related: [[project_deck_edit_button]], [[feedback_never_duplicate_decks]].

## feedback_deliverables_google_sheets
*Listas y cruces de datos se entregan en Google Sheets (vía conector de Drive), no en Claude Docs ni artifacts*  
*type: feedback · last updated 2026-10-05*

El 5-oct-2026, cuando empecé el cruce Money20/20 × TCL como Claude Doc, German cortó: "pero quiero que me traigas todo en un google sheets".

**Why:** German vive en Google Workspace y comparte estas listas con Susana, Samuel y Sean; un Claude Doc no entra en ese flujo.

**How to apply:** cualquier lista, cruce o tabla de contactos va directo a un Google Sheet. Vía que funciona sin OAuth: `mcp__claude_ai_Google_Drive__create_file` con `contentMimeType: text/csv` y `textContent` (se convierte solo a Sheet; una pestaña). El xlsx en base64 también convierte, pero el parámetro base64 de un workbook de 55 KB (74K chars) supera el límite de salida por turno; usar CSV compacto (< 45 KB) y guardar el xlsx completo en el repo. Ver [[feedback_drive_download_to_disk]] para LEER hojas grandes.

## feedback_drive_download_to_disk
*Para leer un Google Sheet grande completo sin OAuth: download_file_content como xlsx → el harness lo guarda en disco → decodificar base64 con Python y abrir con openpyxl*  
*type: feedback · last updated 2026-10-05*

Descubierto el 5-oct-2026. `mcp__claude_ai_Google_Drive__read_file_content` solo devuelve 5-6 filas de muestra por pestaña en hojas grandes, y gsheets_read / service account / gcloud siguen sin acceso (ver [[project_gsheets_mcp]]).

**How to apply:** llamar `mcp__claude_ai_Google_Drive__download_file_content` con `exportMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`. Cuando el resultado supera el límite de tokens, el harness lo guarda en `~/.claude/projects/<proyecto>/<sesión>/tool-results/mcp-claude_ai_Google_Drive-download_file_content-<ts>.txt` (JSON con `content` en base64). Decodificar con Python (`json.load` → `base64.b64decode` → `.xlsx`) y volcar cada pestaña a TSV con openpyxl. Funcionó con la TCL completa (1.9 MB, 5 pestañas) y con la lista de Money20/20 (1.1 MB, 13 pestañas). Exportar como `text/csv` solo trae la primera pestaña por posición (en la hoja de Money20/20 era "Cadence", no la útil).

Límite relacionado: WebSearch tiene tope de 200 búsquedas por sesión compartido entre todos los subagentes ([[feedback_websearch_budget_shared]]).

## Email 1 — no name dropping
*Email 1 (opener) must always use the Yuno description boilerplate, never client name dropping. Name dropping is for Email 2+.*  
*type: feedback · last updated 2026-04-06*

Email 1 always uses the descriptive Yuno boilerplate ("Yuno is a global payment infrastructure platform..."), never the name-dropping variant (GoFundMe, Uber, OpenAI, etc.). Client logos / name dropping is reserved for later emails in the cadence.

**Why:** The first email should establish what Yuno is. Name dropping belongs in follow-up emails where social proof reinforces the initial pitch.

**How to apply:** When writing /email1, always use Variant A (description). When writing /email2 or later cadence emails, name dropping is allowed and encouraged.

## feedback_email_length_senior
*Email 1 and Email 2 must be shorter, denser with value, senior AE tone (same voice)*  
*type: feedback · last updated 2026-10-05*

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

## feedback-email-no-links-sober
*Correos a prospectos que German envía él mismo van sobrios y sin links ni menciones de "sección X del deck"; German agrega el link o adjunto a mano*  
*type: feedback · last updated 2026-09-24*

Al redactar correos que German va a enviar (propuestas, follow-ups), no meter links (Papermark, Drive, deck.y.uno) ni referencias tipo "sección 06, slides 36 y 37". Tampoco listas numeradas de beneficios ni frases de cierre grandilocuentes ("se paga más de diez veces"). Tono plano y corto: qué mando, en qué se basó, la cifra clave, y cómo seguimos.

**Why:** 24-sep-2026, correo de propuesta a Yango: German rechazó la primera versión ("menos allá", "esa vaina de meter links y eso no, yo me encargo de esa parte").

**How to apply:** Borradores de Gmail sin URLs; German pega el link o adjunta el PDF. Mantener [[feedback-email-length-senior]] y [[feedback-no-dashes]]. Ver [[project-yango]].

## feedback_gmail_update_draft_detaches_thread
*Gmail MCP update_draft desprende el borrador del hilo original; para cambiar un borrador de respuesta, recrearlo con create_draft + replyToMessageId*  
*type: feedback · last updated 2026-09-21*

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

## gmail-workflow-central
*German quiere a Claude siempre dentro de su Gmail (conector claude.ai); leer threads y dejar drafts sin preguntar*  
*type: feedback · last updated 2026-08-05*

German dijo (2026-08-05) que conectar Gmail con Claude es "importantísimo" porque necesita a Claude entrando a su correo siempre.

**Why:** Su workflow de AE vive en el correo: threads de deals (Hostinger, Lululemon, Eventbrite), RFPs, follow-ups. Quiere que Claude opere ahí directamente, no que le pase texto para copiar/pegar.

**How to apply:** Si el conector claude.ai Gmail está autenticado en la sesión, usarlo proactivamente: leer el thread relevante antes de redactar, y dejar el draft creado en Gmail (draft, no enviar sin OK). Si NO está autenticado, avisarle al inicio y darle el paso de claude.ai/settings/connectors. Pendiente al 2026-08-05: German estaba por autorizarlo. Relacionado: [[project_hostinger]] (primer uso previsto: draft en el thread de Hostinger con las respuestas del RFP).

## feedback_linkedin_shorter
*LinkedIn outreach messages should be a bit shorter than the standard email version*  
*type: feedback · last updated 2026-07-20*

When a persona-tailored outreach message is for LinkedIn (connection message, InMail, LinkedIn DM), make it a bit shorter than the standard email version. Tighten the middle: keep the hook + one crisp Yuno line + the value in one sentence + soft CTA. Full-length structure is fine for email.

**Why:** LinkedIn is read on smaller screens and skimmed; long blocks get ignored. Email tolerates more length.

**How to apply:** Same persona angle and grounding as always (see [[reference_buyer_personas]]), just condensed. Keep no-dashes, no-name-drop-in-opener rules. Default to the shorter form whenever the channel is LinkedIn/Sales Navigator; keep full length only when German says it's for email.

## feedback-meeting-brief-structure
*Meeting briefs — agenda y open questions SIEMPRE al final (ahí arranca German a tomar notas); TL;DR battle card al inicio*  
*type: feedback · last updated 2026-08-03*

En todo meeting brief para German: la **agenda de la llamada y las open/discovery questions van SIEMPRE como últimas secciones** del documento. Razón: German toma notas a partir de la agenda, así que todo el contenido de estudio va antes y la zona de trabajo en vivo queda al final, con espacio de notas ("Notes: ___") bajo cada bloque de agenda y cada pregunta.

**Why:** German lee el brief de arriba hacia abajo antes de la reunión y usa el final del doc como su hoja de notas durante la llamada.

**How to apply:** Estructura v2: (1) header con logística + objetivo + action flags, (2) TL;DR battle card de 1 página, (3) quién está en la sala, (4) la empresa (incl. subsidiarias/estructura corporativa), (5) payments money map, (6) top markets, (7) news & signals con fechas, (8) cómo vender Yuno + landmines, (9) "Be ready for" (qué te pueden preguntar a ti, con respuestas listas), y de últimas SIEMPRE (10) agenda con espacio de notas y (11) discovery questions con espacio de notas, + checklist post-meeting. Ver [[project-meeting-brief-skill]].

## feedback_never_duplicate_decks
*Never create a duplicate deck/merchant; if it already exists, just say so*  
*type: feedback · last updated 2026-06-02*

NEVER duplicate a deck/merchant. If a merchant already exists (in `public/merchants.csv`, `src/data/merchants.generated.js`, `public/merchants/{slug}.png`, or Supabase), STOP and just tell the user it already exists. Do not rebuild, do not overwrite the logo, do not add a second row.

**Why:** In the super.com /builddeck run, the Supabase existing-merchant check returned "Invalid API key" so I never confirmed existence, AND I skipped checking the local files. super-com already existed (CSV, manifest, logo). I created duplicate CSV + manifest entries and overwrote the original logo, which the user flagged. Had to git revert.

**How to apply:** In /builddeck pre-flight, the existing-merchant check must include LOCAL files, not only Supabase: `grep` the slug in `public/merchants.csv`, `merchants.generated.js`, and `ls public/merchants/{slug}.png`. If the Supabase key lookup fails, the local grep is the authoritative fallback, never assume "not found" on a failed API call. If found anywhere, stop and report it exists. See [[feedback_auto_commit_push.md]] and [[project_salesmaker_protected_master.md]].

## feedback-no-dashes
*Never use em-dashes or dashes as punctuation in any written content (emails, decks, messages, copy).*  
*type: feedback · last updated 2026-05-25*

Never use em-dashes (—) or hyphens used as punctuation (" - ") in written content delivered to the user. Use commas, periods, parentheses, or restructure the sentence instead.

**Why:** User flagged it explicitly. Dashes read as AI-generated copy and break the natural voice he wants in outbound emails and decks.

**How to apply:** All written deliverables — emails, slide copy, LinkedIn messages, business cases, follow-ups. Applies across every project and skill. Hyphens inside compound words (e.g., "follow-up", "high-leverage") are fine; the rule is about dashes as sentence punctuation.

## Never put false info — disclaimer when uncertain
*Never put information you're not sure about into deliverables. When uncertain about a fact (especially PSPs, payment providers, internal infrastructure), add a disclaimer like "according to web data" or "assumptions were made when selecting current providers". Applies to ALL projects, not just deck.yuno.tools.*  
*type: feedback · last updated 2026-06-07*

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

## no-pdf-cursor-artifacts
*Yuno PDF deck exports must never show vertical cursor caret artifacts (\"|\" lines) captured during Google Slides PDF export*  
*type: feedback · last updated 2026-05-27*

When building Yuno decks via [[slide-builder]], [[builddeck]], or any Google Slides workflow, the user has flagged a recurring issue: PDF exports often capture text cursor (caret) artifacts as thin vertical "|" lines that appear between words on slides. Documented examples on a SpaceX / Starlink deck: lines appeared between "about" and "your business" (slide 2), between "together." and "one platform" (slide 3), between "pillars ·" and "One brain" (slide 4), between "merchant-first" and "team built by" (slide 7), and between "economy," and "together" (slide 8).

**Why:** Google Slides captures the blinking text cursor inside any text box that was last in edit / focused state at the moment of PDF export. The user said verbatim: "Asegúrate de que eso nunca salga cuando yo descargue el PDF."

**How to apply:**
- When generating decks via the Google Slides API, never leave a text box in edit / focused state at the end of the build. After updating text content, deselect or click outside the box programmatically before telling the user the deck is ready.
- When the user is about to download as PDF, instruct them to first click once on the slide canvas background (outside every text box) on any slide that was recently edited, then File → Download → PDF Document.
- After any deck build, suggest a quick visual scan post-PDF-export and a re-export if any "|" lines appear. Treat this as a QA checkpoint.
- Do NOT confuse intentional underlines or design borders (e.g., the horizontal teal underline under "global scale" on the SpaceX cover) with the unwanted vertical cursor artifacts. Only thin vertical lines that break text mid-sentence between two words are the issue.

## no-slide-overlap
*Slide elements must never visually overlap. Bottom-row footer stats on slide 3 (and any slide) must clear the content boxes above with safe padding.*  
*type: feedback · last updated 2026-05-27*

When building Yuno decks, no element on any slide may visually overlap another. Specifically flagged: on slide 3 ("Yuno brought it all together"), the footer-row stat callouts at the bottom ("$1-2M cost to set up and manage each direct PSP connection" and "$118B lost annually to failed payments industry-wide") were overlapping the bottom edge of the two bordered content cards above them (PSP logo grid on the left and narrative text on the right). This makes the deck look unpolished.

**Why:** The user flagged this verbatim: "los números del tercer slide abajo se superponen sobre la información de arriba. Asegúrate de que eso no pase." Bottom stats must sit clearly below the cards with breathing room, not cross into them.

**How to apply:**
- On slide 3 specifically, the bottom footer stat row must end at a y-coordinate that leaves at least 40px (in a 1920×1080 frame) of empty vertical space below the bordered content boxes. If the cards extend to y=900, the footer stats must start at y=940 or later.
- General principle: every slide layout must be verified for non-overlap before declaring the deck ready. No text, icon, or chip should sit on top of another container border.
- When adapting the standard slide-3 template ([[builddeck]] / [[slide-builder]]) to a new merchant, recheck the vertical heights of the PSP grid and right-side narrative card. If either card grew due to more content, the footer stats must shift down accordingly. Do not assume the default coordinates always clear.
- Apply the same non-overlap check to every other slide, especially slides with KPI rows, footer chips, or page-number bars.

## Never use "no small feat
*Never use the phrase "no small feat" in any outreach email or written content*  
*type: feedback · last updated 2026-04-06*

Never use the expression "no small feat" in emails or any written output.

**Why:** User explicitly flagged this as a phrase to avoid — likely sounds cliché or overly salesy.

**How to apply:** When writing cold emails, LinkedIn messages, or any prospect-facing content, avoid this phrase entirely. Use direct, natural compliments instead.

## feedback_paypal_not_processor
*PayPal is a wallet/APM, never a processor/PSP; never count it in PSP totals or topology chips*  
*type: feedback · last updated 2026-07-10*

PayPal must always be treated as a wallet / Alternative Payment Method (APM), never as a processor / PSP / gateway. Do not list it among "PSPs", do not include it in PSP counts, and do not put it in slide-3 topology chips (which are gateways/PSPs/MoR only, see [[feedback_psps_chips_scope]]).

**Why:** German flagged that the Lightricks deck counted PayPal as one of "3 PSPs" on web checkout. PayPal Wallet/Checkout is an APM; the real processors were Stripe + Adyen (2). Miscounting it inflates the "multi-PSP no orchestrator" angle with a false fact ([[feedback_no_false_info_disclaimer.md]]).

**How to apply:** When building/QA-ing any deck, put PayPal in the `apms` list only. Fix PSP counts to exclude it (Lightricks: 2 PSPs = Stripe + Adyen). Applies to research briefs and business cases too. Related: [[project_lightricks_psp]].

## feedback-pdf-no-transform-scale
*In the yuno-sales-pitch-maker PDF pipeline, never wrap PrintViewer slides in a transform:scale container. SlideBase-based slides render empty.*  
*type: feedback · last updated 2026-05-26*

In `yuno-sales-pitch-maker/src/components/PrintViewer.jsx`, never wrap each `.pdf-page` in a `transform: scale(...)` container around the slide Component. The cover slide survives (it has its own absolute-positioned layout), but every slide built on top of `SlideBase` (BusinessOverview, Diagnostic, YunoSolve, ProductSuite, Dashboard, Leadership, TrustedBy, CTA, etc.) loses all body content — only the chrome (section pill + Yuno logo) survives in the PDF.

**Why:** SlideBase's outer div uses `width: 100%; height: 100%` and its body uses flex layout. The transform:scale wrapper's logical box sizing interacts with these cascades in a way that produces empty/0-sized layout for the body section. Cover doesn't hit this because every element is `position: absolute` with explicit px values.

**How to apply:** If the goal is to render the PDF at a smaller viewport to match the live tool's vw resolution (this was the failed fix from commit 38aa4d5, reverted in 2c50656), use a different approach instead:
- CSS `zoom` per-slide (like the existing `[data-pdf-root] [data-slide='leadership'] { zoom: 0.96 }` hack at `src/index.css`)
- Replace `vw`-based clamps in individual offending slides with px equivalents
- Or accept the 1920×1080 capture viewport and add targeted zoom-hack overrides to the slides that genuinely overflow

Capture viewport, @page size, and `page.pdf()` size must all stay at 1920×1080 unless the entire slide layout system is rewritten to be viewport-agnostic.

Related: [[feedback-no-dashes]] is the broader "deck rendering rules" cluster.

## PSP chips = gateways/PSPs/MoR only
*Slide 3 "Today's Topology" PSP chips must only contain gateways, acquirers/PSPs, or merchant-of-record. Never list payment methods (BNPL, wallets, card networks, issuers, LPMs).*  
*type: feedback · last updated 2026-05-11*

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

## published-stats-only
*\"+12% auth uplift\" and \"20–30% decline recovery\" are flagged as fabricated; use Yuno's published figures 7% uplift / 30% recovered revenue (or verified client figures like McDonald's +4.7%/18 markets/$3.2M)*  
*type: feedback · last updated 2026-09-09*

The deck QA reviewer flagged the default impact tiles "+12% average auth-rate uplift" and "20–30% decline recovery" as fabricated on six consecutive decks (Sep 2026). The approved replacements are Yuno's published figures: **7% authorization uplift** and **30% recovered revenue** (both published on y.uno). Verified client figures are also acceptable: McDonald's +4.7% acceptance across 18 markets, $3.2M additional revenue.

**Why:** The +12% / 20–30% numbers have no public source and keep failing deck QA; shipping them risks credibility with prospects. See [[no-false-info-disclaimer]].

**How to apply:** On any deck (SlideYunoSolve `impact.stat*`, SlideCTA `proof.*` tiles), override the defaults via the deck's `business_overview.deckOverrides` (buckets `yunoSolve` and `cta`) with +7% / 30%, and add the source line "> Yuno published figures · y.uno". Airalo and gamma-ai are already fixed this way. Also flagged repeatedly: "Reconciliation · One ledger across every PSP" must be footnoted as roadmap (settlement, payout and fee reconciliation is not GA) — override `arch.feature2` → "Reconciliation*" + `arch.note`, and `productSuite.pillar3.item1.desc` → "Unified visibility across providers…".

## rbp-methodology
*Standard top-down methodology for structuring any Yuno presentation/deck — Requirement, Benefit, Proof*  
*type: feedback · last updated 2026-09-02*

The methodology German uses to build presentations top-down is **Requirement, Benefit, Proof (RBP)**:

1. **Requirement** — diagnose the problem: what the client actually needs/is struggling with (the pain, the gap).
2. **Benefit** — organize the solution: what Yuno delivers that addresses that requirement.
3. **Proof** — back it with evidence: verified data, case studies, or facts that substantiate the benefit.

**Why:** This is German's explicit, standing instruction for how decks/presentations should be structured — top-down, one argument at a time, each moving from diagnosis to solution to substantiation. He corrected a prior guess (McKinsey issue-tree / Minto SCQA) — RBP is the actual name, not those.

**How to apply:** Use this as the default narrative/section structure whenever building or reviewing a Yuno deck, business case, or pitch (e.g. via [[project_meeting_brief_skill]], slide-builder, business-case skills). Each slide or slide-group should be checkable against Requirement → Benefit → Proof rather than a generic problem/solution layout. Combine with [[feedback_no_false_info_disclaimer]] — the "Proof" step must always be verified facts, never assumed or padded.

## feedback-reply-in-english
*German wants every reply in English, regardless of the language he writes in; switch languages only when he explicitly asks for another one in that message*  
*type: feedback · last updated 2026-10-06*

Always answer German in English, even when he writes in Spanish. The only exception is when he explicitly says to reply in another language; that applies to that request only, then go back to English.

**Why:** Standing instruction given on 2026-10-06 ("de ahora en adelante quiero que siempre me contestes en inglés, independientemente de cómo te hable yo").

**How to apply:** This covers chat replies only. Deliverables keep the language the audience needs (emails to Cruz Verde, Palco, Línea Directa, UNICEF stay in Spanish; outreach to US accounts in English). See [[feedback-email-no-links-sober]] and [[feedback-email-length-senior]] for the writing rules that still apply to those pieces.

## sheet-house-format
*German's preferred Google Sheets look (copied from his \"SF AI Prospects – Yuno ICP (Oct 2026)\" sheet) and the working way to apply formatting via the Sheets API service account*  
*type: feedback · last updated 2026-10-06*

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

## feedback-single-currency-usd
*Decks and business cases speak in one currency (USD); never print amounts in local currencies (₩, €, PKR, C$...), use USD or currency-free metrics*  
*type: feedback · last updated 2026-09-16*

German's rule (2026-09-16, Higgsfield deck): every figure in a deck is in USD. No local-currency amounts anywhere, even on country slides.

**Why:** the reader compares markets side by side; mixed currencies break the comparison and look unfinished. Converting with an assumed FX rate adds an unsourced number.

**How to apply:** when a verified stat only exists in local currency (₩1.1T/day easy-pay, €157B iDEAL, PKR 23.3T Raast, C$554B Interac), swap it for a currency-free metric from the same source (users, transaction counts, shares, growth rates) rather than converting. Phrases like "local AED / KRW acquiring" are fine: they describe local-currency processing, not amounts. Related: [[project-higgsfield]], [[feedback-no-false-info-disclaimer]].

## feedback_slide2_always_complete
*Slide 2 (business overview) must always be fully populated, never sparse*  
*type: feedback · last updated 2026-06-09*

Slide 2 ("What we know about your business" / SlideBusinessOverview) must ALWAYS be complete: revenue, description, recent catalyst, commerce footprint, top operating countries (with flags + shares), alternative payment methods accepted, and business lines. Never leave it sparse/empty.

**Why:** Auto-built decks (runtime /builddeck → Supabase row) often leave the `business_overview` column thin, so the slide renders mostly empty and looks unfinished in front of a prospect.

**How to apply:** First check what the Supabase row already has (open the live deck). Two cases:
- **Supabase content is good but a section is missing** (common: countries + apms): do NOT use forceLocalOverview (it would clobber the good content with weaker estimates). Instead add a partial merge: `slide-overrides.json` → `"<slug>": { "slide2": { "countries": [...], "countriesSource": "...", "apms": [...] } }`. The reader does `{ ...row.business_overview, ...overrides.slide2 }`, so listed keys are ADDED/overridden and everything else is preserved. (Despite the _doc saying "countries only", apms and any overview key also merge.)
- **Supabase content is genuinely empty/wrong:** add the full slug entry to `business-overviews.json` and set `forceLocalOverview: true` so the local overview fully replaces the row.

Research real figures; mark estimates with `estimated:true` + a `footprintNote`/`countriesSource` disclaimer per [[feedback_no_false_info_disclaimer]]. For app-only merchants (e.g. Dream Games / Royal Match), "countries" = top app-store revenue markets and "apms" = store billing rails (Apple App Store IAP, Google Play Billing, Amazon Appstore, Samsung Galaxy Store).

**Omnichannel / retail merchants (PetSmart, Nordstrom, Costco, etc.):** one of the footprint anchors must ALWAYS be the **digital share of sales** (e-commerce/digital vs in-store %), real or estimated. It is the single most payment-relevant scale metric for a brick-and-mortar retailer, so never omit it. If no exact figure is public, use a sourced estimate and mark it as such.

## feedback_websearch_budget_shared
*WebSearch tiene tope de 200 búsquedas por sesión, compartido entre todos los subagentes; planear lookups masivos (LinkedIn) en pasadas de ≤180 y priorizar*  
*type: feedback · last updated 2026-10-05*

El 5-oct-2026 lancé 6 subagentes en paralelo para buscar LinkedIn de 304 personas (Money20/20 × TCL). El tope de 200 búsquedas por sesión se agotó en minutos y ~180 personas quedaron sin buscar; los agentes intentaron curl contra buscadores públicos y casi todos los bloquearon (solo Yahoo Japan y Seznam respondieron).

**Why:** el presupuesto es por sesión (variable CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION, la cambia German, no yo), no por agente.

**How to apply:** antes de un lookup masivo, ordenar por prioridad (Title Tier 1 y 2 primero) y limitar la pasada a ~180 búsquedas, una por persona. Query que mejor funcionó para LinkedIn: WebSearch con `allowed_domains: ["linkedin.com"]` y "Nombre Apellido" + empresa + fragmento del cargo; aceptar solo si el título del resultado muestra nombre + empresa o cargo. Lo no buscado queda vacío y se marca para una segunda sesión. Relacionado: [[project_money2020_lv2026_tcl_match]].

---

# Reference material (positioning, pricing, personas, tools)

## reference_buyer_personas
*Yuno's 13 buyer personas — tailor any outreach/email to the persona German names*  
*type: reference · last updated 2026-07-01*

Yuno's 6 buyer personas. **How to apply:** when German names a persona to contact, take the base message (his finalized Email 1, e.g. [[project_praktika]]) and re-angle it toward that persona's priorities, KPIs and pain points. Keep his intro/hook and Yuno boilerplate; reshape the middle paragraphs and CTA to speak to what that persona cares about. Never invent facts; keep no-dashes, no-name-drop-in-email1 rules.

**CFO** — Profitability & efficiency. Pains: high payment costs, revenue lost to declines/chargebacks, manual reconciliation, compliance burden, too many vendors. KPIs: Cost of Payments, Operating Margin, Cash Flow, Fraud/Chargeback Rates, ROI. Yuno angle: cut fees via smart routing, recover revenue via approval uplift, unified reconciliation, fraud/compliance control, vendor consolidation. Proof stat: 5-20% approval uplift + vendor-consolidation savings.

**VP / Head of Payments** — Performance & reliability. Pains: multiple providers, low approval rates, slow method rollout, manual ops, scalability risk. KPIs: Authorization Rate, Success Rate by Region, Transaction Costs, # Methods Supported, Uptime, Fraud/Chargeback, Settlement Reconciliation. Yuno angle: smart routing + dynamic retries for approvals, rapid no-integration method enablement, automated retries/reconciliation/settlement, real-time dashboards (approval by region, provider health), high-availability uptime.

**CCO (Chief Commercial Officer)** — Revenue & global growth. Pains: lost sales from declines, hard market expansion, competitive checkout pressure, fragmented visibility, checkout friction hurting loyalty, missing local methods limiting conversion. KPIs: Revenue Growth, Conversion Rate, Market Expansion, CLV, Profit Margin. Yuno angle: approval uplift via routing, 1,000+ methods across 190+ countries for faster expansion, smoother unified checkout, centralized visibility, orchestration layer (no need to replace providers).

**Engineering Leads (CTO / VP Eng)** — Scalable, secure, efficient systems. Pains: integration overload, maintenance/tech debt, PCI burden, limited in-house scalability eating eng time. KPIs: Development Velocity, Uptime/Reliability, Security/Compliance, Resource Allocation, Scalability. Yuno angle: single API replaces fragmented integrations, Yuno handles maintenance/compliance/PCI/tokenization, cloud-native scalability, faster feature delivery, expert support. Frees engineers for core product.

**CPO (Chief Product Officer)** — Smooth UX & fast innovation. Pains: slow payment integrations, checkout friction, engineering drain, inconsistent global experiences, complex security. KPIs: Feature Delivery Speed, Checkout Conversion, User Satisfaction, Retention/Churn, Global Feature Coverage. Yuno angle: faster payment-feature launches, one-click/saved cards, easy subscriptions (tokenization + automated retries), consistent global UX via one orchestration layer, offloaded security/compliance.

**Marketing / Growth Leaders** — Acquisition, conversion, retention. Pains: cart abandonment, limited payment options, checkout friction wasting ad spend, recurring payment failures cutting LTV, no payment data for campaigns. KPIs: Conversion Rate, Cart Abandonment, CAC vs Conversion, LTV, Geographic Growth, NPS. Yuno angle: more methods + faster checkout to cut abandonment, one-click/saved/localized experiences, intelligent retries/routing to reduce failed renewals (LTV), real-time payment insights to optimize acquisition/ROI/CAC.

**CEO / Founder** — Growth, margins, strategic risk, scale, fundraising/valuation. Pains: payments quietly leaking revenue and margin, inability to expand into new markets fast enough, payments becoming a strategic bottleneck instead of an enabler, infra/vendor concentration risk, no clean payment visibility for the board and investors. KPIs: Revenue Growth, Gross Margin, Market Expansion Speed, Customer Growth/Retention, Operating Efficiency/Valuation. Yuno angle: turn payments into a growth lever (approval uplift = more revenue with no extra CAC), enter new markets in weeks not quarters via one API, protect margin through routing + vendor consolidation, one strategic infrastructure partner that scales with the company, board-level payment visibility, de-risk single-rail/single-vendor dependency. Proof: 5-20% approval uplift, InDrive 10 LATAM markets <8 months.

**Product Manager** — Ships payment/checkout features and owns funnel metrics (more tactical than the CPO). Pains: payment features take too long and depend heavily on engineering, checkout friction hurting activation/conversion, hard to A/B test payment methods or routing, inconsistent payment data to make decisions, slow method launches blocking roadmap. KPIs: Feature Delivery Velocity, Checkout Conversion, Funnel/Activation Completion, Time-to-launch new method, Experiment throughput. Yuno angle: pre-built payment capabilities + SDKs so features ship without heavy eng, no-code enablement of new methods/PSPs (config not project), one-click and saved-card checkout, easy A/B testing across methods and routing, unified payment analytics for fast decisions. Frees the roadmap from payment plumbing.

**Treasurer** — Cash, liquidity, settlement, FX, and financial risk. Pains: fragmented settlement across multiple PSPs, slow or unpredictable settlement timing, FX and cross-border costs eroding funds, manual reconciliation, poor cash visibility across markets/currencies, counterparty/concentration risk. KPIs: Cash Flow/Liquidity, Settlement Time, FX & Processing Costs, Days Sales Outstanding, Reconciliation Accuracy, Working Capital. Yuno angle: unified reconciliation and settlement visibility across every provider in one dashboard, faster and more predictable settlement, multi-currency + local acquiring to cut FX/cross-border cost, a single real-time view of money movement for forecasting, reduced dependence on any one processor/bank. Pairs closely with the CFO angle (cost/margin) but focused on liquidity and cash timing.

**Head of Payment Operations** — The practitioner running payments day to day (often the real champion). Pains: manual reconciliation and settlement matching, firefighting failed payments and disputes, chargeback handling across providers, no single place to monitor approval rates/provider health, slow method or PSP rollout dependent on eng, inconsistent data across PSPs. KPIs: Authorization/Success Rate, Chargeback & Dispute Rate, Reconciliation Time, Failed-payment Recovery Rate, Provider Uptime, Time-to-add a method/PSP. Yuno angle: one dashboard across every processor and method (approvals, refunds, chargebacks, provider health) with real-time monitoring and proactive alerts (Payments Concierge via Slack/WhatsApp/Telegram, Rappi ms detection), automated retries/reconciliation/settlement, smart routing + failover to lift approvals and recover soft declines, no-code method/PSP enablement. Turns firefighting into oversight.

**Head of Fraud / Risk & Compliance** — Protects revenue from fraud and chargebacks while staying compliant (maps to Yuno's security & risk pillar). Pains: chargeback and fraud losses, false declines killing good revenue, cross-border transactions wrongly flagged, managing many disconnected fraud tools, 3DS friction hurting conversion, SCA/PCI compliance burden across markets. KPIs: Fraud & Chargeback Rate, False-decline Rate, Dispute Win Rate, Approval Rate (net of fraud), 3DS/SCA compliance, Cost of Fraud Ops. Yuno angle: real-time risk screening across 50+ fraud tools from one layer, agnostic/optimized 3DS that minimizes friction while staying compliant, network tokens + account updater to cut fraud exposure and silent failures, early dispute resolution before chargebacks, local acquiring to solve cross-border fraud flags. Reduces losses AND lifts approvals at once.

**COO** — Operational efficiency and scaling the org without adding complexity. Pains: too many payment vendors/contracts to manage, operations not scaling with growth, fragmented systems and reporting, engineering and ops time drained by payment maintenance, market expansion bottlenecked by payment setup. KPIs: Operating Margin/Efficiency, Cost per Transaction, Vendor Count, Time-to-market for new geos, Process Automation, Uptime/Reliability. Yuno angle: consolidate every provider into one platform and one contract, automate retries/reconciliation/settlement, launch new markets in weeks via one API, unified operational visibility, scalable cloud-native infra so ops and eng focus on core business. Overlaps with CEO (strategy) and CFO (cost) but centered on operational execution and vendor consolidation.

**Controller / Head of Finance Ops** — Owns the close, reconciliation, and reporting accuracy (more granular than CFO/Treasurer). Pains: manual, multi-PSP reconciliation slowing month-end close, mismatches between processor reports and bank settlements, refund/chargeback tracking across markets, error-prone spreadsheets, no single source of truth for payment data, audit complexity. KPIs: Time-to-close, Reconciliation Accuracy/Match Rate, Manual Adjustment Volume, Refund/Chargeback Tracking, Audit Readiness. Yuno angle: unified reconciliation consolidating every processor and method into one dashboard with real-time approvals/refunds/chargebacks, automated matching to accelerate close and cut manual work, centralized audit trails per market, one source of truth for finance. Bridges the CFO (cost/margin) and Treasurer (cash/settlement) angles at the operational accounting level.

## reference_colombia_processors
*Procesadores de tarjetas en Colombia verificados el 29-sep-2026 (tarifas públicas, qué está conectado a Yuno, Bre-B recurrente, DRUO); no existe dato público de aprobación por procesador*  
*type: reference · last updated 2026-09-29*

Verificación hecha el 29-sep-2026 para Experian, reutilizable en cualquier deal de Colombia. Archivo completo con fuentes: Deals/Experian/experian-colombia-card-processors-research-2026-09-29.md.

- **Tarifas públicas verificadas:** Wompi 2.65% + $700 + IVA (Plan Avanzado, plana; Plan Gateway sin costo de Wompi, se negocia directo). ePayco 2.64% + $690 + IVA para Davivienda y 3.29% + $700 + IVA otros bancos. PayU, Mercado Pago y Bold sin fuente oficial accesible y con cifras contradictorias entre blogs.
- **PayU:** Rapyd cerró la compra de PayU GPO el 14-mar-2025; la página de tarifas de PayU Colombia redirige a Rapyd.
- **Conectados a Yuno según páginas públicas:** Wompi, PayU, Redeban, Kushki, Mercado Pago, ePayco, Nuvei, dLocal. Credibanco sin confirmación pública. Bold y DRUO sin evidencia.
- **Bre-B:** más de 110 millones de llaves y casi 8 millones de transacciones diarias. El cobro recurrente no es nativo del sistema oficial (prensa may y jul 2026); lo ofrecen terceros. DRUO habilita débito automático sobre llaves Bre-B desde el 5-may-2026 y hace débito directo a cuentas vía API.
- **Yuno y PayRetailers:** alianza del 24-sep-2026, en Colombia cubre Bre-B y PSE.
- **EBANX:** +10 pp de aprobación con network tokens en Colombia (comunicado 11-dic-2025, dato interno de EBANX, contexto cross-border).

**No usar con clientes:** rangos de tasa de aprobación por tipo de adquirencia, spread de 10 a 25 pp por BIN, mix de pagos del e-commerce colombiano (las fuentes se contradicen). Ver [[feedback_no_false_info_disclaimer]] y [[feedback_published_stats_only]].

Para listas de "mejor performance" hace falta el benchmark interno de Yuno. Relacionado: [[project_experian]], [[project_unicef_colombia]], [[project_cruz_verde]], [[project_linea_directa]].

## reference-money2020-vegas-2026-supercar-event
*Evento de Yuno y PayPal en Money20/20 Las Vegas 2026: 'Payments Unlocked: An exclusive supercar experience' en SpeedVegas; invite Luma luma.com/10q4wvgc; usar para invitar a prospectos que van a Vegas*  
*type: reference · last updated 2026-10-05*

**"Payments Unlocked: An exclusive supercar experience", hosted by Yuno & PayPal.** Money20/20 Las Vegas 2026 (la feria es 18 a 21-oct). Invite: https://luma.com/10q4wvgc (registro con aprobación del host, cupos limitados).

- Lugar: SpeedVegas, 14200 S Las Vegas Blvd, Las Vegas.
- Agenda: salida 2:15 pm, pista 3:45 a 5:00 pm (vueltas guiadas con instructor + cinco vueltas conduciendo solo), recepción de networking a las 5:00 pm.
- Requisitos: licencia de conducir vigente y zapato cerrado.
- **Fecha exacta no visible en el fetch de la página de Luma** (verificar antes de escribirla en un correo). Al 5-oct-2026 no está en el calendario de German.

**Cómo usarlo:** gancho corto en correos a prospectos que están en la lista de Money20/20 ("Are you into cars?"), link a Luma, sin pitch. Primer uso: A.J. Tus de DoorDash (ver [[project-doordash-aj-tus]]). Candidatos: Ashwyn Singhal de HBO Max ([[project-hbo-max]]), Debbie Guerra de Arrive ([[project-arrive]]).

## rfp-training-guide
*Google Doc \"Payments & Yuno: Guía de Entrenamiento\" (glosario + productos + RFPs + call Riot) para entrenar a German en terminología técnica de payments*  
*type: reference · last updated 2026-08-03*

Google Doc de entrenamiento creado 2026-08-03: https://docs.google.com/document/d/1LOxFGmdlQ9ZypbT1y8E3fUxqGimrowXaa3Rq7qALPak/edit

Fuentes: RFP técnico de tokenización/routing (sheet 1L8znsdohMTpNZYxmX27fvIK4EdTM-5JESs8V1FWfvMw), RFP de Roblox (sheet 1WNgwouyGTV7N8GauvT6TtRy-DsvI9KcJDVR9M0EKVfU, tab "RFP Responses"), transcript call Riot Games 31-jul-2026 ([[riot-games]]) y docs.y.uno.

18 secciones: actores del ecosistema, anatomía del pago, routing, fallbacks/Monitors/retries, tokenización (vault, network tokens, network transaction ID), CAU, 3DS, fraude, PCI (SAQ A vs D), checkout/SDKs, suscripciones, webhooks/reconciliación, AI (Smart Routing + Payments Concierge), cheat sheet de números para RFPs (incluye pricing del RFP Roblox), lecciones del call de Riot y glosario A-Z. Si German pide ampliar o actualizar la guía, editar ese mismo Doc.

## reference-salesops-legal
*Canal Slack #salesops-legal (C07QPMCDMUH) = donde German pide NDAs y documentos legales; contacto Ivvy Soberay; formato y tono de sus mensajes*  
*type: reference · last updated 2026-09-27*

Los pedidos de NDA, documentos corporativos y revisiones legales de deals van al canal de Slack **#salesops-legal** (ID C07QPMCDMUH). Contacto habitual de German: **Ivvy Soberay** (U07V68ET42G). También responde María Gabriela Tovar (U0B2DSHUDM1).

**Formato que usa German:** un mensaje encabezado tipo "NDA Suno :thread:" y el pedido dentro del hilo, en inglés, corto, tono cercano ("Hello Ivvy!", "LMK if you need anything"), y suele cerrar con "I'll also forward you the email".

**How to apply:** redactar en inglés y dejarlo como borrador con slack_send_message_draft (solo admite un borrador por canal y no puede crear el hilo, así que encabezado y cuerpo van en un mismo mensaje). Los adjuntos de Gmail no se pueden subir desde aquí; German reenvía el correo. Ver [[project-cruz-verde]], [[project-hostinger]], [[project-suno-jasper]].

## reference-subscriptions-stats
*Where the Yuno Subscriptions engine stats come from (launch deck sep-2026, Reface 26.49 pp case via Payments Concierge), what is live vs roadmap, and Jarrett's gap list; use before quoting any subs number externally*  
*type: reference · last updated 2026-09-18*

**Fuente oficial del producto:** deck interno "Yuno Subscriptions · Internal Launch" (Subscriptions/deck-subscriptions-launch-3.pdf, offsite 7-11 sep-2026) y el Google Slides de Daniel Lozano "[WiP] Subscriptions Deck - Offsite" (id 189Bo4jm__Ox-UI5-jyoFhpeP6AL69wohkJKfKUSNdls). Daniel Lozano es el PM; pedirle OK antes de sacar cifras del deck a un prospecto (está marcado "internal, do not forward").

**Cifras del engine (Control Center, 31-ago-2026):** 16 merchants en producción, 135K suscripciones activas; aprobación por ciclo 86% tras retries vs 83% primer intento; 69K suscripciones past-due reactivadas en 30 días. Portfolio: $1.3B/trimestre de volumen recurrente en 65 merchants, 97% fuera del engine; $7.2M/mes declinado en renovación en el portfolio del engine (jul-2026), solo 47.5% de intentos recurrentes aprueban al primer intento (este último NO usarlo externo, es negativo). Magdalena ya usó "16 merchants / 135K" en outbound (15-sep).

**Stat 26.49 pp (US PayPal vs card):** es Reface, anonimizado. Payments Concierge en #roberto-ai, 9-sep-2026: 88,740 subs activas, 350,202 pagos recurrentes/mes, aprobación total 55.87%; US: PayPal enrollment 69.34%, Apple Pay 50.58%, Google Pay 46.48%, Card 42.85%; DE PayPal 88.29%. Ventana móvil de 30 días: refrescar antes de presentar. Es un spread entre MÉTODOS, no entre proveedores; no sirve como prueba de "segunda ruta"/retries. Concierge no puede autorizar uso externo; eso es Comms.

**Live (sep-2026):** planes con fases y precio por país; trials; retries DEFAULT / CUSTOM_SCHEDULE / SMART (ML) con A/B desde Dashboard; pause/resume/cancel/cambio de plan KEEP/RESTART; PAST_DUE + webhook en cada transición; meters (usage-based, gated por org); cards, Apple Pay, Google Pay, PayPal, Pix Automático; Analytics tab; Stripe Billing bridge y Stripe Proxy. Roadmap: promociones/cupones V0 fin sep-2026; test clock, prepaid, cambiar método de pago, pagar ciclo por link = backlog.

**Gaps (Jarrett, DM 31-ago-2026, parcialmente desactualizado):** sin bundles/add-ons/multi-línea, sin proration, sin entitlements, sin invoicing/tax/credit notes, sin dunning emails al cliente final, sin rev-rec/ERP. Jarrett: "if we don't have them we are better off not pitching" a quien pida billing engine completo. "Typical migration about a week" NO tiene fuente en ningún lado.

**How to apply:** para pitches de retries/recovery usar 83→86% y 69K reactivadas (con OK de Daniel); usar Reface solo como caso de visibilidad por método. Relacionado: [[project-yuno-vs-stripe-subscriptions]], [[feedback-published-stats-only]], [[project-peacock]].

## yuno-agents-platform
*Cómo funciona la plataforma interna Yuno Agents (ai.agents.y.uno): owner + admins por agente, transferencia de ownership vía equipo plataforma en #yuno-agents, Personal vs Service, Private/Public*  
*type: reference · last updated 2026-09-09*

Plataforma interna **Yuno Agents**: https://ai.agents.y.uno (agentes con Toolkits, Skills, Channels, Scheduled tasks, Evals, Settings). Soporte en Slack **#yuno-agents** (C0AT02E2DDK), equipo plataforma = subteam S08P1PFDQKV ("ia-crew"): Simón Martínez, Gustavo Mendes, Rafael Tejon, Ben Lee.

Hechos verificados en hilos de #yuno-agents (sep 2026):
- Cada agente tiene un **owner** y el owner puede **agregar admins** desde el workspace del agente. Los admins ven el agente en "My Agents" y pueden abrirlo/editarlo (hilo Melissa Pottenger 2026-09-08).
- Si el agente está **Private**, los admins agregados reciben error al abrirlo; hay que ponerlo **Public** (Ben Lee, mismo hilo). Al crear un agente **Service** queda Private por defecto.
- **Transferencia total de ownership**: la hace el equipo plataforma a pedido en #yuno-agents con el Agent ID (Gustavo Mendes, hilo 2026-09-02). SecOps (Chiara La Valle) no autoriza usar permisos de ex-empleados; agentes de equipo deben ser tipo Service.
- **No se puede cambiar Personal → Service** (Gustavo Mendes, 2026-08-10); hay que crear el agente como Service desde el inicio.
- Personal agents = DMs (incl. WhatsApp desde el celular); Service agents = canales compartidos para equipos (Simón Martínez, 2026-07-08).
- Toolkits tienen permiso "Can view" / "Can edit" por toolkit, y se pueden marcar tools exactas (Rafael Tejon, 2026-08-26). Conectores tipo Atlassian/Salesforce son per-user: cada usuario autoriza una vez.

Relacionado: [[lucky-agent-yuno-agents]].

## reference_yuno_positioning
*Official Yuno one-liner positioning / pitch to use in decks, emails, and deliverables*  
*type: reference · last updated 2026-08-27*

Canonical Yuno positioning statement (use verbatim or lightly adapted as the boilerplate in outreach, decks, and business cases):

"Yuno is an AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem that includes payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins to lower payment processing costs, increase authorization rates, expand globally, and become more operationally efficient."

Updated 2026-08-27 from "unified operating system" to "AI native operating system" per German's correction, confirmed while drafting his LinkedIn About section.

Four outcomes it drives: lower processing costs · higher authorization rates · global expansion · operational efficiency.

The fragmented ecosystem it orchestrates across: payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins.

Prefer this framing over the older "460+ integrations / 1,000+ methods / 180+ currencies / 190+ countries" stat-list boilerplate when a positioning/narrative line is needed (the stat list is still fine as supporting detail). Note "stablecoins" is now explicitly part of the pitch. Relates to [[feedback_no_dashes]] (avoid em-dashes when writing it out).

## yuno-pricing
*Yuno's standard product pricing model — $50K processed free, then $0.05 per transaction*  
*type: reference · last updated 2026-09-21*

Yuno's pricing model: the first **$50,000 processed is free**. Beyond that threshold, Yuno charges **$0.05 per transaction**.

**Why:** This is the standard pricing German uses whenever a deck, business case, proposal, or email references Yuno's cost/pricing to a prospect — it must always be stated this way, not approximated or invented differently.

**⚠️ 21-sep-2026:** The official Finance pricing policy ([[yuno-pricing-policy]]) does NOT contain this "$50K free then $0.05/tx" structure. The closest thing there is "first $50K TPV/month through Subscriptions included in pay-ins", and the policy says the platform fee is not waived. For formal proposals/quotes the policy governs; treat this entry as a lightweight default for outreach/decks only, pending German's confirmation of where it came from.

**How to apply:** Use this exact structure (free tier up to $50K processed, then $0.05/transaction) in any pricing section of a business case, deck, or outreach — e.g. [[project_business_case_tripadvisor_deck]], slide-builder/business-case skill outputs, CellPoint-style pricing slides ([[project_cellpoint_whitelabel]]). Consistent with [[feedback_no_false_info_disclaimer]]: never restate pricing differently or invent tiered variations not confirmed here — if a deal has custom/negotiated pricing, that overrides this default and should be noted as deal-specific, not treated as the standard rate.

## yuno-pricing-policy
*Yuno Products Pricing Policy (Finance, Laura Galan): list/minimum price por producto, zonas de aprobación green/yellow/red, segmentación V1-V5 x M1-M4, tranches vs tiers, credits, MMG, billing terms. Consultar SIEMPRE al construir propuestas o quotes*  
*type: reference · last updated 2026-09-21*

# Yuno · Products Pricing Policy (leído completo 21-sep-2026, cuerpo + 69 hilos de comentarios)

**Fuente:** Google Doc `Yuno_Pricing_Policy_Merchants_Banking_DRAFT_WIP`, id `11_giTduW5KONFvQ2qGYyH0_OKoPa8IVrn_x8KD7Uq3o`, owner Laura Galan (Finance), creado 27-jul-2026, última edición 21-sep-2026. Todo en USD.
**Companions:** Cheatsheet (Sheet `17Fv6SB8M-e-2zqCLzYWUSpsWe8wkt-60Aw9gs_ZxYZs`); Pricing Calculator Template (Sheet `1YtGixylPmxoZPe0v1YZnNlejFFcUUfcrrAZPUHofKR0`, tab `industry_gm` = gross margin por industria). Dudas: Slack `#finance-merchants`.

**Why:** German construye propuestas y necesita list price, minimum price, levers y reglas de aprobación de cada producto.
**How to apply:** Al armar cualquier propuesta, quote, pricing slide o respuesta de precio, partir de aquí. Es DRAFT WIP: si la propuesta es importante, releer el Doc en vivo (puede haber cambiado) y el calculator para el precio por segmento. ⚠️ INTERNAL ONLY: el minimum price es el walk-away line, NUNCA aparece ni se insinúa en nada customer-facing (decks, emails, propuestas). En entregables solo va el precio cotizado. Reemplaza como fuente formal a [[yuno-pricing]] (ver conflicto abajo).

## 10 fundamentals
1. Cotizar al merchant DESPUÉS de pasar por Salesforce (evitar take-backs).
2. Abrir en list price, nunca cruzar minimum price; el espacio entre ambos es negociable.
3. Zonas: 🟢 Green auto-aprueba; 🟡 Yellow revisión manual (RevOps, Sales Ops o GM); 🔴 Red requiere Global Controller/CFO + CRO.
4. Solo los levers listados en la página del producto; si no está listado, no existe.
5. Default Tranches (ladder); Tiers (cliff) solo si el deal lo exige (cede más margen).
6. Price splitting = lever más amplio, solo deals complejos/estratégicos y solo en los ejes que liste el producto.
7. Credits cubren el ramp de integración: reducen ítems específicos en meses específicos.
8. Contratos tienen Billing start date; billing NUNCA atado a la primera transacción live. El ramp se cubre con credits.
9. Estructura que ninguna página ofrece: escalar como business case a Finance + leadership (solo strategic merchants).
10. Salesforce no bookea precios fuera de política; bajo el mínimo sin sign-off, el deal se frena.

## Zonas y aprobaciones
- 🟢 Green: de list price hasta un límite inferior. Auto-aprobado en Salesforce.
- 🟡 Yellow: bajo green hasta minimum price. Aprobación manual RevOps/Sales Ops/GM, SLA 2 business days.
- 🔴 Red: bajo minimum price. Global Controller/CFO + CRO, SLA 5 business days. Solo decisión deliberada para cuentas estratégicas.
- Ejemplo del doc: list $0.030, min $0.020 → green $0.030–0.024, yellow $0.023–0.020, red <$0.020. El calculator da las zonas reales por merchant.
- También van por yellow: billing mensual de platform fee/MMG (en vez de anual), payment terms distintos a net 30, MMG embebido en la fee fija, waive de platform fee, plazos más largos.

## Segmentación (define list y min por merchant vía calculator)
- **Size** (tx pay-in mensuales steady-state, aplica a todos los productos): V1 <25K · V2 25K–100K · V3 100K–1M · V4 1M–5M · V5 >5M. ⚠️ Dimensionar por la OPORTUNIDAD, no por el logo.
- **Gross margin de la industria** (aplica a precios de pay-ins): M1 Thin <15% (airlines, delivery, mobility, bus/rail, remittance, food & drinks) · M2 Mid 15–35% (retail, restaurants, travel, ticketing, payments, marketplace, loyalty, e-learning) · M3 Healthy 35–60% (gaming, gambling, streaming, edtech, hosting, utilities) · M4 Rich >60% (software, AI, digital goods, luxury & apparel, social/advertising, crypto).
- "Overall deal size cannot be under 10k" (el doc no aclara si mensual o anual).
- **Strategic merchant:** TPV ≥ $38.0M/mes o ≥ 1.2M tx pay-in/mes; O al menos 2 de: market recognition, referenceability (logo rights; NDA total no cuenta), beachhead value, halo/network effect. CRO y Sales Ops llevan la lista.

## Toolkit
- **Billing unit:** fijo (platform fee) o usage (por evento). Solo tráfico live factura; sandbox/test nunca.
- **Modelos:** Flat · Tranches (default, cada banda a su precio y se suman) · Tiers (una banda aplica a TODO el volumen). Rangos en tx o en TPV. Ejemplo doc: 60K tx con bandas 10K@$0.065 / 40K@$0.050 / >50K@$0.040 → Flat $0.05 = $3,000; Tranches = $3,050; Tiers = $2,400. Pitch de tranches: "you always pay the lower rate on your higher volume".
- **Price splitting (4 ejes):** Business unit · Country/Region · Time phase (fases del contrato, no hora/día) · Payment method (cards vs APMs lo más común). Cada stream se tarifica sobre SU volumen, nunca se agrupa para alcanzar banda más barata. Menos streams posibles.
- **Credits:** monto fijo contra facturas mensuales nombradas, escrito en contrato. Solo contra platform fee, MMG y otras fees fijas; NUNCA para productos usage. Mes no usado se pierde (no se pospone ni acumula), no transferible, sin valor cash. No cambia list/min ni permite bajar del mínimo. Por encima de cierto tamaño requiere sign-off. Si la integración se demora, los credits no se extienden.
- **Moneda:** pricing USD / billing USD = estándar. USD/LC a pedido (tasa oficial del banco central, nombrada en contrato). LC/LC excepción solo MX, CO, BR, QA, SA. LC/USD no se usa. Si la ley exige facturar en LC (ej. dos entidades colombianas), es obligatorio.
- **Billing frequency:** platform fee y MMG = anual upfront (estándar); mensual vía yellow. Usage = mensual in arrears.
- **Payment terms:** net 30; excepciones por yellow.
- **Billing date:** siempre día 1 de un mes calendario, campo separado de la signature date, puede ser antes o después de la firma.
- **Jerarquía para armar el quote (top-down):** Business unit → Country/Region → Time phase → Payment method → pricing model → precio (price basis fijo vs % TPV solo en pay-ins y pay-outs). Usar solo los splits que el cliente realmente necesite.

## Catálogo: list / minimum (overall; el calculator da el precio por segmento)

| Producto | Unidad | List | Minimum | Status |
|---|---|---|---|---|
| Platform fee (merchants) | 1 cargo/mes | V1 $5,000 · V2 $7,000 · V3 $10,000 · V4 $16,000 · V5 $25,000 | $4,000 (todos) | Live |
| Pay-ins | tx exitosa (fijo $ o % TPV) | $0.10 | $0.01 | Live |
| Subscriptions | tx exitosa, % TPV | 0.7% TPV | 0.3% TPV | "Under development, not sellable yet" |
| Pay-outs | tx exitosa (fijo) | $0.07 | $0.03 | Live |
| Card Account Updater | 1 update | $0.40 | $0.20 | Live, billing activation pending |
| Network Tokens | creación / update | $0.35 / $0.07 | $0.20 / $0.04 | Live |
| Monitors | fee mensual + alerta | $0.02 | $0.001 | Live |
| Yuno 3DS | intento de autenticación | $0.06 | $0.02 | Live |
| 3DS external | intento | $0.06 | $0.02 | Live |
| Passkey | intento | $0.06 | $0.02 | Pilot |
| Risk conditions | tx evaluada | $0.02 | $0.001 | Live |
| Fraud Engine | screening call | $0.03 | $0.007 | Live |
| Chargeback Alerts | alerta matched (unmatched no factura) | $15 | $9.80 | Live |
| Reconciliation | fee mensual + tx reconciliada | $2,500/mes + $0.03 | $1,500/mes + $0.0085 | Live |
| PCI Token Vault | incluido en core | $0 | $0 | Live |
| Vault-only edge case | card almacenada/mes | $500/mes + $0.00015 por card/mes, anual upfront | — | Live |

PENDING / no vendible: Yuno Smart Optimization, Smart Authentication, Smart Protection (bundles padre), Payment Button, Tap2Pay, Tap2Add, precios de todo Financial Services (platform/maintenance fee, implementation fee, active client, integrations as a service). FS RevShare: list "15% of TPV", min equivalente ≥ $0.01/tx. Recovery/Nova: sección "WIP NOT REVIEWED", precios PENDING (cost-plus).

### Detalle por producto
- **Platform fee:** incluye connection management, routes & rules, transaction management, reporting & analytics, payment methods & checkout builder, users & roles (20 seats; extra $10 c/u), webhooks, PCI Vault. Se fija: flat; con allotment de tx incluidas (no preferido, single-month, sin rollover; ej. $12,000 con 50K tx); time-phased ramp (ej. 24 meses: m1-3 $0, m4-6 $3K, m7-9 $6K, m10-12 $9K, m13-24 $12K); por rangos de volumen/TPV (ej. ≤100K tx $10K, >100K $12K). Levers: Flat o Tiers, split solo Time phase, credits mensuales totales o parciales. Don'ts: no rollover del allotment; no apilar una platform fee por producto sobre la global; NO waive (excepción = yellow). Multi-entidad legal: definir prorrata por uso, peso fijo o una sola entidad. Bundleables en la platform fee: Network Tokens, Yuno 3DS y Passkey (suben el precio del pay-in), 3DS external, Risk conditions, Monitors; se recomienda monetizar por producto cuando se pueda. En contrato FS se llama "Maintenance fee".
- **Pay-ins:** nunca bundled ni gratis. TPV = Net TPV (suma de tx exitosas, sin chargebacks ni declines). Surcharges por conexión: Prosa (MX) MXN 0.601; Vtex / plataformas e-commerce 15% (el doc dice "of TPV", el comentario de Alonso dice "+15% sobre el precio estándar": confirmar); Pix Iniciador (PIX Automático/Biométrico) monto BRL en blanco. Card verification: PENDING si cuenta como tx. Levers: fijo o % TPV; Flat/Tiers/Tranches por tx o TPV; split en los 4 ejes; credits contra MMG. No agrupar volumen con otros productos.
- **MMG:** compromiso mensual (en tx pay-in o en conteo de todos los productos usage, siempre con equivalente en dinero); uno por deal, a nivel cuenta. Fixed fee + MMG = facturación mínima mensual; aditivo preferido, embebido = excepción legacy vía yellow. True-up al cierre: ej. MMG $40K, real $32K → $8K. Credits reducen el MMG en el ramp. El MMG NUNCA autoriza bajar del piso de $0.01.
- **Subscriptions:** motor propio, corre sobre token almacenado con cualquier PSP que acepte cards sin CVV. Factura ENCIMA de pay-ins (fee por la capa de gestión). Primeros $50,000 de TPV/mes por subscriptions incluidos en pay-ins (reset mensual). Split: BU, Country/Region. Sin credits.
- **Pay-outs:** split solo Country/Region; no agrupar volumen.
- **CAU:** Visa, Mastercard, ELO; uplift objetivo ~1.2–2.8 pts de aprobación. **Network Tokens:** modelo Flat únicamente; fallback a PAN si el token no está activo.
- **3DS:** se cobra por intento, tenga éxito o no. Providers: Netcetera, Checkout.com, Cybersource. Split: Country/Region, Time phase. No cobrar 3DS dentro del blend de pay-ins Y como línea propia (one lane per deal). **3DS external** no es lead product: solo si el merchant insiste en su provider; mismo precio a propósito para no competir con Yuno 3DS; pitch "move your volume to Yuno 3DS and we'll beat your current rate".
- **Risk conditions:** si no le atrae al cliente, bundlear en la fee mensual ($0). **Fraud Engine:** siempre standalone, Flat; conecta Cybersource, Riskified, Forter; emparejar con risk conditions como primer filtro barato. **Chargeback Alerts:** Ethoca + Verifi, 48h para refund/cancel; sin splitting.
- **Reconciliation packs:** 50K tx → $1,500/mes, adicional $0.032 · 250K → $5,000, $0.022 · 1M → $14,000, $0.016 · 3M → $30,000, $0.0085. GTM puede crear packs consistentes con estos, o usar tranches/tiers por tx reconciliada.
- **Nova (referencias pre-markup de contratos):** ~$0.01 por mensaje WhatsApp; survey session AR $0.10 · CO $0.03 · PE/CL $0.07 · resto $0.05; voz por minuto solo en llamadas conectadas (transcript ≥ 1,000 chars).

## Inconsistencias y puntos abiertos del draft (verificar antes de apoyarse en ellos)
- Billing frequency: §4 dice platform fee + MMG anual upfront; la página de platform fee dice "monthly, quarterly or annually in advance"; la de pay-ins dice "MMG: monthly in arrears"; el glosario dice MMG in advance.
- Glosario define "Band" como negociable sin aprobación, pero yellow sí requiere revisión manual.
- Subscriptions figura "not sellable yet" aunque German ya lo vende ([[project_suno_jasper]], [[project_peacock]]): confirmar con Laura/Finance antes de cotizar. Reconciliation figura Live, contra [[feedback_published_stats_only]] que lo marca roadmap.
- Monitors aparece bajo Optimization en el cuerpo y bajo Protection en la tabla.
- Comentarios abiertos: Laura pregunta a Alonso/Juan Bernate "do we go with these numbers?"; Rafael Werneck objeta los SLAs de aprobación (pide 6 h / 1 business day), el pricing en USD para Brasil y el sizing por oportunidad en enterprise; pendiente si implementation fee se embebe en el primer año de platform fee.
- Decisiones de los comentarios: costos de reselling NO se comparten con GTM (los protege list/min); comisiones hoy = billable revenue, no gross profit. La tabla de descuento por commitment (10%→2%, etc.) fue ilustrativa, no está en la política: no usarla.

## Relación con deals activos
Vault standalone: [[project_hostinger]], [[project_chess_com]]. Recon + network tokens ballpark: [[project_appmaking]]. Propuestas en curso para contrastar contra list/min: [[project_flighthub]], [[project_palco_ticketing]], [[project_cellpoint_whitelabel]].

---

# Accounts, deals and ongoing work

## project_ai_apps_batch_2026_06_17
*Batch of 5 AI/consumer-app SDR research briefs (2026-06-17) pending next steps (decks/outreach)*  
*type: project · last updated 2026-06-17*

On 2026-06-17 ran `/research` for 5 AI/consumer-subscription prospects. Briefs saved in `data/research/`:
- [[project_bending_spoons_psp]] — bending-spoons-2026-06-17.md
- [[project_replika_psp]] — replika-luka-2026-06-17.md
- [[project_lightricks_psp]] — lightricks-2026-06-17.md
- [[project_chai_ai_psp]] — chai-ai-2026-06-17.md
- [[project_perplexity_psp]] — perplexity-ai-2026-06-17.md

Common Yuno thesis across all 5: heavy Apple/Google IAP dependence (15-30% tax) + drive to web billing + APM gaps (UPI/Pix/local wallets) in emerging markets. User wants to "avanzar con todo el proceso" — i.e. continue to decks (/builddeck), business cases, and outreach (email1/email2/lk-opener) next.

## airalo-deck
*Airalo deck fix pass 2026-09-09 — thesis is \"orchestration is in, coverage is not\" (Stripe + partial orchestration layer confirmed); revenue ~$150M FY2023 Forbes; BeyondOne proof slide slug-scoped after The Solve*  
*type: project · last updated 2026-09-09*

Airalo deck (slug `airalo`, Supabase-driven) went through a full QA fix pass on 2026-09-09. Key standing facts:

- Thesis: **"orchestration is in, coverage is not"** — Airalo publicly names Stripe (own blog) and runs an orchestration layer in partial rollout. Never pitch "you have no orchestration"; two Airalo contacts were already told we know. Topology shows merchant → "Orchestration layer (partial rollout)" → Stripe.
- Revenue: **~$150M USD FY2023, reported by Forbes citing Alternative PE** (never Growjo's $286M; Airalo has never disclosed revenue). Funding: "$220M round led by CVC" — Airalo never uses "Series C". US holding entity with consumer sales contracted through its Singapore entity (not "headquartered in Delaware").
- Top markets (SimilarWeb all devices): US 23.5%, Canada 7.2%, Italy 6.9%, UK 6.6%, Germany 6.4%.
- Lead pain: MoR in Singapore vs. US/UK/DE/CA/IT traffic → cross-border corridors; USD processing vs 17 display currencies. Strongest APM gap: Brazil (Pix, Boleto, Elo & Hipercard first). No BNPL chips (ticket $4–$68). The 2025 "security breach" claim is dead (was 2 user reviews).
- Strengths: subscriptions LIVE (auto-renewals on saved cards); no Apple IAP/Play Billing = 100% of volume addressable; KYC/KYB (Jumio+Onfido) and Tax removed from MISSING.
- Business line is "Co-branding Solution", not "White-Label eSIM".
- Custom slide: [[SlideAiraloBeyondOne]] — BeyondOne (global eSIM platform on Yuno: 144 countries/1 integration, ~175K payments/mo, 7 providers, 0 degradations in 30 days, 8 local methods in core market, wallet 73% / bank transfer 81% approval; blended approval + loss data excluded). Slug-scoped after The Solve in SlideViewer + PrintViewer.
- Impact tiles use published figures per [[published-stats-only]]; reconciliation footnoted as roadmap.

## airlines-targeted-list
*Google Sheet \"Airlines Targeted · Oct 2025 to Oct 2026\" (37 airlines, leads, head of payments, last contact) built 2026-10-06 from Gmail, Calendar, NORAM/TCL/Recovery sheets; CSV copy in repo*  
*type: project · last updated 2026-10-06*

Sheet ID `1EsmeI6bwXYSFD3hVd1vsZJU_11Iu_GAWfGjFQ0XcV9Y` (German's My Drive), tab "Airlines - WW Status" (German renamed it), formatted 2026-10-06 with the house format (see [[sheet-house-format]]); shared as writer with the gtm-claude-editor service account. CSV copy: `Lists & ICP/airlines-targeted-2025-10-to-2026-10.csv` (commit 38198da, 2026-10-06).

37 airlines German touched between Oct 2025 and Oct 2026. Columns: Company, Website, HQ Country, Leads I've talked to, Head of Payments, Last contact, Status/notes, Sources.

Key facts captured there (verified via LinkedIn web search or Gmail signatures):
- United: Chris Thompson = Director Digital Payments (RFP owner). TAP: Diogo Jacinto = Payments Strategy Manager. flydubai: Jayadev Nair = VP Revenue, Expenditure & E-payments. Hahn Air: Benjamin Sibbald = Head of Payments. Air Canada: Keith Wallis = Sr Director Payments & Distribution; Giacinto Rico = Manager Distribution & Payment Forecasting. JetBlue: Brian Duran = Manager Payments. WestJet: Christian Novosel = EVP Chief Digital Officer. Air Serbia: Srdjan Prokic = Head of E-Commerce. Clic Air: Isaac Herrera Madrid = General Manager (since Feb 2026). Saudia: Frank Vahldiek left (was VP Digital & Ancillaries).
- Southwest's email domain is wnco.com (not southwest.com).
- LinkedIn DMs are not reachable from Claude Code; lead LinkedIn URLs came from the "Recovery - Lost Opps/Unresponsive" and NORAM Pipe sheets.
- The TCL "Final List" stakeholders column is misaligned (shows Coinbase/Riot/SoFi execs on airline rows). Never use it. See [[tcl-final-list-misaligned]].

**Why:** German asked for this list on 2026-10-06 to plan airline re-engagement; it is the canonical record of who was contacted and when.
**How to apply:** When German asks about an airline prospect, check this sheet first for leads and last-contact date before searching Gmail again. Update the sheet (not a new one) when new airline touches happen. Related: [[flair-contacts]], [[never-duplicate-decks]].

Second tab "Airlines in the US and Canada" (added 2026-10-06): 45 US and Canada based passenger airlines that sell direct (majors, LCC/ULCC, leisure, semi-private, regionals that sell direct), same columns; CSV `Lists & ICP/airlines-us-canada-2026-10.csv`. Excluded on purpose: capacity-purchase regionals (SkyWest, Republic, Envoy, Mesa, Jazz...), cargo/charter (Atlas, GlobalX, Omni), ceased carriers (Lynx, Jetlines, New Pacific) except Spirit, Silver and Sunwing which sit in German's own sheets.
- Allegiant Air is a live deal owned by Samuel Vieira and Adam Mawdesley: demo 2025-09-11, Salhar Memon = Manager Payments and Risk, Madilyn Jones = Payments, Jesse Johnson = Treasury; German handed over 2025-11-17. Allegiant and Sun Country are combining (2026).
- Air Canada: Keith Wallis is now Managing Director Customer Digital & Distribution; payments sits under Mark Nasr (EVP & COO).

Update 2026-10-06 (evening): the workbook is now shared with an external airline consultancy that will help Yuno get into these airlines. Added a "Level of engagement" column (col D) to both tabs with an 8-level scale and color coding, German asked to delete the Legend tab; the level definitions now live as a note on the column header plus a dropdown on the column (no extra tabs). Scale: Signed; Active deal; Met, paused; Met, stalled; Lost / declined; Responded, no meeting; Contacted, no response; Not contacted. Allegiant = Signed (see [[allegiant-signed]]); Sun Country rows note the Allegiant acquisition. German trimmed the US/Canada tab himself to 43 rows. The repo CSVs mirror the sheet after each edit.

## allegiant-signed
*Allegiant Air signed with Yuno (German confirmed 2026-10-06) and acquired Sun Country; deal was run by Samuel Vieira and Adam Mawdesley after German's Aug to Nov 2025 outreach*  
*type: project · last updated 2026-10-06*

Allegiant Air (Las Vegas, ULCC) is a SIGNED Yuno customer as of October 2026 (German, 2026-10-06). Allegiant also acquired Sun Country Airlines (2026), so Sun Country is now reachable through the Allegiant relationship.

History: German ran the cadence in Aug 2025 (Kim Downing, Danny Burguillos, Greg Anderson CEO, Kristen Schilling-Gonzales, Jennifer Resonable, Joe Kurishingal, Robert Neal), got the demo on 2025-09-11 (Justo, Bernabe, Samuel, Drew Snyder), and on 2025-11-17 handed Madilyn Jones's follow-up to Adam Mawdesley and Samuel, who closed it. Payments owner: Salhar Memon (Manager Payments and Risk); also Madilyn Jones (Payments), Jesse Johnson (Treasury), Jason Kolodny, Kathleen Steacy, Shannon Zamudio Perry.

**Why:** It is the first North American airline logo and the reference German can use with other US and Canada carriers; it also changes how Sun Country should be approached.
**How to apply:** Treat Allegiant as a reference account in airline outreach (with Samuel's OK on what can be said). Do not prospect Sun Country cold; route via Allegiant. Related: [[airlines-targeted-list]].

## project-american-red-cross
*American Red Cross — call inbound 2-sep-2026 (Susana SDR) con Carlos Carneiro (Merchant Services, seniority sin confirmar); sin recap ni follow-up después; brief en data/research/american-red-cross-meeting-brief-2026-09-02.md*  
*type: project · last updated 2026-09-24*

American Red Cross (una sola entidad legal; 63% del revenue FY2025 es B2B de Biomedical Services). Contacto: Carlos Carneiro (carlos.carneiro@redcross.org, "Consultant, Merchant Services" según ZoomInfo, sin LinkedIn encontrado). Call de 30 min el 2-sep-2026 10:30 COT organizada por Susana Awad (SDR), German invitado. Brief completo con ángulos (tres combinaciones de gateways desconectadas en donaciones, Invoice Central B2B sin vault, desembolsos internacionales por wire) en data/research/american-red-cross-meeting-brief-2026-09-02.md.

**Estado 24-sep-2026:** no hay recap de Fireflies, ni correo de seguimiento, ni respuesta de Carlos después del 2-sep. No está en el Deal Status GTM; fila opcional (Status "Discovery") en Lists & ICP/Pipeline Sync/manual_adds/ (flag --with-stale).

**How to apply:** antes de meterlo al tracker, confirmar con Susana si la call ocurrió y qué quedó; si se retoma, el ask es llegar al dueño de pagos (CIO org o Financial Shared Services), no vender a Carlos.

## project-anthropic-shaa
*Anthropic / Shaa (shaa@anthropic.com), hilo de Magdalena "Yuno's Subscription Engine for Anthropic" (Gmail 1a0a68b971b71667); Justo y Magda sin respuesta; German entra por email 6-oct tras WhatsApp*  
*type: project · last updated 2026-10-06*

**Anthropic.** Contacto: Shaa (shaa@anthropic.com), rol sin verificar. German lo conoció EN PERSONA en abril 2026 (SF, evento sin confirmar): nunca presentarse de cero en mensajes a Shaa, abrir con "since we met back in April". Hilo de Gmail "Yuno's Subscription Engine for Anthropic", id 1a0a68b971b71667, To Shaa, CC Justo y German.

**Cronología:** 15-sep-2026 Magda manda el deck de suscripciones (deck.y.uno/anthropic-subscriptions: engine de subs + Stripe Billing bridge, ángulo = billing y procesamiento en un solo proveedor, renovación declinada vuelve por el mismo rail) y ofrece presencial en SF en octubre con Justo, Juan Pablo, Sean y German. 16-sep Justo responde en el hilo ("en SF con CTO y VP Prod", OpenAI go local 25 mercados a dic + 40 a ene). 22-sep Magda invita al webinar "why subscriptions fail" (Piotr). Cero respuestas de Shaa. 6-oct-2026: German le escribió por WhatsApp y además entra al hilo por email (borrador reply a 1a0c677f88591967, CC Magda y Justo): corto y friendly, sin auto-intro (se conocieron en abril), está en SF, café cerca de su oficina o call, 30 min esta semana o la próxima.

**Why:** cuenta Bay Area de alta prioridad durante la estadía de German en SF (ver [[project-sf-relocation-fall-2026]]); el ángulo es suscripciones, no expansión de mercados.

**How to apply:** no repetir el pitch del deck ni links; German ya tiene canal de WhatsApp con Shaa. Si responde, proponer presencial en SF. Verificar rol de Shaa antes de escalar. Ver [[feedback-cc-handoff-reply-pattern]], [[feedback-email-no-links-sober]].

## project-appmaking
*Appmaking/Wowmaking (Cyprus app group, AstroSoul/Atrix) — demo done 2026-09-04, live Solidgate vs Truegate bake-off on web funnel, next step tech deep dive + proposal*  
*type: project · last updated 2026-10-05*

Appmaking LTD (Limassol, HE 437099) = one of 4 sibling Cyprus entities (Appmaking, Gototop, Applabel, Appsella); internal brand appears to be Wowmaking (Minsk, bootstrapped, ~77 staff). Astrology subscription apps: AstroSoul (6.5M installs, IAP-only, stale) + Atrix (the web bet).

KEY FACT: they already run a LIVE web quiz funnel (quiz.atrix.guide, MoR Appsella) A/B testing Solidgate vs Truegate (Larnaca orchestrator) with hand-tuned geo/OS splits. Yuno = neutral vendor #3. NEVER say "you have no orchestrator" or "PSP shortlist open". Sibling Astroline outdoes Atrix (BRL/INR pricing, 4 MoR entities incl. HK/Dubai).

CALL 04-sep (44 min, Gong) done: Tatsiana Gubarevich (Payment Manager) + Dzmitry Katsiushchyk attended (k.butrym declined). Confirmed: subscription business, **95% revenue web / 5% stores**; already run TWO orchestrators (Solidgate + a second they refused to name, underperforming; funnel evidence says Truegate ⚠️ never assert); want Yuno as THIRD layer to diversify, PSP-agnostic, out of flow of funds. **Solidgate exclusivity: cannot use Adyen/JPMorgan/Checkout.com via other gateways** (exclude from phase 1). Phase-1 PSPs for Yuno: Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl (signed, not live), NMI, +1 garbled (Nuvei? 🔍). Markets: EU + US ~40% + Japan + LatAm; Pix/UPI just started on Solidgate. Volumes: start ~10K txn/mo → ~$1M/mo ≈ 50K txn in 3-5 months; AOV ~$18; asked pricing IN WRITING with ramp to 100K txn. Explicit asks: network-token portability (own tokens, usable outside Yuno), TC40/TC15 SAFE data + bank/fraud rates per PSP, Verifi + Ethoca alert pricing, sandbox, docs, AI products (Concierge/Nova). NDA signed both parties (Susana sends with follow-up).

Follow-up recap email drafted in Gmail 04-sep (copy: Deals/Appmaking/appmaking-followup-email-2026-09-04.md); ⚠️ attach signed NDA before sending. Next call: week of Sep 14 (proposed 15/16, 5pm EEST) = preliminary proposal review + AI products walkthrough. PENDING: build preliminary proposal (platform fee + fee per successful txn, ramp pricing, standalone subs/vault/recon + Verifi/Ethoca) once they send ramp-up; confirm connector coverage in writing for their PSP list; provision sandbox.

Full briefs: data/research/appmaking-ltd-2026-09-03.md + appmaking-meeting-brief-2026-09-04.md; Google Doc "Meeting Brief: Yuno <> Appmaking (Sep 4, 2026)".

**Borrador fixed fee del 10-sep ($6,500 a $13,000, año 1 $120.5K con curva supuesta): SUPERSEDIDO por el deck del 14-sep (ver MODELO DE PRICING VIGENTE abajo). Archivos en Deals/Appmaking quedan como respaldo.**

**14-sep-2026: preguntas abiertas de Tatsiana** (tracker vivo en Deals/Appmaking/appmaking-open-questions-2026-09-14.md; German va pasando la info por partes): muestras TC40/SAFE, TRID bajo su entidad, proveedor de prevention alerts, lista completa de PSPs, intro a bancos (a la call). Call 15-sep 9 AM COT / 5 PM EEST, con Sean en copia del hilo.
⚠️ TC40/SAFE hoy: SOLO dLocal, dLocal deja archivos en SFTP, el equipo de Thiago baja la data y Leo la convierte en webhook al merchant (no se entregan archivos). Contradice el recap del 4-sep ("normalized reports across all your providers"): la respuesta debe corregirlo. dLocal no está en su fase 1.
Leo lidera TC40/SAFE internamente: Yuno no entrega archivos, los lee por el merchant y manda un webhook `payment.pre_chargeback` por pago (aviso, aún no es contracargo, no se movió plata). Su payload de ejemplo es de ADYEN (NOTIFICATION_OF_FRAUD), lo que choca con "solo dLocal": confirmar. Sanitizar el ejemplo (datos de otro merchant: BR/BRL/Google Pay) antes de compartir.

**14-sep-2026 (tarde):** respuestas 1 a 4 de Tatsiana ENVIADAS a las 15:19 COT (TC40/SAFE con payload genérico y corrección del recap, TRID default vs passthrough, Ethoca, top de PSPs por mercado; el correo afirma "full coverage of your phase 1 providers": verificar Ecompay/Payabl/NMI). Call 15-sep 9:00 COT confirmada por Tatsiana; Dzmitry, Sean y Joaquin aceptaron, Jarrett sin responder. Propuesta de pricing y slide (HTML + PNG) actualizadas con la CURVA REAL de Tatsiana (8-sep): 20K, 30K, 45K, 65K, 90K, 120K, 150K tx en meses 1 a 7, AOV $18 exacto; fully ramped en mes 7. Con esa curva: meses 1 a 7 $68,500 (520K tx), año 1 $133,500 (1.27M tx, $0.105), régimen $156K/año; el unitario baja todos los meses. Escalones por volumen recomendados. Pendientes para la call: status Verifi, proveedores con TC40/SAFE hoy, respuesta a "intro a bancos" (acordar con Sean), quién demo AI products, correr calculadora. Guía completa de la semana: Deals/weekly-prep-2026-09-14.md.

**Brief de la call 15-sep:** data/research/appmaking-meeting-brief-2026-09-15.md (Google Doc v2 con "Proposal Debrief": https://docs.google.com/document/d/1tWauG1gv7ImsxlQhyY_KRKw-YEnMSbuOF5fcIz0VQNs/edit; el v1 quedó renombrado "[superseded v1]"). Plan de la call dicho por German a Jarrett (Slack 14-sep 18:13): demo completo del dashboard de lo NO mostrado el 4-sep (se mostró routing, connections, subscriptions) y averiguar qué productos quieren usar; Jarrett sin responder ni aceptar. TC40/SAFE: Leo (Andres Leonardo Moreno) es el dueño interno; Thiago (reporting) lo refirió; Jira YSHUB-6715 y PRIOR-513. ⚠️ Verificar en el catálogo Shift4 y Payabl antes de repetir "full coverage" (no aparecen en la lista de proveedores del RFP de Hostinger; Ecommpay, Unlimint, NMI, Airwallex y Stripe sí).

**⚠️ MODELO DE PRICING VIGENTE (deck "Proposal - AppMaking + Yuno", Google Slides 1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc, 18 slides, PDF en Deals/Appmaking, revisado 14-sep noche):** German reemplazó el fixed fee por **platform fee + fee por tx exitosa, ambos escalonados por banda mensual**: $5,000 + $0.20 (0 a 25K, tope $10,000) / $5,500 + $0.12 (a 50K, $11,500) / $6,500 + $0.065 (a 100K, $13,000) / $7,500 + $0.05 (a 150K, $15,000) / $7,500 + $0.05 por tx arriba de 150K. Fully ramped $15,000/mes = $180K/año. Sobre la curva real de Tatsiana: año 1 $155,575 (1.27M tx, $0.12), meses 1 a 7 $80,575; unitario cae cada mes ($0.45 → $0.10). Todo verde sin aprobaciones (F1 $5,000 lista; $7,500 > piso verde F3 $6,325; $0.05 > ladder V3; take rate 56 bps). Quirk: la tarifa de banda aplica a todo el mes, la factura baja al cruzar banda (50,000 tx $11,500 vs 50,001 $9,750; M4 cuesta menos que M3). ⚠️ La slide 13 aún muestra meses y caja "What it means" de la curva vieja (Months 1 to 9 $109,000 / Year 1 $154,000): corregir a Month 1 / 2 to 3 / 4 to 5 / 6 to 7 / 8 onward y Months 1 to 7 $80,575, 520k, $0.155 / Months 8 to 12 $75,000 / Year 1 $155,575, ~1.27M, $0.12. Slide 11 tiene dos bullets heredados de FlightHub ("Your routing platform stays, Yuno extends it"; "Network tokens across all seven providers"). El fixed-fee ladder del 10-sep ($6,500 a $13,000, año 1 $133,500) queda como alternativa de respaldo, no se presenta. Paso a paso de venta, lógica y objeciones: brief 15-sep sección 4 "Proposal Debrief".

**CALL 2 (15-sep-2026, 47 min, grabada; Jarrett + Joaquin Mann nuevo BDM NA observando; Sean Calabro GM NA en la invitación):** volumen total **~500K tx/mes (agosto)**; ramp del correo **~20K mes 1 → ~150K mes 7** (30% de su volumen); driver del ramp = performance comparada. Solidgate sin mínimo escrito pero se abarata con volumen (por eso concentran ahí; Justo: Solidgate está en el money flow). Orquestador #2: equipo pequeño, fixes lentos, caídas de aprobación y billing; si migran, sería desde ellos. Quieren **TRID propio** (legal revisando; Jarrett: ~1 semana, tokens portables); no vaultean tokens hoy. Quieren usar un mismo PSP (Unlimit) por dos orquestadores (dolor: recon + alertas duplicadas). Gaps: LatAm, Korea, África; Pix/Pix Automático y UPI/Autopay ya vía Solidgate. 3DS nativo de cada orquestador. Sandbox probado y les gustó. Próximo: call corta para cerrar datos de la propuesta + canal de Slack.

**Feedback interno:** Sean pide saber (1) timelines y mercados prioritarios, (2) qué mueve el ruteo post go-live / estrategia de partners, (3) subscriptions y recon in-house o con Yuno. Justo (WhatsApp): la clave es **si los MIDs son de ellos o de Solidgate**; si son de ellos hay que onboardearlos con procesadores; **hablar con Piotr que los conoce bien**. Doc de preguntas consolidado (Sean + Justo + capabilities + volumen, depurado con lo respondido en la call): Deals/Appmaking/appmaking-discovery-questions-2026-09-15.md. Call corta pendiente para cerrar inputs; la propuesta se manda después (comprometer 17 o 18-sep).

**Brief de la call corta (proposal inputs), formato meetingbrief, 15-sep:** data/research/appmaking-proposal-inputs-call-brief-2026-09-15.md; publicado como artifact https://claude.ai/artifact/SXJg4yTSZp3giN9t1YgUBb (el conector de Google Drive no estaba disponible; .html y .docx en Deals/Appmaking para subir a Drive). Estructura: study zone (battle card, quién está, lo que estableció la call, asks de Sean/Justo, checklist de capabilities, modelo vigente, be ready for) y live zone (agenda 30 min, 63 preguntas con Notes, checklist).

**CALL 3 (15-sep-2026, call corta ~19 min, German con Tatsiana; transcript en Deals/Appmaking/appmaking-call-transcript-2026-09-15-tatsiana-short.md):** timeline "as soon as possible" si acuerdan pricing (TRID y nuevas conexiones con bancos toman tiempo). **Los MIDs son de ellos** (acuerdos directos con bancos); Solidgate tiene adquirencia y PSP propio y usan ambos; restricción contractual: PSPs que Solidgate ayudó a abrir (Adyen ej.) solo vía Solidgate. **Quieren a Yuno totalmente separado de Solidgate**, no lo dejan; Yuno = tercer orquestador. Ruteo post go-live: si funciona un PSP por dos orquestadores, repartirían Unlimit y Ecompay (ya con tráfico vía orquestador #2), sobre todo Europa; empiezan en 20K, escalan cuando reportes y fraude estén OK. Volumen: confirmó **~500K/mes** (German dijo 1M por error); podrían extender ramp a 200K nivel por nivel; necesitan ver precio a 20K y 50K; no acepta 250K sin Dzmitry. German ofreció primer mes sin costo a cambio de más volumen (abierto). Subscriptions engine: OK a $50K procesados gratis + por tx. Reconciliation: discutir después (siguen con manual). Monitors: German los ofreció gratis. **Propuesta se envía martes 16-sep.**

**PRICING v3 (decisión de German 15-sep, doc Deals/Appmaking/appmaking-pricing-v3-2026-09-15.md + prompt claude-design-prompt-pricing-v3-2026-09-15.md; reemplaza v2 en el deck cuando se aplique):** $6,000 + $0.24 (0 a 25K, tope $12,000) / $6,500 + $0.15 (a 50K, $14,000) / $7,500 + $0.09 (a 100K, $16,500) / $8,500 + $0.06 (a 150K, $17,500) / $8,500 + $0.05 arriba de 150K ($18,500 a 200K). Sobre la curva: M1 $10,800, M2 $11,000, M3 $13,250, M4 $13,350, M5 $15,600, M6 $15,700, M7 $17,500; meses 1 a 7 $97,200; año 1 $184,700 (1.27M tx, $0.145); régimen $210K/año. Sube y baja monotónico en su curva. Subscriptions engine: estándar ($50K procesados gratis, luego $0.05/tx). Monitors incluidos. Reconciliation, vault/network tokens, Verifi/Ethoca: Pending.

**PRICING FINAL EN LA SLIDE (deck slide 13, construido por German en Claude Design 15-sep, reemplaza la v3 propuesta):** platform fee BAJA y rate baja: $9,750 + $0.09 (0 a 25K, tope $12,000, mes 1) / $9,500 + $0.08 (a 50K, $13,500, meses 2 a 3) / $9,000 + $0.06 (a 100K, $15,000, meses 4 a 5) / $8,500 + $0.05 (a 150K, $16,000, meses 6 a 7 en adelante) / $8,000 + $0.045 arriba de 150K ($17,000 a 200K, $19,250 a 250K). Sobre la curva: M1 $11,550, M2 $11,900, M3 $13,100, M4 $12,900, M5 $14,400, M6 $14,500, M7 $16,000; meses 1 a 7 $94,350 ($0.181); año 1 $174,350 (1.27M tx, $0.137); fully ramped $16,000/mes = $192K/año. Incluye monitors; subs engine $50K gratis + $0.05; reconciliation y vault/tokens pending; Verifi/Ethoca fuera. ⚠️ Pendiente en la slide (15-sep): quitar "3-year contract term", corregir unitarios M4 $0.20 y M5 $0.16, agregar "Reporting & dashboard · Included". Quirk: M4 < M3 por cambio de banda. Ojo: en la call German dijo que el fijo subiría; la slide lo baja (mejor para ellos).

**PRICING FINAL v4 (deck revisado 15-sep 21:47 UTC, export en Deals/Appmaking/Proposal - AppMaking + Yuno (2026-09-15 export).pdf):** platform fee PLANO $8,500 en todos los tiers + rate que baja: $0.14 (0 a 25K, $12,000) / $0.10 (a 50K, $13,500) / $0.065 (a 100K, $15,000) / $0.05 (a 150K, $16,000, fully ramped) / growth tiers $0.0425 (a 200K, $17,000), $0.038 (a 250K, $18,000), $0.035 (>250K, $19,000 a 300K). Curva: M1 $11,300, M2 $11,500, M3 $13,000, M4 $12,725, M5 $14,350, M6 $14,500, M7 $16,000; meses 1 a 7 $93,375 ($0.180); año 1 $173,375 ($0.137); régimen $192K/año. Matemática verificada. "3-year contract term" se mantiene por decisión de German. Feedback dado 15-sep: slide 11 Key Advantages aún con copy de FlightHub ("Your routing platform stays, Yuno extends it" contradice a Tatsiana; "Network tokens across all seven providers" está pending) y notas de esa slide mencionan a Kraken; apéndice 15-16 compara contra "single PSP/MoR" (no aplica a Appmaking) con stats sin fuente; falta slide RBP "What we heard" + "How we start"; inDrive dice 11 países (research dice 10).

**18-sep-2026, alertas (Tatsiana 04:53 COT en el hilo "Call Recap and Next Steps"):** revisó la propuesta y no encontró el pricing de alertas "que pedimos incluir (RDR, Ethoca)". La slide 13 dice "$14 for every alert" sin nombrar la red. Juan Sebastián Bernate fue quien le dijo a German que cobrara $14 (Slack #int-ethoca-alerts-for-startup 20-ago: Ethoca cobra a Yuno $7/alerta, lista Yuno $15; Ethoca excluye Pharma, Nutra, Gaming, Continuity, Club, Adult, Direct Marketing MCC 5962/5966/5967; Appmaking es suscripción MCC 8999, validar "Continuity"). Verifi RDR: Yuno NO tiene integración directa ni lo revende; llega vía el PSP y Yuno lo marca `is_pre_dispute` (PRIOR-786 en prod 17-sep para Stripe y Adyen; Checkout.com también). Jarrett dijo en la call del 15 que RDR y Ethoca se están "revamping". Internamente (Valentina Oliveros 20-ago): alertas se reciben y se ven en el dashboard, sin superficie para actuar; backend v1 + inbox DAS-17387 en To Do en julio. Ajuste acordado con German para la caja de la slide 13: "Ethoca alerts, Mastercard network: $14 for every alert" + "Verifi RDR: enrolled through your PSP; cases surface in Yuno flagged as pre-dispute, live on Stripe today". German aplicó el ajuste A MANO en la slide el 18-sep (script Deals/Appmaking/build/fix_s13_alerts.py queda como referencia; token de Slides muerto, ver [[project-slides-api-token-dead]]). ⚠️ Al editar, el bullet 1 quedó "First 3K transactions processed free" en vez de "First $50,000 processed free" que dice el correo del 15-sep y el estándar de Yuno: pendiente que German lo revierta o lo confirme. Respuesta a Tatsiana aún no enviada.

**⚠️ 18-sep (German): Appmaking NO está con Stripe.** Nunca escribir "live on Stripe" ni usar Stripe como prueba en su material; su tráfico real va por Unlimit y Ecompay (fase 1 también Airwallex, Shift4, Payabl, NMI; Adyen excluido por Solidgate). Evidencia interna sobre RDR/pre-dispute: PRIOR-786 (prod 17-sep) solo Stripe y Adyen; Caio (#ext-boosta-yuno 22-jun): la entrega de payment.pre_chargeback depende de que el conector del proveedor esté enrolado en el programa de alertas, "not universal, confirm coverage per provider"; fuentes hoy Ethoca, Stripe EFW, Adyen RDR/RFI. Ninguno de los PSPs fase 1 de Appmaking está confirmado. Texto FINAL de la 3ª línea decidido por German 18-sep: "Verifi RDR: enrolled through your PSP; cases surface in Yuno flagged as pre-dispute" (sin "live on Stripe", sin condición por proveedor). Si Tatsiana pregunta por Unlimit/Ecompay, la respuesta honesta es "confirmándolo por proveedor": pedir confirmación a Valentina antes de la próxima call. Para Ethoca a $14: confirmar con Valentina/Juan Sebastián el matching de alertas (ARN/RRN) en Unlimit y Ecompay antes de contrato, como pasó con Worldpay en Boosta.

**18-sep (cierre del ajuste):** German decidió mantener el bullet 1 como "First 3K transactions processed free, then $0.05" (3,000 × $18 = $54K, algo más generoso que los $50,000 del correo del 15). Caja final de la slide 13: 3K tx gratis + $0.05; Ethoca $14/alerta; Verifi RDR vía PSP, flagged as pre-dispute. Borrador de respuesta a Tatsiana en el hilo (draft msg 1a0b4e2748ef8725, reemplaza al anterior ya borrado; cc Dzmitry, Jarrett, Sean, Piotr): nombra Ethoca $14, RDR vía PSP, avisa el cambio a 3,000 tx, propone revisar juntos el LUNES 21-sep a las 5 PM EEST (9:00 COT, libre en calendario; Palco es a las 11:00) y dice que Yuno está feliz de seguir avanzando. Invite pendiente hasta que ella confirme. ⚠️ Antes de enviar: confirmar que el link que ella abre (deck.y.uno/amprop, tracked por Gong) muestra la slide actualizada; si apunta a un PDF, re-exportar. Pendiente interno: Valentina confirme pre-dispute en Unlimit/Ecompay.

**18-sep (enviado):** la respuesta de alertas SÍ se envió el 18-sep 09:21 COT (Ethoca $14, RDR vía PSP, 3,000 tx gratis en subs, propuesta de call lunes 21). Pricing v4 ($8,500 + 7 tiers) APROBADO por Juan Sebastián Bernate en Salesforce el 17-sep (#deal-proposals-1bn-arr); los add-ons no están en esa aprobación.

**21-sep-2026 (Tatsiana 10:01 COT, mismo hilo; Piotr quedó fuera del cc):** siguen revisando pricing y piden (1) ballpark de reconciliation y network tokens (siguen "Pending" en la slide 13), (2) tres preguntas de one-click: CIT `CARD_ON_FILE` + `USED` salta CVV/3DS?; Apple Pay/Google Pay vaulteado se cobra sin abrir el wallet y hay que guardar el `vaulted_token`?; PayPal guardado se cobra sin redirect? (3) P.S. se perdió la invitación; quiere call cuando tenga toda la info. Huecos a las 9:00 COT (5 PM EEST): jue 24 y vie 25 (mié 23 hay Deal Desk 8:00 a 9:15).
Referencias internas de pricing (Slack): network tokens se cobran por EVENTO (creación + lifecycle update), nunca por uso; vault no se cobra si usan orquestación; decisión del dueño de la relación, se puede bundlear si el pay-in aguanta; mantener siempre wording de passthrough (Alonso Benavides, #deal-proposals-1bn-arr 10-jul). Números vistos: calculadora $0.2973 creación / $0.0595 update; FinX (Sara Gómez 28-ago) ~$0.20 / $0.011; deals cerrados $0.04 + $0.01 (APAC), $0.01 por token (Intch, deal de Piotr). Reconciliation: "paquetes + transacciones extra" (Laura Galan 28-ago); calculadora $0.0188/tx; Intch (Piotr) lo lleva como módulo opcional a $1,000 activable después. Ojo: settlement/fee recon marcado como no GA en QA de decks: confirmar alcance con Thiago de Souza y si Unlimit/Ecommpay son fuentes configuradas.
Hallazgos técnicos (verificar con Jarrett / Ilya Ryabukhin antes de escribirle): (a) ⚠️ ECOMMPAY, su PSP real: caso vivo en #ext-overgear-yuno-ecommpay (8 a 10-sep): saved card CARD_ON_FILE/USED + paso 3DS de Yuno + sin CVV = rechazo 3201 "cvv required"; sin paso 3DS y sin CVV pasa normal; escalado, sin fix confirmado. (b) Wallets: docs confirman que Apple Pay/Google Pay se desencriptan a network token, quedan como registro CARD oculto, el `vaulted_token` solo viene en la respuesta del CIT (con `vault_on_success: true`), no aparece en Retrieve Enrolled Payment Methods (FR OR-1122), cargos posteriores van por `detail.card.stored_credentials`; one-click sin hoja del wallet probado en otro merchant vía Stripe; depende del proveedor (casos de rechazo en Cielo, emerchantpay) y Google Pay PAN_ONLY devuelve FPAN; riesgo CORECM-19001 sobre retrieve-by-id. (c) PayPal: método `PAYPAL_ENROLLMENT` (aprobación única con redirect, luego `vaulted_token` sin redirect); Reface lo usa en prod; gotcha: stored_credentials va en `detail.wallet`, no en `detail.card` (ticket 21-sep de Varun Pathi); ZPY-590 (Zuora) seguía fallando al 20-ago; solo workflow Checkout/SDK, no Direct. Nunca nombrar esos merchants a Appmaking.

**21-sep (tarde), add-ons para la slide 13:** Laura Galan compartió el "Yuno · Products Pricing Policy" (Google Doc 11_giTduW5KONFvQ2qGYyH0_OKoPa8IVrn_x8KD7Uq3o, DRAFT_WIP). Lo que aplica: PCI Token Vault $0 bundled en core (nunca cobrarlo aparte si procesan pay-ins); Network Tokens list $0.35 creación / $0.07 update, MÍNIMO $0.20 / $0.04 (interno, nunca mostrarlo), bundleable en platform fee; Reconciliation siempre standalone, mínimo $0.0085/tx + $1,500/mes, list $0.03 + $2,500, packs 50K $1,500 (+$0.032), 250K $5,000 (+$0.022), 1M $14,000, 3M $30,000; Chargeback Alerts list $15 / mín $9.8 por alerta MATCHEADA (la slide dice "every alert"); zonas verde/amarilla (RevOps, Sales Ops o GM, 2 días)/roja (CFO + CRO, 5 días); Subscriptions figura "under development, not sellable yet" con $50K TPV/mes incluido y 0.3% a 0.7% de TPV. ⚠️ Mi recomendación previa de network tokens ($0.05 + $0.01) queda BAJO el mínimo = zona roja; German debe decidir (established / floor / list / included). German pidió: duplicar la slide 13 y en la copia poner token vault gratis, network tokens y un estimado de reconciliation. Script listo y probado offline: Deals/Appmaking/build/dup_s13_addons.py (--inspect, --nt obligatorio, --matched, --dry); NO aplicado porque el token de Slides sigue muerto (ahora "deleted_client"), ver [[project-slides-api-token-dead]]. Texto de la caja: título "ADD-ONS", subtítulo "Estimated pricing. Reconciliation is optional and can be added later.", fila 1 "Token vault Included · Network tokens $X per token, $Y per update", fila 2 "Reconciliation $1,500 / month incl. 50,000 reconciled trx, then $0.032 each" (en su rampa: $1,500 hasta el mes 3, ~$4,700 a 150K; sobre ~160K conviene el pack 250K).
**Copia del deck (21-sep 15:26 COT):** German pidió copiar el Google Slides y hacer el ajuste ahí. Copia creada vía Drive: "Proposal - AppMaking + Yuno (add-ons, 2026-09-21)", ID 1bAhlH3l7fDhmvxokTFvGHsk0wY4xqjQcIIYwoGAJy-U, misma carpeta. `dup_s13_addons.py` apunta a esa copia por defecto (`--pid` para otro deck); el original detrás de deck.y.uno/amprop no se toca. Sigue SIN aplicar por el token de Slides. Vía rápida propuesta a German: correr él mismo `auth_slides.py ~/.config/mcp-gdrive/gcp-oauth.keys.json` (cliente OAuth vivo del MCP de gdrive; Claude no lee ese archivo) y habilitar la Slides API en ese proyecto si hace falta. Opción de network tokens a aplicar salvo que diga otra cosa: `established` ($0.05 + $0.01), con el aviso de zona roja antes de enviarlo.
**Prompt de Claude Design (21-sep):** German prefirió hacer el ajuste en Claude Design en vez de reautenticar la Slides API. Prompt en Deals/Appmaking/claude-design-prompt-addons-box-2026-09-21.md: duplica la slide 13 como 14 y cambia solo la caja inferior derecha a "ADD-ONS" (vault Included; network tokens $0.05 creado + $0.01 update; reconciliation $1,500/mes con 50,000 incluidas, luego $0.032). Incluye sincronizar la caja inferior izquierda con el texto puesto a mano en Google Slides el 18-sep (3K trx, Ethoca $14, Verifi RDR), porque el canvas de Claude Design puede estar desactualizado.
**Respuesta a Tatsiana (21-sep, BORRADOR en Gmail, sin enviar):** draft msg 1a0c5bf6bcda6d3d en el hilo (reply a 1a0c47d10ec58f1a; cc Dzmitry, Jarrett, Sean; Piotr fuera). German ajustó la propuesta vía Claude Design: slide 14 "PROPOSAL · PRICING" con Token vault Included dentro de "What the rate covers", caja ADD-ONS (network tokens $0.05 creado + $0.01 update; reconciliation $1,500/mes incl. 50,000, luego $0.032) y Ethoca "$14 per alert"; export "Appmaking-Yuno-Proposal" (Slides 1S67SOkg0uw2QkAb4b9mAgRHyfd9DP9s7cVgzKVJpTV4). El correo repite esos números, responde las 3 preguntas de one-click con docs + casos internos (sin nombrar merchants), promete validar Unlimit y Ecommpay en sandbox y propone call jueves 24-sep 5 PM EEST (9:00 COT) con Jarrett + canal de Slack. Copia y tabla de fuentes: Deals/Appmaking/appmaking-reply-email-2026-09-21.md. Pendiente antes de enviar: adjuntar el PDF; network tokens sigue en zona roja sin firma; confirmar con Jarrett el requisito de vaulting de PayPal y ZPY-590.
**Respuesta a Tatsiana v2 (21-sep 17:45 COT, BORRADOR):** draft msg 1a0c61f1e7db4171 reemplaza a la v1 (borrada). Incorpora lo que respondió el bot Jordan Belfort en el DM de Slack de German (contestó en ALEMÁN, probablemente por leer "German" como idioma; pedirle "answer in English" la próxima vez): casos de step up (issuer, riesgo, exención rechazada, regulación local), token del wallet atado al dispositivo, dominio Apple Pay verificado, PayPal = billing agreement con botón de enrollment dedicado (changelog Web SDK v1.11.9, 18-sep). Foco del correo: responder cada pregunta + propuesta adjunta con el full package; cierra con call jueves 24 5 PM EEST con Jarrett. Falta: adjuntar PDF y enviar.
**Slide 13 FINAL (21-sep noche, imagen de German) y respuesta v3:** la slide quedó como una sola (13), con caja ADD-ONS: **PCI token vault $500 / mes** (ya NO incluido; la policy dice $0 bundled y prohíbe cobrarlo aparte a quien procesa pay-ins, $500 es el precio "vault-only": avisado a German), network tokens $0.05 creado + $0.01 update, reconciliation $1,500/mes incl. 50,000, luego $0.032. Panel azul "fully ramped at 150,000": transacciones $7,500 + platform $8,500 = payments $16,000/mes ($192,000/año); vault $500; network tokens $1,200 (supuesto 20,000 tokens nuevos + ~17,000 updates; la etiqueta dice "80% of trx", confusa); reconciliation $4,700; total estimado $22,400/mes, $268,800/año; $0.107 por trx en payments, $0.149 con add-ons. Ethoca "$14 per alert". Borrador v3 en Gmail (draft msg 1a0c6240f0cd9ce6; v1 y v2 borradas): German pidió lenguaje simple, sin campos de API; el detalle técnico lo lleva Jarrett a la call del jueves 24.
**Respuesta v4 (21-sep 18:00 COT, BORRADOR draft msg 1a0c62defbf08503; v1 a v3 borradas):** sección one-click verificada con fuentes primarias. Cambios: "normally no 3DS" era sobreafirmación (los docs dicen que un CIT "typically requires cardholder authentication") → ahora "Yuno does not ask for the CVV and does not force 3DS; runs if your routing rules call for it or the bank demands it"; token del wallet = DPAN atado al dispositivo (Apple: se desactiva al cambiar de teléfono o quitar la tarjeta); PayPal debe APROBAR y habilitar reference transactions (developer.paypal.com). Jordan Belfort no entregó el fact-check (respondió "still working", reacción ❌). ⚠️ Riesgos internos para la call con Jarrett: ECOMMPAY 3201 "cvv required" en saved card + 3DS de Yuno sigue ABIERTO desde 8-sep sin fecha de fix; UNLIMIT one-click sin CVV corregido en prod 18-ago (YSHUB-6529), ajuste en curso YSHUB-6951 / PR #173, conexión debe ser tipo "recurring", 3DS hospedado por Unlimit no soportado (PRIOR-1137), rebills de wallet vía Unlimit rotos hasta 10-sep (YSHUB-6814).
**Respuesta v5 (21-sep ~18:10 COT, BORRADOR draft msg 1a0c6323ea2ae6c6; v1 a v4 borradas):** Jordan Belfort sí terminó el fact-check (en inglés): confirmó 1a, 2a, 2b, 3a; pidió reformular la causa de ruteo (1b) y marcó "varies by provider" (2d) como sobreafirmado porque el framework es portable. Aplicado: "if your routing rules are set up to request it", portabilidad del token ("whichever provider your routing selects", textual en docs) + caveat por proveedor, "if it expires" en el token del wallet, y dos notas de implementación verificadas textual en docs (crear el customer antes y mandar su ID o no vuelve token; marcar bien stored credentials o bajan aprobaciones y se pierden disputas). No aplicado: su cita de `expires_at` (no está en el doc), límites del agreement de PayPal (sin fuente). Tabla completa en Deals/Appmaking/appmaking-reply-email-2026-09-21.md. Falta: adjuntar PDF y enviar.
**Respuesta v6, revisión final (21-sep ~18:25 COT, BORRADOR draft msg 1a0c64888d2c786f):** German editó el v5 a mano en Gmail (link https://deck.y.uno/amprop en vez de adjunto; "We can walk" en vez de "Jarrett can walk"); por eso NO se borró su borrador (r-4366462570319751211) y el v6 quedó como segundo borrador en el hilo con sus ediciones incluidas: debe descartar uno. ⚠️ El slug correcto del link de la propuesta es `amprop` (una p), verificado decodificando los correos del 15 y 18-sep; es un link de Papermark, hay que subir la versión nueva del PDF ahí para que sirva la slide 13 actual. Correcciones del v6: lógica de 3DS en dos situaciones, exención de bajo valor (menos de €30; su ticket ~$18), condición "save option on" en wallets, "usually tied to the device", nota de customer ID sin ambigüedad. **Regla aprendida:** antes de recrear un borrador, revisar si German lo editó a mano (el messageId cambia); si lo editó, no borrarlo.
**Borrador DEFINITIVO (21-sep ~18:35 COT):** German pidió borrar el draft y crear el último. Único borrador en el hilo: draft r5872066007782123811, msg 1a0c65059f126c3c, mismo texto del v6 (link https://deck.y.uno/amprop, "We can walk", low value exemption). El v6 anterior ya no existía y el v5 editado a mano se borró por instrucción suya. Falta solo que German confirme que el link de Papermark sirve el PDF nuevo y lo envíe.
**Borrador v7 SIMPLE (21-sep ~18:50 COT, único en el hilo: draft r7512580152847433251, msg 1a0c657b7636981e):** German quitó a mano la línea del vault ($500) y el párrafo del total estimado, y pidió las respuestas de one-click lo más simples posible y sin "developer notes". Quedó: pricing solo network tokens + reconciliation; 2 o 3 frases por pregunta; validación en sandbox de Unlimit y Ecommpay una sola vez al cierre; call jueves 24 5 PM EEST. Link directo https://deck.y.uno/amprop (su versión pegada traía un redirect google.com/url).
**Borrador v8 (21-sep ~19:00 COT, único en el hilo: draft r6631016278681225668, msg 1a0c65ba5faa2d1c):** German pidió quitar los "Yes." al inicio de cada respuesta y la frase "We will validate all three on Unlimit and Ecommpay..."; el cierre quedó "We can walk your technical team through the details on a call. Does Thursday at your 5:00 PM work?". El correo ya no menciona la validación en sandbox: el bug de Ecommpay (3201) hay que llevarlo con dueño a la call del jueves 24.
**Estado 24-sep-2026:** el correo v8 (full package + one-click) SÍ se envió el 21-sep 23:48Z proponiendo jueves 24 a las 5 PM EEST; Tatsiana NO respondió y no hubo call el 24. Tatsiana se conectó al webinar de subscriptions del 23-sep (sesión de Piotr sobre por qué fallan las renovaciones; dato de German). FUP v2 en BORRADOR en Gmail (draft r1173793838454375522, msg 1a0d3fde0e771898, reply al mensaje enviado 1a0c65f4246c28ba, cc Dzmitry+Jarrett+Sean; el v1 r-6863983892358874360 se borró): reconoce el webinar y ofrece ayuda, pregunta avances del pricing review y propone revisar la propuesta juntos martes 29 o miércoles 30 a las 5 PM EEST. ⚠️ 5 PM EEST = 7 AM PT (German en SF desde el 28-sep). Texto en Deals/Appmaking/appmaking-followup-email-2026-09-24.md.
**28-sep-2026: Tatsiana RECHAZÓ la propuesta** (mensaje visto la mañana del 28; texto exacto no leído, Gmail no disponible en esa sesión). Hipótesis de German: precio, por todo lo que rodea al subscriptions engine. Sean Calabro (WhatsApp 6:57 AM) se sorprendió y pidió: solicitar una call para entender la decisión, SIN preguntas en el correo (mejores respuestas por teléfono que por email). German quiere darle la vuelta al deal. Correo redactado (honesto, corto, pide call de 20 minutos esta semana, sin precio ni concesiones): Deals/Appmaking/appmaking-rejection-reply-email-2026-09-28.md. Pendiente: confirmar si Sean ya le escribió a Tatsiana en el hilo, enviar, y preparar la call de recuperación (palancas: subs engine, platform fee, add-ons).
**Estado 5-oct-2026:** texto exacto del rechazo de Tatsiana (28-sep 10:46Z): "After internal discussion, we've decided to move forward with a different solution that better fits our business needs at this stage" (sin nombrar razón ni proveedor). La respuesta de German del 28-sep (pide call de 20 min, "I did not expect it") SÍ se envió a las 12:13Z. Sean Calabro SÍ escribió en el hilo el 1-oct 09:30Z: se presentó, preguntó si fue pricing, capability, timing o fit, y pidió call de 20 min con German y él "this week or early next" a su 5:00 PM. Tatsiana no respondió a ninguno. FUP #3 en BORRADOR (5-oct, reply al mensaje de Sean 1a0f6cceb9d1ffa3; cc Dzmitry, Jarrett, Sean): corto, sin preguntas, "sit down to understand what the right solution looks like for Appmaking and what we would need to do differently to be that solution", propone miércoles 7 o viernes 9-oct a su 5:00 PM (7:00 AM PT, libre en calendario). Copia: Deals/Appmaking/appmaking-followup-email-2026-10-05.md. Si no responde: cambiar de canal (LinkedIn/WhatsApp) o pausar y retomar en 2027.
**5-oct (tarde): Piotr entra al deal.** Sean le pidió ayuda a Piotr Sierpinski (Sales Manager Europe, Slack U08RSQDCQ3U). Piotr (DM 5-oct): hay un **Stripe event en Warsaw el jueves 8-oct**; oyó de un "common friend" que Appmaking estará ahí, pero hay que confirmarlo preguntándoles en el correo (no revelar la fuente). Piotr se ofrece a conocerlos ahí en persona. FUP #3 REHECHO (borrador en Gmail, reply a Sean 1a0f6cceb9d1ffa3; cc Dzmitry, Jarrett, Sean y ahora Piotr): primero in-person con Piotr en Warsaw el jueves; si no van, call online con German y Sean el viernes 9-oct a su 5:00 PM (7:00 AM PT). Copia: Deals/Appmaking/appmaking-followup-email-2026-10-05.md.
**5-oct (ajuste de tono):** Piotr YA estaba presentado en el hilo desde el 15-sep (cc de German; Piotr se presentó como basado en Warsaw, BD Europa, foco subs y apps); el intento de verse en Limassol (WN Conference) no cuajó y Tatsiana cerró con "Hope we can catch you next time!" (18-sep). El FUP #3 trata Warsaw como ese "next time", sin volver a presentarlo ("Piotr will be at the Stripe event in Warsaw this Thursday, his home city... He is in copy"). Borrador vigente creado 5-oct (único en el hilo; los dos anteriores borrados).

## project-arrive
*Arrive (Arrive Recommerce, arrive.com) — Amit Chhabra (Chief Architect for Payments) call 29-oct-2026 vía Susi; Debbie Guerra (Head of Payments) va a Money20/20 Vegas; pedido de intro para café en borrador*  
*type: project · last updated 2026-10-05*

**Arrive** = Arrive Recommerce (arrive.com), plataforma de rental y resale para marcas (Eddie Bauer, YETI, Burton). No confundir con Arrive Logistics.

**Contactos:** Amit Chhabra, Chief Architect for Payments (amit.chhabra@arrive.com). Debbie Guerra, Head of Payments según German (debbie.guerra@arrive.com), título sin verificar.

**Cronología:** German outbound a Amit 27, 30, 31-mar y 2-abr-2026 ("Payments @ Arrive", "How about success?"), sin respuesta. 2-oct-2026 Susana Awad (Susi) escribe a Amit y a Debbie por separado para verse en Money20/20 (German en cc del de Amit). 3-oct Amit: no va al evento, acepta call 1 o 2 semanas después. **Call confirmada jueves 29-oct-2026 1:00 PM PT** (evento "Meeting with Susana Awad", Susi + German + Amit). Debbie sin respuesta a Susi, pero aparece en la lista de asistentes de Money20/20 (German, 5-oct).

**5-oct-2026:** BORRADOR en el hilo "See you at Money 20/20?" (reply a Susi, To Amit, cc Susi): agradece la call del 29, dice que lleva meses siguiendo a Arrive, cuenta que vio a Debbie en la lista y pide que los conecte para un café en Vegas, dejando claro que la call con él sigue igual. Copia: Deals/Arrive/arrive-amit-money2020-email-2026-10-05.md.

**How to apply:** tratar a Amit como el dueño técnico y no saltarlo; Debbie es la puerta comercial. Preparar brief antes del 29-oct (stack de pagos de Arrive, modelo rental/resale, marcas partner). Relacionado: [[project-sf-relocation-fall-2026]].

## project_babbel
*Babbel (Lesson Nine GmbH) — multi-PSP (Adyen+Stripe) no orchestrator; orchestration + churn-recovery angle*  
*type: project · last updated 2026-07-27*

Babbel (babbel.com) — language-learning subscription, Berlin (Babbel GmbH / Lesson Nine GmbH parent) + Babbel Inc. (Delaware/NY, US entity). €352M revenue FY2024 (+6.6%), 18M subscriptions sold 2024 / 25M+ cumulative. New CEO Tim Allen (Jun 2025), IPO "off the table", AI focus. CFO Dr. Christian Baier owns payments (no VP Payments named). Funding ~$34M (Scottish Equity Partners, Kizoo, REV, IBB — NOT Reach Capital/Scottish Mortgage/Vitruvian).

Traffic: US 36.29%, Germany 16.02%, France 7.82%, Italy 5.23%, UK 4.86% (top-5 only public), ~3.5-3.9M visits/mo declining. Local entities only in DE + US; FR/IT/UK cross-border.

**Lead angle (NOT "you lack APMs"):** multi-PSP, NO orchestrator. **Adyen confirmed first-party** (Adyen knowledge-hub names Babbel running Auto Rescue failed-payment recovery, dated 2026-06-16) + **reported Adyen→Stripe migration** ($100M+ recurring revenue, manual consultant-led via Invocation.io). Failed-payment recovery done PSP-side (Adyen only), not across processors. babbel.gifts on separate Shopify rail. = classic orchestration pitch (like [[project_nyt_gus_jacobs]], [[project_lightricks_psp]]).

APMs (from Babbel's OWN help center, verified): cards + PayPal (worldwide EXCEPT Turkey & Brazil) + Apple Pay + iDEAL (NL only) + Klarna (BE only). NO German-local methods listed in home market. SEPA/Sofort/Giropay/Google Pay = NOT VERIFIED (don't claim absent). Secondary angle = thin geo-gated local methods.

Complaints (strong): auto-renewal surprise charges (#1, BBB 90/3yr), 50% partial-refund friction, account-updater re-billing without consent, PissedConsumer 1.4/5. → cross-processor retries + account updater + smart routing.

ICP score 16 = 🔴 High. Research 2026-07-27: `data/research/babbel-2026-07-27.md`. 3rd e-learning after [[project_cambly]], [[project_praktika_psp]]. ATV ~$60-90 blended (monthly $14.99 → annual $95.88 → lifetime $249-299).

## project_bending_spoons_psp
*Bending Spoons payment stack + Yuno angle (research 2026-06-17)*  
*type: project · last updated 2026-06-17*

Bending Spoons S.p.A. (Milan app roll-up: Evernote, WeTransfer, Vimeo, Remini, Splice, Meetup, AOL, Eventbrite). Filed Nasdaq IPO (ticker BSP) 2026-06-08, ~$20B target. FY2025 rev ~$1.31B, ~9M subs, 500M+ MAU.

Payment stack: fragmented per acquired brand — WeTransfer/Vimeo = Stripe, Evernote = card + PayPal via MoR "Conceptive Apps LLC", all mobile = Apple/Google IAP. F-1 admits ~⅓ of electronic-payment revenue runs through stores at 15-30% vs ≤5% for Adyen/PayPal/Stripe. No third-party orchestrator (in-house "Spoon Engine" payments).

Yuno angles: (1) IAP fee leakage quantified in their own S-1 — strongest cold open; (2) post-acquisition PSP consolidation layer (buys a company every few weeks); (3) APM gap in top markets (Brazil/India/Philippines/Japan). Best cases: Rappi, Reserva, InDrive. Part of [[project_ai_apps_batch_2026_06_17]].

## project-bounce
*Bounce (luggage storage, bounce.com): campaña de Samuel Carreño 28-sep-2026 a 11 contactos con German en CC; 11 replies en borrador Gmail 29-sep; contacto previo real = correo a Léa Brutkiewicz oct-2025 que declinó sin dar razón; stack Stripe Connect*  
*type: project · last updated 2026-09-29*

Bounce (bounce.com, también usebounce.com): red de luggage storage, CEO y cofundador Cody Candee, oficina en Lisboa además de US.

**Datos públicos verificados 29-sep-2026:**
- Stripe case study: 32.000+ locations en 100+ países; usa Stripe Connect, Payments, Link, Radar y Sigma; Europa y UK son la mitad del revenue.
- Checkout (help center): tarjetas, PayPal, Apple Pay, Google Pay y Bounce Credits. Sin métodos de pago locales.
- Serie B de $19M en nov-2024 liderada por Sapphire Sport (a16z y General Catalyst ya estaban); APAC creciendo hasta 4x YoY según el CEO en esa fecha.

**Contacto previo (Gong, cuenta CRM 001Ps00000Zdu9SIAR):** German escribió "Payments at Bounce" a Léa Brutkiewicz el 28-oct-2025. Ella respondió: "For now we won't move forward but if it change in the future I'll let you know". No dio razón ni mencionó orquestación, Stripe o escala. Sin llamadas en Gong.

**Campaña de Samuel Carreño (Global Sales Strategy Associate), 28-sep-2026:** correo "Bounce payments convo" a 11 contactos, uno por hilo, German en CC: Andrew (andrew@bounce.com), Cody (cody@usebounce.com), Olivier Russeau, Ryan Fong, Luís, Bruno, Johnny, Tiago, Guilherme (duarte@usebounce.com), Lennart, Laura. ⚠️ El correo de Samuel dice que Bounce "was looking into orchestration but still scaling"; el registro no lo respalda, así que los replies de German solo dicen que estuvo en contacto el otoño pasado y el timing no era el correcto.

**Estado 29-sep-2026:** 11 replies de German en BORRADOR de Gmail, cada uno dentro de su hilo, CC Samuel. Proponen 20 minutos jueves 1 o viernes 2-oct en la mañana PT (tarde en Europa). Ángulo: mantener Stripe y sumar adquirencia y métodos locales. Prueba alternada: inDrive 90% en 10 mercados o McDonald's +4.7%. Roles de los 11 contactos sin verificar.

**Why:** Samuel replica el patrón de Magdalena de meter a German en CC para que entre al hilo.

**How to apply:** si alguien responde, revisar el hilo y agendar; si German envía después del 2-oct, cambiar los días propuestos. No nombrar a Léa salvo que German lo pida. Nunca plantear reemplazar Stripe. Patrón del reply en [[feedback-cc-handoff-reply-pattern]]; campaña hermana en [[project_magdalena_bc_campaigns_sep_2026]].

## project_british_airways
*British Airways web deck (/m/british-airways, vertical merchant, 11 slides): edición de texto 21-sep-2026 aplicada solo en Supabase; dónde vive cada campo; pendientes visuales (detalle 01 slide 4 recortado, Expected Impact +12%/20–30% intacto)*  
*type: project · last updated 2026-09-21*

Deck web **/m/british-airways** (deck.yuno.tools y decks.internal-tools.y.uno leen la misma fila de Supabase, sin deploy). Vertical `merchant`, orden ALL_SLIDES: 1 Cover, 2 Business Overview, 3 Infrastructure, 4 Diagnostic, 5 Solve, 6 Product Suite, 7 Dashboard, 8 Global Presence, 9 Leadership, 10 Trusted By, 11 CTA.

**Edición 21-sep-2026 (German dictó el texto exacto, "text only"):**
- Slide 2: `business_overview.description` última frase = operating profit 2025 £2.23B, 15.2% margin, +£182M vs 2024, £7B programme.
- Slide 4: títulos en columna `pain_titles`; detalles en `deckOverrides.diagnostic.painDescs`; capability stack reducido con `deckOverrides.diagnostic.capabilityKeys = [payouts, tokenization, fraud]` (fuera IAP, Subscriptions, KYC/KYB, BaaS, Tax). Ángulo: acquirer único Worldpay 20+ años, 50 incidentes status page 15-jul a 31-ago-2026, sin fallback.
- Slide 5: columnas `capability_titles` (04 = "Authentication", antes "Unified Orchestration") y `capability_descs` (Worldpay primary + segundo acquirer, Klarna UK, 3DS/SCA UK-India-Sudáfrica). Las descripciones solo se ven al voltear la tarjeta (print CSS oculta el reverso, verificar en la ruta interactiva).
- Slide 6: `deckOverrides.productSuite` → `pillar0.item2.desc`, `pillar3.item1.desc` (Reconciliation = pilar IA), `pillar2.item2.desc`.
- Slide 7: `deckOverrides.dashboard['bullet0.body']` (segundo acquirer bajo contrato propio, Worldpay se queda).
- Slide 11: `deckOverrides.cta` → `proof.indrive.*` = +14% Wingo, `proof.rappi.*` = +4.7% McDonald's 18 mercados, tercer stat default Weeks; `subtitle` = "One integration for every acquirer you add."; `ctaLine` = technical walkthrough.

**Pendientes / gotchas:**
- ⚠️ Slide 4, tarjeta 01: el detalle tiene 4 líneas y la tarjeta recorta la cuarta ("have no automatic fallback.") a 1920×1080. `diagnostic.contentZoom` solo escala la columna izquierda; NO existe knob por deck para la columna de pains. Arreglo = acortar el detalle o añadir un knob en SlideDiagnostic.jsx (código + deploy Railway y Neverland).
- Slide 5 fila Expected Impact sigue con +12% / 20–30% (no pedido; ver [[feedback_published_stats_only]]).
- Verificación en vivo: Playwright desde dentro del repo (`node scripts/x.mjs`, el scratchpad no resuelve el paquete), ruta `/m/<slug>/pdf` con `.pdf-page` nth(i); la ruta interactiva necesita `sessionStorage.deckOpenEmail` para saltar el gate de email.

Relacionado: [[project_deck_override_layer]], [[feedback_deck_edits_scoped]].

## business-case-tripadvisor-deck
*New standalone \"Business Case TripAdvisor\" report deck in yuno-sales-pitch-maker (slug business-case-tripadvisor), ported from an external PDF; deployed live*  
*type: project · last updated 2026-08-11*

Built and deployed a brand-new 27-slide "Business Case TripAdvisor" report deck inside the internal deck tools (yuno-sales-pitch-maker), reachable at `https://decks.internal-tools.y.uno/m/business-case-tripadvisor`. Content was ported verbatim from an external PDF business case ("TripAdvisor-sdr-business-case.pdf", `Business Cases/` folder) prepared by Magdalena Torrealba — NOT built with this codebase originally. It coexists with (and is fully separate from) the pre-existing standard `tripadvisor` merchant sales-pitch deck.

**Why:** The user (German) wanted the exact business-case content and layout (four chapters: Context, Why Yuno, Business Case region-by-region, Proposal, plus a detailed "Growing / Emerging Markets" 5-country-card closing slide) reproduced pixel-faithfully inside the same tool used for all other Yuno decks, not as a one-off static file.

**How it was built (reusable pattern):** This is a new "report-style" deck family — light canvas (`#F8F9FC` bg, navy ink, Yuno blue `#3E4FE0` accent, monospace `> breadcrumb` lines, bottom-right wayfinding label), distinct from the standard dark merchant SlideBase chrome. Implementation lives in `src/components/slides/tripadvisor-bc/` (shared shell `shared.jsx` + ~16 slide components, several reused 3x per region via a `REGIONS` data array in `src/data/tripadvisorBc.data.js`). Wired into `SlideViewer.jsx`/`PrintViewer.jsx` via a slug-scoped `BUSINESS_CASE_ORDER` array (same precedent as the `eventbrite`/`coinbase`/`lululemon-connections-ca-usa` custom storytelling decks), and registered in `App.jsx`'s `RESEARCHED` static-fallback map (no Supabase row) with `SLIDE_OVERRIDES.merchantName` driving the cover's company name. Added slug to `LIGHT_THEME_SLUGS` in both viewer files.

**How to apply:** If asked to build another one-off "Business Case" deck for a different merchant from an external PDF/doc, this is the exact pattern to follow — copy the `tripadvisor-bc` folder's shell conventions, extract content into a new data file, register a new slug the same way. Kingdom service name for this whole app is `decks` (not `yuno-sales-pitch-maker`) — deploys go through `yuno:deploy-quick decks`, single environment named `dev` (maps to the public internal-tools domain).

## project_cambly
*Cambly online English tutoring — Stripe+EBANX, local APMs only in Brazil; BC focused on missing APMs per market*  
*type: project · last updated 2026-07-24*

Cambly (cambly.com) — on-demand 1-on-1 English tutoring over live video (+ Cambly Kids). US/Delaware, San Francisco, YC W14. Founders Sameer Shariff (CEO), Kevin Law (CTO), both ex-Google. Profitable. $60M raised (Series B 2022, Benchmark + Bessemer; NOT SoftBank), ~$250M valuation. Revenue ~$250M est (getlatka). ~40,000 tutors. Heavy demand in Brazil, Turkey, Japan, Korea, Saudi, Mexico.

**Payments:** Stripe (global cards + web recurring) + **EBANX (Brazil ONLY: Pix, Boleto, 3/6/12x installments)** + Apple/Google IAP for app subs. No orchestrator. "Cambly installments" = 12-mo plan over 4 payments, 2% fee. Account required, no guest checkout.

**APM gap (the wedge — user wanted this as the focus):** rich local coverage exists ONLY in Brazil. Japan = card ONLY (missing Konbini/PayPay/Rakuten). Turkey installments broken (taksit charged as tek çekim, şikâyetvar complaints). Mexico/Korea/Indonesia/China/South Africa presumed card-only (LOW confidence, verify live checkout). Saudi has Mada. India UPI only via app IAP, not web. They already proved local-method value with EBANX in Brazil but did it once → Yuno replicates that playbook everywhere via one integration.

Complaints: auto-renewal surprise charges, refund refusal (no partial refund of cycle), declined-card friction. Trustpilot 2.1/5.

BC built 2026-07-24: `Business Cases/BC sheets - Cambly.xlsx` (standard template, 13 sheets). 31.5M annual visits. Regions: NA (US,CA), LatAm (BR,MX), EMEA (TR,UK,ZA,SA), APAC (JP,KR,ID,CN,IN; India swapped in for Taiwan/Thailand for UPI story). Modeled TPV $160M. **New APM TPV Growth $5.39M = headline lever**; Acceptance 3.44 + Fee Reneg 1.45 + Eng 4.39 = total $14.66M. e-learning benchmarks. See [[project_ai_apps_batch_2026_06_17]], [[project_praktika_psp]].

## cellpoint-whitelabel-deal
*CellPoint Digital (no \"Sellpoint\") — pivot 1-sep de full white-label ($50k) a propuesta liviana de APM connectivity ($15k/mes + rev-share 50/50 O integration fee $500)*  
*type: project · last updated 2026-10-05*

**CellPoint Digital** (cellpointdigital.com, correos @cellpointmobile.com) — orquestador de pagos enfocado en aerolíneas/travel ("Leading Payment Orchestration"). Su modelo de orquestador no funcionó; pivotan a consultoría y quieren la plataforma de Yuno como **white label** para su base.

Contactos CellPoint: **Andrew Goddard** (Chief Strategy & Product Officer, andrew.goddard@) y **Patrick Uckermark** (patrick.uckermark@). Lado Yuno: Justo Benetti (CRO, dueño de la relación), Bernabé Murata en cc, German prepara la propuesta.

Cronología: intro call 26-jun-2026 (Justo + Bernabé). Andrew pidió NDA + demo + términos el 6-jul y follow up 27-jul. El 27-jul-2026 German envió el NDA mutuo (Andrew como firmante) y prometió la propuesta. Justo vuelve de OOO el 1-ago-2026 para agendar call.

Estructura comercial ✅ **VERIFICADA contra el PDF enviado el 11-ago** (`Reference Presentations/Proposal - CellPoint Digital + Yuno (1).pdf`, slide "Proposal"):
- Platform fee: **USD 50.000/mes** (white label de la plataforma, marca CellPoint, 1.500+ integraciones, one API, equipo dedicado + sandbox).
- **USD 0.07 por transacción exitosa** (tarifa inicial, todo el portafolio; incluye network tokens, smart routing, vault, 3DS y fraud orchestration). ⚠️ NO es $0.10 como decía esta memoria antes.
- Por cada deal que CellPoint cierre: **revenue share 50/50 sobre net platform revenue**. CellPoint es dueño del cliente y fija el precio final.
- Término de contrato: 1 año.
- CellPoint aporta consultoría/relaciones; Yuno la plataforma. El deal incluye "todo lo que tengan ahora mismo" (portafolio existente).

Deck propuesta (basado en el BC de Flair, rearmado vía Claude Design): quitar "Our understanding of the context", quitar Total Impact y Build vs. Buy; queda Cover + Agenda + Why Yuno + sección renombrada **"Proposal"** (1 slide de pricing con 3 tarjetas: platform fee / success fee / rev share 50-50 en azul) + closing. Todo en inglés, sin datos inventados de CellPoint.

Hilo Gmail: "Re: Follow up" (thread 19fa4980fec52ae5).

**Update 2026-08-20:** el deal está más avanzado de lo que este memo sugería. NDA **completamente firmado por ambas partes** (German lo envió firmado el 03-ago). Call principal de descubrimiento/demo el **11-ago** (Andrew, Patrick, Justo, Bernabé, Jarrett, German), muy bien recibida, cero objeciones ("this is beyond an expectation" - Andrew). Jarrett está en el deal porque trabajó 4 meses en CellPoint antes de Yuno. **Mauricio Madrigal es de YUNO** (lidera el producto white label de Yuno), NO de CellPoint. Patrick Uckermark confirmado como **CTO** (firma de correo). En la call, Justo no leyó cifras exactas de pricing en voz alta, solo dijo que es "probably 30% or maybe less" que el pricing white label estándar de Yuno.

**Update 2026-08-31 (estado real antes de la call del 1-sep):**
- **Cero feedback escrito sobre la propuesta en 20 días.** German lo pidió explícitamente el 11-ago. Toda la correspondencia posterior es solo logística de calendario. Este es el riesgo real del deal, no las fechas.
- Papermark: Andrew y Patrick abrieron la propuesta el 12-ago; **Andrew la volvió a abrir el 31-ago desde Surbiton (Londres)**, la mañana antes de la call.
- **Workshop Dallas del 4-sep muerto.** Andrew lo declinó el 27-ago tras avisar el 24-ago que no puede viajar ("urgent personal commitment"). Ping-pong de fechas: Andrew ofreció 9-11 sep (Yuno no), Yuno ofreció semana 14-18 sep (sin respuesta), Andrew preguntó 7 u 8 sep (Yuno no, evento de compañía), Yuno reofreció semana del 14 "any day". Andrew 26-ago: "juggling dates and will revert". Silencio desde entonces.
- **Palanca no usada aún: proponer Londres en vez de Dallas.** Andrew vive en Londres y Patrick viaja allí seguido (estuvo 10-12 ago). Andrew ha evitado viajar dos veces.
- ⚠️ **El título de Andrew cambió 3 veces en 5 semanas**: "Chief Product & Partnerships Officer" (29-jul, 4-ago) → "Chief Partnerships & Marketing Officer" (24-ago); la call del 11-ago lo listó como "Chief Strategy & Product Officer". Se aleja de Product. Inferencia, nunca decirlo en voz alta, pero justifica preguntar quién más de producto/ingeniería debe estar en el workshop.
- Call de alineación **1-sep 9:30-10:00 COT**, 30 min, Andrew y Patrick aceptaron. Brief: `data/research/cellpoint-digital-meeting-brief-2026-09-01.md`.

**Research externo 2026-08-31 (contexto de leverage, no mencionar en llamada):**
- Accionista mayoritario: **Tosca Penta CPM Limited** (Toscafund/Penta Capital, Jersey), 50-75% desde jun-2023. El "parachuted in at the beginning of the year" es **Kevin Murphy**, nuevo Group CEO (director desde dic-2025), operador de turnarounds de PE en lending (Colthurst, Avant Money, Bank of Ireland), sin background en travel. El fundador Kristian Gjerding (CEO desde 2007) ya no aparece en el team page, sin salida anunciada.
- Señales de tensión financiera: ronda de capital jul-2025 (GBP 67,9M) nunca anunciada en prensa; CellPoint ya no aparece en el portfolio de Penta Capital; último cierre de cliente público fue oct-2025 (nada en todo 2026); dos directores aviation-heavy (ex-Amadeus, ex-Southwest) entraron y salieron en <5 meses; FY2022 (última cifra pública) mostró pérdida neta de $22M sobre $2,6M de ingresos.
- Competencia: Sabre firmó con **Juspay** (nov-2025); Gr4vy cerró exclusividad con **Datalex** (ago-2025); Amadeus/Outpayce es la amenaza nativa mejor financiada.
- Lectura: el leverage probablemente está del lado de Yuno. No ablandar la estructura comercial preventivamente.

**Call "Workshop Alignment" 1-sep-2026 (21 min, Andrew + Patrick vs. Justo + Jarrett + Bernabé + German) — PIVOT MAYOR DEL DEAL:**

Andrew abrió la call diciendo que la propuesta full white-label ($50k/mes) "cuts to the heart of what we do" y los hizo frenar en seco. Su freno no es cultural ni de producto, es de **valuación de accionistas**: CellPoint tiene 12+ años de inversión de capital metidos en construir su plataforma de orquestación propia ("Velocity", corre desde su dev center en India). Reemplazar ese motor por Yuno como white label mata el "asset value" que están construyendo hacia una historia de valuación futura con sus shareholders (Tosca Penta/Toscafund). Cita textual: *"there is asset value on the balance sheet... if you then move all of... effectively replace the engine with a third party powering your capability, then that becomes quite a really complicated piece in terms of future value."* Andrew y Patrick (con el CEO Kevin Murphy) necesitan tiempo para digerir esto internamente antes de decidir sobre el white-label completo; NO lo mataron, solo lo pausaron ("that's not killing that by any means").

**Lo que sí pidió Andrew como paso intermedio:** un "aggregator solution" o "interim version", solo las conexiones a APMs, sin tocar su core de orquestación. Justo confirmó que Yuno puede dar esto como componentes standalone: **conexiones a APMs, 3DS orchestration, account updater, standalone poll** (no el stack completo). Esto es lo que hay que cotizar en la nueva propuesta.

**Contexto adicional de la call:**
- Justo dio el pitch de "clean slate": darles la plataforma completa bajo su marca en vez de ir conectando piezas sueltas; mencionó que Yuno ya corre white label con socios que mueven $70-100B en TPV.
- Andrew mencionó dLocal como comparación ("no-code integration" que vio en un artículo); Justo lo desestimó como marketing, no real ("no es no-code, alguien tiene que programar cada APM").
- **Jarrett confirmó que Yuno está construyendo funcionalidad de reseller en el white label**: CellPoint mantiene el control comercial/revenue-share de cada APM sin que el merchant vea que Yuno está debajo, más reconciliación/billing/settlements completos para el rol de "primary provider" de APMs.
- Eventos para sincronizar agenda: **TTRL Londres semana del 21-sep** (Yuno es lead sponsor) y **WAF Lisboa 13-15 oct**; Andrew invitó a Yuno a TTRL, sobre Lisboa quedó en veremos.
- German preguntó cuántos APMs quieren integrar; Andrew no tenía el número (pendiente, un ejercicio de prospección interno que termina "el viernes", sin fecha exacta dada).

**Nueva propuesta en construcción (2026-09-01), reemplaza la de $50k, PENDIENTE de enviar:**
- **Platform fee: $15,000/mes** (baja de $50k). Cubre: equipo de estrategia dedicado (CAM/TAM) acompañando, acceso a 1,200+ payment connections, y el mantenimiento/costo de mantener esas conexiones live. ⚠️ El número "1,200+" no coincide con las cifras de "1,500+ integraciones" / "1,000+ payment methods" que usa el resto del deck (páginas Why Yuno) — no reconciliar automáticamente sin confirmar con German cuál es la cifra correcta para conexiones/APMs específicamente.
- Se van a presentar **dos opciones side-by-side** para comparar en la misma propuesta (decisión explícita de German, 1-sep):
  - **Opción 1 — Revenue share:** Platform fee ($15k/mes) + revenue share 50/50 sobre todas las transacciones que pasen por los APMs que Yuno provee. Sin fee por transacción, sin integration fee.
  - **Opción 2 — Integration fee:** Platform fee ($15k/mes) + integration fee de $500 por cada integración/APM nueva. Sin revenue share, sin fee por transacción.
- El $0.07/transacción exitosa del modelo anterior **se elimina** en ambas opciones nuevas (confirmado explícitamente por German).
- Sigue pendiente el término de contrato (el "3-year contract term" del PDF viejo era para el white-label completo; no asumir que aplica igual a este modelo más liviano).
- Prompt de Claude Design para este rediseño: `Deals/CellPoint Digital/claude-design-prompt-two-pricing-options-2026-09-01.md`.

**Update 2026-09-25:** existe un grupo de WhatsApp con CellPoint (German menciona a un "Ashwyn" en el grupo, contacto no verificado en correo ni calendario; los conocidos siguen siendo Andrew Goddard y Patrick Uckermark). CellPoint dijo que la semana del 21-sep estarían revisando la propuesta liviana (APM-only, $15k/mes + rev-share 50/50 o $500/integración) y alineando internamente. German propuso por WhatsApp call el mié 30-sep o jue 1-oct a las 3:30 pm UK (10:30 am ET, 7:30 am PT), mismo slot de la call del 1-sep. Horarios de las calls anteriores: 11-ago 11:45 COT (5:45 pm UK) y 1-sep 9:30 COT (3:30 pm UK), ambas de 30 min. Andrew está en Londres; German en SF (PT) desde el 28-sep.

**Update 2026-09-29:** CellPoint NO respondió al mensaje de WhatsApp del 25-sep (call 30-sep / 1-oct). Tampoco hay correo de ellos desde el 8-sep (Andrew: "Patrick and I have not had time to meet... will revert"). Señal Papermark del **24-sep**: Andrew reabrió las DOS propuestas (white label completa y "Proposal APMs") y una persona nueva, **michael.kelly@cellpointmobile.com** (rol sin verificar), abrió ambas varias veces ese mismo día. La propuesta está circulando internamente. ⚠️ No mencionar el tracking de Papermark al cliente. German pidió el 29-sep un nudge corto por WhatsApp para reunirse esta semana; se propuso jue 1-oct o vie 2-oct a las 3:30 pm UK (7:30 am PT, calendario de German libre en ambos) e invitar a quien más del equipo quiera sumarse.

**Noticia verificada (press release CellPoint 21-sep-2026 + cfotech.news 23-sep-2026):** CellPoint levantó **USD 34M** de Toscafund (gestionado por Penta Capital) y lanzó **Zenith**, "AI decisioning platform for airline and hospitality payments", descrita como "a decisioning layer that sits above a payment orchestrator" que se despliega sin reemplazar la infraestructura de pagos existente. Nombramientos: **Kevin Murphy** Group CEO, **Michael Kelly = Chairman** (es quien abrió ambas propuestas en Papermark el 24-sep), **Patrick Uckermark** Chief Product and Technology Officer. 50 contrataciones nuevas (producto, data, AI, ventas, partnerships). Andrew Goddard no aparece en la nota. Lectura (inferencia, no hecho): el valor de activo ahora se cuenta sobre Zenith, no sobre el orquestador, así que Yuno como capa de orquestación/conectividad debajo de Zenith es complementario y la objeción de valuación del 1-sep pierde peso. Nudge WhatsApp 29-sep reescrito con este ángulo (felicitar por funding + Zenith, catch up de qué cambió internamente). En el grupo felicitar a nivel compañía, no a Patrick por el cargo, porque Product salió del título de Andrew.

**Update 2026-10-05 (brief para la call del 7-oct):**
- **Call "Catch up CP & Yuno": mié 7-oct-2026, 11:45 a 12:45 PT** (Google Doc del brief: https://docs.google.com/document/d/1cbSJWY5PtbvN8KnfjX10q31C4ZTFuYggEKs-rup_Lv0/edit) (13:45 Bogotá, 19:45 Londres), 60 min, organizada por Andrew (invite 29-sep). ⚠️ El invite NO tiene link de video. Aceptaron Andrew y Justo; Patrick, Jarrett y Bernabé sin responder (Patrick estuvo de licencia la semana del 28-sep). German figura como "optional". Agenda según Andrew: "feedback on APM proposal and our Zenith development". Brief: `data/research/cellpoint-digital-meeting-brief-2026-10-07.md`.
- ⚠️ **CORRECCIÓN sobre la Propuesta 2 (APM):** el deck en Drive "Proposal 2 - CellPoint Digital + Yuno" (editado por última vez 3-sep) NO tiene dos opciones. Estructura única: **$15,000/mes platform fee + $0.02 por transacción solo en conexiones APM de Yuno + 4 integraciones APM nuevas por trimestre incluidas + $500 por cada APM adicional (una vez, al salir a producción), SIN revenue share, término de 3 años.** Incluye 1,200+ conexiones, 190+ países, KAM+TAM dedicados, mantenimiento. Las "dos opciones" (rev share 50/50 vs $500/integración) fueron el plan de diseño del 1-sep, no lo que quedó en el deck. Pendiente verificar qué versión tiene el PDF de Papermark ("Proposal APMs", enviado 1-sep 23:16 UTC, abierto por Patrick a las 23:23 UTC, antes de la edición del 3-sep).
- **Chat de WhatsApp "Yuno-Cellpoint"** (export en `Deals/CellPoint Digital/WhatsApp Chat - Yuno-Cellpoint.zip`): creado el 9-jun-2026 por "Preston Clark" (no identificado); Justo agregó a German el 31-ago. Miembros vistos: Preston Clark, Justo, German, Andrew, "Kevin" (⚠️ casi seguro Kevin Murphy, Group CEO; respondió el 29-sep). NO hay ningún "Ashwyn" en el chat; descartar esa nota anterior.
- **Dos pistas abiertas de Justo (WhatsApp):** 15-sep "updated idea on how to make it work for both companies"; 16-sep "one opp where I think your approach can help". Nada en email/Slack/Gong lo documenta. Andrew (21-sep): compartirá "what optimisation framework looks like" para "supporting your orchestration discussions", "different to the APM proposal". Lectura (inferencia): CellPoint quiere ofrecer Zenith/optimización sobre merchants de Yuno = partnership de dos vías.
- **Títulos verificados en la team page (5-oct):** Kevin Murphy Group CEO & Board Director; Andrew Goddard **Chief Partnerships and Marketing Officer**; Shaun Donaghey CCO; Patrick Uckermark Chief Product & Technology Officer; Mike Mayfield Transformation Director (nuevo); Ian Kelly CFO (nuevo, reemplaza a Shawn Rea). Kristian Gjerding ya no aparece.
- Papermark: sin vistas desde el 24-sep. Salesforce muestra el deal en $7,000 (Pipeline Brief 5-oct); corregir a $15K/mes.
- WAF Lisboa 13 a 15-oct: CellPoint Gold Sponsor; Patrick en panel el 13-oct 12:20 ("Agentic AI and automation in travel payments"). Sin evento de Yuno en calendario para Lisboa.

## project_chai_ai_psp
*Chai AI (Chai Research) payment stack + Yuno angle (research 2026-06-17)*  
*type: project · last updated 2026-06-17*

Chai AI / Chai Research Corp. (Delaware, Palo Alto; founded Cambridge UK, relocated 2022). AI-companion app, 10M+ users, ~1M DAU, $80M ARR Q1 2026, ~$2.4B reported valuation, lean ~15-20 person team. Founders William Beauchamp + Thomas Rialan. Backed by CoreWeave + AMD.

Payment stack: mostly Apple/Google IAP; ALSO has direct web checkout at chai-ai.com with distinct web-only pricing ($159.99/yr web vs $134.99/yr iOS) = deliberately steering off-store. Web PSP NOT publicly disclosed (descriptor "Chai AI Service Fee"); no orchestrator. 2026 removing free tier region-by-region. Global users US/Vietnam/Germany/Poland/India. Heavy complaints: double charges, charged-after-cancel, refund friction.

Yuno angles: single-rail web billing to confirm; global users likely card-only (UPI/BLIK/MoMo gap); involuntary-charge complaints; lean team offload payments roadmap; free-tier removal raises conversion stakes. Scored 🟡 Med(9) — thesis High but verify live web PSP/APMs. Best cases: Rappi, InDrive, Livelo. Part of [[project_ai_apps_batch_2026_06_17]].

## project-chess-com
*Chess.com / Sean Walkinshaw (Sr PM Payments & Pricing, Texas): infra work late Q1 2027, vault first (Basis Theory), shortlist Yuno/Checkout.com/Stripe/Global Payments; touch base Dec-2026; one-pager Yuno vs Basis Theory sent 8-sep*  
*type: project · last updated 2026-09-18*

Sean Walkinshaw (sean.walkinshaw@chess.com, +1 817, Central time) is the only contact. Thread "Let's Reconnect | Chess.com & Yuno" (May to Sep 2026), cc Justo and Alejandro. His position, twice in writing (27-may and 2-sep-2026): no payments infra work prioritized; late Q1 2027 to start, **vault payment and network tokens first (Basis Theory), then enable another PSP**; shortlist in no particular order: **Yuno, Checkout.com, Stripe, Global Payments**; "touch base in December 2026". Warm but slow: replies same day, never commits to a call.

Sent: personalized web deck (deck.yuno.tools/m/chess-com, 21-may); one-pager "Yuno vs Basis Theory" PDF (8-sep, Deals/Chess.com/) with the angle "two projects become one: vault + network tokens + Stripe/Global Payments/Checkout.com already integrated behind Yuno". Sean: "This is great. Let me digest in detail." Justo followed 9-sep proposing a call: no answer.

**18-sep-2026:** draft reply in the thread (msg 1a0b4e81a7041b09, reply to Justo's message, to Sean, cc Justo and Alejandro) proposing a 30-min call the week of 21-sep (Wed afternoon or Thu; German is in Montreal Tue 22 with FlightHub) to show token vault + network tokens, orchestration, direct connections to Checkout.com/Stripe/Global Payments, and the line "the last connection your team builds is the one to Yuno". ENVIADO 18-sep-2026 14:27 UTC ("Hope the one pager was useful... I'd like to show..."). Sin respuesta aún.

**How to apply:** never push past his stated timeline; every touch must add a new angle (vault portability, network token import, one-integration framing). Global Payments verified as Yuno partner (y.uno/partner/global-payments). Don't name-drop clients. See [[reference-yuno-positioning]].

## project-cobrana
*Cobrana (Perú, cobros por WhatsApp sobre Kashio, 2 fundadores) — intro vía Isabella Ponce; calls 21 y 24-ago-2026 con Gabriel Shimabuko; sin seguimiento desde entonces; brief en data/research/cobrana-meeting-brief-2026-08-21.md*  
*type: project · last updated 2026-09-24*

Cobrana (cobrana.pe): startup peruana de 2 personas (Gabriel Shimabuko, ex Product Owner de Interbank, y Miguel, CTO) que cobra por WhatsApp con 1% de comisión; es una capa de UX sobre Kashio (proveedor, competidor y punto único de falla). Tracción jun-2026: S/250K transados, 15+ clientes B2B (~USD 67K/mes). Contacto: gabriel.shimabuko@cobrana.pe. Intro por Isabella Ponce (isabella.ponce@y.uno). Calls el 21-ago (30 min) y 24-ago-2026 (Fireflies recap + transcript en Drive). Brief: data/research/cobrana-meeting-brief-2026-08-21.md. ⚠️ Cobertura Perú (Yape, Plin, PagoEfectivo, Culqi, Niubiz) sin confirmar en docs públicos de Yuno.

**Estado 24-sep-2026:** ningún correo ni reunión desde el 24-ago. No está en el Deal Status GTM; fila opcional (Status "Discovery") en Lists & ICP/Pipeline Sync/manual_adds/ (flag --with-stale). Por tamaño, probablemente no es deal de German: decidir si se cierra o se pasa a partnerships.

## project-cruz-verde
*Cruz Verde Colombia (droguerías, Femsa) — Andrés Guzmán (Ecommerce), Michael Vargas (coordina), Sandra P. Vargas, Adriana Buitrago (lleva el NDA); Mercado Pago único, ~60% PSE, 100K tx/mes; propuesta v1 24-sep $13,750/mes; NDA: los 5 documentos de Yuno ENTREGADOS (formulario firmado por JPO vía DocuSign y enviado por JP Pantoja 5-oct en hilo aparte); Michael pidió a Adriana crear el NDA 5-oct; esperando borrador de NDA de CV; info del BC (xlsx 29-sep) sin respuesta; propuesta v2 (tiers, pesos, BC sin L4/L5) SIGUE PENDIENTE de Yuno; correo de pendientes en BORRADOR 6-oct*  
*type: project · last updated 2026-10-06*

Cruz Verde Colombia (cadena de droguerías). Contacto: Andrés Guzmán Forero, Ecommerce Manager (andres.guzmanforero@cruzverde.com.co). Lado Yuno: Susana Awad (SDR, lleva los next steps), Alejandro Bernal, Saman Mortazavi, Carlos Medina (SE); German hizo el primer contacto en mayo. Dos cuentas duplicadas en el CRM de Gong ("Cruz Verde Colombia", ids 001Ps00001rjBY9IAM y 001Hu00003QI2cmIAD).

**Perfil (call 21-may-2026, Gong 8940587603862854221):** Mercado Pago único, incluidos links de pago para puntos de venta; PSE = 58% de las ventas; >100K tx/mes (80K Mercado Pago + 20K efectivo); ticket COP 130,000 a la baja, 40% de las tx bajo COP 30,000 (German el 24-sep: ~USD 20). Dolores: dependencia de un proveedor, caídas de PSE, rechazos altos con fraude bajo, devoluciones PSE. Pidieron métodos nuevos, smart routing, pricing y demo técnica. Objeción: costo por tx en USD con ticket cayendo.

**Cronología:** intro 21-may (German invitado, tentative); "Next Steps" 31-ago; demo 1-sep; revisión de dashboard 22-sep; correo "Siguientes pasos | NDA y Business Case" 23-sep (hilos de Susana, no están en el Gmail de German).

**Pricing recomendado 24-sep-2026 (Deals/Cruz Verde/cruz-verde-pricing-2026-09-24.md):** platform $7,000 + pay-ins por tramos $0.06 (0 a 25K) / $0.05 (25 a 50K) / $0.04 (>50K) = $11,750/mes a 100K (59 bps, $0.1175/tx), todo green contra la celda V3 × M2 del calculator (referencia Palco). Piso: $6,500 + $0.045/$0.04/$0.035 ($10,375). Respuesta a la objeción: tramos, factura en COP a tasa oficial, alternativa 0.25% del TPV solo si bloquea, crédito 50% de platform fee 3 meses. Risk conditions bundled $0; 3DS solo por intento si usan tarjeta; reconciliation después.

**How to apply:** no está en el Deal Status GTM (fila lista en Lists & ICP/Pipeline Sync/manual_adds/). Salesforce antes de cotizar. Ver [[yuno-pricing-policy]], [[project-palco-ticketing]] (misma celda del calculator), [[project-unicef-colombia]] y [[project-linea-directa]] (ola de cuentas colombianas de recaudo con PSE/Nequi).

**Propuesta v1 (24-sep-2026, Google Slides):** https://docs.google.com/presentation/d/1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk/edit (carpeta Drive "Cruz Verde"). Copia literal del deck de Palco (21 slides) aterrizada a Cruz Verde; notas y supuestos en Deals/Cruz Verde/cruz-verde-proposal-2026-09-24.md, scripts en Deals/Cruz Verde/build/. **Pricing dictado por German:** platform $7,500 + tramos $0.06 (0 a 25K) / $0.04 (25 a 50K) / $0.035 (>50K) + conciliación $2,000 flat = $13,750/mes ($165K/año) a 100K tx; todo verde contra el calculator de Alejandro ("Yuno — Pricing Calculator V2 - Cruz Verde", Sheet 1F5pFJxj0p9WNQQXlhHO0iyyrhWaHmV1kFmJssk7NyY4: Retail, 97K tx, AOV $20, V2×M2). Cortes 25K/50K los puse yo. Reglas de German para este deck: NADA de network tokens, IA ni suscripciones; el token vault NO va dentro de lo incluido (quitado del slide 16 el 24-sep; sigue como capacidad en S6/S7). Quedaron como en Palco y sin confirmar: "Contrato a 3 años" y la franja opcional 3DS $0.04 / antifraude $0.018. **BC v2 (24-sep tarde, 5 palancas por pedido de German):** base 100K × $20 = $24M/año; L1 aprobación 91% → 92.5/94% ($0.40M/$0.79M); L2 nuevos métodos que ELLOS quieren (Apple Pay, Google Pay, Addi, Bre-B, Nequi, Daviplata) = +2% a +5% de volumen ($0.48M/$1.20M, base: billeteras 5% + BNPL 4% del ecommerce CO según dLocal/AMI, Bre-B 34.9M usuarios); L3 10 a 20 bps ($24K/$48K); L4 costo de integrar los 6 métodos en casa ($55K/$90K: 8 a 12 sem. de ingeniería c/u, 2 a 3 personas 4 a 8 meses, 20 a 30% mantenimiento, $50K/FTE); L5 operación 1 a 2 FTE ($50K/$100K); total $1.00M/$2.23M, promedio $1.62M. Todo declarado como supuestos. ⚠️ Bre-B en Yuno NO verificado (deck dice 'vía proveedores conectados, a confirmar'); Apple Pay, Google Pay, Nequi, Daviplata y Addi sí. La v1 con 'continuidad de PSE' quedó descartada. Datos Gong 21-may: aprobación 91% sin reintentos, fraude <0.05%. ⚠️ Ticket: cliente dijo COP 130,000; deck usa $20 (German/calculator); confirmar. **Sesión con Gerencia y TI: viernes 25-sep-2026 11:00** (Michael Sneydder Vargas Parra pidió enfoque comercial y de valor de negocio; Alejandro Albarracín confirmó; también en cc Santiago Castaño y Adriana Buitrago). Michael pidió el 23-sep el formulario de proveedor (Excel firmado por rep. legal + PDF) y 4 documentos (existencia legal, beneficiarios finales <60 días, certificado bancario, ID del rep. legal) para el NDA. Vía Slides que funciona: el conector de Drive SÍ pudo compartir la copia con el service account (24-sep).


**Reunión presencial Gerencia y TI 25-sep-2026 (HECHA; notas en Deals/Cruz Verde/cruz-verde-meeting-notes-2026-09-25.md):** asistentes CV Andrés, Sandra P. Vargas, Michael Vargas, Edisson Olarte, Francy Silva, Santiago Castaño (cc Guillermo Gutiérrez). Dijeron: mix ~60% PSE / 40% tarjetas; devoluciones ~5% (PSE); aprobación tarjetas ~90% (⚠️ vs 83% de Tati), rechazos = hard declines bancarios, PSE casi 100%; fraude y contracargos muy bajos, antifraude NO es prioridad; proveedores conversados PayU, Redeban, Movii, Kushki; quieren negociar en pesos. Interés: recon primero, Sistecrédito, gift cards/créditos CV para devoluciones (Mercado Pago tiene algo similar), checkout por tipo de entrega (same-day vs next-day), subs a futuro. BC: Sandra pidió QUITAR L4 y L5; supuestos aceptados; aseguran que sí llegan a 100K tx → cambiar tramos a TIERS. Next steps: CV revisa propuesta internamente; reunión técnica con TI la próxima semana (esfuerzos); revisión con Finanzas; proceso de RFP y luego oferta comercial o contrato; hablar con Michael la próxima semana con cifras reales. Yuno debe: documento de información requerida + propuesta v2 con tiers y BC sin L4/L5. **Follow-up ENVIADO 25-sep** (asunto "Cruz Verde + Yuno", a los 6 invitados, cc Guillermo, Alejandro, Susana, Carlos Medina).

**NDA (27-sep-2026):** Alejandro Albarracín puso a German en cc del hilo "Siguientes pasos | NDA y Business Case – Yuno" para que lleve la firma del NDA en paralelo. El formulario de proveedor (Excel FC-FI-FO-01) viene adjunto en ese hilo. Pedido a Legal en BORRADOR de Slack en #salesops-legal (tag a Ivvy Soberay) con el formulario + los 4 documentos; German lo envía y le reenvía el correo con el Excel. Ver [[reference-salesops-legal]].

**NDA, estado 28-sep-2026 (hilo Slack "Cruz Verde - NDA", ts 1790553688.958639):** pedido ENVIADO a Legal el 27-sep; Ivvy lo pasó a **María Gabriela Tovar**, que prepara los documentos (German le reenvió el correo con el Excel el 28-sep). Tres puntos de María: (1) el certificado de accionistas/UBO es documento con reserva, lo comparte directamente **Juan Pablo Pantoja (Compliance Manager de Yuno)** idealmente con Compliance de la contraparte → falta que Cruz Verde dé el contacto; (2) certificado bancario: Laura Galan debe confirmar cuenta de la sociedad colombiana, moneda **COP** (respuesta de German); (3) firma del formulario: solo firman JN y JPO por la sociedad colombiana y se demoran; German dijo que NO es urgente y se espera esa firma (no se pide a CV aceptar la del Compliance Manager). **Correo a Michael pidiendo el contacto de Compliance: BORRADOR Gmail r8607530486062465658** (reply a 1a0e54a6ccaac293 en el hilo "Siguientes pasos | NDA y Business Case", cc Santiago, Adriana, Alejandro, Susana, Carlos), copia en `Deals/Cruz Verde/cruz-verde-nda-email-contacto-compliance-2026-09-28.md`. German trata a Michael de "Mike".

**Solicitud de información para el BC (29-sep-2026):** Cruz Verde pidió que Yuno les solicite TODOS los datos para un business case a la medida (German: hasta el % de rechazos hard vs soft). Entregable: `Deals/Cruz Verde/Solicitud de información - Cruz Verde + Yuno.xlsx` (se regenera con `build/build_data_request.py`): 14 hojas, 90 solicitudes (41 A / 37 B / 12 C), dos caminos (Opción A = export transaccional de Mercado Pago con 24 campos; Opción B = tablas resumen), período sep-2025 a ago-2026, COP; cada solicitud trae el dato que ya nos dieron para confirmar. Códigos de rechazo = `status_detail` de Mercado Pago (verificados en su documentación). Respeta a Sandra: sin L4/L5 (la única pregunta de horas es opcional y fuera de ahorros). **Versión que se envía = Google Sheet SENCILLO de una sola hoja** (German rechazó la versión de 13 hojas: "mucho más sencillo y en un solo tab"): https://docs.google.com/spreadsheets/d/1xipYBM6dNEVmCj_cxezIAqsfMb-gbPCimMJmXaGIMJQ/edit, carpeta Drive "Cruz Verde"; hoja "Información" con 3 columnas (Campo, Respuesta, Comentarios) y 36 campos en 9 secciones, incluye % de rechazos hard, soft, fraude y datos mal digitados; se genera con `build/build_data_request_simple.py`. ⚠️ NO correr `build_data_request_gsheet.py --rebuild` (devuelve el Sheet a 13 hojas). Vía usada: conector de Drive crea el Sheet vacío + lo comparte con la service account, luego Sheets API. El Excel detallado queda como respaldo. **Correo en BORRADOR Gmail r5317102337443385744** (reply en el hilo "Cruz Verde + Yuno", a los 6 + cc Guillermo, Alejandro, Susana, Carlos); German agrega el link y comparte el Sheet con Cruz Verde desde la interfaz. Notas en `Deals/Cruz Verde/cruz-verde-data-request-2026-09-29.md`. Contacto de Compliance de CV para el certificado UBO ya resuelto el 28-sep: Adriana Buitrago dio mariateresa.silva@cruzverde.com.co. Pendiente: propuesta v2 (tiers, pesos, BC sin L4/L5); sin reuniones de CV agendadas en calendario al 29-sep.

**Correo de la solicitud de información, versión vigente (29-sep-2026, tarde):** German decidió ADJUNTAR el documento en vez de compartir el link. Borrador Gmail vigente **r8537645621480480793** (reply en el hilo "Cruz Verde + Yuno", mismos destinatarios): dice "les adjunto" y agrega una línea pidiendo día para la reunión técnica con TI. Archivo listo para adjuntar: `Deals/Cruz Verde/Información para el business case - Cruz Verde + Yuno.xlsx`, export del Google Sheet EN VIVO (German editó el Sheet a mano: agregó "hard declines", "Do not honor", "Con Mercado Pago (desglozado por volumen)"; ⚠️ typo "desglozado" sin corregir). Si se regenera el Sheet con el script se pierden esas ediciones; para actualizar el adjunto, exportar el Sheet (service account + export?format=xlsx). 

**NDA, estado 30-sep-2026 (mismo hilo Slack):** Legal ya subió 3 de los 5 entregables: certificado de existencia (⚠️ expedido 11-jun-2026, código de verificación CCB vencido a los 60 días; pedir uno nuevo), cédula del rep. legal Juan Pablo Ortega Merino, y certificado bancario J.P. Morgan Colombia cuenta corriente COP del 29-sep (⚠️ sin SWIFT ni direcciones, que Mike pidió). Pendientes: formulario FC-FI-FO-01 (María Gabriela Tovar lo diligencia; Finanzas debe dar referencia bancaria, información tributaria y contacto de facturación: Laura Galan, Chevy Díaz, Tatiana Lizarralde, William Peña; luego firma JN o JPO) y certificado UBO (lo envía Juan Pablo Pantoja directo a mariateresa.silva@; German lo sumó al hilo de correo el 30-sep). **FUP de avance en BORRADOR Gmail r4219961008964291876** (versión 1-oct, reply a 1a0f30c6798367da, a Mike y Adriana, cc Santiago, Alejandro, Susana, Carlos, JP Pantoja; ofrece certificado de existencia más reciente si lo piden; el borrador del 30-sep fue borrado); German adjunta los 3 PDFs desde Slack. 1-oct: William Peña ya dio la información tributaria del formulario; María Gabriela sin responder sobre el certificado nuevo y declinó la llamada de alineación del 1-oct. Copia en `Deals/Cruz Verde/cruz-verde-nda-followup-documentos-2026-09-30.md`. Ojo: Mike dijo que el NDA es requisito para compartir la información del BC, así que el NDA sí frena la solicitud del 29-sep.

**Solicitud de información ENVIADA 29-sep-2026 (18:19 UTC):** German envió el correo (mensaje 1a0ee644fdb8c422, hilo "Cruz Verde + Yuno") con el xlsx adjunto ("Cruz Verde + Yuno _ Información para el business case.xlsx"). Antes de enviar QUITÓ del borrador la opción del export transaccional de Mercado Pago y el párrafo de datos personales/NDA; dejó la línea pidiendo día para la reunión técnica con TI. Borrador viejo r5317102337443385744 BORRADO el 29-sep; no quedan borradores de Cruz Verde en Gmail. Esperando: documento diligenciado + día para la reunión con TI. Sigue pendiente la propuesta v2 (tiers, pesos, BC sin L4/L5).

**Estado 6-oct-2026 (correo de pendientes):** Los 5 documentos del NDA quedaron ENTREGADOS: certificado de existencia, certificación bancaria y cédula (German, 1-oct, hilo NDA); UBO (JP Pantoja a mariateresa.silva@, 1-oct); formulario FC-FI-FO-01 firmado por JPO vía DocuSign el 5-oct y enviado por JP Pantoja el 5-oct en un hilo aparte donde German NO está (lo registra el Jira YLT-486; pedirle a JP el reenvío). Según el Jira, Michael le pidió a Adriana avanzar la creación del NDA el 5-oct; Jira YLT-486 = PENDING W/ COUNTERPARTY, due 14-oct, asignado a German; María Gabriela revisa el NDA cuando llegue. Pendiente de CV: borrador del NDA, info del BC, fecha reunión técnica TI, conversación con Mike + Finanzas, lineamientos del RFP. Pendiente de Yuno: propuesta v2 (tiers, pesos, BC sin L4/L5) NO enviada desde el 25-sep. **Correo de pendientes en BORRADOR Gmail (6-oct)**, reply en el hilo "Cruz Verde + Yuno" a los 6 + cc Adriana, Guillermo, Alejandro, Susana, Carlos, JP Pantoja; compromete la propuesta v2 "esta semana" y propone 30 min con Mike y Adriana. Copia en `Deals/Cruz Verde/cruz-verde-pendientes-email-2026-10-06.md`. No hay canal de Slack propio de Cruz Verde; todo vive en #salesops-legal y en Gmail.

## project-curology
*Curology deck — slide 2 lives in Supabase business_overview column (precedence over local JSON); card-only checkout is the lead angle*  
*type: project · last updated 2026-07-30*

Curology deck (deck.yuno.tools/m/curology, built 2026-07-30, commit cdddb1d). **Slide 2 source of truth is the Supabase `business_overview` COLUMN** (patched directly so the slide rendered before the bundle deploy landed); it shadows the bundled business-overviews.json entry, so edit slide 2 via Supabase or flip forceLocalOverview, same trap as [[project-stubhub]]/Riot. Logo also mirrored to storage bucket `merchant-logos/curology-64712b47.png` via `logo_url` (manifest wins post-deploy; identical asset). Storage API gotcha: the `sb_secret_` key fails as Bearer JWT, must send it in the `apikey` header too.

Key research: card-only checkout confirmed by official support article (no PayPal/Apple Pay/prepaid; HSA/FSA cards OK) = strongest verified missing-methods deck angle. Revenue OMITTED (only contradictory aggregator estimates). Catalyst: Walmart Prescription Acne Kit, 1,000 stores, jul-16-2026, kit $24.97 redime online 60 días de Rx. 5M+ pacientes desde 2014. Logo wordmark sacado del PR de Walmart (logo.dev solo tenía el tile cuadrado).

## project_deck_edit_button
*Self-serve \"Editar deck\" button feature — flow, files, and pending one-time setup*  
*type: project · last updated 2026-07-14*

Self-serve deck editing so any @y.uno user can request changes without relaying through German. Built 2026-06-30 in yuno-sales-pitch-maker.

**Flow:** Edit button (last slide / SlideCTA) → POST /api/edit-request → labeled GitHub issue (`deck-edit`) → `.github/workflows/deck-edit.yml` runs Claude Code Action → opens PR → merge → Railway auto-deploys → `.github/workflows/deck-edit-notify.yml` → POST /api/edit-done → email requester. Decisions: PR (not direct push), email-only notify, any @y.uno session.

**Files:** [src/components/EditDeckButton.jsx], mounted in SlideViewer (NOT SlideCTA anymore), server endpoints `/api/me` `/api/edit-request` `/api/edit-done` (reuse session + Gmail helpers), 2 workflows, docs/DECK_EDIT_SETUP.md.

**PER-SLIDE button (2026-07-03):** the Edit button now shows on EVERY slide (mounted once in SlideViewer for the current slide, `!shared`), reads "Editar slide", and auto-scopes each request to the slide the user is on — it sends `slideHint = "Slide N · <label>"` and the modal shows an "Applies only to Slide N" banner (manual slide field removed). The routine's #1 rule keys off the `**Slide / sección:**` line: it finds the component by grepping the label in SlideViewer.jsx's order arrays (`{ Component: SlideX, label: '...' }`) and edits only that SlideX file. EXCEPTION: on the LAST slide (`isLast`) the button flips to OPEN/deck-wide scope (reads "Editar deck", amber banner) and sends slideHint "Deck completo · alcance abierto..." — the agent then may make structural changes (add/remove/reorder slides via the order arrays), still respecting deck scope.

**Setup DONE 2026-07-02.** Label `deck-edit` created; repo secrets ANTHROPIC_API_KEY + DECK_BASE_URL (https://deck.yuno.tools) + EDIT_NOTIFY_SECRET all set via `gh`; Railway env GITHUB_EDIT_TOKEN (reused the classic `GITHUB_PAT` from .env.local, scope `repo` → creates issues, no org approval needed) + matching EDIT_NOTIFY_SECRET. Verified: server responds on deck.yuno.tools, /api/edit-done secret matches, token has repo access. Claude GitHub App NOT needed — deck-edit.yml uses `secrets.GITHUB_TOKEN`, so the org-owner install block German hit is irrelevant. German is `maintain` (not admin) on the repo but can still write Actions secrets + create labels via `gh`. STILL UNVERIFIED (needs a live button click): (1) button renders for @y.uno session, (2) Actions "allow create PRs" toggle — needs admin German lacks; if PR creation 403s, patch deck-edit.yml to pass a PAT as github_token instead of the native GITHUB_TOKEN. Reminder: rotate the Anthropic API key (pasted in plaintext during setup).

Button invisible to clients (/api/me returns null without @y.uno session). Caveat: shared-component copy edits affect ALL decks in that language; per-merchant data is in Supabase. Scope every edit to the one target deck — see [[feedback_deck_edits_scoped]].

**Yuno does NOT use GitHub Actions (team policy, confirmed 2026-07-03)** — so the Actions-based auto-flow is dead. Replaced with a SCHEDULED CLOUD AGENT (Claude routine `deck-edit-processor`, id `trig_01DUa5G7hbY8woWrMgwnhiMv`, https://claude.ai/code/routines/trig_01DUa5G7hbY8woWrMgwnhiMv) that runs hourly (`0 * * * *` UTC — 1h is the platform minimum, NOT 15min), model claude-sonnet-5, source repo yuno-payments/yuno-sales-pitch-maker. Each run: STEP 0 non-destructive `git push --dry-run` credential check (prints PUSH-CREDENTIALS: OK/FAILED), then processes open `deck-edit` issues per the scoping rules ([[feedback_deck_edits_scoped]]), builds, pushes to main, closes issue. For truly urgent edits, trigger it on demand (Run now / RemoteTrigger run) instead of waiting for the hour. RESOLVED 2026-07-03: the cloud CCR env CAN push to the private org repo — test run printed `PUSH-CREDENTIALS: OK`. Gotcha caught: a fresh clone defaults HEAD to `master`, so the agent wrongly assumed master was production; prompt now hard-codes the branch fact (deploy=`main`, `master`=protected decoy, always `git checkout main` + push origin main). See [[project_salesmaker_protected_master]].

**2026-07-14 — REBUILT to instant auto-apply (no deploy, always email).** The async-routine flow was unreliable (applied via hardcoded per-slug conditionals in components, needed a Railway deploy each time, and didn't reliably email). Replaced with a synchronous apply path:
- **Per-deck override layer** ([[project_deck_override_layer]]): `business_overview.deckOverrides = { slideKey: { fieldKey: value } }` on the deck's Supabase row, surfaced on `data.OVERRIDES`, applied by `ov(data, slideKey, fieldKey, fallback)` / `ovSlot()` in `src/lib/deckText.js`. The 8 shared banking/PSP/wallet slide components are retrofitted (MarketContext, OrchestrationEra, BankingPlaybook, WhatIsOrchestration, Infrastructure, ValueLevers, WhiteLabelPromise, CTA). An override wins over both base copy AND the old slug-conditional fixes. Writing it = live on next load, NO deploy.
- **`/api/edit-request` now auto-applies** (server/index.mjs): Claude (`server/lib/deck-edit-apply.mjs` + `deck-copy-catalog.js`) translates the request into an override patch → PATCH Supabase → read-back verify (never claims live unless confirmed) → email requester "ya está en línea". Anything it can't safely apply (verify-a-fact, structural, off-catalog slide) is escalated to an OPEN issue labeled `needs-human` and the requester is emailed "en cola". Fail-safe: any error → escalate + email, never a broken deck.
- Verified end-to-end 2026-07-14: Supabase override write → renders live on deck.yuno.tools (Playwright). Endpoint deployed (401 gated). The Claude planning call itself is only exercisable via a real @y.uno session (auth) — acceptance test = click Edit on a deck and request a simple wording change.
- CATALOG MAINTENANCE: `deck-copy-catalog.js` holds the fieldKey→current-Spanish-text map Claude matches against; update the sample text if a slide's copy is reworded, and add new slideKeys when new slides are retrofitted. Slides NOT in the catalog (Cover, Leadership, MarketCharts, etc.) escalate to human.
- The hourly cloud routine still exists as a fallback for escalated/off-catalog issues but is no longer the primary path.

**Prior context — GitHub Actions was also DISABLED on the repo** (workflows API total_count=0, 0 runs, edit issues pile up OPEN and never process). So the button files issues correctly but the agent NEVER runs — this is why edits appear "slow/not happening." Enabling Actions needs repo ADMIN (German is only `maintain`), likely an org owner: Settings→Actions→General→"Allow all actions" + Workflow permissions "Read and write" + "Allow GitHub Actions to create and approve pull requests." Until then, process pending `deck-edit` issues MANUALLY: read issue body, apply scoped change, `npm run build`, commit + push to main (Railway auto-deploys), then `gh issue close`. Cleared issues #8/#9/#10 this way on 2026-07-02. Note: `timeout` cmd doesn't exist on macOS; run `npm run build` directly. Related: [[project_salesmaker_protected_master]] (deploy from main), [[project_supabase_service_key_location]].

## project_deck_languages
*yuno-sales-pitch-maker supports 4 deck languages (en/es/pt/fr) and how to add more*  
*type: project · last updated 2026-06-09*

The deck app (yuno-sales-pitch-maker) renders in **4 languages**: en, es (LatAm Spanish), pt (Brazilian Portuguese), fr (European French). Added 2026-06-09. SDR picks language in the LandingPage modal (EN/ES/PT/FR buttons).

**Architecture (all in `src/lib/i18n.js` + per-slide):**
- `t(lang, en, es, pt, fr)` — single-string/JSX localizer (returns the matching arg; works with JSX). `pickLang(lang, {en,es,pt,fr})` — selects a whole parallel data structure.
- Slide components use `t()` for inline strings and `pickLang()` for parallel data blocks (e.g. `PILLARS`/`PILLARS_ES`/`PILLARS_PT`/`PILLARS_FR`). SlideDiagnostic's `PAIN_TAXONOMY` carries desc/descEs/descPt/descFr.
- `audience.js` AUDIENCES bundles have en/es/pt/fr noun sets (bank/PSP/wallet).
- Share-link compact token encodes language as an **absolute 2-bit code** (en=0,es=1,pt=2,fr=3) in bits 1-2 of the digit, theme in bit0 (en/es back-compatible). See `SlideCTA.jsx buildShareUrl` + `App.jsx` decode + `LANGUAGE_BY_CC`.
- Per-merchant content (pain titles, capability copy): Supabase `*_es/_pt/_fr` column trios; `src/lib/supabase.js toSlideData` picks by language with English fallback. `server/lib/translate.mjs` is language-parameterized; `POST /api/translate-merchant/:slug?lang=es|pt|fr` backfills. `migration 0003` adds the pt/fr columns.

**To add a 5th language:** extend `t()`/`pickLang` usage isn't needed (they're generic) but you must: add the arg slot to `t()`, add a picker button, add the `_XX` parallel-data siblings in each slide, add the audience bundle, widen the share-code (currently 2 bits = 4 langs max, needs 3 bits), add `*_xx` DB columns + migration, and a `translate.mjs` LANGS entry. Rule: **no em-dashes** in any copy ([[feedback_no_dashes.md]]).

**Outstanding for pt/fr per-merchant content:** the DB migration `0003` must be applied and the translate endpoint run per merchant (`?lang=pt`, `?lang=fr`); until then those decks show English pain/capability text (the static chrome is already fully translated).

## project_deck_override_layer
*Per-deck copy override layer — how any vertical-deck slide text is edited live via Supabase, no deploy*  
*type: project · last updated 2026-09-08*

Per-deck copy overrides let any single deck's slide wording change instantly by writing to its Supabase row — no code change, no deploy. Built 2026-07-14 in yuno-sales-pitch-maker. Powers the instant [[project_deck_edit_button]] auto-apply.

**How it works:**
- Storage: `merchants.business_overview.deckOverrides = { "<slideKey>": { "<fieldKey>": "<new text>" } }` (non-destructive; absent for unedited decks).
- Surfaced on `data.OVERRIDES` (App.jsx banking branch + vBase branch + toSlideData all carry it through; banking decks render `{...BANKING_DATA}` so it's injected explicitly).
- Applied in components via `ov(data, slideKey, fieldKey, fallback)` and `ovSlot(data, slideKey, fieldKey)` (additive slots like footnotes) from `src/lib/deckText.js`.
- Precedence: Supabase override > hardcoded per-slug fix (applySlugOverrides) > base localized copy.

**Retrofitted slides (8, shared across banking/PSP/wallet):** SlideMarketContext (`marketContext`), SlideOrchestrationEra (`orchestrationEra`), SlideBankingPlaybook (`bankingPlaybook`), SlideWhatIsOrchestration (`whatIsOrchestration`), SlideInfrastructure (`infrastructure`), SlideValueLevers (`valueLevers`), SlideWhiteLabelPromise (`whiteLabelPromise`), SlideCTA (`cta`). Field-key convention: `card0.body`, `proof.indrive`, `lever01.stat`, etc. Full contract lives in `server/lib/deck-copy-catalog.js`.

**To edit a deck's copy directly (bypassing the button):** PATCH the Supabase row's `business_overview.deckOverrides` with the slideKey/fieldKey/value. Supabase URL `https://mlwiosgalwsroisdkytl.supabase.co` (public, in the client bundle); service key in [[project_supabase_service_key_location]]. Live on next deck load.

**To add override support to a new slide:** wrap its rendered strings with `ov()`/`ovSlot()`, add its slideKey + field samples to `deck-copy-catalog.js`. Un-retrofitted slides escalate to a human in the edit flow.

**Structural bridge (merchant decks):** `deckOverrides.diagnostic|yunoSolve|globalPresence` also merge into `SLIDE_OVERRIDES.slide3|slide4|slide7` (mergeSlideOverrides in supabase.js), so structural keys ride in the same buckets as ov() field keys.

**Extensions added 2026-09-08 (McAfee/1Password QA batch, commit 939741d):**
- `diagnostic.pspCap` (int) — raise the 4-chip topology cap; `diagnostic.capabilityDefs` ([{key,label}]) — replace the capability stack wholesale (e.g. add Wallets/Local methods chips); `diagnostic.contentZoom` (0.5–1) — CSS-zoom the whole diagnostic card so oversized topologies/chip sets fit (keep `width:100%`; % width does NOT rescale under zoom in Chromium — a `100/z%` width overflows the column and overlaps the pain cards); `diagnostic.missingMethodsExact` — render missing_methods verbatim, skip geo-backfill.
- `yunoSolve`: `'__REMOVE__'` as a feature-pill override (`arch.feature{i}`) drops the pill; `statOverrides: {i:{n:'__REMOVE__'}}` drops an impact stat box (grid columns now follow stat count); `archPsps` pins slide-5 provider tiles.
- `businessOverview` data (in business_overview itself, not deckOverrides): `countries[].shareLabel` (verbatim % display), `revenue.sourceCaption` (replaces Estimated badge when estimated:false), `bottomThirdLeft` (stack Business Lines under countries when APM chips need the full right column).
- `productSuite.'pillarN.itemM.tag'` — small tag chip next to an item title (e.g. ROADMAP); slide-6 stats via `statN.n`.
- SlideCTA slide-11 stats stay code-side: `DEFAULT_STAT_OVERRIDES_EN[slug]` in SlideCTA.jsx (magnific, mcafee, 1password); `cta.ctaLine` adds the closing ask line.
- IMPORTANT: PostgREST PATCH REPLACES the whole `business_overview` column (no JSON merge) — always send the FULL object (overview + deckOverrides) or you wipe slide 2.

## project_deck_tools_handover
*Deck tools (yuno-sales-pitch-maker + Neverland + deck counter) are being handed over to Magdalena Torrealba and Yamin Lahmeur (Sep 2026); they will replicate the tool in a new repo/Supabase and own it. Handover doc lives in docs/HANDOVER.md and as an artifact.*  
*type: project · last updated 2026-09-23*

On 2026-09-23 German asked for a full English handover of everything around the web deck tool (repo `yuno-payments/yuno-sales-pitch-maker`, Railway `deck.yuno.tools`, Neverland `decks.internal-tools.y.uno`, Supabase `mlwiosgalwsroisdkytl`, the `/team` `/decks` `/views` deck counter, the Edit button, `/builddeck`) for **Magdalena Torrealba and Yamin Lahmeur**, who will build a NEW project replicating the tool with everything that exists and become its owners (they plan improvements).

Deliverables: `yuno-sales-pitch-maker/docs/HANDOVER.md` (commit 4a86a03 on `main`, 17 sections incl. phase 0-7 replication plan) and a published Artifact page "Deck Tools Handover" (same content, built with `marked` from the MD in the scratchpad `handover-build/build.mjs`).

Facts captured that day: Supabase had 1,332 rows (458 curated merchant, 505 auto merchant, 21 banking, 9 PSP, 7 wallet); Railway `/api/health` ok but bundle stale since ~8-sep; Neverland unreachable without VPN; GitHub default branch still `master`; `gh` unauthenticated; `.env.local` PAT expired; Kingdom API queries were blocked by the auto-mode classifier (credential exploration), so live Kingdom env/secret state was NOT verified.

**Why:** German is relocating to SF (Sep 28 to Nov 4) and the team wants to own and evolve the deck platform without depending on him.

**How to apply:** When Magdalena or Yamin ask about the deck tool, point them to `docs/HANDOVER.md` first and keep it updated when architecture changes (it is the living runbook). Recommended plan in the doc: new repo + new Supabase project seeded by copy, own Neverland service via `/yuno:deploy-neverland` Path B, change `PUBLIC_DECK_ORIGIN`/`DECK_BASE_URL`, decide Railway vs public Neverland, fix PDF Chromium. If German asks to update the handover, edit the MD and re-run the build script, then republish the same artifact URL. Related: [[neverland-migration]], [[project_deck_edit_button]], [[project_deck_override_layer]], [[railway-stale-sep-2026]], [[project_salesmaker_protected_master]], [[project_supabase_service_key_location]].

## project-doordash-aj-tus
*DoorDash — A.J. Tus (Head of Payments & FinTech Partnerships) es la puerta; respondió una sola vez (sep-2025) y derivó a Alodie Taveras; German lo contactó él mismo el 5-oct-2026 para Money20/20 (borrador de Claude eliminado)*  
*type: project · last updated 2026-10-05*

**DoorDash.** Contacto principal: **A.J. Tus** (aj.tus@doordash.com; firma "A.J."; Head of Payments & FinTech Partnerships según la lista de Money20/20; en su firma de 2025 decía "Business Development"). LinkedIn: linkedin.com/in/alexanderjohntus. **Alodie Taveras** (alodie.taveras@doordash.com) es de su equipo; German la conoció en Stripe Tour New York (30-sep-2025); estuvo de licencia de maternidad hasta octubre 2026.

**Cronología:**
- sep-2025: German invita a A.J. a Stripe Tour NY; A.J. responde (único correo suyo) que no va y presenta a Alodie. German y Alodie se ven en el evento.
- mar y abr-2026: 4 correos fríos de German a A.J. (hilo "Payments @ DoorDash" + "How about success?"), sin respuesta.
- abr-2026: German vio la sesión de A.J. en Stripe Sessions; intentó saludarlo después, no se dio. Deck ss26.yuno.tools/m/doordash (enviado a Alejandro internamente, no a DoorDash).
- 22-jul-2026: German revive el hilo de Stripe Tour NY a A.J. y Alodie (cc Alejandro); rebota el auto-reply de maternidad de Alodie; A.J. no responde.
- 1-oct-2026: Samuel Carreño escribe "Flying to SF to meet you" a Ravi Inukonda y Hui Theng Poh (German y Samuel en cc).
- 5-oct-2026: A.J. está en la lista de asistentes a Money20/20 Las Vegas (tier 1 en money2020-x-tcl-matched.json). Claude dejó un borrador con la invitación al evento supercar de Yuno y PayPal ([[reference-money2020-vegas-2026-supercar-event]]), pero **German lo ENVIÓ él mismo ese día (5-oct 21:22 UTC) como respuesta en el hilo de Stripe Tour NY, con Sean en cc**, y pidió borrar el borrador suelto. Siguiente paso: esperar respuesta de A.J. No volver a escribirle a A.J. sobre Money20/20 sin que German lo pida.

**Datos para no equivocarse:** DoorDash figura como "Open Opportunity" en Salesforce (TCL). A.J. nunca ha tenido una conversación de fondo con German; no decir "since we last spoke", sí "since we were last in touch".

Relacionado: [[project-sf-relocation-fall-2026]].

## doTERRA uses Cybersource
*doTERRA's PSP is Cybersource, relevant for any outreach or BC referencing their payment stack*  
*type: project · last updated 2026-04-15*

doTERRA processes payments through **Cybersource** (Visa-owned gateway).

**Why:** User (SDR) confirmed this directly 2026-04-15. Not publicly disclosed in research, so it must come from memory, not re-research.

**How to apply:** Any doTERRA-related BC, email, cold call, or slide should reference Cybersource by name as the incumbent. Lean into Cybersource-specific pain: limited native orchestration and smart routing, weak APM coverage in LATAM and APAC (no Pix, OXXO, PayPay, Kakao Pay), cross-border MDR exposure, Decision Manager fraud complexity, and no native recovery layer for recurring LRP declines.

## project_eve_events_agent
*Agente "Eve" en Yuno Agents (ai.agents.y.uno) para buscar eventos gratis en SF, registrar a German y avisarle por correo; hoja de Google "SF Events Feed · Eve" como puente con el playbook*  
*type: project · last updated 2026-09-30*

German creó el 30-sep-2026 en Yuno Agents un agente llamado "Eve" para: registrarlo en todos los eventos gratis del viaje a SF y avisarle por correo cuando aparezcan eventos. Pidió que estuviera "conectado" al artifact del playbook.

Límites verificados: el artifact de claude.ai responde 403 sin sesión (curl) y la base `db` del calendario solo se lee dentro del viewer de claude.ai, así que un agente externo NO puede leerlo. Puente: Google Sheet "SF Events Feed · Eve (Sep 28 to Nov 4, 2026)" TODO EN INGLÉS (pestañas Events = 64 filas desde events.json, New, Guide; la versión en español 15KKbk… quedó en la papelera el 30-sep), generada con openpyxl y subida por el conector de Drive. Si cambia events.json o el equipo agrega cosas al calendario, regenerar la hoja.

Yuno Agents: tiene cron por agente (/agents/<id>/cron), toolkits con permiso Can view / Can edit (Google Workspace, Slack, Salesforce, Glean, Yuno Payments); no consta un toolkit de navegador. Registro automático en Luma/Partiful/Eventbrite depende de eso; sin navegador, Eve manda links y German se registra.

**Why:** German quiere no perderse eventos y automatizar registros durante el viaje.

**How to apply:** los textos de los campos Identity (who, what, sound, advanced rules) se entregaron el 30-sep en el chat; si pide ajustes, mantener: solo eventos gratis se registran, nunca pagos ni datos de tarjeta, TODO EN INGLÉS (German lo pidió el 30-sep: correos, hoja y etiquetas; nada de 'Gratis', usar 'Free'), correo diario 7:30 am PT, precio siempre visible. Relacionado: [[project-sf-trip-playbook]], [[reference_yuno_agents_platform]].

## eventbrite-bakeoff
*Eventbrite orchestrator eval — call 2026-08-04 hecho: Paul Pasion en su ÚLTIMA SEMANA en Eventbrite (confirmado 2026-08-11, antes se estimaba ~08-18), decisores = Noe/Giacomo/Filippo (Bending Spoons Milán, ya en CC directo); MNDA + materiales custom antes del vie 2026-08-14; Justo en Milán fin de agosto*  
*type: project · last updated 2026-09-18*

**Update 2026-08-20 (call con Filippo, primera con el equipo de Milán sin Paul):** Paul confirmado fuera del todo (su correo ahora auto-responde "no longer with Eventbrite", redirige a Alfredo Riggio alr@bendingspoons.com). Solo llegó **Filippo Bernardoni, Product Manager** (no "líder de commerce" como se asumía); Noe y Giacomo faltaron sin explicación, no se les preguntó por qué. El deck de 46 slides nunca se mostró en la call, se mencionó recién al cierre como algo para la próxima vez.

**Hallazgo clave, cambia el ángulo:** el interés real de Filippo NO es pay-in orchestration (el eje del deck actual), sino **payouts + sacar a Eventbrite del flujo de fondos por completo**, empujado por PSD2/PSD3 en Europa. Textual: hoy Eventbrite es el merchant, cobra y paga a los organizadores; están evaluando que cada organizador sea su propio merchant of record (vía BYOC, bring your own credentials) para dejar de estar en el flujo de fondos. Jarrett (SE) respondió muy bien en vivo: estructura de marketplace (Stripe Connect, Adyen for Platforms, PayPal PPCP, JPMorgan embedded), los 3 modelos de KYC, timelines de integración (2-3 días típico). Fever se mencionó como referencia y aterrizó bien cuando Filippo preguntó por marketplaces similares (Fever = mismo modelo, el organizador es el merchant of record).

**⚠️ Riesgo a verificar YA:** Jarrett afirmó en la call grabada que tienen "capabilities and API endpoints" para JPMorgan embedded al mismo nivel que Stripe/Adyen/PayPal. La memoria previa indica que el conector JPMorgan estaba en modo MOCK al 11-may. Si sigue mock, hubo un overclaim en vivo frente a un prospecto obsesionado con compliance regulatorio. Verificar con Jarrett/producto antes de que se repita.

**German llevó poco peso en la call** (smalltalk inicial + mención tardía del deck), Jarrett cargó toda la sustancia técnica y comercial. Cero de las preguntas de descubrimiento planeadas (formato de evaluación, competencia, estado MNDA) se hicieron.

**Follow-up (mismo día, borrador dejado en Gmail, thread "Re: Eventbrite + Yuno", no enviado):** recap del interés real (payouts + salir del flujo de fondos), NDA aún sin firmar (pendiente, nunca se confirmó su firma pese a la tarea del portal Zip del 11-ago), link al deck web (deck.yuno.tools/m/eventbrite, el Slides no se pudo compartir por política de la organización que bloquea sharing externo vía API), propuesta de call la primera semana de septiembre (mié 2 o jue 3), presencial en Milán si Justo viaja. To: Filippo (fber-bsp@eventbrite.com), cc Noe/Giacomo/Justo/Jarrett, Paul quitado de la copia.

**Para la próxima conversación:** reordenar el pitch, payout orchestration + BYOC + salida del funds flow primero, pay-in orchestration como secundario. Esta vez sí mostrar el deck.

**Corroboración interna (Slack, mismo día):** Jarrett, sin haber visto este análisis, llega a la misma lectura por su cuenta: "they don't want to deal with money anymore, so they want to get out of the flow of funds, global remittance is a pain in the ass with KYC/KYB, money transmission, they want to push that onto the event holders, but who knows". Confirma que el ángulo BYOC/payout-exit no es una interpretación mía aislada del transcript, el equipo lo está leyendo igual. Ojo con el "but who knows" de Jarrett: Filippo lo enmarcó como algo que están evaluando a mediano plazo, no una decisión tomada, no venderlo como si ya estuviera resuelto.

Eventbrite (Bending Spoons subsidiary, MoR under EPP). Orchestrator eval formal. **Call realizado 2026-08-04** (49 min, Paul Pasion + German/Justo/Jarrett/Tomas/Joaquin). Transcript: `Deals/Eventbrite/eventbrite-call-transcript-2026-08-04.md`. Resumen detallado: `Deals/Eventbrite/eventbrite-call-summary-2026-08-04.md`.

**Cambio de escenario:** Paul (Director of PM, Commerce / Head of Payments, ex-Uber/Amazon/Marqeta/Recurly) SALE de Eventbrite ~2026-08-18 (Hawaii, sin planes). Su tarea final = shortlist de orchestrators para el liderazgo entrante: **Noe, Giacomo, Filippo** (líderes de commerce, Bending Spoons, Milán, background suscripciones, "new to marketplaces", quieren educación). Eventbrite = ~1/3 del revenue de Bending Spoons (~50 compañías; puerta al portafolio, p.ej. Vimeo). Mandato: correr Eventbrite con 40-50 personas (antes 700-800; eng de payments era 27).

**Pains confirmados en el call:** cero orquestación hoy (sin failover cascade, sin BIN routing, sin debit rails); stack: Stripe, PayPal/Braintree, JPM Chase, Wells Fargo, Mercado Pago, Banco Galicia. Multi-PSP ya decidido (Paul desconfía de consolidar en un gateway). Use case ChaseNet (descuentos JPM tarjetas Chase, routing por BIN). Cierre de entidades LatAm (BR/AR/MX/CO) → MoR (hablan con EBANX vía Braintree, reporting malo). Data normalization + portal único (chargebacks). Interchange+ downgrades + retry economics. Fraude de colusión marketplace (eventos falsos + tarjetas robadas; ¿amarra pay-in↔payout?). Lock-in Stripe Connect (doble FX, re-onboarding). Salir del funds flow (PSD3, agent exception muriendo en EU/UK/CA; no quieren ser PSP/MSB).

**El gap ganador (textual Paul):** "great orchestrators for pay-ins, decent for payouts, no one's tied those two things together". Nuestra respuesta = arquitectura [[gofundme-marketplace]] + Fever (su competidor #1 en Europa; a Paul le pareció "reassuring") + Fiverr ($900K FX ahorrados en 6 meses) + Zuora (rails; Paul conoce a Tien).

**Riesgos internos:** ⚠️ Justo afirmó ChaseNet "we have that connection" pero el connector JPMORGAN era MOCK al 2026-05-11 → verificar con Jarrett/producto ANTES de escribirlo en materiales. CFO Copilot en beta con Fever (release "~2 meses") → tratarlo como roadmap. Preguntas de colusión y downgrades quedaron sin respuesta completa → responder en materiales. Nombres Noe/Giacomo/Filippo sin verificar en LinkedIn.

**⚠️ Sensibilidad de tono con Paul (2026-08-10):** a Paul lo sacaron de Eventbrite, no fue salida voluntaria. Nunca enmarcar correos alrededor de "tus últimos días/semanas en la empresa" (suena mal dado el contexto). Frame positivo alternativo: su viaje a Hawaii (él mismo lo mencionó en la call del 04-ago). Al 2026-08-10 llevaba 4 días sin responder el follow-up del 06-ago; se envió un nudge corto (MNDA + intro a Milán + data ofrecida + competencia + formato de evaluación) como reply al mismo thread.

**Next steps:** Paul envía MNDA → firmar as-is; materiales custom + pedirle DATA a Paul (él ofreció) antes del **viernes 2026-08-14**; intro a Milán post-MNDA; workshop Milán con viaje de Justo (~fin agosto); café Juan Pablo + Paul en Bay Area; WhatsApp Justo↔Paul activo.

**Update 2026-08-11:** Paul confirma en el thread que está en su **última semana en Eventbrite** (no ~08-18 como se estimaba) y hace la intro formal en CC directo a Noe (noeg-bsp@eventbrite.com), Giacomo (gste@bendingspoons.com) y Filippo (fber-bsp@eventbrite.com). MNDA: llegó el mismo día (2026-08-11, 02:43 UTC, 9 min antes del correo de Paul) vía Zip (vendor management de Eventbrite), enviado por Commercial Contracts (commercialcontracts@eventbrite.com), request #4183, tarea asignada directo a German (no a Justo como Paul esperaba): "Upload Pre-Signed Mutual NDA" → hay que entrar al portal Zip con el magic link, firmar y subir el documento firmado, no es solo recibir/responder. Pide explícitamente: (1) insights de cómo Yuno ayuda a marketplaces con PSD2 hoy y PSD3 (Europa), (2) fit para retos de Brasil/LatAm. Instrucción de Paul: coordinar next steps directo con Filippo. German respondió (draft dejado, no enviado aún) proponiendo call de 30 min esta semana vía Chili Piper, confirmando firma de MNDA en cuanto llegue, y comprometiendo deck + materiales antes del viernes 08-14. [[eventbrite-deck]]

Deliverables previos: Q&A bank (data/research/eventbrite-pre-questions-2026-08-04.md), deep dives, deck (Deals/Eventbrite/ + Google Slides). Landmines siguen: no "you lack", PayPal ≠ processor, no layoffs talk.

**Update 2026-09-17:** Filippo no ha respondido nada desde la call del 20-ago. Correo de German del 7-sep (thread "Re: Eventbrite + Yuno", cc Giacomo/Noe/Justo/Jarrett): felicitó por Airtable (cerrada 4-sep), compartió link al deck, reiteró invitación de Justo a Milán semana del 14-sep o la siguiente. Justo estuvo en Milán la semana del 14-sep y NO se logró reunión. Bending Spoons anunció adquisición de Miro el 10-sep-2026 ($1.355B EV, cierre esperado Q4). Nuevo follow-up ENVIADO 17-sep 15:41 UTC (reply al 7-sep, mismos destinatarios): reconoce que no cuadró Milán, felicita por Miro y la racha de adquisiciones, propone retomar por call (sin viaje) sobre Eventbrite (payouts + salir del funds flow) y el portafolio Bending Spoons. Instrucción de German: ya NO proponer in-person en Milán.

## eventbrite-deck
*Eventbrite en 2 formatos: Deck.pptx (29 slides, con ⚠VERIFY pendientes) + deck web /builddeck (23 slides, 13 custom slug-scoped, SOLO claims documentados); deadline 2026-08-14*  
*type: project · last updated 2026-08-05*

Deck final: `Deals/Eventbrite/Eventbrite Deck.pptx` (29 slides, 2026-08-05). Fuentes: storytelling v2 (`Eventbrite/deck-storytelling.md`), pptx proposal draft, Google Slides draft (`179NWg6qX3SS4fXv-BZVnaf8pdujxsHFGara1O_fS5Pg`, house slides exportados como PNG vía Slides API + token del MCP gdrive).

Estructura: Cover → **Exec Summary como slide 2** (pedido de German, con top 10 países de 122: US UK CA AU IT DE ES IE FR MX) → Agenda (con 05 The Path Forward agregado) → Why Yuno (8 slides casa) → Gap (2) → Modular by Design (9) → Path Forward (divider + Bending Spoons + Next steps, construidos nativos duplicando slide 20) → Closing.

Slide de logos RECOMPUESTO con PIL (15 aprobados, checkerboard intacto): sin Fever, sin Moonactive, sin NetEase (reglas duras del storytelling). Sin logo de Fiverr disponible → quedó fuera.

**Build vs Buy (2026-08-05, commit f3620c2):** deck web cierra con 2 slides estilo Flair BC antes del CTA (22 slides total): (A) checklist in-house + anclas de SUS números (27 FTE equipo de payments pre-transición, empresa dimensionada a 40-50 personas) + estimados marcados "(est.)" (squad 6-10 FTE, ~$1-1.5M/yr, 12-18 meses); (B) tabla Buy·Yuno vs Build·in-house con fila "LatAm and EBANX" hablando de su evaluación viva de EBANX directo (el portal extra que su payment ops lead ya rechazó) vs EBANX detrás de la capa normalizada (EBANX SÍ está en partners.generated.js = catálogo canónico, nombrable). Estimados siempre etiquetados, nunca como hechos.

**Fixes de viewer real (2026-08-05, commit 64830ec):** el print route (1440x810) NO detecta todos los overlaps; QA también en /m/eventbrite vivo (email gate: pasar con german.tatis@y.uno; esperar ~5s por animaciones de entrada o el slide parece vacío). ProductSuite eventbrite-only: Concierge = ítem del pilar AI, banda inferior eliminada, items flex '1 1 auto' (estiran), Payouts en Orchestration, Network tokens en Security & Risk. Diagnostic fit: chip "J.P. Morgan" (no "Chase", ocupaba 3 líneas) + `capabilityKeys` en slide-overrides.json = 1 fila de 5 chips live.

**PDF download (2026-08-05, commit 24e523d):** /api/pdf generaba el deck completo en Chromium por request (~70s en Railway = botón "no descarga"). Ahora: cache en disco (os.tmpdir()/deck-pdf-cache, key slug+sig+lang+event, TTL 15min) + de-dupe inflight + stale-while-revalidate → segunda descarga ~0.01s. CARET FIX: page.pdf() pinta un hairline "|" en el borde de spans con background-clip:text gradiente; regla en index.css `html[data-print-mode] span[style*="background-clip: text"]` aplana a #7c89ef sólido (print-only, todos los decks). OJO local: el server cachea build/index.html al boot; si rebuildeas, REINICIA el server o sirve un bundle borrado (MIME error, __PDF_READY__ nunca llega). Además `npm run build` local a veces CUELGA (timeout) sin escribir build/: verificar timestamp de build/assets tras cada build.

**Pase de Justo (2026-08-05, commit eb3c8c9):** deck = **18 slides, arco REQUIREMENT→BENEFIT→PROOF** (exec+situación+gap → solve+infra+suite+modular+MoR → presence+trusted+leadership → CTA). FUERA: Dashboard std, Build vs Buy (x2), Stages. Modular OS = grid 4x2 compacto con íconos, título "...for financial infrastructure". Freedom: "How your model looks today" vs "The modular model, with Yuno". MoR = modelo GLOBAL (3 pasos + 90+ providers dato de Justo + dLocal/Unlimit/EBANX; ya no es slide de LatAm). Suite: engine enumera "Pay-in, payouts, tax and KYC/KYB on one control plane". GLOBAL: SlideDashboard dice "Connect any provider" (4 idiomas). story.jsx: tipografía subida (body 13-17.5, cardTitle 18-29) + Card centrada verticalmente. OJO: macOS zsh NO tiene `timeout` → nunca usarlo en builds locales (falla silencioso y build/ queda viejo).

**Pase editorial (2026-08-05, commit f4893f4):** German no es fan de "las cajitas" → sistema editorial en story.jsx: primitivo `Step` (numeral fantasma grande + hairline, sin caja) usado en payouts/splits/MoR/routing; tabla Freedom con check/cross y hairlines sin celdas; gap con laterales sin caja (solo el centro punteado encerrado); loop rehecho con ledger glowing central + endpoints circulares; suite: fuera el ítem Payouts suelto, el engine enumera todo. Tipografía base subida otra vez (body 13.5-18.5). OJO builds locales: `npm run build` CUELGA si vite dev corre en paralelo → matar el dev server (lsof -ti :5199 | xargs kill -9) antes de build. QA por viewer vivo requiere pasar el gate y esperar detach del input + ~2.4s por slide de animación.

**Pendiente antes de ENVIAR** (deadline viernes 2026-08-14): los badges ⚠ VERIFY siguen en slides de pay-in routing (ChaseNet, US debit rails), LatAm entities (85+ MoR, EBANX direct) y dashboard (Starlink); checklist sección 6 del storytelling se valida con Justo/Jarrett y luego se quitan los badges.

Build reproducible: `scratchpad/build_deck.py` (python-pptx; duplica slides con re-mapeo de rels de imágenes, renumera páginas con word_wrap=False). QA: export PDF vía PowerPoint AppleScript + pypdfium2 → PNGs. PDF de QA en `~/Downloads/eventbrite-deck-qa.pdf`.

**Deck web /builddeck (final 2026-08-05, commit 6a01a21):** deck.yuno.tools/m/eventbrite = **20 slides vía EVENTBRITE_ORDER explícito** (patrón Polymarket/Lulu) en SlideViewer Y PrintViewer (listas duplicadas; olvidar PrintViewer deja el PDF sin los slides). Arco: cover → exec (top10 países, sin "of 122") → Infrastructure → ProductSuite (los "4 pillars" que German pidió de vuelta) → GlobalPresence → TrustedBy → Leadership → Diagnostic (topología con LOS 6 RIELES vía pspCap slug-aware en SlideDiagnostic, otros decks siguen en 4; pains con SUS palabras) → Solve (reintegrado a pedido) → gap → modular (OS/freedom/routing/payouts/splits/loop/latam) → Dashboard std → stages → CTA. FUERA: Stack/Spoons/Next (borrados; next steps van por correo). capability_titles/descs actualizados al estándar actual (la fila vieja tenía los retirados + errores). TrustedBy: swap Hotmart→**Fever** vía MERCHANT_LOGO_SWAPS scoped a eventbrite (regla cero-Fever DEROGADA por German para este deck; asset `public/trusted/fever.png`). Pain DESCS por merchant viven en `src/data/slide-overrides.json` (LOCAL, requiere deploy), NO en Supabase deckOverrides. capabilities_live = payouts/kyc/kyb (solo lo confirmado). missing_methods corregidos a sus mercados top-10 (Mercado Pago quitado: es un riel suyo, no un método faltante). REGLA: claims ⚠VERIFY nunca en el deck web (vivo); solo docs.y.uno. QA Playwright /m/eventbrite/pdf (1440x810/slide) con Chrome for Testing.

## project_experian
*Experian (DataCrédito Colombia) deal; Carlos Falla (PM) + Cristian Vargas (Midatacrédito) + Milena Olaya (operaciones); prioridades 29-sep = débito a cuentas (Davivienda, Grupo Aval), alternativa a PayU en tarjetas, Bre-B tokenizable; implementación desde abril 2027; follow-up 29-sep en borrador Gmail; conciliación con Milena por agendar*  
*type: project · last updated 2026-09-29*

Experian DataCrédito (Colombia). Contactos: Carlos Falla (PM, carlos.falla@experian.com, decide junto a producto), Cristian Vargas (dueño de Midatacrédito, cristian.vargasm@experian.com, coordina sesiones y fija prioridades), Milena Olaya (operaciones, asistió en abril, es la persona para conciliación). Intro original feb-2026 vía Clariana Carreño a Julián Buitrago (Country Manager CO). BC en PDF (Business Cases/Business Case - Experian.pdf, abr-2026). Magdalena Torrealba coordina agenda; Daniel Lozano (PM Subscriptions) es la contraparte técnica; Joaquín Mann acompaña.

Call 23-sep-2026 (primera desde abril): stack = PayU (tarjetas), Wompi (Bancolombia, Nequi, Daviplata), PSE + enrolamiento + débito automático por archivo a Bancolombia (respuesta D+1). Split ~55/25/20, el 55 es cuentas; ~100 a 150K suscriptores efectivos, base ~300K. Carlos: "esto no lo hemos visto en el mercado". Pidió diagrama del flujo de integración y tarifarios para business case por transacción. ~150M COP de desarrollo de su lado; piloto ~20K cuentas vs modelo actual.

Call 29-sep-2026 (deep dive suscripciones, 41 min; German, Daniel, Joaquín con Carlos y Cristian): demo de conexiones y ruteo (porcentajes, 2 fallbacks, condiciones por BIN/emisor/metadata) y del motor de suscripciones (planes, reintentos estándar/Smart Recharge/custom, A/B testing, pausar/upgrade, meters). Prioridades de Cristian: (1) débito automático a cuentas de ahorro y corriente, sobre todo Davivienda y Grupo Aval; (2) tarjetas: explorar alternativas a PayU porque la efectividad baja tras la adquisición (cambio frente al 23-sep, cuando Carlos no quería tocar PayU ni Wompi); (3) Bre-B como medio tokenizable. Yuno dijo: integración directa con Nubank y BBVA, explorando un tercero para el pool de bancos colombianos; banking as a service en desarrollo, cierre esperado en semanas. Timeline nuevo: iniciar implementación en abril 2027 (inicio de su año fiscal); antes deben adelantar vinculación de proveedores y caso de negocio.

**Why:** cuenta grande en Colombia con un caso de uso nuevo (suscripciones sobre débito a cuenta, no tarjetas). El fit depende de la cobertura de bancos: Davivienda y Grupo Aval son la prioridad 1 y hoy Yuno solo tiene Nubank y BBVA directos.

**How to apply:** próximos pasos abiertos = (a) Cristian agenda conciliación con Milena y propone las opciones de agenda (German tenía libres jueves 1 y viernes 2-oct, 10:00 a.m. o 2:30 p.m. COT, pero no las ofreció por escrito); (b) German comparte opciones de débito automático para Davivienda y Grupo Aval (la lista de tarjetas va en el follow-up del 29-sep); (c) Daniel confirma estado de tokenización de Bre-B; (d) tarifarios después de conciliación (consultar [[reference_yuno_pricing_policy]]); (e) pedir documentación de vinculación de proveedores. Sin cerrar desde el 23-sep: migración de cuentas de ahorro ("validando, creemos que sí") y diagrama del flujo de integración. No citar en correos cifras internas (split, suscriptores, 150M COP) ni el comentario sobre la efectividad de PayU. En notas y transcripts "Breve" = Bre-B. Archivos en Deals/Experian/ (resumen y follow-up del 29-sep). Relacionado: [[project_unicef_colombia]] (mismo patrón de débitos batch y ACH en Colombia), [[project_sf_relocation_fall_2026]] (German en PT, COT = PT + 2 h).

**Estado 29-sep-2026:** follow-up del 23-sep ENVIADO con one-pager de suscripciones adjunto, sin respuesta escrita de Experian. Follow-up del 29-sep en BORRADOR de Gmail (versión 2) como respuesta en el hilo "Yuno + Experian" (a Cristian y Carlos, cc Magdalena, Daniel, Joaquín): texto corto de German reorganizado en Resumen, Alternativas a PayU para tarjetas y Próximos pasos. Lista enviada = Wompi (ya contratado), Redeban, Mercado Pago, Kushki, sin tarifas ni tasas de aprobación. Antes de enviar: confirmar con Daniel que los cuatro soportan cobro recurrente en Colombia vía Yuno, y pedir benchmark interno de aprobación por procesador. German prefirió NO poner por escrito los bancos conectados (Nubank, BBVA) ni proponer horarios de conciliación; espera las opciones de Cristian. El transcript de Google Meet del 29-sep salió inservible y Gong no tenía la llamada al redactar. Verificación de procesadores en [[reference_colombia_processors]].

## project_fanduel
*FanDuel deck + research — US*  
*type: project · last updated 2026-07-01*

FanDuel deck live at deck.yuno.tools/m/fanduel (slug `fanduel`, industry "Gaming & Payments"). Built via [[project_supabase_service_key_location]] /builddeck then enriched with full /research 2026-07-01.

Key facts: #1 US online sportsbook (~41-43% GGR) + iGaming (~26-28%), FY24 US revenue $5.8B (+30% YoY, $4.39B→$5.73B), wholly owned by Flutter Entertainment since Jul 2025. US-concentrated (92.6% traffic), Canada/Ontario second market.

**Payment stack (the pitch):** PayNearMe is the confirmed hub (cash + open banking via Trustly + push-to-debit), Sightline/Play+ prepaid wallet, plus PayPal/Venmo/Apple Pay/ACH. **No independent orchestrator publicly evidenced** across Sportsbook/Casino/Racing/DFS/Predicts — core Yuno angle. Active "Lead PM Payments" job = in-house payments org.

**Top pains (verified):** payout/withdrawal friction is the #1 Trustpilot complaint; structural card declines (credit cards barred for US deposits + bank MCC blocks). Newest catalyst: FanDuel Predicts CFTC prediction-markets entry (Dec 2025, expanded via Crypto.com/OG Jun 2026) = new settlement rails.

Research brief saved at Documents/GERMAN CLAUDE CODE/GTMCoding/data/research/fanduel-2026-07-01.md. Competitors: DraftKings, BetMGM, Fanatics, Caesars.

## project-fareportal
*Fareportal (CheapOair/OneTravel) deal state, Tom Spagnola champion, Manish Kumar Sharma owns payments budget, 2027 supplier window opened July 2026*  
*type: project · last updated 2026-09-21*

Fareportal (OTA: CheapOair, OneTravel; NYC HQ). Contact: Tom Spagnola, SVP Supplier Relations & Partnerships (tspagnola@fareportal.com, LA-based, informal tone, impressed by client logos). He is a door-opener, NOT the payments buyer.

Deal state: Dec 9 2025 their Finance Team said "no new suppliers for 2026, revisit July 2026 for the 2027 cycle". **Jul 27 2026 call OUTCOME (11 min, Tom from a San Diego parking garage): Tom will forward Yuno intro to Manish Kumar Sharma AND Naveen Gupta (new CIO, owns the payments/infra stack) "tomorrow" (Jul 28). New team oversees 2027 partners; 2027 roadmap ownership sits with Naveen's team, not Tom. German sent follow-up email (Gmail draft Jul 27): deck.yuno.tools/m/fareportal + CheapOair BC ($119.7M) + OneTravel BC ($3.94M), combined "$120M+" framing. NEXT: confirm Tom forwarded; then meeting ask to Manish + Naveen.**

**Update sep-2026:** Tom confirmó 28-ago que Naveen "ultimately is going to be the decision-maker". Magdalena Torrealba (Global Sales Strategy) entró al deal: conectó con Naveen por LinkedIn y el 14-sep le envió el hilo "Fareportal x Yuno: Business Case" (To: ngunti@fareportal.com; cc Tom, German, Alejandro) con BC actualizado ($20.9M CheapOair + $3.4M OneTravel, deck.y.uno/fareportal) pidiendo 30 min; sin respuesta al 21-sep. 21-sep: German preparó borrador muy soft en ese hilo (se presenta como quien ha hablado con Tom, interés en la evaluación de proveedores 2027, "díganos qué necesitan"). German quiere tono SOFT con Fareportal, nada intenso. ⚠️ El email de Naveen es ngunti@ (apellido podría ser Gunti, no Gupta): usar solo "Naveen" hasta verificar.

Payments org: CFO Gary Starr; **Manish Kumar Sharma, SVP Finance & Fintech Products** owns merchant processing, virtual cards, banking (at Fareportal since 2013, CPA, Kellogg MBA); **Naveen Gupta, CIO (new, per Tom Jul 27 2026), handles orchestration/infra decisions and 2027 roadmap**. CEO & President: Amit Singh, ex-CFO of Despegar (joined Aug 2025), understands LatAm OTA payments natively.

Stack: supplier side orchestrated (Amadeus Outpayce B2B Wallet, Jan 2026); they SELL "payment orchestration" via Enterprise Solutions (Apr 2026). **Consumer PSP CONFIRMED 2026-07-27 (first-party checkout JS via Wayback; both brands = same platform): CyberSource (Visa) for cards + Google Pay; Braintree (PayPal) for PayPal + Venmo; CardinalCommerce 3DS; Accertify (Amex) anti-fraud + Fraud.net (2019 case study) + in-house Gurgaon review team; Akamai bot mgmt. Multi-PSP, NO consumer orchestrator.** Methods: cards (Visa/MC/Amex/Discover/Diners/Synchrony PLCC), PayPal/Venmo, Apple Pay, Google Pay, Paze (COA), Affirm, Accrue (COA only). Ruled out: Stripe/Adyen/Worldpay/Chase; Riskified/Signifyd/Forter/Sift/Kount. Never pitch "you lack orchestration"; pitch = consumer-side acquiring layer that routes across CyberSource+Braintree + adds local methods (India card-only, INR display only, no UPI evidence).

OneTravel specifics (RESOLVED 2026-07-27): traffic is US-dominant (SimilarWeb annual: US 61.4%, Canada 10.6%, India only 1.76% and −64%; Philippines +300% = growth pocket). Semrush's "India 46%" was panel contamination, likely Fareportal's own Gurgaon ops traffic; NEVER pitch OneTravel as India-led. Legal entity: WK Travel Inc d/b/a OneTravel (owned by Fareportal Inc); RSH Travel Inc = Canada seller-of-travel licensee; all payments in USD per own FAQ (cross-border for ~39% of traffic). Killer outreach hook: OneTravel's own billing FAQ pre-writes answers for "multiple charges per booking" / "duplicate charges" / "charged more than quoted" + dedicated billing phone line = reconciliation pain in their own words. Second hook: ClubMiles loyalty rebuild (Jun 2026) quoted to Manish Sharma ("rebuilt to remove friction"). BC built: Business Cases/BC sheets - OneTravel.xlsx, $3.94M/yr total benefit on $220M modeled TPV (NA-led; CheapOair same platform ≈6x traffic = group upside).

APM verification (2026-07-27, live/Wayback): **Affirm is the ONLY BNPL verified native on both brands** (OneTravel snapshot Nov 2025 w/ live Affirm JS; loans via Cross River). Sezzle/Zip = app virtual-card overlays, NOT integrations — never list them. Accrue pivoted to B2B (byaccrue.com), CheapOair mention gone, checkout-JS ref likely legacy. Paze: 2026 code-level stands, consumer lists no longer show CheapOair (not re-verified). cheapoair.ca FAQ warns CAD cardholders "currency conversion rates in effect" = USD-settlement/cross-border acquiring signal. ICP score 16 🔴 (multi-PSP now verified). Killer analog case: Southwest + CellPoint (cards+APMs+Rapid Rewards points in ONE transaction = exactly the ClubMiles points+card problem).

**Deck live: deck.yuno.tools/m/fareportal** — custom subaccount topology (Fareportal → CheapOair/OneTravel → CyberSource+Braintree under each), built via new `slide3.subaccounts` override in slide-overrides.json (opt-in per slug, reusable for any multi-brand merchant). Slide 3 fit fix: capabilityKeys trimmed to payouts/tokenization/fraud/tax + 4 missing-method chips (full 10 remain in the Supabase row).

Landmines: Vincent Minier is at Ubisoft, NOT Fareportal (Apollo task was misleading). Don't raise NY AG $2.6M settlement / Quebec class action unprompted (no case movement found 2025-26 per CLG/registry sweeps).

Full research: data/research/fareportal-2026-07-27.md (v8.0 refresh, supersedes 2026-07-23), data/research/onetravel-2026-07-27.md and data/stripe-sessions/facebook/thomas-spagnola-fareportal-2026-07-24.md in the repo. Related: [[reference-buyer-personas]]

## project_fc_barcelona
*FC Barcelona — licitación de sistemas de pagos pendiente desde nov-2025; Yuno homologado en portal de proveedores + NDA mutuo firmado (ene-2026); Àlex Castelló (Sistemes de Pagaments i Blockchain) y Arnau Alcaraz (compras) son los contactos; pliego pospuesto 3 veces; sin respuesta desde 17-jun-2026*  
*type: project · last updated 2026-09-25*

**FC Barcelona**, licitación de pagos del club. Origen: Arnau Alcaraz intentó agendar demo en la web de Yuno (nov-2025); Ángelo Da Silva (Commercial Growth Lead Europe) llevó la cuenta hasta el handover a German (13-may-2026, correo "Yuno//FC Barcelona - Angelo Handover"). Hilo principal: "Homologación Portal de proveedores del FC Barcelona" (Gmail thread 19ac075568fcb255). SFDC/Gong account 001Ps00001AYwJTIA1.

**Contactos:** Àlex Castelló, Sistemes de Pagaments i Blockchain, Àrea de tecnologia (+34 689818001) = dueño técnico del pliego, quien da los updates. Arnau Alcaraz Garcia-Barzanallana = compras/portal de proveedores y NDA (OOO agosto hasta el 20). Rosana Rivera (rol sin verificar, en cc desde jun-2026). Yuno en cc: Justo, Sonal.

**Estado:** Yuno homologado en el portal (categorías "Servicio de Asesoramiento IT" y "Consultorías"), NDA bilateral firmado por ambas partes (7-ene-2026), cuenta activa para recibir la RFP. **El pliego nunca se publicó.** Cronología de postergaciones: 10-feb Àlex "en una o dos semanas"; 4-mar "se espera a las elecciones del 15-mar, previsión abril"; 17-jun Àlex "a partir del 1-jul retomamos el debate con la nueva dirección" (Laporta reelegido). Follow-ups de German sin respuesta: 7-jul (propuso verse en España semana del 20-jul con Justo), 4-ago (auto-reply OOO de Arnau), 24-ago. Ángelo también ofreció in-person en Barcelona 19-21 ene sin respuesta.

**17-sep-2026:** ENVIADO 15:33 UTC (era borrador, salió el mismo día) en el hilo (reply al 24-ago) a Àlex + Arnau, cc Rosana/Justo/Sonal. Ángulo nuevo: la Asamblea única de socios de septiembre 2026 (cierre 2025-26 + presupuesto 2026-27 + financiación extra Camp Nou; anunciada 29-jul) como posible gate del pliego; pregunta directa si la licitación depende de ese presupuesto; ofrece resumen corto de novedades de producto para cuando armen el pliego; "en octubre podemos pasar por Barcelona" ⚠️ German no tiene viaje; Lucca Zadra (Yuno Europa) planeaba Barcelona 16-oct a 16-nov pero el 16-sep dijo que quizá cambia a Madrid (Slack #travel-requests), confirmar antes de enviar.

**Contexto útil:** Fever es el partner exclusivo de ticketing del club hasta jun-2030 (acuerdo ago-2024, incluye "múltiples métodos de pago"); no confundir el pliego de pagos con ticketing. Estilo de German en este hilo: cálido, referencia futbolera de apertura, "Un abrazo", trato de ustedes.

**25-sep-2026:** BORRADOR en Gmail (reply al 17-sep, mismo hilo 19ac075568fcb255, draft id r-8872438928794773465, el anterior r4931843187171109830 fue a la papelera) a Àlex + Arnau, cc Rosana + Justo. Es el "último push" suave: reconoce que la licitación no es prioridad ahora, German deja de insistir por ahora, quedan a disposición y piden aviso cuando retomen el pliego. Sin fútbol ni links; lleva P.D. felicitando por el cierre de la Asamblea del 19-sep-2026 (financiación de 510M EUR aprobada para terminar el Spotify Camp Nou, verificado en prensa). Pendiente de que German lo envíe. Si lo manda, siguiente toque solo si ellos escriben o en dic-2026.

## project_flair_contacts
*Flair Airlines buying committee + meeting context for Yuno orchestration pitch*  
*type: project · last updated 2026-10-06*

Flair Airlines (Canadian ULCC, flyflair.com) is an active Yuno orchestration prospect. First "Flair + Yuno" call was 2026-06-18 12:30 Bogota via Google Meet.

Buying committee:
- **Juliana Ramirez** (juliana.ramirez@flyflair.com) — VP Digital / Ancillary Revenue & Digital Experience. Champion + technical buyer. Owns flyflair.com checkout/booking, ancillary, Flair FWD. Mexican, native Spanish speaker (ex-Volaris, ex-OYO Mexico) → open rapport in Spanish. Runs 20-25 A/B tests/month. Quote: "ancillary is digital, digital is ancillaries"; publicly "expanding payment methods to smooth checkout."
- **Lucas Oordt-Bosman** (lucas.oordtbosman@flyflair.com) — Director, Payments and Digital Strategy. The actual payments decision owner. Ex-BBTV (creator payments), UBC International Economics. Vancouver-based, Dutch native, Spanish only elementary → do NOT open in Spanish with him; engage peer-to-peer in English. Public face of Flair Vacations launch (Jan 2026): "fewer steps and better value."

Key stack facts (UPDATED on 2026-07-03 discovery call w/ Juliana + Lucas + Abigail): Flair processes through THREE PSPs — **Elavon (live Nov 2024) + Nuvei (live Mar 2025) + Braintree/PayPal (live May 2025)** — PLUS **FlexPay** APM = 4 integrations to maintain. CORRECTION to prior memory: Flair DOES have its OWN in-house orchestration layer (Juliana: "we have our own property layer of orchestration... capability in house to build this layer") with basic smart-routing business rules → do NOT pitch "you lack an orchestrator" (NYT-style landmine). Retry/failover TODAY only exists inside Nuvei (resend without CVV); NO cross-processor failover → concrete gap. Reconciliation is MANUAL (downloads PDFs per dashboard). Their mandate (Juliana): lower distribution/processing cost, control/raise approval rate, smarter/more agile business rules, improve revenue integrity + chargebacks — but a big roadmap they can't build fast in-house = Yuno's opening (offload roadmap, faster TTM). Operate CA/US/MX. Volume ~4,000 trx/day upper-bound ("maybe less across channels"), ATV $200 USD. Deck live at deck.yuno.tools/m/flair-airlines.

Pricing quoted on call: min fee ~$10-12K/mo (fixed SaaS + variable per APPROVED trx, no separate min); makes sense >100K trx/mo. Follow-ups DELIVERED (Jun 18): deck + written quote = **$6K/mo fixed + $0.08 per approved trx, $12K/mo combined minimum**. KEY OBJECTION (Lucas, Jul 2 email): COST is the main sticking point — "we really like the product but the cost is a challenge... it's a build vs. buy situation and I'm trying to push us towards the buy." He asked for a call on fees / several fee-structure options. NEXT MEETING: technical+commercial deep-dive Tue Jul 7 2026 3:30pm EDT, German + Justo Benetti (CRO) + Jarrett Falasco (SE) vs Lucas + Juliana + Abigail; bring flexible pricing options + business case showing recovered revenue > fee. Abigail's real name/email = Abigail Wigle (abigail.wigle@flyflair.com), Juliana called herself Chief Digital Officer on the Jul 3 call. Full transcript saved at Flair/flair-call-transcript-2026-07-03.md; organized research summary at Flair/flair-research-summary.md. Business-case value-levers slide (Epic-structure) built at Flair/Business Case/flair-value-levers.{html,png}: base ~$9.24M/yr (conversion +$4.3-7.2M, retries +$2.2-3.6M, MDR +$0.22-0.36M, run-ops +$0.25-0.38M). See [[project_flair]] (FlightHub is a separate account).

Strongest hook: **Flair Vacations** (flights+hotels, live EN/FR/ES across US/MX/Caribbean, built with HBX Group + Onlinetravel) = fragmented multi-currency acquiring = orchestration sweet spot. CRITICAL open question: do Flair Vacations payments run through Flair's Elavon stack or through HBX/Onlinetravel?

Landmines: position Yuno as complement to Elavon (not rip-and-replace); never claim a payment method is "missing" (checkout not verifiable, 403); financial fragility (777 Partners exit/fraud, aircraft seizures, CRA arrears) is subtext not headline; CFO Sumanth Rao has pending legal matter — never mention. New CEO Len Corrado (Feb 2026), agenda = GDS listing 2026 + Flair Vacations + leisure packages.

Full research brief: ~/Documents/GERMAN CLAUDE CODE/GTMCoding/data/research/flair-airlines-2026-06-18.md

**Estado 24-sep-2026 (dicho por German):** Lucas dijo que de momento la propuesta no hace sentido, pero ha seguido revisándola. German le propuso **1 mes gratis para probar toda la plataforma** y está esperando respuesta de Lucas. Último correo en Gmail es del 25-ago (Lucas: "let me run some more numbers"); el intercambio reciente no está en el hilo, así que no citar fecha ni canal. Juliana Ramirez ya no está en Flair; Abigail Wigle sigue como contacto. Status en el tracker: Negotiation. Si Lucas no contesta, gancho = aprobación UK/Europa de Flair (23-sep).

**Estado 1-oct-2026 (chat de WhatsApp exportado en Deals/Flair/):** el canal con Lucas es WhatsApp. Objeción textual de Lucas: 10-sep "little to no savings from our current process, but it would allow us to make changes quicker"; 11-sep "we have the build already but it's more of a manual process to make changes... I'd love to make changes in an instant. We've done 90% of the rules, it's the last 10% I'm trying to capture" (él calculó el ahorro en $0.02 CAD por transacción); 14-sep "I don't think I can make it work... our current costs are basically null with our in house orchestration". German ofreció proyecto sin compromiso (15-sep) y 1 mes gratis (18-sep), sin respuesta. Nuevo ángulo 1-oct: mensaje corto pidiendo call de 20 min para entender el costo real de in-house (dev work, time to market, cost of management), sin volver a empujar precio.

**2-oct-2026 (dicho por German):** el 1-oct le escribió a Lucas por WhatsApp proponiendo sentarse a revisar si hay forma de hacer algo juntos. Esperando respuesta; no insistir antes de mediados de la semana del 5-oct.

**6-oct-2026 (WhatsApp, pegado por German):** Lucas cerró la puerta suave: "I've tried pitching the product, the cost is too high for us. Our breakeven is 0.02 CAD, at 0.06-0.08 I can't justify the cost. Sorry maybe in the future things change." Su internal pitch falló; compara el all-in de Yuno (~$0.08-0.10/trx en la propuesta de ago-26) contra el ahorro del "último 10% de reglas". Reply de WhatsApp REDACTADO (Deals/Flair/whatsapp-reply-lucas-2026-10-06.md): cómo deriva el costo (failover cross-PSP, approval rate, conciliación manual, dev time no están en su $0.02), qué le falta a su plataforma in-house (abre scope más estrecho sin cotizar), y una última call de 30 min para cerrar el loop, ofreciendo hablar con quien decide la aprobación. Sin precio nuevo. Si hay call y el scope se achica, Pricing Policy da margen (pay-ins min $0.01/tx, platform min $4K; mínimos nunca customer-facing).

## project_flighthub
*FlightHub (Montreal OTA) — Anna-Lena Schlenner contraparte; Nick Hart CFO; sin network tokens = hook; volúmenes REALES 3-sep (500-800K tx/mes, 80-92%, ~$800 CAD); presencial 22-sep HECHO (Will, todo es precio); deck final 24 slides $10K + tranches; respuestas Jarrett retries/disputes 22-sep; borrador post-presencial en Gmail pidiendo call 23-sep; ver bloques 22-sep*  
*type: project · last updated 2026-09-28*

FlightHub (flighthub.com, OTA de Montreal bajo FlightHub Group / Momentum Ventures; marca hermana JustFly). Relación desde ~dic-2025.

**Contactos (corregido 2026-08-31):**
- **Anna-Lena Schlenner — Product Manager, FlightHub.com & Justfly.com.** AHORA es la contraparte principal. Ella diseñó las specs del **orquestador interno** de FlightHub en Q2-2026, con implementación el trimestre siguiente. Respondió el 24-ago y agendó ella misma la call tras el silencio de Nick. Primera call con Yuno: **2-sep-2026**.
- **Nick Hart — Chief Financial Officer** (según su propia firma de correo, 27-jun-2026). ⚠️ La memoria vieja decía "Chief Corporate Development Officer + board director"; usar CFO. No respondió ninguno de los 5 follow-ups de German entre el 30-jun y el 24-ago.
- Hakan Ersoy (COO, tentative en la call de jun, no asistió). Billy Lim (accounting), Ezequiel Safirsztein.
- Lado Yuno: William Wong (lead en Canadá, Toronto, entró ~jun-2026, asignado a la visita presencial en Montreal que nunca ocurrió), Justo, Jarrett, Alejandro.

**Stack de pagos real, CONFIRMADO en el transcript completo de la call del 30-jun-2026 (boca de Nick, 7 proveedores ya live):**
- Pay-in: **Chase Paymentech, Stripe, Nuvei** (✅ confirmado dos veces por Nick, ya no es incierto), **Airwallex, Adyen** (✅ live desde ~30-jun, NO "en roadmap"), **Braintree** (subyace a PayPal, confirmado por Nick tras inspección del checkout de German).
- Pay-in y payout: **ConnectPay** (principal hoy en ambos lados).
- Payout: ConnectPay + agregando **Wex**, Adyen y Airwallex; **Float** en Canadá.
- Tarjetas virtuales ya en uso vía ConnectPay: toman la tarjeta del cliente, emiten virtual card y se la pasan a la aerolínea.
- Fraude: **modelo interno propio** + varios proveedores de data. **Riskified es solo "a backstop"**, no el sistema principal.
- Ticket promedio: rango **~$500-700 USD** (no un punto fijo de $700; el transcript limpio aclara "between five and 700").
- Ejemplos de reglas que Justo usó en vivo con Nick (reutilizables en la demo con Anna-Lena): metadata field de Uber para marcar VIPs; caso Amazon México (tarjetas US de expats ruteadas como domésticas vs internacionales, de ~4% a ~1.6-1.9% de interchange).
- ⚠️ El título de Nick es ambiguo: su firma de correo dice CFO, pero LinkedIn, Crunchbase Y el propio tag del grabado de la call dicen "Chief Corp Development Officer". Usar CFO al dirigirse a él, pero no sorprenderse si el equipo lo trata como corp dev.

**EL HOOK PRINCIPAL: no usan network tokens.** Nick textual: "we don't use tokens. we have the PAN and we have it encrypted right now." Son PCI DSS compliant. Es la palanca más concreta de approval rate + reducción de scope PCI, y es justo lo que un build interno de una sola empresa no puede armar solo.

**Matiz de BINs (importante, Justo lo malinterpretó en vivo):** cuando Nick habla de BINs se refiere a **las tarjetas virtuales que emiten para pagar a las aerolíneas**, no a BINs de emisor en el pay-in. "the more bins we have the better... the cards that we're passing to the airline having multiple bins." Wex se agrega en parte para ampliar ese pool de BINs.

**KPIs:** solo dos, acceptance rate y fees. Nick: "lower my cost and accept more." Dijo que con Adyen "no pain points". Cuenta poco dramática, muy numérica.

**Señal de compra del propio CFO:** "maybe Anna-Lena can get a walkthrough of your platform and see if it's something that maybe it's easier for us to just integrate with you guys."

**Datos económicos:** ticket promedio ~**USD 700**. Multiples entidades en varios países, procesan local para bajar tasas. ⚠️ **El volumen mensual de transacciones nunca lo dieron** (Nick empezó "between five and..." y se cortó, prometió mandarlo, nunca lo hizo). Ese número bloquea la propuesta de fees que Nick pidió el 30-jun.

**Compromisos de Yuno abiertos desde el 30-jun:** (1) estructura de fees detallada, bloqueada por el volumen; (2) sesión presencial en Montreal con William Wong.

**Contexto de settlement:** como agencia de viajes (no operador), la liquidación con aerolíneas va por **BSP (IATA) y ARC**, con GDS para reservas. Yuno orquesta el movimiento de dinero alrededor de eso, no el GDS.

**Material ya recibido por ellos:** Loom "Yuno | FlightHub" (oct-2025), Business Case "FlightHub + Yuno" (feb-2026). Nunca recibieron pricing.

**Research externo 2026-08-31 (no mencionar en la call):**
- Anna-Lena firma como Product Manager, pero un snippet de LinkedIn (página no cargó completa) la muestra como "Marketing Manager, Compare and Ads". Trasfondo confirmado: M.A. en Psicología/Neurociencia Conductual (Concordia, 2021), ex-Research Associate en UC San Diego, fuerte en Python/estadística. Tratarla como analista cuantitativa exigente con evidencia, no como ejecutiva de ventas.
- 🔴 **Nick Hart fue multado personalmente con CAD $400.000** en el consent agreement de la Competition Bureau de feb-2021 por drip pricing (total compañía + directores $5.8M, 10 años de prohibición hasta 2031). Nunca mencionar. También hubo demanda de California AG (sep-2019) y consent order del DOT ($300k, feb-2022). Todo esto explica una cultura cost-conscious y cautelosa con disclosures, no relevante para la conversación de pagos.
- FlightHub tuvo **CCAA (bancarrota protegida) en 2020**: caída de ingresos >90%, ~108 despidos, plan aceptado 100% por acreedores, terminado may-2021.
- **Hook nuevo y muy concreto:** los Términos de Servicio de FlightHub (§15) dicen textualmente que "multiple charges may appear on your credit card... may be charged by more than one party" — confirman modelo split-tender/multi-MID en su propia letra legal, lo cual es exactamente el problema de reconciliación que Yuno resuelve.
- Estructura legal: padre Momentum Ventures; entidades Flighthub Group Inc., Flighthub Service Inc., SSFP Corp., Justfly Inc. (PEI), Justfly Corp. (Delaware), 11644670 Canada Inc. (entidad québécoise).
- Evidencia pública adicional del stack: Affirm CA (may-2024, min $200 CAD), Accrue Pay-by-Bank en justfly.com (ago-2024, explícitamente para bajar fees de tarjeta), Riskified case study (+30% approval, -80% manual reviews, -75% tiempo de revisión de chargebacks). Braintree/Adyen no tienen evidencia pública (normal, nunca se publicita esa relación).
- Dos vacantes de pagos distintas publicadas (Payment Manager + Product Manager Payments) más 2 Fraud Analyst — refuerza que el build interno está siendo staffeado en serio, no es un side project.
- ⚠️ CEO no está claro: sitio corporativo + Forbes jun-2026 dicen Henri Chelhot; un perfil viejo de Forbes Business Council dice Christopher Cave.

Brief de la call del 2-sep: `data/research/flighthub-meeting-brief-2026-09-02.md`. Doc: https://docs.google.com/document/d/111-z3VVEboFyuy9-C5ZXBd3DERv8JDoqyX2055B6y_M/edit

**Call del 2-sep-2026 (demo, 27 min, transcript completo disponible):** asistieron German + Jarrett (SE) por Yuno, y Anna-Lena sola por FlightHub. **Nick no asistió** (confirmado, no solo "optional sin responder"). ⚠️ El header del transcript de esta call lista a Anna-Lena como **"Marketing Manager"** (no "Product Manager"), lo cual corrobora el snippet de LinkedIn que ya había levantado la duda el 31-ago. Igual sigue siendo la contraparte técnica real, la que pregunta por modelos ML de ruteo y pide el cost estimate.

- **Anna-Lena solo lleva en su posición desde enero-2026.** El sistema de reglas de ruteo en acquiring ya existía antes de ella ("ha estado ahí por un par de años... es de antes del boom de IA"); ella no lo construyó desde cero, lo heredó y ahora lo está evolucionando. En el lado de **issuing** (payout a aerolíneas) están construyendo algo nuevo: un "BIN/issuer rotation engine" que selecciona inteligentemente el issuer y posiblemente el BIN según inputs como aerolínea y oficina usada.
- **Nuevo detalle de stack: ConnectPay hace acquiring E issuing** (no solo payout como se pensaba). Confirmado por Anna-Lena en vivo.
- Jarrett hizo la demo completa del dashboard: connections library, no-code routing config, condition sets (issuing country, card brand, metadata custom field, etc.), smart routing por conversion rate/latency (ML interno, alimentado por data cross-portfolio, no solo de FlightHub), feature nueva "routing recommendation" (sugiere el mejor route y se puede confirmar por chat), vaulting/token vault propio, Payments Concierge (asistente IA conversacional que sugiere cambios de ruteo y los aplica si se lo confirmas). Explicó que las conexiones nuevas se levantan en 1-2 días una vez hay credenciales, integración completa con QA en 3-5 días.
- Precio: confirmó que solo cobran sobre **transacciones exitosas** (fee fijo de plataforma + fee variable por transacción exitosa), cero costo por declines.
- **Anna-Lena mostró interés real:** preguntó específicamente si Yuno ya tiene modelos que predicen qué BIN tiene mejor chance de aprobación en qué processor, y dijo textual que prefiere confiar en ML/AI para la decisión de ruteo en vez de reglas manuales. Buena señal de fit con el pitch de smart routing.

**Next steps acordados en vivo (2-sep):**
1. German le manda un correo con lo que necesita para el cost estimate: **volumen de transacciones (en cantidad de transacciones, NO en dólares, confirmado por ella)**, approval rate actual, ticket promedio.
2. Se propuso workshop presencial en Montreal con **William Wong** (Head of Account Management, Toronto) — mencionado en vivo como posible "la semana después de la próxima" (~semana del 14 al 18-sep-2026). Jarrett mencionó que Yuno ya tiene otra reunión en Montreal en un par de semanas, así que el timing podría alinearse.
3. **Compromiso de fees del 30-jun sigue abierto pero ahora desbloqueándose:** Anna-Lena se comprometió a conseguir el volumen ("I can get that one that I have").

**Propuesta comercial (3-sep-2026, en construcción vía Claude Design):**
- Deck live en Drive: "Proposal - FlightHub + Yuno" (Google Slides, ~20 slides, Why Yuno? + Proposal). Ojo: hubo un leftover "CPD" (CellPoint) en el título de un slide; el prompt de BC incluye el fix.
- Pricing (Deal Calculator "Yuno — Pricing FlightHub", tab Deal Calculator): **platform fee $10.000/mes + pay-ins en ladder de 3 tiers**: 0-175K a $0.0333, 175.001-350K a $0.0292, 350.001-700K+ a $0.0260 (blended ~$0.0286 a 700K = ~$20K/mes). Sin MMG en la propuesta (el sheet muestra $5K en pay-ins pero el resumen dice "No MMG set"). Reconciliations, 3DS y Network Tokens van como "Pending scoping", sin precio, porque no se han hablado.
- **⚠️ Los volúmenes son estimados de German, NO de FlightHub**: 700K trx/mes y $580 ATV (dentro del rango $500-700 de Nick). TPV estimado $406M/mes = $4.87B/año, por encima del "$3B+ in sales" público del grupo. Recalibrar todo cuando Anna-Lena mande los reales.
- Business Case (2 slides estilo Flair, valores a nivel NET revenue con benchmark 15% de take OTA del calculator; cost levers a valor pleno): L1 conversion +1.5-2.5%, L2 retries +0.75-1.25%, L3 costo 7.5-12.5 bps, L4 run-ops 4-5 FTE a ~$100K. Totales anuales: Conservative $20.60M / Average $27.25M / Optimistic $34.00M.
- Prompts guardados en `Deals/FlightHub/`: claude-design-prompt-pricing-proposal-2026-09-03.md y claude-design-prompt-business-case-slides-2026-09-03.md.

**⚠️ 14-sep-2026: el correo post-demo pidiendo volúmenes NUNCA SE ENVIÓ** (último correo a Anna-Lena: 3-ago). Borrador creado el 14-sep como reply al hilo "FlightHub + Yuno | Next Steps" (a Anna-Lena, cc Nick, William, Justo, Jarrett) pidiendo tx/mes en cantidad, approval rate total y por proveedor, ticket promedio y mix por proveedor, con agenda propuesta para el 22; pendiente de envío. Anna-Lena agendó **"Yuno x Flighthub - In-Person" el martes 22-sep-2026, 10:00 a 11:00 COT, en 3333 Boulevard Côte-Vertu Ouest, Suite 600, Saint-Laurent, QC (sala SR-71)**; Nick invitado (sin responder), William aceptó, Justo opcional, German figura como opcional en la invitación de ella. Decisión pendiente: si German viaja o va William + Jarrett. El deck de propuesta sigue sobre volúmenes estimados (700K tx, $580); recalibrar cuando lleguen los reales. Prep (slides, demo, info a extraer): Deals/weekly-prep-2026-09-14.md sección 4.


**⚠️ CORRECCIÓN 21-sep-2026 (verificado leyendo los 28 mensajes del hilo "Next Steps"): las entradas de arriba del 3-sep y 14-sep están MAL en dos puntos.**
1. El correo post-demo SÍ se envió el 2-sep, y **Anna-Lena respondió el 3-sep con datos REALES**: 500-800K tx/mes según estacionalidad, success rate 80-92% "depending on how you calculate it", ticket promedio de sale transactions ~$800 CAD (todos los procesadores y monedas). Los 700K / $580 / 86% del deck salen de ahí, NO son inventados por German. Duda abierta: ella dio el ticket para "sale transactions", así que el conteo puede incluir otros tipos de transacción (incluso issuing vía ConnexPay).
2. El deck vivo (Slides 1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI, modificado 4-sep) cotiza **$10K platform + $0.06 / $0.05 / $0.04 + mínimo mensual $25K + 3 años** = $39.330/mes ($471.960/año, $0.065 all-in a 602K exitosas). NT va INCLUIDO; pendientes sin precio: Nova AI, reconciliation, monitors. El ladder $0.0333/$0.0292/$0.0260 es solo lo que sugiere el Deal Calculator; German subió precios tras feedback de Sean (3-sep: ticket $580 aguanta más por tx; normalmente platform fee O mínimo, no ambos). BC vivo: $26.00M / $34.65M / $43.10M. El PDF en `Deals/FlightHub/` es un export VIEJO (título "CPD", NT pendiente, slide de compliance bancario).
- El presencial se movió del 18 al 22-sep A PEDIDO de German para que Nick pudiera asistir; Nick sigue sin responder la invitación. Anna-Lena espera revisar la propuesta ahí ("looking forward to meeting William and discussing the proposal"). Jarrett NO está en la invitación.
- La capa de ruteo de FlightHub YA está live (hace un par de años, cascada por reglas); el objetivo de Anna-Lena es "improve it significantly". El proveedor se llama **ConnexPay** (en transcripts sale "Connect Pay"); Jarrett quedó debiendo confirmar cobertura de payouts, nunca se respondió.
- Riesgo del BC: benchmark 15% net take probablemente alto para OTA aérea; a 5% el caso sigue dando ~$15M/año.
- Briefing completo para Will: `Deals/FlightHub/flighthub-will-wong-briefing-2026-09-21.md` + Google Doc https://docs.google.com/document/d/1yjPj7lFz8axm_ZWS22Z1P6mCJQ7cwvpMWlOQUZ5yVNQ/edit (privado, sin compartir).

**18-sep-2026:** NO existe ningún borrador de correo de volúmenes en Gmail (revisado); si se quiere pedir volúmenes reales antes del 22-sep hay que escribirlo desde cero. Reunión 22-sep 10:00 COT / 11:00 Montreal, William confirmado, Justo opcional sin responder, Nick Hart sin responder. German viaja a San Francisco el 28-sep (ver [[project-sf-relocation-fall-2026]]).

**22-sep-2026, presencial HECHO en Montreal (Will Wong con Nick y Anna-Lena; notas de Will pasadas por German, inicio del mensaje recortado, el "ck" es Nick):** call positiva, amigable. Repasaron routing y lo encontraron "super simple"; preguntaron por A/B testing de rutas. Preguntas abiertas que Will quedó debiendo: (1) chargeback y dispute management: ¿existe en el portal, se puede orquestar, cómo funciona, vía API? Ellos ya tienen proveedor de chargebacks. (2) Retries: preguntaron por instant retries y por la posibilidad de configurar un delay en el retry de una ruta: VALIDAR con SE. (3) Nunca se han caído; con Yuno seríamos single point of failure: ofrecer sesión con alguien de Yuno sobre uptime y manejo de fallas. Sin preguntas de integraciones adicionales; monitors les gustó dentro del routing; Nova AI mencionado y no les interesó; al ver el dashboard hablaron de payment links; pocas preguntas de reconciliación. Ambos esperan la propuesta de German. Lectura de Will: es todo precio y el trade-off build interno vs orquestador.

**Pricing v2 (decisión de German 22-sep, para rehacer la slide 16 en Claude Design; prompt en `Deals/FlightHub/claude-design-prompt-pricing-v2-2026-09-22.md`):** platform fee $9,000/mes (era $10K) + $0.055 / $0.05 / $0.04 (mismos cortes 175K / 350K); monitors y PCI token vault pasan a Included; network tokens como add-on $0.005 por token creado + $0.01 por update; reconciliation $1,500/mes con 200,000 tx conciliadas incluidas y luego $0.032 (la referencia "lo mismo que ayer" = Appmaking, que fue $0.032, no 3.6 centavos); Nova AI único pending; mínimo $25K y 3 años se mantienen. A 602K exitosas: $37,455/mes, $449,460/año, $0.062 all-in (antes $39,330); low 430K $30,575; peak 688K $40,895; el mínimo aplica bajo 302,500 (antes 265,000). Add-ons fuera de esos totales. ⚠️ Zona roja según Pricing Policy: NT muy por debajo del mínimo $0.20/$0.04 (y creación más barata que update, al revés de la lista); recon 200K por $1,500 está por debajo del pack 250K ($5,000). A 602K conciliadas la recon sale ~$14.4K/mes (el pack 1M de la policy es $14,000 plano). Deck vivo sigue en Slides 1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI (slide 16 = pricing; slides 13 y 14 del BC aún traen el text box suelto "$ 0.71").
- **Add-on extra pedido por German 22-sep: chargeback alerts + fraud alerts.** En la Pricing Policy (Doc releído en vivo 22-sep) es UN solo producto, "Chargeback Alerts" (Ethoca + Verifi, grupo Protection): list $15 / mínimo interno $9.80 por alerta MATCHED, unmatched no factura, siempre standalone, sin fee mensual, billing mensual in arrears, levers flat/tiers/tranches por rango de alertas, sin splitting ni credits. No existe un producto "fraud alerts" aparte (0 menciones en el Doc); los fraud alerts de Ethoca van dentro de ese mismo producto. Recomendado y puesto en el prompt: $15 por alerta matched (list, zona verde; Appmaking fue $14). Los otros candidatos de la policy (Fraud Engine $0.03/screening, Risk conditions $0.02/tx) NO aplican: FlightHub tiene modelo de fraude propio + Riskified.
- Preguntas para Jarrett (en inglés, solo lo que Will marcó como "validate": scheduled/delayed retries + chargeback/dispute orchestration y alerts) en `Deals/FlightHub/flighthub-internal-validation-questions-2026-09-22.md`. A/B de rutas y payment links NO se validan, ya se saben.

**DECK FINAL (22-sep-2026, revisado slide por slide en PDF exportado, 24 slides):** estructura Why Yuno (1-11) · Business Case (12-14, sin cambios: $26.00M / $34.65M / $43.10M) · Proposal (15-16) · Build vs Buy (17-19, NUEVO) · Appendix (20-24). **Pricing final en la slide 16 (German la rehizo en Claude Design, NO siguió el prompt v2 al pie):** platform fee $10,000/mes flat + tranches incrementales de 200K: $0.06 (0-200K) / $0.04 (200,001-400K) / $0.03 (400,001-600K) / $0.02 (600,001-800K) / $0.015 (>800K); mínimo mensual $20,000 (deja de aplicar sobre 166,700 tx); 3 años, rates locked, tiers revisados anualmente. Incluido: orquestación y rules engine, smart routing y retries, monitors y auto-failover, PCI token vault, dashboard, KAM+TAM. Add-ons puro uso: network tokens $0.05 creado + $0.01 update (eligió $0.05, no $0.005), reconciliation $1,500/mes incl. 200,000 tx conciliadas y luego $0.032, chargeback & fraud alerts $15 por alerta matched (Ethoca + Verifi), Nova AI pending review. Ilustración a 700,000 tx EXITOSAS/mes: $28,000 tx + $10,000 = $38,000/mes, $456,000/año, $0.054 all-in; low 500K $33,000; peak 800K $40,000. Toda la aritmética verificada. ⚠️ Zona roja policy: NT bajo mínimo $0.20/$0.04; recon 200K por $1,500 bajo pack 250K ($5,000). Ojo de consistencia: el BC usa 700K como INTENTOS (86% = 602K aprobadas) y la slide de pricing usa 700K como EXITOSAS; a 602K la factura sería $36,040/mes. El text box "$ 0.71" de las slides 13/14 NO se ve en el export (elemento fuera de canvas), no bloquea.
- **Headcount del equipo de orquestación interno: NO existe el dato en ninguna fuente** (revisado 22-sep: transcripts 30-jun Nick, 30-jun alignment interno, 2-sep Anna-Lena, Gong 2 calls + 21 emails, notas de Will 22-sep). Lo único dicho: Nick, "not a team but a person" hace la reconciliación; Anna-Lena "in charge of payments" escribió las specs de la plataforma (Q2-2026); ella dice que las integraciones "are done within a month usually, we are fast" y que Adyen (asíncrono) exigió "a bunch of workarounds"; Jarrett mencionó "your engineers" sin número. Público: 2 vacantes de pagos (Payment Manager + PM Payments) + 2 Fraud Analyst. Los "4 to 5 FTE" del deck son estimación nuestra, no dato de ellos. Pregunta 8 del briefing (tiempo de ingeniería en mantener las 7 integraciones) sigue sin respuesta.

**22-sep-2026, tarde. Respuestas de Jarrett (Slack) a las dos preguntas de Will:** (1) retries con delay: NO hay delay configurable en la lógica de failover hoy; el retry completo (create payment) ya lo controla el merchant, así que pueden meter la lógica de retry que quieran de su lado, con latencia y UX como único trade-off; Jarrett quiere entender el caso de uso concreto. (2) disputes/chargebacks: "yes" pero admite que la respuesta real es más matizada; alinear con Martin quién es owner de disputes en producto para capacidades actuales vs roadmap. Decisión de German 22-sep: al cliente ambas cosas van como un "sí" claro (delayed retries disponibles porque ellos controlan el create payment; disputes disponible en dashboard y API), sin mencionar que el failover no tiene delay configurable; los detalles los da Will.
- **Borrador de correo post-presencial CREADO en Gmail** (reply al hilo "Next Steps", a Anna-Lena + Nick, cc Will/Justo/Jarrett): feedback positivo de Will, las dos respuestas en tono soft, Will da seguimiento, propuesta lista y pedido de 30 min el 23-sep. Copia en `Deals/FlightHub/flighthub-email-post-inperson-2026-09-22.md`. Pendiente de que German lo envíe. Fuera del correo: la sesión de uptime/SPOF que Will ofreció, aún sin agendar.

- **22-sep, bloqueantes del deck APLICADOS en el Slides vivo** (service account, ver [[project-slides-api-token-dead]]): slide 16 "Network tokens" (ya no "Network and security tokens"), slide 13 palanca 2 "Routing & retries", slide 19 Assumptions reconciliada con L4 ($0.4M a $0.5M + infra/PCI/tooling) y caja estrechada al margen. German subió Tier 5 a $0.018. Pendientes recomendados (no bloqueantes): "$15 p|er" bold, coma ",TPV,", "4–5 FTE", 450+ vs 460+, "(est.)" en 12 a 18 meses. Deck compartido como Editor con la service account.
- **Respuestas de Jarrett (Slack 22-sep 12:39):** (1) delayed retry: NO hay delay configurable en el failover hoy; el failover es instantáneo; un retry con espera lo hace FlightHub desde su lado con otra llamada de create payment (solo latencia/UX como límite); Jarrett quiere saber qué buscan lograr antes de responder mejor. (2) orquestar chargebacks/disputas: "yes" con guiño ("I could give you the real answer but I'd get in trouble"): capacidad parcial/roadmap, confirmar con Martin Mexia (SVP Product) quién es owner de disputes y qué está live vs roadmap antes de prometer. Mensaje seguro a FlightHub: visibilidad y alertas hoy, gestión completa a validar. Guardado en Deals/FlightHub/flighthub-internal-validation-questions-2026-09-22.md.
- **23-sep-2026: call "FlightHub + Yuno | Proposal" 10:00 a 10:30 COT (Meet)**, German presenta el deck final; Anna-Lena y Sean Calabro aceptaron, Nick y Will sin responder. Guía de coaching (levers con matemática y defensa, sensibilidad, pricing, build vs buy, objeciones, run of show, agenda + 11 preguntas): Google Doc 1gnvVu5ZayyuG_rNCpdPr6kpdS_fdd_I_DozjyIR7Xe4 + resumen en Deals/FlightHub/flighthub-proposal-call-guide-2026-09-23.md. Reglas para la sala: cero negociación de precio (recoger reacciones), decir antes que ellos que 15% take, 4 a 5 FTE y 12 a 18 meses son supuestos nuestros, no cifras de uptime improvisadas, no stats del apéndice.

**23-sep-2026, call "FlightHub + Yuno | Proposal" (22 min, Gong; Anna-Lena sola, Nick NO vino; Sean y Joaquin Mann presentes):** ella lleva todo a Nick y "run some numbers". Pidió (1) tiers por bucket, no tranches: al alcanzar un tier la tarifa aplica a TODO el volumen ("that's what we usually have with any other provider"); (2) fee fija lo más baja posible o inexistente: "a fixed monthly bill of 10,000 is a huge impact", el mínimo de $20K "pretty steep"; margen de la industria extremadamente bajo. Alternativa = build in-house: "the integrations are not the pain point anymore... the one thing that was interesting is the smart routing for acquiring"; no han dimensionado el costo del build, la comparación les sirve. Equipo real: 1.5 personas integración, mantenimiento ella, recon = accounting (NetSuite, "fairly manual"). NT opcionales (pueden seguir con PAN); alertas solo si las usan. Corto plazo 7 procesadores; entidad australiana nueva. "Number that makes sense: as little as possible".
**Pricing v3 (decisión de German post call, borrador de correo listo):** platform fee $10K se mantiene; SIN mínimo mensual; tiers por bucket $0.08/$0.06/$0.04/$0.035/$0.03 (buckets de 200K, 800K+ al 3¢; ladder propuesto por Claude a partir de las opciones "8,6,4 / 7,5,3" de German, confirmar); recon plana $7,500/mes; NT y alertas igual, opcionales; 3 años "happy to discuss". Resultado: 500K $30,000 (-9%), 700K $34,500 (-9%), 800K $34,000 (-15%); año a 700K $414,000 vs $456,000; año estacional -10%. Quirk cliff: 600,000 paga $34,000 y 600,001 $31,000. Policy: recon $7,500 está en el piso a 700K y bajo el piso a 800K ($8,300); NT sigue en rojo. Notas: Deals/FlightHub/flighthub-pricing-v3-2026-09-23.md. Correo: borrador Gmail r-5103156988531742640 (v2 sin tablas: German pidió quitar tiers y tabla de costos del correo, van en el deck; abre con 'good call' y 'keep the conversation going') en el hilo Next Steps (reply a 1a0cb09592e982b5; to Anna-Lena + Nick, cc Sean/William/Justo/Jarrett), copia en Deals/FlightHub/flighthub-followup-email-proposal-v3-2026-09-23.md. ⚠️ Antes de enviar: actualizar slide 16 del deck a v3 y adjuntar PDF. German ya les escribió el 22-sep que chargeback/dispute management existe "in the dashboard and via API" y que William hace follow-up de retries y chargebacks.

**28-sep-2026 (verificado en Gmail):** el correo con la propuesta v3 SÍ se ENVIÓ el 23-sep 16:51 UTC (mensaje 1a0cf2d8201d71e0, to Anna-Lena + Nick, cc Sean/William/Justo/Jarrett, con link al deck). Sin respuesta de FlightHub desde entonces. German pidió un FUP corto: estamos pendientes de que revisen la propuesta para repasarla juntos. Borrador vigente en Gmail r-3559356975700857226 (v2; reply a 1a0cf2d8201d71e0, mismos destinatarios), copia en `Deals/FlightHub/flighthub-followup-email-checkin-2026-09-28.md`. Pendiente de que German lo envíe. Tono: "Hi Anna-Lena, Nick", cálido, sin pricing ni links, ofrece call corta esta semana. A German NO le gustó "We are standing by on our side... run your numbers" (v1 borrado); quedó pregunta directa: "Have you had a chance to look at it? I would love to go through it together and hear your thoughts."

## gamma-deck
*Gamma (never \"Gamma AI\", slug gamma-ai) deck fix 2026-09-09 — Stripe sole PSP (public case study), never rip-and-replace framing; India 10.8% largest market, Gamma reported 22% revenue lift from UPI; OpenAI logo on proof wall*  
*type: project · last updated 2026-09-09*

Gamma deck (slug `gamma-ai`, name now "Gamma" — "Gamma AI" is two unrelated entities, gamma.ai and gamma.com.ai; merchantName override in slide-overrides.json). Fix pass 2026-09-09:

- Stack: **Stripe sole PSP** (Payments, Checkout, Billing, Invoicing, Link, Adaptive Pricing) — public Stripe case study stripe.com/customers/gamma + checkout observed at billing.gamma.app. 43% of transactions ride Stripe Link alone. Never claim "no PSPs disclosed" and never rip-and-replace framing (kills the entry angle); CTA closes "One layer above your current stack, not a replacement for it".
- Traffic: **India 10.8% is the single largest market; LatAm 17.3% ≈ 3x the US (5.81%)**. Only legal entity is US → everything processes cross-border. BRL pricing observed at R$70/month (localized price, cross-border rail); 9 currencies confirmed by Stripe.
- India argument: **Gamma publicly reported a 22% revenue lift from adding UPI** — use their own number; the pitch gap is UPI Autopay for recurring.
- APM chips: Brazil first (Pix, Pix Automático, Parcelado, Elo, Boleto — Brazil observed at live checkout), UPI Autopay · India, SPEI · Mexico, PSE/Nequi · Colombia, QRIS · Indonesia, MoMo · Vietnam. No GCash/M-Pesa/BLIK/iDEAL/Bancontact/GrabPay (off top-14 markets).
- Capabilities: subscriptions LIVE; tokenization + fraud "Unverified" (amber assumed state); IAP missing with source (help.gamma.app: "In-app purchases are not supported in v1"); Payouts/KYC-KYB/BaaS/Tax removed (off ICP).
- Trusted By: gamma-ai swaps NetEase Games → **OpenAI** (approved client, AI-native proof). ⚠️ Confirm internally before sending: Ant Group, Crypto.com, Kraken, Zuora logos.
- Cover shows "gamma.app" under the lockup (cover `companyDomain` override slot). Impact tiles: published 7% / 30% per [[published-stats-only]].

## project-gcloud-cli
*Google Cloud CLI instalada en la Mac de German (22-sep-2026) con Python 3.12 vía uv; proyecto GCP gtm-claude-tools-260922 en su Gmail personal para las integraciones de Sheets/Slides/Docs*  
*type: project · last updated 2026-09-22*

Instalado 22-sep-2026 sin sudo: `~/google-cloud-sdk` (gcloud 586) + Python 3.12 vía uv en `~/.local/share/uv/python/cpython-3.12-macos-aarch64-none/bin/python3.12` (el Python del sistema es 3.9 y gcloud no arranca con él). `~/.zshrc` exporta CLOUDSDK_PYTHON y el PATH; en Bash no interactivo hay que exportar CLOUDSDK_PYTHON a mano antes de llamar `~/google-cloud-sdk/bin/gcloud`.

Cuentas autenticadas en gcloud: german.tatis@y.uno (NO puede crear proyectos: "No permission to create project in organization") y german.tatism@gmail.com (activa; aceptó los ToS de Cloud el 22-sep). Login sin navegador local: `tail -f code.txt | gcloud auth login --no-launch-browser` en background, German abre la URL y pega el código en el chat, se escribe al archivo.

Proyecto: **gtm-claude-tools-260922** ("GTM Claude Tools"), dueño german.tatism@gmail.com, APIs habilitadas: sheets, slides, docs, drive. Pendiente en consola (no hay API para esto): consent screen External + test user german.tatis@y.uno + Publish, y OAuth client tipo Desktop → JSON → `tools/gsuite/auth_gsuite.py`. Helper de escritura: `tools/gsuite/gsuite.py` (sheets meta/read/append/update, slides get/batch, docs get/batch) con `~/.config/gsuite/token.json`.

**Why:** German quiere que Claude edite toda su suite de Google (Sheets, Slides, Docs) desde la máquina; los clientes OAuth anteriores murieron al borrarse sus proyectos GCP. El proyecto vive en el Gmail personal solo como contenedor; el acceso a datos lo da la cuenta y.uno al autorizar.

**How to apply:** ver [[project_gsheets_mcp]] para el estado del acceso a Sheets y [[project-slides-api-token-dead]] para Slides. Enlaces directos de consola: /auth/overview, /auth/audience, /auth/clients/create con ?project=gtm-claude-tools-260922.

## project-genspark
*Genspark AI (MainFunc) — Winnie Wei (Head of Finance) único contacto; Stripe único; RESPONDIÓ 5-oct: esta semana no (SF Tech Week), equipo volcado en implementar NetSuite; respuesta de German en borrador proponiendo presencial semana del 26-oct*  
*type: project · last updated 2026-10-05*

**Genspark AI** (MainFunc Inc.). Contacto: **Winnie Wei** (winnie@mainfunc.ai; **Head of Finance**, confirmado por su firma del 5-oct-2026; escribe desde GenMail, el correo de Genspark). **German NO la conoce en persona** (corrección suya, 2-oct-2026): en Stripe Sessions (29-abr-2026) quien la conoció fue Justo; German estaba con Justo en el evento. El correo de German del 29-abr ("Great meeting you", "the deck we reviewed together") fue el follow-up estándar del evento, no prueba de que se hayan visto. En correos: "I was with Justo at Stripe Sessions when the two of you met". Deck: ss26.yuno.tools/m/genspark-ai.

**Cronología:**
- 14-may-2026, Winnie a Magdalena: "we don't have bandwidth to switch to another payment platform right now since the engineering team has a lot of competing priorities. We will reach out once we are ready." Es su único correo de fondo; la objeción real es esfuerzo de ingeniería y la palabra "switch".
- 28-jul: Magdalena reabre con business case (Stripe único sin fallback, Japón y Corea como mercados top sin métodos locales, renovaciones fallidas). Hilo "Genspark x Yuno, picking up where we left off" (thread 19faa80b48668977), cc Justo y German. Sin respuesta.
- 29-sep: Magdalena, mismo hilo: German y Justo en SF hasta inicios de noviembre, café presencial, subscription engine con retry por segundo proveedor. Sin respuesta.
- **2-oct: FUP de German ENVIADO** (reply al correo de Magdalena del 29-sep, cc Magdalena, Justo y Sean; message id 1a0fd723bc595d3c). Tesis: no hay que cambiar de plataforma, Stripe se queda y Yuno va encima; dos beneficios (renovación fallida reintentada por segundo proveedor, métodos locales en Japón y Corea); proof point inDrive 90% en 10 mercados; propone café presencial con German y Sean Calabro el jueves 8-oct o miércoles 14-oct temprano en la tarde (ambos calendarios libres 12:00 a 15:00 PT); promete llevar un one-pager de lo que un primer paso le costaría a su equipo de ingeniería. Sin respuesta al 5-oct.
- **5-oct: FUP #2 ENVIADO** (reply al correo de German del 2-oct, mismo hilo, mismos cc; German ajustó el texto y adjuntó la foto). Gancho: German vio la publicidad de Genspark por toda la estación de Caltrain y adjunta una foto (la foto la pega German a mano, no estaba en el Mac). Tesis: una campaña así implica otra escala que la de mayo, y ahí los dos puntos (renovaciones fallidas en Stripe sin reintento, métodos locales en Japón y Corea) se vuelven dinero real. Propone verse en persona jueves 8 o viernes 9-oct por la tarde, "happy to come to you".
- **5-oct (misma tarde): WINNIE RESPONDIÓ** (solo a German, cc Magdalena, Justo y Sean; message id 1a10dfc5dae47e81): "This week is a little bit challenging for me since it is SF tech week, maybe we connect at a later time? (we are in the process of implementing Netsuite, so my team is swamped in the implementation right now)". Primera respuesta suya desde mayo. La objeción ya no es "switch" sino ancho de banda del equipo de Finance por NetSuite.
- **5-oct: respuesta de German = BORRADOR en Gmail v2** (reply a Winnie, mismos cc). German rechazó la v1 ("Let's pick this up once the dust settles... week of October 26th") por sonar a robot de IA. v2 en tono humano: "Oh wow, a NetSuite implementation on top of Tech Week. I can only imagine the whole team heads down on that right now", café en las próximas dos semanas "whenever you can breathe for half an hour", nada que preparar, tema = prioridades una vez NetSuite esté en vivo + un par de ideas, Sean y German en SF hasta inicios de noviembre y van a donde ella; si de verdad hay que esperar al fin de la implementación, "just say the word". Calendario de referencia: semana del 26-oct ambos con tardes libres salvo Arrive jue 29 13:00 PT (German).

**Datos para no equivocarse:**
- Winnie es Finance, no ingeniería: hablarle de prioridades, costo y conciliación, no de integración. NetSuite en implementación (oct-2026) = posible ángulo de datos de pagos hacia el ERP más adelante, no forzarlo ahora.
- Stripe = único procesador (política de privacidad de Genspark). Japón y Corea son los dos mercados de mayor tráfico; los porcentajes difieren entre los dos research locales (25%/25% vs 19%/13%), así que no citar cifras.
- "Nuestro GM de North America" = **Sean Calabro** (ver [[sean-calabro-manager]]). En Slack su título es "VP of Sales Americas"; en el correo va como "who leads North America for Yuno". Está en San Francisco (zona horaria PT, eventos en SF en su calendario). No estaba en cc del hilo al 2-oct.
- La campaña fría de German de mar-abr 2026 a ~10 personas de Genspark terminó con Breno Melo pidiendo que lo sacaran de la secuencia; no reactivar esa lista.

Research: data/research/genspark-ai-2026-03-25.md y Events/Research/Genspark AI/genspark-ai-stripe-sessions-research.md. Relacionado: [[project-sf-relocation-fall-2026]], [[feedback-cc-handoff-reply-pattern]].

## project-godaddy
*GoDaddy — Sunil Joshi (Director PM Payments, SF) respondió a la campaña BC de Magdalena; café presencial en SF por agendar*  
*type: project · last updated 2026-10-05*

Magdalena Torrealba corrió una campaña "The BC around GoDaddy's Payment Stack" (30-sep-2026, ~12 contactos) presentando a German. El 1-oct respondió **Sunil Joshi** (linkedin.com/in/joshisunil), Director of Product Management / Payments, basado en SF: quiere conocer al equipo mientras estén en la ciudad.

Sean Calabro pidió café con él el lunes 5 o martes 6-oct. Magdalena respondió el 1-oct ofreciendo opciones; al 2-oct sin confirmación. German ya lo tiene en LinkedIn y puede darle un toque el 2-oct, o Magda hace FUP el lunes 5.

**Why:** primera respuesta real de la campaña y reunión presencial durante la estadía en SF ([[project_sf_relocation_fall_2026]]).

**How to apply:** coordinar por el group DM German + Magdalena + Sean; preparar brief de Sunil y repasar el deck del BC antes del café. Ver [[project_magdalena_bc_campaigns_sep_2026]].

**5-oct-2026 (LinkedIn, chat grupal "Yuno + GoDaddy - SF" con Sunil y Magdalena):** German propuso verse esta semana para oír prioridades Q4 de GoDaddy. Sunil (9:31 AM) preguntó si German estará en el Visa Enabler Summit del miércoles 7-oct. German NO va. Respuesta preparada: no vamos al summit, pero seguimos buscando espacio en SF (café o lunch cerca de su oficina, o call corta), German se adapta a su agenda.

## gofundme-marketplace
*GoFundMe is Yuno's first live Marketplace-solution merchant (Feb 2026) — Stripe+Adyen+Tabapay, splits+recipients+transfers; PayPal marketplace in build; the reference for platform deals*  
*type: project · last updated 2026-08-04*

GoFundMe went live 2026-02-19 as Yuno's FIRST merchant on the Marketplace solution (Recipients / Split Payments Marketplace product). Publicly named as a client on y.uno homepage (no case study page); architecture details and volumes are INTERNAL — get permission (Samuel Vieira / Justo) before naming specifics externally.

- Processors: Stripe primary (Connect connected accounts created via Yuno, splits w/ application_fee + transfer_data, transfer reversals, delayed capture, ACH us_bank_account), Adyen live (hosted onboarding, ACH Plaid splits, cross-border payout flags), Tabapay (card pulls + recipient KYC). PayPal marketplace in build (Jarrett, Jul 2026). No JPM anywhere.
- Splits: donation + tip + processing fee; recipients onboarding + beneficiary transfers in prod.
- Volumes (INTERNAL): 25K txns Feb 2026 → 294K Mar → 468K Apr; expected 3.5M-10M/month at full ramp.
- Integration: headless direct API; GFM is pilot merchant for the new Universal SDK; evaluating Klarna + iDeal.
- Split payments also live with Pagar.me in Brazil (cards+Pix); Zoop connector extension for Ze Delivery in build (Aug 2026).
- People who know the account: Jarrett Falasco (marketplace product), Samuel Vieira (closed it), Joaquin Ginzo (go-live), William Wong (weekly calls), Juan Ferrari (implementation), Tomas Calle Espinal (TAM).
- "Yuno for Platforms" is NOT a public product name; internally the product is Recipients/Marketplace solution. Used as reference in [[eventbrite-bakeoff]].

## project-gopuff
*Gopuff deck — Stripe (payouts) + Forage (EBT/FSA-HSA) confirmed, consumer acquirer unknown; slide 2 lives in Supabase business_overview column*  
*type: project · last updated 2026-07-30*

Gopuff deck (deck.yuno.tools/m/gopuff, built 2026-07-30, commit 69e2836, industry Marketplace & Delivery). PSP topology = 2 CONFIRMED sin disclaimer: Stripe con rol "US · GoDrive payouts" y Forage "US · EBT + FSA/HSA rails". El acquirer de consumo NO es público (Braintree solo hint por PayPal+Venmo+Cash App, nunca afirmarlo). NUNCA decirle a Gopuff que le "falta" un método: los missing methods del deck son BNPL US + wallets en web (Apple/Google Pay y Venmo son app-only según help center oficial) + Open Banking/Clearpay UK. Revenue omitido (solo Business of Apps ~$2B 2024, no aceptable). **Slide 2 vive en la columna business_overview de Supabase** (patched instant-live, shadowea el JSON local), mismo patrón que [[project-curology]]. Logo wordmark de logo.dev quedó perfecto sin retoque; mirror en storage merchant-logos/gopuff-82d36941.png.

Lead angle (brief v8.0, data/research/gopuff-2026-07-09.md): consolidación de stack fragmentado + pay-ins/payouts unificados + agenda pre-IPO del CFO nuevo Matt McBrady (nov 2025, $250M raise @ $8.5B, ~$4 contribution profit/order). Pains BBB: renovaciones Fam sorpresa, charged-but-cancelled, refunds a GoCash con expiración.

## project_gsheets_mcp
*Google Sheets editing is wired up via the gdrive MCP server — how to use it and where the config lives*  
*type: project · last updated 2026-10-05*

German can ask Claude Code to edit his Google Sheets directly. Setup done 2026-07-01 via the **`@isaacphi/mcp-gdrive`** MCP server (Drive + Sheets, OAuth).

**Config (global, in `~/.claude.json` → mcpServers.gdrive):** command `npx -y @isaacphi/mcp-gdrive`, env `CLIENT_ID`/`CLIENT_SECRET` (OAuth Desktop client from his personal GCP project "Gemini API", ID `gen-lang-client-0895240279` — his y.uno org blocks new-project creation, so we reused that project), `GDRIVE_CREDS_DIR=/Users/germantatis/.config/mcp-gdrive`.

**Creds dir `~/.config/mcp-gdrive/`:** `gcp-oauth.keys.json` (OAuth client) + `.gdrive-server-credentials.json` (saved token with refresh_token, both chmod 600). OAuth already completed — token self-refreshes, no re-auth needed.

**Scopes:** `drive.readonly` + `spreadsheets` (can edit sheets, cannot delete Drive files).

**4 tools:** `gdrive_search`, `gdrive_read_file`, `gsheets_read`, `gsheets_update_cell` (writes are **one cell at a time** — batch loop for bulk; range-write would need extending the server).

To point at a sheet: paste the link (extract the ID) or search by name. If tools are missing in a session, user must Reload Window in VSCode so the extension starts the MCP server.

**⚠️ MUERTO desde ~18/21-sep-2026:** el refresh del token devuelve `deleted_client: The OAuth client was deleted` (proyecto GCP `gen-lang-client-0895240279` borrado, misma ola que el token de Slides, ver [[project-slides-api-token-dead]]). Síntoma en sesión: gsheets_read/gsheets_update_cell fallan con "Method doesn't allow unregistered callers". No hay otra credencial de Google en la máquina (sin gcloud, sin clasp login, sin service account; los scripts de ~/.config/tcl-engine usan las mismas creds). El conector Google Drive de claude.ai solo lee Sheets (read_file_content) y no escribe celdas. **Fix (lo hace German, requiere navegador):** crear proyecto GCP nuevo, habilitar Drive API + Sheets API, crear OAuth client tipo Desktop, guardar el JSON como `~/.config/mcp-gdrive/gcp-oauth.keys.json`, actualizar CLIENT_ID/CLIENT_SECRET en `~/.claude.json` (mcpServers.gdrive.env), borrar `~/.config/mcp-gdrive/.gdrive-server-credentials.json` y Reload Window en VSCode para que el server abra el OAuth. El mismo client sirve para revivir Slides con auth_slides.py. Mientras tanto, entregar filas listas para pegar (ej. UNICEF 22-sep en Deal Status GTM, pendiente).

**⚠️ 22-sep-2026:** el token del MCP gdrive está muerto (`gsheets_read` devuelve "Method doesn't allow unregistered callers" y el refresh da 401). Hay que re-autenticar el server (`npx -y @isaacphi/mcp-gdrive` con las creds en `~/.config/mcp-gdrive/`). Mientras tanto, para crear Sheets usar el conector claude.ai Google Drive (`create_file` con .xlsx en base64 → conversión automática) y para leerlos `read_file_content`.

**Plan acordado 22-sep-2026 (reemplazo de todo el acceso):** un solo proyecto GCP nuevo + OAuth client Desktop + APIs Sheets/Slides/Docs/Drive habilitadas; consent screen External con german.tatis@y.uno como test user y app PUBLICADA. Script `tools/gsuite/auth_gsuite.py <client_secret.json>` escribe `~/.config/gsuite/token.json` (scopes spreadsheets + presentations + documents + drive.file, solo sensibles, sin restringidos) y duplica el token en `~/.config/yuno-slides/token.json` para que engine.py siga funcionando. Escrituras de Sheets/Docs/Slides se hacen con Python (google-api-python-client ya instalado) usando ese token; búsquedas y gestión de archivos de Drive con el conector de Drive de claude.ai. El mcp-gdrive (drive.readonly, scope restringido) queda opcional y no se recomienda reactivarlo.

**24-sep-2026:** confirmado otra vez: gdrive MCP muerto ("unregistered callers"), service account sin acceso al Deal Status GTM (403) y `share_file` del conector de Drive falla con "The caller does not have permission" incluso en un Sheet que German posee (política del dominio contra compartir externo por API). Única vía: German comparte la hoja desde la UI con gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com como Editor; luego `python3 "Lists & ICP/Pipeline Sync/manual_adds/add_rows_2026-09-24.py"` escribe UNICEF, Experian y Línea Directa. Alternativa manual: pegar `rows_2026-09-24.tsv`. Glean también está caído (401 Invalid Secret).

**5-oct-2026, FUNCIONA:** `share_file` del conector de Drive de claude.ai SÍ compartió el Sheet "Money20/20 LV 2026 x Target Account List - Matches" (`1R0GJ0h4vLTi4CrLhwvoklBtxnRry0zmD0IMxZWkiiSo`) con `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` como writer, y acto seguido el service account (`~/.config/gsuite/sa.json`) leyó y borró filas vía Sheets API batchUpdate/deleteDimension. Flujo recomendado para editar cualquier Sheet: 1) intentar `share_file` con el SA como writer, 2) Python con service_account + sheets v4. Si share_file da 403, pedir a German que comparta desde la UI.

## project_hbo_max
*HBO Max / Warner Bros. Discovery — ya orquestan con Spreedly (+ Adyen, Checkout.com, iyzico como SDKs separados); Ashwyn Singhal (Sr Director Product Payments, NYC) = decisor global, Karime Velazquez (Payments Manager LATAM, CDMX, ex-PPRO) = puerta LatAm; BC $15M/año enviado 20-ago sin respuesta; follow-up in-person ENVIADO 17-sep-2026*  
*type: project · last updated 2026-10-06*

**HBO Max (Warner Bros. Discovery)**, streaming DTC, 140M+ subs, LatAm = 5 de sus top 8 mercados web (BR #2, MX #3). Deck: deck.yuno.tools/m/hbo-max. Brief 11-ago: `data/research/hbo-max-meeting-brief-2026-08-11.md`. BC: `Business Cases/BC sheets - HBO Max.xlsx` (total $14.98M/año en 10 mercados: US, BR, MX, CO, AR, CL, PL, ES, TR, AU).

**Stack (verificado código auth.hbomax.com, 11-ago):** Spreedly = orquestador/vault; Adyen, Checkout.com e iyzico (Turquía) cargados como SDKs separados; PayPal wallet; Kount fraude; Arkose bots; SAP BRIM billing + Vertex tax. Brasil oficial (help center, verificado 17-sep): tarjetas + Nupay, sin Pix ni boleto listados. México: solo tarjetas.

**Contactos:** Ashwyn Singhal, Sr Director Product Payments, NYC (ZoomInfo/LinkedIn), lidera payments product global según Madhura → decisor real, nunca respondió. Karime Velazquez (Irma Karime Velázquez Magaña), Payments Manager LATAM, CDMX, ex-PPRO 2019-2023, relación de Alejandro Albarracín. Michael Ward (payments), Robert Hardy (Manager Payments, Knoxville, US), Madhura Bhargave (HBO Asia, única que respondió, hizo la intro 23-jul). Bounces: patty.hirsch, jeff.c, meredith.dwyer.

**Cronología:** 14-jul outbound a ~12 contactos "Payments at HBO Max" → 23-jul Madhura intro a Ashwyn/Michael → 23-jul German centraliza hilo (Ashwyn, Michael, Robert, Karime) → 11-ago call "Catch up" con Karime SÍ ocurrió (21 min, Alejandro + German; transcript Drive 1o_YHm-1m8Djhg5BLFSUc7Re2Zkjnw6L8tQHXprA0ZH4 es inutilizable, frases sueltas; no citar contenido) → 20-ago BC enviado ($15M) → 27-ago case anónimo US subs (+6pp, 45% recovery) + loop Daniel Lozano → 1-sep nota de Daniel (engine subs: 300K+ subs, $15M/mes, Pix Automático recurrente). **Cero respuestas escritas de WBD desde el 23-jul.**

**17-sep-2026:** ENVIADO 15:25 UTC (era borrador, salió el mismo día) en el hilo (reply a nota de Daniel) a Ashwyn+Karime+Michael+Robert, cc Justo/Alejandro/Daniel. German rechazó dos versiones (una dura con datos Q2/Recurly/stack y "five emails in"; otra con NYC/CDMX y semanas). Versión final, a todo el grupo: "traveling around in October, set something up in person, take a look at the business case we shared, hear how things evolved, an hour in person in October, tell me city and week". Sin ciudades ni fechas. Feedback de German: para HBO Max nada de contar correos ni presionar; tono de pasar a saludar.

**Landmines:** nunca "les falta orquestación"; no criticar Spreedly; no decir "you lack Pix/OXXO" (preguntar roadmap); merger Paramount Skydance CERRADO el 6-oct-2026 (grupo renombrado Skydance, ver [[project_skydance]]); la regla anterior de no mencionarlo ya no aplica, pero German decide cuándo usarlo; PayPal no es PSP; no repetir Livelo/inDrive (ya usados). Karime vendió orquestación en PPRO: hablar en números, peer to peer.

**5-oct-2026:** German vio que Ashwyn estará en **Money20/20 USA (Las Vegas, The Venetian, 18 a 21-oct-2026)**. BORRADOR en Gmail (reply al correo de German del 17-sep, msg 1a0aff8d73a2b55f; To Ashwyn, Karime, Michael, Robert; cc Justo; abre "Hi Team," y luego "Ashwyn, I saw...", formato pedido por German): "saw you will be at Money20/20, we will be there too, this is the in person conversation I was hoping to set up in October, 30 minutes over coffee between sessions, pick the day and time". Sin links ni stats. Copia: Deals/HBO Max/hbo-max-money2020-email-2026-10-05.md. ⚠️ El viaje de German a Vegas no está en su calendario (solo el "Money 20/20 Touch Point" interno del 8-oct); confirmar asistencia antes de enviar.

## headshots-con-camisa-yuno
*Pipeline tools/swap_shirt.py para poner la camiseta negra Yuno a fotos de equipo (Headshots/); bloqueado 22-sep-2026 por falta de API key de modelo de imagen*  
*type: project · last updated 2026-09-22*

German guarda fotos de equipo en `Headshots/` (formato 4000x5236, deben quedar <4000 px por lado para la app que las sube; se reducen a 3800 en el lado largo). Su foto de referencia con la camiseta Yuno es `Headshots/55 copy.jpg`. El 22-sep-2026 pidió editar `Headshots/60.jpg` (persona con top marrón sin mangas, brazos cruzados) para ponerle la misma camiseta negra con logo blanco "yuno", sin tocar nada más.

**Estado:** script listo en `tools/swap_shirt.py` (Gemini o OpenAI + composite sobre el original hi-res con máscara bajo el mentón), probado en seco. Falta ejecutar con `GEMINI_API_KEY` u `OPENAI_API_KEY` en el entorno; no hay keys de imagen en la máquina y el clasificador bloquea buscar credenciales.

**How to apply:** si German da una key, correr el script con `--provider gemini` (default) y revisar `*_work/preview.jpg`; ajustar `--threshold` / `--protect-top` si la máscara come cara o deja marrón. Nunca commitear los JPG originales de 13-15 MB, solo las versiones reducidas.

## project_hertz
*Hertz account state — single-PSP Stripe angle, 13 active leads, John March dropped*  
*type: project · last updated 2026-07-20*

Hertz (Hertz Global Holdings, NASDAQ: HTZ) is an active outbound account.

**John March (jmarch@hertz.com) is no longer being contacted as of 2026-07-20.** Do not propose outreach, follow-ups, or re-engagement for him. He had an older, deeper sequence (deck sent, Alejandro Albarracin involved, International RAC partner angle on 2026-07-15) — that thread is closed out.

Active sequence: 13 leads emailed Email 1 on 2026-07-15, Email 2 written 2026-07-20 (Brock Ashford owns payments; Scott Haralson CFO; Sandeep Dube commercial; Seshu Pandey, Tarak Reddy, Matthew Stollenwerk, Dhritiman Saha, Ned Ryan eng/infra/architecture; Yilun Zhang conversion; Kalyan Chintam auth-hold flow; Vikram Rajagopalan intelligence; Jake Farrell ops; Sadashiv I. concentration risk).

Core angle: Hertz consolidated onto **Stripe as sole global PSP in 2024** (in-person Terminal + online, ~160 countries). Pitch is a layer **on top of Stripe, never replacing it** — second acquirer, failover, local acquiring for International RAC, vendor neutrality. Critical: Stripe already runs Adaptive Acceptance, Card Account Updater and network tokens for them, so **never claim they lack those features**. See [[reference_yuno_positioning]] and research file hertz-2026-07-15.md.

## project-higgsfield
*Higgsfield AI research brief 2026-09-16 (supersedes 2026-03-27); Stripe-only at $700M annualized revenue, India/Korea/Brazil cross-border, payment roles open, score 14 High*  
*type: project · last updated 2026-09-16*

Higgsfield AI (AI video/image gen, Higgsfield Inc. SF + Almaty hub). Brief: `data/research/higgsfield-ai-2026-09-16.md` (v8.0, 4 agents). The 2026-03-27 brief is outdated: no official mobile apps exist (App Store/Play listings were clones), revenue is now $700M annualized (Series B $400M at $5.4B, 2026-08-17).

Key verified facts: Stripe is the sole PSP (Terms 9.1, help center, trust page, 162 JS bundles), no orchestrator, no MoR. 75% of revenue outside the US per Stripe case study; Stripe's 95.6% auth rate covers only US/EU/AU. Traffic Aug 2026: US 18%, India 9%, South Korea 6%, Brazil 3.7%, Germany 3.6%; Korea and Japan top five by users (VentureSquare 2026-08-25). No local entities outside the US. Help center (2026-08-01) lists cards Visa/MC/Amex/JCB, Apple Pay, bank payments; states PayPal and crypto not supported (merchant's own words). Stripe lists Pix, Kakao Pay, Naver Pay, PayCo, WeChat Pay, Klarna, Affirm, Link.

Buying signals: PM Lifecycle & Retention (2026-07-28, dunning / payment recovery) and Head of Revenue Accounting (2026-09-01, Stripe reconciliation, refunds, chargebacks). Targets: Alex Mashrabov (CEO), Shotan Jakupov (Data & Growth Lead, quoted in Stripe case study). No CFO publicly announced.

**Why:** Outreach must stay on the "layer above Stripe" framing (same as [[project-gamma]] and [[project-hertz]]); never claim missing APMs, use the help-center "ask your bank to authorize international payments" line as the cross-border hook.

**How to apply:** If a deck or email is requested, pull facts only from the 2026-09-16 brief, not the March one. Suno, Gamma and Perplexity are already in pipeline and excluded from the competitor outreach list.

**Deck (2026-09-16, pedido de Justo vía WhatsApp):** business case con la estructura del deck OpenAI_Yuno_MAY 2026 (Industry/AI/OpenAI) + 2 slides nuevos (industry context estilo Suno, "what you get" estilo Bending Spoons con KYC/KYB, taxes, distribution deals). Contenido slide a slide en `Industry/AI/Higgsfield/higgsfield-deck-content-2026-09-16.md`; modelo en `Industry/AI/Higgsfield/model/`. Números deliberadamente más conservadores que xAI: hero ~$25M/yr (L1 $21.4M, L2 $1.3M, L3 $2.8M) sobre 12M MAU y la tabla SimilarWeb de German (US 15.13%, India 12.54%, RU 3.82%...). Top 20 = tabla de German (US baseline, Rusia excluida); wave 2 = 20 emergentes elegidos por Claude. Brasil/Corea/China con uplift bajo porque Stripe ya les da Pix / Kakao-Naver-PayCo / WeChat Pay.

**Google Slides construido (2026-09-16):** https://docs.google.com/presentation/d/17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g/edit ("Higgsfield_Yuno_SEP 2026", carpeta Industry/AI de Drive). Es una copia del Google Slides "OpenAI_Yuno_MAY 2026" (id 1g-NZo-Tuk5E3WhSgui06GiBcCuDZpjJ-XdhMD11G_s8) editada vía Slides API con el token de ~/.config/yuno-slides/token.json (scope presentations; para copiar se usa el conector Drive de claude.ai). Scripts en `Industry/AI/Higgsfield/build/` (engine.py preserva estilos por párrafo; los slides país se mapean por posición; India tiene coordenadas propias). Lecciones: los chips/pills tienen fondo en un rect separado (recolorear ese, y poner NOT_RENDERED el fill del cuadro de texto), las barras de tablas escalan con scaleX, los layouts deben pertenecer al master vecino al hacer createSlide, logos de merchant vía clearbit no funcionan (usar cuadro de texto), banderas vía flagcdn.com sí.

**Top-20 completo (16-sep-2026):** el appendix tiene deep dive para los 20 mercados de la tabla de German, incluidos EE. UU. (baseline Stripe + upside ~$4.0M/yr fuera del hero) y Rusia (excluido por sanciones, $0). German pidió explícitamente que ningún país del top 20 falte en el appendix; si se agregan mercados al top 20, hay que crear su slide país (duplicar uno existente con add_us_ru.py como patrón).

## project_hostinger
*Hostinger (hosting, Lituania) — demo HECHA 24-sep-2026: Paulius quiere empezar por INDIA (Razorpay+BillDesk bajo una integración, 2º mercado) y vault-as-a-service aparte; ~2M tokens, NTs bajo su propio TRID; billing sigue in-house; 3 correos ENVIADOS tras la demo (recap 24-sep, redline NDA 24-sep, token migration de Dirk 25-sep) SIN respuesta; NDA mutuo con redline de Ivvy en manos de Hostinger, sin envelope nuevo; India prometida por escrito en \"a few days\" pero interno ~8-oct; FUP de German en borrador Gmail 30-sep (India kick-off 1-oct, NDA, working session 13/14-oct); ⚠️ el hilo de la demo estaba en la Papelera y se restauró el 30-sep*  
*type: project · last updated 2026-10-02*

**Hostinger** (hostinger.com), hosting web / website builder con sede en Lituania. Negocio de suscripción con renovaciones prepagadas, gran base de card-on-file.

**Contacto único: Paulius Lapenas — Head of Payments | Hostinger Global** (paulius.lapenas@hostinger.com), zona horaria de Vilnius. Es el dueño del RFP y controla tanto el roadmap como el calendario. Viaja mucho y toma descansos largos (OOO 29-abr a 4-may, 6-11 may, 5-18 jun, última semana de agosto + 1-sep). Perfil: practicante técnico que ya fue sobrevendido antes; pregunta por los modos de falla que los vendors esconden.

**⚠️ Es un RE-ENGAGEMENT, no una cuenta nueva.** Hubo una evaluación previa de Yuno que no convirtió. German escribió el 6-may: "your experience with Yuno will be very different this time", y el 5-jun se refirió al cuestionario como "the one you originally shared with Yuno previously". El resultado de esa evaluación anterior no está documentado en el hilo. **Nunca sacar el tema a menos que Paulius lo saque.**

**Cronología:**
- **29-abr-2026:** se conocieron en persona en **Stripe Sessions SF, Booth 214**. Asistieron Juan Pablo Ortega (co-fundador de Yuno), German, Justo y Paulius. Deck: `ss26.yuno.tools/m/hostinger`. **India** fue el mercado que abrió la puerta.
- 4 follow-ups de German (may-jun), casi todos cayeron en OOO.
- **7-jul-2026:** Paulius responde textual: *"We finalised our plans and capacity for Q3 and we don't have plans for new integrations, but as readiness for Q4 maybe we could revisit this somewhere in August or early September?"* → **Q4 es la ventana de compra.**
- 8-jul: Paulius manda el cuestionario y pide primera semana de septiembre.
- 3-5 ago: trabajo interno de Yuno en las respuestas (Samuel Vieira Tamayo redactó).
- **6-ago-2026:** German devuelve las respuestas completas en dos formatos.
- **Sin respuesta desde el 6-ago (25 días de silencio).**
- **3-sep-2026:** call de debrief HECHA (45 min). Yuno: German, Justo (CRO), Antoine Cathelin (Head of Product), Dirk Van Der Meulen (SE). Paulius solo por Hostinger. Transcript: `Deals/Hostinger/hostinger-call-transcript-2026-09-03.md`.
- **17-sep-2026 (jueves, misma hora):** deep dive agendado — vault standalone + subscription engine + India.

**Call 3-sep-2026 — lo que reveló Paulius:**
- **Interés #1 confirmado: vault standalone por business continuity.** 60-70% del revenue viene de suscripciones; quiere ser dueño de los tokens y poder cambiar de capa sin parar cobros si "el orquestador se cae". Decisión este año, plan de ejecución para el próximo.
- **Ya usan un orquestador third-party hoy** para suscripciones con tarjeta (fallbacks entre PSPs + reglas de retry viven en esa capa). No dijo cuál. Los APMs recurrentes (PayTM, LatAm, India) van por integraciones directas sin fallback.
- Stack confirmado en su voz: **Stripe, Adyen, Checkout.com**, proveedores locales APAC/LatAm, e India directo con **Razorpay + BillDesk** (cross-border; ~70% UPI / 30% tarjetas).
- **Billing = Chargebee, migrando in-house gradualmente.** Dunning: hasta 5 retries en 21 días. Dolores: Chargebee solo controla el gap entre retries (no hora del día ni día del mes; cobran a medianoche del cliente), y los batches de renovación disparan reglas de fraude en los PSPs. **Restricción clave para el pitch de Yuno:** la inteligencia de retries puede mover el intento DENTRO de la ventana de dunning, nunca retrasar su ciclo (lo dijo explícito: optimizar jueves→viernes sí, "delay one week" no sirve).
- **India como mini-deal propio:** quiere una sola integración sobre Razorpay+BillDesk (hoy mantiene dos, con journeys distintos) y claridad sobre el mandato de token portability de UPI. ⚠️ Justo afirmó en la call que el mandato del banco central existe y que los players deberían cumplir a fin de año, y que Razorpay lo tenía para este año (verificar antes de repetirlo por escrito); prometió status actualizado vía el GM local de India.
- **Agentic payments:** prioriza protocolos stablecoin (x402, wallet de Cloudflare, MPP) sobre rieles de tarjeta ("card payments won't be soon there" para service businesses); ya habla con Stripe por los specs. Pregunta abierta suya: cómo facturar micro-pagos (¿invoice por micro-pago o agregado por sesión?). Antoine pidió su feedback de merchant para el diseño de la integración MPP de Yuno.
- **Compromisos Yuno:** Justo → material completo de vault standalone, status India, e info de Revolut Pay / notificación Mastercard de tarjeta fondeada; Dirk → confirmar que el retry timing de Yuno opera dentro del dunning schedule de ellos.
- **NDA: papel de Hostinger** (su legal revisa más rápido). Datos enviados en el follow-up: entidad **YUNO TECNOLOGIAS S.A.P.I. DE C.V.** y sus afiliadas (Calle Cráter 38, Col. Jardines del Pedregal, Álvaro Obregón, CDMX, CP 01900), firmante **Diego Felipe Alonso Cruz** (diego@y.uno), aprobador legal interno **Ivvy Larissa Bueno Soberay** (ivvy@y.uno).
- Follow-up enviado a borrador Gmail 3-sep (recap 3 bullets + next steps 3 bullets + datos NDA): `Deals/Hostinger/hostinger-followup-email-paulius-2026-09-03.md`.
- Contexto org: "overall organization is shifting priorities for the way we position ourselves in the market" — cuadra con el pivote AI-first bajo el CEO nuevo Giedrius Zakaitis.

**El RFP:** se titula "Questions to **orchestrators**" (plural) → **es competitivo**, Yuno se compara por escrito contra otros. 17 secciones. Aproximadamente la mitad (network tx ID, network tokenization, account updater, recurring engine) es una sola pregunta: cómo perder menos renovaciones.

**Lo que el RFP revela de Hostinger:**
- Planean **migrar su vault** (preguntan por backfill de network tx IDs y por qué % de su token DB tiene al menos uno). Ese es el centro comercial del deal.
- Tienen **volumen de débito US** relevante (3 preguntas de pinless debit / least-cost routing).
- Tienen un **book de billing agreements de PayPal** que migrar.
- Siguen mandatos de esquemas de cerca (citan un KB específico de Cybersource sobre Apple Pay MPAN).
- Presencia EU con co-badged cards (Cartes Bancaires, IFR 2015/751).
- Equipo de BI real: distinguen approval rate a nivel transacción vs a nivel orden, y piden export a data warehouse.

**⚠️ Puntos débiles de las respuestas de Yuno (6 difieren a "on request"):** matriz de PSPs que aceptan network tx ID (2.1), salud del token DB (2.4), matriz de aceptación de network tokens (3.5), conectores de data warehouse (4.4, **la peor respuesta del documento**), version control de routing (6.3), y matriz de wallet-token MITs (13.3). Otros gaps reales: account updater solo Visa y Mastercard (**sin Amex**), suscripciones **solo tarjetas**, retries **topados en 5** en producción, logs de entrega de webhooks no visibles en la pantalla de pagos, pinless debit es capacidad del adquirente no de Yuno, y **no hay SDKs de backend** (un borrador interno afirmaba Kotlin/Java y Node y fue corregido antes de enviar; NO resucitar esa afirmación).

**Jugada de mayor palanca:** llegar a la call con las matrices scopeadas a los proveedores reales de Hostinger. Convierte la columna más débil de la comparación en la más hecha a la medida.

**Research externo 2026-08-31 (hallazgo central, no nombrar en la call salvo que Paulius lo saque):**
- **Hostinger ya tuvo una capa de orquestación (ProcessOut) y un adquirente (Credorax) que terminaron absorbidos por competidores de Yuno.** ProcessOut fue su partner de optimización de pagos (según entrevista pública con su payments lead), adquirido por **Checkout.com** en feb-2020. Credorax (adquirente de Hostinger desde abr-2021) se renombró **Finaro** (dic-2021) y fue comprado por **Shift4** por $575M (mar-2022). Es casi seguro el motivo real del RFP: un partner independiente que deja de serlo al ser comprado por un PSP. Es el mejor argumento de independencia de Yuno, pero no nombrarlos preventivamente.
- Paulius: perfil de RocketReach (sin verificar contra 2da fuente) — antes en **Western Union** y **Lindorff** (cobranza nórdica), MA en E-business Management (Mykolas Romeris University, 2014-2017). Su trasfondo de cobranza explica preguntas del RFP sobre *recuperar*, no solo evitar, renovaciones fallidas.
- ⚠️ Puede existir un segundo "Head of Payments": **Gediminas Griška** (entró 2018, retention→payments) aparece en una entrevista externa, y hay una vacante abierta de "Head of Payments". No preguntar directo, pero no sorprenderse si hay más de una persona decidiendo.
- Estructura de pagos interna: dentro del área de producto, equipo técnico ("hPayments") + equipo de estrategia (relación con PSPs, negociación, optimización) con 5 personas dedicadas a fraude/chargebacks/disputas.
- Financials: ingresos 2022-2025 con CAGR 58% (€69.6M→€275.4M), 2023 primer año EBITDA positivo. Bootstrapped sin VC; ConHostinger GmbH tomó ~31% en 2021; payout de stock options de €11.8M en mar-2026 — señal de preparación pre-liquidez, no de distress.
- Modelo de negocio: términos prepago largos, **renovación ~3.5-4x el precio de entrada** — por eso una renovación declinada es un evento de ingreso grande, no marginal. Esa es la lógica de negocio detrás de todo el enfoque del RFP en network tokens/NTID/account updater.
- Stack externo inferido: 6 descriptores de tarjeta distintos (múltiples rieles de adquirencia), EBANX probable en LatAm (`EBN*` prefix), dLocal en Japón, Ravelin (fraude) + iDenfy (identidad). Dolor propio citado: *"Lack of 3DS coverage in Latin America makes fighting chargebacks challenging."*
- CEO nuevo: **Giedrius Zakaitis** (16-jun-2026), reemplaza a Daugirdas Jankus.
- Doc: https://docs.google.com/document/d/1CqI5ig5Z-K4iE0uPrLol6-aab49BRiIPh89Tu8YYYCU/edit

Brief: `data/research/hostinger-meeting-brief-2026-09-03.md`.

**✅ CORRECCIÓN 15-sep-2026: el recap del 3-sep SÍ se envió** (3-sep 15:22Z, cc Justo, Antoine, Dirk, con entidad y firmante del NDA) y el 9-sep salió un recordatorio de NDA. Paulius no ha respondido por correo desde el 8-jul (aceptó la invitación del 17-sep el 4-sep). NDA sin firmar a 15-sep. No hay borradores pendientes a Paulius. Los compromisos de Justo (material vault, status India, Revolut/Mastercard) y de Dirk (retry timing dentro del dunning) siguen sin evidencia de envío. Opp "Hostinger-" transferida a German en SFDC el 9-sep.

**Sync interno 15-sep-2026 (Piotr, Dirk, German; transcript en Drive doc 1daJRgWHXMssDzJr-X8EwZg9vzyRVUFtqK9xmiNsrCFI):** Piotr fue AM de Hostinger en Braintree/PayPal y les vendió Braintree vía ProcessOut; en MPE Berlín (fin de marzo 2026) le dijeron "felices con ProcessOut, no buscamos, pero ayúdanos con conexiones en India". **✅ ProcessOut (Checkout.com) es el orquestador third-party que Paulius no nombró.** Piotr: ProcessOut fuerte en EU/US, flojo en APAC; India es la cuña. Acuerdos: NO demo interactiva desde cero, pocos puntos fuertes con prueba en vivo; Dirk demo y mira India; Piotr callado salvo historia; TJ (Tautvydas) entra 10 min por presencia local en Vilnius (Piotr lo llama VP of Engineering, Slack dice Engineering Management Consultant, verificar); German manda brief; Piotr comparte notas de marzo. Pregunta abierta de Dirk: "¿por qué buscan alternativas?" nunca se preguntó. **Antoine declinó la demo del 17-sep** (15-sep); TJ aceptó el 16-sep; Justo sin responder al 16-sep. **⚠️ 17-sep: Paulius pidió mover la call ("unplanned conflict"); reagendada al jueves 24-sep-2026 6:00 COT / 14:00 Vilnius, mismo Meet; Paulius y Dirk aceptaron el 24-sep.** 3er pedido de NDA en borrador Gmail 17-sep (reply en el hilo "Hostinger + Yuno | Demo", ofrece template de Yuno como alternativa). Al 16-sep no hay evidencia en Slack ni Gmail de sandbox, matrices, retry timing (Dirk) ni status India (Justo) cerrados.

**NDA 18/21-sep-2026:** el 18-sep Paulius pidió datos del firmante, German los reenvió y Paulius respondió "sent to our Legal"; Hostinger mandó su NDA directo por DocuSign a Diego. **21-sep: Ivvy (legal, #salesops-legal) dijo que NO se puede firmar como llegó:** es unilateral (solo protege a Hostinger, todas las obligaciones a Yuno), penalidad fija EUR 10k por evento y cláusula que les da propiedad de todo lo desarrollado durante la vigencia. Tres salidas: (A) NDA mutuo estándar de Yuno, (B) redlines de Yuno sobre su template (ya hechas, Ivvy tiene el archivo), (C) pedirles su template mutuo. Diego NO firma el envelope actual; Hostinger debe anularlo. Borrador a Paulius en Gmail 21-sep (reply en hilo "Hostinger + Yuno | Demo", cc Ivvy + equipo) con las 3 opciones, sugiriendo B o C porque su legal prefiere su papel. Pendiente: enviar, y responderle a Ivvy en Slack cuál ruta.

**Sync Antoine/German 2-sep (Drive doc 1QbHKlFAOYBs76XBFyvQvDGRJyDmy0P1QEYyfHzZuMkk):** ⚠️ Amex network tokens NO está live aunque la respuesta RFP 3.1 lo lista (Antoine: "meses"); account updater solo Visa/MC. Antoine citó 5.5 bps MC / 7.5 bps Visa de ahorro con NT/3DS (sin verificar, no citar por escrito). Checkout NL sin iDEAL, CO solo PayPal/GPay/APay/Nequi (LPMs = hilo posterior, el RFP no pregunta por LPMs). Mala experiencia previa: Miguel (ex GM Europa) + un BD, sin respuesta al cuestionario.

**Docs verificados 15-sep:** retries de suscripciones = DEFAULT (5h,12h,24h,36h,48h,96h), SMART (ML por decline reason/país/emisor/proveedor), CUSTOM_SCHEDULE (delay por intento 1s a 7 días); **tope 6 en producción (el RFP dijo 5, corregir)**. Deck interno de subscriptions (sep-2026) lista cards + Apple/Google Pay + PayPal + Pix Automático live (el RFP dijo "solo cards"; confirmar con Daniel Lozano); cifras del deck (16 merchants, 135K subs, 86%/ciclo) son internas, no citar afuera. India: NPCI planea portabilidad de mandatos UPI Autopay (Mint 31-ago-2026, anuncio esperado en Global Fintech Fest), NO live; no repetir "el mandato existe" como hecho. 🔍 Pendiente Dirk: si el timing SMART aplica a MITs programados por el billing del merchant o solo a ciclos del engine.

**Hilo India de Piotr (marzo-abril 2026, compartido por German el 15-sep):** en MPE Berlín Hostinger le mencionó "some challenges with UPI"; en abril Piotr les escribió preguntando si seguía siendo el caso, dijo que Yuno invierte fuerte en India con oficina local, y les mandó la lista "Payment Methods, India, Recurring / MIT Support": cards recurrentes Visa/MC/RuPay/Amex/Diners/JCB/Discover vía Airwallex, Adyen, Stripe, Checkout.com, Splitit, Worldpay, Unlimint, Nuvei, NMI; Apple Pay MIT vía Adyen/Stripe/Checkout/Airwallex/Braintree; Google Pay MIT vía Stripe/Airwallex/Adyen; UPI Autopay "vía proveedores UPI habilitados" (sin nombrar); Afterpay y Cash App Pay vía Stripe (no son India). ⚠️ Razorpay y BillDesk (los proveedores reales de Hostinger en India) NO están en esa lista; el jueves hay que nombrarlos explícitamente y nombrar qué conexiones corren UPI Autopay. No se sabe si respondieron la pregunta de UPI.

**Brief técnico interno para el 17-sep:** data/research/hostinger-technical-deep-dive-brief-2026-09-17.md (+ .html, Google Doc "Technical Deep Dive Brief: Hostinger (Sep 17, 2026)": https://docs.google.com/document/d/1_jBl7CvKactL-qzqpdpNJ-TeSC9OOxO3zASd3cZ0w5s/edit; German pidió el nombre en inglés, "Technical", no "Técnico"). Estructura: TL;DR, lo hablado, prioridades rankeadas (1 vault standalone, 2 renewal auth NT/NTID/AU, 3 retries dentro del dunning, 4 India, 5 routing, 6 BI), 4 proof points en vivo, facts say/don't say, open items, run of show y preguntas al final.

**Piotr Sierpinski (Sales Manager Europe, Varsovia) y la propiedad de la cuenta (Slack, 3-sep-2026):** Hostinger fue merchant de Piotr en Braintree; trabajó mucho con Paulius y con un **Mindaugas** (rol en Hostinger sin verificar; LinkedIn muestra Mindaugas Barzdenis y Mindaugas Krasauskas, ninguno con título de pagos). No tenía opp en SFDC porque "siempre decían estar felices con su proveedor actual", pero discutió Europa y APAC con ellos en julio 2026. Tenía una oportunidad en la cuenta 001Ps00000a47hL y reportó en #piotr-salesforce que German abrió otra para el mismo merchant; el 9-sep SFDC transfirió la opp "Hostinger-" a German. Tono colaborativo. Sync interno 15-sep 10:45 organizado por él (con Dirk). En el grupo Slack "Hostinger" (Justo, Antoine, Dirk, German) Dirk preguntó si les interesa orquestación o solo vault; German: "mainly vaulting, but demo everything". Tautvydas (TJ) = Engineering Management Consultant, en la invitación del demo, rol en la cuenta desconocido. Brief del sync: data/research/hostinger-internal-sync-brief-2026-09-15.md (Google Doc "Internal Sync Brief: Hostinger demo prep (Sep 15, 2026)": https://docs.google.com/document/d/1dawyrxuyxnN3lGYGnIYzfEeGHq6GqMKUyZPpDKAejPI/edit).


**Brief de la demo 24-sep-2026 (escrito 23-sep):** data/research/hostinger-meeting-brief-2026-09-24.md (+ .html) y Google Doc "Meeting Brief: Yuno <> Hostinger (Sep 24, 2026)": https://docs.google.com/document/d/11y_CjPPciH9MsobwCQgXNTz2cOMTetiZaLRFWwn4-T4/edit. Consolida el brief técnico del 17-sep, el sync del 15-sep, la demo (4 proof points A-D + India 6 min + cierre), alineación interna, run of show y preguntas al final. Ask de la demo: sesión de ingeniería con hPayments en 2 semanas + propuesta escrita (vault standalone + India) en 1 semana + ruta de NDA.

**Estado al 23-sep-2026:**
- Invite 24-sep: Paulius ✅ (17-sep), Dirk ✅, Antoine ✅ (18-sep, había declinado el 17), Piotr ✅ (23-sep), Justo y TJ sin responder.
- **TJ = Tautvydas Paukštė, "VP Transaction Rails" según Slack (23-sep)**, ya no "Engineering Management Consultant"; timezone Slack = São Paulo aunque Piotr lo describe como local en Vilnius (verificar antes de presentarlo como local).
- **NDA:** el correo del 21-sep con las 3 opciones SÍ se envió (cc Ivvy, Antoine, Dirk, Justo, Piotr, TJ) con adjunto "EN - Mutual NDA - Yuno Payments Limited.docx.pdf". ⚠️ La numeración salió mal (la opción de redlines quedó dentro del punto 1) y ⚠️ la entidad del template (Yuno Payments Limited) no coincide con la que German le dio a Paulius (YUNO TECNOLOGIAS S.A.P.I. DE C.V.): confirmar con Ivvy. Paulius no ha respondido; envelope de DocuSign a Diego sin anular. Ruta pendiente de responder a Ivvy en #salesops-legal.
- Sin evidencia en Gmail/Slack/Drive de sandbox, matrices, retry timing (Dirk), status India ni material vault (Justo), ni de las notas de Berlín de Piotr.
- **Hechos docs.y.uno verificados 23-sep:** subscriptions soportan CARD, PAYPAL_ENROLLMENT y PIX_AUTOMATIC (el RFP 11.1 decía "solo cards": corregir); retries DEFAULT/SMART/CUSTOM_SCHEDULE, tope 6 en producción y 5 en sandbox, SMART aplica desde el 2º retry; campos de reportes network_transaction_id, network_token(_type), merchant_order_id, subscription_id, billing_cycles_* ✅; conectores de data warehouse no aparecen en docs; docs de migración no cubren exportación de tokens al salir.
- **India (cambió vs. 17-sep):** NPCI tiene framework de interoperabilidad de mandatos UPI Autopay (MIC, purpose code AZ; reportes 31-ago; portabilidad de usuario 1 vez cada 90 días con UPI PIN); MyUPI lanzado en GFF 10-sep (vista única de mandatos); Razorpay afirma ejecutar mandatos entre gateways/acquirers sin re-registro (blog 6-oct-2025, rollout escalonado desde jul-2026 según prensa). ⚠️ NO verificado que la portabilidad merchant-side esté live en todo el ecosistema ni el status de BillDesk. Interno ✅: ebanx-int v2.10.6 (21-sep) arregló creación de mandatos UPI Autopay en conexiones EBANX India → UPI Autopay recurrente corre en producción vía EBANX India; PayU India (cards, RuPay, card SI + UPI Autopay) = acuerdo de partner firmado 21-sep para otro merchant, integración ❓. Razorpay y BillDesk como conexiones Yuno: ❓.
- Gong (1 call + 13 emails desde 1-sep): Paulius quiere ver vault standalone completo, subscription engine (creación de plan + retry logic) y update de India.
- Noticias Hostinger: 1-sep Managed Hermes Agent; 2-sep Kodee → "Hostinger Agent" (91% de ~1.5M conversaciones/mes resueltas solo); 23-sep mantenimiento de emergencia servidor IN-840 resuelto en 22 min (statuspage). LinkedIn de Paulius: lt.linkedin.com/in/paulius-lapenas-25964976 (bloqueado para lectura automática).


**DEMO 24-sep-2026 HECHA (43 min; transcript: Deals/Hostinger/hostinger-call-transcript-2026-09-24.md; Gong y Fireflies grabaron).** Yuno: German, Dirk, Piotr, TJ. Justo y Antoine NO entraron (Antoine pasó a "Maybe" esa mañana).
- **NDA:** Paulius desautorizó a su legal (mandaron uno unilateral); Hostinger envía su **NDA MUTUO** (el que usan con otros proveedores) "hoy o mañana". Ruta C. Ivvy en cc del follow-up.
- **Pidió enfocar en dos cosas:** India como caso de uso y vaulting as a service.
- **Split de volumen:** ~70% MIT recurrente, ~30% one-time / card-on-file (por verificar). Planes: anual > mensual > 2-4 años. "Bread and butter is subscription payments... convert during the auto-renewal flow without the customer in session."
- **Routing (Dirk):** preguntó por routing por metadata (sí, text y number), prioridad network token vs PAN (controlada por el merchant en la ruta; modelo de optimización a futuro), y en qué datos se entrena el smart routing (cost = datos del merchant; conversion/latency = datos de plataforma). Bug de sandbox al seleccionar decline codes.
- **Subscription engine:** Chargebee hoy solo emite facturas y manda la señal de cobro con dunning configurado ahí. **Paulius: migrar catálogo/pricing/billing a Yuno "I don't see that happening, to be honest."** Lo que quiere: "smart subscription management" que, cuando ELLOS inician el cobro, Yuno elija un mejor momento dentro de su ventana (ej. retrasar 20 h). German: se puede hacer un puente billing in-house/Chargebee → Yuno ejecuta el cobro. ⚠️ Piotr respondió "Exactly" a si el smart routing puede retrasar un MIT creado por ellos: SIGUE SIN VERIFICAR (ítem de Dirk desde 3-sep); el follow-up solo promete respuesta escrita. ⚠️ German dijo en la call que el engine corre cards, Pix Automático, Apple Pay, Google Pay, PayPal y "terminando UPI Autopay"; docs dicen CARD, PAYPAL_ENROLLMENT, PIX_AUTOMATIC: no repetir por escrito.
- **Token migration (su pregunta central):** qué pasa con network tokens y scheme/network transaction IDs al cambiar de orquestador (ha visto declines cuando un orquestador manda el scheme ID equivocado). Tokens hoy en el vault del orquestador actual, **bajo el nombre/TRID de Hostinger**. **Volumen: "a couple of million tokens"** (no migrarían inactivos). Dirk: Yuno hace la transferencia con el proveedor actual y entrega reporte de mapeo; NTs bajo su nombre deberían reutilizarse (a verificar); enviará overview paso a paso (datos que se toman, qué se pide a las redes, cómo se protege el auth rate).
- **India:** tokens y mandatos UPI Autopay están **directo en Razorpay y BillDesk**, no en el orquestador. Paulius: RBI no permite compartir tokens entre proveedores (que él sepa; regulación en camino); pide **ejemplo en producción** de migración desde Razorpay/BillDesk. Piotr: "somos locales en India", opción de tomar raw card data y re-tokenizar (brainstorm, no plan). TJ: consulta con el owner del vault y vuelve.
- **Cierre de Paulius:** "If we can focus on India, that would be a very straightforward case. Now we handle it separately at the PSP level; it can move to the orchestration platform with proper routing, proper token storage, adhering to local requirements. Strong case. Second market in size. Good starting point. And then vaulting as a service as a separate track." TJ: "we're going to come back regarding the India case." Paulius: "That is quite important."
- **TJ se presentó** como VP of Engineering del lado de rails (integraciones, orquestación, transaction core), ~1.5 meses en Yuno; ofreció reunirse en Vilnius; Piotr se apuntó.

**Slack grupo "Hostinger" (C0BUUNA0Y7N: Justo, Piotr, German, Antoine, Dirk, TJ) post-call 24-sep:**
- Reparto: German manda resumen + next steps; **TJ manda el follow-up de India**; Dirk el de token migration.
- Piotr habló con TJ sobre tokens en India: "looks like we indeed can do this".
- **Antoine:** "we are discussing India local reg with Elizabeth Sargeant and the team. This is not straightforward and will require quite some work. Give us a couple of weeks." Sobre NTs: Hostinger tiene TRID propio → "they need to do some paperwork to make us the TR-TSP, but nothing ground breaking; we can import their tokens."
- Justo preguntó si tienen entidad local en India; German: no, hacen cross-border (facturan desde Hostinger PTE Singapur, GSTIN no residente).

**Follow-up de German:** borrador en Gmail 24-sep (reply en el hilo "Hostinger + Yuno | Demo", cc Antoine, Dirk, Justo, Piotr, TJ, Ivvy); copia y notas de sustento en Deals/Hostinger/hostinger-followup-email-paulius-2026-09-24.md. Compromisos escritos: India por TJ en ~2 semanas; token migration overview por Dirk en días; retry timing para cobros iniciados por su billing en la misma nota; working session con su equipo tras el NDA.

**Pendientes al 24-sep:** NDA mutuo de Hostinger (ellos); respuesta India (TJ/Antoine/Elizabeth, ~8-oct); token migration overview + retry timing por escrito (Dirk); verificar reutilización de NTs bajo su TRID y el trámite TR-TSP; confirmar Razorpay y BillDesk como conexiones; propuesta comercial (vault standalone + India) sigue sin fecha; pricing vault standalone (Justo).

**Secuencia de follow-ups 24-sep (acordada con Dirk):** German manda el recap y da pie; Dirk responde en el mismo hilo con su nota de token migration (borrador guardado en Deals/Hostinger/hostinger-dirk-token-migration-email-draft-2026-09-24.md); TJ manda India aparte. Follow-up de German = v2 ENVIADO 24-sep (German confirmó que lo mandó; la v1 se borró porque describía datos de migración y el "registration step" de NTs, que ahora cubre Dirk). ⚠️ **Contradicción abierta sobre network tokens:** Dirk (borrador) dice que no son portables entre token requestors y que Yuno provisiona tokens nuevos bajo un requestor ID operado para Hostinger; Antoine (Slack 24-sep) dice que con TRID propio de Hostinger solo hace falta trámite TR-TSP y "we can import their tokens". Paulius preguntó esto en la call; alinear Dirk + Antoine antes de que salga la nota de Dirk. Además el borrador de Dirk trae texto suelto ("SpaceX/Starlink India compliance answer.", frases cortadas en el bullet de Monitors) y no cubre retry timing para cobros iniciados por su billing (prometido "this week" en el correo de German, sin owner confirmado).

**24-sep, tarde:** German ENVIÓ su follow-up (v2) a Paulius. Dirk tiene green light para mandar su nota de token migration en el mismo hilo una vez corrija: NTs (alinear con Antoine y con RFP 3.2/3.3), piloto "full billing cycle" (planes anuales → usar tokens con renovación en 30 días), texto suelto en Monitors, India apuntando a TJ, y si puede el retry timing.

**NDA 24-sep-2026, tarde (Ivvy, #salesops-legal 14:38 COT):** llegó el NDA MUTUO de Hostinger para firma (ruta C). Ivvy NO lo firma tal cual: pide 2 cambios en redline (archivo Slack F0C445EPENP, "09242026 - IS - Mutual Non-Disclosure Agreement v2 - Yuno and Hostinger.docx"): (1) Art. III.B: propiedad de invenciones limitada a las derivadas de la Confidential Information del Disclosing Party (como estaba, cualquier invención durante la vigencia pasaba a la otra parte); (2) Art. II.E: quitó el texto de "premises" y autorización escrita para guardar info en computador, y agregó carve-out de back-ups y copias exigidas por ley. Además typo "from"→"to" en la definición de Disclosing Party y completó datos de Yuno (TECNOLOGÍAS con tilde, RFC YTE220608U90, Diego como Executive Vice President). Pide a Hostinger un envelope nuevo de DocuSign y Diego firma. **Correo a Paulius con estos puntos + redline adjunto = BORRADOR en Gmail 24-sep** (reply en hilo "Hostinger + Yuno | Demo", cc Ivvy + equipo); copia en Deals/Hostinger/hostinger-nda-redline-email-paulius-2026-09-24.md. Pendiente: enviarlo y confirmar que Hostinger anuló el envelope unilateral original.

**Estado al 29-sep-2026 (verificado en Gmail, Slack y Calendar):**
- **Los tres correos post-demo SÍ se enviaron** en el hilo "Hostinger + Yuno | Demo": recap de German (24-sep 13:29Z), redline del NDA con adjunto (24-sep 20:27Z) y nota de token migration de Dirk (25-sep 10:48Z; Dirk la dirigió a German con Paulius en cc). **Paulius no ha respondido a ninguno**; su último correo es del 18-sep. No hay borradores viejos pendientes.
- ⚠️ **El recap enviado difiere de la copia local:** German cambió India de "within two weeks" a "We will update you in a few days once we confirm everything" y quitó el punto de retry timing. Es decir, por escrito India quedó en "a few days" y no hay promesa escrita de nota de retry timing.
- **Nota de Dirk enviada ya corregida:** NTs planteados como dos caminos según de quién sea el TRID (propio de Hostinger = importar; del proveedor = re-provisionar) y le pregunta a Paulius cuál aplica. Contradicción Dirk/Antoine resuelta así. Pregunta del TRID sin responder.
- **NDA:** sin envelope nuevo de DocuSign; último mensaje en #salesops-legal es de German el 24-sep.
- **India:** cero novedades en Slack desde el 24-sep (Antoine: "a couple of weeks").
- Sin reunión en calendario. Gong: opp en Discovery, $0, close date 11-mar-2027.
- **FUP de German = BORRADOR en Gmail 29-sep** (reply en el mismo hilo, cc equipo + Ivvy): reconoce que India tarda más y promete respuesta escrita para el viernes 9-oct (⚠️ confirmar con TJ/Antoine antes de enviar), pide el envelope nuevo, recuerda la pregunta del TRID y propone working session la semana del 12-oct preguntando quién de su equipo entra. Copia: Deals/Hostinger/hostinger-followup-email-paulius-2026-09-29.md.


**Estado al 30-sep-2026:**
- ⚠️ **El hilo "Hostinger + Yuno | Demo" (id 1a0ae5f99f71a2d0) estaba completo en la Papelera de Gmail** (recap, redline NDA, nota de Dirk y update NDA del 21-sep) y el borrador del 29-sep había desaparecido. Se restauró el hilo con untrash_thread el 30-sep. Si vuelve a pasar, no crear borradores nuevos sin restaurar primero (Gmail purga la papelera a los 30 días).
- **India (Antoine, group DM Slack 29-sep):** kick-off interno con todos los equipos impactados el jueves 1-oct para *local India processing*; cross-border "ya lo podemos hacer". Sin fecha de respuesta escrita; estimado sigue siendo ~8-oct.
- **NDA:** sin envelope nuevo; último mensaje en #salesops-legal sigue siendo del 24-sep.
- Paulius mudo desde el 18-sep. Sin reunión en calendario. Piotr preguntó el 30-sep por DM si hay algo suyo para Hostinger; German: "the team is aligning internally on India".
- **FUP de German = BORRADOR en Gmail 30-sep** (reply a la nota de Dirk, cc equipo + Ivvy): kick-off India jueves + cross-border listo, respuesta escrita "next week" (⚠️ confirmar con Antoine/TJ antes de enviar), envelope nuevo del NDA, working session mar 13 o mié 14-oct en la tarde de Vilnius + quién entra + pregunta del TRID. Copia: Deals/Hostinger/hostinger-followup-email-paulius-2026-09-30.md.

**Estado al 1-oct-2026:**
- **Paulius rompió el silencio (1-oct 08:15Z):** "You should receive revisited MNDA shortly, our Legal accepted suggestions." Los dos cambios de Ivvy quedaron aceptados; falta que llegue el envelope nuevo.
- El FUP del 30-sep SÍ se envió el 1-oct 09:38Z (India: respuesta escrita "next week"; working session mar 13 o mié 14-oct). German respondió "Thanks!" a las 13:09Z.
- **Ivvy (#salesops-legal, 1-oct):** "we are receiving the same NDA for signature" y pide que Hostinger anule el que le reenvían a diario a Diego. ⚠️ German aclaró que Ivvy habla de lo que llegó HOY: tras el aviso de Paulius, lo que llegó para firma sigue siendo el mismo NDA, NO el revisado. El envelope con los dos cambios sigue sin llegar.
- (Actualización 2-oct: el double email SÍ se envió el 1-oct 13:18Z.)
- **Double email a Paulius = BORRADOR en Gmail 1-oct (v2)** (reply al "Thanks!", cc equipo + Ivvy): avisa que lo recibido hoy es el mismo NDA de antes, pide que salga el revisado como envelope nuevo y que anulen el anterior. La v1 (solo pedía anular) se borró. Copia: Deals/Hostinger/hostinger-nda-void-envelope-email-paulius-2026-10-01.md. Pendiente: enviar y responderle a Ivvy en Slack.

**Estado al 2-oct-2026:**
- **NDA FIRMADO** (Ivvy en #salesops-legal: "NDA signed"). Queda desbloqueada la working session con datos de Hostinger.
- El double email del 1-oct (13:18Z) se envió. Paulius no ha respondido a las fechas (mar 13 o mié 14-oct), ni a quién entra, ni a la pregunta del TRID.
- ⚠️ **India, cambio fuerte (Antoine, grupo Slack 2-oct):** el kick-off del 1-oct concluyó que local India processing "will take quite some time to have in prod", "not before the end of the year". Luego Elizabeth Sargeant pidió frenar el trabajo de "Zuora India" hasta nuevo aviso y Antoine paró el scoping de local India; él le avisó que hay dos prospectos interesados (un "Singapore airline" por RFP y Hostinger) y ella respondió "if its not just Zuora thats fine". Antoine puso en ese RFP "we are scoping local india and would know more in 27". Cross-border sigue siendo "we can already do it". German respondió "Still a GO!" y que apuntan a Razorpay y BillDesk.
- Hostinger procesa India **cross-border** (Paulius, 3-sep: "Yeah, we do cross border"). Punto sin resolver: si su caso (Razorpay + BillDesk bajo una integración, tokens y mandatos según regulación local) entra en lo que ya se puede hacer o depende del scope pausado; Antoine hoy lo cuenta como "local india processing". Validar con él.
- Sigue debiéndose la respuesta escrita sobre RBI, tokens y mandatos UPI Autopay, prometida para la semana del 5-oct; sin dueño con fecha.
- **FUP a Paulius = BORRADOR en Gmail 2-oct (v2)** (reply en el mismo hilo, cc equipo + Ivvy): NDA firmado; foco único = agendar la working session de token migration (mar 13 o mié 14-oct, quién entra, Dirk la conduce); India como afirmación: "cross-border processing is live today, and we are targeting early 2027 to go live with local processing". German pidió quitar la pregunta del TRID (network tokens no es lo relevante ahora) y la pregunta cross-border vs local. ⚠️ "early 2027" es de German; internamente Antoine solo dijo "not before the end of the year" y el scoping está pausado: confirmar antes de enviar. Copia: Deals/Hostinger/hostinger-followup-email-paulius-2026-10-02.md.

## project_lightricks_psp
*Lightricks payment stack + Yuno angle (research 2026-06-17)*  
*type: project · last updated 2026-06-17*

Lightricks Ltd. (Jerusalem; US + UK entities). Creative apps Facetune, Photoleap, Videoleap + LTX Studio AI video. ~$300M rev / $250M ARR, 6.6M+ monthly paying users. 2026: split Facetune (consumer, ~100 staff) from LTX AI unit, cut 75 jobs.

Payment stack — STRONGEST SIGNAL: web checkout already runs THREE PSPs in parallel (Stripe + Adyen + PayPal; Apple/Google Pay via Adyen), confirmed in their own refund policy/ToU, but NO orchestrator — stitched in-house. Plus heavy IAP. Facetune billing complaints: 1.4★ Trustpilot, 350+ (surprise charges, cancel friction, "shadow subscriptions").

Yuno angles: (1) 3 PSPs no orchestrator = in-house plumbing tax (lead angle); (2) IAP fee-escape needs approval-rate uplift; (3) LATAM/APAC traffic (India 10.8%, Brazil 4.4%) no confirmed Pix/UPI; (4) lifecycle complaints; (5) new LTX-2 API = B2B payments surface. Best cases: Rappi, InDrive, Reserva. Part of [[project_ai_apps_batch_2026_06_17]].

## project-linea-directa
*Línea Directa (Colombia, Grupo Elede; venta directa de moda) — inbound vía Susana Awad; Luis Paternina (Dir. Tesorería) + Jesús Cubides; 300K tx/mes CO + 25K PE; llamada 30-sep HECHA; propuesta Google Slides 30-sep (20 slides, sin BC): platform $7.5K + compromiso $7.5K (125K tx) = mínimo $15K/mes, $0.06/$0.05 = $25,250/mes a 325K; pendiente enviarla y confirmar Dale*  
*type: project · last updated 2026-10-01*

Línea Directa S.A.S. (La Estrella, Antioquia; filial de Grupo Elede S.A.S.): confección y venta directa por catálogo + e-commerce; marcas Carmel, Pacifika, Loguin, Real Human y Casalma (hogar). Web lineadirecta.com.co, LinkedIn linkedin.com/company/l%C3%ADnea-directa-s.a.s. No confundir con Línea Directa Aseguradora (España).

**Origen:** inbound trabajado por Susana Awad (SDR). Reunión Susana + Luis + Jesús ~23-sep-2026 (sin Gong ni transcript encontrados; Glean con token inválido). Susana pidió datos el 23-sep y compartió el brochure; el 24-sep sumó a German al hilo "Pasos a seguir Linea Directa x Yuno" para el overview del dashboard y una propuesta aterrizada.

**Contactos:** Luis Guillermo Paternina Vergara, Director de Tesorería (luis.paternina@lineadirecta.com.co, tel 604 4485533); Jesús Hernando Cubides Ballesteros, Gerente USC (jesus.cubides@lineadirecta.com.co).

**Datos dados por Luis (24-sep):** ~300.000 tx digitales/mes en Colombia + ~25.000 en Perú; países iniciales Colombia y Perú; medios actuales Nequi, Daviplata, Wompi, PSE, Dale, App Bancolombia (quieren esos mismos + los del pool de Yuno y revisar tarjeta débito/crédito); en Perú, Yape; ticket promedio COP 180.000 / PEN 200; integran vía API o web service. Caso de uso: checkout para recaudo digital (cobro a su red de vendedoras/asesoras por catálogo, inferencia ⚠️ verificar en la call).

**Estado 24-sep-2026:** Luis aceptó el miércoles 30-sep 2:00 pm COT (12:00 pm PT, German ya en SF) para la intro de German + demo del dashboard; Susana debe mandar la invitación. Fila lista para el Deal Status GTM (Status "Demo") en Lists & ICP/Pipeline Sync/manual_adds/.

**Why:** cuenta colombiana de volumen alto en APMs locales (Nequi, Daviplata, PSE, Bre-B) y expansión a Perú (Yape); ángulo = un solo checkout/integración para todos los métodos locales de CO y PE + ruteo, no venta de tarjetas.

**How to apply:** antes del 30-sep, armar brief con /meetingbrief; preguntar quién procesa hoy cada método (Wompi como agregador?), si el recaudo es B2B2C (asesoras) o B2C, y volúmenes en pesos. Relacionado: [[project-unicef-colombia]] y [[project_experian]] (misma ola de cuentas colombianas de recaudo), [[project-sf-relocation-fall-2026]].

**Llamada 30-sep-2026 HECHA (31 min; German + Susana con Luis y Jesús).** Transcript de Meet ilegible y Fireflies no fue admitido: solo existen las notas resumidas. Lo nuevo: venta por catálogo, ~150.000 clientes por campaña (ciclos de 21 días, 18 al año); el cliente paga el saldo en un portal de pedidos antes de volver a pedir (botón de pago, no carrito); mix ~70% digital / ~30% físico (Efecty, Gana, Supergiros, corresponsales); Nequi ~55% del total; integraciones hoy = PSE directo, Bancolombia/Wompi directo, Nequi vía plataforma; sin tarjetas y sin PCI (checkout alojado por Yuno); estructura = cuenta matriz + subcuentas Colombia y Perú; Yuno solo orquesta, no entra en el flujo del dinero. German dijo en la llamada ~$15K de platform y ~$0.07 a $0.08 por tx; Luis prefiere cargar más al variable. Next steps: German envía propuesta con lista de métodos de CO y PE; Susana agenda la revisión.

**Propuesta construida 30-sep-2026 (Google Slides):** https://docs.google.com/presentation/d/126rE0knbVczAsHtRVCtRWopV4lOh3yrKx5038hhjdew/edit (carpeta Drive "Línea Directa"). Copia del deck de Palco, 22 slides (S16 nuevo = métodos de pago CO y PE); notas en Deals/Línea Directa/linea-directa-proposal-2026-09-30.md, scripts en Deals/Línea Directa/build/ (model.py tiene toda la aritmética). **Pricing dictado por German:** sin conciliación ni productos extra; $0.06 tramo 1 y $0.05 tramo 2; orquestación, monitores y network tokens abajo como "opcional para revisar después". Platform $15,000 (el de la llamada) y corte de tramo en 150,000 los puse yo: a 325K tx = $32,750/mes ($393K/año, $0.101/tx). BC: base $211M/año (TRM 3,341.23 y SBS 3.45); L1 pagos Colombia +1%/+2% ($1.94M/$3.88M), L2 pagos Perú ($174K/$348K), L3 5 a 10 bps ($106K/$211K), L4 integraciones 6 a 1 ($25K/$44K); total $2.24M/$4.48M. ⚠️ Ahorro duro (L3+L4) no cubre el fee; el caso depende de L1. ⚠️ Dale NO aparece en el catálogo público de Yuno (docs.y.uno/reference/payment-type-list): el deck dice "en validación", confirmar con Producto. ⚠️ Moda = M4 en la Pricing Policy: validar zona en el calculator y Salesforce. Logo oficial = "Eledé Línea Directa" (lineadirecta.com.co redirige a elede.com.co). Ver [[yuno-pricing-policy]], [[project-palco-ticketing]], [[project-cruz-verde]].

**Pricing v2 (30-sep-2026, tarde, instrucción de German):** platform fee $7,500 + compromiso mínimo de $7,500 en transacciones (= 125,000 tx exitosas a $0.06) = facturación mínima mensual $15,000; tramos $0.06 / $0.05 con corte en 150,000 (el corte sigue siendo supuesto mío). A 325K tx = $25,250/mes ($303K/año, $0.078/tx). Aplicado con build/fix2_commitment.py. **German editó el deck a mano y QUITÓ la sección de Business Case**: quedan 20 slides, agenda = ¿Por qué Yuno? / Conexiones en Colombia y Perú / Propuesta; métodos = S13, pricing = S15. No reintroducir el BC ni re-correr build_ld.py.

**Pricing v3 (1-oct-2026, instrucción de German):** orquestación y smart routing INCLUIDOS en el platform fee; franja inferior del slide de pricing = conciliación opcional a $1,000 fijos/mes por 200,000 trx conciliadas + $0.03 por trx conciliada adicional (interpretación mía del pack + excedente, sin confirmar); monitores y network tokens siguen opcionales sin precio. Aplicado con build/fix3_orchestration_recon.py. Deck en 21 slides (German sigue editando a mano; pricing = S16): antes de tocarlo, comparar contra el último JSON para no pisar sus cambios. ⚠️ Fijo de conciliación $1,000 < mínimo de política ($1,500/mes).

## localiza-andre-aires
*Localiza re-engagement — André Aires, LinkedIn group message with Alejandro after missed H1 call*  
*type: project · last updated 2026-07-27*

Localiza (Brazilian car rental giant) account. Contact: André Aires. A call was scheduled in early 2026 (H1) but never happened. Re-engagement play (July 2026): joint LinkedIn group message from German + Alejandro, warm tone, asking for a 30-minute payments conversation, with a graceful out if timing is wrong. Message sent in English.

## lucky-agent-yuno-agents
*Lucky" = agente creado en la plataforma Yuno Agents (2026-09-09); deal strategist BD entre discovery call y demo; produce MEDDIC doc + account plan desde transcripts/Granola + research*  
*type: project · last updated 2026-09-09*

Alguien del equipo de German (no German) creó el agente **Lucky** en la plataforma interna **Yuno Agents** (visto 2026-09-09). German quiere editarlo; el creador es el owner. Estado RUNNING, tipo SERVICE, visibilidad Public, Language Guard On.

**Qué es:** deal strategist para el equipo BD de Yuno. Vive entre la discovery call y la demo. Toma transcripts de llamadas (y resumen Granola si existe) + research propio de la compañía y produce los artefactos de qualification/prep que BD y SE necesitan para una demo fuerte.

**Entregables:**
1. Documento MEDDIC, cada elemento poblado solo con lo dicho en la call o verificable por research. Donde falta evidencia, declara el gap y escribe la pregunta específica que lo cerraría + a quién hacerla.
2. Account plan: opportunity overview, personas y roles en la decisión, setup actual de pagos (providers, acquirers, métodos, regiones, volúmenes, flujos), noticias recientes, detalles no obvios, blockers/riesgos/prioridades competidoras.

**Tono:** colega senior escribiendo prep notes para otro colega senior. Directo, específico, sin preámbulo.

**Modelo:** DeepSeek V4 Pro vía OpenRouter (acceso: OpenRouter, OpenRouter your key, Baseten). Configuración disponible: Toolkits, Skills, Channels, Scheduled tasks, Evals.

**Why:** el equipo quiere automatizar la prep post-discovery (MEDDIC + account plan) que hoy hace a mano o con Claude en esta carpeta. Lucky es la versión "producto interno" de ese flujo.

**How to apply:** si German pide briefs MEDDIC o account plans, preguntar si van para Lucky (prompt/skill del agente) o para uso directo. Mantener los mismos principios que aplican aquí: solo hechos verificados, omitir lo que no se puede probar ([[no-false-info-disclaimer]]), tono senior sin preámbulo, estructura RBP donde aplique ([[rbp-methodology]]). Relacionado: [[meeting-brief-skill]], [[meeting-brief-structure]].

## project-lululemon
*Lululemon account — Eric Mei (PM Payments) sole contact; NA PSP assessment is the door; Mexico company-operated (direct) since Sept 2024, lululemon.mx*  
*type: project · last updated 2026-10-01*

Lululemon Athletica (apparel, Vancouver). Contact: **Eric Mei, Product Manager Payments** (emei@lululemon.com, Vancouver; career: Retail Commerce & Payments Specialist > Global Payments Specialist > PM Payments, Omni & Retail Tech). Met at Stripe Sessions booth 214 (2026-04-30), deck: ss26.yuno.tools/m/lululemon-athletica.

Key dynamic (May 1 2026 email): orchestration evaluation **deferred until after their NA PSP assessment**; "Yuno is on my radar". Warm, replies fast when topic = PSP assessment. Open item: he never shared the assessment questionnaire (asked 2026-07-10). First call held 2026-07-29 (German + Susana Awad + Samuel).

Company context (mid-2026): interim co-CEOs Meghan Frank (CFO) + Andre Maestrini, CEO search ongoing; FY26 guidance cut, stock ~-43% YTD, ~$380M gross tariff hit; EU e-com via ESW MoR; NA methods incl. Klarna/Afterpay/PayPal/wallets. Angle: help run the PSP assessment (respond to questionnaire, production bake-off between finalists via orchestration), margin-recovery framing.

Global footprint (10-K FY2025, period ended 2026-02-01, filed 2026-03-17):
- **Mexico = operación directa bajo marca lululemon.** El 2024-09-10 lululemon adquirió las tiendas/operaciones de su licenciatario mexicano (Grupo Exalta, 15 tiendas). Hoy 26 tiendas propias + ecommerce lululemon.mx (lanzado 2023). Los pagos de México cuelgan del stack corporativo, no de un distribuidor.
- Tiendas propias (feb-2026, total 811): US 379, CA 71, MX 26, CN 172, AU 34, KR 22, HK 11, JP 10, SG 9, NZ 8, TW 7, MY 5, TH 5, Macao 3; EMEA: UK 20, DE 9, FR 6, IE 4, ES 3, NL 2, SE 2, IT 1, NO 1, CH 1.
- Licencia/supply (marca lululemon, operador tercero): UAE 13, Saudi 9, Israel 8, Kuwait 4, Qatar 4, Turquía 3, Bélgica 2, Baréin 1, Dinamarca 1. Online Medio Oriente = lululemon.me operado por Majid Al Futtaim.
- Ecommerce: shop.lululemon.com (US/CA), lululemon.mx, sitios país APAC, lululemon.eu (EU, vía ESW MoR), China WeChat + Tmall/JD; marketplaces regionales Zalando, Lazada, SSG.
- Expansión 2026 (PR dic-2025): Grecia, Austria, Polonia, Hungría, Rumania (online vía lululemon.eu) + India (marketplaces Tata CLiQ).

Deck "Lululemon - Connections CA/USA" (2026-07-29): deck.yuno.tools/m/lululemon-connections-ca-usa, 6 slides custom (Cover, Canada detail, Our Connections in Canada, US detail, Our Connections in USA, CTA) vía LULU_CONNECTIONS_ORDER en SlideViewer/PrintViewer. Listas de providers CA/US verbatim del sheet de German. No toca el deck lululemon-athletica.

**Update 2026-08-20:** la call del 29-jul (Eric + German/Susana Awad/Samuel) **no tiene transcript utilizable**, tanto Fireflies como el transcript nativo de Google Meet capturaron solo 8 segundos. Gong grabó la call completa pero no hay acceso a Gong desde las herramientas disponibles, esta es la única fuente real (junto con el recap que German le envió a Eric). Lo que sí se confirmó: el "NA PSP assessment" es en realidad una **migración activa** a un nuevo proveedor en NA, no solo una evaluación. Stack confirmado: NA = **JPMorgan Chase (acquirer) + Aurus** (plataforma en tienda, ortografía sin confirmar, también aparece "Auris"), internacional = **Adyen** (con "cierta insatisfacción" según Airwallex). Esto reemplaza el supuesto previo de Adyen como PSP único global. Ventana real para Yuno: FY27 AOP, se confirma en septiembre 2026. Para profundizar piden NDA "cuando sea apropiado", no enviado aún. ⚠️ **Airwallex está corriendo una conversación paralela sobre la misma cuenta** (sync 05-ago con Jaime Kingston/James Simpson), posicionándose como opción de compra (wallet "arri", 360 routing, pricing de success fee), coordinando con Yuno pero sin resolver quién es dueño del contacto con Eric vs. con "David" (contacto internacional, sin apellido confirmado, solo conocido vía Airwallex). ⚠️ Info contradictoria sobre el CEO: un doc de abril dice Heidi O'Neill (ex Nike) entra el 8-sep, otro doc de julio dice co-CEOs interinos Meghan Frank + Andre Maestrini desde feb-2026, ninguna corroborada por tercera fuente, verificar antes de mencionar en vivo. Siguiente paso: Eric confirma en septiembre si avanza, seguimiento interno asignado a Magdalena Torrealba sin fecha específica.

**Update 2026-09-22 (hilo "Lululemon Athletica + Yuno at Stripe Sessions", Gmail):** Eric lleva mudo desde el 30-jul ("provide an update after AOP is confirmed in September"). Toques de septiembre sin respuesta: German 9-sep (circle back + cc Will Wong, Head of Account Management NA en Toronto, que conoce a Eric y a Zoe Denom de antes) y Will 14-sep (menciona "orchestration on pinpads" y ofrece café en Vancouver el lunes 21-sep). Gong no devuelve nada para la cuenta (ask_account = 0 calls). 22-sep: German manda nota corta por LinkedIn ("pendiente de cuándo reconectar"), canal distinto al email para no saturar. Siguiente hook posible: German en SF desde el 28-sep (ver [[project-sf-relocation-fall-2026]]), Vancouver queda cerca para un presencial.

**Update 2026-10-01:** Eric sigue mudo (nada en Gmail ni Slack; sin noticia de que el café de Will del 21-sep haya ocurrido). FUP soft **en borrador** en el mismo hilo (reply sobre el mensaje de Will del 14-sep, to Eric, cc Will + Justo): sin presión por el AOP, pide una nota corta cuando haya claridad de FY27 "even if the answer is not this cycle", y menciona que German está en SF hasta inicios de noviembre (misma zona horaria, vuelo corto a Vancouver para un café). Es el 4º toque sin respuesta desde el 30-jul; si tampoco responde, pausar hasta que haya un trigger nuevo.

## project_magdalena_bc_campaigns_sep_2026
*Campañas de business case de Magdalena (Magnific/Freepik, T-Mobile, Best Buy) donde German va en CC; 26 follow-ups ENVIADAS 17-sep 17:07-17:15 UTC (antes decía en borrador) desde 2026-09-17, cero respuestas*  
*type: project · last updated 2026-09-18*

Magdalena Torrealba (Global Sales Strategy Associate) corrió tres campañas de business case y en el follow-up presentó a German para pedir llamada. Ningún contacto había respondido al 2026-09-17.

**Magnific (Freepik, Málaga)** 8 contactos: Ignacio (nacho.marcos@), Alejandro (agomez@), Antonio (ajerez@), Francisco (fcastro@), Marina (mlara@), Omar (opera@), Javier (fgonzalez@), Pablo (pnegre@) @freepik.com. Hilo "Sharing the Magnific Business Case" (25-27 ago + FUP 15-16 sep). Tesis: todo factura desde España en euros por un solo gateway con Chargebee encima; top 5 mercados India, Brasil, US, Indonesia, Colombia sin adquirencia local ni APM local; upside ~$18M/año (floor). German ya les había escrito a Pablo, Alejandro, Francisco y Omar en jun-jul 2026 (deck deck.yuno.tools/m/magnific + "Should I be reaching to someone else?") sin respuesta.

**T-Mobile** 18 contactos (@t-mobile.com): Solange Sanderson, Reid Erickson, Kym Bowen, Sailesh Chaudhary, Abdallah Aldajaa, Brandon Screen, Hassen Ayed, Kristen Weaver, Peter Osvaldik, Bryan-Earl K, john@ (genérico, 2 hilos duplicados), Anshul Saxena, Leslie Lagan, Chris Hooppaw, Jonathan Bowden, Irada Abasova, Tristan Liabraaten, Ron Comeau (hilo ya leído). Hilo "The Math on T'Mobile's Payment Stack" (21-24 ago + FUP 28 ago/2 sep). Tesis: postpaid checkout, AutoPay mensual y Metro son 3 superficies separadas sin capa que recupere declines; palanca mayor = recurring recovery (retry de renovaciones AutoPay + network tokens + account updater); floor ~$402M/año. Ángulo nuevo de German (17-sep): subscription engine relanzado, 16 merchants y 135K+ suscripciones activas.

**Best Buy** 1 contacto: Paul Mueller (paul.mueller@bestbuy.com). Hilo "Sharing a tailored payment analysis for Best Buy" (24 ago + FUP 2 sep). Tesis: checkout + marketplace Mirakl + Stripe agentic sin capa única; floor ~$429M/año.

**Estado 2026-09-17:** 26 borradores de German creados en Gmail dentro de cada hilo (CC Magdalena), proponiendo llamada la semana del 21-25 sep con días ajustados a su calendario. Pendiente que German los revise y envíe. ⚠️ Los FUPs de Magdalena citaron por error el correo de "Hi Pablo" en los hilos de otros Freepik y "Hi Adam" en el de Paul; avisarle.

Relacionado: [[feedback_gmail_workflow]], [[feedback_gmail_update_draft_detaches_thread]].

## project_mcafee_psp
*McAfee payments research — MoR (Digital River) collapse + in-house billing build = lead angle*  
*type: project · last updated 2026-09-08*

McAfee (consumer cybersecurity, private since Mar 2022 Advent/Permira ~$14B; sold enterprise → Trellix 2021). Research brief: Documents/GERMAN CLAUDE CODE/GTMCoding/data/research/mcafee-2026-07-23.md. ICP score 🔴 High (14).

**Killer angle (NOT "you lack an orchestrator"):** McAfee billed via **Digital River as merchant of record** ("DRI*" descriptor). **Digital River collapsed/insolvent Jan 2025**, forcing a billing re-platform; replacement MoR/PSP is undisclosed. Simultaneously McAfee is **hiring a Group PM Subscription Payments + Commerce/checkout/payments-&-fraud + Subscription Mgmt Platform PMs** = building billing in-house right now. Pitch = MoR-exit / buy-vs-build the orchestration + recovery layer, avoid a new single-vendor dependency.

**Supporting pains:** structural auto-renewal / involuntary churn ($80M class-action 2016, UK CMA 2021 refund enforcement, continuous Trustpilot complaints). Global tails India 8% / Japan 8% / Brazil 4% = local-method + cross-border acquiring angle. Confirmed APMs: Visa/MC/Amex/Discover/JCB/PayPal (never claim others missing).

**Topology verified in live checkout (Magdalena QA, Sep 2026 — deck updated to match):** Digital River is GONE from the deck. Current rails observed across US/DE/IN/BR/JP: Braintree (PayPal rail), EBANX (Brazil), local processing (Japan), Apple IAP (iOS), Google Play (Android); card acquirer not publicly identifiable (server-side via McAfee's own endpoint). Offered APMs now include PIX, Boleto, Elo, UPI Autopay, Net Banking, PayPay, Konbini, SEPA, Lastschrift. Missing in own checkout: Apple Pay / Google Pay (wallets only inside app stores), Venmo, Cash App Pay, ACH, Klarna/Affirm (US). Top markets (SimilarWeb Jun 2025–Jun 2026): US 32.3%, IN 8.6%, JP 5.8%, DE 4.2%, UK 4.0%. Note: slide-5 capability card descs in the Supabase row still mention "Digital River stack" (Magdalena's edit list didn't cover them).

**Buyer map (all ex-Experian, ROI/identity-fluent):** CPEO Joe Manna owns product+eng (payments rolls up here), CFO Brian Herb owns auth-rate/cost, CEO Craig Boundy. Practitioner champion = the Group PM Subscription Payments. See [[reference_buyer_personas]].

## project-meeting-brief-skill
*Skill nuevo de meeting briefs (v2) en construcción — plantilla basada en el brief de Riot optimizada; ejemplo demo en Google Doc; pendiente escribir el skill*  
*type: project · last updated 2026-08-03*

**Skill CREADO y commiteado 2026-08-03:** `.claude/commands/meetingbrief.md` (`/meetingbrief <company>`; renombrado desde meeting-brief el mismo día). Flujo: (1) buscar la reunión en Google Calendar por company name (la próxima que haga match; flags si el externo no está en el invite), (2) research interno (memoria + data/research + Gmail + Gong opcional) y externo en paralelo, (3) brief v2 en dos zonas, (4) output SIEMPRE Google Doc vía Drive create_file text/html, sin carpeta (German lo reubica), + copia markdown en data/research + commit. Opción A aprobada por German. Ejemplo demo: Google Doc "TEMPLATE EXAMPLE: Meeting Brief v2 (Riot Games demo)".

Decisiones ya tomadas:
- Estructura según [[feedback-meeting-brief-structure]] (agenda + preguntas al final con espacio de notas, TL;DR battle card al inicio).
- Contenido mínimo: noticias de la empresa, temas/estrategia, qué hace, subsidiarias/estructura corporativa, quién va a la reunión + qué hacen + qué han hecho, payments stack, sales angle, sección "Be ready for" (qué le pueden preguntar a German, con respuestas), checklist post-meeting.
- Research pipeline se hereda del skill meeting-prep existente (Gmail thread, calendario, research briefs locales en data/research/, memoria, web) pero el output template cambia al v2.
- Reglas transversales que el skill debe respetar: no em-dashes, nunca decir al prospect que "le falta" algo, solo hechos verificados (marcar inferencias), evidencia con fechas, fuentes al final.

Base de referencia: data/research/riot-games-meeting-brief-2026-07-31.md + doc de Riot en Drive.

## milo-intro-routine
*Rutina cloud \"Milo Intro-Reply (Gmail)\" (trig_01SW3DdQ2gYYkPgpGLkp6ujf) corre cada hora L-V 8am-6pm COT; ejecuta Milo/intro-reply-single.md del repo GitHub; Gmail conectado a nivel claude.ai*  
*type: project · last updated 2026-08-25*

Rutina cloud programada (2026-08-06): **Milo Intro-Reply (Gmail)**, id `trig_01SW3DdQ2gYYkPgpGLkp6ujf`, https://claude.ai/code/routines/trig_01SW3DdQ2gYYkPgpGLkp6ujf

- Cron `0 13-23 * * 1-5` UTC = cada hora en punto, lunes a viernes, 8:00 a 18:00 Bogota. Minimo permitido por la plataforma es 1 hora (German pidio 30 min; imposible).
- Modelo claude-sonnet-5, repo fuente github.com/germantatism/German-GTM-Coding. El agente cloud NO ve el Mac de German, solo el repo: **Milo/intro-reply-single.md debe estar pusheado** (el prompt tiene guard: si el archivo no existe en el repo, la corrida termina en no-op reportando "esperando push").
- El prompt de la rutina es un bootstrap delgado: lee Milo/intro-reply-single.md (fuente de verdad, editable sin tocar la rutina) y ejecuta Flujo A (detectar intros de Magdalena → borrador → pedir OK) y Flujo B (procesar OK → enviar al lead). Safety en el prompt: nunca enviar a lead sin OK de Magdalena, labels Milo-Intros/* como estado, version de Magda VERBATIM, si Gmail no esta disponible terminar sin actuar, si solo hay drafts reportar como pendiente.
- Conectores adjuntos automaticamente al crear (todos los de la cuenta): **Gmail SI esta conectado a nivel claude.ai** (uuid e2ff4c73), aunque en sesiones locales aparezca como "requiere auth". Tambien Slack, Drive, Calendar, Atlassian, Excalidraw.
- Editar la rutina: skill /schedule + RemoteTrigger (update con trigger_id). Borrarla: solo via https://claude.ai/code/routines
- **Test 2026-08-06:** 3 corridas disparadas; el correo [MILO] a Magdalena NO llego. Repo verificado clonable en el ultimo commit (descartado como causa). Hipotesis principal: token OAuth del conector Gmail EXPIRADO a nivel claude.ai (en sesiones locales Gmail aparece "requiere auth" desde 08-05) → las corridas terminan con "Gmail no disponible". Fix: re-autorizar Gmail en claude.ai/customize/connectors y re-disparar.
- **⚠️ El repo German-GTM-Coding es PUBLICO en GitHub** (verificado 2026-08-06, HTTP 200 sin auth) y contiene transcripts de calls, contactos y datos de deals (Riot, Eventbrite, Flair). Recomendado pasarlo a privado; verificar despues que la rutina cloud siga pudiendo clonarlo (GitHub App de Claude con acceso al repo).
- Skill fuente: [[eventbrite-bakeoff]] no relacionado; el skill Milo vive en Milo/ del repo GTM (single-file + version empaquetada intro-reply/SKILL.md).
- **⚠️ INCIDENTE 2026-08-25: la rutina quedo DESHABILITADA (enabled:false) por esta sesion, pausala solo con autorizacion de German.** Se crearon 26 drafts (forwards de emails de julio a magdalena.torrealba@y.uno para revision interna, ninguno debia enviarse). Entre 20:54 y 21:02 UTC, 13 de esos 26 aparecieron como REALMENTE ENVIADOS (label SENT) a Magdalena sin ningun OK de German, y los otros 13 desaparecieron por completo (no estan en drafts, no en sent, no en trash de hoy, probablemente borrados permanentemente via drafts.delete). El run de Milo de las 20:03 (cse_019qdA297ivJrg3T7kZC17SE) coincide en ventana de tiempo pero su log solo muestra "mcp_auth_required" y arranque de entorno, sin tool-calls visibles de Gmail, asi que la atribucion exacta a Milo NO esta 100% confirmada, solo es la hipotesis mas fuerte por timing y porque el unico proceso automatizado con acceso a Gmail + drafts dirigidos a Magdalena es este. Antes de reactivar: revisar los run logs completos en claude.ai/code/routines, y considerar que Flujo A/B de Milo puede estar tratando CUALQUIER draft dirigido a magdalena.torrealba@y.uno como si fuera su propio flujo de intros, no solo los que el crea.

## project_money2020_lv2026_tcl_match
*Money20/20 Las Vegas 2026 (18-21 oct): cruce de la lista de asistentes de Susana contra la TCL; Google Sheet entregado 5-oct; segunda pasada de LinkedIn pendiente*  
*type: project · last updated 2026-10-05*

Money20/20 USA 2026, The Venetian Las Vegas, 18 a 21 de octubre de 2026 (owner del evento: Susana Awad). Lista de asistentes: Google Sheet `1RTXjsf2fzSNOrl2jBRuXaAdP5JZkg0rBhUPpQn4v5Vg` (pestañas Raw List Tiered = universo 6,536 personas; Enriched Merchant List / General Attendees / Important Attendees / Confirmed Meetings traen LinkedIn y email).

Cruce hecho el 5-oct-2026 contra la TCL (Final List + TCL_v2 + TCL + Backups): 71 empresas en ambas listas, 350 personas, 121 con LinkedIn. Entregado en Google Sheet `1R0GJ0h4vLTi4CrLhwvoklBtxnRry0zmD0IMxZWkiiSo` (una pestaña: Matches + bloque NOTAS al final). Copia completa de 3 pestañas en `Events/Money2020 Las Vegas 2026/Money2020_LV2026_x_TCL_matches.xlsx` del repo, con scripts `match.py` y `build.py`.

Homónimos descartados (NO son la empresa de la TCL): Titan, Branch, Nomad, Circle/Circle Internet Group/Banking Circle, Republic Bank, Indigo, Bloomberg (reportera), Vested (PR), EDX Markets, "Max" (= MaxMyInterest, no HBO Max). Rain mezcla dos empresas (Rain EWA de Alex Bradford = TCL; Rain stablecoin cards de Farooq Malik). Amazon agrupa AWS (21 personas de ventas FSI).

Asisten pero no están en la TCL: Super.com (3), Arrive (Debbie Guerra + Amit Chhabra), Mercado Pago/Libre, Nubank, Samsung (11), Waymo, Collinson, Google (36), Microsoft. Reuniones ya confirmadas por el equipo: AWS (Bikram Saha), Tesla (Howard Ro), Samsung, Collinson, Amazon (Preethi Ravisankar); Waymo en FUP.

**Pendiente:** segunda pasada de LinkedIn para ~180 personas que quedaron sin buscar (tope de 200 búsquedas web por sesión, ver [[feedback_websearch_budget_shared]]). Truco que funcionó: WebSearch con allowed_domains ["linkedin.com"] + fragmento del cargo. Relacionado: [[project_hbo_max]], [[project_arrive]], [[project_super_contacts]], [[project_tcl_agent]].

## project-money2020-must-talk-list
*Money20/20 Las Vegas 2026 (18-21 oct): lista 'sí o sí' de German cruzando asistentes × TCL × deals propios × dueños internos; quién NO tocar porque ya tiene dueño en Yuno*  
*type: project · last updated 2026-10-05*

Armada 5-oct-2026 con la hoja de asistentes de Susana (Raw Merchant List 660 filas, Enriched 179, Important/Confirmed), el cruce con la TCL (71 empresas) y Gong. Ver [[project_money2020_lv2026_tcl_match]].

**Tier A, deals de German con gente senior en Vegas:**
- HBO Max/WBD: Ashwyn Singhal (Sr Director Payments, decisor global, nunca respondió) + Spencer Case, Eric Fishman, Kyle Evans, Rachel Bourne. Borrador "coffee between sessions" pendiente de enviar ([[project_hbo_max]]).
- DoorDash: A.J. Tus (Head of Payments & FinTech Partnerships) + Billy Kim (Dir Finance & Strategy). ⚠️ Gong: Rasheed lleva el outreach (último toque 22-may-2026, sin opp formal pese a "Open Opportunity" en TCL); coordinar con él. Invite supercar en borrador ([[project-doordash-aj-tus]]).
- Fareportal: Nipun Joshi (AVP Product & AI Experiences) + Leon Mulder (Sr Dir Partnerships): puerta nueva hacia Naveen ([[project-fareportal]]).
- FanDuel: Michael Petersen (VP Payments & Risk Ops) + Franco Mezzadra (Dir Payments & BizOps). Deck + research listos ([[project_fanduel]]).
- Arrive: Debbie Guerra (Head of Payments); intro pedida a Amit vía Susi ([[project-arrive]]).
- Super.com: Rick Galasieski (SVP/GM Payments & Fintech), Joanna Moroz (CoS Fintech), Gage Sonntag (Head of Data); Akshay no va ([[project_super_contacts]]).

**Tier B, cuentas grandes sin dueño con payments leaders presentes:** eBay (Juan M Molero GM Payments, Eduardo Righi GM Financial Services, Renata Camera Santos Head of Wallet, Darwin Lui), TikTok/ByteDance (Zhipeng Jiang Head of Payment, Hua Li Head of Payment Risk, Ankur Singh, Ashley Shen; TikTok Shop MX/BR), Roku (Chris Underwood Sr Dir Roku Pay, dhruv patel, Jason Korosec VP; nota interna "get a dinner with JP"), Yum!/Taco Bell (Balagopal Thachangot Payments PM, Shelly Richardson, Brynn Pearson, Jon Lee), Airbnb (Gerum Haile Chief Payment Architect, Mini Atwal, Yong Rhyu, Rahul Conda Payment Partnerships), Upwork (Roopa Patel Dir Product Payments; ⚠️ Alejandro Bernal es dueño en Gong, frío desde abr-2026), Instacart (Shivendra Kishor Sr Dir Fraud/Reconciliation), Booking Holdings Financial Services (William Matos CEO), OnlyFans/Fenix (Lee Taylor CFO, Chris Hancox SVP Finance Ops), BetterMe (Volodymyr Melnyk Head of Payments), Fresha (Pawel Iwanow CPO), Booksy (Piotr Posadzy Head of Payments), Remitly (Yezy Lim Principal PM, Sundeep Kurcharlapati), United Airlines (Jarad Fisher President MileagePlus), Fanatics (Roy Grinapell SVP), Gen Digital (Ashish Modi Head Corp Dev), Dating.com (Ivan Sharkov Head of Acquiring & Risk), Cover Genius (Gus McDonald CEO, Ehsan Azizi SVP Product), Microsoft (Dean Jordaan Principal PM).
- Coinbase: Briana Gargurevich (Head of AMER Stablecoin Payments) es ex-Yuno; saludar; ángulo stablecoins como método.

**NO tocar (ya tienen dueño o reunión):** Tesla (Justo, confirmada con Howard Ro), Amazon/AWS (JP Ortega + Mauricio, Connections Lounge mesa 8), Samsung (coordinando), Collinson y Waymo (Samuel), Adobe (Samuel, "no need"), Discord (Samuel/Justo/Sean, opp activa, call 9-oct), Copa Airlines ("no need to reach out"). LatAm: iFood (Wallace Barbosa Head Payments), Mercado Pago/Libre, Nubank, Grupo Elektra, Grupo OLX, Lojas Renner → pasar a equipo LatAm. Whop aparece en tooling interno junto a Rappi (posible merchant live): confirmar con KAM antes de abordar. Perplexity, eBay, Upwork y Navan tienen sesión en la agenda (solo AEs de Perplexity en la lista).

**Partners, no merchants:** PayPal (co-host del evento supercar), Google/GPay, Apple Pay, Shopify, Affirm, Cash App/Afterpay, Bitso, Nium, Rain, Kraken, Robinhood, Wise, Chime, SoFi, Western Union, Paysend, Airtm, Yellow Card, Coins.ph.

German no tiene eventos de Money20/20 en su calendario al 5-oct (verificar pase/viaje). Gancho para invitaciones: [[reference-money2020-vegas-2026-supercar-event]].

## neverland-migration
*Decks app DEPLOYED live en Neverland (decks.internal-tools.y.uno, 2026-07-30); service-role key OK (2026-08-03); Railway sigue como dominio de prospectos; pendiente ANTHROPIC_API_KEY + export Railway + OAuth SecOps*  
*type: project · last updated 2026-08-05*

Migración decks Railway→Neverland: **DEPLOYED y validado 2026-07-30** en https://decks.internal-tools.y.uno (health-check 200, decks públicos renderizan, assets OK).

Servicio Kingdom: `decks` (ms_id `bbfe08b3-d14d-4f45-8dfc-d427b31bacf2`, env dev `959e071e-7663-42fd-9f34-3dfd303a567b`), kingdom `neverland`, technology `typescript`, team `sales-representative`, alerting_team `devops` (el deploy FALLA si queda vacío), subdomain `decks`, público: false → deploy directo desde `main` sin tag.

Fixes que lo hicieron funcionar (2 intentos de deploy):
1. Fallback runtime de Supabase (commit 9df8e83): el build de Kingdom NO pasa env vars a Vite → server inyecta `window.__RUNTIME_CONFIG__` (URL + publishable key) en index.html; `src/lib/supabase.js` cae a eso. Railway no cambia (build-time gana).
2. `tsconfig.json` stub (commit 4507fb5): `Dockerfile_typescript.j2` hace `COPY tsconfig*.json ./` y el repo es JS puro → COPY failed.

Config: SUPABASE_URL/VITE_SUPABASE_URL como env vars (API `environment/update` exige `variables` como DICT, no array); VITE_SUPABASE_ANON_KEY en Wilson (Kingdom lo clasifica sensible por "key" en el nombre).

**Why:** Fede Falour anunció la vía oficial en #tech; Railway va a dejar de usarse para los decks.

**How to apply:** RESUELTO 2026-08-03: SUPABASE_SERVICE_ROLE_KEY creada en Wilson (`decks-dev-supabase-service-role-key`, id `4a697fa3-af73-467e-a34b-2e1d79e4722e`) + rollup (`POST /kingdom/v1/deployment/rollup` con `applying_changes:true` sobre el deploy en estado deployed, tarda ~70s) → `/api/builddeck` ya pasa el gate de Supabase. El clasificador puede bloquear el POST del secret; con autorización explícita del usuario en el chat, pasó. ANTHROPIC_API_KEY también RESUELTA 2026-08-03 (Wilson `decks-dev-anthropic-api-key` id `9310a87d-8784-4f50-8a4e-2b4f2a0a78c0`, valor aportado por German + copiado a `.env.local`; builddeck verificado end-to-end con sonda Gopuff→existing:true). RESUELTO 2026-08-05: acceso GitHub restaurado (org exigió 2FA + acceso al repo restaurado por el equipo vía German E. Bravo). Commit `27c5658` (SlideCTA "Copy link" SIEMPRE emite dominio público via PUBLIC_DECK_ORIGIN en src/lib/deckLink.js; fix VPN para prospectos externos) deployado y verificado en vivo en AMBOS: Railway y Neverland (deploy Kingdom 6706a4c1). El token de Kingdom dura ~34h; renovar con Google SSO (`login.sh kingdom`) antes de cualquier operación. Pendientes: (1) resto de export Railway a `.env.railway-backup` (Google OAuth, Gmail senders, SESSION_SECRET, EDIT_NOTIFY_SECRET, GITHUB_EDIT_TOKEN); (3) SecOps #secops_on_schedule: OAuth redirect `https://decks.internal-tools.y.uno/auth/google/callback` + revisión exposición pública; (4) PDF export roto (alpine sin Chromium) hasta PLAYWRIGHT_EXECUTABLE_PATH/CDP; (5) master-vs-main si se vuelve público ([[salesmaker-deploy-branch]]). NO apagar Railway: deck.yuno.tools (CNAME `hsq59i6a.up.railway.app`) es donde apuntan los links ya compartidos; al apagarlo, repuntar o apagar [[railway-watchdog-routine]]. Runbook: `yuno-sales-pitch-maker/docs/NEVERLAND_MIGRATION.md`.

## project_neverland_pdf_export_broken
*PDF export (/api/pdf/:slug) fails on Neverland (decks.internal-tools.y.uno) with a browser-level connection error, while it works fine on Railway*  
*type: project · last updated 2026-08-14*

PDF download of merchant decks fails on `decks.internal-tools.y.uno` (Neverland/Kingdom deployment) with Chrome showing "Site wasn't available" (a connection-level failure, not an app error) — confirmed 2026-08-14 with the eventbrite deck.

**Root cause (likely):** `/api/pdf/:slug` in `server/index.mjs` generates PDFs synchronously using Playwright-core + a real Chromium browser, inline in the same Express process (see [[project_pdf_vw_paper_width]] and [[feedback_pdf_no_transform_scale]] for the rendering approach). This takes ~7-60s per deck. The Railway deployment's Dockerfile is a Playwright base image with Chromium pre-installed. Neverland/Kingdom's generic container build likely does NOT have Chromium installed the same way, so the `getBrowser()` launch or `page.pdf()` call probably hangs/crashes, and Neverland's ingress/proxy drops the connection mid-request rather than surfacing an app-level error.

**Verified NOT broken:** the exact same code works perfectly on the Railway domain — `curl https://deck.yuno.tools/api/pdf/eventbrite` returned HTTP 200, valid 16MB PDF, in ~7.5s (2026-08-14 test). So this is an infra/deployment gap on Neverland, not an application bug.

**Why:** ties into [[project_neverland_migration]] — the migration was explicitly left with "pendiente resto export Railway" (some Railway-specific setup, likely the Playwright/Chromium runtime, wasn't ported to Kingdom yet).

**How to apply:** Until Neverland's container has Chromium properly installed, tell German to use the direct Railway PDF link (`https://deck.yuno.tools/api/pdf/{slug}`) as a workaround — that route is intentionally public/ungated even though the rest of deck.yuno.tools now requires auth. Flag this to whoever owns the rest of the Neverland migration.

## nyt-gus-jacobs
*LinkedIn outreach to Gus Jacobs at The New York Times; NYT already orchestrates payments*  
*type: project · last updated 2026-06-09*

German's LinkedIn outreach to **Gus Jacobs (The New York Times)**.

Thread so far (no reply from Gus): Apr 21 2026 connection thank-you + business case link (deck.y.uno/nyt) + "free by end of week?"; Apr 23 2026 Stripe Sessions nudge. As of Jun 9 2026, still no reply (~7 weeks silent).

**Why:** NYT **already orchestrates payments**, so the pitch angle is decline/renewal recovery, auth-rate uplift on cross-border cards, and "build together" value, NOT "you lack an orchestrator."

**How to apply:** On follow-ups, lead with the lever that applies even to companies already orchestrating (recovering failed subscription renewals + auth-rate on cross-border cards), tie to NYT's public moves, and offer a low-friction value-first CTA (e.g. a short teardown, no meeting). Give an easy out. English (whole thread is in English).

**Verified facts to anchor hooks:** Q1 2026 earnings (recent, strong trigger): +310k net digital subs to ~13.1M total, on track for 15M by 2027, ARPU up on price step-ups + promo-to-full-price transitions, digital sub revenue +16% driven by the multi-product bundle (News/Games/Cooking/Wirecutter/The Athletic). The price-increase angle is the sharpest payments hook: price step-ups spike involuntary churn (declines, failed re-auths), so failed-renewal recovery at the moment of the step-up = direct revenue. All-access bundle and international growth are NOT new (bundle since ~2021, Athletic 2022), so use as context not as a fresh trigger.

**Orchestrator vendor UNCONFIRMED:** German is "almost sure" NYT uses Spreedly, but it could not be verified (NYT is not on spreedly.com/customers; search snippets claiming it were unreliable). NYT does orchestrate (per German's own note) but keep messaging vendor-agnostic until confirmed; do not name Spreedly as fact.

## palco-ticketing
*Palco (ex Palco4, pal.co) white-label ticketing ES+LatAm; deal ACTIVO: demo 9-sep + deep dive 15-sep hechos; reunión de PROPUESTA lun 21-sep 11:00 COT con Patricio+Alfonso+Fernando (+Miguel tentativo); resumen completo en Deals/Palco/palco-deal-summary-2026-09-16.md; TPV $457M, aprobación MX 56-60%; cuentas de procesamiento son de sus clientes*  
*type: project · last updated 2026-09-24*

Palco = **Palco4 Tecnología y Servicios SL** (Madrid), rebrand a "PALCO" en **pal.co**. White-label B2B ticketing: 500+ venues, 30 países, 8M+ tickets/año (Bad Bunny RD, Tini AR, Don Omar MX, Shakira UY 2025). Research: data/research/palco-ticketing-2026-09-08.md. Brief de reunión: data/research/palco-meeting-brief-2026-09-09.md.

**Estado del deal (sep 2026):** demo + payment orchestration review 9-sep. Magdalena Torrealba es la dueña de la relación (1ra call 30-jul, SIN grabación en Gong). German entra como AE. Contrapartes: **Patricio Villalobos Cuevas (CEO y co-dueño, Madrid, +34 669 561085)**, Fernando Nava Feldman (VP Engineering), Javier Sánchez (SSE).

**Lo que ellos mismos mandaron por email (2-sep, confidencial):**
- TPV LTM ~$457M USD, ticket promedio $37.09, ~235,000 tx/mes
- ⚠️ Los tres números NO cuadran: $37.09 es precio por TICKET, la orden lleva ~4 tickets (~$148). La tabla mensual por país omite España, Puerto Rico y Panamá.
- Mix: tarjeta 75.7% ($346M), efectivo/OXXO 13.2%, pinpad taquilla 6.3%, transferencia 3%
- GTV anual: México $211M, Argentina $62M, España $55M, RD $36M, PR $31M
- **Aprobación por procesador**: Openpay MX 58.0%, Banorte MX 59.6%, Santander MX 56.1%, Mercado Pago v2 67.9%, MP Wallet 92.1%, Redsys ES 88.1%, ECI ES 99.7%, UepaPay RD 98%, Fiserv UY 43.7%, **Line VE 8.7%**. Blended 70.85%, 900,120 declines/año.
- Benchmark México: ~72% crédito / 69% débito → **PALCO está 10-16 puntos debajo de su propio mercado**
- Sin dato consolidado de fraude/contracargos: **cada tenant es merchant of record**

**Sus 6 preguntas (la agenda real):** split payments MX con tenant MoR, 3DS obligatorio y su impacto, tokenización/recurrentes para abonos, modelo comercial multi-tenant, API directa sin SDK y alcance PCI, ruteo por BIN para preventas bancarias.

**Ángulo ganador:** ellos ya diagnosticaron el problema y pidieron "ruteo inteligente y reintentos". El frame es **convertir pagos en línea de ingreso de PALCO** (30 bps sobre $457M ≈ $1.37M/año) porque el uplift de aprobación se lo llevan los tenants (son MoR), no PALCO. Nunca decirles que les falta orquestador: construyeron 50+ integraciones in-house y están orgullosos.

**Pricing modelado (GREEN, score 89.5, sin aprobaciones):** $10,000/mes platform fee + $0.0354/tx blended (ladder 3 tramos) = **$18,320/mes ≈ $220K/año**. Hoja "Yuno — Pricing Palco" en Drive. ⚠️ Corregir billing currency (quedó en COP) y recalcular take rate cuando se aclare el AOV real.

Adquirida oct/nov 2025 por **Bocel Private Equity + Patricio Villalobos y Miguel Ramírez Lombana** (ex mediotiempo.com); plan de nuevos mercados LatAm a mediados 2026.

**Deep dive técnico: martes 15-sep-2026, 10:00 a 10:45 COT** (Fernando lo confirmó el 14-sep). Fernando firma como **Technical Account Manager, Palco México (CDMX)** aunque Patricio lo presentó como VP of Engineering. Asisten por Palco: Fernando, **Alfonso Uribarri Carrasco** (co-fundador de Palco4 en 2017, Manager of Development and Support, Madrid; RocketReach sin 2da fuente; dueño de las 50+ integraciones, el más sensible a "reemplazar") y **Alvaro** (alvaro@pal.co, rol desconocido, preguntar). **Patricio NO está en la invitación.** Javier Sánchez OOO del 14-sep a fin de mes. Por Yuno: Carlos Medina (solutions), Joaquin Mann, Magdalena. Agenda: API vs SDK y PCI, split con promotor MoR + tokenización abonos, ruteo MX y BIN para preventas, cobertura BO/VE, más discovery de negocio (fee por ticket y si monetizan pagos, quién es el tenant y quién firma, plan de mercados, piloto MX con baseline, reconciliar $37.09 ticket vs ~$148 orden). Pricing no se presenta en esta sesión. Guía: Deals/weekly-prep-2026-09-14.md.

**Brief del deep dive 15-sep:** data/research/palco-meeting-brief-2026-09-15.md (Google Doc "Meeting Brief: Yuno <> PALCO Technical Deep Dive (Sep 15, 2026)": https://docs.google.com/document/d/1RJsB9UXPm9w3N3H8RgK901ELrjvB40OAwLrIDG4zfp4/edit), con sección 0 "What you must know cold" (20 hechos). Carlos Medina = **Implementation Engineer** (Bogotá); confirmó por Slack el 14-sep pero pidió que le recordaran el objetivo (lo confundió con ProntoPaga): hay que briefearlo antes de la call. Objetivo dicho por German a Carlos: "deep dive en el dashboard y hablar de cómo funcionaría la integración". Pendientes técnicos que Carlos debe verificar antes: modelo multi-tenant en Yuno (cuenta por tenant vs una cuenta con ruteo por tenant), conectores en catálogo para Openpay/Banorte/Santander/MP/Redsys/Cybersource/Authorize.net/Fiserv y ausencia probable de Line VE, Pixel Pay HN, Recurrente GT, Bancard PY, UepaPay DR, ECI ES; split al capturar con tenant MoR por procesador mexicano; recurrencia con procesadores MX.

**Deep dive técnico 15-sep-2026 HECHO (48 min, Fireflies).** Por Palco: Alfonso Uribarri (Madrid), Fernando Nava (TAM, CDMX), **Álvaro García Torres** (alvaro@pal.co). Por Yuno: German, Carlos Medina (demo del dashboard), **Joaquin Mann (BDM NA, mexicano, se unió la semana del 7-sep, German lo suma a reuniones)**, Magdalena. Transcript: Deals/Palco/palco-call-transcript-2026-09-15.md.

**Lo que corrigieron del modelo (Alfonso):** las cuentas de procesamiento son de SUS CLIENTES (partners por país), no de Palco; en el 99% de operaciones el cliente recauda y liquida mensualmente a Palco (fee por ticket o precio fijo por evento). Palco quiere cuentas propias en MX/Europa "eventualmente". Interés #1 (Fernando): acceder a integraciones de métodos de pago sin construirlas. Fricción #1 (Alfonso): el costo se traslada al cliente final y sus clientes eligen pasarela por precio, no por seguridad; esperan que el ahorro por ruteo compense. Sus clientes se autoconfiguran llaves → quieren cargar credenciales por API (existe organization API). Preguntaron split de pagos (fee a una cuenta, ticket a otra) y panel en tiempo real para on-sales. Integración: 90% SDK. Feedback Alfonso: "bastante logrado, fácil de configurar y bastante completo", "me ha gustado bastante".

**Dos modelos sobre la mesa (German):** white label (fee fijo + variable) vs solo conexión (solo variable). Alfonso: marca blanca con comercio propio de Palco para recintos grandes y clubes deportivos (clientes nuevos); proveedores locales actuales difícil de cambiar. ⚠️ German dijo en la call "alrededor de $15K como fee mínimo mensual" (el modelo interno es $18.3K); Alfonso asumió rango $15K a $30K mensual.

**Follow-up 15-sep ENVIADO** (16:28Z, reply al thread "Palco + Yuno - Próximos Pasos", to Patricio+Alfonso+Fernando+Álvaro, cc Magdalena+Carlos): sandbox ya enviado por Carlos (Fernando usuario principal), docu SDK + API, y 4 opciones de fecha. ⚠️ El correo enviado dice "Inicialmente, veremos a Yuno como una solución directa para sus clientes actuales" (NO menciona los dos modelos que sí estaban en el borrador local). Fernando eligió **lunes 21-sep 11:00 COT**. Patricio 16-sep: "looking fwd man a la propuesta 👊🏽".

**Reunión "Palco + Yuno | Propuesta": lun 21-sep-2026, 11:00 a 11:45 COT (10:00 CDMX, 18:00 Madrid).** Aceptaron Patricio, Fernando, Alfonso y Joaquin; **Miguel Ramírez Lombana (mike@pal.co) tentativo**. Magdalena y Carlos NO están invitados. German + Joaquin bloquearon "Propuesta PALCO" interno el mié 16-sep 13:15 a 15:00 para armarla. Javier Sánchez OOO hasta fin de mes.

**Lectura interna post deep dive (Carlos, Slack 15-sep):** "los vi bien, interesados"; fase 1 más sencilla = que usen a Yuno para crear conexiones y routing "como un proveedor", checkout de sus merchants sobre nuestro SDK, "ningún rollo con la integración". German: "lo veo igual". Gong ahora sí tiene la call del 15-sep (id 891469394762814345) bajo la cuenta CRM "Palco4" (001Ps00001VqkdvIAB); la cuenta "Palco" (001Ps00001qNjCWIA0) solo tiene emails.

**Resumen completo del deal (sin números, para armar la propuesta):** Deals/Palco/palco-deal-summary-2026-09-16.md. Cabos sueltos que la propuesta debe cerrar: modelo (solo conexión vs ambos), precio que resista "el cliente final no paga más", reconciliar ticket vs orden, alinear el número dicho en call ($15K) vs modelo ($18.3K), piloto MX con baseline, pendientes técnicos de Carlos (split al capturar por procesador MX, recurrencia MX, cobertura de catálogo), permiso GoFundMe, quién presenta.

**Propuesta comercial v1 construida 2026-09-16 (Google Slides):** https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit (carpeta Drive "Palco"). Copia del deck "Proposal - AppMaking + Yuno" traducida al español, 18 slides; build reproducible en Deals/Palco/build/ (engine de Higgsfield), notas en Deals/Palco/palco-proposal-2026-09-16.md. Slide 13: platform fee $10,000 + ladder por tramos (cada tramo a su tarifa): $0.08 hasta 58,750 tx exitosas/mes, $0.06 hasta 117,500, $0.05 después → a 235,000 tx = $24,100/mes ($289,200/año). 3DS $0.0403, fraud engine $0.0184, risk conditions $0.0139 cotizados a precio Suggested de la hoja calculator (1Shux23cA23PBCcAlyhAiNrzXgzU6lbtQsLxUHgQ5NH8); pendientes: conciliación, network tokens, token vault; contrato 3 años. ⚠️ Supuestos por validar con German: ladder vs cliff, cobro solo sobre exitosas, "dar" 3DS/fraude = cotizar (no gratis), ticket vs orden sin reconciliar. Lección técnica: Slides API cuenta UTF-16 (banderas emoji = 4 unidades); fix con updateTextStyle range ALL.

**Deck v2 (16-sep tarde, hecho por German + Claude Design):** 20 slides; agenda 02 Business Case; S13 cuatro palancas, S14 Impacto total, S15 pricing layout Flair: **$7,000 platform + $0.06 / $0.055 / $0.045** (tramos 58,750 / 117,500) = $19,044/mes pagos, $23,404 con 3DS ($0.04 × 100K) y antifraude ($0.018 × 20K); risk conditions quedó en $0.04 (sugerido $0.0139, revisar). **REGLA DE GERMAN: el ticket de Palco es $37.09 (el que reportó Patricio); nunca usar el $163 derivado.** BC reajustado con $37.09: L1 $3.6M/$7.2M, L2 $0.40M/$0.67M, L3 $0.26M/$0.43M, L4 $0.23M/$0.36M; total $4.5M/$8.7M, promedio $6.6M; GTV recuperado tenants $6.0M. QA completo en Deals/Palco/palco-deck-qa-2026-09-16.md (25 hallazgos; pendientes de decisión listados al final). **Deck v3 (16-sep noche): 24 slides.** Sección de contexto montada por API (agenda 4 puntos; S3 divisor; S4 Resumen ejecutivo; S5 La capa de pagos de Palco hoy con tabla de aprobación por procesador; S18 divisor Propuesta; S19 pricing). Scripts en Deals/Palco/build/ (build_context.py, fix_context.py). **BC v3 (16-sep noche): base única 235,000 tx exitosas/mes × $37.09 = $104.6M/año (regla de German: así se llega al TPV; nunca usar $457M ni volúmenes de la tabla por procesador, de ahí solo tasas y pesos).** L1 $4.7M/$9.3M, L2 $0.52M/$0.86M, L3 $59K/$99K, L4 $230K/$360K; total $5.5M/$10.7M, promedio $8.1M; GTV recuperado $7.7M. German eliminó los 3 slides de contexto; deck = 21 slides.

**Revisión de la propuesta 18-sep-2026 (sin aplicar, token Slides muerto):** Deals/Palco/palco-proposal-review-2026-09-18.md + script build/fix_review_0918.py (dry / apply). Aritmética BC y pricing cuadran al 100% y siguen GREEN, salvo **Risk conditions $0.04 (lista $0.02, sugerido $0.0139)**. Bloqueantes de alineación: el deck no responde las 6 preguntas de Patricio (slide propuesto "Lo que nos pidieron y cómo lo cubrimos"); "Contrato a 3 años" vs piloto pedido desde el 30-jul (bloque Piloto México, fee reducido ≤3 meses de crédito); objeción de Alfonso sin responder y L3 ($59K a $99K, 7.5 a 12.5 bps) no compensa el costo ($281K, 27 bps): lo que compensa es la aprobación, 18x a 36x; 3DS a 100K vs "obligatorio en todos los flujos" (a volumen completo $8,400 a $10,000/mes); "Palco procesa $104.6M al año" contradice su $28.3M/mes → decir "base de modelación"; "exitosas" no lo dijo Patricio. Preguntas antes del lunes: ¿$37.09 por boleto o por transacción? (su tabla da $120/tx, ~3 boletos), ¿235K aprobadas o intentos?, ¿3DS obligatorio por quién?; a Carlos: catálogo Openpay/Banorte/Santander/MP/Fiserv, split al capturar MX, recurrencia MX.

**Brief de la reunión de propuesta 21-sep:** data/research/palco-meeting-brief-2026-09-21.md (Google Doc "Meeting Brief: Yuno <> PALCO Commercial Proposal (Sep 21, 2026)": https://docs.google.com/document/d/1h4L49gak_2Nbs_maT9sn2M-SIf1ypWD-aRfLprtL48s/edit) + plan de presentación Deals/Palco/palco-proposal-meeting-plan-2026-09-21.md. ⚠️ El evento del calendario quedó de 30 min (11:00 a 11:30, acortado el 16-sep 20:44Z) aunque las aceptaciones dicen 11:00 a 11:45; Miguel sigue "Maybe"; Carlos y Magdalena no invitados. Flujo acordado con German: cuatro palancas (titular optimista L1 $9.3M, L2 $0.86M, L3 $99K, L4 $360K, una razón por palanca) → escenarios (base 235K × $37.09, cohorte, anclas MP 67.9% / mercado MX 72%, quién captura, 18x a 36x) → propuesta (estructura, número, silencio, 27 bps, piloto, cierre con "¿qué tenants?" y "¿quién firma?"). Perfiles nuevos: Miguel Ramírez Lombana = CRO de Palco desde sep-2025 (mediotiempo, juanfutbol, sonder.mut, Kellogg; CDMX); Fernando Nava aparece en LinkedIn ligado a sonder.mut (llegó con los dueños nuevos ⚠️); Alfonso confirmado en LinkedIn como Manager of Development and Support.

**Reunión de propuesta HECHA 21-sep-2026 (25 min, Gong).** Asistieron Patricio, Alfonso, Fernando y **Miguel Ramírez Lombana** ("socio mío, lleva todo el tema del revenue"); por Yuno German + Joaquin. German presentó 4 palancas ($8M) + pricing ($7K + tramos); NO se propuso piloto, cierre = "apenas me den el go avanzamos con el contrato"; pidieron el deck para revisarlo a profundidad. **Volumen real dicho por Patricio (confidencial): ~$245M a agosto 2026, ~$430M GTV en 2025, 2026 "muy arriba de $500M"; la base de $104.6M es "muy conservadora".** Patricio cuestionó antifraude a 20K (espera volumen completo: 235K × $0.018 = $4,230/mes) y preguntó ruteo por tipo de tarjeta por cliente (sí). Miguel preguntó qué gana Palco en la palanca de costo y si Yuno vende junto a él: German dijo que Palco vende y Yuno queda detrás, pero presenta procesadores y apoya negociación de tasa. ⚠️ German dijo network tokens incluidos en el platform fee; el deck los deja "pendiente". Notas: Deals/Palco/palco-proposal-meeting-notes-2026-09-21.md. Follow-up con el deck en borrador (hilo "Próximos Pasos", to Patricio+Miguel+Alfonso+Fernando). Next: go de Palco → contrato; oportunidad de sesión de enablement con Miguel.
**Estado 24-sep-2026:** el FUP con el deck (link Papermark) se ENVIÓ el 21-sep 16:50Z a Patricio, Miguel, Alfonso y Fernando (cc Joaquín, Magdalena, Carlos); cero respuesta desde entonces. Javier Sánchez fuera de oficina hasta el 31-sep. WhatsApp corto para Patricio preparado (lo manda German a mano): "estamos atentos a su feedback para seguir avanzando" + oferta de sesión corta; texto en Deals/Palco/palco-whatsapp-patricio-2026-09-24.md.

## patreon-kritika
*Patreon outreach — Kritika Rooney-Cespedes (Head of Payment Ops); warm but slow, moving to email*  
*type: project · last updated 2026-10-06*

**Kritika Rooney-Cespedes — Head of Payment Ops at Patreon.** Primary Yuno prospect contact at Patreon.

Thread (LinkedIn group with German + Samuel Vieira, Jan to May 2026): Samuel intro'd German; long courtship, Kritika warm but very slow to respond ("apologize for the extreme delay"). She won't attend Stripe Sessions; said she'd reach out by email. German repeatedly proposed calls (incl. Samuel in NYC early May). As of mid-2026 moving the conversation to **email**, attaching the Patreon business case, with **Justo (Yuno CRO)** and **Samuel Vieira** cc'd to signal high interest.

**Why:** Patreon = creator membership platform. Her Payment Ops world centers on subscription billing + creator payouts.

**How to apply:** Lead with the two angles German already pitched and that fit her role: (1) end-to-end subscription management (create/pause/resume/cancel) and (2) creator payout orchestration, both via a single Yuno API. Keep outreach warm and patient (she is slow but receptive); emphasize genuine interest. English. Patreon business case deck already exists (Business Cases/Business Case - Patreon + Yuno.pptx).

**Actualización 6-oct-2026:** Kritika está en licencia parental hasta enero 2027 (auto-reply del 28-ago-2026 en Gmail, hilo "Patreon + Yuno" 19eae49469683c4b; externos → Michael Mincieli, Sr Director Tax, mmincieli@patreon.com). German ya escribió a Michael el 31-ago y a Dino (dino@patreon.com) el 28-ago, cc Magdalena, sin respuesta registrada. Kritika aceptó la conexión de LinkedIn de German el 6-oct-2026; nota friendly enviada por LinkedIn (bebé, retomar en enero, o que señale a quien cubre si tiene sentido antes). Siguiente toque: enero 2027, salvo que ella señale a alguien.

## project_pdf_vw_paper_width
*Why deck PDFs overflowed vs the live link, and the 1440px-page fix*  
*type: project · last updated 2026-06-07*

In yuno-sales-pitch-maker, slides size type/spacing with `clamp(min, Xvw, max)`. Chromium's `page.pdf()` resolves `vw` against the **paper width**, not the browser viewport (verified with Playwright: a 100vw box fills any paper size regardless of context viewport). At a 1920px page every clamp hits its max (~33% bigger than the ~1440px laptop the deck is tuned for), so text overflowed the fixed 1080px boxes — the cause of "PDF se viene mal con errores visuales."

**Fix (commit c3df5e6):** capture on a **1440x810** page (`page.pdf` in [server/index.mjs](yuno-sales-pitch-maker/server/index.mjs) + `@page` in [index.css](yuno-sales-pitch-maker/src/index.css)) and `zoom: 0.75` (1440/1920) each `.pdf-page`. `zoom` (unlike transform:scale, see [[feedback_pdf_no_transform_scale]]) does NOT empty SlideBase. This makes the PDF render identically to the live link. Removed the old leadership `zoom:0.96` band-aid.

**Why:** PDF must match the link exactly, nothing should change.
**How to apply:** keep paper size + `@page` + the `.pdf-page` zoom in sync; if text looks too big/small in PDF, the lever is the capture page width (1440 = laptop reference). Related: [[feedback_no_pdf_cursor_artifacts]].

## project-peacock
*Peacock / NBCUniversal account state (Brendan Callinan silent since Jul-2026), verified stack (Spreedly vault + Adyen), current prices post 18-ago-2026, and the Subscriptions one-pager review of 18-sep-2026*  
*type: project · last updated 2026-09-18*

**Contactos:** Brendan Callinan (brendan.callinan@nbcuni.com) es el único contacto real; LinkedIn → email 29-jul-2026 → Alejandro 30-jul → nudge 10-ago → solo OOO. Cero respuestas. Su OOO señala a Rakhi Seth-Forrest (escalations) y Andrea Babcock (Payment Operations), ambas ya contactadas sin respuesta para Stripe Tour NY sep-2025. En Gong hay un tercer contacto, Sunny Mui, solo outbound sin respuesta. Título de Brendan no consta en el repo.

**Stack verificado (18-sep-2026):** Spreedly hace vault y tokenización (claves `sas-nbcu.spreedlyForm.*` en peacocktv.com) y Adyen es la ruta visible / componente de fallback (clave `adyen.retryButton`). Sin orquestador de retries visible. Help center: una tarjeta corregida se cobra "beginning with the next billing cycle".

**Precios vigentes (subida 18-ago-2026 nuevos, 17-sep existentes):** Select $8.99/mo · $89.99/yr; Premium $12.99 · $129.99; Premium Plus $19.99 · $199.99. Estudiante: $5.99/mo x 12 meses según dealnews (fin ago-2026), pero la página oficial /student indexa "$6.99/mo for 12 months"; verificar desde IP US antes de citar. 48M suscriptores pagos = Comcast Q2-2026 (verificado).

**Business Case (Magdalena, ago-2026):** Google Slides "Business Case - Peacock + Yuno" (id 1JwF7MsSwOF4wn-IzD0v_Z9SnFC1TL7_PLtNQ0QjPS08), $27-31M/yr; en Papermark; NUNCA enviado a Brendan (solo lo vio Magdalena). LinkedIn FUP 4-sep en Deals/Peacock/ ofrecía enviarlo.

**One-pager Subscriptions (18-sep-2026):** revisado, no "go" hasta corregir precios del mockup (estaban pre-subida), quitar "typical migration about a week" (sin fuente), y reemplazar/reencuadrar el stat 26.49 pp (ver [[reference-subscriptions-stats]]). Recomendación: liderar con Way in 2 (renewals + retries bajo su billing), pilotar un ciclo de facturación, no una semana.

**Why:** Peacock corre un commerce platform compartido con NOW/SkyShowtime; mover el catálogo de planes a Yuno es irreal y dispara el reflejo "no migramos billing". Ver gaps de Jarrett (31-ago) en [[reference-subscriptions-stats]].

**How to apply:** cualquier pieza para Peacock usa los precios de arriba, cita Spreedly + Adyen como stack, y pide decline codes de renovación para un cohorte. Si Brendan sigue mudo, la puerta alterna es Andrea Babcock (Payment Ops). Relacionado: [[project-hbo-max]], [[project-suno-jasper]].

## project-pedidosya
*PedidosYa (PeYa): oportunidad B2B de Collections con Belén Casaret (cobro de deuda de partners, conciliación de 15 bancos, pago en el portal de vendors); 1ª llamada 29-sep-2026 hecha, deep dive con Fanny propuesto 8 o 9-oct; stack Spreedly + dLocal, split Uber/SSW*  
*type: project · last updated 2026-09-29*

PedidosYa (Delivery Hero, HQ Montevideo, 15 países LatAm). Lead CALIENTE, no cold: Belén Casaret (belen.casaret@pedidosya.com) llegó vía un amigo de Alonso. Alejandro Albarracín organizó la primera llamada y estuvo en ella.

## Llamada 1, 29-sep-2026 (German + Alejandro + Belén, 32 min)

Fuente: resumen que pasó German. El transcript de Google Meet quedó inservible (transcribió el español como inglés).

**Belén:** lidera Collections, lleva 3 meses en el cargo, opera en 15 países. Habla de vos (rioplatense).

**Qué es "collections" en PeYa (resuelto):** SOLO B2B. Es la deuda de los partners (restaurantes y comercios) por comisiones, servicios de marketing y créditos. La deuda nace cuando la liquidación semanal no cubre lo que el partner debe. Los servicios de marketing se facturan aparte a 30/60/90 días y se pagan offline. NO es checkout de consumidor ni efectivo de riders.

**Segmentos de partners:**
- Multi (McDonald's, Carrefour, Coto): pagan por portal, email o transferencia; ordenados.
- Non-multi (restaurantes chicos): difíciles de contactar, concentran la deuda sin resolver.
- Más de 20.000 cuentas en cobranza; parte in-house, parte en agencias externas (etapa de write-off).

**Dolores:**
1. Conciliación: un banco por país, 15 bancos, cada uno devuelve un formato distinto. Muchos no identifican quién pagó (sin CUIT ni datos del ordenante). Los pagos llegan sin matchear y quedan como partidas abiertas en el ledger de deudores. Hoy es manual; quiere automatizar.
2. Métodos de pago: los partners solo pagan por transferencia, efectivo en Western Union o dLocal (3 a 4 países). Los links de dLocal no son permanentes y se generan a mano por transacción y por monto. No hay checkout ni autoservicio.
3. El portal de vendors existe pero Collections no está integrado: el partner no ve ni paga su deuda ahí.

**Sus dos objetivos:** saber quién está pagando y lograr que más partners paguen.

**Marco que German le dio a Belén en la llamada (usar siempre estas tres claves, en este orden):** 1) métodos de pago y checkout, 2) procesadores y visibilidad/reporting, 3) conciliaciones.

**Fit conversado (tres frentes):** checkout con métodos nuevos embebido en el portal de vendors; agregación bancaria (vista única de los 15 países bajo una API); motor de conciliación que matchee pagos con partners sin comprobante manual.

**Próximos pasos:**
- Deep dive demo con Belén + Fanny (líder de Cash Application, dueña operativa). Belén pidió un recorrido concreto de punta a punta de cómo funcionaría la identificación del partner y el matching. Prefiere jueves o viernes; están en cierre de mitad de mes, así que puede correrse una semana.
- Follow-up de German en BORRADOR de Gmail 29-sep (cc Alejandro, asunto "PedidosYa + Yuno"): propone jueves 8 o viernes 9-oct-2026, pide la lista de bancos de los 15 países y una muestra anonimizada del archivo de un banco. German lo editó a mano (no sobrescribir el borrador); el ajuste de las tres claves se le pasó por chat para que lo pegue él.
- Pendiente: recibir la lista de bancos y revisar cobertura.

⚠️ Antes del deep dive confirmar con producto qué está GA en conciliación y en agregación bancaria. Conciliación de settlement, payouts y fees figura como roadmap (ver [[published-stats-only]]). No prometer el matching automático de transferencias hasta tenerlo confirmado. PeYa ya usa Simetrik y SAP para conciliación (job listing).

Es la primera exploración B2B con PeYa; las conversaciones anteriores de Yuno con PedidosYa fueron B2C (pay-ins).

## Contexto de la cuenta

Stack B2C: Spreedly publicado como vault (evidencia 2018, usado sobre todo como token vault); dLocal = proveedor principal según Belén (rastro público: billers "Dlocal Service" en Bancard Paraguay y El Salvador); deck interno dice Worldpay y otros PSPs vía Spreedly; Chile débito Klap + Webpay; fraude Cybersource (2021); riders Pago46 (AR, CL); PeYa Wallet sobre Wibond (AR).

Política interna: Head of Payments sería ex-dLocal (nombre desconocido). Nunca criticar dLocal; posicionarlo como proveedor que se queda detrás de Yuno.

Historial Delivery Hero: opp de Justo en Salesforce. Elliot Watnik (DH) dijo que la prioridad 2026 de PeYa era time-to-market de APMs; mudo desde dic-2025. Lars Hofmann (Global Payments Director DH) visto en MPE Berlin 17-mar-2026. Saad Saif: RFP APAC. Deck "Delivery Hero + Yuno Business Deck V3" en Drive (id 1to6J7baTYnqFR8_22oGD3MyVL330h-CX) = deck.y.uno/DeliveryHero; hecho nov-2025 para Berlín, desactualizado tras el deal de Uber. Alguien de Yuno mandó "Touchpoint" a Leandro Malandrini (CPO) el 21-sep-2026.

Uber firmó compra de Delivery Hero el 16-jul-2026 (cierre esperado H2 2027): Uber se queda 13 mercados de PeYa; SSW Partners se queda Chile y Ecuador (TSA hasta 24 meses). Uber es relación activa de Yuno: no cruzar información entre Uber y PeYa.

**Why:** cuenta estratégica con ventana por el split de dueños y un champion interno que pidió la reunión. El caso de uso real resultó ser cobranza B2B a partners, distinto del pitch de orquestación B2C.

**How to apply:** para el deep dive y cualquier follow-up, armar el caso sobre identificación y matching de transferencias y pago de deuda en el portal de vendors, no sobre checkout de consumidor. Notas del call y correo en `Deals/PedidosYa/`; research previo en `data/research/pedidosya-2026-09-29.md` y brief en `data/research/pedidosya-meeting-brief-2026-09-29.md`. Correos a Belén en voseo. Relacionado: [[feedback-email-no-links-sober]], [[published-stats-only]], [[feedback-client-data-requests-simple]].

## project_perplexity_psp
*Perplexity AI payment stack + Yuno angle (research 2026-06-17)*  
*type: project · last updated 2026-06-17*

Perplexity AI, Inc. (SF; UK entity, Singapore presence). AI answer engine. ~$450M+ ARR (Mar 2026), ~$22.6B valuation. ~138M monthly web visits; India is #2 market (~10.5%) after US (Airtel free-Pro bundle drove India surge). CEO Aravind Srinivas.

Payment stack: web subscriptions (Pro $20/mo, Max $200/mo) + API billing via Stripe (single cross-border PSP); iOS/Android IAP; agentic commerce "Buy with Pro"/Instant Buy via PayPal+Venmo (US-only). PCI DSS SAQ A, SOC 2 Type II. No orchestrator. India card-only (Airtel users asked to add card) — UPI gap. Trustpilot ~1.6/5 (post-cancel charges, non-refundable).

Yuno angles (TWO-FOLD, strong): (1) India #2 but card-only = UPI gap at hyperscale; single cross-border Stripe = recoverable declines; (2) Perplexity is BECOMING a payments surface (agentic commerce) stuck on one US rail — orchestration to globalize checkout. Amazon won injunction blocking Comet shopping agent (favors owned rails). Scored 🔴 14. Best cases: InDrive, Rappi, Reserva, Livelo. Part of [[project_ai_apps_batch_2026_06_17]].

## project-pipeline-sync
*Pipeline Sync Apps Script (TCL Final List -> Deal Status GTM cada 15 min); manual + fuente en Lists & ICP/Pipeline Sync; owner Magdalena Torrealba*  
*type: project · last updated 2026-08-04*

Pipeline Sync: Google Apps Script que copia leads de "Target Company List GT - BDM" (tab `Final List`, ID `1QY5pH4Td2sRitHpHI3Eec69sFfGdK2nuY-QMleqEnek`) al "Deal Status GTM" (tab `Deal Status Tracker`, ID `1WPz1JW9zQm06SQg9ncrBM-4BH8ZKWh5O2Pn18XvKKPc`) cada 15 minutos. Owner: Magdalena Torrealba (magdalena.torrealba@y.uno).

Regla: un lead viaja cuando su `Status` es distinto de `Inactive` (vacío también bloquea). Identidad por `Company` normalizado. 6 columnas sincronizadas por nombre de header: Company, Website, LinkedIn URL, Industry, Comments, Status. One-way, nunca borra, idempotente. Tabs generados en destino: DASHBOARD y KEY (se reconstruyen en cada run) + `_LOG` oculto (contadores de días por status; no borrar).

Manual operativo completo + snapshot del código: `Lists & ICP/Pipeline Sync/PIPELINE_SYNC_HANDOFF.md` y `pipeline_sync.gs` en el repo GTMCoding (integrados 2026-08-04 desde handoff por WhatsApp). La copia canónica del script vive en el proyecto Apps Script vinculado al sheet fuente.

Skill `/pipeline-sync` (`.claude/commands/pipeline-sync.md`, creado 2026-08-04): opera todo end-to-end — status/diagnóstico leyendo KEY/DASHBOARD vía gsheets_read, cambios de CONFIG, cambios de código y restore. Deploy vía `npx @google/clasp` (setup one-time pendiente: `clasp login` + Script ID → `.clasp.json`); fallback = instrucciones de paste en el editor. clasp NO está instalado global (npm global requiere sudo); usar siempre `npx -y @google/clasp`. Relacionado: [[project-tcl-agent]].

## project_polymarket_psp
*Polymarket's primary payment processor is MoonPay (fiat on-ramp)*  
*type: project · last updated 2026-06-17*

Polymarket's main/primary payment processor is **MoonPay** (a fiat on-ramp), confirmed by the user 2026-06-17. Single-PSP dependency is a Yuno talking point (concentration risk).

Reflected in the Polymarket cost-reduction deck (deck.yuno.tools/m/polymarket): `src/data/polymarket.json` carries `PSPS: [{ name: "MoonPay", role: "Global · fiat on-ramp" }]` so MoonPay leads the arch tiles on the Solve slide, and pain_1 names MoonPay. That deck is a custom slug-scoped order (cover, infrastructure, two cost levers, solve, trusted-by, CTA) signed by German Tatis. See [[feedback_no_false_info_disclaimer]] for the facts-only rule applied to its copy.

## project_praktika_psp
*Praktika AI language app — 100% Apple/Google IAP, zero web checkout; App Store fee-recovery BC*  
*type: project · last updated 2026-07-23*

Praktika (praktika.ai) — AI language-learning app, ~$20M ARR, 2M MAU, $35M Series A (Blossom Capital), 38 employees. Delaware C-corp ("Praktika.ai Company", Wilmington DE), ops in London. Founders: Adam Turaev (CEO), Anton Marin (CTO), Ilya Chernyakov (CPO).

**Payments:** bills 100% through Apple App Store + Google Play IAP. Own Terms say "all billing handled by the Application Store." NO web checkout, no MoR, no PSP, no local APMs. Pricing anchor ~$99/yr (~$8/mo). NOT eligible for 15% Small Business Program (>$1M) → Apple 30% yr1 / 15% after, Google 15% subs.

**BC angle (same cluster as [[project_bending_spoons_psp]], [[project_replika_psp]], [[project_voodoo_psp]]):** App Store fee recovery via web checkout, now legal to steer in US (Epic v. Apple), EU (DMA), South Korea, India (CCI). Competitors Duolingo/Babbel/ELSA already bill on web. Complaints: trial abuse, post-cancel charges, refund deflection.

BC built 2026-07-23: `Business Cases/BC sheets - Praktika.xlsx`. STANDARD template structure (Context, Aceptance Rate Delta, APMs, RESUMEN, per-region Pay-ins full rows, Devs.Eng dept breakdown, Current Payment Methods). App-only → "Annual Total Visits" derived from ARR (3.37M; ATV $99, conv 0.06), no web traffic. Top-13 markets = ~62% ARR = $12.38M TPV. **App-store fee captured in standard Current MDR 15% → New MDR 4%, so Fee Renegociation line = IAP recovery.** Total benefit $6.525M (~32.6% ARR): Acceptance 0.257 + Fee Reneg 1.315 + New APM 0.461 + Eng 4.493. Eng large by standard $21,600/dept method (same as Suno). See [[project_ai_apps_batch_2026_06_17]].

## railway-stale-sep-2026
*deck.yuno.tools (Railway) dejó de publicar commits de main desde ~8-sep-2026; bundle vivo index-DahtyNRA.js tiene agosto pero no septiembre; Neverland es el target real*  
*type: project · last updated 2026-09-14*

Observado 2026-09-14: el bundle vivo de Railway (`/assets/index-DahtyNRA.js` en deck.yuno.tools) incluye los commits de agosto (Pedro Ferrer, teléfonos de German y Magdalena, Eventbrite BSP) pero NO los de septiembre (Airalo BeyondOne 12dd370 del 9-sep, Gamma 0e27870, Prateek Gurani 7acb8cd del 14-sep). Railway auto-deploy está detenido o fallando desde ~8-sep-2026; la sesión del 9-sep ya lo sabía implícitamente (commits "renders on current prod bundle too" / "degrade gracefully on stale bundles").

No se pudo diagnosticar desde la máquina: el hook bloquea `railway` CLI, el token GitHub de `.env.local` está vencido ("Bad credentials"), y `gh` no está autenticado. Falta revisar el dashboard de Railway (build fallido, auto-deploy apagado, o rama cambiada).

**Why:** German pide que cada cambio quede publicado; si solo se verifica el push a main, un cambio de código puede quedar invisible en ambos dominios.

**How to apply:** Tras cada commit de código en yuno-sales-pitch-maker: (1) disparar deploy Kingdom a Neverland según [[deck-changes-deploy-neverland]] (requiere VPN: internal-infra.y.uno y decks.internal-tools.y.uno resuelven a 10.x); (2) verificar el bundle vivo bajándolo a archivo y usando `grep -a` (NUNCA `echo "$var" | grep` en zsh: `\c` en el JS minificado corta la salida y da falsos 0). Cambios de solo datos (Supabase overrides) no dependen de esto. Related: [[salesmaker-deploy-branch]], [[neverland-migration]].

## railway-watchdog-routine
*Watchdog de deck.yuno.tools reescrito 2026-08-03 en modo SILENCIOSO (solo Gmail draft, NUNCA calendario/push) tras ~65 falsas alarmas; el sandbox cloud no alcanza deck.yuno.tools (curl exit 56)*  
*type: project · last updated 2026-08-03*

Cloud routine `trig_015ZR5VN1Vwpnjhme7bZZXpr` ("Railway watchdog — deck.yuno.tools (silencioso)"), hourly :07 UTC.

**Incidente 2026-07-31→08-03:** la versión original creaba un evento de calendario con popup (notificación al teléfono) + Gmail draft en cada "caída". El sandbox cloud NO alcanza deck.yuno.tools (curl exit 56 / HTTP 000 en todos los intentos, en todas las corridas) aunque el sitio estuvo siempre arriba → ~65 falsas alarmas por hora corrida. German pidió explícitamente: NUNCA más reuniones de calendario ni notificaciones por este tema. Los ~65 eventos "🚨 deck.yuno.tools CAÍDO (Railway)" fueron borrados del calendario el 2026-08-03.

**Versión actual (2026-08-03):** conector de Calendar REMOVIDO de la rutina; reglas absolutas de no-calendario/no-notificaciones en el prompt; retries dentro de curl (`--retry 3`, sin sleep que el harness bloquea); chequeo de control contra google.com (si la red del sandbox falla → INCONCLUSIVE, sin alerta); segunda opinión contra /decks/health-check; en caída real confirmada → SOLO un Gmail draft (dedupe vía list_drafts, máximo uno). Ojo: si el sandbox sigue sin poder alcanzar deck.yuno.tools pero sí google.com, puede crear 1 draft silencioso falso (capado a uno).

**Why:** el watchdog vigila el dominio donde apuntan los links de prospectos; German solo quiere enterarse de caídas reales y sin ruido.

**How to apply:** No re-agregar el conector de Calendar ni alertas push a esta rutina. Si German reporta ruido de nuevo, considerar deshabilitarla en https://claude.ai/code/routines/trig_015ZR5VN1Vwpnjhme7bZZXpr (borrar solo se puede desde esa UI). Al apagar Railway (post-migración [[neverland-migration]]), apagar o repuntar esta rutina. Related: [[salesmaker-deploy-branch]].

## project_replika_psp
*Replika (Luka Inc) payment stack + Yuno angle (research 2026-06-17)*  
*type: project · last updated 2026-06-17*

Replika by Luka, Inc. (US/Delaware, SF). Leading AI-companion app, 40M+ users / 150+ countries. Sibling apps Blush ($99/yr) and Tomo. Founder Eugenia Kuyda stepped down as CEO 2025 (→ Wabi); Dmytro Klochko runs day-to-day. Est. rev ~$24-30M.

Payment stack: web Replika Pro via single PSP (Stripe) + PayPal; majority of revenue via Apple/Google IAP (15-30%). No orchestrator. Card-only web checkout — no local APMs (Pix/UPI/iDEAL/OXXO) confirmed despite Mexico/India/Brazil/France/Germany base. BBB F-rating (29 complaints): double-charges, trial→annual auto-upgrade, cancel friction. €5M Garante GDPR fine (2025).

Yuno angles: single web PSP + IAP dependence margin gap; cross-border APM gap; billing-trust complaints (retry/dunning); app-to-web migration reusable across Replika/Blush/Tomo. Best cases: InDrive, Rappi, Livelo. Part of [[project_ai_apps_batch_2026_06_17]].

## project-riot-games
*Riot Games — call 2026-07-31 con Andreas Borngraeber hecho; core middle tier CERRADO (CEO ex-CFO), puerta abierta = physical goods/mail order en 1-2 años vía RFP; jugada activa = entrar junto a Airwallex*  
*type: project · last updated 2026-08-05*

Riot Games (gaming, LA, Tencent 100%). Intro del CSO **Abhi Ramprasad** → **Andreas Borngraeber** (aborngraber@riotgames.com). **Call realizada 2026-07-31** (23 min, German + Samuel). Transcript: `Deals/Riot Games/riot-call-transcript-2026-07-31.md`.

**Andreas:** basado en **Dubai** (no Europa; corrige hipótesis anterior). Construyó todo el stack de payments de Riot; hoy lidera un **proyecto confidencial en el espacio "commercial"**. Alemán, background CFO/treasury/payments en gaming antes de Riot (consistente con el lead Travian/TG Payment; él dijo "trading games" en el transcript).

**Outcome del call:**
- Middle tier in-house (~2015) = hub central de PSPs con fallback + dynamic routing. Hosted payment fields, tokens atados a cada PSP (evitan SAQ-D). Traffic por juego/región al mejor PSP, failover automático por declines.
- **Core CERRADO:** dos traumas third-party (Fat Fugu colapsó en el launch de LoL 2008-09; middle layer coreano con incidente de seguridad casi catastrófico vía payments). El CEO actual era el CFO de esa época. Textual: "as long as our CEO is CEO, there won't be a way in". NUNCA pitchear reemplazo del middle tier.
- **Puerta abierta:** physical goods / mail order (address, capture on ship, returns, refunds); Andreas ve a Yuno "in a complementary way once you go into mail order". Timeline meses a 1-2 años, ligado a sus proyectos comerciales. Compra SIEMPRE por RFP (10-12 vendors, 3 rondas). Le interesó el AI/Payments Concierge (leyó docs solo). Acordado: ping cada pocos meses.

**Jugada activa (ago 2026): entrar con Airwallex.** Airwallex habla con Riot y avanza bien; plan = intercambio de mapa de cuenta + narrativa conjunta (Airwallex mueve fondos, Yuno capa técnica del flujo physical goods) + entrar al RFP como propuesta combinada. Brief para esa reunión: `Deals/Riot Games/riot-airwallex-partner-brief-2026-08-05.md`.

**⚠️ INCIDENTE (2026-08-05):** German compartió el correo de Andreas con un ejecutivo de Airwallex (cabana executive) sin permiso; Andreas se molestó y lo reclamó por email. Disculpa enviada (draft en `Deals/Riot Games/riot-apology-email-andreas-2026-08-05.md`): admisión directa, compromiso de no compartir nada suyo sin OK explícito. REGLA para esta cuenta de ahora en adelante: NADA de Riot (contactos, contenido de calls) se comparte con terceros, Airwallex incluido, sin permiso explícito de Andreas; la jugada conjunta con Airwallex se coordina solo con intel de Airwallex, no exponiendo a Andreas. La relación con Andreas es más valiosa que el atajo.

Research base: `data/research/riot-games-2026-07-10.md`, brief pre-meeting: `data/research/riot-games-meeting-brief-2026-07-31.md`. [[project-lululemon]] mismo motion outbound.

Otros contactos de la secuencia: Nate Portner, Thiago Pinto (QA Payments), Gonçalo Pereira (payment partnerships, gpereira@), Armando Gonzalez, Mark Stitz, Eric Danker, Sridhar Ranga, Jack Calvi, Brent Rich, Tolga Tekin (rechazó); Garrett Mills y Olaf Westheider rebotaron.

## project_salesmaker_protected_master
*yuno-sales-pitch-maker — deploy branch is main (Railway auto-deploys); master is a protected, unused decoy*  
*type: project · last updated 2026-07-02*

In the `yuno-sales-pitch-maker` nested repo (remote `github.com:yuno-payments/yuno-sales-pitch-maker`):

- **`main` is the live deploy branch.** Railway (`railway-app[bot]`) auto-deploys to production ("Sales Deck Maker / production") on every push to `main`. It is NOT protected — push directly to ship.
- **`master` is a protected decoy.** It only holds an unrelated "Initial commit" README and rejects direct pushes (requires PR review). Do NOT target master — it has nothing to do with the live deck.

**Why:** Discovered 2026-05-29. First attempt pushed work to `master`, got blocked by branch protection, and a PR (#7) was opened pointlessly — then closed once we found Railway actually deploys from `main` (last prod deploy before our change was `a0c3cda` on `origin/main`).

**How to apply:** Per [[feedback_auto_commit_push]], commit automatically, then `git push origin main` to deploy. The user's standing instruction (2026-05-31): **always publish to production immediately after a change, without asking** ("siempre publica enseguida"). So push to `main` right after committing — do NOT ask for confirmation each time. (The auto-mode classifier may still block a given push; if it does, that single push needs an explicit OK, but the default is push-immediately.) Local working files like `.env.local` (holds a GITHUB_PAT) are gitignored — never committed.

**⚠️ GOTCHA — GitHub's DEFAULT BRANCH is still `master`, and this breaks the self-serve Edit button (discovered 2026-07-02).** The `deck-edit` flow ([[project_deck_edit_button]]) uses an `issues: labeled` GitHub Action (`.github/workflows/deck-edit.yml`), but GitHub only fires issue-triggered workflows from the file version on the **default branch**. The workflows live on `main`; the default branch is `master` (which has no `.github/workflows`), so **zero runs ever trigger** — edit-request issues (e.g. #8/#9 from alejandro.bernal@y.uno) sit OPEN forever with no PR. Fix needs **admin** (my token is `maintain` only, master is protected): change the repo default branch `master` → `main` (Settings → Branches). After that, re-fire stale issues by toggling the `deck-edit` label. Repo Actions secrets present: `ANTHROPIC_API_KEY`, `DECK_BASE_URL`, `EDIT_NOTIFY_SECRET`. Edit requests are visible via `gh issue list --label deck-edit --state all` (requester email embedded as `<!-- deck-edit:requester=... -->`).

## samuel-knowledge-transfer
*Prompt sent to Samuel Vieira's Claude (Oct 2026) to brain-dump its payments/RFP/research training; German will paste the output back for ingestion*  
*type: project · last updated 2026-10-05*

On 2026-10-05 German asked for a long English prompt to send to Samuel Vieira so that Samuel's Claude Code instance dumps everything it knows (payments fundamentals, global payment methods by country, PSP/orchestrator landscape, Yuno product and objections, RFP playbook with question bank, research methodology, business-case formulas and benchmarks, vertical playbooks, deal craft, regulation, glossary, myths, gaps) plus its reasoning chains and the rules Samuel gave it.

SENT to Samuel Vieira (Slack user U06U4SEVB50, samuel@y.uno, Business Development Manager) by Slack DM on 2026-10-05 as a .md file plus run instructions; Samuel and German DM each other in English. Waiting for Samuel to send back the output.

The prompt lives in the repo at `Knowledge Transfer/samuel-claude-knowledge-transfer-prompt.md`. It asks for output in parts (Part 0 index, then A through O), with confidence tags [VERIFIED / INTERNAL / ESTIMATE / RULE OF THUMB / UNSURE], dates on everything, [CONFIDENTIAL: ask Samuel] markers, and a Part O ingestion guide.

**Why:** German wants me to answer any payments/RFP/fintech question at Samuel's Claude's level and to "always know how to act".

**How to apply:** When German pastes the output (one or many parts), ingest it instead of just reading it: save each part under `Knowledge Transfer/samuel-claude-output/` in the repo, then create reference memories per domain (payments fundamentals, country playbooks, provider landscape, RFP question bank, benchmarks, glossary) and feedback memories for Samuel's rules that German adopts. Keep the confidence tags; anything tagged ESTIMATE/UNSURE stays out of customer-facing material per [[no-false-info-disclaimer]] and [[published-stats-only]]. Follow Part O's ingestion guide when it arrives. Related: [[yuno-sales-deck-skill]] (Samuel's Roblox decks), [[sf-relocation-fall-2026]] (German and Samuel together in SF until Nov 4).

## sean-calabro-manager
*Sean Calabro, nuevo Head of North America de German (ex-Worldpay); su estilo de gestion, expectativas y estructura de trabajo del equipo*  
*type: project · last updated 2026-09-01*

Sean Calabro (ex-Worldpay) es el nuevo jefe de German como Head of North America. Primera reunion 2026-09-01, notas tomadas por German.

**Estilo de management:**
- Feedback en ambas direcciones, transparencia total; no endulza nada ("va a ser hp" segun German)
- Cultura orientada a equipo/colaborativa, pero el foco final es un solo numero: revenue
- Coaching/feedback frecuente, con la intencion explicita de que nunca sea "mean"
- Mucha presion, pero con contexto: "el va a querer feedback y transparencia"
- Cree en impacto organizacional: propone que el equipo trabaje para "quedarse sin trabajo" (que el no necesite estar en las calls de nadie) e impulsa promociones internas

**Como opera el pipeline/forecast:**
- Todos en el equipo deben correr el mismo proceso: Excel de pipeline con cuentas, status, y generacion de forecast de revenue
- Reunion de forecasting de NorthAm los jueves al mediodia
- Formato: target vs forecast, deals listados, gap identificado, plan para cerrar el gap (trabajo conjunto con el equipo)
- Exige pipeline sostenible a largo plazo, no solo deals de corto plazo: ejemplo dado, construir hoy deals de julio 2027 que alimenten 2028
- Metodologia de relacionamiento: iniciar conversaciones y construir relaciones ~6 meses antes de que el deal este maduro ("mark it, work it, buy it")
- Espera que cada rep se posicione con 2 anos de anticipacion

**Comp / RAC plans:**
- Metodologia: empezar del goal, definir actividades necesarias, identificar en que es bueno cada rep para esas actividades
- Comp: flat rate pagado por dolar generado, independiente de si se llega al target o goal (no es todo-o-nada)
- Hay cliffs en el comp plan (detalle pendiente de precisar)

**Por que importa:** Define como German debe reportar pipeline (Excel unificado, forecast semanal jueves), como priorizar deals (pipeline de largo plazo, no solo quick wins), y que esperar en 1:1s/coaching (directo, sin filtro, enfocado en revenue).

**Como aplicar:** Al ayudar a German con pipeline, forecasting, o prep para calls con Sean, usar este formato (target/forecast/gap/plan) y enfatizar deals con horizonte multi-año, no solo el trimestre actual. Ver [[user_german_profile]].

## project-sf-relocation-fall-2026
*German, Samuel Vieira y Joaquin Mann viven en San Francisco del 28-sep al 4-nov-2026 (Airbnb aprobado por Justo y Sean el 17-sep); planear reuniones presenciales Bay Area y horarios PT*  
*type: project · last updated 2026-10-06*

German y Samuel Vieira estarán en San Francisco del 28-sep-2026 (check-in 3PM) al 4-nov-2026. Airbnb propuesto por German el 17-sep en el group DM con Justo, Sean y Joaquin; Sean OK (<$4k/mes), Justo asignó "blue one for German". La semana del 21-sep es la última en Colombia antes del viaje; el 22-sep hay FlightHub presencial en Montreal (decisión pendiente si German viaja).

Actualización 6-oct-2026: Joaquin Mann también vive con ellos en SF este mes; los tres hacen reuniones presenciales, visitas a merchants y eventos. German publica en LinkedIn un post de los tres (foto + CTA a conectar) con PS de que Yuno busca un Solutions Engineer.

**Why:** cambia zona horaria a PT y abre presenciales en Bay Area (Perplexity, Replika, Gamma, Higgsfield, Chai, Anthropic, OpenAI, xAI, Patreon, Chess.com cerca en SLC).

**How to apply:** al proponer reuniones a partir del 28-sep usar horario PT y ofrecer presencial en SF a cuentas del Bay Area. Relacionado: [[project-flighthub]], [[project-higgsfield]], [[project-perplexity-psp]].

## project-sf-trip-budget-sheet
*Google Sheet del presupuesto día a día del viaje de German a San Francisco (28-sep → 4-nov-2026), supuestos clave y cómo regenerarlo*  
*type: project · last updated 2026-09-22*

Google Sheet "Presupuesto San Francisco · 28-sep → 4-nov-2026 · German": https://docs.google.com/spreadsheets/d/1CWZeat_H4fsNuvZ0n5_b3zLfxXLgyaaH6OSsvOlRzII/edit (creado 22-sep-2026, 6 pestañas: Resumen, Supuestos, Dia a dia, Politica Yuno, Research SF, Comparacion).

Fuente y regeneración: `Travel/SF Sep-Nov 2026/build_budget.py` genera el .xlsx; se subió vía conector Google Drive (base64 .xlsx → conversión a Sheets). `push_to_gsheets.py` (Sheets API con token del MCP gdrive) NO funciona: el token está muerto y el classifier bloquea inspeccionar credenciales.

Supuestos que German debe confirmar: precio real del Airbnb (SOMA Executive Retreat Lower, 2BR, compartido con Samuel; Sean aprobó "<$4k/mes" → usé $130/noche la unidad, 50% para German); qué 10 noches son en casa de Joaquín (supuse las últimas: 25-oct → 4-nov, editable con dropdown en columna D). Vuelo pagado $1,064 (Avianca Flex).

Política SF (Travel & Expense Policy v1.0 abr-2026): hotel $220/noche sin impuestos, desayuno $15, almuerzo $25, cena $50, comida cliente/equipo $85 pp, transporte $55/día; tips dentro del tope; estadías 7+ noches → avisar a Finance; el Airbnb aún no tiene hilo en #travel-requests (solo el vuelo, 14-sep).

**Why:** German pidió comparar política vs costo real de SF; el sheet es el artefacto vivo para el viaje.

**How to apply:** si pide ajustar el presupuesto, editar `build_budget.py` y re-subir (o editar celdas directamente); nunca crear un segundo sheet sin avisar. Relacionado: [[project-sf-relocation-fall-2026]], [[project_gsheets_mcp]].

## project-sf-trip-playbook
*Playbook del viaje a SF (28-sep a 4-nov-2026) con pestaña Interactive Calendar; cómo se construye, reglas que pidió German y hallazgos verificados de eventos y precios*  
*type: project · last updated 2026-09-28*

Artifact "Playbook SF Payments": https://claude.ai/artifact/991q3UE3WaEfqaqb22epMg (capability `db`). Fuente en `Travel/SF Sep-Nov 2026/`.

**Cómo se construye:** `events.json` es la fuente única de eventos (lista del Playbook + bloques base del calendario); `calls.json` = llamadas del calendario de German (snapshot 28-sep); `src/page.html`, `src/calendar.css|html|js` son las plantillas; `python3 build_playbook.py` genera `sf-playbook.html`. Republicar ese mismo archivo para conservar el link. Lo que el equipo agrega desde la página vive en la base del artifact (colecciones `items` y `status`), no en el repo: un republish no lo borra. Para agregar filas por pedido usar ArtifactData sobre `items`.

**Reglas que pidió German:**
- Van TRES (Joaquín Mann, Samuel Vieira, German) y van juntos a todo: el plan no divide al equipo; si dos eventos chocan elige uno y deja el otro como plan B.
- Sin el marco "la lista de Samuel": una sola lista de eventos por fecha.
- SIEMPRE mostrar el precio de la entrada de cada evento; si es gratis, decir "Gratis".
- La pestaña se llama exactamente "Interactive Calendar" y los tres deben poder agregar cosas.

**Tesis:** no hay conferencia de payments para merchants en el Bay Area en la ventana; el viaje se gana con reuniones (226 cuentas TCL con sede Bay Area, 44 High) y eventos propios (desayuno 8-oct, cenas 14 y 28-oct, propuestos).

**Hechos verificados 27 y 28-sep:** FTW día 1 $495; Money20/20 pase estándar $4,199 ($299 menos por pase comprando 3+ juntos), JP Ortega habla 20-oct 3:15pm y Mauricio Schwartzmann 19-oct 1:15pm, también Perplexity, eBay, Upwork y Navan; GamesBeat Next $899; Gamesforum SF NO vende pases a proveedores, solo patrocinio (los cancela y reembolsa); Disrupt $949; bloque Tech Week 5 y 6-oct gratis (Fintech House, Fintech Coffee, Visa 4pm, Mastercard 5:30pm con 9 cupos); Subscription Show no se pudo confirmar que exista. Samuel tiene vuelo a Vegas aprobado; de German y Joaquín no había solicitud.

**Why:** German pidió que el viaje sea muy exitoso en merchants grandes, reuniones y comunidad de payments.

**How to apply:** cambios de contenido van en `events.json` o `src/page.html`, luego build y republish. Relacionado: [[project-sf-relocation-fall-2026]], [[project-sf-trip-budget-sheet]], [[project_tcl_final_list_misaligned]].

## project_skydance
*Skydance = nombre del grupo Paramount + Warner Bros. Discovery desde el cierre del 6-oct-2026 (David Ellison CEO, Ynon Kreiz co-CEO); incluye Paramount+ y HBO Max. Cuenta Paramount en Salesforce: OPP / LOST, la trabajan Alejandro Albarracín + Samuel Carreño; bloqueo = integración con Recurly. HBO Max es la cuenta de German*  
*type: project · last updated 2026-10-06*

**Skydance (6-oct-2026):** Paramount Skydance cerró la compra de Warner Bros. Discovery ($31/acción, ~$110B EV) y el grupo combinado se renombró **Skydance**. CEO David Ellison, co-CEO Ynon Kreiz (ex Mattel). Dentro: Paramount+, HBO Max, CBS, CNN, Nickelodeon, TNT, Pluto TV, Skydance Animation/Interactive/Sports. Cierre posible tras el acuerdo con 12 fiscales estatales y el WGA (sep-2026). Skydance Media como standalone ya no existe (se fusionó con Paramount el 7-ago-2025).

**ICP:** sí, enterprise streaming subs, 60+ países, dos stacks de pago distintos que ahora conviven. Listas locales: Paramount+ fit 9 en `Lists & ICP/yuno_icp_master_bank.csv` y HIGH/8 en `Yuno_ICP_Target_List_B2C_US.csv` (SF Status "OPP / LOST").

**Cuenta Paramount en Salesforce (crmId 001Hu00003OAHy5IAH):** la trabajan Alejandro Albarracín (lleva la comunicación) y Samuel Carreño (SDR). Calls Gong: 16-ago-2024, 9-oct-2024, 27-ene-2026 ("Paramount / Yuno - Payments"). Contactos: Maria Perera, Alan Moreno, Rory Fitzpatrick, Edinam Agbenyeke. Querían APMs (Mercado Pago, Pix, OXXO) + network tokens. **Bloqueo:** Paramount+ factura con Recurly y solo avanza con partners ya integrados a Recurly; sin fecha confirmada no asignan ingeniería. Último toque: mar-2026, intento de verse en MPE Berlin. German conoció a Erika Seberhagen (Paramount, no es de payments) en Stripe Tour NYC oct-2025 con Drew Snyder.

**Lado WBD:** HBO Max es cuenta de German, ver [[project_hbo_max]] (Spreedly + Adyen/Checkout/iyzico, SAP BRIM; Ashwyn Singhal decisor). El ángulo post-cierre es la consolidación de dos stacks de suscripción (Recurly en Paramount+ vs Spreedly/SAP BRIM en HBO Max), no "les falta orquestación".

**Antes de tocar Paramount:** coordinar con Alejandro (dueño de la relación Paramount y también de Karime en HBO Max).

**Liderazgo DTC post-cierre (anunciado 5-oct-2026):** JB Perrette (ex WBD, mano derecha de Zaslav) = Co-Chair & Chief Business Officer de Skydance DTC y Skydance TV, con oversight directo de distribución, ads, DTC strategy y business operations. Casey Bloys (ex HBO) = Co-Chair & Chief Content Officer de Skydance DTC. George Cheeks sigue como co-chair de Skydance TV. Zaslav, Wiedenfels y Bruce Campbell salen. Paramount+ y HBO Max se fusionarán en un solo servicio "over time", sin fecha, nombre ni precio. Implicación: el equipo de payments de HBO Max (Ashwyn, Karime, Robert, Michael) ahora reporta dentro de Skydance DTC bajo Perrette, que viene del lado WBD; nada publicado sobre quién lidera payments en la unidad combinada.

## project-slides-api-token-dead
*Google Slides API token (~/.config/yuno-slides/token.json) dead since 2026-09-18: its GCP project 304613953104 was deleted; engine.py edits fail with 403 until re-auth*  
*type: project · last updated 2026-09-22*

Since 2026-09-18 the Slides API path used to edit Google Slides decks (Palco, Higgsfield, Appmaking) returns 403 "Project #304613953104 has been deleted". The OAuth client behind `~/.config/yuno-slides/token.json` and `Design System/client_secret_304613953104-*.json` belongs to that deleted project. `Industry/AI/Higgsfield/build/engine.py` (service(), replace_requests) still works once a fresh token exists.

**Why:** Google Slides edits are the delivery path for German's proposal decks; without the token, Claude can only prepare scripts and text, not apply changes.

**How to apply:** Before promising a Slides edit, test `service().presentations().get(...)`. If 403 CONSUMER_INVALID, ask German to run `Deals/Appmaking/build/auth_slides.py <new client_secret.json>` (new GCP project with Slides API enabled, Desktop OAuth client). The claude.ai Google Drive connector cannot edit Slides content (update_file is metadata only) and the auto-mode classifier blocks reading other credential files (mcp-gdrive). Pending edit queued: `Deals/Appmaking/build/fix_s13_alerts.py` (see [[project-appmaking]]).

**21-sep-2026:** sigue muerto; el refresh ahora devuelve `deleted_client: The OAuth client was deleted`. El conector de Drive de claude.ai solo copia archivos completos y cambia título/carpeta (no duplica ni edita slides), y subir un PPTX editado por base64 no es viable por tamaño. Ediciones en cola: Appmaking `dup_s13_addons.py` y la revisión de Palco del 18-sep.

**22-sep-2026, VÍA NUEVA QUE FUNCIONA (usada para FlightHub): service account.** `gcloud auth application-default login` con scopes sensibles queda BLOQUEADO por Google para el cliente por defecto de gcloud ("This app is blocked"), así que no sirve. Lo que sí sirve: service account `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` (proyecto GCP personal de German, Slides/Sheets/Docs/Drive APIs habilitadas), llave en `~/.config/gsuite/sa.json` (0600). Requisito por archivo: German comparte el Slides/Sheet/Doc con ese correo como Editor (el conector de Drive de claude.ai NO puede compartir con cuentas externas al dominio: "The caller does not have permission"). Auth en Python: `service_account.Credentials.from_service_account_file(SA_KEY, scopes=[...])`. Ejemplo completo con dry-run y replaceAllText por slide: `Deals/FlightHub/build/apply_blocker_fixes_2026-09-22.py`. Verificación visual: exportar PDF con el conector de Drive (download_file_content, application/pdf, base64 → PyMuPDF). Gotcha: replaceAllText no re-ajusta cajas; si el texto crece, revisar el borde derecho (bbox) y estrechar con updatePageElementTransform (scaleX; el texto no se escala).

## project_stripe_tour_berlin_event
*Stripe Tour Berlin event deck build — batched roster of ~100 companies, progress tracker*  
*type: project · last updated 2026-06-19*

Building the Stripe Tour Berlin events playlist in yuno-sales-pitch-maker, replicating the [[project_stripe_tour_paris_event]] exercise. Event `stripe-tour-berlin` lives in `src/data/events.js` (city Berlin; metadata = date/venue/booth/attendees/sessions left as placeholders per user, to fill later). Inside an Event every company renders the Event Deck Template from merchant content, so `deckType` is just a display label; all need a merchant row + logo + business overview.

**Per-company pipeline (from Paris):** `_finish-merchant.sh <slug> <domain>` (untracked, in scripts/) auto-fetches logo via logo.dev, normalizes to white PNG (`_logo-one.mjs`), inserts local files (`_add-merchant.mjs` → merchants.generated.js + merchants.csv + business-overviews.json) and upserts the Supabase `merchants` row. Reads service key from `/tmp/.sbkey` (populate from .env.local SUPABASE_SERVICE_ROLE_KEY). Requires `/tmp/<slug>.json` ({slug,name,industry,overview}) and `/tmp/<slug>-row.json` (full Supabase row). Then add entry to the berlin `companies:` array and commit/push to `main`.

**Research is delegated to parallel general-purpose subagents** (one per company, ~15 per batch) returning a single JSON object {slug,name,domain,industry,overview,row}. Rules enforced: no fabrication (omit if unverifiable), no em-dashes, no "no small feat", PSP decision tree (≥2 confirmed→list; 1→list only it; 0→seed region PSPs + psps_disclaimer). Capability set = Yuno's 4 standard levers (Smart Routing/Failover+Recovery/1,000+ Local Methods/NOVA) with merchant-specific scale.

**GOTCHA:** `business-overviews.json` country `share` must be a FRACTION (0-1); SlideBusinessOverview does `share*100` and filters `>=0.01`. Agents return percentages → divide by 100 before writing.

**STATUS: COMPLETE (2026-06-19).** 109 companies wired into the berlin `companies` array. 12 reused existing decks + 97 newly built across 7 batches (commits b972e35, 02faf29, f14bcea, b4274f0, f8773dc, 3b8c34c, 37f1972, baf7ab1). All have Supabase rows + logos + business overviews and build/deploy clean.

**Skipped as unidentifiable** (agents returned `unidentified`; never fabricated): `Harvest AI`, `Savigny` (only match is Savigny Partners, an M&A advisory, not a merchant), `MWMV GmbH` (real but a one-person consulting micro-firm, no payment surface), `Nda` (placeholder/NDA artifact). If the user can supply the real identity/domain for any, build them with the same pipeline.

**Judgment calls applied across the build:** illustrative PSP seeds + disclaimer where no PSP was publicly confirmed; new industry buckets coined where needed (Energy & CleanTech, Industrial & Consumer Goods, InsurTech, Subscription Commerce, Logistics & Delivery, Consumer Goods & Distribution, Travel & Corporate); revenue marked estimated/omitted when not verifiable; country `share` divided by 100 (fraction) at emit time; U.S. Bank Europe deckType tagged 'acquirers' (Elavon), rest 'merchant'.

**STILL TODO (not done):** event metadata (date/venue/booth/attendees/sessions) is still placeholder — fill `EVENTS['stripe-tour-berlin'].event` when the team supplies real logistics. Optionally backfill es/pt/fr per-merchant translations via the translate endpoint.

User decisions during build: batches of ~15 (push after each); research ambiguous names with best interpretation; event metadata = placeholders for now.

## project_stripe_tour_paris_event
*Stripe Tour Paris event playlist build — progress and remaining companies*  
*type: project · last updated 2026-06-11*

Building the `stripe-tour-paris` event playlist in yuno-sales-pitch-maker (events vertical, `src/data/events.js`). An Event references existing decks by `{name, deckType, slug}` — it does NOT duplicate deck data.

**Event Deck Template engine shipped 2026-06-05 (commit 5be59ab).** Events are no longer just a playlist of normal decks: opening any company inside a tour now renders a lean Event Deck (EVENT_DECK_ORDER in SlideViewer) populated with that merchant's research. Each event in events.js carries an `event` object (name, logo, dateLabel, venue, city, booth{number,hall,note}, attendees[]{name,title,photo}, sessions[]{title,speaker,time,stage}). New slides: SlideEventOverview (briefing+booth), SlideEventProgram (Yuno sessions+team). App attaches EVENTS[key].event as data.EVENT; SlideViewer keys off data.EVENT; SlideCover shows an event badge; SlideCTA shows a "meet us at {event}" close. Stage 3 (per-merchant event decks) works automatically for every company in the tour. **Stage 2 DONE (commit 2d5ba4b):** Stripe Tour Paris filled — booth 11 (Expo Hall, Level 1), June 16 2026; 6 Yuno attendees (Sonal Rankin GM Europe, Kim Reynolds BD Manager, Francisco Quintana Partnerships Manager, Caio Freitas Sales Engineer, Yamin Lahmeur SDR, Magdalena Torrealba SDR); 1 session (June 16 10:30-10:50, Partner Theatre, Yamin speaking, FR title). Attendee face cards added (commit 5e239ab): 6 headshots at public/events/stripe-tour-paris/<slug>.jpg (square 420px smart-crop), wired into attendees[].photo. Venue building name still TBC (shows "Paris"). Event share links carry the tour via `?e=stripe-tour-paris` (SlideCTA buildShareUrl + App parse) so shared event-deck links reopen as the event deck. To add a company that already has a deck, just append an entry; for one without a deck, run the full `/builddeck` flow first, then append. deckType: merchant | banking | acquirers | wallets.

User opted in (2026-06-10) to: auto-source logos from the web, build in priority batches.

User decided (2026-06-10): build sub-brands SEPARATELY (own deck each), not folded into parent.

**Done (35 of 54 attendees):**
- Pre-existing decks wired in: Airbnb, Amazon, Apple, ElevenLabs, Mews (Mews uses deckType `acquirers` — Mews Payments embedded payfac angle).
- Batch 1 (commit 43883f2): LVMH, Kering, Chanel, Accor, Orange, Ubisoft, Ledger, AXA, Stellantis, Michelin. New industries: "Telecom & Connectivity", "Insurance", "Automotive & Mobility".
- Batch 2 (commit f9c2c7a): ManoMano, Back Market, Fnac Darty, Leroy Merlin, La Redoute, TheFork, Sorare, Wonderbox, Banijay Entertainment, Veja. Some logos are icon-only / logo.dev (Wonderbox came as "Collectivités" variant) — swap if user drops better files in Logos/.
- Batch 3 (commit 285961b): SFR, RED by SFR, Altice France, Free2move, Rakuten, Rakuten France, Longchamp, Balenciaga, Match Group, Canal+ myCanal (slug canal-mycanal). NOTE: git history was reorganized around 2026-06-05 (user's Event Deck Template commits 5be59ab/2d5ba4b absorbed the data-file writes); batch-3 data files were already in HEAD, so 285961b only added events.js entries + 10 logos. Rakuten=in-house Rakuten Payment PSP; Rakuten France & Balenciaga single-PSP (Mangopay / Adyen-via-Kering). Free2move logo: their site SVG is light-grey, reprocess by forcing white from the alpha mask (logo.dev returns the off-brand "eSolutions" co-brand).

**Remaining ~19 attendees** (mostly French): Paris Attitude, Le Monde, Le Figaro, Orange Business Services, Canal+ already done, Mövenpick Hotels & Resorts, AXA en France, L'olivier Assurance, Benda Bili, Ritz Paris, AWS, Pixmania, PMU, Taster, SundayApp. **Banking deckType (5):** Cofidis Group, Cofidis Business Solutions, Crédit Agricole Personal Finance & Mobility, Groupe BPCE, BPCE Payment Services.


Note: AXA en France / Orange Business Services / Rakuten France / RED by SFR are sub-brands of parents already built or in the list — decide whether to build separate decks or fold into the parent before doing them.

**2026-06-11 expansion to user's ~70-company list (target ~70-72):** tour was 45, user gave full list. Wave 1 DONE (commit 306f06e) added 7 -> 52: L'Oréal(loreal), Louis Vuitton(louis-vuitton), EssilorLuxottica(essilorluxottica), Club Med(club-med), Vestiaire Collective(vestiaire-collective), Leboncoin(leboncoin) + Hyatt(hyatt-hotels, pre-existing). Essilor/Leboncoin/Vestiaire logos fell back to name text (no clean public source). **REMAINING ~20 to build:** merchant: Benda Bili, Pixmania, PMU, Taster, SundayApp, Bouygues Telecom, CANAL+ (separate from canal-mycanal), Click and Boat, Mon Marché, La Bécanerie, Getaround, Axa Insurance Ireland, Tupperware, Jonak, Gedimat Terrasson Distribution. banking (use deckType merchant in-event anyway): Cofidis Group, Cofidis Business Solutions, Crédit Agricole Personal Finance & Mobility, Groupe BPCE, BPCE Payment Services. (List artifacts to ignore: "Admiral Group Plc" = part of L'olivier; "Mavenpick" = Mövenpick already in tour.)

**2026-06-11 list COMPLETE: tour = 71 companies** (wave 2 commit e384859 added 14 merchants: Bouygues Telecom, CANAL+ (canal-plus), Getaround, Click&Boat, PMU, Pixmania, Taster, Sunday (sunday-app), Tupperware, AXA Insurance Ireland, Jonak, Mon Marché, La Bécanerie, Gedimat; wave 3 commit 7d70df9 added 5 banking: Cofidis Group, Cofidis Business Solutions, Crédit Agricole Personal Finance & Mobility, Groupe BPCE, BPCE Payment Services — all deckType 'merchant' so they render the event deck with their own research). Benda Bili SKIPPED = it's Sézane's parent (Sézane already in tour). All new have Supabase rows + business-overviews + manifest + CSV. **Logos still text-fallback (drop into Logos/ or public/merchants/<slug>.png to fix):** essilorluxottica, leboncoin, vestiaire-collective, bouygues-telecom, pmu, pixmania, taster, sunday-app, tupperware, jonak, la-becanerie, gedimat, click-and-boat. (CANAL+, L'Oréal, Louis Vuitton, Club Med, Getaround, AXA Insurance Ireland, Mon Marché + all 5 banking have logos.)

Build recipe used (reusable): fan out research to parallel general-purpose subagents (one per company, structured JSON return + logo URL), then one Node script writes business-overviews.json + manifest + CSV + /tmp supabase rows, a second reuses [[builddeck]] `toWhiteOnTransparent` to process logos, curl upserts rows, edit events.js, build, commit, push. Convert all revenue to USD (slide hardcodes `$`). PSP chips = gateways/PSPs/MoR only (see [[feedback_psps_chips_scope]]); slide renders top 4.

## project_stubhub
*StubHub (STUB) research — global ticket marketplace, payout pain, no orchestrator, high-fit ICP*  
*type: project · last updated 2026-07-30*

StubHub Holdings (NYSE: STUB, IPO Sept 2025, CEO Eric Baker) = global two-sided secondary ticket marketplace; runs **StubHub** brand in North America + **viagogo** internationally (200+ countries, 30+ languages, 45+ currencies, $9.2B GMV FY2025). Scored 🔴 High (~17/20).

Lead angles: (1) **seller payout delays** = loudest complaint AND deliberate float strategy (~$41M interest income on held seller cash) → Yuno unified pay-in + payout; (2) **cross-border acquiring on the viagogo LATAM/APAC tail** with no local entity → local acquiring + smart routing; (3) fresh IPO = margin/auth-rate scrutiny; (4) FTC $10M drip-pricing settlement (Apr 2026).

No payment orchestrator found. Card-acquiring PSP NOT confirmed (SEC 403 + JS support pages) — needs S-1 read + live checkout. Malta entity "YSG Safe Processing Ltd" may be in-house processing. CFO Connie James; open Director of Treasury Operations role. Confirmed: BNPL Afterpay/Klarna/Zip/Affirm, wallets+PayPal+cards; payouts via PayPal/Payoneer/bank. Research file: data/research/stubhub-2026-07-09.md. Related: [[reference_buyer_personas]].

Deck live (2026-07-30): deck.yuno.tools/m/stubhub, commit a6b7bb7. PSPs seeded Stripe+Adyen with disclaimer (acquirer unverifiable); FY25 numbers refreshed from Mar-2026 earnings release ($9.2B GMS +6%, $1.7B rev, 19% take rate); capabilities_live = payouts only; countries US 92.9% / CA 2.1% (SimilarWeb jun-2026).

## project-suno-jasper
*Suno account — full outreach history (LinkedIn + email campaign), research brief, and live meeting state as of 2026-08-06.*  
*type: project · last updated 2026-10-02*

**Prospect:** Jasper van Rijckevorsel (He/Him), Music + Engineering @ Suno. 1st-degree LinkedIn connection.

**Chat history (LinkedIn):** full verbatim transcript + analysis saved at `Deals/Suno/jasper-linkedin-thread-2026-02-20_2026-04-29.md` (repo). Load-bearing facts:
- 2026-02-20 opener name-dropped OpenAI, Lovable, Whop, Hotmart, GoFundMe, McDonald's, SpaceX, Uber (relevant: the Aug 7 meeting audience is ex-Uber/ex-Disney payments people who can validate those claims).
- 2026-03-05 Jasper: "early stages of optimizing our mobile payment flows and potentially moving payment vendors... I'd love an honest assessment." = active vendor evaluation, asked for assessment not pitch.
- 2026-03-06 German: 3 angles (single-acquirer decline recovery w/ Livelo 50%, smart retries for mobile leakage, APMs/Pix in days) + BC `deck.y.uno/sunobc`. Jasper: "It's a great answer, let me look at the deck... connect now or a little further into the future." = objection was TIMING, never fit.
- 2026-03-10 / 03-18 / 04-10 follow-ups no reply. Apr 10 asserted "your current Stripe setup" (never corrected; later verified) + App Store/Google Play billing rethink as "single biggest saving" + Stripe Sessions SF invite.
- 2026-04-29: German sent one more message (content unknown, blank in paste); Jasper reacted with emojis 😆👏👍 (no text). Weak-but-positive signal.

**Email campaign history (German's Gmail, all SENT, zero email replies from Suno):**
- 2026-02-18: cold wave "hobby making music" opener to 9 contacts: jasper.vr@, ekew@ (Eke), georg@ (Georg Kucsko, co-founder), miles@, martin@ (Martin Camacho, co-founder), brinn.sanders@, franklin@, rebecca@, henry@ (all @suno.com). 4-touch cadence each: opener → insights → Rappi success case → onepager (through 2026-03-05).
- 2026-03-12 a 03-16: "Check out this Business Case" wave to the same list + jack@suno.com. Jack got an Apr 14 follow-up referencing the Jasper LinkedIn conversation.
- 2026-05-25: "Picking up Suno & Yuno" to jasper.vr@suno.com (email mirror of the LinkedIn thread; references mobile flow work + vendor evaluation).
- 2026-06-03: group thread "Congrats on the Series D | We prepared a song" to martin@, jasper.vr@, jeremy@ (Jeremy Sirota, CCO), georg@, jack@; cc João Athas + Alejandro. Includes BC deck.y.uno/sunobc + a Suno-generated song about Yuno. Follow-ups: João 06-11, German adds CRO Justo Benetti 06-16 (name-drops xAI/OpenAI/Lovable), German "door stays open" 07-28.

**MEETING BOOKED, AND ES INBOUND: "Suno & Yuno", Fri 2026-08-07 2:00-2:30pm Colombia (3pm ET), Google Meet.** Attendees (all accepted): Justo Benetti (organizer), German, **madden.titus@suno.com**, **gurwinder.gulati@suno.com**. Madden escribió a Justo por WhatsApp el 08-06 (transcript en `Deals/Suno/madden-whatsapp-justo-2026-08-06.md`): lleva **3 días en Suno** (ex-Disney), nombró "payment orchestration" sin que nadie se lo pitcheara, y dijo "I don't know what I don't know". Justo comprimió de "next week" a mañana. Postura para la call: discovery + entregar el mapa del research como regalo, ayudar a definir criterios de evaluación, y ojo con build-vs-buy (Gurwinder ex-Uber). NO pitch de categoría: Madden ya la nombró.
- Madden Titus: ex Director, Payments & Fraud Product Management at Disney Streaming (2021-2026), ex-Netflix payments/fraud analytics (2016-2020), Yale EMBA, NYC. El claim de Spotify quedó DESCARTADO (era Lex Ledger, otra persona; nunca mencionarlo). Activo clave: charla era-Netflix "Shining a Light on the Transaction Lifecycle" (false declines = datos y fraude desconectados en la cadena = la tesis de Yuno en sus palabras). Vivió el exit de Disney+ del App Store (oct 2024). Suno title unverified, check LinkedIn. Meeting brief completo: `data/research/suno-meeting-brief-2026-08-07.md` + Google Doc "Meeting Brief: Yuno <> Suno (Aug 7, 2026)". ⚠️ Dato sensible: breach de Suno nov-2025 (revelado jul-2026, 55.3M emails + registros Stripe, class action jul-24); NUNCA sacarlo primero en la call.
- Gurwinder Gulati: [INFERENCE, likely] Senior SWE / Tech Lead of Uber One Membership Payments at Uber, ex Netflix Ads eng, LinkedIn, Facebook, Hulu (weekday.works/getprog profiles). Verify LinkedIn before the call.
- Signal: Suno hiring senior payments product + payments infra people confirms the vendor evaluation Jasper mentioned in March is real and now staffed.

**Current state (2026-08-06):** still silent since the 2026-04-29 emoji reaction. Full /research brief done 2026-08-06 → `data/research/suno-2026-08-06.md` (score 13, 🔴 High). Fresh hooks now available: (1) WMG settlement Nov 2025 + licensed-model relaunch 2026 with download-overage purchases; (2) Spark incubator already paying cash grants to artists + opt-in artist licensing = payout rails incoming (Rosie Nguyen is "Head of Creative Economy and Monetization"); (3) $300M ARR / 2M paid subs (Feb 2026) + $400M Series D at $5.4B (Jun 2026) + MBW "building toward IPO readiness" (Jul 2026); (4) BBB rating F, 93 complaints, recurring card-decline reviews = his March "optimizing payment flows" concern got publicly worse. Stripe confirmed sole direct processor per Suno's own ToS/help center; 17 currencies, single US entity (cross-border BR/DE/JP/KR/IN). Other door if Jasper stays cold: Jeremy Sirota (CCO, ex-Merlin) or Controller Jake McNeill (ex-Crunchyroll).

**PRIMERA LLAMADA REAL, 2026-08-07 (34 min), transcript en Deals/Suno/call-transcript-summary-2026-08-07.md:** ⚠️ Madden pidió explícitamente "no AI notetakers/recorders" al inicio, Justo dijo "no problem", pero el Yuno Notetaker igual grabó todo y llegó transcript completo al correo de German — riesgo de confianza sin resolver, hablar con Justo. Confirmado en vivo: Madden 4 días (no 5), Gurwinder ~1.5 meses (no arrancó junto con Madden), son todo el equipo de pagos, sin 1:1 entre ellos aún. Stack: usan RevenueCat para IAP (su webhook se cayó ESE MISMO DÍA), Stripe hosted checkout + Radar + 3DS. Madden confirma "solo entidad US" y nombra Japón/PayPay como gap real de recurrencia + "Stripe has a really bad retry scheduler" (valida la tesis central del BC en su propia voz). Justo dijo el número "$12M/año" en voz alta; Madden respondió "I think you're underselling yourself" (número aceptado como conservador, reacción muy positiva). Madden reveló que el litigio UMG/Sony tiene a legal "heads down", ralentizando la velocidad de contratación de nuevos vendors. Justo reveló en la llamada trabajo activo con OpenAI/Sora/Whop($3B TPV)/Anthropic frente a un prospecto distinto — patrón a vigilar (ver [[project_riot_games]] incidente similar). Pedidos de Madden: case studies de migración de Stripe, reference calls (Justo ofreció esto). NO se cerró fecha concreta para sesión técnica ni data sprint — sigue pendiente, empujar activamente.

**Estado 2026-09-03:** Technical deep dive movido al **17-sep-2026** (Gur se lo pidió a German ese día). Madden estará fuera la semana del 7-sep. NDA en curso: Madden le dijo a Justo esa semana que ya tenía "figured out" cómo funciona el NDA; German le escribe por WhatsApp directo (Justo le pasó el número, chat abierto 3-sep) para que lo comparta y avanzar firmas antes de su salida. Madden es el encargado de producto de payments en Suno.

**Dato de stack (German, 2026-08-06):** Suno YA tiene Pix en Brasil (el help center público NO lo documenta; la lista oficial de métodos está incompleta). Gaps confirmados por German: PayPal en web, Klarna, SPEI, OVO. Ángulo fino para decks: tienen métodos one-time (Pix, UPI) pero no los rails recurrentes de suscripción (Pix Automático, UPI Autopay). Nunca afirmar ausencias solo desde el help center; checkout real manda.

**Why:** Jasper is interested but stuck — likely still mid-vendor-evaluation or priority shifted. Emoji reaction = signal he still sees German's messages.

**How to apply:** Any new outreach to Jasper must lead with something new (insight, data point, peer benchmark, or product news) — not a recap of prior pitch. Already-shared deck lives at `deck.y.uno/sunobc`; new deck should differentiate. See [[feedback-no-false-info-disclaimer]] when citing Suno-specific stats.

**FRENO DE MADDEN + OFERTA SUBS GRATIS, 2026-09-21:** Madden respondió al recap con el link DocuSign del NDA de Suno (German lo reenvió a ivvy@y.uno para firma) y avisó: "we will slow down a little... we first need to spend time on our commerce infrastructure before we can make any moves away from Stripe as we are so deeply intertwined with their billing. I don't expect we will make significant progress this quarter." Jugada acordada con Justo (WhatsApp 21-sep): ofrecerles el subscription engine de Yuno **gratis por 6 meses mientras construyen el suyo in-house, con el equipo ayudándolos**; objetivo interno = que salgan de Stripe Billing ya y, una vez dentro, venderles subs + orquestación + recons. Justo: NO llamar a Madden todavía, darle tiempo de contestar el correo. Borrador de respuesta en Gmail (hilo "Suno + Yuno", 21-sep) en dos partes: (1) cuándo podrán priorizar el proyecto, (2) oferta del engine + pedir call de 30 min sobre subs con Madden y Gur. Ojo al pitchear: el engine NO tiene proration, invoicing/tax ni dunning emails (ver [[reference-subscriptions-stats]]); posicionarlo por control de retries (su dolor #1) y agnosticismo de procesador, no como reemplazo completo de Stripe Billing.

**NDA BLOQUEADO EN VALIDACIÓN, 2026-09-21:** el PowerForm de DocuSign de Suno solo deja ver el documento al firmar, y quien valida en Yuno no es el signatario. Borrador en Gmail (hilo "Suno + Yuno", respuesta al mensaje de Madden) pidiéndole el NDA en PDF/Word para validarlo primero; luego se firma por su flujo de DocuSign. Pendiente: que German lo envíe y que Madden mande el archivo.

**TECHNICAL DEEP DIVE HECHO, 2026-09-17 (13:00 COT, Jarrett presentó; notas en Deals/Suno/call-notes-2026-09-17-technical-deep-dive.md).** Confirmado por Suno: Stripe only, US entity only, **Stripe Billing** para suscripciones web y app (mismo precio hoy), web y app separados, sin multi-país. Dolor #1: el retry/recovery de Stripe. **Quieren sacar billing de Stripe Billing y controlarlo in-house** (encaja con el ledger rebuild y con el engine de subscriptions de Yuno, quedó como tema "later"). PCI no es driver (iframe). Lo que resonó: routing por reglas con 100+ campos + metadata y decline groups; MIT/CIT separados con dunning que puede quedarse en Suno; smart routing ML (necesita 2+ procesadores, split 20/80 para A/B); agnostic 3DS reutilizando la autenticación entre proveedores; wallets desencriptadas como card para retries entre adquirentes; provider health; vault agnóstico con export de tokens desde Stripe. Primer paso recomendado: auth rate en un mercado. Parqueado para otra sesión: data visibility, insights/reporting, monitors, reconciliaciones, in-house subscriptions. **Next steps:** Caio envía sandbox + docs de SDK y reporting; agendar sesión de estrategia de routing. **NO se tocaron:** NDA, reference call de migración desde Stripe, fecha del data sprint; siguen abiertos. Debrief interno pendiente. FUP en borrador de Gmail el 17-sep.

**22-sep-2026:** el correo pidiendo el NDA en PDF/Word SÍ se envió (21-sep 1:26pm COT, hilo "Suno + Yuno"); sin respuesta de Madden. German prepara WhatsApp a Madden con dos puntos: recordatorio del PDF del NDA y que Sean Calabro (GM North America) está en Nueva York la semana del 21-sep y quiere conocerlo en persona (café o cerveza, 30 min, sin agenda). Ver [[sean-calabro-manager]].

**2-oct-2026 (dicho por German):** Justo le escribió directamente a Madden para avanzar. La pelota está en Justo/Madden; German no debe duplicar el toque. NDA en PDF sigue pendiente.

## supabase-deck-down-sep-2026
*El proyecto Supabase del deck tool (mlwiosgalwsroisdkytl) dejó de resolver el 30-sep-2026; vive en la org de Isabella Ponce*  
*type: project · last updated 2026-10-01*

Verificado el 30-sep-2026: `mlwiosgalwsroisdkytl.supabase.co` y `db.mlwiosgalwsroisdkytl.supabase.co` devuelven NXDOMAIN en todos los resolvers (local, 1.1.1.1, 8.8.8.8, DoH de Google). supabase.com responde normal, así que no es la red local. El 23-sep-2026 todavía estaba arriba (1,332 filas en `merchants`, según docs/HANDOVER.md).

El proyecto vive en la organización "isabellaponce-spec's Org", en plan Pro desde el 10-ago-2026 (correo de bienvenida en Gmail de German, usuario Supabase `germantatism`). Pro no pausa por inactividad, así que la causa es pausa manual, borrado o un cambio de plan o facturación en esa org. Causa NO confirmada: en el Gmail de German no hay correo de pausa ni de borrado.

Isabella Ponce De Leon (isabella.ponce@y.uno) no aparece como usuaria en Slack al 30-sep-2026 y su último correo a German es del 19-may-2026; posible salida de Yuno, sin confirmar. Si la org y la tarjeta eran suyas, eso puede explicar la caída.

Esta sesión (VSCode) no tiene herramientas de navegador (ni Claude in Chrome, ni browser integrado, ni computer use), y buscar tokens de Supabase en la máquina está bloqueado por permisos. Para operar el dashboard hace falta que German conecte la extensión de Chrome o entregue él mismo un access token.

No hay export completo local de `merchants` (solo merchants.csv parciales y los JSON de auditoría de mayo).

**Why:** alguien pidió por WhatsApp revisar si el Supabase seguía arriba y que lo agregaran como colaborador; desde la CLI no se puede ni confirmar la causa ni invitar miembros (requiere el dashboard o un access token personal).

**How to apply:** antes de cualquier trabajo que lea o escriba decks ([[project_deck_override_layer]], [[project_deck_edit_button]], /builddeck), comprobar que el host resuelve. Si sigue caído, no intentar escrituras y avisar a German. Relacionado: [[project_supabase_service_key_location]], [[project_deck_tools_handover]].

**1-oct-2026, sigue caído y el efecto es visible para prospectos:** con Supabase sin resolver, TODOS los decks (`/m/<slug>` en ss26.yuno.tools y deck.yuno.tools) caen a `_default.json`: slide 3 dice "No PSPs publicly disclosed" y los diagnósticos muestran placeholders `[merchant]`, `[MAU count]`. Verificado con Playwright headless contra el link vivo de Thinkific.

**Salida mientras tanto, filas fijadas en el bundle:** `src/data/pinned-merchant-rows.json` (misma forma que una fila de `merchants`). `fetchMerchantContent` en `src/lib/supabase.js` devuelve la fila fijada y NO consulta Supabase para ese slug, así que el botón "Editar deck" no tiene efecto sobre un deck fijado; para devolverlo a Supabase se borra su entrada. Primer deck fijado: thinkific (ver [[project_thinkific]]). Requiere deploy para verse (Neverland vía Kingdom con VPN; Railway no publica main, ver [[railway-stale-sep-2026]]). El contenido de otros decks se puede reconstruir de los transcripts de sesiones anteriores (`~/.claude/projects/-Users-germantatis-Desktop-GTMCoding/*.jsonl`, buscar el GET/PATCH de la fila).

**Verificación local sin deploy:** `npx vite --port 5199` en yuno-sales-pitch-maker, abrir `/m/<slug>` con `sessionStorage.deckOpenEmail` puesto (salta el gate de email); PDF con `/m/<slug>/pdf?sig=gt`, viewport 1920x1080, esperar `window.__PDF_READY__`, `page.pdf` a 1440x810. `vite build` se cuelga si stdin queda abierto: correrlo con `< /dev/null`.

## project_supabase_service_key_location
*Where the Supabase service-role key for /builddeck upserts is stored*  
*type: project · last updated 2026-06-09*

The Supabase **service-role key** for the yuno-sales-pitch-maker `merchants` table (used by `/builddeck` for INSERT/PATCH) is saved in the gitignored file `yuno-sales-pitch-maker/.env.local` under `SUPABASE_SERVICE_ROLE_KEY`.

**How to apply:** During `/builddeck`, load it from that file and use it directly in the upsert curl, do NOT ask the user to paste it and do NOT grep chat history (the harness security classifier blocks credential scanning):
```bash
KEY=$(grep -E '^SUPABASE_SERVICE_ROLE_KEY=' /Users/germantatis/Desktop/GTMCoding/yuno-sales-pitch-maker/.env.local | cut -d= -f2-)
```
Never echo or commit the key. Project URL: `https://mlwiosgalwsroisdkytl.supabase.co`; anon read key is `sb_publishable_2DtpydQUpys--Waoc_Vy-g__fjTrzr2`. The user dislikes being asked for the key every run. Note: the `.claude/commands/builddeck.md` text still says to grep chat history, but that path is blocked, so prefer `.env.local`. Relates to [[feedback_auto_commit_push]].

## project_super_contacts
*Super.com (Yuno target) key contacts and relationship history for outreach*  
*type: project · last updated 2026-10-05*

Super.com (super-com deck) outreach contacts as of 2026-06-02:

- **Akshay Kohli** — leads/fronts **fintech products** at Super.com, has visibility across the whole payment surface (card program, travel booking, Super+ billing, cash advances). German last spoke with him ~mid-2025 (about a year before 2026-06). Primary outreach target; pitch the orchestration layer holistically across all products, not just travel.
- **Sarah Bohmer** — former Super.com contact German also spoke with; has since left Super. Use as a warm-reconnection reference, not a live contact.
- Other named payments people from research: Rick Galasiewski (GM, Payments & Fintech Innovation), Daniel Weisenfeld (CFO), Hussein Fazal (CEO), Henry Shi (co-founder/CTO).

**Why:** Re-engagement, not cold. German has prior rapport with Akshay + Sarah, so messages should open on the relationship before the business case.

**How to apply:** Frame the deck around the confirmed stack: Qolo runs card issuing (do NOT pitch replacing Qolo), the $1B+ travel-booking flow has an unidentified acquirer, and orchestration spans card + travel + Super+ + cash advance. See research brief [[feedback_never_duplicate_decks]] context and the saved brief at data/research/super-com-2026-06-02.md.

**Carol Schimmelpfeng (ex Super.com):** ya no está en Super ("unfortunately Super did not work out"); empieza "a new adventure soon". German le pidió café en SF por LinkedIn (4-oct); ella respondió 5-oct pidiendo esperar a ubicarse. German insistió con tono sin agenda (catch up de industria, solo un mes en SF). Contacto de relación, no de deal por ahora.

**Rick Galasieski (5-oct-2026):** linkedin.com/in/fintechbuilder; registrado en Money20/20 LV 2026 como "GM, Financial Products & Earnings" (la lista raw dice SVP/GM; el case study de Qolo lo llama GM Payments & Fintech Innovation). Email rick@super.com, tel +1 949 933 0791 (hoja de Susana). Es speaker. German nunca había hablado con él. Email de intro + catch-up para café en Vegas (lun 19 o mar 20-oct) EN BORRADOR 5-oct, sin enviar; copia en Deals/Super.com/. También van Joanna Moroz (CoS Fintech, joanna.moroz@super.com) y Gage Sonntag (Head of Data, gage@super.com). Akshay no va. Super levantó Series D $65M (TPG, jul-2026, $1.2B).

## project_tango_live
*Tango Live (tango.me) research — live-streaming/gifting, web top-up already bypasses app-store fee, dual-sided orchestration play*  
*type: project · last updated 2026-07-27*

Tango (TangoMe): live-streaming/creator-economy app, virtual gifting (Coins in / Diamonds out). 450M+ registered users, 170+ countries. MENA/India heavy (traffic: US 18.8%, India 14%, Egypt 7%, Turkey 5.7%, Russia 5.5%). Entities: TangoMe Inc (US, Mountain View, non-EU users) + TangoMe Cyprus Ltd/Technologies Ltd (EU users, Limassol; HQ moved there 2022); Tel Aviv office = payments operations. Founders Uri Raz + Eric Setton (current CEO ambiguous — verify). ~$373M raised, Alibaba $215M (2014), peak val $2.3B. India alone ~$12M/month (Dec-2024 investor deck, best-sourced); global revenue figures = content-farm noise, unverified.

**Strong Yuno ICP — 🔴 High (16).** Key wedge: Tango ALREADY runs a web coin store on tango.me that bypasses Apple/Google 30% fee (up to 40% bonus coins), accepting Visa/MC/Amex + Fawry (EG) + UPI/NetBanking (IN) + crypto stablecoins + "regional methods." Acquirer UNDISCLOSED, NO orchestrator (greenfield). Dual-sided orchestration play: (1) pay-in = smart routing + decline recovery across MENA/India/CIS web top-ups (documented "paid but no coins" + repeated card declines); (2) payouts = 20+ rails run manually (Airwallex, Tipalti, Payoneer, PIX, GCash, STCPay, SBP, carrier billing, all settle USD) with "approved-but-not-settled" complaints → multi-rail redundancy + reconciliation. Catalyst: Dec-2024 Google Play delisting (reinstated May 2025) makes web rail strategic. Personas: Head of Payments/Payments-Ops (Tel Aviv), CTO, VP Finance (US/Cyprus). Never claim they "lack" a method (broad set). Category peers doing same web-topup fee-bypass: Bigo (bigo.tv), TikTok (tiktok.com/coin), MICO, Chamet — good next targets. Brief: data/research/tango-live-2026-07-27.md. Related: [[reference_yuno_positioning]] [[project_thrivecart]] [[feedback_no_false_info_disclaimer]] [[feedback_paypal_not_processor]]

## project_tcl_agent
*Target Company List (TCL) build — German's AE outbound list of ~695 companies being enriched into a full sourced schema in Google Sheets*  
*type: project · last updated 2026-07-02*

German is building his AE Target Company List in a Google Sheet (ID `1QY5pH4Td2sRitHpHI3Eec69sFfGdK2nuY-QMleqEnek`), edited via [[project_gsheets_mcp]]. Goal: every contact must be defensible with a source.

**Tabs:** `TCL` = original preliminary list (~700 rows, keep intact). `TCL_v2` = new 36-column schema tab (created 2026-07-01) with 695 deduped companies imported. 7 dupes removed (Sympla, Activision Blizzard, Picsart, Quizlet, Civitatis, Clapper, Privalia).

**TCL_v2 schema (36 cols A–AJ):** Company, Website, LinkedIn, Description, Industry, Vertical, Business Model, Type, HQ Country, HQ City, #Employees, Public/Private, Annual Revenue, Top Countries (SimilarWeb % share), Current PSPs, Orchestrator?, Multi-PSP Signal, APMs top-5, Payment Pain Points, Competitor-of-Yuno in use, Trigger Events (dated), Insight 1/2/3, Signal/Why Now, Rating(1-10), Tier, SF Status, Status, Stakeholder 1/2/3, Next Step, Confidence, Sources, Last Verified.

**Already filled from old list:** Company, Website, Description, Industry, Type (100%); Signal/Why Now seed + SF Status (~97%). Everything else the agent must research + source.

**Engine:** reuse the `/research` skill methodology (4 parallel agents, integrity rules: URL or omit, `[INFERENCE]` label, never claim a missing APM without live-checkout). Scoring = Yuno rubric from the /research skill (SECTION 11D). Rating = urgency/why-now; Tier = deal size (separate axes).

**Approach chosen:** Fase 0 (dedupe + prefill) DONE. Batch in waves by priority subset German provides (not alphabetical). Pilot 10 first to calibrate. Writes done via node scripts + googleapis (NOT the one-cell MCP tool); workflow returns structured rows, main loop batch-writes.

**DONE:** SimilarWeb key saved at `~/.config/similarweb/api_key`. Pilot (10) ran + written to TCL_v2 rows 2-11. Reusable **engine at `~/.config/tcl-engine/`**: `gen_wave.mjs N` (picks next N rows where Rating/col Z is empty, fetches SimilarWeb, emits `wave_current.js` + `wave_data.json`), then run `Workflow({scriptPath: wave_current.js})`, then `merge_wave.mjs <output-file>` writes back + verifies Rating/LastVerified alignment. Each company = 3 agents (firmo ∥ payments → synth). Scale = **waves of 50, same depth** (German approved). ~685 remaining ≈ 14 waves, ~3.5M tokens each.

**Sources column: REMOVED** — German doesn't want source URLs in the sheet (col AI kept blank). Evidence still cited inline in insights/PSP cells. Enriched-row detection uses Rating (col Z), NOT Last Verified.

**SimilarWeb API RETIRED** (key ran out of July credits after ~110 calls). Top operating countries are now RESEARCHED ONLINE by the firmo agent (fetches public similarweb.com/website/<domain> profile + press + app-store availability), written to col N. Backfilled the 53 already-done rows via `backfill_gen.mjs`/`backfill_current.js`/`backfill_merge.mjs` (countries + re-scored rating).

**PARALLEL WAVES:** running 2 waves concurrently to halve wall-clock. `gen_wave.mjs N` now: skips rows with Rating (col Z) OR in `claimed.json`; emits `wave_<id>.js` + `wave_<id>.json`; reserves picked companies in `claimed.json`. Launch each with `Workflow({scriptPath: wave_<id>.js})`. On completion: `node merge_wave.mjs <output-file> wave_<id>.json` (writes back, verifies Z/AJ alignment, releases claims). Keep 2 in flight: when one finishes, merge it + gen+launch a replacement. Per wave of 50 ≈ 23-25 min, ~3.5M tokens. ~640 remain ≈ 13 waves ≈ ~3h wall-clock in parallel.

**Timing refs:** wave of 50 (3 agents each) ≈ 24 min; backfill (1 agent) ≈ 2 min; pilot(10) ≈ 6 min.

**ECONOMY MODE (2026-07-01, after hitting the account MONTHLY SPEND LIMIT at ~155/695 done):** wf_template.js rewritten to **ONE agent per company on Sonnet** (`model:'sonnet', effort:'low'`), 4-6 searches total, concise ~350-char fields, returns full ROW_SCHEMA directly (no firmo/payments/synth split). ~8-10x cheaper than the 3-Opus-agent version. Deadline: German needs the full list by ~8am 2026-07-02. BLOCKER: account spend limit must be raised at claude.ai/settings/usage before anything runs. Resume = `node gen_wave.mjs 50` → Workflow(wave_<id>.js), keep ~4 parallel, merge each with `merge_wave.mjs <output> wave_<id>.json`.

**COMPLETE 2026-07-02: all 695/695 rows enriched** in TCL_v2. Note: 50-company waves run ~5-17 min each; 90-company waves stalled badly (~7-8h) — keep waves at ~50. Rating spread: 10=5,9=5,8=40,7=90,6=144,5=22,4=211,3=102,2=53,1=23. Tiers: T1=254, T2=194, T3=223. Top (rating≥8,T1): Shein, Expedia, Riot Games, Coinbase, StubHub, Navan, Hopper, Crunchyroll, Klook, Canva, ByteDance, Betway, Betsson, Air France-KLM, StockX. Engine at ~/.config/tcl-engine reusable for refreshes/new companies.

Stakeholders: never scrape Sales Navigator (LinkedIn ToS/ban risk); use Apollo/Clay/Cognism or manual. Tier1/rating8+ rows get human review before outreach. Respect [[feedback_no_false_info_disclaimer]] and [[feedback_no_dashes]].

## project_tcl_final_list_misaligned
*En la TCL (Google Sheet), la pestaña Final List tiene columnas desalineadas desde Insight 3 hasta Confidence; usar TCL_v2 para rating, tier, SF status y stakeholders*  
*type: project · last updated 2026-09-27*

Detectado el 27-sep-2026 en la TCL (Sheet `1QY5pH4Td2sRitHpHI3Eec69sFfGdK2nuY-QMleqEnek`): en la pestaña `Final List` (1,320 filas) las columnas Insight 3, Signal / Why Now, Rating, Tier, SalesForce Status, Stakeholder 1/2/3, Next Step y Confidence no corresponden a la compañía de la fila. Conservan el orden de `TCL_v2` (ejemplo: la fila de Delta muestra los stakeholders de Coinbase; Perplexity muestra al CFO de Sympla). Company, HQ City, PSPs, Priority Score y Priority Tier sí están bien.

**Why:** Pipeline Sync lee de `Final List`, y cualquier análisis que use stakeholders o SF status de esa pestaña sale mal.

**How to apply:** para rating, tier, SF status y stakeholders cruzar por nombre de compañía contra `TCL_v2`. German fue avisado el 27-sep; no se corrigió el sheet. Relacionado: [[project_tcl_agent]], [[project_pipeline_sync]].

## project_thinkific
*Thinkific (Vancouver, TSX THNC, Thinkific Payments = Stripe en 36 países, cero LatAm/India) — Darren (VP Product) solo le contesta a Justo; 4 FUPs sin respuesta; 23-sep-2026 reorganización (96 puestos, foco Plus + FCF); research 24-sep contra prioridades Skool + mensaje para Justo en Deals/Thinkific*  
*type: project · last updated 2026-10-06*

**Thinkific** (Vancouver). Hilo: "Re: Thinkific + Yuno at Stripe Sessions" (Gmail thread 19ddaaf62bafc410). Deck: ss26.yuno.tools/m/thinkific. Reunión presencial en Stripe Sessions SF 30-abr-2026 (booth, organizó Magdalena).

**Contactos:** Darren Guarnaccia, VP Product (ex SVP Product Hootsuite) = quien decide y el único que ha respondido. Tauqeer Ahmad, Group Product Manager = a quien Darren delegó el follow-up de orquestación. Greg (greg@thinkific.com) y Amy Oilman en copia, roles sin verificar. Yuno: Justo (CRO) en cc desde mayo, William Wong (NA Head of AM, Toronto) en cc desde el 9-sep.

**Cronología:** 29-abr German → Darren con deck. 6-may German propone slots. **13-may Justo nudgea y Darren le responde a Justo el mismo día:** "Tauqueer will follow up later this summer when we start to look again into Orchestration." Justo cierra: "think of us as an extension of your payments team". Después: follow-ups de German 15-jul, 20-jul (Q3 roadmap session), 10-ago, 9-sep (viaje a Canadá con William, propone call o presencial) → **cero respuestas de Thinkific desde el 13-may.** Patrón: Darren solo le contesta a Justo (CRO a VP).

**17-sep-2026:** German le pide a Justo que ponga un nudge corto en el hilo (reply-all a Darren y Tauqeer) para reactivar, apoyándose en que Darren dijo "después del verano" y en el viaje a Canadá con William.

**Deck web /m/thinkific corregido 17-sep-2026 (solo Supabase, sin deploy):** slide 3 = 5 diagnósticos nuevos (Penetration Plateau, Coverage Ceiling, One Currency Lock, Recurring Runs On Cards Only, Margin Compression; títulos en `pain_titles`, descripciones en `deckOverrides.diagnostic.painDescs`), 7 APMs exactos (Pix, Boleto, UPI, OXXO, SPEI, GCash, Konbini; Thinkific YA ofrece iDEAL, Bancontact, EPS, P24, Sofort), capability stack todo LIVE salvo BaaS. Slide 4 = tiles Stripe + Razorpay + Paystack + Xendit (`deckOverrides.yunoSolve.archPsps`; nada de LatAm, sus gaps son India, África, SEA) + 5ª card "Subscription Management". Slide 10 = 460+ providers / 190+ countries / Weeks. Gotchas: el chip KYC/KYB solo matchea el alias `kyc` (no `kyc_kyb`) en `capabilities_live`; con 7 APMs + 8 chips el card necesita `deckOverrides.diagnostic.contentZoom` 0.87. Pendiente NO pedido: slide 4 card 03 aún dice "iDEAL in Netherlands, BLIK in Poland" y card 04 "Stripe + PayPal settlement"; fila de impacto +12% / 20–30% sigue ahí (ver [[feedback_published_stats_only]]).

**24-sep-2026, research profundo + mensaje para Justo:** doc en `Deals/Thinkific/thinkific-research-skool-priorities-2026-09-24.md` (commit en main). Hechos clave verificados: Thinkific Payments es Stripe en exactamente 36 países (US, CA, UK, 27 UE/EEE, NO, CH, SG, HK, AU, NZ), ningún país de LatAm, India, Japón, Medio Oriente ni África, sin anuncios de expansión 2025-26; una moneda de cobro y payout por sitio; "Local Currency at Checkout" (Q1-2026) solo para pagos únicos; suscripciones solo con tarjeta, Apple/Google Pay y Link, siempre en la moneda del sitio; Smart Retries de Stripe 8x en 3 semanas, tras eso cancelación salvo Plus (Unpaid 90 días desde 25-ago-2026); fee subs +0.7% (era +0.5%); third-party gateway fee 5/2/1/0.5%, Plus exento. Revenue: US 53%, RoW 33%, CA 14%. 23-sep-2026 reorganización: 96 puestos, ~$19M ahorro, foco Plus + AI, target FCF 25% en F2027, EBITDA Q3 subido a 7-10%; acción +75% el 24-sep (CA$1.20 a ~CA$2.10). Teachable (Hotmart) ya vende Pix/iDEAL/SEPA en 40+ mercados; Kajabi a la par de Thinkific; Skool solo USD/tarjeta. Referencias: Whop y Hotmart son logos públicos en y.uno (cifras internas: Whop $216M recuperados es interno, OK de William Wong; países de Hotmart, OK de Martin Seggewiss); Skool live 15-sep-2026 en ventana POC de 90 días, no nombrar sin OK de Samuel y Sam Ovens; Open English único caso público edtech. Mensaje: versión A (~210 palabras, tres bloques subs / métodos recurrentes / local acquiring, cierre 30 min) y versión B (nudge). No decir: Pix Automático de Hotmart es caso de EBANX no de Yuno; UPI solo en marketing de y.uno; sales tax es de 2023; "$1.34" no existe. Si no responden en ~10 días, siguiente toque a Greg Smith (CEO, supervisa producto desde abr-2026; probablemente el "greg@" del hilo).

**24-sep-2026, borrador en Gmail:** German decidió enviarlo él (no Justo). Draft creado como reply al mensaje del 9-sep (id 1a086a13e92755f1) en el hilo 19ddaaf62bafc410, a Darren + Tauqeer, cc greg@, amy.oilman@, justo@, william@; firmado German; versión A del doc (tres bloques: subs / métodos recurrentes / local acquiring en 36 países, Whop y Hotmart nombrados, Skool anonimizado, cierre 30 min). German lo ENVIÓ el 24-sep-2026 (dijo que ya lo mandó; el draft sobrante se borró). Siguiente: esperar respuesta; si no hay en ~10 días, toque a Greg Smith (CEO).

**1-oct-2026, deck reescrito y fijado en código (commit b78ef76 en main de yuno-sales-pitch-maker, SIN desplegar):** German pasó una lista de cambios ("THINKIFIC DECK CHANGES"). El deck ya no vive en Supabase: la fila está en `src/data/pinned-merchant-rows.json` (ver [[supabase-deck-down-sep-2026]]) y se edita ahí + deploy. 12 slides: slide 3 con el stack publicado como cuatro rails LIVE (Thinkific Payments, Stripe direct, PayPal, App Store and Google Play) + callout "does not load balance", 5 diagnósticos nuevos en orden margen, recurrente, proveedor único, plateau, cobertura (forward looking), 7 APMs con título "Methods not available today, forward looking"; slide 4 con tiles 1 / Weeks / 460+ / 190+ sin footnote y 5ª card; slides nuevos 5 "Subscriptions, the part that works today" y 6 "Thinkific today, and Thinkific on Yuno" (4 columnas + nota "Directional"). PDF borrador en `Deals/Thinkific/Thinkific + Yuno_Oct26_DRAFT.pdf` (firma German).

**Fact-check del 1-oct contra filings y support docs (pendiente decisión de German, el texto quedó como él lo pasó):** (1) split de revenue 51/13/36 es FY2024; el vigente (FY2025 y Q2 2026) es US 53, RoW 33, Canadá 14. (2) El diagnóstico líder "Margin Compression" solo es cierto en Q1 2026 (64% vs 63%, margen bruto 72%); en Q2 2026 el costo de Commerce bajó a 61% (de 64%) y el margen bruto quedó plano en 73%, con el CFO atribuyéndolo a eficiencias de Payments, así que "growing payments is currently costing margin" queda contradicho. (3) "14 percent of traffic" no tiene fuente. (4) "enrollments span 190" es un dato de dic-2020. (5) "a third of volume is recurring" viene del customer story de Stripe (~2023, 32% del GMV). (6) PayPal "USD only" está matizado en los docs (adopta la moneda del sitio con Stripe o Thinkific Payments). (7) TCommerce ya incluye Smart Retries y Card Account Updater, así que "retries are the only recovery layer" y "adds account updater" se solapan. (8) Nombre exacto: "Third-Party Payment Gateway Fee" (Basic 5%, Start 2%, Grow 1%, Expand 0.5%, Plus sin fee; solo primer $1M/año y solo US/CA/UK/EU); Stripe propio requiere Grow o superior. Confirmados: 36 países, cita "our custom, Stripe-powered payment processor", Affirm retirado 27-feb-2026 sin override por sitio, BNPL 3x AOV, penetración 67% y "plateau in the mid-to-high 60-percent range" (CFO Leigh Ramsden, call Q2 del 5-ago-2026), sin Interac en los docs, cancelación inmediata tras Smart Retries en planes no Plus, Branded Mobile 30%. Clientes: ~35,000 (no 60,000); revenue FY2025 $73.2M.

**1-oct-2026, segunda ronda (commit bcbe18b en main, sigue SIN desplegar):** German resolvió 5 de los 8 puntos del fact-check. Aplicado: (1) fuera la frase "growing payments is currently costing margin"; el diagnóstico 01 queda con los datos de Q1 y "True in the United States alone, 53 percent of revenue"; (2) Canadá "at 14 percent" en slides 3 y 6; (3) PayPal sin "USD only"; (4) capa de recuperación replanteada: Thinkific YA tiene Smart Retries y Card Account Updater, el hueco real es que todo vive dentro de un solo proveedor (slides 3, 5 y 6); (5) escalera del fee por plan: 5% Basic, 2% Start, 1% Grow, 0.5% Expand, sin fee en Plus. Siguen en el deck sin decisión: "14 percent of traffic" (sin fuente), "enrollments span 190" (dato de 2020), "a third of volume is recurring" (Stripe, ~2023), y el diagnóstico 01 sigue apoyado solo en Q1 aunque Q2 mejoró.

**1-oct-2026, versión Google Slides (plantilla de propuestas):** https://docs.google.com/presentation/d/1An73Yu_iYBtE-P9Q8wVVD4eg_-L6u8_y-JCvBc7MOWE/edit ("Thinkific + Yuno", 18 slides, copia del deck de FlightHub vía conector de Drive, compartida con la service account). Mismo contenido que el deck web: Why Yuno (slides casa, sin "Selected credentials" porque German no quiere case studies de terceros) / Thinkific today (stack + 5 diagnósticos) / Thinkific on Yuno (solve, subscriptions, tabla de 4 columnas). Sin business case, pricing ni build vs buy. Scripts en `Deals/Thinkific/build/` (build_tk.py tiene todo el contenido y un helper `box()` para crear slides desde cero sobre un lienzo duplicado; fix1.py = patrón para rehacer un slide). PDF del deck web en `Deals/Thinkific/Thinkific + Yuno_Oct26.pdf`. Ojo: el conector de Drive SÍ pudo compartir con la service account esta vez (share_file, writer); la service account no puede copiar archivos (cuota 0).

**Hilo paralelo de Magdalena con Beverley Ferguson (beverley@thinkific.com), "Re: Sharing the Thinkific Business Case", Gmail thread 1a0f96f9f0bed1d8:** Magda mandó el BC el 17-sep; Beverley respondió el 1-oct (quiere compartir el deck con colegas, pregunta si abre con cualquier email @thinkific; globalización no este año, retomar a inicios de 2027). Magda contestó el mismo día reencuadrando a US + Canadá (routing + subs recovery, nombró Skool, Hotmart y Whop) y pidió call. 6-oct-2026: German entra al hilo con el reply de CC handoff (borrador creado, reply a 1a0f96f9f0bed1d8, To Beverley, CC Magda): empezar por US y Canadá donde está la mayoría del revenue, global cuando Thinkific decida, Whop y Hotmart como referencia (sin Skool), propone jue 8-oct 9 AM o vie 9-oct 1 PM PT. Versión final (más corta, sin mención de SF) dice que German conoció a Tauqeer y a otros del equipo en Stripe Sessions en abril. Rol de Beverley sin verificar.

## project_thrivecart
*ThriveCart research brief — checkout platform building payments in-house; embed-Yuno angle not merchant sale*  
*type: project · last updated 2026-07-27*

ThriveCart (thrivecart.com): bring-your-own-processor checkout/cart + LMS platform for digital products/courses. 75k+ businesses, $8B+ cumulative GMV, 70M+ txns. HQ Austin TX, founded 2016 by Josh Bartlett; CEO Ismael Wrixen (ex-FE International, since May 2024); $35M raise 2023 (LTV SaaS Growth Fund).

**Not a normal merchant — it's a Yuno-adjacent checkout LAYER.** Merchants connect their OWN processor (Stripe Connect+, PayPal, Authorize.net [maintenance-mode], plus first-party ThrivePay Installments). Hard lock-in: "cannot integrate processors we don't natively support." One processor per product, NO cross-PSP failover/routing/orchestration. No third-party orchestrator (no Spreedly/Primer). Coverage capped by each merchant's single Stripe-account country.

**Lead angle = platform/EMBEDDED partnership, NOT a merchant acquiring deal.** Catalyst: ThriveCart is building payments in-house RIGHT NOW — open Head of Engineering–Payments + PM–Payments roles ("integrating third-party providers"), custom Stripe Connect+ (Apr 2025), ThrivePay card-linked BNPL, PCI DSS Level 1 (Jul 2026), subscription-pricing pivot (Jul 2026), StealthSeminar + VBOUT acquisitions. Pitch: embed Yuno as orchestration engine instead of building routing/failover/local-APM coverage for 75k merchants. Fallback: white-label "payment optimization" (routing +7% / recovery 50%) feature for their merchant base. Personas: Head of Eng–Payments / PM–Payments (once named), Ismael Wrixen (CEO, strategy), Josh Bartlett (founder/product). Scored 🔴 High (17). Never say they "lack" methods (broad Stripe/PayPal set) — angle is single-account coverage cap + no orchestration. Brief: data/research/thrivecart-2026-07-27.md. Related: [[reference_yuno_positioning]] [[reference_buyer_personas]] [[feedback_no_false_info_disclaimer]]

**Deck status (shipped 2026-07-27):** thrivecart deck has HD vector logo (`public/merchants/thrivecart.svg`, real wordmark) + full Slide 2 "What we know about your business" (`src/data/business-overviews.json` → `thrivecart`). Revenue OMITTED on purpose (private, one-time pricing, no credible figure); $2B labeled as GMV not revenue. Cover: registered in `DARK_LOGO_MERCHANTS` so the navy wordmark forces white on the black cover.

## project-tiendamia
*Tiendamia (marketplace cross-border LatAm, HQ Miami; AR/BR/CR/EC/PE/UY) — intro call vie 25-sep-2026 9:00 COT agendada por Pedro Ferrer (SDR) con Salvador Boidi; Yuno ya les hizo demo en feb-2024 (Cybersource Uruguay)*  
*type: project · last updated 2026-09-24*

Tiendamia.com: marketplace cross-border (productos de Amazon/Walmart/eBay entregados en LatAm), HQ Miami, opera en Argentina, Brasil, Costa Rica, Ecuador, Perú y Uruguay; inversor Cartesian Capital. Web tiendamia.com, LinkedIn linkedin.com/company/tiendamia.

**Historia con Yuno:** en feb-2024 hubo canal compartido #tiendamia-yuno (Lucas Glustman, Santiago Palenque; del lado de ellos German Cañón e Hilario Villamar) y una demo de Rafael Kawase con flujo Cybersource para Uruguay (cuenta sandbox "Tiendamia Demo"). No hay cuenta en el CRM de Gong ni hilos de Gmail antes de sep-2026.

**Estado 24-sep-2026:** Pedro Ferrer (SDR) agendó "Tiendamia <> Yuno" el viernes 25-sep 9:00 a 9:30 COT (meet.google.com/sig-mexh-yja) con Salvador Boidi (rol sin confirmar); German aceptó y se bloqueó el 24-sep 4 a 5 pm para prepararla. No está en el Deal Status GTM; fila lista (Status "Discovery") en Lists & ICP/Pipeline Sync/manual_adds/.

**How to apply:** antes de la call, preguntar a Pedro qué disparó el inbound y confirmar el rol de Salvador; en la call, qué cambió desde 2024 (stack actual por país, quién procesa Uruguay/Argentina/Perú, pain de cross-border y FX). Relacionado: [[project-linea-directa]], [[project-sf-relocation-fall-2026]].

## project-unicef-colombia
*UNICEF Colombia, inbound; demos 21 y 29-sep hechas, follow-up 29-sep ENVIADO sin respuesta; propuesta Google Slides armada 2-oct, pricing v6 del 6-oct (platform $7K + 0.28%/0.24% por transacción aprobada, corte 100K trx + suscripciones $0.015 por trx enviada con las primeras 50K gratis = $14,500/mes; facturación mínima $10K), SIN enviar; stack Credibanco iPay, Redeban, Wompi, Nuvei, débitos batch 3 bancos*  
*type: project · last updated 2026-10-06*

UNICEF Colombia (oficina país, agencia ONU). Demo inbound vía Chili Piper el 21-sep-2026 4:00pm COT, 32 min, en español. Yuno: Susana Awad (SDR, organiza) + German. Alejandro Albarracín en cc. Transcript guardado en Deals/UNICEF (follow-up) y brief en data/research/unicef-colombia-2026-09-21.md.

**Asistentes UNICEF (confirmado en llamada):** Idual Kerguelen (ikerguelen@unicef.org) = encargado de Business Intelligence dentro de Fundraising y dueño técnico del CRM Salesforce, llegó a Yuno porque su jefe le compartió material de Yuno y le interesó el uso de IA para optimizar procesos transaccionales. Leidy Guio (lguio@unicef.org) = proceso transaccional de venta no presente a donantes, hizo las dos preguntas duras (reintentos y migración de tarjetas a la bóveda). Sebastian Garavito (sgaravito@unicef.org) = Business Data & Analytics intern, pidió "orquestación". Harold Martinez = dio la tasa de aceptación (~85%), NO está en la invitación y no tenemos su correo. Sede: calle 72 con 11, Bogotá, híbridos.

**Números dichos por ellos:** ~150.000 donantes recurrentes en Colombia (>1M en LatAm), 92% donan cada mes, ticket promedio COP 50.000, tasa de aceptación ~85%, 80% de la base se envía a cobro la primera semana del mes. NO recuperan cartera: donación no cobrada en el mes = donación perdida. Presupuesto 2027 contempla trabajar fuerte en IA.

**Stack real (dicho por Idual, reemplaza lo inferido del sitio):** Credibanco = procesador principal, producto iPay (tarjetas crédito/débito, tokeniza, API + batch mensual desde el CRM). Redeban para parte de las tarjetas. Wompi en modelo agregador Y gateway (Nequi, Daviplata, Botón Bancolombia, PSE solo donación única, recurrencia con tarjeta). Bre-B en testeo (llave/QR, sin recurrencia). Nuvei = PSP nuevo vía alianza global UNICEF, integrado vía middleware, empezará con tarjeta y traerá Google Pay (avanzado) y Apple Pay (en desarrollo) para el canal digital. Débitos a cuenta de ahorro/corriente en batch (archivos txt/CSB por banco) con Bancolombia, Davivienda y Banco de Bogotá, muy manual. CRM Salesforce con módulo transaccional. Agencia digital externa hace las integraciones del canal digital. PCI DSS vía proveedor. Canales: digital, alianza Grupo Aval (telemercadeo al entregar tarjeta), face to face (200 personas, El Dorado). Firstoken y Mercado Pago (del research web) NO fueron mencionados en la llamada; no afirmarlos.

**Dolores:** orquestación manual (rechazo en un gateway se reenvía a otro a mano), reintentos manuales clasificando causales de rechazo, débito a cuenta muy manual, comisiones por rechazos y prenotificación. NO buscan métodos de pago nuevos ("nadie en el sector tiene tantos"); buscan eficiencia, tasa de efectividad y menor costo transaccional con IA. No planean más procesadores aparte de Nuvei.

**Qué se les dijo:** Yuno como capa encima de lo que tienen (conexiones directas a Nequi/Daviplata sin pasar por Wompi), motor de suscripciones con planes de montos abiertos donde Yuno dispara el cobro mensual sin intervención del donante, reintentos configurables por ellos (hard decline no se reintenta, falla de procesador sí), migración de tarjetas a la bóveda recomendada pero no obligatoria. Reconciliación se mencionó como producto: OJO, es roadmap (ver [[published-stats-only]]).

**Estado 22-sep-2026:** borrador de follow-up en Gmail (asunto "UNICEF Colombia & Yuno | Gracias por el espacio y opciones para la demo", a los tres, cc Susana y Alejandro) con 4 horarios COT de 45 min: jue 24 3pm, vie 25 10am, mar 29 3pm, mié 30 2pm. Evitados jue/vie 11am (tienen reunión) y lun 28 (viaje a SF, ver [[project-sf-relocation-fall-2026]]). El borrador promete sumar un SE a la demo; hay que conseguirlo. Copia en Deals/UNICEF/unicef-followup-email-2026-09-22.md.

**Why:** el ángulo es recuperar cobros recurrentes fallidos en la capa de pagos (routing/failover sobre sus procesadores, reintentos inteligentes, subs engine) y quitar lo manual, no vender métodos de pago.

**How to apply:** demo enfocada en orquestación sobre stack existente + subscriptions + IA en tasa de efectividad; pendiente técnico con SE: consumir tokens de Credibanco iPay vs migrar a bóveda Yuno, y cómo cubrir débitos a cuenta batch. Compra vía procesos ONU (RFP/LTA, PCI SAQ D + AoC). Sensibilidad a fee por ticket bajo. Ver [[feedback-no-false-info-disclaimer]].

**Deal Status GTM (22-sep):** UNICEF Colombia NO está aún en el tracker; German recibió la fila lista para pegar (Company "UNICEF Colombia", Website donaciones.unicef.org.co, LinkedIn linkedin.com/company/unicefcolombia, Industry "Nonprofit & Fundraising", Status "Discovery"). No se pudo escribir porque el gdrive MCP está muerto (ver [[project_gsheets_mcp]]). Verificar en la próxima sesión que la fila exista.

**Estado 29-sep-2026:** "Dashboard Demo Unicef x Yuno" HECHA (3:00 pm COT; por Yuno German, Susana, Joaquin Mann). Transcript de Google Meet vacío; revisar Gong. Follow-up escrito por German en BORRADOR Gmail (reply en el hilo "UNICEF + Yuno", a los tres, cc Susana y Alejandro), copia en Deals/UNICEF/unicef-followup-email-2026-09-29.md. ⚠️ El saludo dice "Iván" y el contacto es Idual: confirmar antes de enviar. Lo que el correo compromete: integración vía API (el middleware lo deciden ellos); **ACH sin smart routing ni fallbacks** (corrección de lo dicho en la demo); migración de cuentas ahorro/corriente ya prenotificadas con datos en claro; suscripciones independientes sin plan (monto y frecuencia propios) si no usan el checkout de Yuno; monto abierto en el checkout de Yuno SIN confirmar. Pendientes de German: tiempos de respuesta de ACH y propuesta de integración + precios para revisar la semana del 5-oct. PCI: dijeron que su entorno digital es PCI compliant vía un proveedor tercero, no certificación propia; tokens de Credibanco guardados en el CRM.

**Dashboard Demo 29-sep-2026 (resumen automático guardado en Deals/UNICEF/unicef-call-summary-2026-09-29.md, con notas de corrección):** Salesforce es el motor de cobro y hub de datos, conectado vía un middleware que provee UNICEF Global (no APIs directas de Salesforce); modelo preferido = empujar datos a Yuno vía API, el middleware puede quedarse intacto. ACH: Leidy descarga, rutea y reimporta a mano los archivos planos todos los días. Nuvei aún no está live (mandato global). Mandatos: optimizar costo, subir aprobación, orquestación y suscripciones a futuro. Se mostró: marketplace, routing rules, monitors (ejemplo Credibanco bajo 85% en 10 tx/30 min), smart routing, insights, Payments Concierge y agente Nova (contacta donantes con cobro rechazado y ofrece link de pago). Retries estándar dichos: ~7 min, 5 h, 47 h, 5 días, 12 días. ⚠️ En la demo se dijo "Wingo +12% aprobación" (no publicada, ver [[published-stats-only]]) y que el ruteo ACH entre bancos era posible (corregido en el follow-up: NO). Abiertos de German: soporte de prenotificación ACH (auth de valor cero), tiempos de respuesta ACH, montos libres en suscripciones (consultar al product lead de subs), propuesta de integración y precios.

**Estado 24-sep-2026:** FUP del 22-sep ENVIADO; Sebastián confirmó el martes 29-sep 3:00 pm COT y Susana agendó "Dashboard Demo Unicef x Yuno" (29-sep 3:00 a 3:45 pm COT, Idual y Leidy aceptaron). Sigue pendiente conseguir el SE. Fila para el Deal Status GTM (Status "Demo") lista en Lists & ICP/Pipeline Sync/manual_adds/; la hoja aún no está compartida con la service account.

**Estado 2-oct-2026, PROPUESTA ARMADA (sin enviar):** el follow-up del 29-sep SÍ se envió (22:51 UTC, salió con "Iván" en el saludo) y nadie de UNICEF ha respondido. La demo del 29-sep no está en Gong (solo la llamada del 21-sep); en Gong/Salesforce hay dos cuentas "UNICEF" duplicadas (001Ps00001nvKRuIAM y 001Ps00001t6o8PIAQ). Deck "Propuesta - UNICEF Colombia + Yuno", Slides `111EW1tmbSYPYtxLYRa5Mf_yx0Cn-BxA4wT2FAZeGpe0` (raíz de My Drive, 20 slides, copia de la de Línea Directa sin el slide de Perú, compartido con la service account). Inputs de German: todo en USD, 150,000 trx/mes, ticket promedio $15 ($2.25M de volumen aprobado), platform fee $10,000, tarifa variable en % "como en la propuesta de Yango", motor de suscripciones $0.02 por transacción enviada. Slide de pricing (15): 0.25% de $0 a $1.5M y 0.20% por encima = $5,250; suscripciones 150,000 × $0.02 = $3,000; platform $10,000; **total $18,250/mes, $219,000/año, $0.12 all-in por trx, 0.81% del volumen**; sin compromiso mínimo; opcionales sin precio (conciliación, monitores, network tokens, Nova). ⚠️ Supuestos míos por confirmar: las tasas y el corte son los de Yango final (German no dio los números); las 150K pasan todas por el motor con un envío cada una (si los reintentos cuentan, sube); "sin fee de setup" y "3 años" heredados. ⚠️ Policy: suscripciones a $0.02 por trx no coincide con la copia del 21-sep (0.7%/0.3% del TPV, "not sellable"); confirmar con Finance; falta Salesforce. Registro en Deals/UNICEF/unicef-proposal-2026-10-02.md y scripts en Deals/UNICEF/build/ (model.py = aritmética). Siguen abiertos: mix por método, proceso de compra y decisor, middleware, tiempos y prenotificación ACH, monto abierto en checkout. Ver [[project_linea_directa]], [[project_yango]], [[yuno-pricing-policy]].

**2-oct-2026 (tarde), pricing v2:** German corrigió que las tarifas y los tramos van sobre TRANSACCIONES APROBADAS, no sobre volumen aprobado. Slide 15 reescrito con build/fix2_tx_tiers.py: "Fee de plataforma más un porcentaje por transacción aprobada"; 0.25% del valor de cada transacción aprobada de 0 a 100,000 trx y 0.20% por encima; mismos totales ($18,250/mes, $219,000/año, $0.12 all-in por transacción aprobada). ⚠️ Interpretación por confirmar: sigue siendo un % (no un fijo en dólares por trx) y el corte de 100,000 trx sale de $1.5M de Yango ÷ $15.

**2-oct-2026 (tarde), pricing v3 (reemplazada por v4):** German dio las tasas: **0.28% de 0 a 100,000 trx aprobadas y 0.24% por encima** (ya no son las de Yango). Tramo 1 $4,200 + tramo 2 $1,800 = $6,000; suscripciones $3,000; platform $10,000; **total $19,000/mes, $228,000/año, $0.13 all-in por transacción aprobada**. Aplicado con build/fix3_rates.py. Sigue por confirmar solo el corte de 100,000 trx y el supuesto de 150K envíos por el motor de suscripciones.

**2-oct-2026 (tarde), pricing v4 (reemplazada por v5):** German: en suscripciones se regalan las primeras 50,000 transacciones. Slide 15: 0.28% (0 a 100,000 trx aprobadas) / 0.24% (más de 100,000) = $6,000; suscripciones (150,000 − 50,000) × $0.02 = $2,000; platform $10,000; **total $18,000/mes, $216,000/año, $0.12 all-in por transacción aprobada**. Aplicado con build/fix4_subs_free.py. ⚠️ Por confirmar: que las 50K gratis sean por mes (así quedó en el slide), el corte de 100,000 trx y el supuesto de 150K envíos por el motor.

**4-oct-2026, pricing v5 (reemplazada por v6):** German pidió facturación mínima mensual de **$14,000 = $10,000 de plataforma + $4,000 en transacciones**. $4,000 ÷ ($15 × 0.28%) = **95,238 transacciones aprobadas al mes** ("cerca de 95,000" en el slide; 80,645 si contara también la tarifa de suscripciones, no se usó). Total estimado sigue en $18,000/mes (mínimo cubierto). Aplicado con build/fix5_min_billing.py: filas nuevas "Facturación mínima mensual $14,000 / mes" (panel medio) y "Facturación mínima: $14,000 (≈95,000 trx) | Cubierta" (panel derecho). Policy: fee fija + MMG aditivo = estructura preferida; cobro mensual del mínimo = zona amarilla.

**6-oct-2026, pricing v6 = VIGENTE en el deck:** German pidió bajar el fee de plataforma a **$7,000**, la facturación mínima mensual a **$10,000** y cobrar el motor de suscripciones a **$0.015** por transacción enviada. Slide 15: tramos 0.28% / 0.24% iguales ($6,000); suscripciones (150,000 − 50,000) × $0.015 = $1,500; plataforma $7,000; **total $14,500/mes, $174,000/año, $0.10 all-in por transacción aprobada (0.64% del volumen)**. Mínimo $10,000 = $7,000 de plataforma + $3,000 en transacciones = 71,429 trx aprobadas ("cerca de 71,000" en el slide). Aplicado con build/fix6_v6_lower_fees.py (solo texto, mismos IDs que v5; se niega a escribir si el slide no coincide con v5). ⚠️ Supuesto: el mínimo de $10K es el total facturado (plataforma incluida), como en v5. ⚠️ $7K de plataforma está por debajo del list de V3 ($10K): validar zona de precio antes de enviar. QA: "$0.015" ya no es token prohibido; el footer "Contrato a 3 años" sigue 33 pt off-page desde la plantilla de Línea Directa (no se tocó).

## universal-psp-and-naming
*Universal Destinations (theme parks) deck — internal name \"Universal\" only, single bank-acquirer PSP topology (Chase or BofA) with disclaimer*  
*type: project · last updated 2026-05-26*

Universal Destinations & Experiences (theme park / experiences division of Comcast NBCUniversal) is the merchant behind slug `universal-destinations`.

Two rules for any deliverable referencing this account:

1. **Internal name**: always just "Universal". Never write "Universal Music Group" (different company) and avoid "Universal Destinations & Experiences" in customer-facing chrome. The merchant `name` field already reads "Universal".

2. **PSP topology**: Universal runs acquiring through a single PSP that is bank acquiring. Default to **Chase Paymentech** (or Bank of America Merchant Services) as the single-PSP chip on slide 3, and always pair with the disclaimer "No public information on providers so assumptions were made" per [[no-false-info-disclaimer]].

**Why:** German confirmed verbally on 2026-05-26 that the merchant uses bank-direct acquiring and is not Universal Music Group, so the deck shouldn't imply multi-PSP complexity or carry the wrong corporate parent.

**How to apply:** When building or refreshing the Universal deck, hardcode the single bank-acquirer PSP via `slide-overrides.json > universal-destinations > slide3.psps` and `pspsDisclaimer`. If Supabase later gets refreshed PSP research, the override should still win until German says otherwise. Per [[feedback_psps_chips_scope]] the chip must stay a gateway/PSP/MoR — Chase Paymentech qualifies; "Chase Bank" alone does not.

## project_us_qsr_retail_batch
*US QSR/fast-casual/retail batch (45 brands) added to TCL + enriched 2026-07-27; mostly weak Yuno fit (US-only)*  
*type: project · last updated 2026-07-27*

45 US QSR/fast-casual/retail brands added to German's Final List (TCL) skeleton + fully enriched 2026-07-27 (part of the 558-row master block). Core finding: **US-only merchants are structurally weak Yuno ICP** (single country, mature in-house payments, closed wallets) and scored 2-9/18 Tier 3. **Global/multi-market QSR are the real fits.**

Tier-1 fits: **Burger King (16, RBI group play + McDonald's/Arcos Dorados precedent), KFC (14, Yum!, Byte in-house US only), Papa John's (14, Checkout.com UK-only + ex-Domino's CDTO Kevin Vasconi), Starbucks (14, siloed Chase/Adyen/Alipay + China JV), Pizza Hut (13, ⭐ PE carve-out to LongRange Capital closing ~Q3 2026 = greenfield window).** Tier-2: Wingstop (12, own MyWingstop stack), Popeyes/Tim Hortons (11, RBI).

Incumbent-orchestrator flags (NOT greenfield): **Wendy's = ACI Omni-Commerce; Dunkin'/Sonic/Jimmy John's/Arby's = Fiserv Carat (Inspire Brands); Ding = Gr4vy; Avianca/Gol = CellPoint.** Kroger just signed EXCLUSIVE Worldpay (Oct 2025). H-E-B (7) = only US retailer with real fit (US+Mexico, OXXO/SPEI + own H-E-B Debit fintech). Weakest: Publix/Dollar General/Dollar Tree (2), most grocers/dollar stores (3).

Recurring theme for QSR pitch: lead with McDonald's/Arcos Dorados (Yuno across 21 LATAM countries, +4.7% approval) as proof; frame as international acquiring/local-APM layer BEHIND their in-house stack (Byte/ACI/Carat), not rip-and-replace. Master paste block: data/tcl-COMBINED-master-558-paste-at-A695.tsv. Related: [[project_thrivecart]] [[project_tango_live]] [[reference_yuno_positioning]] [[feedback_no_false_info_disclaimer]]

## project-vix
*ViX (TelevisaUnivision) deal history — decision-maker structure, Recurly conflict, Mastercard POP interest, Yuno<>Stripe co-sell prep*  
*type: project · last updated 2026-08-26*

ViX has had a live, multi-touch relationship with Yuno for months (in-person meeting Oct 1, 2025 in NY; dinner outreach Jul 20, 2026; Yuno<>Stripe prep call Aug 24, 2026 — see [[project_meeting_brief_skill]] and `data/research/vix-meeting-brief-2026-08-24.md` / `data/research/vix-2026-08-24.md`). This memory adds firsthand deal context from German that isn't in the desk-research briefs.

**Decision-maker structure:** ViX's actual payments decision does NOT get made at the TAM (LatAm) level. **Lorena Velarde** (Head of Payments, TAM) is the warm, confirmed contact — strong personal relationship (German has shared meals with her, she was even considered for a Head of Product hire at Yuno) — but she is not the final decision-maker. Her boss, based in **Miami**, a CFO-type exec, is the one who actually approves deals. German does not recall this person's name (referred to informally, name/nickname forgotten). Do not conflate this Miami exec with TelevisaUnivision CFO Juan Pablo Newman from the research brief — that link is unconfirmed, treat as a separate unnamed person until verified.

**Why the deal stalled:** ViX had pre-approved Yuno to be their payments orchestrator, but it kept getting deprioritized — most recently paused because the World Cup was the priority. Conversations are restarting now (as of Aug 2026) since the acute need for local/alternative payment methods (especially tokenizable ones) hasn't gone away — cards-only isn't sufficient for ViX, and they have no local acquiring identity in most non-US markets.

**Recurly conflict (historical, resolved):** ViX runs all subscription integrations through **Recurly**, a subscriptions-only orchestrator (not a payments orchestrator). The original plan was for Yuno to be ViX's payments provider working alongside Recurly. Recurly refused to allow an orchestrator on their platform and pushed back hard — this created friction and at one point made Yuno look like it had over-promised to ViX. It's in the past now; the personal relationship with Lorena stayed positive throughout. Yuno is NOT pitching a subscription engine to ViX — Recurly keeps that role; the Yuno ask is specifically the payment-methods/orchestration layer.

**Mastercard POP interest:** ViX has shown real interest in Mastercard's POP product — detects a subscription decline due to insufficient funds, checks if the same card was approved elsewhere, and can push through approval at ViX based on that signal, lifting subscription approval rates significantly. Worth exploring how Yuno could package/charge for this, but keep it a minor talking point, not a lead angle.

**How to apply:** When prepping anything for the Yuno<>Stripe ViX co-sell motion, lead with the local-APM/tokenization gap and the Recurly-adjacent orchestration angle (not a subscription-engine pitch). Route any "who really decides" framing to the Miami CFO-type exec, not Lorena — she's the champion/relationship, not the economic buyer. Do not name Juan Pablo Newman as that Miami exec without independent confirmation.

## project_voodoo_psp
*Voodoo (mobile games + BeReal) payment stack and Yuno angle*  
*type: project · last updated 2026-06-22*

Voodoo SAS (Paris, €623M rev 2024, owns BeReal): consumer revenue is Apple/Google IAP. Net-new payments surface = **Stripe web checkout, live June 2025, US iOS only, Stripe as Merchant of Record** (escapes Apple's 30%). No orchestrator, no second PSP. Yuno angle = orchestrate that external web-checkout rail across geos (India 8% traffic, BeReal #1 in Japan → UPI/PayPay/Konbini gaps) + add failover on single-PSP concentration. ICP list tags it NO OPP (IAP-dominated); the Stripe move reopens it on the web-billing rail. Brief: data/research/voodoo-2026-06-22.md.

## warby-parker-eben
*Warby Parker / Eben Timko (Product Manager); blocker original \"solo US y Canadá\"; re-engagement jul-2026 sin respuesta; 3er toque sep-2026 con ángulo growth (tiendas + Intelligent Eyewear)*  
*type: project · last updated 2026-09-14*

Contacto: **Eben Timko**, Product Manager, eben.timko@warbyparker.com. Hilo Gmail "Let's meet! | Stripe Tour New York".

Historia:
- Sep 2025: outreach por Stripe Tour NY. Eben respondió abierto a hablar pero con blocker: "Warby only operates in the US and Canada, so at the moment I'm not sure we'd need Yuno's services". Canceló la reunión en booth 102 (otras prioridades). Sin respuesta desde el 30-sep-2025.
- 22-jul-2026: German re-engancha (el blocker US-only ya no aplica). 27-jul-2026: Alejandro (pre-sales) suma voz: en US/Canadá el valor es aprobación de tarjeta + stack centralizado. Sin respuesta.
- 25-ago-2026: German reenvió el hilo a Magdalena.
- 14-sep-2026: borrador del 3er toque (cc Alejandro), ángulo growth con datos Q2 2026.

Datos verificados (8-K Q2 2026): revenue +9.8% a $235.5M; 352 tiendas (15 netas en Q2); meta 50 aperturas 2026; guidance FY2026 $959-976M (+10-12%); active customers 2.71M (+4.1%); revenue por cliente $336 (+6.6%); invirtiendo para el lanzamiento de "Intelligent Eyewear". Shop-in-shops en Target desde 2025.

Canal digital (10-K FY2025, tabla de revenue por canal): e-commerce $226.7M (2023, 33.8% del total) → $233.6M (2024, 30.3%) → $240.9M (2025, 27.6%), crece ~3% anual mientras retail crece 17-21%. Q2 2026 (call, Dave Gilboa): e-commerce $58.7M (-0.3% por el cierre de Home Try-On a fines de 2025, ~25% del revenue); sin HTO, las órdenes online de lentes y contactos crecieron low double digits; retail +13.6%. Ángulo usado: 1% del revenue online ≈ $2.4M/año, todo card-not-present.

No repetir el argumento US-only ni los logos (ya usados dos veces). PSP de Warby no verificado: no afirmar.

## project-yango
*Yango deal — driver-recharge payments across LatAm, Aug 19 2026 discovery call findings, key contacts, and BC data gaps*  
*type: project · last updated 2026-10-02*

Yango (ride-hailing super-app, Dubai HQ) is evaluating vendors to consolidate driver top-up/recharge collection across Colombia, Peru, Bolivia and Venezuela. HQ wants a decision by end of August 2026. Yuno's pitch: complement Cobre (which already handles real-time driver payout/dispersal in Colombia via Fast Pay, 120k+ drivers), not replace it — Yuno sits on the collection/recharge side only.

**Key contacts:** Javier Patiño (jpatino@yango-team.com, main contact since May 2026), Alejandro Sanabria Cárdenas (pcardenas@yango-team.com, data gatekeeper), Luis Montealegre (lmontealegre@yango-team.com, ex-Rappi ops). Yuno side: German Tatis (BDM), Justo Benetti (CRO, justo@y.uno), Maria Jose Pineda (Sr KAM, maria.pineda@y.uno). HQ names surfaced but unconfirmed roles: "Konstantin" (reportedly owns CO/PE/BO/Africa payments decision) and "Sergey Solyakov" (linkedin.com/in/sergey-solyakov/, HQ Dubai) — next meeting is being scheduled with both. 2026-08-31: German drafted a LinkedIn DM (English) to Sergey directly, referencing the Colombia-team conversations and offering to share the existing proposal with him; sent status not yet confirmed back to Claude.

**Aug 19, 2026 discovery call — real findings (source: live notes taken during the call, not the auto-transcript which came out corrupted):**
- **Card authorization root cause identified:** card binding (vinculación) success rate is only 68–70%, because Yango's acquirers have no local presence — banks flag the small verification charges as foreign transactions and block them. Once a card is successfully bound, the success rate on subsequent transactions jumps to 90–92%. The binding step, not steady-state processing, is the real bottleneck. Yuno's proposed fix: zero-cost pre-authorization + smart routing (multi-provider fallback) to raise binding success directly.
- Colombia average recharge ticket: ~$3.20 USD. Ticket size is low across all 4 markets, which is why Yango wants a variable-only pricing model (fixed per-transaction fees hurt disproportionately at this ticket size).
- Current processor stack: PayU (cards, historically majority) + Unlimit (cards, described as stable now, not "underperforming" like the May 2026 read) + Inswitch also live for pay-ins acquiring ("funcionamiento estable"). Unlimit has a global master agreement, making it Yango's default when entering new markets. Pricing: Unlimit 2.4% flat (variable only); Inswitch 2.4% + $150 COP fixed fee.
- Yango explicitly wants everything consolidated onto one platform, partly to minimize taxable movements under Colombia's 4x1000 tax.
- Scope may expand beyond the original 4 LatAm markets: Yango wants a payments solution that works at a global level, not just LatAm — worth positioning the proposal at that scale going forward.

**Payout confirmed in Peru:** Monnet (spelling to confirm with German — deck spells it "Monnet", German referred to it as "Monet") is the confirmed payout processor in Peru, per German directly (2026-08-20). This resolves what was previously flagged as an unverified name on the deck's "current landscape" slide — it's real, not a placeholder. Colombia (Cobre) and Peru (Monnet) are now the two confirmed payout markets; Bolivia and Venezuela remain open/unconfirmed.

**Business case gaps still open after the call** (approval rate now partially answered by the binding-rate finding above, but not broken out per country): monthly recharge volume (count + $) per country, real driver counts (not proxies) per country, ticket size for Peru/Bolivia/Venezuela, payment methods actually live today per country (vs. what's just market-popular), PayRetailers migration status, and whether the binding-rate numbers vary by country/processor.

**Follow-up sent:** recap + data-request email sent by German on 2026-08-19 to Javier/Alejandro/Luis (cc Justo, Maria, jpatino@yango.com) — went out just before the card-binding finding surfaced, so that finding is NOT in the sent email. Use it in the next presentation/proposal instead. Next step after data comes back: meeting with Konstantin and Sergey at HQ.

Deck ("Yango + Yuno_Aug 26", Slides id 1XPdfoKEGoT-s7-XcIoewxbOWnMidO9JfcMTUgYvclak) had 3 leftover Eventbrite template artifacts flagged for fixing (slide 6 eyebrow, slide 19 KAM/source line, slide 29 GoFundMe case QA note) — confirm these were fixed before the next send.

**Update 2026-08-20:** ⚠️ discrepancia importante: el 18-ago se reconciló localmente un modelo financiero completo (+$29M/año sobre ~$332M de volumen y ~162,000 conductores CO+PE+BO, con Bolivia revisado a ~27,000 conductores y Venezuela modelado en ~3,100 conductores/$9.4M). Verificado directamente contra el deck real enviado a Yango el 20-ago: ninguna de esas cifras aparece en el deck. El deck fue reconstruido hacia alcance global (~20 países, formato tabla de métodos/proveedores por país) sin TAM en dólares. Decidir si se reintegra el modelo financiero o si el cambio fue intencional antes de citar esas cifras con Yango. Los 3 artefactos Eventbrite ya no aparecen (deck reestructurado), fixes de card-binding y payouts sí confirmados en el deck vivo. También sin resolver: transición PayRetailers→Inswitch (mayo tenía PayRetailers en recargas, agosto ya no lo menciona y aparece Inswitch, fecha de transición desconocida), reunión con Konstantin/Sergey pedida el 19-ago sin confirmar agendada, y la call del "equipo cashless" del 20-ago sin registro de qué se habló. El transcript de la call 19-ago está confirmado corrupto (1m27s de texto ilegible), Gong grabó completo pero sin acceso desde las herramientas disponibles.

**Deck vigente (desde 4-sep):** "Business Case Yango + Yuno", Slides `1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw` (36 slides, secciones 01 Today / 02 Proposed Model / 03 Why Yuno / 04 inDrive / 05 Business Case), enviado el 4-sep vía Papermark **deck.y.uno/yangobclatam** (Javier lo abrió 16-sep). Base del BC (slide 31, data de Yango ago-2026): $87.7M/año en recargas cashless, 38.9M tx, ticket blended $2.25 (CO $3.50 / PE $3.20 / BO $1.50 / VE $2.80); caso rail de tarjeta $3.21M/año ($2.33M aceptación + $0.88M MDR), $10.7M identificados en total.

**22-sep-2026, PROPUESTA DE PRICING (Javier escribió que en el BC no vio los costos de Yuno):** construida como sección nueva **06 · Proposal** (divider + 2 slides, más línea en la agenda). Modelo: **platform fee $10,000/mes + % del volumen de recargas aprobadas por tramos, un solo stream para CO+PE+BO+VE: 0.60% (0 a $2.5M/mes) / 0.50% ($2.5M a $5M) / 0.45% (>$5M)**; declines y verificaciones de tarjeta (binding) no se cobran; add-ons network tokens $0.05/$0.01, reconciliation y Nova pending; 3 años. Alejandro pidió tarifa VARIABLE (Gong 19-ago: el ticket bajo hace que los fijos pesen), por eso es % y no $/tx. A volumen completo ($7.3M/mes, 3.24M tx): tx fee $37,873 + $10,000 = **$47,873/mes, $574,471/año, $0.015 por recarga, 0.66% del volumen**; el caso del rail de tarjeta es 5.6x el costo. Rollout acumulado: Colombia $21,578 → +Perú $31,128 → +Bolivia $44,129 → +Venezuela $47,873. Archivos: `Deals/Yango/yango-pricing-proposal-2026-09-22.md` (modelo, zonas de policy, alternativas, respuesta a Javier), `claude-design-prompt-proposal-section-2026-09-22.md`, `build/yango_pricing_model.py`, `build/yango_proposal_slides.py` (Slides API vía service account; `--html` para previews, `--pid` para insertar en el deck real), previews `yango-proposal-slide35/36/37.png`. ⚠️ NO enviada: falta Salesforce y resolver zonas: pay-ins bajo list (Doc min $0.01 → amarillo; Cheatsheet dice min $0.08 → rojo; Yango es strategic merchant ≥1.2M tx/mes), platform fee $10K probablemente amarillo (V4 list $16K), network tokens rojo, "verificación no cobrada" pendiente en policy. ⚠️ La service account NO tiene cuota de Drive (no puede crear decks propios): para insertar las slides German debe compartir el deck real con `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` como Editor, o correr el prompt en Claude Design. Tras insertar, re-subir el PDF a Papermark (mismo slug).

**24-sep-2026, REVISIÓN PRE-ENVÍO (`Deals/Yango/yango-proposal-review-2026-09-24.md`):** el deck vivo (39 slides, editado 22-sep 23:26) YA NO tiene el modelo % de arriba: la sección 06 · Proposal quedó como **tranches por transacción pooled en los 4 países: $0.023 (0 a 500K tx/mes) / $0.020 / $0.017 / $0.014 / $0.011 (2M a 3M) / $0.008 (>3M) + platform fee $10,000/mes + "Monthly minimum billing: $25,000"**; add-ons network tokens $0.05/$0.01 y **reconciliation $2,000/mes por 500K tx + $0.0003/tx** (Nova ya no aparece). A volumen pleno: **$59,930/mes, $719,165/año, $0.018/recarga, 0.82% del volumen**; CO+PE $33,414; caso rail tarjeta 4.5x. Slide 37 asigna por share de tx: CO $10,194 / PE $10,377 / BO $33,865 / VE $5,494. Aritmética verificada completa (sección LIVE de `build/yango_pricing_model.py`). **Pendientes antes de compartir:** 🔴 reconciliation $0.0003/tx está 10x bajo el mínimo de policy ($1,500 + $0.0085/tx; pack 3M = $30K/mes), volver a "Pending review" o cotizar en policy; 🔴 mínimo $25K ambiguo (¿incluye platform fee?), contradice "variable" de Alejandro y "platform fee o mínimo, no ambos" de Sean, y con solo Colombia la factura calculada es $22,526 → se cobra $25K mientras la slide 37 dice "Colombia $10,194" (decidir: quitarlo o aclararlo + rampa en slide 37); 🟡 caja oculta "$ 75.56" en slides 34/36/37 (borrar); 🟡 QA visual de 6 tranches en slide 36 sin hacer (SA sin acceso; export PDF del conector falla por 27 MB); 🟡 slide 31 dice datos "July 2026" vs "August 2026" en 30/36. Zonas: tranche 6 $0.008 < min $0.01 🔴, platform $10K 🟡, tokens 🔴, recon 🔴, 3 años 🟡; Salesforce antes de cotizar. Script listo `build/apply_review_fixes_2026-09-24.py` (dry-run; --delete-stray / --min keep|drop / --ramp / --source / --recon pending / --thumbs) cuando German comparta el deck con la SA. Tras corregir: re-subir PDF a Papermark (slug yangobclatam) y responder a Javier (texto actualizado al modelo per-tx en el review). Gong: sin interacciones con Yango después del 1-sep.

**24-sep-2026 (tarde), PROPUESTA FINAL en el deck (German la ajustó tras el review):** tarifa VARIABLE como pidió Alejandro: **% del volumen de recargas aprobadas pooled 4 países: 0.25% ($0 a $1.5M/mes) / 0.20% ($1.5M a $3M) / 0.15% ($3M a $4.5M) / 0.10% (>$4.5M) + platform fee $12,000/mes; sin mínimo mensual, sin fijo por tx, declines y verificaciones gratis; add-ons tokens $0.05/$0.01 y reconciliation $2,000 + $0.0003/tx (se mantuvo)**. A volumen pleno **$23,805/mes, $285,660/año, $0.0073/recarga, 0.33% del volumen**; rampa CO $16,609 → +PE $19,839 → +BO $22,973 → +VE $23,805; caso rail 11.2x. Aritmética verificada completa (sección FINAL de build/yango_pricing_model.py). ⚠️ Policy: todas las bandas equivalen a $0.0023 a $0.0056/tx, bajo el mínimo $0.01 del Doc (rojo, CFO+CRO); recon sigue 10x bajo mínimo; residuo "$ 75.56" en slides 34/36/37 y "July 2026" en slide 31 siguen sin corregir. **Correo a Javier/Alejo/Luis (cc Justo, Majo, jpatino@yango.com) en BORRADOR de Gmail** (draft r7820567250410170120, versión corta y sobria; German pidió correo menos vendedor y SIN links, él agrega el link/adjunto) como reply al hilo "Yango + Yuno: resumen de la llamada y próximos pasos" (mensaje del 4-sep), con link deck.y.uno/yangobclatam: German debe re-subir el PDF a Papermark antes de enviar.

**2-oct-2026 (dicho por German + Slack):** la propuesta se ENVIÓ por WhatsApp (no por el correo en borrador). Javier dijo el 30-sep que la revisaron y "hace mucho sentido"; el equipo de Colombia la presentó a HQ el 1-oct y German espera feedback. Piotr Sierpinski (EMEA, su jefa Maria es GM EMEA) habla en paralelo con el HQ ruso de Yango y pidió copia de la propuesta el 30-sep (confirmar que se la pasaron). Sigue pendiente: oportunidad en Salesforce (el Pipeline Brief del 2-oct la marca "not entered") y aprobación de pricing en zona roja.

## yuno-sales-deck-skill
*Local skill .claude/skills/yuno-sales-deck (Samuel Vieira's package, 2026-09-17) adapted to German; builds research-backed .pptx sales decks with pptxgenjs + deck_qa.py; where it lives, what was changed, pending QA fixes on Anthropic/Higgsfield decks*  
*type: project · last updated 2026-09-17*

The `yuno-sales-deck` skill lives at `.claude/skills/yuno-sales-deck/` (SKILL.md, 7 references, scripts/yuno_deck.js + deck_qa.py + slides_thumbs.py; pptxgenjs installed under scripts/node_modules, gitignored). Origin: Samuel Vieira (BDM, samuel@y.uno) shared it by Slack DM on 2026-09-17 (Drive folder id 1GjWDpxCt1TZRp4pyCnrujXshk3cAhBxU). It merges German's outside-in three-lever business cases (xAI, Anthropic, Higgsfield, Flair) with Samuel's Roblox decks (10-K-driven BC, C-suite product session, first-meeting deck). Five deck types A-E, evidence ledger with [F]/[E]/[Y]/[A] tags, conservative/base/upside, floor, return net of Yuno cost, ends on The Ask.

Adaptations made for German: operator is German (not Samuel); local paths (`Deals/<Merchant>/`, `Industry/<Vertical>/<Merchant>/`, memory dir, deck app research cache in yuno-sales-pitch-maker); German's tool stack (Gong, Slack, Gmail, Drive, Calendar, Glean, context7 for docs.y.uno, /research, /business-case); house rules folded into references + deck_qa.py (no dashes, "no small feat" banned, facts only, USD only, published stats 7%/30% only, standard pricing $50K free then $0.05/tx, PayPal is an APM not a PSP, client-reported metrics win, RBP structure); brand tokens Yuno Blue 3E4FE0 / Unity Black 282A30 / Titillium Web (Samuel's navy+Arial preset via `YUNO_DECK_THEME=navy`, font via `YUNO_DECK_FONT`); dark cover with the `yuno | merchant` lockup from local logo assets.

**Why:** German asked to turn Samuel's package into a skill of his own; the team standard for decks should be one pipeline, with German's rules enforced automatically instead of by review.

**How to apply:** invoke `/yuno-sales-deck <merchant> [A|B|C|D|E]`. No LibreOffice on this Mac, so the visual QA is deck_qa geometry warnings plus Google Slides thumbnails (`scripts/slides_thumbs.py <presentationId> <outdir>`, Slides token scope is presentations only, no Drive upload). Pending from Samuel's QA of decks already sent: Anthropic deck has four different totals ($1.25B, $2.5B, $105M/mo, $238M/mo), India MAU above global MAU, a Spanish working note on the Lever 1 table slide and a Mastercard Agent Pay paragraph in "Why move now"; Higgsfield deck says 18 markets in some places and 20 in others, has "$6.1M MAU" with a dollar sign and "Adyen's own routing" text in the Yuno column of the architecture slide. See [[project_higgsfield]], [[feedback_no_false_info_disclaimer]], [[feedback_published_stats_only]], [[reference_yuno_pricing]].

## project-yuno-vs-stripe-subscriptions
*Ongoing initiative to build a side-by-side Yuno Subscriptions vs Stripe Billing comparison; German will keep feeding info and send a not-yet-ready presentation*  
*type: project · last updated 2026-09-02*

Goal: build a side-by-side comparison proving Yuno's subscriptions product beats Stripe Billing. Started 2026-09-02. German is feeding this incrementally (docs, notes, and eventually a presentation draft that wasn't ready yet as of 2026-09-02) — treat this as a living brief, re-read before building final deliverables.

**Why:** GTM/competitive positioning material, likely for prospect conversations where Stripe Billing is the incumbent or alternative being evaluated. Follows [[feedback_no_false_info_disclaimer]] — comparison must be scrupulously factual, no spin/fabrication, and must not hide genuine Stripe strengths.

**How to apply:** Before building the final comparison deck/doc, re-fetch both docs sources if >2-4 weeks old (both products ship fast) and merge with whatever German has sent since. Use [[reference_yuno_positioning]] for Yuno's core narrative (orchestration across PSPs/methods/antifraud/KYC).

## Yuno Subscriptions — key facts (source: docs.y.uno/docs/payment-features/subscriptions)
- Statuses: CREATED → ACTIVE/TRIALING → PAUSED/PAST_DUE → COMPLETED/CANCELED/ERROR. Clean 8-state model.
- PAST_DUE is opt-in per account (must ask Yuno to enable); otherwise subscription just keeps retrying while staying ACTIVE.
- Payment methods confirmed: CARD, PAYPAL_ENROLLMENT, PIX_AUTOMATIC (Brazil).
- **Pix Automático is a real differentiator**: rail-native recurring debit with mandatory D-4 scheduling (`billing_cycles.scheduling_date` = next_at minus 4 days), fixed retry ladder (max 3 attempts, D/D+1/D+2/D+3, 7-day window), only weekly/monthly/quarterly/half-yearly/yearly (no daily — BCB rail restriction). Requires enablement via Yuno reps.
- One-call flow: send a `subscription` block on Create Payment → charge + subscription created atomically; if charge declines, no subscription is created ("nothing starts billing if the payment fails"). No `incomplete`/zombie-subscription state like Stripe. Limitation: one-call route only supports `frequency.type: MONTH`, no trial_period/plan_id/metadata/retries config on that route — must use two-call (enroll then Create Subscription) for full feature set.
- Trial periods: reduced amount for N cycles, partial or total discount, `TRIALING` status.
- Webhooks: subscription.active, payment.purchase (per-cycle), subscription.cycle_executed, subscription.past_due, subscription.trialing.
- Billing model as documented: single amount (FIXED or VARIABLE) + frequency — did NOT find evidence of a Product/Price catalog, tiered/per-seat/usage-based pricing, multi-item subscriptions, proration, coupons, or a self-serve customer portal equivalent. **Open gap — verify with German whether these exist but are undocumented, or genuinely absent** — this is Stripe Billing's strongest area, don't concede it without checking.
- **CONFIRMED headline differentiator (German, 2026-09-02): Yuno Subscriptions runs on Yuno's multi-PSP orchestration layer.** One subscriptions engine can route recurring charges through Stripe, Adyen, Braintree, etc. under the same umbrella. Adding a new processor to an existing subscriptions setup is just a connection — Yuno already built and maintains that PSP integration, so the merchant does zero extra integration work.
- **CONFIRMED pricing (German, 2026-09-02): first $50,000/month in processing volume is free, then $0.05 per transaction — on top of (in addition to) the underlying payment-processing cost.**

## Stripe Billing — key facts (source: docs.stripe.com/billing)
- Statuses: trialing, active, incomplete, incomplete_expired, past_due, canceled, unpaid, paused. Three linked objects per charge: Subscription + Invoice + PaymentIntent, each with their own status — more granular but more complex to integrate against.
- New subscriptions default to `incomplete` and give the customer 23 hours to pay before `incomplete_expired` — genuine "zombie subscription" cleanup burden Yuno's one-call flow avoids.
- Pricing models: flat-rate, per-seat, tiered (graduated/volume), usage-based — all via Product + Price objects, multi-currency. Rich and flexible; multi-item subscriptions supported.
- Usage-based billing: being migrated to **Metronome** (acquired by Stripe) for new integrations — real-time metering, prepaid credits/credit burndown, enterprise contracts/ramps, dimensional/composite pricing. Old "Billing Meters" API still supported for existing integrations only.
- Trial Offers (new, preview API as of 2026-03-25): free or paid trials, item-level trials, upgrade trials, configurable billing-cycle-anchor behavior on trial end (now vs unchanged, controls proration).
- Smart Retries: AI-driven retry timing (device/time-of-day signals), default 8 tries within 2 weeks, configurable 1wk-2mo window, or fully custom retry schedule (up to 3 retries). Stripe markets ~41% average recovery of failed invoices (from search result, not yet confirmed on an official stats page — verify before quoting in a deck). Won't retry on hard decline codes (stolen card, lost card, etc.) or India-issued cards. Also retries local payment methods (ACH, ACSS, BECS AU/NZ, BACS, SEPA) — note: **no Pix, no LatAm APMs in this recurring-retry list**, all US/EU/Oceania-centric.
- Automations: no-code visual workflow builder (triggers + filters + actions) for dunning emails, collections notifications, cancellation confirmations, uncollectible write-offs — materially more mature/self-service than what's documented for Yuno so far.
- Customer Portal: full self-service (update payment method/plan, cancel immediate or end-of-cycle, view/pay invoices, cancellation-deflection coupons), localized in 38+ languages, supports 30+ payment methods. **No equivalent found yet in Yuno docs — flag as open gap**, same caveat as above (verify before conceding).
- **Single-processor lock-in (confirmed by German, 2026-09-02): Stripe Billing's subscriptions engine is wired directly and only to Stripe.** Stripe does technically allow connecting other processors at the payments level, but Stripe does not build or maintain those integrations — the merchant has to build and maintain each additional processor integration themselves, with no native multi-PSP orchestration inside Billing itself. This is the mirror image of the Yuno fact above and is the core of the headline differentiator.
- **CONFIRMED pricing (German, 2026-09-02): $0.07 per transaction, on top of payment processing — 2 cents higher than Yuno's $0.05.**

## Early comparison angles (refine as more info arrives)
**Likely Yuno wins:**
0. **HEADLINE ANGLE — multi-PSP orchestration, confirmed.** Yuno Subscriptions: one engine, connect Stripe/Adyen/Braintree/etc. under one umbrella, zero extra merchant integration work per processor. Stripe Billing: hard-wired to Stripe only; adding another processor means the merchant builds and maintains that integration themselves, with no native cross-processor orchestration for recurring billing. Reframe as: Stripe Billing = single-rail subscriptions bolted onto a single-PSP setup; Yuno Subscriptions = subscriptions as one layer of a full orchestration stack (routing, failover, cost optimization across processors all apply to recurring charges too, not just one-time payments).
0.5 **HEADLINE ANGLE — pricing, confirmed.** Yuno: first $50K/month processing free, then $0.05/transaction. Stripe: $0.07/transaction, no stated free tier. Both fees are on top of underlying payment processing. Cheaper AND a free volume tier Stripe doesn't offer.
1. LatAm-native recurring rails (Pix Automático today, presumably more local APMs later) vs Stripe's recurring retry support being US/EU/Oceania only.
2. Atomic one-call subscription+payment creation, no incomplete/zombie states to clean up.
3. Simpler status model (8 states vs Stripe's cross-product Subscription×Invoice×PaymentIntent matrix) — faster integration, fewer edge cases to handle.

**Stripe currently ahead (be honest about these, don't hide them):**
1. Pricing model flexibility — tiered/per-seat/usage-based/multi-item vs Yuno's single amount+frequency model (pending verification).
2. Self-service customer portal — nothing found yet on Yuno's side.
3. No-code dunning/automations builder — more mature merchant-facing tooling.
4. Smart Retries is AI-adaptive vs Yuno's fixed retry ladders (at least for Pix) — though Yuno's predictability could be reframed as a strength (transparency/compliance) depending on audience.

## Next steps
- Wait for German's additional info drops and the presentation draft.
- Before finalizing: verify (a) whether Yuno has pricing-model flexibility / customer portal / proration not yet documented, (b) Stripe's 41% recovery stat source. (Multi-PSP orchestration angle is now confirmed, no longer open.)

## project-zoom-drew-curhan
*Drew Curhan, Payments Lead en Zoom (basado en Santa Barbara, CA); 3 emails fríos feb-mar 2026 sin respuesta; 4-oct-2026 German pasa a ángulo networking casual desde SF*  
*type: project · last updated 2026-10-04*

Drew Curhan (drew.curhan@zoom.us, linkedin.com/in/drew-curhan-0337b8a) es Payments Lead en Zoom: procesamiento, vendors y flujos transaccionales. Vive en Santa Barbara, CA, no en San Francisco. Ex Director eCommerce Ops en Topps y UrbanDaddy, Tufts.

German le mandó 3 correos fríos: 24-feb-2026 "Leaders in Payments", 26-feb FUP, 2-mar "How about success?" (cc Alejandro). Cero respuestas. El 4-oct-2026 German cambió a un mensaje de LinkedIn sin agenda comercial: recién mudado a SF, ampliar network, café presencial o virtual.

**Why:** ya fue pitcheado tres veces sin responder; el ángulo que queda es relación, no producto.

**How to apply:** nada de pitch de Yuno ni name dropping con Drew hasta que responda. Si acepta café, ofrecer virtual o cuando él suba a SF (Santa Barbara está a 5 horas). Ver [[project-sf-relocation-fall-2026]] y [[feedback-linkedin-shorter]].
