import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load realistic customer dataset
df = pd.read_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/input/customers.csv")

# -------------------------------
# 1️⃣ Population-Specific Error
# -------------------------------
# Mistakenly assuming dataset represents all age groups
young_only = df[df['Age'] < 30]

plt.figure(figsize=(8, 4))
sns.histplot(df['Age'], kde=True, color='blue', label='Full Population')
sns.histplot(young_only['Age'], kde=True, color='red', label='Biased Subset')
plt.title("Population-Specific Error: Age Distribution")
plt.xlabel("Age")
plt.legend()
plt.tight_layout()
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
# Randomly remove responses from 'Subscribed'
non_response_indices = df.sample(n=100, random_state=42).index
df.loc[non_response_indices, 'Subscribed'] = np.nan
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
# Frame includes only online customers (with a website)
frame_error = df[df['Website'].notna()]

print(f"\nSample Frame Error: Frame size = {len(frame_error)}, Total population = {len(df)}")
