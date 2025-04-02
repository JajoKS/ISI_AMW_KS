"""Write a query that uses filter to calculate the average body masses of heavy penguins 
(those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. 
Is it possible to do this using where instead of filter?
ANS: Its impossbile to do it simultaneously by using where, because 
"""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT 
    AVG(body_mass_g) FILTER (WHERE body_mass_g > 4500) AS avg_heavy_penguins,
    AVG(body_mass_g) FILTER (WHERE body_mass_g < 3500) AS avg_light_penguins
FROM penguins;
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)

