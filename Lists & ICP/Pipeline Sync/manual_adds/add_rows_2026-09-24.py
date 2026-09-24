#!/usr/bin/env python3
"""Append UNICEF Colombia, Experian (DataCredito), Linea Directa, Tiendamia and Cruz Verde Colombia to Deal Status GTM > Deal Status Tracker.

Auth: service account ~/.config/gsuite/sa.json (the sheet must be shared as Editor with
gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com).
Idempotent: skips a row if the Company already exists (case-insensitive, trimmed), same rule as the sync.
Usage: python3 add_rows_2026-09-24.py [--dry] [--with-stale]
"""
import os, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

SA = os.path.expanduser("~/.config/gsuite/sa.json")
SID = "1WPz1JW9zQm06SQg9ncrBM-4BH8ZKWh5O2Pn18XvKKPc"
TAB = "Deal Status Tracker"
HEADERS = ["Company", "Website", "LinkedIn URL", "Industry", "Comments", "Status"]

ROWS = [
    ["UNICEF Colombia",
     "https://donaciones.unicef.org.co",
     "https://www.linkedin.com/company/unicefcolombia",
     "Nonprofit & Fundraising",
     "Inbound demo Sep 21 done (Idual Kerguelen, BI/CRM owner; Leidy Guio; Sebastian Garavito). 150K recurring donors, ~85% acceptance, manual orchestration across Credibanco iPay, Redeban, Wompi, Nuvei and batch bank debits. Dashboard demo booked Sep 29 3pm COT; need an SE for token migration and batch-debit questions.",
     "Demo"],
    ["Experian (DataCredito)",
     "https://www.datacredito.com.co",
     "https://www.linkedin.com/company/datacr%C3%A9dito",
     "Financial Services",
     "Call Sep 23 with Carlos Falla (PM) and Cristian Vargas (Midatacredito). Opportunity = subscriptions engine on savings-account debits (their main collection channel); PayU and Wompi stay. Pilot ~20K accounts, project in their next FY (Jan to May 2027). Subscriptions session Sep 29 2pm COT, reconciliation session Sep 30; send integration flow diagram + pricing after.",
     "Demo"],
    ["Linea Directa",
     "https://www.lineadirecta.com.co",
     "https://www.linkedin.com/company/l%C3%ADnea-directa-s.a.s",
     "Retail & E-commerce",
     "Inbound via Susana (SDR). Colombian fashion direct-sales group (Carmel, Pacifika, Loguin; Grupo Elede). Luis Paternina (Treasury Director) and Jesus Cubides (USC Manager). 300K digital tx/month in CO + 25K in PE, ticket COP 180K / PEN 200. Want Nequi, Daviplata, Wompi, PSE, Dale, Bancolombia app, cards, and Yape in Peru; integrate via API. Intro + dashboard demo Sep 30 2pm COT (Luis confirmed the slot, invite pending).",
     "Demo"],
    ["Tiendamia",
     "https://www.tiendamia.com",
     "https://www.linkedin.com/company/tiendamia",
     "E-commerce & Retail",
     "Booked by Pedro Ferrer (SDR): intro call Sep 25 9am COT with Salvador Boidi. Cross-border marketplace (Miami HQ; AR, BR, CR, EC, PE, UY). Yuno already demoed them in Feb 2024 (Cybersource flow for Uruguay, Slack #tiendamia-yuno); no CRM account in Gong. Confirm Salvador's role and what changed since 2024.",
     "Discovery"],
    ["Cruz Verde Colombia",
     "https://www.cruzverde.com.co",
     "https://www.linkedin.com/company/droguerias-cruz-verde-colombia",
     "Retail & E-commerce",
     "Inbound via Susana and Alejandro Bernal: intro May 21 (Andres Guzman Forero, Ecommerce Manager), demo Sep 1, dashboard review Sep 22; NDA and business case in progress (Sep 23). Mercado Pago only (incl. POS payment links), PSE 58% of sales, 100K tx/mo (80K MP + 20K cash), ticket ~$20 and falling. Pains: single-provider dependency, PSE downtime, rejections. Pricing model requested; concern = USD per-tx cost. Recommended open: $7K platform + $0.06/$0.05/$0.04 tranches (~$11.75K/mo).",
     "Demo"],
]

# SDR-sourced inbound with no follow-up on record. Added only with --with-stale.
STALE_ROWS = [
    ["American Red Cross",
     "https://www.redcross.org",
     "https://www.linkedin.com/company/american-red-cross",
     "Nonprofit & Fundraising",
     "Inbound via Susana (SDR): 30-min call Sep 2 with Carlos Carneiro (Merchant Services, seniority unconfirmed). No recap, follow-up or reply on record since. Angle if pursued: three disconnected gateways across donation surfaces and B2B Invoice Central on the blood-products line.",
     "Discovery"],
    ["Cobrana",
     "https://www.cobrana.pe",
     "",
     "Financial Services",
     "Intro via Isabella Ponce: calls Aug 21 and Aug 24 with Gabriel Shimabuko (co-founder, ex-Interbank). WhatsApp collections layer on top of Kashio in Peru, ~USD 67K/month; two-person startup. No follow-up since Aug 24.",
     "Discovery"],
]

def main():
    dry = "--dry" in sys.argv
    rows = ROWS + (STALE_ROWS if "--with-stale" in sys.argv else [])
    creds = service_account.Credentials.from_service_account_file(SA, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    svc = build("sheets", "v4", credentials=creds, cache_discovery=False)
    vals = svc.spreadsheets().values().get(spreadsheetId=SID, range=f"'{TAB}'!A1:F").execute().get("values", [])
    header = vals[0] if vals else []
    assert header[:6] == HEADERS, f"unexpected header: {header}"
    existing = {r[0].strip().lower() for r in vals[1:] if r and r[0].strip()}
    last = max((i + 1 for i, r in enumerate(vals) if r and r[0].strip()), default=1)
    to_add = [r for r in rows if r[0].strip().lower() not in existing]
    print(f"rows in tab: {len(vals)}, last filled row: {last}, to add: {[r[0] for r in to_add]}")
    if dry or not to_add:
        return
    rng = f"'{TAB}'!A{last + 1}:F{last + len(to_add)}"
    svc.spreadsheets().values().update(spreadsheetId=SID, range=rng, valueInputOption="USER_ENTERED", body={"values": to_add}).execute()
    print("written:", rng)

if __name__ == "__main__":
    main()
