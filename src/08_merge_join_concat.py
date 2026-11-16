"""
Lesson 08: Combine tables with merge, join, and concat.

- merge: combine by a shared column, like id. This is like a SQL join.
- concat: stack tables on top of each other or side by side.
Run: uv run python src/08_merge_join_concat.py
"""

import pandas as pd

people = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Ana", "Ben", "Cara"],
    }
)

orders = pd.DataFrame(
    {
        "id": [1, 1, 3],
        "item": ["Book", "Pen", "Bag"],
    }
)

print("People:")
print(people)
print()
print("Orders:")
print(orders)
print()

print("Left merge, keep all people, add orders where they match:")
print(people.merge(orders, on="id", how="left"))
print()

print("Inner merge, keep only people who have an order:")
print(people.merge(orders, on="id", how="inner"))
print()

print("Outer merge, keep everything from both sides:")
print(people.merge(orders, on="id", how="outer"))
print()

# concat, stack rows.
more_people = pd.DataFrame({"id": [4], "name": ["Dan"]})
print("Concat, stack more_people under people:")
print(pd.concat([people, more_people], ignore_index=True))
print()

# Check for duplicate keys before a merge in real work.
print("Duplicate ids in orders:")
print(orders.duplicated(subset=["id"], keep=False))
