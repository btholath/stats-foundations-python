"""
Simple Random Sampling
This technique selects samples randomly from the entire population, giving each element an equal chance. It's straightforward but can miss subgroups.

Real-World Scenario: A retail company surveys customer satisfaction from a database of 1000 customers to infer overall satisfaction ratings (scale 1-10). This helps estimate population mean with a confidence interval for marketing decisions.
"""
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Generate synthetic population data: 1000 customers with satisfaction scores (1-10)
np.random.seed(42)
population_size = 1000
population = pd.DataFrame({
    'CustomerID': range(1, population_size + 1),
    'Satisfaction': np.random.randint(1, 11, size=population_size)
})

# Population stats
pop_mean = population['Satisfaction'].mean()
print(f"Population Mean Satisfaction: {pop_mean:.2f}")

# Simple Random Sampling: Select 100 samples
sample_size = 100
sample = population.sample(n=sample_size, random_state=42)

# Sample stats
sample_mean = sample['Satisfaction'].mean()
# Ensure sample is a 1D array for stats.sem
sample_data = sample['Satisfaction'].values  # Convert Pandas Series to NumPy array
confidence_interval = stats.t.interval(0.95, df=sample_size-1, loc=sample_mean, scale=stats.sem(sample_data))

# Debug: Inspect confidence_interval
print("Debug: confidence_interval =", confidence_interval)
print("Debug: Type of confidence_interval[0] =", type(confidence_interval[0]))
print("Debug: Shape of confidence_interval[0] =", getattr(confidence_interval[0], 'shape', 'N/A'))

print(f"Sample Mean Satisfaction: {sample_mean:.2f}")

# Handle confidence_interval elements
if isinstance(confidence_interval[0], np.ndarray):
    if confidence_interval[0].size == 1:  # Check if single-element array
        ci_lower = float(confidence_interval[0])
        ci_upper = float(confidence_interval[1])
    else:
        raise ValueError(f"confidence_interval[0] is a multi-element array: {confidence_interval[0]}")
else:
    ci_lower = float(confidence_interval[0])  # Already a scalar
    ci_upper = float(confidence_interval[1])

print(f"95% Confidence Interval: ({ci_lower:.2f}, {ci_upper:.2f})")
print("Interpretation: This interval likely contains the true population mean, aiding decisions like service improvements.")

# Visualize
plt.hist(population['Satisfaction'], alpha=0.5, label='Population')
plt.hist(sample['Satisfaction'], alpha=0.5, label='Sample')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.title('Simple Random Sampling: Customer Satisfaction')
plt.legend()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_techniques/simple_random_sampling_02.png")