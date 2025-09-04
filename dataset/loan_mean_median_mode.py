# loan_amount_stats_abs_path.py
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any

# Hardcoded input CSV path
IN_CSV = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"

def _to_numeric_currency(series: pd.Series) -> pd.Series:
    """Convert '$12,345.67' -> 12345.67; non-parsable -> NaN."""
    if series.dtype.kind in "biufc":
        return pd.to_numeric(series, errors="coerce")
    return (series.astype(str)
                 .str.replace("$", "", regex=False)
                 .str.replace(",", "", regex=False)
                 .pipe(pd.to_numeric, errors="coerce"))

def compute_stats(df: pd.DataFrame,
                  col_priority=("loan_amount_num", "loan_amount")) -> Dict[str, Any]:
    # Pick first available column
    col: Optional[str] = next((c for c in col_priority if c in df.columns), None)
    if not col:
        raise ValueError(f"None of the expected columns found: {col_priority}")

    s = df[col]
    if col == "loan_amount":   # parse currency if needed
        s = _to_numeric_currency(s)

    s = s.dropna()
    if s.empty:
        raise ValueError("No valid numeric values found for loan_amount.")

    mean_val = float(s.mean())
    median_val = float(s.median())
    modes = s.mode().round(2)  # can be multiple
    mode_vals = [float(x) for x in modes.tolist()] if not modes.empty else []

    return {
        "column_used": col,
        "count": int(s.size),
        "mean": round(mean_val, 2),
        "median": round(median_val, 2),
        "mode": mode_vals  # may contain multiple values
    }

def main():
    df = pd.read_csv(IN_CSV)
    stats = compute_stats(df)

    print("=== loan_amount summary ===")
    print(f"CSV Path    : {IN_CSV}")
    print(f"Column used : {stats['column_used']}")
    print(f"Count       : {stats['count']}")
    print(f"Mean        : {stats['mean']:.2f}")
    print(f"Median      : {stats['median']:.2f}")
    if stats["mode"]:
        print(f"Mode(s)     : {', '.join(f'{v:.2f}' for v in stats['mode'])}")
    else:
        print("Mode(s)     : (no repeated values)")

if __name__ == "__main__":
    main()
