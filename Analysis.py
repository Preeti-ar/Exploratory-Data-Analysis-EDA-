
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(BASE / "sales_eda_dataset.csv")

print("DATASET OVERVIEW")
print("Shape:", df.shape)
print("\nFirst five rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean the data
df = df.drop_duplicates().copy()
df["city"] = df["city"].fillna("Unknown")
df["discount_percent"] = df["discount_percent"].fillna(
    df["discount_percent"].median()
)

# Calculate revenue after discount
df["revenue"] = (
    df["units_sold"]
    * df["unit_price"]
    * (1 - df["discount_percent"])
)

# Statistical summary
print("\nDESCRIPTIVE STATISTICS")
print(df.describe(numeric_only=True))

print("\nREVENUE BY PRODUCT")
print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))

print("\nREVENUE BY CITY")
print(df.groupby("city")["revenue"].sum().sort_values(ascending=False))

# Save cleaned data
df.to_csv(OUT / "cleaned_sales_data.csv", index=False)
df.describe(include="all").to_csv(
    OUT / "descriptive_statistics.csv"
)

# Graph 1: Revenue by product
df.groupby("product")["revenue"].sum().plot(
    kind="bar", title="Revenue by Product"
)
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_product.png")
plt.close()

# Graph 2: Revenue by city
df.groupby("city")["revenue"].sum().plot(
    kind="bar", title="Revenue by City"
)
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_city.png")
plt.close()

# Graph 3: Correlation matrix
numeric = df[
    ["units_sold", "unit_price", "discount_percent", "revenue"]
]
correlation = numeric.corr()

plt.figure(figsize=(7, 5))
plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=45, ha="right")
plt.yticks(range(len(correlation.index)), correlation.index)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(OUT / "correlation_matrix.png")
plt.close()

print("\nEDA complete. Check the outputs folder.")
