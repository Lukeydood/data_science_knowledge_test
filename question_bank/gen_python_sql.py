"""General data science revision: Python, pandas, SQL and tooling (not assessed KSBs)."""
from ._helpers import make_builder

q, QUESTIONS = make_builder("GEN", "General data science (optional revision beyond the assessed KSBs)", start=1)

# --- Python -------------------------------------------------------------------------
q("py-mutable", "Which Python type is immutable?",
  ["tuple", "list", "dict", "set"],
  "A", "Tuples cannot be changed after creation; lists, dicts and sets can.")
q("py-default-arg", "Why is `def add(item, items=[]):` a common Python bug?",
  ["The default list is shared between calls", "Lists are not allowed as default arguments", "The function returns None by default", "Default arguments must be integers"],
  "A", "Defaults are evaluated once; use `items=None` and create a new list inside.")
q("py-comprehension", "What does `[x**2 for x in range(4)]` produce?",
  ["[0, 1, 4, 9]", "[1, 4, 9, 16]", "[0, 2, 4, 6]", "[0, 1, 2, 3]"],
  "A", "range(4) gives 0–3; each is squared.")
q("py-dict-get", "What does `d.get('k', 0)` return if 'k' is not a key in dictionary d?",
  ["0", "None", "KeyError", "'k'"],
  "A", "`get` returns the default instead of raising KeyError.")
q("py-generator", "What is the main advantage of a generator expression over a list comprehension for large data?",
  ["Values are produced lazily, using little memory", "Results are cached so a second pass costs nothing", "It runs in parallel across all CPU cores", "It automatically sorts the produced values"],
  "A", "Generators yield items one at a time and can only be iterated once.")
q("py-is-eq", "What is the difference between `is` and `==` in Python?",
  ["`is` checks identity; `==` checks equality of value", "`is` checks equality of value; `==` checks identity", "`is` works only for numbers; `==` works for any type", "They are interchangeable in all situations"],
  "A", "Use `is` for None checks (`x is None`), `==` for values.")
q("py-float", "Why does `0.1 + 0.2 == 0.3` evaluate to False in Python?",
  ["These decimals have no exact binary form", "Python rounds every float to one decimal place", "The + operator concatenates the two numbers", "Python treats 0.3 as an integer in comparisons"],
  "A", "Use `math.isclose` or `decimal.Decimal` when exactness matters.")
q("py-venv", "What does a Python virtual environment provide?",
  ["An isolated set of packages for one project", "A faster Python interpreter for the project", "A sandbox that blocks all network access", "A copy of the operating system for testing"],
  "A", "venv/conda environments prevent conflicts between projects' dependencies.")
q("py-with", "What does a `with open('f.csv') as fh:` block guarantee?",
  ["The file is closed when the block exits", "The whole file is read into memory at once", "The file is locked against other readers", "The file is converted to UTF-8 on read"],
  "A", "Context managers handle clean-up even if an exception occurs.")
q("py-fstring", "What does `f\"{3.14159:.2f}\"` produce?",
  ["'3.14'", "'3.1'", "'3.14159'", "'03.14'"],
  "A", "`.2f` formats with two decimal places.")
q("py-zero-index", "Given `x = [10, 20, 30, 40]`, what is `x[1:3]`?",
  ["[20, 30]", "[10, 20, 30]", "[20, 30, 40]", "[10, 20]"],
  "A", "Slices include the start index and exclude the end index; indexing starts at 0.")
q("py-negative-index", "Given `x = [10, 20, 30, 40]`, what is `x[-1]`?",
  ["40", "10", "30", "An IndexError"],
  "A", "Negative indices count from the end.")

# --- pandas / NumPy -----------------------------------------------------------------
q("pd-loc-iloc", "In pandas, what is the difference between `.loc` and `.iloc`?",
  ["`.loc` selects by label; `.iloc` by integer position", "`.loc` selects by integer position; `.iloc` by label", "`.loc` selects rows only; `.iloc` selects columns only", "`.loc` returns copies; `.iloc` returns views"],
  "A", "Mixing them up is a common source of off-by-one and label errors.")
q("pd-groupby", "What does `df.groupby('region')['incidents'].sum()` return?",
  ["Total incidents for each region", "The number of rows in each region", "The region with the most incidents", "Incidents sorted by region name"],
  "A", "groupby splits, applies an aggregation, and combines the results.")
q("pd-merge", "`pd.merge(a, b, on='site_id', how='left')` is equivalent to which SQL operation?",
  ["LEFT JOIN on site_id", "INNER JOIN on site_id", "UNION ALL of a and b", "CROSS JOIN of a and b"],
  "A", "how='left' keeps all rows of a; check for unexpected duplicates after merging.")
q("pd-merge-dupes", "After a left merge, the result has more rows than the left table. Why?",
  ["The key is duplicated in the right table", "The left table contained missing key values", "The merge dropped unmatched right rows", "pandas adds a header row to the output"],
  "A", "One-to-many matches multiply rows; use `validate='m:1'` to catch this.")
q("pd-settingwithcopy", "pandas raises a SettingWithCopyWarning. What does it usually indicate?",
  ["You may be modifying a copy, not the original DataFrame", "The DataFrame has too many columns to display in full", "A column contains a mixture of data types", "The index is not sorted in ascending order"],
  "A", "Use `.loc` on the original or an explicit `.copy()` to make intent clear.")
q("pd-isna", "Which method counts missing values in each column of a DataFrame?",
  ["df.isna().sum()", "df.count().sum()", "df.nunique()", "df.describe()"],
  "A", "`isna()` gives a boolean frame; summing counts True values. `count()` counts non-missing.")
