import sqlite3

conn = sqlite3.connect("rooms.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    type TEXT,
    price REAL,
    available INTEGER
)
""")

conn.commit()
conn.close()
