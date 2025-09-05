
"""
So all that the correlation tells us
is how strong or weak the two variables are correlated.
It tells us how they move or change together,

but it does not tell us
whether one causes the other.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Function to generate and plot data for a given correlation type
def plot_correlation(x, y, title):
    corr_coef, _ = pearsonr(x, y)
    plt.scatter(x, y, alpha=0.7)
    plt.title(f'{title} (r = {corr_coef:.2f})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

# Generate synthetic datasets
np.random.seed(42)  # For reproducibility

# 1. Strong Positive Correlation
x_strong_pos = np.linspace(0, 10, 50)
y_strong_pos = x_strong_pos + np.random.normal(0, 0.5, 50)  # Small noise

# 2. Weak Positive Correlation
x_weak_pos = np.linspace(0, 10, 50)
y_weak_pos = x_weak_pos + np.random.normal(0, 5, 50)  # Larger noise

# 3. No Correlation
x_no_corr = np.random.uniform(0, 10, 50)
y_no_corr = np.random.uniform(0, 10, 50)  # Completely random

# 4. Strong Negative Correlation
x_strong_neg = np.linspace(0, 10, 50)
y_strong_neg = -x_strong_neg + np.random.normal(0, 0.5, 50)  # Small noise, negative slope

# Create 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot each in separate subplots
plt.sca(axs[0, 0])
plot_correlation(x_strong_pos, y_strong_pos, 'Strong Positive Correlation')

plt.sca(axs[0, 1])
plot_correlation(x_weak_pos, y_weak_pos, 'Weak Positive Correlation')

plt.sca(axs[1, 0])
plot_correlation(x_no_corr, y_no_corr, 'No Correlation')

plt.sca(axs[1, 1])
plot_correlation(x_strong_neg, y_strong_neg, 'Strong Negative Correlation')

# Adjust layout and show plots
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/correlation_coefficient/show_how_strong_or_weak_two_variables_correlated.png")