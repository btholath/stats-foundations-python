"""
Interpretation Guide
Plot Type	    Variable Type	    Insight
PMF	            Discrete	        Probability of exact values (e.g., 3 purchases)
PDF	            Continuous	        Density of values across a range (e.g., spend distribution)
CDF	            Both	            Probability of values ≤ threshold (e.g., ≤ $50 spent)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

# Load dataset
df = pd.read_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/distribution/customer_behavior.csv")

# -------------------------------
# 1️⃣ PMF: Discrete Variables
# -------------------------------
def plot_pmf(column):
    counts = df[column].value_counts().sort_index()
    probs = counts / counts.sum()

    plt.figure(figsize=(6,4))
    sns.barplot(x=probs.index, y=probs.values, hue=probs.index, palette='Blues', legend=False)
    plt.title(f"PMF of {column}")
    plt.xlabel(column)
    plt.ylabel("Probability")
    plt.tight_layout()
    plt.show()
    plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/distribution/customer_behavior_discrete_variables.png")

plot_pmf("ProductsPurchased")
plot_pmf("VisitFrequency")

# -------------------------------
# 2️⃣ PDF: Continuous Variables
# -------------------------------
def plot_pdf(column):
    data = df[column].dropna()
    kde = gaussian_kde(data)

    x_vals = np.linspace(data.min(), data.max(), 1000)
    y_vals = kde(x_vals)

    plt.figure(figsize=(6,4))
    plt.plot(x_vals, y_vals, color='green')
    plt.fill_between(x_vals, y_vals, alpha=0.3)
    plt.title(f"PDF of {column}")
    plt.xlabel(column)
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()
    plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/distribution/customer_behavior_continuous_variables.png")

plot_pdf("AmountSpent")
plot_pdf("TimeInStore")

# -------------------------------
# 3️⃣ CDF: Any Numeric Variable
# -------------------------------
def plot_cdf(column):
    data = df[column].dropna()
    sorted_data = np.sort(data)
    cdf = np.arange(1, len(sorted_data)+1) / len(sorted_data)

    plt.figure(figsize=(6,4))
    plt.plot(sorted_data, cdf, color='purple')
    plt.title(f"CDF of {column}")
    plt.xlabel(column)
    plt.ylabel("Cumulative Probability")
    plt.tight_layout()
    plt.show()
    plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/distribution/customer_behavior_cumulative_probability.png")

plot_cdf("ProductsPurchased")
plot_cdf("AmountSpent")
