"""Write a query that uses filter to calculate the average body masses of heavy penguins 
(those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. 
Is it possible to do this using where instead of filter?
ANS: Its impossbile to do it simultaneously by using where, because 
"""

import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create the 'notes' table
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

# Query to check all notes
cursor.execute("SELECT * FROM notes;")
rows = cursor.fetchall()
print("All notes:")
for row in rows:
    print(row)

# Query to select notes by author
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

# Clean up
conn.close()