import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

unique_ages_per_sex = df_merge.groupby('Sex')['Age'].nunique()

print(unique_ages_per_sex)