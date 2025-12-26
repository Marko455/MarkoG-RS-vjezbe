import aiosqlite

DB_PATH = "users.db"

async def init_db():
    db = await aiosqlite.connect(DB_PATH)
    await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT,
            role TEXT,
            created_at TEXT
        )
    """)
    await db.commit()
    return db
