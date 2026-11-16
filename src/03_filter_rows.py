"""
Lesson 03: Filter rows.

A filter makes a True and False list, then keeps the True rows.
Run: uv run python src/03_filter_rows.py
"""

from common import make_students

df = make_students()

print("Score above 80:")
print(df[df["score"] > 80])
print()

print("City is Austin and score above 90, use & and parentheses:")
print(df[(df["city"] == "Austin") & (df["score"] > 90)])
print()

print("City is Austin or Miami, use | :")
print(df[(df["city"] == "Austin") | (df["city"] == "Miami")])
print()

print("City in a list, isin:")
print(df[df["city"].isin(["Austin", "Miami"])])
print()

print("Score between 60 and 90:")
print(df[df["score"].between(60, 90)])
print()

print("Name starts with A, string filter:")
print(df[df["name"].str.startswith("A")])
print()

print("Filter and pick columns in one line with loc:")
print(df.loc[df["score"] > 80, ["name", "score"]])
print()

print("query, same filter in a short string form:")
print(df.query("score > 80 and city == 'Austin'"))
