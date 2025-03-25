import pandas as pd

df = pd.read_csv("titanic/gender_submission.csv")

df_concat = pd.concat([df, df], ignore_index=True)

df_no_duplicates = df_concat.drop_duplicates()

print("Размер изначального (строки, столбцы):", df_concat.shape)
print("Размер очищенного (строки, столбцы):", df_no_duplicates.shape)