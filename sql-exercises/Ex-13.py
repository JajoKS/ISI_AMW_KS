"""What happens if you try to delete rows that don't exist (e.g., all entries in work that refer to juna)?
Nothing will happen, the database will just give a result that 0 rows were deleted.
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE notes (
    author TEXT,
    note TEXT
);
""")

cursor.executemany("""
INSERT INTO notes (author, note) VALUES (?, ?);
""", [
    ("Duad", "Commit suicide."),
    ("Hadan", "Deez nuts."),
    ("Candice", "Who's candice."),
    ("Andy", "Everything is dandy.")
])


cursor.execute("SELECT * FROM notes;")
rows = cursor.fetchall()
print("All notes:")
for row in rows:
    print(row)


cursor.execute("DELETE FROM notes WHERE author = 'Joe';")
notes = cursor.fetchall()
for note in notes:
    print(note)

conn.close()