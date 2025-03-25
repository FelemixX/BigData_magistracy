import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

df_merge['Age_Normalized'] = df_merge.groupby('Pclass')['Age'].transform(lambda x: x - x.mean())

print(df_merge[['Pclass', 'Age', 'Age_Normalized']].head(10))