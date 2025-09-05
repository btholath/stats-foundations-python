"""
Reads your dataset from the fixed path, computes the spread of salary (income) across each year of experience 
using standard deviation, and plots it as a red line labeled “Spread”.

What this shows: 
for each year of experience, we calculate the standard deviation of income and plot that as a red line labeled “Spread”—a direct visual of how salary variability changes with experience.
"""

# spread_by_experience_abs_path.py
# --------------------------------
# Plots salary (income) "spread" vs experience as a red line with legend "Spread".
# Uses standard deviation of income per experience year.
# Input CSV (fixed): /workspaces/stats-foundations-python/dataset/loan_applications_2000.csv
# Output PNG:        /workspaces/stats-foundations-python/dataset/spread_by_experience.png

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

IN_CSV  = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"
OUT_PNG = "/workspaces/stats-foundations-python/dataset/spread_by_experience.png"

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    """Convert '$12,345.67' -> 12345.67; non-parsable -> NaN."""
    if series.dtype.kind in "biufc":
        return pd.to_numeric(series, errors="coerce")
    return (series.astype(str)
                 .str.replace("$", "", regex=False)
                 .str.replace(",", "", regex=False)
                 .pipe(pd.to_numeric, errors="coerce"))

def main():
    # Load data
    df = pd.read_csv(IN_CSV)
    df.columns = [c.strip().lower() for c in df.columns]

    # Experience (years)
    if "experience" not in df.columns:
        raise ValueError("Expected an 'experience' column (years).")
    exp = pd.to_numeric(df["experience"], errors="coerce")

    # Salary/Income (numeric): prefer cleaned 'income_num', else parse 'income'
    if "income_num" in df.columns:
        income = pd.to_numeric(df["income_num"], errors="coerce")
    else:
        if "income" not in df.columns:
            raise ValueError("Expected 'income' or 'income_num' column.")
        income = _to_numeric_currency(df["income"])

    # Keep valid rows
    mask = exp.notna() & income.notna()
    dfv = pd.DataFrame({"experience": exp[mask].astype(int), "income": income[mask]})
    if dfv.empty:
        raise ValueError("No valid rows with both experience and income.")

    # Compute spread: standard deviation per integer year of experience
    spread = (
        dfv.groupby("experience")["income"]
           .std(ddof=1)                     # sample std dev
           .dropna()                        # groups with N<2 will be NaN
           .sort_index()
    )

    if spread.empty:
        raise ValueError("No experience groups have >=2 records to compute spread.")

    # Plot: red line with legend "Spread"
    fig = plt.figure(figsize=(9, 6))
    ax = plt.gca()
    ax.plot(spread.index.values, spread.values, color="red", linewidth=2.0, label="Spread")
    ax.set_title("Salary (Income) Spread by Experience")
    ax.set_xlabel("Experience (years)")
    ax.set_ylabel("Income spread (Std. Dev., USD)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    # Save figure
    os.makedirs(os.path.dirname(OUT_PNG), exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    # Console summary
    print("=== Salary Spread by Experience ===")
    print(f"CSV Path     : {IN_CSV}")
    print(f"Output chart : {OUT_PNG}")
    print(f"Experience years analyzed: {spread.index.min()}–{spread.index.max()}")
    print(f"Mean spread  : {spread.mean():,.2f}")
    print(f"Max spread   : {spread.max():,.2f} at {spread.idxmax()} years")

if __name__ == "__main__":
    main()


