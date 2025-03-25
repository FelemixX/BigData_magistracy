import pandas as pd

df = pd.read_csv("titanic/test.csv")

print("Пропущенные значения:\n", df.isnull().sum())

# если надо заполнить конкретный столбец
# df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df.fillna(df.mean(numeric_only=True), inplace=True) # заполнить средним значением

# df.fillna(df.median(numeric_only=True), inplace=True) # заполнить медианным значением


print("\nПропущенные значения после заполнения:\n", df.isnull().sum())
