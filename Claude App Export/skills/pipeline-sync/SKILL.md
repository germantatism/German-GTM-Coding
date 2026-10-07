---
name: pipeline-sync
description: "/pipeline-sync — Operate, tune, and fix the Pipeline Sync (TCL → Deal Status GTM Apps Script) end to end. Input: <what you want: status | change config | fix something | restore>"
---

> **Ported from Claude Code on 2026-10-06.** In Claude Code this ran as a slash command. Wherever the text says `$ARGUMENTS`, read it as whatever the user typed when invoking this skill (company name, merchant, URL, etc.). Paths under `/Users/germantatis/Desktop/GTMCoding/` refer to German's local GTMCoding repo (GitHub: germantatism/German-GTM-Coding); if the Claude app has no access to that folder, ask German for the file or skip that step.

# Pipeline Sync — Operator

You own the Pipeline Sync for German. He tells you what he wants in plain language ("cambia el refresh a 30 min", "agrega la columna Annual Revenue", "¿por qué no viajó Comcast?", "se dañó, arréglalo") and you do everything: diagnose, edit, deploy, verify. Never send him to read the manual; you ARE the manual.

## What the system is

A Google Apps Script that copies leads from the Target Accounts sheet into the Deal Status tracker every 15 minutes, one-way, and keeps a dashboard.

| Role | File | Tab | Spreadsheet ID |
|---|---|---|---|
| Source | Target Company List GT - BDM | `Final List` | `1QY5pH4Td2sRitHpHI3Eec69sFfGdK2nuY-QMleqEnek` |
| Destination | Deal Status GTM | `Deal Status Tracker` | `1WPz1JW9zQm06SQg9ncrBM-4BH8ZKWh5O2Pn18XvKKPc` |

**The rule:** a lead travels when its `Status` is anything other than `Inactive` (empty also blocks, because `INCLUIR_STATUS_VACIO: false`). If the status changes later, the tracker row is updated in place. Identity key = `Company`, normalized (lowercased, trimmed, inner whitespace collapsed). Six columns travel, matched by header name: `Company · Website · LinkedIn URL · Industry · Comments · Status`. One-way only, never deletes, never duplicates, idempotent.

**Tabs in Deal Status GTM:** `Deal Status Tracker` (the leads; script writes only the 6 synced columns), `DASHBOARD` (rebuilt every run), `KEY` (last-run report, rebuilt every run), `_LOG` (hidden; day counters per status — deleting it resets every counter to zero).

**Owner:** Magdalena Torrealba (magdalena.torrealba@y.uno). German operates it via this skill.

## Local files (the mirror)

- `Lists & ICP/Pipeline Sync/pipeline_sync.gs` — canonical local copy of the full script. Every edit happens HERE first.
- `Lists & ICP/Pipeline Sync/PIPELINE_SYNC_HANDOFF.md` — full operating manual with the same script in the appendix. When you change a documented default (interval, columns, thresholds, blocking value), update the manual's config table AND the appendix so they never drift.
- The truly canonical copy lives in the Apps Script project bound to the source sheet. Local edits reach it via clasp push (preferred) or manual paste (fallback). Keep local and remote identical.

## Entry points in the script

| Function | When | What |
|---|---|---|
| `instalar()` | after changing `MINUTOS`, or fresh install | Full sync + recreates the time trigger |
| `actualizar()` | every 15 min automatically; run once after any other config change | The sync itself |
| `verTabs()` | diagnostics | Writes a map of every tab + headers into `KEY` |

## What to do per request type

### 1. Status / "how is it going" / "why didn't X travel"

Read the destination sheet directly with `mcp__gdrive__gsheets_read` (spreadsheet ID `1WPz1JW9zQm06SQg9ncrBM-4BH8ZKWh5O2Pn18XvKKPc`):
- `KEY` tab → last run timestamp, OK/ERROR, leads added/updated, rows skipped, and the "Rows that did not travel" table (company, reason, source row number).
- `DASHBOARD` tab → totals, deals by status, needs-attention list.

Answer from there. For a specific lead, find it in the skipped table and give the exact reason and source row. If `KEY` shows ERROR, the error message and a tab/header map are printed right there — diagnose from it using the troubleshooting table below.

### 2. Config changes

All in the `CONFIG` block at the top of `pipeline_sync.gs`. Edit locally, then deploy (see Deploy). After deploy, the function to run is `actualizar` — EXCEPT interval changes, which need `instalar` (it recreates the trigger).

| Request | Edit |
|---|---|
| Add/remove synced column | `COLUMNAS` array. Names must match source headers (case/extra spaces forgiven). Different names per side: `{ origen: 'X', destino: 'Y' }`. Mirror everything: `COLUMNAS : 'TODAS'` |
| Change refresh interval | `MINUTOS`. Only 1, 5, 10, 15, 30, 60 allowed. Then run `instalar`, not `actualizar` |
| Change what blocks a lead | `VALOR_BLOQUEADO`. One value only; several values = code change in `ejecutarSync_` at the `normalizar_(status) === bloqueado` branch |
| Let empty statuses through | `INCLUIR_STATUS_VACIO : true` — WARN German first: a large share of source rows have empty Status; this sends ALL of them in one run |
| Protect a hand-owned column | `COLUMNAS_PROTEGIDAS : ['Comments']` — only needed when a tracker column shares a name with a synced one |
| Aging thresholds | `DIAS_ATENCION` (default 21), `DIAS_ESTANCADO` (45) |
| Point at other tab/file | `ORIGEN_TAB` / `DESTINO_TAB` / IDs. NEVER set `CREAR_TAB_DESTINO: true` to work around a name mismatch — it creates a silent duplicate tab |
| Restyle | `TEMA` block; `navy` drives everything |

