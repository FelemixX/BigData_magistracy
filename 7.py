import pandas as pd

df = pd.read_csv("titanic/test.csv")

mean_fare_by_sex = df.groupby("Sex")["Fare"].mean()

print(mean_fare_by_sex)
