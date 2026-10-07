#!/usr/bin/env python3
"""
organize.py  -  ORGANIZE step for the consolidated AI-company prospect master (Yuno).

Input : master_merged.json  (list of rows, header first, 34 columns)
Output: master_final.json, master_final.csv, organize_log.md   (same folder unless --outdir)

What it does (in this order):
  1. Hygiene pass on every cell (trim, em/en-dash, " - " punctuation, row length).
  2. Column rules: ARR / Valuation numeric strings, Bay Area Yes/No/"", Yuno fit A/B/C/"",
     "ARR as of" date formats, HQ "City, Country".
  3. Duplicate detection by normalized company name and by website domain
     (keeps the row with more filled cells, merges the other's non-empty cells into it).
  4. Sort: ARR desc; ties -> Valuation desc (missing last) -> Company A to Z.
     Rows without ARR after, by Valuation desc (missing last) then Company A to Z.
     The bundled "AIOS, WorldEngine, BrightAI, Corgi, Thoughtful AI" row is pinned last.
  5. Rank 1..N for rows with an ARR, blank otherwise. "List status" keeps Samuel's "#n".
Every change is written to organize_log.md.  No network access.
"""
import argparse
import collections
import csv
import datetime
import json
import os
import re
from decimal import Decimal, InvalidOperation

HERE = os.path.dirname(os.path.abspath(__file__))
N_COLS = 34
BUNDLE_NAME = "AIOS, WorldEngine, BrightAI, Corgi, Thoughtful AI"
COLON_COLS = {"Stripe evidence", "Yuno status"}          # " - " -> ": " only here
NOTE_COL = "Merge notes"                                  # audit column that receives preserved facts

NUM_OK = re.compile(r"^\d+(\.\d+)?$")
DATE_OK = re.compile(r"^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}|FY\d{4}|Q[1-4] \d{4}|H[12] \d{4}|\d{4})$")
HQ_OK = re.compile(r"^[^,/()]+, [^,/()]+$")
MONTH_FIX = {"Sept": "Sep", "January": "Jan", "February": "Feb", "March": "Mar", "April": "Apr",
             "June": "Jun", "July": "Jul", "August": "Aug", "September": "Sep", "October": "Oct",
             "November": "Nov", "December": "Dec"}

# ---- explicit judgment fixes (company, column) -> (new value, note kept in Merge notes or None, reason)
DATE_FIXES = {
    ("Midjourney", "ARR as of"): ("2025", None,
        "Samuel wrote '2025-26' (estimate range); German research dates the ~$500M estimate to 2025"),
    ("Suno", "ARR as of"): ("Feb 2026", "ARR as of per Samuel: Feb-Jun 2026",
        "Samuel wrote 'Feb-Jun 2026'; the $300M annualized figure is dated Feb 2026 in German research"),
    ("Turing", "ARR as of"): ("2024", "ARR as of per Samuel: 2024-26 (no newer confirmed figure)",
        "Samuel wrote '2024-26'; Notes say the $300M ARR was cited for 2024 with no confirmed newer figure"),
    ("Uniphore", "ARR as of"): ("", "ARR date undated (tracker claim)",
        "Samuel wrote 'Undated'; no date is known, left blank"),
    ("Gamma", "ARR as of"): ("Nov 2025", None,
        "Samuel wrote 'Late 2025'; German research dates the $100M+ ARR to Nov 2025"),
    ("Photoroom", "ARR as of"): ("2024", None,
        "Samuel wrote 'End 2024'; kept the year only (Sacra 2024 estimate, stale)"),
}
# raw HQ value -> (new value, note or None)
HQ_FIXES = {
    "London / New York": ("London, UK", "HQ per Samuel: London / New York (dual), first-listed kept"),
    "New York, US / Paris": ("New York, US", "HQ per Samuel: New York, US / Paris (dual), first-listed kept"),
    "San Francisco / Bengaluru": ("San Francisco, US", "HQ per Samuel: San Francisco / Bengaluru (dual), first-listed kept"),
    "San Francisco, US (remote-first)": ("San Francisco, US", "Remote-first (Samuel)"),
    "Singapore": ("Singapore, Singapore", None),
    "Singapore, Singapore (est.)": ("Singapore, Singapore", "HQ Singapore is an estimate (Samuel)"),
    "Cambridge, MA, US": ("Cambridge, US", "Cambridge, MA"),
    "Not verified": ("", "HQ not verified (Samuel)"),
    "US (city not verified)": ("", "HQ: US, city not verified (Samuel)"),
    "US (not verified)": ("", "HQ: US, not verified (Samuel)"),
}
HQ_FLAG_ONLY = {"New Jersey, US": "state-level HQ, city not verified; kept as is"}


