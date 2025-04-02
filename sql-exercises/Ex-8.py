"""What is the average body mass of penguins that weight more than 3000.0 grams"""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT AVG(body_mass_g) AS average_body_mass_g
FROM penguins
WHERE body_mass_g > 3000.0;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)
