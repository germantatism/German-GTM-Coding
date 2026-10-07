#!/usr/bin/env python3
"""Merge fill agent results (fill/out_f*.json) into master.json -> master_merged.json + merge_log.md.

Deterministic and re-runnable. Rules (from fill/MERGE_BRIEF.md):
- fill blanks only; never overwrite a non-empty master cell
  (exception: "Pending: lookup rate-limited, retry in progress" in the payments-lead title counts as blank)
- contradictions: keep master, append "Fill agent: <field> = <value>" to "Merge notes"
- Notes: append with " | "; founded -> "Founded YYYY." appended to German's notes; fill_notes -> Merge notes
- normalize: ARR ($M) numeric string, dates "Mon YYYY", HQ "City, Country" with US, Bay Area Yes/No,
  Stripe evidence default "Not verified", no em-dashes or " - " as punctuation
- "light" fill rows: only valuation_b, notes, fill_notes apply
"""
import glob
import json
import os
import re
import sys
from collections import Counter, OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(BASE, "master.json")
FILL_GLOB = os.path.join(BASE, "fill", "out_f*.json")
OUT_JSON = os.path.join(BASE, "master_merged.json")
OUT_LOG = os.path.join(BASE, "merge_log.md")

PENDING = "Pending: lookup rate-limited, retry in progress"

# fill key -> master header (simple 1:1 "fill blank" columns)
SIMPLE_MAP = OrderedDict([
    ("description", "Company description"),
    ("hq", "HQ"),
    ("bay_area", "Bay Area"),
    ("pricing", "Plans / pricing"),
    ("arr_text", "ARR (German research)"),
    ("arr_m", "ARR ($M)"),
    ("arr_as_of", "ARR as of"),
    ("figure_basis", "Figure basis"),
    ("confidence", "Confidence"),
    ("users", "Users"),
    ("website", "Website"),
    ("linkedin_company", "LinkedIn (company)"),
    ("segment", "Segment"),
    ("revenue_model", "Revenue model"),
    ("yuno_fit", "Yuno fit"),
    ("payments_angle", "Payments angle"),
    ("stripe_evidence", "Stripe evidence"),
    ("valuation_b", "Valuation ($B)"),
])
LIGHT_KEYS = {"valuation_b", "notes", "fill_notes"}

# fill values that mean "I do not know", never a contradiction of a non-empty master cell
NON_ASSERTIVE = {
    "bay_area": {"unverified", ""},
    "stripe_evidence": {"not verified", ""},
    "confidence": {"no figure", ""},
    "hq": {"not verified", "us (city not verified)", "us (not verified)", ""},
}

ALIASES = {
    "fal": ["fal ai"], "arena": ["lmarena"], "chai": ["chai research"],
    "cursor": ["anysphere"], "thinking machines": ["thinking machines lab"],
    "handshake": ["handshake ai"], "cognition": ["cognition devin windsurf"],
    "superhuman": ["grammarly"], "intercom": ["fin"], "bolt new": ["stackblitz"],
    "replika": ["luka"], "tolan": ["portola"], "poke": ["interaction company", "the interaction company"],
    "world labs": ["marble"], "labelbox": ["alignerr"], "langchain": ["langsmith"],
    "cerebras": ["cerebras inference"], "invideo": ["invideo ai"], "vercel": ["v0"],
    "groq": ["groqcloud"], "amp": ["sourcegraph"], "poe": ["quora"], "xai": ["grok"],
    "artisan": ["ava"], "magnific": ["freepik"], "manus": ["butterfly effect"],
    "picturethis": ["glority"],
}

MONTHS = {
    "jan": "Jan", "january": "Jan", "feb": "Feb", "february": "Feb", "mar": "Mar", "march": "Mar",
    "apr": "Apr", "april": "Apr", "may": "May", "jun": "Jun", "june": "Jun", "jul": "Jul", "july": "Jul",
    "aug": "Aug", "august": "Aug", "sep": "Sep", "sept": "Sep", "september": "Sep", "oct": "Oct",
    "october": "Oct", "nov": "Nov", "november": "Nov", "dec": "Dec", "december": "Dec",
}