### 3. Code changes

Allowed, but these design decisions are NOT up for debate (each one exists because the previous approach broke silently in production):
- Columns resolved by header name at runtime, never by position (no IMPORTRANGE+VLOOKUP ever).
- Header row found by scanning first 10 rows for `Company`, never assumed at row 1.
- `SpreadsheetApp.openById()` always; `getActiveSpreadsheet()` returns null in time triggers.
- No `SpreadsheetApp.getUi().alert()` — results go to `KEY`.
- Idempotent; matched-before-insert; only writes cells that actually differ.
- Never deletes rows; never writes back to the source.

### 4. Restore from scratch

Open the SOURCE sheet → Extensions → Apps Script (creating it bound to the sheet is what makes the `Sync Yuno` menu appear) → delete default code → paste full `pipeline_sync.gs` → Cmd+S → select `instalar` in the dropdown → Run → approve permissions (Review → account → Advanced → Go to project → Allow) → read `KEY` in the destination.

## Deploy (local edit → live script)

Check for `Lists & ICP/Pipeline Sync/.clasp.json`:

**If it exists (clasp configured):**
1. `cd "Lists & ICP/Pipeline Sync" && npx -y @google/clasp pull` into its rootDir, diff the pulled code file against `pipeline_sync.gs` to detect remote drift (someone edited in the browser). If drifted, show German the diff and merge remote changes into the local canonical BEFORE applying his edit.
2. Apply the edit to `pipeline_sync.gs`, copy its content over the clasp code file, `npx -y @google/clasp push`.
3. Tell German which function to run (`actualizar` or `instalar`) — or run it with `npx -y @google/clasp run <fn>` if the project has run permissions set up.
4. Verify by reading `KEY` via gsheets_read after the run.

**If it does not exist (first time):** offer the one-time setup, then deploy as above:
1. German runs `npx -y @google/clasp login` in his terminal (opens browser, one click) and enables the Apps Script API at script.google.com/home/usersettings.
2. Ask him for the Script ID: source sheet → Extensions → Apps Script → ⚙️ Project Settings → Script ID.
3. Create `Lists & ICP/Pipeline Sync/.clasp.json`: `{"scriptId":"<ID>","rootDir":"gas"}`, then `npx -y @google/clasp pull` to fetch the real `appsscript.json` + code file into `gas/`.

**Fallback (no clasp, German declines setup):** give him the exact manual steps: open Apps Script editor → select all → paste the new `pipeline_sync.gs` → **Cmd+S (mandatory — an unsaved editor runs the old version with no error)** → select the right function in the dropdown (**this matters — the default selection silently runs something else**) → Run → read `KEY`.

## Troubleshooting table

| Symptom | Cause → Fix |
|---|---|
| Ran it, nothing happened, no error | Wrong function selected in editor dropdown → select `actualizar`/`instalar` explicitly |
| Still old behaviour | File not saved → Cmd+S, run again |
| `Rows skipped` = total rows | All source rows Inactive/empty status → expected |
| Specific lead didn't travel | `KEY` → "Rows that did not travel" has the exact reason + source row |
| `there is no tab called "X"` | Name mismatch (trailing space etc.) → `KEY` lists real names+gids; copy exact into CONFIG |
| `required column "Status" is missing` | Header truly absent → fix the sheet header, or map with `{origen, destino}` |
| Second empty tracker tab appeared | `CREAR_TAB_DESTINO` was true + name mismatch → delete empty tab, fix `DESTINO_TAB`, set back false |
| Day counters reset to 0 | `_LOG` deleted → unrecoverable, restarts from today |
| Two rows for same company | Pre-script rows or names differ beyond spacing → `KEY` lists them; merge by hand, script uses the first |
| `Another run is already in progress` | Lock from overlapping runs → wait a minute |

## Known limits (state them, don't rediscover them)

Day counters started when the script started (no earlier history). Duplicate source companies: first row wins, rest reported in `KEY`. `KEY` skipped list caps at 200 (count always exact); dashboard needs-attention caps at 40. One blocking status only. `Comments` is synced (overwritten each run) unless protected via 6.5. Quotas: ~8s per run, negligible.

## After every change

1. Keep `pipeline_sync.gs` and `PIPELINE_SYNC_HANDOFF.md` consistent (config table + appendix).
2. Commit and push the repo (standing rule).
3. If a default changed durably (interval, columns, blocking value), update the `project-pipeline-sync` memory file.
4. Confirm to German in one short paragraph: what changed, where it is live, what he should see on the next run.
