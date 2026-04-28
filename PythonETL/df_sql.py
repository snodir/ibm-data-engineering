# You can run SQL queries directly on a Pandas DataFrame using libraries like pandasql, duckdb, or sqlite3.
# Here’s a complete, runnable example using the most common approaches.

# 1️⃣ Using pandasql (Lightweight, Simple)
# Python
import pandas as pd
from pandasql import sqldf

# Sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40]
})

# SQL query function
pysqldf = lambda q: sqldf(q, globals())

# Example SQL query
query = "SELECT name, age FROM df WHERE age > 30"
result = pysqldf(query)

print(result)

# ✅ Pros: Very easy to use, SQL syntax is familiar.
# ⚠ Cons: Slower for large datasets, limited SQL features.

# 2️⃣ Using duckdb (Fast, Feature-Rich)
#Python
import pandas as pd
import duckdb

# Sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40]
})

# Run SQL directly on DataFrame
result = duckdb.query("SELECT name, age FROM df WHERE age > 30").to_df()

print(result)

# ✅ Pros: Very fast, supports complex SQL, works with large datasets.
# ⚠ Cons: Requires installing duckdb.

# 3️⃣ Using sqlite3 (Persistent, Standard SQL)
# Python
import pandas as pd
import sqlite3

# Sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40]
})

# Create in-memory SQLite DB
conn = sqlite3.connect(":memory:")

# Load DataFrame into SQLite
df.to_sql("people", conn, index=False, if_exists="replace")

# Run SQL query
result = pd.read_sql_query("SELECT name, age FROM people WHERE age > 30", conn)

print(result)

conn.close()

#✅ Pros: Standard SQL, supports joins across multiple tables.
#⚠ Cons: Slightly more setup.

#💡 Recommendation:

#For quick analysis → use pandasql.
#For large datasets & performance → use duckdb.
#For persistent storage & standard SQL → use sqlite3.
