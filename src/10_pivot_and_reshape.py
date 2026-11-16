"""
Lesson 10: Reshape data with pivot_table, melt, and crosstab.
Run: uv run python src/10_pivot_and_reshape.py
"""

import pandas as pd

from common import make_students

df = make_students()

print("pivot_table, mean score by city:")
print(df.pivot_table(index="city", values="score", aggfunc="mean"))
print()

sales = pd.DataFrame(
    {
        "city": ["Austin", "Austin", "Denver", "Denver"],
        "item": ["Book", "Pen", "Book", "Pen"],
        "qty": [3, 5, 2, 4],
    }
)

print("pivot_table, qty by city and item:")
print(sales.pivot_table(index="city", columns="item", values="qty", aggfunc="sum", fill_value=0))
print()

wide = pd.DataFrame(
    {
        "name": ["Anna", "Ben"],
        "math": [90, 70],
        "english": [85, 75],
    }
)

print("Wide table:")
print(wide)
print()

print("Melt, wide to long:")
print(wide.melt(id_vars="name", value_vars=["math", "english"], var_name="subject", value_name="score"))
print()

print("crosstab, count of city by passed or not:")
df2 = df.copy()
df2["passed"] = df2["score"] >= 70
print(pd.crosstab(df2["city"], df2["passed"]))
