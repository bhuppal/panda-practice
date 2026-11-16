"""
Lesson 02: Select columns and rows with loc and iloc.

Rule:
- iloc uses position numbers, 0, 1, 2.
- loc uses labels and column names.
Run: uv run python src/02_select_loc_iloc.py
"""

from common import make_students

df = make_students()

print("One column, a Series:")
print(df["name"])
print()

print("Two columns, a DataFrame:")
print(df[["name", "score"]])
print()

print("iloc, first row by position:")
print(df.iloc[0])
print()

print("iloc, first row, first column, a single value:", df.iloc[0, 0])
print("iloc, rows 0 to 1 and columns 0 to 1:")
print(df.iloc[0:2, 0:2])
print()

print("loc, row label 0, column name:")
print(df.loc[0, "name"])
print()

print("loc, rows 0 to 2, columns name and score:")
print(df.loc[0:2, ["name", "score"]])
print()

# A clean custom index shows the loc and iloc difference best.
df_indexed = df.set_index("name")
print("With name as index:")
print(df_indexed)
print()
print("loc by label Cara:", df_indexed.loc["Cara", "score"])
print("iloc by position 2:", df_indexed.iloc[2])
