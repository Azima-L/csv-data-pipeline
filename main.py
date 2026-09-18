import pandas as pd
import argparse
from pathlib import Path
from validate import run_validation
from transform import run_transform

parser = argparse.ArgumentParser(description="CSV Data Pipeline")
parser.add_argument("--input", default="employees.csv", help="Input CSV file")
parser.add_argument("--output", default="employees_clean.csv", help="Output CSV file")
args = parser.parse_args()

def page_divider(option):
    divider_length = 60
    if option == 1:
        print("\n" + "-" * divider_length)
    elif option == 2:
        print("-" * divider_length + "\n")

def main(df, output_path):
    print("\n>>> CSV DATA PIPELINE <<<")
    print("=" * 60)

    print("\n[1/2] Validating data...")
    page_divider(1)

    issues_count = run_validation(df)

    page_divider(2)

    if issues_count > 0:
        print(f"[WARN] {issues_count} issues found — data will be cleaned in transform step.")
    else:
        print("[INFO] No issues found — data is clean.")

    page_divider(1)
    print("\n[2/2] Transforming data...")
    page_divider(1)

    run_transform(df, output_path)

    page_divider(2)
    print("[INFO] Pipeline Complete\n")

if __name__ == "__main__":
    input_path = Path(__file__).parent / args.input
    output_path = Path(__file__).parent / args.output
    df = pd.read_csv(input_path)
    main(df, output_path)