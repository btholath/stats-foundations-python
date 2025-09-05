import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
num_customers = 1000
regions = ['North', 'South', 'East', 'West']
genders = ['Male', 'Female']
names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Jamie', 'Drew', 'Quinn', 'Avery']

# Generate synthetic data
data = {
    'CustomerID': range(1, num_customers + 1),
    'Name': [random.choice(names) + str(i) for i in range(1, num_customers + 1)],
    'Age': np.random.normal(loc=40, scale=12, size=num_customers).astype(int),
    'Gender': [random.choice(genders) for _ in range(num_customers)],
    'Region': [random.choice(regions) for _ in range(num_customers)],
    'Income': np.random.normal(loc=60000, scale=15000, size=num_customers).round(2),
    'Subscribed': np.random.choice(['Yes', 'No'], size=num_customers, p=[0.7, 0.3]),
    'Website': np.random.choice(
        [np.nan, 'www.customerportal.com'], size=num_customers, p=[0.2, 0.8]
    )
}

df = pd.DataFrame(data)

# Clean up unrealistic ages and incomes
df['Age'] = df['Age'].clip(lower=18, upper=80)
df['Income'] = df['Income'].clip(lower=20000, upper=150000)

# Save to CSV
df.to_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/sampling_errors/input/customers.csv", index=False)

print("✅ customers.csv file generated with", num_customers, "records.")
