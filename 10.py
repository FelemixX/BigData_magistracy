import pandas as pd

df1 = pd.read_csv("titanic/test.csv")
df2 = pd.read_csv("titanic/gender_submission.csv")

# вертикальное объединение
df_concat = pd.concat([df1, df2], ignore_index=True)

# горизонтальное объединение
df_merge = pd.merge(df1, df2, on="PassengerId", how="inner")

print("\nГоризонтальное объединение (merge):")
print(df_merge.values)

print("\nВертикальное объединение (concat):")
print(df_concat.values)
