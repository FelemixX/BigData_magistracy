import pandas as pd

df = pd.read_csv("titanic/test.csv")

filtered_df = df[df["Age"] > 30].copy()

filtered_df["Age_in_Days"] = filtered_df["Age"] * 365

filtered_df.to_csv("titanic/filtered_data.csv", index=False)

print("Данные сохранены")