from aiohttp import web

async def zbroj(request):
    data = await request.json()

    brojevi = data.get("brojevi")
    if not brojevi:
        return web.json_response(
            {"error": "Lista brojeva nije proslijeđena"},
            status=400
        )

    rezultat = sum(brojevi)
    return web.json_response({"zbroj": rezultat})

app = web.Application()
app.router.add_post("/zbroj", zbroj)

if __name__ == "__main__":
    web.run_app(app, port=8083)
