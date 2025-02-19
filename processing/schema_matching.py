import pandas as pd


tableA = pd.read_csv("output/tableA.csv")
tableB = pd.read_csv("output/tableB.csv")

# Print schema of each table
# print("\n🔹 Schema of Table A:")
# print(tableA.dtypes)

# print("\n🔹 Schema of Table B:")
# print(tableB.dtypes)

# # Identify common and extra attributes
# common_columns = list(set(tableA.columns) & set(tableB.columns))
# extra_in_A = list(set(tableA.columns) - set(tableB.columns))
# extra_in_B = list(set(tableB.columns) - set(tableA.columns))

# # Display schema comparison
# print("\nCommon Attributes (Same in Both Tables):", common_columns)
# print("❌ Extra Attributes in Table A (Missing in Table B):", extra_in_A)
# print("❌ Extra Attributes in Table B (Missing in Table A):", extra_in_B)



# Print initial column names
# print("\nInitial Schema of Table A:", list(tableA.columns))
# print("Initial Schema of Table B:", list(tableB.columns))

# # Rename mismatched columns in Table B
# rename_map = {
#     "Cost": "Price",
#     "Stars": "Rating",
#     "Availability": "Stock"
# }
# tableB.rename(columns=rename_map, inplace=True)

# # Ensure both tables have the same columns
# all_columns = set(tableA.columns).union(set(tableB.columns))

# # Add missing "Author" column to Table A
# if "Author" not in tableA.columns:
#     tableA["Author"] = None  # Add empty "Author" column

# # Merge "Author" from Table B into Table A (based on 'ID' & 'Title')
# merged_table = tableA.merge(
#     tableB[['ID', 'Title', 'Author']],  # Only merge "Author"
#     on=['ID', 'Title'], 
#     how='left'
# ).copy()  # Copy to avoid chained assignment issues

# # Fill missing values properly
# merged_table["Author_x"] = merged_table["Author_x"].combine_first(merged_table["Author_y"])

# # Rename the merged column correctly
# merged_table.rename(columns={"Author_x": "Author"}, inplace=True)

# # Drop extra columns ("Author_y" and "ISBN")
# merged_table.drop(columns=["Author_y", "ISBN"], inplace=True, errors="ignore")

# # Save cleaned tables
# merged_table.to_csv("output/clean_tableA.csv", index=False)
# tableB.to_csv("output/clean_tableB.csv", index=False)

# # Print updated schema
# print("\nSchema updated! Cleaned tables saved as clean_tableA.csv & clean_tableB.csv")
# print("Updated Schema of Table A:", list(merged_table.columns))




# Print sample rows for debugging
print("\nSample Rows from Table A:")
print(tableA.head())

print("\nSample Rows from Table B:")
print(tableB.head())

# Check how many IDs match
matching_ids = tableA["ID"].isin(tableB["ID"]).sum()
print(f"\nMatching IDs between tables: {matching_ids} out of {len(tableA)}")

# Check how many Titles match
matching_titles = tableA["Title"].isin(tableB["Title"]).sum()
print(f"Matching Titles between tables: {matching_titles} out of {len(tableA)}")
