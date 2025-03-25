import pandas as pd

df = pd.read_csv("titanic/test.csv")

print("Размер DataFrame (строки, столбцы):", df.shape)
print("\nНазвания столбцов:", df.columns.tolist())
print("\nТипы данных в столбцов:\n", df.dtypes)
