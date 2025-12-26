from aiohttp import web
from db import init_db
from handlers import *

def create_app():
    from cors_middleware import cors_middleware

    app = web.Application(middlewares=[cors_middleware])


    app.router.add_get("/health", health)
    app.router.add_get("/availability", check_availability)

    app.router.add_post("/availability/hold", hold_room)
    app.router.add_post("/availability/confirm", confirm_room)
    app.router.add_post("/availability/release", release_room)

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    return app


async def on_startup(app):
    app["db"] = init_db()
    print("✅ Availability Service started")


async def on_cleanup(app):
    app["db"].close()
    print("🛑 Availability Service stopped")


async def health(request):
    return web.json_response({"status": "ok"})


if __name__ == "__main__":
    web.run_app(create_app(), port=8003)
