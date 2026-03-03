#!/usr/bin/env python3
"""
tal_db.py — TAL Database Manager
Manages the local SQLite database for:
  - TAL (Target Account List) accounts
  - SDR profiles (name, region, industries)
  - Worked account tracking (auto-skipped in future prioritization runs)

Usage:
  python scripts/tal_db.py import-tal data/tal/samu-tal.csv --sdr samu
  python scripts/tal_db.py set-profile --sdr alejandro --region Global --industries "Retail,Fashion,Marketplaces"
  python scripts/tal_db.py get-profile --sdr alejandro
  python scripts/tal_db.py list-accounts --sdr alejandro --status free
  python scripts/tal_db.py mark-worked "Nike" --sdr alejandro
  python scripts/tal_db.py mark-blocked "Amazon" --reason "Active opp with AE"
  python scripts/tal_db.py get-next --sdr alejandro --count 5
  python scripts/tal_db.py stats --sdr alejandro
  python scripts/tal_db.py reset-worked --sdr alejandro
"""

import sqlite3
import csv
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List

import typer
from rich.console import Console
from rich.table import Table
from rich import box

# ─── Config ────────────────────────────────────────────────────────────────────
DB_PATH = Path(__file__).parent.parent / "data" / "tal" / "tal.db"
console = Console()
app = typer.Typer(
    name="tal-db",
    help="TAL Database Manager — tracks accounts, SDR profiles, and worked history.",
    add_completion=False,
)

# ─── DB Bootstrap ──────────────────────────────────────────────────────────────
def get_db() -> sqlite3.Connection:
    """Return a DB connection, creating the DB and schema if needed."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _init_schema(conn)
    return conn


def _init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS sdr_profiles (
            sdr_name    TEXT PRIMARY KEY,
            region      TEXT,
            industries  TEXT,          -- JSON array string
            updated_at  TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS accounts (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            sdr_name        TEXT NOT NULL,
            company_name    TEXT NOT NULL,
            website         TEXT,
            industry        TEXT,
            hq_country      TEXT,
            notes           TEXT,
            status          TEXT DEFAULT 'free',   -- free | worked | blocked | skip
            worked_at       TEXT,
            blocked_reason  TEXT,
            created_at      TEXT DEFAULT (datetime('now')),
            UNIQUE(sdr_name, company_name)
        );

        CREATE TABLE IF NOT EXISTS prioritization_log (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            sdr_name        TEXT NOT NULL,
            run_date        TEXT NOT NULL,
            companies_json  TEXT,           -- JSON list of company names surfaced
            created_at      TEXT DEFAULT (datetime('now'))
        );
    """)
    conn.commit()


# ─── Commands ──────────────────────────────────────────────────────────────────

