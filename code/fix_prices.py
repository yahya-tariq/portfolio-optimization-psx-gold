import pandas as pd
import numpy as np

# Load the Excel file
file_path = "closingpricesdata.xlsx"
df_raw = pd.read_excel(file_path, sheet_name="Sheet1", header=None)

# Define stock names manually based on column positions
stock_names = ["INDUS", "PKGS", "KTML", "NESTLE", "MUREB"]
data = []

# Loop over each stock's column pair: (date_col, price_col)
for i, stock in enumerate(stock_names):
    date_col = df_raw.iloc[1:, i * 2]       # skip header
    price_col = df_raw.iloc[1:, i * 2 + 1]

    # Clean and build individual DataFrame
    df_stock = pd.DataFrame({
        "Date": pd.to_datetime(date_col, errors='coerce'),
        "Closing Price": pd.to_numeric(price_col, errors='coerce'),
        "Stock": stock
    })

    # Drop rows with no date
    df_stock = df_stock[df_stock["Date"].notna()]
    data.append(df_stock)

# Combine all stocks into one tidy DataFrame
df = pd.concat(data)

# Pivot to get stocks as columns, dates as index
pivot_df = df.pivot(index="Date", columns="Stock", values="Closing Price").sort_index()

# Fill missing values with average of two above and two below
def fill_missing(series):
    for i in range(len(series)):
        if pd.isna(series.iloc[i]):
            above = series.iloc[max(0, i-2):i]
            below = series.iloc[i+1:i+3]
            series.iloc[i] = pd.concat([above, below]).mean()
    return series

pivot_df = pivot_df.apply(fill_missing)

# Save the cleaned, aligned dataset
output_file = "processed_closingpricesdata.xlsx"
pivot_df.to_excel(output_file)

print(f"✅ Done. Cleaned data saved to: {output_file}")
