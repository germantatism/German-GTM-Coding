# Claude App Export · German Tatis (Yuno GTM)

Exported 2026-10-06 from Claude Code (VS Code extension, project `GTMCoding`). Everything German built or configured in Claude Code, packaged so it can be rebuilt in the Claude desktop / web app.

## What is in this folder

| Path | What it is | Use it for |
|---|---|---|
| `skills-zips/*.zip` (25) | One zip per skill, each containing `<name>/SKILL.md` (+ references/scripts where they exist) | Upload to the Claude app as Skills |
| `skills/` | Same skills, unzipped, for reading or editing | Browse before uploading |
| `skills-manifest.json` | Name, source file, description and local-dependency flag per skill | Checklist while importing |
| `PROJECT_INSTRUCTIONS.md` | German's profile plus every standing rule he has given Claude (35 feedback memories) | Paste into a Claude Project's custom instructions |
| `MEMORY_FULL.md` | All 151 memories, grouped by type, full text, with index | Upload as Project knowledge so the app knows everything that has happened |
| `MEMORY_INDEX.md` | The one-line-per-memory index Claude Code loads each session | Quick orientation |
| `SETUP.md` | Connectors, MCP servers, plugins, settings and local tooling German uses | Reconnect the same data sources in the app |

## How to rebuild it in the Claude app

1. **Create a Project** (suggested name: "German · Yuno GTM").
2. **Custom instructions**: paste the contents of `PROJECT_INSTRUCTIONS.md`. If the field rejects the length, paste the "Who German is" section plus the rules you use most, and upload the whole file as knowledge instead.
3. **Project knowledge**: upload `MEMORY_FULL.md` (and optionally `SETUP.md`). This is the "full memory" of every account, deal, rule and tool.
4. **Skills**: in the Claude app go to Settings → Capabilities → Skills and upload each zip from `skills-zips/`. The zip layout (`<name>/SKILL.md`) is the format the app expects. Upload the ones you use daily first (see priority list below).
5. **Connectors**: enable the same connectors listed in `SETUP.md` (Gmail, Google Calendar, Google Drive, Google Sheets, Slack, Gong, Claude Docs, Yuno Docs). Skills assume these exist.
6. **Memory**: the app's own memory starts empty. The first few conversations, point Claude at `MEMORY_FULL.md` and tell it to treat it as prior memory.

## Skills: import priority

**Daily outreach (no local dependencies, port 1:1)**
- `research`, `email1`, `email2`, `email-bizcase-teaser`, `email-successcase`, `lk-opener`, `coldcall`, `cadence-builder`, `negative-response`, `industrysnapshot`, `signals`, `newaccounts`, `prioritizeaccounts`, `business-case`

**Meetings and accounts**
- `meeting-prep`, `meetingbrief`, `profile`, `stripe-sessions-research`, `prioritize`

**Decks and deliverables**
- `yuno-sales-deck` (pptx; needs Node + `npm install` in `scripts/`, and Python for `deck_qa.py`), `slide-builder` (Google Slides), `mbr-builder`, `builddeck` (web decks on deck tool)

**Operations / automation**
- `pipeline-sync` (Apps Script TCL → Deal Status GTM), `intro-reply` (Milo routine on Yuno Agents)

## Skills with local-machine dependencies

These 10 reference files, scripts or services that live on German's Mac or in the GTMCoding repo. They still work as instructions, but some steps need the repo folder to be accessible to the app (or German to supply the file):

`stripe-sessions-research`, `builddeck`, `mbr-builder`, `meeting-prep`, `meetingbrief`, `pipeline-sync`, `prioritize`, `profile`, `slide-builder`, `yuno-sales-deck`

Typical dependencies: `tools/gsuite/gsuite.py` (Google service account), `yuno-sales-pitch-maker/` (deck tool + Supabase), `scripts/*.py` (business-case builders), Python/Node runtimes. See `SETUP.md`.

## What does not port 1:1

- **Slash-command arguments**: Claude Code passed `$ARGUMENTS`. In the app, the user's message is the argument. Each SKILL.md carries a note explaining this.
- **Auto-memory**: Claude Code saved memories to disk automatically. In the app, memory is the app's own; `MEMORY_FULL.md` is the seed.
- **Git auto-commit rule**: "always commit and push" only applies when Claude is working inside the GTMCoding repo.
- **Plugins** (`yuno`, `factory` from `yuno-payments/yuno-claude-plugin`) are Claude Code plugins and have no app equivalent; the connectors cover most of what German used from them (Glean, Datadog are not needed for GTM work).

## Source of truth

The live versions stay in the repo: `.claude/commands/*.md`, `.claude/skills/yuno-sales-deck/`, `Milo/intro-reply/`. Memory lives at `~/.claude/projects/-Users-germantatis-Desktop-GTMCoding/memory/`. Re-run `python3 tools/build_claude_app_export.py` from the repo root whenever they change; it rebuilds this whole folder (skills, zips, MEMORY_FULL.md, PROJECT_INSTRUCTIONS.md). README.md and SETUP.md are hand-written and preserved only if you re-add them, so copy them aside first.
