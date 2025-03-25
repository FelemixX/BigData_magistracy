import pandas as pd

df = pd.read_csv("titanic/test.csv")

print(df.shape)

filtered_df = df[df["Name"].str.contains("James", case=False, na=False)]

print(filtered_df.shape)

# print(filtered_df)

