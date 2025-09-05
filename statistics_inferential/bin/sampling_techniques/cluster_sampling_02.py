"""
Cluster Sampling
This divides the population into clusters, randomly selects clusters, and samples all elements within them. It's cost-effective for geographically dispersed populations.

Real-World Scenario: A market research firm surveys households clustered by city neighborhoods (10 clusters of 100 households each) to infer average income for urban planning.
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Generate synthetic population: 10 clusters (neighborhoods) x 100 households, with incomes
np.random.seed(42)
num_clusters = 10
cluster_size = 100
clusters = np.repeat(range(1, num_clusters + 1), cluster_size)
incomes = np.random.normal(50000, 10000, num_clusters * cluster_size) + (clusters * 2000)  # Vary by cluster
population = pd.DataFrame({'Neighborhood': clusters, 'Income': incomes})

# Population stats
pop_mean_income = population['Income'].mean()
print(f"Population Mean Income: ${pop_mean_income:.2f}")

# Cluster Sampling: Randomly select 3 clusters, take all households in them
selected_clusters = np.random.choice(range(1, num_clusters + 1), size=3, replace=False)
sample = population[population['Neighborhood'].isin(selected_clusters)]

# Sample stats
sample_mean_income = sample['Income'].mean()
confidence_interval = stats.t.interval(0.95, df=len(sample)-1, loc=sample_mean_income, scale=stats.sem(sample['Income']))
print(f"Sample Mean Income: ${sample_mean_income:.2f}")
print(f"95% Confidence Interval: (${confidence_interval[0]:.2f}, ${confidence_interval[1]:.2f})")
print("Interpretation: Cost-effective for spread-out areas; interval helps stakeholders plan budgets accurately.")

# Visualize
population.boxplot(column='Income', by='Neighborhood', showfliers=False)
plt.suptitle('')
plt.title('Cluster Sampling: Household Incomes by Neighborhood')
plt.ylabel('Income ($)')
sample.boxplot(column='Income', by='Neighborhood', positions=[1,2,3], widths=0.5, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_techniques/cluster_sampling_02.png")