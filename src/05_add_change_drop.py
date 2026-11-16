"""
Lesson 05: Add, change, rename, and drop columns.

Important note: if you rename score to test_score, later code must use
test_score. Using the old name after a rename is a common bug.
Run: uv run python src/05_add_change_drop.py
"""

from common import make_students

df = make_students()
print("Start:")
print(df)
print()

df["passed"] = df["score"] >= 70
df["score_plus_5"] = df["score"] + 5
print("Added passed and score_plus_5:")
print(df)
print()

df = df.rename(columns={"score": "test_score"})
print("Renamed score to test_score:")
print(df)
print()

df = df.drop(columns=["score_plus_5"])
print("Dropped score_plus_5:")
print(df)
print()

# Work with the new name from here on.
print("Filter with the new name:")
print(df.loc[df["test_score"] > 80, ["name", "test_score"]])
print()

print("Top 3 with the new name:")
print(df.nlargest(3, "test_score"))
print()

# Make a new text column by joining two columns.
df["name_city"] = df["name"] + " - " + df["city"]
print("New joined column name_city:")
print(df[["name", "city", "name_city"]])
print()

# Change values with replace and with a condition.
df["city"] = df["city"].replace({"Austin": "ATX"})
print("Replaced Austin with ATX:")
print(df)
