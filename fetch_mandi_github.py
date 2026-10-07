#!/usr/bin/env python3
"""
fetch_mandi_github.py — GitHub Actions version of mandi fetcher.
Outputs consolidated JSON files for VM consumption.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
BASE_URL = f"https://api.data.gov.in/resource/{RESOURCE_ID}"

WATCHLIST = [
    "Rice", "Wheat", "Maize",
    "Bengal Gram", "Red Gram", "Green Gram", "Black Gram", "Gram",
    "Crude Palm Oil", "Mustard", "Groundnut", "Sunflower", "Soyabean",
    "Sugar", "Cotton",
    "Onion", "Tomato", "Potato", "Garlic", "Ginger", "Turmeric",
    "Brinjal", "Lemon", "Bhindi(Ladies Finger)", "Green Chilli",
    "Ginger(Green)", "Carrot", "Cabbage", "Pumpkin", "Bottle gourd",
    "Bitter gourd", "Snakeguard", "Cluster beans", "Green Avare(W)",
    "Banana", "Banana - Green",
]

FIELDS = "state,district,market,commodity,variety,grade,arrival_date,min_price,max_price,modal_price"
PAGE_SIZE = 1000
MAX_PAGES = 20
RATE_SLEEP = 0.5

def parse_date(s):
    if not s:
        return None
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s.strip(), fmt).date().isoformat()
        except ValueError:
            continue
    return None

def extract_rows(payload):
    if isinstance(payload, dict):
        for key in ("records", "data", "result", "results"):
            if isinstance(payload.get(key), list):
                return payload[key]
    if isinstance(payload, list):
        return payload
    return []

def fetch_commodity(key, commodity):
    all_rows = []
    for page in range(MAX_PAGES):
        params = {
            "api-key": key,
            "format": "json",
            "limit": PAGE_SIZE,
            "offset": page * PAGE_SIZE,
            "fields": FIELDS,
            f"filters[commodity]": commodity,
        }
        url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "indian-markets-desk/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                body = r.read().decode("utf-8")
        except Exception as e:
            print(f"WARN: {commodity} page {page}: {e}", file=sys.stderr)
            break
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            break
        if isinstance(payload, dict) and payload.get("error"):
            print(f"WARN: {commodity} API error: {payload['error']}", file=sys.stderr)
            break
        rows = extract_rows(payload)
        if not rows:
            break
        all_rows.extend(rows)
        if len(rows) < PAGE_SIZE:
            break
    # Find latest date
    latest = None
    for r in all_rows:
        d = parse_date(r.get("arrival_date"))
        if d and (latest is None or d > latest):
            latest = d
    if not latest:
        return None, None
    # Filter to latest day
    day_rows = [r for r in all_rows if parse_date(r.get("arrival_date")) == latest]
    return day_rows, latest

def main():
    key = os.environ.get("DATA_GOV_IN_API_KEY")
    if not key:
        print("ERROR: DATA_GOV_IN_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    all_data = {}
    all_spikes = []
    latest_date_overall = None

    for commodity in WATCHLIST:
        rows, latest = fetch_commodity(key, commodity)
        if not rows or not latest:
            continue
        if latest_date_overall is None or latest > latest_date_overall:
            latest_date_overall = latest

        # Compute modal avg
        modals = [float(r.get("modal_price") or 0) for r in rows
                  if str(r.get("modal_price") or "").strip() not in ("", "0", "0.0")]
        if not modals:
            continue
        avg = sum(modals) / len(modals)
        min_p = min(modals)
        max_p = max(modals)

        all_data[commodity] = {
            "arrival_date": latest,
            "markets": len(modals),
            "modal_avg": round(avg, 2),
            "modal_min": round(min_p, 2),
            "modal_max": round(max_p, 2),
            "rows": [
                {
                    "state": r.get("state"),
                    "district": r.get("district"),
                    "market": r.get("market"),
                    "variety": r.get("variety"),
                    "grade": r.get("grade"),
                    "min_price": float(r.get("min_price") or 0),
                    "max_price": float(r.get("max_price") or 0),
                    "modal_price": float(r.get("modal_price") or 0),
                }
                for r in rows
            ],
        }

    # Output consolidated JSON
    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "latest_date": latest_date_overall,
        "commodities": all_data,
    }

    with open("mandi_latest.json", "w") as f:
        json.dump(output, f, indent=2)

    # Also output just the summary for quick reads
    summary = {
        "fetched_at": output["fetched_at"],
        "latest_date": latest_date_overall,
        "commodities": {k: {k2: v2 for k2, v2 in v.items() if k2 != "rows"} for k, v in all_data.items()},
    }
    with open("mandi_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"Fetched {len(all_data)} commodities for {latest_date_overall}")
    print("Written: mandi_latest.json, mandi_summary.json")

if __name__ == "__main__":
    main()