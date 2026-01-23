import sqlite3

conn = sqlite3.connect("reservations.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER,
    room_id INTEGER,
    check_in TEXT,
    check_out TEXT,
    active INTEGER
)
""")

conn.commit()
conn.close()
