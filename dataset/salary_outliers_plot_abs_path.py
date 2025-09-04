# salary_outliers_plot_abs_path.py
# --------------------------------
# Detect and plot income outliers vs experience, using a fixed CSV path.
# Saves a scatter plot highlighting:
#   - Outlier salaries: RED dot(s)
#   - Mean salary: BLUE dot
#   - Median salary: GREEN dot
"""
Reads your CSV from the fixed path /workspaces/stats-foundations-python/dataset/loan_applications_2000.csv
uses experience (x-axis) and income (y-axis)
parses currency to numeric if needed
detects income outliers with the IQR rule

plots a scatter:
regular points (default color)
outliers as red dots
mean income as a blue dot
median income as a green dot
saves the chart to /workspaces/stats-foundations-python/dataset/salary_outliers.png
also writes a CSV of the outliers (optional but handy)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fixed input and output paths
IN_CSV  = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"
OUT_PNG = "/workspaces/stats-foundations-python/dataset/salary_outliers.png"
OUT_CSV = "/workspaces/stats-foundations-python/dataset/salary_outliers_only.csv"

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    """Convert '$12,345.67' -> 12345.67; non-parsable -> NaN."""
    if series.dtype.kind in "biufc":
        return pd.to_numeric(series, errors="coerce")
    return (
        series.astype(str)
              .str.replace("$", "", regex=False)
              .str.replace(",", "", regex=False)
              .pipe(pd.to_numeric, errors="coerce")
    )

def main():
    # 1) Load data & normalize columns
    df = pd.read_csv(IN_CSV)
    df.columns = [c.strip().lower() for c in df.columns]

    # 2) Prepare income numeric
    if "loan_amount_num" in df.columns:
        # Some pipelines store numeric loan amounts, but here we need income:
        pass  # ignore; we care about income
    # Prefer already-parsed numeric income if present
    if "income_num" in df.columns:
        income = pd.to_numeric(df["income_num"], errors="coerce")
    else:
        if "income" not in df.columns:
            raise ValueError("Expected 'income' or 'income_num' column not found.")
        income = _to_numeric_currency(df["income"])

    # 3) Experience (years)
    if "experience" not in df.columns:
        raise ValueError("Expected 'experience' column not found.")
    exp = pd.to_numeric(df["experience"], errors="coerce")

    # Drop rows without both exp and income
    mask_valid = exp.notna() & income.notna()
    dfv = df.loc[mask_valid].copy()
    exp = exp[mask_valid]
    income = income[mask_valid]

    if dfv.empty:
        raise ValueError("No valid rows with both experience and income.")

    # 4) Outlier detection on income using IQR rule
    q1 = income.quantile(0.25)
    q3 = income.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outlier_mask = (income < lower) | (income > upper)

    # 5) Mean & median income
    mean_income = float(income.mean())
    median_income = float(income.median())

    # Choose x-positions for the mean/median dots: use mean/median experience
    mean_exp = float(exp.mean())
    median_exp = float(exp.median())

    # 6) Plot
    fig = plt.figure(figsize=(9, 6))
    ax = plt.gca()

    # Base scatter
    ax.scatter(exp[~outlier_mask], income[~outlier_mask], s=18, alpha=0.7, label="Applicants")

    # Outliers in RED
    if outlier_mask.any():
        ax.scatter(exp[outlier_mask], income[outlier_mask], s=32, color="red", alpha=0.9, label="Outliers")

    # Mean (BLUE) and Median (GREEN) dots
    ax.scatter([mean_exp], [mean_income], s=80, color="blue", label="Mean income")
    ax.scatter([median_exp], [median_income], s=80, color="green", label="Median income")

    ax.set_title("Income vs Experience with Outliers, Mean (blue), Median (green)")
    ax.set_xlabel("Experience (years)")
    ax.set_ylabel("Monthly Income (USD)")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.25)

    # 7) Save plot and outlier CSV
    os.makedirs(os.path.dirname(OUT_PNG), exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    if outlier_mask.any():
        outliers_df = dfv.loc[outlier_mask].copy()
        outliers_df.to_csv(OUT_CSV, index=False)

    # 8) Console summary
    print("=== Income Outlier Detection ===")
    print(f"Rows evaluated       : {len(dfv)}")
    print(f"Outliers detected    : {int(outlier_mask.sum())}")
    print(f"Income Q1/Q3         : {q1:,.2f} / {q3:,.2f}  (IQR={iqr:,.2f})")
    print(f"Lower/Upper fences   : {lower:,.2f} / {upper:,.2f}")
    print(f"Mean income (blue)   : {mean_income:,.2f} at exp={mean_exp:.1f} yrs")
    print(f"Median income (green): {median_income:,.2f} at exp={median_exp:.1f} yrs")
    print(f"Chart saved to       : {OUT_PNG}")
    if outlier_mask.any():
        print(f"Outliers CSV         : {OUT_CSV}")

if __name__ == "__main__":
    main()
