import pandas as pd

df = pd.read_csv("titanic/test.csv")

df["Name"] = df["Name"].apply(lambda x: x.upper())

print(df.values)
