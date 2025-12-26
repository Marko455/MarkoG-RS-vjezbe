from aiohttp import web
from db import init_db
from handlers import *

def create_app():
    from cors_middleware import cors_middleware
    app = web.Application(middlewares=[cors_middleware])


    app.router.add_get("/health", health)

    app.router.add_post("/bookings", create_booking)
    app.router.add_get("/bookings/{id}", get_booking)
    app.router.add_delete("/bookings/{id}", cancel_booking)

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    return app


async def on_startup(app):
    app["db"] = init_db()
    print("✅ Booking Service started")


async def on_cleanup(app):
    app["db"].close()
    print("🛑 Booking Service stopped")


async def health(request):
    return web.json_response({"status": "ok"})


if __name__ == "__main__":
    web.run_app(create_app(), port=8004)
