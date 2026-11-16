"""
Lesson 01: Create a table and inspect it.

Goal: make a DataFrame, then learn the first checks you run on any new data.
Run: uv run python src/01_create_and_inspect.py
"""

import pandas as pd

from common import make_students

df = make_students()
print("Full table:")
print(df)
print()

print("First 2 rows, head:")
print(df.head(2))
print()

print("Last 2 rows, tail:")
print(df.tail(2))
print()

print("Shape, (rows, columns):", df.shape)
print("Columns:", list(df.columns))
print("Index:", list(df.index))
print()

print("Data types:")
print(df.dtypes)
print()

print("Info:")
print(df.info())
print()

print("Describe, summary math for number columns:")
print(df.describe())
print()

# Change a type on purpose. Score as float, name as string type.
df2 = df.copy()
df2["score"] = df2["score"].astype(float)
print("Score changed to float:")
print(df2.dtypes)
