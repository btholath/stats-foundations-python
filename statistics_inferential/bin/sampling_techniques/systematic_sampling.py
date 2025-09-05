"""
Scenario: Selecting every 10th transaction for audit from a log.
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'TransactionID': range(1, 1001),
    'Amount': np.random.exponential(scale=100, size=1000)
})

# Systematic sample: every 10th transaction
step = 10
systematic_sample = df.iloc[::step]

print("Systematic Sample:\n", systematic_sample.head())
