import pandas as pd

df = pd.read_csv("../data_cleaned/cleaned_data.csv")

# Average ride length by user type
avg_ride = df.groupby("member_casual")["ride_length"].mean()
print(avg_ride)

# Rides by day of week
rides_by_day = df.groupby(["member_casual", "day_of_week"]).size()
print(rides_by_day)