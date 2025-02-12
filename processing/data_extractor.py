from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# Create output directory
os.makedirs("output", exist_ok=True)

### 📘 Extract BooksToScrape Data
def extract_books_to_scrape():
    """Extract book details from BooksToScrape HTML files."""
    data = []

    for file in os.listdir("extracted_data/books_html"):
        with open(f"extracted_data/books_html/{file}", "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.strip()
            rating = book.p["class"][1]
            stock = "In stock" if "In stock" in book.select_one(".instock.availability").text else "Out of stock"

            data.append([
                f"book_{len(data)+1}",  # Unique ID
                title,
                price,
                rating,
                stock
            ])

    df = pd.DataFrame(data, columns=["ID", "Title", "Price", "Rating", "Stock"])
    df.to_csv("output/tableA.csv", index=False)
    print("✅ BooksToScrape data saved in tableA.csv")

extract_books_to_scrape()

### 📙 Extract Open Library Data
def extract_open_library():
    """Extract book details from Open Library JSON."""
    with open("extracted_data/openlibrary_html/books.json", "r", encoding="utf-8") as f:
        books = json.load(f)["docs"]

    data = []
    for i, book in enumerate(books[:100]):  # Limit to 100 books
        title = book.get("title", "")
        author = book.get("author_name", ["Unknown"])[0]
        isbn = book.get("isbn", ["N/A"])[0]

        data.append([
            f"openlib_{i+1}",  # Unique ID
            title,
            author,
            isbn
        ])

    df = pd.DataFrame(data, columns=["ID", "Title", "Author", "ISBN"])
    df.to_csv("output/tableB.csv", index=False)
    print("✅ Open Library data saved in tableB.csv")

extract_open_library()
