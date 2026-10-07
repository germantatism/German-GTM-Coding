import os, re, shutil, zipfile, json, datetime
from pathlib import Path

REPO = Path("/Users/germantatis/Desktop/GTMCoding")
MEM  = Path("/Users/germantatis/.claude/projects/-Users-germantatis-Desktop-GTMCoding/memory")
OUT  = REPO / "Claude App Export"
TODAY = "2026-10-06"

if OUT.exists(): shutil.rmtree(OUT)
(OUT/"skills").mkdir(parents=True); (OUT/"skills-zips").mkdir()

# ---------- helpers ----------
def split_fm(text):
    if text.startswith("---"):
        parts = text.split("\n---", 1)
        if len(parts) == 2:
            fm = parts[0].lstrip("-").strip("\n")
            body = parts[1].lstrip("\n")
            return fm, body
    return "", text

def fm_get(fm, key):
    m = re.search(rf"^{key}:\s*(.*?)$(?:\n(?:\s{{2,}}|\t).*)*", fm, re.M)
    if not m: return None
    block = m.group(0)
    first = block.split("\n")[0].split(":",1)[1].strip()
    if first in (">-", ">", "|", "|-"):
        lines = [l.strip() for l in block.split("\n")[1:]]
        return " ".join(lines).strip()
    return first.strip('"').strip("'")

def kebab(s):
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", "-", s)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# ---------- 1. commands -> skills ----------
NOTE = ("> **Ported from Claude Code on " + TODAY + ".** In Claude Code this ran as a slash command. "
        "Wherever the text says `$ARGUMENTS`, read it as whatever the user typed when invoking this skill "
        "(company name, merchant, URL, etc.). Paths under `/Users/germantatis/Desktop/GTMCoding/` refer to "
        "German's local GTMCoding repo (GitHub: germantatism/German-GTM-Coding); if the Claude app has no "
        "access to that folder, ask German for the file or skip that step.\n\n")

LOCAL_DEP_RE = re.compile(r"tools/gsuite|scripts/|python3?|\.py\b|node |npx|supabase|\.env\.local|sa\.json|yuno-sales-pitch-maker")
manifest = []
for cmd in sorted((REPO/".claude/commands").glob("*.md")):
    raw = cmd.read_text(encoding="utf-8")
    fm, body = split_fm(raw)
    name = kebab(cmd.stem)
    if name == "stripesessionsresearch": name = "stripe-sessions-research"
    desc = fm_get(fm, "description") if fm else None
    if not desc:
        h1 = next((l for l in body.splitlines() if l.startswith("# ")), f"# {name}")
        desc = re.sub(r"^#\s*(/\S+\s*[—\-–:]\s*)?", "", h1).strip()
    hint = fm_get(fm, "argument-hint") if fm else None
    if hint: desc = f"{desc}. Input: {hint}"
    desc = desc.replace('"', "'")
    skill_dir = OUT/"skills"/name; skill_dir.mkdir()
    content = f'---\nname: {name}\ndescription: "{desc}"\n---\n\n{NOTE}{body}'
    (skill_dir/"SKILL.md").write_text(content, encoding="utf-8")
    manifest.append(dict(name=name, source=f".claude/commands/{cmd.name}", desc=desc,
                         local_dep=bool(LOCAL_DEP_RE.search(raw)), lines=len(body.splitlines())))

# ---------- 2. real skills (copy, no node_modules) ----------
def copy_skill(src, name, source_label):
    dst = OUT/"skills"/name
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("node_modules", "__pycache__", "*.pyc", ".DS_Store"))
    raw = (dst/"SKILL.md").read_text(encoding="utf-8")
    fm, body = split_fm(raw)
    desc = (fm_get(fm,"description") or "").replace('"',"'")
    (dst/"SKILL.md").write_text(f'---\nname: {name}\ndescription: "{desc}"\n---\n\n{NOTE}{body}', encoding="utf-8")
    manifest.append(dict(name=name, source=source_label, desc=desc,
                         local_dep=bool(LOCAL_DEP_RE.search(raw)), lines=len(body.splitlines())))
