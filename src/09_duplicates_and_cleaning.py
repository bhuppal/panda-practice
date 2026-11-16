"""
Lesson 09: Clean data, duplicates, text, and types.
Run: uv run python src/09_duplicates_and_cleaning.py
"""

import pandas as pd

raw = pd.DataFrame(
    {
        "name": [" Anna ", "Ben", "Cara", "Cara", "Dan"],
        "city": ["austin", "Denver", "Austin", "Austin", "Miami"],
        "score": ["88", "72", "95", "95", "60"],
    }
)

print("Raw, messy data:")
print(raw)
print(raw.dtypes)
print()

clean = raw.copy()
clean["name"] = clean["name"].str.strip()
clean["city"] = clean["city"].str.title()
clean["score"] = clean["score"].astype(int)

print("Clean, trimmed names, title case city, score as int:")
print(clean)
print(clean.dtypes)
print()

print("Full duplicate rows:")
print(clean.duplicated())
print()

print("After drop_duplicates:")
print(clean.drop_duplicates())
print()

print("Duplicates by city only, keeps the first row per city:")
print(clean.drop_duplicates(subset=["city"]))
print()

print("Duplicates by name and city:")
print(clean.drop_duplicates(subset=["name", "city"]))
print()

# Safe number change: bad values become missing instead of an error.
mixed = pd.DataFrame({"value": ["10", "20", "bad", "40"]})
mixed["value"] = pd.to_numeric(mixed["value"], errors="coerce")
print("to_numeric with errors coerce, bad becomes NaN:")
print(mixed)
