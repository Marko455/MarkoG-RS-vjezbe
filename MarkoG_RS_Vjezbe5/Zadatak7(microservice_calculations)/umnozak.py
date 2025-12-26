from aiohttp import web
from functools import reduce
import operator

async def umnozak(request):
    data = await request.json()

    brojevi = data.get("brojevi")
    if not brojevi:
        return web.json_response(
            {"error": "Lista brojeva nije proslijeđena"},
            status=400
        )

    rezultat = reduce(operator.mul, brojevi, 1)
    return web.json_response({"umnozak": rezultat})

app = web.Application()
app.router.add_post("/umnozak", umnozak)

if __name__ == "__main__":
    web.run_app(app, port=8084)