copy_skill(REPO/".claude/skills/yuno-sales-deck", "yuno-sales-deck", ".claude/skills/yuno-sales-deck/ (full folder, node_modules removed; run `npm install` in scripts/)")
copy_skill(REPO/"Milo/intro-reply", "intro-reply", "Milo/intro-reply/ (Yuno Agents cloud routine skill)")

# ---------- 3. zip each skill ----------
for d in sorted((OUT/"skills").iterdir()):
    zp = OUT/"skills-zips"/f"{d.name}.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(d.rglob("*")):
            if f.is_file(): z.write(f, f"{d.name}/{f.relative_to(d)}")

# ---------- 4. memory consolidation ----------
mems = []
for f in sorted(MEM.glob("*.md")):
    if f.name == "MEMORY.md": continue
    raw = f.read_text(encoding="utf-8")
    fm, body = split_fm(raw)
    typ = fm_get(fm, "type") or f.stem.split("_")[0]
    mems.append(dict(file=f.name, name=fm_get(fm,"name") or f.stem, desc=fm_get(fm,"description") or "",
                     type=typ, body=body.strip(), mtime=datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")))
order = ["user","feedback","reference","project"]
titles = {"user":"Who German is","feedback":"Standing rules (how German wants Claude to work)",
          "reference":"Reference material (positioning, pricing, personas, tools)","project":"Accounts, deals and ongoing work"}
lines = [f"# German Tatis · Full Claude memory export", "",
         f"Exported {TODAY} from Claude Code (project GTMCoding). {len(mems)} memories: " +
         ", ".join(f"{sum(1 for m in mems if m['type']==t)} {t}" for t in order) + ".",
         "", "Each entry keeps its original slug (useful when a memory links to another with `[[slug]]`), its one-line description and the full body. Dates inside entries are absolute. Everything here was true when written; verify anything time-sensitive before acting on it.", "",
         "## Index", ""]
for t in order:
    lines.append(f"### {titles[t]}")
    for m in [m for m in mems if m["type"]==t]:
        lines.append(f"- **{m['name']}** · {m['desc']}")
    lines.append("")
for t in order:
    lines += [f"---", "", f"# {titles[t]}", ""]
    for m in [m for m in mems if m["type"]==t]:
        lines += [f"## {m['name']}", f"*{m['desc']}*  ", f"*type: {m['type']} · last updated {m['mtime']}*", "", m["body"], ""]
(OUT/"MEMORY_FULL.md").write_text("\n".join(lines), encoding="utf-8")
shutil.copy(MEM/"MEMORY.md", OUT/"MEMORY_INDEX.md")

# ---------- 5. project instructions (user + feedback) ----------
pi = ["# Project instructions for German Tatis (Yuno GTM)", "",
      f"Distilled {TODAY} from German's Claude Code memory: his profile plus every standing rule he has given. Paste into the Claude app Project's custom instructions, or upload as project knowledge if it exceeds the limit. Full context lives in MEMORY_FULL.md.", ""]
for t in ["user","feedback"]:
    pi += [f"## {titles[t]}", ""]
    for m in [m for m in mems if m["type"]==t]:
        pi += [f"### {m['desc'] or m['name']}", m["body"], ""]
(OUT/"PROJECT_INSTRUCTIONS.md").write_text("\n".join(pi), encoding="utf-8")

json.dump(manifest, open(OUT/"skills-manifest.json","w"), indent=2, ensure_ascii=False)
print(f"skills: {len(manifest)}  memories: {len(mems)}")
print(f"MEMORY_FULL.md: {len(lines)} lines / {os.path.getsize(OUT/'MEMORY_FULL.md')//1024} KB")
print(f"PROJECT_INSTRUCTIONS.md: {len(pi)} lines / {os.path.getsize(OUT/'PROJECT_INSTRUCTIONS.md')//1024} KB")
for m in manifest: print(f"  {'[local-dep] ' if m['local_dep'] else '            '}{m['name']:28s} {m['lines']:4d} lines  {m['desc'][:70]}")
