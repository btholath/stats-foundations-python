"""
customer_behavior.csv
This dataset simulates customer behavior in a retail setting and includes:

Column Name	            Type	    Description
CustomerID	            Discrete	Unique identifier (integer)
ProductsPurchased	    Discrete	Number of products bought (0–10)
VisitFrequency	        Discrete	Visits per month (1–12)
AmountSpent	            Continuous	Total spend in USD
TimeInStore	            Continuous	Time spent per visit in minutes

"""

import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Discrete variables
products_purchased = np.random.poisson(lam=3, size=n)  # PMF-friendly
visit_frequency = np.random.randint(1, 13, size=n)     # Uniform discrete

# Continuous variables
amount_spent = np.random.normal(loc=50, scale=15, size=n).round(2)  # PDF-friendly
time_in_store = np.random.exponential(scale=20, size=n).round(2)    # Skewed PDF

# Assemble dataset
df = pd.DataFrame({
    'CustomerID': range(1, n + 1),
    'ProductsPurchased': products_purchased,
    'VisitFrequency': visit_frequency,
    'AmountSpent': amount_spent,
    'TimeInStore': time_in_store
})

# Clip unrealistic values
df['AmountSpent'] = df['AmountSpent'].clip(lower=0)
df['TimeInStore'] = df['TimeInStore'].clip(lower=0)

# Save to CSV
df.to_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/distribution/customer_behavior.csv", index=False)
print("✅ Dataset 'customer_behavior.csv' generated.")
