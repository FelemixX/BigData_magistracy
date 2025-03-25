import pandas as pd

df = pd.read_csv("titanic/test.csv")

df = df.set_index("Name")

print("DataFrame с новым индексом:")
print(df)

df_reset = df.reset_index()

print("\nDataFrame после сброса индекса:")
print(df_reset)