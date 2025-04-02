"""Explain why the output of the previous query has a blank line before the rows for female and male penguins.
ANS: Because the first value is NULL NULL
Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much."""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT 
    body_mass_g, 
    COUNT(*) AS penguin_count
FROM penguins
GROUP BY body_mass_g;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)