# SETUP · Connectors, MCP servers, plugins, settings and local tooling

Snapshot of everything German's Claude Code environment relies on, as of 2026-10-06. No secrets are included; only where they live.

## 1. claude.ai connectors (the ones skills assume exist)

| Connector | Used for | Notes |
|---|---|---|
| Gmail | Reading threads, drafts, replies. Claude works inside German's Gmail by default | Rule: never `update_draft` on a reply (detaches the thread); use `create_draft` + `replyToMessageId` |
| Google Calendar | Finding meetings for briefs, scheduling | `meetingbrief`, `meeting-prep` |
| Google Drive | Reading/creating Docs, Sheets, PDFs; saving research | Large Sheets: download as xlsx and parse locally |
| Google Sheets | Lists, pipeline, deliverables (German wants lists as Sheets, never Claude Docs) | House format: header navy #10284A, Roboto 10 white, thin borders, freeze B2, no gridlines |
| Slack | Reading channels/threads, #salesops-legal for NDAs (English, header + thread) | |
| Gong | `ask_account`, `ask_deal`, `generate_brief` for call history | |
| Claude Docs | Living docs (briefs, plans) | |
| Yuno Docs (`https://docs.y.uno/mcp`) | Yuno API documentation search | Also added to Claude Code at user scope on 2026-10-06 |
| Atlassian, Excalidraw | Configured but need re-authorization | Not used for GTM work |

Skills already synced into the app from Anthropic's catalog (seen in Claude Code as `anthropic-skills:*`): `account-plan`, `business-case-calculator`, `company-financial-profile`, `deep-research`, `docs`, `docx`, `pdf`, `pptx`, `xlsx`, `google-workspace`, `morning`, `skill-creator`, browser and computer-use skills. Nothing to import for those.

## 2. Claude Code MCP servers (user scope, `~/.claude.json`)

| Name | Type | Status |
|---|---|---|
| `yuno-docs` | HTTP → `https://docs.y.uno/mcp` | Connected. Added 2026-10-06 |
| `gdrive` | stdio → `npx -y @isaacphi/mcp-gdrive`, creds in `~/.config/mcp-gdrive` | Dead since Sep-2026; replaced by `tools/gsuite` (below) |

Plugins (Claude Code only, marketplace `yuno-plugins` = `git@github.com:yuno-payments/yuno-claude-plugin.git`): `yuno` 0.0.45 and `factory` 2.11.0. They provide Glean, Datadog, GitHub, Kingdom, Metabase, SonarQube tools. GTM work uses almost none of them; Glean is the only one worth noting.

Settings (`~/.claude/settings.json`): permission mode `auto`, model `fable[1m]`, effort `xhigh`, push notifications on. No hooks configured. No CLAUDE.md files exist (all guidance lives in memory).

## 3. Local tooling on German's Mac (referenced by skills)

| Tool | Location | Purpose |
|---|---|---|
| GTMCoding repo | `~/Desktop/GTMCoding` · GitHub `germantatism/German-GTM-Coding` (branch `main`) | All deals, decks, lists, scripts. Rule: commit + push after every file change |
| `tools/gsuite/gsuite.py` | repo | Google Sheets/Slides/Docs via service account. Share the target file with the service account `gtm-claude-editor@…` first; key at `~/.config/gsuite/sa.json` |
| gcloud SDK | `~/google-cloud-sdk`, project `gtm-claude-tools-260922` | OAuth consent screen never finished; ADC blocked, so the service account is the working path |
| Deck tool (`yuno-sales-pitch-maker/`) | git submodule in repo; deploy from `main` (`master` is a protected decoy) | Web decks at `decks.internal-tools.y.uno` (Neverland, VPN). Railway `deck.yuno.tools` is stale since ~8-Sep-2026. Supabase service-role key in `yuno-sales-pitch-maker/.env.local` (never ask for it). Supabase host was down (NXDOMAIN) from 30-Sep-2026 |
| `yuno-sales-deck` skill | `.claude/skills/yuno-sales-deck/` | pptx via pptxgenjs (`npm install` in `scripts/`), QA via `scripts/deck_qa.py` |
| Business-case builders | `scripts/build_*_bc.py`, `scripts/generate_*_docx.py`, `scripts/md_to_gdoc_html.py`, `scripts/save_research_to_gdrive.py`, `scripts/tal_db.py` | Excel BCs, docx briefs, Drive uploads, TAL database |
| Pipeline Sync | Google Apps Script, TCL `Final List` → Deal Status GTM every 15 min | Operated through the `pipeline-sync` skill |
| Headshot tool | `tools/swap_shirt.py` | Needs an image API key (pending) |

## 4. Yuno Agents platform (`ai.agents.y.uno`)

Agents German built or uses: **Lucky** (BD agent: MEDDIC + account plan from transcripts), **Eve** (SF events agent; bridge = Google Sheet "SF Events Feed · Eve"), **Milo** (hourly intro-reply routine Mon–Fri 8–18 COT; skill in `Milo/intro-reply/`, included in this export). Admins can see Public agents; transfer ownership in Slack `#yuno-agents` with the Agent ID.

## 5. Key Google Sheets and Docs referenced in memory

- Money20/20 LV 2026 × TCL match: Sheet `1R0GJ0h4vLTi4CrLhwvoklBtxnRry0zmD0IMxZWkiiSo`
- Airlines targeted list: Sheet `1EsmeI6bw…` (two tabs: 37 global airlines, 43 US/Canada)
- RFP training guide: Google Doc "Payments & Yuno: Guía de Entrenamiento"
- SF trip budget sheet (28-Sep → 4-Nov-2026), regenerate with `build_budget.py`
- TCL_v2: 695 companies, 36 columns (TCL agent build)

Full detail on each is in `MEMORY_FULL.md`.

## 6. Memory location (Claude Code)

`~/.claude/projects/-Users-germantatis-Desktop-GTMCoding/memory/` · 151 files + `MEMORY.md` index. Format: one fact per file with frontmatter (`name`, `description`, `type` = user | feedback | project | reference). The consolidated copy is `MEMORY_FULL.md` in this folder.
