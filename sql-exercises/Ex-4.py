"""Use the not operator to select penguins that are not Gentoos.

SQL's or is an inclusive or: it succeeds if either or both conditions are true. 
SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, 
but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on 
Torgersen Island but not both.
"""

import sqlite3

db_path = "db/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
SQL = """
SELECT *
FROM penguins
WHERE NOT species = 'Gentoo';
"""
cursor = conn.execute(SQL)
wyn = cursor.fetchall()
print(wyn)

SQL2 = """
SELECT *
FROM penguins
WHERE (sex = 'female' OR island = 'Torgersen')
AND NOT (sex = 'female' AND island = 'Torgersen');
"""
cursor = conn.execute(SQL2)
wyn = cursor.fetchall()
print(f"\n {wyn}")