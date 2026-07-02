import requests
import json

def test_connection():
    print("Testing connection to https://mcp.mospi.gov.in...")
    try:
        # Fetch root or SSE info
        r = requests.get("https://mcp.mospi.gov.in", timeout=10)
        print(f"Status Code: {r.status_code}")
        print("Response Headers:")
        for k, v in r.headers.items():
            print(f"  {k}: {v}")
        
        # FastMCP / HTTP servers might serve tools list under /tools or /mcp/tools
        print("\nTesting tools/list POST request...")
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "list_datasets",
                "arguments": {}
            }
        }
        r_tools = requests.post("https://mcp.mospi.gov.in/", headers=headers, json=payload, timeout=10)
        print(f"POST tools/call list_datasets Status: {r_tools.status_code}")
        with open("datasets.txt", "w", encoding="utf-8") as f:
            f.write(r_tools.text)
        print("Successfully saved raw list_datasets output to datasets.txt!")
            
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
