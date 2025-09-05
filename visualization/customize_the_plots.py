# customize_the_plots.py
# ------------------------------------------------------------
# Customise various elements of the plot for visual appeal.
# ------------------------------------------------------------

import os
import matplotlib.pyplot as plt

csv_path = "/workspaces/stats-foundations-python/visualization/salesdata2.csv"
out_png  = "/workspaces/stats-foundations-python/visualization/customize_the_plots.png"

# Read file
with open(csv_path, "r", encoding="utf-8") as f:
    salefile = f.readlines()

# Create the sales lists
s_list, c_list = [], []
for line in salefile:
    line = line.strip()
    if not line:
        continue
    sale, cost = line.split(",", 1)
    s_list.append(int(sale))
    c_list.append(int(cost))

# Composite list for boxplot
sale_list = [s_list, c_list]

# 1) Scatter Plot
plt.subplot(2, 3, 1)
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(
    s_list,
    c_list,
    marker="*",
    s=100,
    c="#FF5733"
)

# 2) Boxplot
plt.subplot(2, 3, 2)
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(
    sale_list,
    patch_artist=True,
    boxprops=dict(facecolor="g", color="r", linewidth=2),
    whiskerprops=dict(color="r", linewidth=2),
    medianprops=dict(color="w", linewidth=1),
    capprops=dict(color="k", linewidth=2),
    flierprops=dict(markerfacecolor="r", marker="o", markersize=7),
)

# 3) Histogram of sales
plt.subplot(2, 3, 3)
plt.title("Histogram of Sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9, color="c")

# 4) Line plot of stock
x_days   = [1, 2, 3, 4, 5]
y_price1 = [9, 9.5, 10.1, 10, 12]

plt.subplot(2, 3, 4)
plt.title("Stockprice History")
plt.ylabel("Price")
plt.xlabel("Day")
plt.plot(x_days, y_price1, color="green", marker="o", markersize=10, linewidth=3, linestyle="--")

# 5) Bar Chart of temperature variation
x_cities = ["NewYork", "London", "Dubai", "New Delhi", "Tokyo"]
y_temp   = [75, 65, 105, 98, 90]

plt.subplot(2, 3, 5)
plt.title("Temperature Variation")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.xticks(rotation=45)  # <-- FIX: rotation expects a number or 'vertical'/'horizontal'
plt.bar(x_cities, y_temp, color=["r", "g", "c", "y", "m"])

# tidy layout and save BEFORE show
plt.tight_layout()

# Ensure output directory exists
os.makedirs(os.path.dirname(out_png), exist_ok=True)

plt.savefig(out_png, dpi=150, bbox_inches="tight")
plt.show()

print(f"Saved figure to: {out_png}")
