"""
Variance
Avergae of the squared difference of the data from the Mean.

Average squared deviation from the mean	Units²
Variance helps you understand how volatile or stable each feature is.

"""

# generate_customers_and_variance.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------- 1) Generate a synthetic customers.csv ----------
np.random.seed(42)
n = 500

# Age: clipped normal distribution
age = np.clip(np.random.normal(loc=38, scale=12, size=n).round(), 18, 75).astype(int)

# Income (annual USD): log-normal for realistic right skew
income = np.random.lognormal(mean=np.log(60000), sigma=0.5, size=n)
income = np.clip(income, 15000, 250000).round(2)

# SpendingScore (1–100): weakly related to income (-) and age
noise = np.random.normal(0, 10, size=n)
spending = 50 + 0.00025 * (income - 60000) - 0.18 * (age - 38) + noise
spending = np.clip(spending, 1, 100).round(0).astype(int)

df = pd.DataFrame({
    "Age": age,
    "Income": income,
    "SpendingScore": spending
})

# Write the dataset
df.to_csv("customers.csv", index=False)
print("✅ Wrote customers.csv with columns: Age, Income, SpendingScore")

# ---------- 2) Compute variance and write to CSV ----------
features = ["Age", "Income", "SpendingScore"]
df_selected = df[features].dropna()
variance = df_selected.var()  # sample variance (ddof=1)
print("\n📈 Variance of Each Feature:\n", variance)

# Save variance to CSV as well
variance.rename("variance").to_csv("feature_variance.csv", header=True)
print("✅ Wrote feature_variance.csv")

# ---------- 3) Plot variance (same style you used) ----------
plt.figure(figsize=(6, 4))
sns.barplot(x=variance.index, y=variance.values, palette="viridis")
plt.title("Feature Variance")
plt.ylabel("Variance")
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/variance/feature_variance.png")