import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===============================
# 1. LOAD DATA
# ===============================
df = pd.read_csv("../data_cleaned/cleaned_data.csv")

# Convert datetime safely
df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")

# Remove nulls just in case
df = df.dropna(subset=["started_at", "ride_length", "member_casual", "day_of_week"])

# Remove extreme outliers for clean visuals
df = df[df["ride_length"].between(1, 120)]

# ===============================
# 2. GLOBAL STYLE (MODERN LOOK)
# ===============================
sns.set_theme(
    style="white",
    palette="Set2",
    font_scale=1.2
)

plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titleweight"] = "bold"

# ===============================
# 3. VISUAL 1 — RIDE LENGTH COMPARISON
# ===============================
plt.figure()
sns.boxplot(
    data=df,
    x="member_casual",
    y="ride_length"
)
plt.title("Ride Length Comparison: Casual vs Members")
plt.xlabel("User Type")
plt.ylabel("Ride Length (Minutes)")
plt.tight_layout()
plt.show()

# ===============================
# 4. VISUAL 2 — AVERAGE RIDE LENGTH
# ===============================
avg_ride = (
    df.groupby("member_casual", as_index=False)["ride_length"]
    .mean()
)

plt.figure()
sns.barplot(
    data=avg_ride,
    x="member_casual",
    y="ride_length"
)
plt.title("Average Ride Length by User Type")
plt.xlabel("User Type")
plt.ylabel("Average Ride Length (Minutes)")
plt.tight_layout()
plt.show()

# ===============================
# 5. VISUAL 3 — WEEKLY USAGE PATTERN
# ===============================
day_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

plt.figure()
sns.countplot(
    data=df,
    x="day_of_week",
    hue="member_casual",
    order=day_order
)
plt.title("Weekly Ride Distribution by User Type")
plt.xlabel("Day of Week")
plt.ylabel("Number of Rides")
plt.legend(title="User Type")
plt.tight_layout()
plt.show()

# ===============================
# 6. VISUAL 4 — HOURLY BEHAVIOR (ADVANCED)
# ===============================
df["hour"] = df["started_at"].dt.hour

hourly_avg = (
    df.groupby(["hour", "member_casual"], as_index=False)["ride_length"]
    .mean()
)

plt.figure()
sns.lineplot(
    data=hourly_avg,
    x="hour",
    y="ride_length",
    hue="member_casual",
    marker="o"
)
plt.title("Average Ride Length by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Average Ride Length (Minutes)")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()