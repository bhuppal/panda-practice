"""
Lesson 12: Read and write files, CSV and JSON.

This lesson reads data/students.csv from the repo root.
Run it from the repo root folder:
uv run python src/12_read_write_files.py
Run: uv run python src/12_read_write_files.py
"""

from pathlib import Path

import pandas as pd

root = Path(__file__).parent.parent
csv_path = root / "data" / "students.csv"
out_dir = root / "out"
out_dir.mkdir(exist_ok=True)

df = pd.read_csv(csv_path)
print("Read from CSV:")
print(df)
print()

passed = df[df["score"] >= 70]
print("Only passed, score 70 or more:")
print(passed)
print()

passed.to_csv(out_dir / "passed.csv", index=False)
passed.to_json(out_dir / "passed.json", orient="records", indent=2)

print("Wrote out/passed.csv and out/passed.json")
print("Tip: index=False stops an extra row number column in the CSV.")
print()

back = pd.read_json(out_dir / "passed.json")
print("Read the JSON back:")
print(back)
