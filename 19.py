import pandas as pd

data = {
    "Date": pd.date_range("2025-01-01", periods=10, freq="D"),
    "Value": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
}

df = pd.DataFrame(data)

df.set_index("Date", inplace=True)

df["Rolling_Mean_3"] = df["Value"].rolling(window=3).mean()

print(df)