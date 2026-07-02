import esankhyiki
import sys
import pprint

sys.stdout.reconfigure(encoding='utf-8')

try:
    print("--- NAS Annual GDP Growth Rate ---")
    data = esankhyiki.get_data("NAS", {
        "indicator_code": 22,
        "frequency_code": 1,
        "base_year": "2011-12",
        "series": "Current",
        "approach_code": 2,
        "revision_code": 3
    })
    print("Length of annual GDP growth:", len(data))
    if len(data) > 0:
        pprint.pprint(data[:5])
except Exception as e:
    print("Error:", e)