q("pd-apply", "Why is `df['x'] * 2` usually preferred to `df['x'].apply(lambda v: v * 2)`?",
  ["The vectorised version is much faster", "apply is not designed for numeric columns", "apply changes the column's data type", "The vectorised version also handles text"],
  "A", "apply calls Python once per element; vectorised operations run in compiled code.")
q("pd-pivot", "Which pandas function reshapes long data into a wide summary table with aggregation?",
  ["pivot_table", "melt (unpivot)", "explode", "stack"],
  "A", "`melt` goes wide → long; `explode` expands list cells; `stack` moves columns into the index.")
q("pd-datetime", "Which call converts a text column of dates to pandas datetime values?",
  ["pd.to_datetime(df['date'])", "df['date'].astype(int)", "pd.Timestamp.now(df['date'])", "df['date'].str.split('-')"],
  "A", "Pass `format=` for speed and to avoid ambiguous day/month parsing.")
q("pd-resample", "Which pandas method aggregates a time-indexed series from hourly to daily values?",
  ["resample('D')", "rolling('D')", "shift(24)", "diff(24)"],
  "A", "`resample` changes frequency; `rolling` computes moving windows.")
q("np-broadcast", "In NumPy, adding an array of shape (3, 1) to one of shape (1, 4) gives an array of shape:",
  ["(3, 4)", "(1, 1)", "(4, 3)", "An error"],
  "A", "Broadcasting stretches size-1 dimensions to match.")
q("np-axis", "For a 2-D NumPy array `a`, what does `a.mean(axis=0)` compute?",
  ["The mean of each column", "The mean of each row", "The overall mean", "The mean of the diagonal"],
  "A", "axis=0 collapses rows, giving one value per column.")

# --- SQL ------------------------------------------------------------------------------
q("sql-distinct", "Which query returns the number of different stations in a readings table?",
  ["SELECT COUNT(DISTINCT station) FROM readings", "SELECT DISTINCT COUNT(station) FROM readings", "SELECT COUNT(*) FROM readings GROUP BY station", "SELECT station FROM readings LIMIT 1"],
  "A", "COUNT(DISTINCT col) counts unique non-NULL values; the GROUP BY version returns one row per station.")
q("sql-like", "Which WHERE clause finds names starting with 'North'?",
  ["WHERE name LIKE 'North%'", "WHERE name = 'North*'", "WHERE name LIKE '%North'", "WHERE name IN ('North')"],
  "A", "`%` matches any characters; '%North' would match names ending in North.")
q("sql-case", "Which SQL construct creates a new column with 'High' or 'Low' depending on a value?",
  ["CASE WHEN … END", "GROUP BY … HAVING …", "UNION ALL …", "WITH … AS …"],
  "A", "CASE expressions implement conditional logic in SQL.")
q("sql-coalesce", "What does `COALESCE(phone, mobile, 'unknown')` return?",
  ["The first non-NULL value of the three", "All three values joined into one string", "The number of non-NULL values", "NULL if any of the values is NULL"],
  "A", "COALESCE is commonly used to supply defaults for missing values.")
q("sql-row-number", "Which window function helps keep only the latest reading per station?",
  ["ROW_NUMBER() OVER (PARTITION BY station ORDER BY ts DESC)", "COUNT(*) OVER () with no partition or ordering at all", "SUM(value) OVER (PARTITION BY station ORDER BY value)", "AVG(value) OVER (PARTITION BY ts) as a running mean"],
  "A", "Number rows within each station by descending time, then filter to row 1.")
q("sql-explain", "What does running `EXPLAIN` before a SQL query show?",
  ["The plan the database will use to execute it", "The rows that the query will return, in order", "The users who have permission to run it", "The history of edits to the query text"],
  "A", "Execution plans reveal full scans, join strategies and missing indexes.")
q("sql-self-join", "Joining a table to itself, e.g. to pair each employee with their manager in the same table, is a:",
  ["Self join", "Cross join", "Natural join", "Semi join"],
  "A", "Use table aliases to distinguish the two copies.")

# --- Tooling ---------------------------------------------------------------------------
q("jupyter-restart", "Before sharing a notebook, why should you restart the kernel and run all cells?",
  ["To check results don't rely on hidden state", "To reduce the file size of the notebook on disk", "To convert the notebook into a Python package", "To clear the version history of the notebook file"],
  "A", "Restart-and-run-all is a basic reproducibility check.")
q("cli-basics", "In a Unix-like shell, what does `head -n 5 data.csv` do?",
  ["Shows the first five lines of the file", "Deletes the first five lines of the file", "Counts the lines in the file", "Shows the last five lines of the file"],
  "A", "`tail` shows the end; `wc -l` counts lines.")
q("regex-basics", "Which regular expression matches one or more digits?",
  ["\\d+", "\\w*", "[a-z]+", "\\s?"],
  "A", "`\\d` is a digit and `+` means one or more.")
q("r-vs-python", "Which TWO statements about R and Python for data science are accurate?",
  ["Both have mature ecosystems for statistics and ML", "R's tidyverse and Python's pandas cover similar ground", "Only Python can produce publication-quality charts", "Only R can be used for machine learning"],
  "AB", "Both are capable; team skills and platform support usually decide.")
q("bi-tools", "Power BI and Tableau are primarily:",
  ["Business intelligence and dashboarding tools", "Programming languages for statistical modelling", "Distributed storage systems for data lakes", "Version control systems for analytical code"],
  "A", "They connect to data sources and build interactive reports and dashboards.")
