import pandas as pd

df = pd.read_csv("titanic/test.csv")

df["Sex"] = df["Sex"].astype("category")

category_counts = df["Sex"].value_counts()

print(category_counts)