import pandas as pd

df = pd.read_csv("titanic/test.csv")

df["Age_in_Days"] = df["Age"] * 365 # возраст в днях
df["Age_in_Days"] = df["Age"].fillna(0) * 365 # избавиться от NaN

print(df)