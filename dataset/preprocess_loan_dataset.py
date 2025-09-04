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

    # --- NEW: normalize applicant full name if present ---
    if "applicant" in df.columns:
        # Trim whitespace and standardize to Title Case (e.g., "liam j. smith" -> "Liam J. Smith")
        df["applicant"] = df["applicant"].astype(str).str.strip().str.title()

    # Numeric parsing
    df["income_num"] = df["income"].apply(parse_currency)
    df["loan_amount_num"] = df["loan_amount"].apply(parse_currency)
    df["dependents"] = pd.to_numeric(df["dependents"], errors="coerce").astype("Int64")
    df["term"] = pd.to_numeric(df["term"], errors="coerce").astype("Int64")
    df["credit_history"] = pd.to_numeric(df["credit_history"], errors="coerce").astype("Int64")

    # Categorical normalization
    for cat in ["gender", "married", "self_employed", "property_area"]:
        if cat in df.columns:
            df[cat] = df[cat].astype(str).str.lower().str.strip()

    # Target normalization
    if "status" in df.columns:
        df["status"] = df["status"].astype(str).str.upper().str.strip()
        df["status_int"] = df["status"].map({"Y": 1, "N": 0}).astype("Int64")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    df.to_csv(out_csv, index=False)
    print(f"✅ Wrote cleaned CSV to {out_csv}")

if __name__ == "__main__":
    preprocess(IN_CSV, OUT_CSV)