class Log:
    def __init__(self):
        self.changes = []        # (section, company, column, before, after, reason)
        self.notes = []          # free-text lines per section
        self.sections = collections.OrderedDict()

    def change(self, section, company, column, before, after, reason=""):
        if before == after:
            return
        self.changes.append((section, company, column, before, after, reason))

    def note(self, section, text):
        self.notes.append((section, text))


def norm_ws(v):
    return re.sub(r"\s+", " ", v.replace("\u00a0", " ")).strip()


def clean_number(v):
    s = v.strip().replace("$", "").replace(",", "").replace(" ", "")
    s = re.sub(r"(?i)[mb]n?$", "", s)  # stray unit suffixes
    if not s:
        return ""
    if not NUM_OK.match(s):
        return None
    try:
        d = Decimal(s).normalize()
    except InvalidOperation:
        return None
    return format(d, "f")


def clean_date(v):
    s = norm_ws(v)
    if not s:
        return ""
    if s.lower() in {"undated", "n/a", "na", "unknown", "-"}:
        return ""
    s = re.sub(r"^FY\s+(\d{4})$", r"FY\1", s)
    s = re.sub(r"^(Q[1-4])[- ]?(\d{4})$", r"\1 \2", s)
    s = re.sub(r"^(H[12])[- ]?(\d{4})$", r"\1 \2", s)
    for long, short in MONTH_FIX.items():
        s = re.sub(r"^%s\.? (\d{4})$" % long, r"%s \1" % short, s)
    s = re.sub(r"^([A-Z][a-z]{2})\.? (\d{4})$", r"\1 \2", s)
    m = re.match(r"^(?:Late|Early|Mid|End|Start)[- ](\d{4})$", s, re.I)
    if m:
        s = m.group(1)
    return s


def add_note(row, idx, text):
    if not text:
        return
    cur = row[idx[NOTE_COL]]
    if text in cur:
        return
    row[idx[NOTE_COL]] = (cur + " | " + text) if cur else text


def norm_name(s):
    s = s.lower().strip()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\bformerly\b.*$", "", s)
    s = re.sub(r"[^a-z0-9]+", "", s)
    s = re.sub(r"(inc|ai|labs|technologies|technology|corp|corporation|ltd|llc|hq)$", "", s)
    return s


def domain(u):
    u = u.lower().strip()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.split("/")[0]


