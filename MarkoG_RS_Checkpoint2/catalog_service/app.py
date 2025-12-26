from aiohttp import web
from db import init_db
from handlers import *

def create_app():
    from cors_middleware import cors_middleware
    app = web.Application(middlewares=[cors_middleware])

    app.router.add_get("/health", health)

    # Hotels
    app.router.add_get("/hotels", list_hotels)
    app.router.add_post("/hotels", create_hotel)
    app.router.add_get("/hotels/{id}", get_hotel)
    app.router.add_put("/hotels/{id}", update_hotel)
    app.router.add_delete("/hotels/{id}", delete_hotel)

    # Rooms
    app.router.add_get("/hotels/{id}/rooms", list_rooms_for_hotel)
    app.router.add_post("/rooms", create_room)
    app.router.add_get("/rooms/{id}", get_room)
    app.router.add_put("/rooms/{id}", update_room)
    app.router.add_delete("/rooms/{id}", delete_room)

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    return app


async def on_startup(app):
    app["db"] = init_db()
    print("✅ Catalog Service started")


async def on_cleanup(app):
    app["db"].close()
    print("🛑 Catalog Service stopped")


async def health(request):
    return web.json_response({"status": "ok"})


if __name__ == "__main__":
    web.run_app(create_app(), port=8002)
