import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

# Функция вычисляет разницу между max и min значением в группе
def range_agg(series):
    return series.max() - series.min()

age_range_per_class = df_merge.groupby('Pclass')['Age'].agg(range_agg)

print(age_range_per_class)