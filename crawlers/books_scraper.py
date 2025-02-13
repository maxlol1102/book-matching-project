import requests
from bs4 import BeautifulSoup
import os
import time


os.makedirs("extracted_data/books_html", exist_ok=True)

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_books_data():
    """Scrape at least 1,000 books from BooksToScrape"""
    book_count = 0
    for page in range(1, 51): 
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            with open(f"extracted_data/books_html/page_{page}.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"✅ Page {page} saved successfully!")
            
            # Count books
            soup = BeautifulSoup(response.text, "html.parser")
            book_count += len(soup.select("article.product_pod"))
            
            if book_count >= 1000:
                print(f"✅ Collected {book_count} books, stopping crawl.")
                break

        else:
            print(f"❌ Failed to fetch {url}")
        
        time.sleep(2)  # Avoid limiting

fetch_books_data()
