"""Write a query to select the body masses from penguins that are less than 3000.0 grams.

Write another query to select the species and sex of penguins that weight less than 3000.0 grams. 
This shows that the columns displayed and those used in filtering are independent of each other."""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT body_mass_g
FROM penguins
WHERE body_mass_g < 3000.0;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)

SQL2 = """
SELECT species, sex
FROM penguins
WHERE body_mass_g < 3000.0;
"""
cursor = conn.execute(SQL2)
wyn = cursor.fetchall()
print(f"\n {wyn}")