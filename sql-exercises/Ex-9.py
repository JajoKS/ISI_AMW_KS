"""How many different body masses are in the penguins dataset?"""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT COUNT(DISTINCT body_mass_g) AS distinct_body_mass_count
FROM penguins;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)
