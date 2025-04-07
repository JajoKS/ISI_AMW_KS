"""Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. 
Use a query to check that the notes have been stored and that you can (for example) select by author name.

What happens if you try to insert too many or too few values into notes? What happens if you insert a number instead of a string into the note field?
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


cursor.execute("SELECT * FROM notes WHERE author = 'Duad';")
print("Duad notes:")
notes = cursor.fetchall()
for note in notes:
    print(note)

# Test cases: Inserting too many or too few values
try:
    cursor.execute("INSERT INTO notes (author, note) VALUES ('Derek');")
except sqlite3.OperationalError as e:
    print("\nError inserting too few values:", e)

try:
    cursor.execute("INSERT INTO notes (author, note) VALUES ('Eve', 'Prepare report', 'Extra Value');")
except sqlite3.OperationalError as e:
    print("\nError inserting too many values:", e)

# Inserting a number into the 'note' field
cursor.execute("INSERT INTO notes (author, note) VALUES ('Frank', 12345);")
cursor.execute("SELECT * FROM notes WHERE author = 'Frank';")
frank_notes = cursor.fetchall()
print("\nNotes by Frank (number as a note):")
for note in frank_notes:
    print(note)


conn.close()