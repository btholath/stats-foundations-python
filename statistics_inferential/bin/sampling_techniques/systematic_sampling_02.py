"""
Systematic Sampling
This selects every k-th element from a list, starting from a random point. It's efficient for ordered data but risks periodicity bias.

Real-World Scenario: A manufacturing firm samples every 10th product from a production line of 800 items to infer defect rates for quality control reporting.
"""
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Generate synthetic population: 800 products with defect rates (0=no defect, 1=defect)
np.random.seed(42)
population_size = 800
population = pd.DataFrame({
    'ProductID': range(1, population_size + 1),
    'Defect': np.random.choice([0, 1], size=population_size, p=[0.95, 0.05])
})

# Population stats
pop_defect_rate = population['Defect'].mean() * 100
print(f"Population Defect Rate: {pop_defect_rate:.2f}%")

# Systematic Sampling: Every 10th product, starting from random index
k = 10
start = np.random.randint(0, k)
sample_indices = range(start, population_size, k)
sample = population.iloc[sample_indices]

# Sample stats
sample_defect_rate = sample['Defect'].mean() * 100
confidence_interval = stats.t.interval(0.95, df=len(sample)-1, loc=sample_defect_rate, scale=stats.sem(sample['Defect']) * 100)
print(f"Sample Defect Rate: {sample_defect_rate:.2f}%")
print(f"95% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
print("Interpretation: Useful for assembly lines; interval estimates true defect rate, informing production adjustments.")

# Visualize
plt.plot(population['ProductID'], population['Defect'], label='Population Defects', alpha=0.5)
plt.scatter(sample['ProductID'], sample['Defect'], color='red', label='Sample')
plt.xlabel('Product ID')
plt.ylabel('Defect (1=Yes)')
plt.title('Systematic Sampling: Product Defects')
plt.legend()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_techniques/systematic_sampling_02.png")