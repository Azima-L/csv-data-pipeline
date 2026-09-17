import pandas as pd
from pathlib import Path
import re

def name_casing(df):
    issues = 0
    all_correct = True

    for index, row in df.iterrows():
        if row['name'] != row['name'].title():
            print(f" {row['employee_id']} - {row['name']} (not Title Case)")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All names are title cased.")
    return issues

def salary_range(df):
    issues = 0
    all_correct = True

    for index, row in df.iterrows():
        if row['salary'] < 50000 or row['salary'] > 200000:
            print(f" {row['employee_id']} - {row['name']} (suspicious salary)")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All salaries within expected range.")
    return issues

def date_format(df):
    issues = 0
    all_correct = True

    for index, row in df.iterrows():
        if not re.match(r"\d{4}-\d{2}-\d{2}", row['start_date']):
            print(f" {row['employee_id']} - {row['name']} (date in wrong format)")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All dates correctly formatted.")
    return issues

def run_validation(df):
    total_issues = 0

    print("\n" + "=" * 40)
    print("VALIDATION REPORT")
    print("=" * 40)

    print("\n[CHECK 1] Name Casing")
    total_issues += name_casing(df)

    print("\n[CHECK 2] Salary Range")
    total_issues += salary_range(df)

    print("\n[CHECK 3] Date Format")
    total_issues += date_format(df)

    print(f"\nTotal issues found: {total_issues}\n")
    return total_issues

if __name__ == "__main__":
    csv_path = Path(__file__).parent / "employees.csv"
    df = pd.read_csv(csv_path)
    run_validation(df)