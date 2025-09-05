"""
Scenario: Selecting a few store locations and surveying all customers within them.
"""
import pandas as pd
import numpy as np

# Simulated data: 10 stores, each with 100 customers
df = pd.DataFrame({
    'StoreID': np.repeat(range(1, 11), 100),
    'CustomerID': range(1, 1001),
    'PurchaseAmount': np.random.gamma(2, 50, 1000)
})

# Randomly select 3 stores (clusters)
selected_stores = np.random.choice(df['StoreID'].unique(), size=3, replace=False)
cluster_sample = df[df['StoreID'].isin(selected_stores)]

print("Cluster Sample from Stores:", selected_stores)
print(cluster_sample.head())