BAY_AREA_CITIES = {
    "san francisco", "oakland", "berkeley", "palo alto", "mountain view", "sunnyvale", "san jose",
    "redwood city", "menlo park", "san mateo", "foster city", "los gatos", "santa clara", "cupertino",
    "fremont", "burlingame", "south san francisco", "san carlos", "belmont", "emeryville", "walnut creek",
    "hayward", "milpitas", "campbell", "los altos", "san rafael", "sausalito", "alameda", "san bruno",
    "daly city", "pleasanton", "san ramon", "newark", "union city", "richmond", "novato", "mill valley",
    "half moon bay", "saratoga", "morgan hill", "livermore", "dublin", "brisbane", "san leandro",
}
US_CITY_STATE = {
    "san francisco": "CA", "oakland": "CA", "berkeley": "CA", "palo alto": "CA", "mountain view": "CA",
    "sunnyvale": "CA", "san jose": "CA", "redwood city": "CA", "menlo park": "CA", "san mateo": "CA",
    "foster city": "CA", "los gatos": "CA", "santa clara": "CA", "cupertino": "CA", "fremont": "CA",
    "burlingame": "CA", "south san francisco": "CA", "san carlos": "CA", "emeryville": "CA",
    "los angeles": "CA", "san diego": "CA", "costa mesa": "CA", "irvine": "CA", "santa monica": "CA",
    "sacramento": "CA", "pasadena": "CA", "venice": "CA", "culver city": "CA", "long beach": "CA",
    "new york": "NY", "brooklyn": "NY", "miami": "FL", "orlando": "FL", "tampa": "FL",
    "pittsburgh": "PA", "philadelphia": "PA", "cambridge": "MA", "boston": "MA", "somerville": "MA",
    "st. louis": "MO", "st louis": "MO", "seattle": "WA", "bellevue": "WA", "redmond": "WA",
    "austin": "TX", "dallas": "TX", "houston": "TX", "denver": "CO", "boulder": "CO", "chicago": "IL",
    "washington": "DC", "atlanta": "GA", "salt lake city": "UT", "lehi": "UT", "provo": "UT",
    "portland": "OR", "las vegas": "NV", "phoenix": "AZ", "scottsdale": "AZ", "minneapolis": "MN",
    "nashville": "TN", "raleigh": "NC", "durham": "NC", "charlotte": "NC", "detroit": "MI",
    "ann arbor": "MI", "columbus": "OH", "madison": "WI", "princeton": "NJ", "jersey city": "NJ",
    "stamford": "CT", "new haven": "CT", "wilmington": "DE", "arlington": "VA", "reston": "VA",
    "baltimore": "MD", "bethesda": "MD", "providence": "RI", "burlington": "VT", "honolulu": "HI",
}
CITY_STATES = {"singapore": "Singapore", "hong kong": "Hong Kong", "monaco": "Monaco"}


# ---------------------------------------------------------------- helpers
def s(v):
    """Cell value as a stripped string ('' for None)."""
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def blank(v):
    return s(v) == ""


def norm_name(name):
    n = s(name).lower()
    n = re.sub(r"\([^)]*\)", " ", n)
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def name_keys(name):
    """All normalized keys a company name may match under (full name, name before parenthesis, aliases)."""
    keys = set()
    full = norm_name(name)
    if full:
        keys.add(full)
    # name before any parenthesis, and parenthetical contents
    base = norm_name(re.split(r"\(", s(name), 1)[0])
    if base:
        keys.add(base)
    for inner in re.findall(r"\(([^)]*)\)", s(name)):
        inner_n = norm_name(re.sub(r"\b(formerly|the|inc\.?|spinout)\b", " ", inner, flags=re.I))
        if inner_n:
            keys.add(inner_n)
    for k in list(keys):
        for canon, alts in ALIASES.items():
            if k == canon or k in alts:
                keys.add(canon)
                keys.update(alts)
    return keys


def fix_punct(text):
    """No em/en dashes, no ' - ' as punctuation. Replace with commas."""
    t = s(text)
    if not t:
        return t
    t = t.replace("—", ", ").replace("–", ", ")
    t = re.sub(r"\s+-\s+", ", ", t)
    t = re.sub(r"\s*,\s*,", ",", t)
    t = re.sub(r" {2,}", " ", t)
    t = re.sub(r",\s*$", "", t)
    return t.strip()


def norm_number(v):
    """Numeric string without commas; '' if not numeric (caller logs)."""
    t = s(v)
    if not t:
        return ""
    cleaned = t.replace(",", "").replace("$", "").replace("~", "").strip()
    cleaned = re.sub(r"\s*(M|B|m|b|million|billion)$", "", cleaned)
    try:
        f = float(cleaned)
    except ValueError:
        return None
    if f.is_integer():
        return str(int(f))
    return ("%.4f" % f).rstrip("0").rstrip(".")


