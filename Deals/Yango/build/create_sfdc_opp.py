#!/usr/bin/env python3
"""Create the "Yango (Col, Pe, Bol, Ven)" opportunity in Yuno's Salesforce via the REST API.

Needs credentials in the repo-root .env (never committed):
  SF_USERNAME, SF_PASSWORD, SF_SECURITY_TOKEN      (username-password flow; fails if the org is SSO-only), or
  SF_INSTANCE_URL + SF_ACCESS_TOKEN                 (a session id / OAuth access token, e.g. from a Connected App)
  SF_DOMAIN                                         optional, default "login"

Usage:
  python3 create_sfdc_opp.py --describe             print required fields, picklists and record types for Opportunity
  python3 create_sfdc_opp.py                        dry run: show the payload and any open opps already on the account
  python3 create_sfdc_opp.py --create               create the opp, attach contact roles, print the URL
  python3 create_sfdc_opp.py --create --advance "Discovery,Demo/BP"   also walk the stage forward after creation
  python3 create_sfdc_opp.py --create --set LeadSource=Outbound --set Forecast_Category__c=Pipeline

What it does NOT do: click "Set Pricing" (a Salesforce Flow). Submit pricing in the UI from the spec in
Deals/Yango/yango-salesforce-opp-2026-10-07.md; Finance approval moves the opp to Proposal Sent automatically.
"""
import argparse
import os
import sys
from pathlib import Path

try:
    from simple_salesforce import Salesforce
except ImportError:
    sys.exit("pip3 install simple-salesforce")

ROOT = Path(__file__).resolve().parents[3]
SPEC = ROOT / "Deals/Yango/yango-salesforce-opp-2026-10-07.md"

ACCOUNT_ID = "001Hu00003QIh8UIAT"          # Yango (not Yango Deli Israel 001Ps00001YsGJyIAN)
OPP_NAME = "Yango (Col, Pe, Bol, Ven)"
CLOSE_DATE = "2026-12-31"                   # assumption: Q4 2026
AMOUNT = 285_660                            # USD / year at full four-country volume ($23,805 / month)
START_STAGE = "Meeting Booked"
PROPOSAL_LINK = "https://deck.y.uno/yangobclatam"

DESCRIPTION = (
    "Driver top-up (recharge) collection for Colombia, Peru, Bolivia and Venezuela on one platform; Yuno on the "
    "collection side only (Cobre keeps payouts in CO, Monnet in PE). Root cause from the 19-aug-2026 discovery call: "
    "card binding succeeds 68-70% because acquirers have no local presence; bound cards approve at 90-92%. Pitch: "
    "zero-cost card verification + smart routing + local methods. Business case sent 4-sep (deck.y.uno/yangobclatam): "
    "$87.7M/yr cashless recharges, 38.9M tx, card-rail case $3.21M/yr. Final proposal sent by WhatsApp ~30-sep: "
    "$12,000/mo platform fee + 0.25/0.20/0.15/0.10% of approved recharge volume pooled across the four countries, no "
    "minimum, no fixed per-tx fee, declines and card verification free; $23,805/mo ($285,660/yr) at full volume. "
    "Presented to HQ 1-oct by the Colombia team; decision owners Konstantin (payments) and Sergey Solyakov "
    "(integrations). Incumbents: PayU, Unlimit, Inswitch."
)
NEXT_STEP = (
    "HQ feedback on proposal (presented 1-oct); meeting with Konstantin and Sergey; Set Pricing + Finance sign-off on "
    "red-zone items; align with Piotr Sierpinski on the Russian-HQ channel."
)

CONTACTS = [
    # (first, last, email, title, role, primary)
    ("Javier", "Patiño", "jpatino@yango-team.com", "Head of Operations, Colombia", "Champion", True),
    ("Alejandro", "Sanabria Cárdenas", "pcardenas@yango-team.com", "Finance Manager", "Economic Buyer", False),
    ("Luis Alejandro", "Montealegre Díaz", "lmontealegre@yango-team.com", "Ops Manager, Colombia", "Influencer", False),
]


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def connect():
    load_env()
    if os.environ.get("SF_ACCESS_TOKEN") and os.environ.get("SF_INSTANCE_URL"):
        return Salesforce(instance_url=os.environ["SF_INSTANCE_URL"], session_id=os.environ["SF_ACCESS_TOKEN"])
    missing = [k for k in ("SF_USERNAME", "SF_PASSWORD", "SF_SECURITY_TOKEN") if not os.environ.get(k)]
    if missing:
        sys.exit(f"No Salesforce credentials. Fill {', '.join(missing)} (or SF_INSTANCE_URL + SF_ACCESS_TOKEN) in {ROOT / '.env'}")
    return Salesforce(
        username=os.environ["SF_USERNAME"],
        password=os.environ["SF_PASSWORD"],
        security_token=os.environ["SF_SECURITY_TOKEN"],
        domain=os.environ.get("SF_DOMAIN", "login"),
    )


