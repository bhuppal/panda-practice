"""
Lesson 11: Work row by row, text columns, and date columns.

- map works on one column, value by value.
- apply can work on a column or on a whole row.
- str works on text columns. dt works on date columns.
Run: uv run python src/11_apply_strings_dates.py
"""

import pandas as pd

from common import make_students

df = make_students()

print("map, add a grade letter from score:")


def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 70:
        return "B"
    if score >= 50:
        return "C"
    return "F"


df2 = df.copy()
df2["grade"] = df2["score"].map(grade)
print(df2)
print()

print("apply on a row, make a label that uses two columns:")
df2["label"] = df2.apply(lambda row: f"{row['name']} ({row['city']})", axis=1)
print(df2[["name", "city", "label"]])
print()

print("String tools:")
print("Upper:", list(df["name"].str.upper()))
print("Contains Aus in city:", list(df["city"].str.contains("Aus")))
print("Length of name:", list(df["name"].str.len()))
print()

events = pd.DataFrame(
    {
        "event": ["Start", "Mid", "End"],
        "day": ["2026-01-05", "2026-01-20", "2026-02-02"],
    }
)
events["day"] = pd.to_datetime(events["day"])
events["year"] = events["day"].dt.year
events["month"] = events["day"].dt.month
events["weekday"] = events["day"].dt.day_name()
print("Date tools:")
print(events)
