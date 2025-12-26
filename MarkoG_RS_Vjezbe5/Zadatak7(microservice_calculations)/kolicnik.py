from aiohttp import web

async def kolicnik(request):
    data = await request.json()

    zbroj = data.get("zbroj")
    umnozak = data.get("umnozak")

    if zbroj == 0:
        return web.json_response(
            {"error": "djeljenje s nulom nije dopušteno"},
            status=400
        )

    rezultat = umnozak / zbroj
    return web.json_response({"kolicnik": rezultat})

app = web.Application()
app.router.add_post("/kolicnik", kolicnik)

if __name__ == "__main__":
    web.run_app(app, port=8085)
