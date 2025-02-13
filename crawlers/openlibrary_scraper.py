import requests
import os
import time

# Create directory for storing Open Library HTML files
os.makedirs("extracted_data/openlibrary_html", exist_ok=True)

BASE_URL = "https://openlibrary.org/search?q=python&page={}"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_openlibrary_pages():
    """Scrape Open Library search result pages and save as HTML files."""
    for page in range(1, 11):  # Fetch first 10 pages
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            with open(f"extracted_data/openlibrary_html/page_{page}.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"✅ Page {page} saved successfully!")
        else:
            print(f"❌ Failed to fetch {url}")
        
        time.sleep(2)  # Avoid getting blocked

fetch_openlibrary_pages()
