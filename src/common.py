"""Shared data for all lessons. Import this instead of copying data."""

import numpy as np
import pandas as pd


def make_students() -> pd.DataFrame:
    data = {
        "name": ["Anna", "Ben", "Cara", "Dan", "Lynn"],
        "city": ["Austin", "Denver", "Austin", "Miami", "Baltimore"],
        "score": [88, 72, 95, 60, 34],
    }
    return pd.DataFrame(data)


def make_students_with_missing() -> pd.DataFrame:
    data = {
        "name": ["Anna", "Ben", "Cara", "Dan", "Lynn", "Mike"],
        "city": ["Austin", "Denver", None, "Miami", "Baltimore", None],
        "score": [88, np.nan, 95, 60, 34, np.nan],
    }
    return pd.DataFrame(data)
