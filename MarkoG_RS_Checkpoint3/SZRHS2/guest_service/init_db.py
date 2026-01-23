import sqlite3

conn = sqlite3.connect("guests.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS guests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()
