"""
Scenario: Selecting a random subset of customers for a satisfaction survey.
"""
import pandas as pd
import numpy as np

# Simulated customer dataset
df = pd.DataFrame({
    'CustomerID': range(1, 1001),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
    'SpendingScore': np.random.normal(50, 15, 1000)
})

# Simple random sample of 100 customers
sample = df.sample(n=100, random_state=42)

print("Simple Random Sample:\n", sample.head())