def to_float(v):
    try:
        return float(v) if v != "" else None
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default=os.path.join(HERE, "master_merged.json"))
    ap.add_argument("--outdir", default=HERE)
    args = ap.parse_args()

    data = json.load(open(args.inp, encoding="utf-8"))
    header = [norm_ws(c) for c in data[0]]
    rows = [list(r) for r in data[1:]]
    if len(header) != N_COLS:
        raise SystemExit("header has %d columns, expected %d" % (len(header), N_COLS))
    idx = {c: i for i, c in enumerate(header)}
    log = Log()
    n_in = len(rows)

    # ------------------------------------------------------------------ 1. row length
    for r in rows:
        name = r[idx["Company"]] if len(r) > idx["Company"] else "?"
        if len(r) < N_COLS:
            log.change("Row length", name, "(row)", "%d cells" % len(r), "%d cells" % N_COLS, "padded with blanks")
            r.extend([""] * (N_COLS - len(r)))
        elif len(r) > N_COLS:
            log.change("Row length", name, "(row)", "%d cells" % len(r), "%d cells" % N_COLS,
                       "truncated, dropped: %r" % r[N_COLS:])
            del r[N_COLS:]
        for i, v in enumerate(r):
            if v is None:
                r[i] = ""
            elif not isinstance(v, str):
                r[i] = str(v)

    # ------------------------------------------------------------------ 2. whitespace + dashes
    for r in rows:
        name = r[idx["Company"]]
        for i, v in enumerate(r):
            col = header[i]
            new = norm_ws(v)
            if new != v:
                log.change("Whitespace", name, col, v, new, "trimmed / collapsed")
            v2 = new
            # em-dash -> comma
            v2 = re.sub(r"\s*\u2014\s*", ", ", v2)
            # en-dash: spaced = punctuation -> comma ; unspaced = range -> hyphen
            v2 = re.sub(r"\s+\u2013\s+", ", ", v2)
            v2 = v2.replace("\u2013", "-")
            # " - " punctuation
            if " - " in v2:
                v2 = v2.replace(" - ", ": " if col in COLON_COLS else ", ")
            v2 = re.sub(r",\s*,", ",", v2)
            if v2 != new:
                log.change("Dashes", name, col, new, v2,
                           "em/en-dash or ' - ' punctuation" + (" (-> ': ')" if col in COLON_COLS else ""))
            r[i] = v2

    # ------------------------------------------------------------------ 3. column rules
    for r in rows:
        name = r[idx["Company"]]

        for col in ("ARR ($M)", "Valuation ($B)"):
            v = r[idx[col]]
            new = clean_number(v)
            if new is None:
                log.change("Numeric", name, col, v, "", "non-numeric value cleared (kept in Merge notes)")
                add_note(r, idx, "%s raw value: %s" % (col, v))
                r[idx[col]] = ""
            elif new != v:
                log.change("Numeric", name, col, v, new, "normalized numeric string")
                r[idx[col]] = new

        v = r[idx["Bay Area"]]
        new = {"yes": "Yes", "y": "Yes", "true": "Yes", "no": "No", "n": "No", "false": "No", "": ""}.get(v.lower())
        if new is None:
            log.change("Bay Area", name, "Bay Area", v, "", "only Yes/No/blank allowed; fact kept in Merge notes")
            add_note(r, idx, "Bay Area %s (Samuel)" % v.lower())
            new = ""
        elif new != v:
            log.change("Bay Area", name, "Bay Area", v, new, "normalized")
        r[idx["Bay Area"]] = new

        v = r[idx["Yuno fit"]]
        new = v.strip().upper()
        if new not in {"A", "B", "C", ""}:
            log.change("Yuno fit", name, "Yuno fit", v, "", "only A/B/C/blank allowed; raw kept in Merge notes")
            add_note(r, idx, "Yuno fit raw value: %s" % v)
            new = ""
        elif new != v:
            log.change("Yuno fit", name, "Yuno fit", v, new, "normalized")
        r[idx["Yuno fit"]] = new

        v = r[idx["ARR as of"]]
        if (name, "ARR as of") in DATE_FIXES:
            new, note, reason = DATE_FIXES[(name, "ARR as of")]
            log.change("ARR as of", name, "ARR as of", v, new, reason)
            add_note(r, idx, note)
        else:
            new = clean_date(v)
            if new != v:
                log.change("ARR as of", name, "ARR as of", v, new, "date format normalized")
        if new and not DATE_OK.match(new):
            log.note("ARR as of", "NON-CONFORMING after pass: %s | %r" % (name, new))
        r[idx["ARR as of"]] = new

        v = r[idx["HQ"]]
        if v in HQ_FIXES:
            new, note = HQ_FIXES[v]
            log.change("HQ", name, "HQ", v, new, "City, Country format" + ("; fact kept in Merge notes" if note else ""))
            add_note(r, idx, note)
        else:
            new = v
            new = re.sub(r"\b(USA|United States|U\.S\.)$", "US", new)
            new = re.sub(r",\s*[A-Z]{2},\s*US$", ", US", new)  # City, ST, US -> City, US
            if new != v:
                log.change("HQ", name, "HQ", v, new, "City, Country format")
        if new in HQ_FLAG_ONLY:
            log.note("HQ", "FLAG %s | %r: %s" % (name, new, HQ_FLAG_ONLY[new]))
        elif new and not HQ_OK.match(new):
            log.note("HQ", "NON-CONFORMING after pass: %s | %r" % (name, new))
        r[idx["HQ"]] = new

    # ------------------------------------------------------------------ 4. duplicates
    def filled(r):
        return sum(1 for v in r if v != "")

    dup_report = []
    groups = collections.OrderedDict()
    for i, r in enumerate(rows):
        keys = {"name:" + norm_name(r[idx["Company"]])}
        if r[idx["Website"]]:
            keys.add("web:" + domain(r[idx["Website"]]))
        groups.setdefault(i, set()).update(keys)
    # union rows sharing any key
    key_to_rows = collections.defaultdict(list)
    for i, ks in groups.items():
        for k in ks:
            key_to_rows[k].append(i)
    parent = list(range(len(rows)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for k, members in key_to_rows.items():
        for m in members[1:]:
            parent[find(m)] = find(members[0])
    clusters = collections.defaultdict(list)
    for i in range(len(rows)):
        clusters[find(i)].append(i)
    drop = set()
    for members in clusters.values():
        if len(members) < 2:
            continue
        members.sort(key=lambda i: (-filled(rows[i]), i))
        keep, others = members[0], members[1:]
        kr = rows[keep]
        for o in others:
            orow = rows[o]
            merged_cols = []
            for c, i in idx.items():
                if kr[i] == "" and orow[i] != "":
                    kr[i] = orow[i]
                    merged_cols.append(c)
            add_note(kr, idx, "Merged duplicate row '%s' (%d filled cells) into this row" % (orow[idx["Company"]], filled(orow)))
            dup_report.append((kr[idx["Company"]], orow[idx["Company"]], filled(kr), filled(orow), merged_cols))
            drop.add(o)
    rows = [r for i, r in enumerate(rows) if i not in drop]

    # ------------------------------------------------------------------ 5. sort + rank
    bundle = [r for r in rows if r[idx["Company"]] == BUNDLE_NAME]
    body = [r for r in rows if r[idx["Company"]] != BUNDLE_NAME]

    def sort_key(r):
        arr = to_float(r[idx["ARR ($M)"]])
        val = to_float(r[idx["Valuation ($B)"]])
        return (0 if arr is not None else 1,
                -(arr if arr is not None else 0.0),
                0 if val is not None else 1,
                -(val if val is not None else 0.0),
                r[idx["Company"]].lower())

    body.sort(key=sort_key)
    rows = body + bundle
    old_rank = {}
    n_rank = 0
    for r in rows:
        before = r[idx["Rank"]]
        if to_float(r[idx["ARR ($M)"]]) is not None and r is not (bundle[0] if bundle else None):
            n_rank += 1
            new = str(n_rank)
        else:
            new = ""
        if before != new:
            old_rank[r[idx["Company"]]] = (before, new)
        r[idx["Rank"]] = new

    # ------------------------------------------------------------------ 6. outputs
    os.makedirs(args.outdir, exist_ok=True)
    out_json = os.path.join(args.outdir, "master_final.json")
    out_csv = os.path.join(args.outdir, "master_final.csv")
    out_log = os.path.join(args.outdir, "organize_log.md")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump([header] + rows, f, ensure_ascii=False, indent=1)
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

    # ------------------------------------------------------------------ 7. log
    with_arr = [r for r in rows if r[idx["Rank"]]]
    blanks = collections.OrderedDict((c, sum(1 for r in rows if r[idx[c]] == "")) for c in header)
    sam_rank = lambda r: (re.search(r"Samuel top 100 #(\d+)", r[idx["List status"]]) or [None, ""])[1]
    unranked_with_arr = [r for r in with_arr if not sam_rank(r)]

    L = []
    L.append("# organize_log.md")
    L.append("")
    L.append("Generated %s by organize.py from `%s`." % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), os.path.basename(args.inp)))
    L.append("")
    L.append("## Sort summary")
    L.append("")
    L.append("- Rows in: %d. Rows out: %d (duplicates merged: %d). Columns: %d." % (n_in, len(rows), len(dup_report), N_COLS))
    L.append("- Rows with ARR (ranked 1..%d): %d. Rows without ARR: %d (incl. the bundled row pinned last)." % (len(with_arr), len(with_arr), len(rows) - len(with_arr)))
    L.append("- Order: ARR ($M) desc; ties by Valuation ($B) desc (missing last), then Company A to Z. Rows without ARR follow, by Valuation desc (missing last), then Company A to Z.")
    L.append("- `%s` kept as ONE row at the very end with Rank blank (five tracker-only companies, not split)." % BUNDLE_NAME)
    L.append("- Rank re-numbered 1..N. Samuel's original rank is untouched in `List status` (\"Samuel top 100 #n\"). New Rank differs from Samuel's #n because %d rows with an ARR that Samuel did not rank (German-only rows and Samuel's not-ranked tab) are now interleaved." % len(unranked_with_arr))
    L.append("")
    L.append("### Top 15 by ARR")
    L.append("")
    L.append("| Rank | Company | ARR ($M) | ARR as of | Valuation ($B) | Samuel # |")
    L.append("|---|---|---|---|---|---|")
    for r in rows[:15]:
        L.append("| %s | %s | %s | %s | %s | %s |" % (r[idx["Rank"]], r[idx["Company"]], r[idx["ARR ($M)"]], r[idx["ARR as of"]], r[idx["Valuation ($B)"]], sam_rank(r) or ""))
    L.append("")
    L.append("### Ranked rows that Samuel did not rank (%d)" % len(unranked_with_arr))
    L.append("")
    L.append(", ".join("#%s %s (%s)" % (r[idx["Rank"]], r[idx["Company"]], r[idx["ARR ($M)"]]) for r in unranked_with_arr))
    L.append("")
    L.append("### First rows without ARR (ordered by Valuation desc)")
    L.append("")
    no_arr = [r for r in rows if not r[idx["Rank"]]]
    L.append(", ".join("%s (%s)" % (r[idx["Company"]], r[idx["Valuation ($B)"]] or "no val") for r in no_arr[:15]) + (" ..." if len(no_arr) > 15 else ""))
    L.append("")

    L.append("## Hygiene changes (%d cell edits)" % len(log.changes))
    L.append("")
    by_sec = collections.OrderedDict()
    for ch in log.changes:
        by_sec.setdefault(ch[0], []).append(ch)
    for sec in ["Row length", "Whitespace", "Numeric", "Bay Area", "Yuno fit", "ARR as of", "HQ", "Dashes"]:
        items = by_sec.get(sec, [])
        L.append("### %s (%d)" % (sec, len(items)))
        L.append("")
        if sec == "Dashes" and items:
            cnt = collections.Counter(c[2] for c in items)
            L.append("Per column: " + ", ".join("%s %d" % kv for kv in cnt.most_common()) + ".")
            L.append("")
            L.append("Rules: em-dash -> \", \"; spaced en-dash -> \", \"; unspaced en-dash inside ranges (e.g. $100-200/mo) -> hyphen; \" - \" -> \": \" in Stripe evidence and Yuno status, \", \" everywhere else (List status included; the \"Samuel top 100 #n\" tokens are unaffected).")
            L.append("")
        if not items:
            L.append("none")
            L.append("")
            continue
        L.append("| Company | Column | Before | After | Why |")
        L.append("|---|---|---|---|---|")
        for _, comp, col, b, a, why in items:
            esc = lambda s: s.replace("|", "\\|").replace("\n", " ")
            L.append("| %s | %s | %s | %s | %s |" % (esc(comp), esc(col), esc(b)[:140], esc(a)[:140], esc(why)))
        L.append("")
    sec_notes = [t for s, t in log.notes]
    L.append("### Flags (not changed)")
    L.append("")
    L.extend(["- " + t for t in sec_notes] or ["none"])
    L.append("")

    L.append("## Duplicates")
    L.append("")
    L.append("Checked by normalized company name (lowercase, parentheticals and suffixes removed) and by website domain.")
    L.append("")
    if dup_report:
        for keep, other, fk, fo, cols in dup_report:
            L.append("- Kept `%s` (%d filled) and merged `%s` (%d filled). Cells pulled in: %s" % (keep, fk, other, fo, ", ".join(cols) or "none"))
    else:
        L.append("None found (%d distinct companies)." % len(rows))
    L.append("")

    L.append("## Blank counts per column (final)")
    L.append("")
    L.append("| Column | Blank | Filled |")
    L.append("|---|---|---|")
    for c, b in blanks.items():
        L.append("| %s | %d | %d |" % (c, b, len(rows) - b))
    L.append("")

    L.append("## Validation")
    L.append("")
    L.append("- All rows have %d cells: %s" % (N_COLS, all(len(r) == N_COLS for r in rows)))
    L.append("- ARR ($M) numeric or blank: %s" % all(r[idx["ARR ($M)"]] == "" or NUM_OK.match(r[idx["ARR ($M)"]]) for r in rows))
    L.append("- Valuation ($B) numeric or blank: %s" % all(r[idx["Valuation ($B)"]] == "" or NUM_OK.match(r[idx["Valuation ($B)"]]) for r in rows))
    L.append("- Bay Area in {Yes, No, blank}: %s" % all(r[idx["Bay Area"]] in {"Yes", "No", ""} for r in rows))
    L.append("- Yuno fit in {A, B, C, blank}: %s" % all(r[idx["Yuno fit"]] in {"A", "B", "C", ""} for r in rows))
    L.append("- ARR as of conforming or blank: %s" % all(r[idx["ARR as of"]] == "" or DATE_OK.match(r[idx["ARR as of"]]) for r in rows))
    L.append("- HQ 'City, Country' or blank: %s" % all(r[idx["HQ"]] == "" or HQ_OK.match(r[idx["HQ"]]) for r in rows))
    L.append("- Em-dashes remaining: %d; en-dashes remaining: %d; ' - ' remaining: %d" % (
        sum(v.count("\u2014") for r in rows for v in r), sum(v.count("\u2013") for r in rows for v in r), sum(v.count(" - ") for r in rows for v in r)))
    L.append("- Samuel top 100 markers present: %d" % sum(1 for r in rows if sam_rank(r)))
    L.append("- Rank sequence 1..%d contiguous: %s" % (len(with_arr), [r[idx["Rank"]] for r in rows if r[idx["Rank"]]] == [str(i) for i in range(1, len(with_arr) + 1)]))
    L.append("- Last row: %s (Rank %r)" % (rows[-1][idx["Company"]], rows[-1][idx["Rank"]]))
    L.append("")
    with open(out_log, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    # ------------------------------------------------------------------ 8. stdout summary
    top5 = ", ".join("%s ($%sM)" % (r[idx["Company"]], r[idx["ARR ($M)"]]) for r in rows[:5])
    print("Rows: %d data rows + header, %d columns (in: %d)" % (len(rows), N_COLS, n_in))
    print("Rows with ARR (ranked): %d; without ARR: %d" % (len(with_arr), len(rows) - len(with_arr)))
    print("Top 5 by ARR: %s" % top5)
    print("Duplicates found: %d" % len(dup_report))
    print("Blanks: Payments lead: name %d, Website %d (hygiene edits: %d)" % (blanks["Payments lead: name"], blanks["Website"], len(log.changes)))


if __name__ == "__main__":
    main()
