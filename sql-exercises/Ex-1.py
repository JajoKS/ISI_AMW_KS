"""Write a SQL query to select the sex and body mass columns from the little_penguins in that order, 
sorted such that the largest body mass appears first."""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT sex, body_mass_g
FROM penguins
ORDER BY body_mass_g DESC;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)