"""
Practice drills. Try each one yourself first, then run this file to check.

Run: uv run python exercises/drills.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from common import make_students, make_students_with_missing  # noqa: E402

df = make_students()

# Drill 1: names of students with score above 80
answer1 = list(df.loc[df["score"] > 80, "name"])
print("Drill 1, score above 80:", answer1, "| expected: ['Anna', 'Cara']")

# Drill 2: mean score for Austin only
answer2 = df.loc[df["city"] == "Austin", "score"].mean()
print("Drill 2, Austin mean:", answer2, "| expected: 91.5")

# Drill 3: count per city, sorted high to low
answer3 = df["city"].value_counts().to_dict()
print("Drill 3, count per city:", answer3)

# Drill 4: add a passed column, then count how many passed
df4 = df.copy()
df4["passed"] = df4["score"] >= 70
print("Drill 4, passed count:", int(df4["passed"].sum()), "| expected: 3")

# Drill 5: fill missing scores with the median, fill missing city with Unknown
df5 = make_students_with_missing()
df5["score"] = df5["score"].fillna(df5["score"].median())
df5["city"] = df5["city"].fillna("Unknown")
print("Drill 5, missing left after fill:", int(df5.isna().sum().sum()), "| expected: 0")
print(df5)

# Drill 6, challenge: top student in each city
top_per_city = df.sort_values("score", ascending=False).drop_duplicates("city")
print("Drill 6, top student per city:")
print(top_per_city.sort_values("city"))
