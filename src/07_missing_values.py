"""
Lesson 07: Missing values, isna, fillna, and dropna.

Use None for missing text and numpy nan for missing numbers.
A number column with a missing value becomes float, for example 88.0.

Common bug to avoid: do not write df["score"] = df.dropna().
dropna returns a whole table, not a column. Keep fillna and dropna apart,
as shown below.
Run: uv run python src/07_missing_values.py
"""

import pandas as pd

from common import make_students_with_missing

df = make_students_with_missing()
print("Table with missing values:")
print(df)
print()

print("isna, True where a value is missing:")
print(df.isna())
print()

print("Missing count per column:")
print(df.isna().sum())
print()

print("Total missing in the whole table:", df.isna().sum().sum())
print()

# Fill, work on a copy so the original stays for the next example.
filled = df.copy()
filled["city"] = filled["city"].fillna("Unknown")
filled["score"] = filled["score"].fillna(0)
print("Filled city with Unknown and score with 0:")
print(filled)
print()

filled_mean = df.copy()
filled_mean["city"] = filled_mean["city"].fillna("Unknown")
filled_mean["score"] = filled_mean["score"].fillna(filled_mean["score"].mean())
print("Filled score with the mean, 69.25:")
print(filled_mean)
print()

filled_median = df.copy()
filled_median["score"] = filled_median["score"].fillna(
    filled_median["score"].median()
)
print("Filled score with the median:")
print(filled_median)
print()

print("dropna, drop any row with a missing value:")
print(df.dropna())
print()

print("dropna on score only:")
print(df.dropna(subset=["score"]))
print()

print("Forward fill and backward fill:")
print(df.ffill())
print(df.bfill())
