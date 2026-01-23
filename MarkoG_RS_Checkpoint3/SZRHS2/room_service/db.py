import aiosqlite

DB = "rooms.db"

async def get_db():
    return await aiosqlite.connect(DB)
