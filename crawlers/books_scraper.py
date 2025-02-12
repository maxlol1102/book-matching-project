import requests
from bs4 import BeautifulSoup
import os
import time

# Create directory to store HTML files
os.makedirs("extracted_data/books_html", exist_ok=True)

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_books_data():
    """Scrape book data from BooksToScrape"""
    for page in range(1, 6):  # Scrape first 5 pages (adjust as needed)
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            with open(f"extracted_data/books_html/page_{page}.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"✅ Page {page} saved successfully!")
        else:
            print(f"❌ Failed to fetch {url}")
        
        time.sleep(2)  # Delay to avoid rate limiting

fetch_books_data()
