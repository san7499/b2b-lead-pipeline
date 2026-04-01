import requests
from bs4 import BeautifulSoup
import json
import os


def scrape_books():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    base_url = "https://books.toscrape.com/catalogue/"

    books = []

    try:
        for page in range(1, 6):  # scrape 5 pages
            page_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, "html.parser")

            items = soup.find_all("article", class_="product_pod")

            for item in items:
                name = item.h3.a["title"]
                price = item.find("p", class_="price_color").text

                books.append({
                    "name": name,
                    "description": price
                })

        # Save data
        os.makedirs("data", exist_ok=True)

        with open("data/raw.json", "w", encoding="utf-8") as f:
            json.dump(books, f, indent=4)

        print(f"✅ Scraped {len(books)} books successfully")

        return books

    except Exception as e:
        print("❌ Error:", e)
        return []


if __name__ == "__main__":
    scrape_books()