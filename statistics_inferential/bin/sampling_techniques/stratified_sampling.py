"""
Scenario: Ensuring proportional representation of regions in a market analysis.

"""
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'CustomerID': range(1, 1001),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
    'SpendingScore': np.random.normal(50, 15, 1000)
})

# Stratified sampling based on 'Region'
_, stratified_sample = train_test_split(df, test_size=0.1, stratify=df['Region'], random_state=42)

print("Stratified Sample:\n", stratified_sample['Region'].value_counts())
