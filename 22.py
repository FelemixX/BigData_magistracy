import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

filtered_df = df_merge.groupby('Pclass').filter(lambda x: x['Age'].mean() > 30)

print("\nУникальные значения Pclass после фильтрации:", filtered_df['Pclass'].unique())