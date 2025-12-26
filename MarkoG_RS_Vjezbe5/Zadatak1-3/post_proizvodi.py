from aiohttp import web
import json
proizvodi = []

async def dodaj_proizvod(request):
    data = await request.json()

    naziv = data.get("naziv")
    cijena = data.get("cijena")
    kolicina = data.get("količina")

    print(f"Primljen proizvod:{naziv}{cijena}, {kolicina}")

    proizvod = {
        "naziv": naziv,
        "cijena": cijena,
        "količina": kolicina
    }
    proizvodi.append(proizvod)
    return web.json_response(proizvodi)


app = web.Application()
app.router.add_post("/proizvodi", dodaj_proizvod)

if __name__ == "__main__":
    web.run_app(app, port=8080)
