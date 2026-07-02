import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_rbi_rates():
    url = "https://www.rbi.org.in/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    rates = {}
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for table in soup.find_all("table"):
                text = table.get_text()
                # Use regex to find rate names followed by colons and percentage values
                # We normalize the text spaces first
                normalized_text = re.sub(r'\s+', ' ', text)
                
                # Ratios & Rates names
                pattern = r"(Policy Repo Rate|Standing Deposit Facility Rate|Marginal Standing Facility Rate|Bank Rate|Fixed Reverse Repo Rate|CRR|SLR)\s*:\s*([\d\.]+\%)"
                matches = re.findall(pattern, normalized_text)
                for key, val in matches:
                    rates[key] = val
    except Exception as e:
        print(f"Error scraping RBI rates: {e}")
    return rates

if __name__ == '__main__':
    res = scrape_rbi_rates()
    print("Parsed rates:", res)
