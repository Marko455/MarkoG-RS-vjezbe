from aiohttp import web
import asyncio

async def pozdrav(request):
    await asyncio.sleep(3)
    return web.json_response(
        {"message": "Pozdrav nakon 3 sekunde"}
    )

app = web.Application()
app.router.add_get("/pozdrav", pozdrav)

if __name__ == "__main__":
    web.run_app(app, port=8081)
