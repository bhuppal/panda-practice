# Pandas Practice

A clear, hands-on Pandas practice repo for learning how to work with tables in Python.

Pandas is the main Python tool for data in rows and columns, like a spreadsheet you can program. This repo teaches the core ideas in small, runnable lessons, in plain simple words, with one small dataset used again and again so you can focus on the idea, not on new data each time.

All examples use a simple students table: name, city, and score.

## Who this is for

- You know basic Python and want to learn Pandas step by step.
- You learned Pandas before and want a clean practice set to refresh.
- You want short lessons you can run, change, and run again.

## What you will learn

1. Create a table and inspect it: head, tail, shape, columns, dtypes, info, describe
2. Select data with loc and iloc, and know the difference
3. Filter rows with conditions, and, or, isin, between, and query
4. Sort, rank, and quick math: sort_values, value_counts, nlargest, rank
5. Add, change, rename, and drop columns, without breaking later code
6. Group data with groupby, agg, and transform
7. Handle missing values with isna, fillna, and dropna
8. Combine tables with merge, join ideas, and concat
9. Clean data: duplicates, text cleaning, and type changes
10. Reshape data with pivot_table, melt, and crosstab
11. Work with apply, map, text columns, and date columns
12. Read and write CSV and JSON files

Plus practice drills with expected answers in `exercises/drills.py`.

## Setup

You need Python 3.12 or newer and uv.

Check you have uv:

```bash
uv --version
```

Install the project tools and libraries:

```bash
uv sync
```

That is the only setup step. This repo uses uv with `pyproject.toml`.

## How to run the lessons

Run lessons in order the first time. Each file prints its results, so you can compare the code with the output.

```bash
uv run python src/01_create_and_inspect.py
uv run python src/02_select_loc_iloc.py
uv run python src/03_filter_rows.py
uv run python src/04_sort_and_rank.py
uv run python src/05_add_change_drop.py
uv run python src/06_groupby.py
uv run python src/07_missing_values.py
uv run python src/08_merge_join_concat.py
uv run python src/09_duplicates_and_cleaning.py
uv run python src/10_pivot_and_reshape.py
uv run python src/11_apply_strings_dates.py
uv run python src/12_read_write_files.py
```

Run the drills after the lessons:

```bash
uv run python exercises/drills.py
```

Tip for lesson 12: run it from the repo root folder, as shown above. It reads `data/students.csv` and writes files into a new `out/` folder.

## Project structure

```text
pandas-practice/
  README.md
  pyproject.toml
  data/
    students.csv          Sample data as a file
  src/
    common.py             Shared sample data for all lessons
    01_create_and_inspect.py
    02_select_loc_iloc.py
    03_filter_rows.py
    04_sort_and_rank.py
    05_add_change_drop.py
    06_groupby.py
    07_missing_values.py
    08_merge_join_concat.py
    09_duplicates_and_cleaning.py
    10_pivot_and_reshape.py
    11_apply_strings_dates.py
    12_read_write_files.py
  exercises/
    drills.py             Practice drills with expected answers
```

## Key ideas to remember

- A DataFrame is a table. A Series is one column.
- `iloc` uses position numbers. `loc` uses labels and column names.
- A filter is a list of True and False values. Pandas keeps the True rows.
- For and, use `&`. For or, use `|`. Put each condition in parentheses.
- `groupby` means: split by a column, pick a column, do math.
- Missing text is often filled with a word like Unknown. Missing numbers are often filled with 0, the mean, or the median.
- `fillna` fills values in place in a column. `dropna` drops whole rows. Do not mix them in one line.
- If you rename a column, use the new name in all later code.
- `merge` combines tables by a shared column. `concat` stacks tables.
- Always check new data first: `shape`, `dtypes`, `isna().sum()`, and `head()`.

## Common mistakes this repo helps you avoid

1. Using the old column name after a rename.
2. Writing `df["score"] = df.dropna()`. That mixes a column with a whole table and will fail or give wrong data.
3. Using Python `and` and `or` for row filters. Use `&` and `|` instead.
4. Forgetting parentheses around each filter condition.
5. Filling a number column and a text column with the same value. Fill each column in a way that fits its type.
6. Sorting or grouping without checking for missing values first.

## How to practice

1. Run a lesson and read the output.
2. Change one value in the data and run it again. Guess the output before you run it.
3. Write the same result in a second way. For example, filter with brackets once, then with `query`.
4. Do the drills in `exercises/drills.py` without looking at the answers first.

## Make it your own

- Add your own small CSV file in `data/` and repeat lessons 01 to 07 on it.
- Add a new lesson file for a topic you learn next, and keep the same style: goal at the top, small data, clear prints.

## License

MIT. Use it, share it, and learn from it freely.
