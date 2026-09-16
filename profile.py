import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "employees.csv"
df = pd.read_csv(csv_path)

print("\n" + "=" * 40)
print("EMPLOYEE DATA PROFILE")
print("=" * 40)

print(f"\nShapes: {df.shape[0]} rows, {df.shape[1]} columns")

print("\n--- Data Sample (first 5 rows) ---")
print(df.head())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Salary Statistics ---")
print(f"Min: {df['salary'].min():,}")
print(f"Max: {df['salary'].max():,}")
print(f"Average: {df['salary'].mean():,.0f}")

print("\n--- Headcount by Department ---")
print(df['department'].value_counts(), "\n")