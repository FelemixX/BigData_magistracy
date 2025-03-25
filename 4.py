import pandas as pd

df = pd.read_csv("titanic/test.csv")

desired_age = 50
filtered_df = df[df["Age"] > desired_age]

print(filtered_df)
