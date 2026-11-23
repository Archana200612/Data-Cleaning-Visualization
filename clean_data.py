
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Create Visualizations Directory
# -----------------------------------

OUTPUT_DIR = "visualizations"

if os.path.isfile(OUTPUT_DIR):
    os.rename(OUTPUT_DIR, "visualizations_old")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Visualization folder is ready!")

# -----------------------------------
# 2. Load Dataset
# -----------------------------------

DATA_FILE = "data.csv"  # Change this to your actual CSV filename

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(
        f"Dataset '{DATA_FILE}' not found. "
        "Place your CSV file in the project folder."
    )

df = pd.read_csv(DATA_FILE)

print("\nDataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------
# 3. Dataset Information
# -----------------------------------

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------
# 4. Remove Duplicate Records
# -----------------------------------

df = df.drop_duplicates()

# -----------------------------------
# 5. Handle Missing Values
# -----------------------------------

for column in df.columns:

    if df[column].isnull().sum() > 0:

        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())

        else:
            mode_values = df[column].mode()

            if not mode_values.empty:
                df[column] = df[column].fillna(mode_values[0])

print("\nMissing values handled successfully!")

# -----------------------------------
# 6. Save Cleaned Dataset
# -----------------------------------

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

# -----------------------------------
# 7. Generate Visualizations
# -----------------------------------

numeric_df = df.select_dtypes(include=np.number)

if not numeric_df.empty:

    # Histogram
    numeric_df.hist(figsize=(12, 8), bins=20)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "histograms.png"))
    plt.close()

    # Correlation Heatmap
    if numeric_df.shape[1] >= 2:
        plt.figure(figsize=(10, 6))
        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
        plt.close()

    # Boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=numeric_df)
    plt.xticks(rotation=45)
    plt.title("Outlier Detection")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "boxplot.png"))
    plt.close()

else:
    print("No numeric columns available for visualization.")

# -----------------------------------
# 8. Final Summary
# -----------------------------------

print("\n========== PROJECT SUMMARY ==========")
print("Original data processing completed.")
print("Duplicate records removed.")
print("Missing values handled.")
print("Cleaned dataset saved.")
print("Visualizations generated.")
print("=====================================")
