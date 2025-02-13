from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import shutil

# Create output directory
os.makedirs("output", exist_ok=True)

### 📘 Extract BooksToScrape Data
def extract_books_to_scrape():
    """Extract book details from BooksToScrape HTML files and ensure 1,000 rows."""
    data = []

    for file in sorted(os.listdir("extracted_data/books_html")):  # Sort to maintain order
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

            if len(data) >= 1000:  # Stop when we reach 1,000 books
                break

        if len(data) >= 1000:
            break

    df = pd.DataFrame(data, columns=["ID", "Title", "Price", "Rating", "Stock"])
    df.to_csv("output/tableA.csv", index=False)
    print(f"✅ BooksToScrape data saved in tableA.csv ({len(df)} rows)")

extract_books_to_scrape()

### 📙 Extract Open Library Data
def extract_open_library():
    """Extract book details from Open Library JSON and ensure 1,000 rows."""
    with open("extracted_data/openlibrary_html/books.json", "r", encoding="utf-8") as f:
        books = json.load(f)["docs"]

    data = []
    for i, book in enumerate(books[:1000]):  # Limit to 1,000 books
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
    print(f"✅ Open Library data saved in tableB.csv ({len(df)} rows)")

extract_open_library()



### 📦 ZIP HTML Files
def zip_html_files():
    """Compress extracted HTML files into ZIP archives."""
    books_html_folder = "extracted_data/books_html"
    openlibrary_html_folder = "extracted_data/openlibrary_html"

    books_zip = "output/books_data.zip"
    openlibrary_zip = "output/openlibrary_data.zip"

    if os.path.exists(books_html_folder):
        shutil.make_archive("output/books_data", 'zip', books_html_folder)
        print("✅ BooksToScrape HTML pages compressed into books_data.zip")
    else:
        print("❌ No BooksToScrape HTML folder found!")

    if os.path.exists(openlibrary_html_folder):
        shutil.make_archive("output/openlibrary_data", 'zip', openlibrary_html_folder)
        print("✅ Open Library HTML pages compressed into openlibrary_data.zip")
    else:
        print("❌ No Open Library HTML folder found!")

zip_html_files()