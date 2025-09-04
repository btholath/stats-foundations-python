"""
prints the table you want and then computes the mean, variance (using your definition: average of squared differences, i.e., divide by n), and standard deviation.
"""

# ny_temp_stats.py
import math

# Day 1..7 temperatures for New York
temps = [20, 21, 19, 20, 21, 19, 20]

n = len(temps)
mean = sum(temps) / n

print("Day, X, X - Mean(X), (X - Mean(X))^2")
print("-" * 48)

sumsq = 0.0
for day, x in enumerate(temps, start=1):
    diff = x - mean
    diff2 = diff * diff
    sumsq += diff2
    print(f"{day:>3}, {x:>2}, {diff:>9.2f}, {diff2:>16.2f}")

print("-" * 48)
variance = sumsq / n                 # as requested: Average = total of squared diffs / number of days
std_dev  = math.sqrt(variance)

print(f"Mean (X̄):                     {mean:.2f}")
print(f"Total of (X - X̄)^2:          {sumsq:.2f}")
print(f"Variance (σ² = avg sq diff):  {variance:.6f}")
print(f"Std. Deviation (σ):           {std_dev:.6f}")


"""
What it does

Difference = 
𝑋
−
𝑋
ˉ
X−
X
ˉ

Difference Squared = 
(
𝑋
−
𝑋
ˉ
)
2
(X−
X
ˉ
)
2

Average (Variance) = 
∑(𝑋−𝑋ˉ)2 /𝑛∑(X−Xˉ)2/n

Standard Deviation = 
Variance
Variance
	​
With your data [20, 21, 19, 20, 21, 19, 20], the script will show a mean of 20.00, variance of 4/7 ≈ 0.571428, and standard deviation of √(4/7) ≈ 0.75593.
"""