def norm_date(v):
    """'Mon YYYY' when the value is a month+year; leave FY2026 / Q1 2025 / H1 2026 / 2024 / Undated alone."""
    t = s(v)
    if not t:
        return t, ""
    note = ""
    m = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", t)
    if m and re.match(r"^(FY)?\d{4}$", m.group(1).strip()):
        note = t
        t = m.group(1).strip()
    m = re.match(r"^([A-Za-z]+)\.?\s+(\d{4})$", t)
    if m and m.group(1).lower() in MONTHS:
        return f"{MONTHS[m.group(1).lower()]} {m.group(2)}", note
    m = re.match(r"^(\d{4})-(\d{1,2})$", t)
    if m:
        mon = int(m.group(2))
        if 1 <= mon <= 12:
            return f"{list(dict.fromkeys(MONTHS.values()))[mon - 1]} {m.group(1)}", note
    m = re.match(r"^([A-Za-z]+)\s*-\s*([A-Za-z]+)\s+(\d{4})$", t)  # Feb-Jun 2026
    if m and m.group(1).lower() in MONTHS and m.group(2).lower() in MONTHS:
        return f"{MONTHS[m.group(1).lower()]}-{MONTHS[m.group(2).lower()]} {m.group(3)}", note
    return t, note


def norm_hq(v):
    t = fix_punct(v)
    t = re.sub(r"\bU\.?S\.?A\.?\b", "US", t)
    t = re.sub(r"\bUnited States\b", "US", t)
    t = re.sub(r"\bUnited Kingdom\b", "UK", t)
    t = re.sub(r"\s+,", ",", t)
    return t


def norm_yes_no(v):
    t = s(v).lower()
    if t in ("yes", "y", "true"):
        return "Yes"
    if t in ("no", "n", "false"):
        return "No"
    if t in ("unverified", "unknown", "not verified"):
        return "Unverified"
    return s(v)


def hq_city_country(hq):
    """Parse an HQ string -> (city, state_or_None, country) or None when unparseable/unverified."""
    t = s(hq)
    if not t:
        return None
    low = t.lower()
    if "not verified" in low or "(est.)" in low or "/" in t:
        return None
    t = re.sub(r"\s*\([^)]*\)", "", t).strip()  # drop "(remote-first)" etc.
    parts = [p.strip() for p in t.split(",") if p.strip()]
    if len(parts) == 1:
        if parts[0].lower() in CITY_STATES:
            return parts[0], None, CITY_STATES[parts[0].lower()]
        return None
    if len(parts) == 2:
        return parts[0], None, parts[1]
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    return None


def location_german(hq):
    """'City, ST' for US cities, 'City, Country' otherwise; '' when it cannot be derived."""
    p = hq_city_country(hq)
    if not p:
        return ""
    city, state, country = p
    if country == "US":
        st = state or US_CITY_STATE.get(city.lower())
        return f"{city}, {st}" if st else ""
    return f"{city}, {country}"


def bay_area_from_hq(hq):
    p = hq_city_country(hq)
    if not p:
        return ""
    city, state, country = p
    if country == "US" and city.lower() in BAY_AREA_CITIES:
        return "Yes"
    if city.lower() in US_CITY_STATE or country != "US":
        return "No"
    return ""


def canon_for_compare(field, v):
    t = fix_punct(s(v)).lower()
    t = re.sub(r"\s+", " ", t)
    if field in ("arr_m", "valuation_b"):
        n = norm_number(t)
        return n if n is not None else t
    if field == "hq":
        return norm_hq(t).lower()
    return t


def append_text(existing, addition, sep):
    existing, addition = s(existing), s(addition)
    if not addition:
        return existing, False
    if addition.lower() in existing.lower():
        return existing, False
    return (existing + sep + addition) if existing else addition, True


