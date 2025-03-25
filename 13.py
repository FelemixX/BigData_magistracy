import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

pivot_table = df_merge.pivot_table(values="Fare", index="Sex", columns="Survived", aggfunc="mean") # распределение выживших по полу

print(pivot_table.fillna(0))