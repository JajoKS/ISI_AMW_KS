"""Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table.
Your result should have 11 rows. Modify your query to select distinct combinations of island and species 
from the same rows and compare the result to what you got in part 1."""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT island,species FROM penguins
LIMIT 11 OFFSET 49;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)

SQL2 = """
SELECT DISTINCT island,species FROM penguins;
"""
cursor = conn.execute(SQL2)
wyn = cursor.fetchall()
print(wyn)