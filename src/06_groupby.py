"""
Lesson 06: Group data with groupby.

Read groupby in three steps: split by a column, pick a column, do math.
Example: split by city, look at score, take the mean.
Run: uv run python src/06_groupby.py
"""

from common import make_students

df = make_students()

print("Mean score per city:")
print(df.groupby("city")["score"].mean())
print()

print("Count per city:")
print(df.groupby("city")["score"].count())
print()

print("Size, rows per city:")
print(df.groupby("city").size())
print()

print("Many stats at once with agg:")
print(df.groupby("city")["score"].agg(["count", "mean", "min", "max", "sum"]))
print()

print("Group result as a table, reset_index:")
result = df.groupby("city", as_index=False)["score"].mean()
print(result)
print()

print("Sort groups by mean score, high to low:")
print(
    df.groupby("city")["score"].mean().sort_values(ascending=False)
)
print()

# transform keeps the same number of rows as the input.
# Use it to add a group mean back onto each row.
df2 = df.copy()
df2["city_mean_score"] = df2.groupby("city")["score"].transform("mean")
print("Each row with its city mean added:")
print(df2)
