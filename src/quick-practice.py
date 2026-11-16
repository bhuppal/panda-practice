import pandas as pd
import numpy as np

data = {
    "name": ["Anna", "Ben", "Cara", "Dan", "Lynn"],
    "city": ["Austin", "Denver", "Austin", "Miami", "Baltimore"],
    "score": [88, 72, 95, 60, 34]
}

df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df.describe())

print(df["name"])

print(df[["name", "score"]])

print(df.iloc[0])

print(df.iloc[0, 0])

print(df.loc[0, "name"])
'''
iloc uses position numbers
loc uses labels and column names
'''

# Filter rows
print(df[df["score"] > 80])
print(df[(df["city"] == "Austin") & (df["score"] > 90)])

print(df[df["city"].isin(["Austin", "Miami"])])

# Sort and rank
print(df.sort_values("score"))
print(df.sort_values("score", ascending=False))

print(df.sort_values(["city", "score"]))

print(df["score"].max())
print(df["score"].min())
print(df["score"].mean())
print(df["score"].value_counts())

# Add, Change, and Drop
df["passed"] = df["score"] >= 70
df["score_plus_5"] = df["score"] + 5

df = df.rename(columns={"score": "test_score"})
df = df.drop(columns=["score_plus_5"])

# Group data
print(df)
print(df.groupby("city")["score"].mean())
print(df.groupby("city")["score"].count())
print(df.groupby("city")["score"].agg(["count", "mean", "max"]))

# Handle missing value
print(df.isna().sum())

dataNA = {
    "name": ["Anna", "Ben", "Cara", "Dan", "Lynn", "Mike"],
    "city": ["Austin", "Denver", None, "Miami", "Baltimore", None],
    "score": [88, np.nan, 95, 60, 34, np.nan]
}
dfNA = pd.DataFrame(dataNA)
print(dfNA)

print(dfNA.isna())
print(dfNA.isna().sum())
print(dfNA.isna().sum().sum())

# Fill missing values, fillna
# Filling text column with a word.
# For the column city if the value is none, replaced with "Unknown"
dfNA["city"] = dfNA["city"].fillna("Unknown")
dfNA["score"] = dfNA["score"].fillna(0)
dfNA["score"] = df.dropna()
print(dfNA)


people = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ana", "Ben", "Cara"]
})

orders = pd.DataFrame({
    "id": [1, 1, 3],
    "item": ["Book", "Pen", "Bag"]
})

result = people.merge(orders, on="id", how="left")

result = people.merge(orders, on="id", how="left")
print(result)

print(df)
# 1. Filter + pick
print(df.loc[df["score"] > 80, ["name", "score"]])

# 2. Top 3
print(df.nlargest(3, "score"))

# 3. Count per group, sorted
print(df["city"].value_counts())

# 4. New column to new column
df["namecity"] = df["name"] + ' ' + df["city"]
print(df["namecity"])

# 5. Remove duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["city"])
