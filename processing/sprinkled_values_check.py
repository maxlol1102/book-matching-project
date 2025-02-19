import pandas as pd
import re

tableA = pd.read_csv("output/clean_tableA.csv", encoding="utf-8")

# ---------- CHECK FOR MISSING OR "UNKNOWN" AUTHORS ----------
missing_authors = tableA[tableA["Author"].isna() | (tableA["Author"].str.lower() == "unknown")]

# ---------- CHECK FOR INCONSISTENT AUTHOR FORMATS ----------
def check_author_format(author):
    """Detect if author names have inconsistent formats (Last, First vs. First Last)."""
    if re.match(r"^[A-Z][a-z]+, [A-Z][a-z]+$", str(author)): 
        return "Last, First format detected"
    return None

tableA["Author Format Issue"] = tableA["Author"].apply(lambda x: check_author_format(x))
author_format_issues = tableA[tableA["Author Format Issue"].notna()]

# ---------- CHECK FOR MULTIPLE AUTHOR VARIATIONS ----------
multiple_authors = tableA[tableA["Author"].str.contains(r"&|;", na=False)] 

# ---------- CHECK FOR EXTRA NON-AUTHOR INFO ----------
def check_non_author_text(author):
    """Detect if author contains extra information like 'Dr.', 'PhD'."""
    if re.search(r"Dr\.|PhD|Prof\.|Sir", str(author)):  
        return "Non-author info detected"
    return None

tableA["Non-Author Info"] = tableA["Author"].apply(lambda x: check_non_author_text(x))
non_author_info_issues = tableA[tableA["Non-Author Info"].notna()]

# ---------- CHECK FOR WEIRD SYMBOLS ----------
def check_encoding_issues(text):
    if re.search(r"[âÂÃ�]", str(text)):  # Common encoding error symbols
        return "Encoding issue detected"
    return None

tableA["Encoding Issue"] = tableA["Author"].apply(lambda x: check_encoding_issues(x))
encoding_issues = tableA[tableA["Encoding Issue"].notna()]

# Print results
print("\nData Quality Issues in `Author` Attribute:")

if not missing_authors.empty:
    print(f"\n{len(missing_authors)} books have missing or 'Unknown' authors:")
    print(missing_authors[["Title", "Author"]].head())

if not author_format_issues.empty:
    print(f"\n{len(author_format_issues)} authors found with inconsistent `Last, First` format:")
    print(author_format_issues[["Author"]].head())

if not multiple_authors.empty:
    print(f"\n{len(multiple_authors)} books have multiple authors with inconsistent delimiters:")
    print(multiple_authors[["Title", "Author"]].head())

if not non_author_info_issues.empty:
    print(f"\n{len(non_author_info_issues)} authors contain non-author information (Dr., PhD, etc.):")
    print(non_author_info_issues[["Author"]].head())

if not encoding_issues.empty:
    print(f"\n{len(encoding_issues)} books contain weird symbols (encoding issues):")
    print(encoding_issues[["Title", "Author"]].head())

if missing_authors.empty and author_format_issues.empty and multiple_authors.empty and non_author_info_issues.empty and encoding_issues.empty:
    print("\nNo additional data quality issues found.")

print("\nAuthor attribute verification completed.")