# ---------------------------------------------------------------- main
def main():
    master = json.load(open(MASTER, encoding="utf-8"))
    header = master[0]
    rows = [list(r) + [""] * (len(header) - len(r)) for r in master[1:]]
    col = {h: i for i, h in enumerate(header)}
    for needed in list(SIMPLE_MAP.values()) + ["Company", "Location (German)", "Notes", "German's notes",
                                                "Payments lead: title", "Payments lead: name",
                                                "Payments lead: LinkedIn", "Backup contact", "Merge notes"]:
        if needed not in col:
            sys.exit(f"master.json header is missing column {needed!r}")

    # index master rows by every name key
    index = {}
    for ri, r in enumerate(rows):
        for k in name_keys(r[col["Company"]]):
            index.setdefault(k, []).append(ri)

    fills = []
    for path in sorted(glob.glob(FILL_GLOB)):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as e:  # partial / corrupt file: skip, report
            fills.append({"_error": f"{os.path.basename(path)}: {e}"})
            continue
        if isinstance(data, dict):
            data = data.get("rows") or data.get("fills") or list(data.values())
        for fr in data:
            if isinstance(fr, dict) and s(fr.get("company")):
                fr["_src"] = os.path.basename(path)
                fills.append(fr)

    log_rows = []          # per company dict
    unmatched = []
    file_errors = [f["_error"] for f in fills if "_error" in f]
    fills = [f for f in fills if "_error" not in f]
    seen_fill = Counter()
    total_filled = 0
    total_conflicts = 0
    filled_by_col = Counter()
    conflicts_by_col = Counter()
    touched_rows = set()

    for fr in fills:
        company = s(fr["company"])
        kind = s(fr.get("kind")).lower() or "full"
        # ---- match
        cands = []
        for k in name_keys(company):
            for ri in index.get(k, []):
                if ri not in cands:
                    cands.append(ri)
        if not cands:
            unmatched.append((company, kind, fr["_src"]))
            continue
        if len(cands) > 1:
            # prefer exact normalized full-name match
            exact = [ri for ri in cands if norm_name(rows[ri][col["Company"]]) == norm_name(company)]
            cands = exact or cands[:1]
        ri = cands[0]
        row = rows[ri]
        seen_fill[ri] += 1
        touched_rows.add(ri)
        entry = {"company": row[col["Company"]], "fill_company": company, "kind": kind, "src": fr["_src"],
                 "filled": [], "conflicts": [], "appended": [], "skipped": []}

        def cell(h):
            return s(row[col[h]])

        def put(h, value, field):
            nonlocal total_filled
            row[col[h]] = value
            entry["filled"].append(f"{h} = {value}")
            filled_by_col[h] += 1
            total_filled += 1

        def conflict(field, h, value):
            nonlocal total_conflicts
            note = f"Fill agent: {field} = {fix_punct(value)}"
            new, added = append_text(cell("Merge notes"), note, " | ")
            if added:
                row[col["Merge notes"]] = new
            entry["conflicts"].append(f"{h}: master = {cell(h)!r}, fill = {s(value)!r}")
            conflicts_by_col[h] += 1
            total_conflicts += 1

        active_keys = LIGHT_KEYS if kind == "light" else set(fr.keys())

        # ---- simple fill-blank columns
        for fk, h in SIMPLE_MAP.items():
            if fk not in active_keys:
                continue
            raw = fr.get(fk, "")
            val = s(raw)
            extra_note = ""
            # normalize
            if fk in ("arr_m", "valuation_b"):
                n = norm_number(val)
                if n is None:
                    entry["skipped"].append(f"{h}: non-numeric fill value {val!r} not written")
                    extra_note = f"Fill agent: {fk} = {val}"
                    val = ""
                else:
                    val = n
            elif fk == "arr_as_of":
                val, extra_note = norm_date(val)
                if extra_note:
                    extra_note = f"Fill agent: arr_as_of = {extra_note}"
            elif fk == "hq":
                val = norm_hq(val)
            elif fk == "bay_area":
                val = norm_yes_no(val)
            else:
                val = fix_punct(val)
            if extra_note:
                new, added = append_text(cell("Merge notes"), fix_punct(extra_note), " | ")
                if added:
                    row[col["Merge notes"]] = new
                    entry["appended"].append("Merge notes <- " + fix_punct(extra_note))

            master_val = cell(h)
            if master_val == "":
                if val != "":
                    put(h, val, fk)
            else:
                if val == "" or val.lower() in NON_ASSERTIVE.get(fk, set()):
                    continue
                if canon_for_compare(fk, val) != canon_for_compare(fk, master_val):
                    conflict(fk, h, val)

        if kind != "light":
            # ---- Stripe evidence default
            if cell("Stripe evidence") == "":
                put("Stripe evidence", "Not verified", "stripe_evidence")
            # ---- Bay Area: Yes/No from effective HQ when blank or Unverified
            ba = cell("Bay Area")
            if ba in ("", "Unverified"):
                derived = bay_area_from_hq(cell("HQ"))
                if derived and derived != ba:
                    if ba == "":
                        put("Bay Area", derived, "bay_area")
                    else:
                        row[col["Bay Area"]] = derived
                        entry["filled"].append(f"Bay Area = {derived} (derived from HQ, was Unverified)")
                        filled_by_col["Bay Area"] += 1
                        total_filled += 1
            # ---- Location (German) from effective HQ, only if blank
            if cell("Location (German)") == "" and cell("HQ"):
                loc = location_german(cell("HQ"))
                if loc:
                    put("Location (German)", loc, "hq")
                else:
                    entry["skipped"].append(f"Location (German): cannot derive City, ST/Country from HQ {cell('HQ')!r}")

        # ---- Notes (append)
        if "notes" in active_keys and s(fr.get("notes")):
            new, added = append_text(cell("Notes"), fix_punct(fr["notes"]), " | ")
            if added:
                was_blank = cell("Notes") == ""
                row[col["Notes"]] = new
                filled_by_col["Notes"] += 1
                total_filled += 1
                (entry["filled"] if was_blank else entry["appended"]).append(
                    ("Notes = " if was_blank else "Notes <- ") + fix_punct(fr["notes"]))

        if kind != "light":
            # ---- founded -> German's notes
            founded = s(fr.get("founded"))
            if founded:
                yr = re.search(r"\d{4}", founded)
                gn = cell("German's notes")
                if yr and not re.search(r"founded[^.;|]{0,25}\b%s\b" % yr.group(0), gn, flags=re.I):
                    add = f"Founded {yr.group(0)}."
                    new = (gn + " " + add) if gn else add
                    row[col["German's notes"]] = new
                    filled_by_col["German's notes"] += 1
                    total_filled += 1
                    (entry["filled"] if not gn else entry["appended"]).append(
                        ("German's notes = " if not gn else "German's notes <- ") + add)

            # ---- payments lead
            name = fix_punct(fr.get("payments_lead_name"))
            title = fix_punct(fr.get("payments_lead_title"))
            linkedin = s(fr.get("payments_lead_linkedin"))
            lvl_raw = s(fr.get("payments_lead_level"))
            try:
                level = int(float(lvl_raw)) if lvl_raw else 0
            except ValueError:
                level = 0
            if title and level == 2 and "finance owner" not in title.lower():
                title += " (finance owner; no dedicated payments role found)"
            elif title and level == 3 and "general owner" not in title.lower():
                title += " (general owner; small team, no payments or finance role found)"
            mt, mn, ml = cell("Payments lead: title"), cell("Payments lead: name"), cell("Payments lead: LinkedIn")
            title_blank = mt == "" or mt == PENDING
            if name or title:
                if title_blank and mn == "":
                    if title:
                        put("Payments lead: title", title, "payments_lead_title")
                    if name:
                        put("Payments lead: name", name, "payments_lead_name")
                    if linkedin and ml == "":
                        put("Payments lead: LinkedIn", linkedin, "payments_lead_linkedin")
                else:
                    # master already has a lead (people verification) -> never regress; note disagreement only
                    if name and mn and canon_for_compare("n", name) != canon_for_compare("n", mn):
                        conflict("payments_lead_name", "Payments lead: name", name)
                    if title and mt and not title_blank and canon_for_compare("t", title) != canon_for_compare("t", mt):
                        conflict("payments_lead_title", "Payments lead: title", title)
                    if title and title_blank and mt == PENDING:
                        # same person already named by master but title pending -> fill the title
                        if not name or canon_for_compare("n", name) == canon_for_compare("n", mn):
                            put("Payments lead: title", title, "payments_lead_title")
                    if linkedin and ml == "" and (not name or canon_for_compare("n", name) == canon_for_compare("n", mn)):
                        put("Payments lead: LinkedIn", linkedin, "payments_lead_linkedin")

            # ---- backup contact
            bname, btitle = fix_punct(fr.get("backup_name")), fix_punct(fr.get("backup_title"))
            if bname:
                backup = f"{bname}, {btitle}" if btitle else bname
                if cell("Backup contact") == "":
                    put("Backup contact", backup, "backup")
                elif canon_for_compare("b", bname) not in canon_for_compare("b", cell("Backup contact")):
                    conflict("backup_contact", "Backup contact", backup)

        # ---- fill_notes -> Merge notes
        fn = fix_punct(fr.get("fill_notes"))
        if fn:
            new, added = append_text(cell("Merge notes"), fn, " | ")
            if added:
                row[col["Merge notes"]] = new
                filled_by_col["Merge notes"] += 1
                entry["appended"].append("Merge notes <- " + fn)

        # final punctuation pass on cells this fill wrote (never on untouched master text)
        log_rows.append(entry)

    # ---------------------------------------------------------------- outputs
    out = [header] + rows
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    key_cols = ["ARR ($M)", "ARR as of", "HQ", "Bay Area", "Segment", "Yuno fit", "Stripe evidence",
                "Valuation ($B)", "Company description", "Location (German)", "Plans / pricing",
                "ARR (German research)", "Website", "LinkedIn (company)", "Payments lead: title",
                "Payments lead: name", "Payments lead: LinkedIn", "Backup contact"]

    def remaining(h):
        return sum(1 for r in rows if s(r[col[h]]) == "" or (h == "Payments lead: title" and s(r[col[h]]) == PENDING))

    dupes = [(rows[ri][col["Company"]], n) for ri, n in seen_fill.items() if n > 1]
    no_fill = [r[col["Company"]] for ri, r in enumerate(rows) if ri not in touched_rows]
    leftover_dash = sum(1 for r in rows for v in r if isinstance(v, str) and (re.search(r"\s-\s", v) or "—" in v))

    L = []
    L.append("# Merge log: fill/out_f*.json -> master_merged.json\n")
    L.append(f"- Master rows: {len(rows)} (header excluded), {len(header)} columns")
    L.append(f"- Fill rows read: {len(fills)} from {len(set(f['_src'] for f in fills))} files"
             + (f"; file errors: {file_errors}" if file_errors else ""))
    L.append(f"- Fill rows matched: {len(fills) - len(unmatched)}; unmatched: {len(unmatched)}; master rows touched: {len(touched_rows)}")
    L.append(f"- Cells filled or appended: {total_filled}; conflicts (master kept, noted in Merge notes): {total_conflicts}")
    if dupes:
        L.append(f"- Master rows hit by more than one fill row: {dupes}")
    L.append(f"- Master cells still containing ' - ' or an em-dash (untouched master text, not rewritten): {leftover_dash}")
    L.append("")
    L.append("## Cells filled per column\n")
    for h in header:
        if filled_by_col.get(h):
            L.append(f"- {h}: {filled_by_col[h]}")
    L.append("")
    L.append("## Conflicts per column\n")
    if conflicts_by_col:
        for h, n in conflicts_by_col.most_common():
            L.append(f"- {h}: {n}")
    else:
        L.append("- none")
    L.append("")
    L.append("## Remaining blanks per key column (after merge)\n")
    for h in key_cols:
        L.append(f"- {h}: {remaining(h)} blank / {len(rows)}" + (" (10 'Pending' titles counted as blank)" if h == "Payments lead: title" and any(s(r[col[h]]) == PENDING for r in rows) else ""))
    L.append("")
    L.append("## Unmatched fill rows\n")
    if unmatched:
        for c, k, src in unmatched:
            L.append(f"- {c} ({k}, {src})")
    else:
        L.append("- none")
    L.append("")
    L.append("## Master rows with no fill row\n")
    L.append("- " + (", ".join(no_fill) if no_fill else "none"))
    L.append("")
    L.append("## Per company\n")
    for e in sorted(log_rows, key=lambda e: e["company"].lower()):
        L.append(f"### {e['company']}  ({e['kind']}, {e['src']})")
        if e["filled"]:
            L.append(f"- Filled ({len(e['filled'])}): " + "; ".join(x.split(" = ", 1)[0] if " = " in x else x for x in e["filled"]))
        else:
            L.append("- Filled: none")
        for a in e["appended"]:
            L.append(f"- Appended: {a}")
        for c in e["conflicts"]:
            L.append(f"- Conflict: {c}")
        for sk in e["skipped"]:
            L.append(f"- Skipped: {sk}")
        L.append("")
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"rows={len(rows)} fills={len(fills)} matched={len(fills) - len(unmatched)} unmatched={len(unmatched)}")
    print(f"filled={total_filled} conflicts={total_conflicts}")
    print("remaining blanks: " + ", ".join(f"{h}={remaining(h)}" for h in key_cols))
    print(f"wrote {OUT_JSON}\nwrote {OUT_LOG}")


if __name__ == "__main__":
    main()
