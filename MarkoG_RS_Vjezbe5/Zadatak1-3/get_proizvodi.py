from aiohttp import web

async def dohvat_proizvoda(request):
    proizvodi = {"naziv": "kruh", "cijena": "1 euro", "kolicina": "1"}
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', dohvat_proizvoda)
web.run_app(app, host= "localhost", port=8081)
