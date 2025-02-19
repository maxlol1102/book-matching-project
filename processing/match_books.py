import pandas as pd
import requests
import time

# Load BooksToScrape Data (Table A)
tableA = pd.read_csv("output/tableA.csv")

# OpenLibrary API base URL
OPENLIBRARY_SEARCH_URL = "https://openlibrary.org/search.json?q={}"

# Function to search for a book in OpenLibrary
def search_openlibrary(title):
    """Searches OpenLibrary for a book title and returns the best match."""
    try:
        response = requests.get(OPENLIBRARY_SEARCH_URL.format(title), timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data["numFound"] > 0:
                return data["docs"][0].get("author_name", ["Unknown"])[0]  # Get the first author found
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data for '{title}': {e}")
    return "Unknown"

# Add an "Author" column to Table A
if "Author" not in tableA.columns:
    tableA["Author"] = None

# Search OpenLibrary for each book title
for index, row in tableA.iterrows():
    if pd.isna(row["Author"]):  # Only search if the author is missing
        author_name = search_openlibrary(row["Title"])
        tableA.at[index, "Author"] = author_name
        print(f"✅ Matched: {row['Title']} → {author_name}")
        time.sleep(1)  # Sleep to avoid API rate limits

# Save updated table
tableA.to_csv("output/clean_tableA.csv", index=False)
print("\n✅ Updated clean_tableA.csv with matched authors from OpenLibrary.")
