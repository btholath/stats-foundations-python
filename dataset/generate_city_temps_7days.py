# city_temps_7days.py
import pandas as pd

# Construct symmetric 7-day sequences around 20 so that:
# - Sum = 140 -> Mean = 20
# - Middle (4th value when sorted) = 20 -> Median = 20

city_sequences = {
    "New York":      [20, 21, 19, 20, 21, 19, 20],  # symmetric with extra 20
    "Los Angeles":   [22, 23, 21, 18, 19, 17, 20],  # symmetric (±5, ±3, ±1, and 20)
    "Chicago":       [12, 11, 13, 20, 25, 29, 31],  # symmetric (±6, ±2, ±1, and 20)
}

rows = []
for city, temps in city_sequences.items():
    for day, temp in enumerate(temps, start=1):
        rows.append({"city": city, "day": day, "temperature": temp})

df = pd.DataFrame(rows, columns=["city", "day", "temperature"])

# Verify means and medians
summary = df.groupby("city")["temperature"].agg(mean="mean", median="median").round(2)

print(df)
print("\nVerification (per city):")
print(summary)

# Optional: save to CSV
df.to_csv("/workspaces/stats-foundations-python/dataset/city_temps_7days.csv", index=False)
print("\nSaved to city_temps_7days.csv")
