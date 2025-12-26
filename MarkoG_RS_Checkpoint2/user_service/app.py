from aiohttp import web
import sqlite3

from auth_middleware import auth_middleware
from handlers import get_me

DB_PATH = "users.db"

def create_app():
    from cors_middleware import cors_middleware
    app = web.Application(middlewares=[cors_middleware])

    app.router.add_get("/health", health)
    app.router.add_get("/me", get_me)

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    return app


async def on_startup(app):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT,
            role TEXT,
            created_at TEXT
        )
    """)
    conn.commit()

    app["db"] = conn
    print("✅ User Service started")


async def on_cleanup(app):
    app["db"].close()
    print("🛑 User Service stopped")


async def health(request):
    return web.json_response({"status": "ok"})


if __name__ == "__main__":
    web.run_app(create_app(), port=8001)
