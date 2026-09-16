import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "employees.csv"
df = pd.read_csv(csv_path)

df['name'] = df['name'].str.title()
df['salary'] = df['salary'].clip(lower=50000, upper=200000)
df['start_date'] = pd.to_datetime(df['start_date'])

output_path = Path(__file__).parent / "employees_clean.csv"
df.to_csv(output_path, index=False)

print("\n[INFO] Transformations applied:\n"
      " - Name casing normalized\n"
      " - Salary values clipped to [50000, 200000]\n"
      " - Dates parsed to datetime format"
      )
print(f"[INFO] Cleaned data written to {output_path.name}\n")