import esankhyiki
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    print("--- IIP get_data with invalid param to trigger error ---")
    data = esankhyiki.get_data("IIP", {
        "base_year": "2011-12",
        "frequency": "Monthly",
        "category_code": 4,
        "invalid_param_xyz": 123
    })
    
except Exception as e:
    print("Error getting IIP data:", e)
