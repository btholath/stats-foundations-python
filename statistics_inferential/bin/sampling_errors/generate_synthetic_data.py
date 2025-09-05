import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# -------------------------------
# 1️⃣ Generate Synthetic Dataset
# -------------------------------
# Simulate customer data
n = 1000
age = np.random.normal(40, 10, n)                      # Age in years
income = age * 1000 + np.random.normal(0, 10000, n)    # Income correlated with age
spending_score = income * 0.3 + np.random.normal(0, 5000, n)  # Spending score influenced by income

df = pd.DataFrame({
    'Age': age,
    'Income': income,
    'SpendingScore': spending_score
})

# -------------------------------
# 2️⃣ Sample Bias Demonstration
# -------------------------------
# Biased sample: only customers under 30
biased_sample = df[df['Age'] < 30]

# Compare distributions
plt.figure(figsize=(10,4))
sns.histplot(df['Age'], kde=True, color='blue', label='Full Population')
sns.histplot(biased_sample['Age'], kde=True, color='red', label='Biased Sample')
plt.title("Sample Bias: Age Distribution")
plt.legend()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/output/Sample_Bias_Demonstration.png")
# -------------------------------
# 3️⃣ Correlation vs. Causality
# -------------------------------
# Correlation matrix
correlation = df.corr()

print("\n🔗 Correlation Matrix:\n", correlation)

# Plot correlation heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Between Variables")
plt.show()

# ⚠️ Reminder: Correlation ≠ Causation
print("\n⚠️ Note: High correlation between Income and SpendingScore does not prove causality.\n")
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/output/Correlation_Between_Variables.png")

# -------------------------------
# 4️⃣ Covariance and Covariance Matrix
# -------------------------------
# Covariance matrix
cov_matrix = df.cov()

print("📊 Covariance Matrix:\n", cov_matrix)

# Visualize covariance matrix
sns.heatmap(cov_matrix, annot=True, cmap='YlGnBu')
plt.title("Covariance Matrix")
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/output/Covariance_Matrix.png")
