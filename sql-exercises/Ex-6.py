"""Use SQLite's .nullvalue command to change the printed representation of null to the string null and 
then re-run the previous query. When will displaying null as null be easier to understand?
When might it be misleading?"""

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

#.nullvalue null
formatted_rows = [
    [str(value) if value is not None else 'null' for value in row]
    for row in wyn
]

# Print the formatted rows
for row in formatted_rows:
    print(row)