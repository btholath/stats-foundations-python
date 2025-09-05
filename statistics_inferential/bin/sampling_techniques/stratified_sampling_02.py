"""
Stratified Sampling
This divides the population into strata (subgroups) and samples proportionally from each, ensuring representation of key groups.

Real-World Scenario: A hospital analyzes patient recovery times stratified by age groups (young, middle, senior) from 900 patients. This reduces bias in inferring average recovery time for treatment planning.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # For stratified sampling
from scipy import stats
import matplotlib.pyplot as plt

# Generate synthetic population: 900 patients with age groups and recovery times (days)
np.random.seed(42)
population_size = 900
ages = np.random.choice(['Young', 'Middle', 'Senior'], size=population_size, p=[0.3, 0.4, 0.3])
recovery_times = np.where(ages == 'Young', np.random.normal(10, 2, population_size),
                          np.where(ages == 'Middle', np.random.normal(15, 3, population_size),
                                   np.random.normal(20, 4, population_size)))
population = pd.DataFrame({'AgeGroup': ages, 'RecoveryTime': recovery_times})

# Population stats
pop_mean = population['RecoveryTime'].mean()
print(f"Population Mean Recovery Time: {pop_mean:.2f} days")

# Stratified Sampling: Sample 150 total, proportional to strata
sample_size = 150
sample = population.groupby('AgeGroup', group_keys=False).apply(lambda x: x.sample(frac=sample_size/population_size))

# Sample stats
sample_mean = sample['RecoveryTime'].mean()
confidence_interval = stats.t.interval(0.95, df=len(sample)-1, loc=sample_mean, scale=stats.sem(sample))
print(f"Sample Mean Recovery Time: {sample_mean:.2f} days")
print(f"95% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
print("Interpretation: Stratification ensures age groups are represented, leading to more accurate inferences for targeted healthcare.")

# Visualize strata distribution
population['AgeGroup'].value_counts().plot(kind='bar', alpha=0.5, label='Population', position=0, width=0.4)
sample['AgeGroup'].value_counts().plot(kind='bar', alpha=0.5, label='Sample', position=1, width=0.4)
plt.ylabel('Count')
plt.title('Stratified Sampling: Patient Recovery by Age Group')
plt.legend()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_techniques/stratified_sampling_02.png")