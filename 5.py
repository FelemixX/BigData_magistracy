import pandas as pd

df = pd.read_csv("titanic.csv")

selected_columns = df[["Name", "Age"]]

rows_count = 5

print(selected_columns.head(n=rows_count))
