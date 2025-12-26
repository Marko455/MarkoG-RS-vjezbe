from aiohttp import web
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

def create_app():
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_static("/static", BASE_DIR / "static")
    return app

async def index(request):
    return web.FileResponse(BASE_DIR / "templates" / "index.html")

if __name__ == "__main__":
    web.run_app(create_app(), port=8000)
