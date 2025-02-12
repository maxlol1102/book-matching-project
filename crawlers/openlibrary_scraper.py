import requests
import os
import json
import time

# Create directory to store Open Library data
os.makedirs("extracted_data/openlibrary_html", exist_ok=True)

API_URL = "https://openlibrary.org/search.json?q=python&limit=50"

def fetch_openlibrary_data():
    """Fetch book data from Open Library API."""
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        with open("extracted_data/openlibrary_html/books.json", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("✅ Open Library data saved successfully!")
    else:
        print("❌ Failed to fetch Open Library data")

fetch_openlibrary_data()
