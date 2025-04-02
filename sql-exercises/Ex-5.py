"""Write a single query that calculates and returns:

A column called what_where that has the species and island of each penguin separated by a single space.
A column called bill_ratio that has the ratio of bill length to bill depth.
You can use the || operator to concatenate text to solve part 1, or look at the documentation for SQLite's format() function.
"""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT 
    species || ' ' || island AS what_where,
    bill_length_mm / bill_depth_mm AS bill_ratio
FROM penguins;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)