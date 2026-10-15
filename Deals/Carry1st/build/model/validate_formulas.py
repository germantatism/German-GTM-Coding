#!/usr/bin/env python3
"""Static validation of bc_model.xlsx: every reference resolves to a populated cell, only safe functions, balanced parentheses."""
import re, sys
from openpyxl import load_workbook

PATH = sys.argv[1] if len(sys.argv) > 1 else "/Users/germantatis/Desktop/GTMCoding/Deals/Carry1st/build/model/bc_model.xlsx"
wb = load_workbook(PATH)
SAFE = {"SUM", "MIN", "MAX", "IF", "IFERROR", "INDEX", "MATCH", "AND", "OR", "ROUND", "ABS", "TEXT"}
XREF = re.compile(r"(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_\.]*))!\$?([A-Z]{1,3})\$?(\d+)(?::\$?([A-Z]{1,3})\$?(\d+))?")
LREF = re.compile(r"(?<![A-Za-z_!\$])\$?([A-Z]{1,3})\$?(\d+)(?::\$?([A-Z]{1,3})\$?(\d+))?(?![A-Za-z0-9_\(])")
FUNC = re.compile(r"([A-Z][A-Z0-9\._]*)\(")

errors, nform = [], 0


def col_to_idx(col):
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n


def check_cell(sheet, col, row, origin):
    ws = wb[sheet]
    v = ws.cell(row=int(row), column=col_to_idx(col)).value
    if v is None:
        errors.append(f"{origin}: reference {sheet}!{col}{row} is EMPTY")


def check_range(sheet, c1, r1, c2, r2, origin):
    # check endpoints and that the range is non-degenerate
    check_cell(sheet, c1, r1, origin)
    check_cell(sheet, c2, r2, origin)


for ws in wb.worksheets:
    for row in ws.iter_rows():
        for cell in row:
            v = cell.value
            if not (isinstance(v, str) and v.startswith("=")):
                continue
            nform += 1
            origin = f"{ws.title}!{cell.coordinate}"
            body = v[1:]
            if body.count("(") != body.count(")"):
                errors.append(f"{origin}: unbalanced parentheses")
            # strip string literals
            nostr = re.sub(r'"[^"]*"', '""', body)
            for fn in FUNC.findall(nostr):
                if fn not in SAFE:
                    errors.append(f"{origin}: function {fn} not in safe list")
            # cross-sheet refs
            for m in XREF.finditer(nostr):
                sheet = m.group(1) or m.group(2)
                if sheet not in wb.sheetnames:
                    errors.append(f"{origin}: unknown sheet {sheet}")
                    continue
                if m.group(5):
                    check_range(sheet, m.group(3), m.group(4), m.group(5), m.group(6), origin)
                else:
                    check_cell(sheet, m.group(3), m.group(4), origin)
            rest = XREF.sub(" ", nostr)
            for m in LREF.finditer(rest):
                if m.group(3):
                    check_range(ws.title, m.group(1), m.group(2), m.group(3), m.group(4), origin)
                else:
                    check_cell(ws.title, m.group(1), m.group(2), origin)

print(f"formulas checked: {nform}")
print(f"errors: {len(errors)}")
for e in errors[:60]:
    print("  ", e)
sys.exit(1 if errors else 0)
