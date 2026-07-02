import esankhyiki
import sys
import pprint

sys.stdout.reconfigure(encoding='utf-8')

print("--- Testing CPI latest records (limit=500) ---")
try:
    cpi_data = esankhyiki.get_data("CPI", {
        "base_year": "2012",
        "series": "Current",
        "group_code": "0",
        "sector_code": 3,
        "state_code": 99,
        "limit": 500
    })
    print("Length of CPI:", len(cpi_data))
    # Print the first 5 records (should be the newest from API)
    print("Newest CPI records:")
    pprint.pprint(cpi_data[:5])
except Exception as e:
    print("Error:", e)

print("\n--- Testing RBI USD/INR latest records (limit=500) ---")
try:
    ex_data = esankhyiki.get_data("RBI", {
        "indicator_code": 33,
        "reference_rate_code": 1,
        "currency_code": 5,
        "limit": 500
    })
    print("Length of USD/INR:", len(ex_data))
    print("Newest USD/INR records:")
    pprint.pprint(ex_data[:5])
except Exception as e:
    print("Error:", e)

print("\n--- Testing RBI Forex latest records (limit=500) ---")
try:
    fx_data = esankhyiki.get_data("RBI", {
        "indicator_code": 47,
        "foreign_exchange_reserve_currency_code": 2,
        "foreign_exchange_reserve_type_code": 5,
        "limit": 500
    })
    print("Length of Forex:", len(fx_data))
    print("Newest Forex records:")
    pprint.pprint(fx_data[:5])
except Exception as e:
    print("Error:", e)
