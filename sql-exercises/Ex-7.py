"""Write a query to find penguins whose body mass is known but whose sex is not.

Write another query to find penguins whose sex is known but whose body mass is not."""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT *
FROM penguins
WHERE body_mass_g IS NOT NULL
AND sex IS NULL;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)

SQL2 = """
SELECT *
FROM penguins
WHERE sex IS NOT NULL
AND body_mass_g IS NULL;
"""
cursor = conn.execute(SQL2)
wyn = cursor.fetchall()
print(f"\n {wyn}")