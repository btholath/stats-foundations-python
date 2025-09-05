# measure_of_dispersion_abs_path.py
# ---------------------------------
# Computes key measures of dispersion for the income column.
# Reads from a fixed absolute path (edit IN_CSV if your workspace changes).

"""
Why “Measures of Dispersion” matter (purpose & advantages)

Purpose
    Quantify how spread out your data is around its center (mean/median).
    Reveal volatility & risk: same average income can hide very different variability.
    Help spot outliers and skew, guiding cleaning and robust modeling choices.

Advantages
- Complements central tendency: 
    mean/median alone can mislead without spread.
- Model selection: 
    high variance or heavy tails suggest robust estimators (IQR/MAD), transformations, or regularization.
- Comparability: 
    the coefficient of variation normalizes spread, so you can compare variability across metrics with different units/scales.
- Decision-making: 
    smaller dispersion means more predictable outcomes (useful in pricing, risk, and capacity planning).
"""

import pandas as pd
import numpy as np

# Absolute input path
IN_CSV = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"

# Column priority: use numeric if present, else parse currency in 'income'
COLUMN_PRIORITY = ("income_num", "income")

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    """Convert '$12,345.67' -> 12345.67; non-parsable -> NaN."""
    if series.dtype.kind in "biufc":
        return pd.to_numeric(series, errors="coerce")
    return (series.astype(str)
                 .str.replace("$", "", regex=False)
                 .str.replace(",", "", regex=False)
                 .pipe(pd.to_numeric, errors="coerce"))

def pick_column(df: pd.DataFrame, candidates=COLUMN_PRIORITY) -> str:
    for c in candidates:
        if c in df.columns:
            return c
    raise ValueError(f"None of the expected columns found: {candidates}")

def measures_of_dispersion(s: pd.Series) -> dict:
    s = pd.to_numeric(s, errors="coerce").dropna()
    if s.empty:
        raise ValueError("No valid numeric values to analyze.")

    # Core stats
    n = int(s.size)
    s_min = float(s.min())
    s_max = float(s.max())
    s_range = s_max - s_min
    mean = float(s.mean())
    median = float(s.median())
    var_sample = float(s.var(ddof=1))           # sample variance
    std_sample = float(s.std(ddof=1))           # sample std dev

    # Robust stats
    q1 = float(s.quantile(0.25))
    q3 = float(s.quantile(0.75))
    iqr = q3 - q1
    mad = float((s - median).abs().median())    # median absolute deviation (raw)
    # (Optional) Consistent MAD estimator for normal data: 1.4826 * MAD

    # Relative spread (unitless)
    cv = float(std_sample / mean) if mean != 0 else float("nan")  # coefficient of variation

    # Outlier fences (IQR rule)
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers = s[(s < lower_fence) | (s > upper_fence)]

    return {
        "count": n,
        "min": round(s_min, 2),
        "max": round(s_max, 2),
        "range": round(s_range, 2),
        "mean": round(mean, 2),
        "median": round(median, 2),
        "variance_sample": round(var_sample, 2),
        "std_dev_sample": round(std_sample, 2),
        "q1": round(q1, 2),
        "q3": round(q3, 2),
        "iqr": round(iqr, 2),
        "mad": round(mad, 2),
        "coefficient_of_variation": round(cv, 4),
        "lower_fence": round(lower_fence, 2),
        "upper_fence": round(upper_fence, 2),
        "num_outliers": int(outliers.size)
    }

def main():
    df = pd.read_csv(IN_CSV)
    df.columns = [c.strip().lower() for c in df.columns]

    col = pick_column(df)
    s = df[col]
    if col == "income":
        s = _to_numeric_currency(s)

    stats = measures_of_dispersion(s)

    print("=== Measures of Dispersion (Income) ===")
    print(f"CSV Path                : {IN_CSV}")
    print(f"Column analyzed         : {col}")
    for k, v in stats.items():
        print(f"{k:>24}: {v}")

if __name__ == "__main__":
    main()