def describe(sf):
    d = sf.Opportunity.describe()
    print("== Required on create (no default) ==")
    for f in d["fields"]:
        if f["createable"] and not f["nillable"] and not f.get("defaultedOnCreate"):
            print(f"  {f['name']:40} {f['type']}")
    print("\n== Picklists of interest ==")
    for f in d["fields"]:
        if f["type"] == "picklist" and f["name"] in {"StageName", "LeadSource", "Type", "ForecastCategoryName"} or (
            f["type"] == "picklist" and any(k in f["name"].lower() for k in ("forecast", "region", "vertical", "industry", "product", "pricing"))
        ):
            vals = [p["value"] for p in f["picklistValues"] if p["active"]]
            print(f"  {f['name']} ({f['label']}): {vals}")
    print("\n== Custom fields that look like pricing / proposal / deal-desk ==")
    keys = ("fee", "pric", "minimum", "mrr", "arr", "tar", "acv", "proposal", "decision", "blocker", "comment", "credit", "contract", "sdr", "kam", "engineer")
    for f in d["fields"]:
        if f["custom"] and any(k in f["name"].lower() for k in keys):
            print(f"  {f['name']:45} {f['type']:12} {f['label']}")
    print("\n== Record types ==")
    for r in sf.query("SELECT Id, Name, DeveloperName, IsActive FROM RecordType WHERE SobjectType = 'Opportunity'")["records"]:
        print(f"  {r['Id']}  {r['Name']}  ({r['DeveloperName']})  active={r['IsActive']}")


def open_opps(sf):
    q = ("SELECT Id, Name, StageName, IsClosed, Owner.Name, CloseDate, Amount FROM Opportunity "
         f"WHERE AccountId = '{ACCOUNT_ID}' ORDER BY CreatedDate DESC")
    return sf.query(q)["records"]


def ensure_contacts(sf, create):
    rows = sf.query(f"SELECT Id, Email, Name FROM Contact WHERE AccountId = '{ACCOUNT_ID}'")["records"]
    by_email = {(r["Email"] or "").lower(): r["Id"] for r in rows}
    out = []
    for first, last, email, title, role, primary in CONTACTS:
        cid = by_email.get(email.lower())
        if not cid:
            if create:
                cid = sf.Contact.create({"FirstName": first, "LastName": last, "Email": email, "Title": title, "AccountId": ACCOUNT_ID})["id"]
                print(f"  created Contact {first} {last} -> {cid}")
            else:
                print(f"  (dry run) would create Contact {first} {last} <{email}>")
        out.append((cid, role, primary, f"{first} {last}"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--describe", action="store_true")
    ap.add_argument("--create", action="store_true")
    ap.add_argument("--stage", default=START_STAGE)
    ap.add_argument("--advance", default="", help='comma-separated stages to step through after creation, e.g. "Discovery,Demo/BP"')
    ap.add_argument("--record-type", default="", help="RecordType Name or DeveloperName (e.g. New Merchant)")
    ap.add_argument("--set", action="append", default=[], metavar="Field=Value", help="extra fields, e.g. LeadSource=Outbound")
    args = ap.parse_args()

    sf = connect()
    if args.describe:
        describe(sf)
        return

    print("== Open/closed opps already on the Yango account ==")
    for o in open_opps(sf):
        flag = "OPEN " if not o["IsClosed"] else "closed"
        print(f"  {flag} {o['Id']} {o['Name']!r} stage={o['StageName']} owner={o['Owner']['Name']} close={o['CloseDate']} amount={o['Amount']}")
    dupes = [o for o in open_opps(sf) if not o["IsClosed"] and o["Name"].strip().lower() == OPP_NAME.lower()]
    if dupes:
        sys.exit(f"An open opp named {OPP_NAME!r} already exists: {dupes[0]['Id']}. Not creating a duplicate.")

    payload = {
        "Name": OPP_NAME,
        "AccountId": ACCOUNT_ID,
        "StageName": args.stage,
        "CloseDate": CLOSE_DATE,
        "Amount": AMOUNT,
        "CurrencyIsoCode": "USD",
        "Description": DESCRIPTION,
        "NextStep": NEXT_STEP[:255],
    }
    if args.record_type:
        rts = sf.query("SELECT Id, Name, DeveloperName FROM RecordType WHERE SobjectType = 'Opportunity'")["records"]
        match = [r for r in rts if args.record_type.lower() in (r["Name"].lower(), r["DeveloperName"].lower())]
        if not match:
            sys.exit(f"Record type {args.record_type!r} not found. Run --describe to list them.")
        payload["RecordTypeId"] = match[0]["Id"]
    for kv in args.set:
        k, v = kv.split("=", 1)
        payload[k] = v
    # drop CurrencyIsoCode if the org is single-currency
    fields = {f["name"] for f in sf.Opportunity.describe()["fields"]}
    payload = {k: v for k, v in payload.items() if k in fields}

    print("\n== Payload ==")
    for k, v in payload.items():
        print(f"  {k}: {str(v)[:110]}{'...' if len(str(v)) > 110 else ''}")

    print("\n== Contacts ==")
    contacts = ensure_contacts(sf, create=args.create)

    if not args.create:
        print("\nDry run. Re-run with --create to write. Spec:", SPEC)
        return

    opp_id = sf.Opportunity.create(payload)["id"]
    url = f"{sf.base_url.split('/services')[0].replace('.my.salesforce.com', '.lightning.force.com')}/lightning/r/Opportunity/{opp_id}/view"
    print(f"\nCreated opportunity {opp_id}\n  {url}")

    for cid, role, primary, label in contacts:
        if cid:
            try:
                sf.OpportunityContactRole.create({"OpportunityId": opp_id, "ContactId": cid, "Role": role, "IsPrimary": primary})
                print(f"  contact role: {label} -> {role}")
            except Exception as e:  # role picklist may differ; keep going
                print(f"  contact role failed for {label}: {e}")

    for stage in [s.strip() for s in args.advance.split(",") if s.strip()]:
        try:
            sf.Opportunity.update(opp_id, {"StageName": stage})
            print(f"  stage -> {stage}")
        except Exception as e:
            print(f"  stage -> {stage} BLOCKED by validation: {e}")
            break

    print("\nNext: open the opp, set Lead Source if not passed, upload the Business Proposal Link, then click Set Pricing "
          "with the numbers in", SPEC)


if __name__ == "__main__":
    main()
