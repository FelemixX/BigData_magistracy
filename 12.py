import pandas as pd

df = pd.DataFrame({
    "Date": ["2025-03-01", "2024-12-15", "2023-07-10"]
})

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

print(df)