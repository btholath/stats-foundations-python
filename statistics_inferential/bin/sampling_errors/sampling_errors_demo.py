import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/input/customers.csv")

# -------------------------------
# 1️⃣ Population-Specific Error
# -------------------------------
# Mistakenly assuming the dataset represents all age groups
young_only = df[df['Age'] < 30]

plt.figure(figsize=(6,4))
sns.histplot(df['Age'], kde=True, label='Full Population', color='blue')
sns.histplot(young_only['Age'], kde=True, label='Biased Subset', color='red')
plt.title("Population-Specific Error: Age Bias")
plt.legend()
plt.show()

# -------------------------------
# 2️⃣ Selection Error
# -------------------------------
# Selecting only customers from one region
selected = df[df['Region'] == 'North']

print("\nSelection Error: Only 'North' region selected")
print("Region distribution:\n", selected['Region'].value_counts())

# -------------------------------
# 3️⃣ Non-Response Error
# -------------------------------
# Simulate missing responses in 'Subscribed' column
df['Subscribed'] = df['Subscribed'].replace(np.random.choice(df['Subscribed'], size=100), np.nan)
non_response_rate = df['Subscribed'].isna().mean()

print(f"\nNon-Response Error: {non_response_rate:.2%} of responses missing in 'Subscribed'")

# -------------------------------
# 4️⃣ Sample Error
# -------------------------------
# Draw a small random sample and compare income mean
sample = df.sample(n=50, random_state=42)
population_mean = df['Income'].mean()
sample_mean = sample['Income'].mean()

print(f"\nSample Error: Population mean income = {population_mean:.2f}, Sample mean = {sample_mean:.2f}")

# -------------------------------
# 5️⃣ Sample Frame Error
# -------------------------------
# Frame includes only online customers, missing offline ones
frame_error = df[df['Website'].notna()]  # Assuming 'Website' implies online presence

print(f"\nSample Frame Error: Frame size = {len(frame_error)}, Total population = {len(df)}")


"""
Summary Table
Error Type	            Cause	                            Python Illustration
Population-Specific	    Misrepresenting target group	    Age filter bias
Selection Error	        Biased inclusion criteria	        Region filter
Non-Response Error	    Missing data from participants	    NaNs in 'Subscribed'
Sample Error	        Random variation in small sample	Mean comparison
Sample Frame Error	    Incomplete sampling frame	        Online-only filter


✅ What You’ve Demonstrated
1️⃣ Selection Error
You filtered only 'North' region customers.
✅ Output confirms: 247 records, all from 'North'.
📊 Suggestion: Visualize region distribution before and after selection to show imbalance.

2️⃣ Non-Response Error
You replaced 100 values in 'Subscribed' with np.nan.
⚠️ But the result shows 100% missing—likely because np.random.choice(df['Subscribed'], size=100) sampled only existing values, and then replaced all of them.
🔧 Fix: Use .sample() instead to target specific rows:
df.loc[df.sample(n=100, random_state=42).index, 'Subscribed'] = np.nan

3️⃣ Sample Error
You compared population vs. sample mean income.
✅ Sample mean is slightly higher—great illustration of sampling variability.
📊 Suggestion: Run multiple samples and plot distribution of sample means to show sampling error range.

4️⃣ Sample Frame Error
You filtered customers with a 'Website' entry.

✅ Frame size = 789, Total = 1000 → 21.1% excluded.
📊 Suggestion: Show how excluding offline customers could bias digital engagement metrics.
"""
