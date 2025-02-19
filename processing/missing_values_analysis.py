import pandas as pd
tableA = pd.read_csv("output/clean_tableA.csv")
# Define 
missing_report = {}

# Loop 
for col in tableA.columns:
    missing_count = tableA[col].isnull().sum()
    
   
    if col == "Author":
        missing_count += (tableA[col] == "Unknown").sum()
    
    missing_fraction = missing_count / len(tableA)
    missing_percentage = missing_fraction * 100

    # Store results
    missing_report[col] = {
        "Missing Count": missing_count,
        "Missing Fraction": f"{missing_fraction:.2f}",
        "Missing Percentage": f"{missing_percentage:.2f}%"
    }

# Convert 
missing_values_df = pd.DataFrame.from_dict(missing_report, orient="index")

# Save report
print("\nMissing Values Report:\n", missing_values_df)
missing_values_df.to_csv("output/missing_values_report.csv")

print("\nMissing values report saved.")
