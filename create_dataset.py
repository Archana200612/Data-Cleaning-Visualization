
import pandas as pd
import numpy as np

np.random.seed(42)

# Generate sample retail sales data
n = 1000

data = {
    "Transaction_ID": range(1, n + 1),
    "Product": np.random.choice(
        ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"],
        n
    ),
    "Category": np.random.choice(
        ["Electronics", "Accessories"],
        n
    ),
    "Quantity": np.random.randint(1, 10, n),
    "Unit_Price": np.random.randint(100, 50000, n),
    "Customer_Age": np.random.randint(18, 65, n),
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        n
    )
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Introduce some missing values for cleaning practice
df.loc[10:20, "Customer_Age"] = np.nan
df.loc[30:35, "Region"] = np.nan

# Introduce duplicate records
df = pd.concat([df, df.iloc[:5]], ignore_index=True)

df.to_csv("data.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print("Saved as: data.csv")
