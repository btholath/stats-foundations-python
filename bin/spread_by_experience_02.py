"""
Reads your dataset from the fixed path, computes the spread of salary (income) across each year of experience 
using standard deviation, and plots it as a red line labeled “Spread”.

What this shows: 
for each year of experience, we calculate the standard deviation of income and plot that as a red line labeled “Spread”—a direct visual of how salary variability changes with experience.
"""

# salary_and_spread_abs_path.py
# -----------------------------
# Plots Salary (blue dots) and "Spread" (green horizontal lines) vs Experience.
# Input CSV: /workspaces/stats-foundations-python/dataset/loan_applications_2000.csv
# Output PNG: /workspaces/stats-foundations-python/dataset/salary_and_spread.png

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

IN_CSV  = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"
OUT_PNG = "/workspaces/stats-foundations-python/dataset/salary_and_spread.png"

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
    # Load and normalize columns
    df = pd.read_csv(IN_CSV)
    df.columns = [c.strip().lower() for c in df.columns]

    # Experience
    if "experience" not in df.columns:
        raise ValueError("Expected an 'experience' column (years).")
    exp = pd.to_numeric(df["experience"], errors="coerce")

    # Income (prefer numeric column if present)
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

    # Spread (Std. Dev.) per integer experience year (groups with n>=2)
    spread = (
        dfv.groupby("experience")["income"]
           .std(ddof=1)
           .dropna()
           .sort_index()
    )

    # Plot
    fig = plt.figure(figsize=(9, 6))
    ax = plt.gca()

    # Salary points as BLUE dots
    ax.scatter(dfv["experience"], dfv["income"], s=18, alpha=0.7, color="blue", label="Salary")

    # Spread as GREEN horizontal lines centered at each experience value
    if not spread.empty:
        for x, s in spread.items():
            # short horizontal segment around x (±0.45 on x-axis) at y = spread value
            ax.hlines(y=s, xmin=x - 0.45, xmax=x + 0.45, color="green", linewidth=2.5)
        # legend handle for spread
        spread_handle = Line2D([0], [0], color="green", lw=2.5, label="Spread")
        handles, labels = ax.get_legend_handles_labels()
        handles.append(spread_handle)
        labels.append("Spread")
        ax.legend(handles, labels, loc="best")
    else:
        ax.legend(loc="best")

    ax.set_title("Salary vs Experience with Spread")
    ax.set_xlabel("Experience (years)")
    ax.set_ylabel("Monthly Income (USD)")
    ax.grid(True, alpha=0.3)

    # Save
    os.makedirs(os.path.dirname(OUT_PNG), exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    # Console summary
    print("=== Salary & Spread by Experience ===")
    print(f"CSV Path     : {IN_CSV}")
    print(f"Output chart : {OUT_PNG}")
    if not spread.empty:
        print(f"Experience range with spread: {int(spread.index.min())}–{int(spread.index.max())} years")
        print(f"Mean spread  : {spread.mean():,.2f}")
        print(f"Max spread   : {spread.max():,.2f} at {int(spread.idxmax())} years")
    else:
        print("Not enough data per experience year to compute spread (need at least 2 points per year).")

if __name__ == "__main__":
    main()
