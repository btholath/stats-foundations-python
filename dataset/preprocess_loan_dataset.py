
# preprocess_loan_dataset_abs_paths.py
# ------------------------------------
# Version with ABSOLUTE file paths (no CLI args).
# Input:
#   /workspaces/stats-foundations-python/dataset/loan_applications_2000.csv
# Output:
#   /workspaces/stats-foundations-python/dataset/loan_applications_2000_clean.csv

import os
import pandas as pd
import numpy as np

# --- Absolute paths (edit here if your workspace path differs) ---
IN_CSV  = "/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv"
OUT_CSV = "/workspaces/stats-foundations-python/dataset/loan_applications_2000_clean.csv"

def parse_currency(s):
    if pd.isna(s): 
        return np.nan
    return float(str(s).replace("$", "").replace(",", ""))

def preprocess(in_csv: str, out_csv: str) -> None:
    df = pd.read_csv(in_csv)
    df.columns = [c.strip().lower() for c in df.columns]

    # Numeric parsing
    df["income_num"] = df["income"].apply(parse_currency)
    df["loan_amount_num"] = df["loan_amount"].apply(parse_currency)
    df["dependents"] = pd.to_numeric(df["dependents"], errors="coerce").astype("Int64")
    df["term"] = pd.to_numeric(df["term"], errors="coerce").astype("Int64")
    df["credit_history"] = pd.to_numeric(df["credit_history"], errors="coerce").astype("Int64")

    # Categorical normalization
    for cat in ["gender","married","self_employed","property_area"]:
        df[cat] = df[cat].astype(str).str.lower().str.strip()
    df["status"] = df["status"].astype(str).str.upper().str.strip()

    # Target as int
    df["status_int"] = df["status"].map({"Y":1, "N":0}).astype("Int64")

    # Make sure the output directory exists
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    df.to_csv(out_csv, index=False)
    print(f"✅ Wrote cleaned CSV to {out_csv}")

if __name__ == "__main__":
    preprocess(IN_CSV, OUT_CSV)
