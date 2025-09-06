import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load dataset
df = pd.read_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/normal_distribution/simulated_normal.csv")

# Use the 400-sample column
data = df['n400'].dropna()

# Calculate mean and std
mean = data.mean()
std = data.std()

# Plot histogram
plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(data, bins=20, density=True, alpha=0.6, color='skyblue', label='Histogram')

# Plot PDF curve
x = np.linspace(min(bins), max(bins), 1000)
pdf = norm.pdf(x, loc=mean, scale=std)
plt.plot(x, pdf, 'r-', linewidth=2, label='PDF Curve')

# Labels and legend
plt.title("Real-World Normal Distribution (n=400)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/normal_distribution/simulate_normal_distribution.png")