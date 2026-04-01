import requests
from bs4 import BeautifulSoup
import json

def scrape_yc():
    base_url = "https://www.ycombinator.com/companies"
    companies = []

    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.find_all("a")

        for card in cards:
            try:
                name = card.text.strip()
                if name:
                    companies.append({
                        "name": name,
                        "description": "N/A"
                    })
            except Exception:
                continue

        # Save raw data
        with open("data/raw.json", "w") as f:
            json.dump(companies, f, indent=4)

    except Exception as e:
        print("Error:", e)

    return companies