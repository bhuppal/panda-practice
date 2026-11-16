"""
Lesson 04: Sort, rank, and quick math.
Run: uv run python src/04_sort_and_rank.py
"""

from common import make_students

df = make_students()

print("Sort by score, low to high:")
print(df.sort_values("score"))
print()

print("Sort by score, high to low:")
print(df.sort_values("score", ascending=False))
print()

print("Sort by city, then score high to low inside each city:")
print(df.sort_values(["city", "score"], ascending=[True, False]))
print()

print("Max score:", df["score"].max())
print("Min score:", df["score"].min())
print("Mean score:", df["score"].mean())
print("Median score:", df["score"].median())
print("Sum of scores:", df["score"].sum())
print()

print("Count of each city, value_counts:")
print(df["city"].value_counts())
print()

print("Count of each score:")
print(df["score"].value_counts())
print()

print("Top 3 by score, nlargest:")
print(df.nlargest(3, "score"))
print()

print("Bottom 2 by score, nsmallest:")
print(df.nsmallest(2, "score"))
print()

print("Rank, 1 is the highest score:")
df_ranked = df.copy()
df_ranked["rank"] = df_ranked["score"].rank(ascending=False).astype(int)
print(df_ranked.sort_values("rank"))
