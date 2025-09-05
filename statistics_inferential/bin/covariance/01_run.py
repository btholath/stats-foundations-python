"""
Variance and Covariance of Height and Weight

Variance of X (Height): which is just the spread of height values.
Covariance of X with Y (Height vs. Weight): which shows how height and weight vary together.


Metric	                Meaning
Variance of X	        How much height varies across individuals
Covariance of X with Y	Whether taller people tend to weigh more (positive value)

If cov_xy is positive, height and weight tend to increase together.
If cov_xy is negative, taller people tend to weigh less (unlikely here).
If cov_xy is near zero, there's no consistent relationship.

"""
import numpy as np
import pandas as pd

# Simulate realistic data
np.random.seed(42)
n = 100
height = np.random.normal(loc=170, scale=10, size=n)  # cm
weight = height * 0.45 + np.random.normal(loc=0, scale=5, size=n)  # kg, loosely correlated

df = pd.DataFrame({'Height': height, 'Weight': weight})

# -------------------------------
# 1️⃣ Variance of X (Height)
# -------------------------------
var_x = np.var(df['Height'], ddof=1)  # sample variance
print(f"📈 Variance of Height (X): {var_x:.2f} cm²")

# -------------------------------
# 2️⃣ Covariance of X with Y
# -------------------------------
cov_xy = np.cov(df['Height'], df['Weight'])[0, 1]
print(f"🔗 Covariance of Height and Weight (X,Y): {cov_xy:.2f} cm·kg")
