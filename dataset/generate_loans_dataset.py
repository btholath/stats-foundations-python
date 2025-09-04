# generate_loans_dataset.py
import csv, random, math, argparse
from typing import List

def fmt_currency(x: float) -> str:
    return f"${x:,.2f}"

# --- Name pools (small, diverse, dependency-free) ---
MALE_FIRST = [
    "Liam","Noah","Oliver","Elijah","James","William","Benjamin","Lucas","Henry","Alexander",
    "Ethan","Jacob","Michael","Daniel","Logan","Jackson","Levi","Sebastian","Mateo","Jack"
]
FEMALE_FIRST = [
    "Olivia","Emma","Charlotte","Amelia","Ava","Sophia","Isabella","Mia","Evelyn","Harper",
    "Camila","Gianna","Abigail","Luna","Ella","Elizabeth","Sofia","Emily","Avery","Mila"
]
LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
    "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
    "Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson"
]

def make_full_name(gender: str) -> str:
    if gender == "male":
        first = random.choice(MALE_FIRST)
    else:
        first = random.choice(FEMALE_FIRST)
    last = random.choice(LAST_NAMES)

    # ~30% chance to add a middle initial for realism
    if random.random() < 0.30:
        middle_initial = chr(ord('A') + random.randrange(26))
        return f"{first} {middle_initial}. {last}"
    return f"{first} {last}"

def make_record(i: int) -> dict:
    loan_id = f"ID{1000 + i}"
    gender = random.choices(["male", "female"], weights=[0.52, 0.48], k=1)[0]
    applicant = make_full_name(gender)
    married = random.choices(["yes", "no"], weights=[0.62, 0.38], k=1)[0]
    dependents = random.choices([0,1,2,3,4], weights=[0.36,0.28,0.18,0.12,0.06], k=1)[0]
    self_employed = random.choices(["yes", "no"], weights=[0.15, 0.85], k=1)[0]
    property_area = random.choices(["urban", "rural"], weights=[0.7, 0.3], k=1)[0]
    credit_history = random.choices([1,0], weights=[0.75, 0.25], k=1)[0]

    # Monthly income (log-normal for skew)
    income = random.lognormvariate(math.log(5500), 0.45)
    income = max(1800.0, min(income, 25000.0))

    # Loan term (months)
    term = random.choices(
        [12,24,36,48,60,120,180,240,360],
        weights=[3,5,12,15,20,15,10,8,7],
        k=1
    )[0]

    # Loan amount tied to annual income
    annual_income = income * 12.0
    ratio = random.uniform(0.08, 0.55)
    loan_amount = max(500.0, min(ratio * annual_income, 250000.0))

    # Simple approval heuristic (for realism)
    affordability = loan_amount / (annual_income + 1.0)
    score = 0.0
    score += 1.0 if credit_history == 1 else -1.0
    score += 0.2 if married == "yes" else 0.0
    score += 0.1 if property_area == "urban" else 0.0
    score += (0.5 - affordability)
    score += random.uniform(-0.2, 0.2)
    status = "Y" if score >= 0.4 else "N"

    return {
        "loan_id": loan_id,
        "applicant": applicant,   # <-- NEW
        "gender": gender,
        "married": married,
        "dependents": dependents,
        "self_employed": self_employed,
        "income": fmt_currency(income),
        "loan_amount": fmt_currency(loan_amount),
        "term": term,
        "credit_history": credit_history,
        "property_area": property_area,
        "status": status,
    }

def generate_csv(path: str, n: int, seed: int = 42) -> None:
    random.seed(seed)
    headers = [
        "loan_id","applicant","gender","married","dependents","self_employed",
        "income","loan_amount","term","credit_history","property_area","status"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for i in range(1, n+1):
            writer.writerow(make_record(i))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate synthetic loans CSV.")
    ap.add_argument("--out", default="/workspaces/stats-foundations-python/dataset/loan_applications_2000.csv", help="output CSV path")
    ap.add_argument("--n", type=int, default=2000, help="number of rows")
    ap.add_argument("--seed", type=int, default=42, help="random seed")
    args = ap.parse_args()
    generate_csv(args.out, args.n, args.seed)
    print(f"✅ Wrote {args.n} rows to {args.out}")
