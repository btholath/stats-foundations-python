# spread_summary_abs_path.py
# --------------------------
# Computes spread statistics for numeric columns in a CSV:
#   count, min, max, range, mean, median, sample variance, sample std dev,
#   Q1, Q3, IQR, MAD, coefficient of variation, IQR outlier fences, #outliers
#
# Input CSV (fixed):
#   /workspaces/stats-foundations-python/dataset/loan_applications_2000.csv
# Output CSV:
#   /workspaces/stats-foundations-python/dataset/spread_summary.csv

"""
What you get (per numeric column)
    Range: max − min
    
    Variance / Std Dev: average squared/absolute deviation from the mean
    
    IQR: middle 50% spread (Q3 − Q1), robust to outliers
    
    MAD: median absolute deviation, very robust
    
    CV: unitless spread = std dev ÷ mean (handy for comparing different scales)
    
    Outlier fences: IQR rule (Q1 − 1.5×IQR, Q3 + 1.5×IQR) and # outliers detected
"""

import os
import pandas as pd
import numpy as np

IN_CSV  = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"
OUT_CSV = "/workspaces/stats-foundations-python/dataset/spread_summary.csv"

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    """Convert currency strings like '$12,345.67' to float; non-parsable -> NaN."""
    return (
        series.astype(str)
              .str.replace("$", "", regex=False)
              .str.replace(",", "", regex=False)
              .pipe(pd.to_numeric, errors="coerce")
    )

def _as_numeric(name: str, s: pd.Series) -> pd.Series:
    """Best-effort numeric conversion with special handling for currency-like columns."""
    name_l = name.lower()
    if name_l in {"income", "loan_amount"}:
        return _to_numeric_currency(s)
    # Already numeric?
    if pd.api.types.is_numeric_dtype(s):
        return pd.to_numeric(s, errors="coerce")
    # Try generic numeric parse
    return pd.to_numeric(s, errors="coerce")

def _spread_stats(s: pd.Series) -> dict:
    """Compute spread statistics from a numeric Series (NaNs allowed)."""
    s = pd.to_numeric(s, errors="coerce").dropna()
    if s.size < 2:
        return None

    n = int(s.size)
    s_min, s_max = float(s.min()), float(s.max())
    s_range = s_max - s_min
    mean = float(s.mean())
    median = float(s.median())
    var_sample = float(s.var(ddof=1))
    std_sample = float(s.std(ddof=1))

    q1 = float(s.quantile(0.25))
    q3 = float(s.quantile(0.75))
    iqr = q3 - q1
    mad = float((s - median).abs().median())  # raw MAD
    cv = float(std_sample / mean) if mean != 0 else float("nan")

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    num_outliers = int(((s < lower_fence) | (s > upper_fence)).sum())

    return {
        "count": n,
        "min": round(s_min, 4),
        "max": round(s_max, 4),
        "range": round(s_range, 4),
        "mean": round(mean, 4),
        "median": round(median, 4),
        "variance_sample": round(var_sample, 4),
        "std_dev_sample": round(std_sample, 4),
        "q1": round(q1, 4),
        "q3": round(q3, 4),
        "iqr": round(iqr, 4),
        "mad": round(mad, 4),
        "coefficient_of_variation": round(cv, 6),
        "lower_fence": round(lower_fence, 4),
        "upper_fence": round(upper_fence, 4),
        "num_outliers": num_outliers,
    }

def main():
    df = pd.read_csv(IN_CSV)
    df.columns = [c.strip() for c in df.columns]

    results = []
    for col in df.columns:
        # Try to create a numeric view for this column
        s_num = _as_numeric(col, df[col])
        # Only keep if at least 2 valid numeric values
        if s_num.dropna().size >= 2:
            stats = _spread_stats(s_num)
            if stats is not None:
                stats["column"] = col
                results.append(stats)

    if not results:
        raise ValueError("No columns with at least 2 numeric values were found.")

    summary = pd.DataFrame(results).set_index("column").sort_index()

    # Print a readable snapshot
    print("=== Spread Summary (per numeric column) ===")
    print(f"Input CSV: {IN_CSV}\n")
    print(summary.to_string())

    # Save to CSV
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    summary.to_csv(OUT_CSV)
    print(f"\nSaved spread summary to: {OUT_CSV}")

if __name__ == "__main__":
    main()
