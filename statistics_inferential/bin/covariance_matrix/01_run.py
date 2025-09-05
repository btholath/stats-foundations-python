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

# Select relevant numeric columns
features = ['Age', 'Income', 'SpendingScore']
df_selected = df[features].dropna()

# -------------------------------
# 2️⃣ Covariance Matrix
# -------------------------------
cov_matrix = df_selected.cov()
print("\n📊 Covariance Matrix:\n", cov_matrix)

plt.figure(figsize=(6,4))
sns.heatmap(cov_matrix, annot=True, cmap='YlGnBu')
plt.title("Covariance Matrix")
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/variance/covariance_matrix.png")