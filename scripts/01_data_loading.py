import pandas as pd
import os

# Path to raw data folder
data_path = "../data_raw"

# List all CSV files
files = [file for file in os.listdir(data_path) if file.endswith(".csv")]

# Read and combine all CSV files
df_list = []
for file in files:
    temp_df = pd.read_csv(os.path.join(data_path, file))
    df_list.append(temp_df)
df = pd.concat(df_list, ignore_index=True)
print("Dta loaded successfully!")
print(df.head())
print(df.shape)