import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")


grouped_df = df_merge.groupby(['Pclass', 'Sex']).agg({
    'Age': 'mean',   # Средний возраст
    'Fare': 'sum',   # Сумма стоимости билетов
    'Survived': 'mean'  # Доля выживших (среднее по 0 и 1)
})

print(grouped_df)