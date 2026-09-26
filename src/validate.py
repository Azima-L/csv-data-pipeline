import pandas as pd
from pathlib import Path
import re

def name_casing(df):
    issues = 0
    details = []
    all_correct = True

    for index, row in df.iterrows():
        if row['name'] != row['name'].title():
            print(f" {row['employee_id']} - {row['name']} (not Title Case)")
            details.append(f" {row['employee_id']} | {row['name']} | not Title Case")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All names are title cased.")
    return issues, details

def salary_range(df, config):
    issues = 0
    details = []
    all_correct = True

    salary_min = config["salary_min"]
    salary_max = config["salary_max"]

    for index, row in df.iterrows():
        if row['salary'] < salary_min or row['salary'] > salary_max:
            print(f" {row['employee_id']} - {row['name']} (suspicious salary)")
            details.append(f" {row['employee_id']} | {row['name']} | suspicious salary")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All salaries within expected range.")
    return issues, details

def date_format(df):
    issues = 0
    details = []
    all_correct = True

    for index, row in df.iterrows():
        if not re.match(r"\d{4}-\d{2}-\d{2}", row['start_date']):
            print(f" {row['employee_id']} - {row['name']} (date in wrong format)")
            details.append(f" {row['employee_id']} | {row['name']} | date in wrong format")
            issues += 1
            all_correct = False
    if all_correct:
        print(" All dates correctly formatted.")
    return issues, details

def run_validation(df, config):
    total_issues = 0
    all_details = []

    print("\n" + "=" * 40)
    print("VALIDATION REPORT")
    print("=" * 40)

    print("\n[CHECK 1] Name Casing")
    count, details = name_casing(df)
    total_issues += count
    all_details.extend(details)

    print("\n[CHECK 2] Salary Range")
    count, details = salary_range(df, config)
    total_issues += count
    all_details.extend(details)

    print("\n[CHECK 3] Date Format")
    count, details = date_format(df)
    total_issues += count
    all_details.extend(details)

    print(f"\nTotal issues found: {total_issues}\n")
    return total_issues, all_details

if __name__ == "__main__":
    import json
    
    csv_path = Path(__file__).parent.parent / "data" / "employees.csv"
    config_path = Path(__file__).parent.parent / "config" / "rules.json"
    with open(config_path) as f:
        config = json.load(f)

    df = pd.read_csv(csv_path)
    run_validation(df, config)