@app.command("import-tal")
def import_tal(
    csv_file: Path = typer.Argument(..., help="Path to TAL CSV file"),
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name to associate accounts with"),
):
    """
    Import a TAL CSV into the database.
    Expected columns: Company Name, Website, Industry, HQ Country, Notes
    Skips duplicates (company already exists for this SDR).
    """
    if not csv_file.exists():
        console.print(f"[red]File not found:[/] {csv_file}")
        raise typer.Exit(1)

    conn = get_db()
    inserted = 0
    skipped = 0

    with open(csv_file, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = (row.get("Company Name") or "").strip()
            if not company:
                continue
            # Normalise column name variations
            website    = (row.get("Website") or "").strip()
            industry   = (row.get("Industry") or "").strip()
            hq_country = (row.get("HQ Country") or row.get("Country/HQ") or "").strip()
            notes      = (row.get("Notes") or "").strip()

            # Skip if notes indicate existing client
            if "yuno client" in notes.lower() or "already a client" in notes.lower():
                status = "skip"
            else:
                status = "free"

            try:
                conn.execute(
                    """
                    INSERT INTO accounts
                        (sdr_name, company_name, website, industry, hq_country, notes, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (sdr, company, website, industry, hq_country, notes, status),
                )
                inserted += 1
            except sqlite3.IntegrityError:
                skipped += 1  # Already exists for this SDR

    conn.commit()
    conn.close()

    console.print(f"[green]✓ Imported[/] [bold]{inserted}[/] accounts for SDR [bold]{sdr}[/]")
    if skipped:
        console.print(f"[yellow]⚠ Skipped[/] {skipped} duplicates (already in DB)")
    console.print(f"  DB location: [dim]{DB_PATH}[/]")


@app.command("set-profile")
def set_profile(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    region: str = typer.Option(..., "--region", "-r", help="Region (e.g. Global, LATAM, US)"),
    industries: str = typer.Option(
        ..., "--industries", "-i",
        help="Comma-separated list of target industries"
    ),
):
    """
    Save or update an SDR profile (name, region, target industries).
    This is stored once — no need to re-enter on every /prioritize run.
    """
    industry_list = [i.strip() for i in industries.split(",") if i.strip()]
    conn = get_db()
    conn.execute(
        """
        INSERT INTO sdr_profiles (sdr_name, region, industries, updated_at)
        VALUES (?, ?, ?, datetime('now'))
        ON CONFLICT(sdr_name) DO UPDATE SET
            region     = excluded.region,
            industries = excluded.industries,
            updated_at = excluded.updated_at
        """,
        (sdr, region, json.dumps(industry_list)),
    )
    conn.commit()
    conn.close()

    console.print(f"[green]✓ Profile saved[/] for [bold]{sdr}[/]")
    console.print(f"  Region:     {region}")
    console.print(f"  Industries: {', '.join(industry_list)}")


@app.command("get-profile")
def get_profile(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
):
    """Print the stored profile for an SDR."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM sdr_profiles WHERE sdr_name = ?", (sdr,)
    ).fetchone()
    conn.close()

    if not row:
        console.print(f"[yellow]No profile found for[/] [bold]{sdr}[/]")
        console.print("Run: [bold]python scripts/tal_db.py set-profile --sdr {sdr} --region ... --industries ...[/]")
        return

    industries = json.loads(row["industries"] or "[]")
    console.print(f"[bold]SDR:[/] {row['sdr_name']}")
    console.print(f"[bold]Region:[/] {row['region']}")
    console.print(f"[bold]Industries:[/] {', '.join(industries)}")
    console.print(f"[bold]Last updated:[/] {row['updated_at']}")


@app.command("list-accounts")
def list_accounts(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    status: Optional[str] = typer.Option(None, "--status", help="Filter by status: free|worked|blocked|skip"),
    limit: int = typer.Option(50, "--limit", "-n", help="Max rows to show"),
):
    """List accounts for an SDR, optionally filtered by status."""
    conn = get_db()
    query = "SELECT * FROM accounts WHERE sdr_name = ?"
    params: list = [sdr]
    if status:
        query += " AND status = ?"
        params.append(status)
    query += " ORDER BY company_name LIMIT ?"
    params.append(limit)

    rows = conn.execute(query, params).fetchall()
    conn.close()

    if not rows:
        console.print(f"[yellow]No accounts found[/] for {sdr}" + (f" with status={status}" if status else ""))
        return

    table = Table(title=f"Accounts for {sdr}", box=box.SIMPLE_HEAVY)
    table.add_column("#", style="dim", width=4)
    table.add_column("Company", style="bold")
    table.add_column("Industry")
    table.add_column("Country")
    table.add_column("Status")
    table.add_column("Worked At")

    status_styles = {
        "free": "[green]✅ free[/]",
        "worked": "[blue]✔ worked[/]",
        "blocked": "[red]🔒 blocked[/]",
        "skip": "[dim]⏭ skip[/]",
    }

    for i, row in enumerate(rows, 1):
        s = status_styles.get(row["status"], row["status"])
        table.add_row(
            str(i),
            row["company_name"],
            row["industry"] or "—",
            row["hq_country"] or "—",
            s,
            row["worked_at"] or "—",
        )

    console.print(table)
    console.print(f"[dim]Total: {len(rows)} accounts shown[/]")


@app.command("mark-worked")
def mark_worked(
    company: str = typer.Argument(..., help="Company name (exact match)"),
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
):
    """
    Mark a company as worked. It will be auto-skipped in future /prioritize runs.
    """
    conn = get_db()
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    result = conn.execute(
        """
        UPDATE accounts
        SET status = 'worked', worked_at = ?
        WHERE sdr_name = ? AND company_name = ?
        """,
        (now, sdr, company),
    )
    conn.commit()

    if result.rowcount == 0:
        console.print(f"[yellow]No account found:[/] '{company}' for SDR '{sdr}'")
        console.print("Check exact company name with: [bold]python scripts/tal_db.py list-accounts --sdr {sdr}[/]")
    else:
        console.print(f"[green]✓ Marked as worked:[/] [bold]{company}[/]")
        console.print(f"  SDR: {sdr} | At: {now}")
    conn.close()


@app.command("mark-blocked")
def mark_blocked(
    company: str = typer.Argument(..., help="Company name (exact match)"),
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    reason: str = typer.Option("", "--reason", "-r", help="Reason for blocking"),
):
    """
    Mark a company as blocked (active opp, AE ownership, etc.).
    It will be auto-skipped in future /prioritize runs.
    """
    conn = get_db()
    result = conn.execute(
        """
        UPDATE accounts
        SET status = 'blocked', blocked_reason = ?
        WHERE sdr_name = ? AND company_name = ?
        """,
        (reason, sdr, company),
    )
    conn.commit()

    if result.rowcount == 0:
        console.print(f"[yellow]No account found:[/] '{company}' for SDR '{sdr}'")
    else:
        console.print(f"[red]🔒 Marked as blocked:[/] [bold]{company}[/]")
        if reason:
            console.print(f"  Reason: {reason}")
    conn.close()


@app.command("get-next")
def get_next(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    count: int = typer.Option(20, "--count", "-n", help="Number of accounts to return (default 20, /prioritize will pick top 5)"),
):
    """
    Return the next N free accounts for an SDR, sorted by industry match (if profile exists).
    These are the candidates that /prioritize will score and select the top 5 from.
    Excludes: worked, blocked, skip.
    """
    conn = get_db()

    # Load SDR profile to check industry preferences
    profile = conn.execute(
        "SELECT * FROM sdr_profiles WHERE sdr_name = ?", (sdr,)
    ).fetchone()

    rows = conn.execute(
        """
        SELECT * FROM accounts
        WHERE sdr_name = ? AND status = 'free'
        ORDER BY company_name
        LIMIT ?
        """,
        (sdr, count * 4),  # Fetch extra so we can sort by industry match
    ).fetchall()
    conn.close()

    if not rows:
        console.print(f"[yellow]No free accounts remaining for {sdr}.[/]")
        console.print("All accounts may have been worked or blocked.")
        return

    # Sort by industry match if profile exists
    if profile:
        pref_industries = [i.lower() for i in json.loads(profile["industries"] or "[]")]
        def industry_score(row):
            ind = (row["industry"] or "").lower()
            return -1 if any(p in ind or ind in p for p in pref_industries) else 0
        rows = sorted(rows, key=industry_score)

    rows = rows[:count]

    table = Table(title=f"Next {len(rows)} accounts for {sdr} (candidates for /prioritize)", box=box.SIMPLE_HEAVY)
    table.add_column("#", style="dim", width=4)
    table.add_column("Company", style="bold")
    table.add_column("Website")
    table.add_column("Industry")
    table.add_column("Country")
    table.add_column("Notes")

    for i, row in enumerate(rows, 1):
        table.add_row(
            str(i),
            row["company_name"],
            row["website"] or "—",
            row["industry"] or "—",
            row["hq_country"] or "—",
            (row["notes"] or "")[:60],
        )

    console.print(table)

    if profile:
        industries = json.loads(profile["industries"] or "[]")
        console.print(f"[dim]Profile: {sdr} | Region: {profile['region']} | Industries: {', '.join(industries)}[/]")


@app.command("stats")
def stats(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
):
    """Show account pipeline stats for an SDR."""
    conn = get_db()

    totals = conn.execute(
        """
        SELECT status, COUNT(*) as cnt
        FROM accounts
        WHERE sdr_name = ?
        GROUP BY status
        """,
        (sdr,),
    ).fetchall()

    sessions = conn.execute(
        "SELECT COUNT(*) as cnt FROM prioritization_log WHERE sdr_name = ?", (sdr,)
    ).fetchone()

    last_session = conn.execute(
        """
        SELECT run_date, companies_json FROM prioritization_log
        WHERE sdr_name = ?
        ORDER BY created_at DESC LIMIT 1
        """,
        (sdr,),
    ).fetchone()

    conn.close()

    counts = {row["status"]: row["cnt"] for row in totals}
    total = sum(counts.values())

    console.print(f"\n[bold]📊 Pipeline Stats — {sdr}[/]\n")
    console.print(f"  Total accounts in TAL:   {total}")
    console.print(f"  ✅ Free (untouched):      {counts.get('free', 0)}")
    console.print(f"  ✔  Worked:               {counts.get('worked', 0)}")
    console.print(f"  🔒 Blocked:              {counts.get('blocked', 0)}")
    console.print(f"  ⏭  Skipped (client etc): {counts.get('skip', 0)}")
    console.print(f"\n  Prioritization runs:     {sessions['cnt'] if sessions else 0}")

    if last_session:
        companies = json.loads(last_session["companies_json"] or "[]")
        console.print(f"  Last run date:           {last_session['run_date']}")
        console.print(f"  Last run companies:      {', '.join(companies[:5])}" + (" ..." if len(companies) > 5 else ""))

    if total > 0:
        pct_worked = counts.get('worked', 0) / total * 100
        console.print(f"\n  Coverage:               {pct_worked:.1f}% of TAL worked")


@app.command("reset-worked")
def reset_worked(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    confirm: bool = typer.Option(False, "--confirm", help="Must pass --confirm to execute"),
):
    """
    Reset all 'worked' accounts back to 'free' for an SDR.
    Use with caution — this un-marks all previously worked accounts.
    """
    if not confirm:
        console.print("[red]⚠ Dangerous operation.[/] This will un-mark all worked accounts.")
        console.print("Pass [bold]--confirm[/] to execute.")
        return

    conn = get_db()
    result = conn.execute(
        "UPDATE accounts SET status = 'free', worked_at = NULL WHERE sdr_name = ? AND status = 'worked'",
        (sdr,),
    )
    conn.commit()
    conn.close()

    console.print(f"[green]✓ Reset {result.rowcount} worked accounts back to free for {sdr}[/]")


@app.command("log-session")
def log_session(
    sdr: str = typer.Option(..., "--sdr", "-s", help="SDR name"),
    companies: str = typer.Option(..., "--companies", "-c", help="Comma-separated list of company names surfaced this session"),
):
    """
    Internal: Log a prioritization session (called automatically by /prioritize after output).
    Records which companies were surfaced so future runs can avoid repeating too soon.
    """
    company_list = [c.strip() for c in companies.split(",") if c.strip()]
    today = datetime.utcnow().strftime("%Y-%m-%d")
    conn = get_db()
    conn.execute(
        "INSERT INTO prioritization_log (sdr_name, run_date, companies_json) VALUES (?, ?, ?)",
        (sdr, today, json.dumps(company_list)),
    )
    conn.commit()
    conn.close()
    console.print(f"[dim]Session logged: {len(company_list)} accounts surfaced for {sdr} on {today}[/]")


# ─── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app()
