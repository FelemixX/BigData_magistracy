import pandas as pd

df = pd.read_csv("titanic/test.csv")

sorted_df = df.sort_values(by="Fare", ascending=False)

print(sorted_df)
