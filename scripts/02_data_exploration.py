import pandas as pd

df = pd.read_csv("../data_raw/202401-divvy-tripdata.csv")

print(df.columns)
print(df.info())
print(df.isnull().sum())