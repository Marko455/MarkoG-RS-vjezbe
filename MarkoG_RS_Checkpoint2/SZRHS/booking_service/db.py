import sqlite3

DB_PATH = "bookings.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            room_id INTEGER NOT NULL,
            date_from TEXT NOT NULL,
            date_to TEXT NOT NULL,
            status TEXT NOT NULL,
            hold_id INTEGER,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn
