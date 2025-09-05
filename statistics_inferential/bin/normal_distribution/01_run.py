"""
✅ Generated a realistic dataset of 365 daily temperatures in Los Angeles using a normal distribution centered at 30°C with a standard deviation of 3°C.

✅ Calculated the probability that the temperature falls between 32°C and 33°C, which is approximately 9.38%.

✅ Created a bar graph (histogram) of the temperature data and overlaid a red curve representing the Probability Density Function (PDF) of the normal distribution.

✅ Included a legend to distinguish the histogram from the PDF curve.

This visualization is ideal for teaching continuous distributions and interpreting real-world probabilities. The red curve shows the theoretical density, while the bars reflect the empirical distribution from the synthetic data.

Generates a realistic temperature dataset for Los Angeles
Plots a histogram (bar graph) of the data
Overlays a red Probability Density Function (PDF) curve
Calculates the probability that temperature is between 32°C and 33°C
Includes a legend for clarity
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------
# 1️⃣ Generate Synthetic Temperature Data
# -------------------------------
np.random.seed(42)
n_days = 365
mean_temp = 30      # Average LA temperature in °C
std_temp = 3        # Standard deviation

# Simulate daily temperatures
temperatures = np.random.normal(loc=mean_temp, scale=std_temp, size=n_days)

# -------------------------------
# 2️⃣ Calculate Probability: 32°C to 33°C
# -------------------------------
prob_32_33 = norm.cdf(33, loc=mean_temp, scale=std_temp) - norm.cdf(32, loc=mean_temp, scale=std_temp)
print(f"📊 Probability that temperature is between 32°C and 33°C: {prob_32_33:.2%}")

# -------------------------------
# 3️⃣ Plot Histogram + PDF Curve
# -------------------------------
plt.figure(figsize=(10, 5))

# Histogram
count, bins, ignored = plt.hist(temperatures, bins=20, density=True, alpha=0.6, color='skyblue', label='Temperature Histogram')

# PDF Curve
x = np.linspace(min(bins), max(bins), 1000)
pdf = norm.pdf(x, loc=mean_temp, scale=std_temp)
plt.plot(x, pdf, 'r-', linewidth=2, label='PDF Curve (Normal Distribution)')

# Labels and Legend
plt.title("Temperature Distribution in Los Angeles")
plt.xlabel("Temperature (°C)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/normal_distribution/probability_density_function_los_angeles_weather.png")

