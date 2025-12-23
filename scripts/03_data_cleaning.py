import pandas as pd
import os

df = pd.read_csv("../data_raw/202401-divvy-tripdata.csv")

# Convert datetime columns
df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

# Create ride length in minutes
df["ride_length"] = (df["ended_at"] - df["started_at"]).dt.total_seconds() / 60

# Remove negative or zero rides
df = df[df["ride_length"] > 0]

# Create day of week
df["day_of_week"] = df["started_at"].dt.day_name()

# Drop rows with missing member type
df = df.dropna(subset=["member_casual"])

# Save cleaned data
df.to_csv("../data_cleaned/cleaned_data.csv", index=False)

print("Cleaning completed!")
