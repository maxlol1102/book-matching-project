import pandas as pd
import re  

tableA = pd.read_csv("output/clean_tableA.csv")

# Clean "Price" 
if "Price" in tableA.columns:
    tableA["Price"] = tableA["Price"].astype(str).apply(lambda x: re.sub(r"[^\d.]", "", x))  
    tableA["Price"] = pd.to_numeric(tableA["Price"], errors="coerce")  

attribute_types = {}

# Classify 
for col in tableA.columns:
    if pd.api.types.is_numeric_dtype(tableA[col]):  # Check if it's numeric
        attribute_types[col] = "Numeric"
    elif tableA[col].nunique() < 10:  # If it has few unique values, it's categorical
        attribute_types[col] = "Categorical"
    elif tableA[col].dtype == "object":  # If it's a string, it's textual
        attribute_types[col] = "Textual"
    else:
        attribute_types[col] = "Unknown"

# Convert to DataFrame
attribute_types_df = pd.DataFrame(attribute_types.items(), columns=["Attribute", "Type"])

# Print and save
print("\n Attribute Classification:\n", attribute_types_df)
attribute_types_df.to_csv("output/attribute_classification.csv", index=False)

# Save cleaned table
tableA.to_csv("output/clean_tableA.csv", index=False)

print("\nAttribute classification report saved.")


# ---------- TEXT LENGTH ANALYSIS ----------
# Select only textual attributes
textual_columns = [col for col, dtype in attribute_types.items() if dtype == "Textual"]

# Compute text length report in table format
text_length_report = {}

for col in textual_columns:
    tableA[col] = tableA[col].astype(str)  # Ensure text format
    text_length_report[col] = {
        "Min Length": tableA[col].str.len().min(),
        "Max Length": tableA[col].str.len().max(),
        "Avg Length": round(tableA[col].str.len().mean(), 2)
    }

# Convert dictionary to DataFrame
text_length_df = pd.DataFrame.from_dict(text_length_report, orient="index")

# Print formatted text length table
print("\nText Attribute Length Report:\n", text_length_df.to_string())

print("\nText length analysis completed.")