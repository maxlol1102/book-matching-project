import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tableA = pd.read_csv("output/clean_tableA.csv")

# -------- HISTOGRAMS FOR NUMERIC ATTRIBUTES --------
numeric_columns = ["Price", "Rating"]

for col in numeric_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(tableA[col].dropna(), bins=20, kde=True)  
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig(f"output/histogram_{col}.png")  
    plt.show()

print("\n✅ Histograms generated for numeric attributes (`Price`, `Rating`).")

# -------- HISTOGRAM FOR TEXT LENGTH (Title) --------
tableA["Title Length"] = tableA["Title"].astype(str).str.len()


plt.figure(figsize=(8, 5))
sns.histplot(tableA["Title Length"], bins=20, kde=True)
plt.title("Histogram of Title Length")
plt.xlabel("Title Length (Characters)")
plt.ylabel("Frequency")
plt.savefig("output/histogram_title_length.png") 
plt.show()

print("\n✅ Histogram generated for `Title Length`.")
