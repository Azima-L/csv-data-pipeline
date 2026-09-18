import pandas as pd
from pathlib import Path

def run_transform(df, output_path):
    df['name'] = df['name'].str.title()
    df['salary'] = df['salary'].clip(lower=50000, upper=200000)
    df['start_date'] = pd.to_datetime(df['start_date'])

    df.to_csv(output_path, index=False)

    print("\n[INFO] Transformations applied:\n"
        " - Name casing normalized\n"
        " - Salary values clipped to [50000, 200000]\n"
        " - Dates parsed to datetime format\n"
        )
    print(f"[INFO] Cleaned data written to {output_path.name}\n")
    return df

if __name__ == "__main__":
    csv_path = Path(__file__).parent / "employees.csv"
    df = pd.read_csv(csv_path)
    output_path = Path(__file__).parent / "employees_clean.csv"
    run_transform(df, output_path)